"""Contrat additionnel local. Ne certifie pas les traces déclarées ni les sources."""
from collections import Counter
from datetime import datetime
import hashlib
import json
import re
from personna_evaluate import grade as grade_personna
from urllib.parse import urlsplit

HASH = re.compile(r'^[0-9a-f]{64}$')
STEPS = ['F0_CADRAGE', 'F1_RECHERCHE', 'F2_OPTIONS', 'F3_DECISION']
TOPICS = ['idees', 'architecture', 'production_pilote', 'roadmap']


def workflow_digest(workflow, evidence):
    """Entrées stables ; les retours de cycles ne créent pas de dépendance circulaire."""
    keys = ['schema_version', 'run_id', 'niche', 'brief_version', 'research', 'competencies', 'profiles']
    payload = {key: workflow[key] for key in keys}
    payload['delegation_context'] = [
        {key: agent[key] for key in ['id', 'role_id', 'profile_sha256', 'brief_version',
                                    'mandate_path', 'mandate_sha256', 'spawn_evidence_id', 'started_sequence',
                                    'persona_load_evidence_id', 'loaded_sequence']}
        for agent in workflow['delegates']]
    ids = set()
    for platform in workflow['research']['platforms']:
        ids.update(platform['evidence_ids'])
    for profile in workflow['profiles']:
        ids.update(profile['training_evidence_ids'])
        ids.update(profile['calibration_evidence_ids'])
        if profile.get('evaluation'):
            ids.add(profile['evaluation']['evidence_id'])
    for agent in workflow['delegates']:
        ids.update([agent['spawn_evidence_id'], agent['persona_load_evidence_id']])
    payload['evidence_context'] = sorted([e for e in evidence if e['id'] in ids], key=lambda e: e['id'])
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':')).encode('utf-8')).hexdigest()


