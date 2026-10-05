---
name: newsit-seo
description: "Newsit SEO : concevoir, construire ou reprendre un site vitrine, marchand, d'affiliation ou hybride avec newsite, newpro, brain, organisation et seo-methodologie. Pour un nouveau site, demander le type s'il manque, proposer exactement deux stacks argumentées et recommander la meilleure pour le projet. Respecter l'architecture souhaitée, intégrer et vérifier les exigences SEO actuelles pertinentes de Google et Bing, dont title, descriptions et données structurées. Aller jusqu'à la réalisation vérifiée quand elle est demandée. Reconnaître aussi Newsite SEO et New Site SEO ; une retouche isolée ou un audit SEO seul suit le parcours ciblé."
compatibility: "Codex et assistants disposant de fichiers et, pour les recherches actuelles, du web. Charger les skills sources réellement disponibles ; les outils, connecteurs, sous-agents et accès externes restent facultatifs."
metadata:
  version: "1.0.2"
  language: "fr"
---

# Newsite SEO — système de réalisation

Produire le meilleur site défendable pour le besoin, les preuves, les contraintes et les moyens du projet. Faire converger architecture, utilité, direction artistique, SEO et conversion. Un beau site sans parcours utile, ou beaucoup de pages sans réponse distinctive, ne remplit pas la mission.

Le nom visible est **Newsit SEO**, l'identifiant unique est `newsit-seo`. Ce skill ajoute un parcours aux skills sources ; il ne les renomme pas et n'en remplace pas les installations.

## Contrat prioritaire de réalisation complète

Une demande « crée un site de bout en bout » avec niche et type déclenche la fabrication complète dans le périmètre autorisé, pas seulement un brief ou une tranche verticale. Les choix réversibles sont délégués : recommander une stack et avancer, sans imposer une validation intermédiaire. Comparer deux stacks lorsque le choix reste ouvert ; ne pas attendre une réponse optionnelle. Les décisions déjà validées restent prioritaires. Une question n'arrête que les opérations qui dépendent réellement de sa réponse.

