"""Compare two explicit SEO snapshots offline; no network or publication side effects."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit


def load(path):
    data = json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if not isinstance(data, dict) or data.get('version') != 1 or not isinstance(data.get('pages'), list) or not data['pages'] or not isinstance(data.get('site_id'), str) or not data['site_id'].strip():
        raise ValueError('Expected version 1, nonempty site_id and pages array')
    pages = {}
    for page in data['pages']:
        if not isinstance(page, dict) or set(page) != {'id', 'url', 'canonical', 'noindex'}:
            raise ValueError('Every page requires exactly id, url, canonical and noindex')
        if not isinstance(page['id'], str) or not page['id'].strip() or page['id'] in pages:
            raise ValueError('Page IDs must be unique, nonempty strings')
        for key in ('url', 'canonical'):
            value = page[key]
            if key == 'canonical' and value is None: continue
            if not isinstance(value, str): raise ValueError('Invalid URL')
            parsed = urlsplit(value)
            if parsed.scheme not in ('http','https') or not parsed.hostname or parsed.username or parsed.password:
                raise ValueError('URLs must be HTTP(S) without credentials')
        if type(page['noindex']) is not bool: raise ValueError('noindex must be boolean')
        pages[page['id']] = page
    return data['site_id'], pages


def compare(before, after):
    if before[0] != after[0]: raise ValueError('Snapshot site IDs differ')
    before, after = before[1], after[1]
    changes = []
    for key in sorted(before.keys() | after.keys()):
        if key not in before: changes.append({'id': key, 'field': 'added'})
        elif key not in after: changes.append({'id': key, 'field': 'removed'})
        else:
            for field in ('url', 'canonical', 'noindex'):
                if before[key][field] != after[key][field]:
                    changes.append({'id': key, 'field': field, 'before': before[key][field], 'after': after[key][field]})
    return {'status': 'FAIL' if changes else 'PASS', 'scope': 'provided snapshots only; URL, canonical, noindex', 'changes': changes}


def main():
    p = argparse.ArgumentParser(description='Compare two authorized, manually supplied JSON snapshots. No network requests.')
    p.add_argument('before'); p.add_argument('after'); args = p.parse_args()
    try: result = compare(load(args.before), load(args.after))
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({'status':'NOT_RUN','error':str(exc)},ensure_ascii=False)); return 2
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 1 if result['status']=='FAIL' else 0

if __name__ == '__main__': raise SystemExit(main())

