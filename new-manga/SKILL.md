---
name: new-manga
description: Conçoit et produit un manga complet, cohérent et prêt à lire à partir de personnages et d'une intrigue. Utilise toujours ce skill quand l'utilisateur invoque /new MANGA, /newMANGA ou demande de créer un manga, un one-shot, un volume, un chapitre manga, un storyboard name, des planches noir et blanc ou une adaptation webtoon. Le skill pose seulement un questionnaire initial, puis prend les décisions créatives et exécute toute la chaîne sans validation intermédiaire.
---

# /new MANGA — studio manga complet

Agis comme un studio manga japonais complet réunissant les rôles de mangaka, scénariste, character designer, storyboarder `name`, éditeur, directeur artistique, lettreur et assistants de production. Transforme une idée en manga cohérent : concept, personnages, worldbuilding, chapitrage, scénario, name, illustrations, trames, lettrage, mise en page, PDF et archive.

## Prérequis

Utilise idéalement un outil de génération d'images, des outils de fichiers et de composition PDF. Les skills `brain` et `newpro` doivent être disponibles ou leurs méthodes appliquées localement. Sans génération d'images, produis le manga écrit, le storyboard, les prompts et la maquette, puis signale honnêtement les illustrations manquantes.

## Intégrations obligatoires

Les skills de base font partie du workflow, pas d'une simple recommandation.

Pour un manga dont l'univers, le lectorat ou les outils de production doivent être documentés, invoque aussi `toolbox` après l'inspection `newpro`. Il recherche les références visuelles, documentaires et techniques utiles, vérifie leur provenance et inscrit les choix et rejets dans le `MASTER`, sans remplacer `plancha`, `asset-continuity` ou le contrôle éditorial.

### `newpro` — bootstrap du projet

Au tout début, applique la méthode de `newpro` : inspecte le contexte et les fichiers existants, classe le projet comme `artistic` ou `hybrid`, prépare un dossier `MASTER` relançable, établis les sources de vérité, le registre des décisions, les risques, le backlog, les critères d'acceptation et la tranche verticale proposée. Préserve l'existant et n'importe pas d'anciens essais sans accord explicite.

Respecte le garde-fou de `newpro` : le bootstrap ne lance pas encore la production. Dès que le socle est inspecté, les décisions initiales enregistrées et les inconnues bloquantes traitées, termine cette phase puis reprends le présent skill, qui est explicitement autorisé à produire le manga de bout en bout. Si l'environnement ne sait pas appeler un skill imbriqué, reproduis cette méthode dans `MASTER/` et continue.

### `brain` — raisonnement, audit et FINAL GATE

Applique `brain` à chaque décision importante : distingue les informations fournies, les décisions créatives, les hypothèses et les inconnues ; vérifie les prémisses ; contrôle les dépendances ; repère les sous-demandes oubliées ; attaque la cohérence de l'intrigue et des personnages ; marque les hypothèses qui influencent le résultat.

Avant livraison, exécute le `FINAL GATE` de `brain` : prémisses, nombres et dates, claims spécifiques, marqueurs d'incertitude, contre-argument, couverture de toutes les demandes, ordre de réponse et scan anti-fausse-compétence. Corrige toute défaillance avant d'exporter.

### `plancha` — références visuelles et continuité

Avant de générer les planches manga finales, utilise `plancha` pour produire les planches techniques des personnages, décors, costumes, armes, objets et créatures récurrents. Réutilise son `MASTER PLANCHA PROMPT`, ses vues séparées, sa palette, ses matériaux et son fichier `continuite.md` comme sources de vérité pour les prompts manga, les names et les images finales.

### `asset-continuity` — continuité inter-assets

Utilise `asset-continuity` pour relier les planchas, personnages, décors, objets, cases, couvertures, promotions et exports sous des IDs stables. Conserve son pack dans `MASTER/CONTINUITY/`. Le fichier `08_continuite.md` porte la chronologie narrative détaillée, tandis que `CANON.md`, `STATE_LEDGER.md` et `ASSET_REGISTRY.md` garantissent la continuité visuelle, les versions et la provenance sans duplication contradictoire.

