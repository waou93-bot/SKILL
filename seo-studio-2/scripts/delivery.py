"""Executable delivery contract; data proofs are not certificates of truth."""
from __future__ import annotations
import argparse
from datetime import date, datetime, timezone, timedelta
import hashlib
from html.parser import HTMLParser
import ipaddress
import json
import math
from pathlib import Path
import re
import socket
import subprocess
import sys
from urllib.parse import urlsplit, urljoin
from urllib.request import build_opener, HTTPRedirectHandler, Request
from urllib.error import HTTPError

PHASES = ("audit", "design", "products", "pilots", "batches", "qa")
CHECKS = {
    "audit": {"scope", "sources", "template_adaptation"},
    "design": {"design_system", "responsive", "user_approval", "niche_fit", "depth", "cinematic_direction", "component_states"},
    "products": {"source_provenance", "affiliate_program", "prices", "images"},
    "pilots": {"editorial", "navigation", "conversion"},
    "batches": {"editorial", "pseo", "internal_links"},
    "qa": {"visual", "editorial", "security", "accessibility", "functional", "niche_fit", "depth", "cinematic_direction", "component_states"},
}
DOCS = {
    "audit": ("00_CADRAGE.md", "01_RECHERCHE.md", "03_ARCHITECTURE.md"),
    "design": ("04_DESIGN.md", "PROJECT_SKIN.yaml", "design-system.md"),
    "products": ("06_PARTENAIRES.md",),
    "pilots": ("05_CONTENU.md",),
    "batches": ("05_CONTENU.md",),
    "qa": ("11_QA.md",),
}
MARKERS = re.compile(r"A_COMPLETER|À VÉRIFIER|TODO|LOREM IPSUM|Repère Salon|Ligne [ABC]\b|votre-domaine\.fr|produits et mesures fictifs", re.I)
SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".astro", ".cache"}
HASH = re.compile(r"^[0-9a-f]{64}$")

def api():
    # Lazy import avoids a cycle when studio imports delivery.
    import studio
    return studio

def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    allow_nan=False, separators=(",", ":")).encode()).hexdigest()

def now():
    return datetime.now(timezone.utc)

def parsed_date(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)

def save(path, value):
    path.write_text(api().json_text(value), encoding="utf-8", newline="\n")

def config(project):
    s = api()
    state = s.load(s.safe_path(project, "state.json", True))
    plan = s.load(s.safe_path(project, "EXECUTION.json", True))
    if not isinstance(plan, dict) or plan.get("version") != 1 or plan.get("run_id") != state["run_id"]:
        raise ValueError("Contrat EXECUTION absent, mal formé ou lié à une autre mission")
    if plan.get("scope") != "SITE":
        raise ValueError("Le périmètre SITE est requis pour une livraison locale")
    if plan.get("site_kind") not in ("NEW", "MIGRATION") or type(plan.get("affiliation")) is not bool:
        raise ValueError("Préciser création/reprise et applicabilité de l'affiliation")
    if ("affili" in state.get("site_type","").casefold() or any(x.get("paid") and x.get("active_at_launch") for x in state.get("placements",[]))) and not plan["affiliation"]:
        raise ValueError("Affiliation du mandat ne peut pas être désactivée")
    for key in ("pages", "batches", "captures", "pilot_ids"):
        if not isinstance(plan.get(key), list):
            raise ValueError(key + " : liste obligatoire")
    if not isinstance(plan.get("receipts"), dict):
        raise ValueError("receipts : objet obligatoire")
    return state, plan

def tree(root, exclude_roots=()):
    root = Path(root).absolute()
    s = api()
    if not root.is_dir():
        raise ValueError("Dossier site/sources absent")
    excluded = [Path(x).absolute() for x in exclude_roots]
    if root in excluded:
        raise ValueError("Les sources et les preuves doivent avoir des dossiers distincts")
    result = {}
    for p in root.rglob("*"):
        if any(p.is_relative_to(x) for x in excluded):
            continue
        rel = p.relative_to(root)
        if any(x in SKIP for x in rel.parts) or p.name.startswith(".env") or p.suffix in (".pem", ".key", ".pyc"):
            continue
        if p.is_symlink():
            raise ValueError("Lien symbolique interdit dans les sources/site")
        if p.is_file():
            s.safe_path(root, rel.as_posix(), True)
            if p.stat().st_size > 30_000_000:
                raise ValueError("Périmètre de capture dépassé, borner le dossier explicitement")
            result[rel.as_posix()] = s.digest(p)
    if not result:
        raise ValueError("Dossier site/sources vide")
    return result

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.images, self.h1, self.titles, self.canonicals = [], [], [], [], []
        self.robots, self.search, self.visible = "", False, []
        self.stack = []
        self.products = {}
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        hidden = (self.stack[-1][1] if self.stack else False) or tag in ("script", "style", "template") or "hidden" in a or a.get("aria-hidden") == "true"
        owner = a.get("data-product-id") or (self.stack[-1][2] if self.stack else None)
        if owner:
            self.products.setdefault(owner, {"text":[], "images":[], "links":[]})
        if tag not in ("img", "input", "meta", "link", "br", "hr", "source", "area", "wbr"):
            self.stack.append((tag, hidden, owner))
        if tag == "meta" and a.get("name", "").lower() == "robots":
            self.robots += a.get("content", "").lower()
        if tag == "link" and "canonical" in a.get("rel", "").split():
            self.canonicals.append(a.get("href", ""))
        if hidden:
            return
        if tag == "a" and a.get("href"):
            self.links.append(a)
            if owner: self.products[owner]["links"].append(a)
        if tag == "img":
            self.images.append(a.get("src", ""))
            if owner: self.products[owner]["images"].append(a.get("src", ""))
        if tag == "input" and (a.get("type") == "search" or a.get("role") == "searchbox"):
            self.search = True

    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self.stack and self.stack[-1][1]:
            return
        self.visible.append(data)
        if self.stack and self.stack[-1][2]: self.products[self.stack[-1][2]]["text"].append(data)
        if any(x[0] == "h1" for x in self.stack):
            self.h1.append(data)
        if any(x[0] == "title" for x in self.stack):
            self.titles.append(data)

    @property
    def text(self):
        return " ".join(" ".join(self.visible).split())

