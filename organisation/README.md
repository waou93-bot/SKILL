# Organisation

Routeur transversal pour démarrer, reprendre, planifier, auditer, développer et faire évoluer un projet avec un parcours proportionné. Les rôles LUNA, TERRA, SOL et ASTRA ne sont pas des identifiants de modèles. Un seul agent suffit par défaut.

## Installer à portée utilisateur

1. Identifier l’environnement réellement utilisé par Codex et son répertoire personnel. Sous Windows natif, résoudre `$HOME` dans le profil utilisateur de l’app ; sous WSL, utiliser le répertoire personnel de la distribution active. Ne pas prendre le compte technique d’un shell protégé pour le profil de l’app.
2. Copier le dossier `organisation` complet dans `$HOME/.agents/skills/organisation/`, emplacement utilisateur documenté. Vérifier les autres racines reconnues, notamment `$CODEX_HOME/skills` ou `~/.codex/skills`, avant de créer une seconde instance. Si Organisation existe, comparer les fichiers et sauvegarder ceux qui changent avec une date ; préserver ses adaptations utiles et signaler les conflits. Ne pas écraser silencieusement.
3. Pour une relance identique, laisser les fichiers inchangés. Ne pas créer un deuxième dossier de skill. Ce dépôt ne contient pas d’installateur automatique : la conservation des sauvegardes et la fusion sont des étapes d’installation à effectuer explicitement.
4. Pour le routage global, utiliser [le bloc ORGANISATION_ROUTER](assets/ORGANISATION_ROUTER.md). Déterminer le fichier chargé dans `CODEX_HOME`, ou `~/.codex` par défaut : un `AGENTS.override.md` non vide peut remplacer `AGENTS.md`. Sauvegarder le fichier qui va changer puis ajouter ou remplacer uniquement le bloc identifié, une seule fois, en conservant les autres instructions. Ne pas créer un override uniquement pour imposer ce routage. Le fichier modèle dans assets n’est pas chargé automatiquement.
5. Vérifier le YAML, les références, l’absence de doublon et les sauvegardes. Exécuter le validateur système `skill-creator/scripts/quick_validate.py` s’il est disponible, puis vérifier la découverte dans le catalogue ou avec `skills/list`. Ces contrôles de fichiers ne prouvent pas une sélection automatique ou un comportement correct sur tous les projets.

Dans une nouvelle conversation, invoquer `$organisation` suivi de la demande. Si le skill n’apparaît pas après détection des changements, redémarrer Codex. La politique `allow_implicit_invocation: true` autorise la sélection implicite ; elle ne garantit pas le choix du skill et ne lance aucun modèle.

## Contenu et intégrations

- [SKILL.md](SKILL.md) : instructions opérationnelles et garde-fous.
- [agents/openai.yaml](agents/openai.yaml) : interface et politique d’invocation.
- [references/routing.md](references/routing.md) : rôles, capacités, délégation et escalade.
- [references/harnesses.md](references/harnesses.md) : profils de contexte, plan et outils par rôle.
- [references/completion-and-verification.md](references/completion-and-verification.md) : preuves de couverture, statut et validation proportionnelle au risque.
- [references/integrations.md](references/integrations.md) : contrats souhaités et inventaire local daté.
- [references/tests.md](references/tests.md) : contrôles réellement effectués, simulations et limites.
- [evals/evals.json](evals/evals.json) : vingt scénarios de référence pour comparer les versions du routeur.

Organisation reste utilisable seul. Vérifier et lire les skills réellement installés avant raccordement. `brain` fournit une méthode de raisonnement ; il ne faut pas le confondre avec New Pro Brain. `newpro` prépare un socle MASTER sans lancer la production. Les autres parcours absents sont annoncés comme disponibles après installation, sans exécution fictive.

Les résultats consignés proviennent de l’installation Windows de référence du 16 septembre 2026 : validation de fichiers, découverte par le chargeur Codex, simulations et relance idempotente. Le changement de chemins pour publication est une adaptation documentaire ; les tests comportementaux historiques n’ont pas été rejoués pour cette copie. L’installation locale ne synchronise pas les autres ordinateurs.

Documentation officielle : [skills](https://learn.chatgpt.com/docs/build-skills), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
