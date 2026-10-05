# Liaison GA4–Search Console

Procédure Google vérifiée le 5 octobre 2026 : [liaison](https://support.google.com/analytics/answer/10737381?hl=en), [portée des propriétés](https://support.google.com/webmasters/answer/34592?hl=en), [propriété vérifiée](https://support.google.com/webmasters/answer/9008080?hl=en). Revalider avant opération.

## Prérequis et procédure officielle

Créer le lien exige Éditeur GA4 et propriétaire vérifié GSC. Les deux propriétés doivent mesurer les mêmes pages. Un flux web ne peut être lié qu’à une propriété GSC, réciproquement ; une propriété GA4 ne peut avoir qu’un flux lié à GSC.

Dans GA4 : Administration → Liens avec les produits → Liens Search Console. Lire la table, puis Lier → choisir la propriété GSC → confirmer → sélectionner le flux web → examiner → envoyer. Un lien ne se modifie pas : changer implique supprimer puis recréer. Supprimer exige Éditeur GA4.

La collection Search Console est initialement non publiée ; la publier depuis Bibliothèque. Elle comprend requêtes organiques et trafic organique Google. Les données GSC arrivent environ 48 heures après collecte et couvrent au plus 16 mois ; leur début dépend du plus tardif entre création du flux et vérification GSC. Les dimensions compatibles comprennent page de destination, pays et appareil. Changer le flux affecte toutes les plages de dates affichées.

## Contrat opérationnel du skill

1. Identifier le site canonique réellement ciblé, propriété GA4, ID du flux web et propriété GSC depuis les accès disponibles. Aucun ID deviné ; aucun mot de passe/token dans les preuves. Vérifier URL finale, hôte/protocole/chemin, URL et pages réellement mesurées du flux ; une propriété Domaine peut couvrir davantage que le site canonique. Une propriété préfixe doit couvrir les pages exactes. Comparer la portée effective, pas seulement le nom affiché ; un flux cross-domain demande vérification du périmètre avant association.
2. Inventorier les liens existants côté GA4 et associations GSC accessibles. Lien exact présent : réutiliser et vérifier, aucune nouvelle création. Autre association occupant une limite : conflit explicite, pas de suppression/recréation implicite. Préparer les différences, impact et permissions nécessaires pour une migration expressément autorisée.
3. Vérifier mandat et rôles réellement affichés. Un accès lecture, utilisateur complet GSC ou propriétaire délégué ne prouve pas le statut propriétaire vérifié requis. Si accès insuffisant : `BLOQUE_ACCES` avec rôle/cible/intervention précise, poursuivre audit/soumissions indépendants. Sans cible : préparation générique uniquement.
4. Sans GA4 ou sans flux : constater `BLOQUE_CONFIGURATION` ou `NON_APPLICABLE` justifié ; créer propriété/flux/tag seulement dans un mandat adapté. Préserver CMP/consentement, exemptions et choix de mesure du projet. Une liaison n’autorise ni nouveau suivi, ni contournement du refus, ni collecte de données personnelles. Si politique de collecte inconnue, préparer la liaison sans activer de collecte et signaler le blocage.
5. Pour une création autorisée : vérifier le récapitulatif du couple exact avant envoyer ; relire ensuite la table. Résultat inconnu/timeout : `NON_VERIFIE`, rechercher le lien avant toute nouvelle écriture. Ne pas créer de doublon ni inférer succès depuis un clic.
6. Vérifier séparément configuration, publication de collection et données des deux rapports sur une période éligible. Publier la collection seulement avec droits et mandat applicables. Consigner `LIEN_VERIFIE`, `RAPPORTS_VISIBLES`, `DONNEES_EN_ATTENTE` ou `DONNEES_OBSERVEES`, sans confondre ces étapes. Retard normal, période trop récente ou absence de trafic ne prouvent pas une panne ; après délai, diagnostiquer portée, collecte, vérification et publication avant correction.
7. Registre : domaine canonique, propriété GSC/type/portée, propriété GA4/flux et portée, rôles observés, liens avant/après, autorisation/source, date/action, preuve non sensible, rapports/période inspectés, état collecte/consentement, limites et prochaine action. Comparer clics GSC, sessions GA4 et événements clés comme mesures distinctes : pas d’égalité attendue ni attribution par requête/utilisateur inventée. Soumission, indexation et mesure restent distinctes.

## Scénarios de revue (fixtures, pas comptes réels)

| Entrée | Décision attendue |
| --- | --- |
| Couple exact déjà lié | Réutiliser ; contrôler rapports sans création |
| www/https/préfixe incompatible avec la cible, ou flux d’un autre site | Bloquer association ; démontrer différence de portée ; une variante légitime couverte n’est pas un défaut |
| Lecteur GA4, utilisateur complet ou propriétaire délégué GSC | Bloquer écriture ; préciser Éditeur/propriétaire vérifié requis |
| Flux/propriété déjà lié ailleurs | Signaler conflit ; ne pas supprimer sans mandat |
| Timeout après envoyer | Rechercher lien réel ; résultat inconnu suspend répétition |
| GA4 absent ou consentement non cadré | Préparer ; aucune installation/collecte implicite |
| Lien confirmé, collection non publiée | État configuration distinct ; publication seulement autorisée |
| Rapports vides avant délai/période éligible | Données en attente ; aucune panne ni réussite de collecte inventée |
