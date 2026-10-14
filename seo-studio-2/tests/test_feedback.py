"""Synthetic source data; no GSC calls, account writes or published-site claim."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import studio
from feedback import check_feedback

class FeedbackTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.state={'run_id':'test','pages':[{'id':'p'}],'reviews':[{'id':'r'}]}
        self.save('release.json',self.state)
        self.row={'page_id':'p','baseline':{'impressions':1000,'clicks':100},'current':{'impressions':1000,'clicks':60},'indexation':'INDEXED'}
        self.save('export.json',{'rows':[self.row]})
        self.data={'schema_version':'1','run_id':'test','release_snapshot':{'path':'release.json','sha256':studio.digest(self.root/'release.json')},'source':{'provider':'SYNTHETIC','exported_at':'2026-10-14','path':'export.json','sha256':studio.digest(self.root/'export.json'),'limitations':'Synthetic only'},'baseline':{'start':'2026-08-01','end':'2026-08-30'},'current':{'start':'2026-09-01','end':'2026-09-30'},'rows':[self.row]}
    def save(self,path,data):
        (self.root/path).write_text(json.dumps(data),encoding='utf-8')
    def check(self):
        return check_feedback(self.root,self.state,self.data,load=studio.load,safe_path=studio.safe_path,digest=studio.digest)
    def test_ctr_signal_without_writes(self):
        before=(self.root/'release.json').read_bytes()
        result=self.check()
        self.assertEqual(result['actions'][0]['recommendation'],'REVIEW_SNIPPET_AND_INTENT')
        self.assertEqual(result['review_ids_to_reopen_if_changes_approved'],['r'])
        self.assertEqual(before,(self.root/'release.json').read_bytes())
    def test_unknown_is_not_zero(self):
        self.row['current']['clicks']=None
        self.save('export.json',{'rows':[self.row]});self.data['source']['sha256']=studio.digest(self.root/'export.json')
        self.assertEqual(self.check()['actions'][0]['recommendation'],'OBSERVE')
    def test_edited_export_blocked(self):
        self.save('export.json',{'rows':[]})
        with self.assertRaises(ValueError):self.check()
    def test_low_sample_no_rewrite(self):
        self.row['current']={'impressions':10,'clicks':0}
        self.save('export.json',{'rows':[self.row]});self.data['source']['sha256']=studio.digest(self.root/'export.json')
        self.assertEqual(self.check()['actions'][0]['recommendation'],'OBSERVE')
    def test_bad_windows_blocked(self):
        self.data['current']['end']='2026-09-15'
        with self.assertRaises(ValueError):self.check()
    def test_fabricated_normalized_rows_blocked(self):
        self.save('export.json',{'rows':[]});self.data['source']['sha256']=studio.digest(self.root/'export.json')
        with self.assertRaises(ValueError):self.check()

if __name__=='__main__':unittest.main()
