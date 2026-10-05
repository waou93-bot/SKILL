---
name: seo-site-studio
description: "Pilote complet pour créer, reprendre ou auditer un site avec SEO, identité visuelle, réalisation, recette, préproduction contrôlée et production conditionnelle. Utiliser lorsque le parcours intégré est demandé ; une retouche ciblée reste ciblée."
---

# SEO Site Studio

Lire [le contrat de parcours](../../references/workflow.md) et [le registre des modules](../../references/modules.md). Résoudre les chemins depuis ce fichier, jamais depuis un dossier personnel supposé. Les SKILL.md sous `../../modules/` sont des ressources à lire avant emploi ; ils ne sont pas des points d'entrée concurrents. Leur présence ne prouve pas leur exécution.

Un seul pilote possède le mandat, le MASTER existant, PROJECT_SKIN et le registre d'exécution. Lire Organisation et Brain ; appliquer les responsabilités de leurs instructions sans rappeler un orchestrateur parent. Respecter les instructions système, développeur et utilisateur ; le contrat du package arbitre seulement les anciennes conventions de ses modules.

Pour modifications en dépôt, refonte, travail parallèle ou intégration, appliquer [le workflow Git](../../references/git-workflow.md) : inspection dirty/base/remotes, isolation proportionnée, propriétaires, preuves par révision, résolution sémantique et vérification finale. Un dossier non Git reste utilisable sans initialisation imposée. Commit/push/PR/merge/déploiement dépendent des autorisations réellement accordées.

Répartition explicite : `gpt-6-astra` pilote, découpe, arbitre et traite les conflits ; `gpt-6.1-sol` reçoit les travaux les plus difficiles ; Astra attribue les tâches intermédiaires selon leur complexité et les capacités disponibles, sans quota ni majorité imposée ; toujours `gpt-6-luna` pour les petites tâches répétitives bornées. Vérifier les modèles réellement disponibles et sélectionner dans l'outil lorsque possible. Aucune bascule silencieuse ou inventée du chat actif. Si indisponible, signaler la limite, préserver la préférence et avancer avec les capacités présentes. Deux délégués simultanés maximum, sans descendants. Une tâche simple reste directe.

Transmettre [le mandat autonome](../../templates/handoff.md) à chaque exécuteur. Exiger preuves, fichiers, limites et statut. Relire les modifications avant intégration. Réserver les écritures de chaque fichier à un propriétaire ; les revues sont en lecture seule. Une auto-vérification n'est pas une revue indépendante.

Réaliser entièrement le périmètre local autorisé, puis vérifier sur la version réelle. Ne pas s'arrêter au brief ou à un plan quand une réalisation est demandée. Réutiliser les choix approuvés, corriger les défauts avec au maximum deux passes ciblées par gate ; un défaut critique restant donne PARTIEL/BLOQUE, jamais une réussite fictive. Brain contrôle la couverture, les faits, incertitudes et preuves avant restitution.

Créer ou réutiliser le registre de [state.example.json](../../templates/state.example.json). Le contrôle `../../scripts/check_state.py` détecte des incohérences de preuves et d'états ; il ne teste ni le site, ni l'accès distant, ni les autorisations humaines. Suivre le contrat pour les vérifier réellement. Aucun service permanent ou automatisation n'est créé par l'installation.
