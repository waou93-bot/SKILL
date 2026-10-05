# Contrat de complétion et validation proportionnelle

## Quand l'appliquer

Appliquer ce contrat aux audits, revues de plusieurs fichiers, changements de code ou configuration, tâches multi-étapes, délégations et livrables destinés à être exécutés ou transmis. Pour une question simple ou une correction triviale, rester direct.

## Registre de couverture

Avant de conclure, comparer le périmètre demandé avec les éléments réellement traités. La restitution doit permettre de distinguer preuve et déclaration :

| Champ | Contenu attendu |
| --- | --- |
| Demandé | Livrables, fichiers, systèmes ou décisions explicitement couverts par la demande. |
| Réalisé | Actions et éléments effectivement lus, créés, modifiés ou comparés. |
| Vérifié | Contrôles réellement exécutés, résultat observable et portée de chaque preuve. |
| Non vérifié | Éléments omis, inaccessibles, périmés, non reproductibles ou seulement supposés. |
| Statut | `COMPLET`, `PARTIEL` ou `BLOQUE`, avec une raison si autre que `COMPLET`. |

Ne jamais déduire une couverture complète du seul fait qu'un sous-agent ou un outil annonce avoir terminé. Pour une revue exhaustive, tenir une liste des fichiers ou éléments attendus et la rapprocher des lectures effectivement observées.

## Niveaux de validation

| Risque d'une fausse réussite | Validation minimale |
| --- | --- |
| Faible | Relecture ciblée ou contrôle déterministe simple. |
| Modéré | Tests ou comparaison reproductible, inspection du diff et critères d'acceptation. |
| Élevé | Vérificateur indépendant ou contrôle en lecture seule séparé, plus preuves déterministes disponibles. |
| Critique | Arrêt avant libération si les preuves nécessaires manquent ; arbitrage humain ou ASTRA si la décision est stratégique. |

Évaluer le risque selon l'impact, la réversibilité, l'exposition externe et la difficulté pour l'utilisateur de détecter l'erreur. Ne pas appeler ASTRA lorsque des tests déterministes suffisent. Un vérificateur peut produire de faux refus : enregistrer séparément erreurs acceptées et résultats corrects bloqués.

## Conditions de sortie

- `COMPLET` : tous les critères d'acceptation applicables sont couverts par des preuves actuelles.
- `PARTIEL` : une partie utile est livrée, mais le périmètre ou les contrôles restent incomplets ; nommer exactement ce qui manque.
- `BLOQUE` : une permission, une entrée, une capacité ou une décision indispensable manque ; indiquer l'action minimale qui débloque.

Une sortie concise reste possible. Le contrat impose la véracité et la couverture, pas un long rapport.
