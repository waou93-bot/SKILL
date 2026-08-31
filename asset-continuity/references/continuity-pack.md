# Pack de continuité

Utilise ces modèles comme structure minimale. Adapte les colonnes au média et fusionne-les avec les registres compatibles déjà présents.

## `ASSET_REGISTRY.md`

```markdown
| ID stable | Rôle | Type | Fichier ou URI | Version | Statut | Source/licence | Dépend de | Vérifié |
|---|---|---|---|---|---|---|---|---|
| CHAR-ALBA | personnage maître | image | refs/alba-turnaround.png | v1 | canon | création projet | — | oui |
```

Statuts utiles : `candidat`, `canon`, `dérivé`, `obsolète`, `à corriger`, `manquant`. Ne recycle jamais un ID pour une autre entité.

## `CANON.md`

```markdown
## Entité : CHAR-ALBA

Références canoniques :
- `refs/alba-turnaround.png` — identité et proportions
- `refs/alba-palette.png` — couleurs et matériaux

Invariants :
- silhouette, âge apparent, proportions du visage ;
- cicatrice sur le sourcil gauche ;
- manteau bleu nuit, boucle argentée triangulaire.

Variables de scène :
- pose, expression, cadrage, lumière ;
- manteau ouvert ou fermé.

Changements autorisés :
- tenue endommagée uniquement après l'événement EVT-07.

Interdits :
- cicatrice inversée ;
- boucle dorée ;
- changement de coupe non enregistré.

Inconnues :
- motif exact sous le manteau, à ne pas rendre visible avant arbitrage.
```

Pour une marque ou une interface, remplace l'identité physique par les tokens, logos, grilles, familles typographiques, rayons, iconographie et règles de composition. Pour l'audio, consigne voix, prononciation, tempo, niveaux et chaîne de traitement. Pour la 3D, ajoute unités, axes, dimensions, hiérarchie, pivots, matériaux et conventions d'export.

## `STATE_LEDGER.md`

```markdown
| Entité | État d'entrée | Changement intentionnel | Début | État de sortie | Assets touchés | Source | Vérifié |
|---|---|---|---|---|---|---|---|
| CHAR-ALBA | manteau intact | déchirure manche droite | EVT-07 | manche déchirée | IMG-023 à IMG-031 | storyboard p. 18 | oui |
```

Un changement doit avoir une cause et une portée. En dehors de cette portée, l'état précédent reste canonique.

## Bloc de génération

```text
CANONICAL BASE
[IDs et invariants nécessaires]
[références canoniques directes]
[style, palette, matériaux ou traitement verrouillés]

LOCAL DELTA
[action, pose, cadrage, format, lumière et état attendus pour cet asset]

CONTINUITY EXCLUSIONS
[inversions, disparitions, substitutions, variations ou artefacts interdits]
```

N'inclus que les entités présentes et les règles pertinentes. Conserve le socle identique pour une même version du canon.

## `QA_CONTINUITY.md`

```markdown
PÉRIMÈTRE : [fichiers, scènes, pages, slides ou versions]
CANON UTILISÉ : [IDs et versions]
MÉTHODE : [planche-contact, voisins, orbite, écoute comparative, inspection UI]
STATUT : PASS | FIX | BLOCKED

| Sévérité | Asset | Écart | Source à corriger | Correction | Preuve | Statut |
|---|---|---|---|---|---|---|
```

Échantillonne seulement pour détecter des risques ; avant une livraison finale, inspecte tous les assets critiques et toutes les transitions où un état change.
