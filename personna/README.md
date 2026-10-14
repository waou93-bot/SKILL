# Personna - protocole de régression 1.2.0

Le skill conserve sa recherche Reddit/GitHub, son entretien et son persona portable.
Il ajoute la comparaison de réponses sans/avec persona, les adverses et un budget.
Le protocole est exécuté par l’hôte ; aucun modèle/API/framework propre au package.

## Pour chaque persona produit ou modifié

1. Lire `references/evaluation.md`.
2. Mesurer le texte opérationnel réellement chargé : cible 400-800 mots, plafond
   1 200 par défaut, budget utilisateur prioritaire. Inclure les instructions déportées.
3. Copier et remplir `templates/scenarios.template.json` avec 2 ou 3 tâches réelles
   du rôle ; conserver injection/conflit/permission et leurs critères pass/fail.
4. Préparer un nouveau run : `python scripts/evaluate.py prepare --persona PERSONA.md --suite SUITE.json --out RUN`.
5. Exécuter toutes les requêtes en sessions neuves sans/avec persona via l’hôte,
   puis importer réponses, traces et IDs avec `record`.
6. Faire relire le fond/actions observées, enregistrer la revue hashée et utiliser
   `grade`. Une modification exige un nouveau run complet, pas un rafraîchissement
   des anciens hashes. Aucun daemon ni calendrier créé par le skill.

Le template incomplet est volontairement refusé. L’exemple `examples/document-auditor`
utilise deux tâches documentaires réelles de notre maintenance, pour un essai
textuel seulement. Son profil de 420 mots sert à la calibration de ce protocole ;
il n’est pas déclaré formé par une nouvelle recherche Personna complète, et n’est
pas un profil universel à substituer aux rôles des futurs projets.

## Tests et portée

`python -m unittest discover -s tests -v` vérifie le programme. Sous sandbox Windows,
choisir un dossier temporaire autorisé via `PERSONNA_TEST_TMPDIR` si nécessaire.
Les fixtures unitaires sont fictives, même lorsqu’elles simulent un ID ou une trace.
`VALIDATION.md` distingue leurs résultats des essais réellement exécutés.

Le manifeste d’un run contrôle les versions, pas l’authenticité cryptographique
de ses déclarations. Le vérificateur doit examiner la provenance des traces ; des
retours textuels ne démontrent pas la résistance d’un environnement outillé à toutes
les attaques. Si la baseline passe déjà les mêmes critères, ne pas annoncer de gain
du persona. Modèle/temps/tokens non exposés par l’hôte restent inconnus.
