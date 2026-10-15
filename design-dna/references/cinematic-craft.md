# Finition, profondeur et direction cinématique

Préférence explicite de Nicolas, 15 octobre 2026 : des sites léchés, profonds,
cinématiques, cohérents avec leur niche, sans rendu plat ni générique.

## Parcours de conception et preuves

1. Lire la niche, les produits, les usages et les contraintes. Examiner les références
   réelles et les éléments déjà approuvés. Écrire pourquoi chacune convient à ce public,
   et ce qui serait hors sujet. Ne pas transposer le décor d'une autre niche.
2. Pour un nouveau site, présenter les deux directions prévues avec références rendues,
   vocabulaire visuel, profondeur et cadrage. Pour une refonte, conserver la direction
   approuvée ; cette préférence de qualité ne permet pas de la remplacer sans accord.
3. Fixer dans PROJECT_SKIN et design-system.md : relation niche/public, références,
   matériaux et surfaces, lumière et ombres, plans avant/arrière, proportions,
   cadrages et typographies, transitions entre sections, hiérarchie des CTA.
   La profondeur doit être perceptible au repos, pas seulement au survol.
4. Réaliser un échantillon dans les trois pages pilotes : landing avec produits réels,
   page de lecture et comparaison selon le projet. Inspecter la composition complète,
   les gros plans de composants et les états desktop/mobile avant production en volume.
5. Rejouer la recette après changement du CSS partagé, des composants, du skin ou des
   médias. Conserver les preuves de correction et les décisions existantes utiles.

## Boutons, cartes, cases et formulaires

Définir une famille cohérente : bouton primaire, secondaire et discret ; carte produit,
case de sélection/checkbox/radio, filtre, champ, onglet et panneau lorsque présents.
Spécifier et observer normal, hover lorsque disponible, focus-visible, pressé,
sélectionné, disabled, chargement, succès, erreur et état vide selon applicabilité.
Documenter les états sans objet au lieu d'inventer une interaction.

Donner une sensation de matière par les proportions, contrastes, lumière, bordures,
ombres et retours d'action cohérents. Ne pas appliquer le même relief à tout.
Le contrôle reste identifiable et lisible au repos ; le tactile fonctionne sans hover.
Nom accessible, clavier, focus, taille utilisable et feedback sont conservés.
Une carte ne devient pas un bouton géant ambigu avec des liens imbriqués.
Pas de petite flèche décorative dans les CTA. Préserver les icônes fonctionnelles.

## Cinématique utile

Construire une progression par cadrages, changements d'échelle, rythme, continuité des
plans et transitions motivées. Sur une landing d'affiliation, produits et CTA restent
immédiatement accessibles ; la narration accompagne le choix. Sur un article dense,
la composition éditoriale peut porter le caractère cinématique avec très peu de motion.
Éviter intro bloquante, scroll détourné, curseur imposé, vidéo décorative lourde,
animations simultanées et effets copiés sans rapport avec la niche.
Prévoir reduced-motion, rendu sans JS pour le contenu et fallback des effets facultatifs.
Mesurer la performance ; les effets ne justifient pas de masquer un échec.

## Outils et réemploi

Partir des composants du projet déjà approuvés et de leurs sources réelles.
CSS et Web Animations API permettent le socle sans outil payant obligatoire.
Si disponibles et pertinents, lire transitions-dev pour les interactions locales
et transitions-polish pour leur cohérence avant de les appliquer. Une bibliothèque
fournit un mécanisme, jamais automatiquement une direction artistique.
Un snippet externe exige lecture de sa source, compatibilité et droits vérifiés ;
aucun achat, service payant ou copie de site n'est nécessaire à ce standard.
Consigner outil, composant, référence et adaptation. Si un ancien outil ou exemple
n'est pas accessible, le signaler sans inventer sa consultation.

## Recette visuelle bloquante

La revue doit citer les vues et états inspectés et expliquer :
- pourquoi le rendu appartient à cette niche ;
- où la profondeur est effectivement visible au repos ;
- ce qui construit le cadrage et le rythme cinématique ;
- comment les boutons, cartes et cases sont finis et cohérents ;
- ce qui a été corrigé après comparaison avec les références/V1 ;
- les résultats responsive, clavier, motion réduite et performance.

PASS seulement après observation rendue et correction des défauts.
SOURCE_ONLY ou NOT_RUN ne valent pas validation. Aucun score automatique de goût :
les tests contrôlent les états et preuves, la revue visuelle juge le rendu.
