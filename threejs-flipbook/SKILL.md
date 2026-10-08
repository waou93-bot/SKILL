---
name: threejs-flipbook
description: Créer ou intégrer un livre, magazine ou portfolio 3D feuilletable avec Three.js, pages courbées, clics rapides et vue de lecture. Utiliser pour réemployer le moteur FOLIO dans un autre projet.
---

# Three.js Flipbook

Réutiliser le moteur de pages de `assets/starter/` en adaptant le contenu et la direction artistique au projet. FOLIO est un exemple d'intégration, pas une identité à imposer. Garder les choix explicites de l'utilisateur et les instructions du projet.

## Réemploi

- Pour un prototype autonome, copier `assets/starter/` dans un nouveau dossier du projet. Installer ses dépendances avec `npm install`, puis lancer `npm run build`. Ouvrir `FOLIO.html` ou `index.html`.
- Pour une application existante, porter le moteur de `src/paper.mjs` et les interactions utiles de `src/main.mjs` dans son cycle de vie. Nettoyer les listeners, observers, RAF, matériaux, textures, géométries et renderer au démontage. Ne pas copier aveuglément les IDs DOM ou la configuration du starter.
- Adapter les planches dans `src/art.mjs` ou remplacer les textures par les contenus du projet. Le starter compte sept feuilles, couverture comprise. Si ce nombre change, synchroniser `SHEETS`, les textures recto/verso, les chapitres et les limites de navigation.
- Si une direction visuelle est demandée, utiliser `design-dna` lorsqu'il est disponible et créer le skin du projet; ne pas reprendre automatiquement le rouge, la typographie ou les illustrations de FOLIO.

## Invariants du moteur

- Les pages sont dans le plan XY; +Z est au-dessus du papier. Une progression de 0 à 1 tourne la feuille de la droite vers la gauche. Le bord libre suit le pli : `angle = progress * PI - curl * direction`, avec direction +1 vers la gauche et -1 vers la droite. À mi-course les profils sont miroirs. Lisser le changement de direction pour une inversion en vol; à plat, initialiser directement le signe puisque la courbure est nulle. Préserver la longueur d'arc lors de la déformation.
- Le verso partage les positions et normales du recto, mais possède ses propres UV inversés horizontalement et un matériau `BackSide`.
- Ne pas bloquer les clics pendant une animation. La zone de navigation reste attachée au plan du livre, indépendante des triangles en vol. Les clics rapprochés accélèrent les pages sans remettre leur progression à zéro; les changements de direction restent acceptés.
- Un pointeur pressé n'est pas encore un glissement. Suspendre une feuille uniquement quand le déplacement de glissement a effectivement commencé.
- Le bord extérieur est une zone de saisie explicite, avec curseur grab. Pendant la saisie, la progression suit directement la souris, sans animation automatique concurrente. Mesurer la course sur la largeur projetée du livre, pas celle de la fenêtre. Au relâchement, terminer ou revenir selon la moitié franchie; au pointercancel, revenir à la destination précédente. Conserver les clics au centre.
- Calculer directement les normales à partir du profil, partager les buffers de déformation et éviter les recalculs de bounding sphere à chaque frame. Dans ce modèle, une seule subdivision verticale suffit.
- Arrêter le RAF au repos et lorsque la page est masquée. Actualiser les ombres quand la géométrie ou le transform change. Conserver le mouvement réduit, le mode à plat et l'accès clavier.

## Livraison et contrôles

`build.mjs` compile avec esbuild puis embarque CSS et JS dans un HTML autonome. Pour insérer du JavaScript dans une chaîne HTML, utiliser une fonction de remplacement : `html.replace('</body>', () => payload)`. Un remplacement par chaîne interprète les séquences `$&` de Three.js et peut corrompre les shaders. Échapper les balises de fermeture de script et vérifier que le JS extrait du HTML est identique au bundle.

Lancer `npm test` pour contrôler le profil, le sens de courbure, les bornes et les faces des doubles pages. Tester aussi dans le navigateur cible : ouverture du fichier livré, cinq clics rapides sans attente, inversion immédiate, glissement, vue lecture, mobile et mouvement réduit. Des tests de géométrie ou un renderer simulé ne prouvent pas le rendu GPU ou les FPS.

Le moteur conserve un artefact de référence `assets/starter/FOLIO.html`. La géométrie, la navigation et les rafales de clics ont été testées dans la session d'origine; le rendu GPU de la dernière correction d'assemblage n'a pas été confirmé visuellement. Ne pas annoncer cette validation comme acquise.

Conserver `THIRD_PARTY_LICENSE.txt` lors des distributions contenant Three.js. Aucune publication, dépense ou configuration externe n'est nécessaire à ce skill.
