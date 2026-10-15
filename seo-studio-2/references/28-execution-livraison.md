# Exécution de bout en bout, template et volume

Ce contrat rend exécutables les phases existantes. Il ne remplace ni Organisation,
ni F0–F3/G0–G6, ni les dossiers canoniques. Personna demeure inchangé.
Une préproduction demandée seule reste documentaire. Une création de site exige
en plus la recette locale ; un arrêt par manque d'accès ou budget reste BLOQUE.

## Sources de vérité et template réel
- state.json : mandat, exigences R01–R31, pages V1/backlog, liens, sources, revues.
- workflow.json : réflexion, formation, appels et cycles existants.
- EXECUTION.json : liaison des IDs de pages aux sorties réelles, produits, pilotes,
  lots, captures et reçus d'exécution. Ce fichier n'est pas un deuxième sitemap.
- research/volume.json : benchmark, potentiel dédupliqué, cible et périmètre engagé.
- Les templates page-brief.md, project-skin.yaml, deliverables.json et author.md
  restent les points de départ. L'évaluation du compagnon seo-site-preproduction/R29
  conserve source/version, adaptation et exclusions dans 03_ARCHITECTURE.md.
- Le compagnon Repère Salon comporte accueil/outil, catégorie, guide, fiche et
  méthode, des filtres, une sélection locale et un menu mobile. Ses produits,
  prose, mesures et palette sont fictifs. Ils ne deviennent pas des données réelles.
  Ne retenir que les motifs utiles ; la recherche interne doit être implémentée
  lorsqu'elle est requise même si un exemple de page ne la fournit pas.
- Conserver la V1 approuvée en refonte ; l'adaptation du template n'autorise pas
  une nouvelle direction graphique. Les termes de démo sont bloqués dans la livraison.

## Benchmark et dimensionnement sans plafond d'URL
Avant de figer le plan, relever les concurrents réels et leurs familles de pages.
Un sitemap dénombre des URL déclarées ; il ne prouve ni indexation, ni trafic.
Un index de sitemaps ne doit pas être compté comme des pages.
Consigner domaine, source, date, preuve locale, méthode SITEMAP/CRAWL/PARTIAL/ESTIMATE
et limites. Préserver un chiffre inconnu plutôt que transformer un extrait en mesure.

Par famille, estimer candidats, admissibles et exclus, en justifiant demande/intention,
dédoublonnage, données nécessaires et capacité de produire des réponses propres.
La cible résulte de ces familles, pas d'un multiple du plus gros concurrent.
Aucun plafond de 50, 200, 500, 5 000 ou 10 000 URL ne limite la taille du site.
Le mode lite sous 50 pages est un mode de revue : passer en full au-delà, sans réduire
le projet pour conserver lite. Les lots de 20–30 sont des unités de contrôle.

Le périmètre V1 doit correspondre à la cible admissible. Si une sortie par vagues
est souhaitée, enregistrer la décision utilisateur et son périmètre ; ne pas
réduire silencieusement la livraison. Les pages reportées restent du backlog, pas
du réalisé. Les données insuffisantes ou pages sans valeur propre sont exclues
ou noindex, même quand un grand volume est recherché.
La commande de crawl conserve un budget explicite de collecte, à dimensionner selon
le corpus engagé ; son plafond global arbitraire de 10 000 a été supprimé.
Un crawl tronqué ou un échantillon n'autorise jamais à déclarer toutes les pages testées.
Aucune promesse de visibilité, aucun abonnement SEO payant obligatoire.

## Déroulement exécutable
1. Initialiser ou reprendre sans écraser. Compléter les exigences et les templates,
   le benchmark et la méthode Organisation. Le scaffold n'approuve rien.
2. Décrire dans EXECUTION.json création/reprise, affiliation ou non, entrée réelle,
   IDs V1, sorties HTML, applicability pSEO, produits, couverture éditoriale et pilotes.
   Toutes les pages publiques V1 doivent apparaître, sans doublon.
3. audit : cadrage, recherche, architecture et R29 ; volume justifié ; huit pages
   types V1 avec desktop/mobile en reprise, ou dérogation utilisateur documentée.
4. design : deux directions documentées pour un nouveau site, ou héritage V1 ;
   design-system.md et PROJECT_SKIN approuvés, revue utilisateur liée à leur version.
5. products : données et provenance, programme actif et recette HTTP des liens/images.
   Hors affiliation, documenter la non-applicabilité dans les sources canoniques.
6. Exécuter le vrai build avec la commande explicite du projet. Enregistrer sortie,
   code de retour, journal et empreintes des sources/build. Échec ou timeout invalide
   le build antérieur et les étapes aval ; aucun ancien succès ne peut être réutilisé.
