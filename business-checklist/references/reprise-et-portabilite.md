# Reprise, versions et plusieurs ordinateurs

## Deux objets séparés

Le skill contient la méthode et ses modèles. Le projet contient ses preuves,
BUSINESS/, décisions et chiffres. Installer le skill sur un second PC ne transfère
ni les fichiers du projet, ni les secrets, ni l'historique de conversation.

## Projet existant

Lire en priorité le MASTER canonique, le dernier dossier BUSINESS, les décisions,
les ventes/mesures accessibles et les engagements en cours. Ne pas créer un autre
MASTER parce qu'un dossier est incomplet. Actualiser les parties affectées.

Consigner coûts passés, engagements encore dus et investissements futurs séparément.
Une dépense déjà engagée peut avoir une conséquence de cash future : ne pas l'effacer
en invoquant les coûts irrécupérables. Une dette existante continue à compter.

## Un PC ou deux

Employer la même version du skill sur les machines qui travaillent sur le projet.
Utiliser des chemins relatifs dans les livrables ; ne pas y figer un nom Windows.
Avant reprise, vérifier version du dossier et éventuels conflits. Ne pas faire écrire
deux agents simultanément dans les mêmes fichiers. Ne pas lancer un pull, reset,
commit ou push non demandé ; respecter le dépôt canonique s'il est fourni.

Un dépôt de skills peut partager la méthode ; le dépôt/dossier du projet partage
les données. Éviter d'y publier données clients, clés ou identifiants privés.
Une vérification locale dans un environnement hébergé ne prouve pas l'installation
sur l'ordinateur de l'utilisateur.

## Mise à jour du skill

Version 2 change le nom technique de `business` à `business-checklist` et le contrat
JSON. Ne pas renommer aveuglément un dossier existant personnalisé. Sauvegarder
hors des répertoires scannés, comparer, préserver les règles locales et déterminer
une unique version active. Garder les décisions V1 et les marquer comme historiques.
Ne pas les convertir automatiquement en nouveaux GO sans examen des preuves.
