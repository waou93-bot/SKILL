# Roadmap, budget et transfert à la production

## Prioriser sans produire à l'aveugle

Classer par besoin utilisateur, preuve de demande, avantage propre, effort, coût de
maintenance, risque et dépendances. Écrire la raison de priorité. Un score de confort
interne est permis s'il est transparent ; ne pas lui donner une précision probabiliste
ou financière qu'il n'a pas. Le coût de contrôle des produits fait partie de l'effort.

Préparer deux niveaux : carte complète du site cible, puis version de lancement assez
petite pour pouvoir vérifier et maintenir chaque page. Toutes les pages V1 ont un brief
complet, tous les articles du backlog ont un rôle et des conditions de production.
Un backlog de cent sujets n'autorise pas une publication en masse.

## Séquence de livraison

Lot 0 : résoudre les dépendances et preuves qui pourraient invalider l'approche.
Lot 1 : valider un parcours entier (entrée → compréhension → choix → action utile),
avec ses pages de méthode/confiance et son instrument de mesure.
Lot 2 : élargir les clusters dont la preuve, la capacité et les premiers retours le justifient.
Lot 3 : améliorer les offres, contenus et outils avec des observations comparables.

Une projection 30/60/90 jours peut organiser le travail, mais ne garantit pas du trafic
à 90 jours. Si budget ou capacité sont inconnus, donner des tailles relatives et les
hypothèses, pas un planning ferme inventé. Inclure le scénario où aucune vente n'arrive
pendant l'observation. Prévoir `CONTINUER`, `CORRIGER`, `ARRETER`, `NON_CONCLUANT`.

## Ticket de réalisation

ID, exigence, objectif, URL/composant/dataset, propriétaire, entrées, preuves, changement,
hors périmètre, dépendances, taille/estimation et statut, test d'acceptation, rollback,
critique assigné, permission et version de mandat. Aucun « optimiser le SEO » sans
changement vérifiable. Un ticket de production ne réécrit pas les décisions stratégiques.

## Livrer au développeur

Fournir architecture/routes, modèle de données, skin, gabarits et états, textes V1,
composants partenaires, graphe de liens, sources/assets/droits, ADR, tests, priorités,
restrictions et autorisations. Inclure commandes connues du projet, jamais deviner une
commande de build. Les secrets restent hors du dossier ; décrire leur nom et usage
uniquement si nécessaires et autorisés.

Geler le dossier avec un manifeste d'empreintes. Le producteur signale toute ambiguïté
ou impossibilité avant de changer la solution. Les changements concernent la bonne
version et propagent leur invalidation vers contenu, liens, tracking et QA. Le maintien
de la cohérence l'emporte sur la commodité d'un composant préfabriqué.

## Post-lancement

Préparer le périmètre de seo-post-deploy et les contrôles au moment où les données sont
suffisantes. Les résultats sont séparés par canal, marque/hors marque, gabarit et appareil
si les données le permettent. Tester les hypothèses plutôt que modifier tout le site
après trois jours sans clic. Les contrôles manuels de monitoring peuvent être exécutés dans le périmètre autorisé
avec les données disponibles. Seule leur exécution récurrente exige une demande
et un ordonnanceur réel ; une lecture ponctuelle n'exige pas une automatisation.
