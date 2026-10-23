# Mesure et expérimentation

## Chaîne de visibilité

Mesurer séparément : `ACCESS` (fetch), `INDEX` (éligibilité/indexation),
`RETRIEVAL` (sélection pour une requête ou sous-requête), `CITATION` (source affichée),
`ABSORPTION` (information effectivement utilisée), `FIDELITY` (usage fidèle),
`VISIT` (arrivée attribuable) et `OUTCOME` (action qualifiée). Ne jamais présenter
une étape comme preuve automatique de la suivante.

## Trois tableaux séparés

1. Éligibilité technique : contrôles URL/HTTP/robots/rendu et accès réels démontrés.
2. Visibilité observée : mentions, citations et recommandations d'un panel reproductible.
3. Acquisition : visites dont la provenance est observable, actions et conversions réellement disponibles.

Ne pas multiplier les trois pour produire une prévision de revenus sans données. Un bot n'est
pas un prospect ; une citation sans clic n'apparaît pas dans un rapport de sessions.

## Protocole du panel

Conserver un panel versionné de questions, avec intention, cible et URL pertinente. Séparer marque
et sans marque ; ne pas forcer une citation ou donner son domaine dans les questions d'acquisition.
Fixer plateforme ET surface (application web/mobile/API, Google AI Mode vs autre), langue, pays,
recherche activée, modèle affiché s'il existe et état de personnalisation. Utiliser un contexte
neutre lorsque possible ; documenter toute impossibilité.

Répéter chaque condition exploratoire au moins trois fois, sur plusieurs dates si possible,
puis augmenter l'effectif lorsque le désaccord entre runs reste matériel. Les répétitions ne sont
pas des utilisateurs indépendants. Pour une requête locale ou commerciale, contrôler séparément
la localisation déclarée par l'application, le pays/région réseau, la localisation nommée dans la
requête et la langue. Une sortie API ne remplace pas une observation du produit public. Ne pas
contourner CAPTCHA, conditions d'utilisation ou quotas ; commencer manuellement si nécessaire.

Pour chaque observation : `run_id`, `query_id`, `platform`, `surface`, `branded`, `language`,
`country`, `search_enabled`, `context_control`, `synthetic`, `observed_at` avec fuseau,
`status` (`ok`, `error`, `not_tested`), preuve, puis `mentioned`, `cited`, `recommended`.
Les trois booléens exigent une annotation de la réponse, pas une simple recherche de sous-chaîne.
Conserver aussi texte du prompt, réponse, URLs réelles, annotation et modèle dans les preuves,
en minimisant les données personnelles. Ne pas pousser des conversations privées dans GitHub.

Taux de citation = réponses valides citant le périmètre défini / réponses valides du même segment.
Idem pour mention et recommandation. Toujours afficher effectif, questions uniques, erreurs et
non-testés. Aucun ratio si dénominateur nul. `measure_panel.py` sépare plusieurs dimensions mais
ne sépare pas automatiquement les versions de modèle ou périodes : préparer des lots comparables.
Sa référence de preuve est une chaîne non vide, pas une vérification que la preuve existe.

## Attribution conservatrice

Parser le hostname, pas chercher « chatgpt.com » dans toute l'URL. Conserver UTM, referrer et
signal bot comme informations distinctes ; signaler les conflits au lieu de réécrire silencieusement
une campagne. Les UTM peuvent être ajoutés par n'importe qui ; un referrer peut manquer. Le trafic
sans provenance reste inconnu, pas « probablement IA ». Le classifieur ne prouve ni humain,
organique, recommandation, session ni conversion.

Les domaines du script sont une liste de départ à actualiser. Les nouveaux domaines ou relais
inconnus ne doivent pas être classés par intuition. Ne pas détecter AI Overviews/AI Mode à partir
d'un simple referrer google.com. Les visites de tests et les agents sont isolés de la production.

