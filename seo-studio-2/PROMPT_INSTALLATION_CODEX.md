# Installation à transmettre à Codex

Copier le bloc ci-dessous dans la session qui possède les fichiers du package.

```text
Installe le bundle depuis sa racine avec scripts/install.py : il contient les skills
seo-studio-2 et seo-site-preproduction à placer dans deux dossiers frères reconnus
par l'hôte. Lis README.md, les deux SKILL.md et MANIFEST.sha256.json. N'en recrée pas
une version simplifiée. N'écrase aucun skill différent existant.
Détecte les emplacements de skills réellement lus par cet hôte. Inventorie les
copies existantes de seo-studio-2 ainsi que Brain, Organisation, No Slop, Design DNA,
tous les identifiants contenant SEO et le vrai /personna (vérifier aussi persona
comme candidat, sans l'assimiler automatiquement à la commande demandée).
Lis les SKILL.md réels et consigne version, chemin, empreinte et rôle.
Inclure site-checklist, pSEO, redaction-editoriale-web, webapp-testing,
cross-platform-qa, security-best-practices et web-perf dans ce contrôle.
Utiliser le catalogue actif pour les dépendances absentes du dépôt ; aucune
installation automatique, API ou service payant obligatoire.
N'écrase aucune personnalisation. Si une version différente existe, sauvegarde-la,
présente le diff et la migration nécessaire ; l'installateur refuse cet écrasement.
Ne crée pas de /personna de remplacement. S'il manque, signale le chemin ou le package
nécessaire ; installe néanmoins SEO STUDIO 2 si le reste de l'installation est sûr,
mais laisse son état de préparation stricte BLOQUE_DEPENDANCE.
Utilise scripts/install.py avec un chemin cible vérifié, d'abord sans --apply, puis
avec --apply pour installer explicitement les deux skills.
N'installe pas les autres skills automatiquement et ne change pas leur version.
Ne modifie aucun projet, dossier MASTER/BUSINESS/SEO, site, compte ni config globale.
Après copie, contrôle les empreintes et la découverte réelle du skill dans l'hôte.
Vérifie que son invocation explicite charge le SKILL.md complet et non un doublon.
Sépare dans ton bilan : fichiers installés, tests locaux, détection hôte, dépendances
et formation /personna. Ne transforme pas une copie réussie en preuve de fonctionnement
multiagent ou de résultats SEO. Aucun push ou déploiement n'est demandé.
```
