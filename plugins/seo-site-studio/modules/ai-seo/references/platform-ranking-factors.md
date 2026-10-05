# Plateformes : accès et contrôles, pas des facteurs de classement secrets

Révision documentaire : 2026-10-04. Sources primaires dans [sources.md](sources.md).
Vérifier à nouveau les contrôles avant application. Les plateformes et les surfaces ne
partagent pas nécessairement leur index, leurs outils ou leurs signaux de classement.

| Surface | Contrôle/documentation utile | Ce qu'il ne faut pas déduire |
|---|---|---|
| ChatGPT Search | `OAI-SearchBot` pour recherche ; IP officielles et WAF | Autorisation = éligibilité technique, pas recommandation garantie. |
| Entraînement OpenAI | `GPTBot`, politique indépendante de la recherche | Bloquer GPTBot ne signifie pas bloquer ChatGPT Search. |
| Visite demandée à ChatGPT | `ChatGPT-User` ; robots peut ne pas s'appliquer à l'action utilisateur | Ce fetcher ne détermine pas l'inclusion dans Search. |
| Perplexity recherche | `PerplexityBot`, non destiné à l'entraînement des modèles fondamentaux | Ne pas assimiler une visite à une citation. |
| Visite demandée à Perplexity | `Perplexity-User`, fetch utilisateur pouvant ignorer robots | robots n'est pas une protection d'accès. |
| Claude recherche | `Claude-SearchBot` | Ce n'est pas `ClaudeBot`. |
| Entraînement Claude | `ClaudeBot` | Choix distinct de la recherche. |
| Visite demandée à Claude | `Claude-User` | Appliquer les contrôles Anthropic, pas ceux d'OpenAI par analogie. |
| Google AI Overviews / AI Mode | Googlebot, indexation et contrôles Search de prévisualisation | `Google-Extended` n'est pas le contrôle d'inclusion ou de classement Google Search. |
| Certains usages Gemini | Google-Extended contrôle entraînement et grounding des produits précisés par Google | Ce token n'a pas un UA HTTP séparé ; ne pas généraliser à toutes les surfaces Google. |
| Bing / Copilot | Vérifier la documentation Bing actuelle et l'indexation Bing | Ne pas prétendre connaître toutes les sources de toutes les versions Copilot. |
| Autre agent | Identifier comment il découvre et lit le site, puis vérifier son contrat réel | Un agent arbitraire n'obéit pas nécessairement à cette matrice. |

## Procédure robots et WAF

Sauvegarder l'existant. Déterminer les chemins réellement publics. Construire des cas de test
pour accueil, contenu, produit, recherche interne, compte, panier, staging et fichiers sensibles.
Un groupe spécifique à un robot peut remplacer le groupe `*` : ne pas ajouter un Allow global
sans répéter les exclusions nécessaires et vérifier la sémantique du fournisseur.

Ne pas utiliser robots pour sécuriser une ressource. Maintenir authentification/autorisation,
contrôles serveur et exclusions voulues. `Disallow` n'est pas équivalent à `noindex` : un robot
bloqué peut ne pas lire une directive de page. Ne retirer une restriction qu'après vérification
de l'intention du propriétaire. Ne pas supposer un support uniforme de tous les robots meta.

Au WAF, privilégier l'identification vérifiée offerte par le fournisseur ou les plages publiées
actualisées, puis des exceptions limitées aux chemins publics et méthodes nécessaires. Un UA
se falsifie. Ne jamais désactiver globalement la sécurité, les limites ou la protection des
comptes pour laisser passer un bot. Garder journal, test avant/après et rollback.

## Rapport attendu

Pour chaque robot/surface : source + date, intention autorisée, URL testée, règle applicable,
HTTP observé, identité vérifiée ou simulée, verdict confirmé/indice/inconnu, action à effectuer.
Le parseur de `audit_snapshot.py` n'est qu'un triage ASCII simplifié, pas la validation finale
RFC ni le comportement réel du robot. Confirmer les cas ambigus avec un parseur compatible.

Autoriser un crawl ne contraint pas un moteur à indexer, citer ou recommander. Aucun levier
d'entraînement n'est présenté comme un canal d'acquisition mesurable à court terme.
