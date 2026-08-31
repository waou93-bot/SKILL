---
name: newsite
description: "Cadrer et construire un site de conversion non marchand avec un MASTER validé, une équipe de sous-agents, une stack choisie et une interface contrôlée. Use when the user asks to create, launch, redesign, bootstrap, or resume a website project. Do not use for a small isolated correction when no project launch workflow is needed."
---

# /newsite

## Mission

Conduire un projet de site en deux temps : décider et documenter, puis produire après accord explicite. Pour un site non marchand, le résultat attendu est une conversion relationnelle mesurable : une demande de rendez-vous, de devis, d'échange, de brief ou un téléchargement utile. Ce résultat ne se réduit pas à un clic.

L'art direction précède les composants. Le site doit avoir un concept, une composition, une typographie, une grille, un langage d'interaction et un langage de mouvement cohérents avant que la réalisation ne choisisse ou ne fabrique des composants. La stack sert cette direction ; elle ne la remplace pas.

Le skill est un orchestrateur. Brain garde la décision finale et vérifie les preuves. Les sous-agents apportent des livrables distincts de stratégie marketing, UX de conversion, direction UI, puis réalisation et recette. Ne pas appeler une tâche « revue spécialisée » si aucun rôle n'a réellement été exécuté.

Avant d'agir, trouver les skills disponibles et lire entièrement leurs instructions ainsi que leurs références obligatoires. Suivre cet ordre :

1. brain pour le besoin, les sources, les risques et la décision de passage.
2. newpro pour inspecter le contexte et créer ou reprendre le MASTER.
3. toolbox pour repérer les références du domaine, les outils pertinents et les contraintes d'accès ou de licence.
4. product-marketing et cro pour la cible, la promesse, les objections et l'action principale.
5. no-slop pour toute rédaction visible ou documentaire.
6. design-taste-frontend et asset-continuity pour la direction UI et les médias.
7. Les skills de la stack retenue, webapp-testing et web-design-guidelines après validation du MASTER.

Pour une direction créative, charger aussi les skills ou références nécessaires à GSAP, au WebGL, à la 3D ou à la stack retenue, uniquement après avoir établi le besoin dans le MASTER.

Si une capacité est absente, l'indiquer et appliquer le rôle séquentiellement lorsque cela reste possible. Ne pas inventer d'instruction, de recherche, de test ou de source.

## Phase A : cadrage

### 0. Router le périmètre

Avant de déclencher le cadrage complet, classer la demande :

- nouvelle marque, nouveau site, changement de conversion, de public, de preuve, de stack ou de direction : exécuter toute la Phase A ;
- MASTER déjà validé et évolution bornée qui ne change aucun de ces éléments : ne pas invoquer `newsite` pour un simple correctif. Reprendre directement la Phase B avec une vérification ciblée du Contrat de conversion, du canon, de la continuité et des critères d’acceptation touchés ;
- périmètre incertain : exécuter la Phase A plutôt que de supposer que l’ancien MASTER reste valable.

Le routeur évite de refaire une recherche de références ou un bootstrap lorsque le projet est déjà décidé. Il ne permet jamais de contourner la validation quand le changement modifie la promesse, la preuve ou la conversion.

### 1. Vérifier le besoin

- Reformuler le résultat concret, le public, l'action principale et la preuve de réussite.
- Tester les prémisses importantes. Distinguer faits, hypothèses, décisions et inconnues.
- Inspecter le dossier de travail avant de poser une question.
- Poser au plus une question à la fois, uniquement si la réponse change réellement la solution.
- Vérifier sur des sources actuelles toute information susceptible d'avoir changé.
- Dès que le thème et le domaine sont suffisamment clairs, appliquer `toolbox` pour rechercher et documenter les références, outils et ressources utiles au projet.
- Dès que le thème, le domaine et le type de site sont suffisamment clairs, rechercher exactement trois sites actuels qui constituent des références pertinentes pour la création en cours. Les choisir pour leur proximité avec le domaine, le public, l'offre, le niveau d'intention ou le type de conversion ; ne pas retenir trois exemples génériques uniquement parce qu'ils sont visuellement populaires.
- Inspecter les pages principales de ces trois sites et, lorsque c'est pertinent et autorisé, leurs éléments observables côté technique. Pour chaque référence, analyser séparément la pertinence métier, la direction visuelle, la composition, la typographie, la hiérarchie, les interactions, le parcours utilisateur, les mécaniques de conversion, les performances perceptibles et les motifs à adapter ou à rejeter. Ne pas déduire une stack sans preuve.
- Utiliser des sources actuelles et conserver pour chaque site son nom, son URL, sa date de consultation, la raison de sa sélection, les observations visuelles et techniques, les enseignements UX, les éléments réutilisables sous forme de principes et les éléments explicitement exclus. Marquer les observations Certain/Likely/Assuming/Unknown et ne jamais copier un site ou ses assets.
- Si trois références parfaitement directes n'existent pas, documenter la recherche effectuée et compléter avec des références adjacentes clairement étiquetées ; ne jamais inventer une référence, une observation ou une justification.

