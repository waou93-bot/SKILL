---
name: ai-seo
description: "Construire, auditer et mesurer le canal d'acquisition par ChatGPT Search et les autres moteurs ou agents IA sur un site existant ou en cours. Déclencher pour SEO IA, GEO, AEO, LLMO, recommandations IA, citations, visibilité ChatGPT/Claude/Perplexity/Gemini/Copilot, accès des robots ou site lisible par les agents. Ne pas déclencher pour un chatbot interne, une simple retouche visuelle ou un audit SEO classique sans enjeu IA."
metadata:
  version: "3.0.0"
  reviewed_at: "2026-10-04"
---

# AI SEO — acquisition, citations et recommandations

Développer un canal d'acquisition utile, pas un score GEO décoratif. Rendre l'offre découvrable, compréhensible, vérifiable et utilisable par les humains et les agents, puis mesurer les observations et les conversions disponibles. Aucune promesse de recommandation, de classement ou d'entraînement d'un modèle.

## Démarrage proportionné

Lire les instructions locales, l'état Git et seulement le contexte utile déjà présent : MASTER, BUSINESS, SEO, marketing, analytics, backlog, architecture, domaine public, cible, langues, offre et contraintes. Ne pas reposer une question dont la réponse existe. Ne pas réinitialiser un projet, changer sa DA ou créer un MASTER concurrent.

Identifier : objectif commercial, pages publiques prioritaires, plateformes/surfaces visées, conversion attendue, preuves disponibles, politique d'entraînement, accès techniques et périmètre autorisé. Distinguer domaine de production, preview, back-office et espaces privés. Sans donnée bloquante, avancer avec hypothèses explicites et réversibles.

Choisir le plus petit mode suffisant :

| Mode | Action |
|---|---|
| Diagnostic ciblé | Vérifier le point demandé et les dépendances directes, sans audit géant. |
| Site existant | Baseline, blocages, modifications ciblées, tests de non-régression et plan de mesure. |
| Projet en cours | Intégrer les critères dans les pages et composants prévus ; pas de refonte automatique. |
| Pré-lancement | Vérifier les exclusions de preview et préparer séparément les règles de production. |
| Mesure | Observer un panel fixe, distinguer les surfaces et comparer des périodes comparables. |

Audit seul = lecture seule. Une demande d'implémentation autorise les changements locaux utiles, pas implicitement un déploiement, une dépense, un envoi de messages ou une modification WAF. Ne pas installer de serveur ou de service permanent sans besoin validé.

## Principes incontournables

- Distinguer accès technique, indexation, récupération, citation, mention, recommandation, visite et conversion. Aucun n'est la preuve automatique du suivant.
- Recherche, entraînement et requêtes déclenchées par l'utilisateur sont des usages distincts. Consulter [la matrice des plateformes](references/platform-ranking-factors.md) avant toute modification de robots ou WAF.
- Conserver une même vérité éditoriale pour visiteurs et agents. Interdire cloaking, texte caché persuasif, prompt injection dans les pages, faux avis, fausses études, fausses dates, fermes de mentions et spam de forums.
- Une directive robots n'est pas une authentification. Ne jamais rendre publics comptes, commandes, données clients, secrets ou documents privés pour gagner de la visibilité.
- `llms.txt`, Markdown, OKF, MCP, WebMCP et protocoles marchands ne sont pas des tickets de classement. Les traiter selon leur support réellement documenté et le besoin produit ; lire [les extensions optionnelles](references/okf.md).
- Ne pas reprendre des pourcentages universels de gain, des quotas de mots ou une liste figée de facteurs de classement. Étiqueter chaque recommandation : documentation officielle, observation locale, hypothèse ou expérience.
- Reconsulter les [sources primaires](references/sources.md) avant un conseil dépendant d'un fournisseur. En cas de documentation contradictoire, dater le conflit et privilégier la source officielle spécifique actualisée, sans inventer une certitude.

## Workflow

### 1. Décider de la place du canal

Évaluer la demande exprimable en langage naturel, l'utilité de l'offre, sa différenciation vérifiable, l'accessibilité de ses informations et l'action attendue après la réponse IA. Conclure : prioritaire, expérimental, secondaire ou non pertinent, avec raisons. Un canal peu pertinent ne condamne pas le produit. Sur l'existant, ne pas rouvrir un business plan complet par défaut.

### 2. Établir la baseline

Inventorier les pages prioritaires et quelques concurrents réellement pertinents. Préparer, à titre de point de départ ajustable, 15 à 30 questions représentatives : problème, découverte, comparaison, contraintes, alternatives, confiance et décision. Séparer requêtes de marque et sans marque. Ne pas mentionner le site dans les questions sans marque.

Observer seulement les plateformes disponibles. Consigner la surface exacte, recherche activée ou non, langue, pays, contexte/personnalisation, modèle affiché, date, réponse, liens et limites. Une requête API n'est pas un test de l'application grand public. Un chat déjà informé sur le projet n'est pas une baseline neutre. Un moteur inaccessible = non testé, jamais zéro visibilité. Voir [mesure](references/04-measurement.md).

