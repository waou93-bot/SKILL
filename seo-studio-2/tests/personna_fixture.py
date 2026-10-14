"""Synthetic contract records. No agent, source or model execution is claimed."""
import json
import personna_evaluate as evaluator


def evaluation_fixture(project, profile, role):
    base = project / 'EVALUATIONS' / role
    base.mkdir(parents=True)
    cases = [{'id': 'B' + str(n), 'kind': 'real', 'task': 'Synthetic document task ' + str(n)} for n in (1, 2)]
    cases += [{'id': 'A' + str(n), 'kind': 'adversarial', 'adversary': name, 'task': 'Synthetic adversarial task ' + name}
              for n, name in enumerate(['injection', 'instruction_conflict', 'permission_denied'], 1)]
    for case in cases:
        case['criteria'] = [{'id': 'review', 'kind': 'review', 'description': 'Synthetic fixture expectation'}]
    def save(path, obj):
        path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    suite = base / 'suite.json'
    save(suite, {'schema_version': '1', 'common_context': 'SYNTHETIC FIXTURE ONLY, no behavioral evidence.', 'cases': cases})
    run = base / 'run'
    manifest = evaluator.prepare(profile, suite, run)
    reviews = {}
    for case in cases:
        for variant in evaluator.VARIANTS:
            key = case['id'] + '-' + variant
            response = base / (key + '.txt')
            response.write_text('SYNTHETIC contract response only', encoding='utf-8')
            trace = base / (key + '-trace.json')
            session = 'synthetic-' + role + '-' + key
            save(trace, {'schema_version': '2', 'run_id': manifest['run_id'], 'case_id': case['id'], 'variant': variant,
                         'input_sha256': manifest['requests'][key], 'session_id': session, 'model': 'synthetic-test-model',
                         'response_sha256': evaluator.digest(response), 'host_trace': 'Synthetic trace; no actual agent execution.'})
            evaluator.record(run, case['id'], variant, response, trace, session, 'synthetic-test-model')
            record = evaluator.read_json(run / 'records' / (key + '.json'))
            reviews[key] = {'context': evaluator.review_context(manifest, record), 'reviewer': 'synthetic reviewer',
                            'response_sha256': record['response_sha256'], 'trace_sha256': record['trace_sha256'],
                            'criteria': [{'id': 'review', 'passed': True, 'evidence': 'Synthetic fixture assertion only'}]}
    review_path = base / 'reviews.json'
    save(review_path, reviews)
    report = base / 'report.json'
    save(report, evaluator.grade(profile, suite, run, review_path))
    return {key: path.relative_to(project).as_posix() for key, path in
            [('suite_path', suite), ('run_path', run), ('reviews_path', review_path), ('report_path', report)]}
