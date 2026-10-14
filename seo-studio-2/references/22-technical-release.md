# Recette technique avant publication — contrat 3.3.0

Conserver `site_check.py` comme contrôle statique léger et hors réseau. Le compléter avec crawl HTTP, navigateur réel et performance de laboratoire. Un PASS statique ne certifie ni le rendu JavaScript ni la navigation ni les performances des visiteurs.

Le [crawl borné](../scripts/technical_audit.py) utilise des GET, le même origin et des redirections internes limitées. Par défaut : localhost, 200 pages, délai de 10 secondes et profondeur de crawl 20. Une cible distante exige `--allow-remote` et un périmètre explicitement autorisé ; cette option ne donne aucune permission de publication ou d'écriture.

```text
python scripts/technical_audit.py http://localhost:8000/ --max-pages 200 --depth-budget 20 --output HTTP_AUDIT.json
```

Le fichier de sortie doit être nouveau. Le crawl vérifie statuts, redirections, title/H1, canonical, robots/noindex, sitemap, liens et JSON-LD minimal. Une profondeur de navigation supérieure à trois est un avertissement à examiner, pas une interdiction universelle. Les orphelines indexables, une incohérence sitemap/canonical et un crawl tronqué bloquent la recette ; augmenter les bornes exige de conserver un périmètre maîtrisé.

Le contrôle JSON-LD couvre la syntaxe et quelques champs minimaux d'`Article`, `BlogPosting`, `BreadcrumbList`, `Organization` et `Product`. Un type non pris en charge reste `NOT_VERIFIED` ; aucun résultat enrichi Google n'est garanti. Ne pas bloquer une URL par robots.txt en prétendant que Google lira son `noindex`. [Documentation Google](https://developers.google.com/search/docs/crawling-indexing/block-indexing).

Le [probe navigateur](../scripts/browser_probe.cjs) est un adaptateur facultatif Node/Playwright gratuit, exécuté lorsque ce runtime est disponible. Le manifest fournit `base_url` localhost, `mobile: true` et des pages avec `route`, `essential_text` et `essential_links` internes. Il vérifie présence du texte/liens essentiels dans HTML brut et DOM rendu, navigation réelle et erreurs console. Les requêtes tierces sont bloquées ; ce périmètre doit être mentionné dans les limites.

```text
node scripts/browser_probe.cjs MANIFEST_NAVIGATEUR.json PREUVE_NAVIGATEUR.json
```

La performance importe des mesures réelles de laboratoire mobile : `lcp_ms`, `cls`, `tbt_ms`, accompagnées des budgets correspondants, outil, version, route, profil et date. Les nombres doivent être finis, positifs ou nuls et dans les budgets approuvés. Lighthouse local est une option gratuite ; aucun score ou métrique ne doit être fabriqué si l'outil manque. TBT n'est pas INP et le laboratoire ne certifie pas les Core Web Vitals terrain. [Mesures laboratoire et terrain](https://web.dev/articles/lab-and-field-data-differences).

Pour la validation de publication, compléter le rapport avec `run_id`, `site_context_sha256`, `site_snapshots` (chemin/SHA des fichiers du site) et les sections HTTP, navigateur et performance. `state.technical_audit` désigne chemin du rapport et preuve `test_report`. Chaque section dispose d'une preuve indépendante : son fichier JSON correspond exactement au contenu de la section, sauf `evidence_id`, avec empreinte actuelle dans `state.evidence`. Le contrôleur refuse un PASS global si une section échoue, manque de provenance, reste `NOT_RUN` ou contredit sa preuve.

Un snapshot périmé, un fichier de site modifié, un budget dépassé ou une recette incomplète impose une nouvelle exécution/revue avant publication. Ces contrôles vérifient intégrité et cohérence des preuves déclarées ; ils n'authentifient pas cryptographiquement l'origine d'un outil. Les fixtures unitaires restent signalées comme fictives et ne constituent jamais la recette d'un site livré.

Lier aussi state.technical_audit à target_url, browser_routes, performance_routes et scope_reason. Le crawl couvre les routes publiques V1 ; les parcours navigateur et laboratoire représentent les types de pages indexables, avec périmètre justifié. Les URLs observées doivent correspondre au site et aux routes déclarés, y compris requestedUrl/finalUrl du rapport Lighthouse brut.
