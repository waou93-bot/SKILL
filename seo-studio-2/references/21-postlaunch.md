# Boucle après publication — contrat 3.3.0

Étendre le parcours `seo-post-deploy` existant avec des observations mesurées, sans créer un skill concurrent ni imposer un service payant. Les revues J0, J+30 et J+90 sont des étapes du planning humain. Le script ne crée ni tâche planifiée ni surveillance en arrière-plan et n'écrit dans aucun compte externe.

Conserver un instantané de l'état publié dans `monitoring/release-state.json`. Son chemin et SHA sont inscrits dans `release_snapshot`. Cet instantané reste figé ; une décision de correction ouvre une nouvelle révision et ne réécrit pas l'historique de publication. Le dossier de transfert initial reste conservé.

Créer `monitoring/state.json` à partir du [template](../templates/monitoring.json). Il lie le `run_id`, l'instantané publié, deux fenêtres distinctes de même durée et la source fournie : fournisseur, date d'export, fichier, SHA, couverture et limites. Le fichier source normalisé contient `rows` ; le contrôleur exige des lignes identiques dans le registre et dans cet export. Conserver aussi l'export brut pour la revue de sa normalisation. L'empreinte établit l'intégrité locale, pas l'authenticité d'une exportation Search Console.

Chaque ligne désigne une page de l'instantané et ses impressions, clics, conversions et position pour les deux fenêtres. Les valeurs absentes restent `null`. L'indexation distingue `INDEXED`, `NOT_INDEXED` et `UNKNOWN`. Préciser pays, appareil, filtres, changement de position, saisonnalité et couverture lorsque ces facteurs limitent la comparaison.

Exécuter depuis le dossier du skill :

```text
python scripts/feedback.py DOSSIER_PROJET --input monitoring/state.json
```

Le [contrôleur](../scripts/feedback.py) vérifie projet, fichiers, empreintes, fenêtres et métriques. Par défaut, il examine une baisse relative de CTR d'au moins 20 % lorsque chaque fenêtre compte au moins 100 impressions. Ces seuils sont configurables et constituent des signaux d'investigation, pas une preuve de causalité ou une règle universelle.

La sortie propose `OBSERVE`, `REVIEW_SNIPPET_AND_INTENT` ou `INVESTIGATE_INDEXATION`. Une non-indexation invite à examiner accès, canonical et utilité. Aucun article n'est supprimé, aucun snippet réécrit et aucun lien soumis automatiquement. Si une correction est approuvée, les revues impactées sont rouvertes ; le script énumère les revues à rouvrir, sans modifier l'état.

Distinguer propositions, actions réellement effectuées et résultats observés. Une fenêtre trop petite, une métrique inconnue ou un export absent ne justifient ni conclusion de performance ni promesse de classement. Les informations terrain sur l'expérience utilisateur restent distinctes des mesures de laboratoire de la [recette technique](22-technical-release.md).
