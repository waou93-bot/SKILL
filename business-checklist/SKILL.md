---
name: business-checklist
description: >-
  Benchmark web et Reddit, checklist de viabilité, tests de demande et business
  plan sourcé en dix parties. Utiliser pour un nouveau projet à monétiser, un
  audit économique d'un projet existant, un changement de cible/prix/modèle ou
  une décision de financement. Fonctionne seul ou avec Organisation ; échange
  avec SEO si pertinent. Ne pas déclencher pour un bug, une retouche ou un loisir
  non commercial sans décision économique.
---

# Business Checklist — Benchmark, preuves, viabilité et business plan

Version 2.0 · 16 septembre 2026 · Français par défaut.
Succède au package Business v1.0 ; nom technique canonique : `business-checklist`.

## Mission et limites

Déterminer le prochain engagement raisonnable : tester, ajuster, piloter, lancer
progressivement ou arrêter la version actuelle. Produire les preuves, la checklist
et le business plan, pas une justification automatique de l'idée.

Distinguer trois lectures : viabilité pour le porteur, finançabilité bancaire,
compatibilité avec un investisseur déterminé. Ne pas écarter une niche rentable
parce qu'elle n'est pas adaptée au capital-risque. Ne garantir ni succès ni financement.

Une étude documentaire n'est pas une validation commerciale. Un prototype peut
constituer une expérience : ne pas bloquer tout apprentissage en exigeant un
produit validé avant de pouvoir le tester. Un avis favorable n'autorise aucune dépense.

## Entrée, modes et capacités

Lire les instructions applicables, le MASTER, les décisions et les données autorisées
utiles. Ne pas charger tout le disque ni supposer qu'un autre PC est accessible.

Déterminer le mode :
- `NOUVEAU_PROJET` : hypothèses initiales, benchmark, tests et plan complet.
- `AUDIT_EXISTANT` : réalisé/prévu/mesuré, coûts futurs et décisions à réexaminer.
- `MISE_A_JOUR` : uniquement les hypothèses affectées, puis leurs conséquences.
- `FINANCEMENT` : dossier adapté au financeur, sans améliorer fictivement les preuves.
- `PRE_LANCEMENT` : revue des preuves et limites avant engagement commercial.

Une demande ciblée ne déclenche pas cinquante contrôles indépendants : appliquer
les contrôles pertinents et identifier le périmètre non réévalué. Un audit complet
ou un nouveau dossier conserve les dix rubriques, même si certaines restent inconnues.

Déclarer les accès réels : fichiers, web, Reddit, données clients/ventes, tableur,
skills et délégation. Utiliser les connecteurs disponibles pour les données concernées,
avec les autorisations appropriées. Sans accès, livrer la partie réalisable et
nommer les limites ; ne jamais inventer une recherche, une vente ou un entretien.

## Orchestration sans dépendance obligatoire

Organisation présent : respecter son routage et lui restituer la décision. S'il a
déjà appelé ce skill, ne pas le rappeler pour recommencer la même tâche.
Organisation absent : exécuter directement, sans demander son installation préalable.

Conserver `run_id`, `project_id`, `entrypoint` et le mode. Aucun sous-agent ni changement
de modèle n'est implicite. Luna/Terra/Sol/Astra restent les rôles définis par le vrai
routeur ; en mono-agent, parler de lectures successives, pas de revue indépendante.

