# Plan de mesure

MODÈLE À COMPLÉTER — aucun compte connecté ni événement installé par ce fichier.

## Objectif et période

Objectif réel ; événement ; population ; pays/langue ; périodes comparables ;
baseline ; délai de conversion ; saison ; dates de modifications et incidents.

| Niveau | Métrique proposée | Définition / dénominateur | Source réelle | Limites | Responsable |
|---|---|---|---|---|---|
| Technique | URL importantes accessibles / indexation vérifiée | À définir | À vérifier | Couverture, délais | |
| Visibilité | Impressions / requêtes / pages | À définir | À vérifier | Marque, agrégats | |
| Visite | Sessions éligibles / engagement utile | À définir | À vérifier | Collecte, consentement | |
| Action | Leads qualifiés / achats / téléchargement réel | À définir | À vérifier | Doublons, qualité | |
| Économie | Revenu net / marge / coût complet | À définir | À vérifier | Attribution != causalité | |
| IA | Mentions, citations, impressions, renvois | Une définition par outil | À vérifier | Pas de total multi-outils naïf | |

## Funnel de page

| Couche | Question | Signal minimal | Décision si le signal manque |
|---|---|---|---|
| L1_VISIBLE | La page est-elle trouvable ? | Accès, impression ou indexation observable | Corriger découverte ou marquer NON_VERIFIE |
| L2_CHOISIE | La page est-elle sélectionnée ? | Clic, consultation depuis un résultat ou entrée sociale | Tester angle, extrait et adéquation à l'intention |
| L3_FIXEE | La page répond-elle correctement ? | Réponse utile, liens, preuve, accessibilité et parcours contrôlés | Corriger le blocage le plus important |
| L4_CONVERTIT | La page fait-elle progresser ? | Événement aval, visite qualifiée ou clic commercial défini | CORRIGER, ARRETER ou NON_CONCLUANT selon la fenêtre |

Définir les événements projet avant le test. Une visite qualifiée Reddit/X est une
session issue de la source qui consulte au moins deux pages ou déclenche
`article_to_atelier`, `view_pieces` ou `share_look` lorsque ces événements existent.
Cette définition ne prouve ni identité, ni causalité, ni achat ; elle doit être
adaptée au parcours réel et conservée dans le journal de mesure.

Conserver si disponible `utm_source`, `utm_medium`, `utm_campaign` et `utm_content`
dans les événements locaux. Ne pas ajouter de cookie, de fournisseur tiers ou de
collecte non consentie pour satisfaire ce modèle.

## Qualité

Contrôler événements et doublons ; distinguer nouveaux clients et achats répétés ;
filtrer trafic interne/bots si possible ; aucune collecte de secret ou identifiant
personnel inutile. Vérifier règles applicables avant installation du suivi.

## Analyse

Marque/hors marque, moteur, pays/langue, appareil, intention et landing page.
Ne pas additionner les vues IA à leurs totaux parents. Ne pas exiger l'égalité
GSC/analytics. Garder les périodes incomplètes hors comparaison ou les étiqueter.

## Expérience

Hypothèse ; groupe ; changement ; baseline ; seuils justifiés ; coût maximal ;
fenêtre ; indicateurs techniques immédiats et commerciaux ultérieurs ; confondants ;
résultats possibles CONTINUER / CORRIGER / ARRETER / NON_CONCLUANT.

## Journal

Ce qui a été réellement mesuré, par qui, comment et quand ; aucune donnée future.
