# Mesure et expérimentation

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

Répéter un sous-ensemble sur plusieurs dates pour estimer la variabilité. Les répétitions ne sont
pas des utilisateurs indépendants. Une sortie API ne remplace pas une observation du produit public.
Ne pas contourner CAPTCHA, conditions d'utilisation ou quotas ; commencer manuellement si nécessaire.

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

## Expériences

Formuler hypothèse, traitement, pages/panel témoins si possibles, métrique primaire, garde-fous,
coût maximal autorisé, fenêtre et règle d'arrêt avant changement. Journaliser SEO, prix, campagnes,
modèles et saisonnalité. Éviter de conclure à une causalité depuis une poignée de réponses favorables.
Un intervalle d'incertitude doit respecter le plan d'échantillonnage ; pas de faux intervalle issu
d'observations dépendantes. Privilégier descriptions et effectifs quand le panel est petit.

Une revue périodique est une recommandation tant qu'aucune tâche planifiée n'a été créée avec
l'autorisation de l'utilisateur. Ne pas annoncer une surveillance permanente inexistante.
