# SEO, sources actuelles et recette

## Sources primaires

Vérifier la documentation officielle au moment d'utiliser une règle technique ; le skill est une méthode, pas un calendrier de garanties. Repères consultés le 3 octobre 2026 :

| Sujet | Source officielle | Application |
| --- | --- | --- |
| Liens rémunérés | https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links | `sponsored` pour une relation rémunérée ; sémantique des liens |
| Facettes | https://developers.google.com/crawling/docs/faceted-navigation | Choisir stratégie de crawl/indexation et éviter un espace infini d'URLs |
| Navigation commerce | https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure | Catégories et fiches accessibles par liens |
| URLs commerce | https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites | Paramètres, variantes et cohérence des URLs |
| Product snippets | https://developers.google.com/search/docs/appearance/structured-data/product-snippet | Pages de produit, analyses et agrégateurs selon critères |
| Merchant listings | https://developers.google.com/search/docs/appearance/structured-data/merchant-listing | Rôle vendeur et offre réellement disponible |
| Descriptions | https://developers.google.com/search/docs/appearance/snippet | Résumer fidèlement chaque page ; extrait final décidé par le moteur |

Ces repères ont été consultés directement ou via résultats officiels. Relever dans le projet URL finale, date, passage utile et limite de consultation. Ne pas présenter une URL de référence comme une source lue dans un futur projet si elle n'a pas été ouverte.

Autres règles à consulter si elles s'appliquent : Google Search Essentials, contenu utile, sitemaps, robots/noindex, canonical, liens explorables, migration d'URLs, hreflang, images/vidéos et Discover. Utiliser les documents officiels actuels et la documentation du framework effectivement utilisé.

## Décider de l'indexation

Créer les pages utiles au visiteur. Pour chaque route, consigner une décision d'indexation liée à une intention et au contenu réel. Éviter combinaisons automatiques, pages vides, recherche interne sans valeur et données privées.

`robots.txt` règle l'exploration ; `noindex` nécessite que le moteur puisse lire la directive ; `canonical` désigne une version préférée et n'est pas une garantie d'exclusion. Ne pas appliquer automatiquement disallow + noindex à la même URL en supposant que les deux seront lus. Canonical n'est pas le seul remède à une explosion des facettes.

Un contenu distinct et indexable possède un canonical cohérent, une route correctement rendue, un titre/réponse utiles et un chemin de découverte. Le sitemap liste les URLs canoniques indexables attendues, pas les recherches, paniers ou erreurs. Une inclusion sitemap ne garantit pas l'indexation.

## Contrôles par environnement

| Contrôle | Preuve minimale |
| --- | --- |
| Fichiers/build | Commande exécutée, résultat et version source concernée |
| HTTP | URLs et statuts constatés ; distinguer 404 réelle et page erreur avec 200 |
| Accès moteurs | Robots, directives et rendu contrôlés, en précisant méthode et limite |
| Métadonnées | Title, description, canonical et langue sur un échantillon représentatif |
| Liens et navigation | Liens HTML, absence de pages importantes orphelines, retour utilisateur |
| Données structurées | HTML/JSON-LD lu, données visibles cohérentes, validation si outil disponible |
| Mobile/accessibilité | Navigation dans navigateur, clavier, focus, contraste, formulaires et images |
| Conversion | Événement/action réellement observé, échec/succès et absence de duplication |
| Mesures organiques | Export/rapport Search Console autorisé, période, pays, langue et limites |

Décrire population connue, échantillon, routes, appareil, environnement et date. Une extraction de texte ne démontre pas l'absence de JSON-LD. Un navigateur automatisé n'est pas un test avec visiteurs réels. Une note globale ne masque pas un défaut critique.

## Gabarits et parcours

Échantillonner accueil, offre/catégorie, fiche, guide/comparatif, situation interactive, paramètres, langues et erreur selon ce qui existe. Tester le changement de filtre, route profonde, rechargement et navigation retour. Le texte utile et les liens restent accessibles sans dépendre uniquement d'un canvas ou d'un parcours de questionnaire.

Prévoir sémantique des titres, libellés accessibles, dimensions réservées des médias et provenance. Contrôler le rendu des médias dans les breakpoints finaux. Éviter l'image qui montre une variante différente ou un accessoire absent de l'offre.

## Mesure et décision

Vitrine : demande effectivement reçue puis qualification si données disponibles. Marchand : commande confirmée et dédupliquée, avec mode test identifié. Affiliation : clic exact ; ventes/commissions rapportées séparément. Ne pas additionner deux rapports qui contiennent déjà le même événement.

Définir baseline, hypothèse, événement, fenêtre et critères continuer/corriger/arrêter/non concluant adaptés au volume observé. Aucun seuil arbitraire n'est une loi universelle. Proposer fréquence de maintenance ou de mesure ; ne pas créer une automatisation permanente à partir de cette proposition.

## Migration et publication

Inventaire des URLs et données existantes, mapping pertinent, sauvegarde/retour arrière, tests des redirections et contrôle de la version servie. Ne pas rediriger toutes les anciennes pages vers l'accueil. Protéger les pages utiles et données privées. Une publication autorisée et une version déployée ne prouvent pas un classement ni une conversion future.
