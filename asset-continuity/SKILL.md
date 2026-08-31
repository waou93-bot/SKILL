---
name: asset-continuity
description: Garantit la cohérence et la continuité d'une série d'images, vidéos, modèles 3D, interfaces, slides et autres assets liés. Utiliser ce skill dès qu'un sujet, un style, une marque, un décor, un objet ou un état doit rester reconnaissable entre plusieurs fichiers, versions, scènes ou médias, ainsi que pour auditer ou reprendre les assets d'un projet existant. Ne pas l'activer pour un livrable isolé sans élément récurrent.
---

# Asset Continuity

Préserve l'identité du projet pendant la création, la révision et la conversion entre médias. La continuité porte autant sur les fichiers et leur provenance que sur leur contenu visuel ou sonore.

## Contrat de continuité

Avant toute production en série, identifie les éléments récurrents et crée un pack de continuité. Utilise le dossier `MASTER/CONTINUITY/` quand un `MASTER` existe ; sinon crée `CONTINUITY/` à la racine du livrable. Pour un projet ancien, inventorie l'existant sans déplacer, renommer ni remplacer les originaux. Une référence ne devient canonique qu'après inspection.

Le pack minimal contient :

- `ASSET_REGISTRY.md` — ID stable, rôle, type, chemin, version, statut, source ou licence et dépendances ;
- `CANON.md` — invariants, variantes autorisées, références canoniques et éléments interdits ;
- `STATE_LEDGER.md` — état initial, changements intentionnels, moment ou livrable concerné et état résultant ;
- `QA_CONTINUITY.md` — périmètre inspecté, écarts, corrections, preuves et statut.

Lis [references/continuity-pack.md](references/continuity-pack.md) lorsque tu dois créer ou réparer ce pack. Réutilise un registre compatible déjà présent au lieu de dupliquer les mêmes informations.

## Hiérarchie des sources

Résous les conflits dans cet ordre : demande explicite la plus récente de l'utilisateur, référence canonique approuvée, brief ou bible verrouillée, registre d'état, asset dérivé. Une sortie générée ne redéfinit jamais silencieusement le canon.

Sépare systématiquement :

- les **invariants** qui définissent l'identité ;
- les **variables de scène** comme pose, cadrage, expression, lumière ou format ;
- les **changements d'état autorisés** comme blessure, usure, météo, version de produit ou évolution de costume ;
- les **inconnues**, qui restent marquées comme telles plutôt que transformées en détails inventés.

Si deux références se contredisent, choisis ou demande un arbitrage seulement si le conflit change matériellement le résultat. Consigne la décision et conserve l'ancienne version.

## Production

1. Attribue un ID stable à chaque entité récurrente et à chaque asset canonique.
2. Verrouille d'abord les références maîtres : identité, proportions, palette, matériaux, typographie, logo, architecture, voix ou autre signature pertinente.
3. Compose chaque nouvelle génération avec un **socle canonique** inchangé puis un **delta local** limité à la scène ou au format. Ne recopie pas au hasard une description différente à chaque prompt.
4. Fournis aux outils et agents parallèles le même extrait canonique, les mêmes références et l'état d'entrée attendu. Un asset dérivé n'a pas le droit d'inventer une nouvelle version du sujet.
5. Enregistre le fichier produit, sa version, ses références sources, ses paramètres réutilisables quand ils existent et les changements d'état qu'il introduit.

Une graine, une image précédente ou un prompt très insistant ne suffit pas à garantir la continuité. Préfère les références canoniques directes. N'utilise pas uniquement le dernier asset produit comme référence : cela accumule la dérive. Pour une série longue, compare régulièrement au canon et à un voisin logique.

## Contrôle qualité

Vérifie les assets dans leur contexte réel, pas seulement isolément. Pour une série visuelle, crée ou inspecte une planche-contact représentative ; pour une séquence, compare aussi les voisins avant/après ; pour la 3D, inspecte les vues de référence et des angles d'orbite ; pour l'audio, compare voix, niveau, spatialisation et traitement ; pour une interface ou un deck, compare les composants répétés, tokens, grilles et styles typographiques.

Contrôle au minimum :

- identité, silhouette, proportions, orientation et nombre d'éléments ;
- couleurs, matériaux, texture, lumière et langage graphique ;
- logo, typographie, iconographie, dimensions, formats et transparence ;
- position, échelle, architecture, chronologie et changements d'état ;
- noms, versions, provenance, licences, liens rompus et doublons.

Classe chaque écart `BLOCKER`, `MAJEUR` ou `MINEUR`. Corrige d'abord la source la plus amont, propage la modification aux dérivés touchés, puis régénère ou remplace uniquement ce qui est nécessaire. Ne marque `PASS` que si les assets inspectés respectent le canon ou si les écarts intentionnels sont enregistrés.

## Reprise d'un projet existant

Commence par un audit en lecture seule : inventaire, regroupement des quasi-doublons, détection des contradictions et proposition des candidats canoniques. Préserve les chemins utilisés par le projet. Ajoute le pack de continuité sans réécrire l'historique, puis relie progressivement les assets actifs à leurs IDs stables. Toute migration destructive, suppression de doublon ou réécriture massive exige une autorisation distincte.

## Livraison

Indique les références canoniques retenues, les assets créés ou corrigés, les écarts encore ouverts et le statut du contrôle. Ne prétends pas qu'une série est cohérente si elle n'a pas été comparée aux sources de vérité et inspectée dans son contexte.
