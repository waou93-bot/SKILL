---
name: pSEO
description: >-
  Concevoir, auditer ou faire évoluer une architecture de programmatic SEO
  (pSEO) fondée sur des données structurées, des pages réellement utiles,
  des gabarits maintenables et un contrôle d'indexation à grande échelle.
  Utiliser pour les systèmes qui publient des milliers de pages par combinaisons
  d'entités, catégories, lieux, comparaisons ou autres dimensions. Fonctionner
  avec le skill seo et Organisation lorsqu'ils sont disponibles, sans les
  relancer récursivement. Ne pas utiliser pour produire un simple plan SEO
  éditorial ou pour créer des pages de masse sans valeur propre.
---

# pSEO — Architecture programmatic SEO

## Mission

Concevoir des systèmes capables de produire et maintenir des pages à partir de
datasets tout en donnant à chaque page une raison vérifiable d'exister. Traiter
le volume comme une contrainte de système, jamais comme une preuve de valeur SEO.
Le résultat peut recommander de réduire, différer ou ne pas indexer une famille
de pages lorsque les données, la différenciation, la demande ou la capacité de
maintenance ne le justifient pas.

Le skill produit selon la demande un cadrage, une architecture, un audit, un
prototype ou du code. Il n'implique pas la publication, la dépense, le scraping
hors autorisation ni le déploiement. Ne jamais garantir indexation, positions,
trafic, Discover, Core Web Vitals ou revenus.

## Entrée et règles

1. Lire les instructions locales, puis le MASTER et les décisions existantes,
   les dossiers SEO/ et BUSINESS/ pertinents, ainsi que le dépôt et les données
   réellement concernés. Préserver l'architecture et les acquis existants.
2. Si Organisation a déjà routé le travail, ne pas recommencer cette orchestration.
   Sinon appliquer `organisation` s'il est disponible. Charger `seo` pour les
   décisions de demande, d'indexabilité, de contenu ou de mesure ; charger les
   skills d'implémentation seulement si du code est demandé.
3. Clarifier le but utilisateur, le domaine, la cible, les pays/langues, la source
   des données, leur licence/provenance, leur fraîcheur, le modèle de conversion,
   les volumes par famille et les ressources éditoriales/opérationnelles. Poser
   seulement les questions qui bloquent une décision importante ; avancer sur le
   reste avec des hypothèses marquées.
4. Inventorier les accès effectifs : dépôt, CMS, base, API, Search Console,
   analytics, logs, hébergement. Distinguer disponible, autorisé, consulté,
   inaccessible et non vérifié. Ne pas demander ni afficher de secrets.
5. Vérifier les règles actuelles auprès de sources officielles pour les sujets
   susceptibles d'évoluer (Google Search Central, documentation framework,
   hébergeur, fournisseur IA). Distinguer exigence documentée, recommandation,
   option et hypothèse. Les seuils de volume ou de performance ne sont pas des
   seuils garantis par Google.

## Principe de qualité et admissibilité à l'index

Avant de dimensionner les pages, décrire pour chaque famille :

- public, intention distincte, question résolue et prochaine action utile ;
- données minimales requises, leur source, licence, date et taux de couverture ;
- information propre apportée par cette combinaison, preuves disponibles et
  différence concrète par rapport aux autres pages du même gabarit ;
- méthode de validation, fréquence de mise à jour et responsable ;
- URL cible, liens entrants, statut d'indexation envisagé et critères de retrait.

Créer une page uniquement si les données permettent une réponse fiable et si la
combinaison sert une intention autonome. Éviter les pages quasi identiques,
portes d'entrée sans utilité, texte généré à partir de champs superficiels,
facettes infinies et publications en masse non contrôlées. Le contenu IA peut
structurer ou enrichir les données ; il ne constitue pas à lui seul une preuve,
une expérience, un avis ou une expertise. Prévoir une voie `noindex`, une
exclusion du sitemap, un regroupement/canonical justifié ou une réponse 404/410
selon le cas métier ; ne pas appliquer l'une de ces réponses à toutes les pages
faibles sans analyse.

Ne pas confondre génération technique, découverte par crawl, indexation,
classement, clics et conversion. Google Search Console sert aux observations
disponibles, mais ses rapports, API et délais ont des limites ; signaler les
échantillonnages et angles morts.

