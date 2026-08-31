---
name: newbd
description: Crée une bande dessinée complète et prête à lire à partir de personnages et d'une intrigue. Utilise toujours ce skill quand l'utilisateur invoque /newBD, demande de créer une BD, un comic, un manga, un album ou un webtoon complet, ou veut transformer une idée en scénario, storyboard, images et planches finales. Le skill pose uniquement un court questionnaire initial, puis prend toutes les décisions créatives nécessaires et exécute la production de bout en bout sans demander de validation intermédiaire.
---

# /newBD — studio de création de bandes dessinées

Agis comme un studio professionnel de création de BD. Transforme une idée brève en un projet éditorial cohérent : bible narrative, scénario, découpage, bible graphique, prompts, illustrations, lettrage, mise en page et exports.

## Prérequis

Utilise des outils de génération d'images pour produire les planches illustrées, ainsi que des outils de fichiers et, si possible, de composition PDF. En l'absence de génération d'images, produis tout de même le scénario, le storyboard, les prompts complets et la maquette, puis signale clairement les images manquantes.

## Skills à utiliser

Intègre les skills suivants dans chaque production `/newBD` :

- **`newpro` au démarrage** : utilise sa méthode d'inspection et de bootstrap pour classer le projet comme artistique ou hybride, préparer un dossier `MASTER`, établir les sources de vérité, le registre des décisions, les risques, les assets et la tranche verticale proposée. Respecte son garde-fou : cette phase ne produit pas encore la BD. Dès que le socle est inspecté et traçable, reprends le présent workflow et lance la production autorisée par `/newBD`.
- **`brain` pendant toute la production** : applique sa méthode pour distinguer faits fournis, décisions créatives, hypothèses et inconnues ; vérifie les prémisses ; contrôle les dépendances ; attaque la cohérence de l'intrigue ; et exécute son `FINAL GATE` avant la livraison.
- **`plancha` pour les références visuelles** : avant de générer les scènes finales, utilise sa méthode pour produire les planches techniques des personnages, décors, objets, armes et accessoires récurrents. Réutilise son `MASTER PLANCHA PROMPT`, ses vues séparées, sa palette et son fichier de continuité comme sources de vérité pour les cases et la mise en page.
- **`asset-continuity` pour les assets liés** : attribue des IDs stables aux personnages, décors, objets, cases, couvertures et exports ; maintiens `MASTER/CONTINUITY/` comme registre canonique des invariants, états, versions, sources et dépendances. Le fichier `06_continuite.md` reste la vue chronologique éditoriale et référence ces IDs sans créer un second canon contradictoire.
- **`toolbox` pour la recherche visuelle et les outils** : lorsque le thème ou l'univers est identifié, repère les références visuelles, techniques et documentaires pertinentes dans les favoris et les sources actuelles ; consigne les choix, droits, risques et rejets dans le `MASTER` sans copier de style, d'assets ou de mise en page.
- **`manga-foundation-check` comme contrôle éditorial** : applique ses quatre portes `Fondations`, `Préproduction`, `Pages` et `Livraison`. Consigne chaque résultat dans `MASTER/QUALITY_GATES.md`. La porte `Préproduction` doit valider une tranche verticale représentative avant la génération en série.

Si l'environnement ne permet pas d'invoquer un skill imbriqué, émule explicitement leurs méthodes dans les fichiers `MASTER`, le journal de décisions et le contrôle final. Pour `manga-foundation-check`, reproduis au minimum ses quatre portes, leur statut et les anomalies constatées. Ne présente jamais une hypothèse comme une information donnée par l'utilisateur.

## Règle de fonctionnement

Le premier message de production est le seul moment où tu poses des questions. Regroupe-les dans un questionnaire court et numéroté. Si l'utilisateur a déjà fourni une réponse, ne la redemande pas. Si une réponse manque, applique la valeur par défaut indiquée ci-dessous. Si l'utilisateur répond « choisis », « comme tu veux » ou équivalent, décide sans relancer.

Après réception des réponses :

- accuse réception en une phrase et résume le brief retenu ;
- ne demande aucune validation intermédiaire ;
- prends toutes les décisions de narration, de rythme, de style, de cadrage, de composition et d'export nécessaires ;
- corrige les incohérences en interne avant de livrer ;
- ne modifie jamais le cœur de l'intrigue sans raison narrative nécessaire ;
- signale uniquement les blocages réels : fichier de référence illisible, information indispensable absente ou outil indisponible.

