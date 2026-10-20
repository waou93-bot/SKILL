---
name: site-editorial-release
description: >-
  Prépare un site existant pour publication par une revue visuelle et éditoriale
  de toutes ses pages publiques. Coordonne human-reading, redaction-editoriale-web
  et no-slop, repère les répétitions entre pages, corrige les textes, puis commit,
  push, déploie sur demande et lance seo-post-deploy après un déploiement confirmé.
  À utiliser pour une revue et une mise en ligne à l'échelle du site, pas pour une
  retouche ponctuelle d'une page.
metadata:
  version: "1.0.0"
---

# Site editorial release

## Mission

Réaliser une passe cohérente sur un site existant avant publication : lire l'expérience visuelle de chaque page, corriger les textes avec les skills éditoriaux, éliminer les répétitions inutiles dans le corpus, puis vérifier, committer, pousser et déployer le périmètre demandé. Après un déploiement confirmé, exécuter le suivi de `seo-post-deploy` sur le domaine de production concerné.

Les contrôles produisent des constats et des réserves, pas un veto. Si l'utilisateur demande commit, push et publication, ne redemander aucune validation intermédiaire et ne suspendre pas l'action pour un avis défavorable, une page non vérifiée ou un contrôle incomplet. Signaler les réserves avec leur preuve, leur portée et le correctif recommandé. Seule une impossibilité opérationnelle réelle peut empêcher matériellement une étape ; décrire alors l'erreur ou l'accès manquant.

## Périmètre et prérequis

Utiliser ce skill pour une révision à l'échelle d'un site existant. Pour une retouche isolée, appeler directement les skills utiles et limiter la relecture aux pages affectées.

Au début, identifier à partir du contexte disponible :

- dépôt local, branche, remote, état des modifications et conventions de commit ;
- domaine de production, locale(s), rôle du site et prochaine conversion attendue ;
- sources qui recensent les pages : routes, CMS/export, sitemap XML/HTML, menus et liens internes ;
- hébergeur ou mécanisme de publication, accès et commandes de déploiement ;
- règles éditoriales, validations factuelles, liens partenaires et limites du projet.

Reprendre les informations déjà données. Si le workspace n'est pas un projet de site, créer et livrer uniquement le skill demandé ; ne pas traiter un dépôt de skills ou de documentation comme un site web, et ne pas inventer son domaine. Si le domaine ou l'accès de production manque, continuer les corrections et le commit/push autorisés, puis marquer le déploiement et `seo-post-deploy` comme non applicables ou en attente de la donnée nécessaire.

Lire les instructions du projet et les skills disponibles suivants : `human-reading`, `redaction-editoriale-web`, `no-slop` et, après publication, `seo-post-deploy`. Les consulter une fois pour le périmètre complet et tenir un seul registre de revue. Ne pas lancer plusieurs audits identiques page par page sous des noms de skills différents.

## Parcours de revue

### 1. Établir l'inventaire exhaustif

Établir un manifeste des pages publiques à partir des routes réellement servies, du CMS/dépôt, des sitemaps et de la navigation. Inclure les pages fixes, les pages issues de données, les locales et les pages de confiance. Repérer redirections, doublons d'URL, pages privées ou non accessibles. Pour chaque page, enregistrer URL canonique, langue, gabarit, accès visuel, statut et couverture éditoriale.

Ne pas appeler une revue « complète » si une source de pages est inaccessible ou si des routes restent non visitées. Continuer le travail accessible et marquer clairement les écarts de couverture. Ne pas extrapoler d'une page d'exemple à tout un gabarit sans vérifier ses variations de contenu.

### 2. Lire visuellement chaque page

Appliquer `human-reading` au rendu réel du site : capturer toutes les pages publiques du manifeste sur desktop et mobile aux tailles de livraison réelles, puis inspecter chaque écran individuellement. Un contact sheet est un index, pas une inspection. Examiner hiérarchie, taille, contraste, texte sur image, titres, tableaux, CTA, liens, mentions, césures, débordements, éléments tronqués et ordre de lecture.

Consigner un constat par page/élément dans le registre commun : route, viewport, preuve visuelle, problème, priorité et correction proposée. Si une page ne peut pas être rendue, indiquer « non vérifiée » ; ne pas transformer l'inspection de quelques captures en validation du site entier. Appliquer les ratios de contraste et autres consignes du skill `human-reading`.

### 3. Constituer le corpus et repérer les répétitions

Extraire les textes visibles et métadonnées de toutes les pages : title, meta description, H1, intertitres, chapô, corps, tableaux, légendes, CTA, libellés, alt, liens contextuels, bannières, footer et annonces.

Analyser les répétitions exactes et proches entre pages. Comparer en contexte les mots, expressions, phrases, paragraphes et formulations d'offre. Pour chaque répétition notable, noter les pages et occurrences, la fonction de la répétition et la décision : **conserver**, **uniformiser**, **réécrire** ou **supprimer**.

Distinguer les doublons éditoriaux des éléments intentionnellement partagés : navigation, mentions légales, nom de marque, terminologie nécessaire, composants communs, mentions commerciales ou appels à l'action cohérents. Ne pas viser zéro répétition. Garder le même terme pour la même chose ; éviter les synonymes artificiels et la variation « pour faire différent ». Réduire les expressions répétées qui n'apportent rien, les intros interchangeables, les métadonnées identiques et le bourrage de mots-clés sans retirer les termes centraux utiles au lecteur ou à la recherche. Une requête partagée ne rend pas deux pages identiques si leur intention et leur réponse diffèrent.

### 4. Corriger l'éditorial et le style du site

