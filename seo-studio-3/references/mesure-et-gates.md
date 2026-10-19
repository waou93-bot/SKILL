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

## Gates proportionnées

Les gates ne sont pas un score global ; un blocage critique ne se compense pas par de bons résultats ailleurs.

1. **BUSINESS** — offre, client/payeur, mécanisme de revenu, coût, contribution et contrainte de cash sont compris ou explicitement inconnus.
2. **SEO** — intention/demande et opportunité sont observées, hypothétiques ou inconnues ; le niveau de preuve est noté.
3. **PILOTE** — tranche la plus petite qui permet une décision ; baseline, action, coût max et critère d'arrêt existent.
4. **RÉALISATION** — périmètre, données, partenaire, autorisation, sauvegarde/rollback et QA nécessaire sont disponibles. Pour un site rendu ou un changement de contenu visible, le contrôle `human-reading` a inspecté les écrans concernés à leur taille réelle sur les formats visés ; les défauts ont été corrigés et réinspectés, ou les contrôles non effectués sont explicitement signalés. Pour une analyse sans rendu, ce contrôle est `NON APPLICABLE`.
5. **MESURE** — données aval suffisantes pour décider ; sinon état non concluant et prochaine observation concrète.

Pour chaque gate, indiquer `FAVORABLE`, `DÉFAVORABLE`, `INCONNU`, `NON CONCLUANT` ou `NON APPLICABLE`, avec preuve datée. Une décision de poursuivre est bornée par un périmètre, un plafond, un responsable et une date de revue. Aucune probabilité de réussite ou promesse de rang n'est déduite d'un avis d'agent.
