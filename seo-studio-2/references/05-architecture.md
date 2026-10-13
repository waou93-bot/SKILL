# Architecture de pages, données et maillage

## Un besoin, une intention, un propriétaire

Regrouper les variantes qui appellent la même réponse. Affecter une page propriétaire
par intention ; plusieurs intentions proches peuvent partager une page si elle y
répond clairement. Ne pas créer un article par mot-clé ni fusionner des pages utiles
au seul motif qu'elles partagent des termes. Garder les pages existantes qui servent
le lecteur et vérifier les impacts avant toute modification d'URL.

Chaque page a : ID stable, URL, langue, type, rôle dans le parcours, intention,
public, parent, contenu distinctif, preuve attendue, title/H1, description proposée,
canonical, politique d'indexation, action suivante, propriétaire et vague de sortie.
Le domaine peut rester inconnu pendant le plan ; utiliser des chemins stables.

Pour chaque hub, catégorie ou index riche en contenus, préciser le corpus recherché,
les types et champs couverts, les filtres utiles et les destinations des résultats.
Prévoir une recherche en tête de rubrique selon [le contrat de design](06-design.md#recherche-en-tête-des-rubriques),
sur tout ce corpus, y compris les entrées hors de la première page. Une recherche
globale seule ne suffit pas ; une courte rubrique peut justifier son absence.

Pour les pages prioritaires, intégrer la [matrice de sous-questions et propriétaires](14-fanout-retour-sites.md)
à l'inventaire : branche observée ou hypothèse, réponse/section, preuve, décision et
action suivante. Une branche peut rester sur la page principale ou renvoyer vers
une page existante ; le fan-out n'impose pas une nouvelle URL par question.

## Architecture selon le site

| Type | Pages et parcours prioritaires | À ne pas imposer |
|---|---|---|
| Média / affiliation | accueil orientant, hubs d'usage, guides, comparatifs, méthodes, auteurs réels, transparence | boutique fictive, panier, produit testé sans essai |
| Comparateur / outil | choix du besoin, critères, résultat expliqué, fiches sources, alternatives, limites | dizaines de pages de résultats minces indexables |
| Vitrine / service | prestation, cas d'usage, preuve, périmètre géographique réel, contact/devis | affiliation parasite, blog quotidien, fausses implantations |
| E-commerce | catégories, variantes réelles, fiches, livraison/retour, aide au choix | reprendre le fabricant sans valeur, indexer tous les filtres |
| SaaS | produit, cas d'usage, prix réels, démo, intégrations, aide/docs publiques | indexer les espaces privés ou inventer des clients |
| Annuaire | catégories, fiches vérifiées, filtres utiles, contribution/modération | pages locales quasi identiques sans offre réelle |

## Graphe de maillage explicite

Ne pas livrer « créer un cocon ». Produire les liens au niveau page :
`from`, `to`, ancre, emplacement, raison utilisateur, type de relation et statut.
La structure minimale utile est parent/hub → page de décision → page d'action,
avec retour contextuel vers les prérequis et alternatives. Les pages de preuve et
méthode sont accessibles là où le lecteur en a besoin, pas uniquement au footer.

Une nouvelle page décrit ses liens entrants depuis des pages existantes ET ses
sortants. Lier vers une ressource pertinente d'un autre cluster si la tâche le
justifie ; ne pas enfermer le lecteur dans un silo artificiel. Une page indexable
prioritaire sans chemin depuis l'accueil est un défaut bloquant du plan.

Les ancres expliquent la destination, pas une suite répétée de mots-clés. Les liens
utiles doivent devenir des ancres HTML explorables ; les cartes et menus visuels
ne remplacent pas les liens. Voir S06 pour la recommandation Google. La profondeur
visée est définie par le projet ; « trois clics » n'est pas une loi de classement.

Éviter blocs géants de recommandations sans ordre, maillage réciproque systématique
entre tous les sites du propriétaire, liens cachés, pages satellites et achat de
liens suivis. Une citation externe utile n'est pas obligatoirement affiliée.
Les liens internes n'utilisent pas d'UTM pour simuler une nouvelle acquisition.

## Taxonomie et indexation

Distinguer catégorie de navigation, tag, attribut produit et filtre. Une combinaison
indexable doit répondre à une intention propre avec contenu suffisant et catalogue
pertinent. Spécifier la politique des tris, recherches internes, paramètres, filtres,
pagination, variantes, pages vides, rupture, archives, erreurs et futures langues.
Ne pas canoniser systématiquement les pages 2+ sur la première ; analyser le contenu.
`robots.txt` n'est ni une authentification ni un effacement garanti de l'index.

## Modèle CMS/data

Prévoir, selon le besoin : Page, Hub, Article, Guide, Comparison, Product, Variant,
Offer, Partner, Author, Source, Claim, Media, Link, Disclosure et Redirect. Éviter
copier le même prix dans dix articles : séparer le contenu durable de l'offre datée.
Un auteur porte une identité et des compétences réelles ; une équipe IA n'est pas
une équipe médicale ou une rédaction de testeurs humains.

Documenter IDs, champs obligatoires, relations, statuts, règles d'unicité, fraîcheur,
validation, droits d'édition et passage brouillon/relecture/publié. Une offre périmée
peut être masquée sans casser le guide. Une fiche documentaire ne devient pas une
fiche de marchand parce qu'un lien affilié est présent.

## Migration ou site existant

Importer l'inventaire, mapper anciennes/nouvelles URLs, décider maintenir/enrichir/
fusionner/rediriger au cas par cas, prévoir retour arrière et tests. L'audit seul
n'autorise aucune suppression. Le changement de framework n'est jamais une tâche SEO
par défaut. Documenter l'impact sur chaque brief, lien entrant et événement mesuré.
