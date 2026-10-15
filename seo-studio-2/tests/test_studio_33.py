"""Contracts, not a real niche site or simulated SEO success."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'scripts')]
import studio
from test_studio import fixture
from technical_fixture import complete_technical
from workflow import workflow_digest

class UpgradeTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.project=Path(self.tmp.name)/'project';self.state=fixture(self.project)
    def result(self,stage='handoff'):
        (self.project/'state.json').write_text(studio.json_text(self.state),encoding='utf-8')
        return studio.validate_project(self.project,stage)
    def approve_inputs(self):
        for review in self.state['reviews']:review['inputs_sha256']=studio.input_digest(self.state)
    def test_common_footer_affiliation_no_per_placement_text(self):
        self.state['affiliate_notice']={'text':'Certains liens sont affiliés et peuvent générer une commission.','location':'footer_and_legal','legal_path':'/mentions-legales/','compliance_note':'Context-specific obligations to verify; no universal legal certification'}
        self.state['placements'][0]['disclosure']='GLOBAL';self.approve_inputs()
        self.assertEqual(self.result()['status'],'STRUCTURE_OK')
    def test_global_without_notice_blocks(self):
        self.state['placements'][0]['disclosure']='GLOBAL';self.approve_inputs()
        self.assertTrue(any('mention commune' in e for e in self.result()['errors']))
    def test_sponsored_remains_required(self):
        self.state['placements'][0]['rel']=[];self.approve_inputs()
        self.assertTrue(any('sponsored' in e for e in self.result()['errors']))
    def test_changed_serp_invalidates_existing_approval(self):
        p=self.project/'research/serp.json';data=studio.load(p);data['observations'][0]['gap']='Modified after review'
        p.write_text(studio.json_text(data),encoding='utf-8')
        self.assertTrue(any('SERP' in e and 'modifiée' in e for e in self.result()['errors']))
    def test_lite_initialization_preserves_requirements_and_search(self):
        other=Path(self.tmp.name)/'lite'
        studio.init_project(other,'niche','contenu',True,'lite')
        state=studio.load(other/'state.json')
        self.assertEqual(state['planning_mode'],'lite')
        self.assertEqual({r['id'] for r in state['requirements']},{r['id'] for r in studio.load(studio.ROOT/'schemas/requirements.json')['requirements']})
        self.assertEqual(studio.validate_project(other)['status'],'STRUCTURE_OK')
    def test_default_author_portable_and_no_fake_contact(self):
        text=studio.initial_files('niche fictive','vitrine')['AUTEUR.md']
        self.assertIn("Nicolas, l'auteur des pages",text)
        self.assertNotIn('capillairo.fr',text)
        self.assertNotIn('coiffeur',text)
        self.assertNotIn('@',text)
    def test_capillary_author_retains_health_limit(self):
        files=studio.initial_files('soins capillaires','comparateur')
        self.assertIn("Il n'est ni coiffeur ni dermatologue",files['AUTEUR.md'])
        self.assertEqual(studio.load(studio.ROOT/'templates/state.json')['editorial_identity']['name'],'Nicolas')
    def test_author_route_cannot_be_omitted_from_handoff(self):
        self.state['pages']=[p for p in self.state['pages'] if p['path']!='/auteur/']
        self.assertTrue(any('Page auteur' in e for e in self.result()['errors']))
    def test_mode_change_not_silent_reinitialization(self):
        with self.assertRaises(ValueError):studio.init_project(self.project,self.state['niche'],self.state['site_type'],True,'lite')
    def test_release_requires_current_technical_report(self):
        self.state['permissions']['publication']=True;self.state['gates'][-1].update(status='APPROVED',evidence_ids=['review']);self.state['live_evidence_ids']=['http','authorization']
        self.assertTrue(any('technical audit absent' in e for e in self.result('release')['errors']))
        complete_technical(self.project,self.state)
        self.assertEqual(self.result('release')['status'],'BLOQUE')
        self.assertTrue(any('Livraison' in e for e in self.result('release')['errors']))
    def test_serp_snapshot_included_without_approval(self):
        self.result();snap=studio.review_snapshot(self.project)
        self.assertIn('research/serp.json',[a['path'] for a in snap['reviewed_artifacts']])

if __name__=='__main__':unittest.main()
