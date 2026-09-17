# Modèle financier — règles de construction et de contrôle

Spécification de travail. Fondements généraux : S02, S03, S07, S08, S10–S12.
Ce document ne fixe ni taux fiscal ni choix juridique. Les vérifier à chaque projet
sur des sources officielles du territoire, et faire revoir les engagements sensibles.

## 1. Les hypothèses avant les tableaux

Un modèle doit expliquer pourquoi des clients arrivent, ce qu'ils achètent et
quand l'argent entre ou sort. Chaque entrée porte : identifiant, unité, période,
source/observation ou hypothèse, date, scénario, confiance et lien vers le test.
Le statut `INCONNU` n'est pas égal à zéro. Les objectifs ne sont pas des prévisions.

Horizon par défaut : trois ans ; mensualisation des 36 mois lorsque les informations
permettent une granularité utile. Années 4–5 annuelles seulement si pertinentes au
financement/développement. Pour une idée très précoce, d'abord modèle paramétrique
et fourchettes ; présenter clairement que ce n'est pas un prévisionnel validé.

Livrables chiffrés lorsque les entrées existent : hypothèses, acquisition/ventes,
cohortes, coûts directs, personnel/charges, investissements, résultat, BFR, dette,
trésorerie, bilan, financement, scénarios et contrôles. Si génération de tableur,
utiliser les capacités tableur de l'hôte et vérifier les formules/recalculs.

## 2. Chiffre d'affaires par mécanisme

**Achat unique** : unités livrées × prix net reconnu. Traiter remboursements,
remises, coût de distribution, migrations, support et mises à jour. Ne pas appeler
MRR une moyenne mensuelle de ventes ponctuelles. Une valeur vie client existe
éventuellement, mais ne se calcule pas comme celle d'un abonnement sans justification.

**Abonnement** : cohortes de nouveaux clients, activation payante, attrition,
réactivations et évolution du revenu des clients existants. Une facture annuelle
encaissée d'avance ne devient pas automatiquement douze mois de revenu à la date
du paiement : appliquer les règles comptables retenues et documentées.

**Services** : capacité facturable × utilisation × tarif net. Retrancher vente,
administration, congés, préparation et support du temps disponible ; le chiffre
d'affaires ne peut pas dépasser la capacité sans embauche/sous-traitance chiffrée.

**Marketplace** : volume de transactions × commission, plus revenus propres
séparés. Le volume d'affaires des vendeurs n'est pas par défaut le revenu de la
plateforme ; vérifier le rôle principal/agent et les règles applicables.

**Jeu / contenu** : ventes ou audience monétisable, commissions, remboursements,
cadence, coût du catalogue/contenu et durée de vie. Wishlists, vues et abonnés
ne se convertissent pas en ventes selon un taux universel.

**Matériel / commerce** : commandes, livraisons, stocks, retours, SAV, garanties,
capacité fournisseur et délais. Ne pas confondre prise de commande et vente réalisée.

Pour tous : l'acquisition doit produire les volumes prévus avec un délai crédible.
Une croissance de CA « +30 %/an » peut être un résultat du modèle, pas son unique cause.

## 3. Coûts et temps du fondateur

Classer coûts directs, fixes, variables et paliers en explicitant les conventions.
Inclure frais de paiement/distribution, hébergement, licences, données, calcul IA,
stockage, support humain, contrôle qualité, erreurs, remboursements et fraude selon
le produit. Une automatisation peut déplacer le coût vers la supervision.

Séparer : dépenses réellement décaissées ; charges comptables ; rémunération
économique du fondateur et coût d'opportunité. Ne pas additionner deux fois salaire
réel et salaire théorique. Montrer une lecture « cash » et une lecture « activité
capable de rémunérer le travail » lorsque le fondateur se paie peu ou pas au début.

## 4. Indicateurs, définitions et limites

**Marge sur coûts variables** = chiffre d'affaires net − coûts variables.
**Taux de marge sur coûts variables** = marge sur coûts variables / CA net.
**Seuil de rentabilité en CA** = charges fixes / taux de marge sur coûts variables,
si le taux est strictement positif et le mix d'offre cohérent.
Pour une seule offre à prix et coût stables :
**Unités d'équilibre** = charges fixes / (prix net unitaire − coût variable unitaire),
arrondies au supérieur quand l'unité est indivisible.

Si la contribution est nulle ou négative, augmenter les unités ne suffit pas à
atteindre l'équilibre dans ces hypothèses. Recalculer les paliers de capacité ;
ne pas étendre un coût fixe inchangé à un volume qui nécessite un recrutement.
L'équilibre d'exploitation ne couvre pas automatiquement dette, investissement
et calendrier de cash : les montrer séparément.

**CAC** : coûts d'acquisition définis / nouveaux clients acquis correspondants,
en respectant le décalage temporel du cycle de vente. Présenter par canal et en
vision complète, incluant travail commercial, outils et prestataires ; une mesure
marginale de campagne doit être étiquetée comme telle. Coût par lead ≠ CAC.
Ne pas diviser par des prospects non convertis ni par tous les clients historiques.