def catalogue(project, plan):
    s = api()
    if not plan["affiliation"]:
        return []
    rows = s.load(s.safe_path(project, plan["catalogue_path"], True))
    if not isinstance(rows, list) or not rows:
        raise ValueError("Catalogue vérifié absent ou vide")
    ids = []
    fields = ("id", "nom", "marque", "modèle", "source_url", "lien_affilié", "image_url",
              "prix", "date_prix", "date_vérification", "statut", "devise",
              "source_evidence_path", "program_evidence_path")
    for row in rows:
        if not isinstance(row, dict) or any(k not in row or row[k] is None or row[k] == "" for k in fields):
            raise ValueError("Produit incomplet")
        if not isinstance(row["id"], str) or row["statut"] != "VERIFIE":
            raise ValueError("Produit non vérifié")
        if isinstance(row["prix"], bool) or not isinstance(row["prix"], (int, float)) or not math.isfinite(row["prix"]) or row["prix"] < 0:
            raise ValueError("Prix invalide")
        for field in ("date_prix", "date_vérification"):
            day = date.fromisoformat(row[field])
            if day > now().date():
                raise ValueError("Date produit future")
        for field in ("source_url", "lien_affilié", "image_url"):
            u = urlsplit(row[field])
            if u.scheme not in ("https", "http") or not u.hostname or u.username or u.password:
                raise ValueError("URL produit invalide")
        evidence = s.load(s.safe_path(project, row["source_evidence_path"], True))
        if evidence.get("reference") != row["modèle"] or evidence.get("source_url") != row["source_url"] or not evidence.get("session_reference"):
            raise ValueError("Provenance produit non liée à la référence et à la session")
        if evidence.get("source_kind") not in ("AFFILIATE_FEED", "AMAZON_API", "MANUFACTURER", "MERCHANT"):
            raise ValueError("Source officielle autorisée requise")
        read_at = parsed_date(evidence["read_at"])
        if now() - read_at > timedelta(days=1) or read_at > now():
            raise ValueError("Source non lue dans la session récente")
        program = s.load(s.safe_path(project, row["program_evidence_path"], True))
        if program.get("status") != "ACTIVE" or not program.get("program") or not program.get("account_evidence"):
            raise ValueError("Preuve d'affiliation active manquante")
        s.safe_path(project, program["account_evidence"], True)
        ids.append(row["id"])
    if len(ids) != len(set(ids)):
        raise ValueError("ID produit dupliqué")
    return rows

def product_inputs(project, plan):
    s = api()
    products = catalogue(project, plan)
    files = {}
    if plan["affiliation"]:
        names = {plan["catalogue_path"]} | {r[f] for r in products for f in ("source_evidence_path", "program_evidence_path")}
        for row in products:
            names.add(s.load(s.safe_path(project, row["program_evidence_path"], True))["account_evidence"])
        files = {p:s.digest(s.safe_path(project, p, True)) for p in names}
    return files

def image_signature(data, content_type):
    return content_type.startswith("image/") and (
        data.startswith(b"\x89PNG\r\n\x1a\n") or data.startswith(b"\xff\xd8\xff")
        or data.startswith((b"GIF87a", b"GIF89a"))
        or data[:4] == b"RIFF" and data[8:12] == b"WEBP"
        or b"ftypavif" in data[:40] or b"ftypavis" in data[:40])

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args):
        return None

