---
name: cross-platform-qa
description: "Recette opérationnelle d'un site sur desktop, Safari iOS et Chrome Android : rendu, interactions, consentement, tableaux, clavier et animations, avec preuves par route/état/version et distinction appareil réel, émulation et resize. Utiliser pour une repasse multiplateforme ou une comparaison mobile/desktop, sans prétendre tester une plateforme absente."
---

# Recette multiplateforme

Compléter Site Checklist par une procédure d'exécution, sans refaire son audit SEO/légal ni redéfinir l'identité Design DNA. Lire les critères pertinents de site-checklist, human-reading, design-dna et no-slop depuis le catalogue réel ou le registre du plugin. Human Reading s'applique aux écrans de l'échantillon déclaré ; ses recommandations de correction ne dépassent pas le mandat lecture seule ou les modifications autorisées. Ne pas rappeler son pilote. Un audit reste en lecture seule ; corrections locales seulement dans le mandat, déploiement distinct.

1. Identifier URL/code, version livrée, environnement local/préproduction/production et routes/gabarits/états critiques. Lire PROJECT_SKIN et décisions existantes. Choisir une couverture proportionnée et déclarer l'échantillonnage. Lire [le protocole](references/protocol.md).
2. Inventorier outils et plateformes réellement accessibles. Matrice desktop avec navigateur/version ; Safari iOS avec appareil/OS/version ; Chrome Android avec appareil/OS/version. Étiqueter chaque essai `real_device`, `browser_emulation` ou `viewport_resize`. Un WebKit desktop ou un profil iPhone émulé ne prouve pas Safari iOS réel ; un resize Chrome ne prouve pas Android. Les outils agent ne sont pas des trackers du site.
3. Exécuter les contrôles applicables sur chaque route/état de la matrice. Observer les captures à taille lisible avec Human Reading et interactions réelles ; une capture seule ne prouve ni clic ni événement reçu. Conserver preuves, date, cible/version, navigateur, appareil, orientation, dimensions et méthode. Platform indisponible = `BLOCKED` et procédure manuelle précise ; jamais PASS global par extrapolation.
4. Comparer captures/états à la baseline validée à conditions égales, diagnostiquer défauts sans imposer une identité nouvelle. Corriger dans le périmètre autorisé puis rejouer les états et plateformes affectés ; invalider preuves anciennes. Deux passes ciblées maximum par gate du plugin, puis PARTIAL/BLOCKED avec défaut restant. Préserver flèches/chevrons fonctionnels et choix typographiques approuvés.
5. Distinguer tests du code local et de la version servie. Après déploiement autorisé, contrôler URL finale, version et parcours réels ; un build local n'est pas une recette production. La carte Analytics décrit une configuration attendue ; confirmer séparément tags observés, consentement, livraison d'événement et accès au rapport. Pas de compte, consentement utilisateur ou tracking modifié implicitement.

Restituer matrice PASS/FAIL/PARTIAL/BLOCKED/N/A avec preuves, défaut/impact/correctif, exclusions et essais manuels restants. N/A demande raison. La réussite porte sur le périmètre observé uniquement. Aucun test live du site cité en exemple n'est démontré par l'installation de ce skill.

Pour vérifier les invariants du skill, utiliser [les scénarios documentaires](references/scenarios.md) ; leur revue ne remplace pas un essai de navigateur.
