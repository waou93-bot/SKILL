# Rythme, typographie et mise en page éditoriale

## Rythme de lecture

Ces repères sont des choix éditoriaux adaptés à partir d’un échantillon, pas les chartes officielles des médias ni des seuils SEO.

- Un chapô de 2 à 3 phrases : réponse ou verdict, usage concerné, réserve essentielle. Viser environ 40 à 70 mots lorsque le sujet le demande ; une brève peut être plus courte.
- Une idée par paragraphe, généralement développée en 2 à 4 phrases. Viser souvent 35 à 80 mots ; au-delà d’environ 100 mots, vérifier si une coupure correspond à un vrai changement d’idée. Ne pas couper mécaniquement chaque phrase.
- Varier les phrases : une phrase courte pose le point, une phrase moyenne explique, une autre précise une limite. Les phrases de 12 à 25 mots constituent un repère souple ; garder une phrase plus longue si elle évite une ambiguïté. Éviter les séries télégraphiques et les phrases de même longueur.
- Relier fait, conséquence pratique et limite lorsque pertinent, sans reproduire systématiquement cette formule dans chaque paragraphe.
- Ajouter un intertitre à un changement de question ou d’usage, souvent après 2 à 5 paragraphes. Ne pas poser un H2 au-dessus de chaque phrase ni fabriquer des sections vides pour atteindre un quota.
- Une transition indique un lien réel : cause, conséquence, réserve, étape suivante. Éliminer les connecteurs de remplissage et les conclusions qui répètent le chapô.
- Alterner les modes de lecture selon le besoin : une synthèse se parcourt vite, les paragraphes développent la décision, un visuel explique ou identifie, puis une offre permet d'agir. Après une liste ou un tableau, reprendre une prose qui apporte une explication nouvelle ; ne pas empiler résumé, puces et tableau racontant la même chose.
- Donner aux fiches des repères comparables, avec une longueur proportionnée aux différences utiles. Éviter les textes interchangeables, les pavés et le découpage systématique en phrases isolées. Une limite et sa conséquence restent ensemble, même lorsqu'un module commercial suit.
- Utiliser le gras pour une décision, une condition ou une donnée importante, rarement plus d’un fragment par paragraphe. Éviter le gras sur tous les mots-clés, les phrases entièrement grasses et les emojis décoratifs.

Exemple original : « Pour le train, commence par vérifier la réduction du bruit. Cette fonction peut rendre un trajet plus confortable, mais son efficacité doit être évaluée dans un environnement comparable au tien. Une simple mention sur la fiche technique ne suffit pas. »

## Espaces entre les mots et ponctuation française

- Une seule espace entre les mots ; jamais de doubles espaces, de tabulations ou d’espaces répétés pour aligner du texte.
- Aucune espace avant virgule ou point ; une espace après. Pas d’espace immédiatement à l’intérieur des parenthèses.
- Dans la prose française, utiliser des espaces insécables autour du texte dans les guillemets « ainsi », avant les deux-points et entre une valeur et son unité ou symbole : 300 €, 45 W, 128 Go, 20 %.
- Employer si possible l’espace fine insécable U+202F avant ; ? ! et pour les groupes de milliers ; sinon l’espace insécable U+00A0. Appliquer une convention cohérente avec le CMS : 1 299 €, 6,7 pouces, 1 h 30 min. Ne pas modifier l’écriture d’un nom de modèle.
- Préférer apostrophe typographique ’, guillemets français et virgule décimale dans la prose. Préserver les caractères requis dans URLs, code, commandes, JSON et libellés exacts d’interface.
- Ne pas injecter des entités HTML dans un article Markdown ordinaire. Conserver les caractères Unicode si le support les accepte ; signaler les substitutions nécessaires sans altérer la syntaxe technique.

### Deux-points : contrôle de tous les textes

Utiliser réellement U+202F avant chaque deux-points de prose française (ou U+00A0 selon le support). Le caractère insécable relie le signe au mot précédent. Ne pas laisser une espace ordinaire sous prétexte que le CMS devrait corriger le texte. Contrôler aussi les titres, sous-titres, métas, intertitres, puces, cellules de tableau, légendes, mentions commerciales et libellés de bouton. Préserver URLs, heures, code, YAML et JSON.

