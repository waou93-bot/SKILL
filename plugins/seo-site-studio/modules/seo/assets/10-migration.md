# Migration / refonte — fiche de protection

MODÈLE — ne pas exécuter sans validation du périmètre et des permissions.

## Avant changement

Date, propriétaire, domaine, environnements, versions, sauvegardes et rollback.
Inventaire : URL, visites utiles, conversions, liens/importance métier, statut,
canonical, langues et contenu. Les données manquantes doivent être déclarées.

| Ancienne URL | Valeur connue / preuve | Décision | Destination équivalente | HTTP attendu | Canonical/langue | Test / résultat |
|---|---|---|---|---|---|---|
| À REMPLIR | | Conserver / modifier / fusionner / retirer | | | | |

Pas de fusion ou suppression sur la seule absence de trafic. Préserver les pages
utiles à l'assistance ou au parcours. Ne pas rediriger tout vers l'accueil.

## Tests

Liens internes et entrants critiques ; sitemaps ; canonical/hreflang ; statuts ;
absence de boucles ; contenu rendu ; formulaires ; assets ; mobile ; mesure.
Préserver protection du staging et indexabilité voulue de production.

## Mise en ligne

Autorisation de publication distincte ; propriétaire ; lot ; preuve du déploiement ;
contrôles sur production ; anomalies ; seuil de rollback et procédure.
Ne pas déclarer succès de production à partir de la seule staging.

## Observation

Journal des modifications et fenêtres de mesure. Rechercher les causes techniques
avant d'attribuer une baisse à un algorithme. Préparer suivi sans inventer exécution
future ni automatisation permanente.
