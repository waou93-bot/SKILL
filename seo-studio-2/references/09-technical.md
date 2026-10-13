# Technique, SEO classique, recherche IA et mesure

## Deux options de réalisation

À chaque projet, présenter deux architectures réalistes, leurs coûts connus ou
inconnus, compétences, maintenance, édition, rendu, commerce éventuel, hébergement,
sécurité, performance et réversibilité. Recommander une option via ADR. Pour un site
existant, l'option de conserver la stack doit être examinée avant une migration.
Ne pas figer les versions ni les prix à partir de cette bibliothèque : vérifier la
documentation actuelle et le lockfile du projet.

Un site éditorial peut comparer rendu statique/serveur et CMS classique ; un commerce
compare les options marchandes réellement pertinentes ; un outil interactif peut
nécessiter plus d'état mais conserve ses contenus explicatifs accessibles. Le choix
se fait après produit, contenu et design, pas à partir d'un starter préféré.

## Matrice de spécifications SEO

Pour chaque gabarit, définir HTML initial/rendu, HTTP, URLs, canonical, robots meta,
X-Robots-Tag, robots.txt, sitemap, title/description, titres sémantiques, données
structurées applicables, hreflang si nécessaire, médias et maillage. Spécifier les
états suppression, erreur, redirect, preview et contenu privé. Les balisages doivent
correspondre aux données réelles affichées ; voir S07 et la documentation du type.

S01–S03 et S06 donnent le socle éditorial et d'exploration. Les scripts de ce package
ne crawluent pas le futur site et ne mesurent pas son indexation. `site:` est un indice,
pas un inventaire exhaustif. L'absence de JSON-LD dans un texte extrait ne prouve pas
son absence dans le HTML/rendu. Contrôler le HTML brut puis le DOM et les outils de
validation adaptés. Ne pas dépendre d'un outil retiré comme l'ancien Mobile-Friendly Test.

Pas de pages de recherche interne ou de variations de filtres indexables par défaut.
Préserver authentification et noindex des previews ; ne pas ouvrir une route privée
pour satisfaire un robot. Les sitemaps décrivent les URLs publiques canoniques
indexables et des `lastmod` honnêtes, pas toutes les routes de l'application.

Pour un site existant, appliquer [versions, dates et recette des branches](14-fanout-retour-sites.md).
Identifier source/commit ou artefact et version publique avant republication ;
préserver les routes plus récentes absentes de la copie locale. Pour lastmod et
dateModified, vérifier le changement significatif du contenu et sa provenance ;
le dernier commit du fichier, un build ou une restauration ne suffit pas seul.

## Qualité et performance

Objectifs internes par gabarit : poids média, JS initial, polices, budget tiers,
latence de l'outil, reflow et stabilité. Les bonnes valeurs de Core Web Vitals
sont LCP ≤ 2,5 s, INP ≤ 200 ms et CLS ≤ 0,1, mesurées au 75e percentile, segmentées
mobile/desktop (S11). Ce sont des objectifs terrain à vérifier, pas une prédiction
à partir d'un build. Les mesures de laboratoire diagnostiquent sans prouver les
résultats terrain. Une absence de données CrUX reste absence de données.

Tester poids/images responsive, dimensions réservées, chargement de l'image critique,
limite des scripts affiliés/analytics, interaction clavier et absence de blocage.
Préparer le protocole WCAG applicable (S12) ; un score automatique n'est pas une
certification. Prévoir les tests sur navigateurs et appareils réellement disponibles.

## Recherche IA

Le socle est une offre compréhensible et vérifiable, avec contenu et liens accessibles.
Google indique ne pas exiger de fichier IA ou de schema spécifique pour ses fonctions
IA (S08). OAI-SearchBot, GPTBot et les accès à la demande ont des rôles distincts (S09).
Ne pas changer la politique d'entraînement pour gagner du trafic. Une permission
robots n'est pas une garantie d'apparition ; un user-agent simulé n'est pas un vrai bot.

Produire, si pertinent, un panel fixe de questions problème/choix/contraintes/confiance,
avec pages de réponse et preuves. Mesurer séparément mention, citation, recommandation,
visite et action ; documenter plateforme, surface, date et personnalisation. Une API
n'est pas automatiquement un test de l'application grand public. Le chat déjà informé
sur ce projet n'est pas un témoin neutre. `llms.txt` reste une option motivée, pas un gate
magique de classement. Aucun texte caché, cloaking ou injonction pour manipuler l'agent.

## Plan de mesure

Définir les événements par rôle de page : lecture utile selon une définition locale,
outil commencé/terminé, critère choisi, comparatif consulté, clic partenaire, contact
qualifié, panier ou achat réellement observé. Chaque événement précise paramètres
non personnels, déclenchement, déduplication, consentement applicable, système source,
responsable et méthode de test. Ne pas envoyer de noms, emails, problèmes médicaux ou
texte libre sensible dans une URL/événement pour améliorer l'attribution.

Distinguer clics Search Console, sessions Analytics et conversions du partenaire ;
ils n'ont pas la même mesure ni le même périmètre. Pas de tracking tiers installé par
défaut. Pour France/UE, vérifier les règles CNIL et l'exemption éventuelle de mesure
d'audience selon la configuration réelle (S13), sans supposer que tout outil est exempt.

## Préparer l'après-déploiement, sans l'exécuter

Transmettre au vrai seo-post-deploy : domaine réel, accès/propriétés autorisés,
sitemap, URLs pilotes, preuve de recette, choix bots/consentement et registre existant.
Ne pas créer de propriété en doublon. Ne pas utiliser l'Indexing API Google générale
pour soumettre des articles ordinaires. IndexNow notifie ses participants, pas tous
les moteurs ; une notification reçue ne prouve pas l'indexation. Vérifier la procédure
primaire actuelle lors de l'action, pas seulement cette instruction.

Prévoir contrôles de lancement, après premières données puis aux fenêtres décidées.
Calendrier = plan, pas tâche récurrente créée. Toute surveillance effective nécessite
une demande et un ordonnanceur réel. Une soumission ou un déploiement ne se déduit pas
implicitement de « créer ma préprod ».
