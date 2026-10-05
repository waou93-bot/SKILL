# Registre personnel d'assets gratuits

Registre de depart pour les projets Three.js, logiciels, artistiques et hybrides. Les ressources sont referencees ; elles ne sont jamais telechargees ou copiees automatiquement par `newpro`.

Derniere verification des pages : **2026-08-03**. Re-verifier la page de licence de l'asset choisi avant une diffusion publique, surtout pour les sources de priorite `B` et `TEST`.

## Regle de selection

- `A` : point de depart recommande ; licence globale claire, souvent CC0.
- `B` : utile, mais verifier les conditions de chaque service ou asset.
- `TEST` : principalement pour tester Three.js, glTF et les loaders.
- Format prefere pour le Web : `.glb` ou `.gltf`. Garder les textures et les fichiers annexes avec le modele.

## Sources a piocher

| ID | Usage | Formats utiles | Licence | Priorite | Lien |
|---|---|---|---|---|---|
| `polyhaven-models` | Modeles realistes, props, environnements | glTF, Blend, FBX | CC0 | A | [Modeles Poly Haven](https://polyhaven.com/models) |
| `polyhaven-hdri` | Eclairage et reflets realistes | HDR, EXR | CC0 | A | [HDRI Poly Haven](https://polyhaven.com/hdris) |
| `polyhaven-textures` | Materiaux PBR et surfaces | PNG, JPG | CC0 | A | [Textures Poly Haven](https://polyhaven.com/textures) |
| `kenney-3d` | Packs stylises, low-poly, props, vehicules | GLB, FBX, OBJ | CC0 | A | [Assets 3D Kenney](https://kenney.nl/assets) |
| `quaternius-fantasy-props` | Props medievales et fantasy | glTF, FBX, OBJ, Blend | CC0 | A | [Fantasy Props MegaKit](https://quaternius.com/packs/fantasypropsmegakit.html) |
| `quaternius-characters` | Personnages humanoides rigges | glTF, FBX, Blend | CC0 | A | [Universal Base Characters](https://quaternius.com/packs/universalbasecharacters.html) |
| `quaternius-space` | Sci-fi, vaisseaux, planetes, ennemis | glTF, FBX, OBJ, Blend | CC0 | A | [Ultimate Space Kit](https://quaternius.com/packs/ultimatespacekit.html) |
| `ambientcg-pbr` | Sols, rochers, metal, bois, HDRI | JPG, PNG, HDR | CC0 | A | [ambientCG](https://ambientcg.com/) |
| `mixamo-characters-animation` | Animations et personnages humanoides | FBX, DAE, OBJ | Conditions Mixamo | B | [Mixamo](https://www.mixamo.com/) |
| `sketchfab-free` | Objets specifiques et scans | glTF, GLB, FBX, OBJ | Par asset | B | [Sketchfab Free](https://sketchfab.com/features/free-3d-models) |
| `khronos-gltf-samples` | Tests glTF, PBR, Draco, Meshopt, animations | glTF, GLB | Par modele | TEST | [Khronos glTF Samples](https://github.khronos.org/glTF-Assets/) |

## Combinaisons de depart

### Scene realiste

`polyhaven-hdri` + `polyhaven-models` + `ambientcg-pbr`

### Prototype stylise

`kenney-3d` + `quaternius-fantasy-props`

### Personnage anime

`quaternius-characters` + `mixamo-characters-animation`

### Test technique Three.js

`khronos-gltf-samples` + [GLTFLoader Three.js](https://threejs.org/docs/pages/GLTFLoader.html)

## Trace a conserver dans un projet

Quand un asset est retenu, ajouter dans `docs/03_INVENTAIRE_DES_ASSETS.md` :

- l'ID du registre ;
- l'URL exacte de l'asset ;
- la licence et l'auteur ;
- le format et la version telecharges ;
- le statut : `a examiner`, `retenu`, `importe`, `exclu` ;
- les transformations effectuees.

Ne pas reconditionner ou redistribuer les fichiers bruts d'une source dont les conditions ne l'autorisent pas explicitement.
