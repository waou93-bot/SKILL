# Gates et acceptation stricte

## États distincts

Le package logiciel peut être écrit et testé alors que son corpus de référence reste
partiel. Un dossier projet peut être utile mais provisoire. Un build local peut passer
sans que la production soit testée. Ne pas fusionner ces états.

Le validateur retourne un résultat **structurel**. `STRUCTURE_OK` signifie que les
conditions qu'il sait contrôler sont satisfaites par les fichiers fournis ; il ne
certifie ni faits, ni indépendance, ni conformité visuelle, juridique ou moteur.
Les revues métier et preuves de l'hôte sont obligatoires pour le statut final.

## Gates

| Gate | Ce qui doit être présent | Motif bloquant typique |
|---|---|---|
| F0–F3 | cadrage, recherche métier LinkedIn/Reddit, options, décision et cycle idées clos | ordre sauté, profil générique, source seulement en extrait, critique simulée |
| G0 | contexte, permissions, exigences, inventaire lu, profils /personna et agents créés | dépendance absente, rôle non formé, droits inventés |
| G1 | recherche niche sourcée, limites du benchmark, positionnement, test de canal | statistiques imaginées, niche non comprise, preuve d'expertise fictive |
| G2 | routes/intention, parcours, CMS, maillage entrant et sortant | page importante orpheline, intention dupliquée, route privée indexable |
| G3 | skin, gabarits, briefs V1, pilotes, encarts et méthode | copie générique, image trompeuse, affiliation cachée, fausse expérience |
| G4 | deux stacks, choix motivé, dépendances, capacité de validation, instrumentation | roadmap irréalisable, mesures sans consentement, versions/prix inventés |
| G5 | critiques, corrections, arbitrages, traçabilité, hashes, transfert gelé | objection P0/P1 ouverte, preuve caduque, auto-revue présentée indépendante |
| G6 | recette et preuves live de production autorisée | noindex de prod, lien cassé, prix non vérifié, soumission prétendue |

G0 à G5 concernent la préproduction. G6 est préparé mais ne se valide qu'après réalisation
et autorisation. L'absence d'un site live ne bloque pas un bon dossier de préproduction :
elle interdit seulement d'y écrire « production testée ».

La [revue fan-out](14-fanout-retour-sites.md) complète les gates existants : G2
contrôle propriétaires/frontières/liens, G3 les réponses et preuves livrées, G5 la
recette et l'état de réalisation. Une carte de termes ou des metas enrichies ne
valident pas les réponses du corps. Le validateur structurel ne juge pas cette utilité.

## Gravité

P0 : sécurité, confidentialité, tromperie, permission, vérité des preuves, contradiction
majeure de périmètre. P1 : parcours non exécutable, preuve essentielle absente, maillage
cassé, composant clé non défini. P2 : amélioration non bloquante argumentée. Tous les P0/P1
ouverts empêchent le transfert strict ; les P2 sont affectés dans le backlog. Une moyenne
sur dix n'efface pas une fuite de données ou un article inventé.

## Conformité « à la lettre »

Transformer chaque phrase opératoire du mandat en règle testable. Les exigences du
package `schemas/requirements.json` sont le minimum. Ajouter les contraintes de la niche
et les corrections utilisateur au registre de projet. Chaque règle indique statut,
propriétaire, artefacts et preuves de vérification. Une dérogation explicite comporte
raison, impact et décision d'Astra ; les règles de sécurité, vérité et permission ne
sont jamais dérogeables. Une exigence applicable ne devient pas NON_APPLICABLE pour
faire monter un score.

## Contrôles automatiques

Le script contrôle notamment IDs, types, chemins de preuve internes et hashes, couverture
des exigences, présence des livrables, références page/lien, graphes et orphelins, unicité
d'intention, confidentialité, relations sponsorisées, profils et traces déclarées,
critiques/arbitrages et présence des gates. Les cas malveillants de path traversal et
symlink sont refusés. Il n'exécute aucun contenu téléchargé ni appel réseau.

## Contrôles de fond

Le critique vérifie que les sources soutiennent effectivement les affirmations, que les
comparaisons donnent une valeur propre, que le plan est réalisable, que le design appartient
à cette niche et que les encarts servent le lecteur. La preuve est une sortie réellement
obtenue avec contexte, pas une affirmation « vérifié » dans une table. Un hash protège
l'intégrité d'un fichier ; il ne prouve pas que le fichier raconte la vérité.

À la reprise après modification, recalculer l'impact et retirer les approbations touchées.
Le validateur refuse les preuves de fichiers modifiés dont les hashes ne correspondent
plus. La relecture doit porter sur la nouvelle version, pas sur le même nom de fichier.

## Instantanés de revue

