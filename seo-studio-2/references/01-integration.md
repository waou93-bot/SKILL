# Contrat d'intégration et ordre d'autorité

## Inventaire réel

Le socle consulté se trouve dans `research/dependencies.json`. Ce relevé daté n'est
pas une liste d'installations locales. À chaque invocation, consulter le catalogue
réel et les emplacements autorisés. `scripts/studio.py inventory` est une aide de
lecture locale, pas un installateur et pas une preuve que l'hôte charge le fichier.

Rechercher `SKILL.md` sans ignorer la casse, lire le frontmatter, et relever nom,
chemin, version, empreinte SHA-256, champ description et références nécessaires.
Tout nom/chemin de skill contenant `seo` est retenu. Les descriptions contenant SEO
sont des candidats supplémentaires à qualifier. Le script exclut `seo-studio-2`.
Un alias `persona` reste un candidat pour `/personna`, pas un équivalent établi.

Lire tous les SKILL.md retenus, puis leurs références pertinentes à chaque phase.
Deux copies de même nom ne fusionnent pas : comparer leurs empreintes et décider
quelle installation est réellement utilisée. Ne supprimer aucune copie sans droit.
Le registre de projet distingue `LU`, `INTROUVABLE`, `A_LIRE`, `NON_APPLICABLE` et
`PREPARE_PHASE_ULTERIEURE`. Une exclusion donne un motif spécifique au site.

## Répartition sans concurrence de routeurs

| Dépendance | Responsabilité réservée | Usage par SEO STUDIO 2 |
|---|---|---|
| brain | preuves, incertitudes, contre-argument, complétude | toutes les décisions et revue finale |
| organisation | coordination, capacités, modèles, permissions | point d'entrée unique ; même run_id |
| design-dna | préférences, identité, skin, qualité visuelle | avant toute direction artistique |
| no-slop | précision des textes, patterns UI non motivés | avant gel éditorial et visuel |
| seo | décision de canal, intentions, stratégie, mesure | G1/G2/G4 ; socle organique |
| seo-audit | diagnostic technique et on-page | spécifications en préprod ; tests après réalisation |
| ai-seo | accès recherche IA, citations, recommandations, mesure | pilote IA conditionnel ; politique des bots préservée |
| seo-content-engine | briefs, lots, validation et capacité éditoriale | production V1 et maintenance, brouillon par défaut |
| seo-post-deploy | production, propriétés, sitemaps et mesures réelles | préparer le transfert ; exécuter seulement après autorisation |
| /personna | formation/configuration des agents | préalable obligatoire à chaque mandat métier |

Ne pas appeler Organisation à nouveau depuis chaque spécialiste. Conserver le
`run_id`, l'`entrypoint`, la version du brief et la propriété des fichiers.
D'autres skills SEO découverts rejoignent le registre sans dupliquer un périmètre.
Les coordinateurs concurrents (par exemple seo-site-studio ou newsit-seo si découverts)
sont lus et classés NON_APPLICABLE à l'appel, avec motif « coordinateur concurrent ».
Ne pas les rappeler, former une seconde équipe ou créer un autre registre. Leurs
copies de modules sont comparées par empreinte avant de choisir la source effective.
Business Checklist est pertinent pour la viabilité d'un nouveau site monétisé ;
New Site/New Pro pour le transfert, Analytics pour la mesure, Human pour les assets.
Les lire s'ils sont présents et requis, sinon consigner la limite ; ne pas les inventer.

## Contradictions

Instructions supérieures et permissions priment. Pour les choix produit et design,
la dernière décision utilisateur applicable prime sur les anciennes références.
Pour une affirmation fournisseur, consulter la documentation primaire actuelle.
Un seuil interne plus exigeant reste possible, mais doit être nommé « convention
projet » et non « obligation Google ». Les autres conflits remontent à Astra.

Astra ne peut pas déclarer une source observée lorsqu'elle manque, déroger à la
confidentialité, autoriser un achat à la place de l'utilisateur, ou remplacer une
validation qualifiée. Voir `research/conflicts.md` pour les arbitrages de conception
proposés à partir des contradictions rencontrées pendant la création du package.

## Sans dépendance ou outil

Le travail indépendant continue en `PROVISOIRE`. La dépendance concernée reste
`INTROUVABLE` et son gate reste bloqué. Aucune mention « exécuté » parce qu'un fichier
est cité. La préparation peut être utile sans être strictement complète ; le bilan
doit le dire. Les modules post-déploiement, non applicables au stade préproduction,
sont préparés et non artificiellement marqués réussis.

## Contrôles de fin de préproduction et réalisation

| Dépendance | Responsabilité | Passage Studio |
|---|---|---|
| site-checklist | SC01–SC20, Safari SF01–SF08 et web-perf en audit uniquement | couverture documentaire G5 ; recette réelle G6 |
| seo-audit | exploration/indexation, technique, on-page, contenu et liens | revue G5 obligatoire ; contrôles réels G6 |
| pSEO | familles de pages issues de données, utilité et indexabilité | applicabilité G1 ; conception G2–G4 si pertinente ; revue G5/G6 |

Lire [le contrat de contrôle final](17-controle-final.md). Charger les trois skills
réels ; justifier l'absence de système pSEO plutôt que le créer artificiellement.
L'intégration de seo-audit déjà existante devient un passage explicite à G5.

## Indépendance de la réalisation — version 3

Le Studio possède son parcours de développement et de recette dans
[18-realisation-complete.md](18-realisation-complete.md). Ne pas exiger GSD,
BMad, OpenCode, CrewAI, OpenHands, LangGraph, un cloud ou un service payant.
Les skills locaux sont des instructions ; ils ne constituent pas une autorisation
d'installer leurs outils ni de payer leurs services. Conserver le vrai /personna,
ses entrées, sa calibration et les preuves de chargement des agents.
La recherche utilise les accès publics ou les données autorisées disponibles ;
aucun compte LinkedIn, Reddit, outil de mots-clés ou abonnement ne doit être créé.
L'absence d'accès conserve les limites déjà prévues, sans arrêter les réalisations
locales indépendantes ni inventer les preuves. Ne pas annoncer un transfert strict
si un prérequis réel manque. Les dépendances du runtime Codex sont explicites :
un skill ne fournit ni son propre modèle ni une inférence gratuite hors de l'hôte.

## QA, sécurité et performance — contrat 3.1

Appliquer [le contrat commun](19-qa-security-performance.md) : webapp-testing pour
les interactions, cross-platform-qa pour la couverture et la méthode,
security-best-practices pour le code sécurisé et la revue applicable, web-perf pour
les mesures et recommandations. Conserver un seul registre de preuves dans 11_QA.md.
Aucun service payant requis ; lectures, tests locaux, émulation et appareils réels
restent des preuves distinctes. Les corrections respectent le mandat existant.
