"""Bounded GET crawl and data-only release evidence checks; no browser certification."""
import argparse
from collections import Counter, deque
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib
import json
import math
from pathlib import Path
import urllib.error
import urllib.request
from urllib.parse import urljoin, urlsplit, urldefrag
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET


def object_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(',', ':')).encode('utf-8')).hexdigest()


def site_context_digest(state):
    report_path = (state.get('technical_audit') or {}).get('report_path')
    artifacts = [a for a in state['artifacts'] if a['path'] != report_path]
    ids = {a.get('evidence_id') for a in artifacts}
    return object_digest({'run_id': state['run_id'], 'brief_version': state['brief_version'],
                          'pages': state['pages'], 'links': state['links'],
                          'technical_scope': {key: (state.get('technical_audit') or {}).get(key)
                                              for key in ('target_url', 'browser_routes', 'performance_routes', 'scope_reason')},
                          'artifacts': artifacts,
                          'evidence': sorted([e for e in state['evidence'] if e['id'] in ids], key=lambda e: e['id'])})


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.canonicals, self.ld = [], [], []
        self.title, self.description, self.h1, self.robots = '', '', [], ''
        self.capture, self.buffer = None, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag == 'link' and 'canonical' in a.get('rel', '').lower().split():
            self.canonicals.append(a.get('href', ''))
        if tag == 'meta':
            if a.get('name', '').lower() == 'description': self.description = a.get('content', '')
            if a.get('name', '').lower() == 'robots': self.robots += ',' + a.get('content', '')
        if tag in ('title', 'h1') or (tag == 'script' and a.get('type', '').lower() == 'application/ld+json'):
            self.capture, self.buffer = tag, []

    def handle_data(self, data):
        if self.capture: self.buffer.append(data)

    def handle_endtag(self, tag):
        if tag != self.capture: return
        value = ''.join(self.buffer).strip()
        if tag == 'title': self.title = value
        elif tag == 'h1': self.h1.append(value)
        elif tag == 'script': self.ld.append(value)
        self.capture = None


SUPPORTED = {'Article': ('headline',), 'BlogPosting': ('headline',),
             'BreadcrumbList': ('itemListElement',), 'Organization': ('name',),
             'Product': ('name',)}


def jsonld_checks(blocks):
    results = []
    for block in blocks:
        try: value = json.loads(block)
        except (ValueError, TypeError):
            results.append({'status': 'FAIL', 'reason': 'malformed JSON-LD'}); continue
        nodes = value if isinstance(value, list) else [value]
        for node in nodes:
            if isinstance(node, dict) and '@graph' in node:
                nodes.extend(node['@graph'] if isinstance(node['@graph'], list) else []); continue
            if not isinstance(node, dict):
                results.append({'status': 'FAIL', 'reason': 'JSON-LD node must be an object'}); continue
            types = node.get('@type', [])
            types = types if isinstance(types, list) else [types]
            if not types: results.append({'status': 'NOT_VERIFIED', 'reason': 'no supported type'})
            for kind in types:
                fields = SUPPORTED.get(kind) if isinstance(kind, str) else None
                missing = [key for key in fields or () if not node.get(key)]
                results.append({'type': kind, 'status': 'FAIL' if missing else 'PASS' if fields else 'NOT_VERIFIED',
                                'missing': missing, 'scope': 'syntax and minimal fields only; rich-result eligibility not certified'})
    return results


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs): return None


