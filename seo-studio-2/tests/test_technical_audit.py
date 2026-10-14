"""Local HTTP fixture only; mocked browser/lab records are not production proof."""
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from technical_audit import audit, jsonld_checks, site_context_digest, validate_technical


class Handler(BaseHTTPRequestHandler):
    routes = {}
    def log_message(self, *args): pass
    def do_GET(self):
        code, headers, content = self.routes.get(self.path, (404, {}, 'missing'))
        self.send_response(code)
        for key, value in headers.items(): self.send_header(key, value)
        self.end_headers(); self.wfile.write(content.encode())


class TechnicalTests(unittest.TestCase):
    def setUp(self):
        self.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True); self.thread.start()
        self.url = 'http://127.0.0.1:%s/' % self.server.server_port
        Handler.routes = {'/': (200, {'Content-Type': 'text/html'}, self.html()),
                          '/robots.txt': (200, {}, 'User-agent: *\nAllow: /'),
                          '/sitemap.xml': (200, {}, '<urlset><url><loc>' + self.url + '</loc></url></urlset>')}

    def html(self, extra=''):
        return '<title>Fixture</title><meta name="description" content="Fixture"><link rel="canonical" href="' + self.url + '"><h1>Fixture</h1>' + extra

    def tearDown(self): self.server.shutdown(); self.server.server_close(); self.thread.join()

    def test_http_real_fixture(self):
        report = audit(self.url)
        self.assertEqual(report['status'], 'PASS')
        self.assertEqual(report['browser']['status'], 'NOT_RUN')
        self.assertTrue(report['http']['pages'][0]['body_sha256'])

    def test_redirect_and_failure(self):
        Handler.routes['/go'] = (302, {'Location': '/'}, '')
        report = audit(self.url + 'go')
        self.assertEqual(report['http']['pages'][0]['redirects'][0]['status'], 302)
        Handler.routes['/'] = (500, {}, 'bad')
        self.assertEqual(audit(self.url)['status'], 'BLOCKED')

    def test_redirected_root_is_navigation_origin(self):
        home = self.url + 'home'
        Handler.routes['/'] = (302, {'location': '/home'}, '')
        Handler.routes['/home'] = (200, {'content-type': 'text/html'}, self.html().replace(self.url + '\"', home + '\"'))
        Handler.routes['/sitemap.xml'] = (200, {}, '<urlset><url><loc>' + home + '</loc></url></urlset>')
        report = audit(self.url)
        self.assertEqual(report['status'], 'PASS', report['errors'])

    def test_lowercase_content_type_and_robots_header(self):
        Handler.routes['/'] = (200, {'content-type': 'text/html', 'x-robots-tag': 'noindex'}, self.html())
        Handler.routes['/sitemap.xml'] = (200, {}, '<urlset/>')
        report = audit(self.url)
        self.assertEqual(report['status'], 'PASS', report['errors'])
        self.assertTrue(report['http']['pages'][0]['noindex'])
        Handler.routes['/robots.txt'] = (200, {}, 'User-agent: *\nDisallow: /')
        self.assertTrue(any('reading noindex' in e for e in audit(self.url)['errors']))

    def test_crawl_cap_blocks(self):
        Handler.routes['/'] = (200, {'Content-Type': 'text/html'}, self.html('<a href="/other">Other</a>'))
        self.assertFalse(audit(self.url, depth_budget=0)['http']['complete'])

    def test_robots_noindex(self):
        Handler.routes['/'] = (200, {'Content-Type': 'text/html'}, self.html('<meta name="robots" content="noindex">'))
        Handler.routes['/robots.txt'] = (200, {}, 'User-agent: *\nDisallow: /')
        self.assertTrue(any('reading noindex' in e for e in audit(self.url)['errors']))

    def test_jsonld_scope(self):
        self.assertEqual(jsonld_checks(['{'])[0]['status'], 'FAIL')
        self.assertEqual(jsonld_checks(['{"@type":"Unlisted"}'])[0]['status'], 'NOT_VERIFIED')
        self.assertEqual(jsonld_checks(['{"@type":"Article"}'])[0]['status'], 'FAIL')
        self.assertEqual(jsonld_checks(['{"@type":"Article","headline":"Fixture"}'])[0]['status'], 'PASS')

    def test_sitemap_seed_does_not_hide_orphan(self):
        other = self.url + 'orphan'
        Handler.routes['/orphan'] = (200, {'Content-Type': 'text/html'}, self.html().replace(self.url + '\"', other + '\"'))
        Handler.routes['/sitemap.xml'] = (200, {}, '<urlset><url><loc>' + self.url + '</loc></url><url><loc>' + other + '</loc></url></urlset>')
        self.assertTrue(any('orphan' in e for e in audit(self.url)['errors']))

    def test_external_redirect_never_followed(self):
        Handler.routes['/'] = (302, {'Location': 'http://example.com/'}, '')
        report = audit(self.url)
        self.assertIn('outside target', report['http']['pages'][0]['error'])

    def test_remote_requires_explicit_scope(self):
        with self.assertRaises(ValueError): audit('https://example.com/')
        with self.assertRaises(ValueError): audit('http://user:secret@127.0.0.1/')

    def test_release_requires_browser_lab_and_current_context(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td); (project / 'index.html').write_text(self.html(), encoding='utf-8')
            def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
            state = {'run_id': 'fixture', 'brief_version': '1',
                     'pages': [{'path': '/', 'public': True, 'indexable': True, 'wave': 'V1', 'kind': 'home'}],
                     'links': [], 'artifacts': [], 'evidence': [],
                     'technical_audit': {'report_path': 'report.json', 'evidence_id': 'report',
                                         'target_url': self.url, 'browser_routes': ['/'], 'performance_routes': ['/'],
                                         'scope_reason': 'Synthetic one-route protocol fixture'}}
            report = audit(self.url); report.update(run_id='fixture', site_context_sha256=site_context_digest(state),
                                                    site_snapshots=[{'path': 'index.html', 'sha256': digest(project / 'index.html')}])
            def save():
                for kind in ('http', 'browser', 'performance'):
                    (project / (kind + '.json')).write_text(json.dumps({k: v for k, v in report[kind].items() if k != 'evidence_id'}), encoding='utf-8')
                (project / 'report.json').write_text(json.dumps(report), encoding='utf-8')
                state['evidence'] = [{'id': x, 'kind': 'http' if x == 'http' else 'test_report',
                                      'path': x + '.json', 'sha256': digest(project / (x + '.json'))}
                                     for x in ('report', 'http', 'browser', 'performance')]
            report['http']['evidence_id'] = 'http'; save()
            kwargs = {'load': lambda p: json.loads(p.read_text(encoding='utf-8')),
                      'safe_path': lambda p, v: p / v, 'digest': digest}
            errors, _ = validate_technical(project, state, **kwargs)
            self.assertTrue(any('NOT_RUN' in e for e in errors))
            for kind in ('browser', 'performance'):
                record = {'tool': 'SYNTHETIC_TEST', 'version': '1', 'route': '/', 'profile': 'fixture', 'observed_at': '2026-10-14'}
                record.update(requested_url=self.url, final_url=self.url)
                if kind == 'browser': record['checks'] = {'rendered_dom': True, 'navigation': True, 'console_errors': False,
                                                        'raw_content_present': True, 'raw_links_present': True}
                else: record.update(measurement='laboratory', mobile=True, metrics={'lcp_ms': 100, 'cls': 0, 'tbt_ms': 0},
                                    budgets={'lcp_ms': 2500, 'cls': .1, 'tbt_ms': 200})
                report[kind] = {'status': 'PASS', 'target': self.url, 'evidence_id': 'http', 'runs': [record]}
            # Evidence must use the appropriate kind; HTTP evidence cannot certify browser/lab.
            save(); errors, _ = validate_technical(project, state, **kwargs)
            self.assertTrue(any('missing evidence' in e for e in errors))
            report['browser']['evidence_id'] = 'browser'; report['performance']['evidence_id'] = 'performance'
            save(); self.assertEqual(validate_technical(project, state, **kwargs)[0], [])
            report['performance']['runs'][0]['metrics']['tbt_ms'] = 201
            save(); self.assertTrue(any('over budget' in e for e in validate_technical(project, state, **kwargs)[0]))
            report['performance']['runs'][0]['metrics']['tbt_ms'] = 0
            lab = report['performance']['runs'][0]
            lab.update(tool='Lighthouse', raw_report_path='lighthouse.json')
            raw = {'lighthouseVersion': lab['version'], 'fetchTime': lab['observed_at'],
                   'requestedUrl': self.url, 'finalUrl': self.url,
                   'configSettings': {'formFactor': 'mobile'},
                   'audits': {'largest-contentful-paint': {'numericValue': 100},
                              'cumulative-layout-shift': {'numericValue': 0},
                              'total-blocking-time': {'numericValue': 0}}}
            (project / 'lighthouse.json').write_text(json.dumps(raw), encoding='utf-8')
            lab['raw_report_sha256'] = digest(project / 'lighthouse.json')
            save(); self.assertEqual(validate_technical(project, state, **kwargs)[0], [])
            report['browser']['runs'][0]['route'] = '/not-crawled'
            save(); self.assertTrue(any('observed route differs' in e for e in validate_technical(project, state, **kwargs)[0]))
            report['browser']['runs'][0]['route'] = '/'
            raw['finalUrl'] = 'http://elsewhere.invalid/'
            (project / 'lighthouse.json').write_text(json.dumps(raw), encoding='utf-8')
            lab['raw_report_sha256'] = digest(project / 'lighthouse.json')
            save(); self.assertTrue(any('raw provenance differs' in e for e in validate_technical(project, state, **kwargs)[0]))
            raw['finalUrl'] = self.url
            (project / 'lighthouse.json').write_text(json.dumps(raw), encoding='utf-8')
            lab['raw_report_sha256'] = digest(project / 'lighthouse.json')
            state['pages'].append({'path': '/missing', 'public': True, 'indexable': True, 'wave': 'V1', 'kind': 'home'})
            save(); self.assertTrue(any('HTTP public V1 route coverage incomplete' in e for e in validate_technical(project, state, **kwargs)[0]))
            state['pages'].pop()
            report['target'] = 'http://elsewhere.invalid/'
            save(); self.assertTrue(any('report target differs' in e for e in validate_technical(project, state, **kwargs)[0]))
            report['target'] = self.url
            lab['metrics']['lcp_ms'] = 101
            save(); self.assertTrue(any('raw measurement differs' in e for e in validate_technical(project, state, **kwargs)[0]))
            lab['metrics']['lcp_ms'] = 100
            raw['configSettings']['formFactor'] = 'desktop'
            (project / 'lighthouse.json').write_text(json.dumps(raw), encoding='utf-8')
            lab['raw_report_sha256'] = digest(project / 'lighthouse.json')
            save(); self.assertTrue(any('raw provenance differs' in e for e in validate_technical(project, state, **kwargs)[0]))
            report['browser'] = []
            (project / 'report.json').write_text(json.dumps(report), encoding='utf-8')
            state['evidence'][0]['sha256'] = digest(project / 'report.json')
            self.assertTrue(any('invalid' in e for e in validate_technical(project, state, **kwargs)[0]))
            report['browser'] = {'status': 'NOT_RUN'}
            (project / 'index.html').write_text('modified', encoding='utf-8')
            self.assertTrue(any('snapshot stale' in e for e in validate_technical(project, state, **kwargs)[0]))


if __name__ == '__main__': unittest.main()
