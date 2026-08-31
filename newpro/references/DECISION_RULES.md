# Regles d'arbitrage et de securite

## Ce qui peut etre automatise

- inventaire de fichiers et d'extensions ;
- detection de Git et de marqueurs de profil ;
- creation de dossiers et de templates manquants ;
- generation d'une proposition de tranche verticale ;
- validation structurelle et rapport de bootstrap.

## Ce qui doit rester explicite

- objectif et indicateur de reussite ;
- import ou exclusion d'anciens assets ;
- plateforme, stack ou moteur lorsqu'ils sont difficiles a changer ;
- contraintes legales, budgetaires ou commerciales ;
- direction artistique fondamentale ;
- autorisation de lancer la production.

## Regles de fichiers

1. Ne jamais supprimer.
2. Ne jamais ecraser un fichier existant sans option explicite qui n'est pas fournie par la V1.
3. Refuser un dossier non vide sans manifeste, sauf `--adopt-existing` explicitement choisi.
4. Conserver un manifeste `.newpro-manifest.json` pour rendre les relances identifiables.
5. En cas de conflit de template, conserver le fichier existant et signaler l'arbitrage.
6. Inventorier les sources historiques sans les copier par defaut.

## Regles de contenu

- `decision` signifie valide ; `hypothese` signifie a confirmer ; `proposition` signifie a arbitrer ; `rejet` doit avoir une raison.
- Toute inconnue reste visible sous `[A ARBITRER]`.
- Toute tranche doit pouvoir etre testee et abandonnee sans avoir engage tout le projet.
- Toute conclusion doit rappeler l'absence de production et nommer une prochaine action unique.

## Projet ChatGPT

La creation du Projet ChatGPT, sa memoire limitee et ses conversations ne sont pas automatisees par ce skill. Le MASTER peut fournir les instructions, les fichiers a importer et le texte de reprise, mais l'utilisateur conserve la main sur ces actions d'interface.
