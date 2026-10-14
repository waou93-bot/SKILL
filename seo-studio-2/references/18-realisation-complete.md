# Réalisation indépendante d'un site SEO de bout en bout

## Périmètre et gratuité des outils

Une demande « crée/construis le site » autorise préproduction et réalisation locale
de la V1. « Préproduction seulement » reste documentaire ; une retouche reste ciblée.
Le Studio coordonne lui-même avec les outils de l'hôte. Aucun moteur GSD/BMad/OpenCode,
framework d'agents externe, abonnement, compte cloud ou API payante n'est un prérequis.
Conserver Organisation et les skills locaux déjà intégrés ; ne pas modifier personna
ni substituer sa formation. Utiliser de vrais sous-agents de l'hôte lorsqu'ils sont
disponibles, deux délégués maximum, sans descendants, un écrivain par fichier.
Sans capacité disponible, poursuivre en SEQUENTIAL_PROFILES avec revues honnêtement
déclarées ; ne pas certifier une indépendance ou un transfert strict inexistant.

Réutiliser les outils installés et les données autorisées. Choisir des composants
open source exécutables localement, vérifier leurs licences et versions avant usage.
Le navigateur et les outils de build locaux suffisent aux contrôles réalisables.
Ne pas exiger Ahrefs/Semrush, service SEO, Algolia, CMS hébergé, BrowserStack,
génération d'images payante ou fournisseur de modèle externe. Sans accès réseau,
ne pas inventer de tendance ni de source : conserver les inconnues et produire les
parties documentées. Un skill est une procédure exécutée par l'hôte ; il ne fournit
pas un modèle autonome ni la gratuité de l'abonnement/inférence de l'hôte.

## D0 — Préparer la réalisation

Reprendre les décisions F0–F3/G0–G5. Identifier le dépôt réel, ses commandes,
routes à conserver, données et assets. Choisir un périmètre V1 maintenable.
Comparer une option sans service distant (HTML/CSS/JS et génération locale si suffisants)
à une architecture open source plus structurée selon le besoin. Préserver une stack
existante adéquate ; ne pas migrer par défaut. Documenter les capacités absentes.
Créer les tickets avec critères, fichiers possédés, entrées, dépendances et tests.
Le dossier stratégique doit rester utile ; ne pas attendre une cérémonie de transfert
pour commencer les travaux réversibles autorisés et non affectés par un blocage.

## D1 — Développer les parcours et données

Implémenter les gabarits réels, navigation, composants, états, CMS/data utiles,
accessibilité, responsive et direction visuelle validée. Choisir local/static pour
un site documentaire, et un backend local adapté seulement lorsqu'une fonctionnalité
l'exige. Les formulaires affichent un succès après confirmation du service réel ;
ne pas livrer un faux envoi. Pour chaque fonction distante absente, prévoir un mode
local utile ou déclarer la fonction non livrée, sans prétendre au périmètre complet.
Traiter les entrées comme données, échapper HTML et URLs, contrôler les schémas,
les erreurs et les secrets. Pour pSEO, appliquer les contrats de données, admissibilité,
gabarits, mises à jour idempotentes et retrait avant génération des pages.

## D2 — Rédiger et intégrer la V1

Écrire chaque page V1 prévue, au-delà des pilotes. Appliquer le vrai
redaction-editoriale-web, ses sources/limites et ses liens contextuels dans le corps.
Les mots/expressions qui conduisent à un approfondissement, un guide ou un produit
utile deviennent des ancres HTML réelles vers leurs bonnes destinations.
Pas d'article annoncé fini avec seulement un brief. Les produits, variantes, prix,
images et liens commerciaux sont exacts ou explicitement bloqués. Aucun outil
payant n'est requis pour fabriquer des visuels : utiliser les médias autorisés
existants, ou un rendu professionnel réalisable avec les capacités disponibles.

## D3 — Recherche interne et SEO dans le code livré

