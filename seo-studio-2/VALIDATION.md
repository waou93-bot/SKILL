# Vérification 3.6.0 — 15 octobre 2026

247 tests distincts consolidés : 246 réussis, 1 ignoré (symlink Windows).
Suite complète 245 tests, puis correction de trois fixtures de bundle et relance
des 19 tests fichiers/installation ; 35 tests moteur finaux après critères Design DNA.
Ce bilan consolide les dernières exécutions, sans prétendre à un run unique entièrement vert.
Chromium réel : six visites de pages et deux scénarios d'interaction sur fixture locale ;
interactions du template original également exécutées. Quatorze tests HTTP produits locaux.
Installation neuve et relance identique vérifiées ; projet incomplet correctement bloqué.
Benchmark sans plafond d'URL et revues niche/profondeur/cinématique/composants obligatoires.
Fixtures synthétiques, pas une livraison client ou une approbation visuelle réelle.
Personna conservé, aucun outil payant obligatoire, aucun déploiement public.

# Vérification 3.3.0 — 14 octobre 2026

- Suite complète finale : 197 tests en 480.812 secondes, aucun échec,
  un test symlink ignoré faute de capacité OS. Les tests antérieurs restent inclus.
- Registre SERP : sources, architecture et approbation liées ; modification
  coordonnée d'une source et de son empreinte rend l'ancienne approbation caduque.
- Publication : les preuves HTTP/navigateur/Lighthouse correspondent au même
  site et aux routes attendues ; source brute et métriques normalisées rapprochées.
- Pilote local réel : cinq routes HTTP et Chromium mobile, dont /auteur/.
  Lighthouse 13.5.0 : LCP 751.171 ms, CLS 0, TBT 0.
  Une mesure mobile locale représente le gabarit commun ; aucune donnée terrain.
- Quatre sessions textuelles neuves comparant les consignes 3.2/3.3 sur affiliation
  et SERP. La règle d'affiliation commune est adoptée ; les deux versions refusent
  les positions inventées. Une réponse 3.3 fait 180 mots pour « moins de 180 » :
  petit écart de format conservé dans le bilan, aucune réussite universelle affirmée.
- Auteur Nicolas par défaut, nom du site adapté, réserve capillaire contextualisée,
  route publique V1 requise. La bio ne prouve pas les relectures ou tests annoncés.
- Mode lite conserve R01–R28, la recherche interne et la formation Personna.
- Aucun fichier Personna modifié, évaluateur embarqué identique à la version 1.2.
  Aucun outil payant obligatoire. Lighthouse a été exécuté gratuitement dans un
  cache temporaire du workspace ; aucun compte, achat ou publication de site.

Ce pilote vérifie le protocole technique, pas une niche commerciale, une formation
Personna complète, Safari réel, des résultats SEO ou l'authenticité cryptographique
des pièces locales. Les tests de contrats utilisent des fixtures explicitement
synthétiques ; elles ne servent pas de preuve de lancement d'un projet réel.
Les contrôles ci-dessous restent historiques.

# Vérification 3.2.0 — 14 octobre 2026

- Suite complète : 154 tests en 799.162 secondes, aucun échec,
  un test symlink ignoré faute de capacité OS ; 11 tests d'intégration inclus.
- Personna : 17 tests de régression réussis. Évaluateur intégré byte-identique.
- Dix sessions textuelles neuves, revue séparée des 14 critères de fond et quatre
  assertions regex : PASS sans/avec. Aucun gain causal sur baseline démontré.
- Preuves textuelles actuelles importées dans un dossier Studio synthétique :
  acceptées, puis bloquées STALE après modification du profil ; restauration acceptée.
- Modèle/paramètres non observés, traces finales sans journal complet des outils.
  Le parcours métier complet recherche/entretien/site n'a pas été exécuté ici.
- Aucun outil payant obligatoire ; recherches et entretien Personna conservés.

Les résultats 3.1.0 ci-dessous sont historiques.

# Vérification 3.1.0 — 14 octobre 2026

Maintenance du package sous Windows / Python 3.12.10, avec répertoire temporaire
dans le workspace après refus du temporaire sandbox initial.

- Suite complète : 142 tests en 574.068 secondes, aucun échec, un test
  symlink ignoré (capacité OS indisponible). Trois tests de dépendances nouveaux inclus.
- Contrôleur HTML final après correction canonical : 11 tests réussis séparément.
- JSON, liens locaux, IDs R01–R28, diff borné et intégrité SHA-256 contrôlés.
- Revue séparée des 16 SKILL.md intégrés et des corrections ; limites dans
  research/audit-3.1.md. Cinq scénarios comportementaux ajoutés, non exécutés.
- Aucun fichier personna modifié. Aucun outil payant obligatoire ajouté.

Les fixtures valident la structure ; elles ne prouvent ni formation personna,
ni navigateur, ni sécurité d'un site, ni performance terrain ni résultat SEO.
Les preuves historiques ci-dessous conservent leur date et leur périmètre.

---

# Vérification documentaire 2.3.2 — 13 octobre 2026

Ajout ciblé des accès produits affiliés vers les partenaires, des boutons
orientés action et de la mention d’affiliation séparée. Contrôles exécutés :
diff borné, liens locaux et ancres, JSON, conservation des IDs R01–R28 ;
seule la formulation de R16 évolue. Manifeste recalculé et vérifié.
Aucun script ni schéma machine modifié. Aucun lien partenaire réel, moteur
ou rendu de site testé ; aucun site publié. Les suites historiques ci-dessous
ne constituent pas une nouvelle exécution pour cette révision documentaire.

---

# Vérification documentaire 2.3.1 — 13 octobre 2026

Ajout ciblé de la recherche en tête des rubriques riches en contenus.
Contrôles exécutés : diff borné aux instructions, liens locaux et ancres,
JSON et conservation des IDs R01–R28 ; seule la formulation de R12 évolue.
Le manifeste est recalculé et vérifié pour cette copie de travail.
Aucun script de production ni schéma machine modifié ; aucun moteur de recherche
de site implémenté ou testé, aucune publication. Les tests de la révision
précédente ci-dessous restent des résultats historiques, sans nouvelle exécution.

---

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

## Révision 3.2.0 : contrat Personna

La suite `tests/test_personna_integration.py` vérifie le recalcul des sessions,
les rapports status-only, empreintes caduques, requêtes et provenance modifiées,
revues anciennes, chemins sortants et identité de l’évaluateur avec Personna.
Les fixtures sont synthétiques ; la réalité des sessions reste soumise à revue.
