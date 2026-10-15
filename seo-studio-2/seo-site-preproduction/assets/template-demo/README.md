# Repère Salon — template de comparateur SEO

Starter statique en français, inspiré des architectures éditoriales et comparatives observées chez AFFISEO : accueil utile, outil de choix, catégories ciblées, guides, fiches modèle et méthode. Le texte, le nom et les produits ci-dessous sont une démonstration originale, pas une marque ni un catalogue réel.

> **Règle obligatoire d’adaptation : les exemples de ce dossier servent à illustrer la structure. À chaque nouvelle demande, adapter le site à la niche expressément demandée par l’utilisateur. Ne pas conserver le canapé, son vocabulaire, ses catégories, ses filtres, ses outils ou ses critères si la niche demandée est différente.**

Les consignes complètes et la vérification avant livraison sont dans [`TEMPLATE_RULES.md`](TEMPLATE_RULES.md). Les lire avant chaque réutilisation du template.

## Règles de personnalisation par niche

1. Identifier d’abord la niche, le public et la décision que le visiteur cherche à prendre à partir de la demande de l’utilisateur. En cas d’inconnue décisive, la clarifier avant de figer le contenu.
2. Garder les principes de structure seulement quand ils sont utiles : page d’accueil, pages de catégorie ou d’intention, guides, fiches, méthode et liens entre elles.
3. Refaire les taxonomies, pages, champs, filtres, outils, critères de comparaison, vocabulaire, exemples et CTA pour le domaine concerné. Un canapé n’est pas une métaphore universelle : choisir des interactions adaptées au produit ou service (dimensions, compatibilité, usage, budget, disponibilité, diagnostic, etc.).
4. Écrire pour les questions réelles de cette niche et son parcours d’achat. Ne pas remplacer mécaniquement « canapé » par un autre mot dans les titres ou paragraphes.
5. Utiliser uniquement des faits, preuves, sources, prix, avis et caractéristiques propres à la niche et vérifiés. Quand ils ne sont pas fournis, conserver des champs à renseigner et les signaler comme exemples ; ne jamais fabriquer de preuve pour rendre la démo plus persuasive.
6. Adapter le modèle de conversion au besoin confirmé : clic marchand, achat, demande de devis, réservation, inscription ou autre prochaine étape. Ne pas présumer l’affiliation parce que le template la démontre.
7. Refaire le `PROJECT_SKIN.yaml` pour l’identité et les codes du secteur sans reprendre la composition d’un site concurrent. La direction visuelle actuelle « table de prise de mesures » est propre à l’exemple canapé, pas une contrainte de marque pour la prochaine niche.

## Aperçu

- `index.html` — accueil et outil de contrôle de largeur.
- `canapes-compacts.html` — catégorie commerciale par besoin.
- `guide-dimensions.html` — guide informationnel relié à la catégorie et à la fiche.
- `modele-canape.html` — gabarit de fiche à remplir avec les données du fabricant ou du marchand.
- `methode.html` — méthode, limites et déclaration d’affiliation à personnaliser.
- `assets/site.css` et `assets/site.js` — styles et interactions sans dépendances.
- `PROJECT_SKIN.yaml` — direction visuelle propre à ce template.
- `TEMPLATE_RULES.md` — règle prioritaire et procédure pour adapter les exemples à la niche demandée.

## Avant publication

1. Remplacer « Repère Salon » par le nom et le domaine réels.
2. Remplacer les textes de démonstration, valeurs de largeur et caractéristiques produit par des données vérifiées. Les modèles « Ligne A/B/C » sont fictifs ; ne pas les présenter comme des références en vente.
3. Ajouter uniquement des photos autorisées et des liens marchands réels. Vérifier chaque taille, prix, disponibilité, frais et condition avant de l’afficher.
4. Rédiger un angle distinctif et utile pour chaque page. Ne pas dupliquer une page par variante de mot-clé.
5. Compléter la méthode, les sources, l’identité de l’éditeur et la déclaration de rémunération. Ne jamais inventer un essai, une note, un témoignage ou une expertise.
6. Remplacer les URL `https://www.votre-domaine.fr/...` dans les canonical et données structurées par les URL de production.
7. Retirer `noindex,follow` des cinq pages seulement quand le domaine, les routes, les preuves et les contenus sont prêts à être publiés.
8. Créer ensuite un sitemap XML qui ne contient que les URL canoniques publiables et mettre à jour `robots.txt` selon l’hébergement retenu.
9. Vérifier les liens, le rendu mobile, le clavier, les filtres, les canonical et les données structurées visibles avant publication.

`PROJECT_SKIN.yaml` garde ses contrôles qualité en attente tant qu’une revue visuelle réelle n’a pas été faite dans les navigateurs et tailles d’écran cibles. La revue de ce livrable est restée statique : le navigateur de cette session a bloqué l’ouverture du fichier local.

## Carte SEO incluse

| Page | Intention | Rôle et liens attendus |
|---|---|---|
| Accueil | Choisir un canapé adapté | Entrée vers le diagnostic, le classement, les catégories et les guides. |
| Canapés compacts | Comparer les modèles compacts | Liste filtrable, critères de choix, lien vers les fiches et le guide de mesures. |
| Guide dimensions | Savoir mesurer avant achat | Réponse pratique, lien vers l’outil, la catégorie et une fiche pertinente. |
| Fiche modèle | Évaluer une référence précise | Données sourcées, points forts et limites, critères, date de vérification et lien marchand. |
| Méthode | Comprendre la sélection et la rémunération | Explique les règles de comparaison, les sources et les limites de l’évaluation. |

L’outil de largeur, la liste à comparer et les filtres ne nécessitent pas de création d’URL indexables. Garder les facettes dans l’interface tant qu’elles ne correspondent pas à une intention distincte et à un contenu réellement utile.

## Principes techniques

- Chaque page possède son `title`, sa description, son canonical, un H1 explicite, des liens HTML internes et des fils d’Ariane visibles.
- Les cinq pages sont en `noindex,follow` par défaut pour éviter de publier par accident le domaine d’exemple. Retirer ce signal uniquement à la mise en ligne.
- Le JSON-LD est limité aux informations réellement visibles : `WebSite` sur l’accueil et `BreadcrumbList` sur les pages concernées. Aucun score, prix, avis, auteur ou offre fictive n’est structuré.
- Les liens rémunérés ajoutés au gabarit fiche doivent porter `rel="sponsored"` et la relation commerciale doit être déclarée aux lecteurs.
- Les pages restent lisibles sans JavaScript ; JavaScript améliore l’outil de largeur, le filtre local, la sélection et le menu mobile.
- Pas de police, analytics, widget, CDN ni image externe chargés par défaut.

## Documentation officielle consultée

- [Google Search Central — Guide de démarrage SEO](https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=fr)
- [Google Search Central — Canonicalisation](https://developers.google.com/search/docs/crawling-indexing/canonicalization)
- [Google Search Central — Règles générales des données structurées](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Google Search Central — Liens rémunérés et qualification](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links)

La présence d’un balisage ou d’un fichier sitemap ne garantit ni l’indexation ni un résultat enrichi. Le template ne contient pas de données de trafic ou de conversion.
