# Implémentation sur la stack existante

Cette checklist est une méthode d'ingénierie, pas une formule de classement. Choisir les contrôles
pertinents pour le changement. Consulter les documentations actuelles du framework et des moteurs.

## Audit par couches

| Couche | Contrôles | Preuves |
|---|---|---|
| URL et HTTP | 200 utile, redirections maîtrisées, vrais 404/410, pas de soft-404 ni challenge 200 | GET/en-têtes/chaîne finale horodatés, outil identifié |
| Indexabilité | robots.txt et groupes spécifiques, meta robots, X-Robots-Tag, canonical, contrôles snippets | règles et URL concrètes, lecture de l'intention publique |
| Découverte | liens HTML crawlables, sitemap d'URLs canoniques voulues, pagination, orphelines | graphe ou échantillon et sitemap validés |
| Contenu | texte essentiel dans HTML initial lorsque possible, parité DOM, sections et liens accessibles | capture initiale + rendue, pas seulement screenshot |
| Entités | nom stable, activité, offre, auteur réel, pays/langue, contacts et preuves | pages visibles et sources |
| Données structurées | type approprié et données vraies, IDs stables, JSON valide, parité visible | validation syntaxique et sémantique distinctes |
| Utilisabilité agent | HTML sémantique, labels, liens/boutons natifs, erreurs compréhensibles, URLs stables | test clavier/arbre d'accessibilité/parcours |
| Conversion | CTA approprié à l'intention, comparateur/contact/achat utilisable, pas de piège | parcours de test, événement et déduplication |
| Production | robots de production distincts de preview, cache purgé au bon niveau | contrôle après déploiement autorisé |

Sitemap : URLs canoniques destinées à l'indexation, pas de données privées ; `lastmod` reflète
une vraie modification substantielle. Ne pas ajouter aveuglément chaque export JSON/Markdown.
IndexNow est une notification optionnelle aux moteurs participants, pas un ordre d'indexation
ni un endpoint direct universel de ChatGPT. Un HTTP 200 confirme la réception seulement.

## Adaptation à la stack

Next.js/React : repérer App/Pages Router et version réelle ; utiliser les mécanismes existants
pour metadata, canonical, robots, sitemap et rendu serveur/statique. Ne pas forcer une migration.
Ne pas compter sur une hydratation lourde pour l'unique copie des prix, usages et caractéristiques.
Vérifier le HTML retourné à une requête réelle, pas uniquement le code source du composant.

WordPress/CMS : réutiliser le plugin SEO et les champs structurés déjà canoniques ; éviter les
titres, canonicals, sitemaps et JSON-LD concurrents produits par deux plugins.

Site statique ou autre framework : utiliser son pipeline natif ; aucune dépendance Next.js
nécessaire. Garder une source de données unique entre rendu visible, exports et schema.

## Structured data sans fiction

Choisir Organization, Person, WebSite, Article, BreadcrumbList, Product/Offer ou d'autres types
uniquement s'ils décrivent réellement la page. Une organisation n'est pas automatiquement un
commerce local. `sameAs` ne contient que des profils réels. Ne pas inventer avis, aggregateRating,
stocks, prix, qualifications ou résultats de tests. Une liste d'affiliation n'est pas forcément
une fiche vendeur éligible à un flux marchand. Vérifier les règles de chaque programme.

JSON-LD : encoder les données avec un sérialiseur ; dans un contexte script HTML, neutraliser
`<` (par exemple en `\\u003c`) pour éviter une fermeture `</script>` injectée. Vérifier la
syntaxe ET la cohérence avec le contenu visible. FAQPage/HowTo ne sont pas des bonus GEO ;
ne promettre aucun rich result sans vérifier l'éligibilité actuelle du moteur.

## Données publiques optionnelles et agents

Un export Markdown/JSON public peut faciliter un usage identifié, mais doit être généré depuis
la même source que la page visible, daté correctement et non plus favorable ou plus riche en
promesses cachées. Définir cache, invalidation, MIME, liens et maintenance. Interdire les secrets.
Pour une API/MCP, commencer en lecture seule, avec périmètre, quotas, validation des entrées et
politique de données. Réserver toute action commerciale à une autorisation explicite, des
contrôles serveur, confirmation, idempotence et journalisation appropriés. Pas de checkout
agentique créé pour une simple demande de référencement.

## Critères de sortie d'un patch

Diff limité, lint/tests/build pertinents, absence de régression d'accès privé, canonical/sitemap
cohérents, contenu disponible, données structurées vraies, parcours utilisable, mesure testée
sans pollution de production. Noter ce qui reste à vérifier après publication. Ne pas affirmer
« indexé » à partir d'un build ou « recommandé » à partir d'un JSON-LD valide.
