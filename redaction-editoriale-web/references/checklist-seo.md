# Checklist SEO et titres

## Cadrage

- Identifier intention informationnelle, comparative, transactionnelle ou navigationnelle ; préciser l'intention dominante d'un contenu mixte.
- Une intention principale et sa carte de fan-out utile, selon [fan-out-editorial](fan-out-editorial.md). Distinguer requêtes observées des hypothèses, relier chaque question retenue à une section, une page existante ou une décision d’exclusion ; aucun quota de mots-clés. Ne pas prétendre disposer de volumes, positions ou questions People Also Ask non consultés.
- Longueur adaptée à l'intention ; chaque section répond à une question utile.
- Pour un article complet, appliquer cette checklist et livrer un H1, un title et une meta description finaux. Réserver le parcours approfondi [h1-metas-trends-astra](h1-metas-trends-astra.md) au benchmark/optimisation ciblé demandé ou à un arbitrage réellement disputé ; ne pas lancer Trends, ASTRA ni variantes multiples par défaut.

## Livrable selon le périmètre

Pour une optimisation ciblée, préparer les cinq titles et les trois ensembles dans le dossier de travail, puis livrer et éditer les seuls champs demandés avec leurs comptes, une justification et les statuts de recherche/arbitrage. Si le brief demande seulement H1 et meta description, ne pas imposer title ou sous-titre supplémentaires ; proposer les variantes détaillées seulement si utiles ou demandées. Pour une création d'article ou un paquet SEO complet, livrer les éléments ci-dessous. Ne pas réécrire tout un article pour modifier ses accroches.

1. Un title recommandé, précis et fidèle à l’article. Proposer jusqu’à trois variantes aux angles distincts seulement si le choix est utile ou demandé. Indiquer intention et justification ; respecter le titre exact ou la convention imposée dans le brief.
2. Title retenu de 60 caractères maximum par défaut ; viser aussi 580 px maximum si une mesure appropriée est disponible. Ce sont des cibles éditoriales du skill, pas des limites imposées par Google. La largeur dépend de la police et de l'affichage : la mesurer si possible, sinon signaler « largeur en pixels non mesurée ». Ne pas convertir mécaniquement caractères en pixels ni promettre l'absence de troncature. Respecter une contrainte explicite du support ; ne pas appliquer cette limite au H1.
3. Meta description unique, concise et fidèle au contenu, qui résume la réponse et les contraintes utiles. Une cible éditoriale de 155 caractères peut aider mais n’est pas une limite Google ; le moteur peut produire un autre extrait. Compter si le brief ou le dossier l’exige.
4. Slug court en minuscules, mots séparés par des tirets, sans accents inutiles.
5. Un seul H1 principal, visible et fidèle à l’intention ; question si elle représente une vraie question du lecteur, titre descriptif sinon. Le title peut différer tout en gardant la même promesse. H2/H3 structurent les sous-questions utiles du fan-out, sans créer un titre pour chaque variante.
6. Textes alternatifs en français décrivant chaque image utile ; pour un visuel simplement proposé, indiquer « visuel suggéré ». Les images décoratives peuvent avoir un alt vide. Choisir une illustration dessinée, photoréaliste ou schématique professionnelle selon ton-et-style.md ; rejeter les schémas rudimentaires.
7. Liens contextuels pertinents réellement intégrés aux mots ou expressions du corps vers articles, guides et fiches produits existants : ancre naturelle, destination précise et justification selon [liens-contextuels](liens-contextuels.md). Priorité au maillage interne lorsqu’une page du site répond au besoin ; liens externes seulement pour une source ou un complément pertinent, avec nouvel onglet (`target="_blank"`, token `noopener` dans `rel`, ou réglage CMS équivalent), sans perdre `sponsored` si requis. Les liens internes restent dans le même onglet. Vérifier le rendu et signaler les réglages impossibles en Markdown seul. Aucun quota ni lien sur toutes les occurrences. Si l'inventaire manque, fournir les propositions dans le dossier sans URL inventée ni faux lien actif ; reprendre les destinations manquantes dans les vérifications finales.
8. Suggestion de données structurées en JSON-LD conforme au contenu visible. Auteur et date de mise à jour fournis ou signalés à vérifier. La date de travail est celle du brouillon, pas une fausse date de publication.
9. Pour un article long, proposer des titres alternatifs pour les réseaux sociaux ou une liste de H2 seulement si le brief les demande ou si cela aide concrètement la publication.

