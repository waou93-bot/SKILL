# Outils locaux — Python 3.10+

Aucune dépendance externe, aucun réseau, aucun appel de modèle, aucune écriture CMS.
Les fichiers attendus sont en UTF-8. Les chemins de preuve sont relatifs au dossier
projet, avec `/` ; les chemins absolus, remontées `..` et liens symboliques sont refusés.
Le validateur rejette également les clés JSON dupliquées et les valeurs NaN/Infinity.

## Inventorier

```sh
python scripts/studio.py inventory --root CHEMIN_SKILLS --root AUTRE_EMPLACEMENT
```

Lecture seule. Détecte noms contenant SEO, candidats par description, socle transversal,
personna/persona et doublons. Ne suit pas les symlinks : fournir leur chemin réel
explicitement autorisé. Les emplacements non lus restent dans `skipped`, jamais
considérés vides. La sortie ne prouve ni lecture intellectuelle, ni installation,
ni découverte du skill par Codex. Consigner l'inventaire réel dans `state.json`.

Le groupe QUALITY inclut aussi les compétences QA, sécurité, performance et rédaction
requises même sans SEO dans leur description. Le transfert strict exige leur lecture
avec provenance. Ajouter ces entrées lors d'une reprise ancienne, sans réinitialiser
le dossier ni fabriquer les preuves ; leur application métier reste conditionnelle.

## Initialiser sans écraser

```sh
python scripts/studio.py init --project CHEMIN/SEO/PREPROD --niche "Niche" --site-type "Type"
python scripts/studio.py init --project CHEMIN/SEO/PREPROD --niche "Niche" --site-type "Type" --apply
```

La première commande n'écrit rien. La seconde crée les documents et `state.json`.
Un projet identique existant n'est pas réécrit. Un contexte différent ou des fichiers
préexistants sans état coherent bloquent la création et demandent une reprise ciblée.
Les documents contiennent des marqueurs A_COMPLETER ; ils ne passent pas le transfert.

## Constituer les preuves

Après le travail réel : enregistrer les notes/captures/logs autorisés dans le dossier
projet, calculer leur SHA-256 et les référencer dans `evidence`. Enregistrer les
lectures de dépendances, formations /personna et retours de sessions réelles. Les
empreintes Git de blobs ne sont pas des SHA-256 de fichiers : conserver le type de
preuve correct. Les preuves d'essai revendiqué portent `kind: test_report`.

Les artefacts relus ont une preuve `kind: artifact` sur leur propre chemin. Les
exigences, gates et retours référencent des IDs de preuve existants. Une source web
observée a une URL, une date et une note/trace locale. Un domaine inaccessible reste
NOT_OBSERVED ; il ne peut pas servir à soutenir un fait.

## Prendre un instantané de relecture

```sh
python scripts/studio.py snapshot CHEMIN/SEO/PREPROD
```

Cette commande lit les fichiers et retourne `inputs_sha256` et `reviewed_artifacts`.
Elle n'effectue **aucune revue**. Après une vraie revue, enregistrer les champs de
l'instantané qui correspondent à la version examinée, avec trace d'exécution,
auteur, critique, sujet et conclusion. Ne pas réactualiser les hashes pour masquer
une absence de nouvelle revue. Les changements des entrées métier ou des fichiers
examinés rendent les anciennes approbations invalides.

## Valider

```sh
python scripts/studio.py validate CHEMIN/SEO/PREPROD --stage draft
python scripts/studio.py validate CHEMIN/SEO/PREPROD --stage handoff
python scripts/studio.py validate CHEMIN/SEO/PREPROD --stage release
```

`draft` tolère le travail incomplet, mais pas des incohérences renseignées. `handoff`
exige G0–G5, preuves, formation, revues indépendantes déclarées, briefs, pilotes et
graphe cohérent. `release` ajoute G6, permission, preuve de cette permission et
preuve live HTTP/navigateur déclarée ; il ne fait aucun test réseau lui-même.
Code de sortie 0 : contrat structurel satisfait. Code 2 : erreur ou blocage.

Le schéma accepte des paramètres d'URL stables lorsque le projet les prévoit.
Il ne remplace pas la politique de filtrage, pagination ou langues à définir avec
les skills SEO. Le validateur ne mesure ni mots-clés, ni rang, ni taux de conversion.

Une exception au nombre de pilotes exige une décision Astra résolue de scope
`pilot_scope`, une raison explicite et au moins un pilote. Une exigence optionnelle
NON_APPLICABLE exige une décision Astra dont le scope est exactement son ID. Les
exigences obligatoires ne se désactivent pas ainsi. Ne pas désactiver l'exigence de
revue indépendante par un simple booléen.

## Installer et contrôler le package

```sh
python scripts/studio.py check-package CHEMIN_DU_PACKAGE
python scripts/install.py --target-root CHEMIN_SKILLS
python scripts/install.py --target-root CHEMIN_SKILLS --apply
```

Le manifeste vérifie l'intégrité, pas l'identité cryptographiquement signée de l'auteur.
L'installation prépare une copie temporaire, la vérifie et refuse une destination
différente existante. Elle ne modifie aucune dépendance, configuration globale ou
projet. Un simple test dans un dossier temporaire n'installe rien sur le PC utilisateur.

## Tests et limites

```sh
python -m unittest discover -s tests -v
```

Les fixtures positives contiennent délibérément des traces fictives : elles testent
le schéma, pas l'authenticité. Le résultat s'appelle STRUCTURE_OK, pas « agents formés »
ou « site validé ». Les scénarios `evals/scenarios.json` nécessitent un vrai hôte
avec les dépendances et ne sont pas exécutés par unittest.

## Workflow et compatibilité

Le validateur lit le compagnon `workflow.json` défini par
`schemas/workflow.schema.json`. Il contrôle F0–F3, sources OBSERVED des deux
plateformes, compétences liées aux rôles, profils/mandats/hash, au moins deux
délégués, ordre des cycles et relectures. Il n'effectue aucun appel d'agent ou réseau.
Un ancien brouillon sans compagnon retourne un avertissement ; handoff/release
restent bloqués. Compléter manuellement depuis les templates sans inventer de
preuves ni réinitialiser. Les nouvelles exigences sont R27/R28.

## Contrôle natif d'un site HTML réalisé

`python scripts/site_check.py CHEMIN_EXPORT --landing-route /` contrôle hors réseau
le HTML, title/meta, liens/fragments, ressources, alt et recherche sur chaque page
hors landing explicitement déclarée. `--public-base` confronte les canonical.
LOCAL_HTML_OK n'est ni une recette navigateur ni une preuve d'indexation.
Voir `references/18-realisation-complete.md` pour le parcours D0–D5.