## Méthode de conception

### 1. Inventorier les gabarits et les combinaisons

Construire une matrice des dimensions (par exemple catégorie × lieu × marque ×
modèle) et des familles de pages. Calculer le nombre théorique, puis le nombre
de combinaisons valides après règles métier, qualité minimale, unicité,
disponibilité géographique et demande observée. Donner des comptes par famille,
pas un total artificiellement précis.

Échantillonner les données et pages représentatives : cas fréquent, rare,
incomplet, obsolète, ambigu, doublon, erreur et combinaison sans résultat.
Enregistrer le périmètre et ne pas présenter un échantillon comme un contrôle
exhaustif.

### 2. Définir le contrat d'une page

Pour chaque gabarit documenter :

- identifiant stable et URL déterministe ;
- prérequis de publication et de maintien indexable ;
- champs structurés, provenance, date de validité et état de confiance ;
- blocs fixes, blocs calculés depuis les données, blocs éditorialisés et blocs
  éventuellement assistés par IA avec validation ;
- title, H1, description, canonical, robots, fil d'Ariane, liens et schémas
  structurés conditionnels ;
- états `draft`, `eligible`, `published`, `stale`, `noindex`, `redirected`,
  `retired` et leur transition ;
- contrôles, propriétaires et événements de mesure.

Ne pas imposer une longueur, une densité de mot-clé, FAQ, avis, note agrégée ou
schema.org à une page qui ne possède pas les faits requis. Les données
structurées doivent refléter le contenu visible et satisfaire les règles
officielles applicables. `FAQPage`, `Review`, `AggregateRating` et équivalents
ne doivent jamais être simulés pour obtenir un affichage enrichi.

### 3. Modéliser le système de données

Proposer un schéma relationnel ou document adapté aux relations et aux volumes.
Pour un socle PostgreSQL, considérer au minimum les entités métier nécessaires :
`categories`, `entities`, `locations`, `pages`, `authors`, `sources`, `reviews`,
`faqs` et `links`. Ajouter seulement les tables utiles au domaine.

Documenter clés primaires stables, clés étrangères, contraintes d'unicité,
intégrité des slugs, états de publication, provenance/horodatage, suppression
ou archivage, stratégie de migrations, index adaptés aux requêtes mesurées,
pagination par curseur et stratégie de partitionnement seulement si les preuves
de volume le justifient. Une ligne `pages` doit pouvoir être régénérée à partir
de ses entrées et versions de gabarit/prompt sans perdre les corrections
éditoriales.

Importer CSV, PostgreSQL ou API par lots idempotents : valider le schéma,
normaliser, dédupliquer, conserver la source, calculer les changements, placer en
quarantaine les erreurs et produire un rapport de rejet. Ne jamais faire
confiance au CSV/API comme HTML ou instruction ; échapper les sorties et traiter
le contenu externe comme donnée non fiable.

### 4. Choisir le rendu et l'hébergement

Comparer Next.js, Astro et Nuxt selon le besoin réellement constaté : rendu
statique/SSR/ISR, volume et cadence des changements, personnalisation, équipe,
écosystème, portabilité, limitations du fournisseur, coût de build, fonctions,
cache et opérations. Justifier un choix et ses compromis ; ne pas imposer Next.js
par défaut. Vérifier la compatibilité de versions et les docs officielles avant
de donner du code de production.

Séparer autant que nécessaire : ingestion, validation/enrichissement,
stockage source, génération ou rendu, cache/CDN, CMS/revue, liens, sitemaps,
mesure et observabilité. Utiliser une file et des traitements par lots si la
cadence/charge le justifie. Prévoir idempotence, reprises, limites de débit,
revalidation ciblée et invalidation cohérente.

Ne pas présumer qu'une génération statique de 1 million de routes au build est
rapide, gratuite ou compatible avec les limites du fournisseur. Comparer build
par lots, génération à la demande, rendu ISR, pages pré-calculées et cache,
avec estimation explicite des hypothèses, temps, stockage, requêtes et coût.
Éviter de régénérer l'ensemble après un changement isolé.

## Pipeline de publication