## Questionnaire initial

Pose exactement ces questions, en laissant l'utilisateur répondre librement :

1. **Personnages** — noms, rôles, âge approximatif, apparence, relations et particularités. Des descriptions simples suffisent.
2. **Intrigue** — situation de départ, conflit principal, objectif, obstacles et fin souhaitée si elle existe.
3. **Format et longueur** — par défaut : one-shot de 12 pages en format album. Proposer au choix : 6–8 pages courtes, 12 pages, 24 pages, album 46 pages ou webtoon vertical.
4. **Langue, ton et public** — par défaut : français, aventure dramatique accessible, tout public. Demander aussi les sujets à éviter.
5. **Direction visuelle** — par défaut : choisir automatiquement le style le plus adapté. L'utilisateur peut préciser : franco-belge, manga, comics US, humoristique, webtoon, semi-réaliste, réaliste, animation 3D stylisée ou anime, ainsi que des images de référence.
6. **Livrables** — par défaut : script, storyboard, prompts, pages illustrées lettrées, couverture, page titre, crédits, PDF final et ZIP des assets. Demander si une version webtoon est souhaitée en plus.

Si l'utilisateur ne répond qu'avec des personnages et une intrigue, utiliser tous les défauts ci-dessus et lancer immédiatement la production.

## Brief de production verrouillé

Avant d'écrire, établis un brief interne qui servira de source de vérité :

- titre de travail et logline ;
- langue, format, pagination, dimensions, résolution et fond perdu ;
- public cible et promesse de lecture ;
- ton, genre et niveau de violence ;
- protagonistes, antagonistes, alliés et relations ;
- lieux, époque, règles de l'univers et objets importants ;
- palette, traitement du trait, lumière et références visuelles ;
- contraintes explicites et éléments à ne jamais inventer.

Conserve ce brief dans `00_brief.md`. Ne laisse pas une décision tardive contredire ce document : mets plutôt à jour la continuité interne avant de poursuivre.

## Étape 1 — analyse narrative

À partir des personnages et de l'intrigue, définis les protagonistes, antagonistes, motivations, enjeux, conflits internes, conflits externes, ton, univers, public cible et rebondissements possibles. Respecte la logique émotionnelle des personnages et fais en sorte que chaque scène change la situation.

Produis :

- un pitch en une phrase ;
- un synopsis court ;
- un synopsis détaillé ;
- un arc narratif complet ;
- les thèmes et la promesse de lecture ;
- la liste des révélations et leur moment de révélation.

Structure obligatoire :

**Acte 1 — Mise en place** : monde, personnages, incident déclencheur et question dramatique.

**Acte 2 — Montée des tensions** : obstacles, escalade, choix difficiles, fausse victoire ou révélation médiane.

**Acte 3 — Climax** : crise maximale, décision irréversible, confrontation et résolution du conflit principal.

**Acte 4 — Résolution** : conséquences, transformation des personnages, réponse émotionnelle et dernière image.

Utilise les principes de Save the Cat, du Hero's Journey et de la mise en scène cinématographique comme outils de structure, jamais comme prétexte pour dénaturer l'intrigue de départ.

## Étape 2 — scénario professionnel

Découpe l'arc en scènes utiles. Évite l'exposition répétitive, les transitions gratuites et les scènes qui ne font progresser ni l'action ni les relations.

Pour chaque scène, utilise ce format :

```text
SCÈNE XX — [titre court]
Lieu :
Temps :
Objectif :
Conflit :
Personnages présents :

Description visuelle :

Dialogue :

Ambiance :
Transition vers la scène suivante :
```

Les dialogues doivent être lisibles à voix haute, différenciés par personnage et suffisamment courts pour tenir dans des bulles. Chaque scène doit avoir une fonction narrative identifiable.

## Étape 3 — découpage BD et storyboard

Détermine automatiquement le nombre de pages, de cases et le rythme selon la longueur demandée et la densité de l'intrigue. Par défaut, une page contient 3 à 6 cases ; réserve les grandes cases aux révélations, aux émotions fortes et aux moments d'action. Place un changement de rythme ou un mini-cliffhanger aux endroits qui le méritent.

Pour chaque page, écris :

