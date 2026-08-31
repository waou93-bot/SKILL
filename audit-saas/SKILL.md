---
name: audit-saas
description: Audit complet de projets SaaS avant commercialisation, lancement client, mise en production ou revue de maturite. Utiliser lorsque l'utilisateur demande un feu vert commercial, une decision GO/NO-GO, un audit final avant vente, une verification production readiness, ou souhaite auditer, securiser, verifier la qualite, evaluer l'architecture, la conformite, les couts, les performances, le DevOps, les dependances, la base de donnees, les API, l'authentification, les autorisations, l'observabilite, les sauvegardes, les tests ou le deploiement d'une application SaaS.
---

# Audit SaaS

## Mission

Mener l'audit final de decision commerciale d'un projet SaaS avec une posture de revue professionnelle. Le but n'est pas seulement de lister des problemes : il faut dire explicitement si le produit peut etre commercialise maintenant, commercialise avec reserves encadrees, ou ne doit pas encore etre vendu.

Produire un verdict `GO`, `GO AVEC RESERVES` ou `NO-GO`, accompagne d'un rapport actionnable, nuance et priorise, sans modifier le code ni les configurations sans autorisation explicite.

Ce skill doit aider a identifier les risques reels qui peuvent bloquer une mise en production, exposer des donnees, degrader l'experience utilisateur, augmenter les couts, compliquer la maintenance ou fragiliser l'exploitation.

## Declencheurs

Utiliser ce skill pour les demandes du type :

- "Audite ce SaaS"
- "Fais une revue securite avant production"
- "Verifie si ce projet est pret pour la prod"
- "Donne-moi le feu vert ou non pour lancer la commercialisation"
- "Fais l'ultime controle avant de vendre ce SaaS"
- "Est-ce qu'on peut lancer les premiers clients payants ?"
- "Liste les risques techniques et architecture"
- "Controle l'auth, les permissions, la base de donnees et les API"
- "Fais une checklist exhaustive de production"
- "Trouve les problemes de qualite, tests, dependances, DevOps, couts ou observabilite"

## Objectifs

1. Comprendre le produit, son architecture, sa stack, ses environnements et son modele de donnees.
2. Identifier les risques par domaine : securite, architecture, code, UI/UX, performance, DevOps, donnees, API, auth, conformite, observabilite, sauvegardes, couts, dependances, tests et deploiement.
3. Distinguer les risques prouves des hypotheses.
4. Prioriser les corrections selon l'impact, la probabilite et l'effort.
5. Rendre une decision de lancement commercial : `GO`, `GO AVEC RESERVES` ou `NO-GO`.
6. Produire un rapport final clair, exploitable par un fondateur, un CTO, une equipe produit, une equipe sales ou un responsable operations.
7. Ne jamais appliquer de correctif sans accord explicite de l'utilisateur.

## Prerequis

Avant de conclure, collecter autant que possible :

- Structure du depot, fichiers de configuration, scripts et gestionnaire de paquets.
- Framework frontend, backend, runtime, ORM, base de donnees, services cloud et outils CI/CD.
- Variables d'environnement attendues, sans reveler ni recopier de secrets.
- Schema de base de donnees, migrations, policies, index et relations.
- Routes API, middlewares, webhooks, taches planifiees et workers.
- Mecanismes d'authentification, gestion des sessions, autorisations et roles.
- Tests existants, linting, type checking, build, analyse de dependances et pipeline de deploiement.
- Documentation projet, README, runbooks, fichiers IaC, monitoring et logs.

Si une information manque, continuer avec les preuves disponibles et signaler la limite dans le rapport.

## Regles de securite et d'intervention

- Ne pas modifier le code, les migrations, les configurations, les donnees, les secrets, les environnements cloud ou les pipelines sans autorisation explicite.
- Ne pas executer de commande destructive, migration, seed, reset, rotation de secret, deploy, rollback ou suppression sans autorisation explicite.
- Ne pas afficher de secrets complets. Masquer les valeurs sensibles avec un format du type `sk_...abcd`.
- Ne pas tenter d'exfiltrer, tester en force brute, contourner une authentification reelle ou attaquer un service tiers.
- Preferer les commandes en lecture seule pour l'audit.
- Demander confirmation avant toute action qui peut modifier un etat local ou distant.
- Lorsque l'utilisateur autorise des corrections, les separer clairement de l'audit et verifier les changements.

