# Audit de couverture, de parcours et de versions

Lire pour un audit éditorial complet, un audit SEO/IA commun, une révision fan-out
ou une préparation de republication. Limiter un audit technique ciblé aux points
pertinents. Cette référence complète les contrôles page par page du skill.

## Couverture utile : question → réponse → preuve → action

Appliquer [le contrat fan-out](../../ai-seo/references/query-fanout.md), présent dans
la distribution conjointe. Si ai-seo manque, poursuivre avec la table ci-dessous,
signaler la référence indisponible et consulter la documentation primaire actuelle.
Ne pas relancer une orchestration Studio pour un audit de quelques pages.

Pour chaque page prioritaire, relever question principale, public, contraintes et
sous-questions utiles. Lire le corps réel, puis chercher les pages et sections déjà
présentes. Les branches sont observées avec preuve, ou des hypothèses éditoriales ;
aucun inventaire ne prouve les sous-requêtes cachées d'un moteur IA.

| Sous-question / provenance | URL et section inspectées | Réponse et preuve | État de couverture | Décision et URL propriétaire | Lien / action suivante | Recette |
|---|---|---|---|---|---|---|

États : `REPOND`, `PARTIEL`, `ABSENT` après inspection, sinon `NON_VERIFIE`.
Décisions : conserver, enrichir une section, lier une page existante, créer pour une
tâche distincte, exclure du périmètre ou bloquer l'affirmation faute de preuve.
Le changement reste proposé pendant un audit en lecture seule.

Contrôler utilité et justesse, pas un quota de mots/questions : réponse directement
compréhensible, critères conditionnels, exemples/procédures pertinents, sources
proches des affirmations et limites. Une faible longueur ne démontre pas du thin
content. Distinguer un guide documentaire d'un test produit réellement exécuté.

Comparer title, H1, H2/H3 et description avec cette couverture. Une description qui
promet compatibilité, autonomie ou conseil absent du texte est une incohérence à
prouver. Une longueur hors convention projet est un indice éditorial. Fournir
propositions avant/après propres à chaque page, avec raison et critère de relecture.
Ne pas changer les textes visibles pendant une simple mission de métadonnées.

## Maillage, hubs et interfaces

Construire les relations hub → guide → article/tutoriel → sélection/outil/action
selon le site. Séparer liens contextuels, navigation, footer, widgets et liens
conditionnels. Vérifier destination finale, ancre, section et chemin retour utile.
Les compteurs de liens servent le diagnostic ; aucun seuil de trois entrants, quota
de liens ou maillage totalement réciproque n'est un facteur universel.

Pour filtre, sommaire, carte, accordéon ou expérience 3D : comparer HTML initial,
rendu et interaction pertinente avant de déclarer un lien ou une réponse absente.
Déclarer la population attendue et la couverture du crawl avant de qualifier un
orphelin. Un domaine qui couvre plusieurs univers peut organiser ses besoins en
hubs ; la dilution supposée seule ne justifie pas une suppression de contenus.

Dans un réseau de sites, la tâche dicte le site propriétaire et la passerelle.
Vérifier les pages réellement présentes ; éviter guides dupliqués et liens entre
tous les sites par défaut. Une proposition de lien n'est pas un lien en production.

## Versions, routes et dates

Avant de proposer une publication, identifier domaine final, URL de déploiement,
source faisant foi, branche/commit ou version d'artefact, copie locale et build.
Produire les différences d'URL entre production et snapshot, puis préserver les
routes publiques utiles absentes de la copie. Si la source reste ambiguë, arrêter
la republication de ce site et poursuivre les sites/actions indépendants.

Contrôler sitemap → réponse HTTP/destination finale → canonical → indexabilité →
source. Un changement de slash ou de domaine peut modifier ces signaux. Les comparer
sur les URL finales, avec exceptions intentionnelles documentées.

Pour chaque `lastmod`, `dateModified` ou date affichée : provenance, fuseau si connu,
modification significative et concordance avec le contenu. Un commit Git est une
preuve candidate : vérifier son diff et le chemin du contenu publié. La date d'un
build, d'un clone, d'une restauration ou du sitemap seul ne prouve pas une révision
éditoriale. Sans date fiable, omettre le champ optionnel et inscrire l'inconnue.
Conserver séparément publication, révision, vérification des sources et déploiement.

## Médias, données structurées et affiliation

Un `alt=""` peut être correct pour un fond, une image décorative ou un logo dont le
nom accessible est déjà fourni. Pour une image informative, vérifier son rôle,
le rendu et le nom accessible ; ne pas générer des alts depuis le seul nom de fichier.

Pour une vignette souhaitée dans les résultats : contrôler image représentative,
accès HTTP/crawl, dimensions et formats applicables, HTML/image principale et
données structurées pertinentes. OG relève aussi du partage social. Aucune balise
OG, image générée ou syntaxe JSON-LD ne garantit une vignette Google.
Lire [les règles images actuelles](https://developers.google.com/search/docs/appearance/google-images).

Le balisage reprend le contenu visible, les dates, la langue et la canonical.
Séparer JSON parseable, propriétés requises, warnings optionnels, éligibilité et
apparition réelle. L'absence de schema sur une route ne constitue pas à elle seule
un défaut de classement ni un prérequis IA.

Identifier la relation commerciale avant d'auditer les liens externes ; relever
URL source, destination, domaine/réseau, nature et `rel`. Un lien Direct Running
peut être affilié via Awin sans hôte Awin visible. Une citation documentaire simple
ne devient pas affiliée parce que le site utilise aussi des liens partenaires.
Vérifier règles actuelles et disclosure applicable au projet, sans inventer de contrat.

## Réception et impact

Un finding reçoit URL/section, version, observation datée, méthode, preuve, statut,
conséquence, correction bornée, priorité et recette. Relever pour les changements
`PROPOSE`, `LOCAL`, `PUSH_VERIFIE`, `PUBLIE_VERIFIE`, `MESURE` séparément.

Comparer collecte, dates de données et publication. Un ancien rapport GSC ou un
avertissement avant correction ne démontre pas un défaut actuel. Un live test,
une soumission reçue ou IndexNow accepté ne prouvent ni indexation ni résultat IA.
Un avant/après pauvre ou des fenêtres chevauchantes donnent `NON_CONCLUANT` pour
l'impact. Vérifier la méthode d'un champ IA fourni par un connecteur tiers.

La [capitalisation des quatre sites](../../ai-seo/references/four-sites-feedback.md)
fournit des exemples datés, sans audit live ni autorisation à reproduire leurs actions.
