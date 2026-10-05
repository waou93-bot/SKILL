# Contrôles et essais d'Organisation

## Extension du 18 septembre 2026 — à rejouer avant installation

Cette révision ajoute un contrat de complétion, une classe de séparabilité avant délégation, des profils de harnais par rôle, une validation proportionnelle au risque et vingt scénarios dans `evals/evals.json`. Les contrôles historiques ci-dessous restent des preuves de la version du 16 septembre ; ils ne valident pas automatiquement cette révision.

Contrôles à exécuter sur la révision :

- validateur `quick_validate.py` et parsing JSON des vingt scénarios ;
- résolution de tous les liens relatifs depuis `SKILL.md` ;
- comparaison comportementale avec la version précédente sur les mêmes modèles, outils, efforts et fixtures ;
- mesure séparée de la réussite, du coût, du temps, des reprises, des fausses réussites acceptées et des résultats corrects bloqués ;
- vérification spécifique des cas de couverture incomplète, de séparabilité faible et de test impossible.

Ne retenir une modification que si elle améliore les cas visés sans régression importante ailleurs. Le petit benchmark sert aux comparaisons de versions d'Organisation ; il ne classe pas universellement les modèles.

Date : 16 septembre 2026. Registre historique du poste de référence ; les chemins personnels ont été remplacés par `$HOME` pour publication. Les sauvegardes et preuves de la machine restent locales. Ces résultats ne décrivent pas une installation déjà effectuée sur la machine du lecteur. Les niveaux ci-dessous sont distincts. Les simulations ne prouvent pas un comportement universel ni une intégration de production.

## 1. Fichiers créés et contrôlés

Installation utilisateur Windows native : `$HOME/.agents/skills/organisation/`. Les cinq fichiers requis existent : `SKILL.md`, `agents/openai.yaml`, `references/routing.md`, `references/integrations.md`, `references/tests.md`.

Contrôles réellement exécutés :

- Validateur officiel `skill-creator/scripts/quick_validate.py` sur la préparation puis sur l'installation : `Skill is valid!`.
- Parsing PyYAML des métadonnées et de `agents/openai.yaml` avec Python 3.12 déjà installé ; nom technique, interface, description courte, prompt `$organisation` et booléen d'invocation implicite contrôlés. Aucune dépendance installée. Le Python embarqué ne disposait pas de PyYAML ; le Python utilisateur existant a permis le contrôle.
- Trois liens relatifs du SKILL.md résolus vers des fichiers présents ; cinq fichiers requis, pas de marqueur de scaffold inachevé.
- Une seule instance d'`organisation` trouvée dans les deux racines utilisateur pertinentes ; un seul bloc `ORGANISATION_ROUTER` dans `$HOME/.codex/AGENTS.md`.
- AGENTS.md était vide ; aucun AGENTS.override.md trouvé. Sauvegarde préalable datée : `$HOME/.codex/AGENTS.md.bak.20260916T093806484831Z`, copie vide vérifiée par SHA-256.
- Réexécution réelle de l'installateur après copie : zéro fichier modifié, les six cibles inchangées, zéro sauvegarde supplémentaire. Les empreintes correspondent. Le test de fusion du bloc couvre aussi des instructions préexistantes, un BOM, deux anciens blocs et des marqueurs malformés : préservation, dédoublonnage et refus des marqueurs incohérents observés.
- Empreintes de `config.toml`, du SKILL.md de `brain` et de celui de `newpro` inchangées. Aucun modèle par défaut, paramètre de sécurité, dépendance ou autre skill modifié. Aucun code applicatif, MASTER, backlog ou dépôt modifié.

Ce registre reçoit les résultats après les contrôles : sa version initiale est sauvegardée avec un suffixe `.bak.<date UTC>` avant sa mise à jour. Les noms exacts des sauvegardes finales et les empreintes sont consignés dans le compte rendu d'installation remis à l'utilisateur. Les sauvegardes ne portent pas le nom exact `SKILL.md` et ne créent pas un deuxième skill.

## 2. Détection réelle par le chargeur Codex

Le binaire installé est `codex-cli 0.154.0-alpha.6.2`. Une requête `initialize` a confirmé `platformOs: windows`, `platformFamily: windows` et `codexHome: $HOME/.codex`. Le CODEX_HOME explicite de l'environnement n'est pas défini. Le compte technique du shell protégé n'est pas le profil utilisateur retenu.

Après installation, `skills/list` avec `forceReload: true` a retourné exactement une entrée `organisation`, chemin correct, `scope: user`, `enabled: true`, interface `displayName: Organisation`, description et prompt attendus ; tableau `errors` vide. Le nombre de skills de cette interrogation est passé de 96 à 97. `brain` et `newpro` sont également actifs à portée utilisateur.

