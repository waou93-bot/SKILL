"""Entirely synthetic observations: no SERP collection or external claim."""
import copy
import studio
from serp import architecture_digest, research_digest, source_evidence_digest


def complete_serp(project, state):
    report = studio.load(studio.ROOT / 'templates/serp.json')
    report.update(run_id=state['run_id'], niche=state['niche'])
    report['context'].update(engine='FIXTURE fictive, pas Google', country='ZZ fixture',
                             language='langue fictive', device='fixture desktop',
                             observed_at='2026-10-14', coverage='Une observation synthétique par intention',
                             limitations=['Aucune collecte réseau, aucun classement réel'])
    for eid, kind in [('serp-source', 'source'), ('serp-review', 'review')]:
        path = 'research/' + eid + '.txt'
        target = project / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text('FIXTURE FICTIVE, aucun test terrain ni source réellement consultée.\n', encoding='utf-8')
        state['evidence'].append({'id': eid, 'kind': kind, 'path': path, 'sha256': studio.digest(target),
                                  'origin': 'FIXTURE FICTIVE uniquement'})
    unknown = {'status': 'UNKNOWN', 'value': None, 'source_url': None, 'evidence_ids': [], 'note': 'Inconnu'}
    for page in state['pages']:
        if not (page['public'] and page['indexable'] and page['wave'] == 'V1'):
            continue
        oid = 'observation-' + page['id']
        report['observations'].append({'id': oid, 'intent': page['intent_id'], 'query': 'fixture ' + page['id'],
                                      'source_url': 'https://example.org/fixture/' + page['id'], 'position': None,
                                      'collection_method': 'SOURCE_REVIEW',
                                      'intention': 'Intention fictive', 'format': 'guide', 'entities': ['fixture'],
                                      'gap': 'Apport fictif à vérifier', 'evidence_ids': ['serp-source'],
                                      'limitations': ['Fixture uniquement'], 'volume': copy.deepcopy(unknown),
                                      'difficulty': copy.deepcopy(unknown)})
        report['targets'].append({'page_id': page['id'], 'main_query': 'fixture ' + page['id'],
                                  'intent': page['intent_id'], 'target_format': 'guide', 'entities': ['fixture'],
                                  'gap': 'Réponse fictive', 'observation_ids': [oid],
                                  'success': {'metric': 'clics fictifs', 'baseline': None, 'target': None,
                                              'window': '30 jours après publication fictive',
                                              'conditions': 'Fixture ; ne prédit aucun résultat'}})
    report['approval'].update(status='APPROVED', architecture_sha256=architecture_digest(state),
                              research_sha256=research_digest(report),
                              source_evidence_sha256=source_evidence_digest(report, state['evidence']),
                              evidence_ids=['serp-review'])
    next(gate for gate in state['gates'] if gate['id'] == 'G2')['evidence_ids'].append('serp-review')
    (project / 'research/serp.json').write_text(studio.json_text(report), encoding='utf-8')
    return report
