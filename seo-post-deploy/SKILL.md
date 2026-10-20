---
name: seo-post-deploy
description: Prendre en charge après déploiement l'audit exhaustif des pages indexables avant toute démarche Google/Bing, la configuration autorisée de GA4, Search Console, Bing Webmaster Tools et Clarity, puis l'optimisation de visibilité fondée sur des données réelles. Conserver les preuves et reprendre les actions inachevées sans promettre de classement ni élargir les autorisations.
---

# Référencement après déploiement

<!-- GOOGLE_STARTER_GUIDE:BEGIN -->
## Socle Google Search Central

Lire et appliquer [les bonnes pratiques du guide SEO Google](../seo/references/google-starter-guide.md) avant les étapes concernées, dans un périmètre proportionné. Contrôler ce socle sur les pages prioritaires réellement publiées. Distinguer réception du sitemap, exploration, indexation et résultats ; adapter les délais de suivi sans multiplier les soumissions ni promettre un effet.

Source consultée le 8 octobre 2026. Le socle prime sur les recettes rigides contradictoires ; il nʼétend aucune autorisation.


Pour les controles specialises (rendu, sitemap, liens, medias, international, recherche generative et mesure), lire uniquement les sections pertinentes des [controles avances Google](../seo/references/google-advanced-practices.md). Verifier les sources actuelles avant application et distinguer exigences, recommandations et options.
<!-- GOOGLE_STARTER_GUIDE:END -->

Exécuter les démarches utiles pour le site de production courant, avec les accès disponibles et dans le périmètre demandé par l'utilisateur. Une demande opérationnelle peut autoriser les soumissions officielles gratuites et les configurations de propriété strictement nécessaires sur ce site ; le skill ne crée pas d'autorisation supplémentaire. Un audit ou une validation du skill reste en lecture seule sur les services externes. Ne pas promettre l'indexation, le classement ou une citation IA.

## Identifier le site et reprendre l'existant

Lire les instructions du projet, son domaine de production, ses décisions SEO et IA, les déploiements et le registre des démarches. Réutiliser les skills seo et ai-seo lorsqu'ils sont disponibles, sans déclencher une nouvelle stratégie complète. Ne jamais réutiliser implicitement le domaine, les comptes ou les résultats d'un autre site. Si plusieurs domaines restent plausibles, demander lequel traiter.

Identifier domaine canonique, langues, pays, pages prioritaires, CMS/hébergement, DNS, comptes Google Search Console et Bing Webmaster Tools, accès API et navigateur. Distinguer connecté, autorisé, vérifié et inaccessible. Ne pas demander des mots de passe ni inscrire de secrets dans les rapports. Un compte connecté ne prouve pas la propriété du domaine ciblé.

Lire [les opérateurs et sources](references/operators.md) pour sélectionner les démarches. Vérifier leurs procédures dans la documentation officielle actuelle avant de les appliquer. Couvrir les services pertinents pour le public et l'activité ; « tous les opérateurs » signifie inventorier les possibilités et justifier les exclusions, pas soumettre partout sans discernement.

## Vérifier la production avant soumission

Appliquer les [contrôles dépôt, publication et indexation](../seo/references/production-indexation.md) lorsqu'il existe une correction ou une republication : PR/branche principale/déploiement réel, pages publiques absentes du dépôt, origines canonical/og:url/JSON-LD/sitemap, exclusions noindex intentionnelles et recontrôle public. Comparer les dates du rapport global Search Console avec celles des inspections individuelles ; un test live valide prouve l'indexabilité actuelle, pas l'indexation. Préserver les validations déjà en cours.

### Point de contrôle obligatoire avant Google et Bing

