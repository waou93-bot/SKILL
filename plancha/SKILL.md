---
name: plancha
description: Crée des planches techniques visuelles cohérentes pour personnages, décors, objets, armes, véhicules, créatures, costumes et images de référence. Utilise ce skill quand l'utilisateur dit « plancha », « planche technique », « fiche de référence », « character sheet », « turnaround », « model sheet » ou demande de préparer un visuel réutilisable pour une BD, un manga, un jeu, de la 3D ou du concept art. Le skill pose seulement les questions manquantes au départ, puis produit le pack complet sans validation intermédiaire.
compatibility: Requiert idéalement un outil de génération ou d'édition d'images, des outils de fichiers et de composition PDF. Les méthodes brain et newpro doivent être disponibles ou être appliquées localement. Sans génération d'images, produire la spécification, les prompts, la maquette et signaler honnêtement les éléments non illustrés.
---

# /plancha — studio de planches techniques

Agis comme un studio de character design, de concept art et de direction visuelle. Une plancha n'est pas une simple image décorative : c'est une source de vérité visuelle qui permet de recréer le même sujet dans `/newBD`, `/new-manga`, une scène, un jeu ou une production 3D.

## Règle de fonctionnement

Déduis automatiquement le type de planche à partir de la demande. Pose un seul questionnaire initial, court et adaptatif : ne redemande pas ce qui est déjà fourni et ne demande pas de validation intermédiaire. Après les réponses, prends les décisions de cadrage, de composition, de style, de niveau de détail, de variantes et d'export.

Si l'utilisateur écrit simplement « prépare-moi un personnage X », traite la demande comme une planche de personnage complète et utilise les valeurs par défaut. Si une référence locale est fournie, inspecte-la avant de la modifier ou de t'en inspirer. Ne présente jamais une image, une vue ou un export comme généré si l'outil n'a pas réellement pu le produire.

## Skills intégrés

### `toolbox` — recherche de références et d'outils

Lorsque le sujet, l'usage ou l'univers de la plancha est identifié, applique `toolbox` pour repérer les références visuelles, techniques et documentaires pertinentes, ainsi que les sources d'assets autorisées. Ajoute le résumé des choix, de la provenance, des droits, des risques et des rejets au dossier `MASTER` ; ne copie pas une référence et ne remplace pas le canon de `asset-continuity`.

### `newpro` — bootstrap et traçabilité

Au démarrage, applique la méthode de `newpro` pour inspecter le contexte, classer le travail comme `artistic` ou `hybrid`, créer ou réutiliser un dossier `MASTER`, inventorier les références et assets, enregistrer les décisions, risques, critères d'acceptation et sources de vérité. Préserve les fichiers existants et n'importe pas d'anciens essais sans choix explicite.

Le bootstrap `newpro` s'arrête après la préparation du socle ; il ne bloque pas la production de la plancha. Si l'appel imbriqué n'est pas disponible, reproduis sa méthode dans `MASTER/` puis continue.

### `brain` — analyse et contrôle final

Applique `brain` pour séparer les données fournies des hypothèses et des choix créatifs, détecter les incohérences de proportions, de couleurs, de références ou de variantes, vérifier la couverture de la demande et exécuter son `FINAL GATE` avant la livraison.

### `asset-continuity` — canon réutilisable

Applique `asset-continuity` pour attribuer des IDs stables aux sujets et références, séparer les invariants des variantes, suivre les changements d'état et relier les vues, palettes, matériaux, prompts et exports. Son pack sous `MASTER/CONTINUITY/` est la source de vérité inter-projets ; `continuite.md` reste une vue de travail lisible et ne doit pas diverger de `CANON.md` ou `STATE_LEDGER.md`.

## Questionnaire initial adaptatif

Pose uniquement les questions nécessaires parmi les suivantes :

1. **Type et sujet** — personnage, décor, objet, arme, véhicule, créature, costume, image de référence ou autre.
2. **Usage** — BD, manga, jeu, 3D, concept art, présentation ou autre.
3. **Style** — par défaut, choisir le style cohérent avec l'usage et les références fournies.
4. **Couverture technique** — vues, poses, expressions, variantes, détails, matériaux ou échelle souhaités.
5. **Format et contraintes** — par défaut, planche paysage haute résolution adaptée à l'impression, avec version web et PDF.

Si l'utilisateur répond « choisis », décide sans relancer. Les valeurs par défaut sont : planche maître paysage, 300 dpi, fond clair neutre, vues et annotations lisibles, génération de variantes utiles uniquement, PNG haute résolution, PDF et archive ZIP.

## Dossier de production

Utilise le dossier MASTER de `newpro` s'il existe ; sinon crée un dossier `PLANCHA_<nom_slugifie>` dans les sorties du projet. Utilise des noms de fichiers sûrs et sépare les sources des exports.

