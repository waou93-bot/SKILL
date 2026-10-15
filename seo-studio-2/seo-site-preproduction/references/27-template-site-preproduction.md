# Préproduction de site depuis un template : contrat SEO Studio 2

## Règle d'adaptation

Le site Repère Salon fourni avec `seo-site-preproduction` illustre une organisation de comparateur éditorial. Les canapés, produits Ligne A/B/C, mesures, catégories, palette, outil de largeur, prose et mentions commerciales sont des exemples fictifs. Pour chaque mission, faire de la niche demandée, de son audience et de la tâche visiteur la source de vérité. Réutiliser un motif uniquement s'il est utile et vérifiable dans ce nouveau contexte. Ne pas remplacer le nom du produit à la chaîne.

## Déclencheur pour création et reprise

Pour une création, une reprise ou une refonte qui touche l'architecture, l'expérience, les contenus ou la conversion, charger `seo-site-preproduction` et appliquer cette évaluation dans la première phase G2/G3 concernée. La règle vaut aussi pour un site existant : l'ancienneté du dossier et la conservation d'un design ou d'une architecture ne dispensent pas de vérifier l'adéquation du modèle.

En reprise ciblée, examiner l'évaluation précédente et ses preuves. La garder si la niche, l'audience, les tâches, le modèle économique et les pages existantes correspondent encore au périmètre. Sinon, rouvrir la première phase impactée et mettre à jour les artefacts touchés. Une retouche qui ne modifie aucun de ces éléments peut réutiliser l'évaluation courante, avec son lien et ses preuves. Ne pas réinitialiser le projet ni rejouer les phases intactes.

Tous les types de site doivent consigner l'applicabilité du template dans R29. Si le projet n'est pas éditorial, comparateur, média, affilié ou content-led, indiquer précisément pourquoi les motifs ne conviennent pas et lesquels, le cas échéant, restent utiles. Une exclusion motivée est une décision ; une omission ne l'est pas.

## Usage pendant G2–G5

- **G2, architecture :** utiliser `references/preproduction-map.md` comme grille de décision. Dans `03_ARCHITECTURE.md`, consigner la source/version du modèle examiné, son applicabilité à la niche, au public, aux tâches et à l'existant, les motifs conservés/adaptés/écartés, et les preuves ainsi que les impacts de reprise. Puis documenter types de pages retenus/rejetés, intentions et tâches, URLs/indexation, taxonomie, navigation, propriétaires des réponses, liens entrants/sortants et critères de maintenance.
- **G3, expérience et éditorial :** dans `04_DESIGN.md` et `PROJECT_SKIN.yaml`, spécifier une direction propre au domaine, les motifs d'interface retenus ou exclus, les gabarits, le responsive, les composants, états, accessibilité, assets autorisés, motion et contrôles. Dans `05_CONTENU.md`, `BRIEFS/` et `PILOTES/`, décrire voix, structure, preuves, objections, limites, vocabulaire et CTA de l'audience.
- **G4, réalisation planifiée :** inscrire dans `07_TECHNIQUE.md` les dépendances des outils, filtres, recherche et données; placer les objectifs et accès réellement disponibles dans `08_MESURE.md`. Ne déclarer aucune capacité ou vérification avant son exécution.
- **G5, transfert :** consigner objections et adaptations dans `10_DECISIONS.md`; lier les preuves et contrôles en `11_QA.md`; documenter manques, propriétaires et portes restantes en `12_HANDOFF.md`.

Ces fichiers restent ceux du dossier Studio existant. R29 et ses preuves se lient aux artefacts et aux gates Studio déjà définis ; ne pas créer une seconde architecture, un deuxième `PROJECT_SKIN`, des registres concurrents ou des portes supplémentaires. Conserver les autres gates Studio, notamment validation de design, preuves de partenaires, formation, revues et autorisation de publier.

## Logique de page à décider, jamais recopier par défaut

Le projet de démonstration comprend accueil/outil, catégorie, guide, fiche modèle et méthode. Pour le projet demandé, retenir seulement les formes de réponse utiles : accueil d'orientation, hub thématique, comparaison, guide pratique, fiche détaillée, méthode/provenance ou autre type dicté par la niche. Attribuer à chaque page une réponse originale, une preuve, une limite, un lien utile et une prochaine action. Exclure toute page qui ne satisfait pas une intention ou tâche distincte; ne pas indexer des facettes sans contenu utile autonome.

## Prose et conversion

Faire suivre la page du cheminement du lecteur : question concrète, réponse utile, comparaison fondée sur des preuves, limites/inconnues et prochaine action. Réécrire ce cheminement pour les codes et décisions de la niche et appliquer le vrai skill `redaction-editoriale-web`. Afficher les faits, sources et dates de vérification disponibles; sinon noter le champ à compléter. Ne pas inventer un test, avis, prix, résultat, expertise, offre, partenaire ou urgence. Relier le CTA au modèle économique confirmé dans `06_PARTENAIRES.md`; ne pas hériter par défaut des boutons affiliés du modèle.