Avant d'ouvrir une propriété ou d'agir dans Google Search Console ou Bing Webmaster Tools (inspection, soumission de sitemap, demande d'exploration/indexation ou IndexNow depuis leur interface), réaliser et présenter un contrôle de toutes les URLs de production destinées à l'indexation. Ne pas confondre ce contrôle avec la publication : il ne retarde ni n'annule un déploiement déjà autorisé. L'objectif est d'éviter d'envoyer aux moteurs un inventaire connu comme incomplet ou incorrect.

1. **Établir le périmètre exhaustif et sa preuve.** Recenser les URLs canoniques publiées depuis les sitemaps et index de sitemaps, le CMS/routes ou l'inventaire du dépôt, puis les comparer à un crawl interne du site. Dédupliquer, normaliser les redirections et réconcilier les écarts. Distinguer les pages qui doivent être indexables des pages volontairement exclues (privées, utilitaires, variantes techniques, `noindex` éditorial intentionnel, etc.). Indiquer le nombre d'URLs par source, les écarts, la date, les erreurs et les limites d'accès. « Toutes les pages » ne peut être déclaré vérifié que si le périmètre a été réconcilié et chaque URL destinée à l'indexation a été contrôlée ; sinon donner la couverture réelle et marquer le contrôle incomplet.
2. **Contrôler chaque page indexable sur la production.** Vérifier réponse HTTP finale (succès attendu), HTTPS/hôte/cible après redirections, accessibilité au crawl, absence de `noindex` non voulu dans `meta robots` ou `X-Robots-Tag`, canonical cohérente, absence de directives contradictoires, contenu utile accessible, présence et pertinence du H1, title et meta description uniques et alignés sur l'intention, et présence dans le sitemap seulement si la page est canonique, publique et indexable. Vérifier les autres balises qui influent sur le rendu ou l'indexabilité lorsque pertinentes (langue, pagination, données structurées), sans traiter Open Graph comme une balise de classement Google.
3. **Vérifier le maillage page par page.** Chaque page indexable doit être atteignable depuis au moins une autre page HTML indexable par un lien interne explorable, avec une ancre compréhensible et un parcours cohérent. Signaler les pages orphelines et les liens cassés/redirects. Une page absente du crawl n'est pas automatiquement orpheline si elle est inaccessible au crawl : la confronter à l'inventaire du CMS et des sitemaps. Ne pas inventer une obligation de nombre de liens.
4. **Vérifier l'intention et le fan-out.** Pour chaque page prioritaire et chaque gabarit éditorial, comparer H1/title/meta et contenu au sujet principal et à sa carte de fan-out (intentions et sous-questions utiles, affectation à la page ou à une page distincte). Repérer fan-out incomplet, questions non traitées, chevauchement/cannibalisation probable, ou sous-intentions qui méritent une autre URL. S'appuyer sur le brief et les résultats de recherche accessibles ; si aucune carte ou preuve n'existe, la construire prudemment ou marquer l'évaluation « hypothèse/non vérifiée ». N'imposer ni quota de mots ni couverture mécanique de variantes.
5. **Faire valider le rapport avant l'accès aux outils moteurs.** Fournir une liste des URLs contrôlées ou un artefact exploitable, la couverture, les défauts par page, les exclusions intentionnelles, les corrections proposées et le statut ; demander explicitement à l'utilisateur de vérifier ce bilan avant d'ouvrir GSC/Bing ou de lancer une soumission. Si l'inventaire n'est pas exhaustif, suspendre ces démarches et demander l'accès ou l'inventaire manquant. Si des défauts subsistent, demander s'ils doivent être corrigés avant soumission ou si l'utilisateur autorise une poursuite avec réserves documentées. Ne jamais soumettre de pages privées, hors domaine, volontairement exclues ou dont les directives d'indexation/canonicals sont erronées. Ce point de contrôle porte sur les démarches aux moteurs, pas sur la publication déjà autorisée.

Contrôler HTTPS, redirections et hôte final, réponses HTTP, robots.txt, meta robots et X-Robots-Tag, canonical, contenu HTML accessible, maillage et sitemaps. Examiner CDN/WAF et logs si disponibles. Une simulation d'user-agent ne prouve pas l'accès du robot réel.

Sitemaps : format valide, URLs absolues canoniques, indexables et publiques, index/enfants accessibles, dates lastmod exactes, limites officielles respectées. Exclure preview, administration, données privées, paramètres inutiles et pages non destinées à la recherche. Ne pas indexer une page volontairement privée ou noindex. Les notifications de suppression IndexNow suivent une voie distincte et peuvent concerner des URLs supprimées.

robots.txt gère le crawl et ne protège pas des données privées ; une URL bloquée peut encore apparaître dans Google. Un noindex doit être accessible au robot pour être lu. Ne pas ouvrir une page privée pour rendre son noindex lisible : conserver son contrôle d'accès. Valider le format existant du sitemap plutôt qu'imposer XML : Google accepte aussi les formats texte, RSS et Atom documentés.

Corriger les blocages démontrés dans le périmètre autorisé, avec la stack existante et un diff vérifiable. Ne pas refaire le design. Une correction locale n'est pas une correction en production : respecter les droits de déploiement et vérifier l'état public après publication. Si un blocage touche un sous-ensemble, poursuivre les démarches des pages éligibles et signaler les exclusions.

## Effectuer les démarches

1. **Google Search Console** : sélectionner une propriété couvrant l'URL exacte (propriété Domaine ou préfixe d'URL avec protocole, hôte et chemin appropriés) ; réutiliser une propriété existante. Ajouter/vérifier si nécessaire avec une méthode autorisée. Pour DNS, ajouter seulement l'enregistrement de validation requis et préserver tous les autres enregistrements. Vérifier le rôle requis pour chaque action : l'interface Sitemaps demande un propriétaire, la demande manuelle d'indexation un propriétaire ou utilisateur complet. Soumettre le sitemap par interface ou API officielle ; vérifier son statut et inspecter les pages prioritaires. La demande d'indexation manuelle, lorsqu'elle est disponible, est distincte de l'API d'inspection en lecture seule, dont les données ne constituent pas un test live. Ne pas utiliser l'Indexing API générale pour des articles ou fiches ordinaires.
2. **Bing Webmaster Tools** : réutiliser ou ajouter la propriété ; importer depuis Search Console seulement si pertinent et autorisé. Vérifier sitemap, couverture et URLs prioritaires. Employer IndexNow ou la soumission officielle disponible ; éviter les soumissions répétées sans changement.
3. **IndexNow** : rechercher l'intégration CMS/CDN existante avant d'en créer une seconde. Vérifier la clé et son fichier public sur l'hôte concerné ; respecter keyLocation, portée du chemin, formats, taille des lots et participants documentés. Séparer les hôtes en lots distincts. Soumettre les URLs créées, modifiées ou supprimées réellement concernées. Une notification à un participant peut être partagée entre participants : ne pas multiplier les envois par moteur. HTTP 200 signifie notification reçue, 202 validation de clé en attente ; aucun ne prouve l'indexation. Diagnostiquer 403 (clé), 422 (hôte/format) et 429 (limitation) avant reprise. Google n'est pas couvert implicitement.
4. **Autres moteurs** : sélectionner leurs outils officiels selon pays/langues et pertinence actuelle. Vérifier s'ils ont un index propre, utilisent un partenaire ou disposent d'une procédure documentée. Ne pas inventer de portail pour Yahoo, DuckDuckGo ou un moteur IA ; noter « pas de démarche directe documentée » si c'est le constat établi.
5. **Recherche IA** : vérifier les règles actuelles des robots de recherche des plateformes pertinentes et les décisions du projet. Distinguer recherche, entraînement et récupération à la demande. Préserver la politique d'entraînement ; ne pas ouvrir tous les bots par défaut. Ne pas présenter llms.txt, Bing ou IndexNow comme une soumission universelle à ChatGPT, Claude, Gemini ou Perplexity.
6. **Modules conditionnels** : activité locale réellement éligible, commerce, images, vidéos, actualités et annuaires professionnels pertinents. Vérifier éligibilité, identité et informations réelles avant toute fiche. Ne pas créer de compte, payer, accepter un contrat nouveau, publier une campagne, contacter des tiers ou diffuser des données personnelles sans autorisation adaptée. Préparer les dossiers et continuer les démarches indépendantes si une validation humaine manque.