def probe_url(url, hosts, allow_local=False):
    """Explicit host allowlist, bounded GETs, no automatic cross-origin redirects."""
    opener = build_opener(NoRedirect)
    chain = []
    for _ in range(9):
        u = urlsplit(url)
        if u.scheme not in ("http", "https") or u.hostname not in hosts or u.username or u.password:
            raise ValueError("URL hors périmètre autorisé")
        addresses = {x[4][0] for x in socket.getaddrinfo(u.hostname, u.port or (443 if u.scheme == "https" else 80))}
        if any(not ipaddress.ip_address(x).is_global for x in addresses) and not (allow_local and all(ipaddress.ip_address(x).is_loopback for x in addresses)):
            raise ValueError("Destination réseau privée interdite")
        try:
            response = opener.open(Request(url, headers={"User-Agent":"SEO-Studio-Delivery/1"}), timeout=10)
        except HTTPError as exc:
            response = exc
        with response:
            status = response.code
            if status in (301, 302, 303, 307, 308):
                target = urljoin(url, response.headers.get("Location", ""))
                if target in [x["url"] for x in chain] or target == url:
                    raise ValueError("Boucle de redirection")
                chain.append({"url":url, "status":status, "target":target})
                url = target
                continue
            data = response.read(2_000_001)
            if status != 200 or len(data) > 2_000_000 or not data:
                raise ValueError("Destination non 200, vide ou trop volumineuse")
            return {"requested_url":chain[0]["url"] if chain else url, "final_url":url,
                    "status":status, "redirects":chain,
                    "content_type":response.headers.get("Content-Type", "").lower(),
                    "body_sha256":hashlib.sha256(data).hexdigest()}, data
    raise ValueError("Trop de redirections")

def probe_products(project, hosts, allow_local=False):
    state, plan = config(project)
    rows, errors, results = catalogue(project, plan), [], []
    for row in rows:
        item = {"id":row["id"], "checks":{}}
        for field in ("source_url", "lien_affilié", "image_url"):
            try:
                receipt, body = probe_url(row[field], set(hosts), allow_local)
                if field == "image_url" and not image_signature(body, receipt["content_type"]):
                    raise ValueError("Image non reconnue")
                if field in ("source_url", "lien_affilié"):
                    doc = Page(body.decode("utf-8", "replace"))
                    reference = re.escape(row["modèle"].casefold())
                    if (not doc.h1 or not doc.titles or not re.search(r"(?<!\w)" + reference + r"(?!\w)", doc.text.casefold())
                            or re.search(r"captcha|access denied|verify you are human", doc.text, re.I)):
                        raise ValueError("Page ou variante non vérifiable, contrôle manuel nécessaire")
                item["checks"][field] = receipt
            except (OSError, ValueError) as exc:
                errors.append(row["id"] + "/" + field + ": " + str(exc))
        results.append(item)
    report = {"run_id":state["run_id"], "observed_at":now().isoformat(),
              "inputs":product_inputs(project, plan), "products":results,
              "errors":errors, "status":"BLOCKED" if errors else "PASS"}
    save(api().safe_path(project, plan["product_report_path"]), report)
    return report

def proof(project, path, phase, required_scope):
    s = api()
    review = s.load(s.safe_path(project, path, True))
    if review.get("phase") != phase or review.get("status") != "PASS" or review.get("findings") != []:
        raise ValueError("Revue absente, échouée ou objections ouvertes : " + phase)
    if not CHECKS[phase].issubset(set(review.get("checks", []))):
        raise ValueError("Revue incomplète : " + phase)
    if not set(required_scope).issubset(set(review.get("scope", []))):
        raise ValueError("Périmètre de revue incomplet : " + phase)
    if review.get("reviewer_type") not in ("HUMAN", "AGENT") or not review.get("reviewer") or not review.get("trace_path"):
        raise ValueError("Provenance de revue absente")
    if phase == "design" and review["reviewer_type"] != "HUMAN":
        raise ValueError("Approbation utilisateur du design requise")
    if review.get("author") == review["reviewer"] or not review.get("author"):
        raise ValueError("Auto-revue interdite")
    s.safe_path(project, review["trace_path"], True)
    return review

def mapping(state, plan):
    expected = {p["id"]:p for p in state["pages"] if p["public"] and p["wave"] == "V1"}
    actual = {p["id"]:p for p in plan["pages"]}
    if not expected or len(actual) != len(plan["pages"]) or actual.keys() != expected.keys():
        raise ValueError("Prévu/réalisé : périmètre V1 absent, dupliqué ou incomplet")
    outputs = [p.get("output_path") for p in plan["pages"]]
    if any(not x for x in outputs) or len(outputs) != len(set(outputs)):
        raise ValueError("Sorties HTML manquantes ou réutilisées pour plusieurs pages")
    return expected, actual

