---
name: seo-opportunity-loop
description: "Transformer les données Search Console en améliorations SEO priorisées, préparer les changements de pages ou outils et mesurer leurs effets. Utiliser pour exploiter les requêtes existantes, améliorer le CTR ou choisir quoi enrichir ; ne remplace pas un audit technique complet ni la production en masse."
---

# SEO Opportunity Loop

Exécuter à la demande la boucle observer → choisir → modifier → mesurer. Livrer des actions fondées sur les données et des changements concrets dans le périmètre autorisé. Aucun classement ou gain garanti.

## Observer

Lire le contexte SEO existant, les objectifs commerciaux et les pages concernées. Utiliser un connecteur GSC réellement disponible ou un export fourni ; vérifier propriété, accès, dates, filtres et fraîcheur. Sans données, préparer les hypothèses sans inventer métriques, volumes ou conversions. Une valeur indisponible est inconnue, pas zéro.

Analyser les couples page–requête et segmenter par pays, appareil et type de recherche quand possible. Conserver provenance et filtres. Les requêtes anonymisées et limites d'export empêchent de considérer leur somme comme le total de la propriété. Ne pas additionner des exports qui se chevauchent ni mélanger des agrégations différentes.

Calculer CTR = somme des clics / somme des impressions, jamais moyenne des CTR. Une position moyenne masque des variations et n'est pas un rang permanent.

## Diagnostiquer et choisir

Chercher demande observée, positions proches du haut des résultats, pertes persistantes et décalages d'intention. Les positions 5–20 sont un filtre exploratoire, pas une règle de priorité. Aucun seuil universel de CTR : comparer des segments comparables avec un volume suffisant.

Examiner les principales requêtes et les résultats dans le contexte pertinent : intention, titre réellement affiché, concurrents et réponses déjà présentes. Si cette observation est impossible, marquer l'explication comme hypothèse. Un faible CTR ne démontre pas un mauvais titre.

Vérifier les pages existantes avant création. Plusieurs URL sur une requête ne prouvent pas une cannibalisation : rechercher une concurrence d'intention et une instabilité observées.

Choisir l'action adaptée :
- Titre ou extrait : corriger une promesse inadaptée à la réponse attendue ; préserver la véracité, sans sensationnalisme ni longueur présentée comme exigence Google.
- Enrichissement : compléter la page qui couvre déjà l'intention avec réponses, exemples ou preuves.
- Nouvelle page : justifier un besoin distinct absent de l'existant ; regrouper les variantes d'une même intention.
- Calculateur : proposer un outil lorsque des entrées individuelles produisent un résultat utile que le texte seul fournit mal ; estimer maintenance et intérêt commercial.
- Fusion : justifier le diagnostic et identifier URL conservée, liens et redirections. Une baisse de trafic seule ne justifie pas une suppression.
- Traduction : sélectionner pages et langues selon demande et capacité de validation ; vérifier langue, unités, contexte local, URL et hreflang. Pas de traduction systématique.
- Observation : maintenir si les preuves ne justifient pas de changement.

## Prioriser et réaliser

Classer selon demande observée, intérêt commercial, potentiel plausible, effort, risques et confiance. Expliquer les arbitrages sans scores pseudo-précis. Séparer visibilité, clics, usage du service et conversions ; GSC seul ne mesure pas les conversions.

Pour chaque action, consigner URL et segment, preuve datée, problème observé, hypothèse, modification, effort, dépendances et critère de succès. Préparer puis réaliser les modifications locales autorisées et contrôles pertinents. Préserver URL et conventions sauf besoin démontré et autorisé. Une proposition ne vaut pas autorisation de publication ou de migration ; respecter les autorisations déjà données.

Pour un calculateur, documenter sources, formule, hypothèses, unités et arrondis. Tester références numériques, entrées invalides et cas limites. Distinguer calcul de stock ou date et recommandation thérapeutique. Pour tout résultat susceptible d'influencer une décision médicale, demander une revue qualifiée avant publication : citer NHS/CDC/FDA ne prouve pas la validation clinique.