### 2. Créer ou reprendre le MASTER

- Appliquer newpro et ses scripts depuis la racine active du skill.
- Commencer par un dry-run lorsque newpro le prévoit.
- Pour un projet existant, préserver l'historique et n'utiliser le mode d'adoption que si l'utilisateur a clairement demandé de reprendre ce dossier.
- Documenter au minimum : objectif, utilisateurs, périmètre, hors-périmètre, architecture, pages, contenu, direction visuelle, données, dépendances, critères d'acceptation, vérifications et tranche verticale initiale.
- Ajouter au MASTER une section nommée `Références du domaine` contenant exactement les trois sites retenus et leur analyse visuelle, technique et UX. Relier cette section au Design Read, au Contrat de conversion et au Toolbox snapshot. Pour un MASTER existant, compléter ou versionner cette section sans supprimer son historique.
- Nommer dans le MASTER le mandat des rôles stratégie marketing, UX de conversion, direction UI et réalisation/recette avant de lancer des sous-agents.
- Quand asset-continuity s'applique, créer ou reprendre MASTER/CONTINUITY/ pour les logos, tokens, typographies, iconographie, médias et variantes responsive. Auditer l'existant avant de choisir les références canoniques.
- Ne pas installer de dépendance, importer massivement des ressources, réinitialiser un dépôt ni commencer le code du site pendant cette phase.
- Exécuter la validation du MASTER prévue par newpro.

### 3. Définir le contrat de conversion

Lire references/conversion-workflow.md. Créer dans le MASTER un Contrat de conversion, en respectant sa convention de nommage documentaire.

- Nommer un visiteur prioritaire, son contexte d'arrivée et son niveau d'intention.
- Définir ce qu'il doit pouvoir reformuler en cinq secondes, son frein principal et les preuves admissibles.
- Choisir une seule conversion principale, son libellé exact et la suite réelle après le clic.
- Définir le signal de réussite et le seuil minimal de qualification sans inventer de taux cible.
- Lister les promesses, chiffres, témoignages, logos, images ou mécaniques qui restent exclus.

Une conversion relationnelle transmet une intention exploitable à l'organisation. Un CTA vague, un compteur, une disponibilité inventée ou une fausse preuve ne valent pas conversion.

### 4. Faire converger les rôles

Lire references/conversion-workflow.md, references/design-toolbox.md et references/anti-template-gate.md.

Pour un site vitrine, portfolio ou landing, lancer en parallèle lorsque les sous-agents sont disponibles :

1. Stratégie marketing : cible, langage client, promesse prouvable, objections, preuves et suite après l'action.
2. UX de conversion : parcours, hiérarchie des actions, contenu requis, frictions et protocole de test.
3. Direction UI : Design Read, les trois références du domaine du MASTER, système typographique, règles de médias, composants admis et motifs refusés.

Le Design Read suit obligatoirement ce protocole de décision, dans cet ordre :

`concept -> direction artistique -> composition -> typographie -> grille -> interaction -> motion language -> implémentation`

Il doit expliquer comment chaque décision découle de la précédente. L'implémentation ne peut pas servir à découvrir le concept après coup. Aucun kit de composants, aucune maquette de section et aucun choix de bibliothèque ne devient la direction artistique par défaut.

Le Design Read doit aussi auditer explicitement les réflexes visuels qui donnent un rendu « AI generated » : hero centré générique, dégradé violet décoratif, cartes répétitives de type shadcn, glassmorphism, icônes Lucide utilisées comme langage visuel et layout SaaS par défaut. Ces motifs sont refusés par défaut ; s'ils sont conservés pour une raison fonctionnelle ou de marque, la justification et la preuve d'usage doivent être documentées.

