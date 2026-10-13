"""Cas adverses du nouveau contrat ; données fictives, pas une orchestration réelle."""
import copy
from pathlib import Path
import tempfile
import unittest
from test_studio import fixture, write
import studio


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.project = Path(self.tmp.name) / 'project'
        self.state = fixture(self.project)
        self.wf = studio.load(self.project / 'workflow.json')

    def tearDown(self):
        self.tmp.cleanup()

    def result(self, stage='handoff'):
        write(self.project / 'workflow.json', studio.json_text(self.wf))
        write(self.project / 'state.json', studio.json_text(self.state))
        return studio.validate_project(self.project, stage)

    def blocked(self, needle):
        result = self.result()
        self.assertEqual(result['status'], 'BLOQUE', result)
        self.assertTrue(any(needle in e for e in result['errors']), result['errors'])

    def test_complete_fixture_is_only_structurally_valid(self):
        self.assertEqual(self.result()['status'], 'STRUCTURE_OK')

    def test_initialization_never_fabricates_execution(self):
        p = Path(self.tmp.name) / 'new'
        studio.init_project(p, 'audio fictif', 'média', True)
        w = studio.load(p / 'workflow.json')
        self.assertTrue(all(s['status'] == 'PLANNED' for s in w['steps']))
        self.assertFalse(w['delegates'])
        self.assertFalse(w['profiles'])
        self.assertFalse(w['competencies'])
        self.assertIsNone(w['preproduction_started_sequence'])
        self.assertEqual(studio.validate_project(p)['status'], 'STRUCTURE_OK')
        self.assertEqual(studio.validate_project(p, 'handoff')['status'], 'BLOQUE')

    def test_legacy_draft_is_readable_handoff_is_blocked(self):
        write(self.project / 'state.json', studio.json_text(self.state))
        (self.project / 'workflow.json').unlink()
        self.assertEqual(studio.validate_project(self.project)['status'], 'STRUCTURE_OK')
        r = studio.validate_project(self.project, 'handoff')
        self.assertEqual(r['status'], 'BLOQUE')
        self.assertTrue(any('workflow.json absent' in e for e in r['errors']))

    def test_reinitialization_does_not_migrate_or_overwrite_existing_work(self):
        write(self.project / 'state.json', studio.json_text(self.state))
        (self.project / 'workflow.json').unlink()
        before = studio.digest(self.project / 'state.json')
        result = studio.init_project(self.project, self.state['niche'], self.state['site_type'], True)
        self.assertEqual(result['status'], 'EXISTS_UNCHANGED')
        self.assertEqual(before, studio.digest(self.project / 'state.json'))
        self.assertFalse((self.project / 'workflow.json').exists())

    def test_missing_reflection_step(self):
        self.wf['steps'].pop()
        self.blocked('F0–F3 doivent')

    def test_reflection_order(self):
        self.wf['steps'][1]['sequence'] = 10
        self.blocked('ordre F0–F3')

    def test_reflection_gap(self):
        self.wf['steps'][1]['status'] = 'PLANNED'
        self.blocked('avant son préalable')

    def test_preproduction_before_decision(self):
        self.wf['preproduction_started_sequence'] = 7
        self.blocked('avant la fin de réflexion')

    def test_no_automatic_transition_claim(self):
        self.wf['preproduction_started_sequence'] = None
        self.blocked('Transition vers préproduction')

    def test_decision_requires_real_ideas_cycle_first(self):
        self.wf['iterations'][0]['recheck_sequence'] = 15
        self.blocked('F3 sans cycle idées')

    def test_duplicate_platform(self):
        self.wf['research']['platforms'].append(copy.deepcopy(self.wf['research']['platforms'][0]))
        self.blocked('une seule fois')

    def test_linkedin_unavailable_is_provisional(self):
        self.wf['research']['platforms'][0]['status'] = 'UNAVAILABLE'
        self.blocked('couverture incomplète')

    def test_partial_draft_can_preserve_provisional_work(self):
        p = self.wf['research']['platforms'][0]
        p.update(status='UNAVAILABLE', source_ids=[], evidence_ids=[], limits='Accès public impossible')
        for c in self.wf['competencies']:
            c['source_ids'] = ['fiction-REDDIT']
        for profile in self.wf['profiles']:
            profile['status'] = 'PROVISIONAL'
        self.assertEqual(self.result('draft')['status'], 'STRUCTURE_OK')
        self.assertEqual(self.result()['status'], 'BLOQUE')

    def test_snippets_are_not_observed_sources(self):
        next(s for s in self.state['sources'] if s['id'] == 'fiction-REDDIT')['status'] = 'NOT_OBSERVED'
        self.blocked('source non lue')

    def test_platform_hostname_spoof(self):
        next(s for s in self.state['sources'] if s['id'] == 'fiction-LINKEDIN')['url'] = 'https://linkedin.com.evil.example/pulse/a'
        self.blocked('hors plateforme')

    def test_no_single_query_claimed_as_deep_research(self):
        self.wf['research']['platforms'][0]['queries'] = ['one']
        self.blocked('requêtes approfondies')

    def test_missing_date(self):
        self.wf['research']['platforms'][0]['attempted_at'] = None
        self.blocked('date de recherche')

    def test_platform_proof_link(self):
        self.wf['research']['platforms'][0]['evidence_ids'] = ['fiction-REDDIT']
        self.blocked('preuve de lecture non reliée')

    def test_competency_without_domain_behavior(self):
        self.wf['competencies'][0]['domain_application'] = ' '
        self.blocked('sans application/comportement')

    def test_profile_needs_both_platforms(self):
        self.wf['competencies'][0]['source_ids'] = ['fiction-LINKEDIN']
        self.blocked('LinkedIn/Reddit non intégrées')

    def test_profile_for_another_niche(self):
        self.wf['profiles'][0]['niche'] = 'another sector'
        self.blocked('rôle/niche/version')

    def test_profile_prepared_before_research(self):
        self.wf['profiles'][0]['prepared_sequence'] = 1
        self.blocked('avant recherche métier')

    def test_profile_missing_calibration(self):
        self.wf['profiles'][0]['calibration_evidence_ids'] = []
        self.blocked('calibration: preuve absente')

    def test_profile_modified(self):
        write(self.project / self.wf['profiles'][0]['profile_path'], 'changed')
        self.blocked('version modifiée')

    def test_two_actual_delegates_required(self):
        self.wf['delegates'].pop(0)
        self.blocked('Au moins deux vrais sous-agents')

    def test_agent_created_without_runtime(self):
        self.wf['delegates'][0]['spawn_evidence_id'] = 'training'
        self.blocked('création: preuve inconnue ou de mauvais type')

    def test_profile_file_without_actual_loading(self):
        d = self.wf['delegates'][0]
        mandate = studio.load(self.project / d['mandate_path'])
        mandate['persona_loading_instruction'] = ''
        write(self.project / d['mandate_path'], studio.json_text(mandate))
        self.blocked('chargement des compétences/persona absent')

    def test_malformed_mandate_fails_without_crashing(self):
        d = self.wf['delegates'][0]
        mandate = studio.load(self.project / d['mandate_path'])
        mandate['persona_loading_instruction'] = ['read']
        write(self.project / d['mandate_path'], studio.json_text(mandate))
        self.blocked('chargement des compétences/persona absent')

    def test_wrong_profile_transmitted(self):
        self.wf['delegates'][0]['profile_sha256'] = 'b' * 64
        self.blocked('profil/brief transmis incohérent')

    def test_runtime_loading_trace_required(self):
        self.wf['delegates'][0]['persona_load_evidence_id'] = 'training'
        self.blocked('chargement du persona: preuve inconnue ou de mauvais type')

    def test_reload_before_recheck(self):
        self.wf['delegates'][1]['loaded_sequence'] = 20
        self.blocked('critique avant chargement du persona courant')

    def test_reload_cannot_reuse_original_spawn_proof(self):
        self.wf['delegates'][1]['loaded_sequence'] = 6
        self.blocked('nouveau chargement sans nouvelle preuve runtime')

    def test_new_load_requires_open_agent_period(self):
        self.wf['delegates'][0]['loaded_sequence'] = 30
        self.blocked('chargement après fermeture')

    def test_mandate_modified_invalidates_proof(self):
        d = self.wf['delegates'][0]
        m = studio.load(self.project / d['mandate_path'])
        m['goal'] = 'Changed mission after review'
        write(self.project / d['mandate_path'], studio.json_text(m))
        self.blocked('mandat: version modifiée')

    def test_training_evidence_changed_invalidates_review(self):
        e = next(e for e in self.state['evidence'] if e['id'] == 'training')
        e['origin'] = 'Updated provenance after review'
        self.blocked('recherche/profil/mandat modifié')

    def test_three_simultaneous_agents(self):
        d = copy.deepcopy(self.wf['delegates'][0])
        d.update(id='third', spawn_evidence_id='runtime')
        self.wf['delegates'].append(d)
        self.blocked('plus de deux actifs')

    def test_duplicate_spawn_proof(self):
        self.wf['delegates'][1]['spawn_evidence_id'] = self.wf['delegates'][0]['spawn_evidence_id']
        self.blocked('preuve de création réutilisée')

    def test_response_not_received(self):
        self.wf['delegates'][1]['return_evidence_ids'] = []
        self.blocked('relecture non reçues de cet agent')

    def test_no_substitute_self_review(self):
        self.wf['iterations'][0]['author_id'] = 'QA_LEAD'
        self.blocked('critique métier distinct absent')

    def test_correction_must_be_rechecked(self):
        it = self.wf['iterations'][0]
        it['recheck_evidence_id'] = it['critique_evidence_id']
        self.blocked('nouvelle relecture absente')

    def test_resolution_before_critique(self):
        self.wf['iterations'][0]['resolution_sequence'] = 7
        self.blocked('mauvais ordre')

    def test_architecture_before_preproduction(self):
        self.wf['iterations'][1]['proposal_sequence'] = 7
        self.blocked('préproduction avant réflexion')

    def test_stale_current_pilot_recheck(self):
        write(self.project / 'PILOTES/pilote-0.md', 'New unreviewed pilot')
        self.blocked('relecture: version modifiée')

    def test_missing_current_approval_link(self):
        self.state['reviews'][0]['trace_id'] = 'unrelated-agent'
        self.blocked('approbation courante non reliée')

    def test_new_failed_cycle_does_not_reuse_old_approval(self):
        it = copy.deepcopy(self.wf['iterations'][1])
        it.update(id='second-architecture', cycle=2, status='CHANGES_REQUIRED')
        self.wf['iterations'].append(it)
        self.blocked('Cycle complet absent : architecture')

    def test_backdated_cycle_number_cannot_restore_old_approval(self):
        self.wf['iterations'][1]['cycle'] = 2
        it = copy.deepcopy(self.wf['iterations'][1])
        it.update(id='later-refusal', cycle=1, status='CHANGES_REQUIRED', proposal_sequence=30,
                  critique_sequence=31, resolution_sequence=32, recheck_sequence=33)
        self.wf['iterations'].append(it)
        self.blocked('Chronologie des cycles incohérente')

    def test_three_separate_iteration_proofs_required(self):
        it = self.wf['iterations'][0]
        it['resolution_evidence_id'] = it['critique_evidence_id']
        self.blocked('trois preuves distinctes')

    def test_research_changed_invalidates_review(self):
        self.wf['research']['platforms'][0]['queries'].append('new query')
        self.blocked('recherche/profil/mandat modifié')

    def test_no_path_escape_in_profile(self):
        self.wf['profiles'][0]['profile_path'] = '../private.txt'
        self.blocked('Chemin interdit')

    def test_no_untyped_sequence(self):
        self.wf['steps'][0]['sequence'] = True
        self.blocked('type attendu')

    def test_snapshot_includes_context_but_does_not_approve(self):
        self.result()
        before = studio.digest(self.project / 'workflow.json')
        result = studio.review_snapshot(self.project)
        self.assertEqual(result['workflow_inputs_sha256'], studio.workflow_digest(self.wf, self.state['evidence']))
        self.assertIn('aucune revue', result['warning'])
        self.assertEqual(before, studio.digest(self.project / 'workflow.json'))


if __name__ == '__main__':
    unittest.main()