Lire et appliquer [le parcours de complétion](references/systeme-execution.md), [la référence d'architecture Thomas](references/architecture-thomas.md) et [les préférences de Nicolas](references/preferences-nicolas.md). Utiliser [le registre des skills](references/registre-skills.md) pour charger les instructions réelles au moment utile. Pour un correctif ou un audit seul, sélectionner les étapes touchées et justifier les exclusions ; ne pas déclencher une reconstruction.

Tenir un seul registre de réalisation dans le MASTER existant, avec [le modèle](assets/execution.json). Chaque étape et chaque page demandée possède un état, une preuve et, si nécessaire, un blocage précis. « Skill cité » ou « fichier lu » ne vaut jamais « travail réalisé ». Vérifier le registre avec [le contrôleur](scripts/check_execution.py) avant le compte rendu final. Ce contrôle vérifie la complétion déclarée ; il ne remplace pas la recette du site.

Les règles ci-dessus précisent le mandat actuel de Nicolas pour ce système et prévalent sur les anciennes pauses de cadrage ci-dessous ou dans les skills sources. Elles n'autorisent pas les dépenses, la publication externe ou les actions hors périmètre. La livraison locale complète et la publication sont deux états distincts. Ne pas marquer une étape applicable comme exclue pour gagner du temps.

## 1. Entrer par le contexte et le type de site

Lire les instructions applicables, le dossier actif, les décisions et le MASTER existant avant de poser une question. Identifier si la demande concerne conception, réalisation, reprise, migration ou correction ciblée. Un MASTER existant demeure la source de vérité ; ne pas créer un second MASTER pour la même activité.

Si le type manque réellement, demander d'abord :

> Quel type de site veux-tu créer : un site vitrine pour présenter une activité et recevoir des demandes, un site marchand pour vendre directement, ou un site d'affiliation pour conseiller et orienter vers des marchands ? Un mélange est possible.

Avec un outil de questions disponible, proposer les trois choix et permettre le cas hybride en réponse libre. Sans outil adapté, poser cette question directement. Si le type est déjà donné ou établi dans le projet, le confirmer brièvement et poursuivre sans le redemander. Si aucune réponse n'arrive, avancer sur les éléments communs et laisser le choix ouvert ; ne pas inventer une boutique ou une affiliation.

Après ce choix, demander seulement les informations qui changent une décision : activité, visiteurs, pays/langue, action attendue, architecture imposée, identité/DA, données disponibles, contraintes de stack/hébergement, budget ou capacité de maintenance. Réutiliser toutes les réponses déjà présentes. Poser une question à la fois lorsque les réponses sont dépendantes ; grouper les inconnues indépendantes si l'hôte le permet.

Fixer explicitement :

| Dimension | Valeurs ou résultat |
| --- | --- |
| Type principal | `vitrine`, `marchand`, `affiliation`, `hybride` |
| Mode | `conception`, `realisation`, `reprise`, `migration`, `cible` |
| Architecture | Arborescence, parcours, données, architecture technique et contraintes imposées |
| Conversion | Demande qualifiée, achat confirmé, clic marchand mesuré ou autre résultat réel |
| Contexte | Neuf/existant, décisions validées, données, accès et capacité de maintenance |
| Autorisation | Travail local, recherche, données privées, publication, dépenses : périmètres distincts |

Lire [les intégrations](references/integrations.md), puis le profil pertinent : [vitrine](references/vitrine.md), [marchand](references/marchand.md), [affiliation](references/affiliation.md). Pour un hybride, composer les profils avec une conversion principale par parcours et une frontière claire entre vendeur et conseil affilié. Pour toute conception ou réalisation complète, lire obligatoirement [le contrat Google et Bing](references/google-bing-seo.md). Ce contrat intègre les [principes Bing pour recherche et réponses IA](references/bing-principes.md) : les lire pour un projet complet ou une demande ciblée Bing, puis traduire les règles applicables en preuves de recette.

## 2. Coordonner les vrais skills

Charger leurs SKILL.md réels et les références requises au moment utile. Garder une seule coordination : Organisation ou Newsit SEO selon le point d'entrée. Un skill appelé restitue son travail sans relancer le même orchestrateur.

| Skill source | Mandat dans Newsit SEO |
| --- | --- |
| `organisation` | Contexte, rôles, dépendances, priorités, contrat de complétion et continuité |
| `brain` | Prémisses, preuves, contradictions, inconnues, couverture et jugement critique |
| `newpro` | Inspection, reprise/bootstrap prudent du MASTER et validation de sa structure |
| `newsite` | Direction artistique, contrat de conversion, stack adaptée, tranche verticale et recette, dans son périmètre non marchand |
| `seo-methodologie` | Intentions distinctes, catalogue fiable, catégories/guides/comparatifs et maillage utile |
| `seo` si disponible | Recherche de demande, diagnostic technique, mesure et priorisation du canal |

`newsite` ne couvre pas à lui seul le checkout ni le modèle marchand : utiliser les profils de ce skill et les compétences de réalisation nécessaires. `newpro` prépare le socle ; il ne construit pas le site. Brain aide au raisonnement ; le nom du skill ne prouve pas l'existence d'un agent ou d'un modèle spécial.

Pour une réalisation complète, charger `Memory`, `toolbox`, `design-dna`, `no-slop` et `human-reading`. Charger selon besoin `design-dna`, `design-taste-frontend`, `no-slop`, `asset-continuity`, `product-marketing`, `cro`, `site-checklist`, `business-checklist` et les skills techniques disponibles. Ne pas charger tout l'inventaire par principe. Pour un nouveau projet explicitement monétisé, intégrer Business avant un investissement important ; réutiliser une étude déjà valable et éviter un business plan complet pour un correctif.

Un skill absent est une dépendance manquante, jamais un skill prétendument exécuté. Continuer les parties réalisables avec les règles présentes, documenter la limite et nommer les travaux bloqués. Lire [les intégrations](references/integrations.md) pour les portes propres à chaque source.

Un agent par défaut. Déléguer seulement si l'utilisateur ou les instructions applicables l'autorisent, si les tâches sont séparables et si l'outil existe ; respecter le routeur d'Organisation et ses limites. À défaut, réaliser les rôles successivement sans annoncer de revue indépendante.

## 3. Rechercher et choisir une proposition

Examiner un échantillon du site existant si pertinent : accueil, pages commerciales, guides, fiche, formulaire/panier, langues et erreurs. Consigner ce qui est réellement observé. Un échec de l'outil n'est pas la preuve d'une panne.

Pour un lancement complet, étudier trois références actuelles pertinentes conformément à `newsite` lorsqu'il est utilisé : métier, intention, navigation, DA, UX, preuve et conversion. Si le domaine est étroit, identifier les références adjacentes ; si l'accès manque, marquer la recherche incomplète. Ne pas copier leurs textes, composants ou médias. Ne pas déduire trafic, ventes ou stack sans preuve. Un audit concurrentiel SEO plus large reste distinct de ces trois références de design.

Rechercher les besoins réels et les alternatives. Utiliser sources primaires, pages fabricants, documentation officielle et données autorisées. Les forums peuvent éclairer le langage et les objections ; ils ne prouvent pas un volume de recherche. Les chiffres SEO non mesurés restent `NON_MESURE`.

Appliquer les principes génériques de parcours ci-dessous ; les historiques privés ne sont pas embarqués. Adapter la logique suivante au domaine : situation, besoin, aide au choix, preuve, solution, action. Relier des besoins seulement si la prochaine étape aide réellement le visiteur. Le commerce et l'affiliation découlent du conseil.

Formuler une recommandation principale : public, promesse prouvable, concept, parcours, architecture, conversion, DA et socle technique. Présenter une alternative seulement si elle expose un vrai arbitrage. Expliquer les raisons et les limites de la recommandation ; ne promettre ni meilleur classement, ni trafic, ni revenu.

## 4. Respecter et enrichir l'architecture souhaitée

Distinguer contraintes imposées, choix validés et suggestions. Garder les URLs utiles, le CMS, la stack et la DA existants lorsqu'ils font partie de l'architecture souhaitée. Ne pas remplacer silencieusement une architecture par un modèle générique de silo SEO.

Construire une table de pages dans le MASTER avec : URL, type, visiteur, intention principale, réponse distinctive, source/donnée, CTA et suite réelle, liens entrants/sortants, statut d'indexation, priorité et maintenance. Utiliser [le modèle](assets/pages.csv) si aucune convention n'existe.

Créer une URL seulement pour une intention distincte et une réponse suffisamment utile. Fusionner les synonymes, éviter les permutations de filtres et relier chaque page importante par de vrais liens HTML. Les liens transversaux suivent la prochaine question du visiteur. Relier une expérience interactive à une réponse et une navigation HTML accessibles à tous.

Si une contrainte compromet le parcours, la découvrabilité ou la maintenance, expliquer le conflit et proposer le plus petit ajustement. Conserver la contrainte tant que son changement n'est pas autorisé. Préparer un mapping et un retour arrière pour toute migration d'URL ; ne pas supprimer sur la seule base d'un faible trafic.

Pour la DA, suivre l'ordre de `newsite` : concept, direction artistique, composition, typographie, grille, interaction, mouvement, implémentation. Réutiliser le Design DNA et le canon validés. Donner aux images un rôle, une provenance et des droits vérifiés. Les effets servent compréhension, preuve ou identité, avec fallback, mobile et mouvement réduit.

### Choix entre deux stacks avant la fabrication

Pour chaque **nouveau site**, proposer exactement deux stacks crédibles, adaptées au type, au parcours, à l'architecture souhaitée et à la maintenance. Lire [le contrat de choix](references/deux-stacks.md). Expliquer pourquoi ces deux options ont été retenues, leurs différences concrètes, les contraintes/coûts vérifiés ou inconnus, et **laquelle paraît la meilleure avec les raisons propres au projet**. En mode conception ou si un choix utilisateur est explicitement requis, présenter ce choix. En réalisation de bout en bout déléguée, retenir la recommandation compatible avec le brief, documenter ce choix et poursuivre sans pause de convenance.

Avec une question optionnelle sans réponse, avancer sur l'option recommandée seulement si l'autorisation de réaliser et les contraintes permettent ce choix réversible ; annoncer l'hypothèse. Une validation obligatoire encore pending ne vaut jamais accord. Si la **stack complète** est déjà imposée ou validée, conserver ce choix et expliquer son adéquation sans redemander ; ne pas proposer une migration inutile. Si seul un framework ou un hébergeur est imposé, le garder comme contrainte et comparer deux compositions compatibles pour les couches encore ouvertes : CMS, backend, catalogue ou moteur marchand.

Consulter les sources techniques actuelles et le routeur réel de `newsite`. Un site éditorial léger peut comparer Astro et une alternative adaptée ; une boutique peut comparer un moteur établi et une autre solution maintenable. Ne pas imposer Astro/Next.js à tous les types ni présenter deux variantes de nom d'une même solution comme un véritable choix. Aucun framework ni prestataire n'est obligatoire et aucune version n'est inventée.

## 5. Organiser contenu, catalogue et preuves

Séparer entités et présentation : situations/besoins, services ou produits, catégories, critères, offres marchandes, kits/looks si utiles, guides et sources. Éviter une seconde copie du catalogue dans chaque article. Lire le profil pour les champs nécessaires.

Pour toute donnée sensible au temps, conserver source, date et responsabilité de mise à jour. Distinguer déclaration fabricant, offre marchand, avis utilisateur, calcul reproductible et essai direct. Ne pas inventer caractéristique, prix, stock, test, expertise, note, témoignage ou résultat. Un média illustratif ne prouve pas une référence produit exacte.

Rédiger selon l'intention : réponse claire, critères utiles, options par profil, compromis, limites, alternative et prochaine étape. Ajouter tableau et FAQ seulement s'ils apportent une réponse. Éviter quantité de mots imposée, mots-clés artificiels et dates mises à jour sans changement réel.

Pour l'affiliation, révéler la relation commerciale près du parcours concerné, qualifier les liens sponsorisés et vérifier les conditions actuelles du programme. Séparer critères de choix et rémunération. Ne pas créer un faux checkout, un panier externe non confirmé ou une fausse possibilité d'achat.

Pour le commerce, exiger références exactes, variantes, prix et stock fiables, livraison/retours réels et parcours de commande côté serveur. Ne pas marquer achat confirmé à partir d'un simple écran de succès. Voir [marchand](references/marchand.md).

## 6. Proposer, puis réaliser dans le périmètre autorisé

En mode conception, livrer une proposition complète et reviewable : brief, architecture, carte des pages, parcours, direction visuelle, données, stack argumentée, tranche verticale, backlog et critères. Ne pas prétendre avoir construit ou testé le site.

En mode réalisation demandé, faire le cadrage nécessaire puis construire effectivement le site. Tenir compte des validations déjà données ; ne pas demander de nouveau accord pour chaque décision réversible. Respecter les portes applicables des skills sources sans transformer une routine technique en permission supplémentaire. Si une décision importante reste incompatible avec le brief, avancer sur les parties indépendantes et poser la seule question nécessaire.

Commencer par la tranche verticale du profil :

| Profil | Première preuve de fonctionnement |
| --- | --- |
| Vitrine | Page d'entrée, offre/preuve, demande qualifiée, réception et confirmation réelles |
| Marchand | Catégorie, fiche/variante, panier, paiement de test, commande serveur confirmée |
| Affiliation | Situation/guide, choix expliqué, produit sourcé, lien marchand exact et événement de clic |
| Hybride | Un parcours de bout en bout, puis le second avec responsabilités clairement séparées |

Contrôler cette tranche avant d'étendre aux pages prioritaires de la portée demandée. Une tranche verticale est une étape de validation, pas une raison de laisser inachevé un site complet déjà autorisé. Prévoir chargement, absence de données, erreur et succès utiles.

Ne pas s'arrêter à un plan lorsqu'une réalisation est demandée. Ne pas réinitialiser l'existant, changer un fournisseur ou engager une dépense pour avancer plus vite. Ne pas installer de serveur, veille ou automatisation permanente sans demande.

## 7. Vérifier séparément technique, contenu et expérience

Lire [SEO et recette](references/seo-et-recette.md) et appliquer obligatoirement [le contrat Google et Bing](references/google-bing-seo.md). À chaque projet complet, actualiser les règles officielles et établir la matrice exhaustive des dimensions pertinentes ; ne pas recopier seulement la checklist datée du skill. Garder quatre états de contrôle : `VERIFIE`, `A_CORRIGER`, `NON_VERIFIE`, `NON_APPLICABLE`, avec preuve, source, date et environnement. Toute exclusion exige une raison.

Le SEO est une exigence de fabrication dès l'architecture, puis dans chaque gabarit : `title`, descriptions, titres visibles, HTML découvrable, directives, canonical, sitemap, liens, images et données structurées appropriées. Les « textes invisibles » désignent les métadonnées légitimes et les descriptions/accessibilités utiles. Ne pas créer de H1 caché, bloc de mots-clés hors écran ou contenu différent pour Googlebot/Bingbot afin de manipuler le classement. Les textes accessibles aux lecteurs d'écran et les contenus accordéons utiles restent légitimes.

Le gate SEO bloque l'annonce « prêt pour publication » tant qu'une exigence critique applicable échoue ou reste sans preuve. Corriger dans le périmètre autorisé, ou livrer `PARTIEL` avec le blocage précis. Sans accès aux règles ou rapports, l'exhaustivité et l'indexation restent non vérifiées ; le site peut être préparé sans fausse déclaration de conformité ou de classement.

- **Technique :** commandes disponibles, types/build, HTTP, erreurs, robots/noindex, canonical, sitemap, liens explorables, rendu HTML, balisage conforme au contenu visible, paramètres et langues si présents.
- **Données/contenu :** référence et catégorie justes, compatibilité des unités, source/prix datés, sélection distinctive, médias cohérents et aucune preuve inventée.
- **Perception/UX :** vraie navigation mobile/desktop, clavier/focus, lisibilité, CTA et suite réelle, compréhension à froid, images dans leur cadrage final, absence de débordement et mouvement réduit. Une donnée techniquement exacte mais visuellement trompeuse échoue.
- **Conversion/mesure :** événements réellement déclenchés, formulaires ou paiement de test aboutis, distinction clic/demande/commande/revenu et absence de double comptage.

Un score Lighthouse ne valide ni le SEO, ni l'indexation, ni la conversion. Sans navigateur, ne pas déclarer la recette visuelle réussie. Sans Search Console, ne pas déclarer une indexation ou une performance organique vérifiée. Avant publication autorisée, vérifier aussi la version réellement servie ; sinon livrer la version locale et ses limites.

## 8. Livrer et maintenir

Suivre les conventions du MASTER existant. Pour un nouveau cadrage, adapter [le brief](assets/brief.md) ; ne pas créer des documents vides pour remplir une liste. Conserver architecture, décisions, sources, carte des pages, données, backlog et preuves. Réutiliser `SEO/` et ses conventions si le skill `seo` les a déjà créés.

Définir événements et dénominateurs avant de mesurer. Les ventes et commissions affiliées nécessitent un rapport marchand autorisé ; un clic sortant n'est pas une vente. Un achat test n'est pas une vente réelle. Ne pas attribuer le trafic direct à un canal précis sans preuve.

Prévoir maintenance selon la volatilité : liens, produits retirés, disponibilité, prix, sources et contenus. Commencer avec des pages maintenables puis étendre selon les observations réelles. Proposer un plan 30/60/90 jours seulement si utile ; il ne garantit pas un résultat SEO et ne programme aucune tâche.

Conclure par résultat, périmètre réalisé, vérifications exécutées, inconnues/blocages et prochaine action utile. Employer `COMPLET`, `PARTIEL` ou `BLOQUE` selon les preuves. Séparer conception validée, site construit, version publiée et performances mesurées.

Pour maintenir ce skill, consulter [le protocole d'évaluation](references/evaluation.md) et [les scénarios](evals/evals.json). Un contrôle de fichiers n'est pas un test comportemental ni une garantie de qualité des futurs sites.

## Préférences permanentes de Nicolas : héros et navigation

Pour les nouveaux sites et les reprises demandées par Nicolas, appliquer ces préférences sauf instruction explicite contraire dans le projet :

- Le héros contient toujours une illustration, une animation ou une vidéo au format 16:9. Le média et sa composition doivent être réellement panoramiques : ne pas placer un média carré dans un conteneur 16:9 pour prétendre satisfaire cette règle. Garder le sujet lisible et entier ; si du texte est superposé, prolonger le décor et préserver le contraste. Sur mobile, conserver le média 16:9 visible sans recadrage destructeur ; adapter la position du texte.
- La navigation principale comprend un lien « Accueil ». Le bandeau se masque quand le visiteur descend et réapparaît dès qu’il remonte ; il reste visible en haut de page. Éviter les espaces de défilement vides et les délais qui cachent les rubriques. Les animations respectent prefers-reduced-motion ; le menu reste accessible au clavier et fonctionne sans JavaScript.
- Vérifier ces comportements dans le navigateur sur ordinateur et mobile, ainsi que l’accès aux liens au clavier. Consigner l’environnement et les limites dans la recette.

Ces préférences enrichissent le cadrage et les contrôles des sections 4 et 7. Elles ne changent pas l’architecture, la direction artistique validée, ni les limites d’autorisation de publication ou de dépenses.