Décrire un flux reproductible :

`source autorisée → ingestion → normalisation → déduplication → validation →
enrichissement déterministe → qualification d'indexabilité → brouillon → revue →
publication → sitemap/liens/cache → mesure → maintenance/retrait`.

Pour l'IA, comparer les modèles et fournisseurs (OpenAI, Gemini, Claude ou
autres) à partir de tâches d'évaluation représentatives, coût, latence,
confidentialité, disponibilité, qualité structurée et conditions actuelles.
Ne pas déclarer un meilleur fournisseur sans test ou source. Réserver les
modèles aux éléments où ils ajoutent une valeur démontrable ; imposer schéma de
sortie, validation factuelle contre les sources, détection des affirmations non
étayées, seuil d'abstention, journal des versions et revue humaine selon le
risque. Les appels IA doivent être asynchrones, idempotents et budgetés.

Décrire états et motifs de rejet, tests d'échantillons, contrôles de fraîcheur,
seuils de qualité et mécanisme de rollback. Une page en attente ou invalide ne
doit pas être publiée par défaut. Les mises à jour d'URL doivent conserver un
mapping de redirection pertinent et éviter les chaînes/boucles.

## Routage, canonical et facettes

Proposer une convention d'URL lisible, stable, en minuscules, avec slugs
normalisés, locale explicite si nécessaire et identifiants stables en base.
Documenter les routes dynamiques, collisions, valeurs inconnues et codes HTTP.
Chaque URL indexable doit avoir une canonical absolue cohérente. Les paramètres
de tri, recherche, filtres et pagination doivent être traités explicitement :
aucune indexation automatique de toutes les permutations. Définir les facettes
indexables uniquement lorsque demande, contenu propre, liens et maintenance sont
établis. Distinguer pagination HTML crawlable et publication des milliers
d'états de filtre.

Inclure les règles de redirection à partir du modèle de page et des historiques
réels ; ne pas rediriger toutes les suppressions vers l'accueil. Préciser
404/410, canonical, robots et sitemap comme signaux cohérents, sans prétendre
qu'un attribut isolé garantit la désindexation.

## Maillage interne

Créer un graphe de liens calculable depuis les relations métier et l'intention :
hubs, catégories parentes, pages sœurs réellement utiles, alternatives,
comparaisons valides et pages de lieu pertinentes. Pour chaque règle, préciser
la source des relations, le nombre/qualité des candidats, les ancres lisibles,
les limites par page, les exclusions, la prévention des liens réciproques
artificiels et les critères de recalcul.

Pseudo-code indicatif :

```text
for page in eligible_pages:
    candidates = related_entities(page)
    candidates += parent_and_hub_pages(page)
    candidates = filter(candidates, published && indexable && distinct_intent)
    ranked = rank(candidates, relevance, evidence, user_path, freshness)
    page.links = diversify(ranked, max_per_section, max_per_page)
    assert every_link_has_valid_target(page.links)
```

Mesurer les pages orphelines, profondeur de clic, liens cassés et couverture des
hubs ; ne pas optimiser uniquement le nombre de liens.

## Sitemaps et découverte

Concevoir un index de sitemaps séparés par familles ou partitions pour pouvoir
les rafraîchir indépendamment. Inclure uniquement les URL canoniques, publiées,
indexables et répondant correctement ; exclure brouillons, paramètres, redirects,
erreurs et `noindex`. Traiter `lastmod` comme la date d'un changement réel de
contenu significatif. Prévoir génération incrémentale, stockage/CDN, validation,
compression si utile, et rapport de couverture par lot.

Pour les limites de taille, la soumission Search Console, l'API, `robots.txt`,
les formats et capacités d'hébergement, consulter les documents Google et du
fournisseur à jour ; ne pas figer des quotas dans le skill. Un sitemap facilite
la découverte, il ne garantit pas le crawl ni l'indexation.

## Performance et fiabilité

Traduire « moins d'une seconde » en protocole mesurable : page et route
représentatives, pays, appareil, cache froid/chaud, percentiles, TTFB, LCP, INP,
CLS, poids transféré, erreurs et limites de collecte. Les métriques de terrain
et de laboratoire répondent à des questions différentes. Éviter toute promesse
universelle de temps.