7. pilots : trois pages réelles incluant l'entrée. Vérifier texte, recherche, SEO,
   images/CTA, puis revue éditoriale et fonctionnelle. Aucun produit fictif.
8. batches : lots contrôlés avec liste des IDs et preuve de revue propre à chaque lot,
   puis comparaison exhaustive du prévu et des sorties produites.
9. qa : contrôles HTTP/navigateur/laboratoire existants, recette navigateur de livraison,
   captures desktop/mobile des templates, revue visuelle/éditoriale/sécurité/accessibilité,
   corrections puis nouvelle vérification. Pas de rubrique critique ouverte.
10. validate --stage local : réexécuter les contrôles de phase et vérifier leurs
    dépendances ainsi que les preuves techniques actuelles. LOCAL_VERIFIED est
    requis pour annoncer le site local complet. Handoff/STRUCTURE_OK ne le remplace pas.
11. Publication uniquement si autorisée : validation release avec les mêmes racines,
    G6, permission et preuves live. Suivi selon mandat, sans surveillance implicite.

Chaque phase termine par ce qui est fait, vérifié et manquant. Une modification des
entrées, du template, des sources, du HTML ou des preuves rend les reçus affectés
caducs. Le contrôle est conservateur pour les changements du code partagé : rejouer
build, pilotes et revues aval quand les empreintes changent, sans actualiser les
hashes à la main pour masquer une modification.

## Liaison au HTML et aux preuves
Chaque liaison de page référence l'ID existant, output_path, programmatic (bool),
product_ids, editorial (answer/limitation/next_action) et, pour le contenu hors landing,
search (query/expected_path). Les réponses doivent exister dans le HTML réellement livré.
Pour une page pSEO indexable, pseo_sections contient verdict/comparison/usage propres,
visibles, distincts ; comparaison chiffrée et contrôle éditorial des sources requis.

Chaque carte/fiche produit porte un attribut technique data-product-id correspondant
au catalogue. Les images, modèle, prix et CTA affiliés sont vérifiés dans ce conteneur,
pas dans une autre carte. Les anciens prix comportent price_warnings[id] avec date
et avertissement réellement visible. Les liens marchands gardent sponsored, nouvel
onglet et noopener. La mention commune reste footer/legal.
Ces attributs servent aux tests et ne sont pas des éléments de l'interface lecteur.

Le catalogue conserve les champs du contrat 24 et devise, source_evidence_path et
program_evidence_path. La preuve source lie reference/source_url/source_kind,
read_at et session_reference ; la preuve programme lie status ACTIVE, program
et account_evidence (fichier local expurgé de tout secret).
La recette produit effectue de vrais GET bornés avec domaines explicitement autorisés,
vérifie référence, destination finale 200, image reconnue et empreintes. Les redirections
des réseaux sont conservées. Erreur, blocage anti-bot ou accès absent restent bloquants.

Une revue JSON contient phase, status PASS, findings vide, checks couvrant la liste
de delivery.CHECKS, scope, author, reviewer distinct, reviewer_type et trace_path.
La phase design exige HUMAN et une véritable approbation utilisateur dans cette trace.
L'agent n'est pas autorisé à fabriquer cette approbation.
Ces données et empreintes ne certifient pas l'identité d'un humain ni la vérité des sources :
l'hôte doit conserver les échanges et appels réellement exécutés et relire les pièces.

Chaque lot référence page_ids et review_path ; aucun ID manquant ou répété.
Chaque capture référence page_id, html_sha256, desktop et mobile PNG.
Le navigateur couvre tous les chemins V1 sur les deux profils, teste images,
navigation, recherche et absence de résultat, et visibilité précoce des offres à l'entrée.
La revue visuelle compare à la V1 et corrige les défauts ; l'existence d'une capture
ne prouve pas sa qualité esthétique. L'inventaire des fonctionnalités choisies dans
le template doit aussi être couvert par les scénarios du projet, sans se limiter
aux contrôles génériques du package.