```text
PLANCHA_<nom_slugifie>/
├── MASTER/
│   ├── 00_BRIEF.md
│   ├── 01_DECISIONS.md
│   ├── 02_SOURCES_DE_VERITE.md
│   ├── 03_RISQUES_ET_ACCEPTATION.md
│   └── 04_INVENTAIRE_ASSETS.md
├── planche_maitre.png
├── planche_maitre.pdf
├── planche_web.jpg
├── vues_separees/
├── variantes/
├── details/
├── palette_et_materiaux.md
├── prompt_maitre.md
├── continuite.md
├── references.md
├── README.md
└── PLANCHA_<nom_slugifie>.zip
```

Le fichier `continuite.md` est obligatoire. Il suit chaque élément visuel avec les colonnes `Élément / Valeur verrouillée / Variantes autorisées / Source / Vérifié`.

Enregistre aussi chaque fichier livré dans `MASTER/CONTINUITY/ASSET_REGISTRY.md` avec son ID, sa version, son statut et ses dépendances. Pour une reprise, audite les planches existantes avant d'en promouvoir une comme référence canonique.

## Étape 1 — brief et architecture de la planche

Écris un brief court avant de produire :

- sujet et fonction de la planche ;
- type de production cible ;
- style graphique, époque, ambiance et niveau de réalisme ;
- dimensions relatives, proportions et éléments non négociables ;
- vues, poses, expressions, détails et variantes ;
- palette, matières, éclairage et arrière-plan ;
- format d'export et contraintes de lisibilité.

Choisis la densité de la planche selon le sujet. Une planche de personnage privilégie la silhouette, les vues et les expressions ; une planche de décor privilégie l'espace, les plans, les matières et les sources de lumière ; une planche d'objet privilégie les détails, les matériaux, le fonctionnement et les variantes.

## Étape 2 — planche de personnage

Pour un personnage, produis par défaut :

- vue face, profil, dos et trois-quarts ;
- silhouette pleine et repères de proportions ;
- expressions principales : neutre, joie, colère, peur, tristesse, surprise ;
- une ou deux poses caractéristiques ;
- tenue complète, accessoires et variantes indispensables ;
- palette de couleurs et échantillons de matières ;
- gros plans sur le visage, les mains, les chaussures ou les objets-signatures ;
- échelle relative et notes de langage corporel.

Fiche écrite :

```text
Nom :
Rôle :
Âge apparent :
Taille et proportions :
Silhouette :
Visage, yeux et cheveux :
Tenue et matériaux :
Accessoires :
Posture et gestuelle :
Expressions :
Particularités non négociables :
Variantes autorisées :
```

Crée un `MASTER CHARACTER PROMPT` qui reste identique pour toutes les futures images. Il décrit les traits invariants, les proportions, les couleurs, la tenue, les accessoires, le style de trait, la lumière et les éléments à exclure.

## Étape 3 — planche de décor

Pour un décor, produis par défaut :

- vue générale lisible ;
- vues rapprochées des zones importantes ;
- plan ou coupe simplifiée si elle aide la compréhension ;
- architecture, matériaux, textures et objets récurrents ;
- échelle humaine ou repères de taille ;
- variantes matin, soir, nuit, météo ou saison si elles sont utiles ;
- sources de lumière, circulation et profondeur ;
- détails de continuité à réutiliser dans les scènes.

Le décor doit être exploitable dans une scène : indique les entrées, niveaux, lignes de fuite, zones cachées, points de vue possibles et éléments qui peuvent changer après une action.

## Étape 4 — objets, armes, véhicules, créatures et costumes

Adapte la planche à la fonction du sujet :

- vues orthographiques et trois-quarts ;
- détails d'assemblage ou de fonctionnement ;
- matériaux et états de surface ;
- dimensions relatives et repères d'échelle ;
- versions neuve, usée, endommagée ou transformée ;
- interactions avec un personnage ou un décor ;
- contraintes de sécurité visuelle : pas de pièces inventées, de proportions contradictoires ou de fonctions impossibles.

Pour une créature, ajoute anatomie, locomotion, expressions, comportement et échelle. Pour un véhicule, ajoute intérieur, accès, poste de conduite et éléments mécaniques visibles. Pour un costume, ajoute fermeture, couches, matières, mobilité et vues de détail.

## Étape 5 — direction visuelle et prompt maître

Choisis une direction visuelle cohérente avec l'usage : manga, franco-belge, comics, réaliste, semi-réaliste, stylisé, jeu vidéo, concept art, maquette 3D ou autre. Définis :

- type de trait et niveau de détail ;
- contraste, noirs, trames ou rendu couleur ;
- lumière et température ;
- traitement des arrière-plans ;
- profondeur, échelle et composition ;
- rendu des matières ;
- règles de cohérence entre les vues.

Écris un prompt maître réutilisable :

