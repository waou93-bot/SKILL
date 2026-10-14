# Intégration Personna 1.2.0 — Studio 3.2.0

Le protocole 1.1.0 pouvait accepter des réponses et revues anciennes dans un
nouveau run, ou perdre la cohérence tâche/suite et provenance. La version 1.2
lie l'enveloppe d'exécution au run et à l'entrée observée, reconstruit les requêtes
et lie la revue au record courant. Les JSON de mauvaise structure sont bloqués.

Studio regrade les pièces du profil courant avec le vérificateur intégré et
exige l'identité du rapport recalculé avec la preuve test_report. Aucun code Python
du dossier projet n'est chargé. Les chemins restent contenus au projet sans liens
symboliques. Les profils sans évaluation restent provisoires en brouillon et sont
bloqués au transfert strict. Les exigences R01–R28 sont conservées.

La copie de l'évaluateur est identique à personna/scripts/evaluate.py ; le test
de synchronisation et le manifeste empêchent une divergence silencieuse de livraison.
La méthode de recherche Reddit/GitHub et l'entretien de Personna sont conservés.

Voir VALIDATION.md pour les contrôles réellement exécutés. Les pièces locales
restent déclaratives : l'intégrité n'atteste pas cryptographiquement l'hôte.
Les critères doivent être pertinents et les appels réellement examinés. Les
fixtures ne prouvent ni formation métier, ni fonctionnement d'un site réel,
ni sécurité outillée. Les dix essais actuels sont textuels et la baseline passe
également ; aucun bénéfice causal du persona n'est revendiqué.

Aucun abonnement, API payante additionnelle ni framework d'agents obligatoire.
