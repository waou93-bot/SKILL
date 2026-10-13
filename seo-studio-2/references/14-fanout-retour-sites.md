# Couverture fan-out et retour des quatre sites

Lire à G1/G2 pour cartographier la couverture, à G3 pour les briefs et à G4/G5 pour
la recette. Une reprise ciblée conserve l'orchestration et ses décisions existantes.

## Contrat commun et dépendances

Utiliser [le contrat de fan-out ai-seo](../../ai-seo/references/query-fanout.md) et son
[retour d'expérience daté](../../ai-seo/references/four-sites-feedback.md), après
vérification de leur présence dans le catalogue. ai-seo fait déjà partie du socle
SEO découvert par le Studio ; ne pas le remplacer par un skill fictif. Si absent,
signaler la limite et préparer la matrice décrite ici sans prétendre l'avoir exécuté.

Le mécanisme possible décrit par Google n'est ni une recette de classement ni une
liste connue de sous-requêtes. Les branches éditoriales restent des hypothèses sauf
preuve observée. Aucun quota de questions, de pages, de mots ou de FAQ n'en découle.

## G1/G2 : questions, propriété et frontières

Partir de la décision utilisateur et de l'inventaire actuel. Pour chaque page V1
prioritaire, produire la matrice : question principale, public/contrainte,
sous-question, provenance et preuve, URL/section actuelle, URL propriétaire prévue,
réponse/preuve/limite, décision, frontières d'intention, liens et action suivante.
L'inscrire dans `03_ARCHITECTURE.md` ou `05_CONTENU.md` ; réutiliser une matrice
existante. Le [modèle CSV](../../ai-seo/templates/fanout-map.csv) est optionnel.

Décider conserver, enrichir une section, lier une page existante, créer pour une
tâche distincte, exclure ou bloquer faute de preuve. Une page par formulation de
requête est injustifiée. Sur un réseau, attribuer la tâche au domaine adapté et
lier pour une prochaine action pertinente ; ne pas multiplier les guides identiques.
Conserver les contenus utiles et URLs quand une nouvelle hiérarchie de hubs suffit.

États de réponse : REPOND/PARTIEL/ABSENT/NON_VERIFIE pour des pages inspectées ;
A_PRODUIRE pour la préproduction. Ne pas déclarer une page future auditable en live.
Les champs « observé » exigent une source effectivement lue, sans faux volume GSC.

## G3 : écrire la réponse et son paquet SEO

Le brief précise la réponse attendue de chaque branche, sa section, ses conditions,
sources, limites et prochaine étape. Charger `redaction-editoriale-web` avant la
rédaction effective. La matrice est une spécification, pas un contenu livré.

Title/H1 décrivent la décision principale, la description résume la réponse présente
sans accumuler toutes les branches. Un plafond de longueur peut relever du projet ;
ne pas transformer une convention de l'un des quatre sites en règle Google.
Comparer une proposition au corps réel et conserver les valeurs avant/après utiles.

Distinction obligatoire pour les affirmations : fiche fabricant, comparaison
documentaire, essai réel, hypothèse et inconnue. Écarter les promesses de confort,
bruit, compatibilité ou autonomie sans preuve appropriée. Les dates de consultation
des sources, révision de l'article et publication restent séparées.

Un guide reçoit des liens contextuels entrants depuis le corpus et sortants vers
prérequis, alternative ou action, lorsque pertinents. Tester la relation livrée,
pas seulement sa présence dans le brief ; inspecter le rendu des filtres/fragments.

## G4/G5 : technique, mesure et transfert

Pour chaque route publique, préparer la comparaison HTTP/destination finale,
canonical, robots/indexabilité, sitemap, contenu, médias et schema applicable.
Déclarer ce qui est spécifié, testé en local, testé en preview ou vérifié en production.

Sur l'existant, le transfert identifie source de vérité, branche/commit ou artefact,
version publique et routes à préserver. Aucune copie ancienne ne remplace un site
qui contient des pages plus récentes. Vérifier les conflits par site, sans bloquer
les actions indépendantes sur les autres domaines.

Pour lastmod/dateModified : modification significative, provenance et correspondance
au contenu public. Le dernier commit ne suffit pas sans vérification du diff ; ne
pas reprendre la date du build ou d'une restauration faute de provenance. Omettre
les dates optionnelles inconnues. Vérifier images informatives/décoratives au rendu,
cohérence du schema et relation commerciale réelle des liens, même hors réseau visible.

Le panel IA relie questions, pages, affirmations et citations observées. Fixer les
conditions, dates effectives, dénominateurs, événements et limites. Une hausse de
compteurs ou un taux de couverture local ne valide ni causalité ni acquisition.
Sans données suffisantes, conserver NON_CONCLUANT et définir la prochaine observation.

## Exigences existantes, sans réinitialisation

R09 porte la propriété des intentions/branches ; R10 leurs liens ; R13 les briefs
et réponses ; R17 les preuves ; R20 la recette/version/dates ; R21 le panel IA si
pertinent ; R22 la mesure et ses limites. Ajouter les contraintes précises du mandat
au registre courant, sans changer ses IDs ni valider de nouveau toutes les phases.
Une reprise en 2.1 peut compléter ces preuves sans recréer `state.json`.

G2 examine les frontières, propriétaires et parcours ; G3 le contenu effectivement
livré ; G5 l'état réel de chaque correction. Une liste de mots-clés dans les metas
ou des branches toutes NON_VERIFIE ne suffisent pas à déclarer cette couverture prête.
La validation structurelle ne lit pas les réponses pour juger leur utilité : prévoir
la revue éditoriale et les contrôles rendus adaptés à la mission autorisée.
