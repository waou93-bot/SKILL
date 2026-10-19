# Architecture de référence et contrôle de l'indexation

## Cas source et limites

Cette architecture reprend le modèle observé sur [Quel Robot Tondeuse](https://www.quel-robot-tondeuse.fr/), combiné à l'analyse fournie par l'utilisateur. L'analyse source décrit robots.txt, douze sitemaps WordPress et la page d'accueil, avec environ 587 URL et des comptages approximatifs ; elle précise qu'il ne s'agit pas d'un crawl page par page et que les codes HTTP, canonicals, le maillage détaillé et l'indexation réelle n'ont pas été vérifiés.

La page d'accueil consultée le 19 octobre 2026 présente un hub de classement, des groupes de critères, des guides, des fiches produits, des comparatifs, des outils et des pages de confiance. Elle affiche cinq tranches de budget dans le menu. L'écart signalé entre menu et sitemap reste à vérifier dans les sitemaps réels ; un menu ou un sitemap ne prouve pas à lui seul l'indexation. Les nombres et risques rapportés pour ce cas sont des pistes de contrôle, jamais des quotas ni des faits universels.

## Squelette obligatoire pour un site multi-pages

Avant de figer l'arborescence, dessiner les nœuds applicables et consigner `INCLURE`, `ADAPTER`, `TESTER` ou `EXCLURE` pour chacun. Transposer les rôles selon la niche : « produit » peut devenir service, offre, recette, équipement, lieu ou autre entité réellement choisie par l'audience.

```text
Accueil
├── Hub principal de choix ou d'offre
│   ├── Pages de critères / catégories / facettes justifiées
│   ├── Pages de marques ou fournisseurs, si elles servent une demande réelle
│   └── Fiches produit / service / offre
├── Hub de comparatifs
│   └── Comparatifs sélectionnés, uniquement si chaque duel a une utilité distincte
├── Hub de guides
│   ├── Choisir et dimensionner
│   ├── Budget et achat
│   ├── Comparer et décider
│   └── Installer, utiliser, entretenir, résoudre, sécuriser selon la niche
├── Blog ou support, regroupé par besoins et étapes du parcours
└── Outils et confiance
    ├── Outils utiles (comparateur, calculateur, configurateur…)
    └── Méthode, transparence, rappels, contact et pages légales utiles
```

Le squelette est obligatoire comme grille de décision, pas comme obligation de publier chaque branche. Un site simple peut utiliser une version réduite ; un site de service peut remplacer produits/marques par services et zones seulement si l'offre et la demande les justifient. Documenter pourquoi un nœud est exclu. Ne jamais produire des pages pour remplir un schéma.

## Carte de pages avant création ou refonte

Pour chaque URL existante ou proposée, garder une ligne dans la carte canonique du projet avec :

- type de page, audience, besoin et intention principale ;
- rôle Business et action aval attendue ;
- requêtes observées ou hypothèse explicitement marquée, source et date ;
- valeur propre de la page : données, inventaire, expérience, expertise ou outil ;
- URL stable, parent/hub, liens internes entrants et sortants prévus ;
- décision d'indexation, canonical, robots et présence attendue dans le sitemap ;
- partenaire et destination sortante confirmés, si un lien commercial est prévu ;
- état : `CRÉER`, `GARDER`, `AMÉLIORER`, `FUSIONNER`, `DÉSAINDEXER`, `REDIRIGER` ou `SUPPRIMER`, avec preuve et autorisation nécessaires.

Une page séparée n'est justifiée que si elle sert une intention ou une tâche distincte, apporte une réponse substantiellement utile, s'appuie sur des informations suffisamment fiables et peut être entretenue. Une facette, une variante « non », une marque, une tranche de prix ou une paire de produits n'est pas automatiquement une page SEO.

## Règles de maillage

- L'accueil conduit aux hubs prioritaires, puis les hubs aux pages de critères, fiches, comparatifs et guides qui aident vraiment la décision.
- Une page de critère relie les produits/offres correspondants, le hub parent et le guide expliquant ce critère. Un guide renvoie vers les critères et pages commerciales pertinents ; un support renvoie au guide ou à l'offre qui résout le problème.
- Une fiche produit/service est reliée à son hub et à quelques comparatifs ou guides vraiment pertinents. Un comparatif relie les fiches concernées et le guide de décision utile.
- Le menu expose les tâches et rubriques principales, pas chaque combinaison de filtres. Une page trouvée dans un sitemap sans lien interne utile n'a pas un parcours éditorial satisfaisant.
- Vérifier les destinations, ancres, statuts et redirections à la profondeur de crawl déclarée. Ne déclarer une page orpheline qu'après exploration complète du graphe atteignable et de la population attendue.
- Les liens publics qui quittent le domaine restent soumis à la règle Studio 3 : destination partenaire confirmée uniquement ; garder les URLs de sources dans les notes internes.

## Indexation, facettes et sitemaps

- Réserver l'indexation aux URL canoniques, accessibles, utiles et différenciées. Vérifier réponse HTTP, directives robots/noindex, canonical, rendu, liens de découverte et Search Console quand l'accès existe.
- Un sitemap doit refléter la liste des URL canoniques et indexables voulues : exclure redirections, erreurs, paramètres de tri/recherche et pages volontairement non indexables. Une absence du sitemap n'établit pas un `noindex` ; rechercher la route, les directives et l'état Search Console. La présence dans le sitemap ne prouve pas l'indexation.
- Utiliser un sitemap index et des sitemaps par type si la taille ou le CMS le justifie ; aucun nombre fixe de sitemaps ou d'URL n'est une règle SEO. Contrôler les écarts entre routes/CMS, navigation, crawl, sitemaps et Search Console.
- Un filtre d'interface en `#fragment` ou paramètres ne crée pas une page d'atterrissage distincte pour le moteur. Si une intention mérite une page, créer une URL stable et découvrable, avec contenu et liens adaptés ; sinon garder le filtre comme outil de navigation sans multiplier les URL indexables.
- Ne pas bloquer dans robots.txt une URL qui doit être explorée pour que le moteur voie son `noindex`. Les règles robots et l'accès des bots IA sont des décisions distinctes et ne garantissent ni classement ni trafic.

## Contrôles qui corrigent les risques observés dans le cas source

| Risque à vérifier | Contrôle imposé par Studio 3 | Correction permise selon preuve |
|---|---|---|
| Grand volume de comparatifs X vs Y | Comparer GSC, recherche de requêtes, SERP, parcours et contenu réel. Refuser les combinaisons automatiques sans demande démontrée et différenciation éditoriale. | Garder les duels utiles ; fusionner, désindexer ou supprimer le reste selon trafic, liens, valeur et risque. Ne pas supprimer en masse sans historique et plan d'URL. |
| Cannibalisation entre articles | Faire une carte requêtes–intentions–URL, comparer les pages et les périodes GSC. Des sujets proches peuvent avoir des intentions distinctes. | Fusionner seulement quand les réponses se recouvrent ; préserver la meilleure URL et rediriger les anciennes si nécessaire. |
| Tranches de prix annoncées mais absentes d'un sitemap | Vérifier si chaque URL existe, son HTTP, canonical, robots, liens internes, sitemap et état GSC. Menu et sitemap ne sont pas interchangeables. | Corriger le sitemap si la page doit être indexable ; réparer le menu ou la route si elle n'existe pas ; ne pas inventer une page juste pour aligner des comptages. |
| Grandes requêtes servies par des filtres `#hash` | Vérifier requête et SERP. Les fragments servent à l'état d'interface, pas à des pages indexables séparées. | Créer une page dédiée si elle passe les critères d'intention et de valeur ; sinon garder un filtre UX et relier au guide général. |
| Slug inversé ou contradictoire avec la page | Vérifier le libellé, la destination, le contenu, les liens entrants et les signaux organiques ; distinguer erreur de lien et erreur d'URL. | Corriger le lien sans migration si seule la destination est erronée. Si le slug change, cartographier les anciennes URL, redirections 301, canonical, liens internes et sitemap, puis mesurer. |
| Facettes de faible valeur ou peu reliées | Contrôler découverte interne, assortiment, demande, qualité et utilité. Ne pas qualifier d'orpheline sur la seule absence du menu ; un crawl complet est nécessaire. | Garder et mailler celles qui aident réellement ; consolider ou exclure de l'index celles sans demande distincte ni réponse utile. Éviter les pages « non » ou micro-variantes sans preuve. |
| Marque mentionnée mais sans page dédiée | Vérifier offre/produits réellement disponibles, requêtes, SERP et possibilité de créer une page marque substantielle. Un article de panne ne prouve pas la demande d'une landing marque. | Créer une page marque seulement si elle aide au choix et a un contenu propre ; sinon garder la marque dans les fiches/guides pertinents. |
| Structure d'URL plate | Séparer organisation des URLs et maillage. Des dossiers lisibles aident la gestion mais ne créent pas seuls un silo ou un avantage de classement. | Utiliser des chemins cohérents par type si le site ou sa migration le justifie. Ne jamais déplacer des centaines d'URL uniquement pour « faire silo ». |
| Pages de confiance qualifiées de « solides » | Vérifier auteurs réels, méthode reproductible, sources, dates, limites, affiliations et corrections. Une page de transparence ne prouve pas à elle seule l'expérience ni la qualité du reste du site. | Décrire ce qui est réellement fait ; corriger les promesses et divulguer clairement les intérêts commerciaux. |

## Protocole d'audit et de migration

1. Nommer les sources utilisées : robots.txt, chaque sitemap, navigation, routes CMS, crawl, Search Console et date de consultation. Marquer chaque constat `OBSERVÉ`, `DÉDUIT`, `À VÉRIFIER` ; estimer la couverture et les écarts.
2. Si l'on n'a lu que robots/sitemaps/home, rapporter une préanalyse, jamais un crawl ni une validation d'indexation. Les comptages XML sont des candidats à vérifier, pas des nombres de pages publiées ou indexées.
3. Avant toute correction structurelle, conserver les URL/pages ayant impressions, clics, liens, ventes ou utilité démontrée. Toute fusion/suppression/migration a une carte d'URL, redirections, canonicals, liens internes, sitemap, mesure et retour arrière proportionné.
4. Après une publication autorisée, vérifier les pages et sitemaps publics, redirections et données disponibles. Ne pas promettre une indexation ni déduire le succès de la seule soumission d'un sitemap.