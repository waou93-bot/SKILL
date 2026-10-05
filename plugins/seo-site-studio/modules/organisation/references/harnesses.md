# Profils de harnais par rôle

Un harnais est l'ensemble formé par le contexte, le plan, les outils, les boucles de contrôle et le format de restitution. L'adapter à la tâche et au rôle ; distinguer rôle, modèle demandé et modèle réellement exécuté ; appliquer la préférence explicite ci-dessous.

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


## Préférence explicite de modèles — 5 octobre 2026

Toujours choisir `gpt-6-luna` pour les petites tâches répétitives bornées, `gpt-6.1-sol` pour les travaux les plus difficiles (selon complexité réelle, sans quota ni majorité imposée), et `gpt-6-astra` pour l'orchestration, le découpage, les arbitrages et conflits. TERRA reste un profil de planification, sans quatrième modèle imposé. Astra attribue les tâches intermédiaires selon leur complexité et les capacités disponibles ; aucun modèle supplémentaire ni quota n’est inventé.

Vérifier les identifiants et capacités dans le catalogue réel de la session avant sélection. Lorsque les sous-agents sont autorisés, transmettre le modèle correspondant à l'outil de lancement ; ne pas se contenter de le mentionner dans le prompt. Ne pas choisir un autre modèle silencieusement. Si indisponible, annoncer la limitation et conserver la préférence dans le transfert ; continuer les actions autorisées avec l'agent actuel lorsque possible. Un chat déjà actif garde son modèle tant qu'une action réelle de l'hôte ne l'a pas changé. Les noms de rôles ne prouvent pas une sélection effective. Ne pas modifier la configuration globale pour simuler ce routage.

Un travail trivial ne demande pas une nouvelle orchestration. Si l'hôte ne peut sélectionner le modèle de ce chat, déclarer cette limite une fois ; ne pas multiplier les agents pour une correction triviale.

Chaque mandat délégué est autonome : objectif, version du mandat, livrables, dépendances, fichiers propriétaires, critères d'acceptation, preuves et sources, décisions Design DNA/No Slop avec provenance, corrections utilisateur, autorisations effectivement accordées et actions exclues. Retour : réalisé, vérifié, non vérifié, fichiers touchés, contradictions et statut. Astra arbitre les contradictions sur preuves sans élargir les permissions. Deux délégués actifs au maximum, sans descendants ni écritures concurrentes.
