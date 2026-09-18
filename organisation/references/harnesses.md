# Profils de harnais par rôle

Un harnais est l'ensemble formé par le contexte, le plan, les outils, les boucles de contrôle et le format de restitution. L'adapter à la tâche et au rôle ; ne pas transformer ces profils en identifiants de modèles.

## Gestion commune du contexte

1. Conserver les instructions applicables, décisions canoniques, critères d'acceptation, état réel et preuves encore valides.
2. Éliminer d'abord par règles déterministes les doublons, sorties anciennes, logs sans rapport, artefacts générés et détails hors périmètre.
3. Résumer seulement lorsque le contexte utile reste volumineux. Marquer ce qui a été omis et ne pas prétendre avoir conservé une preuve qui n'est plus accessible.
4. Après une modification importante, recharger l'état pertinent au lieu de raisonner sur un ancien résumé.

## Profils

| Rôle | Plan | Outils et action | Contexte | Arrêt et restitution |
| --- | --- | --- | --- | --- |
| LUNA | Aucun plan visible pour une tâche triviale ; courte checklist pour un lot répétitif. | Outils structurés et opérations bornées ; éviter les permissions larges. | Entrées minimales et format attendu. | S'arrêter dès que le lot est contrôlé ; signaler les éléments rejetés ou ambigus. |
| TERRA | Plan explicite avec dépendances, livrables et critères d'acceptation. | Lecture, comparaison, backlog et coordination ; ne pas produire du code par défaut. | Décisions, contraintes, capacité réelle des exécutants. | Restituer ordre, dépendances, inconnues et prochain gate. |
| SOL | Plan court orienté reproduction, modification et vérification ; approfondir seulement si le diagnostic l'exige. | Terminal et outils techniques minimaux suffisants ; préférer les contrôles reproductibles. | Fichiers concernés, erreurs, tests, configuration et diff utile. | Ne pas déclarer terminé sans preuves d'exécution ; lister les tests non exécutés. |
| ASTRA | Questions décisionnelles, options, conséquences et seuil de décision ; pas de cérémonie si l'arbitrage est simple. | Lecture, synthèse critique et vérification indépendante lorsque disponible. | Résumé nettoyé, preuves contradictoires, risques et décisions irréversibles. | Décision ou condition d'arrêt claire ; ne pas refaire le travail de SOL ou TERRA. |

## Adapter sans suréquiper

- Un modèle ou agent plus capable ne justifie pas davantage de contexte ni davantage d'outils.
- Un modèle moins autonome peut recevoir un plan plus explicite et des outils bornés.
- Pour un agent compétent avec le terminal, préférer une interface simple si les tests montrent qu'elle réduit le coût sans diminuer la réussite.
- Tester séparément planification, outils et gestion du contexte ; ne pas attribuer un gain à l'ensemble si un seul composant a changé.