Pour un H1 interrogatif, préférer une question directe lorsqu'un deux-points n'ajoute rien : « Faut-il choisir un casque ou des écouteurs pour le train ? ». Lorsqu'il reste utile, livrer « Casque ou écouteurs : les critères de choix » avec le caractère U+202F réel avant le signe. Aucun saut manuel, espace normal, `<br>` ou retour Markdown forcé ne doit isoler le signe ou déplacer artificiellement sa suite. Un deux-points introduisant une vraie liste peut naturellement clore le paragraphe qui l'annonce.

Avant livraison, rechercher les espaces ordinaires avant `:` dans toutes les zones éditoriales, corriger les occurrences et vérifier qu'aucun retour forcé n'est collé au signe. Ne pas modifier les séparateurs de syntaxe technique. Le contrôle des caractères et le contrôle du rendu sont deux vérifications distinctes.

## Mise en page Markdown par défaut

- H1 formulé selon l’intention : question si le lecteur pose une question, titre descriptif pour une sélection ou un explicatif. Ajouter un sous-titre qui donne un début de réponse, un chapô qui la développe, puis une éventuelle synthèse rapide avant le développement. Le sous-titre est une phrase sous le H1, pas un H2 décoratif ; fusionner sous-titre et chapô si le support le demande. Un sommaire est utile pour un guide long, pas pour une brève.
- Une ligne vide entre paragraphes et autour des titres, listes, tableaux et images. Ne pas ajouter des lignes vides multiples ou des sauts de ligne manuels après chaque phrase pour simuler des marges.
- Corps en prose. Puces pour critères parallèles, points forts et limites ; numérotation pour actions ordonnées. Encadré bref pour avertissement ou verdict réellement utile, sans transformer tout l’article en cartes.
- Dans les guides, répéter une même structure de fiche pour permettre la comparaison. Dans les explicatifs, garder une progression continue. Dans les tutoriels, placer le visuel près de l’action concernée.
- Dans les guides pédagogiques, regrouper les options sous le critère expliqué ; dans les sélections, grouper les modèles par profils si cela simplifie le choix. Les offres suivent les points de décision définis dans [structures-et-partenaires](structures-et-partenaires.md), avec une séparation lisible entre argumentation et action commerciale.
- Tableau avec quelques critères qui changent le choix ; scinder un tableau trop large en groupes cohérents. Ne pas réduire la police pour caser dix colonnes.
- Placer une illustration professionnelle à proximité de l’idée qu’elle explique, avec légende et crédit/provenance connus. Ne pas ajouter des visuels à intervalles fixes pour remplir une page.
- Séparer clairement l’article destiné au lecteur du dossier de livraison : variantes de title, mots-clés, propositions de liens, JSON-LD et vérifications ne sont pas des paragraphes à publier dans le corps.

## Si une mise en page HTML/CSS est demandée

Réutiliser la charte existante. Les valeurs suivantes sont des points de départ recommandés, pas des mesures universelles des références : texte 17–19 px sur ordinateur et 16–18 px sur mobile, interligne 1,5–1,75, largeur de lecture autour de 60–75 caractères, marges latérales mobiles 16–24 px, espace entre paragraphes environ 0,9–1,3 em. Vérifier avec la police réelle et le rendu.

- Alignement à gauche ; éviter la justification qui étire irrégulièrement les mots, surtout sur mobile.
- `word-spacing: normal` et `letter-spacing: normal` pour le corps. L’air vient de l’interligne, des marges et de la largeur de colonne, pas d’un écart artificiel entre chaque mot.
- Plus d’espace avant un intertitre qu’après pour rattacher celui-ci au texte qui suit. Maintenir une hiérarchie nette H1/H2/H3 sans recopier les polices, couleurs ou composants d’un média.
- Pour les deux-points, conserver le caractère insécable dans le HTML. Si le CMS l'efface, employer une entité HTML adaptée (`&#8239;` pour U+202F ou `&nbsp;` pour U+00A0). Examiner `word-break`, `overflow-wrap`, les retours forcés et les traitements du CMS sur les titres. Si le rendu isole encore le signe, protéger seulement le mot précédent et le deux-points avec `<span class="ponctuation-liee">mot :</span>` et `.ponctuation-liee { white-space: nowrap; }`. Laisser le reste du titre revenir naturellement à la ligne ; un titre entier sans retour peut déborder sur mobile.
- Images adaptatives, légendes proches ; tableaux lisibles avec défilement local ou représentation adaptée, sans débordement de toute la page.
- Les espaces publicitaires, cookies et menus ne dictent pas le rythme éditorial. Pour les modules commerciaux, reprendre leur fonction et un placement pertinent décrit dans structures-et-partenaires, sans recopier leur habillage ni leur multiplication.