Cette preuve provient du véritable chargeur du binaire local, dans un processus app-server temporaire exécuté sous le profil utilisateur, fermé après la lecture. Aucun serveur permanent n'a été installé. Elle ne constitue pas une observation de l'interface graphique déjà ouverte. Des avertissements d'icônes existaient avant et après ; Organisation ne déclare aucune icône et n'a produit aucune erreur de découverte.

## 3. Tests comportementaux réellement exécutés

Un sous-agent indépendant, sans historique de la rédaction ni résultats attendus, a lu Organisation et traité sept scénarios fictifs en lecture seule. Les rôles ont été appliqués successivement par ce même évaluateur : aucun changement de modèle ni sous-agent descendant. Une reprise complémentaire du cas d'architecture a chargé explicitement le véritable `brain`.

| Cas | Observation | Portée de la preuve |
| --- | --- | --- |
| Corriger une faute | « Le bouton est bleu. » ; LUNA, réponse directe. | Correction effectivement produite ; aucun processus Business. |
| Organiser un backlog | TERRA ; priorités, dépendances avérées/supposées, critères d'acceptation proposés. | Réponse produite sur la fixture ; aucun backlog réel modifié. |
| Réparer un bug | SOL ; reproduction isolée de l'arrondi JavaScript de 1.005, demande ciblée du code et de la règle métier. | Expression effectivement exécutée ; aucune réparation ou réussite de test d'application revendiquée. |
| Architecture majeure | ASTRA ; recommandation conditionnelle et preuves manquantes explicites. Complément avec lecture réelle de `brain` et de sa référence de contrôle. | Deux réponses de simulation ; `brain` distingué de New Pro Brain absent ; aucune migration engagée. |
| Application payante | TERRA ; Business demandé avant réalisation importante, absence signalée. `newpro` lu pour son contrat réel de bootstrap. | Cadrage produit ; ni Business ni bootstrap ni construction exécutés. |
| Audit économique existant | Conservation du MASTER et des preuves déclarées ; calculs 240 €/mois, 150 € après seul hébergement, écart budgétaire 4 000 €. | Calculs isolés exécutés sur données fictives ; aucune vérification d'encaissement ou conclusion de viabilité. Aucun MASTER lu physiquement ou réinitialisé. |
| Skill absent | New Site annoncé « disponible après installation » ; aucune substitution silencieuse ni exécution fictive. | Recherche ciblée du catalogue et des deux racines ; aucune recherche de tout le disque. |
| Recommencer l'installation | Six cibles identiques, aucun doublon, aucune nouvelle sauvegarde. | Installateur réellement relancé sur les fichiers installés, et pas seulement examiné. |

Les réponses détaillées et leurs limites sont conservées dans le compte rendu local remis à l'utilisateur. Ce test mesure un comportement sur ces scénarios, pas une garantie d'exécution future.

## 4. Seulement examinés ou restant à tester

- Invocation implicite réelle et affichage dans le sélecteur de l'app ouverte : non observés. La politique YAML est autorisée et le chargeur reconnaît le skill, ce qui ne prouve pas le choix automatique dans chaque demande.
- Chargement effectif du nouveau bloc global par une nouvelle conversation : non exécuté ici. Le fichier global et l'absence d'override ont été contrôlés ; aucune conversation utilisateur supplémentaire n'a été créée pour ce test.
- New Pro Brain, New Site, New App, Business : absents, donc aucun appel réel. `brain` est une méthode de raisonnement ; `newpro` un bootstrap MASTER sans production. Ce sont des limites d'intégration explicites.
- Orchestration de plusieurs modèles, travail concurrent, escalade après échec, bootstrap `newpro` complet, projet réel et autres PC : non testés. Les règles ont été examinées, sans les déclarer validées en situation réelle.

Pour utiliser le skill dans cette app, démarrer une nouvelle conversation et écrire `$organisation` suivi de la demande. La documentation indique la détection automatique des changements de skills ; si le skill n'apparaît pas, redémarrer Codex. La nouvelle conversation permet également de reprendre le bloc global. Le bloc ne supprime pas les limites de sélection des skills ; l'installation reste locale à ce PC.

Pour retester, utiliser un espace isolé : validateur système, parsing YAML, liens, doublons, sauvegardes, `skills/list` si disponible, puis scénarios. Dater les observations, préserver les preuves encore valides et signaler les contrôles non réalisables.

Sources officielles consultées : [skills locaux et interface](https://learn.chatgpt.com/docs/build-skills), [instructions AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [protocole App Server](https://learn.chatgpt.com/docs/app-server).
