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

## Charger le profil dans le sous-agent créé

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