Privilégier API/connecteurs officiels ; utiliser une session navigateur autorisée si nécessaire et disponible. En cas de connexion, MFA, CAPTCHA ou preuve de propriété manquante, demander uniquement l'intervention indispensable sans contourner le contrôle. Ne pas arrêter tout le workflow pour un seul opérateur inaccessible.

## Installer et raccorder Analytics, Search Console, Bing et Clarity

Pour le site courant, inventorier ce qui existe déjà avant de proposer une inscription : compte/propriété et flux web GA4, collecte effectivement observée, consentement, propriété Search Console vérifiée, site Bing Webmaster Tools, projet Clarity, tag/installation Clarity et intégrations existantes. Distinguer absent, installé, lié, vérifié, accessible et données reçues. Demander à l'utilisateur s'il souhaite créer les propriétés manquantes ou réutiliser les siennes ; demander l'accès ou l'intervention minimale. Ne jamais demander de mot de passe, créer un compte au nom de l'utilisateur, publier un tag/script, changer DNS ou modifier la plateforme de consentement sans autorisation explicite.

Suivre le graphe réel des intégrations, sans promettre de lien natif Analytics–Bing :

- **GA4 ↔ Search Console** : appliquer la [procédure GA4–Search Console](../analytics/references/search-console-link.md). Lire les associations avant création ; vérifier le couple propriété GSC/flux web GA4, leur portée et les rôles requis. Réutiliser l'association correcte ; ne jamais supprimer/recréer un lien occupé ou erroné sans mandat adapté.
- **GA4 ↔ Microsoft Clarity** : une fois GA4 et le projet Clarity configurés, proposer et réaliser, si autorisé et disponible, l'association dans Clarity. Vérifier la propriété/flux sélectionné et noter les limites de portée. L'association ne remplace pas l'installation de la collecte Clarity sur le site.
- **Bing Webmaster Tools ↔ Clarity** : utiliser l'intégration Clarity disponible dans Bing Webmaster Tools si le compte et la propriété le permettent ; confirmer le site exact et l'état affiché.
- **Search Console → Bing Webmaster Tools** : l'import officiel d'une propriété vérifiée GSC peut faciliter l'ajout/vérification dans Bing ; l'utiliser seulement avec le compte Google et les permissions nécessaires. Ce transfert n'est pas une intégration GA4–Bing.