def page_checks(project, state, plan, site_root, ids):
    s = api()
    expected, actual = mapping(state, plan)
    products = {p["id"]:p for p in catalogue(project, plan)}
    own_sections = {}
    for pid in ids:
        item, intended = actual[pid], expected[pid]
        text = s.safe_path(site_root, item["output_path"], True).read_text(encoding="utf-8-sig")
        doc = Page(text)
        if MARKERS.search(doc.text):
            raise ValueError("Démo ou texte provisoire livré : " + pid)
        if not doc.h1 or not doc.titles or " ".join(" ".join(doc.h1).split()) != intended["h1"]:
            raise ValueError("Titre/H1 absent ou différent du prévu : " + pid)
        if len(doc.canonicals) != 1 or urlsplit(doc.canonicals[0]).path.rstrip("/") != intended["canonical_path"].rstrip("/"):
            raise ValueError("Canonical différent du prévu : " + pid)
        if intended["indexable"] and "noindex" in doc.robots or not intended["indexable"] and "noindex" not in doc.robots:
            raise ValueError("Indexation différente du prévu : " + pid)
        if intended["kind"] != "landing" and not doc.search:
            raise ValueError("Recherche interne absente : " + pid)
        for key in ("answer", "limitation", "next_action"):
            value = item.get("editorial", {}).get(key)
            if not isinstance(value, str) or not value.strip() or value not in doc.text:
                raise ValueError("Couverture éditoriale absente : " + pid + "/" + key)
        if type(item.get("programmatic")) is not bool:
            raise ValueError("Applicabilité pSEO non décidée : " + pid)
        if item["programmatic"] and intended["indexable"]:
            sections = item.get("pseo_sections", {})
            if set(sections) != {"verdict", "comparison", "usage"} or len(set(sections.values())) != 3:
                raise ValueError("Trois éléments pSEO propres requis : " + pid)
            for kind, value in sections.items():
                if not isinstance(value, str) or not value.strip() or value not in doc.text:
                    raise ValueError("Élément pSEO absent : " + pid)
                if kind == "comparison" and not re.search(r"\d", value):
                    raise ValueError("Comparaison pSEO non chiffrée : " + pid)
                if (kind, value) in own_sections:
                    raise ValueError("Élément pSEO réutilisé : " + pid)
                own_sections[kind, value] = pid
        for product_id in item.get("product_ids", []):
            if product_id not in products:
                raise ValueError("Produit non prévu/vérifié : " + product_id)
            row = products[product_id]
            container = doc.products.get(product_id)
            if not container:
                raise ValueError("Conteneur data-product-id manquant : " + product_id)
            product_text = " ".join(" ".join(container["text"]).split())
            price_values = {str(row["prix"]), format(row["prix"], ".2f"), str(row["prix"]).replace(".", ","), format(row["prix"], ".2f").replace(".", ",")}
            if row["modèle"] not in product_text or not any(v in product_text for v in price_values):
                raise ValueError("Référence/prix affiché différent du produit : " + product_id)
            if row["image_url"] not in container["images"] or not any(a["href"] == row["lien_affilié"] and "sponsored" in a.get("rel", "").split() and a.get("target") == "_blank" and "noopener" in a.get("rel", "").split() for a in container["links"]):
                raise ValueError("Image ou accès affilié réel absent : " + pid)
            if (now().date() - date.fromisoformat(row["date_prix"])).days > 30:
                warning = item.get("price_warnings", {}).get(product_id, "")
                if not warning or row["date_prix"] not in warning or warning not in product_text:
                    raise ValueError("Prix ancien sans avertissement visible : " + pid)
        if plan["affiliation"] and pid == plan.get("entry_page_id") and not item.get("product_ids"):
            raise ValueError("Page d'entrée sans produit/CTA affilié")
    return expected, actual

TEMPLATE_FEATURES = {"decision_tool","saved_selection","category_filters","mobile_menu","internal_search"}

def feature_plan(project, state, plan, cases_required=True):
    features = plan.get("features")
    if not isinstance(features,list):
        raise ValueError("Évaluation des interactions du template absente")
    ids=[x["id"] for x in features]
    if len(ids)!=len(set(ids)) or not TEMPLATE_FEATURES.issubset(set(ids)):
        raise ValueError("Motifs du template non évalués ou répétés")
    expected={p["id"]:p for p in state["pages"] if p["public"] and p["wave"]=="V1"}
    active=[]
    for feature in features:
        if feature.get("decision") not in ("KEEP","ADAPT","EXCLUDE") or not feature.get("reason"):
            raise ValueError("Décision de fonctionnalité non motivée")
        if feature["id"]=="internal_search":
            if any(p["kind"]!="landing" for p in expected.values()) and feature["decision"]=="EXCLUDE":
                raise ValueError("Recherche obligatoire ne peut pas être exclue")
            continue
        if feature["decision"]=="EXCLUDE":
            continue
        active.append(feature)
        if not cases_required:
            continue
        case=api().load(api().safe_path(project,feature["case_path"],True))
        scenarios=case.get("scenarios",[])
        if case.get("feature_id")!=feature["id"] or {x.get("profile") for x in scenarios}!={"desktop","mobile"}:
            raise ValueError("Scénarios desktop/mobile requis pour "+feature["id"])
        for scenario in scenarios:
            if scenario.get("page_id") not in expected or not scenario.get("expects"):
                raise ValueError("Scénario sans page réelle ni assertion")
            if not scenario.get("actions") and not scenario.get("not_applicable_reason"):
                raise ValueError("Interaction non testée : "+feature["id"])
            for assertion in scenario["expects"]:
                if not assertion.get("selector") or not any(k in assertion for k in ("count","text_contains","visible","attribute")):
                    raise ValueError("Assertion interaction sans contrôle reconnu")
                if "count" in assertion and (type(assertion["count"]) is not int or assertion["count"]<0):
                    raise ValueError("Nombre attendu invalide")
                if "visible" in assertion and type(assertion["visible"]) is not bool:
                    raise ValueError("Visibilité attendue invalide")
                if "attribute" in assertion and ("value" not in assertion or not assertion["attribute"]):
                    raise ValueError("Valeur d'attribut attendue absente")
            for action in scenario.get("actions",[]):
                if action.get("action") not in ("click","fill","press","select","check","uncheck","set_input") or not action.get("selector"):
                    raise ValueError("Action interaction non reconnue")
    return active