Chaque rôle reçoit le même dossier d'entrée : objectif de conversion, public, doute principal, preuves, MASTER, références du domaine, canon, registre d'assets, contraintes de marque, stack envisagée et critères d'acceptation. Il rend ses sources, ses statuts Certain/Likely/Assuming/Unknown et ses blocages.

Un rôle ne peut être marqué comme réalisé que s’il livre un document ou une note identifiable, ses sources effectivement consultées, ses décisions et ses inconnues. Si le pilote réalise un rôle séquentiellement faute de sous-agent, l’indiquer comme tel ; ne jamais le présenter comme une revue indépendante.

Brain compare les livrables, retire les contradictions et rédige le Contrat de conversion. La direction UI traduit ce contrat. Elle ne décide ni la promesse, ni les preuves, ni le CTA à sa place.

### 5. Choisir la stack et figer la boîte à outils

Lire references/stack-router.md et references/toolbox-snapshot-template.md.

- Choisir la stack selon le besoin prouvé, jamais selon une préférence décorative.
- Créer un Toolbox snapshot versionné dans le MASTER avec la stack, les versions confirmées, les polices, les licences, les composants, les médias, le mouvement, les références étudiées, les rejets et les inconnues.
- Vérifier la licence, la provenance et la compatibilité de toute ressource avant intégration.
- Les versions sont figées seulement au moment de l'installation effective de la dépendance.

Le routeur de stack est la source de vérité. Une direction fortement art-directed ne justifie pas à elle seule Next.js : Astro + TypeScript + CSS natif reste le défaut d’un site vitrine ou éditorial ; Next.js ne s’ajoute qu’avec un écosystème React existant ou un besoin serveur/CMS confirmé. Le design spécifique utilise des variables CSS ; CSS Modules ou SCSS ne sont retenus que lorsque la stack et la composition les rendent utiles.

CSS et Web Animations API sont le choix courant pour le mouvement. GSAP, ScrollTrigger, Flip, SplitText ou Lenis sont des candidats, jamais un socle automatique : documenter l’effet impossible à réaliser simplement, la valeur pour la preuve ou la conversion, le coût de performance, le fallback et le comportement réduit. Lenis ne remplace jamais le défilement natif par défaut.

Codrops peut servir de source de patterns créatifs, d'études et d'expérimentations. Les patterns sont étudiés, adaptés et attribués lorsque nécessaire ; ils ne sont pas copiés comme une bibliothèque de templates.

Three.js, React Three Fiber, Drei et GLSL ne sont admis que si la 3D ou le WebGL apporte une valeur perceptible à la compréhension, à la preuve, à l'identité ou à l'interaction. Theatre.js est réservé aux séquences complexes qui ont besoin d'un contrôle temporel ou spatial supérieur à celui de GSAP. Dans les deux cas, documenter la valeur apportée, le coût de performance, le fallback et le comportement réduit.

shadcn/ui et les autres UI kits sont des primitives fonctionnelles éventuelles pour les dialogues, menus, champs, états et accessibilité. Ils ne sont jamais le langage visuel principal ni le point de départ de la composition.

### 6. Porte de validation

Présenter une synthèse courte avec :

- le résultat visé et la conversion principale ;
- les décisions et les preuves retenues ;
- les hypothèses restantes ;
- la direction UI et la stack ;
- les trois références du domaine et les enseignements retenus ou rejetés ;
- la tranche verticale proposée ;
- les critères qui permettront de l'accepter.

Ne pas entrer en production tant que Brain ne confirme pas la cible, la preuve, l'action principale, le parcours, la direction UI, les trois références du domaine et le passage du gate anti-template. Puis s'arrêter et demander une validation explicite.

## Phase B : production

Commencer uniquement si l'utilisateur valide le MASTER ou demande sans ambiguïté de poursuivre un MASTER déjà validé.

### 1. Reprendre le contexte

- Lire le MASTER, les fichiers AGENTS.md applicables, le Contrat de conversion, les Références du domaine, le Toolbox snapshot, le canon et l'état réel du projet.
- Ne pas réinitialiser un projet existant sans autorisation.
- Conserver les choix validés. Signaler tout écart qui change le périmètre, la structure ou la conversion.
- Réutiliser les IDs et références canoniques de asset-continuity dans les composants et pages ; enregistrer les nouvelles variantes et vérifier qu'elles ne dérivent pas entre breakpoints.

### 2. Router le travail de réalisation

