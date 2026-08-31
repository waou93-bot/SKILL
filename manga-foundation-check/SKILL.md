---
name: manga-foundation-check
description: Prévient et audite les erreurs fondamentales de manga, BD, comic, webtoon et storyboard séquentiel avant génération, mise en page ou livraison. Utilise ce skill pour sécuriser la continuité, la lisibilité, le sens de lecture, le découpage, le lettrage et les exports ; il complète un workflow de création sans le remplacer.
---

# Manga Foundation Check

Agis comme un éditeur technique de bande dessinée. Détecte tôt les erreurs coûteuses, corrige-les au niveau de leur source de vérité, puis vérifie que la correction se propage au scénario, au storyboard, aux prompts, aux images, au lettrage et aux exports.

Ce skill ne choisit pas le concept artistique à la place de l'utilisateur et ne produit pas seul une œuvre complète. Il s'intègre à un studio tel que `new-manga` ou `newbd`, ou s'utilise comme audit autonome.

Quand l'œuvre contient plusieurs assets visuels liés, charge `asset-continuity` et utilise son pack comme preuve transversale. Ne duplique pas ses registres : les portes éditoriales restent dans `MASTER/QUALITY_GATES.md`, tandis que le canon, les états, les versions et les écarts d'assets restent dans `MASTER/CONTINUITY/`.

## Sources de vérité minimales

Avant la production visuelle, établis ou identifie :

- le brief verrouillé, le format, le public, la langue et le sens de lecture ;
- la bible des personnages et de leurs variantes ;
- les règles du monde, des pouvoirs et des objets importants ;
- la chronologie et la continuité des états ;
- le scénario paginé et le storyboard page par page ;
- les spécifications d'export réellement visées.
- le registre des assets, leurs IDs stables, leurs références canoniques et leurs versions lorsque `asset-continuity` s'applique.

Une information absente devient soit une décision explicite consignée, soit un blocage si l'inventer trahirait la demande. Ne présente jamais une valeur par défaut comme une contrainte fournie par l'utilisateur.

## Les quatre portes obligatoires

Applique ces portes aux productions complètes. Pour une demande partielle, n'applique que les portes concernées.

1. **Fondations** — avant les fiches finales et les pages : prémisse, causalité, objectifs, règles, pagination, sens de lecture et spécifications sont cohérents.
2. **Préproduction** — avant la génération en série : designs récurrents verrouillés, décors et objets référencés, name lisible, zones de texte prévues, tranche verticale testée.
3. **Pages** — avant le lettrage et l'assemblage : personnages, espace, action, regards, états, bulles prévues et ordre de lecture restent compréhensibles d'une case à l'autre.
4. **Livraison** — avant de déclarer le projet terminé : pages réellement présentes, ordre correct, texte relu, marges et fonds perdus adaptés à la cible, fichiers ouverts et inspectés.

Pour la checklist détaillée et les critères de chaque porte, lis [references/quality-gates.md](references/quality-gates.md). Lors d'une production de bout en bout ou d'un audit complet, ce fichier est obligatoire.

## Méthode de correction

- Classe chaque anomalie `BLOCKER`, `MAJEURE` ou `MINEURE`.
- Corrige d'abord la source la plus amont. Exemple : une tenue incohérente se corrige dans la bible et la continuité avant les prompts ou les images.
- Ne compense pas un storyboard ambigu par une consigne de génération toujours plus longue : répare le découpage.
- N'accepte pas une page parce qu'elle est belle isolément. Vérifie-la avec la page précédente et la suivante, en miniature puis à taille de lecture.
- Pour les séries visuelles, inspecte aussi une planche-contact et compare les personnages, décors et objets aux références canoniques, pas uniquement aux pages voisines.
- N'insère pas de faux texte généré dans l'image. L'art, les bulles et le lettrage restent des couches séparées autant que possible.
- Si une correction visuelle est impossible, marque précisément la page, l'impact et le travail restant. Ne qualifie pas le livrable de final.

## Rapport de porte

Consigne chaque passage dans `MASTER/QUALITY_GATES.md` ou le journal qualité existant :

```text
PORTE : Fondations | Préproduction | Pages | Livraison
STATUT : PASS | FIX | BLOCKED | N/A
PÉRIMÈTRE : chapitres, pages ou fichiers inspectés
BLOCKERS :
ANOMALIES MAJEURES :
ANOMALIES MINEURES :
CORRECTIONS APPLIQUÉES :
PREUVES INSPECTÉES :
RESTE À FAIRE :
```

`PASS` signifie qu'aucune anomalie connue ne compromet la lecture ou la livraison sur le périmètre inspecté. `FIX` signifie que des corrections sont encore nécessaires. `BLOCKED` exige une dépendance réellement manquante ; il ne sert pas à éviter une décision créative raisonnable.

## Intégration avec les studios

Avec `new-manga` ou `newbd` :

- exécute **Fondations** après le brief et la structure paginée ;
- exécute **Préproduction** sur une tranche verticale représentative avant toute génération en série ;
- exécute **Pages** après chaque lot cohérent et avant le lettrage final ;
- exécute **Livraison** après export, en inspectant les fichiers réels.

Le questionnaire initial du studio reste l'unique questionnaire. Ce skill ne crée pas un second cycle de validation utilisateur : il applique les valeurs par défaut autorisées, journalise les décisions et ne sollicite l'utilisateur que pour une inconnue réellement bloquante.
