#!/usr/bin/env python3
"""SEO STUDIO 2: outils locaux déterministes. Aucun réseau, modèle ou CMS.

La validation structurelle ne vérifie pas la vérité d'une source, la qualité d'un
texte, ni l'authenticité d'une trace d'agent. Les revues métier restent nécessaires.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import sys
import uuid
from typing import Any
from urllib.parse import urlsplit
from workflow import validate_workflow, workflow_digest

ROOT = Path(__file__).resolve().parents[1]
CORE = {'brain', 'organisation', 'no-slop', 'design-dna'}
QUALITY = {'site-checklist', 'pSEO', 'webapp-testing', 'cross-platform-qa', 'security-best-practices', 'web-perf', 'redaction-editoriale-web'}
BASE_SEO = {'seo', 'ai-seo', 'seo-audit', 'seo-content-engine', 'seo-post-deploy'}
SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
PLACEHOLDER = re.compile(r'\b(?:A_COMPLETER|TODO|LOREM IPSUM)\b', re.I)
HASH = re.compile(r'^[0-9a-f]{64}$')


def load(path: Path) -> Any:
    def unique_pairs(pairs):
        result={}
        for key,value in pairs:
            if key in result:
                raise ValueError('Clé JSON dupliquée : '+key)
            result[key]=value
        return result
    def reject_constant(value):
        raise ValueError('Constante non JSON : '+value)
    with path.open(encoding='utf-8-sig') as fh:
        return json.load(fh,object_pairs_hook=unique_pairs,parse_constant=reject_constant)


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for part in iter(lambda: fh.read(65536), b''):
            h.update(part)
    return h.hexdigest()


def json_text(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + '\n'


def safe_path(root: Path, value: str, require_file: bool = False) -> Path:
    """Refuse chemins absolus, traversal et liens symboliques dans le dossier."""
    if not isinstance(value, str) or not value or '\\' in value or '\x00' in value:
        raise ValueError('Chemin relatif POSIX attendu')
    p = PurePosixPath(value)
    if p.is_absolute() or PureWindowsPath(value).drive or any(x in ('..', '.') for x in value.split('/')):
        raise ValueError(f'Chemin interdit: {value}')
    root = root.absolute()
    for check in [root, *root.parents]:
        if check.is_symlink():
            raise ValueError('Racine ou parent symbolique: fournir le chemin réel autorisé')
    out = root.joinpath(*p.parts)
    for check in [out, *out.parents]:
        if check == root.parent:
            break
        if check.is_symlink():
            raise ValueError(f'Lien symbolique interdit: {value}')
    if not out.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Chemin sortant: {value}')
    if require_file and not out.is_file():
        raise ValueError(f'Fichier absent: {value}')
    return out


def shape(data: Any, schema: dict, where: str = '$') -> list[str]:
    """Sous-ensemble utilisé par notre schéma; pas un validateur JSON Schema général."""
    errors = []
    kinds = {'object': lambda x: isinstance(x, dict), 'array': lambda x: isinstance(x, list),
             'string': lambda x: isinstance(x, str), 'boolean': lambda x: type(x) is bool,
             'integer': lambda x: type(x) is int, 'null': lambda x: x is None}
    required_type = schema.get('type')
    types = required_type if isinstance(required_type, list) else [required_type]
    if required_type and not any(kinds[t](data) for t in types):
        return [f'{where}: type attendu {required_type}']
    if 'enum' in schema and data not in schema['enum']:
        errors.append(f'{where}: valeur hors enum')
    if isinstance(data, dict):
        for key in schema.get('required', []):
            if key not in data:
                errors.append(f'{where}.{key}: champ obligatoire absent')
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            for key in data.keys() - props.keys():
                errors.append(f'{where}.{key}: champ inconnu')
        for key, value in data.items():
            if key in props:
                errors.extend(shape(value, props[key], f'{where}.{key}'))
    if isinstance(data, list):
        if len(data) < schema.get('minItems', 0):
            errors.append(f'{where}: liste trop courte')
        if 'items' in schema:
            for i, value in enumerate(data):
                errors.extend(shape(value, schema['items'], f'{where}[{i}]'))
    if type(data) is int and data < schema.get('minimum', data):
        errors.append(f'{where}: valeur sous minimum')
    return errors


def input_digest(state: dict) -> str:
    """Empreinte des entrées métier, sans journaux/revues pour éviter un cycle."""
    keys = ['niche','site_type','brief_version','assumptions','unknowns','pages','links','placements','claims','sources']
    payload = {key:state[key] for key in keys}
    return hashlib.sha256(json.dumps(payload,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')).hexdigest()


def review_snapshot(project: Path) -> dict:
    state=load(safe_path(project,'state.json',True))
    errors=shape(state,load(ROOT/'schemas/state.schema.json'))
    if errors:
        raise ValueError('Structure invalide : '+str(errors))
    artifacts=[]
    for a in state['artifacts']:
        path=safe_path(project,a['path'],True)
        artifacts.append({'path':a['path'],'sha256':digest(path)})
    workflow_path = safe_path(project, 'workflow.json')
    workflow_hash = None
    if workflow_path.is_file():
        workflow = load(workflow_path)
        workflow_errors = shape(workflow, load(ROOT/'schemas/workflow.schema.json'))
        if workflow_errors:
            raise ValueError('Workflow invalide : '+str(workflow_errors))
        workflow_hash = workflow_digest(workflow, state['evidence'])
    return {'inputs_sha256':input_digest(state),'workflow_inputs_sha256':workflow_hash,'reviewed_artifacts':artifacts,
            'warning':'Instantané technique uniquement : aucune revue ni approbation effectuée par cette commande.'}


def inventory(roots: list[Path]) -> dict:
    entries, skipped, seen = [], [], set()
    inspected = 0
    for root in roots:
        if not root.is_dir() or root.is_symlink():
            skipped.append({'path': str(root), 'reason': 'absent ou racine symbolique'})
            continue
        for folder, dirs, files in os.walk(root, followlinks=False):
            inspected += 1
            if inspected > 50000:
                skipped.append({'path': str(root), 'reason': 'limite de 50000 dossiers atteinte'})
                break
            for name in list(dirs):
                p = Path(folder) / name
                if name in SKIP_DIRS or p.is_symlink():
                    dirs.remove(name)
                    if p.is_symlink():
                        skipped.append({'path': str(p), 'reason': 'lien symbolique non suivi; inspecter le chemin réel autorisé'})
            for filename in files:
                if filename.lower() != 'skill.md':
                    continue
                p = Path(folder) / filename
                if p.is_symlink():
                    skipped.append({'path': str(p), 'reason': 'fichier symbolique'})
                    continue
                resolved = str(p.resolve())
                if resolved in seen:
                    continue
                seen.add(resolved)
                try:
                    text = p.read_text(encoding='utf-8-sig')
                except (OSError, UnicodeError) as exc:
                    skipped.append({'path': str(p), 'reason': str(exc)})
                    continue
                match = re.match(r'^---\s*\n(.*?)\n---', text, re.S)
                header = match.group(1) if match else ''
                name_match = re.search(r'^name:\s*(.+?)\s*$', header, re.M)
                name = name_match.group(1).strip('"\' ') if name_match else p.parent.name
                norm = name.lower().replace('_', '-')
                # The same canonical name is always excluded to avoid calling ourselves.
                if norm == 'seo-studio-2':
                    continue
                primary = 'seo' in norm or 'seo' in p.parent.name.lower()
                candidate = 'seo' in header.lower()
                selected = primary or candidate or norm in CORE | {n.lower() for n in QUALITY} | {'personna', 'persona'}
                if not selected:
                    continue
                v = re.search(r'^\s*version:\s*(.+?)\s*$', header, re.M)
                entries.append({'name': name, 'path': resolved, 'sha256': digest(p),
                    'version': v.group(1).strip('"\' ') if v else None,
                    'kind': 'SEO_IDENTIFIER' if primary else 'CORE' if norm in CORE else 'QUALITY' if norm in {n.lower() for n in QUALITY} else 'PERSONNA_CANDIDATE' if norm in {'persona','personna'} else 'SEO_DESCRIPTION_CANDIDATE',
                    'status': 'DISCOVERED_NEEDS_READING'})
    groups = defaultdict(list)
    for entry in entries:
        groups[entry['name'].lower()].append(entry)
    return {'generated_at': datetime.now(timezone.utc).isoformat(), 'read_only': True,
            'host_discovery_verified': False, 'entries': entries,
            'duplicates': {n: {'paths':[e['path'] for e in es], 'identical':len({e['sha256'] for e in es}) == 1}
                           for n, es in groups.items() if len(es) > 1},
            'skipped': skipped, 'coverage_complete_for_requested_roots': not skipped,
            'warning': 'Inventaire de fichiers, pas preuve de chargement par l’hôte. Lire les instructions réelles. persona n’est pas automatiquement /personna.'}


def initial_files(niche: str, site_type: str) -> dict[str, str]:
    if not niche.strip() or not site_type.strip():
        raise ValueError('niche et site_type ne peuvent pas être vides')
    state = load(ROOT/'templates/state.json')
    state.update(niche=niche.strip(), site_type=site_type.strip(), run_id=str(uuid.uuid4()))
    contents = {}
    for filename, headings in load(ROOT/'templates/deliverables.json').items():
        title = filename.removesuffix('.md').replace('_', ' ')
        contents[filename] = f'# {title}\n\nSTATUT : A_COMPLETER\n\n' + ''.join(f'## {h}\n\nA_COMPLETER\n\n' for h in headings)
        state['artifacts'].append({'id': filename.removesuffix('.md'), 'path': filename,
            'kind': 'report', 'content_type': None, 'owner': 'TERRA', 'status': 'DRAFT', 'evidence_id': None})
    contents['PROJECT_SKIN.yaml'] = (ROOT/'templates/project-skin.yaml').read_text(encoding='utf-8')
    state['artifacts'].append({'id':'skin','path':'PROJECT_SKIN.yaml','kind':'skin','content_type':None,'owner':'DESIGN_LEAD','status':'DRAFT','evidence_id':None})
    contents['BRIEFS/README.md'] = '# Briefs V1\n\nA_COMPLETER : créer un brief intégral par page V1 depuis le template du skill.\n'
    contents['PILOTES/README.md'] = '# Contenus pilotes\n\nA_COMPLETER : écrire les pilotes correspondant au type de site, sans inventer de preuves.\n'
    workflow = load(ROOT/'templates/workflow.json')
    workflow.update(run_id=state['run_id'], niche=state['niche'], brief_version=state['brief_version'])
    contents['workflow.json'] = json_text(workflow)
    contents['state.json'] = json_text(state)
    return contents


def init_project(project: Path, niche: str, site_type: str, apply: bool = False) -> dict:
    project = project.absolute()
    safe_path(project, 'state.json')
    if (project/'state.json').exists():
        old = load(project/'state.json')
        if old.get('niche') != niche.strip() or old.get('site_type') != site_type.strip():
            raise ValueError('Projet existant différent : aucune réinitialisation autorisée')
        return {'status':'EXISTS_UNCHANGED','written':[], 'message':'Reprendre le dossier existant sans écrasement.'}
    proposed = initial_files(niche, site_type)
    collisions = [f for f in proposed if safe_path(project, f).exists()]
    if collisions:
        raise ValueError('Dossier partiellement existant : reprise manuelle sans écrasement, conflits : '+', '.join(collisions))
    written = []
    if apply:
        for filename, text in proposed.items():
            path = safe_path(project, filename)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open('x', encoding='utf-8', newline='\n') as fh:
                fh.write(text)
            written.append(filename)
    return {'status':'SCAFFOLD_CREATED' if apply else 'DRY_RUN', 'would_create':list(proposed), 'written':written,
            'warning':'Structure uniquement : textes, preuves, formation et revues à produire. Aucun gate validé.'}


def validate_project(project: Path, stage: str = 'draft') -> dict:
    project = project.absolute()
    state_path = safe_path(project, 'state.json', True)
    state = load(state_path)
    errors = shape(state, load(ROOT/'schemas/state.schema.json'))
    warnings = []
    if errors:
        return {'status':'BLOQUE','stage':stage,'errors':errors,'warnings':warnings}
    strict = stage in {'handoff','release'}
    requirements = {r['id']:r for r in load(ROOT/'schemas/requirements.json')['requirements']}
    for field in ('dependencies','roles','requirements','artifacts','evidence','sources','claims','pages','links','placements','reviews','objections','decisions','gates'):
        key = 'name' if field == 'dependencies' else 'id'
        counts = Counter(x[key] for x in state[field])
        errors.extend(f'{field}: identifiant dupliqué {v}' for v, count in counts.items() if count > 1)
    ev = {e['id']:e for e in state['evidence']}
    roles = {r['id']:r for r in state['roles']}
    pages = {p['id']:p for p in state['pages']}
    sources = {s['id']:s for s in state['sources']}
    decisions = {d['id']:d for d in state['decisions']}
    artifacts = {a['path']:a for a in state['artifacts']}
    workflow_errors, workflow_warnings = validate_workflow(project, state, strict,
        load=load, shape=shape, safe_path=safe_path, digest=digest, root=ROOT)
    errors.extend(workflow_errors)
    warnings.extend(workflow_warnings)

    def refs(values: list[str], label: str, needed: bool = False) -> None:
        if needed and not values:
            errors.append(f'{label}: preuve absente')
        for value in values:
            if value not in ev:
                errors.append(f'{label}: preuve inconnue {value}')

    for evidence in state['evidence']:
        try:
            path = safe_path(project, evidence['path'], True)
            if not HASH.fullmatch(evidence['sha256']) or digest(path) != evidence['sha256']:
                errors.append(f"preuve {evidence['id']}: empreinte invalide ou périmée")
            if not evidence['origin'].strip():
                errors.append(f"preuve {evidence['id']}: provenance absente")
        except ValueError as exc:
            errors.append(f"preuve {evidence['id']}: {exc}")

    runtime = state['runtime']
    if runtime['max_active_delegates'] > 2 or runtime['executed_depth'] > 1:
        errors.append('Exécution : deux délégués maximum, aucun descendant')
    if runtime['mode'] == 'SEQUENTIAL_PROFILES' and (runtime['max_active_delegates'] or runtime['executed_depth']):
        errors.append('Mode séquentiel incohérent avec une délégation déclarée')
    if runtime['mode'] == 'DELEGATED' and (not runtime['delegation_available'] or runtime['max_active_delegates'] < 1 or runtime['executed_depth'] != 1):
        errors.append('Mode délégué sans capacité/exécution cohérente')
    if strict and not runtime['independent_review_required']:
        errors.append('Le contrat strict exige une confrontation indépendante ; ne pas la désactiver par un booléen')
    if strict and runtime['independent_review_required']:
        if runtime['mode'] != 'DELEGATED' or not runtime['model_selection_verified']:
            errors.append('Revue indépendante/modèles vérifiés requis pour le transfert strict')

    for role in state['roles']:
        if role['parent_id'] is not None and role['parent_id'] not in roles:
            errors.append(f"rôle {role['id']}: parent inconnu")
        visited, current = set(), role['id']
        while current in roles:
            if current in visited:
                errors.append(f"rôle {role['id']}: cycle hiérarchique")
                break
            visited.add(current)
            current = roles[current]['parent_id']
        refs(role['evidence_ids'], 'rôle '+role['id'], needed=strict and role['assigned'])
        if strict and role['assigned']:
            if role['training_status'] != 'FORME':
                errors.append(f"rôle {role['id']}: /personna non validé")
            if not any(ev.get(x, {}).get('kind') == 'training' for x in role['evidence_ids']):
                errors.append(f"rôle {role['id']}: preuve de formation manquante")
    if strict and not all(x in roles and roles[x]['assigned'] for x in ['ASTRA','TERRA']):
        errors.append('ASTRA et TERRA doivent être affectés')

    personna = state['personna']
    refs(personna['evidence_ids'], '/personna', strict)
    if strict and (personna['status'] != 'EXECUTED' or not personna['source_path'] or not HASH.fullmatch(personna['sha256'] or '')):
        errors.append('/personna canonique non exécuté ou provenance absente')
    deps = {d['name']:d for d in state['dependencies']}
    for dep in state['dependencies']:
        if dep['read_evidence_id']:
            refs([dep['read_evidence_id']], 'dépendance '+dep['name'])
        if strict:
            if dep['status'] not in {'LU','NON_APPLICABLE','PREPARE_PHASE_ULTERIEURE'}:
                errors.append('dépendance non lue : '+dep['name'])
            if not dep['path'] or not HASH.fullmatch(dep['sha256'] or '') or not dep['read_evidence_id']:
                errors.append('provenance de lecture absente : '+dep['name'])
            if dep['status'] != 'LU' and not dep['reason']:
                errors.append('exclusion/phase sans motif : '+dep['name'])
            if dep['name'] in CORE | QUALITY and dep['status'] != 'LU':
                errors.append('socle transversal obligatoire : '+dep['name'])
    if 'seo-studio-2' in deps or 'seo-studio-2' in state['discovered_seo_skills']:
        errors.append('Récursion : le studio ne peut pas se rappeler')
    discovered = set(state['discovered_seo_skills'])
    if strict and not (CORE | BASE_SEO | QUALITY).issubset(deps):
        errors.append('Socle de dépendances incomplet')
    if strict and not BASE_SEO.issubset(discovered):
        errors.append('Inventaire des skills SEO de base incomplet')
    for name in discovered:
        if name not in deps:
            errors.append('Skill SEO découvert non classé : '+name)
    for name in deps:
        if 'seo' in name.lower() and name not in discovered:
            errors.append('Skill SEO omis du relevé : '+name)

    for a in state['artifacts']:
        try:
            path = safe_path(project, a['path'], True)
            text = path.read_text(encoding='utf-8-sig') if path.suffix.lower() in {'.md','.json','.yaml','.yml','.txt'} else ''
            if strict and PLACEHOLDER.search(text):
                errors.append('Artefact encore au stade template : '+a['path'])
            if strict and a['status'] != 'REVIEWED':
                errors.append('Artefact non relu : '+a['path'])
            if a['owner'] not in roles:
                errors.append('Propriétaire inconnu : '+a['path'])
            elif strict and not roles[a['owner']]['assigned']:
                errors.append('Propriétaire non affecté : '+a['path'])
            if a['evidence_id']:
                refs([a['evidence_id']], 'artefact '+a['path'])
                if a['evidence_id'] in ev and ev[a['evidence_id']]['path'] != a['path']:
                    errors.append('La preuve ne porte pas sur cet artefact : '+a['path'])
            elif strict:
                errors.append('Empreinte de relecture absente : '+a['path'])
        except (ValueError, UnicodeError) as exc:
            errors.append(f"artefact {a['path']}: {exc}")
    if strict:
        expected = set(load(ROOT/'templates/deliverables.json')) | {'PROJECT_SKIN.yaml'}
        errors.extend('Livrable obligatoire absent du registre : '+p for p in expected - artifacts.keys())
        if not any(a['kind'] == 'pilot' for a in state['artifacts']):
            errors.append('Aucun contenu pilote écrit dans le registre')
        pilots = [a for a in state['artifacts'] if a['kind'] == 'pilot']
        pilot_exception = any(d['scope']=='pilot_scope' and d['status']=='RESOLVED' and d['summary'].strip() for d in state['decisions'])
        if len(pilots) < 3 and not (len(pilots)>=1 and pilot_exception):
            errors.append('Lot pilote incomplet : trois contenus adaptés, ou exception de périmètre pilot_scope motivée par Astra')

    for s in state['sources']:
        if s['evidence_id']:
            refs([s['evidence_id']], 'source '+s['id'])
        if strict and s['status'] in {'OBSERVED','SUPPLIED'} and (not s['evidence_id'] or not s['consulted_at']):
            errors.append('Source sans preuve/date : '+s['id'])
        if s['status'] == 'OBSERVED' and (not s['url'] or urlsplit(s['url']).scheme not in {'http','https'}):
            errors.append('Source web sans URL HTTP valide : '+s['id'])
    for c in state['claims']:
        refs(c['evidence_ids'], 'affirmation '+c['id'])
        for sid in c['source_ids']:
            if sid not in sources or sources[sid]['status'] == 'NOT_OBSERVED':
                errors.append('Affirmation sur source absente/non observée : '+c['id'])
        if c['type'] == 'FACT' and not (c['source_ids'] or c['evidence_ids']):
            errors.append('Fait sans source/preuve : '+c['id'])
        if c['first_hand'] and not any(ev.get(x,{}).get('kind') == 'test_report' for x in c['evidence_ids']):
            errors.append('Expérience/essai sans rapport : '+c['id'])
    if strict and not any(s['status'] == 'OBSERVED' for s in state['sources']):
        errors.append('Recherche documentaire sans source web observée')

    intent_counts = Counter(p['intent_id'] for p in state['pages'] if p['intent_id'])
    errors.extend('Intention propriétaire dupliquée : '+i for i,c in intent_counts.items() if c > 1)
    route_counts = Counter(p['path'] for p in state['pages'])
    errors.extend('Route dupliquée : '+u for u,c in route_counts.items() if c > 1)
    if strict:
        titles = Counter(p['title'].strip().casefold() for p in state['pages'] if p['public'] and p['indexable'] and p['title'].strip())
        errors.extend('Title dupliqué entre pages propriétaires : '+t for t,c in titles.items() if c > 1)
    for p in state['pages']:
        if not p['path'].startswith('/') or p['path'].startswith('//') or '#' in p['path'] or '\\' in p['path'] or '..' in p['path'].split('/'):
            errors.append('Route canonique de plan invalide : '+p['id'])
        if p['indexable'] and not p['public']:
            errors.append('Page privée indexable : '+p['id'])
        if p['canonical_path'] != p['path'] and p['indexable']:
            errors.append('Page propriétaire indexable sans canonical propre : '+p['id'])
        if strict:
            for field in ['intent_id','title','h1','next_action','proof_plan']:
                if not p[field].strip():
                    errors.append(f"page {p['id']}: {field} absent")
            if p['wave'] == 'V1':
                if not p['brief_path'] or p['brief_path'] not in artifacts or artifacts[p['brief_path']]['kind'] != 'brief':
                    errors.append('Brief V1 absent du registre : '+p['id'])
    adjacency = defaultdict(set)
    launch = defaultdict(set)
    for link in state['links']:
        if link['from'] not in pages or link['to'] not in pages:
            errors.append('Lien vers page inconnue : '+link['id'])
            continue
        if not all(link[k].strip() for k in ['anchor','reason','placement']):
            errors.append('Lien sans ancre/raison/emplacement : '+link['id'])
        adjacency[link['from']].add(link['to'])
        if link['active_at_launch']:
            if pages[link['from']]['wave'] == 'V1' and pages[link['to']]['wave'] != 'V1':
                errors.append('Lien actif V1 vers une page future : '+link['id'])
            launch[link['from']].add(link['to'])
    homes = [p['id'] for p in state['pages'] if p['path'] == '/']
    if strict and len(homes) != 1:
        errors.append('Une racine de navigation / doit être définie')
    if homes:
        def reachable(graph: dict) -> set:
            visited, todo = set(), deque(homes)
            while todo:
                here = todo.popleft()
                if here in visited:
                    continue
                visited.add(here)
                todo.extend(graph.get(here, set()) - visited)
            return visited
        for graph, only_v1 in [(adjacency,False),(launch,True)]:
            reached = reachable(graph)
            for p in state['pages']:
                if p['public'] and p['indexable'] and (not only_v1 or p['wave']=='V1') and p['id'] not in reached:
                    errors.append('Page orpheline'+(' V1' if only_v1 else '')+' : '+p['id'])

    for placement in state['placements']:
        if placement['page_id'] not in pages:
            errors.append('Encart sur page inconnue : '+placement['id'])
        if placement['paid'] and ('sponsored' not in placement['rel'] or not placement['disclosure'].strip()):
            errors.append('Encart payé sans sponsored/disclosure : '+placement['id'])
        if placement['target_type'] != placement['label_target_type']:
            errors.append('Destination annoncée différente de la destination réelle : '+placement['id'])
        if placement['url']:
            split = urlsplit(placement['url'])
            if split.scheme not in {'http','https'} or not split.netloc or split.username or split.password:
                errors.append('URL partenaire non HTTP ou contenant des identifiants : '+placement['id'])
        if placement['url_status']=='VERIFIED' and not placement['url']:
            errors.append('Lien déclaré vérifié sans URL : '+placement['id'])
        if stage=='release' and placement['active_at_launch'] and placement['target_type']!='none' and placement['url_status']!='VERIFIED':
            errors.append('Lien partenaire de lancement non vérifié : '+placement['id'])

    for decision in state['decisions']:
        refs(decision['evidence_ids'], 'décision '+decision['id'], strict)
        if strict and (not decision['summary'].strip() or not decision['scope'].strip()):
            errors.append('Décision non motivée : '+decision['id'])
    for objection in state['objections']:
        refs(objection['evidence_ids'], 'objection '+objection['id'], strict)
        if strict and objection['severity'] in {'P0','P1'} and objection['status']=='OPEN':
            errors.append('Objection bloquante ouverte : '+objection['id'])
        if objection['status']=='ARBITRATED':
            d = decisions.get(objection['decision_id'])
            if not d or d['authority']!='ASTRA' or d['status']!='RESOLVED':
                errors.append('Arbitrage Astra résolu absent : '+objection['id'])
    for review in state['reviews']:
        if not HASH.fullmatch(review['inputs_sha256']) or review['inputs_sha256'] != input_digest(state):
            errors.append('Revue caduque : entrées métier modifiées : '+review['id'])
        if strict and not review['reviewed_artifacts']:
            errors.append('Revue sans instantané des fichiers : '+review['id'])
        for snapshot in review['reviewed_artifacts']:
            try:
                path=safe_path(project,snapshot['path'],True)
                if not HASH.fullmatch(snapshot['sha256']) or digest(path)!=snapshot['sha256']:
                    errors.append('Revue caduque : fichier modifié : '+review['id']+' / '+snapshot['path'])
            except ValueError as exc:
                errors.append('Instantané de revue invalide : '+str(exc))
        refs(review['evidence_ids'], 'revue '+review['id'], strict)
        if review['author_id'] not in roles or review['reviewer_id'] not in roles:
            errors.append('Acteur de revue inconnu : '+review['id'])
        if strict and any(r in roles and not roles[r]['assigned'] for r in [review['author_id'],review['reviewer_id']]):
            errors.append('Acteur de revue non affecté : '+review['id'])
        if review['mode']=='INDEPENDENT':
            if review['author_id']==review['reviewer_id'] or not review['trace_id'] or runtime['mode']!='DELEGATED':
                errors.append('Indépendance déclarée incohérente : '+review['id'])
            if not any(ev.get(x,{}).get('kind')=='runtime' for x in review['evidence_ids']):
                errors.append('Trace runtime de revue absente : '+review['id'])
        if strict and review['verdict']!='APPROVED':
            errors.append('Revue non approuvée : '+review['id'])
    for r in state['requirements']:
        refs(r['evidence_ids'], 'exigence '+r['id'])
    for g in state['gates']:
        refs(g['evidence_ids'], 'gate '+g['id'])
    refs(state['live_evidence_ids'], 'production')
    if strict:
        for topic in ['idees','architecture','roadmap','production_pilote']:
            choices = [r for r in state['reviews'] if r['topic']==topic and r['verdict']=='APPROVED']
            if runtime['independent_review_required']:
                choices = [r for r in choices if r['mode']=='INDEPENDENT']
            if not choices:
                errors.append('Confrontation approuvée absente : '+topic)
        reqs = {r['id']:r for r in state['requirements']}
        errors.extend('Exigence obligatoire non représentée : '+rid for rid in requirements.keys()-reqs.keys())
        for r in state['requirements']:
            refs(r['evidence_ids'], 'exigence '+r['id'], r['status']=='VERIFIE')
            if r['status']=='NON_APPLICABLE':
                decision = decisions.get(r['decision_id'])
                if not requirements.get(r['id'],{}).get('allow_not_applicable') or not decision or decision['status']!='RESOLVED' or decision['scope']!=r['id']:
                    errors.append('Dérogation interdite/non décidée : '+r['id'])
            elif r['status']!='VERIFIE':
                errors.append('Exigence non vérifiée : '+r['id'])
        gates = {g['id']:g for g in state['gates']}
        for gid in [f'G{i}' for i in range(7 if stage=='release' else 6)]:
            g = gates.get(gid)
            if not g or g['status']!='APPROVED':
                errors.append('Gate non approuvé : '+gid)
            elif g:
                refs(g['evidence_ids'], 'gate '+gid, True)
        if stage=='release':
            if not state['permissions']['publication']:
                errors.append('Publication non autorisée')
            refs(state['live_evidence_ids'],'production',True)
            if not any(ev.get(x,{}).get('kind') == 'authorization' for x in state['live_evidence_ids']):
                errors.append('Aucune preuve de permission de publication déclarée')
            if not any(ev.get(x,{}).get('kind') in {'browser','http'} for x in state['live_evidence_ids']):
                errors.append('Aucune preuve live navigateur/HTTP déclarée')
    else:
        warnings.append('DRAFT : la formation, les livrables complets et les gates ne sont pas exigés à ce stade.')
    if not state['niche'] or not state['site_type']:
        errors.append('Niche et type de site obligatoires')
    warnings.append('Les hashes et traces déclarées ne prouvent ni vérité, ni indépendance réelle, ni qualité : revue métier et preuves de l’hôte nécessaires.')
    return {'status':'BLOQUE' if errors else 'STRUCTURE_OK','stage':stage,'errors':list(dict.fromkeys(errors)),
            'warnings':warnings, 'counts':{k:len(state[k]) for k in ['requirements','pages','links','artifacts','reviews']}}


def file_signature(root: Path, exclude: set[str] | None = None) -> dict[str,str]:
    result = {}
    exclude = exclude or set()
    for folder, dirs, files in os.walk(root, followlinks=False):
        for d in list(dirs):
            if (Path(folder)/d).is_symlink():
                raise ValueError('Lien symbolique dans le package')
            if d in SKIP_DIRS:
                dirs.remove(d)
        for filename in files:
            p = Path(folder)/filename
            if p.is_symlink():
                raise ValueError('Lien symbolique dans le package')
            rel = p.relative_to(root).as_posix()
            if rel in exclude or p.suffix == '.pyc':
                continue
            result[rel] = digest(p)
    return dict(sorted(result.items()))


def check_package(root: Path) -> dict:
    manifest_path = safe_path(root, 'MANIFEST.sha256.json', True)
    expected = load(manifest_path)
    if not isinstance(expected,dict) or not all(isinstance(k,str) and isinstance(v,str) and HASH.fullmatch(v) for k,v in expected.items()):
        raise ValueError('Manifeste de package invalide')
    for name in expected:
        safe_path(root,name)
    actual = file_signature(root, {'MANIFEST.sha256.json'})
    package_errors=[]
    if 'SKILL.md' not in actual:
        package_errors.append('SKILL.md obligatoire absent')
    else:
        text=(root/'SKILL.md').read_text(encoding='utf-8-sig')
        if not re.match(r'^---\s*\n',text) or not re.search(r'^name:\s*[\"\']?seo-studio-2[\"\']?\s*$',text,re.M) or not re.search(r'^description:\s*\S',text,re.M):
            package_errors.append('Frontmatter du skill invalide')
    errors = ['fichier absent : '+p for p in expected.keys()-actual.keys()]
    errors += ['fichier non déclaré : '+p for p in actual.keys()-expected.keys()]
    errors += ['empreinte différente : '+p for p in actual.keys() & expected.keys() if actual[p]!=expected[p]]
    errors=package_errors+errors
    return {'status':'BLOQUE' if errors else 'PACKAGE_INTEGRITY_OK','errors':errors,'files':len(actual)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command',required=True)
    p = sub.add_parser('inventory'); p.add_argument('--root',type=Path,action='append',required=True)
    p = sub.add_parser('init'); p.add_argument('--project',type=Path,required=True);p.add_argument('--niche',required=True);p.add_argument('--site-type',required=True);p.add_argument('--apply',action='store_true')
    p = sub.add_parser('validate');p.add_argument('project',type=Path);p.add_argument('--stage',choices=['draft','handoff','release'],default='draft')
    p = sub.add_parser('snapshot');p.add_argument('project',type=Path)
    p = sub.add_parser('check-package');p.add_argument('package',type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command=='inventory': result=inventory(args.root)
        elif args.command=='init': result=init_project(args.project,args.niche,args.site_type,args.apply)
        elif args.command=='validate': result=validate_project(args.project,args.stage)
        elif args.command=='snapshot': result=review_snapshot(args.project)
        else: result=check_package(args.package)
        print(json_text(result),end='')
        return 2 if result.get('status')=='BLOQUE' else 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json_text({'status':'BLOQUE','error':str(exc)}),end='')
        return 2

if __name__=='__main__':
    sys.exit(main())
