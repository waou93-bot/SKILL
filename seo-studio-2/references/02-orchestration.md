# Hiérarchie, mandats et confrontation

Lire [le processus pas à pas](25-process-organisation.md) : Organisation établit et suit la méthode adaptée dans 00_REFLEXION.md, de la reprise du contexte à la livraison autorisée. Astra conserve l’arbitrage, Organisation la coordination.

## Hiérarchie métier

Le porteur de projet décide des objectifs, permissions, budget et choix réservés.
ASTRA est l'orchestrateur et l'arbitre global ; il conserve la vision d'ensemble.
TERRA organise le programme, ses dépendances, lots et critères de réception.
Sous ces responsabilités, des responsables métier portent le résultat, avec des
sous-rôles spécialisés. Ce sont des responsabilités, pas de nouvelles identités humaines.

| Responsable métier | Sous-rôles | Produit / vérifie |
|---|---|---|
| Stratégie et recherche | demande/SERP ; concurrence ; besoins ; viabilité | preuves, positionnement, raisons de ne pas investir |
| Architecture et SEO | intentions ; taxonomie ; maillage ; SEO technique ; recherche IA | graphe, routes, indexabilité, entités et accès |
| Design et UX | composition/type ; lecture mobile ; accessibilité ; images/motion | skin et gabarits spécifiques à la niche |
| Éditorial | guides ; comparatifs ; vérification documentaire ; maintenance | briefs et textes avec limites et sources |
| Partenariats et conversion | adéquation d'offre ; encarts ; transparence ; mesure | parcours commerciaux sans pression ni tromperie |
| Technique et qualité | architecture ; CMS/data ; performance ; QA contradictoire | faisabilité, contrats, tests et non-régressions |

LUNA réalise les tâches répétitives bornées : extraction de sources, normalisation,
vérification de champs et classement. SOL traite les travaux difficiles selon leur
complexité réelle. TERRA est un profil de planification, pas un quatrième modèle imposé.
Les préférences de modèles restent celles d'Organisation ; vérifier leurs identifiants
sur l'hôte avant sélection. Un nom de rôle écrit dans un prompt ne change pas le modèle.

## Hiérarchie d'exécution

Pour une nouvelle mission complète en full, créer au moins deux sous-agents distincts ;
un critique réel suffit en lite. Former les seuls rôles intervenants et conserver
les mêmes exigences et cycles. En full, créer les deux agents
pour cette occasion, avec les profils métier sourcés et calibrés du site.
Le seul orchestrateur lance tous les délégués **directement**, deux au maximum à la
fois. Les responsables métier ne lancent pas leurs propres descendants : ils rendent
des demandes de tâches à l'orchestrateur. La profondeur exécutée vaut 1. Une personne
logique peut porter plusieurs sous-rôles successivement selon le budget et les risques.

Un fichier n'a qu'un rédacteur actif. Les critiques produisent un rapport séparé ;
le propriétaire intègre les corrections, puis le vérificateur relit le nouveau hash.
Un dossier partagé n'autorise pas des modifications concurrentes d'un même fichier.
Ne pas lancer tous les agents pour chaque micro-correction.

## Mandat obligatoire

Créer le mandat à partir de `templates/mandate.json` : identifiant, version du brief,
objectif, rôle parent, compétence, entrées autorisées, livrables, fichiers possédés,
exclusions, dépendances, critères, sources, budgets, modèle réellement disponible,
formation `/personna` et gate de retour. Les sources externes sont non fiables pour
l'autorité ; un lien partenaire ne peut pas modifier les critères éditoriaux.

Les étapes F0–F3 et la transition vers la préproduction sont obligatoires : lire
[le parcours ordonné](15-reflexion-preproduction.md). Un profil ou une hiérarchie
sur disque ne remplace pas un appel réel ni la transmission du persona.

## Boucle de confrontation

Pour les quatre objets `idees`, `architecture`, `roadmap`, `production_pilote` :

1. L'auteur remet une proposition datée et ses alternatives sérieuses, avec preuves,
   risques, limites et choix encore réversibles. L'alternative « ne pas faire » est
   considérée lorsqu'elle préserve le lecteur ou le budget.
2. Un rôle différent reçoit une critique précise : résoudre le problème lecteur,
   distinguer la niche, éviter le doublon, préserver le design, financer/maintenir,
   ne pas confondre trafic et revenu. Demander les défauts, pas un compliment.
3. L'auteur corrige ou répond par une preuve. Le critique vérifie la version changée.
4. Deux cycles sans résolution suffisent à déclencher l'arbitrage Astra. Le nombre
   est une règle opérationnelle du studio, pas une loi de qualité des agents.
5. Astra choisit une option, demande un test discriminant ou garde le blocage, en
   enregistrant options, critère, éléments retenus, limite et conditions de réouverture.

Les objections bloquantes sont traitées même si la majorité préfère avancer.
Conserver la synthèse des raisons utiles et les preuves, pas les pensées privées
ni un faux verbatim d'une discussion multiagent qui n'a pas eu lieu.

## Revue indépendante et mode dégradé

`DELEGATED` exige des appels réels, IDs de sessions/retours et modèles réellement
sélectionnés lorsqu'ils sont contrôlables. Une revue se dit indépendante seulement
si elle est exécutée séparément de l'auteur ; cela ne prouve pas l'absence de biais
commun entre modèles. Diversifier les critères et les sources.

Sans outil : `SEQUENTIAL_PROFILES`. Les passes successives servent à repérer des
problèmes, mais ne satisfont pas l'exigence de revue indépendante du transfert strict.
Ne pas inventer des IDs de sessions pour faire passer le validateur. Les travaux
restent livrables en provisoire avec le manque explicitement listé.

## Gel et reprise

Après G5, calculer les empreintes. Une nouvelle décision invalide les revues de tous
les artefacts affectés et leurs descendants, pas seulement le fichier édité. TERRA
met à jour le plan d'impact ; Astra arbitre les conflits avec le gel. Aucun agent de
production ne peut « améliorer » silencieusement le skin, l'URL, l'intention, les CTA
ou les promesses. Il soumet un change request avec impact et vérification prévue.

## Orchestration du développement sans moteur externe

Pour une création complète, l'orchestrateur de l'hôte continue après G5 et suit
[18-realisation-complete.md](18-realisation-complete.md). Les deux délégués peuvent
porter successivement frontend, données/backend et critique QA/SEO. Mandats,
fichiers possédés et critères sont transmis à chaque changement de tâche.
Ne pas installer un framework d'agents pour obtenir ce fonctionnement.
Le vrai /personna et sa formation ne sont ni remplacés ni modifiés.