def context(project, state, plan, phase, site_root, source_root):
    s = api()
    docs = {}
    for name in DOCS[phase]:
        p = s.safe_path(project, name, True)
        if MARKERS.search(p.read_text(encoding="utf-8-sig")):
            raise ValueError("Document provisoire : " + name)
        docs[name] = s.digest(p)
    payload = {"run_id":state["run_id"], "niche":state["niche"], "kind":plan["site_kind"],
               "affiliation":plan["affiliation"], "phase":phase, "docs":docs}
    if phase != "audit":
        payload["previous"] = plan["receipts"].get(PHASES[PHASES.index(phase)-1])
    if phase == "design":
        payload["features"]=[{k:f[k] for k in ("id","decision","reason")} for f in plan["features"]]
        payload["pages"] = [{k:p[k] for k in ("id","kind","path")} for p in state["pages"]]
    if phase in ("pilots", "batches", "qa"):
        payload["pages"] = state["pages"]
        payload["bindings"] = plan["pages"]
        payload["site"] = tree(site_root)
        payload["sources"] = tree(source_root, (project, site_root))
        payload["build"] = plan.get("build_receipt")
        payload["pilot_ids"] = plan["pilot_ids"]
        payload["entry_page_id"] = plan.get("entry_page_id")
        payload["features"] = plan["features"]
        payload["feature_cases"]={f["case_path"]:s.digest(s.safe_path(project,f["case_path"],True))
                                  for f in feature_plan(project,state,plan)}
    if phase == "products" or plan["affiliation"] and phase in ("pilots", "batches", "qa"):
        payload["products"] = product_inputs(project, plan)
        if plan["affiliation"]:
            payload["product_report"] = s.digest(s.safe_path(project, plan["product_report_path"], True))
    if phase == "audit":
        from volume import volume_inputs
        payload["volume"] = volume_inputs(project,state,plan)
        companion = s.ROOT/"seo-site-preproduction"
        if not companion.exists(): companion=s.ROOT.parent/"seo-site-preproduction"
        names=("SKILL.md","assets/template-demo/TEMPLATE_RULES.md","references/preproduction-map.md")
        payload["template"]={name:s.digest(s.safe_path(companion,name,True)) for name in names}
        payload["baseline"] = plan.get("baseline", [])
        files = [x[k] for x in plan.get("baseline", []) for k in ("desktop","mobile")]
        if plan.get("baseline_waiver_path"):
            files.append(plan["baseline_waiver_path"])
    elif phase == "design":
        payload["directions"] = plan.get("directions", [])
        files = [x[k] for x in plan.get("directions", []) for k in ("desktop","mobile")]
    elif phase in ("batches", "qa"):
        payload["batches"] = plan["batches"]
        files = [x["review_path"] for x in plan["batches"]]
        for name in list(files):
            review=s.load(s.safe_path(project,name,True))
            files.append(review["trace_path"])
        if phase == "qa":
            payload["captures"] = plan["captures"]
            files.append("EXECUTION-browser.json")
            files += [x[k] for x in plan["captures"] for k in ("desktop","mobile")]
    else:
        files = []
    payload["proof_files"] = {name:s.digest(s.safe_path(project,name,True)) for name in files}
    return canonical(payload)

def screenshot(project, name, profile):
    data = api().safe_path(project,name,True).read_bytes()
    if len(data) < 24 or not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("Capture PNG requise")
    width,height = int.from_bytes(data[16:20],"big"),int.from_bytes(data[20:24],"big")
    if width < (1024 if profile=="desktop" else 320) or profile=="mobile" and width > 480 or height < 200:
        raise ValueError("Dimensions de capture incohérentes")

