# Validation de la version 3.0.0

Date : 2026-10-04. Environnement de test : conteneur Linux, Python 3.13.

Exécuté : `python -m unittest discover -s ai-seo/tests -v`.
Résultat : 34 tests, 34 réussis, aucune erreur, aucun test ignoré.

Portée : fonctions de triage HTML/robots, classification de provenance, calcul du panel,
installation en aperçu, copie et empreintes, sauvegarde, restauration après erreur simulée,
préservation des documents, refus de chemins non autorisés, interfaces CLI --help.
Les données sont synthétiques et les installations de test utilisent des dossiers temporaires.
Les cinq fichiers scripts locaux testés ont été comparés par empreinte Git aux blobs publiés.

Non exécuté : installation sur le PC de l'utilisateur, détection dans son Codex, tests Windows/WSL,
scénarios comportementaux de l'agent, crawl de ses sites, rendu navigateur de ses projets,
validation WAF en production, indexation, panel réel multi-moteurs et mesure commerciale.
La compatibilité Python 3.10+ est visée par le code ; cette exécution a utilisé Python 3.13.

Le parseur robots est volontairement simplifié. Les scripts ne valident pas l'authenticité des
bots, l'existence des preuves référencées ni une causalité d'acquisition. Les limites sont dans
scripts/README.md et references/04-measurement.md.

Un arbre Git créé ne prouve pas un push : vérifier séparément le commit atteint par main.
Un push ne prouve pas une installation locale. Le rapport final doit fournir le SHA du commit
vérifié, puis le chemin et l'état de découverte seulement après une installation réellement faite.
