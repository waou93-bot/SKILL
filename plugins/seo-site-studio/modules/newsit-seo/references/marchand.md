# Profil marchand

## Résultat et frontière

Le site vend directement et assume commande, paiement, livraison, retours et support. Distinguer ce profil d'un catalogue qui renvoie vers un marchand extérieur. Confirmer marchand, pays, devises, produits, règles de stock et prestataires existants avant de choisir l'architecture.

Évaluer un moteur marchand établi et sa compatibilité avec le design demandé avant un checkout sur mesure. Préserver les intégrations existantes qui répondent au besoin. Ne pas inventer frais, délais, politiques, mentions légales ou disponibilité ; vérifier les obligations applicables avec les sources officielles actuelles.

## Architecture et données

Accueil, collections/catégories, pages par besoin pertinentes, fiches et variantes, panier, checkout, résultat de commande et service client. Inclure livraison/retours et informations commerciales réelles. Les comptes clients ne sont pas obligatoires s'ils n'apportent aucune valeur.

Catalogue central : ID produit/variante, référence exacte, marque, catégorie, caractéristiques/unités, dimensions et compatibilités utiles, médias et droits, prix/devise/taxes applicables, stock, source/date et état de vente. L'offre et le stock de référence viennent du moteur marchand côté serveur ; ne pas utiliser une valeur du navigateur comme autorité du prix.

Un kit peut regrouper des produits cohérents. Chaque pièce reste identifiée et supprimable si le produit le permet. Documenter variantes, exclusions, disponibilité et prix exact. Une image d'ensemble ne prouve pas que chaque pièce est comprise dans le prix.

## Première tranche vérifiable

Catégorie, fiche/variante, ajout au panier, modification, checkout en mode test et commande confirmée côté serveur. Tester aussi variant indisponible, changement de prix/stock, paiement refusé ou interrompu et répétition d'un retour de paiement.

Utiliser les moyens de test du prestataire. Vérifier montant/devise/variante côté serveur, validation de la notification signée, idempotence et absence de double commande. Un retour navigateur vers une page succès ne prouve pas le paiement. Une simple maquette avec boutons ne vaut pas boutique fonctionnelle.

Ne pas effectuer d'achat réel ni envoyer de notifications de test à des tiers sans autorisation adaptée. Si l'accès paiement manque, achever les parties locales autorisées et nommer précisément le blocage du parcours. Ne pas collecter de données de carte dans du code ad hoc.

## SEO et contenu

Navigation HTML des catégories vers toutes les fiches importantes ; les produits ne doivent pas dépendre uniquement de la recherche interne. Traiter facettes/tri/pagination, URLs de variantes, rupture temporaire et retrait définitif selon le contexte, avec des statuts HTTP corrects. Préserver la valeur des anciennes URLs lors d'une migration.

Utiliser `Product`/`Offer` et les règles merchant listings seulement si les données visibles et le rôle vendeur le justifient. Vérifier les politiques actuelles avant toute inscription Merchant Center autorisée. Le balisage ne garantit pas l'affichage enrichi.

Rédiger une aide à l'achat propre : usage, dimensions, compatibilité, compromis, contenu du colis et entretien selon preuves. Ne pas recopier seulement une fiche fournisseur. Ne pas indexer panier, checkout ou données privées.

## Mesure et recette

Vue fiche, variante choisie, ajout/retrait panier, début checkout, paiement/commande confirmés et remboursements si disponibles. Utiliser un identifiant de commande pour éviter le double comptage. Séparer ventes de test, ventes réelles, montant brut, retours et marge.

Contrôles prioritaires : intégrité prix/stock/commande, aucun faux achat confirmé, ergonomie mobile et clavier, erreurs récupérables, politiques exactes, données privées protégées, catalogue découvrable. Les compétences métier du commerce complètent le design de `newsite` ; son périmètre non marchand ne couvre pas ce parcours.
