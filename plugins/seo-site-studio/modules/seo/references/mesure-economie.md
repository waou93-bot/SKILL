# Mesure, scénarios et économie du canal

## Un contrat de mesure avant la promesse

Définir l'objectif, l'événement, la population, la période, la fenêtre de conversion,
la source, les filtres, les limites et le responsable. Distinguer une micro-conversion
(clic, formulaire démarré) d'un prospect qualifié, d'un nouveau client et d'un revenu.
Une création de compte n'est pas nécessairement une vente. [S13]

Traiter séparément : santé technique ; visibilité ; visites qualifiées ; conversion ;
revenu net ; marge contributive. Pour un projet non commercial, employer des objectifs
utiles au service rendu, sans inventer de prix ou de valeur monétaire.

Search Console et analytics n'observent pas le même événement. Ne pas exiger l'égalité
clics = sessions = utilisateurs. Signaler filtres, anonymisation/agrégation, délais,
consentement, blocages et règles d'attribution. Vérifier la documentation disponible
au moment du travail. Une corrélation avant/après n'est pas un effet causal prouvé.

## Sources et périmètres

Séparer marque/hors marque avec une définition contrôlée (variantes, fautes, ambiguïtés),
pays/langue, appareil, moteur, pages et intentions. Comparer périodes complètes de
longueurs comparables, saison précédente quand pertinente et historique suffisant.
Les valeurs faibles réclament prudence, pas seuils universels. La position moyenne
représente un agrégat, non une position garantie sur toutes les recherches. [S13]

Ne pas extrapoler une liste de requêtes filtrées/anonymisées à 100 % de la demande.
Ne pas stocker mots de passe, jetons, e-mails clients ou contenus confidentiels.
Avant nouvelle instrumentation, respecter le consentement et les règles applicables ;
les vérifier selon le pays plutôt que créer une configuration « sans consentement ».

## Scénarios : calculs transparents, pas prédictions de classement

Mode A, données projet : établir baseline puis variations hypothétiques argumentées
par page/cluster. Mode B, estimation de demande : utiliser des volumes dédupliqués,
datés et localisés ; ne pas ajouter ensuite une baseline recouvrant ce volume.

Formules de scénario possibles (choisir et définir les dénominateurs) :

    clics_estimes = impressions_estimees × CTR_hypothetique
    clients_estimes = sessions_eligibles × taux_de_conversion_hypothetique
    revenu_net_estime = commandes_estimees × panier_net_hypothetique
    contribution_estimee = revenu_net_estime − couts_variables_associes
    solde_canal = contribution_incrementale_estimee − couts_SEO_incrementaux

Ne pas mélanger clics et sessions sans hypothèse de passage. Les impressions estimées
ne sont pas automatiquement tout le volume recherché. Ne pas appliquer un coefficient
« zéro clic » si le CTR choisi intègre déjà cet effet. Les taux dépendent de l'intention,
de l'appareil et des formats ; aucun CTR « top 1 » universel dans le modèle.

Coûts : temps de recherche/rédaction/relecture/expertise, développement, médias,
outils, coordination, maintenance et suivi. Séparer cash et temps valorisé. Distinguer
investissement initial et entretien ; éviter de doubler un coût déjà compté dans Business.

Sur une période et une base cohérentes :

    clients_additionnels_pour_equilibre = cout_SEO / contribution_par_nouveau_client

Valide seulement si contribution positive, horizon compatible et coûts/délais pris
en compte. Pour un abonnement, ne pas utiliser une LTV infinie ou non observée pour
masquer le cash négatif. Un achat unique ne devient pas du revenu récurrent.
Si le dénominateur manque, écrire NON_CALCULABLE. Si aucun nouveau client observé,
un CAC calculé par division par zéro n'est pas zéro.

ROI incrémental seulement si une estimation de l'incrément est défendable ; sinon
rapporter coût et revenus attribués sans prétendre à la causalité. Les achats assistés
et directs sont documentés sans double comptage. Ne pas valoriser un lead au prix
d'une vente et ne pas compter tous les clients comme nouveaux.

Scénarios défavorable/central/favorable ; chaque entrée porte statut et provenance.
Inclure un scénario zéro gain commercial sur la période pilote et son coût maximal.
La planification 30/60/90 jours est un rythme de travail, pas une prévision de traction.
Les effets SEO ont des délais variables. [S02]

## Expériences et suivi

Préenregistrer changement, hypothèse, groupe de pages, baseline, métrique, seuil
justifié, fenêtre et facteurs externes. Le test doit pouvoir échouer ou rester non
concluant. Utiliser un groupe témoin lorsque faisable ; sinon expliciter les limites.
Après publication autorisée : contrôles techniques immédiats et bilan commercial à
une fenêtre adéquate, sans prétendre disposer déjà de données futures.

Les données IA suivent le module dédié. Ne jamais ajouter une sous-catégorie à son
total parent. Sources : [bibliographie](sources.md).