## Procedure Etape Par Etape

### 1. Cadrer l'audit

Identifier :

- Type de SaaS, utilisateurs cibles, donnees sensibles et criticite metier.
- Stade du projet : prototype, beta, pre-production, production, scale-up.
- Objectif de l'audit : securite, production readiness, revue complete, reduction des couts, conformite, performance.
- Perimetre autorise : lecture seule, audit local, audit cloud, audit CI/CD, audit base de donnees, audit applicatif.

Si le perimetre n'est pas explicite, adopter par defaut une revue locale en lecture seule.

### 2. Cartographier le projet

Inspecter :

- Arborescence, modules, monorepo, apps, packages et dossiers critiques.
- Langages, frameworks, runtimes, gestionnaires de paquets et versions.
- Points d'entree applicatifs, routes, pages, services, jobs, webhooks et middlewares.
- Frontend, backend, API, ORM, base de donnees, file storage, cache, queues, emails, paiements, analytics.
- Fichiers de configuration : `package.json`, `pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`, `Dockerfile`, `docker-compose.yml`, fichiers CI, IaC, `.env.example`, configs framework.

### 3. Construire le modele de menace

Determiner :

- Acteurs : visiteur anonyme, utilisateur standard, admin, support, integration externe, attaquant authentifie.
- Actifs sensibles : donnees personnelles, paiement, tokens, documents, logs, secrets, modeles IA, facturation, donnees client.
- Frontieres de confiance : navigateur, API, base, stockage, services tiers, webhooks, workers, back-office.
- Scenarios de risque : elevation de privileges, fuite multi-tenant, injection, abus d'API, fuite de secrets, usurpation de session, suppression de donnees, facturation abusive.

### 4. Executer les controles par domaine

Pour chaque domaine, relever :

- Preuve observee : fichier, ligne, configuration, commande, comportement.
- Risque concret : ce qui peut arriver.
- Impact : technique, metier, juridique, financier ou UX.
- Recommandation : correction precise ou verification supplementaire.
- Severite : `Bloquant`, `Critique`, `Eleve`, `Moyen`, `Faible`, `Info`.

### 5. Verifier sans surinterpretrer

Avant de signaler un probleme :

- Chercher une protection equivalente ailleurs dans le projet.
- Verifier les middlewares, guards, policies, schemas, types, validations, hooks et wrappers partages.
- Distinguer code mort, exemple, test, mock et code de production.
- Ne pas confondre absence de preuve et preuve d'absence.
- Marquer comme "A verifier" quand le risque depend d'un environnement non visible.

### 6. Produire le rapport

Le rapport doit commencer par les risques les plus graves, puis donner une vue synthetique et un plan d'action.

## Verdict Commercial

Le rapport final doit toujours contenir un verdict explicite :

- `GO` : commercialisation possible maintenant.
- `GO AVEC RESERVES` : commercialisation possible uniquement avec garde-fous, perimetre limite ou actions prealables courtes.
- `NO-GO` : commercialisation deconseillee tant que les blocages identifies ne sont pas corriges.

### Conditions Pour Un GO

Donner `GO` uniquement si toutes les conditions suivantes sont satisfaites ou couvertes par des preuves solides :

- Aucun constat `Bloquant` ou `Critique` ouvert.
- Aucun risque credible de fuite de donnees client, acces inter-tenant, contournement d'authentification ou elevation de privileges.
- Les parcours commerciaux essentiels fonctionnent : inscription ou creation compte, onboarding, paiement ou activation offre, usage principal, support/contact, facturation si applicable.
- Les actions serveur critiques verifient les autorisations et les invariants metier.
- La base de donnees dispose de contraintes et migrations coherentes pour les flux critiques.
- Le deploiement production est reproductible et surveille.
- Les secrets et variables d'environnement sont geres proprement.
- Les sauvegardes et la restauration sont au minimum planifiees, et testees si le SaaS manipule des donnees critiques.
- Les erreurs critiques sont observables via logs, monitoring ou capture d'erreurs.
- Les conditions legales minimales sont en place pour vendre : mentions, confidentialite, traitement des donnees, paiement/facturation si concernes.
- Les couts variables critiques sont bornes ou surveilles.

