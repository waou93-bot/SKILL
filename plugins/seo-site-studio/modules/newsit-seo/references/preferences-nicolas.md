# Préférences à appliquer et à vérifier

Source : demandes explicites de Nicolas et fichiers Memory / Design DNA, lus le 4 octobre 2026. Au lancement, relire les versions actuelles et les décisions du projet. Ne pas déduire une préférence d'une simple bibliothèque disponible.

- Corps, interface, navigation et boutons : Plus Jakarta Sans par défaut, fallback lisible. Préserver une police validée ; vérifier chargement, licence et lisibilité.
- Accord Raccord : titres Georgia/Times serif, papier chaud, encre sombre, bordeaux discret, séparateurs fins et composition éditoriale. Cette référence est documentée dans Design DNA ; le site `accord-raccord.fr` n'a pas été accessible lors de cette révision. Ne pas prétendre en avoir fait une inspection live. Vérifier le domaine sans tiret avant de supposer une équivalence.
- Nouveau projet : reprendre la qualité et le rythme de cette référence avec une identité adaptée à la niche. Le serif est la première direction à examiner ; éviter de recopier systématiquement palette et mise en page. Ne pas revenir automatiquement aux anciennes fontes condensées d'Accord Raccord.
- Boutons : CTA rectangulaires sobres, rayon contenu et documenté dans PROJECT_SKIN.yaml ; aucun bouton circulaire ni pillule par défaut. Ne pas inventer une valeur de rayon prétendument préférée. Libellés directs, aucune petite flèche, icône arrow, caractère fléché, pseudo-élément fléché ou flèche au survol dans un CTA. Les chevrons fonctionnels d'ouverture/fermeture sont admis avec état et accessibilité ; ils ne décorent pas un CTA commercial.
- Aucun slop : retirer héros SaaS interchangeable, murs de cartes identiques, badges gratuits, dégradés/glows décoratifs, phrases creuses, fausses preuves et visuels incohérents. Donner une fonction à chaque module.
- Héros : illustration, animation ou vidéo réellement panoramique en 16:9, sujet lisible et média adapté sur mobile. Une boîte 16:9 contenant une image carrée ne suffit pas.
- Navigation : lien Accueil, visible au sommet, se masque en descendant et revient en remontant ; clavier, focus et repli sans JavaScript préservés. Respecter prefers-reduced-motion.
- Conseil contextualisé avant les produits, offre commerciale subordonnée à l'utilité, liens individuels disponibles. Aucun faux panier externe ni choix que le marchand ne peut honorer.

Avant extension des gabarits, examiner au moins accueil, catégorie, guide et parcours principal sur ordinateur/mobile. Vérifier réellement typographies calculées, ratios, boutons dans leurs états normal/focus/survol, navigation, wrapping et contrastes. Conserver les captures et les corrections. Un grep de symboles ou un build ne suffit pas à valider l'apparence.