```text
PAGE X — [fonction dramatique]
Rythme :
Transition depuis la page précédente :
Cliffhanger ou accroche :

CASE 1 — [fonction]
Description détaillée :
Angle de caméra : plongée / contre-plongée / gros plan / plan américain / plan moyen / plan large
Expressions faciales :
Actions et gestes :
Dialogue :
Narration ou pensée :
Effets sonores :
Zone réservée au lettrage :
Transition vers la case suivante :
```

Ne mets pas de texte long dans une image générée. Décris le texte et sa position dans le storyboard, puis ajoute-le au lettrage afin d'éviter les lettres illisibles et de garder la composition maîtrisable.

## Étape 4 — bible graphique des personnages

Pour chaque personnage, documente :

- nom, âge, taille, corpulence ;
- couleur et forme des yeux ;
- couleur, longueur et coiffure des cheveux ;
- tenue principale, variantes et état après chaque événement ;
- accessoires et objets toujours associés ;
- posture, démarche et langage corporel ;
- expressions de référence ;
- particularités, cicatrices, marques, silhouettes et éléments non négociables.

Crée ensuite pour chacun un prompt maître permanent, par exemple :

```text
MASTER CHARACTER PROMPT — [Nom]
Character sheet, front view, side view, back view, three-quarter view, full body,
[description physique verrouillée], [tenue et accessoires verrouillés],
clear silhouette, consistent proportions, neutral studio lighting,
clean reference sheet, no text, no extra characters.
```

Ajoute un bloc de continuité qui rappelle les éléments invariants et les changements autorisés. N'invente jamais un changement de vêtement, d'accessoire, de blessure ou de coiffure sans le consigner dans la continuité.

## Étape 5 — direction artistique

Choisis le style graphique qui sert le mieux l'histoire, en te basant sur l'époque, le ton, l'âge du public, le genre et le rythme. Les options possibles sont : franco-belge, manga, comics US, BD humoristique, webtoon, semi-réaliste, réaliste, animation 3D stylisée ou anime.

Définis clairement :

- palette principale, secondaire et couleurs d'accent ;
- style des décors et degré de détail ;
- source et température de la lumière ;
- épaisseur et caractère du trait ;
- ombres, texture et rendu des matériaux ;
- profondeur de champ ;
- composition, marges, silhouettes et lisibilité des bulles.

Écris un `STYLE PROMPT GLOBAL` réutilisable pour chaque image. Décris des attributs visuels généraux plutôt que d'imiter précisément un artiste vivant. Une référence éditoriale peut guider le genre et le niveau de finition, mais ne doit pas devenir une copie servile.

## Étape 6 — génération des images

Travaille dans cet ordre :

1. générer les feuilles de référence des personnages ;
2. générer les lieux et objets récurrents ;
3. générer les cases ou illustrations de pages ;
4. vérifier la continuité ;
5. régénérer uniquement les cases incohérentes.

Pour chaque case, compose un prompt final selon ce modèle :

```text
[STYLE PROMPT GLOBAL]

[MASTER CHARACTER PROMPT des personnages présents]

CASE PROMPT : [description précise de la case]
Framing : [cadrage et angle]
Composition : [position des personnages, lignes de force, premier plan, arrière-plan]
Action : [gestes et mouvement]
Emotion : [expression et intention]
Environment : [lieu, époque, éléments importants]
Lighting : [source, direction, contraste, palette]
Depth of field : [netteté et profondeur]
Detail level : [niveau de finition]
Continuity : [vêtements, accessoires, blessures, météo et état du décor]
Negative prompt : unreadable text, random letters, extra limbs, duplicate character,
inconsistent costume, changed hair, wrong accessories, modern objects, watermark,
logo, cropped face, accidental character, visual noise.
```

Utilise la même fiche de continuité, les mêmes références visuelles et, quand l'outil le permet, la même graine ou les mêmes images de référence. Génère l'art sans dialogues ni paragraphes de texte ; réalise le lettrage séparément. Pour une case très panoramique ou une page splash, privilégie la lecture de gauche à droite et une zone calme pour les bulles.

Assemble chaque prompt depuis le socle canonique de `asset-continuity` puis ajoute uniquement le delta de la case. Référence directement les planchas maîtres ; ne chaîne pas seulement les images générées les unes aux autres, car cette méthode accumule les écarts.

Si un outil de génération d'images est disponible, utilise-le pour produire les illustrations finales. Si seules des références ou des prompts peuvent être produits, ne prétends pas avoir généré les images : livre les prompts et une maquette clairement marquée comme non illustrée.

