# Liens hypertextes contextuels pendant la rédaction

## Préparer les destinations

Lire l'inventaire réel des articles, guides, catégories et fiches produits fourni,
le CMS ou les routes accessibles. Repérer pour chaque partie un approfondissement,
un prérequis, une alternative ou un produit directement utile. Conserver URL/slug,
titre, nature de destination, variante produit et statut d'accès. Réutiliser les
URLs existantes ; ne pas en déduire une uniquement depuis son titre.

## Intégrer dans la prose

Transformer certains mots-clés et surtout les expressions qui annoncent clairement
la destination en ancres naturelles au point où le lecteur pourrait en avoir besoin.
Exemples de formes d'ancre : « régler la température de couleur » vers un guide,
« différences entre les deux technologies » vers un comparatif, ou nom précis du
modèle vers sa fiche produit interne. Ce sont des formes, pas des URLs à inventer.
La phrase doit rester lisible et exacte avec ou sans le lien. Un lien rejoint une
ressource utile ; il ne sert pas à interrompre artificiellement la réponse.

Livrer `[expression](URL_EXISTANTE)` en Markdown ou `<a href="URL_EXISTANTE">expression</a>`
dans le corps HTML/composant demandé, avec échappement adapté. En intégration CMS,
enregistrer le lien dans le contenu effectivement affiché. Un dossier contenant
seulement « liens à ajouter » n'est pas une intégration terminée.

Choisir une occurrence significative ; ne pas lier automatiquement chaque répétition,
chaque mot-clé secondaire ou tous les noms de marque. Plusieurs accès à une destination
peuvent se justifier dans des sections éloignées répondant à des besoins distincts.
Pas de densité ou quota de liens imposé, pas de liens vers soi sans fragment utile,
pas de « cliquez ici » vague, UTM interne ou liens cachés. Éviter d'enchaîner plusieurs
ancres dans une courte phrase lorsque cela dégrade la lecture.

## Articles, guides, produits et affiliation

Un lien éditorial vers une fiche produit du site conserve l'URL interne de cette
fiche. Un accès direct pour consulter/acheter chez un partenaire utilise son URL
affiliée fournie et autorisée, la bonne référence/variante et une mention séparée
selon structures-et-partenaires. Ne pas convertir une citation constructeur ou un
lien de test en lien commercial. Les liens rémunérés reçoivent `rel="sponsored"`
dans le HTML livré. Le nom du produit dans une phrase peut être une ancre utile,
mais ne remplace pas les preuves, limites et transparence commerciale.

## Vérifier et gérer les manques

Contrôler route, éventuelle redirection, fragment, modèle/variante et concordance
ancre/destination avec les moyens disponibles. Pour un lien interne, inspecter le
contenu cible ou le code/route réel ; pour un site rendu, tester le clic dans les
gabarits concernés. Un fichier existant ne prouve pas une réponse HTTP publique.
Ne pas déclarer une vérification réseau non effectuée. La destination doit répondre
à la promesse de l'ancre, pas seulement retourner un succès technique.

Sans inventaire ou URL confirmée, garder le passage lisible sans lien actif et
consigner dans le dossier « expression → sujet cible → URL à fournir/vérifier ».
Ne pas utiliser `#`, un slug supposé ou une page future comme destination publiée.
Si une nouvelle page est dans le périmètre, créer et vérifier sa route avant de
relier les pages livrées. Les liens manquants demandés restent à réaliser.

À la livraison, fournir un relevé proportionné : page source, ancre, URL, type
article/guide/produit/source, emplacement et statut. Contrôler liens intégrés,
fragments, répétitions, clavier/focus, distinction visuelle et cohérence du maillage.
Une simple optimisation de title/meta ne modifie pas le corps sans demande.
