---
name: human
description: Audit visuel anti-artefact pour images, rendus, captures, sites et séries générées. Utilise ce skill dès qu’une image paraît « trop IA », artificielle, plastique, incohérente, sans âme, ou qu’un utilisateur demande un contrôle humain, une recherche d’artefacts ou une correction de réalisme. Inspecte les pixels dans leur contexte réel, classe chaque anomalie, propose la correction minimale et ne valide jamais une image sur le seul mot « photoréaliste ».
---

# Human — contrôle anti-artefact

Ce skill sépare le goût d’un défaut observable. Il sert à repérer ce qui trahit une image générée et à proposer une correction limitée, vérifiable et compatible avec la série.

## Déclencheurs

Utilise ce skill quand la demande contient ou implique :

- « trop IA », « artificiel », « plastique », « faux », « sans âme », « uncanny » ou « pas humain » ;
- contrôle d’une image, d’un rendu, d’une capture ou d’une série avant publication ;
- recherche d’artefacts, de détails impossibles ou de corrections de réalisme ;
- comparaison avant/après d’une génération ou d’une retouche.

## Orchestration

Active les compétences adaptées, sans les confondre :

1. `brain` vérifie les prémisses, distingue fait observé et préférence et attaque la conclusion.
2. `asset-continuity` verrouille les invariants, les références, les versions et les dérivés.
3. `human-reading` contrôle la lisibilité et le contexte d’affichage pour les pages, captures et documents.
4. `imagegen` intervient seulement pour générer ou éditer une image après le diagnostic.
5. `no-slop` s’applique à tout rapport, alt text, prompt ou recommandation écrite.

Ne demande pas une validation d’architecte ou de métier si le problème est seulement photographique. Inversement, ne transforme pas un défaut spatial ou réglementaire en simple défaut de réalisme.

## Procédure

### 1. Inventorier avant de juger

- Identifie le fichier, son rôle, sa version, sa taille d’affichage et son statut (source, dérivé, actif, historique).
- Charge l’image locale avec `view_image` avant toute édition.
- Inspecte l’image seule à résolution lisible, puis dans la page ou la planche où elle sera vue.
- Retrouve la référence canonique, les invariants et le voisin de série avant de proposer une modification.

### 2. Scanner les zones à risque

Inspecte chaque image selon ces familles. Note la zone précise (haut gauche, baie droite, main au premier plan, etc.) et le niveau de confiance.

| Famille | Signaux à rechercher |
|---|---|
| Géométrie | lignes qui se tordent, angles qui changent, portes ou fenêtres impossibles, escaliers discontinus, objets fusionnés |
| Anatomie | doigts en trop, mains fondues, articulations impossibles, silhouettes sans poids, visages déformés |
| Matériaux | bois sans fil cohérent, pierre liquide, métal sans reflet, verre opaque ou reflets contradictoires, répétitions de texture |
| Physique | ombres incompatibles, objets en lévitation, eau sans horizon ou sans contact, pluie qui ne mouille rien, végétation figée |
| Lumière | sources multiples non justifiées, température incohérente, halos numériques, profondeur atmosphérique plate |
| Usage | objets décoratifs sans fonction, gestes posés, scène trop vide, absence de traces, répétition d’un même personnage ou accessoire |
| Image | netteté artificielle, bokeh uniforme, sur-contraste, bruit absent, peau ou textile plastifiés, compression qui masque un défaut |
| Continuité | orientation, proportions, palette, matériaux ou saison qui dérivent d’une référence active |
| Texte | pseudo-lettres, inscriptions illisibles, logos inventés, signalétique qui doit être remplacée par du HTML |

Un détail n’est pas un artefact parce qu’il est inhabituel. Il devient artefact si sa structure, sa lumière, son usage ou sa continuité ne tiennent pas à l’inspection.

### 3. Classer les constats

Pour chaque constat, indique :

- **BLOCKER** : l’image ne peut pas être publiée (géométrie fausse, corps déformé, texte critique illisible, contradiction de canon) ;
- **MAJEUR** : le défaut attire l’œil ou change la lecture (reflet impossible, objet fusionné, lumière incohérente) ;
- **MINEUR** : défaut visible seulement en inspection rapprochée et sans effet sur la lecture principale ;
- `observé`, `probable` ou `préférence` pour séparer le pixel vérifié de l’interprétation.

Ne fournis jamais une liste d’adjectifs sans emplacement, preuve et sévérité.

### 4. Choisir la correction minimale

Décide dans cet ordre :

1. conserver si le point est une préférence et non un défaut ;
2. recadrer ou masquer si l’anomalie est périphérique ;
3. éditer localement avec `imagegen` si le sujet et les invariants peuvent rester verrouillés ;
4. régénérer l’asset si plusieurs familles sont touchées ou si une retouche locale accumulerait la dérive.

Lors d’une édition, répète les invariants dans le prompt : ce qui change, ce qui reste identique, ce qui est interdit. Ne remplace pas silencieusement un asset actif ; crée une version `-v2`, `-v3` ou un nom équivalent, conserve la source et mets à jour le registre.

### 5. Réinspecter

- Compare avant/après au même format et dans le même contexte.
- Vérifie les zones voisines : une correction locale ne doit pas déplacer une ligne, une main, une ouverture ou une source de lumière.
- Pour une série, inspecte au moins le voisin logique avant et après.
- Refuse le statut PASS si un défaut BLOCKER reste ouvert ou si la correction n’a pas été revue dans la page réelle.

## Rapport obligatoire

Utilise ce format court :

```markdown
# Human QA — [série ou asset]

PÉRIMÈTRE : [fichiers, versions, contexte d’affichage]
RÉFÉRENCE : [canon, voisin de série ou aucune]
STATUT : PASS | FIX | BLOCKED

| Sévérité | Zone | Famille | Constat observable | Confiance | Correction minimale | Statut |
|---|---|---|---|---|---|---|

## Décision
[conserver, éditer, régénérer ou demander une référence]

## Prompt ou delta de correction
[uniquement si une image doit être modifiée]
```

## Règles de langage

- Écris ce qui est visible : « le montant vertical se dédouble au tiers droit », pas « l’image manque de réalisme ».
- N’emploie pas « photoréaliste » comme preuve.
- N’invente pas une cause technique si le pixel seul ne permet pas de la connaître.
- Signale les préférences comme telles et ne les transforme pas en erreurs.
- Un asset généré reste un asset de prototype, jamais une preuve documentaire ou contractuelle.

## Gate final

Avant de livrer, réponds oui/non à chaque point :

- chaque image active a été inspectée à sa taille d’usage ;
- chaque anomalie a une zone, une famille et une sévérité ;
- les invariants de série sont inchangés ;
- les corrections sont versionnées et leurs sources conservées ;
- la page réellement servie a été revue ;
- aucun texte généré dans l’image ne remplace du texte accessible HTML ;
- le rapport sépare observation, probabilité et préférence.

Si un point est non, le statut est `FIX` ou `BLOCKED`, jamais `PASS`.
