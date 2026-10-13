# Query fan-out — couvrir les questions qui composent une décision

Lire pour un audit de couverture, un enrichissement de page ou un panel de recherche
IA. La méthode sert aussi au SEO classique ; elle ne demande pas de réécrire tout le site.

## Ce qui est documenté et ce qui reste une hypothèse

Google décrit un mécanisme possible d'AI Overviews et d'AI Mode : plusieurs recherches
liées à des sous-thèmes et sources contribuent à une réponse. Cela ne révèle ni toutes
les sous-requêtes d'une réponse donnée ni une recette de classement. Ne pas attribuer
ce fonctionnement exact à ChatGPT, Claude, Copilot ou Perplexity sans source propre.

Une carte éditoriale de fan-out est une **hypothèse de besoins à couvrir**, sauf pour
les questions observées et sourcées. Une citation observée indique la page citée et
l'affirmation qu'elle soutient ; elle ne révèle pas une sous-requête cachée du moteur.
L'indexation et l'éligibilité aux extraits sont nécessaires pour un lien de soutien
dans les fonctions IA Google ; elles ne garantissent pas cette apparition.
Le guide actuel mentionne également l'inclusion du site dans les fonctions IA de
Search Console : contrôler ce réglage en lecture seule lorsque l'accès est disponible.
Ne pas modifier un choix d'exclusion au titre d'un simple audit.

Sources primaires consultées le 13 octobre 2026 :