def validate_workflow(project, state, strict, *, load, shape, safe_path, digest, root):
    errors, warnings = [], []
    path = safe_path(project, 'workflow.json')
    if not path.is_file():
        message = 'workflow.json absent : compléter le parcours réflexion/recherche/personas/agents sans inventer l’historique'
        (errors if strict else warnings).append(message)
        return errors, warnings
    workflow = load(path)
    errors = shape(workflow, load(root / 'schemas/workflow.schema.json'), '$workflow')
    if errors:
        return errors, warnings
    ev = {e['id']: e for e in state['evidence']}
    roles = {r['id']: r for r in state['roles']}
    sources = {s['id']: s for s in state['sources']}
    artifacts = {a['path']: a for a in state['artifacts']}

    def refs(ids, label, kinds=None, needed=False):
        if needed and not ids:
            errors.append(label + ': preuve absente')
        for eid in ids:
            evidence = ev.get(eid)
            if not evidence or (kinds and evidence['kind'] not in kinds):
                errors.append(label + ': preuve inconnue ou de mauvais type ' + eid)

    def snapshot(record, label, current=True):
        if not HASH.fullmatch(record['sha256']):
            errors.append(label + ': empreinte invalide')
        try:
            p = safe_path(project, record['path'], current)
            if current and digest(p) != record['sha256']:
                errors.append(label + ': version modifiée ou absente')
        except (ValueError, OSError) as exc:
            errors.append(label + ': ' + str(exc))

    def platform_of(url):
        try:
            parsed = urlsplit(url or '')
            host = (parsed.hostname or '').lower()
            if parsed.scheme not in {'http', 'https'} or parsed.username or parsed.password:
                return None
            for platform, domain in [('LINKEDIN', 'linkedin.com'), ('REDDIT', 'reddit.com')]:
                if host == domain or host.endswith('.' + domain):
                    return platform
        except ValueError:
            pass
        return None

    for field, key in [('steps', 'id'), ('competencies', 'id'), ('profiles', 'role_id'), ('delegates', 'id'), ('iterations', 'id')]:
        if len(workflow[field]) != len({row[key] for row in workflow[field]}):
            errors.append('workflow ' + field + ': identifiant dupliqué')
    for key in ['run_id', 'niche', 'brief_version']:
        if workflow[key] != state[key]:
            errors.append('workflow contexte différent : ' + key)

    steps = {step['id']: step for step in workflow['steps']}
    if set(steps) != set(STEPS):
        errors.append('Réflexion : F0–F3 doivent être représentés')
    completed = [steps[s]['sequence'] for s in STEPS if s in steps and steps[s]['status'] == 'DONE']
    if any(x is None for x in completed) or (all(x is not None for x in completed) and completed != sorted(set(completed))):
        errors.append('Réflexion : ordre F0–F3 incohérent')
    done_seen_gap = False
    for sid in STEPS:
        step = steps.get(sid)
        if not step:
            continue
        refs(step['evidence_ids'], sid, {'artifact', 'review'}, needed=strict or step['status'] == 'DONE')
        if step['status'] != 'DONE':
            done_seen_gap = True
            if strict:
                errors.append('Réflexion incomplète : ' + sid)
        elif done_seen_gap:
            errors.append('Réflexion : étape terminée avant son préalable : ' + sid)
    start = workflow['preproduction_started_sequence']
    if start is not None:
        if len(completed) != 4 or any(x is None or x >= start for x in completed):
            errors.append('Préproduction démarrée avant la fin de réflexion F0–F3')
    elif strict:
        errors.append('Transition vers préproduction non exécutée')

    platforms = workflow['research']['platforms']
    if Counter(p['platform'] for p in platforms) != Counter({'LINKEDIN': 1, 'REDDIT': 1}):
        errors.append('Recherche : LinkedIn et Reddit doivent être représentés une seule fois')
    read_sources = set()
    for p in platforms:
        label = 'Recherche ' + p['platform']
        refs(p['evidence_ids'], label, {'source'}, needed=strict or p['status'] == 'READ')
        if p['status'] in {'READ', 'PARTIAL'}:
            if p['status'] == 'PARTIAL' and strict:
                errors.append(label + ': couverture incomplète, profil provisoire')
            if len({q.strip() for q in p['queries'] if q.strip()}) < 2 or not p['source_ids']:
                if p['status'] == 'READ':
                    errors.append(label + ': requêtes approfondies ou contenu lu absent')
            try:
                datetime.fromisoformat(p['attempted_at'] or '')
            except ValueError:
                errors.append(label + ': date de recherche absente/invalide')
            for sid in p['source_ids']:
                source = sources.get(sid)
                if not source or source['status'] != 'OBSERVED' or platform_of(source['url']) != p['platform']:
                    errors.append(label + ': source non lue ou hors plateforme ' + sid)
                elif not source['consulted_at'] or not source['note'].strip():
                    errors.append(label + ': lecture non documentée ' + sid)
                elif source['evidence_id'] not in p['evidence_ids']:
                    errors.append(label + ': preuve de lecture non reliée ' + sid)
                else:
                    read_sources.add(sid)
        elif strict:
            errors.append(label + ': couverture incomplète, profil provisoire')

    competencies = {c['id']: c for c in workflow['competencies']}
    for c in competencies.values():
        if not c['id'].strip() or any(not c[k].strip() for k in ['label', 'domain_application', 'behavior', 'calibration_case']):
            errors.append('Compétence sans application/comportement/calibration : ' + c['id'])
        if not c['role_ids'] or any(r not in roles or not roles[r]['assigned'] for r in c['role_ids']):
            errors.append('Compétence sans rôle affecté : ' + c['id'])
        if (strict and not c['source_ids']) or any(s not in read_sources for s in c['source_ids']):
            errors.append('Compétence sans sources métier lues : ' + c['id'])
    profiles = {p['role_id']: p for p in workflow['profiles']}
    evaluation_cache = {}
    for rid, p in profiles.items():
        label = 'Profil ' + rid
        if rid not in roles or not roles[rid]['assigned'] or p['niche'] != state['niche'] or not p['version'].strip():
            errors.append(label + ': rôle/niche/version incohérent')
        snapshot({'path': p['profile_path'], 'sha256': p['sha256']}, label)
        refs(p['training_evidence_ids'], label + ' formation', {'training'}, needed=strict)
        refs(p['calibration_evidence_ids'], label + ' calibration', {'training', 'test_report'}, needed=strict)
        evaluation = p.get('evaluation')
        if not evaluation:
            (errors if strict else warnings).append(label + ': évaluation Personna 1.2 absente ; profil provisoire')
        else:
            try:
                suite = safe_path(project, evaluation['suite_path'], True)
                run = safe_path(project, evaluation['run_path'])
                reviews = safe_path(project, evaluation['reviews_path'], True)
                report = safe_path(project, evaluation['report_path'], True)
                if not run.is_dir():
                    raise ValueError('Dossier de sessions absent')
                # Every imported run artifact stays inside the project. Never import
                # Python from a project, suite, evidence or dependency path.
                profile_path = safe_path(project, p['profile_path'], True)
                cache_key = (digest(profile_path), str(suite), str(run), str(reviews))
                if cache_key not in evaluation_cache:
                    for child in run.rglob('*'):
                        safe_path(project, child.relative_to(project).as_posix())
                    evaluation_cache[cache_key] = grade_personna(profile_path, suite, run, reviews)
                actual = evaluation_cache[cache_key]
                if actual['status'] != 'PASS':
                    raise ValueError('Sessions Personna : ' + actual['status'])
                if load(report) != actual:
                    raise ValueError('Rapport différent du recalcul des sessions')
                proof = ev.get(evaluation['evidence_id'])
                if not proof or proof['kind'] != 'test_report' or proof['path'] != evaluation['report_path'] or proof['sha256'] != digest(report):
                    raise ValueError('Preuve du rapport absente ou empreinte différente')
            except (ValueError, OSError, KeyError, TypeError, re.error) as exc:
                errors.append(label + ': évaluation Personna invalide : ' + str(exc))
        if strict and p['status'] != 'VERIFIED':
            errors.append(label + ': profil provisoire/non calibré')
        f1 = steps.get('F1_RECHERCHE', {}).get('sequence')
        if f1 is None or p['prepared_sequence'] <= f1:
            errors.append(label + ': préparé avant recherche métier')
        selected_sources = set()
        for cid in p['competency_ids']:
            c = competencies.get(cid)
            if not c or rid not in c['role_ids']:
                errors.append(label + ': compétence non intégrée au rôle ' + cid)
            else:
                selected_sources.update(c['source_ids'])
        if (strict or p['status'] == 'VERIFIED') and (not p['competency_ids'] or
                {platform_of(sources[s]['url']) for s in selected_sources if s in read_sources} != {'LINKEDIN', 'REDDIT'}):
            errors.append(label + ': compétences LinkedIn/Reddit non intégrées')
    if strict:
        for role in roles.values():
            if role['assigned'] and role['id'] not in profiles:
                errors.append('Profil métier absent : ' + role['id'])

    delegates = {d['id']: d for d in workflow['delegates']}
    minimum = 1 if state.get('planning_mode','full') == 'lite' else 2
    if strict and (len(delegates) < minimum or len({d['role_id'] for d in delegates.values()}) < minimum):
        errors.append('Un délégué critique réel requis en lite' if minimum == 1 else 'Au moins deux vrais sous-agents de rôles distincts requis')
    spawn_ids = [d['spawn_evidence_id'] for d in delegates.values()]
    if len(spawn_ids) != len(set(spawn_ids)):
        errors.append('Sous-agents : preuve de création réutilisée')
    for d in delegates.values():
        label = 'Sous-agent ' + d['id']
        p = profiles.get(d['role_id'])
        if not d['id'].strip() or not p or d['profile_sha256'] != p['sha256'] or d['brief_version'] != state['brief_version']:
            errors.append(label + ': profil/brief transmis incohérent')
        if (d['loaded_sequence'] < d['started_sequence'] or
                (p and d['loaded_sequence'] <= p['prepared_sequence'])):
            errors.append(label + ': persona chargé avant préparation/création')
        refs([d['spawn_evidence_id']], label + ' création', {'runtime'})
        refs([d['persona_load_evidence_id']], label + ' chargement du persona', {'runtime'})
        if d['loaded_sequence'] != d['started_sequence'] and d['persona_load_evidence_id'] == d['spawn_evidence_id']:
            errors.append(label + ': nouveau chargement sans nouvelle preuve runtime')
        refs(d['return_evidence_ids'], label + ' retours', {'runtime', 'review'}, needed=strict)
        if strict and d['status'] != 'RETURNED':
            errors.append(label + ': contribution non reçue')
        if d['closed_sequence'] is not None and d['closed_sequence'] <= d['started_sequence']:
            errors.append(label + ': fermeture avant création')
        if d['closed_sequence'] is not None and d['loaded_sequence'] >= d['closed_sequence']:
            errors.append(label + ': chargement après fermeture')
        if d['status'] == 'RETURNED' and d['closed_sequence'] is None:
            errors.append(label + ': fermeture non tracée')
        try:
            snapshot({'path': d['mandate_path'], 'sha256': d['mandate_sha256']}, label + ' mandat')
            mandate = load(safe_path(project, d['mandate_path'], True))
            expected = {'run_id': state['run_id'], 'brief_version': state['brief_version'],
                        'role_id': d['role_id'], 'niche': state['niche'],
                        'persona_path': p['profile_path'] if p else None,
                        'persona_sha256': d['profile_sha256'],
                        'persona_version': p['version'] if p else None}
            if not isinstance(mandate, dict) or any(mandate.get(k) != v for k, v in expected.items()):
                errors.append(label + ': mandat ne transmet pas le profil courant')
            elif (not isinstance(mandate.get('persona_loading_instruction'), str) or
                  not mandate['persona_loading_instruction'].strip() or
                  not isinstance(mandate.get('competency_ids'), list) or
                  not all(isinstance(cid, str) for cid in mandate['competency_ids']) or
                  not p or set(mandate['competency_ids']) != set(p['competency_ids'])):
                errors.append(label + ': chargement des compétences/persona absent')
        except (ValueError, OSError) as exc:
            errors.append(label + ': mandat invalide ' + str(exc))
    events = [(d['started_sequence'], 1) for d in delegates.values()]
    events += [(d['closed_sequence'], -1) for d in delegates.values() if d['closed_sequence'] is not None]
    active = 0
    for _, delta in sorted(events):
        active += delta
        if active > 2:
            errors.append('Sous-agents : plus de deux actifs simultanément')

    iterations = workflow['iterations']
    latest = {}
    seen_cycles = set()
    for it in iterations:
        key = (it['topic'], it['cycle'])
        if key in seen_cycles:
            errors.append('Cycle dupliqué : ' + str(key))
        seen_cycles.add(key)
        if it['topic'] not in latest or it['cycle'] > latest[it['topic']]['cycle']:
            latest[it['topic']] = it
    for topic in TOPICS:
        history = sorted([it for it in iterations if it['topic'] == topic], key=lambda it: it['cycle'])
        for previous, following in zip(history, history[1:]):
            if following['proposal_sequence'] <= previous['recheck_sequence']:
                errors.append('Chronologie des cycles incohérente : ' + topic)
    for it in iterations:
        label = 'Cycle ' + it['id']
        seq = [it[k] for k in ['proposal_sequence', 'critique_sequence', 'resolution_sequence', 'recheck_sequence']]
        if seq != sorted(set(seq)):
            errors.append(label + ': critique/résolution/relecture dans le mauvais ordre')
        d = delegates.get(it['reviewer_delegate_id'])
        if not d or it['author_id'] not in roles or not roles[it['author_id']]['assigned'] or it['author_id'] == d['role_id']:
            errors.append(label + ': critique métier distinct absent')
        elif (it['critique_sequence'] <= d['started_sequence'] or
              (d['closed_sequence'] is not None and it['recheck_sequence'] >= d['closed_sequence'])):
            errors.append(label + ': relecture hors session du critique')
        elif latest.get(it['topic']) is it and it['critique_sequence'] <= d['loaded_sequence']:
            errors.append(label + ': critique avant chargement du persona courant')
        elif any(eid not in d['return_evidence_ids'] for eid in [it['critique_evidence_id'], it['recheck_evidence_id']]):
            errors.append(label + ': critique/relecture non reçues de cet agent')
        refs([it['critique_evidence_id'], it['recheck_evidence_id']], label, {'runtime', 'review'})
        refs([it['resolution_evidence_id']], label + ' résolution', {'artifact', 'review'})
        if it['critique_evidence_id'] == it['recheck_evidence_id']:
            errors.append(label + ': nouvelle relecture absente')
        if len({it['critique_evidence_id'], it['resolution_evidence_id'], it['recheck_evidence_id']}) != 3:
            errors.append(label + ': critique/résolution/relecture exigent trois preuves distinctes')
        snapshot(it['proposal'], label + ' proposition')
        snapshot(it['reviewed'], label + ' relecture', current=latest.get(it['topic']) is it)
        if it['topic'] != 'idees' and (start is None or it['proposal_sequence'] <= start):
            errors.append(label + ': préproduction avant réflexion')
        if it['status'] == 'PASSED' and latest.get(it['topic']) is it:
            if it['reviewed']['path'] not in artifacts:
                errors.append(label + ': livrable relu hors registre')
            if strict:
                matching = [r for r in state['reviews'] if r['topic'] == it['topic'] and r['verdict'] == 'APPROVED'
                            and d and r['reviewer_id'] == d['role_id'] and r['author_id'] == it['author_id']
                            and r['trace_id'] == d['id'] and r['mode'] == 'INDEPENDENT'
                            and it['recheck_evidence_id'] in r['evidence_ids'] and it['reviewed'] in r['reviewed_artifacts']]
                if not matching:
                    errors.append(label + ': approbation courante non reliée à la relecture')
    if strict:
        for topic in TOPICS:
            if topic not in latest or latest[topic]['status'] != 'PASSED':
                errors.append('Cycle complet absent : ' + topic)
        f3 = steps.get('F3_DECISION', {}).get('sequence')
        if f3 is None or not any(it['topic'] == 'idees' and it['status'] == 'PASSED' and it['recheck_sequence'] < f3 for it in iterations):
            errors.append('Décision F3 sans cycle idées clos auparavant')
        for r in state['reviews']:
            if r.get('workflow_inputs_sha256') != workflow_digest(workflow, state['evidence']):
                errors.append('Revue caduque : recherche/profil/mandat modifié : ' + r['id'])
    return errors, warnings