Chaque revue enregistre `inputs_sha256` et les couples chemin/empreinte de `reviewed_artifacts`. La commande `snapshot` les calcule sans approuver. Une modification du plan métier ou des fichiers examinés invalide ces approbations, même si les hashes généraux des artefacts ont été remis à jour. Une nouvelle vraie revue est nécessaire ; ne pas rafraîchir ces champs pour contourner le gate.

## Gates de réalisation locale et de reprise

Pour les produits proposés chez des partenaires, G3 vérifie la spécification de
l'URL affiliée autorisée, du modèle/variante, du bouton d'action et de la mention
d'affiliation séparée selon [le contrat partenaires](08-partners.md). La recette
contrôle leurs valeurs rendues et la destination lorsqu'accessible. Une URL affiliée
manquante, un bouton « lien affilié », une destination produit incorrecte ou une
mention masquée laisse R16 ouverte pour le module concerné. Les preuves de clic
et de rendu non exécutées restent non vérifiées ; le dossier ne les invente pas.

Pour chaque page publique de contenu hors landing, G2 précise le corpus et les champs de recherche,
G3 spécifie son emplacement en tête de rubrique et ses états, et la recette de
réalisation vérifie [le comportement du moteur](06-design.md#recherche-en-tête-des-rubriques).
Une rubrique concernée sans cette spécification, ou un champ décoratif en réalisation,
laisse l'exigence R12 ouverte. Un petit corpus ne dispense pas de la recherche interne.
Une vérification documentaire ne prouve pas le fonctionnement dans le navigateur.

Pour un site réalisé, compléter G2/G3 par les preuves du
[protocole de réalisation](13-autonomie-production.md) : accès depuis landing/menu,
index et hubs, liens contextuels entrants, articles effectivement rédigés avec
redaction-editoriale-web, photos exactes ou illustrations professionnelles,
encarts utiles et états interactifs. Distinguer validation structurelle, relecture
éditoriale échantillonnée et inspection navigateur. Les étapes non exécutées
restent non vérifiées ; aucune moyenne ni quantité d'articles ne les remplace.

## Contrat additionnel 2.1 : workflow.json

Le [parcours obligatoire](15-reflexion-preproduction.md) complète G0–G5. Le script
refuse un transfert sans F0–F3 ordonnés, recherche LinkedIn/Reddit déclarée lue et
liée à des sources OBSERVED, compétences intégrées dans les profils, au moins deux
appels distincts de sous-agents et quatre cycles complets critique/résolution/relecture.
Le cycle idées doit précéder le démarrage de préproduction ; les autres le suivent.
Les instantanés de revue incluent `workflow_inputs_sha256` : changer contexte,
recherche, compétences, profils ou formation invalide les approbations affectées.
L'historique des critiques/corrections reste dans `workflow.json` avec ses copies
immuables ; `state.reviews` porte les approbations courantes, pas les anciens refus.

Le contrôle structurel ne peut vérifier que le réseau a réellement été consulté,
que les comportements du profil intègrent correctement les sources, ni que l'ID
vient réellement d'un outil. Relire contenus et retours de l'hôte ; aucun champ
auto-déclaré ne constitue une certification. Un brouillon ancien sans workflow
reste lisible avec avertissement ; le transfert demande un complément documenté.

## Gate obligatoire des trois skills de contrôle

Appliquer [le contrat de contrôle final](17-controle-final.md) avant signature de G5 :
site-checklist documentaire SC01–SC20, préparation Safari SF01–SF08 et web-perf
en audit uniquement ; revue seo-audit ; décision pSEO et revue des familles applicables.
G6 rejoue les contrôles sur le site réalisé avec preuves par environnement.
R25 porte cette couverture ; R20 porte les spécifications techniques et pSEO.
La revue documentaire ne certifie pas le site futur. Les tests différés correctement
spécifiés ne bloquent pas seuls G5 ; une lacune bloquante ou dépendance requise absente
interdit le transfert strict. Vérifier le fond : studio.py ne certifie pas ces revues.

## Réalisation complète et recherche hors landing

Une création de site ne s'arrête plus à G5. Exécuter D0–D4 et préparer/exécuter D5
selon [18-realisation-complete.md](18-realisation-complete.md).
R12 couvre désormais toute page publique de contenu hors landing, même courte ;
ancienne exemption de petit corpus supprimée. La recette doit prouver la recherche
fonctionnelle sur les gabarits détaillés et de listes, et les liens intégrés au corps.
`validate --stage handoff` ne prouve pas un site construit. `validate --stage release`
conserve son sens de publication autorisée et preuves live. Le rapport du contrôleur
HTML local et les preuves navigateur distinguent les résultats locaux de la production.
