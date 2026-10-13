"""Données de tests entièrement fictives ; aucun réseau ou agent n'est exécuté."""
import studio
from workflow import workflow_digest


def complete_workflow(project, state):
    def write(path, content):
        p = project / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding='utf-8')

    def proof(eid, kind, path=None):
        path = path or 'TRACES/' + eid + '.txt'
        if not (project / path).is_file():
            write(path, 'FIXTURE FICTIVE uniquement : aucun appel runtime, agent ou source réel.\n')
        state['evidence'].append({'id': eid, 'path': path, 'sha256': studio.digest(project / path),
                                  'kind': kind, 'origin': 'FIXTURE FICTIVE, test de structure seulement'})
        return eid

    wf = studio.load(studio.ROOT / 'templates/workflow.json')
    wf.update(run_id=state['run_id'], niche=state['niche'], brief_version=state['brief_version'],
              preproduction_started_sequence=12)
    for step, seq in zip(wf['steps'], [1, 2, 6, 11]):
        step.update(status='DONE', sequence=seq, evidence_ids=['review'])
    source_ids = []
    for platform, domain in [('LINKEDIN', 'linkedin.com'), ('REDDIT', 'reddit.com')]:
        sid = 'fiction-' + platform
        eid = proof(sid, 'source')
        source_ids.append(sid)
        state['sources'].append({'id': sid, 'url': 'https://www.' + domain + '/fiction-test-only',
                                'status': 'OBSERVED', 'consulted_at': '2026-10-13',
                                'note': 'Lecture fictive pour tests uniquement', 'evidence_id': eid})
        next(p for p in wf['research']['platforms'] if p['platform'] == platform).update(
            status='READ', queries=['requête fictive méthodes', 'requête fictive limites'],
            source_ids=[sid], evidence_ids=[eid], attempted_at='2026-10-13')
    for role in state['roles']:
        if not role['assigned']:
            continue
        rid = role['id']
        cid = 'skill-' + rid
        wf['competencies'].append({'id': cid, 'role_ids': [rid], 'label': 'Compétence fictive',
                                  'domain_application': 'Appliquer au choix du lecteur fictif',
                                  'source_ids': source_ids.copy(), 'confidence': 'INFERENCE',
                                  'behavior': 'Distinguer source et hypothèse', 'calibration_case': 'Fiche sans essai'})
        path = 'PERSONAS/' + rid + '.md'
        write(path, '# Profil fictif\n\nFixture de contrat ; aucun modèle formé ni chargé.\n')
        wf['profiles'].append({'role_id': rid, 'niche': state['niche'], 'version': '1',
                               'profile_path': path, 'sha256': studio.digest(project / path),
                               'competency_ids': [cid], 'training_evidence_ids': ['training'],
                               'calibration_evidence_ids': ['test_report'], 'prepared_sequence': 3, 'status': 'VERIFIED'})
    for rid, seq, close in [('TERRA', 4, 25), ('QA_LEAD', 5, 26)]:
        p = next(p for p in wf['profiles'] if p['role_id'] == rid)
        spawn_id = proof('spawn-' + rid, 'runtime')
        return_id = proof('return-' + rid, 'runtime')
        mandate = studio.load(studio.ROOT / 'templates/mandate.json')
        mandate.update(run_id=state['run_id'], brief_version=state['brief_version'], role_id=rid,
                       niche=state['niche'], persona_path=p['profile_path'], persona_sha256=p['sha256'],
                       persona_version=p['version'], competency_ids=p['competency_ids'],
                       persona_loading_instruction='Lire le profil fictif, pour tests de structure seulement')
        path = 'MANDATS/' + rid + '.json'
        write(path, studio.json_text(mandate))
        wf['delegates'].append({'id': 'fiction-agent-' + rid, 'role_id': rid, 'profile_sha256': p['sha256'],
                                'brief_version': state['brief_version'], 'mandate_path': path,
                                'mandate_sha256': studio.digest(project / path),
                                'spawn_evidence_id': spawn_id, 'persona_load_evidence_id': spawn_id,
                                'return_evidence_ids': [return_id], 'started_sequence': seq,
                                'loaded_sequence': seq, 'closed_sequence': close, 'status': 'RETURNED'})
    reviewed_paths = {'idees': '02_POSITIONNEMENT.md', 'architecture': '03_ARCHITECTURE.md',
                      'production_pilote': 'PILOTES/pilote-0.md', 'roadmap': '09_ROADMAP.md'}
    reviewer = wf['delegates'][1]
    for n, topic in enumerate(['idees', 'architecture', 'production_pilote', 'roadmap']):
        seq = [7, 13, 17, 21][n]
        prop = 'PROPOSITIONS/' + topic + '-v1.md'
        write(prop, '# Proposition fictive antérieure\n\nContrat structurel uniquement.\n')
        critique = proof('critique-' + topic, 'review')
        resolution = proof('resolution-' + topic, 'artifact')
        recheck = proof('recheck-' + topic, 'review')
        reviewer['return_evidence_ids'] += [critique, recheck]
        path = reviewed_paths[topic]
        wf['iterations'].append({'id': 'cycle-' + topic, 'topic': topic, 'cycle': 1,
                                 'author_id': 'TERRA', 'reviewer_delegate_id': reviewer['id'],
                                 'proposal': {'path': prop, 'sha256': studio.digest(project / prop)},
                                 'reviewed': {'path': path, 'sha256': studio.digest(project / path)},
                                 'critique_evidence_id': critique, 'resolution_evidence_id': resolution,
                                 'recheck_evidence_id': recheck, 'proposal_sequence': seq,
                                 'critique_sequence': seq + 1, 'resolution_sequence': seq + 2,
                                 'recheck_sequence': seq + 3, 'status': 'PASSED'})
        r = next(r for r in state['reviews'] if r['topic'] == topic)
        r.update(trace_id=reviewer['id'], evidence_ids=['runtime', recheck])
    write('workflow.json', studio.json_text(wf))
    for review in state['reviews']:
        review['workflow_inputs_sha256'] = workflow_digest(wf, state['evidence'])
    return wf
