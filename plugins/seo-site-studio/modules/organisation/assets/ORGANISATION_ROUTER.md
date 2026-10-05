<!-- ORGANISATION_ROUTER:BEGIN -->
Pour les demandes de travail sur un projet (démarrer, reprendre, planifier, auditer, développer ou faire évoluer), charger d'abord le skill `organisation` depuis le catalogue actif ou le registre du package dans l’environnement constaté. Appliquer un routage proportionné : une tâche simple reste simple. Respecter les instructions locales plus spécifiques et les demandes explicites de l'utilisateur dans la hiérarchie applicable ; ne pas détourner un skill explicitement demandé ni relancer une orchestration déjà active. Si Organisation est indisponible, le signaler et continuer les parties réalisables sans prétendre l'avoir chargé. Ce routage n'étend ni les autorisations ni les capacités de sélection des skills ou des modèles.
<!-- ORGANISATION_ROUTER:END -->


## Préférence explicite de modèles — 5 octobre 2026

Toujours choisir `gpt-6-luna` pour les petites tâches répétitives bornées, `gpt-6.1-sol` pour les travaux les plus difficiles (selon complexité réelle, sans quota ni majorité imposée), et `gpt-6-astra` pour l'orchestration, le découpage, les arbitrages et conflits. TERRA reste un profil de planification, sans quatrième modèle imposé. Astra attribue les tâches intermédiaires selon leur complexité et les capacités disponibles ; aucun modèle supplémentaire ni quota n’est inventé.

Vérifier les identifiants et capacités dans le catalogue réel de la session avant sélection. Lorsque les sous-agents sont autorisés, transmettre le modèle correspondant à l'outil de lancement ; ne pas se contenter de le mentionner dans le prompt. Ne pas choisir un autre modèle silencieusement. Si indisponible, annoncer la limitation et conserver la préférence dans le transfert ; continuer les actions autorisées avec l'agent actuel lorsque possible. Un chat déjà actif garde son modèle tant qu'une action réelle de l'hôte ne l'a pas changé. Les noms de rôles ne prouvent pas une sélection effective. Ne pas modifier la configuration globale pour simuler ce routage.

Un travail trivial ne demande pas une nouvelle orchestration. Si l'hôte ne peut sélectionner le modèle de ce chat, déclarer cette limite une fois ; ne pas multiplier les agents pour une correction triviale.

Chaque mandat délégué est autonome : objectif, version du mandat, livrables, dépendances, fichiers propriétaires, critères d'acceptation, preuves et sources, décisions Design DNA/No Slop avec provenance, corrections utilisateur, autorisations effectivement accordées et actions exclues. Retour : réalisé, vérifié, non vérifié, fichiers touchés, contradictions et statut. Astra arbitre les contradictions sur preuves sans élargir les permissions. Deux délégués actifs au maximum, sans descendants ni écritures concurrentes.
