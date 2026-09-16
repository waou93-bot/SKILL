# Modules conditionnels : IA et types de projets

## Google et résultats IA

Google indique que les fondamentaux SEO restent pertinents pour AI Overviews et
AI Mode ; aucun fichier IA ni schema spécial n'est nécessaire. L'éligibilité n'est
pas une garantie d'apparition. Garder informations utiles en texte et balisage en
accord avec ce que le visiteur voit. [S14]

Actualisation vérifiée le 16/09/2026 : une annonce Google du 03/06/2026 porte sur des
rapports Search Generative AI ; une note mentionne un déploiement mondial achevé
le 31/08/2026. Ils décrivent notamment des impressions ventilées par page/pays/date
et appareil selon la surface. Ces données font aussi partie des rapports globaux.
Ne pas s'appuyer sur une vieille page disant uniquement « tout est agrégé » pour
nier ces rapports. Vérifier les métriques effectivement disponibles dans la propriété ;
ne pas inventer de clics, conversions ou rapports API IA séparés. [S15]

La page AI features consultée porte encore des explications générales sur le rapport
Web : conserver les deux niveaux au lieu de supposer une contradiction absolue.
Les fonctionnalités peuvent évoluer après cette version du skill.

## Bing, Copilot et ChatGPT

Bing a annoncé AI Performance le 10/02/2026 ; les citations mesurées ne sont ni un
rang SEO ni une conversion. L'accès et les dimensions courantes se vérifient dans
la documentation et le compte, pas par supposition. [S16]

La documentation OpenAI distingue OAI-SearchBot (recherche) et GPTBot (entraînement).
Les choix sont indépendants. Ne pas ouvrir tous les robots pour « faire du GEO ».
Respecter le souhait de visibilité et les droits du propriétaire. Aucun changement
de robots.txt/CDN sans autorisation explicite dans le périmètre. [S17]

Les renvois ChatGPT peuvent se mesurer via analytics/paramètres de provenance ; la
FAQ éditeur décrit utm_source=chatgpt.com. Examiner l'instrumentation réelle, sans
supposer que tout le trafic IA est attribué ni que chaque citation est cliquée. [S18]

## Mesurer sans fausse précision

Distinguer : accès robot, présence indexée, mention, citation avec URL, clic, conversion.
Pour un test manuel d'assistant : consigner moteur/version si visible, date, langue,
contexte, prompt exact, répétitions et réponse. Une absence sur quelques prompts ne
prouve pas invisibilité générale ; une présence ne prouve pas une part de marché.
Les conseils GEO non documentés restent des hypothèses à tester.

## Activité locale

Vérifier l'éligibilité Google Business Profile et la réalité de l'activité, du lieu,
de la zone desservie et des horaires. Les activités exclusivement en ligne ne sont
pas éligibles par défaut. Ne pas créer d'adresse fictive ni de pages clonées par ville.
Mesurer contacts qualifiés/réservations si tel est l'objectif, pas seulement la position
sur une grille géographique. [S19]

## International

Vraies pages localisées, navigation linguistique accessible, canonicals cohérentes,
hreflang réciproques si applicable ; ne pas canoniser toutes les langues vers le
français. La localisation couvre offre et vocabulaire, pas seulement la traduction.
Ne pas inventer la demande d'un pays. Vérifier les règles du moteur. [S11]

## Commerce et applications

Commerce : catégories/produits/variantes, filtres/paramètres, stock/prix exacts,
données structurées éligibles et chemin jusqu'à l'achat. Vérifier les guides du type
de résultat avant implémentation. Ne pas baliser des avis ou offres inexistants. [S12]

App/logiciel : distinguer site public, documentation, pages de téléchargement et
interface privée. Web SEO ne remplace pas ASO (stores) ni référencement YouTube.
Proposer une recherche spécialisée distincte si ce canal est décisif ; ne pas appliquer
ses règles sans documentation. Pas d'indexation des données personnelles des utilisateurs.

Arts/médias/association : adapter aux publics et actions réelles (écoute, information,
contact, adhésion...). Ne pas forcer un funnel SaaS. Pour photo/vidéo : médias utiles,
contexte, droits et accessibilité ; garder la DA validée.

Sources : [bibliographie](sources.md).

### Valeurs manquantes des exports

L’aide du rapport Search Generative AI Performance signale que des valeurs
indisponibles représentées par `~` ou `-` peuvent devenir zéro à l’export.
Documenter la sémantique du champ et conserver le statut indisponible lorsqu’il
est connu : ne pas transformer ce zéro technique en absence prouvée d’impressions.
Source [S22].
