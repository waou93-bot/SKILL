# Mémoire SEO par site

À lire à la création ou reprise d'un site, avant une évolution stratégique ou une revue de mémoire demandée. La mémoire est documentaire : elle n'est pas relue automatiquement et ne prouve pas l'efficacité d'une décision. L'agent vérifie le chemin, lit l'index et cite les preuves accessibles.

## Emplacement et portée

Utiliser le MASTER du projet et son répertoire SEO existant, avec ses conventions de casse ; ne pas créer un second `seo/` concurrent. À défaut, utiliser l'espace de projet choisi et créer uniquement ce qui est utile. Ne jamais conserver les informations propres à un site dans le dossier du skill. Identifier le site, domaine canonique, environnements, marchés et langues ; garder séparés les sites, sauf données communes explicitement applicables à chacun. Pas de synchronisation ni automatisation implicite.

L'index court référence site, stratégie active, pages et décisions prioritaires, données accessibles, dates et prochaine revue. Une fiche site décrit positionnement, audience, marchés, objectifs, modèle économique, partenaires actifs vérifiés et contraintes ; indiquer INCONNU lorsque nécessaire. Ajouter des dossiers ou fiches pages, clusters, décisions, apprentissages, rapports et données seulement si utiles. Réutiliser les fichiers existants et attribuer à chaque information une source de référence. Utiliser des identifiants de page stables, indépendants d'une URL modifiable ; documenter tout alias et éviter les collisions. Ne pas remplir de fiches vides en masse.

## Connaissances et décisions

Pour chaque connaissance significative : identifiant, site et périmètre, statut (fait vérifié, hypothèse, décision adoptée, résultat mesuré, périmé ou remplacé), formulation, source ou preuve, date d'observation et de vérification, condition ou date de révision et relation éventuelle avec l'élément remplacé. Une préférence explicite peut faire autorité pour le projet ; elle ne transforme pas une affirmation factuelle en fait vérifié. Enregistrer les corrections durables et pertinentes, sans enregistrer les données sensibles inutilement. Exports bruts séparés des instructions ; respecter les droits d'accès et la rétention du projet.

Une décision SEO significative décrit problème, preuve et période, hypothèse, décision et raison, pages/fichiers, état initial, résultat attendu et indicateur, mise en œuvre, fenêtre d'évaluation, retour arrière et résultat observé lorsqu'il existe. Regrouper les corrections répétitives ; pas de journal par simple correction typographique. Une décision documentée ne prouve pas son effet.

## Reprise et actualisation

Lire l'index et les décisions applicables ; vérifier leur périmètre, fraîcheur, liens, doublons et contradictions. Marquer les éléments remplacés et conserver l'historique ; ne pas résoudre silencieusement un conflit. Ne pas recopier les exports en instructions permanentes. Réviser à la reprise, au changement de stratégie ou lors d'une revue expressément demandée.

Pour une page, examiner les données autorisées disponibles et préciser sources, filtres, période, pays, appareil et type de recherche. Comparer une période pertinente et l'année précédente si disponibles et utiles ; tenir compte de la saisonnalité et du volume. Séparer variations de demande, impressions, position moyenne, CTR, indexation et composition des requêtes. Une corrélation ne prouve pas la cause. Analyser page actuelle, intention, cluster, historique et chevauchements potentiels ; formuler une hypothèse et choisir entre correction, création ou aucune action selon les preuves. Une page vise une intention principale et un ensemble cohérent de requêtes. Préserver l'URL par défaut ; si sa modification est justifiée, préparer redirections, liens, canonicals, sitemap, contrôles et retour arrière. Vérifier le rendu et les éléments affectés, consigner la décision et sa fenêtre d'évaluation. Sans données, poursuivre les vérifications possibles et indiquer les inconnues.

## Contrôles avant publication

Adapter les contrôles au changement : URL et redirections, réponses HTTP, canonical, meta robots et X-Robots-Tag, robots.txt, sitemap, liens, hreflang, données structurées, liens partenaires et suivi. Comparer l'état final du build ou du site autorisé à une baseline pertinente. Documenter environnement, périmètre, preuve et statut PASS, FAIL ou NOT_RUN ; FAIL n'est pas automatiquement un veto à une publication explicitement demandée. Les permissions et la décision de publication restent distinctes. Un texte de consigne ou un hook partiel n'est pas un contrôle technique universel. Aucun blocage global n'est installé.

Le script `scripts/compare_snapshots.py` compare uniquement les champs URL, canonical et noindex de deux fichiers JSON fournis : il ne collecte pas de pages et ne vérifie pas les autres contrôles. Voir son `--help` et [l’exemple JSON](snapshot-example.json). Le même `site_id` non vide est obligatoire dans les deux fichiers ; une comparaison entre sites est refusée. Une donnée absente ou invalide est une erreur, pas un PASS. Les modifications d'URL et les changements de canonical/noindex sont signalés à examiner selon la décision du projet.