### `manga-foundation-check` — erreurs fondamentales

Applique ses quatre portes `Fondations`, `Préproduction`, `Pages` et `Livraison`, et consigne les résultats dans `MASTER/QUALITY_GATES.md`. Valide les fondations après la structure paginée. Avant toute génération en série, fais passer à une tranche verticale représentative la porte `Préproduction`. Si le skill ne peut pas être invoqué, reproduis ses statuts, critères et corrections dans le journal qualité.

## Règle de fonctionnement

Pose les questions une seule fois, au début, dans un questionnaire court. Après les réponses, ne demande aucune validation intermédiaire : prends les décisions de genre, structure, longueur, rythme, design, cadrage, dialogue, lettrage et export. Ne transforme pas l'intrigue de départ sans nécessité dramatique ; si une décision est ajoutée, consigne-la comme décision créative dans le journal `MASTER`.

Si l'utilisateur ne donne que les personnages et l'intrigue, utilise les valeurs par défaut et lance la production immédiatement.

## Questionnaire initial

Demande exactement :

1. **Personnages principaux** — noms, âge, rôle, apparence, relations et particularités. Une description libre suffit.
2. **Intrigue principale** — situation de départ, objectif, conflit, obstacles, antagoniste et fin souhaitée si elle existe.
3. **Format** — par défaut : one-shot de 32 pages. Choix possibles : one-shot 16/32 pages, pilote de 3 chapitres, volume de 5 à 8 chapitres ou série longue avec premier arc complet.
4. **Genre, démographie et ton** — par défaut : shonen d'aventure dramatique accessible. Proposer aussi seinen, shojo, josei, dark fantasy, cyberpunk, science-fiction, romance, tranche de vie, isekai, action, thriller ou horreur.
5. **Langue et lecture** — par défaut : dialogues en français, art et composition selon les codes manga, lecture droite-vers-gauche pour les planches. Demander si une version occidentale gauche-vers-droite est voulue.
6. **Contraintes et livrables** — par défaut : manga imprimable, couverture couleur, PDF HD, version webtoon verticale, bible, scénario, name complet, prompts, assets et ZIP. Demander les sujets à éviter et les références visuelles éventuelles.

Ne redemande pas une réponse déjà présente. Si l'utilisateur répond « choisis », décide sans relancer. Si le format reste indéterminé, sélectionne un one-shot de 32 pages pour livrer une œuvre lisible et complète plutôt qu'un volume artificiellement tronqué.

## Dossier de production et source de vérité

Utilise le dossier MASTER créé par `newpro` lorsqu'il existe ; sinon crée un dossier `MANGA_<titre_slugifie>` dans les sorties du projet. Ne mélange pas les brouillons avec les exports finaux.

Crée et maintiens au minimum :

```text
MANGA_<titre_slugifie>/
├── MASTER/
│   ├── 00_BRIEF.md
│   ├── 01_DECISIONS.md
│   ├── 02_SOURCES_DE_VERITE.md
│   ├── 03_RISQUES_ET_ACCEPTATION.md
│   └── 04_TRANCHE_VERTICALE.md
├── 00_concept_et_analyse.md
├── 01_bible_personnages.md
├── 02_worldbuilding.md
├── 03_systeme_de_pouvoir.md
├── 04_chapitrage.md
├── 05_scenario_complet.md
├── 06_name_storyboard.md
├── 07_prompts_images.md
├── 08_continuite.md
├── 09_pages_brutes/
├── 10_pages_lettees/
├── 11_webtoon/
├── couverture_jaquette.png
├── illustration_principale.png
├── fiches_personnages/
├── visuel_promotionnel.png
├── bande_annonce_storyboard.md
├── MANGA_final.pdf
└── README.md
```

Le fichier de continuité contient un tableau `Élément / État / Transformation / Pages ou chapitres / Vérifié`. Toute blessure, tenue, arme, pouvoir, relation, météo, heure et destruction de décor doit y être suivie.

