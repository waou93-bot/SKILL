# Contrat commun QA, sécurité et performance

## Un parcours et des responsabilités distinctes

Charger les quatre SKILL.md réels et leurs références pertinentes. Relever chemin,
version/hash, outils disponibles et mandat ; ne pas copier leurs consignes comme
preuve d'exécution. Organisation conserve le run et la propriété des fichiers.
La maintenance du package ne déclenche pas la formation des équipes d'un site.
Conserver le vrai personna sans modification ni substitution.

| Skill | G4/G5 : préparer et revoir | D1/D4 : réaliser et vérifier |
|---|---|---|
| webapp-testing | scénarios et critères des parcours | DOM rendu, interactions, console, réseau, captures et assertions |
| cross-platform-qa | routes/états, plateformes, méthode et couverture | comparaison et recette par environnement, navigateur et appareil |
| security-best-practices | stack, applicabilité, références frontend/backend et risques | code sécurisé par défaut ; revue demandée et revalidation des correctifs autorisés |
| web-perf | budgets, protocole et capacité de mesure | traces, réseau, ressources, mesures et recommandations argumentées |

Site-checklist conserve SC01–SC20/SF01–SF08 ; seo-audit conserve exploration,
indexation et contenu ; pSEO conserve données, familles et admissibilité ;
Design DNA/No Slop conservent identité et qualité ; Human Reading porte la lecture
des pixels lorsque nécessaire. Réutiliser les mêmes preuves valides et versionnées,
sans refaire quatre fois un test ni relancer les routeurs. Une capture ne prouve
pas une interaction, une assertion DOM ne prouve pas la qualité visuelle.

## Capacités et outils sans service payant requis

Préférer outils déjà accessibles, Playwright local, DevTools/Lighthouse gratuits,
inspection du code et appareils possédés. Python/JS et navigateurs nécessaires
doivent être réellement présents ; un skill ne les installe pas. Respecter les
interfaces autorisées par l'hôte : si l'automatisation doit passer par son navigateur,
adapter la procédure avec les capacités disponibles sans lancer un navigateur externe.
Pour with_server.py, commencer par --help ; arrêter les serveurs lancés pour le test
et fermer les navigateurs. L'installation d'outils respecte le mandat et les permissions.
Aucun BrowserStack, API SEO, scanner commercial ou traceur supplémentaire obligatoire.

Si un outil manque, poursuivre les analyses accessibles et nommer les contrôles
NON VÉRIFIÉS/BLOCKED, leur impact et une procédure locale/manuelle. Une plateforme
absente n'est jamais NON APPLICABLE par simple manque d'accès. Ne pas exiger un achat
pour lever un blocage. Le coût éventuel de l'hôte reste distinct de cette règle.

## Interactions et couverture

Déclarer routes, gabarits et états échantillonnés. Tester navigation/menu, liens/CTA,
recherche depuis article et hub, résultat hors première page, accents/casse, reset,
aucun résultat, clavier/focus, états vide/erreur et formulaires applicables.
Attendre un état observable pertinent avec délai borné : élément visible, données
chargées ou réponse attendue. Le networkidle proposé par webapp-testing est utilisable
si adapté ; polling, streaming et connexions persistantes ne doivent pas provoquer
une attente infinie. Ne pas masquer un échec avec un délai arbitraire.

La matrice conserve URL/commit/version servie, environnement, route/état, navigateur,
appareil/OS, viewport/orientation, méthode, date, critère, observation, résultat et
preuve. Séparer real_device, browser_emulation et viewport_resize. Chromium mobile
émulé ne valide pas Chrome Android réel ; WebKit desktop ne valide pas Safari iOS.
Fournir les étapes manuelles pour clavier mobile, safe areas et tactile indisponibles.
Garder PASS/FAIL/PARTIAL/BLOCKED/N/A de cross-platform-qa et les statuts SC/SF de
site-checklist dans leurs tableaux propres, avec correspondance expliquée dans le bilan.

## Sécurité adaptée à la stack et au mandat

L'intégration ne transforme pas un audit SEO isolé en audit sécurité exhaustif.
Pour une construction demandée, appliquer le code sécurisé par défaut ; pour une
revue sécurité explicitement demandée, charger toutes les références pertinentes
frontend/backend de security-best-practices. Python, JS/TS et Go sont son périmètre
documenté. Pour une stack non couverte, déclarer la limite et les vérifications
documentées réellement effectuées ; ne pas certifier une couverture inexistante.
Le chargement obligatoire du skill peut être LU avec décision d'application limitée.

Examiner selon les fonctions réelles : entrées et échappement, URLs, secrets,
authentification/autorisation côté serveur, données privées, sessions/CSRF, uploads,
dépendances et frontières de confiance. Ne pas imposer un backend à un site statique.
Un robots/noindex ne protège pas une donnée privée. Ne pas traiter HTTP localhost
comme défaut TLS de production ni imposer HSTS sans contexte. Les tests ne déclenchent
ni attaque active, achat, message réel, changement de droits ou collecte privée implicite.
Les corrections déjà autorisées sont réalisées et retestées sans redemander un accord ;
un audit seul conserve son mandat de lecture. Restituer constats numérotés, gravité,
fichier/ligne/version, impact, preuve et revalidation dans 11_QA.md ou un rapport lié.

## Performance : diagnostic puis correction autorisée

Le passage site-checklist/web-perf produit un audit et des recommandations.
Une demande explicite d'optimisation ou de correction incluant les constats autorise
leur mise en œuvre dans le périmètre demandé. Conserver l'autorisation déjà reçue,
sans exiger une confirmation rituelle. Les budgets prévus lors de la construction
guident le code initial ; ils ne constituent pas un résultat mesuré.
Consulter les sources primaires actuelles indiquées par web-perf avant de citer
seuils ou APIs. Les noms d'outils donnés comme exemples ne prouvent pas leur disponibilité.

Documenter protocole : version, route, machine/navigateur, réseau/CPU, cache froid/chaud,
interactions et nombre de runs ; conserver trace/log et dispersion si répétition.
Distinguer laboratoire, terrain CrUX/RUM, TBT et INP : aucun score Lighthouse ou
build ne prouve le 75e percentile terrain ni le classement SEO. Une donnée terrain
absente reste absente. Vérifier qu'une ressource est inutile avant suppression ;
séparer gain estimé et gain observé ; aucune économie inventée. Après correction,
rejouer le protocole comparable et les parcours concernés.

## Acceptation et reprise

G5 exige compétences lues, spécifications, applicabilité et tests prévus ; les tests
du site futur peuvent rester différés sans être annoncés réussis. D4 porte les
preuves du site local et ses limites. G6/release garde son sens de production
autorisée et réellement contrôlée ; la recette locale n'autorise pas la publication.
Les P0/P1 ouverts interdisent le transfert strict ; une limite de plateforme reste
explicite et ne devient pas PASS global. Après changement, invalider les preuves
affectées et rejouer les contrôles utiles. Deux passes de correction par gate QA
puis statut PARTIAL/BLOCKED si le défaut subsiste, sans empêcher les travaux indépendants.

Ajouter ces dépendances aux anciens state.json lors d'une reprise sans réinitialiser
le dossier. Conserver R01–R28, et couvrir R03/R20/R25/R26 dans les artefacts existants.
Le validateur vérifie présence et provenance de lecture, jamais l'authenticité des
tests ou la vérité d'une revue. Un seul 11_QA.md et backlog portent preuves et défauts.
