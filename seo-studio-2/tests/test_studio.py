"""Fixtures purement fictives : tests structurels, aucun agent/site réel évalué."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import studio
import install as installer
from workflow_fixture import complete_workflow
from serp_fixture import complete_serp


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8')


def fixture(project: Path) -> dict:
    """Preuves factices clairement marquées; suffit uniquement au contrat de structure."""
    studio.init_project(project,'Niche fictive de test','média affilié',True)
    state=studio.load(project/'state.json')
    def evidence(eid: str, path: str, kind: str) -> None:
        state['evidence'].append({'id':eid,'path':path,'sha256':studio.digest(project/path),
                                 'kind':kind,'origin':'FIXTURE FICTIVE — aucun test terrain ni agent réel'})
    write(project/'proof.txt','FIXTURE FICTIVE : trace et source artificielles pour tests unitaires uniquement.\n')
    for kind in ['training','runtime','source','review','test_report','authorization','http']:
        evidence(kind,'proof.txt',kind)
    state['runtime'].update(mode='DELEGATED',delegation_available=True,max_active_delegates=2,
                            executed_depth=1,model_selection_verified=True)
    for role in state['roles']:
        role.update(training_status='FORME',evidence_ids=['training'])
    state['personna'].update(status='EXECUTED',source_path='/fiction/personna/SKILL.md',sha256='a'*64,evidence_ids=['training'])
    for dep in state['dependencies']:
        dep.update(status='LU',path='/fiction/'+dep['name']+'/SKILL.md',sha256='a'*64,read_evidence_id='source')
    for a in state['artifacts']:
        if a['kind']=='skin':
            text=json.dumps({'status':'REVIEWED','fixture':True,'visual_concept':'Fiction de test de contrat'},ensure_ascii=False)
        else:
            text='# Dossier fictif\n\nCe texte sert exclusivement aux tests structurels ; il ne constitue pas une préproduction réelle.\n'
        write(project/a['path'],text)
        evidence('file-'+a['id'],a['path'],'artifact')
        a.update(status='REVIEWED',evidence_id='file-'+a['id'])
    architecture=project/'03_ARCHITECTURE.md'
    with architecture.open('a',encoding='utf-8') as f:
        for heading in studio.TEMPLATE_ASSESSMENT_HEADINGS:
            f.write('\n## '+heading+'\n\nAnalyse fictive de test : adaptation documentée, aucune validation terrain.\n')
    for artifact in state['artifacts']:
        if artifact['path']=='03_ARCHITECTURE.md':
            for item in state['evidence']:
                if item['id']==artifact['evidence_id']:
                    item['sha256']=studio.digest(architecture)
    for n in range(3):
        rel=f'PILOTES/pilote-{n}.md'
        write(project/rel,'# Pilote fictif\n\nLe texte est une fixture, pas un article commercial.\n')
        evidence('pilot-'+str(n),rel,'artifact')
        state['artifacts'].append({'id':'pilot-'+str(n),'path':rel,'kind':'pilot','content_type':['article','guide','comparison'][n],
                                  'owner':'EDITORIAL_LEAD','status':'REVIEWED','evidence_id':'pilot-'+str(n)})
    for pid,route in [('home','/'),('guide','/guide/'),('choice','/choix/'),('author','/auteur/')]:
        bp='BRIEFS/'+pid+'.md'
        write(project/bp,'# Brief fictif\n\nContrat uniquement, aucune source ni demande réelles.\n')
        evidence('brief-'+pid,bp,'artifact')
        state['artifacts'].append({'id':'brief-'+pid,'path':bp,'kind':'brief','content_type':None,
                                  'owner':'EDITORIAL_LEAD','status':'REVIEWED','evidence_id':'brief-'+pid})
        state['pages'].append({'id':pid,'path':route,'intent_id':'intent-'+pid,'title':'Titre fictif '+pid,'h1':'Question '+pid,
                               'public':True,'indexable':True,'canonical_path':route,'wave':'V1','kind':'editorial',
                               'brief_path':bp,'next_action':'Lire une explication pertinente','proof_plan':'Fiche de preuve fictive'})
    for n,(a,b) in enumerate([('home','guide'),('guide','choice'),('choice','home'),('home','author'),('author','home')]):
        state['links'].append({'id':f'L{n}','from':a,'to':b,'anchor':'Lire '+b,'placement':'corps','reason':'Parcours fictif','active_at_launch':True})
    state['sources']=[{'id':'S1','url':'https://example.org/fixture','status':'OBSERVED','consulted_at':'2026-10-08',
                       'note':'Source fictive — aucune requête externe','evidence_id':'source'}]
    state['claims']=[{'id':'C1','text':'Exemple de fait fictif de fixture','type':'FACT','source_ids':['S1'],'evidence_ids':[],'first_hand':False}]
    state['placements']=[{'id':'P1','page_id':'choice','paid':True,'rel':['sponsored'],'disclosure':'Exemple fictif de lien affilié',
                         'target_type':'product','label_target_type':'product','url':'https://example.org/product','url_status':'PROPOSED','active_at_launch':False}]
    for topic in ['idees','architecture','roadmap','production_pilote']:
        state['reviews'].append({'id':'review-'+topic,'topic':topic,'author_id':'TERRA','reviewer_id':'QA_LEAD','mode':'INDEPENDENT',
                                 'trace_id':'FICTION-NOT-A-REAL-SESSION','evidence_ids':['runtime','review'],'verdict':'APPROVED'})
    for req in state['requirements']:
        req.update(status='VERIFIE',evidence_ids=['review'])
    for gate in state['gates']:
        if gate['id']!='G6':
            gate.update(status='APPROVED',evidence_ids=['review'])
    complete_serp(project, state)
    complete_workflow(project, state)
    for review in state['reviews']:
        review['inputs_sha256']=studio.input_digest(state)
        review['reviewed_artifacts']=[{'path':a['path'],'sha256':studio.digest(project/a['path'])} for a in state['artifacts']]
        review['reviewed_artifacts'].append({'path':'research/serp.json','sha256':studio.digest(project/'research/serp.json')})
    return state


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.project=Path(self.tmp.name)/'project'
        self.state=fixture(self.project)
    def tearDown(self): self.tmp.cleanup()
    def result(self,state=None,stage='handoff'):
        write(self.project/'state.json',studio.json_text(state or self.state))
        return studio.validate_project(self.project,stage)
    def blocked(self,needle):
        r=self.result()
        self.assertEqual(r['status'],'BLOQUE',r)
        self.assertTrue(any(needle in e for e in r['errors']),r['errors'])
    def test_complete_fixture_is_only_structurally_valid(self):
        self.assertEqual(self.result()['status'],'STRUCTURE_OK')
    def test_fresh_template_is_not_handoff(self):
        other=Path(self.tmp.name)/'new'
        studio.init_project(other,'autre niche','vitrine',True)
        self.assertEqual(studio.validate_project(other,'handoff')['status'],'BLOQUE')
    def test_fresh_template_is_valid_draft(self):
        other=Path(self.tmp.name)/'new'
        studio.init_project(other,'autre niche','vitrine',True)
        self.assertEqual(studio.validate_project(other,'draft')['status'],'STRUCTURE_OK')
    def test_wrong_type_not_crash(self):
        self.state['pages']='incorrect'
        self.blocked('type attendu')
    def test_bool_is_not_integer(self):
        self.state['runtime']['executed_depth']=True
        self.blocked('type attendu')
    def test_unknown_field(self):
        self.state['guaranteed_rank']=1
        self.blocked('champ inconnu')
    def test_missing_field(self):
        del self.state['personna']
        self.blocked('champ obligatoire')
    def test_empty_niche(self):
        self.state['niche']=''
        self.blocked('Niche et type')
    def test_missing_personna(self):
        self.state['personna']['status']='NOT_LOCATED'
        self.blocked('/personna canonique')
    def test_untrained_role(self):
        self.state['roles'][0]['training_status']='A_FORMER'
        self.blocked('/personna non validé')
    def test_fake_training_evidence_kind(self):
        self.state['roles'][0]['evidence_ids']=['review']
        self.blocked('preuve de formation')
    def test_three_delegates(self):
        self.state['runtime']['max_active_delegates']=3
        self.blocked('deux délégués')
    def test_recursive_delegate(self):
        self.state['runtime']['executed_depth']=2
        self.blocked('aucun descendant')
    def test_unavailable_delegation(self):
        self.state['runtime']['delegation_available']=False
        self.blocked('sans capacité')
    def test_unverified_model_selection(self):
        self.state['runtime']['model_selection_verified']=False
        self.blocked('modèles vérifiés')
    def test_cannot_turn_off_independent_gate(self):
        self.state['runtime']['independent_review_required']=False
        self.blocked('ne pas la désactiver')
    def test_role_hierarchy_cycle(self):
        self.state['roles'][0]['parent_id']='TERRA'
        self.blocked('cycle hiérarchique')
    def test_unknown_role_parent(self):
        self.state['roles'][0]['parent_id']='UNKNOWN'
        self.blocked('parent inconnu')
    def test_unassigned_reviewer(self):
        next(r for r in self.state['roles'] if r['id']=='QA_LEAD')['assigned']=False
        self.blocked('Acteur de revue non affecté')
    def test_omitted_new_seo_skill(self):
        self.state['discovered_seo_skills'].append('seo-future-module')
        self.blocked('découvert non classé')
    def test_missing_core_skill(self):
        self.state['dependencies']=[d for d in self.state['dependencies'] if d['name']!='brain']
        self.blocked('Socle de dépendances incomplet')
    def test_unread_skill(self):
        self.state['dependencies'][0]['status']='A_LIRE'
        self.blocked('dépendance non lue')
    def test_dependency_exclusion_reason(self):
        self.state['dependencies'][-1]['status']='PREPARE_PHASE_ULTERIEURE'
        self.blocked('sans motif')
    def test_evidence_hash_changed(self):
        write(self.project/'proof.txt','Modification après la revue')
        self.blocked('périmée')
    def test_evidence_traversal(self):
        self.state['evidence'][0]['path']='../outside.txt'
        self.blocked('Chemin interdit')
    def test_unknown_evidence_in_draft(self):
        self.state['requirements'][0]['evidence_ids']=['missing']
        r=self.result(stage='draft')
        self.assertEqual(r['status'],'BLOQUE')
    def test_missing_artifact(self):
        (self.project/'07_TECHNIQUE.md').unlink()
        self.blocked('Fichier absent')
    def test_scaffold_not_accepted(self):
        path=self.project/'04_DESIGN.md'
        write(path,'# Design\n\nA_COMPLETER\n')
        next(e for e in self.state['evidence'] if e['path']=='04_DESIGN.md')['sha256']=studio.digest(path)
        self.blocked('stade template')
    def test_pilot_minimum(self):
        self.state['artifacts']=[a for a in self.state['artifacts'] if a['id']!='pilot-2']
        self.blocked('Lot pilote incomplet')
    def test_pilot_exception_requires_motivated_decision(self):
        self.state['artifacts']=[a for a in self.state['artifacts'] if a['id']!='pilot-2']
        self.state['decisions']=[{'id':'D1','authority':'ASTRA','summary':'Dans cette fixture, deux contenus couvrent le périmètre réduit.','scope':'pilot_scope','evidence_ids':['review'],'status':'RESOLVED'}]
        self.assertEqual(self.result()['status'],'STRUCTURE_OK')
    def test_first_hand_claim_needs_test_report(self):
        self.state['claims'][0]['first_hand']=True
        self.blocked('Expérience/essai sans rapport')
    def test_fact_needs_source(self):
        self.state['claims'][0]['source_ids']=[]
        self.blocked('Fait sans source')
    def test_non_observed_source_cannot_support_fact(self):
        self.state['sources'][0]['status']='NOT_OBSERVED'
        self.blocked('source absente/non observée')
    def test_intent_collision(self):
        self.state['pages'][1]['intent_id']=self.state['pages'][0]['intent_id']
        self.blocked('Intention propriétaire dupliquée')
    def test_duplicate_title(self):
        self.state['pages'][1]['title']=self.state['pages'][0]['title']
        self.blocked('Title dupliqué')
    def test_private_page_not_indexable(self):
        self.state['pages'][1]['public']=False
        self.blocked('privée indexable')
    def test_orphan(self):
        self.state['links']=[]
        self.blocked('Page orpheline')
    def test_unknown_link_target(self):
        self.state['links'][0]['to']='missing'
        self.blocked('Lien vers page inconnue')
    def test_future_page_not_linked_at_launch(self):
        self.state['pages'][1]['wave']='LATER'
        self.blocked('page future')
    def test_brief_missing(self):
        self.state['pages'][1]['brief_path']=None
        self.blocked('Brief V1 absent')
    def test_paid_link_needs_sponsored(self):
        self.state['placements'][0]['rel']=[]
        self.blocked('sponsored/disclosure')
    def test_paid_link_needs_visible_disclosure(self):
        self.state['placements'][0]['disclosure']=''
        self.blocked('sponsored/disclosure')
    def test_misleading_search_destination(self):
        self.state['placements'][0]['target_type']='search'
        self.blocked('Destination annoncée')
    def test_unsafe_partner_url(self):
        self.state['placements'][0]['url']='javascript:alert(1)'
        self.blocked('URL partenaire non HTTP')
    def test_credentials_not_in_partner_url(self):
        self.state['placements'][0]['url']='https://user:secret@example.org/product'
        self.blocked('contenant des identifiants')
    def test_self_review_cannot_claim_independence(self):
        self.state['reviews'][0]['reviewer_id']='TERRA'
        self.blocked('Indépendance déclarée')
    def test_missing_real_trace_structure(self):
        self.state['reviews'][0]['trace_id']=None
        self.blocked('Indépendance déclarée')
    def test_missing_review_topic(self):
        self.state['reviews']=[r for r in self.state['reviews'] if r['topic']!='roadmap']
        self.blocked('Confrontation approuvée absente')
    def test_unresolved_objection(self):
        self.state['objections']=[{'id':'O1','severity':'P1','status':'OPEN','decision_id':None,'evidence_ids':['review']}]
        self.blocked('Objection bloquante ouverte')
    def test_arbitration_without_astra_decision(self):
        self.state['objections']=[{'id':'O1','severity':'P1','status':'ARBITRATED','decision_id':None,'evidence_ids':['review']}]
        self.blocked('Arbitrage Astra résolu absent')
    def test_cannot_waive_mandatory_requirement(self):
        self.state['requirements'][0].update(status='NON_APPLICABLE',decision_id=None)
        self.blocked('Dérogation interdite')
    def test_missing_gate(self):
        self.state['gates']=self.state['gates'][1:]
        self.blocked('Gate non approuvé')
    def test_release_requires_permission_and_live_proof(self):
        self.assertEqual(self.result(stage='release')['status'],'BLOQUE')
    def test_release_fixture_validates_structure_only(self):
        self.state['gates'][-1].update(status='APPROVED',evidence_ids=['review'])
        self.state['permissions']['publication']=True
        self.state['live_evidence_ids']=['http','authorization']
        from technical_fixture import complete_technical
        complete_technical(self.project,self.state)
        self.assertEqual(self.result(stage='release')['status'],'BLOQUE')
        self.assertTrue(any('Livraison' in e for e in self.result(stage='release')['errors']))


    def test_business_inputs_change_invalidates_approvals(self):
        self.state['pages'][0]['next_action']='Nouvelle étape différente'
        self.blocked('Revue caduque : entrées métier')
    def test_updated_artifact_hash_does_not_refresh_review(self):
        p=self.project/'04_DESIGN.md'
        write(p,'# Direction modifiée après approbation\n')
        next(e for e in self.state['evidence'] if e['path']=='04_DESIGN.md')['sha256']=studio.digest(p)
        self.blocked('Revue caduque : fichier modifié')
    def test_review_snapshot_missing(self):
        self.state['reviews'][0]['reviewed_artifacts']=[]
        self.blocked('Revue sans instantané')
    def test_readonly_snapshot_is_not_approval(self):
        self.result()
        before=studio.digest(self.project/'state.json')
        snap=studio.review_snapshot(self.project)
        self.assertEqual(snap['inputs_sha256'],studio.input_digest(self.state))
        self.assertEqual(before,studio.digest(self.project/'state.json'))
    def test_valid_optional_exception(self):
        r=next(r for r in self.state['requirements'] if r['id']=='R21')
        r.update(status='NON_APPLICABLE',decision_id='D1')
        self.state['decisions']=[{'id':'D1','authority':'ASTRA','summary':'Canal IA exclu du périmètre de cette fixture.','scope':'R21','evidence_ids':['review'],'status':'RESOLVED'}]
        self.assertEqual(self.result()['status'],'STRUCTURE_OK')
    def test_exception_must_target_correct_requirement(self):
        r=next(r for r in self.state['requirements'] if r['id']=='R21')
        r.update(status='NON_APPLICABLE',decision_id='D1')
        self.state['decisions']=[{'id':'D1','authority':'ASTRA','summary':'Décision sans rapport.','scope':'OTHER','evidence_ids':['review'],'status':'RESOLVED'}]
        self.blocked('Dérogation interdite')


class FilesystemTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.base=Path(self.tmp.name)
    def tearDown(self): self.tmp.cleanup()
    def test_json_duplicate_keys_are_rejected(self):
        path=self.base/'ambiguous.json';write(path,'{"publication":false,"publication":true}')
        with self.assertRaises(ValueError):studio.load(path)
    def test_non_json_nan_is_rejected(self):
        path=self.base/'nan.json';write(path,'{"value":NaN}')
        with self.assertRaises(ValueError):studio.load(path)
    def test_dry_run_creates_nothing(self):
        target=self.base/'project'
        result=studio.init_project(target,'niche','site',False)
        self.assertEqual(result['status'],'DRY_RUN');self.assertFalse(target.exists())
    def test_init_is_idempotent(self):
        target=self.base/'project';studio.init_project(target,'niche','site',True)
        before=studio.digest(target/'state.json')
        self.assertEqual(studio.init_project(target,'niche','site',True)['status'],'EXISTS_UNCHANGED')
        self.assertEqual(before,studio.digest(target/'state.json'))
    def test_init_refuses_other_project(self):
        target=self.base/'project';studio.init_project(target,'niche','site',True)
        with self.assertRaises(ValueError):studio.init_project(target,'autre','site',True)
    def test_init_preserves_existing_files(self):
        target=self.base/'project';write(target/'00_CADRAGE.md','Travail utilisateur')
        with self.assertRaises(ValueError):studio.init_project(target,'niche','site',True)
        self.assertEqual((target/'00_CADRAGE.md').read_text(),'Travail utilisateur')
    def test_inventory_dynamic_seo_and_self_exclusion(self):
        for name in ['brain','seo-new','seo-studio-2','personna']:
            write(self.base/name/'SKILL.md',f'---\nname: {name}\ndescription: Test\n---\nContenu\n')
        result=studio.inventory([self.base]);names={e['name'] for e in result['entries']}
        self.assertEqual(names,{'brain','seo-new','personna'})
    def test_inventory_description_candidates(self):
        write(self.base/'writer'/'SKILL.md','---\nname: writer\ndescription: SEO content\n---\nInstructions\n')
        r=studio.inventory([self.base])
        self.assertEqual(r['entries'][0]['kind'],'SEO_DESCRIPTION_CANDIDATE')
    def test_inventory_duplicate_versions(self):
        for folder,text in [('a','First'),('b','Second')]:
            write(self.base/folder/'SKILL.md',f'---\nname: seo\ndescription: Test\n---\n{text}\n')
        self.assertFalse(studio.inventory([self.base])['duplicates']['seo']['identical'])
    def test_safe_path_blocks_absolute_and_windows(self):
        for path in ['/etc/passwd','../other','C:/Windows/file','C:relative','a\\b','./file']:
            with self.subTest(path=path),self.assertRaises(ValueError):studio.safe_path(self.base,path)
    def test_safe_path_blocks_symlink(self):
        outside=self.base/'outside';write(outside/'a.txt','secret')
        project=self.base/'p';project.mkdir()
        try:(project/'link').symlink_to(outside,target_is_directory=True)
        except (OSError,NotImplementedError):self.skipTest('Symlinks non autorisés par cet OS')
        with self.assertRaises(ValueError):studio.safe_path(project,'link/a.txt',True)
    def make_package(self):
        package=self.base/'source'
        write(package/'SKILL.md','---\nname: seo-studio-2\ndescription: Fixture\n---\nFiction\n')
        companion=package/'seo-site-preproduction'
        write(companion/'SKILL.md','---\nname: seo-site-preproduction\ndescription: Fixture compagnon\n---\nFiction\n')
        write(companion/'MANIFEST.sha256.json',studio.json_text(studio.file_signature(companion)))
        write(package/'MANIFEST.sha256.json',studio.json_text({p:h for p,h in studio.file_signature(package).items() if not p.startswith('seo-site-preproduction/')}))
        return package
    def test_manifest_cannot_certify_empty_skill(self):
        package=self.base/'empty'
        write(package/'MANIFEST.sha256.json','{}')
        self.assertEqual(studio.check_package(package)['status'],'BLOQUE')
    def test_manifest_detects_tamper(self):
        package=self.make_package();write(package/'SKILL.md','alteration')
        self.assertEqual(studio.check_package(package)['status'],'BLOQUE')
    def test_manifest_detects_extra_file(self):
        package=self.make_package();write(package/'extra.md','extra')
        self.assertEqual(studio.check_package(package)['status'],'BLOQUE')
    def test_install_dry_run(self):
        package=self.make_package();dest=self.base/'skills'
        self.assertEqual(installer.install(package,dest)['status'],'DRY_RUN')
        self.assertFalse(dest.exists())
    def test_install_and_idempotence(self):
        package=self.make_package();dest=self.base/'skills'
        self.assertEqual(installer.install(package,dest,True)['status'],'FILES_INSTALLED')
        self.assertEqual(installer.install(package,dest,True)['status'],'ALREADY_IDENTICAL')
    def test_install_refuses_customized_copy(self):
        package=self.make_package();dest=self.base/'skills'
        installer.install(package,dest,True);write(dest/'seo-studio-2'/'custom.md','user')
        with self.assertRaises(ValueError):installer.install(package,dest,True)
        self.assertEqual((dest/'seo-studio-2'/'custom.md').read_text(),'user')
    def test_install_refuses_missing_companion(self):
        package=self.make_package()
        import shutil
        shutil.rmtree(package/'seo-site-preproduction')
        with self.assertRaisesRegex(ValueError,'bundle source'):installer.install(package,self.base/'skills',True)
    def test_install_refuses_corrupt_package(self):
        package=self.make_package();write(package/'SKILL.md','altered')
        with self.assertRaises(ValueError):installer.install(package,self.base/'skills',True)

if __name__=='__main__':unittest.main()
