# FOLIO — Études de mouvement

Ouvrir `index.html` dans Chrome. Tous les fichiers nécessaires sont locaux : aucune installation, aucun serveur et aucune connexion ne sont requis.

## Manipulation

- Cliquer sur la couverture pour ouvrir la revue.
- Cliquer sur la page droite pour avancer, sur la page gauche pour revenir.
- Glisser horizontalement une page pour la courber et la retourner.
- Cliquer plusieurs fois rapidement : les pages peuvent se retourner simultanément et accélèrent avec les clics rapprochés. Un clic inverse est accepté immédiatement.
- Utiliser les flèches du clavier ou les boutons de navigation.
- Le sommaire donne accès aux six études.
- La vue lecture montre les doubles pages à plat. Sur téléphone, faire défiler horizontalement les deux planches.
- Le son du papier est optionnel, désactivé au démarrage.

Les préférences de mouvement réduit sont respectées. Une vue à plat prend le relais si WebGL est indisponible. Le texte de la double page est également présent dans le DOM pour les lecteurs d'écran.

## Contenu et technique

Sept feuilles 3D, six compositions graphiques originales générées sur canvas, pages courbées par intégration de leur profil, éclairage et ombres Three.js. Le bord libre suit le pli dans les deux directions. Le sens de la courbure se mélange progressivement lors des inversions en vol. Les clics sont acceptés pendant les retournements et accélèrent les pages en vol sans réinitialiser leur position. La déformation utilise 64 segments et deux rangées de sommets, partagés entre recto et verso; les normales sont calculées directement à partir du profil. Les ombres sont mises à jour lorsque l'objet change. Le rendu s'arrête lorsque la scène est immobile ou masquée. Les textures sont précalculées et la résolution du rendu est plafonnée à un ratio de pixels de 2.

La référence de concept est le magazine interactif Paper Mono partagé par Three.js : https://paper.design/mono. FOLIO utilise sa propre identité et ses propres planches.

`src/` contient le code source lisible. `assets/main.js` est le bundle autonome avec Three.js. `PROJECT_SKIN.yaml` documente la direction artistique et l'état des vérifications. `THIRD_PARTY_LICENSE.txt` contient la licence de Three.js.

## Vérifications de cette livraison

Compilation du bundle, vérifications de syntaxe, tests du profil de papier, des limites de navigation, du sommaire, du texte accessible et du mode sans WebGL effectués. Les planches et une page de texte ont été contrôlées visuellement sur des rendus canvas. La construction de la scène, les transitions entre chapitres, le passage par la vue lecture et l'arrêt du rendu au repos ont été testés avec un renderer simulé.

L'accès automatisé à Chrome a échoué dans la session : le rendu GPU, les gestes et la mise en page aux différentes tailles restent à valider visuellement dans Chrome. Les tests avec un renderer simulé ne valident pas l'éclairage, les ombres ou la fluidité réelle.
