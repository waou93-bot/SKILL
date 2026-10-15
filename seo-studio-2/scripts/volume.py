"""Benchmark coverage and URL-volume contract. No paid service or traffic promise."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

def validate_volume(project, state, plan):
    import studio
    data = studio.load(studio.safe_path(project, plan["volume_path"], True))
    if data.get("run_id") != state["run_id"] or data.get("niche") != state["niche"]:
        raise ValueError("Benchmark volume lié à une autre mission/niche")
    day = datetime.fromisoformat(data["observed_at"].replace("Z","+00:00"))
    if day.tzinfo is None:
        raise ValueError("Fuseau du benchmark requis")
    day=day.astimezone(timezone.utc)
    if day > datetime.now(timezone.utc):
        raise ValueError("Date de benchmark future")
    sites = data.get("competitors", [])
    if not sites or len({x["domain"] for x in sites}) != len(sites):
        raise ValueError("Benchmark concurrent réel requis, domaines non dupliqués")
    for site in sites:
        source = urlsplit(site["source_url"])
        if source.scheme not in ("http","https") or source.hostname != site["domain"]:
            raise ValueError("Source concurrente non liée au domaine")
        if site.get("coverage") not in ("SITEMAP","CRAWL","PARTIAL","ESTIMATE") or not site.get("limitations"):
            raise ValueError("Couverture/limites du benchmark non déclarées")
        evidence = studio.safe_path(project, site["evidence_path"], True)
        if evidence.suffix.lower() == ".xml":
            try:
                xml=ET.fromstring(evidence.read_bytes())
            except ET.ParseError as exc:
                raise ValueError("Sitemap XML invalide") from exc
            if xml.tag.rsplit("}",1)[-1] != "urlset":
                raise ValueError("Un index de sitemaps n'est pas un décompte de pages")
            urls={x.text.strip() for e in xml for x in e if x.tag.rsplit("}",1)[-1]=="loc" and x.text}
            if site.get("url_count") != len(urls):
                raise ValueError("Décompte sitemap incohérent")
        else:
            raw=studio.load(evidence)
            urls=raw.get("urls")
            if not isinstance(urls,list) or len(urls)!=len(set(urls)):
                raise ValueError("Liste des URL observées requise dans la preuve")
            if site.get("coverage") != "ESTIMATE" and site.get("url_count") != len(urls):
                raise ValueError("Volume concurrent différent de la preuve")
            if site["coverage"] in ("SITEMAP","CRAWL") and raw.get("complete") is not True:
                raise ValueError("Collecte partielle présentée comme exhaustive")
        if type(site.get("url_count")) is not int or site["url_count"]<0:
            raise ValueError("Décompte concurrent invalide")
        for url in urls:
            parsed=urlsplit(url)
            if parsed.scheme not in ("http","https") or (parsed.hostname or "").removeprefix("www.") != site["domain"].removeprefix("www."):
                raise ValueError("URL observée hors domaine concurrent")
    families = data.get("families", [])
    if not families or len({f["id"] for f in families}) != len(families):
        raise ValueError("Familles et potentiel d'URL requis")
    for family in families:
        for field in ("candidate_urls","eligible_urls","excluded_urls"):
            if type(family.get(field)) is not int or family[field] < 0:
                raise ValueError("Potentiel de famille invalide")
        if family["candidate_urls"] != family["eligible_urls"] + family["excluded_urls"]:
            raise ValueError("Dédupliquer et exclure les combinaisons sans valeur")
        if not family.get("rationale") or not family.get("demand_evidence_path") or not family.get("data_feasibility"):
            raise ValueError("Volume sans demande ni faisabilité justifiées")
        studio.safe_path(project,family["demand_evidence_path"],True)
    target = sum(f["eligible_urls"] for f in families)
    planned = len([p for p in state["pages"] if p["public"] and p["wave"]=="V1"])
    if type(data.get("target_urls")) is not int or target != data["target_urls"] or target < planned or planned == 0:
        raise ValueError("Cible d'URL incohérente avec les familles et le périmètre")
    if data.get("delivery_urls") != planned or data.get("backlog_urls") != target-planned:
        raise ValueError("Volume engagé/backlog différent du prévu")
    if planned != target:
        authorization=studio.load(studio.safe_path(project,data["wave_authorization_path"],True))
        if authorization.get("approved_by_user") is not True or not authorization.get("reason") or not authorization.get("trace_path"):
            raise ValueError("Réduction du périmètre de livraison non autorisée")
        studio.safe_path(project,authorization["trace_path"],True)
    if not data.get("strategy") or not data.get("uncertainty"):
        raise ValueError("Stratégie de volume et incertitude requises")
    return data

def volume_inputs(project, state, plan):
    import studio
    data=validate_volume(project,state,plan)
    names={plan["volume_path"]}
    names.update(x["evidence_path"] for x in data["competitors"])
    names.update(x["demand_evidence_path"] for x in data["families"])
    if data.get("wave_authorization_path"):
        names.add(data["wave_authorization_path"])
        a=studio.load(studio.safe_path(project,data["wave_authorization_path"],True))
        names.add(a["trace_path"])
    return {name:studio.digest(studio.safe_path(project,name,True)) for name in names}
