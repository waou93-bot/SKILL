# Gates : décision, état technique et autorisation séparés

Ce cadre est une méthode proposée pour ce skill, pas un barème de Google.

## Quatre gates d'investissement

G1 — Demande/objectif : public, intention, résultats observés et action utile existent
ou peuvent être testés. Une requête générique populaire ne suffit pas.

G2 — Capacité de réponse : offre/page utile, preuve propre, moyens éditoriaux et
techniques disponibles. Le plan n'est pas fondé sur des milliers de pages invérifiables.

G3 — Économie/mesure : coût complet, fenêtre d'observation, chemin vers l'objectif,
mesure minimale et plafond de perte. Si monétisation, lien avec Business sans doublon.

G4 — Livraison sûre : aucun blocage critique connu sur le périmètre du prochain test,
préservation de l'existant, permissions, critères d'acceptation et rollback si nécessaire.

Pour chaque gate : OBSERVE, HYPOTHESE, ECHEC, INCONNU ou NON_APPLICABLE ; lier
preuves et inconnues. Aucun total de points n'efface un ECHEC critique.

## Décisions de canal

A_EVALUER : cadrage/étude incomplète, pas encore de recommandation.
PILOTE : engager uniquement l'expérience définie ; résultats non validés.
PRIORITAIRE : données projet pertinentes soutenant l'objectif, mesure contrôlée,
coût soutenable, contre-analyse et périmètre documentés. L'observation de croissance
seule ne prouve pas toute la causalité ni l'avenir.
SECONDAIRE : présence/recherche utile mais acquisition principale ailleurs ou limitée.
NON_PRIORITAIRE : coût, intention, délai ou capacité défavorables dans cette version ;
justifier et donner conditions de réouverture, sans condamner le projet entier.
BLOQUE_DONNEES : une donnée décisive manque ; indiquer comment l'obtenir.

Sur la seule documentation, PILOTE/SECONDAIRE/NON_PRIORITAIRE sont possibles ;
PRIORITAIRE exige des observations du projet utiles à son objectif, pas juste des
volumes de mots-clés. Le sponsor peut choisir un pari stratégique ; l'enregistrer
comme tel sans falsifier le statut des preuves.

## État technique indépendant

NON_AUDITE : aucune vérification du site ; fréquent avant existence d'un domaine.
PARTIEL : couverture limitée ou contrôles critiques non terminés.
BLOQUANT : défaut établi bloquant le prochain périmètre ; le reste peut avancer.
PRET_POUR_TEST : contrôles critiques du seul périmètre pilote terminés, sans défaut
critique connu. N'implique ni audit exhaustif, ni indexation, ni bon classement.

Un canal PRIORITAIRE peut être momentanément BLOQUANT. La combinaison doit empêcher
le déploiement du périmètre défectueux, pas faire disparaître sa valeur stratégique.

## Permissions

`granted_actions` contient seulement les actions explicitement autorisées par le
porteur et `evidence` leur trace. Rapport par défaut ; code, publication, déploiement,
robots, suppression, suivi distant, achat et prise de contact sont séparés.
`next_action_ids` désigne des tâches du backlog ; toute tâche sélectionnée doit
avoir les permissions correspondant à ses `required_permissions`.

Le contrôle JSON fourni détecte certaines incohérences ; il ne peut pas confirmer
que la trace de permission est authentique ni que le diagnostic est vrai. Le routeur
et l'agent doivent le vérifier avant action. Un fichier valide n'est pas une autorisation.

## Pilote et règle d'arrêt

Choisir quelques pages/intentions avec hypothèse, baseline, metric/dénominateur,
limite de coût, horizon, seuils contextualisés et facteurs perturbateurs. Préciser
ce qui ferait continuer, corriger, arrêter ou conclure NON_CONCLUANT.

Ne pas exiger de résultats SEO immédiats ni attendre indéfiniment : borner le prochain
engagement. Un échec après un vrai test renseigne une version de la stratégie, pas
la validité éternelle du SEO. Aucun test utilisateur simulé par IA n'est une observation.

## Revue et transmission

Organisation arbitre ; Luna collecte, Terra planifie, Sol vérifie/implémente,
Astra intervient pour arbitrage majeur. Pas de délégation prétendue. Une revue
mono-agent n'est pas indépendante ; une validation indépendante demandée mais
indisponible reste à réaliser. Mettre les résultats et les limites dans le handoff.

## Contrat du contrôleur de handoff

`assets/09-handoff.json` est un TEMPLATE, pas un dossier de résultat. Lors d’une
exécution réelle, conserver les champs, définir `kind: HANDOFF`, remplir les identifiants,
la date et les preuves. `evidence_basis` : DOCUMENTAIRE, OBSERVATIONS_PROJET ou MIXTE.
Chaque tâche doit avoir `id`, `action`, `required_permissions`, `dependencies`,
`cash_cost` (EUR décaissés, null si inconnu) et `status` (DONE si déjà terminée).
Actions du contrôleur : analysis, write_report, edit_code, publish, deploy,
edit_robots, delete_content, spend, outreach, install_tracking. La permission de
l’action doit figurer dans required_permissions. Une proposition peut exister
sans permission ; les next_action_ids doivent être autorisés et leurs dépendances
terminées ou placées avant elles. Les montants engagés doivent rester sous le plafond
autorisé. Les contrôles critiques prêts sont décrits par id/status PASS/evidence ;
les observations de résultat par source/observed_at/finding.

Le script vérifie la cohérence déclarée, jamais l’authenticité d’une permission
ou d’une preuve. Organisation doit vérifier la demande utilisateur, le périmètre
et les droits réels avant toute action. Aucun ordonnanceur n’est fourni.
