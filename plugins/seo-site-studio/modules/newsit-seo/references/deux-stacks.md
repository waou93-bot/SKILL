# Contrat de choix entre deux stacks

## Déterminer les candidates

Partir du type de site, de l'architecture imposée, du moteur de conversion, des besoins serveur/CMS, des données, du niveau d'interaction, des compétences disponibles et de la maintenance. Vérifier les versions, compatibilités, capacités et tarifs sensibles au temps dans les sources officielles. Les coûts non calculables restent inconnus ; aucune estimation ne devient un prix fournisseur.

Retenir exactement deux options techniquement crédibles. Chaque option décrit le système complet pertinent : frontend/rendu, contenu/catalogue, backend ou moteur marchand, interactivité, déploiement et maintenance. Écarter une option incompatible avant de la présenter ; ne pas fabriquer une seconde option faible pour faire gagner la première.

Exemples de familles, jamais choix automatiques :

- Vitrine/éditorial : Astro statique avec CMS adapté, ou une solution CMS maintenable dont le design demandé est faisable.
- Affiliation avec configurateur : Astro et îlots ciblés, ou Next.js si l'état, le serveur ou l'écosystème React le justifient.
- Commerce : Shopify avec thème spécifique, ou WooCommerce adapté lorsque les contraintes de propriété, catalogue et maintenance le justifient. Une architecture headless peut être candidate si sa valeur compense réellement le coût ; elle n'est pas une exigence de qualité visuelle.

## Présenter le choix

| Critère | Stack A | Stack B |
| --- | --- | --- |
| Composition réelle | Framework/rendu, CMS/données, moteur, hébergement | Idem |
| Pourquoi ce choix | Besoin concret couvert | Besoin concret couvert |
| SEO Google/Bing | HTML, routes, métadonnées, sitemap, balisage et contrôle | Idem |
| DA et interactions | Faisabilité du concept et fallback | Idem |
| Conversion métier | Formulaire, checkout ou lien marchand réel | Idem |
| Maintenance/propriété | Charge, mises à jour, contrôle et dépendances | Idem |
| Coût | Source/date, hypothèse ou inconnu | Idem |
| Compromis | Limite matérielle du projet | Limite matérielle du projet |

Après la table, recommander explicitement l'une des deux et donner deux ou trois raisons propres au brief. Dire quel changement de besoin ferait préférer l'autre. Demander un choix bref avant fabrication quand il manque, sans transformer chaque bibliothèque interne en nouvelle décision utilisateur.

Si le projet possède déjà une stack complète imposée ou validée, conserver le choix et ses contraintes. Un framework seul ne valide pas toutes les couches : avec Next.js imposé et un moteur marchand inconnu, garder Next.js dans les deux propositions et comparer deux compositions crédibles pour commerce/backend/CMS. Ne pas réouvrir une couche déjà choisie, mais ne pas traiter les couches inconnues comme validées. Une refonte fonctionnelle n'autorise pas une migration. Si la contrainte est incompatible, expliquer précisément le conflit et proposer une correction bornée avant le changement.
