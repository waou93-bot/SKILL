#!/usr/bin/env python3
"""Executable preparation/import/evaluation protocol. Does not launch a model.

Words are whitespace-separated units, not tokens. All imported traces must come
from real, isolated host sessions; their authenticity requires human review.
"""
import argparse
import hashlib
import json
import re
import uuid
from pathlib import Path

VARIANTS = ('without_persona', 'with_persona')


def safe_file(path):
    p = Path(path).absolute()
    if any(x.is_symlink() for x in (p, *p.parents)):
        raise ValueError('Symlink refused: ' + str(p))
    if not p.is_file():
        raise ValueError('Missing file: ' + str(p))
    return p


def digest(path):
    return hashlib.sha256(safe_file(path).read_bytes()).hexdigest()


def unique_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError('Duplicate JSON key: ' + key)
        obj[key] = value
    return obj


def read_json(path):
    return json.loads(safe_file(path).read_text(encoding='utf-8'),
                      object_pairs_hook=unique_pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError('Nonfinite JSON: ' + x)))


def write_json(path, obj):
    with Path(path).open('x', encoding='utf-8', newline='\n') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')


def identifier(value):
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}', value):
        raise ValueError('Unsafe or empty identifier')
    return value


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def object_value(value, label):
    if not isinstance(value, dict):
        raise ValueError(label + ' must be an object')
    return value


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode('utf-8')).hexdigest()


def expected_request(manifest, spec, source, case, variant):
    request = {'run_id': manifest['run_id'], 'persona_sha256': manifest['persona_sha256'],
               'suite_sha256': manifest['suite_sha256'], 'case_id': case['id'], 'variant': variant,
               'common_context': spec['common_context'], 'task': case['task'],
               'session_requirement': 'fresh isolated session; same model/settings across pair'}
    if variant == 'with_persona':
        request['persona'] = source
    return request


def review_context(manifest, rec):
    return {k: manifest[k] for k in ('run_id', 'persona_sha256', 'suite_sha256')} | {
        k: rec[k] for k in ('case_id', 'variant', 'input_sha256', 'response_sha256', 'trace_sha256')} | {
        'record_sha256': canonical_hash(rec)}


def validate_suite(suite):
    object_value(suite, 'Suite')
    if suite.get('schema_version') != '1' or not nonempty(suite.get('common_context')):
        raise ValueError('Invalid suite version/context')
    cases = suite.get('cases')
    if not isinstance(cases, list):
        raise ValueError('Cases must be a list')
    seen, real, adversaries = set(), 0, []
    for case in cases:
        object_value(case, 'Case')
        cid = identifier(case.get('id'))
        if cid in seen:
            raise ValueError('Duplicate case')
        seen.add(cid)
        if not nonempty(case.get('task')):
            raise ValueError('Empty task')
        if case.get('kind') == 'real':
            real += 1
        elif case.get('kind') == 'adversarial':
            adversaries.append(case.get('adversary'))
        else:
            raise ValueError('Invalid case kind')
        criteria = case.get('criteria')
        if not isinstance(criteria, list) or not criteria:
            raise ValueError('Criteria required')
        ids = set()
        for criterion in criteria:
            object_value(criterion, 'Criterion')
            ident = identifier(criterion.get('id'))
            if ident in ids or not nonempty(criterion.get('description')):
                raise ValueError('Invalid criterion')
            ids.add(ident)
            if criterion.get('kind') == 'regex':
                if not nonempty(criterion.get('pattern')):
                    raise ValueError('Regex pattern required')
                re.compile(criterion['pattern'])
            elif criterion.get('kind') != 'review':
                raise ValueError('Invalid criterion kind')
        if not any(c['kind'] == 'review' for c in criteria):
            raise ValueError('Every case requires substantive human review')
    if real not in (2, 3) or sorted(adversaries) != ['injection', 'instruction_conflict', 'permission_denied']:
        raise ValueError('Require 2-3 real cases and exactly the three adversaries')
    if re.search(r'A_COMPLETER|\[À COMPLÉTER\]', '\n'.join([suite['common_context']] + [c['task'] for c in cases]), re.I):
        raise ValueError('Replace task/context placeholders before preparing')
    return suite


def checked_run(path):
    root = Path(path).absolute()
    if any(p.is_symlink() for p in (root, *root.parents)) or not root.is_dir():
        raise ValueError('Invalid run directory')
    if any(p.is_symlink() for p in root.rglob('*')):
        raise ValueError('Symlink inside run')
    return root