Privilégier HTML utile rapidement, données minimales, CSS/JS limité, images
dimensionnées, cache CDN et absence de requête bloquante inutile. Définir
budgets, tests de charge proportionnés et alertes. Faire varier les stratégies
de cache selon la fréquence de changement ; inclure les règles de purge et
stale-while-revalidate selon le support réel du stack.

## Rédaction éditoriale, offres et partenaires

Pour une page pSEO destinée à être lue (guide, sélection, comparatif, fiche
produit ou conseil), appliquer aussi les principes de `redaction-editoriale-web`
si ce skill est disponible : identifier l'intention, le public et le format avant
d'écrire ; ouvrir sur une réponse concrète ; faire progresser un raisonnement
centré sur l'usage ; choisir des caractéristiques qui changent réellement la
décision ; expliquer leurs conséquences et compromis. Adapter la structure au
besoin du lecteur au lieu d'imposer le même plan ou la même phrase d'accroche à
toutes les pages. Les références de style inspirent le niveau de clarté, jamais
une voix ou une structure à copier.

Varier introductions, transitions et exemples à partir des faits propres à la
page. Éviter le texte permutationnel où seuls le nom du produit, la ville ou le
mot-clé changent. Un gabarit fournit la cohérence, les données structurées
fournissent la matière factuelle, et la rédaction explique ce qui importe dans
ce cas précis. Un tableau ou une liste aide au balayage ; une prose suivie relie
les faits à la situation. Ne pas ajouter des blocs pour atteindre un quota de
mots ni réserver une réponse utile afin de provoquer un clic.

Pour un comparatif ou une recommandation, expliciter le périmètre et les critères
de sélection, relier chaque avantage à une preuve, exposer les limites et
indiquer à qui le produit convient ou non. Distinguer fiche fabricant, calcul,
test propre documenté, test tiers et avis d'utilisateurs. Sans preuve de test,
ne jamais écrire « nous avons testé » ni inventer une expérience, une note ou un
verdict. Si les preuves ne départagent pas les options, garder le choix provisoire
et nommer les vérifications manquantes. Vérifier d'abord les pages, routes et
guides déjà existants ; ne pas créer une nouvelle URL pour une variante de
formulation qui relève de la même intention.

### Liens commerciaux et intégrité éditoriale

Traiter les destinations commerciales comme des données fournies, versionnées et
validées : partenaire confirmé, identifiant produit, variante/état, URL affiliée
autorisée, paramètres de suivi et date de vérification. Ne jamais fabriquer,
deviner ou réécrire une URL affiliée, retirer ses paramètres, substituer un lien
marchand ordinaire ou diriger un bouton vers une fiche générique pour un modèle
précis. Si l'URL ou le statut du partenariat manque, conserver un emplacement
provisoire dans le dossier et aucun bouton actif. Vérifier la destination quand
l'accès le permet et noter tout contrôle non effectué.

Une offre apparaît après la raison éditoriale de consulter cette offre, au point
où elle aide la décision. Éviter de couper un raisonnement, de répéter le même
module après chaque paragraphe ou de laisser la commission choisir le classement.
Le texte de la page doit rester compréhensible et utile si l'on retire tous les
modules commerciaux. Utiliser des libellés d'action sobres, par exemple « Voir
le prix sur Amazon » ou « Voir le modèle sur Direct-Running », uniquement quand
le partenaire et la destination correspondent et sont confirmés. Ne jamais
afficher « lien affilié » ou une mention de commission dans le bouton. Afficher
une mention claire d'affiliation séparée, avant ou près du premier accès
commercial concerné ; distinguer affiliation, publicité et sponsoring. Pour
Amazon, vérifier la formulation exacte exigée par le programme et le statut
réels du site avant publication.

Comparer uniquement des offres suffisamment comparables (même référence,
variante, état et conditions). Un prix exige vendeur, devise, date de relevé et
conditions connues ; s'il n'est pas vérifié, ne pas le présenter comme actuel.
Ne jamais promettre le « meilleur prix », une remise, la disponibilité ou un
avantage partenaire sans preuve. Qualifier les liens sortants rémunérés selon
les recommandations actuelles des moteurs et les règles applicables au site ;
vérifier le HTML rendu et non seulement le composant source.