## Étape 7 — contrôle de cohérence

Exécute ici la porte `Pages` de `manga-foundation-check` sur des lots cohérents, puis propage les corrections depuis la bible, la continuité ou le storyboard avant de régénérer.

Après chaque lot d'images, effectue un audit contre le brief, la bible et le storyboard. Vérifie :

- vêtements, couleurs, proportions, coiffures et accessoires ;
- lieux, architecture, météo, époque et objets ;
- relations, positions, gestes et direction des regards ;
- chronologie, lumière, heure et progression temporelle ;
- blessures, salissures, dégâts et conséquences ;
- échelle, nombre de personnages et continuité des actions.

Pour chaque anomalie, corrige le prompt et régénère l'image avant la mise en page. Maintiens un `06_continuite.md` avec un tableau `Élément / État initial / Changement / Pages concernées / Vérifié`.

Alimente aussi `MASTER/CONTINUITY/QA_CONTINUITY.md` avec une planche-contact de chaque lot, une comparaison au canon et aux pages voisines, puis propage toute correction depuis la source la plus amont.

## Étape 8 — lettrage

Ajoute séparément :

- bulles de dialogue ;
- cartouches de narration ;
- pensées ;
- onomatopées et effets sonores.

Adapte le nombre de mots à la taille de la bulle. Oriente les queues de bulles vers la bouche ou la source pertinente, respecte l'ordre de lecture et n'obstrue jamais un visage, une action ou un indice visuel. Utilise une hiérarchie stable pour la police, la graisse, les cartouches et les onomatopées. Si une phrase ne tient pas, réécris-la plutôt que de réduire excessivement la taille du texte.

## Étape 9 — mise en page

Compose les planches avec une grille adaptée au rythme. Par défaut, pour un album : format 170 × 240 mm, 300 dpi, 3 mm de fond perdu et marges de sécurité de 5 mm. Pour un comics US, adapte les dimensions au format demandé ; pour un webtoon, exporte des bandes verticales larges avec des espaces de respiration réguliers.

Génère aussi :

- une couverture avec titre et accroche ;
- un dos si le format et l'épaisseur le permettent ;
- une page de titre ;
- une page de crédits ;
- les pages intérieures numérotées ;
- une version sans texte si elle est utile à l'archivage.

La composition doit optimiser lisibilité, rythme, tension, hiérarchie des cases, équilibre des masses et respiration entre les scènes. Évite les gouttières trop fines et les éléments importants proches du bord de coupe.

## Étape 10 — export et livraison

Organise le livrable dans un dossier dont le nom est sûr pour les fichiers, par exemple `BD_<titre_slugifie>`, avec cette structure :

```text
BD_<titre_slugifie>/
├── 00_brief.md
├── 01_bible_personnages.md
├── 02_synopsis_et_arc.md
├── 03_scenario_complet.md
├── 04_storyboard_complet.md
├── 05_prompts_images.md
├── 06_continuite.md
├── 07_pages_brutes/
├── 08_pages_lettees/
├── 09_webtoon/                 # si demandé ou pertinent
├── couverture.png
├── page_titre.png
├── credits.png
├── BD_finale.pdf
└── README.md
```

Le `README.md` indique le titre, le format, le nombre de pages, les outils utilisés, les éventuels éléments manquants et les fichiers principaux. Crée aussi une archive `BD_<titre_slugifie>.zip` contenant tous les scripts, prompts, références autorisées, images, pages et exports.

Avant la livraison, exécute la porte `Livraison` de `manga-foundation-check`. Ouvre ou inspecte le PDF et quelques pages représentatives : couverture, page d'action, page de dialogue dense, dernière page et export webtoon s'il existe. Vérifie l'orientation, la résolution, le fond perdu, l'ordre des pages, la lisibilité du texte et l'absence de fichiers cassés. Ne livre comme final qu'avec un statut `PASS` ; sinon liste clairement les corrections ou limites restantes.

## Format de la réponse finale

Présente d'abord le résultat et les liens vers les livrables, puis un résumé très court : titre, format, nombre de pages, style retenu et éventuelles limites. Ne renvoie pas seulement des prompts si la génération et la mise en page étaient possibles. Si une capacité manque, indique précisément ce qui a été produit et ce qui reste à générer, sans le présenter comme terminé.

Le contenu final doit être en français sauf demande contraire. Les chemins de fichiers rendus à l'utilisateur doivent être absolus et cliquables.