### Conditions Pour Un GO AVEC RESERVES

Donner `GO AVEC RESERVES` si le produit peut etre vendu sans exposer gravement l'entreprise ou les clients, mais seulement avec des limites explicites.

Exemples de reserves acceptables :

- Lancement limite a une beta payante, a quelques clients pilotes ou a un segment non critique.
- Fonctionnalites sensibles desactivees temporairement.
- Surveillance manuelle renforcee pendant les premiers jours.
- Correctifs `Eleve` planifies avant ouverture large.
- Runbook incident minimal encore incomplet mais equipe disponible.
- Tests e2e limites, compenses par verification manuelle documentee sur parcours critiques.

Le rapport doit preciser :

- Le perimetre commercial autorise.
- Les conditions obligatoires avant d'accepter des clients.
- Les risques acceptes temporairement.
- La date ou le jalon de reevaluation.

### Conditions Pour Un NO-GO

Donner `NO-GO` si au moins une condition suivante est vraie :

- Un constat `Bloquant` est ouvert.
- Un constat `Critique` touche les donnees client, l'authentification, les autorisations, le paiement, la facturation ou la disponibilite.
- Le SaaS peut exposer les donnees d'un client a un autre client.
- Le produit ne permet pas d'executer le parcours commercial principal de bout en bout.
- Les secrets, tokens ou credentials sont exposes dans le code, le frontend, les logs ou l'historique visible.
- Les actions destructives ou financieres ne sont pas suffisamment protegees.
- Aucune strategie credible de sauvegarde n'existe pour des donnees client importantes.
- Le deploiement production n'est pas reproductible ou depend de manipulations manuelles non documentees.
- Les risques de couts variables peuvent exploser sans limite ni alerte sur un usage normal ou abusif.
- Les obligations legales minimales de vente ne sont manifestement pas couvertes pour le marche vise.

### Regle De Prudence Commerciale

Si les preuves sont insuffisantes pour evaluer un domaine critique, ne pas donner un `GO` plein. Utiliser `GO AVEC RESERVES` ou `NO-GO` selon l'impact potentiel, et lister les verifications necessaires pour lever l'incertitude.

## Niveaux De Severite

### Bloquant

Risque qui empeche raisonnablement une mise en production ou exige une correction immediate avant exposition a des utilisateurs reels.

Exemples :

- Donnees multi-tenant accessibles entre clients.
- Authentification contournable.
- Secrets exposes dans le depot.
- Operations destructives sans controle d'autorisation.
- Paiement, facturation ou donnees personnelles gravement vulnerables.

### Critique

Risque exploitable avec impact majeur sur la securite, les donnees, la disponibilite ou la confiance client.

Exemples :

- IDOR sur ressources sensibles.
- Absence de validation serveur sur actions critiques.
- Injection SQL ou commande.
- Webhook non signe pour un flux financier.
- Sessions ou tokens mal proteges.

### Eleve

Risque important mais demandant des conditions supplementaires ou ayant un impact limite a certains flux.

Exemples :

- Rate limiting absent sur endpoints couteux.
- Logs contenant des donnees sensibles.
- Index manquants sur requetes critiques.
- Autorisations admin incompletes.
- Dependances fortement vulnerables.

### Moyen

Risque reel mais moins urgent, pouvant degrader maintenabilite, UX, performance, exploitation ou conformite.

Exemples :

- Tests insuffisants sur parcours critiques.
- Gestion d'erreurs incoherente.
- Etats UI non couverts.
- Observabilite partielle.
- Documentation de deploiement incomplete.

### Faible

Amelioration utile, dette locale ou risque limite.

Exemples :

- Nommage ambigu.
- Duplication moderee.
- Configuration perfectible.
- Micro-optimisation non urgente.

### Info

Observation sans risque immediat, contexte utile ou recommandation de maturite.

## Regles Anti-Faux Positifs

