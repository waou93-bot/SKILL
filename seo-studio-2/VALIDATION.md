# Vérification de la révision 2.3.0 — 13 octobre 2026

Exécution locale Windows / Python 3.12. Les scripts restent sans réseau, modèle,
CMS ou invocation de sous-agent. Les preuves de tests unitaires sont des fixtures
fictives et ne prouvent pas une préproduction réellement exécutée.

- Suite finale : `python -m unittest discover -s tests` — 129 tests, 128 réussis,
  1 ignoré (symlink indisponible sur cet hôte), aucun échec, 326.308 secondes.
- Installateur borné à seo-studio-2 : 6 tests réussis ; sauvegarde, empreintes,
  refus de corruption/concurrence, retour arrière après échec et idempotence.
- Métadonnées Skill Creator, JSON/Python, templates, liens locaux, R01–R28 et
  manifeste : contrôlés ; le manifeste est recalculé après cette note.
- Vrai Personna lu avec ses trois références ; profil critique audio produit,
  calibré par revue de scénarios et transmis à un vrai sous-agent de cette occasion.
- Trois retours réels de revue et corrections conservés dans le dossier local de
  maintenance. Trois défauts du validateur signalés puis corrigés/retestés/revus.
- Recherche publique illustrative LinkedIn/Reddit : cinq contenus exploitables
  avec limites et divergences, détaillés dans research/personas-metier-2026-10-13.md.

Cette maintenance n'a pas exécuté une préproduction entière ni formé toutes les
équipes des quatre sites. Les 29 scénarios du package ne sont pas exécutés de bout
en bout ; trois ont reçu une revue documentaire indépendante. Aucune évaluation
comparative de modèles, essai acoustique, publication ou modification des sites.
L'installation active est confirmée séparément par installation-report.json du
mainteneur, après les tests et la sauvegarde. Les anciennes observations ci-dessous
restent un historique daté, pas l'état du poste au 13 octobre.

---

# Vérification de la livraison

Date : 8 octobre 2026. Environnement de test : Linux, Python 3.13 ; code écrit pour
Python 3.10+. Aucun appel de modèle, site, CMS ou service externe par les scripts.

## Résultats réellement exécutés

`python -m unittest discover -s tests -v` : **78 tests réussis**, aucun échec.
Le journal complet est dans `research/unit-tests.txt`. Le décompte porte sur les
méthodes de test unittest ; les scénarios d'agents ne sont pas compris dedans.

Les tests couvrent initialisation en aperçu, création et idempotence ; préservation
d'un projet existant ; inventaire dynamique et doublons ; schéma et JSON ambigu ;
limites de délégation ; formation manquante ; traces de revue incohérentes ; exigences
et gates ; preuves périmées ; changements de plan/fichier invalidant une revue ;
maillage, orphelins et intentions ; données privées ; encarts payés et destinations ;
permissions de sortie ; chemins dangereux et installation sans écrasement.

## Ce que ces résultats ne prouvent pas

Ils ne démontrent pas l'utilité éditoriale d'une préproduction, l'authenticité des
preuves, une formation d'agent réelle, une revue indépendante ou des résultats SEO.
Les fixtures positives contiennent explicitement des données et sessions fictives
pour tester la structure. Un faux récit correctement formé exige une revue de fond
pour être détecté : le validateur ne prétend pas résoudre ce problème.

Les 24 scénarios comportementaux sont préparés et non exécutés. Aucune mesure
comparative entre modèles n'a été effectuée. Python 3.10 et Windows n'ont pas été
exécutés ici ; leur compatibilité n'est pas déclarée testée.

## Corpus et dépendances

Quatre domaines ont fourni du texte exploitable ; deux restent non observés.
Aucun rendu navigateur des six domaines n'a été inspecté. Les neuf SKILL.md du
socle ont été consultés sur GitHub, pas installés sur le PC utilisateur. Le vrai
/personna n'a pas été localisé et aucune formation n'est déclarée effectuée.

Le fichier `research/coverage.json` distingue le package livré des parties encore
partielles de la demande. Le registre des sources donne le périmètre réel des faits.

## Installation et intégrité

Le manifeste SHA-256 accompagne l'archive. Le contrôle final et le test de copie
locale temporaire sont consignés dans `research/package-smoke.json`. Ces contrôles
ne prouvent pas la découverte par l'hôte ni une installation sur le poste utilisateur.
Aucun dépôt GitHub, projet, site, compte ni configuration globale n'a été modifié.


## Export public du 13 octobre 2026

Les chemins personnels et identifiants locaux sont retirés de la copie destinée
à GitHub. Les références privées restent dans le registre de maintenance local.
Cette adaptation ne change aucun script, schéma, test ou contrat de workflow.
Le manifeste SHA-256 est régénéré pour les octets de cette copie publique ;
ses empreintes peuvent donc différer de la copie installée sur le poste de révision.
L'intégrité de cette copie est contrôlée avant publication. Les résultats de tests
consignés décrivent les exécutions antérieures ; aucun nouveau résultat n'est inventé.
