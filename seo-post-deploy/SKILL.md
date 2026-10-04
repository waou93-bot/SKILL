---
name: seo-post-deploy
description: Prendre en charge après déploiement les démarches de découverte et d'indexation du site courant auprès de Google, Bing, IndexNow et des services pertinents, vérifier les accès des moteurs IA, conserver les preuves et reprendre les actions inachevées. Utiliser pour référencer un site nouvellement publié ou relancer sa prise en charge après une mise à jour.
---

# Référencement après déploiement

Exécuter les démarches utiles pour le site de production courant, avec les accès disponibles et dans le périmètre demandé par l'utilisateur. Une demande opérationnelle peut autoriser les soumissions officielles gratuites et les configurations de propriété strictement nécessaires sur ce site ; le skill ne crée pas d'autorisation supplémentaire. Un audit ou une validation du skill reste en lecture seule sur les services externes. Ne pas promettre l'indexation, le classement ou une citation IA.

## Identifier le site et reprendre l'existant

Lire les instructions du projet, son domaine de production, ses décisions SEO et IA, les déploiements et le registre des démarches. Réutiliser les skills seo et ai-seo lorsqu'ils sont disponibles, sans déclencher une nouvelle stratégie complète. Ne jamais réutiliser implicitement le domaine, les comptes ou les résultats d'un autre site. Si plusieurs domaines restent plausibles, demander lequel traiter.

Identifier domaine canonique, langues, pays, pages prioritaires, CMS/hébergement, DNS, comptes Google Search Console et Bing Webmaster Tools, accès API et navigateur. Distinguer connecté, autorisé, vérifié et inaccessible. Ne pas demander des mots de passe ni inscrire de secrets dans les rapports. Un compte connecté ne prouve pas la propriété du domaine ciblé.

Lire [les opérateurs et sources](references/operators.md) pour sélectionner les démarches. Vérifier leurs procédures dans la documentation officielle actuelle avant de les appliquer. Couvrir les services pertinents pour le public et l'activité ; « tous les opérateurs » signifie inventorier les possibilités et justifier les exclusions, pas soumettre partout sans discernement.

## Vérifier la production avant soumission

Contrôler HTTPS, redirections et hôte final, réponses HTTP, robots.txt, meta robots et X-Robots-Tag, canonical, contenu HTML accessible, maillage et sitemaps. Tester accueil et pages prioritaires, puis un échantillon par gabarit/langue ; déclarer la couverture réelle. Examiner CDN/WAF et logs si disponibles. Une simulation d'user-agent ne prouve pas l'accès du robot réel.

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

## Preuves, reprise et suivi

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
- IndexNow accepte une notification mais aucune preuve d'indexation : statut de soumission uniquement.
- Site local non éligible ou marché hors cible : exclure les fiches/modules concernés avec raison.