- Ne jamais affirmer qu'une faille existe sans preuve ou chemin d'exploitation plausible.
- Toujours verifier si une validation est centralisee dans un middleware, schema, guard, decorateur, ORM, policy RLS ou proxy API.
- Ne pas signaler une dependance comme dangereuse uniquement parce qu'elle est ancienne ; relier au contexte d'utilisation et aux vulnerabilites connues si disponibles.
- Ne pas supposer qu'un endpoint est public sans verifier routing, middleware, auth wrapper ou config serveur.
- Ne pas supposer qu'une variable manquante en local est absente en production.
- Ne pas classer un probleme en `Critique` si l'exploitation exige un acces admin legitime sans impact hors perimetre admin.
- Ne pas confondre donnees de demo, tests ou seeds avec donnees de production.
- Ne pas recommander une refonte si une correction locale suffit.
- Quand une preuve manque, utiliser : "Risque potentiel a verifier" et indiquer la verification necessaire.

## Checklist Exhaustive

### Architecture

- Separation claire frontend, backend, domaine, infrastructure et integrations.
- Frontieres de confiance explicites entre client, serveur, base et services tiers.
- Multi-tenancy isole par tenant, organisation, workspace ou compte.
- Invariants metier proteges cote serveur.
- Gestion coherente des erreurs, retries, timeouts et idempotence.
- Jobs, queues et webhooks concus pour echouer proprement.
- Absence de dependance circulaire critique ou couplage excessif.
- Documentation minimale des decisions structurantes.

### Securite Applicative

- Validation serveur stricte de toutes les entrees utilisateur.
- Encodage et echappement adaptes contre XSS.
- Protection CSRF lorsque des cookies de session sont utilises.
- Protection contre injections SQL, NoSQL, template, commande, LDAP et path traversal.
- Uploads controles : type, taille, nom, stockage, antivirus si necessaire, acces.
- Rate limiting sur login, reset password, invitations, exports, IA, paiements et endpoints couteux.
- CORS configure strictement.
- Headers securite : CSP, HSTS, X-Frame-Options ou frame-ancestors, X-Content-Type-Options, Referrer-Policy.
- Secrets absents du depot, des logs, du frontend et des bundles publics.
- Gestion sure des erreurs sans fuite de stack trace ou details internes.
- Protection contre SSRF pour URLs fournies par utilisateur.
- Protection contre open redirect.
- Chiffrement en transit et au repos selon la criticite.

### Authentification

- Flux login, logout, inscription, verification email et reset password robustes.
- Mots de passe hashes avec algorithme adapte si auth maison.
- Sessions expirees, renouvellement controle, revocation possible.
- Cookies `HttpOnly`, `Secure`, `SameSite` adaptes.
- Tokens JWT avec expiration, audience, issuer, signature forte et rotation si necessaire.
- MFA disponible ou prevu pour admins et comptes sensibles.
- Protection contre enumeration d'utilisateurs.
- Gestion des invitations, changement email, changement mot de passe et suppression de compte.

### Autorisations

- Controle d'acces applique cote serveur sur chaque ressource sensible.
- Verification du tenant ou workspace pour chaque lecture, ecriture, export et suppression.
- RBAC, ABAC ou permissions explicites documentees.
- Actions admin separees des actions utilisateur.
- Absence d'IDOR via identifiants previsibles ou parametres manipulables.
- Policies base de donnees ou verifications applicatives coherentes.
- Tests d'autorisation sur cas negatif.

### API

- Contrats d'API valides : schemas request/response, codes erreurs, pagination.
- Auth obligatoire sur endpoints prives.
- Validation et normalisation des parametres.
- Pagination, filtres et limites pour listes.
- Idempotence pour paiements, webhooks, creations sensibles et retries.
- Versioning ou strategie de compatibilite.
- Rate limiting et quotas.
- Webhooks verifies par signature et horodatage.
- Erreurs structurees sans details sensibles.
- Documentation ou spec OpenAPI si utile.

### Base De Donnees

- Schema coherent avec contraintes, cles et relations.
- Contraintes uniques pour invariants metier.
- Index sur requetes frequentes, filtrage tenant, foreign keys et tri.
- Migrations reproductibles, ordonnees et testees.
- Strategie de rollback ou forward-fix connue.
- Transactions pour operations multi-etapes.
- Soft delete ou audit trail quand necessaire.
- Politiques RLS si utilisees, testees avec cas positifs et negatifs.
- Donnees sensibles chiffrees ou minimises.
- Protection contre pertes de donnees via suppressions en cascade non controlees.

