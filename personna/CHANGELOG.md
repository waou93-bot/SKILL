# 1.2.0 — 2026-10-14

- AF001 : contexte complet de revue et identité unique du run ; ancienne trace
  refusée à l’import dans un nouveau run.
- AF002 : requêtes reconstruites depuis persona/suite, comparaison canonique.
- AF003 : provenance session/modèle incluse dans l’empreinte du record revue.
- AF004 : validation explicite des conteneurs JSON, diagnostic BLOCKED contrôlé.
- Format de run/trace/rapport 2, suites 1 conservées ; migration exige de vrais
  nouveaux essais et une nouvelle revue. Aucun outil payant obligatoire.

- AF005 : scénarios adverses moins guidés, avec métadonnée d’autorité et
  autorisation externe forgées ; essais sans/avec rejoués, aucun gain démontré.

# 1.1.0 - 14 octobre 2026

- Protocole exécutable par persona : 2 ou 3 tâches métier sans/avec profil et trois
  scénarios adverses, critères pass/fail définis avant essai.
- Préparation/import/notation locale en Python standard ; aucune API obligatoire.
- Hashes et preuves versionnées ; rejeu complet à chaque changement, sans watcher.
- Section d’affirmations interdites et budget de 400-800 mots, plafond 1 200 mots
  par défaut pour le texte effectivement chargé ; budget utilisateur prioritaire.
- Les gardes de l’hôte restent identiques dans les deux variantes ; les tests
  structurels et la revue de scénarios ne deviennent pas essais métier réussis.
