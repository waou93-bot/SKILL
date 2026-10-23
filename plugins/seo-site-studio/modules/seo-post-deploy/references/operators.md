# Opérateurs et procédures officielles

Sources consultées le 5 octobre 2026. Google, IndexNow, OpenAI, Yandex, DuckDuckGo, Anthropic, Perplexity et modules Google ci-dessous : contenu officiel consulté. Yahoo et certaines aides Bing : extraits de recherche officiels seulement, pages bloquées, vides ou sous consentement ; procédures détaillées à revalider. Aucune intégration authentifiée ni soumission réelle testée. Reconsulter avant exécution : disponibilité, droits, quotas et participants évoluent.

| Surface | Démarche | Limite |
|---|---|---|
| Google | Search Console, propriété, sitemap, inspection et demande manuelle disponible | Soumettre ne garantit ni crawl ni indexation |
| Bing | Webmaster Tools, propriété, sitemap, inspection, IndexNow | Import Google possible ; préserver les propriétés existantes |
| Participants IndexNow | Notification officielle, intégration CMS/CDN ou clé hébergée | Participants à vérifier ; un envoi peut être partagé |
| Yandex et autres moteurs régionaux | Outils officiels selon marché et accès | Pertinence et procédure à vérifier |
| Yahoo / DuckDuckGo / autres agrégateurs | Identifier index/partenaires et mécanismes actuels | Aucun formulaire universel présumé |
| ChatGPT et autres moteurs IA | Robots de recherche, contenu accessible, sources/indices documentés | Recherche distincte d'entraînement ; aucune garantie de citation |
| Local / commerce / médias | Services officiels, éligibilité et flux selon activité | Aucun compte, engagement ou fiche fictive |

## Sources à ouvrir selon l'action