Événements possibles : usage d'un configurateur, guide consulté, clic affilié, contact envoyé,
essai activé, achat confirmé. Définir les identifiants nécessaires et la déduplication sans
collecte superflue. Un clic Amazon ne prouve pas une commande ; ne pas déduire du revenu d'une
commission théorique. Suivre coûts et gains réellement mesurables et les limites d'attribution.
Respecter la politique de consentement et de rétention du projet ; consulter la réglementation
et les spécialistes nécessaires avant une décision juridique. Les scripts n'ajoutent pas de tracker.

## Google : information actualisée

Au 4 octobre 2026, le guide officiel et l'aide Search Console décrivent un rapport de performances
génératives pour Search. L'aide annonce un déploiement mondial au 31 août 2026, tout en conservant
une section d'indisponibilité liée à la propriété ou aux impressions. Vérifier donc la propriété
réelle. Le rapport documente des impressions pour AI Overviews et AI Mode et leurs dimensions ;
ne pas lui attribuer un détail de clics, de requêtes ou de conversions qu'il ne fournit pas.

L'ancienne page `appearance/ai-features` expose encore une mesure globale : noter le conflit et
utiliser la documentation dédiée récente plutôt que répéter « aucun rapport IA n'existe ».
Sources : [sources.md](sources.md), entrées Google guide et rapport génératif.

Reconsultation du 13 octobre 2026 : le guide actuel et le rapport dédié restent
accessibles. Le rapport décrit les impressions, des dimensions page/pays/date/appareil
et des types texte/multimodal ; ne pas en déduire un tableau de sous-requêtes fan-out.
Ses données sont comprises dans le rapport Web : ne pas additionner les totaux.
L'absence de rapport peut tenir au faible nombre d'impressions ou à une exclusion.
Vérifier le paramètre d'inclusion en lecture seule ; son changement n'est pas autorisé
par un simple audit. Dater la fenêtre effective, distinguer données préliminaires et
agrégation propriété/page, et noter le fuseau du rapport lors des comparaisons.

Pour un traitement fan-out, relier question/branche, URL/section, réponse/preuve et
observation de citation selon [le contrat](query-fanout.md). Conserver séparément
progrès éditorial, indexation, visibilité, visite et conversion. Un taux de couverture
ne mesure ni part de marché ni citations gagnées. Un bilan de 28 jours dont les données
s'arrêtent à la date du traitement ne permet pas d'en mesurer l'effet.

## Expériences

Formuler hypothèse, traitement, pages/panel témoins si possibles, métrique primaire, garde-fous,
coût maximal autorisé, fenêtre et règle d'arrêt avant changement. Journaliser SEO, prix, campagnes,
modèles et saisonnalité. Éviter de conclure à une causalité depuis une poignée de réponses favorables.
Un intervalle d'incertitude doit respecter le plan d'échantillonnage ; pas de faux intervalle issu
d'observations dépendantes. Privilégier descriptions et effectifs quand le panel est petit.

Une revue périodique est une recommandation tant qu'aucune tâche planifiée n'a été créée avec
l'autorisation de l'utilisateur. Ne pas annoncer une surveillance permanente inexistante.

## Cartographie des sources récurrentes

Compléter les observations avec URL exacte, domaine, type de source et affirmation soutenue selon [le protocole de cartographie](citation-map-pilot.md). Séparer citations du site et sources tierces. Pour chaque domaine, compter au plus une occurrence par réponse et afficher réponses valides et questions uniques concernées.

## État de preuve GEO — octobre 2026

Une étude du 10 octobre 2026 sur 158 099 réponses et 468 037 citations associe, au sein
d'un même site, la proximité sémantique entre questions, titres et paragraphes aux citations.
Elle ne montre pas le même signal interne pour FAQ, structured data, encadrés ou vitesse ; ces
facteurs observés entre sites restent confondus. La récupération expliquait davantage de variation
que les propriétés de page dans ce protocole. Traiter ces résultats comme hypothèses à répliquer,
pas comme facteurs universels : https://arxiv.org/abs/2610.15033

Une étude contrôlée du 16 octobre 2026 (31 200 réponses) observe des canaux de localisation
différents selon ChatGPT et Gemini. Toute mesure locale doit donc enregistrer et varier localisation
déclarée et réseau indépendamment : https://arxiv.org/abs/2610.24081
