# Checklist SEO et titres

## Cadrage

- Identifier intention informationnelle, comparative, transactionnelle ou navigationnelle ; préciser l'intention dominante d'un contenu mixte.
- Un mot-clé principal et 3 à 5 secondaires pertinents. Ne pas prétendre disposer de volumes, positions ou questions People Also Ask non consultés.
- Longueur adaptée à l'intention ; chaque section répond à une question utile.

## Livrable systématique

1. Cinq variantes de title : texte, nombre exact de caractères (espaces et ponctuation inclus), intention visée. Recommander une variante avec une justification d'une ligne.
2. Title retenu de 60 caractères maximum ; viser aussi 580 px maximum. La largeur dépend de la police et de l'affichage : la mesurer si un outil approprié existe, sinon signaler « largeur en pixels non mesurée ». Ne pas convertir mécaniquement caractères en pixels ni promettre l'absence de troncature.
3. Meta description de 155 caractères maximum, avec bénéfice et invitation sobre à lire. Compter réellement les caractères. La longueur ne garantit pas son affichage par Google.
4. Slug court en minuscules, mots séparés par des tirets, sans accents inutiles.
5. Un seul H1, différent du title retenu mais fidèle à la même promesse. H2 informatifs et H3 subordonnés, variantes sémantiques naturelles ; pas de saut de niveau gratuit.
6. Textes alternatifs en français décrivant chaque image utile ; pour un visuel simplement proposé, indiquer « visuel suggéré ». Les images décoratives peuvent avoir un alt vide.
7. Trois à cinq liens internes : ancre naturelle, page cible ou sujet cible, emplacement conseillé. Si l'inventaire du site manque, livrer des propositions à valider, sans URL inventée et sans prétendre qu'une page existe.
8. Suggestion de données structurées en JSON-LD conforme au contenu visible. Auteur et date de mise à jour fournis ou signalés à vérifier. La date de travail est celle du brouillon, pas une fausse date de publication.
9. Pour un article long, liste des H2 optimisés et trois titres alternatifs pour les réseaux sociaux.

## Méthode d'accroche pour tous les titres

- Mot-clé principal dans les 30 premiers caractères lorsque naturel.
- Un seul levier d'accroche : chiffre, année, bénéfice concret, contrainte, contraste ou question réelle.
- Promesse tenue dans le texte ; aucune urgence artificielle, MAJUSCULES criardes, exclamations multiples, superlatifs sans classement ou bourrage.
- Année uniquement avec mise à jour annuelle réelle ; marque en fin de title si la place le permet.
- Si l'inventaire du site existe, contrôler titres concurrents et cannibalisation. Sinon noter cette vérification comme non effectuée.

Points de départ à varier :
- Guide : « Meilleur [produit] : la sélection pour [usage] ».
- Comparatif : « [A] vs [B] : lequel choisir pour [usage] ? ».
- Tuto : « Comment [action] en [N] étapes » ; ajouter « sans [frein] » seulement si cela n'empile pas les accroches.
- Explicatif : « [Sujet] : ce que ça change pour [public] ».

## JSON-LD : suggestion, jamais fabrication

Choisir Article pour l'éditorial, ItemList pour une sélection, HowTo pour des étapes et FAQPage pour une FAQ réellement visible ; ces types Schema.org ne garantissent ni prise en charge actuelle par Google ni résultat enrichi. Vérifier la documentation officielle actuelle avant toute promesse d'éligibilité. Product exige un produit identifié et des caractéristiques documentées ; ne pas inventer Offer, prix, disponibilité, Review ou AggregateRating. Un comparatif n'autorise pas à fabriquer deux notes.

Si des champs manquent, omettre les propriétés facultatives. Pour une information requise manquante, fournir un **gabarit non publiable** avec les valeurs [À VÉRIFIER], expliquer les champs à remplir et ne pas l'annoncer valide pour publication. Ne pas inventer d'URL canonique, d'auteur ou de date. Contrôler syntaxe JSON, correspondance avec le texte visible et cohérence des types.

Exemple pédagogique non publiable faute d'auteur et de date :

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Titre réel du contenu]",
  "author": {"@type": "Person", "name": "[À VÉRIFIER]"},
  "dateModified": "[À VÉRIFIER]"
}
```

Références officielles consultées le 9 octobre 2026 : [mises à jour Search Central](https://developers.google.com/search/updates), [fin des résultats HowTo](https://developers.google.com/search/blog/2023/08/howto-faq-changes), [Product](https://developers.google.com/search/docs/appearance/structured-data/product). Les résultats enrichis HowTo ont été supprimés ; le journal 2026 indique aussi la fin de l'affichage FAQ. Recontrôler ces états lors d'une future recommandation ; ne pas les confondre avec la validité des types Schema.org.