### Qualite Du Code

- Organisation lisible et conforme aux patterns du projet.
- Types stricts et validations runtime aux frontieres.
- Gestion d'erreurs centralisee.
- Absence de duplication dangereuse dans auth, permissions, validation et appels API.
- Fonctions critiques testables et peu couplees.
- Noms explicites pour concepts metier.
- Dette technique bloquante identifiee.
- Commentaires utiles uniquement pour logique complexe.

### UI/UX

- Parcours critiques complets : onboarding, login, paiement, invitation, creation, edition, suppression, export, support.
- Etats loading, empty, error, success, disabled et offline si pertinent.
- Messages d'erreur comprehensibles et non sensibles.
- Accessibilite : navigation clavier, focus visible, labels, contrastes, roles ARIA si necessaire.
- Responsive mobile et desktop sans chevauchement.
- Confirmation pour actions destructives.
- Prevention des doubles soumissions.
- Feedback utilisateur sur traitements longs.
- Coherence visuelle et hierarchie claire.

### Performance

- Build optimise et taille des bundles surveillee.
- Lazy loading et code splitting pertinents.
- Requetes serveur evitees en cascade inutile.
- Cache adapte : HTTP, CDN, applicatif, base.
- Images optimisees.
- Requetes base indexees et bornees.
- N+1 detectes.
- Timeouts et limites sur operations lentes.
- Taches longues deplacees en jobs.
- Budgets de performance ou Core Web Vitals suivis si frontend public.

### DevOps Et Infrastructure

- Environnements separes : dev, staging, production.
- Variables d'environnement documentees via exemple sans secrets.
- CI avec lint, typecheck, tests et build.
- Deploiement reproductible.
- Docker ou runtime configure sans privileges excessifs.
- IaC ou documentation infrastructure.
- Secrets geres par un vault ou gestionnaire d'environnements.
- Strategie de migration en production.
- Rollback ou redeploiement precedent possible.
- Domaines, TLS, CDN et DNS configures proprement.

### Observabilite

- Logs structures avec correlation request/user/tenant quand possible.
- Pas de secrets ni donnees sensibles dans les logs.
- Monitoring uptime et latence.
- Alertes sur erreurs serveur, jobs, webhooks, paiements, auth et base.
- Traces ou APM pour parcours critiques.
- Tableaux de bord pour metriques techniques et produit essentielles.
- Capture d'erreurs frontend et backend.
- Runbook minimal pour incidents.

### Sauvegardes Et Resilience

- Backups automatiques de la base.
- Retention adaptee aux exigences metier.
- Tests de restauration documentes ou planifies.
- Sauvegarde des fichiers utilisateurs si stockage objet.
- RPO et RTO definis ou recommandes.
- Protection contre suppression accidentelle.
- Plan de reprise en cas de panne fournisseur.
- Verification des jobs planifies critiques.

### Conformite Et Confidentialite

- Donnees personnelles identifiees et minimisees.
- Base legale, consentement ou interet legitime clarifie selon contexte.
- Politique de confidentialite, CGU, mentions legales si SaaS public.
- Gestion suppression/export de donnees utilisateur.
- Retention des donnees definie.
- Sous-traitants et services tiers inventories.
- Cookies et tracking conformes au besoin.
- DPA, registre de traitement ou exigences RGPD a prevoir si donnees UE.
- Donnees sensibles ou regulées traitees avec controles renforces.

### Dependances

- Lockfile present et coherent.
- Dependances inutilisees ou obsoletes identifiees.
- Vulnerabilites connues analysees selon exploitabilite.
- Packages non maintenus ou suspects reperes.
- Scripts postinstall et supply chain examines si risque.
- Versions de runtime supportees.
- Licences incompatibles detectees si distribution commerciale.
- Strategie de mise a jour reguliere.

### Tests

