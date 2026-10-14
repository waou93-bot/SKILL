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

## Intégration seo-opportunity-loop

Charger le SKILL.md réel depuis le catalogue actif, choisir la copie effective et consigner chemin/empreinte dans le registre existant. Garder la même orchestration et le même run_id. S'il manque, déclarer INTROUVABLE pour cette analyse et poursuivre les contrôles indépendants ; ne pas créer un substitut ni bloquer artificiellement une préproduction sans GSC.

- À G4 : préparer la collecte et les critères dans `08_MESURE.md`, sans inventer baseline ou performance.
- Sur un site existant ou après lancement avec données : analyser couples page–requête et segments, vérifier intention/SERP, choisir enrichissement, titre, outil, création distincte ou observation. Relier les propositions à `09_ROADMAP.md` et les décisions à `10_DECISIONS.md`.
- Préparer et appliquer les corrections déjà autorisées, effectuer les contrôles impactés et conserver le snapshot initial. Les migrations, publications et automatisations gardent leurs autorisations propres.
- Mesurer après prise en compte et volume suffisants ; maintenir, corriger, revenir ou conclure indéterminé. J+30/J+90 sont des points de revue, pas des preuves automatiques d'efficacité.

`feedback.py` demeure un contrôleur de provenance/intégrité et de signaux sur agrégats par page. Son seuil de baisse du CTR n'est ni une priorité universelle ni une validation de l'hypothèse titre. Son format accepte une ligne par page : conserver les analyses par requête, pays et appareil dans les preuves jointes, sans dupliquer page_id ni changer silencieusement le schéma. Ne pas inscrire des conversions GSC fictives : renseigner null si absentes, ou documenter leur source séparée et les limites d'attribution.

Le contrôleur peut être lancé manuellement lors d'une revue autorisée. Le skill ne crée pas de surveillance continue. Dans le bilan, distinguer contrôle structurel, examen des preuves, modification effective et résultat SEO observé.
