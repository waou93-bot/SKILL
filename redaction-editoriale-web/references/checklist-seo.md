# Checklist SEO et titres

## Cadrage

- Identifier intention informationnelle, comparative, transactionnelle ou navigationnelle ; préciser l'intention dominante d'un contenu mixte.
- Un mot-clé principal et 3 à 5 secondaires pertinents. Ne pas prétendre disposer de volumes, positions ou questions People Also Ask non consultés.
- Longueur adaptée à l'intention ; chaque section répond à une question utile.
- Pour créer ou optimiser les H1 et métas, appliquer [h1-metas-trends-astra](h1-metas-trends-astra.md) : références du sujet consultées, comparaison Trends avec filtres explicites, variantes, décision ASTRA réelle si disponible, puis édition et nouveau contrôle. Conserver les observations et limites dans le dossier éditorial.

## Livrable selon le périmètre

Pour une optimisation ciblée, préparer les cinq titles et les trois ensembles dans le dossier de travail, puis livrer et éditer les seuls champs demandés avec leurs comptes, une justification et les statuts de recherche/arbitrage. Si le brief demande seulement H1 et meta description, ne pas imposer title ou sous-titre supplémentaires ; proposer les variantes détaillées seulement si utiles ou demandées. Pour une création d'article ou un paquet SEO complet, livrer les éléments ci-dessous. Ne pas réécrire tout un article pour modifier ses accroches.

1. Cinq variantes de title en question précise : texte, nombre exact de caractères (espaces et ponctuation inclus), intention visée. Recommander une variante avec une justification d'une ligne. Respecter un titre exact ou une convention expressément imposés dans le brief.
2. Title retenu de 60 caractères maximum par défaut ; viser aussi 580 px maximum si une mesure appropriée est disponible. Ce sont des cibles éditoriales du skill, pas des limites imposées par Google. La largeur dépend de la police et de l'affichage : la mesurer si possible, sinon signaler « largeur en pixels non mesurée ». Ne pas convertir mécaniquement caractères en pixels ni promettre l'absence de troncature. Respecter une contrainte explicite du support ; ne pas appliquer cette limite au H1.
3. Meta description de 155 caractères maximum par défaut, comme cible éditoriale, qui commence à répondre à la question du titre : critère décisif, première action ou conséquence confirmée. Elle reste compréhensible seule et reflète les réserves essentielles. Éviter les amorces « Découvrez… » qui ne donnent aucune réponse. Compter réellement les caractères après la dernière édition. Google peut choisir un autre extrait selon la requête ; longueur et contenu de la balise ne garantissent pas son affichage.
4. Slug court en minuscules, mots séparés par des tirets, sans accents inutiles.
5. Un seul H1 en question, adapté à la lecture visible ; proposer une formulation distincte du title par défaut, avec la même promesse. Ce choix éditorial n'est pas une exigence SEO universelle. Prévoir un sous-titre qui donne une première réponse et un chapô qui la développe sans répétition ; fusionner sous-titre/chapô si le support le demande. H2 informatifs et H3 subordonnés, éléments de réponse ou sous-questions utiles, variantes sémantiques naturelles ; pas de saut de niveau gratuit.
6. Textes alternatifs en français décrivant chaque image utile ; pour un visuel simplement proposé, indiquer « visuel suggéré ». Les images décoratives peuvent avoir un alt vide. Choisir une illustration dessinée, photoréaliste ou schématique professionnelle selon ton-et-style.md ; rejeter les schémas rudimentaires.
7. Trois à cinq liens internes : ancre naturelle, page cible ou sujet cible, emplacement conseillé. Si l'inventaire du site manque, livrer des propositions à valider, sans URL inventée et sans prétendre qu'une page existe.
8. Suggestion de données structurées en JSON-LD conforme au contenu visible. Auteur et date de mise à jour fournis ou signalés à vérifier. La date de travail est celle du brouillon, pas une fausse date de publication.
9. Pour un article long, liste des H2 optimisés et trois titres alternatifs pour les réseaux sociaux.

## Méthode d'accroche pour tous les titres

- Mot-clé principal dans les 30 premiers caractères lorsque naturel.
- Une question réelle et un angle précis : usage, budget, critère, difficulté ou conséquence. Le sous-titre et la meta commencent à y répondre ; la formulation interrogative ne justifie ni suspense artificiel ni deuxième promesse.
- Promesse tenue dans le texte ; aucune urgence artificielle, MAJUSCULES criardes, exclamations multiples, superlatifs sans classement ou bourrage.
- Année uniquement avec mise à jour annuelle réelle ; marque en fin de title si la place le permet.
- Si l'inventaire du site existe, contrôler titres concurrents et cannibalisation. Sinon noter cette vérification comme non effectuée.
- Départager les formulations avec le contenu, le benchmark et Trends ; faire arbitrer les ensembles par ASTRA selon la référence dédiée. Ne pas sélectionner mécaniquement le terme en plus forte progression ni annoncer un gain de CTR sans données comparables.
- Séparer H1 visible, balise title, sous-titre, meta description et extrait observé dans un moteur. Une balise concurrente inaccessible reste « non relevée » ; un résultat de recherche ne la remplace pas.

Points de départ à varier :
- Guide : « Quel [produit] choisir pour [usage] ? ».
- Comparatif : « Faut-il choisir [A] ou [B] pour [usage] ? ».
- Tuto : « Comment [action] sur [système] ? » ; préciser une contrainte seulement si elle est réellement traitée.
- Explicatif : « Que change [sujet] pour [public] ? ».

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
