# Réflexion observable, puis préproduction avec de vrais sous-agents

## Parcours obligatoire d'une nouvelle mission Studio

La réflexion produit des synthèses de décisions vérifiables, jamais une transcription
de pensées privées. Elle précède la fabrication de l'architecture, du skin et des
pilotes. La recherche et la préparation des profils appartiennent à ce cadrage.

| Étape | Travail réellement effectué | Sortie et condition de passage |
|---|---|---|
| F0_CADRAGE | Lire l'existant, préciser le problème lecteur, l'objectif, les contraintes et les permissions | `00_REFLEXION.md` : faits, inconnues, périmètre, critères de réception |
| F1_RECHERCHE | Rechercher les besoins et les compétences du secteur, dont LinkedIn et Reddit | `01_RECHERCHE.md`, `01_COMPETENCES.md` : contenus lus, contre-preuves, limites ; profils préparés par le vrai /personna |
| F2_OPTIONS | Comparer des approches réalisables et leurs conséquences | options sérieuses, preuves, coûts inconnus, différenciation, couverture fan-out ; proposition soumise à un sous-agent métier |
| F3_DECISION | Corriger avec sa critique, vérifier puis retenir le périmètre V1 | décision motivée, réponse aux objections, test discriminant, critères ; cycle `idees` réellement clos |
| PREPRODUCTION | Enchaîner G2 à G5 dans le même travail autorisé | architecture et maillage, skin, briefs, pilotes, partenaires, technique, mesure, roadmap et transfert |

Ne pas terminer par « voici le plan, veux-tu que je continue ? ». Après F3, exécuter
la préproduction autorisée et produire les fichiers. Ne demander qu'une information
ou permission réellement indispensable, en poursuivant les travaux indépendants.
La réflexion ne déclenche ni publication ni dépense. Un manque critique ne devient
pas une hypothèse réversible ; documenter le blocage et les sorties encore possibles.

## Former, créer et charger les agents de cette occasion

Après la recherche métier et avant toute délégation métier, appliquer
[le protocole de compétences](16-recherche-personas-metier.md), puis le vrai
`/personna`. Produire un profil propre au domaine, une calibration et un mandat.
Créer au moins deux sous-agents distincts pour une nouvelle mission complète :
un contributeur métier et un critique métier. Ils peuvent couvrir plusieurs rôles
successifs ; ne pas lancer un agent par ligne du catalogue. Deux délégués actifs
maximum, aucun descendant, un rédacteur par fichier.

Transmettre au lancement le **contenu réel du profil** ou un chemin lisible avec
consigne explicite de lecture, sa version/empreinte, les compétences sourcées, le
brief courant, les invariants, les accès, les sorties et les critères. Le simple nom
« expert audio » ou un fichier non transmis ne constitue pas un persona chargé.
Les noms de personnes LinkedIn ne sont pas des identités à imiter. Un agent demeure
un agent IA et ne revendique aucun essai sensoriel, diplôme ou expérience humaine.

Enregistrer les IDs retournés par l'outil, le mandat et le retour effectif. Attendre
les contributions avant intégration. Un outil indisponible produit un dossier
provisoire, des profils et des mandats prêts ; il empêche le transfert strict.
`SEQUENTIAL_PROFILES` ne satisfait pas cette demande de vrais sous-agents.

## Itérer au fil des livrables

Pour chacun des quatre objets `idees`, `architecture`, `production_pilote`, `roadmap` :

1. Enregistrer la proposition dans une copie datée et immuable, avec son empreinte.
2. Confier une critique contradictoire à un autre agent, formé au domaine du site.
3. Intégrer les corrections. Si aucune modification n'est justifiée, répondre
   précisément aux objections avec les preuves ; ne pas fabriquer une correction.
4. Faire relire la version résultante par le critique dans un **nouveau retour réel**.
   Enregistrer critique, résolution, relecture, version et ordre d'exécution.