def audit(base_url, max_pages=200, timeout=10, depth_budget=20, allow_remote=False):
    """Fetch same-origin HTML, robots and sitemap. External redirects are recorded, never followed."""
    u = urlsplit(base_url)
    if u.scheme not in ('http', 'https') or not u.hostname or u.username or u.password:
        raise ValueError('explicit HTTP(S) target without credentials required')
    if not allow_remote and u.hostname not in ('localhost', '127.0.0.1', '::1'):
        raise ValueError('remote target requires explicit allow_remote authorization')
    if not 1 <= max_pages or not 0 < timeout <= 120 or not 0 <= depth_budget <= 30:
        raise ValueError('invalid bounded crawl limits')
    origin = (u.scheme, u.hostname, u.port)
    root = f'{u.scheme}://{u.netloc}/'
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    errors, warnings, pages = [], [], []
    def same(url):
        p = urlsplit(url)
        return (p.scheme, p.hostname, p.port) == origin and not p.username and not p.password
    def fetch(url):
        chain = []
        for _ in range(11):
            try: response = opener.open(urllib.request.Request(url, headers={'User-Agent': 'SEOStudioAudit/3.3'}), timeout=timeout)
            except urllib.error.HTTPError as ex: response = ex
            except (OSError, urllib.error.URLError) as ex:
                return {'url': url, 'status': 0, 'redirects': chain, 'error': str(ex)}, ''
            with response:
                code, headers = response.status, {key.lower(): value for key, value in response.headers.items()}
                raw = response.read(2_000_001)
            if len(raw) > 2_000_000:
                return {'url': url, 'status': code, 'redirects': chain, 'error': 'response size cap'}, ''
            if code in (301, 302, 303, 307, 308):
                target = urljoin(url, headers.get('location', ''))
                chain.append({'url': url, 'status': code, 'target': target})
                if target == url or not same(target):
                    return {'url': url, 'status': code, 'redirects': chain, 'error': 'redirect loop or outside target'}, ''
                url = target; continue
            return {'url': url, 'status': code, 'redirects': chain, 'headers': headers,
                    'body_sha256': hashlib.sha256(raw).hexdigest()}, raw.decode('utf-8', errors='replace')
        return {'url': url, 'status': 0, 'redirects': chain, 'error': 'redirect cap'}, ''
    robots, robot_text = fetch(urljoin(root, 'robots.txt'))
    parser = RobotFileParser(); parser.parse(robot_text.splitlines() if robots['status'] == 200 else [])
    if robots['status'] not in (200, 404): errors.append('robots.txt unavailable')
    sitemap, sitemap_text = fetch(urljoin(root, 'sitemap.xml'))
    sitemap_urls = []
    if sitemap['status'] == 200:
        try:
            tree = ET.fromstring(sitemap_text)
            if tree.tag.rsplit('}', 1)[-1] != 'urlset': errors.append('sitemap index requires explicit expanded crawl; incomplete')
            sitemap_urls = [n.text.strip() for n in tree.iter() if n.tag.rsplit('}', 1)[-1] == 'loc' and n.text]
        except ET.ParseError: errors.append('malformed sitemap XML')
    else: errors.append('sitemap.xml missing or unavailable')
    queue = deque([(base_url, 0)] + [(url, 0) for url in sitemap_urls if same(url)])
    seen = set(); truncated = False; depth_limited = set()
    while queue:
        url, depth = queue.popleft(); url = urldefrag(url)[0]
        if url in seen or not same(url): continue
        if len(seen) >= max_pages: truncated = True; break
        seen.add(url)
        result, html = fetch(url); result['requested_url'], result['depth'] = url, depth
        if result.get('error') or result['status'] != 200:
            errors.append('HTTP failure: ' + url); pages.append(result); continue
        if 'text/html' not in result['headers'].get('content-type', '').lower():
            result['html'] = False; pages.append(result); continue
        doc = Document(); doc.feed(html)
        noindex = 'noindex' in (doc.robots + ',' + result['headers'].get('x-robots-tag', '')).lower()
        result.update(html=True, title=doc.title, description=doc.description, h1=doc.h1,
                      canonicals=[urljoin(result['url'], c) for c in doc.canonicals],
                      links=[urldefrag(urljoin(result['url'], link))[0] for link in doc.links],
                      noindex=noindex, robots_allowed=parser.can_fetch('*', url), jsonld=jsonld_checks(doc.ld))
        if not doc.title or len(doc.h1) != 1: errors.append('missing title or non-single H1: ' + url)
        if not doc.description: warnings.append('description missing: ' + url)
        if len(doc.canonicals) != 1 or not doc.canonicals[0]: errors.append('single canonical required: ' + url)
        elif not same(result['canonicals'][0]): warnings.append('external canonical requires review: ' + url)
        if noindex and not result['robots_allowed']: errors.append('robots blocks reading noindex: ' + url)
        if any(c['status'] == 'FAIL' for c in result['jsonld']): errors.append('JSON-LD invalid: ' + url)
        for link in doc.links:
            target = urldefrag(urljoin(result['url'], link))[0]
            if same(target) and target not in seen:
                if depth >= depth_budget: depth_limited.add(target)
                else: queue.append((target, depth + 1))
        pages.append(result)
    truncated = truncated or bool(depth_limited - seen)
    html_pages = [p for p in pages if p.get('html')]
    indexable = {p['url'] for p in html_pages if not p['noindex'] and p['robots_allowed'] and p['canonicals'] == [p['url']]}
    graph = {p['url']: p.get('links', []) for p in html_pages}
    home = next((p['url'] for p in pages if p.get('requested_url') == urldefrag(base_url)[0]), base_url)
    distances = {}; navigation = deque([(home, 0)])
    while navigation:
        url, depth = navigation.popleft()
        if url in distances: continue
        distances[url] = depth
        navigation.extend((link, depth + 1) for link in graph.get(url, []) if link in graph)
    if indexable - set(distances): errors.append('indexable orphan pages absent from root link graph')
    if any(distances.get(url, 0) > 3 for url in indexable): warnings.append('indexable page navigation depth >3: review priority and justified exceptions')
    if set(sitemap_urls) != indexable: errors.append('sitemap/indexable canonical URL parity differs')
    for field in ('title', 'description'):
        duplicated = [v for v, count in Counter(p[field] for p in html_pages if p[field]).items() if count > 1]
        if duplicated: warnings.append('duplicate ' + field + ': contextual review required')
    if truncated: errors.append('crawl incomplete: depth or page cap reached')
    return {'schema_version': '1.0.0', 'run_id': None, 'site_context_sha256': None,
            'created_at': datetime.now(timezone.utc).isoformat(), 'target': base_url,
            'scope': 'same-origin GET; raw HTML, not rendered DOM; minimal JSON-LD subset',
            'status': 'BLOCKED' if errors else 'PASS', 'errors': errors, 'warnings': warnings,
            'http': {'status': 'FAIL' if errors else 'PASS', 'complete': not truncated,
                     'pages': pages, 'robots': robots, 'sitemap': sitemap, 'sitemap_urls': sitemap_urls,
                     'evidence_id': None},
            'browser': {'status': 'NOT_RUN'}, 'performance': {'status': 'NOT_RUN'}}