- [Google — guide actuel de la recherche générative](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- [Google — guide antérieur, encore accessible](https://developers.google.com/search/docs/appearance/ai-features).
- [Titres de résultats](https://developers.google.com/search/docs/appearance/title-link).
- [Extraits et descriptions](https://developers.google.com/search/docs/appearance/snippet).

Reconsulter les sources avant une décision dépendant de leurs fonctionnalités.

## Construire une carte proportionnée

1. Partir d'une décision principale, de son public et de l'inventaire **actuel** des
   pages. Reprendre questions GSC, recherche interne, retours lecteurs, discussions,
   notices et sources métier réellement consultées. Sans accès ou échantillon utile,
   marquer les formulations proposées `HYPOTHESE_EDITORIALE`, sans volume inventé.
2. Explorer uniquement les branches utiles : critères de choix, comparaison,
   contraintes, compatibilité, installation, diagnostic, entretien, coût total,
   alternatives et limites. Adapter cette liste à la décision ; aucun quota de
   branches, mots, FAQ ou articles n'est nécessaire.
3. Pour chaque question, lire la réponse existante et attribuer une URL propriétaire.
   Chercher articles, hubs, tutoriels, outils et sections avant de proposer une création.
   Examiner la réponse complète, pas seulement la présence d'un terme dans un H2.
4. Décider `CONSERVER`, `ENRICHIR_SECTION`, `LIER_EXISTANT`, `CREER_DISTINCT`,
   `HORS_PERIMETRE` ou `BLOQUE_PREUVE`. Créer une URL seulement si la tâche, le contenu,
   les preuves et l'action suivante sont distincts. Expliquer la frontière entre deux
   pages proches ; ne pas déduire une cannibalisation du seul vocabulaire partagé.
5. Rédiger ou spécifier réponse, conditions, exemple, preuve et limite près de la
   question. Une information requise mais inconnue reste visible comme inconnue.
   Charger `redaction-editoriale-web` avant une réécriture effective, s'il est disponible.
6. Relier la branche à une prochaine étape : vérifier une compatibilité, suivre une
   procédure, comparer, consulter une sélection ou agir sans achat. Ajouter des liens
   contextuels entrants et sortants utiles ; éviter un maillage réciproque systématique.

## Contrat de la matrice

Utiliser [le modèle CSV](../templates/fanout-map.csv) ou une table équivalente dans le
dossier SEO existant. Un audit ciblé peut tenir dans une seule table. Les champs utiles :

| Groupe | Champs et fonction |
|---|---|
| Périmètre | site, langue, environnement/version, date, couverture et limites |
| Besoin | ID, question principale, public/contrainte, sous-question, provenance observée ou hypothèse, preuve de cette provenance |
| Propriété | URL existante inspectée, URL propriétaire prévue, section/ancre, frontière avec pages proches |
| Réponse | extrait ou résumé réel, état `REPOND` / `PARTIEL` / `ABSENT` / `NON_VERIFIE`, preuve factuelle et limite |
| Décision | action proposée, raison, title/H1/meta concernés ou inchangés, statut de réalisation |
| Parcours | lien entrant, lien sortant, ancre/emplacement, prochaine action et événement si mesurable |
| Livraison | priorité, responsable, dépendance, critère de recette et rollback |

Séparer état de couverture et statut de travail : une réponse absente peut être
seulement proposée ; une réponse locale n'est pas une réponse publiée. Pour un site
futur, écrire `A_PRODUIRE` et des critères, pas `REPOND` ou « audit réussi ».
`ABSENT` exige une inspection de la page ; sinon conserver `NON_VERIFIE`.

## Contrôle éditorial et métadonnées

- La réponse respecte une intention principale et traite ses sous-questions utiles.
  Des sections précises, critères, tableaux ou procédures servent la décision ; une
  FAQ mécanique et des variantes lexicales seules ne satisfont pas la couverture.
- Title et H1 décrivent cette décision. La description résume la réponse réellement
  fournie et quelques contraintes décisives quand elles tiennent naturellement.
  Ne pas y accumuler toutes les branches ni promettre une réponse absente du corps.
- Distinguer longueurs observées, préférence du projet et problème de sens. Les
  plafonds de 60/155 ou 30–60/70–160 utilisés dans certains dossiers sont des conventions
  éditoriales locales, jamais des conditions de classement universelles.
- Une comparaison documentaire expose sources, références exactes, conditions et
  inconnues. Elle ne démontre pas bruit, confort, autonomie réelle ou fiabilité sans
  mesure. Les photos illustratives ne prouvent pas un essai ou une expérience vécue.
- Les liens renvoient vers la section ou page réellement utile. Vérifier le fragment
  après rendu si nécessaire ; un lien de filtre n'est pas cassé du seul fait que son
  ancre manque dans le HTML initial.

## Recherche IA et mesure

Relier les questions au panel versionné et à la carte des citations existants.
Conserver séparément les questions principales et les variantes de test : ne pas
gonfler le nombre de besoins couverts avec des répétitions. Pour une citation, ouvrir
la page lorsqu'elle est accessible, vérifier l'affirmation soutenue, relever la
section concernée et décider quelle lacune est effectivement démontrée.

Une proposition de sous-question est `HYPOTHESE_EDITORIALE` ; une question réellement
observée est `OBSERVEE` avec sa preuve ; une sous-requête moteur effectivement exposée
par un outil est `EXPOSEE_PAR_OUTIL` avec surface, date et trace. Ne pas confondre ces états.

Pour le bilan : pages/sections effectivement enrichies, branches inspectées et
résolues, réponses valides du panel, citations/recommandations, visites et actions
mesurables. Toujours fournir périmètre, dénominateur, dates effectives et inconnues.
Un taux de couverture décrit cette matrice, pas un score GEO ni une part de marché.

Enregistrer version du panel, changement éditorial, date de publication, fenêtre de
données, moteur/surface, recherche activée, langue/pays et contexte. Sans panel ou
analytics accessible, rendre la recette éditoriale/technique et un plan de mesure ;
ne pas annoncer d'amélioration de citations, de CTR ou de conversions.

Le guide Google actuel et le [rapport génératif dédié](https://support.google.com/webmasters/answer/16984139)
doivent primer sur les seules indications de mesure globale de l'ancien guide.
Consulter [la mesure et le conflit documenté](04-measurement.md) ; vérifier les
rapports, paramètres d'inclusion et métriques réellement disponibles sur la
propriété. Un connecteur tiers qui appelle un champ « IA » doit expliquer sa source
et sa méthode ; ne pas le présenter comme une mesure officielle indépendante ni
l'ajouter à un total qui l'inclut déjà.

## Recette adaptée au changement

Comparer sur les pages concernées : corps, titres/meta, preuves, HTML initial/rendu,
liens/fragments, action suivante, canonical/indexabilité, médias et balisage pertinent.
Identifier la source et la version publique avant une publication autorisée et
préserver les routes publiques absentes d'une ancienne copie locale. Réutiliser les
contrôles valides ; suivre une instruction explicite de ne pas lancer de tests.
Un build nécessaire et autorisé reste une compilation, pas une suite de tests.

Pour capitaliser sur des projets passés, lire [le retour des quatre sites](four-sites-feedback.md).