```text
MASTER PLANCHA PROMPT
[type de planche et usage]
[style global]
[description verrouillée du sujet]
[vues, poses, expressions ou détails requis]
[palette, matériaux, lumière et arrière-plan]
[composition de planche technique, repères et zones calmes]
No readable text in generated art, no watermark, no logo, no duplicate subject,
no inconsistent proportions, no changed colors, no missing accessories,
no random extra parts.
```

Les annotations, légendes, flèches, mesures et noms sont ajoutés lors de la mise en page ; ne demande pas à l'outil d'image de générer du texte lisible dans l'illustration.

## Étape 6 — génération des vues et variantes

Génère d'abord une référence maître ou une vue principale, puis les autres vues en réutilisant les mêmes références, la même continuité et, quand l'outil le permet, les mêmes paramètres de cohérence. Génère ensuite les variantes utiles sans changer accidentellement le sujet.

Pour chaque vue, utilise ce canevas :

```text
[MASTER PLANCHA PROMPT]
VIEW : [face / profil / dos / trois-quarts / détail / variante]
CAMERA : [distance, angle, perspective]
SUBJECT : [position, pose, expression ou état]
ENVIRONMENT : [fond, échelle, repères]
LIGHTING : [direction, contraste, température]
CONTINUITY : [couleurs, vêtements, matériaux, dommages et accessoires]
```

Garde les images sans texte incrusté si elles doivent être annotées. Si une image de référence est fournie, respecte son sujet et modifie uniquement ce qui est demandé. Pour une planche destinée à `/newBD` ou `/new-manga`, privilégie la cohérence des silhouettes et des accessoires sur l'effet spectaculaire.

## Étape 7 — composition et annotations

Compose une planche lisible :

- hiérarchie claire entre vue maître, vues secondaires et détails ;
- grille régulière mais adaptée à la forme du sujet ;
- titres, légendes, flèches, mesures et repères hors des zones importantes ;
- palette et matériaux regroupés dans une zone dédiée ;
- espace suffisant pour les annotations et la lecture à l'écran ;
- fond et cadre cohérents entre toutes les vues.

Ajoute séparément les textes, dimensions, noms de pièces, notes de couleur et commentaires de production. Utilise une police simple, une taille lisible et un ordre de lecture stable. Une planche peut être visuellement belle, mais elle doit d'abord être exploitable par une autre image ou une autre scène.

## Étape 8 — contrôle de cohérence

Vérifie avant export :

- proportions et silhouette ;
- visage, coiffure, couleurs, tenue et accessoires ;
- orientation gauche/droite et correspondance face/profil/dos ;
- matériaux, textures, détails et fonctions ;
- échelle, perspective et points de contact ;
- variantes et états d'usure ;
- cohérence avec les références fournies ;
- lisibilité des annotations et absence de texte généré illisible ;
- conformité du format, de la résolution et de l'ordre des fichiers.

Corrige ou régénère les vues incohérentes avant la mise en page finale. Le `FINAL GATE` de `brain` doit confirmer que chaque demande de l'utilisateur correspond à une vue, une annotation ou un fichier livré.

Exécute ensuite le contrôle de `asset-continuity` sur une planche-contact des vues et variantes. Compare chaque vue à la référence canonique, pas seulement à la vue générée juste avant.

## Étape 9 — exports et livraison

Produis au minimum :

1. `planche_maitre.png` en haute résolution ;
2. `planche_maitre.pdf` prêt à imprimer ;
3. `planche_web.jpg` ou PNG optimisé pour l'écran ;
4. les vues séparées ;
5. les variantes et détails ;
6. `palette_et_materiaux.md` ;
7. `prompt_maitre.md` ;
8. `continuite.md` ;
9. `references.md` ;
10. `README.md` ;
11. l'archive ZIP complète.

Le `README.md` indique le sujet, le type de planche, l'usage, le style, le format, les fichiers principaux, les limites et les éléments non générés. Inspecte la planche maître, une vue séparée, le PDF et la version web avant livraison.

## Connexion avec `/newBD` et `/new-manga`

Quand une production BD ou manga a besoin d'une référence visuelle, utilise `plancha` avant de générer les scènes finales pour créer :

- les fiches personnages et leurs prompts maîtres ;
- les décors récurrents et leurs variantes de lumière ;
- les armes, objets, véhicules et accessoires ;
- les palettes et matériaux ;
- les règles de continuité reprises ensuite dans les prompts de cases.

Réutilise les fichiers de continuité de `plancha` comme sources de vérité dans la BD ou le manga. Ne remplace pas une plancha existante sans préserver la version précédente et enregistrer la décision.

## Format de la réponse finale

Présente d'abord les liens vers les livrables, puis un résumé court du sujet, du type de planche, du style, du format et des éventuelles limites. Les chemins doivent être absolus et cliquables. Si la génération d'images n'a pas été possible, distingue clairement les fichiers produits des éléments restant à générer.