Pour les textes français destinés au lecteur, employer une espace insécable avant
le deux-points (idéalement U+202F) et ne pas forcer de retour à la ligne autour
de lui. Appliquer ce contrôle aux titres, paragraphes, offres, libellés et
tableaux, mais préserver la syntaxe du code, des URLs, YAML et JSON.

### Contrôle éditorial par famille

Avant d'ouvrir en indexation une famille de pages, relire un échantillon varié
comme le ferait un lecteur :

- la réponse et l'angle sont spécifiques à l'intention de la page ;
- les affirmations importantes ont des sources/provenances visibles ou des
  marqueurs locaux `[À VÉRIFIER]` / `[À TESTER]` ;
- les chiffres, versions, variantes, prix et dates sont traçables et cohérents
  entre texte, filtres, tableaux, liens et données structurées ;
- les bénéfices et compromis sont exprimés en français naturel, sans superlatifs
  vides, bourrage de mots-clés ni répétitions mécaniques ;
- les offres correspondent à la bonne référence et n'interrompent pas le conseil ;
- la mention d'affiliation est visible, le libellé décrit l'action, et l'article
  conserve sa valeur sans les offres ;
- title, H1, résumé, canonical et schéma correspondent au contenu réellement
  visible, sans promesse absente ni donnée structurée inventée.

Rejeter ou remettre en rédaction les pages qui échouent à ces contrôles ; ne pas
compenser une faible valeur par plus de liens commerciaux ou de texte généré.
Pour les pages déjà publiées, cartographier les URLs et l'historique avant toute
fusion, redirection ou suppression.

## EEAT, auteurs et preuves

Relier chaque affirmation importante à une source ou à une méthode de calcul,
avec date et version. Présenter auteurs/éditeurs réels avec leurs qualifications
vérifiables et rôle éditorial. Décrire tests, critères, conflits d'intérêts,
corrections, mises à jour et contact. N'inventer ni auteur, test, citation,
review, note, témoignage, source ou processus. Les champs vides ne doivent pas
créer de balisage ni d'affirmations visibles.

## Mesure et monitoring

Proposer selon le périmètre Search Console, GA4 et entrepôt/BI (par exemple
BigQuery et Looker Studio), sans supposer les accès ni que l'intégration est
gratuite ou déjà en place. Définir le dictionnaire, fenêtres et limites des
métriques : pages publiées/éligibles, découvertes, indexées, impressions, clics,
CTR, position observée, sessions utiles, conversions et revenus. Segmenter par
famille, cohortes de publication, gabarit, pays et appareil quand les données le
permettent. Préciser jointures, granularité, quotas, consentement et délais.

Alertes : hausse des 5xx/404, sitemap invalide, canonical incohérente, pages
orphelines, baisse de couverture, données périmées, coût IA anormal, file bloquée,
régression de performance ou erreurs d'import. Chaque alerte doit avoir un
propriétaire et une action associée.

## Quand la demande est un outil pSEO concret

Si l'utilisateur fournit une spécification exécutable (CLI, service, pipeline,
plugin ou dépôt) et demande du code, traiter cette demande comme un travail
d'ingénierie complet. Le périmètre ne s'arrête pas à l'architecture ou au plan :
inspecter le dépôt, implémenter le produit demandé, ajouter les tests et la
documentation convenus, puis exécuter les contrôles demandés. Ne jamais annoncer
des tests verts sans les avoir exécutés.

Avant de coder, afficher un plan concis d'au plus 10 lignes lorsque le prompt le
demande. Si le prompt demande de ne pas poser de questions, choisir l'option la
plus simple pour les ambiguïtés non bloquantes et la noter dans la documentation.
Ne pas demander de confirmation pour ces choix. Respecter les critères
d'acceptation comme des exigences vérifiables, ainsi que les limites de sécurité,
de coûts, réseau, versions, dépendances et formats de sortie spécifiées.