Lire references/site-delivery.md, sélectionner l’adaptateur de la stack validée et charger uniquement les skills compatibles. Ne pas faire entrer Svelte, React ou une bibliothèque de mouvement dans le projet uniquement parce qu’un guide de livraison les cite.

- Astro + TypeScript + CSS natif reste le défaut pour un site vitrine, un portfolio, un démonstrateur ou des pages éditoriales simples lorsque l'interactivité avancée n'est pas requise ; le choix doit être validé dans le MASTER.
- Next.js + React + TypeScript est une exception justifiée par un écosystème React existant ou un besoin serveur/CMS validé. CSS Modules ou SCSS peuvent alors porter le design spécifique avec des variables CSS.
- Ajouter un îlot Svelte seulement si une interaction améliore réellement une preuve ou la conversion.
- Choisir SvelteKit pour l'authentification, un état complexe, des étapes métier ou des formulaires serveur établis.
- Garder HTML/CSS pour un concept interne très court et le déclarer prototype non livrable.
- Ne pas mélanger React et Svelte sans besoin documenté. Ne pas importer une bibliothèque de composants comme point de départ.

Avant de construire une section, relire sa place dans le protocole `concept -> direction artistique -> composition -> typographie -> grille -> interaction -> motion language -> implémentation`. Les composants sont ensuite des conséquences locales de cette décision, pas l'unité de conception initiale.

### 3. Produire par tranche verticale

- Construire d'abord le plus court parcours qui permet au visiteur prioritaire de comprendre l'offre, vérifier une preuve et accomplir la conversion principale.
- Inclure les états vide, chargement, erreur et réussite lorsque le parcours contient des données ou une action asynchrone.
- Appliquer no-slop aux titres, boutons, formulaires, messages, métadonnées et documents. Écrire des phrases concrètes, nommer les actions et retirer les affirmations invérifiables.
- Passer le gate anti-template avant d'étendre le reste du site.

### 4. Vérifier

- Exécuter les contrôles disponibles : formatage, types, tests et build.
- Vérifier dans un vrai navigateur les largeurs utiles, le clavier, le focus, les erreurs, les liens et l'absence de débordement.
- Vérifier que le CTA principal est visible, précis, accessible et relié à une suite réellement disponible.
- Tester la compréhension de l'offre et de l'action attendue auprès de visiteurs à froid lorsque cela est possible.
- Respecter prefers-reduced-motion et éviter les mouvements sans fonction.
- Contrôler les métadonnées, la structure des titres, les libellés accessibles, les contrastes, les polices et la provenance des médias.
- Marquer clairement ce qui n'a pas pu être vérifié.

## Règles de décision

- Une préférence de style n'est pas une exigence produit.
- Une bibliothèque ne remplace pas une direction visuelle.
- Chaque lancement de site doit s'appuyer sur exactement trois références actuelles et pertinentes du domaine, documentées dans le MASTER avec leurs enseignements visuels, techniques et UX ; elles servent de matière d'analyse, pas de templates à copier.
- L'art direction précède les composants : concept, composition, typographie, grille, interaction et mouvement doivent être décidés avant le choix des primitives.
- Un rendu qui ressemble à un template généré est un défaut de direction, pas un problème que davantage de composants ou d'effets corrigera. Le gate anti-template doit nommer les motifs génériques écartés et la raison des exceptions.
- CSS natif et variables CSS sont le socle visuel. CSS Modules ou SCSS s’ajoutent seulement si la stack les rend plus lisibles ; les UI kits restent des primitives fonctionnelles.
- Toute bibliothèque de mouvement sert un motion language documenté et un effet dont la valeur ne peut pas rester simple et testable en CSS/WAAPI. Three.js, React Three Fiber, Drei, GLSL et Theatre.js exigent une valeur démontrée et un fallback.
- Une animation guide, explique ou confirme.
- Une conversion relationnelle facilite le passage à l'échange. Elle ne crée pas de pression artificielle.
- Une preuve est utilisable seulement si son origine, son statut et son droit d'usage sont connus.
- Un CTA concurrent est admis seulement s'il sert un parcours secondaire réellement distinct.
- Une table est réservée aux données réellement tabulaires.
- Une dépendance externe a une raison, une licence compatible et un plan de maintenance.
- Une affirmation marketing est prouvable ou reformulée.

## Compte rendu final

Commencer par le résultat obtenu. Donner ensuite les fichiers importants, les vérifications exécutées, les limites connues et une seule prochaine action utile. Ne pas annoncer une réussite que les preuves disponibles ne soutiennent pas.
