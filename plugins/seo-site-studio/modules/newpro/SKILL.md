---
name: newpro
description: Bootstrap prudent et relancable de nouveaux projets dans une structure MASTER avec inspection du contexte, classification logiciel/artistique/hybride, registre d'assets gratuits, sources de verite, decisions, risques, backlog, criteres d'acceptation et tranche verticale proposee. Utiliser quand Codex doit transformer une idee, un dossier existant, un brief ou un ancien projet en socle de projet verifie sans lancer la production.
---

# New Project Bootstrap

## Mission

Transformer le contexte disponible en un socle MASTER lisible, trace et verifie. Inspecter d'abord, demander uniquement les informations indispensables, classifier le projet, creer les fichiers manquants sans ecraser silencieusement, puis terminer par les arbitrages ouverts et la prochaine action.

La V1 couvre trois profils : `software`, `artistic` et `hybrid`. Elle prepare la tranche verticale mais ne lance jamais sa production. La creation d'un Projet ChatGPT, le choix de sa memoire et la creation de conversations restent des actions manuelles ; preparer les instructions et la liste des sources a importer si cela est utile.

## Workflow

### 1. Inspecter

Executer l'inspection avant de poser une question :

```text
python scripts/inspect_context.py --root . --json
```

Lire le JSON et les fichiers pertinents sans parcourir aveuglement les dependances ou caches. Relever le nom probable, les fichiers existants, Git, les indices logiciels/artistiques, les decisions deja explicites et les incertitudes. Consulter [PROJECT_TYPES.md](references/PROJECT_TYPES.md) pour les regles de classification.

Si le projet touche Three.js, WebGL, 3D, jeu, audiovisuel ou direction artistique, consulter [ASSET_REGISTRY.md](references/ASSET_REGISTRY.md). Utiliser `python scripts/asset_registry.py --query "..." --format glb` pour piocher dans les sources referencees. Proposer une shortlist, ne rien telecharger automatiquement et verifier la licence de l'asset precis avant import.

Si le projet contient ou prévoit plusieurs images, médias, modèles, composants visuels ou autres assets liés, charger `asset-continuity`. Pour un ancien projet, commencer par son audit en lecture seule. Préparer ou reprendre `MASTER/CONTINUITY/` et relier le registre d'assets de `newpro` aux IDs stables du pack sans déplacer les fichiers ni dupliquer les sources de vérité. Le bootstrap prépare cette continuité mais ne lance aucune régénération.

### 2. Poser les questions minimales

Poser en une seule fois uniquement les questions qui bloquent le bootstrap :

- objectif principal si aucun objectif fiable n'est deja connu ;
- nom si le dossier et la conversation ne permettent pas de le deduire ;
- profil si la classification est indeterminee ou si l'utilisateur la corrige ;
- emplacement MASTER si la destination proposee n'est pas acceptable.

Ne pas demander ce qui peut etre deduit. Ne jamais inventer une decision, une contrainte, une source ou une technologie. Representer les inconnues par `[A ARBITRER]`, et distinguer faits, decisions, hypotheses, propositions, rejets et incertitudes. L'import des anciens essais est opt-in : par defaut, les inventorier sans les copier.

### 3. Previsualiser puis bootstrapper

Previsualiser la structure avant toute ecriture :

```text
python scripts/bootstrap_project.py --root . --project-name "NOM" --objective "..." --project-type auto --dry-run
```

Apres validation du plan, executer sans `--dry-run`. Le script cree un dossier sibling `NOM - MASTER` par defaut, ou l'emplacement donne par `--out`. Il preserve tout fichier existant, refuse d'adopter un dossier non vide sans `--adopt-existing`, ecrit un manifeste interne et peut etre relance sans duplication.

### 4. Valider

Executer la validation du MASTER :

```text
python scripts/validate_project.py --master "NOM - MASTER" --json
```

Corriger les erreurs avant d'annoncer que le socle est pret. Les avertissements non bloquants et les arbitrages ouverts doivent rester visibles dans le rapport final.

### 5. Conclure

Toujours produire ou afficher un rapport avec :

- classification et preuves ;
- fichiers crees et fichiers preserves ;
- arbitrages et questions restantes ;
- tranche verticale proposee, perimetre inclus/exclus et risques testes ;
- affirmation explicite qu'aucune production n'a commence ;
- prochaine action unique, formulee comme une decision ou une validation.

Lire [DECISION_RULES.md](references/DECISION_RULES.md) pour les garde-fous, puis les templates sous `assets/templates/` avant d'adapter la structure. Les scripts sont portables et ne demandent aucune dependance Python externe.

Le registre d'assets est une source de suggestions, pas une source de verite du projet. Lorsqu'un asset est retenu, reporter son ID, son URL, sa licence, son format et son statut dans `docs/03_INVENTAIRE_DES_ASSETS.md` et, s'il est importe, dans `docs/reprise/IMPORT-MANIFEST.md`.

Quand `asset-continuity` s'applique, reporter aussi l'ID stable correspondant dans ces documents ; `MASTER/CONTINUITY/ASSET_REGISTRY.md` devient le registre transversal des versions, dépendances et références canoniques.

## Garde-fous non negociables

- Ne jamais ecraser silencieusement ni supprimer.
- Ne jamais lancer de production fonctionnelle, artistique ou commerciale pendant le bootstrap.
- Ne jamais transformer une hypothese en decision.
- Ne jamais importer des essais historiques sans choix explicite.
- Ne pas multiplier les agents avant d'avoir defini leur mandat dans le MASTER.
- En cas de conflit entre un fichier existant et un template, conserver l'existant et signaler l'arbitrage.
