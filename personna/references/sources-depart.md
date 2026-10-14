# Sources de départ — consultées le 15 septembre 2026

Ces sources ont servi à concevoir le skill. Elles permettent d’amorcer une nouvelle recherche, mais doivent être relues et complétées selon le contexte. La date de consultation ne prouve pas la date de modification. Aucune révision Git n’a été figée et aucun système de ces dépôts n’a été exécuté pendant cette recherche.

## GitHub : définitions et organisations observables

### Bibliothèque de rôles transversaux

[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) présente des rôles en développement, design, marketing, opérations et autres domaines, avec des mécanismes d’adaptation à plusieurs outils. C’est une source d’exemples ; les qualificatifs de performance du README restent des affirmations du projet.

- [Agents Orchestrator](https://github.com/msitarzewski/agency-agents/blob/main/specialized/agents-orchestrator.md) : définition lue ; coordination de spécialistes, étapes de validation, suivi d’état, reprises limitées et remontée des échecs. Les noms d’agents, seuils et validations proposés appartiennent à cet exemple et doivent être adaptés.
- [UX Researcher](https://github.com/msitarzewski/agency-agents/blob/main/design/design-ux-researcher.md) : définition lue ; rapproche personnalité, mission de recherche et livrables. Utile pour comparer un rôle métier à un rôle technique. Les déclarations de mémoire et d’expérience sont du texte de persona, pas une preuve de capacités effectives.

### Vérificateur spécialisé dans Claude Code

[darcyegb/ClaudeCodeAgents](https://github.com/darcyegb/ClaudeCodeAgents) contient plusieurs rôles de contrôle. Le fichier [karen.md](https://github.com/darcyegb/ClaudeCodeAgents/blob/master/karen.md), lu directement, définit un agent qui confronte une réalisation déclarée au fonctionnement observable, adapte son compte rendu et évite d’inventer des défauts. Il illustre une personnalité reliée à des actes. Ce contenu ne démontre pas un gain mesuré par rapport à un agent généraliste.

### Framework de rôles métier

[CrewAI — définition des agents](https://github.com/crewAIInc/crewAI/blob/main/docs/v1.10.1/en/concepts/agents.mdx) expose notamment les champs `role`, `goal` et `backstory`, ainsi que les outils et paramètres d’exécution. Cette documentation officielle versionnée distingue les instructions de rôle de la configuration technique. Vérifier la version cible avant toute exportation ; les modèles et valeurs par défaut de l’exemple ne sont pas des recommandations du skill.

### Superviseur et spécialistes

[langchain-ai/langgraph-supervisor-py](https://github.com/langchain-ai/langgraph-supervisor-py) montre un superviseur, des spécialistes et la personnalisation du contexte transmis. Lors de la consultation, le README recommandait pour la plupart des usages un superviseur directement construit avec des outils plutôt que cette bibliothèque. Cela justifie de vérifier la recommandation actuelle du mainteneur, au-delà de la popularité ou de l’existence d’un dépôt.

## Reddit : témoignages et contradictions

Les constats ci-dessous décrivent ce que des participants rapportent. Ils ne sont ni des benchmarks ni une mesure représentative de tous les utilisateurs. Les messages et commentaires pertinents ont été ouverts ; certaines contributions promotionnelles ou automatisées ont été écartées des conclusions.

| Discussion et date du message initial | Signal retenu et limite |
| --- | --- |
| [Meilleurs usages des sous-agents — r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1mdyc60/whats_your_best_way_to_use_subagents_in_claude/) — 31 juillet 2025 | Certains participants décrivent des rôles spécialisés ou un vérificateur ; d’autres rapportent lenteur et difficultés de contexte. Le lien vers ClaudeCodeAgents permet de confronter un témoignage à une définition réelle. |
| [Collection de sous-agents — r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1mi59yk/we_prepared_a_collection_of_claude_code_subagents/) — 5 août 2025 | Un auteur présente une collection ; des commentaires interrogent l’intérêt des profils génériques face à des rôles adaptés au projet. Utile pour questionner le contexte, sans reprendre la promesse « production-ready » comme un fait. |
| [Sous-agents dans Codex — r/codex](https://www.reddit.com/r/codex/comments/1rvm2si/subagents_are_now_available_in_codex/) — 16 mars 2026 | Des participants signalent des conflits sur les mêmes fichiers et une consommation de contexte inattendue. Ce sont des retours datés, pas une description des capacités actuelles de Codex. |
| [Multi-agent en production — r/aiagents](https://www.reddit.com/r/aiagents/comments/1vl72ur/multiagent_systems_sound_better_on_a_whiteboard/) — 11 août 2026 | Discussion sur la difficulté à diagnostiquer les erreurs à travers plusieurs étapes et sur la perte de contexte. Sert à rechercher des contre-exemples et à préciser les transmissions, sans conclure que tout système multi-agent échoue. |

## Déductions pour la conception du skill

Ces choix sont une synthèse de conception, pas des résultats expérimentaux :

- Interroger sur la tâche et le livrable avant de choisir des traits de caractère.
- Donner à chaque rôle un périmètre et une manière de rendre compte.
- Examiner le contexte transmis, les droits réels, les limites de coût et la fin du travail.
- Comparer agent unique et organisation multi-agent selon les dépendances de la tâche.
- Vérifier les formats dans l’environnement cible, car les exemples et les témoignages vieillissent.

Couverture initiale : quatre dépôts distincts étudiés, plusieurs définitions concrètes, quatre discussions Reddit retenues, et des perspectives Claude Code, Codex, CrewAI, LangGraph et rôles transversaux. Des pages de documentation VS Code trouvées par recherche n’ont pas pu être ouvertes ; elles ne soutiennent aucune affirmation technique ici.