SEO n'est ni obligatoire ni un deuxième routeur. Consulter sa sortie réelle si elle
existe ; sinon préparer une demande ciblée ou documenter l'hypothèse d'acquisition.
Ne jamais affirmer l'avoir exécuté s'il est absent. Voir les contrats
[d'Organisation et SEO](references/integrations.md).

## Lecture progressive

Charger selon le besoin :
- [Recherche web et Reddit](references/recherche-web-reddit.md).
- [Attentes des financeurs](references/criteres-financeurs.md).
- [Gates, tests et décisions](references/gates-validation.md).
- [Prévisionnel et contrôles](references/modele-financier.md).
- [Modèles de revenus](references/modeles-revenus.md).
- [Reprise et usage multi-PC](references/reprise-et-portabilite.md).
- [Bibliographie et statut de vérification](references/sources.md).

La checklist est définie dans [ce modèle](assets/08-checklist.json).
Elle couvre le dossier ; elle ne constitue ni un score de succès ni une obligation
de prouver commercialement toutes les hypothèses avant le premier test.

## 1 — Cadrer et reprendre l'existant

Compléter [le brief](assets/00-brief-projet.md). Réutiliser les réponses déjà connues.
Au premier passage, regrouper au maximum cinq questions réellement bloquantes ;
continuer les travaux indépendants lorsqu'une réponse manque.

Identifier : offre, utilisateur et payeur, bénéfice recherché, territoire, stade,
revenus envisagés, objectifs du porteur, temps disponible, perte acceptable et
preuves existantes. France/français est un contexte possible, pas une juridiction
à imposer si le projet vise ailleurs. Ne pas inventer de société, budget ou équipe.

Respecter les préférences validées pour ce projet. Ne pas imposer abonnement,
microtransactions, dette, salariés, logistique ou levée. Ne pas étendre une
préférence propre à un projet à tous les autres sans contexte.

En audit existant : remplir [l'état de reprise](assets/09-reprise.md), séparer
réalisé/prévu/observé. Préserver code, direction artistique, MASTER et décisions.
Les dépenses passées renseignent l'analyse ; elles ne suffisent pas à justifier
les dépenses futures. Ne pas recommencer le projet de zéro.

## 2 — Définir les hypothèses et rechercher les contre-preuves

Avant recherche, noter les conditions nécessaires, leurs contre-hypothèses et la
décision qu'une observation changerait. Prioriser l'incertitude qui menace le
prochain engagement, pas celle dont les données sont faciles à trouver.

Faire une recherche web datée et spécifique au projet. Lire les sources accessibles,
chercher des faits qui soutiennent ET contredisent la proposition. Distinguer dates
de publication, période des données et date de consultation. Revérifier les prix,
conditions, disponibilités, règles et hypothèses dynamiques qui changent la décision.

Viser 8–15 alternatives et 3–5 analyses approfondies si le marché le permet ;
réduire ou élargir avec justification. Inclure concurrents directs, indirects,
gratuits, manuels, prestataires et statu quo. Évaluer aussi pourquoi leurs clients
restent satisfaits. Ne pas assimiler absence de concurrent et opportunité prouvée.

Pour chaque alternative : segment/payeur, promesse, offre/prix/conditions datés,
canaux observables, points forts, limites documentées, coût de changement et
éléments inconnus. Trafic estimé, levée et prix affiché ne prouvent pas les ventes.
Utiliser [le benchmark](assets/01-benchmark.md).

Sur Reddit : chercher d'abord les communautés de la clientèle, puis les retours
méthodologiques d'entrepreneurs. Lire les désaccords, noter biais, promotion,
périmètre géographique et limites d'accès. Une plainte n'établit pas la demande
solvable ; des votes ne donnent pas une taille de marché. Ne pas contourner un
accès privé, contacter les auteurs ou collecter des données sensibles sans accord.

Arrêter la recherche documentaire lorsque les incertitudes décisives nécessitent
un test terrain plutôt que plus de pages. Consigner les questions non résolues.

## 3 — Tenir le registre de preuves et la checklist

Utiliser [le registre](assets/02-registre-preuves.md). Chaque affirmation déterminante
porte un ID et un type : `FAIT_SOURCE`, `OBSERVATION_TERRAIN`, `CALCUL`,
`HYPOTHESE`, `INCONNU`. Conserver provenance, période, population, vérification,
limites, contradictions et formule/entrées pour les calculs.

Une simulation IA de client ne constitue pas une observation terrain. Une donnée
manquante est `null` ou NON MESURÉ, jamais zéro par défaut. Des avis autodéclarés
restent tels, même lorsqu'ils sont publiés sur un domaine réputé.

Chaque contrôle de checklist contient : question, critère attendu, applicabilité,
statut, justification, preuves, incertitude, prochaine action, responsable et date.
Statuts : `A_EVALUER`, `ETAYE`, `A_TESTER`, `NON_CONFORME`, `BLOQUE`,
`NON_APPLICABLE`. `ETAYE` signifie suffisamment étayé pour le périmètre et le
prochain jalon, pas vérité définitive ni demande commercialement validée.

Une simple rubrique rédigée ne justifie pas ETAYE. NON_APPLICABLE demande une
raison. Les inconnues ne sont pas des échecs. Aucun pourcentage de cases cochées
ne permet d'effacer un blocage critique. La synthèse montre les contrôles qui
changent la décision, pas une note artificielle sur 100.

## 4 — Relier demande, valeur, distribution et modèle de revenus

Distinguer utilisateur, décideur, prescripteur, acheteur et payeur. Reconnaître les
valeurs de plaisir, émotion et créativité autant que les gains de productivité.

Construire TAM/SAM/SOM avec unités et hypothèses cohérentes. Le marché atteignable
part des clients accessibles, du canal, des conversions, du cycle et de la capacité ;
jamais « 1 % d'un marché mondial ». Ne pas confondre revenu du marchand et commission.

Comparer l'offre au coût du statu quo et au coût de changement. Expliquer le
mécanisme distinctif et ses preuves, pas seulement « plus simple » ou « avec IA ».

Prioriser un ou deux canaux réellement accessibles. Distinguer audience, prospect,
activation, achat, réachat et recommandation. Évaluer prix, coût d'acquisition,
délai, travail, support et concentration. Un SEO faible n'invalide pas le projet.
Transmettre les hypothèses SEO via [le brief d'échange](assets/10-seo-interface.md).
Aucune vente SEO prévue uniquement à partir d'un volume de mots-clés.

Appliquer le [module de revenus](references/modeles-revenus.md) pertinent : achat
unique, abonnement, affiliation, service, marketplace, commerce, contenu/jeu ou hybride.
Un hybride comporte des flux séparés et des coûts mutualisés comptés une seule fois.

## 5 — Concevoir le prochain test, pas une production illimitée

Pour les hypothèses critiques, utiliser [le plan de validation](assets/03-plan-validation.md).
Prédéfinir population, recrutement, intervention, métrique et dénominateur, biais,
coût/temps maximum, autorisation, seuils justifiés et interprétation d'un résultat
positif, négatif ou non concluant. Prévoir les raisons possibles d'échec et limiter
les itérations ; ne pas déplacer les seuils pour sauver l'idée.

Les entretiens explorent des comportements passés ; usage, pilote ou achat testent
d'autres hypothèses. Choisir une preuve adaptée au secteur et au stade. Préventes,
quota d'entretiens ou taux de conversion ne sont pas des normes universelles.
Les tests peuvent inclure un prototype technique limité ou une prestation manuelle
transparente ; ils ne justifient pas un produit complet hors périmètre.

Un test est préparé, autorisé, exécuté ou interprété : distinguer ces états.
Ne pas créer de formulaire trompeur, encaisser ou publier sans autorisation.

## 6 — Construire des finances explicables

Lire les [règles financières](references/modele-financier.md) et le
[dictionnaire d'hypothèses](assets/06-hypotheses.json). Relier chaque chiffre à son
statut, source, unité, période, scénario et test éventuel.

Produire un horizon de trois ans, avec années 4–5 si utiles. Mensualiser les 36 mois
lorsque les données permettent une granularité utile ; à défaut expliciter la
granularité et conserver au moins le calendrier de trésorerie du prochain engagement.
Ne pas fabriquer une précision mensuelle à partir d'une idée non mesurée.

Modéliser acquisition/ventes/capacité, compte de résultat, trésorerie, bilan,
investissements, charges fixes/variables/paliers, BFR, dette et financement.
Afficher seuil d'équilibre en CA et unités, point bas de trésorerie, capacité à
rémunérer le porteur, coûts futurs et coût d'opportunité sans double compte.

Trois scénarios : défavorable, central, favorable ; pas de probabilités inventées.
Inclure absence de financement non sécurisé, retard et acquisition décevante si
pertinents. Documenter les valeurs de bascule et les contrôles de cohérence.

Sans entrées suffisantes, produire le modèle paramétrique et les inconnues,
pas un bilan fictif. Si un tableur est livré, suivre les instructions de l'hôte,
recalculer et tester les formules. Un gabarit n'est pas un prévisionnel exécuté.
Vérifier les règles locales sur sources officielles ; faire revoir les engagements
comptables/juridiques déterminants par le professionnel compétent.

## 7 — Passer les six gates et la revue contradictoire

G1 problème/payeur ; G2 valeur/engagement ; G3 distribution ; G4 livraison/droits ;
G5 économie/trésorerie ; G6 adéquation porteur. Pour chacune : preuves, résultat,
incertitudes, criticité pour le prochain périmètre et action. Voir les
[gates](references/gates-validation.md).

Formuler la meilleure thèse favorable, les trois objections les plus fortes et
les observations qui feraient changer d'avis. Les agents ne votent pas la viabilité.
Distinguer obstacle établi, risque, information absente et protocole défaillant.

Décisions : `TESTER`, `PIVOTER`, `GO_PILOTE`, `LANCER_PROGRESSIVEMENT`,
`STOP_VERSION_ACTUELLE`, `BLOQUE_INFORMATION`.

Sans preuve terrain pertinente, ne recommander ni GO_PILOTE ni lancement. Un pilote
qui constitue justement le premier test est classé TESTER, sans empêcher sa préparation.
Un GO exige risques critiques traités pour ce périmètre, limites de cash et temps,
responsable et prochain contrôle. Un STOP vise une version et des contraintes,
jamais une impossibilité universelle. Le porteur conserve l'arbitrage final.

## 8 — Rédiger les dix rubriques obligatoires

Utiliser [le modèle complet](assets/04-business-plan.md), ordre final inchangé :
1. Résumé exécutif, rédigé en dernier, une à deux pages si pertinent.
2. Présentation de l'entreprise.
3. Analyse du marché.
4. Proposition de valeur.
5. Produits ou services.
6. Stratégie commerciale et marketing.
7. Organisation et ressources humaines.
8. Plan opérationnel.
9. Prévisions financières.
10. Besoin de financement.

Pas de quota 70 % chiffres / 30 % présentation. Exiger plutôt provenance des chiffres,
explication des hypothèses et honnêteté sur les preuves. Même en cas de STOP,
conserver les rubriques sous forme de cadrage sans fabriquer un dossier de vente.

## 9 — Livrer, contrôler, transmettre

Dans le MASTER existant, utiliser `BUSINESS/` ; sans accès, remettre les fichiers.
Préserver les chemins existants lorsqu'ils sont déjà référencés :
`00_DECISION.md`, `01_BRIEF.md`, `02_BENCHMARK.md`, `03_PREUVES.md`,
`04_VALIDATION.md`, `05_BUSINESS_PLAN.md`, `06_HYPOTHESES.json`, `07_FINANCES.*`,
`08_SOURCES.md`, `09_HANDOFF.json`, `10_CHECKLIST.json`, `10_CHECKLIST.md`,
`11_REPRISE.md` si existant, `12_ACQUISITION_SEO.md` si pertinent, `CHANGELOG.md`.
Ne pas créer des fichiers vides uniquement pour cocher une liste.

Utiliser [le contrat JSON](assets/05-decision-handoff.json), son
[guide de remplissage](references/handoff-schema.md), et l'auditer avec
`scripts/check_handoff.py`. Les contrôles automatiques vérifient la cohérence des
champs, pas la vérité des preuves, la conformité juridique ou la réussite future.

Restituer : décision et motifs, principale inconnue, état des contrôles critiques,
prochain engagement proposé, trois actions prioritaires et liens vers les livrables.
Séparer travail produit, tests exécutés, installation, intégration réelle et actions
autorisées. Aucun automatisme de publication, facturation, dépense ou synchronisation.

Réouvrir les volets concernés après changement matériel de cible, prix, coûts,
canal, règles, dépendances, financement, délai ou preuve. Une date de revue n'est
pas une tâche planifiée : ne pas annoncer un suivi automatique non configuré.