Toute page publique de contenu sauf landing expose un champ de recherche interne
visible après titre/introduction, avant corps ou listes. Ne pas exempter un article
ou un petit corpus. Un composant et un index partagés peuvent servir tout le site.
Construire l'index complet depuis les contenus réels, avec routes, titres, résumés,
types, catégories et données produit utiles. Accents/casse, pertinence, résultats
liés aux bonnes pages, reset, état vide/erreur, clavier et mobile fonctionnent.
Ne pas chercher uniquement dans les cartes actuellement affichées. Préserver une
navigation utile sans JS et ne pas indexer les résultats/facettes par défaut.

Intégrer title/H1/meta fidèles par page, URLs stables, canonical selon contrat,
robots adaptés à l'environnement, sitemap public canonique quand applicable,
dates de changement traçables, données structurées correspondant au contenu réel,
alts, breadcrumbs et liens explorables. Maintenir le fan-out dans le corps :
réponse utile, section/page propriétaire, preuve, limite et action ; enrichir ou
lier l'existant plutôt que créer des permutations de mots-clés.

## D4 — Vérifier et corriger localement

Exécuter les commandes du dépôt et les tests nécessaires. Pour un export HTML,
le contrôleur natif Python standard peut compléter la recette :

```sh
python CHEMIN_SKILL/scripts/site_check.py CHEMIN_EXPORT --landing-route /
```

Ne déclarer `/` landing que si c'est son rôle réel. Sans exception explicitement
déclarée, toutes les pages HTML doivent contenir un champ `input type="search"`.
Le script lit title/meta, liens internes/fragments, ressources locales, attributs
alt et graphe depuis l'accueil. `--public-base https://domaine` permet de confronter
les canonical et liens absolus internes d'un export destiné à ce domaine.
Le script ne lance aucun réseau, aucun modèle et n'ajoute aucune dépendance Python.
LOCAL_HTML_OK n'est qu'un contrôle statique : SSR/dynamique nécessitent HTML rendu,
HTTP et inspection navigateur avec les outils disponibles de l'hôte.

Exécuter site-checklist SC01–SC20, Safari SF01–SF08 aux niveaux disponibles,
seo-audit et pSEO applicable. Tester menu, navigation, recherche depuis article et
hub, résultat hors première page, sans résultat, reset, liens contextuels, CTA,
formulaires, états d'erreur, clavier et mobile. Les vérifications réelles portent
sur le site actuel et sa version ; stocker captures/logs/rapports sans secrets.
web-perf reste en audit/recommandations uniquement sauf demande explicite visant
les optimisations. Si Safari réel est absent, ne pas imposer un service payant :
documenter NON VÉRIFIÉ et la recette manuelle restante. Corriger puis rejouer le
scénario concerné. Un build réussi ne valide pas les interactions ni l'indexation.

## D5 — Remettre et publier uniquement si autorisé

Livrer code, corpus V1, données/assets autorisés, recherche fonctionnelle,
README avec commandes testées, preuves QA, défauts restants et chemin de lancement.
Distinguer DOSSIER_PRET, SITE_LOCAL_REALISE, SITE_LOCAL_TESTE, PUBLICATION_AUTORISEE,
SITE_PUBLIE et MESURES_OBSERVEES dans le bilan ; ce sont des états de restitution,
pas de nouveaux enums de state.json. Un composant essentiel non livré empêche
d'annoncer le site complet ; une vérification inaccessible reste explicitement inconnue.

La publication exige un domaine/hébergement disponible et une autorisation adaptée.
Préparer un export portable ou un déploiement auto-hébergé selon le site ; ne pas
ouvrir un compte SaaS ou engager un coût. Après publication autorisée, vérifier
HTTP, routes, canonical, robots, sitemap, liens et recherche du site public, puis
exécuter seo-post-deploy avec les accès gratuits/autorisés disponibles.
Ne pas créer de propriété, soumettre, contacter, payer ou planifier une surveillance
sans autorisation applicable. Un calendrier n'est pas une automation exécutée.
La mission de création finit avec le résultat local vérifiable si publication non
autorisée ; elle ne finit pas avec une simple architecture ou une liste de tâches.