def automatic(project, state, plan, phase, site_root, source_root):
    s = api()
    if phase == "audit":
        from volume import validate_volume
        validate_volume(project,state,plan)
    if phase == "audit" and plan["site_kind"] == "MIGRATION":
        baseline = plan.get("baseline", [])
        if (len(baseline) < 8 or len({x.get("kind") for x in baseline}) < 8) and not plan.get("baseline_waiver_path"):
            raise ValueError("Audit V1 : huit pages ou accord utilisateur explicite requis")
        if len(baseline) < 8 or len({x.get("kind") for x in baseline}) < 8:
            waiver = s.load(s.safe_path(project, plan["baseline_waiver_path"], True))
            if waiver.get("approved_by_user") is not True or not waiver.get("reason") or not waiver.get("trace_path"):
                raise ValueError("Dérogation de couverture V1 non autorisée")
            s.safe_path(project, waiver["trace_path"], True)
        if len({x.get("route") for x in baseline}) != len(baseline):
            raise ValueError("Pages de référence répétées")
        for item in baseline:
            for profile in ("desktop", "mobile"):
                screenshot(project, item[profile], profile)
    if phase == "design":
        feature_plan(project,state,plan,False)
        skin=s.safe_path(project,"PROJECT_SKIN.yaml",True).read_text(encoding="utf-8-sig")
        try:
            approved=s.load(s.safe_path(project,"PROJECT_SKIN.yaml",True)).get("status") == "APPROVED"
        except ValueError:
            approved=bool(re.search(r"(?m)^status:\s*[\"\']?APPROVED[\"\']?\s*$",skin))
        if not approved:
            raise ValueError("PROJECT_SKIN non approuvé")
    if phase == "design" and plan["site_kind"] == "NEW":
        if len(plan.get("directions", [])) != 2:
            raise ValueError("Deux directions visuelles requises")
        for direction in plan["directions"]:
            if not direction.get("reference_urls"):
                raise ValueError("Références visuelles manquantes")
            for profile in ("desktop", "mobile"):
                screenshot(project, direction[profile], profile)
    if phase == "products" and plan["affiliation"]:
        rows = catalogue(project, plan)
        report = s.load(s.safe_path(project, plan["product_report_path"], True))
        age = now() - parsed_date(report["observed_at"])
        if report.get("run_id") != state["run_id"] or report.get("status") != "PASS" or report.get("errors") != [] or report.get("inputs") != product_inputs(project, plan) or age < timedelta() or age > timedelta(days=1):
            raise ValueError("Recette produit absente, ancienne ou caduque")
        checked = {x["id"]:x for x in report.get("products", [])}
        if checked.keys() != {x["id"] for x in rows}:
            raise ValueError("Couverture produit incomplète")
        for row in rows:
            for field in ("source_url", "lien_affilié", "image_url"):
                run = checked[row["id"]].get("checks", {}).get(field, {})
                if run.get("status") != 200 or run.get("requested_url") != row[field] or not HASH.fullmatch(run.get("body_sha256", "")):
                    raise ValueError("Test produit absent ou incohérent")
    if phase in ("pilots", "batches", "qa"):
        feature_plan(project,state,plan)
        expected, actual = mapping(state, plan)
        ids = plan["pilot_ids"] if phase == "pilots" else list(expected)
        if phase == "pilots" and (len(ids) != len(set(ids)) or len(ids) < 3 or plan.get("entry_page_id") not in ids):
            raise ValueError("Trois pilotes réels incluant l'entrée requis")
        if not set(ids).issubset(expected):
            raise ValueError("Pilote hors périmètre")
        page_checks(project, state, plan, site_root, ids)
        receipt = plan.get("build_receipt") or {}
        if receipt.get("run_id") != state["run_id"] or receipt.get("returncode") != 0 or receipt.get("site_sha256") != canonical(tree(site_root)) or receipt.get("source_sha256") != canonical(tree(source_root, (project, site_root))):
            raise ValueError("Build non exécuté ou caduc")
        if not receipt.get("argv") or s.digest(s.safe_path(project, receipt["log_path"], True)) != receipt.get("log_sha256"):
            raise ValueError("Journal de build absent/caduc")
    if phase in ("batches", "qa"):
        flat = []
        for i, batch in enumerate(plan["batches"]):
            ids = batch.get("page_ids", [])
            if not ids or len(ids) > 30 or i < len(plan["batches"])-1 and len(ids) < 20:
                raise ValueError("Lots : 20–30 pages, dernier lot plus petit permis")
            flat.extend(ids)
            proof(project, batch["review_path"], "batches", ids)
        if len(flat) != len(set(flat)) or set(flat) != set(expected):
            raise ValueError("Lots incomplets ou pages répétées")
    if phase == "qa":
        browser = s.load(s.safe_path(project, "EXECUTION-browser.json", True))
        if (browser.get("run_id") != state["run_id"] or browser.get("status") != "PASS"
                or browser.get("errors") != [] or browser.get("site_sha256") != canonical(tree(site_root))
                or browser.get("tool") != "Playwright" or not browser.get("version")):
            raise ValueError("Recette navigateur de livraison absente ou caduque")
        runs = browser.get("runs", [])
        pairs = {(x.get("page_id"),x.get("profile")) for x in runs}
        if len(runs) != len(pairs) or pairs != {(pid,profile) for pid in expected for profile in ("desktop","mobile")}:
            raise ValueError("Couverture navigateur desktop/mobile incomplète")
        for run in runs:
            html = s.safe_path(site_root, actual[run["page_id"]]["output_path"], True)
            checks={"rendered","images","entry_products_visible","search","search_empty","navigation"}
            if (run.get("html_sha256") != s.digest(html) or run.get("errors") != []
                    or set(run.get("checks",{})) != checks or not all(v is True for v in run["checks"].values())):
                raise ValueError("Contrôle navigateur échoué/incomplet")
            screenshot(project,run["screenshot_path"],run["profile"])
            if s.digest(s.safe_path(project,run["screenshot_path"],True)) != run.get("screenshot_sha256"):
                raise ValueError("Capture navigateur modifiée")
        feature_runs=browser.get("feature_runs",[])
        wanted=feature_plan(project,state,plan)
        expected_cases=set()
        for feature in wanted:
            case_path=s.safe_path(project,feature["case_path"],True)
            case=s.load(case_path)
            for number,scenario in enumerate(case["scenarios"]):
                expected_cases.add((feature["id"],number))
                matching=[run for run in feature_runs if (run.get("feature_id"),run.get("scenario_index"))==(feature["id"],number)]
                if len(matching)!=1:
                    raise ValueError("Recette interaction manquante : "+feature["id"])
                run=matching[0]
                if (run.get("status")!="PASS" or run.get("errors")!=[]
                        or run.get("case_sha256")!=s.digest(case_path)
                        or run.get("profile")!=scenario["profile"] or run.get("page_id")!=scenario["page_id"]):
                    raise ValueError("Recette interaction échouée/caduque")
        if {(x.get("feature_id"),x.get("scenario_index")) for x in feature_runs} != expected_cases:
            raise ValueError("Recette interaction hors périmètre")
        represented = set()
        for capture in plan["captures"]:
            pid = capture["page_id"]
            if pid not in expected:
                raise ValueError("Capture hors périmètre")
            html = s.safe_path(site_root, actual[pid]["output_path"], True)
            if capture.get("html_sha256") != s.digest(html):
                raise ValueError("Capture liée à un ancien HTML")
            for profile in ("desktop", "mobile"):
                screenshot(project, capture[profile], profile)
            represented.add(expected[pid]["kind"])
        if represented != {x["kind"] for x in expected.values()}:
            raise ValueError("Captures desktop/mobile par template incomplètes")
        for auxiliary in plan.get("auxiliary_outputs", []):
            auxiliary_page=Page(s.safe_path(site_root,auxiliary,True).read_text(encoding="utf-8-sig"))
            if "noindex" not in auxiliary_page.robots:
                raise ValueError("Page auxiliaire indexable hors plan : "+auxiliary)
        allowed = {x["output_path"] for x in actual.values()} | set(plan.get("auxiliary_outputs", []))
        extra = {p for p in tree(site_root) if p.endswith((".html", ".htm"))} - allowed
        if extra:
            raise ValueError("Pages HTML hors contrat : " + ", ".join(sorted(extra)))
        technical_errors, _ = __import__("technical_audit").validate_technical(
            project, state, load=s.load, safe_path=s.safe_path, digest=s.digest)
        if technical_errors:
            raise ValueError("Recette HTTP/navigateur/performance : " + "; ".join(technical_errors))