5. Recommencer si nécessaire ; après deux cycles non résolus, Astra arbitre sur
   preuves. Une objection P0/P1 reste bloquante tant qu'elle n'est pas résolue.

Le cycle `idees` appartient à la réflexion ; les trois autres ont lieu pendant la
préproduction, pas seulement lors d'une cérémonie finale. La carte fan-out passe
dans les critiques d'architecture et de pilote : une sous-question doit posséder
une réponse utile, une preuve, une limite et une URL/section propriétaire.
La fermeture d'un cycle exige la relecture de la version courante. Les avis anciens
restent dans l'historique, sans constituer une approbation de fichiers modifiés.

## Registre et reprise

`state.json` conserve les exigences et les preuves existantes ; `workflow.json`
relie les étapes ordonnées, la recherche, les compétences, les profils, les appels
d'agents et les cycles. Les séquences sont des événements réellement enregistrés,
pas une chronologie reconstruite pour faire passer le validateur. Les preuves
runtime sont les retours de l'hôte, sans secrets. Les empreintes ne prouvent pas
l'authenticité des déclarations : la revue du dossier consulte ces retours.

Une reprise ciblée garde les étapes et les agents encore pertinents. Rechercher et
reformer seulement les profils affectés par un changement de domaine, de besoins,
de preuves ou de mandat. Pour un ancien dossier 2.0, ajouter le registre depuis le
template et les exigences R27/R28 sans réinitialiser le dossier. Ne pas marquer les
étapes faites rétroactivement sans preuve : compléter les manques avant transfert.
Le validateur accepte l'ancien brouillon avec un avertissement ; le transfert sous
le nouveau contrat nécessite ces preuves. Aucun fichier projet n'est migré seul.

## Remplir le registre depuis les événements réels

| Champ | Liaison attendue |
|---|---|
| `steps` | F0–F3, ordre `sequence` et IDs de preuves du registre `state.evidence` |
| `research.platforms` | requêtes distinctes, date, sources `state.sources` OBSERVED et leurs preuves de lecture ; limites même lorsque READ |
| `competencies` | ID, rôles affectés, sources, application au secteur, comportement, calibration et observation/inférence/désaccord |
| `profiles` | rôle, niche, version, chemin/hash, compétences retenues, application du skill et calibration, séquence de préparation |
| `delegates` | ID réel, rôle, mandat/hash et profil courants, création runtime, chargement runtime et sa séquence, retours et période d'activité |
| `iterations` | sujet/cycle, auteur/critique, copie immuable de proposition, livrable relu/hash, trois preuves distinctes et quatre séquences |
| `preproduction_started_sequence` | événement de transition après F3, pas une approbation créée par init |

Le mandat contient `persona_loading_instruction` pour lire le contenu/chemin
transmis. Au lancement, création et chargement peuvent être le même appel/événement.
Après réforme, utiliser un nouvel appel de reprise et sa preuve de chargement,
sans remplacer la trace de création initiale. Le critique ne revoit la version
courante qu'après ce chargement. Un agent peut être conservé entre les cycles.

`state.reviews.trace_id` reprend l'ID du critique réellement appelé ; ses
`evidence_ids` contiennent le retour de relecture et ses `reviewed_artifacts`
incluent le livrable/hash final de ce cycle. `snapshot` prépare ces empreintes,
sans exécuter une revue. Conserver les anciens cycles dans le compagnon ; le
dernier cycle de chaque sujet doit être PASSED. Un nouveau refus invalide l'ancien
accord. Une ancienne empreinte historique n'est pas une approbation du fichier courant.
L'ordre des numéros de cycles doit suivre l'ordre des événements ; un numéro plus
grand ne peut masquer un refus plus récent. Critique, résolution et relecture ont
trois preuves distinctes. Après réforme, la preuve de chargement est un nouveau
retour runtime distinct de la création. Les empreintes du mandat et des preuves
de recherche/formation/chargement participent à l'invalidation des avis courants.
