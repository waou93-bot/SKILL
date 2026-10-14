# Former les rôles avec le vrai /personna

## Découverte actuelle, puis lecture réelle

Lors de la révision du 13 octobre 2026, le vrai skill du catalogue actif a été
lu, avec ses références de recherche, entretien et livraison. Son chemin privé
n'est pas publié et cette lecture datée ne garantit pas sa présence sur un autre hôte. À chaque mission, retrouver et lire le skill réel du catalogue,
son contrat et ses références utiles. Ne pas fabriquer une commande de remplacement.

## Recherche avant formation

Appliquer [la deep research métier LinkedIn/Reddit](16-recherche-personas-metier.md)
avant de produire les profils. Le contrat Personna prévoit une recherche de rôles
d'agents Reddit/GitHub ; la demande Studio précise LinkedIn/Reddit pour les
compétences du secteur. Respecter cette demande, conserver GitHub comme complément
utile sur l'exécution et ne pas remplacer la recherche métier par des prompts SEO.

## Entrées et sorties par rôle réellement affecté

Fournir mission, limites, niche/type/public/pays/langue, version du brief, décisions,
skills lus, outils réels, droits, budget ou inconnues, fichiers possédés et critères.
Joindre la sélection de compétences de `01_COMPETENCES.md`, sources datées lues,
contradictions, comportements attendus, cas métier et limites d'expertise.
Utiliser `agents/personna-input.template.md`, adapté au contrat réel.

Appliquer réellement le workflow du skill, pas seulement écrire son nom. Conserver
son chemin/hash, les entrées, le profil versionné dans `PERSONAS/`, les cas de
calibration et leurs résultats/erreurs/corrections. Le profil doit transformer les
compétences en méthodes de travail et de vérification ; une liste de liens ne suffit
pas. Séparer le profil opérationnel du mandat variable. Aucune expérience humaine,
certification, entraînement des poids ou maîtrise professionnelle n'en découle.

## Calibration propre au site

Chaque rôle reçoit un cas normal, une information manquante/contradictoire et un
hors-périmètre ou conflit de responsabilité. Ajouter un cas discriminant du milieu :
audio sans essai d'écoute, reportage sans présence terrain, route locale sans date
de contrôle, équipement RGB dont la compatibilité n'est pas documentée, par exemple.
Les sources servent à définir ces cas, pas à inventer leur résultat.

Vérifier aussi source absente, test produit inventé, intention cannibale, règle
Design DNA, encart payé, permission et empreinte caduque. Distinguer revue de
scénarios et comportement effectivement observé avec un outil. Consigner les deux
lorsqu'ils existent ; ne pas nommer « test réel » une relecture de prompt.

## Évaluation obligatoire du profil courant (Personna 1.2.0)

Après recherche, entretien et livraison du profil, utiliser le vrai Personna 1.2.0
pour préparer une suite adaptée au rôle : deux ou trois tâches réelles du site,
chacune avec et sans persona, et les trois cas adverses injection, conflit de
consignes et permission refusée. Respecter le budget du profil (400–800 mots par
défaut, plafond 1200 sauf instruction utilisateur) et sa section des affirmations
interdites. Les réponses doivent venir de sessions isolées effectivement exécutées.
La création de fichiers de test ou de traces synthétiques ne forme aucun agent.

Conserver la suite, le dossier des sessions, les revues et le rapport dans le projet.
Dans chaque entrée `workflow.profiles`, ajouter `evaluation` avec `suite_path`,
`run_path`, `reviews_path`, `report_path` et `evidence_id`. Ce dernier désigne une
preuve `test_report` dont le chemin et l'empreinte correspondent au rapport.
Les chemins sont relatifs POSIX, sans traversée ni lien symbolique.

Le contrôle strict recalcule les résultats avec une copie identique de l'évaluateur
Personna livrée dans `scripts/personna_evaluate.py`. Il n'exécute aucun script du
dossier projet. Le rapport enregistré doit être exactement égal au recalcul et
avoir le statut PASS : un simple certificat `{"status":"PASS"}` ne suffit pas.
Le protocole version 2 lie requêtes, réponses, traces et revues au run, au profil,
à la suite et à la provenance déclarée. Toute modification du profil exige un
nouveau run et de nouvelles sessions/revues ; les résultats 1.1.0 sont à rejouer.
Sans cette preuve, le brouillon reste provisoire et le transfert strict est bloqué.

Ce recalcul hors ligne vérifie la cohérence des pièces, pas l'authenticité du
fournisseur de traces. La revue humaine doit contrôler la réalité des appels et
la pertinence des critères. Un PASS de la référence et du persona ne démontre pas
un gain du persona. Aucun abonnement, API payante ou framework externe n'est requis.

## Transmettre le profil évalué au sous-agent

Une fois calibré, transmettre au lancement le contenu ou le chemin lisible du
profil avec instruction explicite de lecture, son hash/version et le mandat.
Enregistrer ID retourné, preuve d'appel, profil transmis, retour, limites et
relectures. Réutiliser un agent de cette mission pour les cycles suivants si son
profil reste pertinent ; le reformer si son domaine ou ses compétences changent.
Une persona sur disque non transmise n'est pas un agent configuré.
Après réforme d'un profil, transmettre le nouveau contenu/chemin/hash dans un vrai
appel de reprise et conserver son retour de chargement avant toute nouvelle revue.
Ne pas remplacer rétroactivement la preuve du lancement initial : tracer séparément
`persona_load_evidence_id` et `loaded_sequence`. Une mise à jour du fichier seule
ne prouve pas que l'agent réutilisé a reçu la nouvelle version.

## Statut et manque

`A_FORMER` → `EN_CALIBRATION` → `FORME` ou `A_CORRIGER`. Seul un profil sourcé,
calibré et lié à des preuves permet `FORME` et un mandat métier validé. Sans
Personna, couverture LinkedIn/Reddit suffisante ou délégation réelle, préparer les
entrées et continuer les travaux indépendants ; profils/dossier provisoires,
transfert strict bloqué. Ne pas marquer tous les rôles formés par une seule étiquette.
