"""Synthetic protocol fixtures. No human approval, product expertise or client delivery claimed."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import copy
import base64
import json
import struct
import sys
import tempfile
import unittest
from unittest.mock import patch
import zlib

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import studio
import delivery as d
from volume import validate_volume

def write(path, data):
    path.parent.mkdir(parents=True,exist_ok=True)
    if isinstance(data,bytes): path.write_bytes(data)
    elif isinstance(data,(dict,list)): path.write_text(json.dumps(data,ensure_ascii=False),encoding="utf-8")
    else: path.write_text(data,encoding="utf-8")

def png(width,height):
    def chunk(t,b):
        return struct.pack(">I",len(b))+t+b+struct.pack(">I",zlib.crc32(t+b)&0xffffffff)
    return b"\x89PNG\r\n\x1a\n"+chunk(b"IHDR",struct.pack(">IIBBBBB",width,height,8,2,0,0,0))+chunk(b"IDAT",zlib.compress((b"\0"+b"\xff\xff\xff"*width)*height))+chunk(b"IEND",b"")

class DeliveryCase:
    def __init__(self,root,kind="NEW"):
        self.root=root;self.project=root/"proof";self.source=root/"source";self.site=root/"dist"
        self.project.mkdir();self.source.mkdir();self.site.mkdir()
        self.state={"run_id":"SYNTHETIC_PROTOCOL_ONLY","niche":"Documentation de validation",
                    "site_type":"documentation","pages":[]}
        self.plan=studio.load(studio.ROOT/"templates/execution.json")
        self.plan.update(run_id=self.state["run_id"],site_kind=kind,affiliation=False,entry_page_id="home")
        self.plan["pilot_ids"]=["home","guide","method"]
        self.plan["features"]=[{"id":ident,"decision":"KEEP" if ident=="internal_search" else "EXCLUDE",
                               "reason":"Synthetic documentation fixture, no optional interactive demo component"}
                              for ident in sorted(d.TEMPLATE_FEATURES)]
        for pid,route in [("home","/"),("guide","/guide/"),("method","/method/")]:
            output="index.html" if pid=="home" else pid+"/index.html"
            self.state["pages"].append({"id":pid,"path":route,"h1":"Question "+pid,"public":True,
                "indexable":True,"canonical_path":route,"wave":"V1","kind":"landing" if pid=="home" else "guide"})
            editorial={"answer":"Réponse propre à "+pid,"limitation":"Limite expliquée pour "+pid,
                       "next_action":"Lire la suite de "+pid}
            self.plan["pages"].append({"id":pid,"output_path":output,"product_ids":[],
                "programmatic":False,"editorial":editorial,
                "search":{"query":"guide","expected_path":"/guide/"}})
            html=self.html(pid,route,editorial)
            write(self.source/"content"/output,html)
        builder = "from pathlib import Path\nimport shutil,sys\nshutil.copytree(Path('content'),Path(sys.argv[1]),dirs_exist_ok=True)\n"
        write(self.source/"builder.py",builder)
        for phase,names in d.DOCS.items():
            for name in names: write(self.project/name,"# Fixture de protocole\nContenu de travail synthétique, non destiné à une livraison client.")
        write(self.project/"PROJECT_SKIN.yaml",{"status":"APPROVED","visual_concept":"SYNTHETIC fixture"})
        write(self.project/"trace.txt","SYNTHETIC TEST TRACE; not an actual user approval or agent call.")
        write(self.project/"desktop.png",png(1440,900));write(self.project/"mobile.png",png(390,844))
        self.plan["directions"]=[{"reference_urls":["https://reference.invalid/fixture"],
            "desktop":"desktop.png","mobile":"mobile.png"} for _ in range(2)]
        self.plan["batches"]=[{"page_ids":self.plan["pilot_ids"],"review_path":"batches.json"}]
        for phase in d.PHASES:
            self.review(phase)
        self.volume()
        self.save()

    def html(self,pid,route,ed):
        links='<nav><a href="/">Accueil</a><a href="/guide/">Guide</a><a href="/method/">Méthode</a></nav>'
        if pid=="home":
            artwork=base64.b64encode(png(160,90)).decode()
            links+='<section data-hero style="position:relative;isolation:isolate;height:180px"><img data-hero-artwork alt="" src="data:image/png;base64,'+artwork+'" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-1"><p>Hero de protocole synthétique</p></section>'
        search="" if pid=="home" else """<form id="search"><label>Recherche<input type="search" aria-label="Recherche"></label></form>
