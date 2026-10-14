"""Personna/Studio offline contract integration; fixtures never prove model behavior."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import studio
import personna_evaluate as evaluator
from personna_fixture import evaluation_fixture
from test_studio import fixture
from workflow import validate_workflow


class PersonnaIntegration(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / 'project'
        self.state = fixture(self.project)
        self.wf = studio.load(self.project / 'workflow.json')
        self.profile = self.wf['profiles'][0]
        self.evaluation = self.profile['evaluation']

    def check(self, strict=True):
        (self.project / 'workflow.json').write_text(studio.json_text(self.wf), encoding='utf-8')
        return validate_workflow(self.project, self.state, strict, load=studio.load, shape=studio.shape,
                                 safe_path=studio.safe_path, digest=studio.digest, root=ROOT)

    def test_current_full_records_pass(self):
        self.assertEqual(self.check()[0], [])

    def test_missing_evaluation_blocks_strict(self):
        del self.profile['evaluation']
        self.assertTrue(any('évaluation Personna' in e for e in self.check()[0]))
        errors, warnings = self.check(False)
        self.assertFalse(any('évaluation Personna' in e for e in errors))
        self.assertTrue(any('évaluation Personna' in e for e in warnings))

    def test_changed_profile_requires_new_sessions(self):
        profile = self.project / self.profile['profile_path']
        profile.write_text('Changed synthetic persona', encoding='utf-8')
        self.profile['sha256'] = studio.digest(profile)
        self.assertTrue(any('évaluation Personna' in e and 'STALE' in e for e in self.check()[0]))

    def test_status_only_certificate_refused(self):
        report = self.project / self.evaluation['report_path']
        report.write_text('{"status":"PASS"}', encoding='utf-8')
        self.assertTrue(any('Rapport différent' in e for e in self.check()[0]))

    def test_mutated_request_even_rehashed_refused(self):
        run = self.project / self.evaluation['run_path']
        manifest = evaluator.read_json(run / 'manifest.json')
        key = next(iter(manifest['requests']))
        request = run / 'requests' / (key + '.json')
        data = evaluator.read_json(request)
        data['task'] = 'Different task'
        request.write_text(studio.json_text(data), encoding='utf-8')
        manifest['requests'][key] = evaluator.digest(request)
        (run / 'manifest.json').write_text(studio.json_text(manifest), encoding='utf-8')
        self.assertTrue(any('évaluation Personna' in e for e in self.check()[0]))

    def test_changed_provenance_refused(self):
        run = self.project / self.evaluation['run_path']
        record = next((run / 'records').glob('*.json'))
        data = evaluator.read_json(record)
        data['session_id'] = 'new-synthetic-id'
        record.write_text(studio.json_text(data), encoding='utf-8')
        self.assertTrue(any('évaluation Personna' in e for e in self.check()[0]))

    def test_old_review_on_new_run_refused(self):
        run = self.project / self.evaluation['run_path']
        manifest = evaluator.read_json(run / 'manifest.json')
        manifest['run_id'] = 'different-run'
        (run / 'manifest.json').write_text(studio.json_text(manifest), encoding='utf-8')
        self.assertTrue(any('évaluation Personna' in e for e in self.check()[0]))

    def test_path_escape_refused(self):
        self.evaluation['run_path'] = '../external'
        self.assertTrue(any('évaluation Personna' in e for e in self.check()[0]))

    def test_malformed_suite_controlled(self):
        suite = self.project / self.evaluation['suite_path']
        suite.write_text('[]', encoding='utf-8')
        self.assertTrue(any('évaluation Personna' in e for e in self.check()[0]))

    def test_invalid_regex_controlled(self):
        suite = self.project / self.evaluation['suite_path']
        data = studio.load(suite)
        data['cases'][0]['criteria'].append({'id': 'bad', 'kind': 'regex', 'description': 'Invalid synthetic expression', 'pattern': '['})
        suite.write_text(studio.json_text(data), encoding='utf-8')
        self.assertTrue(any('évaluation Personna' in e for e in self.check()[0]))

    def test_vendored_evaluator_matches_sibling_release(self):
        sibling = ROOT.parent / 'personna/scripts/evaluate.py'
        if not sibling.is_file():
            self.skipTest('Source sibling absent in standalone installation; package manifest verifies vendored bytes')
        self.assertEqual((ROOT / 'scripts/personna_evaluate.py').read_bytes(), sibling.read_bytes())


if __name__ == '__main__':
    unittest.main()
