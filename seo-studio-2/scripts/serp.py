"""Local SERP contract. Hashes bind declarations, not their external truth."""
from datetime import date
import hashlib
import json
from urllib.parse import urlsplit


def _hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(',', ':')).encode('utf-8')).hexdigest()


def architecture_digest(state):
    """Stable architecture only; approval metadata cannot create a hash cycle."""
    keys = ['id', 'path', 'intent_id', 'public', 'indexable', 'canonical_path', 'wave', 'kind']
    pages = [{key: page[key] for key in keys} for page in state['pages']]
    return _hash({'pages': sorted(pages, key=lambda p: p['id']),
                  'links': sorted(state['links'], key=lambda link: link['id'])})


def research_digest(report):
    return _hash({key: value for key, value in report.items() if key != 'approval'})


def source_evidence_digest(report, evidence):
    """Bind declared source records; review proofs excluded to avoid a cycle."""
    ids = set()
    for observation in report['observations']:
        ids.update(observation['evidence_ids'])
        for key in ('volume', 'difficulty'):
            metric = observation[key]
            if metric['status'] == 'SOURCED':
                ids.update(metric['evidence_ids'])
    selected = [entry for entry in evidence if entry['id'] in ids]
    return _hash(sorted(selected, key=lambda entry: entry['id']))


