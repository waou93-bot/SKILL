# SEO STUDIO 2 — package 3.0.0

Créé le 8 octobre 2026. Ce package transforme une niche et un type de site en dossier
de préproduction puis en site local réalisé et vérifié quand sa création est demandée.
Il comporte les instructions, des playbooks, les mandats
métiers, une bibliothèque de patterns observés, des contrats JSON, des scripts locaux
et leurs tests. Il ne comporte ni serveur autonome, ni abonnement, ni appel API payant.

## Utilisation

Après installation dans un emplacement reconnu par l'hôte :

```text
$seo-studio-2
Niche : [ta niche]
Type de site : [média affilié, comparateur, vitrine, e-commerce, SaaS, annuaire…]
Construis toute la préproduction. Applique le contrat strict, forme les rôles avec
le vrai /personna, confronte les livrables et fais arbitrer les désaccords par Astra.
Réutilise le contexte du projet. Ne publie rien.
```

Dans une interface utilisant `@`, sélectionner le skill s'il est effectivement
présent ; la syntaxe d'invocation dépend de l'hôte. Une mention textuelle n'installe
pas le package. Voir la source officielle S16 dans `research/sources.json`.

## Ce qui est livré à chaque futur projet

Un cadrage sourcé, la place du canal SEO, les parcours et le positionnement, un
Project Skin, l'architecture de contenu et technique, un plan de maillage au niveau
des pages, les briefs et contenus pilotes, des encarts et offres partenaires adaptés,
un plan de mesure, une roadmap dépendante, les gates et le dossier de transfert.
Le détail et les critères sont dans `references/12-deliverables.md`.

Toutes les idées n'ont pas vocation à devenir des pages. Le skill préfère mettre
à jour une page utile plutôt que multiplier les variantes. Il propose aussi de ne
pas acheter ou de ne pas utiliser l'affiliation quand cela sert mieux le projet.

## État réel à la livraison

- Les quatre skills transversaux et les cinq skills SEO identifiés ont été consultés
  dans `waou93-bot/SKILL`, à la révision consignée dans `research/dependencies.json`.
- Quatre domaines de référence ont fourni du contenu exploitable. Garagemalin et
  Doucevenue sont restés inaccessibles dans cet environnement. Ce n'est pas une
  preuve qu'ils sont hors ligne pour les internautes.
- Aucun rendu navigateur des six sites n'a été vérifié ; les constats visuels fins,
  performances, indexation et résultats commerciaux ne sont pas certifiés.
- Le vrai `/personna` n'a pas été localisé dans le catalogue ni dans l'arbre GitHub
  inspectés. Les mandats et entrées de formation sont préparés, pas déclarés exécutés.
- Ce package a été écrit et testé localement. Il ne signifie pas qu'il a été installé
  sur le PC utilisateur, découvert par Codex, poussé sur GitHub ou appliqué à un site.
- Aucune revue multiagent indépendante n'a été exécutée pour sa rédaction. Les tests
  logiciels ne remplacent pas les scénarios comportementaux de `evals/scenarios.json`.

## Installation locale non destructive

Lire `PROMPT_INSTALLATION_CODEX.md`. L'installateur copie seulement ce skill ; il ne
remplace pas Organisation, Design DNA ou les autres dépendances. Aperçu par défaut :

```sh
python scripts/install.py --target-root CHEMIN_DES_SKILLS
python scripts/install.py --target-root CHEMIN_DES_SKILLS --apply
```

L'emplacement utilisateur local documenté pour Codex est `$HOME/.agents/skills`.
Sur Windows, utiliser le véritable profil utilisateur, pas un chemin copié d'une
capture. L'installation refuse un dossier déjà différent : sauvegarder et comparer
avant toute migration ; aucun écrasement automatique. Les doublons d'autres
emplacements sont à traiter après inventaire, pas à supprimer au hasard.

## Vérifications

```sh
python scripts/studio.py check-package .
python -m unittest discover -s tests -v
python scripts/studio.py inventory --root CHEMIN_DES_SKILLS
```

Lire `VALIDATION.md` pour les résultats réellement obtenus. Les scripts fonctionnent
hors ligne avec la bibliothèque standard Python. Ils n'installent pas de dépendance,
ne lancent pas de modèle et n'écrivent jamais sur un CMS.

## Périmètre de la rigueur

Les scripts bloquent des erreurs structurelles, manques de preuves et contradictions
explicites. Ils ne peuvent pas prouver qu'un texte est utile, qu'une source est
interprétée correctement ou qu'un auteur a réellement testé un produit. Ces points
exigent la revue métier et des preuves externes. Aucun prompt ne garantit à lui seul
l'obéissance parfaite d'un modèle ; le package rend les écarts visibles et bloquants.

## Révision 2.3.0 — contrat 2.1

Nouvelle mission : F0 cadrage → F1 recherche → F2 options → F3 décision, puis
préproduction autonome avec au moins deux vrais sous-agents sectoriels. Recherche
LinkedIn/Reddit avant /personna ; profils transmis et calibrés ; quatre cycles réels
proposition/critique/résolution/relecture. Lire references/15 et references/16.

`workflow.json` 1.0 complète `state.json` 2.0 sans renommer R01–R26 ; R27/R28 sont
additionnels. `init` produit des étapes PLANNED et aucune preuve/approbation.
Ancien dossier : aucune réinitialisation ; draft reste lisible, handoff demande les
nouveaux registres/preuves. `snapshot` n'approuve rien et inclut l'empreinte des
entrées de recherche/formation. Les preuves runtime restent à contrôler sur l'hôte.

## Créer le site de bout en bout

```text
$seo-studio-2
Niche : [niche]
Type de site : [type]
Crée le site complet et son corpus V1 jusqu'au résultat local vérifiable.
Conserve le vrai /personna. Aucun framework d'agents externe ni outil payant obligatoire.
Recherche interne sur toutes les pages de contenu sauf landing.
Intègre les liens pertinents aux mots/expressions du corps des articles.
Ne publie rien sans autorisation.
```

Voir `references/18-realisation-complete.md`. Les skills locaux sont conservés.
Le moteur d'inférence reste celui de l'hôte ; le package ne fournit pas de modèle.