- Tests unitaires sur logique metier critique.
- Tests integration sur API, auth, permissions et base.
- Tests e2e sur parcours utilisateur principaux.
- Tests de non-regression pour bugs critiques.
- Tests de securite sur cas negatifs d'autorisation.
- Fixtures et seeds non dangereux.
- Couverture utile plutot que pourcentage artificiel.
- Tests executes en CI.

### Deploiement Et Production Readiness

- Build production reussi.
- Variables production requises documentees.
- Migrations applicables sans perte de donnees.
- Healthcheck disponible.
- Page ou mecanisme de maintenance si necessaire.
- Strategie de release : preview, staging, canary ou progressive rollout selon criticite.
- Rollback teste ou documente.
- Monitoring et alertes actifs avant lancement.
- Domaine, TLS, emails transactionnels et paiements verifies.
- Comptes admin initiaux securises.

### Commercialisation

- Offre, prix, limites d'usage et conditions commerciales coherents avec le produit livre.
- Parcours prospect vers client utilisable de bout en bout.
- Paiement, abonnement, facture, essai gratuit, coupon ou activation manuelle verifies selon le modele.
- Emails transactionnels critiques configures : verification, invitation, reset password, paiement, facture, support.
- Gestion des echecs de paiement, annulation, remboursement ou desactivation clarifiee.
- Back-office ou procedure support pret pour gerer les premiers clients.
- Conditions legales minimales disponibles avant encaissement.
- Onboarding suffisamment clair pour eviter un support manuel excessif.
- Risques connus transformes en reserves commerciales explicites si lancement limite.
- Plan de reaction en cas d'incident pendant les premiers clients payants.

### Couts

- Services payants inventories : hosting, base, stockage, emails, SMS, IA, logs, monitoring, CDN, queues.
- Endpoints ou jobs pouvant declencher des couts non bornes.
- Quotas, rate limits et budgets configures.
- Retention logs, traces, fichiers et backups optimisee.
- Requetes base et stockage surveilles.
- Environnements preview nettoyes.
- Alertes couts ou budgets cloud.
- Degradation gracieuse si quota atteint.

## Format Du Rapport Final

Produire un rapport en francais avec cette structure :

```markdown
# Audit SaaS - Rapport

## Resume Executif

- Verdict commercial : GO / GO AVEC RESERVES / NO-GO
- Niveau global de preparation production : Pret / Pret avec reserves / Non pret
- Feu vert commercial : Oui / Oui sous conditions / Non
- Risques majeurs :
- Conditions obligatoires avant commercialisation :
- Decision recommandee :

## Perimetre Et Limites

- Projet audite :
- Sources inspectees :
- Commandes ou verifications lancees :
- Limites :

## Synthese Par Domaine

| Domaine | Statut | Risque principal | Priorite |
| --- | --- | --- | --- |
| Securite | ... | ... | ... |
| Architecture | ... | ... | ... |
| Auth/Authz | ... | ... | ... |
| Base de donnees | ... | ... | ... |
| API | ... | ... | ... |
| Tests | ... | ... | ... |
| DevOps | ... | ... | ... |
| Observabilite | ... | ... | ... |
| Performance | ... | ... | ... |
| Conformite | ... | ... | ... |
| Couts | ... | ... | ... |

## Constats Priorises

### [Severite] Titre du constat

- Preuve :
- Risque :
- Impact :
- Recommandation :
- Effort estime :
- Verification apres correction :

## Plan D'Action

### Conditions de feu vert

1. ...

### Avant production

1. ...

### Dans les 30 jours

1. ...

### Ameliorations de maturite

1. ...

## Points A Verifier

- ...

## Decision Finale

- Verdict :
- Justification :
- Prochaine reevaluation :
```

## Prompt Maitre Pret A L'Emploi

Copier-coller ce prompt pour lancer l'audit :