def validate_technical(project, state, *, load, safe_path, digest):
    errors, warnings = [], []
    binding = state.get('technical_audit')
    if not binding: return ['technical audit absent'], warnings
    evidence = {e['id']: e for e in state['evidence']}
    def proof(eid, kinds, label, expected_path=None, section=None):
        e = evidence.get(eid)
        if not e or e.get('kind') not in kinds: errors.append(label + ': missing evidence'); return
        p = safe_path(project, e['path'])
        if expected_path and e['path'] != expected_path: errors.append(label + ': wrong evidence path')
        if not p.is_file() or digest(p) != e['sha256']: errors.append(label + ': stale evidence')
        elif section is not None:
            if load(p) != {k: v for k, v in section.items() if k != 'evidence_id'}:
                errors.append(label + ': subordinate evidence does not match report')
    try:
        path = safe_path(project, binding['report_path']); report = load(path)
        proof(binding['evidence_id'], {'test_report'}, 'technical report', binding['report_path'])
        if not isinstance(report, dict): raise ValueError('report must be object')
        if report.get('schema_version') != '1.0.0': errors.append('technical schema unsupported')
        target = binding['target_url']
        base = urlsplit(target)
        if base.scheme not in ('http', 'https') or not base.hostname or base.username or base.password:
            errors.append('technical target invalid')
        origin = (base.scheme, base.hostname, base.port)
        def absolute(route): return urldefrag(urljoin(target, route))[0]
        def same_origin(url):
            value = urlsplit(url)
            return (value.scheme, value.hostname, value.port) == origin and not value.username and not value.password
        if absolute(report.get('target', '')) != absolute(target) or not report.get('target'):
            errors.append('technical report target differs')
        if not isinstance(binding.get('scope_reason'), str) or not binding['scope_reason'].strip():
            errors.append('technical representative scope rationale absent')
        expected = {absolute(p['path']): p for p in state['pages'] if p.get('public') is True and p.get('wave') == 'V1'}
        if not expected: errors.append('technical public V1 routes absent')
        if report.get('run_id') != state['run_id'] or report.get('site_context_sha256') != site_context_digest(state):
            errors.append('technical report context stale')
        snapshots = report.get('site_snapshots', [])
        if not snapshots: errors.append('technical site snapshots absent')
        required_paths = {a['path'] for a in state['artifacts'] if a['path'].lower().endswith(('.html', '.htm', '.css', '.js'))}
        if not required_paths.issubset({s['path'] for s in snapshots}): errors.append('technical site snapshots coverage incomplete')
        for snapshot in snapshots:
            source = safe_path(project, snapshot['path'])
            if not source.is_file() or digest(source) != snapshot['sha256']: errors.append('technical site snapshot stale')
        if report.get('status') != 'PASS' or report.get('errors') != []: errors.append('technical report failed')
        warnings.extend(report.get('warnings', []))
        http = report['http']
        if not isinstance(http, dict): raise ValueError('HTTP section must be object')
        if http.get('status') != 'PASS' or http.get('complete') is not True or not http.get('pages'):
            errors.append('HTTP crawl incomplete')
        proof(http.get('evidence_id'), {'http', 'test_report'}, 'HTTP crawl', section=http)
        if http.get('robots', {}).get('status') not in (200, 404) or http.get('sitemap', {}).get('status') != 200:
            errors.append('HTTP robots/sitemap subordinate failure')
        indexable = set()
        covered = set(); finals = {}
        for p in http.get('pages', []):
            requested, final = p.get('requested_url', p.get('url', '')), p.get('url', '')
            if not same_origin(requested) or not same_origin(final): errors.append('HTTP URL outside technical target')
            if p.get('html') and p.get('status') == 200:
                covered.update((requested, final)); finals[requested] = final; finals[final] = final
            if p.get('status') != 200 or p.get('error'): errors.append('HTTP subordinate failure')
            if p.get('html') and (len(p.get('h1', [])) != 1 or not p.get('title') or len(p.get('canonicals', [])) != 1):
                errors.append('HTTP subordinate HTML failure')
            if any(x.get('status') == 'FAIL' for x in p.get('jsonld', [])): errors.append('JSON-LD subordinate failure')
            if any(x.get('status') == 'NOT_VERIFIED' for x in p.get('jsonld', [])):
                warnings.append('JSON-LD unsupported type or minimal scope only: eligibility not certified')
            if p.get('noindex') and p.get('robots_allowed') is not True: errors.append('robots/noindex subordinate failure')
            if p.get('html') and p.get('noindex') is False and p.get('robots_allowed') is True and p.get('canonicals') == [p.get('url')]:
                indexable.add(p['url'])
        if set(http.get('sitemap_urls', [])) != indexable: errors.append('sitemap/indexable subordinate parity failure')
        if not set(expected).issubset(covered): errors.append('HTTP public V1 route coverage incomplete')
        for kind in ('browser', 'performance'):
            data = report[kind]
            if not isinstance(data, dict): raise ValueError(kind + ' section must be object')
            if kind == 'browser' and data.get('target') != absolute(target): errors.append('browser: scoped target differs')
            if data.get('status') != 'PASS' or not data.get('runs'): errors.append(kind + ': NOT_RUN or missing runs')
            proof(data.get('evidence_id'), {'browser', 'test_report'}, kind, section=data)
            configured = binding[kind + '_routes']
            if not isinstance(configured, list) or not configured or len(configured) != len(set(configured)):
                errors.append(kind + ': route scope must be nonempty and unique'); configured = []
            configured = {absolute(route) for route in configured}
            if not configured.issubset(expected): errors.append(kind + ': route scope outside public V1')
            required_kinds = {p.get('kind') for p in expected.values() if p.get('indexable') is True}
            represented = {expected[url].get('kind') for url in configured if url in expected}
            if not required_kinds.issubset(represented): errors.append(kind + ': indexable page-kind coverage incomplete')
            observed_routes = set()
            for run in data.get('runs', []):
                requested = absolute(run.get('route', ''))
                observed_routes.add(requested)
                if (requested not in configured or run.get('requested_url') != requested
                        or run.get('final_url') != finals.get(requested)
                        or not same_origin(run.get('final_url', ''))):
                    errors.append(kind + ': observed route differs from HTTP/scoped target')
                if not all(run.get(k) for k in ('tool', 'version', 'route', 'profile', 'observed_at')):
                    errors.append(kind + ': provenance incomplete')
                if kind == 'browser':
                    expected_checks = {'rendered_dom': True, 'navigation': True, 'console_errors': False,
                                       'raw_content_present': True, 'raw_links_present': True}
                    if run.get('checks') != expected_checks:
                        errors.append('browser checks incomplete or failed')
                else:
                    metrics, budgets = run.get('metrics', {}), run.get('budgets', {})
                    for metric in ('lcp_ms', 'cls', 'tbt_ms'):
                        v, b = metrics.get(metric), budgets.get(metric)
                        if (isinstance(v, bool) or isinstance(b, bool) or not isinstance(v, (int, float))
                                or not isinstance(b, (int, float)) or not math.isfinite(v) or not math.isfinite(b)
                                or v < 0 or b <= 0 or v > b): errors.append('lab performance invalid/over budget: ' + metric)
                    if run.get('measurement') != 'laboratory': errors.append('performance lab/field mixed')
                    if run.get('mobile') is not True: errors.append('performance mobile profile missing')
                    if run.get('tool') == 'Lighthouse':
                        raw_path = safe_path(project, run['raw_report_path'])
                        if not raw_path.is_file() or digest(raw_path) != run['raw_report_sha256']:
                            errors.append('Lighthouse raw report stale')
                        else:
                            raw = load(raw_path)
                            if (raw.get('lighthouseVersion') != run.get('version')
                                    or raw.get('fetchTime') != run.get('observed_at')
                                    or raw.get('configSettings', {}).get('formFactor') != 'mobile'
                                    or raw.get('requestedUrl') != requested
                                    or raw.get('finalUrl') != run.get('final_url')):
                                errors.append('Lighthouse raw provenance differs')
                            names = {'lcp_ms': 'largest-contentful-paint', 'cls': 'cumulative-layout-shift',
                                     'tbt_ms': 'total-blocking-time'}
                            for metric, name in names.items():
                                value = raw.get('audits', {}).get(name, {}).get('numericValue')
                                if isinstance(value, bool) or not isinstance(value, (int, float)) or value != metrics.get(metric):
                                    errors.append('Lighthouse raw measurement differs: ' + metric)
                    elif run.get('tool') != 'SYNTHETIC_TEST':
                        warnings.append('Performance tool provenance declared; no raw-report adapter for ' + str(run.get('tool')))
            if observed_routes != configured: errors.append(kind + ': configured route coverage incomplete')
        return errors, warnings
    except (KeyError, TypeError, ValueError, OSError, AttributeError) as ex:
        return errors + ['technical report invalid: ' + str(ex)], warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('base_url'); parser.add_argument('--allow-remote', action='store_true')
    parser.add_argument('--max-pages', type=int, default=200); parser.add_argument('--timeout', type=float, default=10)
    parser.add_argument('--depth-budget', type=int, default=20); parser.add_argument('--output', required=True)
    args = parser.parse_args()
    report = audit(args.base_url, args.max_pages, args.timeout, args.depth_budget, args.allow_remote)
    with Path(args.output).open('x', encoding='utf-8') as stream: json.dump(report, stream, ensure_ascii=False, indent=2)
    return 0 if report['status'] == 'PASS' else 1


if __name__ == '__main__': raise SystemExit(main())
