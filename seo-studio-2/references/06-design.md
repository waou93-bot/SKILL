# Design et expérience de lecture

## Hériter des règles, créer l'identité

Lire les références de Design DNA pertinentes : préférences, typographie, motion,
images, anti-slop et qualité. Inscrire la provenance de chaque préférence et des
exceptions dans `PROJECT_SKIN.yaml`. Garder les choix déjà validés ; les arbitrages
d'un autre projet ne deviennent pas ceux de cette niche.

L'ordre de travail est : besoin produit, concept visuel, composition, typographie,
grille, images, interaction, motion, composants puis technique. Écrire un concept
visuel concret, deux pistes réellement différentes et une recommandation justifiée.
Le choix final suit la procédure d'approbation de l'hôte et les permissions actuelles.
Sans sélection obligatoire encore obtenue, livrer une proposition marquée telle et
ne pas prétendre que le rendu final a été approuvé.

## Ce que le skin doit décider

Définir palette et contrastes, rôles typographiques, largeur de lecture, échelle de
texte, grille, densité, espacements, photographie/illustration, ratio d'images,
iconographie, bordures/surfaces, intensité du mouvement, signature propre au projet,
états et fallbacks. Une signature peut être un tableau de diagnostic ou un parcours
de choix utile ; une animation spectaculaire n'est pas une obligation.

Ne pas choisir Inter, Plus Jakarta Sans ou une police condensée par automatisme.
Une fonte neutre peut convenir si sa justification et la hiérarchie sont bonnes.
Pas de petites flèches décoratives ajoutées aux CTA, même au survol ; préserver les
indications fonctionnelles de direction, état et destination externe. Pas de faux
logos de partenaires, compteurs clients, avis, badges d'expertise ou photos de produit
approximatives. Une image générée d'ambiance porte son statut d'illustration.

## Gabarits à spécifier

Définir accueil, hub, article, guide, comparatif, résultat d'outil, page partenaire,
méthode et contact selon leur pertinence. Pour chaque gabarit : rôle, sections dans
l'ordre, hiérarchie visuelle, contenu exact des labels, navigation, CTA principal,
CTA secondaire éventuel, preuve, monétisation, état vide et prochaine étape.
Ne pas aligner tous les gabarits sur la même succession hero + trois cartes + FAQ.

Un article donne rapidement sa réponse, puis nuances et critères ; sa lecture ne
commence pas par un tunnel commercial. Le guide permet au lecteur de retrouver sa
contrainte. Le comparatif distingue critères mesurés, déclarés fabricant et inconnus.
L'encart partenaire reste identifiable, sans imiter un conseil neutre ou recouvrir
les informations nécessaires. Sur mobile, préserver l'ordre des critères et un
moyen compréhensible de comparer plutôt que rétrécir les colonnes à l'extrême.

## Recherche en tête des rubriques

Une rubrique est concernée lorsque son catalogue est étoffé, sa liste paginée ou
son contenu difficile à parcourir rapidement. Tenir compte du corpus réel ou prévu
en V1 ; ne pas imposer un seuil arbitraire à tous les sites. Documenter les rubriques
concernées dans l'architecture et les briefs. Une courte liste lisible peut conserver
une navigation simple, avec cette justification.

Placer un champ de recherche visible après le titre et la courte introduction
éventuelle, avant les filtres, cartes, grilles ou listes. Le rendre directement
accessible sur mobile ; ne pas le cacher uniquement dans le menu, derrière une
icône ou en bas de page. Conserver le H1 et les accès aux catégories.

Adapter le libellé visible au périmètre : « Rechercher un produit », « Rechercher
un article », « Rechercher un guide » ou « Rechercher dans les ressources ».
Un placeholder ne remplace pas le libellé accessible. Prévoir une action de recherche
compréhensible, l'envoi avec Entrée et un contrôle pour effacer la requête.

La recherche couvre par défaut toute la rubrique, pas seulement les cartes chargées
ou la page de pagination courante. Pour des produits, couvrir nom, marque et référence
lorsque ces données existent ; pour des articles et guides, titre, sujet et catégories
documentées. Un hub mixte identifie les types dans les résultats et peut proposer
un filtre produit/article/guide. Les filtres retenus restent visibles et leur effet
sur la recherche est expliqué. Ne pas élargir silencieusement au site entier.

