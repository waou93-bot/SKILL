# Passage à grande échelle

## Capacité et architecture
La demande « à grande échelle » signifie une orchestration de lots et éventuellement plusieurs sites; elle ne définit ni un nombre d'articles, ni un budget illimité, ni une autorisation de publier. Recueillir les nombres cibles de sites et de contenus/mois, les CMS, budgets/devise, la capacité de revue et le délai souhaité. Avancer avec un plan provisoire si ces paramètres manquent.

Pipeline par site et version: découverte → audit → opportunité → arbitrage create/update → brief → rédaction → vérification → brouillon → publication autorisée → mesure → amélioration. Chaque étape réutilise ses artefacts et ses preuves; les entrées inchangées n'exigent pas un nouveau crawl. Les sources fraîches ou sujets sensibles peuvent exiger une nouvelle vérification. Prioriser la mise à jour et éviter les pages déclinées sans besoin distinct, notamment par ville.

Production permanente: ordonnanceur, base transactionnelle, file de messages, workers isolés, stockage de versions, coffre de secrets, adaptateurs CMS/fournisseurs et télémétrie. Au minimum: quotas globaux, par site et fournisseur, verrou par article, clés stables, réconciliation des résultats ambigus, dead-letter queue, pause par site et arrêt global. Dimensionner concurrence sur quotas réellement mesurés. Un connecteur exposé dans une session n'est pas une API serveur utilisable par un worker permanent. Ne pas proposer un worker fictif qui appelle ces outils hors session.

Le script fourni est une file sur une machine unique, sans services ni bibliothèques externes. Il ne fournit pas une infrastructure distribuée ni des workers de génération. Pour un déploiement réel, remplacer cette persistence par une base transactionnelle et intégrer les services effectivement autorisés. Présenter le plan et les dépendances, puis implémenter selon l'environnement choisi; ne pas déclarer l'automatisation active tant que les workers et l'ordonnanceur ne fonctionnent pas.

## File locale exécutable
Node 18+. État de travail dans un répertoire protégé choisi par l'utilisateur, jamais dans le dossier installé du skill. Les tâches contiennent seulement des références d'artefacts, aucune donnée sensible ni secret. Un bail expiré devient needs_reconciliation: l'expiration ne prouve pas que l'action distante n'a pas eu lieu. Ne pas relancer automatiquement.

Commandes (arguments de chemins à adapter):

```text
node scripts/queue.cjs init work/queue.json examples/ScaleConfig.json
node scripts/queue.cjs enqueue work/queue.json work/jobs.json
node scripts/queue.cjs claim work/queue.json worker-1
node scripts/queue.cjs finish work/queue.json JOB_ID LEASE_TOKEN done
node scripts/queue.cjs finish work/queue.json JOB_ID LEASE_TOKEN blocked
node scripts/queue.cjs reconcile work/queue.json JOB_ID done CONFIRMATION_NON_SECRETE
node scripts/queue.cjs reconcile work/queue.json JOB_ID queued PREUVE_DE_NON_EXECUTION
node scripts/queue.cjs pause work/queue.json site-a
node scripts/queue.cjs resume work/queue.json site-a
node scripts/queue.cjs pause work/queue.json all
node scripts/queue.cjs status work/queue.json
```

Les IDs retournés sont à réutiliser. jobs.json est une liste de QueueJob conforme au schéma; enqueue est idempotent pour site/action/article/version. Une même identité avec un autre paquet échoue. claim retourne au plus une tâche et un jeton de bail. Les limites de concurrence globales et par site sont appliquées sous verrou. Coût estimé réservé par site/mois; il ne remplace pas la facturation ni le suivi des coûts réels. Les jobs sans coûts fiables ne sont pas admissibles à une exécution budgétée.

publish nécessite mode automatic explicitement défini ou review, authorization_reference, validated_version identique et validation_passed; une tâche sensible nécessite qualified_approval. Cette porte logicielle vérifie les attestations du worker, pas la véracité de son autorisation ou de son rapport: le worker doit charger le rapport et l'autorisation protégés. draft refuse publish. Le script ne contacte aucun CMS. L'agent reste responsable de vérifier les limites exactes de l'autorisation avant mutation.

Journal dans l'état, sans erreurs brutes ni contenu. Reprise conservatrice après corruption: arrêt, ne pas réinitialiser. Verrou restant après crash: processus arrêté à confirmer avant retrait manuel du seul fichier .lock correspondant. État enregistré par remplacement atomique; ne pas mettre la file sur un partage réseau, plusieurs hôtes ou un système ne garantissant pas cette opération. Conserver sauvegardes et permissions OS. Les tâches dans needs_reconciliation requièrent décision explicite et preuve avant requeue; max_attempts borne leurs prises en charge.

## Pilotage
Suivre coût par contenu validé, débit réellement terminé, taux de défauts, baux ambigus, erreurs CMS, latence, cannibalisation et résultats métier. Déclencher une pause si les budgets/quotas sont atteints, les vérifications indisponibles ou le taux de défauts dépasse le seuil configuré du moteur réel. Lancer un pilote limité, observer, puis augmenter la capacité sans réduire les contrôles. L'utilité et les preuves restent des conditions de publication, quel que soit le volume.