## Mesurer

Consigner avant/après, déploiement, segment, métriques de référence et autres changements connus dans le journal existant. Vérifier si possible la prise en compte par Google et le titre affiché ; cela peut prendre plusieurs jours à plusieurs semaines. Ne pas retoucher continuellement la même page avant observation.

Choisir des périodes complètes et comparables selon volume, saisonnalité et exploration ; 28 jours est un point de départ possible, pas une obligation. Comparer clics, CTR, impressions en tenant compte des positions et du mix de requêtes. Ajouter usage et conversions si une source adaptée existe. Une comparaison avant/après ne démontre pas seule la causalité ; expliciter les facteurs concurrents.

Décider conserver, ajuster, revenir à la version précédente ou observer davantage selon les preuves. Si le volume est insuffisant, conclure indéterminé. Définir le prochain contrôle sans prétendre l'avoir exécuté. Une récurrence nécessite une demande utilisateur et un ordonnanceur réellement disponible ; le skill ne crée pas de service permanent.

## Livrables et intégrations

Réutiliser les documents SEO existants ; sinon fournir une liste courte d'opportunités et un journal proportionné. Inclure changements prêts à relire, contrôles effectués, données manquantes et suivi. Aucun dossier complexe obligatoire.

Pour un audit complet, utiliser seo ou seo-audit si disponibles ; pour lots ou portefeuille, seo-content-engine. Lire le skill concerné avant application sans relancer une orchestration active. Ce skill fonctionne seul avec des exports.

Actualiser les règles externes pertinentes avant application. Sources officielles :
- [Performance GSC](https://support.google.com/webmasters/answer/7576553)
- [Titres Google](https://developers.google.com/search/docs/appearance/title-link)
- [Contenu utile et fiable](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Multilingue](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)

## Contrat opérationnel et décisions reproductibles

Pour une analyse, restituer une fiche par action : id, URL propriétaire, requête ou groupe, pays/appareil/type de recherche, périodes et filtres, source, clics/impressions/CTR/position, limites, intention et observation SERP, hypothèse, changement avant/après, indicateur principal, critère de succès défini avant modification, responsable, effort, statut, version déployée, date de prise en compte connue ou inconnue, prochaine revue et décision. Utiliser les champs existants du projet plutôt que créer un schéma concurrent. Séparer PROPOSE, PREPARE, DEPLOYE, EN_OBSERVATION et CONCLU ; un titre préparé n'est pas un titre publié.

Traiter d'abord les défauts démontrés qui rendent une page inaccessible ou une réponse erronée, puis les opportunités avec demande observée et lien explicite à l'objectif. À potentiel comparable, préférer l'action réversible de moindre effort. Si l'intérêt commercial est inconnu, conserver une priorité exploratoire plutôt qu'un gain de revenu supposé. Le CTR seul ne départage pas les actions.

Pour isoler une hypothèse, limiter les changements simultanés sur le même segment lorsque possible ; sinon consigner les co-interventions. Fixer avant changement les conditions de maintien, correction ou retour arrière. Une erreur fonctionnelle justifie une correction immédiate, sans attendre une fenêtre SEO. Éviter toute conclusion statistique sans méthode adaptée et données suffisantes.

Avec zéro impression, le CTR est indéfini, pas 0 %. Vérifier clics <= impressions, valeurs non négatives, unités et périodes complètes. Identifier séparément la provenance et l'attribution des conversions : aucun export GSC ne fournit à lui seul cette métrique. Ne pas joindre des groupes incompatibles pour fabriquer une conversion par requête.

Dans SEO STUDIO 2, conserver run_id, registres et orchestration. Le contrôleur feedback.py traite des agrégats par page et produit des signaux ; il ne remplace pas l'analyse page–requête segmentée ni l'observation SERP. Stocker ces preuves détaillées séparément du format monitoring existant, sans modifier son contrat ni inventer leur présence. Avant lancement, préparer seulement les accès, événements et critères ; sans données, marquer la boucle PREPARE_PHASE_ULTERIEURE.