- [Google : créer et soumettre un sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google : demander une nouvelle exploration](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl)
- [Search Console : API de soumission de sitemap](https://developers.google.com/webmaster-tools/v1/sitemaps/submit)
- [Search Console : API d'inspection](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect)
- [Google Indexing API : usages autorisés](https://developers.google.com/search/apis/indexing-api/v3/using-api) — offres JobPosting et diffusions BroadcastEvent intégrées à VideoObject, selon critères actuels.
- [Bing : ajouter et vérifier un site](https://www2.bing.com/webmasters/help/add-and-verify-site-12184f8b)
- [Bing : sitemaps](https://www2.bing.com/webmasters/help/sitemaps-3b5cf6ed)
- [Bing : soumission d’URL et quotas](https://www.bing.com/webmasters/help/URL-Submission-62f2860b)
- [Bing : inspection d’URL](https://www.bing.com/webmasters/help/URL-Inspection-55a30305)
- [Bing : Site Explorer](https://www.bing.com/webmasters/help/site-explorer-c680da37)
- [Bing : aide au diagnostic et données absentes](https://www.bing.com/webmasters/help/webmaster-support-24ab5ebf)
- [Bing : robots.txt tester](https://www.bing.com/webmasters/help/robots-txt-tester-623520ca)
- [Bing : Crawl Control](https://www.bing.com/webmasters/help/crawl-control-55a30303)
- [GSC API : ajouter une propriété](https://developers.google.com/webmaster-tools/v1/sites/add)
- [GSC API : soumettre un sitemap](https://developers.google.com/webmaster-tools/v1/sitemaps/submit)
- [GSC API : inspection d’URL](https://developers.google.com/webmaster-tools/v1/urlInspection.index/urlInspection.index)
- [Bing : retrait de la soumission anonyme](https://blogs.bing.com/webmaster/2022/5/Spring-cleaning-Removed-Bing-anonymous-sitemap-submission/)
- [IndexNow : protocole](https://www.indexnow.org/documentation)
- [IndexNow : questions et limites](https://www.indexnow.org/faq)
- [IndexNow : participants](https://www.indexnow.org/searchengines)
- [OpenAI : robots](https://developers.openai.com/api/docs/bots)

Ne pas réutiliser les anciens endpoints de ping Google/Bing. Vérifier les endpoints, OAuth/scopes et quotas avant une intégration, sans copier de jetons dans les livrables.

## Quotas et limites d’indexation vérifiés

Les pages Bing consultées le 23 octobre 2026 annoncent jusqu’à 10 000 soumissions d’URL par domaine et par jour pour la soumission manuelle et l’API, avec des lots API pouvant contenir jusqu’à 500 URL. La page précise que le quota réel peut être inférieur et varie selon les paramètres du site. Le workflow demandé par l’utilisateur plafonne malgré cela les soumissions directes à 100 URL uniques éligibles Bing par exécution ; présenter 100 comme limite de workflow, pas comme le quota officiel Bing. La même page annonce le retrait des anciens endpoints SOAP/POX au 31 août 2026 : relire la documentation courante et privilégier IndexNow ou l’API REST documentée, sans reprendre d’exemples d’anciens endpoints.

L’API GSC Sites.add ajoute une propriété au compte, mais ne valide pas la propriété du domaine. Les propriétés Domaine exigent une preuve DNS. L’API Sitemaps permet de soumettre un sitemap. L’API URL Inspection renvoie l’état de l’index en lecture seule ; elle ne demande pas de nouvelle exploration. Pour demander l’exploration d’une URL Google, utiliser l’interface Search Console lorsqu’elle le permet et respecter le quota quotidien affiché, qui n’est pas un plafond général fixe de 100. Ne jamais utiliser l’Indexing API pour des pages ordinaires.

## Moteurs complémentaires

- **Yandex**, si pertinent pour le marché : [droits](https://yandex.com/support/webmaster/en/service/rights), [sitemaps](https://yandex.com/support/webmaster/en/indexing-options/sitemap), [réexploration](https://www.yandex.com/support/webmaster/en/robot-workings/site-reindex). Réutiliser le site exact et les droits existants ; sinon fichier HTML, meta ou TXT autorisé. Les variantes de protocole/hôte sont distinctes. Soumettre le sitemap dans Indexing → Sitemap files ; les pages modifiées dans Reindex pages, selon quota affiché. « Request processed » constate une visite, pas une indexation. Préserver les preuves de validation.
- **DuckDuckGo** : [sources](https://duckduckgo.com/duckduckgo-help-pages/results/sources) et [DuckDuckBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot). Liens/images principalement issus de Bing, avec d'autres sources et son propre crawler. Vérifier Bing et l'accès du robot ; pas de portail direct établi dans ces sources. Une action Bing ne prouve pas une présence DuckDuckGo.
- **Yahoo** : [outils webmaster](https://help.yahoo.com/kb/SLN2213.html), [soumission](https://help.yahoo.com/kb/SLN2217.html). Extraits officiels consultés : Bing et Slurp mentionnés ; pages complètes non obtenues (429/consentement). Vérifier la directive Sitemap dans robots.txt et la prise en charge Bing ; ne pas inventer de formulaire ni reprendre un ancien ping. Relation et procédure détaillée restent à confirmer lors de l'exécution.
- **Bing** : [sitemaps et recherche IA](https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/) ; [soumission d'URLs](https://www.bing.com/webmasters/help/URL-Submission-62f2860b). Les aides dynamiques peuvent être vides dans un lecteur texte : consulter l'interface autorisée avant d'écrire. L'import Search Console peut aussi importer des sitemaps ; inventorier le résultat avant une soumission supplémentaire.

## Recherche IA : contrôles distincts

- **OpenAI** : documentation bots ci-dessus. OAI-SearchBot concerne la recherche, GPTBot l'entraînement, ChatGPT-User certaines actions utilisateur. Les règles robots.txt peuvent ne pas s'appliquer à ces récupérations à la demande ; l'accès recherche n'autorise pas implicitement l'entraînement.
- **Anthropic** : [robots officiels](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler). Claude-SearchBot concerne la recherche, ClaudeBot la collecte pouvant servir à l'entraînement, Claude-User la récupération à la demande. Vérifier chaque règle séparément et conserver les choix existants ; aucune soumission universelle établie ici.
- **Perplexity** : [crawlers et WAF](https://docs.perplexity.ai/docs/resources/perplexity-crawlers). PerplexityBot sert la recherche, Perplexity-User les demandes utilisateur ; la documentation indique que ce dernier ignore généralement robots.txt. Ne pas traiter robots.txt comme protection privée. Pour une exception WAF autorisée, combiner identité et plages IP officielles actuelles, limiter la règle au trafic nécessaire et vérifier les logs ; un user-agent seul est usurpable. Ne pas désactiver globalement le WAF.
- **Google Search IA** : [AI Overviews / AI Mode](https://developers.google.com/search/docs/appearance/ai-features). Indexation et possibilité d'afficher un extrait sont requises ; aucun fichier IA ou balisage spécial n'est exigé. Googlebot contrôle le crawl Search ; Google-Extended concerne certains autres usages, pas un robot de soumission à Search. [Annonce du contrôle IA et des rapports dédiés](https://blog.google/products-and-platforms/products/search/new-controls-website-owners/) : source plus récente que la page technique consultée. Vérifier sa disponibilité et le choix du projet dans Search Console ; ne pas basculer une exclusion volontaire. Distinguer annonce documentaire et disponibilité observée dans le compte. Ne pas attribuer toutes les impressions Web à l'IA.

## Local et commerce : uniquement si applicables

- **Google Business Profile** : [éligibilité](https://support.google.com/business/answer/13763036?hl=en). Vérifier contact physique avec les clients et exceptions documentées ; une entreprise uniquement en ligne n'est pas éligible par défaut. Rechercher une fiche existante et les droits, puis préparer validation et informations réelles. Une création de compte ou publication de coordonnées demande l'autorisation adaptée.
- **Bing Places** : [aide officielle](https://www.bing.com/forbusiness/help/modernExperience?setlang=en). Extrait officiel consulté : revendication/ajout de fiche et cohérence des informations ; page complète vide dans ce lecteur. Vérifier marché, éligibilité et méthode de validation dans l'interface avant toute action. Une fiche est distincte de Bing Webmaster Tools.
- **Google Merchant Center** : [fiches gratuites](https://support.google.com/merchants/answer/13889434?hl=en), [vérification et revendication de boutique](https://support.google.com/merchants/answer/11586344?hl=en). Réutiliser compte/catalogue ; vérifier produits éligibles, données exactes, disponibilité/prix, retours et livraison requis selon marché. Vérification et revendication sont distinctes ; une URL ne peut être revendiquée que par un compte hors organisation MCA prévue. Si un autre compte la revendique, ne pas déplacer ses droits automatiquement. Une autorisation d'affichage gratuit ne prouve pas la diffusion.
- Images, vidéos et actualités : traiter les extensions sitemap et critères officiels uniquement si ces contenus existent ; aucune campagne ni catalogue fictif. Les modules non étudiés restent NON_VERIFIE, pas « testés ».

## Points techniques à reconsulter

- [Google noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) : bloquer le crawl peut empêcher sa lecture ; conserver l'authentification des pages privées.
- [Droits Sitemaps dans Search Console](https://support.google.com/webmasters/answer/7451001?hl=en) : vérifier le rôle de l'utilisateur pour l'action et le canal réels.
- [Participants IndexNow en JSON](https://www.indexnow.org/searchengines.json) : consulter la liste et les métadonnées au moment d'une intégration ; ne pas figer les participants ni supposer Google couvert. Les limites et réponses proviennent du protocole, pas d'un test effectué ici.