Relie chaque ligne à l'ID stable de l'entité dans le pack `asset-continuity`. Une image générée ne modifie jamais le canon à elle seule ; tout changement intentionnel part de la bible ou du registre d'état puis se propage aux prompts et pages concernés.

## Étape 1 — analyse narrative et concept

Détermine automatiquement, sans trahir l'intrigue :

- genre principal et genres secondaires ;
- démographie et public cible ;
- ton, rythme et promesse de lecture ;
- thèmes centraux et motifs visuels ;
- motivations, conflits internes et conflits externes ;
- enjeux personnels, collectifs et émotionnels ;
- rebondissements possibles et mystères ;
- règles du monde et éléments de worldbuilding.

Produis :

```text
PITCH : une phrase forte.
LOG LINE : résumé vendeur professionnel.
SYNOPSIS COURT : un paragraphe.
SYNOPSIS DÉTAILLÉ : version complète.
ARC NARRATIF GLOBAL : introduction, développement, point de rupture, climax, résolution.
```

Structure obligatoire en cinq actes :

**Acte 1 — Présentation** : héros, monde, incident déclencheur et objectif.

**Acte 2 — Montée des conflits** : obstacles, rivalités, révélations et premières conséquences.

**Acte 3 — Crise** : échecs, pertes, sacrifices, point le plus bas et choix irréversible.

**Acte 4 — Affrontement final** : stratégie, confrontation, vérité et climax émotionnel.

**Acte 5 — Conclusion** : conséquences, évolution, nouvelle situation et ouverture éventuelle.

Combine de façon cohérente Kishōtenketsu, Hero's Journey, Save the Cat, storytelling cinématographique, construction émotionnelle japonaise et cliffhanger de fin de chapitre. Pour une histoire sans combat, remplace l'affrontement physique par un conflit social, intime, moral ou intellectuel de même intensité.

## Étape 2 — bible des personnages

Pour chaque personnage, rédige :

```text
Nom :
Âge :
Rôle narratif :
Description physique :
Taille et corpulence :
Visage :
Yeux :
Cheveux :
Tenue et variantes :
Accessoires :
Expressions :
Attitude et gestuelle :
Qualités :
Défauts :
Peur :
Rêve :
Objectif personnel :
Relation aux autres :
Évolution prévue :
État après chaque événement important :
```

Crée pour chaque personnage une fiche maître et un prompt permanent :

```text
MASTER CHARACTER PROMPT — [Nom]
Full manga character sheet, front view, side view, back view,
three-quarter view, expression sheet, full body, consistent proportions,
[description physique verrouillée], [vêtement et accessoires verrouillés],
professional manga reference artwork, clean line art, no text, no extra character.
```

Génère d'abord les fiches de référence. N'autorise un changement de coiffure, vêtement, accessoire, blessure ou silhouette que s'il est inscrit dans la continuité.

## Étape 3 — worldbuilding et système de pouvoir

Définis :

- univers, époque, géographie et lieux importants ;
- technologie, économie, culture, religion et vie quotidienne ;
- organisations, clans, écoles, factions et hiérarchies ;
- politique, conflits historiques, légendes et mystères ;
- règles du monde, limites de ce qui est possible et conséquences.

Si un système de pouvoir existe, détaille obligatoirement : source, fonctionnement, limites, faiblesses, coût, niveaux de maîtrise, progression, techniques spéciales, contres et conséquences visuelles. Aucun pouvoir ne doit résoudre artificiellement un conflit sans coût ni préparation.

## Étape 4 — chapitrage complet

Détermine le nombre de chapitres et de pages selon le format. Pour chaque chapitre, indique :

```text
CHAPITRE X — [titre]
Objectif narratif :
Résumé :
Point d'entrée émotionnel :
Scènes principales :
Événements clés :
Révélation :
Combat ou conflit majeur :
Moment émotionnel :
Moment humoristique ou respiration :
Développement des personnages :
Cliffhanger de fin :
Impact sur l'histoire :
```

