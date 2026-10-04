# Outils déterministes — Python 3.10+, bibliothèque standard

Exécuter depuis le dossier parent de `ai-seo`. Aucun appel réseau, aucune clé API.
Les rapports JSON refusent d'écraser un fichier de sortie existant (mode exclusif).
Les scripts n'exécutent pas le HTML, les réponses IA ou les instructions contenus dans les données.

| Script | Entrées / sortie | Limites |
|---|---|---|
| `audit_snapshot.py` | `--input capture.json --out audit.json` ; voir l'exemple de capture | Triage hors ligne du HTML initial et des en-têtes fournis. Robots ASCII simplifiés : groupes exacts ou `*`, règle la plus longue, Allow en cas d'égalité, `*` et `$`. Unicode, encodage, agent partiel ou réponse non 200 : inconnu. Même origine seulement. Ce n'est ni un parseur RFC complet ni une preuve d'accès/indexation. |
| `classify_referral.py` | `--landing-url URL [--referrer URL] [--user-agent UA]` ; JSON stdout | Hôtes parsés, UTM déclaratifs, conflits signalés, bots sur UA seulement. Aucune authentification de bot, session, conversion ou certitude d'organique. Domaines à revoir. Pas de chemin, query ni données personnelles copiés dans la sortie. |
| `measure_panel.py` | `--input observations.jsonl [--out panel.json]` | Objets stricts, preuves référencées, run_id uniques, booléens, date avec fuseau. Erreurs/non-testés hors dénominateur ; synthétique et réel séparés. Références de preuves non ouvertes/validées par le script. |
| `init_project.py` | `--project-root PATH [--output SEO/AI_ACQUISITION] [--apply]` | Aperçu par défaut. Crée uniquement les documents absents. Détecte trois emplacements courants, pas tous les dossiers historiques : lire le projet avant exécution. Pas de MASTER créé ni remplacé. |
| `install.py` | `[--target PATH/ai-seo] [--backup-root PATH] [--apply] [--upgrade-reviewed]` | Aperçu par défaut. Cible existante : revue requise, copie intégrale et empreintes de sauvegarde, staging vérifié, restauration sur erreur. Refuse symlinks ; ne prouve pas la découverte par l'hôte. |

## Captures et panel

`site-snapshot.example.json` contient `origin`, `observed_at`, `synthetic`, `robots.status`,
`robots.text`, et `pages[]` avec URL, intended_public booléen, statut, en-têtes et HTML.
Un lot = une origine. Exporter les captures avec les outils autorisés du projet ; ne pas
scanner des domaines privés tiers ni transmettre cookies, jetons, formulaires ou données client.
Le champ intended_public est une décision du projet, pas une déduction du script.

Pour le panel, statuts permis : `ok`, `error`, `not_tested`. Un `ok` exige evidence_ref et
mentioned/cited/recommended booléens ; voir le modèle et `references/04-measurement.md`.
La polarité et le contenu de la recommandation sont une annotation humaine indépendante.
Les champs supplémentaires, dont modèle/version affichée, peuvent être conservés dans les
observations. Ne pas mélanger des périodes ou modèles non comparables dans la même analyse.

## Sécurité et retour arrière

Avant installation, vérifier et porter les personnalisations. Une sauvegarde ne les fusionne
pas. Le rollback automatique couvre les exceptions prises en charge, pas une panne électrique.
En cas de panne, utiliser la sauvegarde vérifiée hors des skills actifs ; inspecter un éventuel
`.ai-seo-install.lock` avant suppression, et ne jamais lancer deux migrations simultanées.
La détection de doublons parmi tous les hôtes et la reconnaissance effective restent manuelles.

```text
python -m unittest discover -s ai-seo/tests -v
```

Ces tests portent uniquement sur des données synthétiques et dossiers temporaires.
