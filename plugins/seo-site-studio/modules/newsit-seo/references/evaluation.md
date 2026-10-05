# Protocole d'évaluation

1. Valider les métadonnées avec le validateur du skill-creator et les fichiers du package avec `scripts/validate_package.py`. Vérifier les références internes et l'encodage. Ce sont des contrôles de structure.
2. Pour les trois scénarios principaux, exécuter le même prompt avec et sans le skill, dans deux dossiers de sortie isolés. Conception uniquement : aucune publication, dépense, commande réelle ou modification de site externe. Donner le même contexte et les mêmes outils aux deux configurations.
3. Examiner les instructions et les outputs réels. Évaluer chaque assertion à partir d'une preuve dans le texte/fichier. Un simple mot présent ne vaut pas respect d'une architecture ou intégrité d'un paiement. Ne pas confondre assertion facile et amélioration causée par le skill.
4. Conserver prompt, conditions, sorties et jugement. Marquer les cas non exécutés. Les durées/tokens ne sont rapportés que si l'hôte les fournit ; ne pas inventer ces mesures.
5. Montrer les résultats avec le viewer du skill-creator si adapté, sinon fournir un résumé reviewable. Une comparaison sur trois prompts ne mesure pas la qualité des sites livrés en production.

Les scénarios supplémentaires vérifient les frontières. Ils peuvent être exécutés séparément selon le risque. Le type absent doit provoquer la question utile ; le type connu ne doit pas être redemandé. L'architecture imposée doit être gardée ou son conflit signalé, jamais remplacée silencieusement.

Après une correction du skill, refaire les scénarios affectés. Ne pas relancer tout le benchmark sans changement qui le justifie. Respecter les permissions de l'hôte pour la délégation, l'exécution et le stockage.
