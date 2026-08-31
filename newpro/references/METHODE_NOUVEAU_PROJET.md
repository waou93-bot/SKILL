# Methode de creation d'un nouveau projet

## Note de provenance

Cette V1 reprend la methode fournie dans la conversation referencee : un MASTER isole, des sources de verite, un cadrage avant production, des registres de decisions et rejets, puis une tranche verticale validee. Le PDF indique dans la demande n'etait pas accessible dans l'environnement de fabrication ; cette reference est donc une transcription operationnelle de la methode visible dans le contexte, et doit etre comparee au PDF original lorsqu'il sera disponible.

## Principe directeur

Le projet commence par son socle de verite, pas par la production. Le MASTER reunit le contexte, les choix valides, les incertitudes, les assets, le backlog et les criteres qui permettront de savoir si la premiere tranche a reussi.

## Sequence recommandee

1. Isoler le projet dans un dossier `[NOM] - MASTER`.
2. Inspecter le dossier, la conversation et les sources existantes.
3. Distinguer les faits, decisions, hypotheses, propositions, rejets et inconnues.
4. Creer les sources de verite et les registres avant les livrables.
5. Classifier le projet et adapter la structure aux risques dominants.
6. Formuler une tranche verticale representative, avec inclus, exclus, preuves et risques testes.
7. Faire valider le Master Brief et la tranche verticale.
8. Demarrer ensuite une mission delimitee, avec retour des decisions et preuves dans le MASTER.

## Sources de verite

- `00_MASTER_BRIEF.md` : pourquoi, pour qui, perimetre et etat.
- `01_REGISTRE_DES_DECISIONS.md` : decisions validees et leurs impacts.
- `02_REGISTRE_DES_REJETS.md` : options ecartees et raisons.
- `03_INVENTAIRE_DES_ASSETS.md` : ressources, provenance et statut.
- `04_BACKLOG_PRIORISE.md` : travail ordonne par valeur et risque.
- `05_CRITERES_D_ACCEPTATION.md` : preuves observables de reussite.
- `06_RISQUES_ET_INCERTITUDES.md` : ce qui manque ou peut faire echouer la tranche.
- documents de profil : architecture/conventions ou direction artistique/bible des assets.

## Tranche verticale

Une tranche verticale relie un parcours ou un artefact complet a une preuve de valeur. Elle doit tester un cas representative de la realite, pas seulement produire un morceau isole.

Elle explicite :

- le resultat attendu ;
- le perimetre inclus ;
- le perimetre exclu ;
- les risques testes ;
- les criteres d'acceptation ;
- les preuves a conserver ;
- les conditions de poursuite, de correction ou d'arret.

## Limites

Le MASTER ne decide pas seul de la vision, du budget, du business model, d'une technologie irreversibile, d'une contrainte juridique ou d'un changement majeur de direction. Il prepare l'arbitrage et conserve sa trace.
