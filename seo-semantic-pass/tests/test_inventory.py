import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from inventory import analyze
class InventoryTests(unittest.TestCase):
 def setUp(self): self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)
 def tearDown(self): self.tmp.cleanup()
 def add(self,name,text): (self.root/name).write_text(text,encoding='utf-8')
 def test_extract_main_excludes_navigation(self):
  self.add('index.html','<title>Guide</title><body><nav>Menu</nav><main><h1>Bureau</h1><p>Texte utile</p><a href="/guide">Guide</a></main><footer>Pub</footer></body>')
  p=analyze(self.root)['pages'][0];self.assertEqual(p['title'],'Guide');self.assertEqual(p['headings'][0]['text'],'Bureau');self.assertNotIn('Menu',p['content_excerpt']);self.assertEqual(p['links'],['/guide'])
 def test_candidates_and_short_content(self):
  words='un éclairage bureau ruban alimentation lumière puissance installation raccordement choix fonctionnement simple utile'
  self.add('a.html','<main>'+words+'</main>');self.add('b.html','<main>'+words+'</main>');self.add('c.html','<main>court</main>')
  r=analyze(self.root);self.assertEqual(len(r['lexical_candidates']),1);self.assertEqual(r['lexical_candidates'][0]['jaccard'],1)
 def test_limits_and_errors(self):
  self.add('a.html','<body>abc</body>');self.add('b.html','<body>def</body>')
  r=analyze(self.root,max_files=1);self.assertFalse(r['coverage']['complete']);self.assertEqual(r['coverage']['skipped_limit'],1)
  r=analyze(self.root,max_bytes=2);self.assertEqual(r['coverage']['failed'],2)
 def test_invalid_utf8(self):
  (self.root/'bad.html').write_bytes(b'\xff');r=analyze(self.root);self.assertEqual(r['coverage']['failed'],1)
 def test_no_html_is_not_complete(self):
  self.assertFalse(analyze(self.root)['coverage']['complete'])
 def test_empty_and_missing_root(self):
  self.add('empty.html','<html><body></body></html>');self.assertTrue(analyze(self.root)['pages'][0]['text_empty'])
  with self.assertRaises(ValueError):analyze(self.root/'missing')
if __name__=='__main__':unittest.main()

