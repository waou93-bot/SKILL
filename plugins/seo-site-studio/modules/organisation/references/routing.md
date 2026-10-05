# Routage, capacités et escalade

## Choisir selon le travail à accomplir

| Situation | Attribution |
| --- | --- |
| Petites tâches répétitives simples et bornées | Toujours Luna (`gpt-6-luna`) lorsque sélection disponible. |
| Travaux les plus difficiles : diagnostic complexe, conception délicate, réalisation ou analyse difficile | Sol 6.1 (`gpt-6.1-sol`). |
| Orchestration, découpage, intégration de branches, arbitrage et conflits | Astra (`gpt-6-astra`). |
| Tâches intermédiaires | Astra attribue selon complexité et capacités, sans modèle supplémentaire inventé ni quota. |
| Nouveau projet monétisé | Mandat économique business-checklist réellement disponible avant engagement important ; prototype expérimental autorisé possible. |

Une faute isolée reste une correction directe. Le modèle du chat actif ne change pas par déclaration ; signaler une sélection impossible sans cérémonie ni multiplication des agents.

## Vérifier ce que l'hôte permet

1. Lire les outils et capacités de la session. Distinguer disponibilité des sous-agents, choix du modèle et réglage de l'effort : une capacité ne prouve pas les autres.
2. Si un choix de modèle apporte un bénéfice réel, vérifier les identifiants et efforts acceptés auprès du catalogue ou de l'outil réellement disponible. La préférence de modèles est explicite ci-dessous ; les noms de rôles seuls ne prouvent aucune sélection effective ; ne jamais inventer un identifiant ou une option.
3. Ne pas modifier le modèle par défaut ni la configuration globale pour effectuer le routage. `agents/openai.yaml` décrit l'interface et l'invocation du skill ; il ne lance ni ne sélectionne aucun modèle.
4. Si les sous-agents ou le changement de modèle ne sont pas disponibles ou autorisés, travailler avec l'agent actuel en adoptant successivement les rôles utiles. Le signaler brièvement lorsqu'un parcours devait bénéficier de ces capacités. Une auto-vérification ne devient pas une revue indépendante.

## Évaluer la séparabilité avant de déléguer

La difficulté seule ne justifie pas plusieurs agents. Classer la tâche à partir de quatre questions :

1. Les branches peuvent-elles produire des résultats utiles sans attendre les mêmes étapes intermédiaires ?
2. Les agents peuvent-ils travailler avec des entrées stables et des périmètres de fichiers distincts ?
3. Les sorties peuvent-elles être vérifiées séparément puis intégrées par Organisation ?
4. Une branche peut-elle échouer sans invalider silencieusement le travail des autres ?

| Classe | Profil | Décision par défaut |
| --- | --- | --- |
| FAIBLE | Travail séquentiel, état partagé, mêmes fichiers ou décisions fortement couplées. | Un agent ; rôles successifs. |
| MOYENNE | Quelques branches indépendantes, mais une intégration ou décision commune reste nécessaire. | Délégation ciblée d'une branche en lecture seule ou sur fichiers distincts. |
| FORTE | Livrables indépendants, entrées stables, preuves séparables et intégration simple. | Parallélisation autorisée si l'hôte, les permissions et le coût le permettent. |

Si la classe est incertaine, commencer en mono-agent. Ne déléguer qu'après avoir isolé une branche avec un livrable et des critères d'acceptation propres. Une recherche parallèle, une inspection de composants distincts ou des évaluations indépendantes peuvent être séparables ; un correctif traversant le même état ou les mêmes fichiers ne l'est généralement pas.

## Déléguer seulement un travail indépendant

Un agent par défaut, au plus deux délégués actifs simultanément. Avant de déléguer, établir que le gain justifie le coût et que le mandat peut progresser indépendamment. Donner à chaque agent : résultat attendu, entrées minimales, critères d'acceptation, périmètre de fichiers, autorisations et contrôles attendus. Lui interdire de créer d'autres sous-agents ; lui signaler que d'autres agents travaillent et qu'il doit préserver leurs modifications.

Aucune écriture concurrente dans les mêmes fichiers. Préférer une revue en lecture seule ou des propriétaires de fichiers distincts. Organisation reste responsable de l'intégration, de la résolution des divergences et de la vérification de l'ensemble ; ne pas consommer tout l'effort dans la délégation.

Chaque restitution applique le contrat de complétion : actions réellement faites, fichiers touchés, preuves et commandes exécutées, limites, statut et décisions attendues. Annoncer une revue indépendante ou plusieurs modèles uniquement lorsque cela a réellement eu lieu.

## Diagnostiquer avant d'escalader

Après un échec, examiner le symptôme, les entrées, les preuves, les permissions et la reproductibilité. Distinguer bug local, contexte manquant, capacité indisponible et décision d'architecture. Ne pas augmenter automatiquement modèle, effort, nombre d'agents ou périmètre.

Escalader uniquement quand le diagnostic révèle une incertitude ou une conséquence justifiant le rôle supérieur. Réutiliser les preuves encore valides en précisant ce qu'elles couvrent ; invalider celles que les changements rendent caduques. En cas de blocage d'autorisation, respecter les protections et présenter l'action précise nécessaire.


## Préférence explicite de modèles — 5 octobre 2026

Toujours choisir `gpt-6-luna` pour les petites tâches répétitives bornées, `gpt-6.1-sol` pour les travaux les plus difficiles (selon complexité réelle, sans quota ni majorité imposée), et `gpt-6-astra` pour l'orchestration, le découpage, les arbitrages et conflits. TERRA reste un profil de planification, sans quatrième modèle imposé. Astra attribue les tâches intermédiaires selon leur complexité et les capacités disponibles ; aucun modèle supplémentaire ni quota n’est inventé.

Vérifier les identifiants et capacités dans le catalogue réel de la session avant sélection. Lorsque les sous-agents sont autorisés, transmettre le modèle correspondant à l'outil de lancement ; ne pas se contenter de le mentionner dans le prompt. Ne pas choisir un autre modèle silencieusement. Si indisponible, annoncer la limitation et conserver la préférence dans le transfert ; continuer les actions autorisées avec l'agent actuel lorsque possible. Un chat déjà actif garde son modèle tant qu'une action réelle de l'hôte ne l'a pas changé. Les noms de rôles ne prouvent pas une sélection effective. Ne pas modifier la configuration globale pour simuler ce routage.

Un travail trivial ne demande pas une nouvelle orchestration. Si l'hôte ne peut sélectionner le modèle de ce chat, déclarer cette limite une fois ; ne pas multiplier les agents pour une correction triviale.

Chaque mandat délégué est autonome : objectif, version du mandat, livrables, dépendances, fichiers propriétaires, critères d'acceptation, preuves et sources, décisions Design DNA/No Slop avec provenance, corrections utilisateur, autorisations effectivement accordées et actions exclues. Retour : réalisé, vérifié, non vérifié, fichiers touchés, contradictions et statut. Astra arbitre les contradictions sur preuves sans élargir les permissions. Deux délégués actifs au maximum, sans descendants ni écritures concurrentes.
