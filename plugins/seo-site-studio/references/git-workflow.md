# Branches, worktrees et intégration

## Inspection et choix proportionné

Avant mutation : vérifier racine réelle (`git rev-parse --show-toplevel`), instructions, branche/HEAD, remotes fetch/push (`git remote -v`), état index/worktree (`git status --short --branch`, diff indexé/non indexé), base attendue et worktrees (`git worktree list --porcelain`). Lire MASTER/PROJECT_SKIN et changements utilisateur. Ne pas présumer que le dossier courant est le checkout voulu. Dossier non Git : continuer les actions locales autorisées ; Git N/A justifié, pas `git init` automatique. Si le projet sauvegardé est demandé directement, respecter ce choix.

Retouche simple : checkout courant lorsque sûr. Refonte ou travaux parallèles séparables : branche dédiée descriptive selon tâche/conventions existantes ; réutiliser branche/worktree pertinent après vérification propriétaire/état/base. Worktree utile pour isoler deux tâches ; jamais imposé à chaque modification. Pour les worktrees gérés Codex, inspecter les artefacts et utiliser les outils natifs lorsqu'ils sont disponibles. Le choix d'une base ne doit pas perdre les changements requis : un worktree neuf ne copie pas les modifications non committées.

État dirty : identifier propriétaires et fichiers avant action. Préserver index et contenu ; snapshot récupérable autorisé ou patch local incluant les fichiers nécessaires avec provenance, sans embarquer secrets. Ne pas transporter tout le checkout aveuglément. Ne pas employer reset/clean/stash destructif ni écraser/switcher des fichiers dirty pour faciliter une intégration. Si les changements pertinents ne peuvent être isolés, garder le checkout et séquencer ou signaler le blocage précis.

## Mandat et exécution

Pilote = propriétaire du registre et des documents canoniques. Chaque tâche : racine/worktree absolu, branche, base SHA, HEAD initial, fichiers propriétaires, dépendances, décisions validées, autorisations et critères. Deux délégués maximum sans descendants ; aucun fichier écrit simultanément par deux agents, y compris dans des branches destinées à fusionner. Résultats liés au SHA exact ou à un identifiant d'artefact dirty documenté avec diff/empreintes, pas au nom mutable de branche.

Commit local, push, création PR, fusion dans une branche cible et déploiement ont des périmètres d'autorisation distincts. Réutiliser l'autorisation humaine existante lorsqu'elle couvre action/cible ; ne pas la redemander par cérémonie. Une installation plugin n'en donne aucune. Avant push : remote/branche exacts, diff final et fichiers autorisés, absence de secrets, état distant actuel. Pas de force push sans autorisation spécifique. Toute PR créée est attachée au chat avec l'outil natif disponible. Aucun contournement de protection/CI.

## Intégration et conflits

1. Lire retour, diff complet relatif à la base et preuves de chaque tâche ; vérifier couverture, fichiers utilisateur conservés et décisions Design DNA/MASTER. Contrôles adaptés au changement, sur la révision réellement intégrable. Ne pas déclarer une CI verte sans exécution observée et SHA correspondant.
2. Comparer base courante/distance cible à la base testée avant fusion ; fetch/lecture distante avec accès disponible. Base évoluée = examiner les changements et intégrer de nouveau dans une branche/checkout sûr, puis rejouer les contrôles affectés. Si accès distant absent, état local uniquement ; fraîcheur distante non vérifiée.
3. Avant fusion autorisée : arbre propre ou changements isolés documentés, point de repli récupérable (SHA/référence/patch), branche cible et méthode conformes au projet. Ne pas fusionner dans une branche dirty ambiguë. Préparer résultat reviewable avant autorisation manquante.
4. Conflit : inventorier fichiers et intentions des deux côtés ; ne pas choisir automatiquement ours/theirs. Astra arbitre contre décisions récentes et critères, Sol traite les résolutions les plus difficiles. Conserver changements légitimes des deux branches ; écrire un journal de résolution. Si décision utilisateur indispensable, garder opération et état récupérables, avancer ailleurs.
5. Relire diff intégré, rechercher marqueurs résiduels et conflits sémantiques sans marqueur (tokens, imports, routes, catalogue, consentement). Build/tests/parcours/rendu pertinents sur HEAD final. Invalider les preuves affectées, attendre CI obligatoire sur cette révision. Vert sur ancien SHA ou avant merge ne valide pas le résultat final. Une fusion sans conflit peut aussi introduire une régression.

## Repli et nettoyage

Repli non destructif : préserver l'état et diagnostiquer ; revert d'un commit publié seulement avec mandat adapté, jamais réécriture historique implicite. Abort d'une opération locale uniquement après vérifier ce qu'il préservera et sauvegarder les changements requis. Cleanup : worktree encore utilisé, dirty, non poussé ou contenant fichiers ignorés nécessaires = conserver jusqu'à sauvegarde récupérable vérifiée. Pour un worktree géré, préférer archivage natif avec snapshot ; préserver les ignorés utiles séparément. Pour un worktree Git ordinaire, vérifier racine/état/commits et sauvegarde puis suppression standard sans force, autorisée. Pas de suppression récursive calculée ni de branche supprimée sans nécessité.

Scénarios : dirty utilisateur → conserver ; deux tâches → propriétaires distincts et intégration revue ; conflit → résolution sémantique puis tests finaux ; base déplacée → preuves anciennes invalidées ; non Git → N/A sans init ; autorisation externe refusée → livraison locale sans push/PR/merge/deploy. Le registre contrôle ces décisions, pas l'état réel de Git : toujours inspecter les commandes et sorties.