## Contrôle final

Lire le chapô puis seulement les intertitres : la décision et le parcours doivent être compréhensibles. Relire un passage à voix haute pour repérer monotonie et ruptures inutiles. Contrôler espaces doubles, ponctuation, nombres/unités, respiration des paragraphes, surusage du gras et cohérence des fiches. Pour une page rendue, vérifier à une largeur mobile et sur ordinateur ; si seul Markdown est livré, ne pas annoncer une validation du rendu, des pixels ou de l’accessibilité.

Retirer les modules commerciaux pendant une relecture : chaque fiche ou critère doit conserver son raisonnement et ses limites. Vérifier ensuite que les liens et offres se placent à la fin d'une unité de sens et que leur répétition aide une nouvelle décision. Le scan complémentaire des deux guides demandé le 13 octobre 2026 est documenté dans structures-et-partenaires ; il porte sur le texte et l'ordre accessible des blocs, sans nouvelles mesures CSS.

Sur une page rendue, inspecter particulièrement les titres longs aux largeurs étroites réellement visées. Aucun deux-points ne doit ouvrir une ligne sans le mot auquel il est rattaché. Vérifier les champs de sous-titre et meta après enregistrement si le CMS est accessible. Sans page ou rendu fourni, annoncer seulement le contrôle des textes, pas une correction visuelle du site.

## Sources et portée du scan — 9 octobre 2026

Échantillon ciblé de quatre articles, texte/structure lus et rendus observés dans le navigateur. Un paragraphe relevé par média ; les tailles, largeurs et marges sont celles de cet échantillon dans la fenêtre consultée. Les marges d’un élément ne représentent pas tous les espacements : des conteneurs et règles de voisinage peuvent les compléter. Aucune moyenne de site ni analyse exhaustive mobile.

| Référence | Observation éditoriale | Relevé du paragraphe : mots ; taille/interligne ; largeur ; marge basse |
| --- | --- | --- |
| [01net, test Pixel Pro XL](https://www.01net.com/tests/test-google-pixel-11-pro-xl-avis-smartphone.html) | Chapô, synthèse atouts/limites, sections par usage et photos créditées. | 70 ; 18/32 px ; 801 px ; 24 px |
| [Frandroid, guide sous 300 euros](https://www.frandroid.com/guide-dachat/smartphones/276805_les-meilleurs-smartphones-a-moins-de-300-euros-en-2017) | Sommaire, sélection rapide, fiches récurrentes, développement et FAQ. | 47 ; 18/27 px ; 604 px ; 0 px sur l’élément |
| [Les Numériques, guide smartphones](https://www.lesnumeriques.com/telephone-portable/guide-achat-quels-sont-les-meilleurs-smartphones-android-et-ios-g243.html) | Méthode annoncée, sélection par gamme, blocs atouts/limites et questions de choix. | 49 ; 17/27,506 px ; 624 px ; 0 px sur l’élément |
| [Android Magazine web, tutoriel de réinitialisation](https://www.android.com/intl/en_uk/articles/how-to-reset-android-device/) | Image de situation, sommaire, contexte, prérequis et étapes hiérarchisées. | 48 ; 16/24 px ; environ 860 px ; 20 px |

Les quatre paragraphes ont `word-spacing: 0px`, `letter-spacing: normal` et `text-align: start`. La référence Android consultée est le contenu anglophone officiel d’android.com, distinct d’un ancien magazine papier homonyme ; elle informe la structure, pas la typographie française. La ponctuation française et les plages de rédaction ci-dessus sont des conventions proposées, pas des règles revendiquées par ces quatre médias. Les pop-ups ont limité certains cadrages visuels chez Les Numériques ; la structure et le paragraphe ont néanmoins été accessibles. Aucun contenu copié, aucune caractéristique produit adoptée comme fait dans le skill.
