"""Real localhost HTTP, entirely synthetic products. No actual merchant/program certified."""
from datetime import timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import copy
import sys
import tempfile
import threading
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
from test_delivery import DeliveryCase, write, png
import delivery as d
import studio

class ProductHandler(BaseHTTPRequestHandler):
    def log_message(self,*args): pass
    def do_GET(self):
        code,headers,body=self.server.responses.get(self.path,(404,{},b"missing"))
        self.send_response(code)
        for k,v in headers.items(): self.send_header(k,v)
        self.end_headers();self.wfile.write(body)

class ProductDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.c=DeliveryCase(Path(self.tmp.name));self.c.plan["affiliation"]=True
        self.server=ThreadingHTTPServer(("127.0.0.1",0),ProductHandler)
        self.server.responses={
          "/product":(200,{"Content-Type":"text/html"},b"<title>Fixture-1</title><h1>Fixture-1</h1>"),
          "/affiliate":(302,{"Location":"/product"},b"redirect"),
          "/image":(200,{"Content-Type":"image/png"},png(32,32))}
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True);self.thread.start()
        self.addCleanup(self.stop)
        self.base="http://127.0.0.1:"+str(self.server.server_port)
        self.row={"id":"SKU","nom":"Fixture product","marque":"Fixture","modèle":"Fixture-1",
            "source_url":self.base+"/product","lien_affilié":self.base+"/affiliate",
            "image_url":self.base+"/image","prix":12.5,"date_prix":d.now().date().isoformat(),
            "date_vérification":d.now().date().isoformat(),"statut":"VERIFIE","devise":"EUR",
            "source_evidence_path":"source.json","program_evidence_path":"program.json"}
        write(self.c.project/"source.json",{"reference":"Fixture-1","source_url":self.row["source_url"],
            "session_reference":"SYNTHETIC_TEST_ONLY","read_at":d.now().isoformat(),"source_kind":"MERCHANT"})
        write(self.c.project/"program.json",{"status":"ACTIVE","program":"SYNTHETIC_PROGRAM",
            "account_evidence":"account.txt"})
        write(self.c.project/"account.txt","Synthetic program evidence, not a real account")
        self.save()
    def stop(self):
        self.server.shutdown();self.server.server_close();self.thread.join()
    def save(self):
        write(self.c.project/"PRODUCTS/products.json",[self.row]);self.c.save()
    def probe(self):
        return d.probe_products(self.c.project,["127.0.0.1"],True)
    def test_real_http_and_redirect_success(self):
        report=self.probe()
        self.assertEqual(report["status"],"PASS")
        self.assertEqual(report["products"][0]["checks"]["lien_affilié"]["redirects"][0]["status"],302)
    def test_each_mandatory_field_is_required(self):
        original=copy.deepcopy(self.row)
        for key in list(self.row):
            with self.subTest(key=key):
                self.row=copy.deepcopy(original);self.row.pop(key);self.save()
                with self.assertRaises((ValueError,KeyError)):d.catalogue(self.c.project,self.c.plan)
    def test_missing_affiliate_program_blocks(self):
        write(self.c.project/"program.json",{"status":"PENDING","program":"fixture","account_evidence":"account.txt"})
        with self.assertRaisesRegex(ValueError,"active"):d.catalogue(self.c.project,self.c.plan)
    def test_competitor_not_an_authorized_product_source(self):
        p=self.c.project/"source.json";r=studio.load(p);r["source_kind"]="COMPETITOR";write(p,r)
        with self.assertRaisesRegex(ValueError,"officielle"):d.catalogue(self.c.project,self.c.plan)
    def test_old_session_source_blocks(self):
        p=self.c.project/"source.json";r=studio.load(p);r["read_at"]=(d.now()-timedelta(days=2)).isoformat();write(p,r)
        with self.assertRaisesRegex(ValueError,"session"):d.catalogue(self.c.project,self.c.plan)
    def test_wrong_reference_in_source_blocks_real_probe(self):
        self.server.responses["/product"]=(200,{"Content-Type":"text/html"},b"<title>Fixture-2</title><h1>Fixture-2</h1>")
        self.assertEqual(self.probe()["status"],"BLOCKED")
    def test_wrong_final_merchant_reference_blocks(self):
        self.server.responses["/affiliate"]=(200,{"Content-Type":"text/html"},b"<title>Other</title><h1>Other model</h1>")
        self.assertEqual(self.probe()["status"],"BLOCKED")
    def test_antibot_does_not_count_as_success(self):
        self.server.responses["/product"]=(200,{"Content-Type":"text/html"},b"<title>Fixture-1</title><h1>Fixture-1 captcha verify you are human</h1>")
        self.assertEqual(self.probe()["status"],"BLOCKED")
    def test_http_failure_blocks(self):
        self.server.responses["/product"]=(403,{},b"Access denied")
        self.assertEqual(self.probe()["status"],"BLOCKED")
    def test_image_must_be_real_image_response(self):
        self.server.responses["/image"]=(200,{"Content-Type":"image/png"},b"<html>Not an image</html>")
        self.assertEqual(self.probe()["status"],"BLOCKED")
    def test_redirect_cannot_escape_authorized_hosts(self):
        self.server.responses["/affiliate"]=(302,{"Location":"https://unapproved.invalid/x"},b"redirect")
        self.assertEqual(self.probe()["status"],"BLOCKED")
    def test_local_requests_need_explicit_permission(self):
        with self.assertRaisesRegex(ValueError,"privée"):d.probe_url(self.base+"/product",{"127.0.0.1"})
    def test_old_price_requires_warning_in_same_product_container(self):
        self.row["date_prix"]=(d.now().date()-timedelta(days=31)).isoformat();self.save()
        self.c.plan["pages"][0]["product_ids"]=["SKU"]
        # Build static fixture directly: this test isolates DOM price guard.
        target=self.c.site/"index.html";base=self.c.html("home","/",self.c.plan["pages"][0]["editorial"])
        card='<article data-product-id="SKU">Fixture-1 12,50 EUR<img src="'+self.row["image_url"]+'"><a href="'+self.row["lien_affilié"]+'" rel="sponsored noopener" target="_blank">Voir le prix</a></article>'
        write(target,base.replace("</main>",card+"</main>"))
        with self.assertRaisesRegex(ValueError,"avertissement"):d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["home"])
        warning="Prix ancien relevé le "+self.row["date_prix"]+", vérifier auprès du marchand."
        self.c.plan["pages"][0]["price_warnings"]={"SKU":warning}
        write(target,base.replace("</main>",card.replace("</article>","<p>"+warning+"</p></article>")+"</main>"))
        d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["home"])
    def test_affiliate_entry_without_declared_product_blocks(self):
        self.c.plan["pages"][0]["product_ids"]=[]
        write(self.c.site/"index.html",self.c.html("home","/",self.c.plan["pages"][0]["editorial"]))
        with self.assertRaisesRegex(ValueError,"Page d'entrée sans produit/CTA affilié"):
            d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["home"])
    def test_unplanned_product_card_blocks_page(self):
        self.c.plan["pages"][0]["product_ids"]=["SKU"]
        base=self.c.html("home","/",self.c.plan["pages"][0]["editorial"])
        verified='<article data-product-id="SKU">Fixture-1 12,50 EUR<img src="'+self.row["image_url"]+'"><a href="'+self.row["lien_affilié"]+'" rel="sponsored noopener" target="_blank">Voir le prix</a></article>'
        unplanned='<article data-product-id="UNVERIFIED">Un modèle non déclaré<img src="'+self.row["image_url"]+'"><a href="'+self.row["lien_affilié"]+'" rel="sponsored noopener" target="_blank">Voir le prix</a></article>'
        write(self.c.site/"index.html",base.replace("</main>",verified+unplanned+"</main>"))
        with self.assertRaisesRegex(ValueError,"Produits affichés absents du plan"):
            d.page_checks(self.c.project,self.c.state,self.c.plan,self.c.site,["home"])
    def test_account_evidence_change_changes_inputs(self):
        before=d.product_inputs(self.c.project,self.c.plan)
        write(self.c.project/"account.txt","Changed evidence")
        self.assertNotEqual(before,d.product_inputs(self.c.project,self.c.plan))

if __name__=="__main__":unittest.main()