**Valeur vie / LTV** : préférer contribution observée par cohorte et intervalle
plausible. Un historique court ne justifie pas une durée de vie de plusieurs années.
La formule simplifiée ARPU × marge / churn repose sur une situation stationnaire
restrictive ; ne pas l'employer sans hypothèses, ni lorsque le churn est nul/non mesuré.

**Délai de récupération du CAC** : temps nécessaire à la contribution cumulée
pour couvrir le CAC ; utiliser les cohortes en cas de variation de prix, coûts ou
attrition. Un ratio LTV/CAC égal à trois n'est pas une norme universelle.

**Rétention** : définir activation, période, utilisateur/client, cohortes et
nombre absolu. **NRR**, si modèle approprié : revenus de la cohorte initiale après
expansion/contraction/pertes / revenus initiaux de cette même cohorte. Exclure les
nouveaux clients du numérateur. Une NRR élevée peut masquer la perte de clients :
montrer aussi rétention brute et concentration.

## 5. Résultat, bilan et trésorerie

Le compte de résultat suit revenus et charges reconnus. Le cash suit les paiements.
Distinguer TVA, délais clients/fournisseurs, acomptes, encaissements annuels, stocks,
impôts, intérêts, remboursement du principal et investissements.

Un capex est un décaissement ; son amortissement est une charge étalée selon la
règle applicable. Le remboursement du capital d'un prêt n'est pas une charge
d'exploitation ; les intérêts sont traités séparément. Ne pas capitaliser un coût
de développement simplement pour embellir le résultat.

**BFR d'exploitation simplifié** = stocks + créances d'exploitation − dettes
d'exploitation, à adapter aux avances clients/fournisseurs et autres postes.
Le relier aux délais et flux réels, sans ajouter deux fois le stock initial ou
les mêmes créances au financement.

**Cash final d'un mois** = cash initial + encaissements − décaissements.
Le cash initial du mois suivant doit être égal au cash final précédent.
Repérer le point bas, le premier mois sous le coussin souhaité et les ressources
nécessaires avant cette date. Le ratio cash/burn moyen peut aider, mais ne remplace
pas cette lecture en présence de saisonnalité ou de gros décaissements.

Vérifier **actif = capitaux propres + passifs** et réconcilier résultat/report à
nouveau, immobilisations/amortissements, dette et cash. Ne pas fabriquer une
« autre dette » ou une trésorerie d'équilibrage pour masquer une incohérence.

## 6. Scénarios et sensibilité

Défavorable : moins de clients, conversion plus basse, cycle plus long, retard de
livraison, remboursements/support plus élevés, coût fournisseur en hausse ou levée
non obtenue — choisir les chocs pertinents, pas une baisse mécanique identique partout.
Central : hypothèses les mieux justifiées ; pas une moyenne esthétique.
Favorable : bonnes performances plausibles avec capacité et coûts correspondants.

Faire varier les trois à cinq variables qui changent le plus la décision. Montrer
les valeurs de bascule : prix minimal, CAC supportable, volume requis, retard maximal,
charge de support limite. Ne pas appeler ces scénarios des probabilités de succès.

## 7. Financement et rendement

Partir d'une trajectoire de cash **avant nouveau financement non sécurisé**, qui
inclut les ressources déjà réellement disponibles une seule fois.
Besoin additionnel minimal à un horizon donné = montant permettant de maintenir
le cash au-dessus du coussin choisi à toutes les dates ; calculer le calendrier
et les contraintes de disponibilité. Les frais et effets du financement sont
ensuite intégrés et le modèle recalculé.

Ventiler les emplois : produit, acquisition, personnes, actifs, BFR et réserve,
avec étapes et résultats attendus. Faire coïncider le plan emplois/ressources et le
cash pour éviter les doubles comptes. Une aide espérée et un accord oral ne sont
pas des fonds sécurisés ; afficher un scénario sans eux.

Pour un prêt : échéancier et couverture du service de la dette, avec définition
précise du cash disponible. Aucun ratio obligatoire sans prêteur/dispositif réel.
Pour des investisseurs : scénarios illustratifs de dilution et sortie si utiles,
avec hypothèses, préférences contractuelles éventuelles et limites. Aucun multiple
ni retour garanti ; ne pas assimiler valorisation sur le papier et argent encaissé.

## 8. Contrôles avant remise

Tous les montants ont unité, devise, période et convention HT/TTC. Les cohortes et
clients ne deviennent pas négatifs. Les conversions restent dans leurs bornes.
Les totaux annuels correspondent aux mois. Les trois états se réconcilient.
Aucun zéro n'a remplacé une inconnue silencieusement. Les embauches et dépenses
ont des dates. Le porteur voit le scénario sans financement et sa perte maximale.
Faire vérifier les aspects comptables, fiscaux et engagements par les professionnels
compétents avant utilisation pour une décision engageante.

## Compléments V2 : affiliation, reprise et SEO

Pour l’affiliation et les modèles hybrides, appliquer [les modules de revenus](modeles-revenus.md).
En reprise, distinguer coûts irrécupérables, engagements restant à payer et nouvelles dépenses.
Les coûts SEO possèdent des IDs uniques partagés ; intégrer le scénario sans nouveaux clients
pendant le test. Ni modèles d’IA ni scores d’agents ne donnent des probabilités de rentabilité.
