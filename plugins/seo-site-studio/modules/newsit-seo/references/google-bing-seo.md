# Contrat obligatoire Google et Microsoft Bing

## Actualité et portée

Lire les [principes Bing](bing-principes.md) en complément de ce contrat : ils précisent la couverture recherche/Copilot, les contrôles de contenu et la mesure des citations.

Il n'existe pas de certification universelle « toutes les normes SEO ». Google et Bing publient exigences, politiques et recommandations ; Schema.org, HTML, robots et sitemaps ajoutent des spécifications techniques. Pour chaque projet complet, lire les sources officielles actuelles, inventorier toutes les dimensions ci-dessous et compléter les nouvelles exigences découvertes. La date du skill ne rend pas ses règles actuelles par elle-même.

Consigner règle, moteur, applicability, source, date de consultation, preuve, environnement, résultat et correction. Reprendre la matrice [SEO obligatoire](../assets/seo-obligatoire.csv). Ne pas considérer une case « présente dans le code » comme test réussi. Évaluer chaque gabarit et les exceptions ; documenter toute dimension non applicable.

En conception, chaque exigence applicable reçoit une spécification et une preuve attendue. En réalisation, elle reçoit un contrôle réellement exécuté. Les échecs critiques empêchent l'annonce « prêt pour publication » ; les points inaccessibles restent `NON_VERIFIE`, avec conséquence et resolver.

## Métadonnées légitimes et contenu visible

| Élément | Exigence |
| --- | --- |
| `<title>` | Titre propre à la page, descriptif, concis, fidèle à l'intention et à la marque ; généré de façon cohérente avec les données |
| Meta description | Résumé spécifique, utile et fidèle ; pas de liste de mots-clés ni de promesse de reprise exacte par le moteur |
| H1/H2 et titre visuel | Structure et titre principal lisibles dans la page ; aucune injection de titres cachés destinés aux moteurs |
| `alt` et accessibilité | Décrire l'image utile selon sa fonction ; `alt` vide pour décoration ; noms accessibles exacts, pas de bourrage de mots-clés |
| JSON-LD | Types/propriétés réellement applicables et cohérents avec le contenu visible ; ni avis, offres, personnes ou prix inventés |
| Canonical/langues | URLs cohérentes, langue du document et alternatives/hreflang pertinents si multilingue |
| Open Graph/cartes sociales | Titres, descriptions et images cohérents pour partage ; ne pas les présenter comme garantie de ranking Google/Bing |
| Directives robots/HTTP | Intentions d'indexation/extrait explicites et compatibles avec les exigences de chaque moteur |

Le `title` n'est pas un texte affiché dans le corps de page ; il peut être visible dans l'onglet et les résultats. Une meta description n'est pas un paragraphe invisible à charger avec tous les mots-clés. Google et Bing peuvent reconstruire titre/extrait à partir d'autres signaux. Ne pas présenter une limite fixe de caractères comme une exigence universelle.

Ne pas créer texte blanc sur blanc, opacité nulle, H1 hors écran, texte derrière image ou contenu réservé au user-agent moteur pour le classement. Les accordéons consultables, onglets utiles et textes destinés aux lecteurs d'écran servent l'usage et ne constituent pas cette manipulation. `meta keywords` ne produit pas de gain d'indexation ou de classement dans Google ; ne pas l'utiliser comme livrable SEO de valeur.

## Matrice des dimensions à examiner obligatoirement