<div data-search-results><a href="/guide/">Guide de validation</a></div>
<script>document.querySelector('#search').onsubmit=e=>{e.preventDefault();document.querySelector('[data-search-results] a').hidden=!document.querySelector('input').value.toLowerCase().includes('guide');}</script>"""
        return '<!doctype html><html lang="fr"><head><title>Fixture '+pid+'</title><link rel="canonical" href="https://fixture.invalid'+route+'"></head><body>'+links+'<main><h1>Question '+pid+'</h1>'+search+''.join('<p>'+x+'</p>' for x in ed.values())+'</main></body></html>'

    def review(self,phase):
        scope=self.plan["pilot_ids"] if phase in ("pilots","batches","qa") else ["project"]
        write(self.project/(phase+".json"),{"phase":phase,"status":"PASS","findings":[],
             "checks":sorted(d.CHECKS[phase]),"scope":scope,"reviewer_type":"HUMAN" if phase=="design" else "AGENT",
             "reviewer":"SYNTHETIC_CHECKER","author":"SYNTHETIC_WRITER","trace_path":"trace.txt"})

    def volume(self,target=3,planned=3):
        write(self.project/"competitor.json",{"urls":["https://competitor.invalid/a"],"complete":True})
        write(self.project/"demand.txt","SYNTHETIC demand coverage; not live SERP.")
        write(self.project/"research/volume.json",{"run_id":self.state["run_id"],"niche":self.state["niche"],
            "observed_at":d.now().isoformat(),"competitors":[{"domain":"competitor.invalid",
            "source_url":"https://competitor.invalid/sitemap.xml","coverage":"CRAWL","url_count":1,
            "evidence_path":"competitor.json","limitations":"Synthetic test only"}],
            "families":[{"id":"docs","candidate_urls":target,"eligible_urls":target,"excluded_urls":0,
            "rationale":"Synthetic coverage","demand_evidence_path":"demand.txt","data_feasibility":"Synthetic fixtures"}],
            "target_urls":target,"delivery_urls":planned,"backlog_urls":target-planned,
            "strategy":"Synthetic pipeline coverage","uncertainty":"No measured demand, test only"})

    def save(self):
        write(self.project/"state.json",self.state);write(self.project/"EXECUTION.json",self.plan)
    def reload(self):
        self.plan=studio.load(self.project/"EXECUTION.json")
    def record(self,phase):
        result=d.record(self.project,phase,phase+".json",self.site,self.source);self.reload();return result
    def prepare_build(self):
        for phase in ("audit","design","products"):self.record(phase)
        result=d.run_build(self.project,self.site,self.source,[sys.executable,"builder.py",str(self.site)])
        self.reload();assert result["status"]=="BUILD_OK"
    def through_pilots(self):
        self.prepare_build();self.record("pilots")
    def browser_fixture(self):
        runs=[]
        for item in self.plan["pages"]:
            for profile in ("desktop","mobile"):
                runs.append({"page_id":item["id"],"profile":profile,"html_sha256":studio.digest(self.site/item["output_path"]),
                 "checks":{k:True for k in ("rendered","images","entry_products_visible","search","search_empty","navigation","hero_artwork")},
                 "errors":[],"screenshot_path":profile+".png","screenshot_sha256":studio.digest(self.project/(profile+".png"))})
        write(self.project/"EXECUTION-browser.json",{"run_id":self.state["run_id"],"tool":"Playwright","version":"SYNTHETIC",
          "site_sha256":d.canonical(d.tree(self.site)),"status":"PASS","errors":[],"runs":runs})
        for item in self.plan["pages"]:
            self.plan["captures"].append({"page_id":item["id"],"html_sha256":studio.digest(self.site/item["output_path"]),
                                         "desktop":"desktop.png","mobile":"mobile.png"})
        self.save()

class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.c=DeliveryCase(Path(self.tmp.name))
    def check(self,through="qa"):
        return d.validate_execution(self.c.project,site_root=self.c.site,source_root=self.c.source,through=through)
    def test_fresh_contract_cannot_deliver(self):
        self.assertIn("audit",self.check()[0])
    def test_cannot_skip_design(self):
        self.c.record("audit")
        with self.assertRaisesRegex(ValueError,"design"):self.c.record("products")
    def test_design_requires_actual_user_review_type(self):
        self.c.record("audit")
        p=self.c.project/"design.json";r=studio.load(p);r["reviewer_type"]="AGENT";write(p,r)
        with self.assertRaisesRegex(ValueError,"utilisateur"):self.c.record("design")
    def test_modified_design_invalidates_proof(self):
        self.c.prepare_build();write(self.c.project/"PROJECT_SKIN.yaml","Modified skin")
        self.assertIn("design",self.check("products")[0])
    def test_trace_edit_invalidates_proof(self):
        self.c.record("audit");write(self.c.project/"trace.txt","Changed synthetic trace")
        self.assertIn("Trace",self.check("audit")[0])
    def test_build_runs_real_process_and_records_log(self):
        self.c.prepare_build()
        self.assertEqual(len(list(self.c.site.rglob("*.html"))),3)
        self.assertEqual(self.c.plan["build_receipt"]["returncode"],0)
    def test_failed_build_invalidates_old_build_and_pilots(self):
        self.c.through_pilots()
        r=d.run_build(self.c.project,self.c.site,self.c.source,[sys.executable,"-c","raise SystemExit(2)"])
        self.c.reload();self.assertEqual(r["status"],"BLOCKED");self.assertNotIn("pilots",self.c.plan["receipts"])
        with self.assertRaisesRegex(ValueError,"Build"):self.c.record("pilots")
    def test_source_change_invalidates_build(self):
        self.c.prepare_build();write(self.c.source/"new.css","body{}")
        with self.assertRaisesRegex(ValueError,"Build"):self.c.record("pilots")
    def test_missing_page_blocks_pilots(self):
        self.c.prepare_build();(self.c.site/"guide/index.html").unlink()
        with self.assertRaises(ValueError):self.c.record("pilots")
    def test_wrong_h1_blocks(self):
        self.c.prepare_build();p=self.c.site/"guide/index.html";write(p,p.read_text(encoding="utf-8").replace("Question guide","Incorrect"))
        with self.assertRaisesRegex(ValueError,"H1"):d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["guide"])
    def test_unchanged_demo_is_rejected(self):
        self.c.prepare_build();write(self.c.site/"index.html",(studio.ROOT/"seo-site-preproduction/assets/template-demo/index.html").read_bytes())
        with self.assertRaisesRegex(ValueError,"Démo"):d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["home"])
    def test_editorial_answer_must_be_in_real_page(self):
        self.c.prepare_build();self.c.plan["pages"][0]["editorial"]["answer"]="Not actually written"
        with self.assertRaisesRegex(ValueError,"éditoriale"):d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["home"])
    def test_hidden_provisional_text_not_reader_content(self):
        doc=d.Page("<h1>Visible</h1><div hidden>TODO</div><script>TODO</script>")
        self.assertNotIn("TODO",doc.text)
    def test_search_required_on_content(self):
        self.c.prepare_build();p=self.c.site/"guide/index.html";write(p,p.read_text(encoding="utf-8").replace('type="search"','type="text"'))
        with self.assertRaisesRegex(ValueError,"Recherche"):d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["guide"])
    def test_thin_pseo_cannot_be_indexed(self):
        self.c.prepare_build();self.c.plan["pages"][1]["programmatic"]=True
        with self.assertRaisesRegex(ValueError,"pSEO"):d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["guide"])
    def test_pseo_reused_sections_blocked(self):
        self.c.prepare_build()
        for x in self.c.plan["pages"][1:]:
            x["programmatic"]=True;x["pseo_sections"]={"verdict":"Réponse","comparison":"Chiffre 12","usage":"Usage"}
            p=self.c.site/x["output_path"];write(p,p.read_text(encoding="utf-8")+"<p>Réponse Chiffre 12 Usage</p>")
        with self.assertRaisesRegex(ValueError,"réutilisé"):d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["guide","method"])
    def test_incomplete_batches_block(self):
        self.c.through_pilots();self.c.plan["batches"][0]["page_ids"]=["home"];self.c.save()
        with self.assertRaisesRegex(ValueError,"Lots"):self.c.record("batches")
    def test_extra_unplanned_output_blocks_qa(self):
        self.c.through_pilots();self.c.record("batches");self.c.browser_fixture()
        write(self.c.site/"unplanned.html","<h1>Extra</h1>")
        with self.assertRaises(ValueError):self.c.record("qa")
    def test_browser_cannot_be_marked_not_run(self):
        self.c.through_pilots();self.c.record("batches");self.c.browser_fixture()
        p=self.c.project/"EXECUTION-browser.json";r=studio.load(p);r["status"]="NOT_RUN";write(p,r)
        with self.assertRaisesRegex(ValueError,"navigateur"):self.c.record("qa")
    def test_qa_requires_existing_technical_audit(self):
        self.c.through_pilots();self.c.record("batches");self.c.browser_fixture()
        with self.assertRaisesRegex(ValueError,"Recette HTTP"):self.c.record("qa")
    def test_complete_synthetic_contract_checks_then_stale_page_fails(self):
        self.c.through_pilots();self.c.record("batches");self.c.browser_fixture()
        with patch("technical_audit.validate_technical",return_value=([],[])):
            self.c.record("qa")
            self.assertEqual(self.check(),[])
            write(self.c.site/"index.html","Changed build output")
            self.assertTrue(self.check())
    def test_migration_needs_baseline_or_explicit_user_waiver(self):
        self.c.plan["site_kind"]="MIGRATION";self.c.save()
        with self.assertRaisesRegex(ValueError,"huit pages"):self.c.record("audit")
    def test_eight_duplicate_baseline_routes_not_coverage(self):
        self.c.plan.update(site_kind="MIGRATION",baseline=[{"route":"/","kind":str(i),"desktop":"desktop.png","mobile":"mobile.png"} for i in range(8)])
        self.c.save()
        with self.assertRaisesRegex(ValueError,"répétées"):self.c.record("audit")
    def test_screenshot_must_be_png_not_text(self):
        write(self.c.project/"fake.png","not an image")
        with self.assertRaisesRegex(ValueError,"PNG"):d.screenshot(self.c.project,"fake.png","desktop")
    def test_path_escape_refused(self):
        self.c.prepare_build();self.c.plan["pages"][0]["output_path"]="../secret.html"
        with self.assertRaises(ValueError):d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["home"])
    def test_template_interactions_cannot_be_silently_omitted(self):
        self.c.plan.pop("features")
        with self.assertRaisesRegex(ValueError,"interactions"):d.feature_plan(self.c.project,self.c.state,self.c.plan)
    def test_content_search_cannot_be_excluded(self):
        next(f for f in self.c.plan["features"] if f["id"]=="internal_search")["decision"]="EXCLUDE"
        with self.assertRaisesRegex(ValueError,"Recherche"):d.feature_plan(self.c.project,self.c.state,self.c.plan)
    def test_retained_feature_requires_executable_cases(self):
        feature=next(f for f in self.c.plan["features"] if f["id"]=="saved_selection")
        feature.update(decision="ADAPT",case_path="cases/save.json")
        case={"feature_id":"saved_selection","scenarios":[{"page_id":"home","profile":profile,"actions":[{"action":"click","selector":"button"}],"expects":[{"selector":"p","unknown":True}]} for profile in ("desktop","mobile")]}
        write(self.c.project/"cases/save.json",case)
        with self.assertRaisesRegex(ValueError,"contrôle reconnu"):d.feature_plan(self.c.project,self.c.state,self.c.plan)
        for scenario in case["scenarios"]:scenario["expects"]=[{"selector":"p","count":1}]
        write(self.c.project/"cases/save.json",case)
        self.assertEqual(len(d.feature_plan(self.c.project,self.c.state,self.c.plan)),1)
    def test_design_and_qa_cannot_omit_niche_depth_or_component_review(self):
        for phase in ("design","qa"):
            p=self.c.project/(phase+".json");review=studio.load(p)
            review["checks"].remove("niche_fit");write(p,review)
            scope=self.c.plan["pilot_ids"] if phase=="qa" else ["project"]
            with self.assertRaises(ValueError):d.proof(self.c.project,phase+".json",phase,scope)
    def test_hero_browser_check_cannot_be_omitted(self):
        self.c.through_pilots();self.c.record("batches");self.c.browser_fixture()
        p=self.c.project/"EXECUTION-browser.json";report=studio.load(p)
        report["runs"][0]["checks"].pop("hero_artwork");write(p,report)
        with self.assertRaisesRegex(ValueError,"navigateur"):self.c.record("qa")
    def test_large_volume_has_no_fixed_url_cap(self):
        state=copy.deepcopy(self.c.state);state["pages"]=[{"public":True,"wave":"V1"}]*100001
        self.c.volume(100001,100001)
        self.assertEqual(validate_volume(self.c.project,state,self.c.plan)["target_urls"],100001)
    def test_unapproved_smaller_delivery_blocks(self):
        self.c.volume(10000,3)
        with self.assertRaises((ValueError,KeyError)):validate_volume(self.c.project,self.c.state,self.c.plan)
    def test_competitor_count_cannot_be_invented(self):
        p=self.c.project/"research/volume.json";data=studio.load(p);data["competitors"][0]["url_count"]=764;write(p,data)
        with self.assertRaisesRegex(ValueError,"Volume concurrent"):validate_volume(self.c.project,self.c.state,self.c.plan)
    def test_sitemap_index_not_counted_as_page_urls(self):
        p=self.c.project/"research/volume.json";data=studio.load(p);data["competitors"][0].update(evidence_path="sitemap.xml",coverage="SITEMAP");write(p,data)
        write(self.c.project/"sitemap.xml","<sitemapindex><sitemap><loc>https://competitor.invalid/1.xml</loc></sitemap></sitemapindex>")
        with self.assertRaisesRegex(ValueError,"index"):validate_volume(self.c.project,self.c.state,self.c.plan)
    def test_build_proofs_do_not_recurse_into_source_when_nested(self):
        nested=self.c.source/"proof";self.c.project.rename(nested);self.c.project=nested
        self.c.prepare_build();self.assertEqual(self.check("products"),[])
    def test_runtime_report_covers_each_page_and_both_profiles(self):
        self.c.through_pilots();self.c.record("batches");self.c.browser_fixture()
        p=self.c.project/"EXECUTION-browser.json";data=studio.load(p);data["runs"].pop();write(p,data)
        with self.assertRaisesRegex(ValueError,"Couverture navigateur"):self.c.record("qa")

if __name__=="__main__": unittest.main()
