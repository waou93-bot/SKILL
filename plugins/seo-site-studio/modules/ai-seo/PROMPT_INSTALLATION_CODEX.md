# Installation dans Codex — à coller dans une session locale

```text
Installe ou mets à jour le skill ai-seo depuis le dossier ai-seo du dépôt
https://github.com/waou93-bot/SKILL, branche main, version attendue 3.0.0.

Lis son README.md, son SKILL.md et scripts/README.md avant exécution.
Récupère le dossier complet à une révision identifiée, sans réinitialiser un clone
qui contient des modifications. Ne crée pas un second skill concurrent.

Détecte la version de Codex, l'utilisateur et l'environnement réel : Windows natif,
WSL ou environnement distant. Vérifie les emplacements de skills reconnus par cette
version, normalement $HOME/.agents/skills pour un usage transversal local.
Ne confonds pas le HOME Windows, le HOME WSL et un conteneur distant.

Recherche ai-seo parmi les emplacements effectivement chargés, ainsi que les anciens
emplacements .codex/skills ou copies de projet qui pourraient créer un doublon.
Compare les personnalisations d'une version existante à la version de référence ;
conserve les ajouts utiles dans le package de migration et signale les conflits.
Sauvegarde intégralement toute copie modifiée hors des dossiers de skills actifs.
Ne modifie aucun projet, MASTER, BUSINESS, SEO ni autre skill pour l'installation.

Exécute les tests du package :
python -m unittest discover -s ai-seo/tests -v

Exécute scripts/install.py en aperçu avec la cible résolue. Relis le diff.
Si la revue est terminée et sans conflit bloquant, applique l'installation ; sur
une cible existante, utilise --apply --upgrade-reviewed. Sur Windows, py -3 peut
remplacer python si c'est l'interpréteur disponible. Ne change pas ExecutionPolicy.

Vérifie les empreintes des fichiers installés, lis le SKILL.md depuis la cible
et vérifie la découverte effective de ai-seo dans Codex. Recharge ou redémarre
Codex si nécessaire. Fais un essai d'invocation sans modifier un projet.

Rends le chemin exact, la version, le commit source, les tests réellement passés,
la sauvegarde et l'état de découverte. Si tu n'as pas accès au PC cible, dis-le :
un push, une copie dans un sandbox ou un plan d'installation ne sont pas une
installation sur mon PC.
```

## Commandes directes après récupération du dépôt

Depuis la racine du dépôt ; adapter la cible seulement après détection :

```text
python ai-seo/scripts/install.py
python ai-seo/scripts/install.py --apply
```

Mise à jour d'une copie existante, après comparaison et conservation des personnalisations :

```text
python ai-seo/scripts/install.py --apply --upgrade-reviewed
```

Le script refuse volontairement les liens symboliques. Si l'installation existante utilise
un lien, examiner la cible et choisir une migration explicite ; ne pas remplacer le lien
aveuglément. L'installation est propre à chaque environnement/ordinateur. Le skill fonctionne
sans Python pour ses instructions ; seuls les utilitaires et ces tests nécessitent Python.