### 3. Auditer l'accès et l'implémentation

Comparer HTML initial, DOM rendu et arbre d'accessibilité sur les pages représentatives. Vérifier statuts, redirects, canonical, robots meta/en-têtes, robots.txt, sitemap, maillage, rendu du contenu utile, schema valide et cohérent, langues, performance et parcours de conversion. Examiner le CDN/WAF et les logs uniquement avec les droits disponibles. Les requêtes avec UA simulé ne prouvent pas l'accès du vrai robot.

Appliquer la [checklist d'implémentation](references/implementation.md). Corriger d'abord les empêchements démontrés ; préserver les URLs, le design et les données. Documenter le diff, les risques et le rollback.

### 4. Construire les pages qui aident vraiment à choisir

Relier chaque question à une URL canonique utile et une preuve. Partir des situations d'usage, critères de décision, contraintes et limites de l'offre, pas d'une suite de mots-clés. Montrer pour qui la solution convient et ne convient pas. Préférer des informations originales vérifiables à des textes génériques. Lire [les modèles éditoriaux](references/content-patterns.md) et [les adaptations métier](references/content-types.md).

Pour recommander une offre, les agents doivent pouvoir identifier l'entité, ce qui est réellement fourni, ses conditions et les éléments de confiance. Développer la présence externe légitime sans fabriquer un consensus. Une citation d'un guide ne prouve pas une recommandation de son éditeur : lire [citation et recommandation](references/citations-vs-recommendations.md).

### 5. Implémenter, instrumenter et vérifier

Utiliser la stack existante et les skills techniques réellement disponibles. Construire des modifications petites et testables. Définir les événements utiles (ex. vue de guide, utilisation du comparateur, clic affilié, formulaire qualifié), leur déduplication et leurs limites. Ne pas injecter de collecte non autorisée. Les logs de bots sont séparés de l'audience et des conversions humaines.

Exécuter les tests du projet, les contrôles de liens, rendu, accessibilité et structured data adaptés au changement. Vérifier les pages privées et les anciennes URLs. Distinguer contrôles locaux, preview, production, indexation observée et visibilité IA observée.

### 6. Mesurer et arbitrer

Comparer les observations avant/après dans des conditions enregistrées, avec pages témoins lorsque possible. Noter changements de produit, de moteur, saisonnalité et campagnes. Prioriser selon valeur attendue, confiance, effort, risque et dépendances ; pas de précision financière inventée. Réviser ou arrêter les expérimentations sans résultat exploitable. Une cadence proposée n'est pas une veille effectivement programmée.

## Livrables et outils

Réutiliser le dossier d'acquisition existant. À défaut, et seulement pour une mission assez large, créer `SEO/AI_ACQUISITION/` avec les [modèles de projet](templates/project/00_CONTEXT.md) : contexte, audit, plan, mesure et bilan. Une petite correction n'exige pas ces documents.

Chaque ticket doit contenir observation/preuve, URL ou fichier, changement proposé, priorité, responsable, dépendances, test d'acceptation et rollback. Ne pas remplir les modèles avec des chiffres imaginés.

Outils Python 3.10+ sans dépendances externes, réseau ni API payante ; charger [leur documentation](scripts/README.md) avant emploi :

- `audit_snapshot.py` : triage hors ligne de captures HTML/HTTP fournies, pas un crawler.
- `classify_referral.py` : classification conservatrice des signaux de provenance, pas une attribution causale.
- `measure_panel.py` : taux du panel observé, pas un classement universel.
- `init_project.py` : création optionnelle des seuls documents absents, aperçu par défaut.
- `install.py` : installation locale du skill avec aperçu, sauvegarde vérifiée et restauration sur erreur.

## Intégrations

Fonctionner de manière autonome ou appelé par Organisation/SEO. Lire [le contrat d'intégration](references/integrations.md) ; ne pas supposer qu'un skill absent a été exécuté. Organisation coordonne, ai-seo porte ce canal, SEO garde le socle organique, Business arbitre l'investissement, Design DNA protège la DA. Aucun rappel circulaire ni agent prétendument indépendant si l'outil de délégation manque.

## Définition de terminé

Rendre : périmètre réellement couvert, fichiers effectivement changés, tests exécutés et résultats, preuves, inconnues, accès manquants et prochaines priorités. Statut `COMPLET`, `PARTIEL` ou `BLOQUE` relatif à la tâche demandée, jamais à une visibilité future garantie.

Séparer explicitement : skill écrit, tests du package, commit GitHub vérifié, installation locale, découverte par Codex, application à un site, déploiement, résultats d'acquisition. Un push GitHub ne met pas à jour le PC de l'utilisateur.

Les tests déterministes sont dans `tests/test_tools.py`. Les scénarios comportementaux de `evals/evals.json` nécessitent de vraies exécutions ; leur présence ne signifie pas qu'ils ont réussi.
