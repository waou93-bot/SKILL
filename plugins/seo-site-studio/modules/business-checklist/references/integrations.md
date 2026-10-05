# Contrats Organisation, SEO et réalisation

Cette spécification ne prouve aucune installation ni modification d'un autre skill.
Lire les versions réellement disponibles avant un raccordement.

## Organisation

Entrée : project_id, run_id, mode, périmètre, documents, contraintes et permissions.
Sortie : décision, justifications, preuves, six gates, inconnues, checklist,
prochain périmètre proposé, plafonds, autorisations distinctes et artefacts.
Le contrat est `assets/05-decision-handoff.json` (schéma local 2.0).

Organisation demeure le routeur. L'appel direct de Business Checklist ne doit pas
échouer faute d'Organisation. En son absence, présenter la même décision à l'utilisateur.
Ne pas déclencher plusieurs orchestrations pour la même demande.

Rôles du routeur : Luna = extraction/mise en forme ; Terra = cadrage/priorités ;
Sol = faisabilité/calculs ; Astra = arbitrages majeurs. Ce ne sont pas des IDs de
modèles configurés par ce package. Les capacités réelles décident de l'exécution.

## SEO : aller-retour borné

Business fournit : offre, segment, payeur, territoire/langue, prix, marge (ou inconnue),
objectifs de conversion, budget de recherche proposé, horizon et preuves.
SEO fournit : intérêt du canal distinct de santé technique, hypothèses de trafic et
conversion avec statuts, coûts/calendrier, risques, test et limites d'observation.

Le contrat `seo/assets/09-handoff.json` V1 inspecté dans le package fourni expose
notamment channel_decision, technical_readiness, evidence_basis, permissions,
project_outcome_evidence, business_return et limitations. C'est une référence de
compatibilité documentaire, pas une preuve d'appel réel. Relire la version installée.

Ne pas transformer visibilité/citations/clics en chiffre d'affaires. Une possibilité
SEO ne vaut pas validation de demande. Un canal non rentable n'interdit pas une
alternative ; renvoyer à Business les conséquences économiques, pas un verdict
universel sur le projet.

Garder des IDs uniques de coûts et une hypothèse propriétaire (Business ou SEO).
Contrôler qu'une dépense de contenu, technique ou acquisition ne soit pas comptée
dans les deux modèles. Pas de boucle SEO→Business→SEO sans question nouvelle.

## New Pro Brain, New Pro, New Site, New App, Design DNA

Leur présence n'est pas obligatoire. Brain éclaire une décision majeure ; il ne
remplace pas les preuves. Les skills de réalisation reçoivent uniquement le périmètre
explicitement autorisé (test, pilote, lot de réalisation). Respecter la DA validée.
Un audit économique n'autorise pas une refonte de code, site ou identité.

## Recommandation ≠ autorisation

Le contrôleur JSON détecte incohérences de champs et limites absentes. Il ne rend
pas une action légitime par magie et ne valide pas l'authenticité d'un accord.
Avant dépense, publication, contact, collecte ou modification distante, vérifier
l'autorisation actuelle, sa portée et sa trace. Préparer sans exécuter en son absence.