def validate_execution(project, state=None, site_root=None, source_root=None, through="qa"):
    try:
        current, plan = config(project)
        if state is not None and state != current:
            raise ValueError("État en mémoire différent du dossier")
        state = current
        if site_root is None or source_root is None:
            raise ValueError("Fournir explicitement --site-root et --source-root")
        for phase in PHASES[:PHASES.index(through)+1]:
            receipt = plan["receipts"].get(phase)
            if not receipt:
                raise ValueError("Étape non terminée : " + phase)
            review = proof(project, receipt["review_path"], phase,
                           plan["pilot_ids"] if phase == "pilots" else [p["id"] for p in plan["pages"]] if phase in ("batches", "qa") else ["project"])
            if api().digest(api().safe_path(project, receipt["review_path"], True)) != receipt.get("review_sha256"):
                raise ValueError("Revue modifiée : " + phase)
            if api().digest(api().safe_path(project, review["trace_path"], True)) != receipt.get("trace_sha256"):
                raise ValueError("Trace de revue modifiée : " + phase)
            if receipt.get("context_sha256") != context(project, state, plan, phase, site_root, source_root):
                raise ValueError("Preuve caduque : " + phase)
            automatic(project, state, plan, phase, site_root, source_root)
        return []
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        return [str(exc)]

def record(project, phase, review_path, site_root, source_root):
    state, plan = config(project)
    i = PHASES.index(phase)
    if i:
        errors = validate_execution(project, state, site_root, source_root, PHASES[i-1])
        if errors:
            raise ValueError("; ".join(errors))
    required = plan["pilot_ids"] if phase == "pilots" else [p["id"] for p in plan["pages"]] if phase in ("batches", "qa") else ["project"]
    review = proof(project, review_path, phase, required)
    automatic(project, state, plan, phase, site_root, source_root)
    plan["receipts"][phase] = {
        "context_sha256":context(project, state, plan, phase, site_root, source_root),
        "review_path":review_path, "review_sha256":api().digest(api().safe_path(project, review_path, True)),
        "trace_sha256":api().digest(api().safe_path(project, review["trace_path"], True)),
        "recorded_at":now().isoformat()}
    for later in PHASES[i+1:]:
        plan["receipts"].pop(later, None)
    save(project/"EXECUTION.json", plan)
    return {"status":"PHASE_RECORDED", "phase":phase, "next":PHASES[i+1] if i+1 < len(PHASES) else "validate --stage local"}

