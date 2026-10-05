# SEO Site Studio 1.1.0

Plugin local de skills, un seul point d'entrée : `seo-site-studio`. 25 modules embarqués comme ressources. Modèles préférés : Astra orchestre, Sol 6.1 reçoit les travaux les plus difficiles, Luna traite les lots répétitifs. Installation ne lance aucun projet ou service.

Depuis le CLI Codex : `codex plugin marketplace add <racine-marketplace> --json`, puis `codex plugin add seo-site-studio@seo-site-studio-marketplace --json`. La racine contient `.agents/plugins/marketplace.json` et `plugins/seo-site-studio`. Vérifier ensuite `codex plugin list --marketplace seo-site-studio-marketplace --json`. Reprendre dans un nouveau chat pour vérifier la découverte par l'hôte.

Le manifest portable `plugin.json` et son équivalent de compatibilité `.codex-plugin/plugin.json` sont identiques. Aucun connecteur/MCP/hook ni exécutable permanent. Ressources originales référencées par le registre ; adaptations de coordination explicites. Les scripts de modules exigent leurs dépendances réellement disponibles.

Ce package et son contrôle de registre ne prouvent pas la réalisation, le rendu ou le déploiement d'un site. Publication publique du plugin et du dépôt non effectuée.