Sources officielles à revalider au moment de la configuration : [lier GA4 à Clarity](https://learn.microsoft.com/en-us/clarity/ga-integration/ga-integration), [FAQ Microsoft Clarity](https://learn.microsoft.com/en-us/clarity/faq), [intégration Clarity de Bing Webmaster Tools](https://www.bing.com/webmasters/help/webmaster-support-24ab5ebf), [importer/vérifier un site depuis Search Console dans Bing](https://www2.bing.com/webmasters/help/add-and-verify-site-12184f8b). Ces intégrations et leurs conditions peuvent évoluer.

Séquence recommandée : terminer le contrôle page par page et obtenir la validation explicite du rapport avant toute action dans GSC/Bing. Si GA4 manque, demander à l'utilisateur de s'inscrire/créer son compte Analytics, sa propriété GA4 et son flux web, ou solliciter son accord pour le guider ; confirmer ensuite que la collecte fonctionne. Puis relier GA4 à GSC si pertinent, vérifier/importer le site dans Bing depuis GSC si autorisé, créer/configurer Clarity si l'utilisateur le demande et raccorder Clarity à GA4 et à Bing quand les intégrations sont disponibles. Poursuivre les tâches indépendantes sans inventer de lien ni de résultat.

Vérifier et consigner séparément propriété créée/vérifiée, tag installé, consentement préservé, association configurée, rapports accessibles et données disponibles ; observer une période éligible et tenir compte des délais documentés. Une liaison n'autorise pas à elle seule un nouveau tag ni une collecte sans consentement requis. Ne jamais assimiler clics GSC à sessions GA4, impressions Bing aux impressions Google, réception de sitemap à indexation, ni configuration réussie à collecte observée. En l'absence de lien Analytics–Bing natif, exploiter séparément leurs rapports et comparer des périodes/périmètres explicites. Après résultat d'écriture inconnu, rechercher l'association avant réessai.

## Optimiser la visibilité après déploiement

Appliquer [la boucle d’optimisation de recherche](references/search-optimization.md) sur les données réelles du site : indexabilité/exploration, requêtes/pages GSC et Bing accessibles, engagement/événements clés GA4 consent-aware, visibilité IA observée avec limites. Comparer périodes/filtres/volumes et saisonnalité ; prioriser intentions, catalogue, maillage, métadonnées et performance démontrés. Réutiliser SEO méthodologie, SEO contenu et IA sans récursion, production massive ni promesse de classement. Sans données : baseline et attente documentées. Séparer recommandations, corrections locales autorisées, publication et écritures de comptes ; consigner historique, preuves, hypothèses et réévaluation sans automation implicite.

## Tenir le registre et reprendre

Réutiliser le dossier SEO ; sinon créer SEO/POST_DEPLOY/. Conserver un registre lisible, éventuellement JSON, par domaine et opérateur : propriété, sitemap/URLs, action, date, preuve non sensible, statut, erreur, accès manquant et prochaine action. Statuts utiles : A_FAIRE, FAIT_VERIFIE, SOUMIS_EN_ATTENTE, BLOQUE_ACCES, BLOQUE_TECHNIQUE, NON_APPLICABLE, NON_VERIFIE. Séparer soumission acceptée, sitemap lu, URL indexée, impressions/clics et visibilité IA.

À chaque relance, lire le registre et l'état réel : ne pas recréer une propriété ni soumettre les mêmes URLs inchangées. Reprendre les opérations inachevées ou justifiées par les changements. Avant de réessayer une écriture dont le résultat est inconnu, vérifier si elle a abouti. Respecter quotas et Retry-After ; après deux échecs comparables sans nouveau diagnostic, consigner le blocage et poursuivre ailleurs. Ne pas lancer des scans coûteux ou répétés pour remplir un rapport.

Si une écriture expire sans réponse et qu'aucun statut fiable ne permet de conclure, conserver NON_VERIFIE avec action/lot/date et résultat inconnu ; suspendre sa répétition automatique. L'absence de preuve d'indexation ne prouve pas l'échec de la soumission. Une recherche site: est un indice de visibilité ponctuel, pas un inventaire exhaustif ni une preuve d'absence de l'index.

Proposer des contrôles à J+3, J+7 et J+30 adaptés au projet : lecture des sitemaps, couverture, erreurs, pages prioritaires et premières données de recherche. Une proposition n'est pas une automation créée. Programmer un suivi uniquement sur demande explicite, avec l'outil officiel et notification seulement en cas de changement utile ou intervention nécessaire.

Livrer un bilan concis : site exact, opérateurs couverts/exclus et raisons, démarches exécutées et preuves, corrections publiées ou locales, pages soumises/indexées observées, limites et interventions restantes. Ne déclarer complet que le périmètre effectivement exécuté ; une indexation future reste en attente.

## Scénarios de vérification du skill

Pour les fixtures et le déroulé manuel, lire [les scénarios](references/scenarios.md). Ils vérifient la cohérence des décisions ; ils ne prouvent ni l'exécution par un agent indépendant ni le fonctionnement d'une intégration réelle.

- Nouveau site sans comptes : audit public et préparation possibles ; soumissions authentifiées bloquées explicitement, aucune réussite inventée.
- Site déjà présent dans Google/Bing : réutiliser les propriétés et sitemaps ; traiter les nouveaux changements sans doublons.
- Blog ordinaire : sitemap/Search Console ; aucune utilisation abusive de Google Indexing API.
- Preview noindex et production publique : traiter seulement la production ; préserver la preview.
- Avant toute action GSC/Bing : réconcilier toutes les URLs attendues avec sitemaps/CMS/crawl, contrôler chaque URL indexable et rendre visible la couverture ; les pages noindex intentionnelles restent exclues.
- GA4, GSC, Bing et Clarity : décrire les liens qui existent réellement, demander les comptes/autorisations absents, ne pas inventer de lien natif GA4–Bing ni publier un tag sans accord.
- IndexNow accepte une notification mais aucune preuve d'indexation : statut de soumission uniquement.
- Site local non éligible ou marché hors cible : exclure les fiches/modules concernés avec raison.