Spécifier résultats liés aux bonnes pages, ordre de pertinence, nombre de résultats,
pagination éventuelle, états chargement/erreur/aucun résultat et remise à zéro.
Une requête vide retrouve la liste initiale ; l'absence de résultat aide à reformuler
ou à retirer un filtre. Définir le traitement de la casse et des accents. Réutiliser
la recherche existante si adaptée ; choisir filtre local ou index côté serveur selon
le corpus et la performance, sans imposer un service tiers. Garder les contenus et
leurs liens accessibles lorsque la recherche est indisponible.

En préproduction, livrer spécification et critères. En réalisation autorisée,
tester une entrée connue hors de la première page, une recherche sans résultat,
une requête vide, effacement, filtres éventuels, liens des résultats, clavier et
petit écran. Un champ sans logique ou une recherche partielle non annoncée échoue
à la recette. Distinguer ces tests réellement exécutés du seul contrôle documentaire.
Appliquer la politique des recherches internes et filtres de
[la référence technique](09-technical.md) ; la présence du moteur ne rend pas ses
pages de résultats indexables par défaut.

## Contrat des composants

Pour les cartes et offres produits, appliquer [le contrat partenaires](08-partners.md) :
URL affiliée autorisée vers le modèle chez le partenaire confirmé, paramètres conservés,
bouton « Voir le prix » ou « Voir le modèle sur [partenaire] », et mention d'affiliation
visible séparée du bouton. Le texte et le libellé accessible du bouton n'emploient
pas « lien affilié ». Nom ou image cliquables à des fins commerciales suivent la même
destination. Spécifier l'état sans URL affiliée sans faux accès actif ; les liens
de sources et de tests restent distincts.

Chaque composant comporte props/données, texte, sources, variantes de contenu,
états default/hover/focus/open/loading/empty/error/unavailable, rôle sémantique,
clavier, largeur mobile, comportement sans JS et événement utile. Prévoir les
libellés longs, un seul résultat, zéro offre vérifiée et prix inconnu. Un encart
sans partenaire réel disparaît sans laisser un rectangle publicitaire vide.

Les tableaux conservent en-têtes, unités et lecture accessible. Les filtres exposent
ce qu'ils modifient ; les résultats expliquent leur logique et n'inventent pas une
compatibilité. Prévoir correction des champs, unités, bornes, erreurs, données
incomplètes et un chemin manuel lorsque l'outil ne peut pas conclure.

## Preuves visuelles

En étude d'un site existant, capturer des pages représentatives sur desktop et mobile
avec URL, date, viewport, état et statut consentement. Inspecter menu ouvert, focus,
comparatif long, formulaire invalide, sans résultat, contenu déplié et motion réduite.
Des viewports de départ 1440 et 390 px sont un protocole interne ajustable, pas une
preuve sur un téléphone réel ; vérifier aussi les petits écrans utiles au projet.

Sans captures rendues, noter `SOURCE_ONLY` ; ne pas noter le contraste, la qualité
photo, les animations ou l'ergonomie tactile comme vérifiés. Une maquette image
n'est pas un test d'interaction et un navigateur desktop rétréci n'est pas Safari iOS.
Les contrôles WCAG, clavier, lecture et reflow s'appuient sur S12, avec périmètre
déclaré ; aucun script de ce package ne certifie l'accessibilité du futur site.

## Performance et motion

Le contenu important est accessible sans attente d'intro ou de slider. Réserver
l'espace des médias, adapter les images au viewport, limiter JS et polices, préserver
`prefers-reduced-motion` et le clavier. Une image LCP ne doit pas être traitée comme
un média hors écran chargé tardivement. Budgets et mesures sont définis dans le
plan technique ; ne pas annoncer les Core Web Vitals depuis une inspection visuelle.

## Recherche et réalisation autonomes

Pour la typographie, les composants, la landing et les médias, appliquer
[le protocole de réalisation](13-autonomie-production.md) : benchmark rendu,
police réellement identifiée ou alternative autorisée, états des boutons, accès
rapide au corpus, images professionnelles et preuve desktop/mobile. Une retouche
conserve le skin validé ; ne pas demander deux nouvelles pistes ni une nouvelle
validation artistique quand la décision locale réversible est déjà autorisée.
