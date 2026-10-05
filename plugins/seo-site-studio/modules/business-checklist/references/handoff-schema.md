# Contrat de transmission 2.0 — guide de remplissage

Le JSON de référence est `assets/05-decision-handoff.json` (depuis la racine du skill).
Les scripts n’exécutent ni paiement, ni publication, ni génération de prévisions.

## Modèle vierge et évaluation

`kind: TEMPLATE` : aucune décision ni permission ; les valeurs restent inconnues.
`kind: ASSESSMENT` : renseigner run_id, project_id, as_of ISO YYYY-MM-DD, mode,
entrypoint, décision, justification et référence de checklist. Le nom d’un fichier
ne prouve pas que son contenu a été vérifié. Lire les preuves avant de les qualifier.

## Une preuve

Chaque entrée de evidence contient :
- id unique, claim décrivant exactement l’affirmation ;
- type : FAIT_SOURCE / OBSERVATION_TERRAIN / CALCUL / HYPOTHESE / INCONNU ;
- verified booléen, source_ref vers la trace réelle, observed_at au format date ISO ;
- relevance : PROJET / EXTERNE / METHODE ;
- compléter utilement population, période des données, méthode, limites, formule
  et IDs des entrées pour les calculs. observed_at n’est pas nécessairement la
  date de publication d’un document ; les deux doivent rester distinguées.

Une observation terrain de concurrent peut éclairer, mais ne devient pas une
observation du projet. Un entretien simulé par IA reste une hypothèse ou une
préparation de test, pas une observation terrain vérifiée.

## Six gates

IDs G1..G6 exactement, result parmi NON_EVALUE, FAVORABLE, DEFAVORABLE,
NON_CONCLUANT, NON_APPLICABLE ; criticité booléenne ; justification et evidence_ids.
Un résultat favorable/défavorable exige des preuves référencées. La force et la
suffisance de ces preuves relèvent de la revue, pas d’un comptage automatique.

## Prochain engagement et permissions

next_step : scope, cash et heures maximums (réels et non négatifs), owner,
review_date ou review_trigger, budget_evidence_ref. `null` n’est pas 0.
permissions : granted_actions, approval_ref et plafonds effectivement accordés.
Une recommandation GO non autorisée est possible ; elle ne permet pas l’exécution.
Vérifier la validité actuelle et la portée de tout accord dans l’hôte réel.

## Finances et SEO

finance.status : NON_MODELISE / PARAMETRIQUE / CHIFFRE / RECONCILIE.
Tout modèle déclaré possède model_ref ; RECONCILIE exige checks_ref.
without_unsecured_funding_reviewed reflète le contrôle réellement effectué.
Un lancement progressif exige un modèle chiffré, pas une case de budget isolée.

seo.status : NON_SOLLICITE / ABSENT / PRESENT_NON_EXECUTE / EXECUTE_AVEC_TRACE.
Une exécution déclarée exige une trace et un contrôle des doubles comptes budgétaires.
L’absence de SEO ou d’Organisation n’est pas un blocage du skill.

## Checklist et validation

Le JSON de checklist partage project_id, run_id et as_of avec le handoff. Un statut
ETAYE référence ses preuves ; les contrôles critiques non résolus interdisent un
GO dans la vérification croisée. Les contrôles non pertinents sont explicitement
non critiques et leur non-applicabilité est justifiée.

Exécuter `scripts/check_handoff.py` avec --checklist pour ces contrôles croisés.
Les liens, IDs, booléens et bornes ne prouvent ni authenticité des données, ni
conformité juridique, ni résultats futurs. Aucun GO produit par un programme n’est
un substitut à l’arbitrage de l’utilisateur ou à ses autorisations.
