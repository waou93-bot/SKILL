# Scénarios de vérification documentaire

| Fixture | Invariant attendu |
| --- | --- |
| Chrome desktop resized 390px, aucun appareil mobile | Resize indiqué ; Safari iOS/Chrome Android réel BLOCKED, procédure manuelle |
| Profil iPhone en Playwright/WebKit desktop | Émulation nommée ; aucune prétention Safari iOS réel |
| Android réel disponible, Safari absent | Résultats Android limités aux essais effectués ; iOS séparément BLOCKED |
| Session cloud sur appareil physique iOS identifié | real_device distant si preuve session/modèle/OS ; limites des contrôles accessibles signalées, pas BLOCKED du seul fait du cloud |
| Table lisible desktop mais CTA coupé paysage/clavier | FAIL de l'état observé, preuve et correctif minimal ; aucune validation globale |
| Capture seule d'un formulaire réussi | Rendu seulement ; envoi/livraison événement non prouvés |
| Carte Analytics activée mais rapport inaccessible | Configuration distincte ; réception inconnue/BLOCKED, pas zéro activité |
| Correctif local, ancienne version encore en production | Local corrigé ; production ancienne, aucune réussite publiée inventée |
| CSS partagé corrigé après QA | Preuves affectées invalidées ; rejouer gabarits/platformes concernés |
| Pas de formulaire, ni animation | N/A contextualisé pour critères correspondants ; pas d'implémentation inutile |
| Refus consentement avec requête observée | Diagnostiquer technologie/état ; ne pas déduire conformité d'une bannière visible |

Ces fixtures vérifient les décisions et frontières des preuves, pas des tests de site réel. Consigner revue/contrôles réellement exécutés et cas non exécutés.