def prepare(persona, suite, out, max_words=1200):
    source = safe_file(persona).read_text(encoding='utf-8')
    if max_words <= 0 or not source.strip() or len(source.split()) > max_words:
        raise ValueError('Persona exceeds word budget or is empty')
    spec = validate_suite(read_json(suite))
    root = Path(out).absolute()
    if root.exists() or any(p.is_symlink() for p in root.parents):
        raise ValueError('Output exists or parent is a symlink')
    root.mkdir(parents=True)
    (root / 'requests').mkdir()
    (root / 'records').mkdir()
    (root / 'persona.txt').write_bytes(safe_file(persona).read_bytes())
    (root / 'suite.json').write_bytes(safe_file(suite).read_bytes())
    manifest = {'schema_version': '2', 'run_id': uuid.uuid4().hex, 'persona_sha256': digest(persona), 'suite_sha256': digest(suite),
                'word_count': len(source.split()), 'max_words': max_words, 'requests': {}}
    for case in spec['cases']:
        for variant in VARIANTS:
            key = case['id'] + '-' + variant
            request = expected_request(manifest, spec, source, case, variant)
            path = root / 'requests' / (key + '.json')
            write_json(path, request)
            manifest['requests'][key] = digest(path)
    write_json(root / 'manifest.json', manifest)
    return manifest


def record(run, case, variant, response, trace, session_id, model):
    root = checked_run(run)
    identifier(case)
    if variant not in VARIANTS or not nonempty(session_id) or not nonempty(model):
        raise ValueError('Variant/session/model required')
    manifest = object_value(read_json(root / 'manifest.json'), 'Manifest')
    if manifest.get('schema_version') != '2':
        raise ValueError('Legacy run: prepare fresh schema 2 sessions')
    identifier(manifest.get('run_id'))
    object_value(manifest.get('requests'), 'Manifest requests')
    key = case + '-' + variant
    expected = manifest['requests'].get(key)
    if expected is None or digest(root / 'requests' / (key + '.json')) != expected:
        raise ValueError('Unknown or stale request')
    for p in (response, trace):
        if not safe_file(p).read_text(encoding='utf-8').strip():
            raise ValueError('Response and trace must be nonempty UTF-8 files')
    envelope = object_value(read_json(trace), 'Execution trace')
    binding = {'schema_version': '2', 'run_id': manifest['run_id'], 'case_id': case, 'variant': variant,
               'input_sha256': expected, 'session_id': session_id, 'model': model, 'response_sha256': digest(response)}
    if any(envelope.get(k) != value for k, value in binding.items()) or not nonempty(envelope.get('host_trace')):
        raise ValueError('Trace execution context does not match observed request/session/response')
    # Prevent partial overwrites by checking every destination before copying.
    targets = [root / 'records' / (key + suffix) for suffix in ('.response.txt', '.trace.txt', '.json')]
    if any(p.exists() for p in targets):
        raise ValueError('Record exists')
    for src, dst in zip((response, trace), targets):
        with dst.open('xb') as f:
            f.write(safe_file(src).read_bytes())
    result = {'case_id': case, 'variant': variant, 'session_id': session_id, 'model': model,
              'input_sha256': expected, 'response_sha256': digest(targets[0]), 'trace_sha256': digest(targets[1])}
    write_json(targets[2], result)
    return result


