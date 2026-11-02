# Cas de validation documentaire

Ces scénarios vérifient la couverture des consignes par relecture ; ils ne sont pas une exécution autonome du skill par un autre agent.

1. Reprise après plusieurs semaines : lire index et décisions, vérifier fraîcheur et accès ; données absentes marquées inconnues.
2. Changement de positionnement : marquer les anciennes décisions remplacées, conserver les preuves et les liens, actualiser l'index.
3. Hypothèse contredite : comparer périmètre, période et source ; ne pas convertir silencieusement la nouvelle observation en causalité.
4. Baisse saisonnière : comparer segments et période annuelle quand disponible ; ne pas attribuer une baisse à une perte de position sans preuve.
5. Canonical ou noindex modifié : l'outil comparateur retourne FAIL sur deux snapshots valides et signale les champs ; la publication suit la décision autorisée.
6. Partenaires de deux sites : conserver leurs règles distinctes et refuser la comparaison de snapshots dont site_id diffère.

Les cas 5 et 6 sont couverts par les tests unitaires du comparateur. Les cas 1 à 4 sont des vérifications documentaires, pas des essais de comportement d'un agent.