| Dimension | Points à spécifier/intégrer/vérifier |
| --- | --- |
| Politiques et contenu utile | Réponse distinctive, sources/expérience réelles, transparence commerciale, absence de cloaking/spam et production massive pauvre |
| Accessibilité aux crawlers | Googlebot/Bingbot, robots.txt, directives meta/X-Robots-Tag, sécurité/CDN et ressources nécessaires |
| Rendu et navigation | HTML utile, contenu/href découvrables, routes profondes, cohérence mobile et absence de contenu réservé aux robots |
| HTTP et erreurs | HTTPS, domaine préféré, 200/404/410 et redirections pertinents, absence de soft 404 ou chaînes accidentelles |
| Métadonnées | Title/descriptions propres, titres visibles, langue et cohérence des templates |
| Indexation et doublons | Canonical, facettes, tri, recherche, pagination, variantes, pages privées et pages faibles |
| Découverte | Liens internes descriptifs, pages importantes reliées, sitemap canonique et `lastmod` reflétant une modification réelle |
| Données structurées | JSON-LD/Schema.org appropriés, propriétés complètes selon règles du moteur et validation sur la version servie |
| Médias | Formats, dimensions, alternatives, droits, rendu et règles images/vidéos selon besoin |
| Mobile et performance | Responsive, accessibilité, stabilité et interactions ; performances labo/terrain distinguées, Core Web Vitals si mesurables |
| Profils | Local, commerce, affiliation, international, actualité/Discover uniquement si activité et contenu le justifient |
| Google Search Console | Préparer vérification et sitemap ; inspection/rapports seulement avec accès autorisé, indexation non garantie |
| Bing Webmaster Tools | Préparer vérification et sitemap ; inspections/rapports Bing seulement avec accès autorisé |
| IndexNow | Évaluer si adapté et supporté ; URLs ajoutées/modifiées/supprimées, propriété/clé et réponses contrôlées ; notification différente de l'indexation |
| IA et extraits | Identifier directives réellement supportées par moteur, choix d'exposition et mesure des mentions/citations/clics ; pas de promesse Copilot ou AI Overview |
| Migration et exploitation | Mapping, retour arrière, version servie, liens/données périmés et plan de mesure/maintenance |

Toutes ces dimensions sont inventoriées ; elles ne sont pas toutes pertinentes à chaque site. Un site monolingue n'a pas besoin de faux hreflang. Une vitrine n'a pas besoin de faux Product. Une FAQ utile n'autorise pas automatiquement un résultat enrichi.

Préparer Search Console, Bing Webmaster Tools et IndexNow ne signifie pas créer des comptes, soumettre un sitemap ou publier une clé sans autorisation correspondante. Ne pas activer une automation récurrente par défaut. Ne pas annoncer de contrôle d'indexation depuis la seule présence de robots/sitemap.

Les directives de snippets et d'usage IA peuvent limiter les aperçus/réutilisations sans empêcher l'indexation. Vérifier la sémantique Google/Bing actuelle avant `nosnippet`, `data-nosnippet`, limites d'aperçu, `noarchive` ou `nocache`. Ne pas copier une consigne d'entraînement d'un robot vers tous les crawlers de recherche.

## Sources primaires et limites du snapshot

| Repère | URL | État à la création, 3 octobre 2026 |
| --- | --- | --- |
| Google spam policies, dont hidden text | https://developers.google.com/search/docs/essentials/spam-policies | Lu directement ; autorise les usages UX/accessibilité, distingue la manipulation |
| Google title links | https://developers.google.com/search/docs/appearance/title-link | Lu directement ; un title influence la préférence, le moteur peut le modifier |
| Google meta et attributs | https://developers.google.com/search/docs/crawling-indexing/special-tags | Repère officiel retrouvé dans les résultats, à ouvrir pour règle spécifique |
| Google sitemaps | https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap | Documentation officielle consultée ; sitemap différent de garantie d'indexation |
| Bing Webmaster Guidelines | https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a | URL consultée, contenu dynamique non extrait ; lecture actuelle complète à faire dans le projet |
| Bing choix du titre | https://blogs.bing.com/webmaster/2014/6/How-Does-Bing-Choose-The-Title-For-My-Web-Page/ | Source officielle historique retrouvée ; ne suffit pas à certifier toutes les règles actuelles |
| Bing data-nosnippet | https://blogs.bing.com/webmaster/2025/10/Bing-Introduces-Support-for-the-data-nosnippet-HTML-Attribute/ | Publication officielle lue directement ; contenu découvrable distinct d'aperçu |
| IndexNow documentation | https://www.indexnow.org/documentation | Lu directement ; 200 prouve réception, pas indexation |
| IndexNow FAQ | https://www.indexnow.org/faq | Source officielle lue directement ; indexation non garantie |

Compléter ces repères avec les guides officiels nécessaires au type réel du site. Un accès impossible ou un snapshot ancien interdit de déclarer l'exhaustivité actuelle vérifiée, mais n'empêche pas de travailler sur les exigences déjà connues et sourcées.


## Actualisation Bing — 4 octobre 2026

Le texte officiel indexé des Guidelines a été consulté ; le rendu direct reste une application JavaScript non extraite. Les 22 principes et les pratiques abusives sont reliés au parcours dans bing-principes.md. Cette lecture ne certifie pas la conformité d’un site. Les mesures AI Performance restent distinctes du classement et des conversions.