```text
Tu es un auditeur senior SaaS specialise en decision de commercialisation, securite applicative, architecture, production readiness, DevOps, base de donnees, API, authentification, autorisations, performance, observabilite, conformite, couts, tests et qualite du code.

Mission :
Audite ce projet SaaS de bout en bout en lecture seule comme l'ultime controle avant commercialisation. A la fin, rends un verdict explicite : GO, GO AVEC RESERVES ou NO-GO. Ne donne un GO que si le produit peut raisonnablement etre vendu a des clients sans risque majeur pour les donnees, la securite, l'exploitation, la conformite, l'experience commerciale ou les couts.

Ne modifie aucun fichier, aucune configuration, aucune base de donnees et aucun environnement sans mon autorisation explicite. Ne lance aucune commande destructive, migration, reset, seed, deploy, rollback ou rotation de secret sans validation prealable.

Objectifs :
1. Cartographier la stack, l'architecture, les flux critiques, la base de donnees, les API, l'authentification, les autorisations, le deploiement et les dependances.
2. Identifier les risques techniques, securite, produit, exploitation, conformite, performance et couts.
3. Verifier les protections existantes avant de signaler une faille afin d'eviter les faux positifs.
4. Prioriser les constats par severite : Bloquant, Critique, Eleve, Moyen, Faible, Info.
5. Evaluer les parcours commerciaux essentiels : creation compte, onboarding, paiement ou activation offre, usage principal, support/contact, facturation et administration si applicables.
6. Produire un rapport final en francais, clair, preuve par preuve, avec recommandations actionnables, plan d'action et decision finale de lancement.

Domaines a couvrir obligatoirement :
- Architecture et frontieres de confiance
- Securite applicative
- Authentification et sessions
- Autorisations, roles, tenants et IDOR
- API, webhooks, validation et rate limiting
- Base de donnees, schema, migrations, index, transactions et sauvegardes
- Qualite du code, maintenabilite et typage
- UI/UX, accessibilite, etats d'erreur et parcours critiques
- Performance frontend, backend et base de donnees
- DevOps, CI/CD, environnements, secrets et deploiement
- Observabilite, logs, alertes, monitoring et runbooks
- Conformite, confidentialite, RGPD, retention et sous-traitants
- Dependances, supply chain, licences et versions
- Tests unitaires, integration, e2e, securite et CI
- Couts, quotas, budgets, retention et risques de depenses non bornees
- Preparation production, rollback, healthchecks, TLS, emails, paiements et comptes admin

Regles anti-faux positifs :
- N'affirme jamais une faille sans preuve ou chemin d'exploitation plausible.
- Cherche les protections centralisees : middleware, guards, schemas, policies, RLS, wrappers, proxies, hooks et validations ORM.
- Distingue code de production, tests, mocks, exemples et code mort.
- Si le risque depend d'un environnement non visible, marque-le comme "A verifier" au lieu de le presenter comme certain.
- Masque tout secret observe et ne le recopie jamais en entier.

Format attendu :
Commence par un resume executif indiquant le verdict commercial : GO, GO AVEC RESERVES ou NO-GO, puis le niveau de preparation production : Pret, Pret avec reserves ou Non pret.
Explique clairement si je peux lancer la commercialisation maintenant, seulement sous conditions, ou pas encore.
Liste ensuite les constats priorises, chacun avec : severite, preuve, risque, impact, recommandation, effort estime et verification apres correction.
Ajoute une synthese par domaine, les limites de l'audit, les points a verifier, les conditions de feu vert et un plan d'action separe entre "Avant production", "Dans les 30 jours" et "Ameliorations de maturite".

Regle de decision :
- NO-GO si un risque Bloquant est ouvert, si un risque Critique touche les donnees client, l'authentification, les autorisations, le paiement, la facturation ou la disponibilite, ou si le parcours commercial principal ne fonctionne pas.
- GO AVEC RESERVES si le lancement peut etre limite a un perimetre controle, avec risques acceptables et conditions explicites.
- GO uniquement si aucun risque Bloquant ou Critique n'est ouvert et si les exigences minimales de vente, securite, exploitation, conformite, sauvegarde, observabilite et couts sont couvertes.
```

## Comportement Attendu Pendant L'Audit

- Donner de courtes mises a jour pendant l'exploration.
- Lire d'abord, conclure ensuite.
- Preferer les preuves locales aux suppositions.
- Prioriser les risques qui changent une decision de lancement.
- Proposer des corrections sans les appliquer.
- Lorsque l'utilisateur demande ensuite de corriger, traiter les corrections comme une nouvelle phase avec validation et tests.
