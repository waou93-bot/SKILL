# ai-seo 3.0.0 — canal d'acquisition par les IA

Skill générique et technique pour ChatGPT Search et les autres moteurs/agents IA, utilisable sur un site existant, un chantier en cours ou un pré-lancement. Le même nom `ai-seo` est conservé pour éviter un doublon avec l'ancien skill du dépôt.

## Ce que le skill fait

Cadrage du canal, baseline de visibilité, audit HTML/HTTP/robots/WAF, contenu orienté décision, données structurées, lisibilité pour agents, réputation légitime, mesure des citations/recommandations et conversions disponibles. Il prépare et réalise les changements autorisés dans la stack du projet, sans la remplacer par défaut.

Il ne garantit aucune recommandation. Les extensions comme llms.txt ne remplacent pas le contenu, les preuves, l'accès et le SEO. Les politiques de recherche et d'entraînement sont séparées. La distinction citation/recommandation est conservée et renforcée.

## Utilisation dans Codex

Installer le dossier COMPLET `ai-seo`, pas seulement SKILL.md. Lire [PROMPT_INSTALLATION_CODEX.md](PROMPT_INSTALLATION_CODEX.md). Codex documente les dossiers `.agents/skills` du projet et `$HOME/.agents/skills` pour les skills locaux ; vérifier la version et l'environnement réellement utilisés. La copie GitHub, l'installation locale et la reconnaissance par l'hôte sont trois états différents. [Documentation officielle](https://learn.chatgpt.com/docs/build-skills).

Exemple après installation :

```text
$ai-seo Analyse ce projet existant pour construire le canal d'acquisition
ChatGPT et moteurs IA. Lis d'abord le contexte, le code et le dossier SEO.
Établis une baseline, corrige les blocages locaux autorisés et prépare la mesure.
Préserve ma DA, mes URLs et mes données. Aucun déploiement sans autorisation.
```

Un audit seul reste en lecture seule. Le skill n'exige pas Organisation, Business ou un accès payant aux moteurs. Si ces capacités existent, il les coordonne sans créer de substituts.

## Scripts et tests

Python 3.10+ ; bibliothèque standard. Depuis le parent de `ai-seo` :

```text
python -m unittest discover -s ai-seo/tests -v
python ai-seo/scripts/install.py
```

La seconde commande montre un aperçu ; elle ne copie rien. Après vérification du chemin et des personnalisations, `--apply` réalise l'installation. Une cible existante exige aussi `--upgrade-reviewed` ; ce drapeau ne remplace pas la revue. Une sauvegarde est hors des skills actifs. Pas de modification des politiques PowerShell.

Détails : [scripts/README.md](scripts/README.md), [VALIDATION.md](VALIDATION.md), [sources](references/sources.md).

## Contenu

`SKILL.md` est le point d'entrée. `references/` contient les procédures détaillées ; `templates/` les fichiers à adapter ; `scripts/` cinq utilitaires ; `tests/` les tests synthétiques ; `evals/` les scénarios à exécuter dans l'hôte ; `agents/openai.yaml` les métadonnées facultatives.

## Migration 2.2.0 → 3.0.0

Les anciennes procédures confondant certains robots de recherche et d'entraînement, les gains universels non étayés et l'adoption supposée de fichiers IA sont remplacés. La mesure Google est actualisée : la documentation du 4 octobre 2026 décrit un rapport de performances génératives ; ne pas recopier l'ancienne affirmation d'absence de rapport. Voir les sources et limites précises.

Ancien état conservé dans `backup/ai-seo-before-v3-2026-10-04`, au commit `51fa097c1e6a195008614f2b050086afada4c913`. Le package n'altère aucun autre skill ni projet. La migration locale doit encore comparer les personnalisations éventuelles du PC ; une sauvegarde ne les fusionne pas automatiquement.