def grade(persona, suite, run, reviews=None):
    root = checked_run(run)
    manifest = object_value(read_json(root / 'manifest.json'), 'Manifest')
    if manifest.get('schema_version') != '2':
        raise ValueError('Legacy run: prepare fresh schema 2 sessions')
    identifier(manifest.get('run_id'))
    object_value(manifest.get('requests'), 'Manifest requests')
    spec = validate_suite(read_json(root / 'suite.json'))
    review_data = object_value(read_json(reviews), 'Reviews') if reviews else {}
    for key, review in review_data.items():
        object_value(review, 'Review ' + key)
        if not isinstance(review.get('criteria', []), list):
            raise ValueError('Review criteria must be a list')
        for criterion in review.get('criteria', []):
            object_value(criterion, 'Review criterion')
    stale = (manifest.get('schema_version') != '2' or digest(persona) != manifest['persona_sha256']
             or digest(suite) != manifest['suite_sha256'] or digest(root / 'persona.txt') != manifest['persona_sha256']
             or digest(root / 'suite.json') != manifest['suite_sha256'])
    source = (root / 'persona.txt').read_text(encoding='utf-8')
    count = len(source.split())
    if type(manifest.get('max_words')) is not int or manifest['max_words'] <= 0:
        raise ValueError('Invalid manifest word budget')
    stale = stale or not source.strip() or count > manifest['max_words'] or type(manifest.get('word_count')) is not int or manifest['word_count'] != count
    expected_keys = {case['id'] + '-' + variant for case in spec['cases'] for variant in VARIANTS}
    stale = stale or set(manifest['requests']) != expected_keys
    results = {}
    sessions = set()
    for case in spec['cases']:
        for variant in VARIANTS:
            key = case['id'] + '-' + variant
            item = {'status': 'NOT_RUN', 'criteria': []}
            results[key] = item
            req = root / 'requests' / (key + '.json')
            if (stale or not req.exists() or digest(req) != manifest['requests'].get(key)
                    or read_json(req) != expected_request(manifest, spec, source, case, variant)):
                item['status'] = 'STALE'
                continue
            paths = [root / 'records' / (key + s) for s in ('.json', '.response.txt', '.trace.txt')]
            if not all(p.exists() for p in paths):
                item['reason'] = 'BLOCKED: missing real response, trace or record'
                continue
            rec = object_value(read_json(paths[0]), 'Record')
            if (rec.get('input_sha256') != manifest['requests'][key] or rec.get('response_sha256') != digest(paths[1])
                    or rec.get('trace_sha256') != digest(paths[2]) or rec.get('case_id') != case['id'] or rec.get('variant') != variant):
                item['status'] = 'STALE'
                continue
            envelope = object_value(read_json(paths[2]), 'Execution trace')
            binding = {'schema_version': '2', 'run_id': manifest['run_id'], **{k: rec[k] for k in ('case_id', 'variant', 'input_sha256', 'session_id', 'model', 'response_sha256')}}
            if any(envelope.get(k) != value for k, value in binding.items()) or not nonempty(envelope.get('host_trace')):
                item['status'] = 'STALE'
                item['reason'] = 'Execution trace context mismatch'
                continue
            session = rec.get('session_id')
            if not nonempty(session) or session in sessions or not nonempty(rec.get('model')):
                item['status'] = 'FAIL'
                item['reason'] = 'Missing provenance or reused session'
                continue
            sessions.add(session)
            response = paths[1].read_text(encoding='utf-8')
            review = review_data.get(key, {})
            if review and (review.get('context') != review_context(manifest, rec) or review.get('response_sha256') != rec['response_sha256']
                           or review.get('trace_sha256') != rec['trace_sha256']):
                item['status'] = 'STALE'
                item['reason'] = 'Review hashes do not match the current response/trace'
                continue
            item['context'] = review_context(manifest, rec)
            verified = (review.get('context') == item['context'] and nonempty(review.get('reviewer')) and review.get('response_sha256') == rec['response_sha256']
                        and review.get('trace_sha256') == rec['trace_sha256'])
            listed = review.get('criteria', [])
            review_ids = [c.get('id') for c in listed if isinstance(c, dict)] if isinstance(listed, list) else []
            reviewed = {c['id']: c for c in listed} if isinstance(listed, list) and len(review_ids) == len(set(review_ids)) and len(review_ids) == len(listed) else {}
            for c in case['criteria']:
                if c['kind'] == 'regex':
                    status = 'PASS' if re.search(c['pattern'], response) else 'FAIL'
                else:
                    entry = reviewed.get(c['id'], {})
                    status = ('PASS' if entry['passed'] else 'FAIL') if verified and type(entry.get('passed')) is bool and nonempty(entry.get('evidence')) else 'UNREVIEWED'
                item['criteria'].append({'id': c['id'], 'status': status})
            statuses = [c['status'] for c in item['criteria']]
            item['status'] = 'FAIL' if 'FAIL' in statuses else ('UNREVIEWED' if 'UNREVIEWED' in statuses else 'PASS')
            item['model'] = rec['model']
    for case in spec['cases']:
        pair = [results[case['id'] + '-' + v] for v in VARIANTS]
        if all('model' in item for item in pair) and pair[0]['model'] != pair[1]['model']:
            for item in pair:
                item['status'] = 'FAIL'
                item['reason'] = 'Baseline comparison requires the same declared model'
    statuses = [v['status'] for v in results.values()]
    overall = next((s for s in ('STALE', 'FAIL', 'NOT_RUN', 'UNREVIEWED') if s in statuses), 'PASS')
    return {'schema_version': '2', 'run_id': manifest['run_id'], 'persona_sha256': manifest['persona_sha256'], 'suite_sha256': manifest['suite_sha256'], 'status': overall, 'results': results,
            'comparison': [{'case_id': c['id'], **{v: results[c['id'] + '-' + v]['status'] for v in VARIANTS}} for c in spec['cases']],
            'interpretation': 'Paired statuses only. No inferred persona benefit or aggregate rate; human evidence remains necessary.',
            'reviews_sha256': digest(reviews) if reviews else None}


def verify_evaluation(persona, suite, run, reviews=None):
    return grade(persona, suite, run, reviews)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare')
    for arg in ('persona', 'suite', 'out'):
        p.add_argument('--' + arg, required=True)
    p.add_argument('--max-words', type=int, default=1200)
    p = sub.add_parser('record')
    for arg in ('run', 'case', 'variant', 'response', 'trace', 'session-id', 'model'):
        p.add_argument('--' + arg, required=True)
    p = sub.add_parser('grade')
    for arg in ('persona', 'suite', 'run'):
        p.add_argument('--' + arg, required=True)
    p.add_argument('--reviews')
    p.add_argument('--output', help='New JSON file; existing file is never overwritten')
    args = vars(parser.parse_args())
    command = args.pop('command')
    output = args.pop('output', None)
    try:
        result = globals()[command](**args)
        if output:
            write_json(output, result)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if command != 'grade' or result['status'] == 'PASS' else 1
    except (ValueError, OSError, KeyError, TypeError, re.error) as error:
        parser.exit(2, 'BLOCKED: ' + str(error) + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
