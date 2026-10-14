# Parcours pas à pas établi et suivi par Organisation

Pour l’affiliation, appliquer les [transferts AFFISEO sourcés](26-affiseo-methodes.md) au périmètre de cette référence ; le contrat 24 et les gates existants restent prioritaires.

Charger le vrai skill Organisation au démarrage. Il établit dans `00_REFLEXION.md`
une section « Méthode et processus de bout en bout », adaptée au projet réel,
puis coordonne son exécution. Ne pas se contenter de citer ce document ou ce parcours.
Conserver les IDs et états dans `state.json` et `workflow.json` : cette section
explique leur déroulement et ne crée pas un registre concurrent.

Pour chaque étape, renseigner : ID, objectif, entrées, action, responsable,
livrable, preuve attendue, critère PASS/FAIL, dépendances, validation humaine
éventuelle et condition de reprise. Une étape optionnelle doit avoir une raison
d'exclusion ; une étape obligatoire ne peut être supprimée par le mode lite.
Les rôles sont des responsabilités, pas des changements de modèle implicites.

## Ordre de réalisation

1. **Reprendre et cadrer.** Lire instructions, existant, décisions, accès,
   permissions et demande. Définir périmètre, inconnues et critères de succès.
   Preuves : exigences tracées, inventaire et méthode adaptée dans 00_REFLEXION.md.
2. **Auditer et rechercher.** F0/F1, G0/G1 : sources métier, SERP et concurrence,
   contenu, produits et URL existants. Pour une refonte affiliée, phase 0 avant code,
   crawl et captures de huit pages types desktop/mobile. Manque : question et blocage
   du travail dépendant, sans invention.
3. **Comparer et décider.** F2/F3 : options, limites et décisions sourcées.
   Après la recherche métier de F1, former et calibrer les profils via le vrai
   Personna avant leurs appels et le cycle idées ; clôturer ce cycle avant F3.
   Appliquer les revues réellement disponibles conformément au contrat, sans
   prétendre à une indépendance absente.
4. **Organiser l'architecture.** G2 : silos, intentions, propriétaires des pages,
   maillage, fan-out, routes et mapping 301. Respecter les prérequis SERP avant G3.
5. **Valider le design.** G3 et phase 1 : extraire la V1 ou proposer deux directions
   pour un nouveau site, maquettes et design-system.md lié au skin.
   Attendre la validation explicite utilisateur ; aucun code de pages anticipé.
6. **Vérifier les produits et préparer la technique.** G3/G4 et phase 2 : données,
   sources lues, images, prix et affiliation active ; rapports des manques.
   Conserver Astro/Cloudflare retenus. Installer et tester le prébuild du projet.
7. **Construire et contrôler les pilotes.** Phase 3 : trois pages réelles,
   templates et contenu propres, recherche interne et SEO intégrés. Inclure la
   page d'entrée réelle (landing si présente, sinon accueil) avec produits vérifiés
   et CTA affiliés visibles dès le premier écran utile.
   Preuves : build, contrôles produit, captures comparées et corrections.
8. **Produire par lots.** Phase 4 : lots de 20–30 pages, dernier lot adapté,
   contrôle avant lot suivant, trois éléments propres par page pSEO indexable.
   Le pSEO complète les piliers et comparatifs rédigés.
9. **Recetter et corriger.** Phase 5, G5/G6, D4 : QA visuelle, fonctionnelle,
   sécurité, performance, produits, balisage et redirections sur tout le périmètre.
   Corriger puis rejouer. Un échec obligatoire interdit une livraison terminée.
10. **Livrer et publier si autorisé.** Remettre sources, commandes reproductibles,
    preuves et état final. D5 ne s'exécute qu'avec autorisation de publication.
    Si publication exclue, la livraison locale vérifiée termine ce périmètre.
11. **Suivre si inclus au mandat.** Après publication autorisée, appliquer
    seo-post-deploy puis seo-opportunity-loop avec données GSC ou exports autorisés.
    Pas d'automatisation, dépense ou suivi permanent créé implicitement.

## Conduite et reprise

À chaque étape : réaliser, critiquer, corriger, vérifier, puis consigner
**ce qui est fait, ce qui est vérifié, ce qui manque** et la prochaine étape permise.
Les portes affiliation du contrat 24 restent obligatoires ; cette liste ne les
remplace pas. Réutiliser les décisions et preuves encore valides en reprise ciblée,
invalider celles affectées, et reprendre à la première étape impactée.
Organisation poursuit jusqu'à la livraison autorisée ou jusqu'à un blocage réel,
qu'elle décrit précisément avec la question nécessaire à sa résolution.
