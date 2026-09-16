# Routage, capacités et escalade

## Choisir selon le travail à accomplir

| Situation | Rôle principal | Passage utile seulement si nécessaire |
| --- | --- | --- |
| Faute, extraction, classement ou formatage | LUNA | Répondre directement ; aucun plan, Business ou délégation de routine. |
| Backlog, priorités, dépendances, critères d'acceptation | TERRA | SOL pour une incertitude de faisabilité déterminante. |
| Bug, code, tests, intégration | SOL | TERRA si le découpage est substantiel ; ASTRA seulement si une décision critique apparaît. |
| Architecture majeure, stratégie, arbitrage très incertain | ASTRA | Expertise spécialisée vérifiée, dont New Pro Brain s'il existe ; SOL pour des preuves techniques. |
| Nouveau produit payant | TERRA pour cadrer | Business avant réalisation importante ; ASTRA pour les arbitrages qui le justifient, SOL ensuite dans le périmètre autorisé. |
| Audit économique d'un produit existant | Business si disponible | Rôle TERRA pour organiser les éléments ; ASTRA si l'arbitrage est critique. Préserver l'historique. |

Ne pas imposer une succession LUNA → TERRA → SOL → ASTRA. Le rôle principal peut suffire. La validation ordinaire reste au niveau adapté à la tâche ; ASTRA n'est pas une étape systématique.

## Vérifier ce que l'hôte permet

1. Lire les outils et capacités de la session. Distinguer disponibilité des sous-agents, choix du modèle et réglage de l'effort : une capacité ne prouve pas les autres.
2. Si un choix de modèle apporte un bénéfice réel, vérifier les identifiants et efforts acceptés auprès du catalogue ou de l'outil réellement disponible. Les noms LUNA, TERRA, SOL, ASTRA ne prouvent aucune correspondance ; ne jamais inventer un identifiant ou une option.
3. Ne pas modifier le modèle par défaut ni la configuration globale pour effectuer le routage. `agents/openai.yaml` décrit l'interface et l'invocation du skill ; il ne lance ni ne sélectionne aucun modèle.
4. Si les sous-agents ou le changement de modèle ne sont pas disponibles ou autorisés, travailler avec l'agent actuel en adoptant successivement les rôles utiles. Le signaler brièvement lorsqu'un parcours devait bénéficier de ces capacités. Une auto-vérification ne devient pas une revue indépendante.

## Déléguer seulement un travail indépendant

Un agent par défaut, au plus deux délégués actifs simultanément. Avant de déléguer, établir que le gain justifie le coût et que le mandat peut progresser indépendamment. Donner à chaque agent : résultat attendu, entrées minimales, critères d'acceptation, périmètre de fichiers, autorisations et contrôles attendus. Lui interdire de créer d'autres sous-agents ; lui signaler que d'autres agents travaillent et qu'il doit préserver leurs modifications.

Aucune écriture concurrente dans les mêmes fichiers. Préférer une revue en lecture seule ou des propriétaires de fichiers distincts. Organisation reste responsable de l'intégration, de la résolution des divergences et de la vérification de l'ensemble ; ne pas consommer tout l'effort dans la délégation.

Chaque restitution indique : actions réellement faites, fichiers touchés, preuves et commandes exécutées, limites, décisions attendues. Annoncer une revue indépendante ou plusieurs modèles uniquement lorsque cela a réellement eu lieu.

## Diagnostiquer avant d'escalader

Après un échec, examiner le symptôme, les entrées, les preuves, les permissions et la reproductibilité. Distinguer bug local, contexte manquant, capacité indisponible et décision d'architecture. Ne pas augmenter automatiquement modèle, effort, nombre d'agents ou périmètre.

Escalader uniquement quand le diagnostic révèle une incertitude ou une conséquence justifiant le rôle supérieur. Réutiliser les preuves encore valides en précisant ce qu'elles couvrent ; invalider celles que les changements rendent caduques. En cas de blocage d'autorisation, respecter les protections et présenter l'action précise nécessaire.