Faire passer l'ensemble du corpus dans `redaction-editoriale-web` pour la clarté, l'exactitude, le fan-out existant, les titres et métadonnées, les liens contextuels, les offres partenaires, les visuels et les limites de preuve. Utiliser les instructions réellement disponibles et les gabarits utiles ; ne pas rédiger un article complet là où une correction ciblée suffit.

Appliquer ensuite `no-slop` à tout le contenu et à l'interface du périmètre : vocabulaire banni, ton promotionnel, formulations génériques, incohérences de termes, affirmations sans preuve et les 30 critères de revue de site. Enregistrer chaque critère comme **pass**, **needs change**, **justified exception**, **not applicable** ou **unverified** avec la page/composant et la preuve. Préserver les exigences explicites et les choix de marque approuvés ; ne pas remplacer mécaniquement un motif visuel seulement parce qu'il figure dans la checklist.

Dédupliquer les actions de revue : exécuter une seule passe éditoriale sur le corpus entier, une seule revue de vocabulaire/répétitions transversale et une seule grille `no-slop` consolidée. Corriger toutes les pages autorisées en lots cohérents. Rejouer un contrôle uniquement quand la modification affecte la preuve, la page ou un composant partagé.

Ne pas inventer auteur, expérience, tests, source, donnée, prix, partenariat ou résultat. Garder les incertitudes visibles dans le dossier et retirer ou réécrire toute affirmation publique que les preuves du projet ne soutiennent pas. Respecter la politique de liens sortants du projet ; dans SEO Studio 3, les hyperliens publics sortants restent réservés aux partenaires confirmés. Garder les sources non partenaires dans les notes internes de ce projet.

Utiliser les scripts ou outils d'analyse de texte seulement pour repérer des candidats ; examiner les occurrences en contexte avant de changer les textes. Un décompte de fréquence n'est ni une preuve de bourrage ni une instruction de supprimer un mot. Ne pas lancer des tests logiciels non demandés. Si une correction touche réellement l'interface, appliquer aussi les consignes UI pertinentes de `no-slop`, notamment sa section Uiverse ; pour de la correction de texte uniquement, ne pas ajouter d'interface.

### 5. Vérifier le site corrigé

Réactualiser le manifeste des routes et le corpus après édition. Rendre le site corrigé, puis refaire une passe visuelle `human-reading` page par page sur desktop et mobile pour l'ensemble des pages publiques. Comparer les écrans au registre initial et vérifier que chaque problème corrigé l'est réellement, sans introduire de nouveaux problèmes de lisibilité. Contrôler également les 30 critères `no-slop` sur le périmètre complet ; réévaluer les critères affectés par les corrections et noter toutes les exceptions ou inconnues restantes.

Refaire une seule analyse transversale des textes corrigés pour trouver les nouvelles répétitions, variations incohérentes et métadonnées dupliquées. Vérifier que les liens, CTA, URL et mentions n'ont pas changé de destination ou de sens par accident. Ne pas annoncer une inspection ou une correction qui n'a pas été observée.

Si le rendu est impossible pour une route, terminer le reste, nommer la route et l'appareil/viewport manquant, et poursuivre la demande de publication avec cette réserve.

### 6. Commit, push et publication

Le périmètre « site entier » comprend les corrections éditoriales autorisées sur toutes les pages inventoriées. Avant commit, relire le diff, ne garder que les fichiers de ce chantier et préserver les changements préexistants d'autres personnes. Ne pas écraser, réinitialiser ou inclure des secrets. Committer sur la branche prévue et pousser sur le remote attendu.

Lorsque la demande inclut explicitement de publier, déployer le commit poussé sur le site de production configuré. Les réserves de revue, défauts non bloquants, pages non vérifiées et statuts `no-slop` ne suspendent pas le processus. Les rapporter clairement, y compris les corrections restantes. Si le système de déploiement refuse l'opération ou si les accès sont réellement absents, fournir le message opérationnel et l'étape nécessaire sans qualifier le site de validé.

Exécuter uniquement le build ou les vérifications obligatoires du mécanisme de publication. Ne pas ajouter ni lancer une suite de tests sans demande explicite. Vérifier que le déploiement correspond au commit poussé et que le domaine de production répond après publication.

### 7. Exécuter le post-déploiement SEO

Après confirmation du déploiement, appeler `seo-post-deploy` pour le domaine de production exact, le commit, les pages prioritaires et les opérateurs pertinents. Laisser ce skill vérifier les démarches autorisées de découverte, sitemaps, indexation, Search Console, Bing, analytics et visibilité IA selon les accès et le site. Ne pas utiliser le dépôt GitHub comme substitut à un domaine en production. Distinguer commit poussé, déploiement, soumission, exploration, indexation et données de performance. Ne jamais promettre un résultat de classement.

Si `seo-post-deploy` ne peut pas agir faute de propriété, de domaine ou d'accès, consigner la limite et poursuivre les étapes indépendantes accessibles ; ne pas inventer une soumission réussie.

## Registre et compte rendu

Tenir un registre unique comprenant :

- manifeste des routes, langues et gabarits, avec couverture initiale/finale ;
- résultats `human-reading` par page et viewport ;
- répétitions examinées, leur décision et exceptions justifiées ;
- état des 30 critères `no-slop` et corrections éditoriales ;
- réserves non résolues et preuves ;
- fichiers commités, branche, commit, push, URL de production et état du déploiement ;
- actions `seo-post-deploy`, opérateurs couverts, preuves et accès manquants.

Le compte rendu met en premier les réserves et éléments non vérifiés. Indiquer le nombre de pages et viewports réellement inspectés, les fichiers changés, l'URL/commit publié, et le résultat réel du post-déploiement. Ne jamais qualifier de « complet » ce dont la couverture est inconnue.