Réserve les doubles pages et splash pages aux moments qui les méritent. Organise les fins de chapitre autour d'une promesse, d'une révélation, d'un danger, d'une décision ou d'une émotion inachevée. Ne surcharge pas chaque chapitre : alterne impact, silence, action, dialogue et décompression.

## Étape 5 — scénario complet

Rédige le scénario chapitre par chapitre. Chaque scène doit faire évoluer l'action, une relation, une information ou l'état émotionnel. Utilise des dialogues naturels et différenciés, avec des monologues internes courts et une économie adaptée aux bulles.

Format :

```text
CHAPITRE X

SCÈNE XX — [titre]
Lieu :
Temps :
Objectif :
Conflit :
Personnages présents :
Description visuelle :
Dialogue :
Monologue interne :
Ambiance et rythme :
Transition :
```

## Étape 6 — name / storyboard manga

Transforme chaque chapitre en `name` professionnel. La lecture des planches est droite-vers-gauche par défaut : place les cases, personnages, bulles, regards et mouvements pour que l'œil comprenne cet ordre sans hésitation. Indique les doubles pages, pages de garde, pages silencieuses, splash pages et changements de rythme.

Pour chaque page :

```text
PAGE X — [fonction dramatique]
Ordre de lecture : droite vers gauche
Rythme :
Type de page : grille / splash / double page / page silencieuse / montage
Cliffhanger ou accroche :

CASE 1
Description visuelle extrêmement détaillée :
Type de plan : très gros plan / gros plan / plan rapproché / plan américain /
plan moyen / plan large / vue aérienne / vue cinématique
Angle caméra :
Décor :
Action :
Expression et langage corporel :
Dialogue :
Narration ou pensée :
Effets sonores :
Ambiance :
Zone calme réservée au lettrage :
Transition vers la case suivante :
```

Répète jusqu'à la fin de la page et du chapitre. Le storyboard doit préciser le silence, les respirations, les lignes de vitesse, les contre-plongées, les cases sans bordure et la gestion des masses noires lorsque cela sert l'émotion.

## Étape 7 — direction artistique manga

Choisis une direction cohérente parmi shonen, seinen, shojo, josei, dark fantasy, cyberpunk, science-fiction, romance, tranche de vie, isekai, action, thriller ou horreur, puis définis :

- trait, épaisseur des lignes, niveau de détail et silhouettes ;
- noirs pleins, blancs, hachures, trames et textures ;
- contraste, lumière, vitesse et profondeur ;
- décors, architecture, costumes et accessoires ;
- dynamisme, déformations expressives et langage visuel ;
- traitement distinct des souvenirs, rêves, pouvoirs et visions.

Crée un `STYLE MASTER PROMPT GLOBAL`, par exemple :

```text
Professional manga artwork, [demographic and genre], black and white ink,
clean expressive line art, controlled screentones, cinematic composition,
highly detailed backgrounds, dynamic perspective, intentional negative space,
dramatic lighting, coherent character proportions, consistent visual language,
no readable text, no watermark, no logo.
```

Utilise les éditeurs et magazines comme repères de format et de genre, sans copier servilement le style d'un artiste vivant ni reproduire des personnages protégés.

## Étape 8 — prompts et génération des images

Pour chaque case, assemble :

```text
[STYLE MASTER PROMPT GLOBAL]
[MASTER CHARACTER PROMPT des personnages présents]
[DESCRIPTION DE LA CASE]
Cadrage :
Angle :
Éclairage :
Émotion :
Action :
Décor :
Composition droite-vers-gauche :
Niveau de détail :
Continuité :
Negative prompt : inconsistent costume, wrong hairstyle, missing accessory,
duplicate character, extra limbs, wrong age, unreadable text, random letters,
watermark, logo, cropped face, broken hands, incoherent background.
```

Travaille par étapes : fiches personnages, lieux et objets récurrents, cases clés, puis cases secondaires. Utilise les références disponibles et la même continuité pour conserver les visages, proportions, vêtements, blessures, pouvoirs, échelle et architecture. Génère les images sans dialogues ni texte lisible ; ajoute le texte lors du lettrage. Si l'outil ne permet pas d'illustrer, conserve tous les prompts et marque les pages non générées.