def run_build(project, site_root, source_root, argv, timeout=300):
    state, plan = config(project)
    errors = validate_execution(project, state, site_root, source_root, "products")
    if errors:
        raise ValueError("; ".join(errors))
    if not argv or argv[0] == "--" or not 1 <= timeout <= 3600:
        raise ValueError("Commande explicite et timeout 1–3600 requis")
    plan["build_receipt"] = None
    for phase in PHASES[3:]:
        plan["receipts"].pop(phase, None)
    save(project/"EXECUTION.json", plan)
    log = api().safe_path(project, "EXECUTION-build.log")
    with log.open("wb") as stream:
        try:
            run = subprocess.run(argv, cwd=source_root, stdout=stream, stderr=subprocess.STDOUT,
                                 timeout=timeout, shell=False)
            code=run.returncode
        except subprocess.TimeoutExpired:
            stream.write(b"Build timeout")
            code=124
    receipt = {"run_id":state["run_id"], "argv":argv, "returncode":code,
               "log_path":log.name, "log_sha256":api().digest(log),
               "source_sha256":canonical(tree(source_root, (project, site_root))),
               "site_sha256":canonical(tree(site_root)) if site_root.is_dir() else None,
               "observed_at":now().isoformat()}
    plan["build_receipt"] = receipt
    save(project/"EXECUTION.json", plan)
    return {"status":"BUILD_OK" if code == 0 and receipt["site_sha256"] else "BLOCKED", "receipt":receipt}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=("prepare", "record", "check", "products", "build"))
    p.add_argument("project", type=Path)
    p.add_argument("--site-root", type=Path)
    p.add_argument("--source-root", type=Path)
    p.add_argument("--phase", choices=PHASES)
    p.add_argument("--review")
    p.add_argument("--allow-host", action="append", default=[])
    p.add_argument("--allow-local", action="store_true")
    p.add_argument("--timeout", type=int, default=300)
    args, argv = p.parse_known_args()
    try:
        if args.command == "prepare":
            if argv: raise ValueError("Arguments inconnus")
            s=api()
            state=s.load(s.safe_path(args.project,"state.json",True))
            path=s.safe_path(args.project,"EXECUTION.json")
            written=[]
            if not path.exists():
                plan=s.load(s.ROOT/"templates/execution.json");plan["run_id"]=state["run_id"]
                with path.open("x",encoding="utf-8") as stream: stream.write(s.json_text(plan))
                written.append("EXECUTION.json")
            volume=s.safe_path(args.project,"research/volume.json")
            if not volume.exists():
                data=s.load(s.ROOT/"templates/volume.json");data.update(run_id=state["run_id"],niche=state["niche"])
                volume.parent.mkdir(parents=True,exist_ok=True)
                with volume.open("x",encoding="utf-8") as stream: stream.write(s.json_text(data))
                written.append("research/volume.json")
            old_ids={x["id"] for x in state["requirements"]}
            for ident in ("R30","R31"):
                if ident not in old_ids:
                    state["requirements"].append({"id":ident,"status":"A_FAIRE","evidence_ids":[],"decision_id":None})
                    written.append(ident)
            if any(x in written for x in ("R30","R31")): save(args.project/"state.json",state)
            result={"status":"PREPARED" if written else "EXISTS_UNCHANGED", "written":written,
                    "warning":"Compléter le contrat et les exigences ; aucune phase approuvée."}
        elif args.command == "products":
            if argv: raise ValueError("Arguments inconnus")
            result = probe_products(args.project, args.allow_host, args.allow_local)
        elif args.command == "record":
            if not args.phase or not args.review or argv: raise ValueError("Phase/revue requises")
            result = record(args.project, args.phase, args.review, args.site_root, args.source_root)
        elif args.command == "build":
            if argv[:1] != ["--"]: raise ValueError("Commande explicite après -- requise")
            result = run_build(args.project, args.site_root, args.source_root, argv[1:], args.timeout)
        else:
            if argv: raise ValueError("Arguments inconnus")
            errors = validate_execution(args.project, site_root=args.site_root, source_root=args.source_root)
            result = {"status":"BLOCKED" if errors else "EXECUTION_OK", "errors":errors,
                      "warning":"Combiner avec studio.py validate --stage local ; aucune certification de vérité."}
        print(api().json_text(result), end="")
        return 2 if result.get("status") in ("BLOCKED", "BLOQUE") else 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError, subprocess.TimeoutExpired) as exc:
        print(api().json_text({"status":"BLOCKED", "error":str(exc)}), end="")
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
