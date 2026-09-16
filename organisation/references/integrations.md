# Contrats d'intégration

## Architecture prévue

Organisation assure l'entrée et la coordination. New Pro Brain porte la réflexion stratégique et l'architecture au-dessus des parcours projet, sans second routeur concurrent. New Pro concerne les projets professionnels, produits, services et marques ; New Site les sites et expériences web ; New App les applications. Business est une couche transverse de benchmark, viabilité et business plan.

Ces responsabilités sont les contrats souhaités, pas une déclaration de disponibilité ou de capacité des skills portant des noms proches.

## Inventaire du poste de référence, vérifié le 16 septembre 2026

Cet inventaire décrit une installation locale observée, pas tous les utilisateurs du dépôt. Les chemins sont rendus portables avec `$HOME`, à résoudre dans l’environnement actif. La présence d’un skill tel que `newsite` dans ce dépôt ne prouve pas son installation dans Codex.

Sources : catalogue de skills fourni par cette session ; recherche des noms et métadonnées dans `$HOME/.agents/skills` et `$HOME/.codex/skills` ; lecture complète des deux SKILL.md pertinents et des règles de décision et profils de `newpro`. Aucune version antérieure d'`organisation` détectée dans ces racines. Le catalogue inclut aussi les skills de plugins, sans correspondance exacte pour les quatre parcours absents ci-dessous. Ne pas généraliser cet inventaire aux autres PC ; le revérifier avant usage si le contexte change.

| Parcours souhaité | Observation locale | Contrat utilisable et limite |
| --- | --- | --- |
| New Pro Brain | Absent sous ce nom. `brain` installé à `$HOME/.agents/skills/brain/SKILL.md`. | New Pro Brain : **disponible après installation**. `brain` est une méthode de raisonnement et de qualité généraliste, pas un architecte de projet ni un routeur. Peut aider ASTRA si utile, avec ses contrôles proportionnés, sans être présenté comme New Pro Brain. |
| New Pro | `newpro` installé à `$HOME/.agents/skills/newpro/SKILL.md`. | Raccordement vérifié pour son périmètre réel : bootstrap prudent d'un socle MASTER, profils software/artistic/hybrid, inspection, décisions, risques, backlog, acceptation et validation. Il prépare une tranche verticale et ne lance pas la production. Ce n'est pas une garantie de toutes les fonctions professionnelles souhaitées. |
| New Site | Aucun skill correspondant détecté. | **Disponible après installation**. Ne pas renommer implicitement un skill web ou Sites en New Site. |
| New App | Aucun skill correspondant détecté. | **Disponible après installation**. Organisation peut cadrer puis utiliser des capacités techniques réelles, sans annoncer New App. |
| Business | Aucun skill correspondant détecté. | **Disponible après installation**. Les skills de marketing ou de pricing présents ne constituent pas Business ; ne pas simuler son analyse ou un avis favorable. |

Un raccordement « vérifié » ci-dessus signifie instructions lues et contrat examiné ; aucune opération de `newpro` ou de `brain` sur un vrai projet n'a été exécutée pendant l'installation.

## Respecter les skills observés

Pour `newpro`, lire son SKILL.md réel puis ses références pertinentes. Ses règles lues comprennent `references/DECISION_RULES.md` et `references/PROJECT_TYPES.md`. L'inspection, le dry-run du bootstrap et le validateur sont ses contrôles propres ; résoudre les scripts depuis son répertoire. Ne pas reproduire ses templates ni contourner son adoption explicite d'un dossier existant. Respecter la validation du plan demandée par ce skill en tenant compte des autorisations déjà données. Si un MASTER existe, le réutiliser ; une reprise ou un audit ne justifie pas la création d'un sibling MASTER. Aucun lancement de production par ce raccordement.

Pour `brain`, conserver le rôle limité d'aide au raisonnement : vérification des prémisses, incertitudes, complétude et contrôle final. Son déclencheur est très large ; cela ne doit pas alourdir une faute ou remplacer les critères de routage d'Organisation. Sa propre méthode prévoit une version proportionnée. Son nom n'est pas la preuve d'une intégration New Pro Brain.

Écarts signalés : le New Pro souhaité est plus large que `newpro` installé ; New Pro Brain et `brain` ne sont pas équivalents. Le contrat générique ne peut pas donner à un skill des responsabilités qu'il ne prévoit pas. Aucun autre skill n'est réécrit par Organisation.

## Contrat d'appel commun

1. Chercher le skill exact dans le catalogue disponible, puis dans les seules racines pertinentes si nécessaire. Ne pas supposer sa présence d'après ce document.
2. Lire ses instructions réelles avant appel. Transmettre objectif, périmètre autorisé, contexte et décisions utiles, critères d'acceptation et livrable attendu. Charger uniquement ses références nécessaires.
3. Garder une chaîne courte : Organisation → skill spécialisé → restitution à Organisation. Transmettre la consigne de ne pas relancer une orchestration identique et détecter les cycles.
4. Examiner le résultat et ses preuves ; intégrer aux documents existants autorisés. Une absence ou une incompatibilité reste explicite. Organisation demeure utilisable seul pour les parties réalisables, en indiquant les limites.

## Business : déclencheurs et décisions

Solliciter le véritable Business avant un engagement important pour tout nouveau projet explicitement monétisé, pour une demande d'audit économique et pour un changement majeur de cible, prix ou modèle économique. Pas de Business systématique sur faute, backlog ou petit bug.

Sur un projet existant, transmettre décisions passées, produit actuel, preuves commerciales et coûts restant à engager, avec leurs sources et dates. Ne pas recommencer de zéro ni effacer l'historique. Si Business est installé ultérieurement, lire ses critères, ses formats et ses fichiers effectifs ; le présent contrat ne s'y substitue pas.

Séparer étude documentaire, hypothèses et validation commerciale. Les issues possibles comprennent : tester une hypothèse, pivoter, lancer un pilote, avancer par étapes, arrêter la version actuelle ou chercher une information manquante. Toute décision doit citer ses preuves et limites. Un feu vert économique n'autorise ni dépense ni action externe.

En l'absence de Business, marquer « disponible après installation ». Signaler qu'aucune analyse Business n'a été exécutée et qu'aucune validation commerciale n'est établie. Cadrer les inconnues et collecter les éléments autorisés ; ne pas engager une réalisation importante en prétendant que cette étape est remplie. Présenter le choix utile à l'utilisateur si son absence bloque la suite. Ne pas installer Business de sa propre initiative.
