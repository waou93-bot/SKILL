"""Exports fictifs : contrôles statiques seulement, aucune recette navigateur."""
import sys
from pathlib import Path
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from site_check import check


class SiteCheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.home = '<title>Accueil</title><meta name="description" content="Accueil utile"><a href="/guide/#usage">Guide</a>'
        self.guide = '<title>Guide</title><meta name="description" content="Guide utile"><input type="search"><h2 id="usage">Usage</h2><a href="/">Accueil</a>'
        self.write('index.html', self.home)
        self.write('guide/index.html', self.guide)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, path, content):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding='utf-8')

    def test_connected_site_with_explicit_landing(self):
        result = check(self.root, ['/'])
        self.assertEqual(result['status'], 'LOCAL_HTML_OK', result)
        self.assertEqual(result['pages'], 2)

    def test_home_is_not_implicitly_a_landing(self):
        self.assertEqual(check(self.root)['status'], 'BLOQUE')

    def test_content_page_requires_search_even_without_listing(self):
        self.write('guide/index.html', self.guide.replace('<input type="search">', ''))
        self.assertTrue(any('recherche interne' in e for e in check(self.root, ['/'])['errors']))

    def test_broken_fragment_is_detected(self):
        self.write('index.html', self.home.replace('#usage', '#absent'))
        self.assertTrue(any('fragment absent' in e for e in check(self.root, ['/'])['errors']))

    def test_missing_internal_asset_is_detected(self):
        self.write('guide/index.html', self.guide + '<img src="/missing.webp" alt="Produit">')
        self.assertTrue(any('destination absente' in e for e in check(self.root, ['/'])['errors']))

    def test_absolute_internal_links_and_canonical(self):
        base = 'https://example.org'
        self.write('index.html', self.home.replace('/guide/#usage', base + '/guide/#usage') + '<link rel="canonical" href="https://example.org/">')
        self.write('guide/index.html', self.guide + '<link rel="canonical" href="https://example.org/guide/">')
        self.assertEqual(check(self.root, ['/'], base)['status'], 'LOCAL_HTML_OK')

    def test_missing_metadata_blocks_result(self):
        self.write('guide/index.html', self.guide.replace('<title>Guide</title>', ''))
        self.assertTrue(any('title absent' in e for e in check(self.root, ['/'])['errors']))

    def test_orphan_content_page_blocks_result(self):
        self.write('isolated/index.html', self.guide)
        self.assertTrue(any('orpheline' in e for e in check(self.root, ['/'])['errors']))

    def test_encoded_path_escape_is_rejected(self):
        self.write('index.html', self.home + '<a href="/%2e%2e/private.html">Hors export</a>')
        self.assertTrue(any('hors export' in e for e in check(self.root, ['/'])['errors']))

    def test_empty_export_is_not_a_verified_site(self):
        empty = self.root / 'empty'
        empty.mkdir()
        self.assertEqual(check(empty)['status'], 'BLOQUE')


if __name__ == '__main__':
    unittest.main()
