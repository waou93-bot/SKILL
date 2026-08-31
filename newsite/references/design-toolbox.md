# Boîte à outils de direction UI

Cette boîte à outils aide à décider. Elle ne fournit pas des composants à copier.

## Entrées requises

Aucune direction UI ne démarre sans :

- le Contrat de conversion approuvé ou un brouillon marqué comme hypothèse ;
- le public, l'action principale et la preuve attendue ;
- le MASTER, le canon et le registre des assets ;
- les contraintes légales, d'accessibilité et de marque ;
- les références retenues et rejetées.

La direction UI produit une phrase Design Read, trois curseurs et un plan de page. Elle ne produit pas de promesse commerciale, de témoignage, de qualification, de chiffre ou d'image attribuée sans source.

## Design Read

Format obligatoire :

> Lecture : [type de page] pour [lecteur], avec [langage visuel], afin de faciliter [action principale].

Les curseurs consignés dans le snapshot :

| Curseur | Échelle | Effet |
| --- | --- | --- |
| Variance | 1-10 | De la grille régulière à une composition plus libre. |
| Mouvement | 1-10 | Du statique à une chorégraphie justifiée. |
| Densité | 1-10 | De la lecture aérée à l'information compacte. |

Toute valeur demande une justification liée au lecteur, à la preuve ou à l'action.

## Sources de travail

| Famille | Sources admises | Usage | Limite |
| --- | --- | --- | --- |
| Analyse de structure | Hallmark, Dribbble, SceneAI, NameThatUI | Nommer un rythme, une hiérarchie ou un principe de composition | Ne jamais reproduire une page, une image, une marque ou un écran. |
| Composants | 21st, React Bits, Uiverse | Étudier un état, une interaction ou une solution d'accessibilité | Aucun collage de bloc. Vérifier compatibilité et licence. |
| Typographie | Fichier sous licence, Fontshare après contrôle, source officielle | Choisir famille, graisses, styles et chargement | Deux familles maximum. Licence, fallback et méthode de chargement sont consignés. |
| Icônes | Phosphor lorsqu'une icône réduit une ambiguïté | Action, statut ou navigation nécessaire | Une famille par projet. Aucune icône décorative. |
| Médias | Photos du client, commande photo, banque sous licence, concept généré déclaré | Prouver un geste, un matériau, un état ou une méthode | Une image générée n'est jamais une référence client ou un chantier. |
| Mouvement | CSS et Web Animations API | Retour d'action, changement d'état, entrée de contenu | Aucune animation de remplissage. Mode réduit obligatoire. |
| QA | webapp-testing, web-design-guidelines | Tester le parcours et relever les écarts | Vérifier les règles à jour et les limites du test. |

Fontshare : https://www.fontshare.com/licenses/itf-ffl  
Phosphor : https://phosphoricons.com/

## Règles de composition

- Chaque section a un rôle : comprendre, vérifier, choisir ou contacter.
- Une section sans preuve, information ou action est retirée.
- La page utilise un thème cohérent. Les changements de fond restent dans la même famille de surface.
- Les cartes servent une hiérarchie réelle. Des séparateurs, une grille et l'espace blanc sont préférés aux cartes répétées.
- Une alternance image-texte ne dépasse pas deux sections successives.
- Les surlignes en capitales sont rares et nomment un sujet, jamais un numéro.
- Les images ne portent ni pastille ni cartouche décoratif. Une divulgation de provenance est une exception : lorsqu’un média est `concept`, généré, provisoire ou susceptible d’être confondu avec une référence réelle, son statut doit rester visiblement lié à l’image, dans son cadre ou sa légende. Ce repère informe, il ne décore pas.
- Les couleurs d'accent signalent une action, un repère ou un état réel.

## Typographie

- Une famille donne le ton, l'autre règle l'information. Elles ne s'opposent pas dans un même titre.
- Les italiques sont réservées à une citation, un nom ou une distinction de sens réelle.
- Les titres restent lisibles sans retour forcé. Les descendants typographiques ne sont jamais coupés.
- Les textes courants évitent les capitales espacées, les libellés codés et les petites tailles décoratives.
- Le snapshot indique source, licence, fichiers, graisses, styles autorisés, fallback, stratégie de chargement et test de stabilité.

## Boutons et formulaires

- Chaque site a une conversion principale et un CTA principal.
- Le CTA nomme la prochaine étape relationnelle.
- Deux CTA n'ont jamais la même intention avec deux libellés différents.
- Un bouton a les états repos, survol, focus visible, actif, désactivé, erreur et réussite lorsqu'une action est asynchrone.
- Le contraste est vérifié sur chaque état. Le libellé ne se replie pas sur deux lignes au bureau.
- Une demande de contact explique les informations utiles et la suite réelle. Elle ne promet ni délai ni résultat sans source.