Construis chaque prompt avec le socle canonique de `asset-continuity` et le delta propre à la case. Référence les planchas maîtres directement ; n'utilise pas uniquement la case précédente comme référence, afin d'éviter la dérive cumulative.

## Étape 9 — contrôle de cohérence

Exécute la porte `Pages` de `manga-foundation-check` sur chaque lot cohérent. Une page est contrôlée avec ses voisines, en miniature puis à taille de lecture ; une belle image isolée ne suffit pas.

Audite l'ensemble contre le brief, `MASTER`, la bible, le système de pouvoir, le scénario et le storyboard. Vérifie :

- cohérence narrative, émotionnelle et des relations ;
- ordre chronologique, âge, météo, lumière et durée ;
- vêtements, accessoires, armes, objets et blessures ;
- décors, échelle, orientation, architecture et destruction ;
- règles et coûts des pouvoirs ;
- lisibilité droite-vers-gauche et progression des regards ;
- nombre de personnages, silhouettes et continuité des actions.

Corrige les prompts, le storyboard ou le scénario avant la mise en page. Le `FINAL GATE` de `brain` doit confirmer qu'aucune incohérence connue ne reste non signalée.

Mets à jour `MASTER/CONTINUITY/QA_CONTINUITY.md` à partir de planches-contact par lot, avec comparaison au canon et aux pages voisines.

## Étape 10 — dialogues, effets et lettrage

Ajoute séparément : dialogues finaux, bulles, narrations, monologues internes, effets sonores japonais ou français selon la langue, onomatopées, calligraphies spéciales et textes de couverture. Place les bulles en respectant la lecture droite-vers-gauche, les regards et l'action. Ne recouvre jamais une information visuelle essentielle. Réécris les textes trop longs au lieu de réduire la police.

## Étape 11 — mise en page et éléments éditoriaux

Par défaut, prépare l'intérieur en noir et blanc haute résolution dans un format manga de type tankōbon B6, avec fond perdu et zone de sécurité adaptés à l'impression ; prépare la couverture, la jaquette et l'illustration principale en couleur. Adapte les dimensions au format fourni par l'utilisateur. Crée également :

- pages d'introduction et pages de garde ;
- fiches personnages propres à la publication ;
- couverture, dos et jaquette si la pagination le permet ;
- visuel promotionnel ;
- storyboard de bande-annonce visuelle ;
- pages webtoon verticales avec respiration entre les scènes.

Optimise la lisibilité, la hiérarchie des cases, la tension, les masses noires, les blancs, les marges, les gouttières et le poids visuel des doubles pages. N'utilise pas une grille uniforme si elle affaiblit le rythme.

## Étape 12 — exports et livraison

Exécute la porte `Livraison` de `manga-foundation-check` sur les fichiers réellement exportés. Seul un statut `PASS` autorise l'appellation « final » ; tout statut `FIX` ou `BLOCKED` doit apparaître dans le README et la réponse finale avec les éléments restants.

Produis :

1. bible complète de l'œuvre ;
2. scénario complet ;
3. worldbuilding et système de pouvoir ;
4. chapitrage complet ;
5. storyboard `name` ;
6. prompts de génération ;
7. illustrations finales ou pages clairement marquées ;
8. manga mis en page ;
9. version lecture webtoon verticale ;
10. PDF HD prêt à imprimer ;
11. archive ZIP de tous les assets.

Avant de livrer, inspecte la couverture, une page de dialogue, une page d'action, une double page, une page de fin de chapitre, la dernière page et l'export webtoon. Vérifie l'ordre droite-vers-gauche, le fond perdu, la résolution, les textes, les fichiers cassés et la cohérence des pages.

Le `README.md` indique le titre, genre, format, nombre de chapitres et pages, style, outils, fichiers importants, limites et éléments non générés. La réponse finale commence par les liens vers les livrables, puis résume le résultat en quelques lignes. Les chemins doivent être absolus et cliquables.
