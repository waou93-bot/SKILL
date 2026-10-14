# Contrôle final : site-checklist, seo-audit et pSEO

## Chargement et périmètre

Pour une mission complète, charger les vrais `site-checklist`, `seo-audit` et
`pSEO` depuis le catalogue actif, puis leurs références applicables. Leurs chemins
locaux doivent être résolus depuis le catalogue actif ; ne pas imposer un chemin
personnel ou une installation propre à un autre hôte.
Conserver chemin, version/hash, périmètre et preuves de lecture dans `state.json`.
Ne pas relancer Organisation ni créer un dossier d'audit concurrent.
Une reprise ciblée ne rejoue que les contrôles impactés.

## pSEO : décision G1, conception G2–G4, revue G5

Évaluer explicitement si des familles de pages sont générées à partir de données
structurées. Sans système programmatique pertinent, consigner la non-applicabilité
motivée dans `03_ARCHITECTURE.md` ; ne pas imposer une production de masse.
Lorsqu'applicable, appliquer le vrai pSEO : familles/dimensions, combinaisons valides,
intention et valeur propres, données minimales, provenance/licence/fraîcheur,
URLs déterministes, collisions, gabarits et états, admissibilité à l'index,
facettes/canonical, maillage calculable et sitemaps cohérents.
Documenter dans `07_TECHNIQUE.md` ingestion idempotente, validation/quarantaine,
régénération préservant les corrections, cache, coûts, maintenance et rollback.
Prévoir dans `08_MESURE.md` les cohortes/familles et leurs limites de mesure,
dans `09_ROADMAP.md` les paliers et conditions d'arrêt.
À G5, examiner les cas fréquent, rare, incomplet, obsolète, ambigu, doublon,
erreur et sans résultat ; un échantillon ne prouve pas une couverture exhaustive.
Consigner par famille `GO`, `PILOTE`, `NOINDEX/EXCLURE` ou `DIFFÉRER`, avec raison.
La génération technique ne vaut ni publication autorisée ni indexation observée.

## seo-audit : contrôle documentaire obligatoire à G5

Appliquer seo-audit aux spécifications, briefs et pilotes, et à l'existant accessible
s'il fait partie du périmètre : exploration/indexation, fondations techniques,
on-page, utilité et preuves du contenu, maillage/autorité.
Lire ses références Google, fan-out/release, affiliation et international selon
le périmètre. Contrôler les réponses réelles des pilotes et les intentions,
pas seulement les metas. Pour chaque constat : URL/gabarit ou fichier/version,
défaut ou recommandation, impact, preuve, correction, responsable et priorité.
Sur un site futur, définir les tests HTTP/HTML/DOM, canonical, robots, sitemap,
schema et parcours ; ne pas annoncer un crawl, une indexation ou une mesure terrain.

## site-checklist : G5 documentaire, G6 sur le site réalisé

À G5, couvrir chacun des 20 points SC01–SC20 avec
`ID | point | périmètre | spécification/preuve | statut | test prévu | responsable | priorité`.
Utiliser les statuts du skill : CONFORME, À CORRIGER, NON VÉRIFIÉ, NON APPLICABLE.
CONFORME précise ici « spécification vérifiée » et ne valide jamais le futur rendu.
Les vérifications de fonctionnement sans site restent NON VÉRIFIÉES avec test prévu.
NON APPLICABLE exige une justification liée au parcours, pas un manque d'accès.
Charger le module Safari de site-checklist et préparer SF01–SF08 séparément des SC.
Charger web-perf en mode audit uniquement pour préparer son protocole ; les mesures
non exécutées restent NON VÉRIFIÉES. Consigner ses constats/recommandations séparément.

À G6, après réalisation dans l'environnement autorisé, rejouer la checklist sur
les routes et parcours réels, ainsi que seo-audit et les contrôles pSEO applicables.
Distinguer local, preview et production, WebKit automatisé, Safari macOS réel et
Safari iOS sur appareil réel. Ne pas déclarer Safari validé sans les preuves requises.
Respecter site-checklist : web-perf produit des recommandations non appliquées ;
leur mise en œuvre demande une autorisation explicite visant les optimisations.
Aucun ajout de traceur, compte, message de test, ouverture d'espace privé ou déploiement
ne découle de cette intégration.

## Preuves et gate de transfert

Conserver les trois revues dans `11_QA.md`, les décisions dans `10_DECISIONS.md`,
les corrections dans le backlog existant et les tests différés dans `12_HANDOFF.md`.
Relier dépendances, artefacts et preuves aux exigences existantes R03, R09/R10,
R12/R13, R17, R19/R20, R22/R24 et R25/R26 ; conserver leurs IDs et les anciens dossiers.
G5 exige les trois compétences chargées, la décision d'applicabilité pSEO,
la revue seo-audit et la couverture documentaire SC/SF/performance.
Un skill requis absent ou une lacune bloquante des spécifications empêche le transfert
strict. Les tests du site futur correctement spécifiés et différés à G6 ne bloquent
pas seuls une préproduction ; ils interdisent de déclarer le site testé.
Les P0/P1 ouverts restent bloquants selon le contrat Studio. Préserver aussi les
réserves Safari et les critères de recommandation de publication de site-checklist.
Le validateur structurel ne prouve ni invocation des skills ni conformité des revues :
contrôler leurs contenus et les preuves de l'hôte avant de signer G5/G6.

## Application à la réalisation indépendante

Les contrôles s'exécutent avec les capacités locales de l'hôte selon
[18-realisation-complete.md](18-realisation-complete.md), sans framework d'agents
ou service payant requis. Remplacer l'ancienne exemption « petit corpus » par la
recherche obligatoire sur chaque page publique de contenu hors landing.
Contrôler aussi les ancres réellement intégrées au corps, leurs pages cibles et
leurs fragments. Les revues pSEO/seo-audit/site-checklist restent celles intégrées.

## QA, sécurité et performance — contrat 3.1

Appliquer [le contrat commun](19-qa-security-performance.md) : webapp-testing pour
les interactions, cross-platform-qa pour la couverture et la méthode,
security-best-practices pour le code sécurisé et la revue applicable, web-perf pour
les mesures et recommandations. Conserver un seul registre de preuves dans 11_QA.md.
Aucun service payant requis ; lectures, tests locaux, émulation et appareils réels
restent des preuves distinctes. Les corrections respectent le mandat existant.
