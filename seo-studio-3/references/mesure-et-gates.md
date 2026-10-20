# Mesure, économie et décisions

Appliquer les contrats actuels des skills `business` et `seo` au contexte. Ce document rassemble uniquement les invariants nécessaires à SEO Studio 3 ; leurs références restent les sources de méthode détaillées.

## Chaîne de valeur

| Étape | Signal à mesurer | Ce que le signal ne prouve pas à lui seul |
|---|---|---|
| Découvrable | état HTTP/rendu/indexabilité ; impressions par page et requête si Search Console accessible | visibilité réelle sur toutes les requêtes, ou rang constant |
| Choisie | clics organiques, CTR avec son dénominateur et son segment | visite, engagement ou intention d'achat |
| Utile | sessions pertinentes selon une définition projet ; visite d'offre ou consultation utile | prospect qualifié ou vente |
| Action | clic interne/CTA, sortie partenaire, formulaire envoyé, appel ou inscription réellement confirmée | transaction, revenu, commission acquise |
| Économie | transaction validée, revenu net, remboursements, contribution, coûts et délai d'encaissement | rentabilité future ou causalité SEO sans étude adaptée |

Présenter les métriques séparément. Search Console mesure des événements de recherche ; analytics, CRM, plateforme d'affiliation et caisse observent d'autres étapes. Ne pas forcer leur égalité. Documenter source, période, filtres, consentement, attribution, décalages et pertes de données.

## Baseline et expérience

Avant un pilote, consigner :

- page ou groupe de pages, audience et intention ;
- problème prioritaire et hypothèse qui pourrait être réfutée ;
- métrique, événement, numérateur, dénominateur et source ;
- période de référence comparable et changements connus ;
- action prévue, responsable, coûts en cash et temps, plafond de perte ;
- fenêtre de mesure, saisonnalité, facteur externe ;
- seuils contextuels pour continuer, corriger, arrêter ou conclure non concluant.

Choisir la fenêtre selon la cadence de données et le cycle d'achat. Quatre semaines, 30/60/90 jours et toute autre durée sont des repères de planification, jamais une garantie que le SEO aura produit un signal. En trafic faible, garder les valeurs absolues et la conclusion `NON_CONCLUANT` si l'échantillon ne permet pas le jugement. Un groupe témoin peut aider lorsqu'il est faisable, mais ne pas présenter un simple avant/après comme preuve causale.

## Économie et cash

Relier les objectifs d'acquisition à Business sans additionner une seconde fois les coûts. Compter recherche, contenus, expertise, développement, outils, création média, validation, maintenance et temps de coordination selon le mandat. Séparer dépenses encaissées, coûts futurs, temps du porteur et investissements déjà engagés.

Pour un site marchand/affilié, distinguer sortie commerciale, clic, commande, commande confirmée, retour/annulation, commission validée et cash encaissé. Pour un service, distinguer clic, demande, lead qualifié, devis et client. Ne pas valoriser un clic comme une vente. Calculer contribution incrémentale seulement si le revenu et les coûts variables sont connus ; sinon `NON_CALCULABLE`. Inclure un scénario zéro nouveau revenu pendant le pilote et son coût maximal.

Si la trésorerie disponible est le frein, classer les actions selon (a) preuve de valeur, (b) coût cash et heures, (c) délai probable avant mesure et encaissement, (d) risque d'endommager l'existant. Le délai SEO est variable ; identifier un canal à retour plus rapide lorsque Business le justifie. Cela n'autorise pas publicité, achat d'outil, contact, publication ni engagement sans permission.

## Repères de décision — publication non bloquante

Ces statuts ne sont pas un score global et ne confèrent aucun pouvoir de bloquer une publication explicitement demandée. Ils rendent les preuves et les réserves visibles afin d'éclairer la décision de l'utilisateur.

1. **BUSINESS** — offre, client/payeur, mécanisme de revenu, coût, contribution et contrainte de cash sont compris ou explicitement inconnus.
2. **SEO** — intention/demande et opportunité sont observées, hypothétiques ou inconnues ; le niveau de preuve est noté. Pour tout site multi-pages, la carte suit l'[architecture de référence](architecture-et-indexation.md) et justifie chaque branche/page par son intention, sa valeur, son rôle et son entretien. Pour un site existant, auditer le maillage, routes, canonicals, directives, sitemap et indexation dans le périmètre déclaré ; marquer `INCONNU/NON_VÉRIFIÉ` ce qui manque. Pour un site à créer, les pages indexables prévues ont une intention distincte et le plan relie les pages prioritaires. Aucun statut favorable sans preuve de contrôle.
3. **PILOTE** — tranche la plus petite qui permet une décision ; baseline, action, coût max et critère d'arrêt existent.
4. **RÉALISATION** — consigner le périmètre, les données, les partenaires, les sauvegardes, la QA et leurs limites. Pour une V1 complète ou une revue complète, produire le relevé `site-checklist` sur ses 20 points et traiter Safari SF01–SF08 séparément si le contexte s'y prête ; garder la preuve, l'environnement et la couverture. Les limites d'accès sont `NON VÉRIFIÉ`, jamais `CONFORME` ; l'absence d'un appareil iOS réel interdit de dire « Safari iOS validé ». Pour un changement ciblé, vérifier uniquement les points affectés et les régressions plausibles. Les analyses `web-perf` sont des recommandations uniquement si ce skill est disponible ; aucune optimisation n'est appliquée sans demande explicite. L'inventaire des liens sortants identifie les partenaires vérifiés, liens non partenaires et destinations inconnues. Selon la règle Studio 3, ne pas ajouter de nouveaux liens non partenaires et corriger les existants si c'est possible dans le périmètre autorisé ; tout élément non corrigé est une réserve documentée, jamais un motif pour bloquer la publication. Garder les URL de recherche et de preuve dans les notes internes, pas dans les liens publics. Si un choix matériel de stack, fournisseur, référence ou outil reste ouvert, documenter la recommandation toolbox comme réserve ou l'omettre du périmètre, sans suspendre la publication demandée. Pour un site rendu ou un changement de contenu visible, inspecter `human-reading` aux formats visés ; corriger les défauts pouvant l'être, et signaler ceux qui restent ainsi que les contrôles non effectués. Pour une analyse sans rendu, ce contrôle est `NON APPLICABLE`.
5. **MESURE** — données aval suffisantes pour décider ; sinon état non concluant et prochaine observation concrète.

Pour chaque repère, indiquer `FAVORABLE`, `DÉFAVORABLE`, `INCONNU`, `NON CONCLUANT` ou `NON APPLICABLE`, avec preuve datée. Les statuts défavorables ou inconnus ne suspendent pas la publication demandée : les annoncer comme réserves et poursuivre. Une décision de poursuivre est bornée par un périmètre, un plafond, un responsable et une date de revue ; cela n'est pas une autorisation donnée au skill d'annuler la publication choisie par l'utilisateur. Aucune probabilité de réussite ou promesse de rang n'est déduite d'un avis d'agent.


