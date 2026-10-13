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

## Contrat des composants

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
