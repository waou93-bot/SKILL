# Audit, opportunités et plan

## Inventaire
Récupérer sitemap, navigation et exports autorisés; échantillonner le crawl quand nécessaire et annoncer sa couverture. Pour chaque URL: statut HTTP horodaté, objectif, offre/public, intention, canonical, meta robots et X-Robots-Tag, accessibilité du contenu, liens internes, preuves originales et page commerciale cible. Consigner robots.txt et sitemap séparément. robots.txt n'est pas une preuve de désindexation; un canonical déclaré n'est pas une preuve du canonical choisi par Google. La duplication peut être suspectée par similarité et confirmée par revue. Sans mesures de performance, vitesse inconnue.

## Sources
Search Console si connecté: dimensions page/requête/pays/appareil, périodes égales, filtres et type de recherche constants; conserver limites, pagination, lignes anonymisées/absentes, fraîcheur et propriété. Les positions sont des moyennes observées, pas des rangs universels. Examiner positions proches de la première page (seuil exploratoire configurable), fortes impressions/faibles clics, pertes et intentions partagées.
Compléter par fournisseur SEO autorisé et résultats étudiés: fournisseur, requête, pays, langue, date, URL et méthode de localisation. Une recherche web générique n'est pas une SERP locale exhaustive. Sans outil: hypothèses explicites, métriques null. Ne pas assimiler absence de données à absence de demande.

## Architecture et intentions
Avant de prioriser ou de créer un calendrier, relier chaque groupe de requêtes à une destination canonique du site et à un objectif business. L'intention décrit le besoin à satisfaire; un cluster de mots-clés ne justifie pas à lui seul une nouvelle URL.

Pour chaque opportunité, vérifier les pages existantes, leur intention, leur canonical observé ou déclaré, leur rôle dans le parcours et leurs liens internes. Décider `update` si une page couvre déjà le besoin, `merge` si plusieurs pages se concurrencent sur la même intention, `create` seulement si une intention ou un besoin distinct est démontré, et `investigate` si les preuves ne permettent pas de trancher. Une demande ou un volume non mesuré reste explicitement une hypothèse.

Pour toute page planifiée, consigner dans les contrats existants: l'intention et `existing_url`/`recommended_action` dans KeywordOpportunity; `target_url`, `action`, `intent` et `internal_links` dans ContentBrief; le hub ou la page pilier avec `pillar_url` dans EditorialCalendar. Utiliser `evidence`, `assumptions`, `missing_data` et `next_action` pour expliquer la décision et son niveau de confiance. Ne pas ajouter de propriétés hors schéma.

Chaque nouvelle page doit avoir un angle et une valeur propres, une place explicite dans la hiérarchie (hub, parent ou page fille), des liens entrants et sortants utiles, et un parcours de conversion cohérent avec l'offre. Vérifier si les résultats de recherche et les besoins observés justifient des pages séparées avant de séparer des intentions proches. Écarter les pages facettes, les variantes et les duels sans valeur distincte; éviter pages orphelines, maillage artificiel et duplication de gabarit.

## Priorisation
Évaluer offre, intention/proximité de conversion, potentiel observable, concurrence, expertise originale, effort et cannibalisation. Score facultatif: notes 0–4; poids 25/20/15/10/15/10/5 %, effort et cannibalisation inversés. Afficher notes, poids, justification et couverture des données. Si composante inconnue, score null ou intervalle avec hypothèses documentées, jamais un zéro arbitraire. Heuristique, pas prédiction.
Grouper par intention et thème, désigner piliers et liens utiles. Même intention existante: mise à jour par défaut; nouvelle page seulement si besoin distinct justifié. Plan de 30 jours avec date, action, propriétaire, effort, coût/devise, dépendances et étape de validation. Ne pas dépasser budget connu; budget inconnu: plan provisoire et estimation explicite. Garder du temps pour mesure et révision.

## Liens
A: rechercher partenaires, ressources, presse, données originales et contextes éditoriaux pertinents; aucune prise de contact automatique. B: réseau entre sites optionnel, désactivé par défaut; réseau éditorial utile = liens choisis pour aider le lecteur; échanges systématiques destinés au classement = risque de spam, ne pas les organiser. Pas d'autorité DA/DR comme succès.
Stocker source_url, target_url, contexte, pertinence, anchor_text, rel_attributes, statut, date de vérification et provenance. Pour liens commerciaux, appliquer sponsored (nofollow peut être approprié); ugc pour contributions utilisateurs selon contexte. Le propriétaire peut retirer tout lien. Aucune création sur site tiers sans droit explicite.

Sources officielles vérifiées le 2026-10-04; revérifier à l'exécution:
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links

## Opportunités issues des citations IA

Si le programme vise les réponses IA, consulter ai-seo et son protocole de cartographie lorsque disponible. Relier les questions de décision aux sources citées, à leur type et aux affirmations soutenues. Ajouter au brief les lacunes de preuve et un pack réutilisable : conclusion, méthode, limites et visuel pertinent. Conserver ces observations dans les preuves existantes sans modifier les schémas. Prioriser les sources pertinentes récurrentes plutôt qu’un quota de liens ou de pages. Vérifier accès et mesure dès le départ ; aucune prise de contact implicite. Les études de corrélation ne garantissent pas un gain causal.
