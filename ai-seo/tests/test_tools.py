"""Synthetic unit tests. No live engine, browser, production site, or user PC."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
from classify_referral import classify, host_of
from measure_panel import summarize
from audit_snapshot import audit, robots_hint
from install import install, inventory
from init_project import initialize


def row(run='r1', **changes):
    value = dict(run_id=run, query_id='q1', platform='ChatGPT', surface='web',
                 branded=False, language='fr', country='FR', search_enabled=True,
                 context_control='fresh', synthetic=True, observed_at='2026-10-04T12:00:00Z',
                 status='ok', evidence_ref='synthetic:answer', mentioned=True,
                 cited=True, recommended=False)
    return {**value, **changes}


def snapshot(public=True):
    return {'origin': 'https://example.test', 'synthetic': True,
            'robots': {'status': 200, 'text': 'User-agent: *\nDisallow: /private'},
            'pages': [{'url': 'https://example.test/private', 'intended_public': public,
                       'status': 200, 'headers': {}, 'html': '<html lang="fr"><head><title>Test</title>'
                       '<link rel="canonical" href="https://example.test/private"></head>'
                       '<body><h1>Test</h1><p>Texte synthétique</p></body></html>'}]}


class ReferralTests(unittest.TestCase):
    def test_unknown_is_not_ai(self):
        self.assertEqual(classify('https://example.test')['channel'], 'unknown')
    def test_exact_referrer(self):
        result = classify('https://example.test', 'https://chatgpt.com/c/1')
        self.assertEqual(result['channel'], 'observed_ai_referral')
        self.assertFalse(result['recommendation_verified'])
    def test_domain_boundary(self):
        for url in ('https://chatgpt.com.evil.test/', 'https://evilchatgpt.com/', 'https://evil.test/chatgpt.com'):
            self.assertIsNone(classify('https://example.test', url)['platform_signal'])
    def test_credentials_refused(self):
        self.assertEqual(host_of('https://chatgpt.com@evil.test'), '')
    def test_utm_is_declared_only(self):
        result = classify('https://example.test?utm_source=chatgpt')
        self.assertEqual(result['channel'], 'declared_ai_campaign')
        self.assertFalse(result['organic_verified'])
    def test_duplicates_conflict(self):
        self.assertTrue(classify('https://example.test?utm_source=a&utm_source=b')['conflict'])
    def test_campaign_conflict(self):
        self.assertEqual(classify('https://example.test?utm_source=email', 'https://claude.ai')['channel'], 'conflicting_signals')
    def test_bot_separated(self):
        result = classify('https://example.test', 'https://chatgpt.com', 'OAI-SearchBot/1.4')
        self.assertEqual(result['channel'], 'machine_user_agent_signal')
        self.assertFalse(result['human_verified'])
    def test_invalid_landing(self):
        with self.assertRaises(ValueError): classify('file:///etc/passwd')


class PanelTests(unittest.TestCase):
    def test_error_excluded(self):
        group = summarize([row(), row('r2', cited=False), row('r3', status='error')])['strata'][0]
        self.assertEqual(group['valid_answers'], 2)
        self.assertEqual(group['citation_rate'], .5)
    def test_synthetic_separate(self):
        self.assertEqual(len(summarize([row(), row('r2', synthetic=False)])['strata']), 2)
    def test_no_valid_is_null(self):
        self.assertIsNone(summarize([row(status='not_tested')])['strata'][0]['citation_rate'])
    def test_duplicate_run_rejected(self):
        with self.assertRaises(ValueError): summarize([row(), row()])
    def test_proof_required(self):
        with self.assertRaises(ValueError): summarize([row(evidence_ref='')])
    def test_bool_not_int(self):
        with self.assertRaises(ValueError): summarize([row(cited=1)])
    def test_timezone_required(self):
        with self.assertRaises(ValueError): summarize([row(observed_at='2026-10-04T12:00:00')])


class SnapshotTests(unittest.TestCase):
    def test_specific_group_not_wildcard_union(self):
        text = 'User-agent: *\nDisallow: /\nUser-agent: OAI-SearchBot\nAllow: /'
        self.assertTrue(robots_hint(text, 'OAI-SearchBot', 'https://example.test/a')['allowed_hint'])
    def test_equal_length_allow(self):
        text = 'User-agent: *\nDisallow: /a\nAllow: /a'
        self.assertTrue(robots_hint(text, 'Googlebot', 'https://example.test/a')['allowed_hint'])
    def test_unicode_unknown(self):
        self.assertIsNone(robots_hint('User-agent: *\nAllow: /', 'Googlebot', 'https://example.test/%C3%A9')['allowed_hint'])
    def test_public_block_detected(self):
        codes = [i['code'] for i in audit(snapshot())['pages'][0]['issues']]
        self.assertIn('ROBOTS_BLOCK_HINT', codes)
    def test_private_not_proposed_for_opening(self):
        codes = [i['code'] for i in audit(snapshot(False))['pages'][0]['issues']]
        self.assertNotIn('ROBOTS_BLOCK_HINT', codes)
    def test_cross_origin_unknown(self):
        data = snapshot(); data['origin'] = 'https://another.test'
        self.assertIsNone(audit(data)['pages'][0]['robots_hints']['Googlebot']['allowed_hint'])
    def test_invalid_jsonld(self):
        data = snapshot(); data['pages'][0]['html'] += '<script type="application/ld+json">{</script>'
        self.assertIn('INVALID_JSONLD', [i['code'] for i in audit(data)['pages'][0]['issues']])
    def test_restrictive_header(self):
        data = snapshot(); data['pages'][0]['headers']['X-Robots-Tag'] = 'noindex'
        self.assertIn('RESTRICTIVE_DIRECTIVE_REVIEW', [i['code'] for i in audit(data)['pages'][0]['issues']])


class FilesystemTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'source'; self.source.mkdir()
        (self.source / 'SKILL.md').write_text('---\nname: ai-seo\ndescription: test\n---\n', encoding='utf-8')
        self.target = self.root / 'active' / 'ai-seo'
        self.backups = self.root / 'backups'
    def test_dry_run_no_write(self):
        result = install(self.source, self.target, self.backups)
        self.assertEqual(result['mode'], 'dry-run'); self.assertFalse(self.target.exists())
    def test_fresh_install(self):
        result = install(self.source, self.target, self.backups, apply=True)
        self.assertEqual(inventory(self.source), inventory(self.target))
        self.assertFalse(result['host_discovery_verified'])
    def test_existing_requires_review(self):
        self.target.mkdir(parents=True)
        with self.assertRaises(ValueError): install(self.source, self.target, self.backups, apply=True)
    def test_backup_verified(self):
        self.target.mkdir(parents=True); (self.target / 'custom.txt').write_text('keep')
        before = inventory(self.target)
        result = install(self.source, self.target, self.backups, True, True)
        self.assertEqual(inventory(Path(result['backup'])), before)
    def test_rollback_on_rename_error(self):
        self.target.mkdir(parents=True); (self.target / 'custom.txt').write_text('keep')
        before = inventory(self.target)
        with patch('pathlib.Path.rename', side_effect=OSError('synthetic fault')):
            with self.assertRaises(OSError): install(self.source, self.target, self.backups, True, True)
        self.assertEqual(inventory(self.target), before)
    def test_nested_backup_refused(self):
        with self.assertRaises(ValueError): install(self.source, self.target, self.target / 'backup')
    def test_symlink_refused(self):
        link = self.source / 'link'
        try: link.symlink_to(self.root)
        except (OSError, NotImplementedError): self.skipTest('symlinks not available')
        with self.assertRaises(ValueError): install(self.source, self.target, self.backups)
    def test_initializer_preserves_existing(self):
        package = self.root / 'pkg'; templates = package / 'templates/project'; templates.mkdir(parents=True)
        (templates / 'plan.md').write_text('template')
        project = self.root / 'project'; project.mkdir()
        with patch('init_project.__file__', str(package / 'scripts/init_project.py')):
            self.assertEqual(initialize(project)['mode'], 'dry-run')
            initialize(project, apply=True)
            target = project / 'SEO/AI_ACQUISITION/plan.md'; target.write_text('custom')
            self.assertEqual(initialize(project, apply=True)['created'], [])
            self.assertEqual(target.read_text(), 'custom')
    def test_initializer_path_traversal(self):
        with self.assertRaises(ValueError): initialize(self.root, '../outside')
    def test_all_cli_help(self):
        for script in SCRIPTS.glob('*.py'):
            result = subprocess.run([sys.executable, str(script), '--help'], capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, script.name)


if __name__ == '__main__': unittest.main()
