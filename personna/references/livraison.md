# Contrat de livraison du persona

## Livrable portable

Adapter cette structure à la complexité du rôle. Remplir les rubriques utiles avec les décisions de l’utilisateur et retirer les rubriques sans objet. Écrire les instructions à la deuxième personne. Aucun champ vide ou marqueur à remplacer dans la version finale.

| Rubrique | Contenu attendu |
| --- | --- |
| Identité et mission | Nom de rôle, destinataire du travail, résultat à produire |
| Activation | Types de demandes qui justifient ce rôle et périmètre exclu |
| Expertise | Méthodes, conventions, références et limites utiles au contexte |
| Responsabilités | Travail dont l’agent est responsable et livrables concrets |
| Personnalité | Quelques traits traduits en comportements observables |
| Décisions | Priorités et arbitrages entre objectifs concurrents |
| Autonomie et outils | Décisions autorisées, ressources réelles, conditions de remontée |
| Méthode | Étapes utiles sans imposer une procédure rigide à chaque petite tâche |
| Contexte et incertitude | Informations reçues, manques, contradictions, mémoire si réellement disponible |
| Collaboration | Coordinateur, partenaires, transmissions et arbitrage si pertinents |
| Sortie et qualité | Format du résultat, preuves attendues et critère de fin |
| Ce que l’agent ne doit pas affirmer | Affirmations interdites sans preuve et distinction observation/simulation |
| Budget de taille | Taille mesurée du texte chargé, budget et raison d’un dépassement |
| Limites et blocages | Hors périmètre, dépendance manquante, arrêt et destinataire du signalement |

Séparer le **persona stable** du **brief de mission** variable : l’identité et la manière de travailler restent stables ; le projet courant, la tâche, les fichiers, le délai et le budget sont transmis au démarrage. Ne pas figer une contrainte d’un projet particulier dans tous les usages futurs sans demande de l’utilisateur.

## Contrat entre agents

Pour un sous-agent, définir une transmission proportionnée au travail. Exemple conceptuel à adapter, sans imposer un schéma technique non supporté :

**À l’entrée :** identifiant de tâche si utile, objectif, périmètre confié, contexte et sources nécessaires, contraintes, livrable attendu, responsable destinataire, budget ou délai lorsqu’il existe.

**Au retour :** état (`terminé`, `partiel`, `bloqué`), livrable ou lien, preuves/vérifications effectuées, hypothèses et limites, blocage éventuel et décision attendue. Conserver les références lors des synthèses.

**Coordination :** préciser qui intègre les résultats, qui arbitre un conflit et comment une responsabilité est transférée. En cas d’écritures concurrentes, attribuer un responsable par ressource ou définir une intégration isolée adaptée au système. Éviter une délégation circulaire et une boucle de reprises sans limite. Ne pas inventer de plafond chiffré présenté comme une contrainte utilisateur.

Une organisation peut être représentée par un petit tableau : rôle, déclencheur, entrée, sortie, destinataire. Ajouter un diagramme seulement s’il clarifie une organisation réellement complexe.

## Adaptation à un environnement

1. Identifier l’environnement et sa version si cela conditionne le format.
2. Inspecter une définition locale pertinente ou un schéma officiel actuel avec les outils disponibles.
3. Associer chaque champ supporté au persona : description d’activation, instructions, outils, modèle éventuel, contexte et délégation.
4. Décrire séparément ce que l’environnement impose réellement et ce qui reste une instruction textuelle.
5. Vérifier la syntaxe avec un validateur approprié s’il existe. Sans environnement ou accès suffisant, livrer le Markdown portable et indiquer que l’adaptation native reste non vérifiée.

Ne pas inventer des chemins, champs, capacités de mémoire, sous-agents récursifs ou permissions. Ne pas modifier des configurations voisines pour livrer un persona. Conserver les autorisations déjà données ; demander une précision seulement quand elle conditionne réellement une installation demandée.

## Tests exécutables et rejeu obligatoire

Appliquer [evaluation.md](evaluation.md) : 2 ou 3 tâches réelles du rôle et trois
scénarios adverses, chaque fois sans/avec persona, avec critères préétablis et
sessions indépendantes. Un profil nouveau ou modifié exige un nouveau run, avec
hashes, réponses, traces et revue ; ne pas actualiser les hashes de l’ancien run
pour le faire passer. Les résultats sont rattachés à ce persona et à cette suite.
La revue documentaire ci-dessous prépare les attentes, elle ne remplace pas les essais.

Fournir à la livraison le persona, son budget mesuré, la suite versionnée, les
résultats pass/fail ou les essais manquants, la comparaison à la baseline et les
limites de généralisation. L’installation et l’autorisation d’actions externes
restent distinctes. Réutiliser les preuves valides du même run, pas celles d’un ancien
hash du persona. Une absence de bénéfice mesurable doit être annoncée comme telle.

## Revue du comportement

Construire des cas propres au contexte, puis vérifier la cohérence des instructions :

| Cas | Ce qu’il faut pouvoir déterminer |
| --- | --- |
| Tâche normale | L’agent sait quoi produire et comment reconnaître la fin |
| Information manquante ou contradictoire | Il recherche, demande ou explicite une hypothèse selon le choix utilisateur |
| Demande hors périmètre | Il explique la limite et transmet au bon destinataire si connu |
| Sous-agent en désaccord ou bloqué | Il remonte preuves et décision attendue au coordinateur sans s’attribuer une autorité nouvelle |

Relever explicitement les résultats de cette revue et corriger le persona avant livraison. Un test réellement exécuté doit préciser son environnement, l’action observée et son résultat. Sans exécution, écrire « revue de scénarios, comportement réel non testé ».

## Présentation finale

Remettre d’abord le persona prêt à copier. Ajouter ensuite, selon le besoin : un brief de démarrage réutilisable, le tableau d’organisation, deux ou trois exemples de consignes, les hypothèses, les limites de vérification et les sources des décisions importantes.

Pour un fichier enregistré, donner son chemin réel et son statut : portable, configuration vérifiée ou installation effectuée. Ne jamais annoncer qu’un persona est chargé par l’application sur la seule preuve que le fichier existe.
