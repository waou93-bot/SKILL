# Contrat des livrables de chaque projet

Les fichiers ci-dessous constituent le dossier de préproduction, dans le répertoire
existant approprié. `scripts/studio.py init` les amorce sans les remplir ni les valider.
L'agent doit ensuite produire leur contenu spécifique et renseigner `state.json`.

| Fichier | Contenu exigé avant transfert |
|---|---|
| 00_REFLEXION.md | F0–F3 : problème, faits, hypothèses, options, preuves, décision et critères |
| 01_COMPETENCES.md | recherche LinkedIn/Reddit, limites, matrice compétences → rôles → comportements → calibration |
| PERSONAS/ | profils sectoriels versionnés produits via le vrai /personna, mandats et calibration |
| workflow.json | étapes, recherche, compétences, profils, vrais agents et cycles ordonnés |
| 00_CADRAGE.md | niche/type, public, but, modèle potentiel, contraintes, acquis, permissions, hypothèses/inconnues |
| 01_RECHERCHE.md | demande/langage, benchmark daté, sources, contre-preuves, limites et avantage propre |
| 02_POSITIONNEMENT.md | promesse, segments prioritaires, exclusions, parcours et test de viabilité/canal |
| 03_ARCHITECTURE.md | arborescence, politique d'URLs/indexation, taxonomie, CMS, états et migrations éventuelles |
| 04_DESIGN.md | concept, deux pistes, choix, gabarits mobile/desktop, composants/états et spécification assets |
| PROJECT_SKIN.yaml | identité concrète, choix/provenance, tokens, images, motion, exclusions/fallbacks et approbation |
| 05_CONTENU.md | clusters, sujets, V1/reste, doctrine sources/auteurs, calendrier et maintenance |
| BRIEFS/ | brief intégral par page V1 ; pas seulement titres et mots-clés |
| PILOTES/ | contenus pilotes adaptés au type de site ; toutes les affirmations étayées ou bloquées |
| 06_PARTENAIRES.md | candidats et statuts, encarts écrits, placements, variantes, disclosure, suivi, indépendance |
| 07_TECHNIQUE.md | deux stacks, ADR, data/CMS, SEO technique, performance, sécurité, tests et dépendances |
| 08_MESURE.md | objectifs/événements, accès, consentement, baseline, attribution, pilote IA si utile |
| 09_ROADMAP.md | lots, tickets, propriétaires, dépendances, capacité, budget ou inconnues, critères de sortie |
| 10_DECISIONS.md | synthèses des revues, objections, corrections, arbitrages Astra et conditions de réouverture |
| 11_QA.md | contrôles exécutés/non exécutés, preuves, couverture, P0/P1/P2, défauts et gates |
| 12_HANDOFF.md | dossier gelé, exigences, chemins, empreintes, versions, droits, limites et consignes de réalisation |
| state.json | inventaire machine des rôles, exigences, preuves, sources, pages, liens, partenaires, revues et gates |

La [couverture fan-out](14-fanout-retour-sites.md) rejoint `03_ARCHITECTURE.md` et/ou
`05_CONTENU.md`, les briefs et la recette : question/sous-question, provenance,
réponse/preuve/limite, URL propriétaire, liens et prochaine action. La baseline et
le panel pertinent restent dans `08_MESURE.md`. Aucun dossier concurrent n'est requis.
Une reprise garde `state.json` et les IDs R09/R10/R13/R17/R20/R21/R22 existants.

## Assertions de réception

- Chaque exigence applicable est reliée à un artefact existant et une preuve actuelle.
- Chaque page V1 a son brief et un chemin de navigation ; les pilotes sont réellement écrits.
- Chaque intention a un propriétaire ; chaque lien a une raison et une destination prévue.
- Chaque encart indique sa nature commerciale quand nécessaire et sa destination exacte.
- Chaque rôle affecté a une formation `/personna` tracée ; une revue indépendante est réelle.
- Chaque désaccord sur les idées, l'architecture, la roadmap et la production pilote est
  résolu ou garde le transfert bloqué ; Astra arbitre ce qui reste contradictoire.
- Chaque fait commercial ou sensible est sourcé, ses inconnues restent présentes.
- Un projet sans site live a des tests spécifiés, pas des tests de production inventés.

Le besoin de livrables dépend du type de site : justifier les `NON_APPLICABLE` prévus
par le contrat. Même lorsqu'aucune monétisation n'est pertinente, `06_PARTENAIRES.md`
explique ce choix et les formats exclus au lieu de fabriquer une offre.

## Contrôles intégrés à conserver dans les livrables existants

Selon [le contrat de contrôle final](17-controle-final.md), `11_QA.md` contient
la revue seo-audit, les tableaux SC01–SC20/SF01–SF08, le protocole ou rapport web-perf
et la revue pSEO applicable. `03_ARCHITECTURE.md` contient sa décision d'applicabilité
et les familles ; `07_TECHNIQUE.md` leur pipeline et les tests ; `08_MESURE.md`
les cohortes ; `09_ROADMAP.md` les paliers ; `12_HANDOFF.md` les tests restant à exécuter.

## Livrables supplémentaires d'une réalisation complète

En plus du dossier conservé, remettre le dépôt/code du site, tout le corpus V1,
les assets autorisés, l'index/moteur de recherche local, les données/CMS nécessaires,
les commandes réellement exécutées et un README de lancement/build/maintenance.
Documenter dans `11_QA.md` les tests locaux et les liens du corps vérifiés ; dans
`12_HANDOFF.md`, le chemin du site, la version, les commandes, le rapport HTML,
les captures/traces navigateur et les limites de publication.

## QA, sécurité et performance — contrat 3.1

Appliquer [le contrat commun](19-qa-security-performance.md) : webapp-testing pour
les interactions, cross-platform-qa pour la couverture et la méthode,
security-best-practices pour le code sécurisé et la revue applicable, web-perf pour
les mesures et recommandations. Conserver un seul registre de preuves dans 11_QA.md.
Aucun service payant requis ; lectures, tests locaux, émulation et appareils réels
restent des preuves distinctes. Les corrections respectent le mandat existant.

## Preuves de la boucle d'opportunités

Conserver baseline, filtres et indicateurs dans `08_MESURE.md`, actions priorisées et propriétaires dans `09_ROADMAP.md`, hypothèses et décisions dans `10_DECISIONS.md`, contrôles réellement exécutés dans `11_QA.md`. Après lancement, préserver `monitoring/release-state.json` ; enregistrer toute correction dans une nouvelle révision et relier sa version à la mesure. Les agrégats monitoring n'établissent pas une analyse page–requête : joindre les preuves segmentées lorsqu'elles existent. Un plan sans données est préparé, jamais déclaré performant.
