import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('evaluate', Path(__file__).parents[1] / 'scripts/evaluate.py')
ev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev)


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=os.environ.get('PERSONNA_TEST_TMPDIR'))
        self.root = Path(self.tmp.name)
        self.persona = self.root / 'persona.md'
        self.persona.write_text('Mission courte et précise.', encoding='utf-8')
        self.suite = self.root / 'suite.json'
        self.data = {'schema_version': '1', 'common_context': 'Projet réel', 'cases': []}
        for i, adversary in enumerate([None, None, 'injection', 'instruction_conflict', 'permission_denied']):
            case = {'id': 'C' + str(i), 'kind': 'adversarial' if adversary else 'real', 'task': 'Analyser le fichier fourni',
                    'criteria': [{'id': 'text', 'description': 'Structure', 'kind': 'regex', 'pattern': 'réponse'},
                                 {'id': 'proof', 'description': 'Respect des permissions et qualité', 'kind': 'review'}]}
            if adversary:
                case['adversary'] = adversary
            self.data['cases'].append(case)
        self.save()
        self.run = self.root / 'run'

    def tearDown(self):
        self.tmp.cleanup()

    def save(self):
        self.suite.write_text(json.dumps(self.data), encoding='utf-8')

    def prepare(self):
        ev.prepare(self.persona, self.suite, self.run)

    def records(self):
        self.prepare()
        response, trace = self.root / 'response.txt', self.root / 'trace.txt'
        response.write_text('réponse valide', encoding='utf-8')
        manifest = ev.read_json(self.run / 'manifest.json')
        reviews = {}
        for case in self.data['cases']:
            for variant in ev.VARIANTS:
                key = case['id'] + '-' + variant
                trace.write_text(json.dumps({'schema_version': '2', 'run_id': manifest['run_id'], 'case_id': case['id'], 'variant': variant, 'input_sha256': manifest['requests'][key], 'session_id': key, 'model': 'INHERITED_UNVERIFIED', 'response_sha256': ev.digest(response), 'host_trace': 'Synthetic fixture, no real inference'}), encoding='utf-8')
                rec = ev.record(self.run, case['id'], variant, response, trace, key, 'INHERITED_UNVERIFIED')
                reviews[key] = {'context': ev.review_context(manifest, rec), 'reviewer': 'humain', 'response_sha256': rec['response_sha256'], 'trace_sha256': rec['trace_sha256'],
                                'criteria': [{'id': 'proof', 'passed': True, 'evidence': 'Trace et réponse examinées : critères satisfaits'}]}
        path = self.root / 'reviews.json'
        path.write_text(json.dumps(reviews), encoding='utf-8')
        return path, reviews

    def test_isolated_pair_and_no_rubric(self):
        self.prepare()
        a = ev.read_json(self.run / 'requests/C0-with_persona.json')
        b = ev.read_json(self.run / 'requests/C0-without_persona.json')
        self.assertIn('persona', a)
        self.assertNotIn('persona', b)
        self.assertNotIn('criteria', a)
        self.assertEqual(a['task'], b['task'])
        self.assertEqual(a['common_context'], b['common_context'])
        with self.assertRaises(ValueError):
            self.prepare()

    def test_budget(self):
        with self.assertRaises(ValueError):
            ev.prepare(self.persona, self.suite, self.run, 1)
        self.assertFalse(self.run.exists())

    def test_contract(self):
        for mutation in ('count', 'duplicate', 'traversal', 'placeholder', 'no_review'):
            data = json.loads(json.dumps(self.data))
            if mutation == 'count':
                data['cases'].pop()
            elif mutation == 'duplicate':
                data['cases'][1]['id'] = 'C0'
            elif mutation == 'traversal':
                data['cases'][0]['id'] = '../escape'
            elif mutation == 'placeholder':
                data['cases'][0]['task'] = '[À COMPLÉTER]'
            else:
                data['cases'][0]['criteria'].pop()
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                ev.validate_suite(data)

    def test_missing_is_blocked(self):
        self.prepare()
        report = ev.grade(self.persona, self.suite, self.run)
        self.assertEqual(report['status'], 'NOT_RUN')
        self.assertIn('BLOCKED', report['results']['C0-with_persona']['reason'])

    def test_no_reviews_cannot_pass(self):
        self.records()
        self.assertEqual(ev.grade(self.persona, self.suite, self.run)['status'], 'UNREVIEWED')

    def test_pass_and_critical_failure(self):
        path, reviews = self.records()
        self.assertEqual(ev.grade(self.persona, self.suite, self.run, path)['status'], 'PASS')
        reviews['C4-with_persona']['criteria'][0]['passed'] = False
        path.write_text(json.dumps(reviews), encoding='utf-8')
        self.assertEqual(ev.grade(self.persona, self.suite, self.run, path)['status'], 'FAIL')

    def test_review_hash_and_evidence_required(self):
        path, reviews = self.records()
        for change in ('hash', 'evidence', 'reviewer'):
            data = json.loads(json.dumps(reviews))
            item = data['C0-with_persona']
            if change == 'hash':
                item['trace_sha256'] = 'wrong'
            elif change == 'evidence':
                item['criteria'][0]['evidence'] = ''
            else:
                item['reviewer'] = ''
            path.write_text(json.dumps(data), encoding='utf-8')
            self.assertEqual(ev.grade(self.persona, self.suite, self.run, path)['status'],
                             'STALE' if change == 'hash' else 'UNREVIEWED')

    def test_source_edits_stale(self):
        self.prepare()
        for source in (self.persona, self.suite):
            original = source.read_bytes()
            source.write_bytes(original + b' ')
            self.assertEqual(ev.grade(self.persona, self.suite, self.run)['status'], 'STALE')
            source.write_bytes(original)

    def test_proof_and_request_tamper(self):
        path, _ = self.records()
        for target in (self.run / 'persona.txt', self.run / 'suite.json', self.run / 'requests/C0-with_persona.json', self.run / 'records/C0-with_persona.response.txt', self.run / 'records/C0-with_persona.trace.txt'):
            original = target.read_bytes()
            target.write_bytes(original + b' ')
            self.assertEqual(ev.grade(self.persona, self.suite, self.run, path)['status'], 'STALE')
            target.write_bytes(original)

    def test_record_overwrite_and_bad_id(self):
        self.records()
        with self.assertRaises(ValueError):
            ev.record(self.run, '../escape', 'with_persona', self.persona, self.persona, 's', 'm')
        with self.assertRaises(ValueError):
            ev.record(self.run, 'C0', 'with_persona', self.persona, self.persona, 's', 'm')

    def test_old_trace_cannot_reimport(self):
        path, reviews = self.records()
        newrun = self.root / 'newrun'
        ev.prepare(self.persona, self.suite, newrun)
        key = 'C0-with_persona'
        with self.assertRaises(ValueError):
            ev.record(newrun, 'C0', 'with_persona', self.run / 'records' / (key + '.response.txt'), self.run / 'records' / (key + '.trace.txt'), key, 'INHERITED_UNVERIFIED')

    def test_request_references_cannot_hide_task_change(self):
        path, _ = self.records()
        key = 'C0-with_persona'
        request = self.run / 'requests' / (key + '.json')
        data = ev.read_json(request)
        data['task'] = 'Different commercial task'
        request.write_text(json.dumps(data), encoding='utf-8')
        manifest_path = self.run / 'manifest.json'
        manifest = ev.read_json(manifest_path)
        manifest['requests'][key] = ev.digest(request)
        manifest_path.write_text(json.dumps(manifest), encoding='utf-8')
        self.assertEqual(ev.grade(self.persona, self.suite, self.run, path)['status'], 'STALE')

    def test_provenance_and_context_review_binding(self):
        path, reviews = self.records()
        key = 'C0-with_persona'
        recpath = self.run / 'records' / (key + '.json')
        tracepath = self.run / 'records' / (key + '.trace.txt')
        rec = ev.read_json(recpath)
        envelope = ev.read_json(tracepath)
        rec['session_id'] = envelope['session_id'] = 'changed-session'
        tracepath.write_text(json.dumps(envelope), encoding='utf-8')
        rec['trace_sha256'] = ev.digest(tracepath)
        recpath.write_text(json.dumps(rec), encoding='utf-8')
        reviews[key]['trace_sha256'] = rec['trace_sha256']
        path.write_text(json.dumps(reviews), encoding='utf-8')
        self.assertEqual(ev.grade(self.persona, self.suite, self.run, path)['status'], 'STALE')

    def test_old_review_context_rejected(self):
        path, reviews = self.records()
        reviews['C0-with_persona']['context']['run_id'] = 'old-run'
        path.write_text(json.dumps(reviews), encoding='utf-8')
        self.assertEqual(ev.grade(self.persona, self.suite, self.run, path)['status'], 'STALE')

    def test_malformed_containers_blocked(self):
        for value in (None, [], 'suite', {'schema_version': '1', 'common_context': 'x', 'cases': [None]}, {'schema_version': '1', 'common_context': 'x', 'cases': ['case']}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                ev.validate_suite(value)
        invalid = json.loads(json.dumps(self.data))
        invalid['cases'][0]['criteria'] = [None]
        with self.assertRaises(ValueError):
            ev.validate_suite(invalid)
        self.prepare()
        path = self.root / 'reviews.json'
        path.write_text('[]', encoding='utf-8')
        with self.assertRaises(ValueError):
            ev.grade(self.persona, self.suite, self.run, path)

    def test_manifest_budget_and_extra_request(self):
        self.prepare()
        path = self.run / 'manifest.json'
        original = ev.read_json(path)
        for change in ('count', 'limit', 'extra'):
            manifest = json.loads(json.dumps(original))
            if change == 'count':
                manifest['word_count'] += 1
            elif change == 'limit':
                manifest['max_words'] = 1
            else:
                manifest['requests']['unknown-with_persona'] = 'hash'
            path.write_text(json.dumps(manifest), encoding='utf-8')
            self.assertEqual(ev.grade(self.persona, self.suite, self.run)['status'], 'STALE')

    def test_ambiguous_json_refused(self):
        for content in ('{"a":1,"a":2}', '{"a":NaN}'):
            path = self.root / 'bad.json'
            path.write_text(content, encoding='utf-8')
            with self.assertRaises(ValueError):
                ev.read_json(path)


if __name__ == '__main__':
    unittest.main()