## Méthode d'accroche pour tous les titres

- Mot-clé principal dans les 30 premiers caractères lorsque naturel.
- Un angle précis et naturel, interrogatif ou déclaratif selon l’intention réelle ; sous-titre et meta répondent au titre sans suspense. La formulation interrogative ne justifie ni suspense artificiel ni deuxième promesse.
- Promesse tenue dans le texte ; aucune urgence artificielle, MAJUSCULES criardes, exclamations multiples, superlatifs sans classement ou bourrage.
- Année uniquement avec mise à jour annuelle réelle ; marque en fin de title si la place le permet.
- Si l'inventaire du site existe, contrôler titres concurrents et cannibalisation. Sinon noter cette vérification comme non effectuée.
- Choisir une formulation fidèle au contenu, au besoin observé et aux preuves. Si un benchmark, Trends ou ASTRA est demandé, consigner les observations et limites selon la référence dédiée ; ne pas annoncer un gain de CTR sans données comparables.
- Séparer H1 visible, balise title, sous-titre, meta description et extrait observé dans un moteur. Une balise concurrente inaccessible reste « non relevée » ; un résultat de recherche ne la remplace pas.

Points de départ à varier :
- Guide : question de choix ou titre descriptif de sélection, selon la requête et le format (par exemple « Quel appareil choisir pour… ? » ou « Les appareils à retenir selon votre usage »).
- Comparatif : nommer A, B et le critère de décision ; question si elle est naturelle, titre comparatif descriptif sinon.
- Tutoriel : annoncer directement l’action, le système ou la version utile ; poser la question « Comment… ? » quand elle correspond à l’intention.
- Explicatif : annoncer le fait confirmé et son effet pour le public ; une question est possible si c’est le besoin observé.

## JSON-LD : suggestion, jamais fabrication

Choisir Article pour l'éditorial, ItemList pour une sélection, HowTo pour des étapes et FAQPage pour une FAQ réellement visible ; ces types Schema.org ne garantissent ni prise en charge actuelle par Google ni résultat enrichi. Vérifier la documentation officielle actuelle avant toute promesse d'éligibilité. Product exige un produit identifié et des caractéristiques documentées ; ne pas inventer Offer, prix, disponibilité, Review ou AggregateRating. Un comparatif n'autorise pas à fabriquer deux notes.

Si des champs manquent, omettre les propriétés facultatives. Pour une information requise manquante, fournir un **gabarit non publiable** avec les valeurs [À VÉRIFIER], expliquer les champs à remplir et ne pas l'annoncer valide pour publication. Ne pas inventer d'URL canonique, d'auteur ou de date. Contrôler syntaxe JSON, correspondance avec le texte visible et cohérence des types.

Exemple pédagogique non publiable faute d'auteur et de date :

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Titre réel du contenu]",
  "author": {"@type": "Person", "name": "[À VÉRIFIER]"},
  "dateModified": "[À VÉRIFIER]"
}
```

Références officielles consultées le 9 octobre 2026 : [mises à jour Search Central](https://developers.google.com/search/updates), [fin des résultats HowTo](https://developers.google.com/search/blog/2023/08/howto-faq-changes), [Product](https://developers.google.com/search/docs/appearance/structured-data/product). Les résultats enrichis HowTo ont été supprimés ; le journal 2026 indique aussi la fin de l'affichage FAQ. Recontrôler ces états lors d'une future recommandation ; ne pas les confondre avec la validité des types Schema.org.