def validate_serp(project, state, strict, *, load, shape, safe_path, digest, root):
    errors, warnings = [], []
    gates = {gate['id']: gate['status'] for gate in state['gates']}
    advanced = any(gates.get(gate) == 'APPROVED' for gate in ['G3', 'G4', 'G5', 'G6'])
    required = strict or advanced or gates.get('G2') == 'APPROVED'
    if advanced and gates.get('G2') != 'APPROVED':
        errors.append('SERP : G2 doit être approuvé avant G3 et les étapes suivantes')
    try:
        path = safe_path(project, 'research/serp.json')
        if not path.is_file():
            (errors if required else warnings).append('SERP : research/serp.json absent ; compléter sans inventer de classement')
            return errors, warnings
        report = load(path)
        structure = shape(report, load(root / 'schemas/serp.schema.json'), '$serp')
        if structure:
            return errors + structure, warnings
    except (OSError, ValueError) as exc:
        return errors + ['SERP : ' + str(exc)], warnings
    for key in ['run_id', 'niche']:
        if report[key] != state[key]:
            errors.append('SERP : contexte différent ' + key)
    context = report['context']
    if any(not context[key].strip() for key in ['engine', 'country', 'language', 'device', 'coverage']):
        (errors if required else warnings).append('SERP : contexte moteur/pays/langue/appareil/couverture incomplet')
    try:
        date.fromisoformat(context['observed_at'])
    except ValueError:
        (errors if required else warnings).append('SERP : date observée invalide (AAAA-MM-JJ)')
    evidence = {entry['id']: entry for entry in state['evidence']}

    def refs(ids, label, kinds):
        if not ids:
            errors.append('SERP : preuve absente ' + label)
        for eid in ids:
            proof = evidence.get(eid)
            if not proof or proof['kind'] not in kinds:
                errors.append('SERP : preuve inconnue/type incorrect ' + label + ' ' + eid)
                continue
            try:
                if digest(safe_path(project, proof['path'], True)) != proof['sha256']:
                    errors.append('SERP : preuve modifiée ' + eid)
            except (OSError, ValueError) as exc:
                errors.append('SERP : preuve inaccessible ' + eid + ' ' + str(exc))

    def web_url(value):
        try:
            parsed = urlsplit(value)
            return parsed.scheme in {'https', 'http'} and bool(parsed.hostname) and not parsed.username and not parsed.password
        except ValueError:
            return False

    observations = {}
    for row in report['observations']:
        if not row['id'].strip() or row['id'] in observations:
            errors.append('SERP : identifiant observation vide/dupliqué')
        observations[row['id']] = row
        if any(not row[key].strip() for key in ['intent', 'query', 'intention', 'format', 'gap']):
            errors.append('SERP : observation incomplète ' + row['id'])
        if not web_url(row['source_url']):
            errors.append('SERP : URL source invalide ' + row['id'])
        if row['position'] is not None and row['collection_method'] != 'RANKED_SERP':
            errors.append('SERP : position réservée à une SERP classée observée, pas à une recherche web générique')
        refs(row['evidence_ids'], row['id'], {'source', 'http', 'test_report'})
        for key in ['volume', 'difficulty']:
            metric = row[key]
            if metric['status'] == 'UNKNOWN':
                if metric['value'] is not None or metric['source_url'] is not None or metric['evidence_ids']:
                    errors.append('SERP : métrique UNKNOWN ne doit pas inventer de valeur/source ' + key)
            elif metric['status'] == 'SOURCED':
                if metric['value'] is None or not web_url(metric['source_url']):
                    errors.append('SERP : métrique sourcée incomplète ' + key)
                refs(metric['evidence_ids'], row['id'] + ':' + key, {'source', 'http', 'test_report'})
            elif key != 'difficulty' or not isinstance(metric['value'], str) or not metric['value'].strip() or not metric['note'].strip():
                errors.append('SERP : appréciation qualitative réservée à une difficulté argumentée')
    pages = {page['id']: page for page in state['pages']}
    expected = {page['id'] for page in state['pages'] if page['public'] and page['indexable'] and page['wave'] == 'V1'}
    owners, queries, targets = {}, {}, set()
    for target in report['targets']:
        pid = target['page_id']
        if pid in targets or pid not in pages:
            errors.append('SERP : page cible inconnue/dupliquée ' + pid)
        targets.add(pid)
        if any(not target[key].strip() for key in ['main_query', 'intent', 'target_format', 'gap']):
            errors.append('SERP : cible incomplète ' + pid)
        if pid in pages and target['intent'] != pages[pid]['intent_id']:
            errors.append('SERP : intention cible/architecture différente ' + pid)
        if target['intent'] in owners and owners[target['intent']] != pid:
            errors.append('SERP : intention principale sans propriétaire unique ' + target['intent'])
        owners[target['intent']] = pid
        query = ' '.join(target['main_query'].casefold().split())
        if query in queries and queries[query] != pid:
            warnings.append('SERP : requête partagée ; examiner le chevauchement sans conclure automatiquement à une cannibalisation ' + query)
        queries[query] = pid
        if not target['observation_ids']:
            (errors if required else warnings).append('SERP : intention sans observation ' + pid)
        for oid in target['observation_ids']:
            observation = observations.get(oid)
            if not observation or observation['intent'] != target['intent']:
                errors.append('SERP : observation absente ou intention différente ' + pid + ' ' + oid)
        success = target['success']
        if any(not success[key].strip() for key in ['metric', 'window', 'conditions']):
            (errors if required else warnings).append('SERP : succès sans période/conditions de mesure ' + pid)
        if success['baseline'] is None or success['target'] is None:
            warnings.append('SERP : baseline/objectif inconnu ; aucune performance promise ' + pid)
    if expected - targets:
        (errors if required else warnings).append('SERP : pages V1 publiques indexables sans cible ' + ', '.join(sorted(expected - targets)))
    approval = report['approval']
    if required and approval['status'] != 'APPROVED':
        errors.append('SERP : recherche et architecture doivent être approuvées avant G3')
    if approval['status'] == 'APPROVED':
        if approval['architecture_sha256'] != architecture_digest(state):
            errors.append('SERP : architecture modifiée depuis approbation G2')
        if approval['research_sha256'] != research_digest(report):
            errors.append('SERP : recherche modifiée depuis approbation G2')
        if approval.get('source_evidence_sha256') != source_evidence_digest(report, state['evidence']):
            errors.append('SERP : preuves sources modifiées depuis approbation G2')
        refs(approval['evidence_ids'], 'approbation G2', {'review'})
        gate = next((gate for gate in state['gates'] if gate['id'] == 'G2'), None)
        if gate and not set(approval['evidence_ids']).issubset(gate['evidence_ids']):
            errors.append('SERP : preuve approbation non rattachée à G2')
    return errors, warnings