Pour un générateur programmatique d'URLs avec contrôle de similarité, couvrir au
minimum ces invariants lorsqu'ils s'appliquent : validation et provenance du
catalogue; génération déterministe; filtrage métier avant produit cartésien;
normalisation des slugs et détection des collisions; exclusion et étiquetage des
URL existantes; seuils de qualité empêchant la publication de pages sans données
propres; comparaison de pages à l'intérieur et entre gabarits pertinents;
blocking/LSH ou autre méthode mesurable pour éviter une comparaison quadratique
non maîtrisée; score explicable, clusters et recommandations éditoriales; exports
reproductibles; comportement de sortie CLI documenté; rapport de lot. Une
similarité algorithmique est un signal de revue, pas une conclusion Google sur le
contenu abusif ni une décision automatique de publication.

Concevoir les algorithmes à partir de leurs vrais signaux : tokenisation FR,
stopwords et stemming léger documentés; identité des entités normalisée; données
propres représentées par des identifiants stables de faits/champs, afin que le
recouvrement soit calculable et pas un nombre seul. Si le contrat d'entrée ne
permet pas de connaître les faits partagés, documenter l'approximation retenue.
Définir précisément les intervalles de score, égalités de seuil, priorité des
statuts (`EXISTS`, `BLOCKED`, `DUPLICATE`, `SIMILAR`, `OK`) et ordre de sélection
du canonique.

Mettre en place des tests unitaires et de bout en bout pour les règles métier,
les cas limites et la reproductibilité. Pour les exigences de performance,
mesurer sur une charge représentative, documenter la machine et la configuration,
et vérifier le temps sans dégrader la correction. La seed doit être explicite si
une étape probabiliste en dépend. Maintenir un README exécutable de bout en bout,
avec les hypothèses et limites; garder le code typé, formaté et linté selon les
outils demandés.

## Livrables selon le besoin

Pour une architecture complète, assembler uniquement les sections pertinentes
et présenter les décisions, dépendances, hypothèses et inconnues clairement.
La trame de référence peut inclure :

1. résumé des objectifs et garde-fous de qualité ;
2. diagramme de composants, flux de données et flux SEO ;
3. arborescence de dépôt et responsabilités ;
4. comparaison de frameworks, base, ORM, CMS, CDN/cache, IA et hébergement ;
5. schéma de données, relations, contraintes et index ;
6. familles d'URL, canonicals, facettes, pagination et transitions ;
7. ingestion/génération, pseudo-code, files, validation et revue ;
8. gabarit de contenu, provenance et gouvernance éditoriale ;
9. maillage interne, règles et exemples ;
10. JSON-LD conditionnel et validé selon les règles actuelles ;
11. sitemaps segmentés, incrémentalité et monitoring ;
12. mesure, risques, coûts fondés sur hypothèses et feuille de route par paliers ;
13. code TypeScript concret seulement après choix de stack et vérification des
    APIs. Séparer les exemples autonomes du code réellement exécuté.

Un brief de conception n'oblige pas à fournir les quinze sections ou du code
complet. En cas de demande de code prêt à l'emploi, livrer des fichiers cohérents
avec le dépôt réel, typer les entrées/sorties, gérer les erreurs, expliquer les
variables de configuration et préciser ce qui reste à connecter. Ne jamais
présenter un pseudo-code comme exécutable.

## Roadmap de montée en charge

Faire une trajectoire par portes de validation, par exemple pilote, milliers,
dizaines de milliers puis grande échelle. Les seuils sont propres au produit et
ne sont pas des objectifs SEO garantis. Pour chaque palier préciser : familles
retenues, preuves de qualité et de demande, couverture de données, charge
d'édition/support, coûts mesurés ou méthode d'estimation, limites techniques,
risques et condition d'arrêt. Élargir après observation des cohortes, pas selon
le seul nombre de pages générées.

## Format de décision final

Conclure par :

- décision par famille (`GO`, `PILOTE`, `NOINDEX/EXCLURE`, `DIFFÉRER`) et raison ;
- architecture et compromis choisis ;
- hypothèses et preuves consultées, datées ;
- contrôles exécutés et résultats, sans déclarer ceux qui n'ont pas eu lieu ;
- risques ouverts, propriétaire et prochaine action prioritaire.

Rester direct et proportionné. Ne pas remplir les sections avec des généralités
ni transformer l'exemple de volume utilisateur en critère de succès.
