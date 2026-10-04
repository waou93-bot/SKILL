# Opérateurs et procédures officielles

Base documentaire vérifiée le 5 octobre 2026 pour Google, Bing, IndexNow et OpenAI. Reconsulter les sources au moment de l'exécution : disponibilité, procédures, quotas et participants peuvent évoluer. Les entrées conditionnelles ci-dessous sont des pistes à vérifier, pas des intégrations testées.

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
- [Bing : retrait de la soumission anonyme](https://blogs.bing.com/webmaster/2022/5/Spring-cleaning-Removed-Bing-anonymous-sitemap-submission/)
- [IndexNow : protocole](https://www.indexnow.org/documentation)
- [IndexNow : questions et limites](https://www.indexnow.org/faq)
- [IndexNow : participants](https://www.indexnow.org/searchengines)
- [OpenAI : robots](https://developers.openai.com/api/docs/bots)

Ne pas réutiliser les anciens endpoints de ping Google/Bing. Vérifier les endpoints, OAuth/scopes et quotas avant une intégration, sans copier de jetons dans les livrables.