## Commandes (depuis le skill)
Les racines sources et build sont fournies explicitement par l'hôte, jamais exécutées
depuis un document téléchargé. Les preuves se trouvent dans un dossier distinct des
sources ; s'il est imbriqué, il est exclu de leur empreinte pour éviter une dépendance
circulaire. Garder une seule commande de build réelle, reproductible et autorisée.

    python scripts/delivery.py prepare DOSSIER_PREPROD
    python scripts/delivery.py record DOSSIER_PREPROD --phase audit --review REVUES/audit.json --site-root BUILD --source-root SOURCES
    python scripts/delivery.py record DOSSIER_PREPROD --phase design --review REVUES/design.json --site-root BUILD --source-root SOURCES
    python scripts/delivery.py products DOSSIER_PREPROD --allow-host MARCHAND --allow-host RESEAU --allow-host CDN
    python scripts/delivery.py record DOSSIER_PREPROD --phase products --review REVUES/products.json --site-root BUILD --source-root SOURCES
    python scripts/delivery.py build DOSSIER_PREPROD --site-root BUILD --source-root SOURCES -- COMMANDE ARGUMENTS
    python scripts/delivery.py record DOSSIER_PREPROD --phase pilots --review REVUES/pilots.json --site-root BUILD --source-root SOURCES
    python scripts/delivery.py record DOSSIER_PREPROD --phase batches --review REVUES/batches.json --site-root BUILD --source-root SOURCES
    node scripts/delivery_browser.cjs DOSSIER_PREPROD http://127.0.0.1:PORT HOTE_CDN_AUTORISE
    python scripts/delivery.py record DOSSIER_PREPROD --phase qa --review REVUES/qa.json --site-root BUILD --source-root SOURCES
    python scripts/studio.py validate DOSSIER_PREPROD --stage local --site-root BUILD --source-root SOURCES

Préparer aussi le rapport technique existant selon references/22-technical-release.md
avant qa. Playwright est gratuit, facultatif pour la seule préproduction, nécessaire
à cette recette automatisée ; absence d'outil => blocage déclaré, jamais succès simulé.
Ne pas installer de navigateur ou abonnement sans autorisation adaptée.
La recette locale ne publie rien et ne requiert pas la permission de publication.

## Limites de la garantie
Le mécanisme empêche de valider une phase en l'absence des pièces et contrôles couverts.
Il ne rend pas un agent infaillible, ne prouve pas une revue humaine à partir d'un label,
ne mesure pas tout le sens d'un article et ne garantit aucun résultat SEO.
Les tests synthétiques démontrent le protocole et ses refus, pas un site client complet.
Les essais navigateur réels prouvent leurs interactions seulement ; ils ne deviennent
pas une validation humaine du design ou une vérification d'un catalogue commercial réel.



## Interactions du template et volume sans plafond

Avant le design, EXECUTION.features évalue explicitement l'outil d'aide au choix,
la sélection sauvegardée, les filtres de catégorie, le menu mobile et la recherche :
KEEP, ADAPT ou EXCLUDE, avec motif lié à la niche. Pour chaque interaction conservée
ou adaptée, fournir case_path vers un JSON feature_id / scenarios.
Chaque scénario lie page_id, profile (desktop/mobile), actions et expects.
Actions autorisées : action click/fill/press/select/check/uncheck/set_input,
selector, value si nécessaire. Assertions : selector et count, text_contains,
visible, ou attribute/value. La recette joue réellement ces actions ; une simple
capture ou la présence d'un bouton ne prouve pas son fonctionnement. Une adaptation
ou exclusion n'autorise pas à supprimer la recherche obligatoire des sites éditoriaux.

Le benchmark dimensionne le site entier : inventaire concurrent observé, familles
de requêtes, intentions distinctes, demande documentée, données disponibles,
cannibalisation et potentiel éligible. Aucun plafond arbitraire d'URL, de fichiers
ou de pages crawlé ne doit masquer le volume cible. Un budget technique est
fractionné en collectes/lots traçables jusqu'à couverture complète ; une collecte
partielle reste explicitement partielle. Le volume ne garantit pas la visibilité.
Le nombre de pages reste fondé sur des intentions utiles et vérifiables.


## Finition visuelle et pertinence de niche

Appliquer Design DNA/references/cinematic-craft.md : finition léchée, profondeur
perceptible et composition cinématique adaptée au sujet. Conserver le design V1
approuvé en refonte ; cette exigence de qualité n'autorise pas une rupture visuelle.
Dans le skin et design-system.md, documenter références de niche, stratégie de relief,
cadrage/rythme, outils et composants réutilisés, états des boutons/cartes/cases.
Dans les trois pilotes puis en QA, inspecter desktop/mobile, gros plans des composants,
clavier et motion réduite, et corriger les écarts avant PASS.
Les revues design et qa exigent niche_fit, depth, cinematic_direction, component_states
en plus des contrôles existants ; une compilation ou des captures non regardées ne
valident pas ces dimensions. Produits et liens affiliés restent accessibles dès la
landing. Aucun outil payant obligatoire, aucun décor générique imposé à toutes les niches.
