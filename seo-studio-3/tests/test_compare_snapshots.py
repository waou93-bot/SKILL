import json, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from compare_snapshots import load, compare

class Snapshots(unittest.TestCase):
 def setUp(self): self.page={'id':'p1','url':'https://a.example/x','canonical':'https://a.example/x','noindex':False}
 def read(self,pages):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'s.json';p.write_text(json.dumps({'version':1,'site_id':'site-a','pages':pages}),encoding='utf-8');return load(p)
 def test_same(self): self.assertEqual(compare(self.read([self.page]),self.read([self.page]))['status'],'PASS')
 def test_changed(self):
  b=dict(self.page,canonical=None,noindex=True);self.assertEqual({x['field'] for x in compare(self.read([self.page]),self.read([b]))['changes']},{'canonical','noindex'})
 def test_removed_added(self):
  self.assertEqual({x['field'] for x in compare(self.read([self.page]),self.read([dict(self.page,id='p2')]))['changes']},{'removed','added'})
 def test_cross_site_rejected(self):
  before=self.read([self.page]); after=('site-b',before[1])
  with self.assertRaises(ValueError):compare(before,after)
 def test_invalid(self):
  for p in (dict(self.page,noindex='false'),dict(self.page,url='file:///x'),dict(self.page,url='https://user:secret@example.com/')):
   with self.assertRaises(ValueError):self.read([p])
  with self.assertRaises(ValueError):self.read([self.page,self.page])
if __name__=='__main__':unittest.main()

