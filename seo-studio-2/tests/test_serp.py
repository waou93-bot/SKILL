"""Synthetic contract tests; no external SERP or performance certification."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import studio
from serp import validate_serp, research_digest
from serp_fixture import complete_serp


class SerpTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.project = Path(self.tmp.name)
        self.state = {'run_id': 'fixture', 'niche': 'fixture', 'evidence': [], 'links': [],
                      'gates': [{'id': 'G2', 'status': 'APPROVED', 'evidence_ids': []},
                                {'id': 'G3', 'status': 'APPROVED', 'evidence_ids': []}],
                      'pages': [{'id': 'p', 'path': '/', 'intent_id': 'i', 'public': True,
                                 'indexable': True, 'canonical_path': '/', 'wave': 'V1', 'kind': 'editorial'}]}
        self.report = complete_serp(self.project, self.state)

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, strict=True):
        return validate_serp(self.project, self.state, strict, load=studio.load, shape=studio.shape,
                             safe_path=studio.safe_path, digest=studio.digest, root=ROOT)

    def save(self, reapprove=False):
        if reapprove:
            self.report['approval']['research_sha256'] = research_digest(self.report)
        (self.project / 'research/serp.json').write_text(studio.json_text(self.report), encoding='utf-8')

    def test_valid_unknown_metrics(self):
        errors, warnings = self.check()
        self.assertEqual([], errors)
        self.assertTrue(any('inconnu' in warning for warning in warnings))

    def test_missing_draft_warning_and_advanced_error(self):
        (self.project / 'research/serp.json').unlink()
        self.assertTrue(self.check()[0])
        for gate in self.state['gates']:
            gate['status'] = 'PLANNED'
        errors, warnings = self.check(False)
        self.assertEqual([], errors)
        self.assertTrue(warnings)

    def test_g3_requires_g2_even_draft(self):
        self.state['gates'][0]['status'] = 'PLANNED'
        self.assertTrue(any('G2 doit' in error for error in self.check(False)[0]))

    def test_architecture_mutation(self):
        self.state['pages'][0]['path'] = '/changed/'
        self.assertTrue(any('architecture modifiée' in error for error in self.check()[0]))

    def test_research_mutation(self):
        self.report['observations'][0]['format'] = 'changed'
        self.save()
        self.assertTrue(any('recherche modifiée' in error for error in self.check()[0]))

    def test_source_hash_mutation(self):
        (self.project / 'research/serp-source.txt').write_text('changed', encoding='utf-8')
        self.assertTrue(any('preuve modifiée' in error for error in self.check()[0]))

    def test_source_and_declared_hash_mutation_stale_approval(self):
        path = self.project / 'research/serp-source.txt'
        path.write_text('changed source after approval', encoding='utf-8')
        next(e for e in self.state['evidence'] if e['id'] == 'serp-source')['sha256'] = studio.digest(path)
        self.assertTrue(any('preuves sources modifiées' in error for error in self.check()[0]))

    def test_old_approval_missing_source_binding_blocked(self):
        self.report['approval'].pop('source_evidence_sha256')
        self.save()
        self.assertTrue(any('preuves sources modifiées' in error for error in self.check()[0]))

    def test_no_invented_unknown(self):
        self.report['observations'][0]['volume']['value'] = 123
        self.save(True)
        self.assertTrue(any('UNKNOWN' in error for error in self.check()[0]))

    def test_query_overlap_only_warning(self):
        page = copy.deepcopy(self.state['pages'][0]); page.update(id='q', intent_id='j', path='/q/')
        self.state['pages'].append(page)
        self.report = complete_serp(self.project, self.state)
        self.report['targets'][1]['main_query'] = self.report['targets'][0]['main_query']
        self.save(True)
        errors, warnings = self.check()
        self.assertEqual([], errors)
        self.assertTrue(any('requête partagée' in warning for warning in warnings))

    def test_duplicate_intent_owner(self):
        duplicate = copy.deepcopy(self.report['targets'][0]); duplicate['page_id'] = 'q'
        page = copy.deepcopy(self.state['pages'][0]); page['id'] = 'q'; self.state['pages'].append(page)
        self.report['targets'].append(duplicate); self.save(True)
        self.assertTrue(any('propriétaire unique' in error for error in self.check()[0]))

    def test_malformed_container_controlled(self):
        self.report['observations'] = [None]; self.save()
        self.assertTrue(any('type attendu' in error for error in self.check()[0]))

    def test_missing_intent_observation(self):
        self.report['targets'][0]['observation_ids'] = []; self.save(True)
        self.assertTrue(any('sans observation' in error for error in self.check()[0]))

    def test_generic_search_has_no_fabricated_position(self):
        self.assertIsNone(self.report['observations'][0]['position'])
        self.report['observations'][0]['position'] = 0; self.save(True)
        self.assertTrue(any('minimum' in error for error in self.check()[0]))

    def test_generic_search_cannot_be_ranked_serp(self):
        self.report['observations'][0].update(collection_method='WEB_SEARCH', position=1)
        self.save(True)
        self.assertTrue(any('position réservée' in error for error in self.check()[0]))


if __name__ == '__main__':
    unittest.main()
