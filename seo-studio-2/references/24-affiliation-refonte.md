# Affiliation : produits vérifiés, continuité visuelle et portes de production

Ce contrat s'applique à la création et à la refonte des sites d'affiliation.
Il complète les gates existants et prime sur leurs consignes contradictoires.
Le mode lite conserve toutes ces exigences. Personna reste inchangé.

## Produits : zéro invention

Un produit apparaît dans le site uniquement si sont vérifiés : nom et référence
exacts (variante comprise), page marchand réelle, prix daté avec devise, image
réelle correspondant au modèle, programme d'affiliation actif et lien autorisé.
Sources admises : flux du réseau d'affiliation, API Amazon, page officielle du
fabricant ou du marchand, ouverte et lue pendant la session. Ni mémoire du modèle,
ni extrait de moteur, ni URL simplement citée ne constituent une vérification.
Une page fabricant seule ne prouve ni prix marchand ni programme actif.
Consigner source, date de consultation, éléments observés et preuve du programme.

Chaque produit vit dans un fichier de données, source unique des affichages :
`id`, `nom`, `marque`, `modèle`, `source_url`, `lien_affilié`, `image_url`,
`prix`, `date_prix`, `date_vérification`, `statut` sont obligatoires.
Ajouter la devise explicite ; dates ISO, prix numérique fini et non négatif.
Un adaptateur de noms de champs existants doit être explicite et testé.
Un champ absent, vide ou incohérent rend le produit non publiable.
Le statut VERIFIE exige des preuves ; A_VERIFIER et NON_TROUVE restent hors site.

Installer un contrôle prébuild dans chaque projet et le brancher à sa commande
réelle de build. Il échoue pour tout produit utilisé si :
- un champ obligatoire manque, notamment source_url ou lien_affilié ;
- une source ou un lien affilié aboutit à autre chose que HTTP 200 ;
- une image est absente, inaccessible ou ne se charge pas ;
- un prix de plus de 30 jours n'a pas d'avertissement visible ;
- référence exacte, image réelle ou affiliation active ne sont pas vérifiées.

Conserver les redirections des réseaux : un 302 intermédiaire est permis si la
destination finale est 200 et correspond à la référence. Un 200 sur une erreur,
un défi anti-bot ou une page générique ne constitue pas un succès. Refus d'accès,
timeout ou contrôle impossible restent NON VERIFIES et bloquent le produit.
Un prix ancien affiche sa date et son avertissement dans chaque usage ; il ne
doit pas être présenté comme actuel dans la page ou ses données structurées.
Ne pas considérer une simple empreinte de fichier comme preuve de vérité.

Pour un produit introuvable : écrire `produits-non-trouves.md` avec référence,
sources consultées, manque et question à résoudre, puis demander à l'utilisateur.
Ne pas remplacer par un équivalent plausible. Interdits dans les pilotes et le
site livré : placeholders produit, produits fictifs, images trompeuses,
caractéristiques approximatives, avis inventés et faux tests.
Les fixtures synthétiques de tests restent isolées du catalogue publié.

## Produits et accès affiliés dès l'entrée du site

Pour un site d'affiliation, la landing et l'accueil mettent les produits vérifiés
et les accès affiliés en avant dès le premier écran utile, après une introduction
courte qui répond au besoin. Pas de long hero ou de mur de texte avant la sélection,
ni de parcours obligatoire par un guide pour accéder aux offres.
Présenter images réelles, noms/références, prix datés, utilité et CTA « Voir le prix »
ou « Voir le modèle sur [marchand] ». Le CTA ouvre directement l'offre exacte via
le lien affilié autorisé ; conserver tracking, variante et balisage sponsored.
Les liens commerciaux externes ouvrent un nouvel onglet avec noopener ; les ancres
éditoriales continuent de servir prioritairement le maillage interne du site.
La mention commune d'affiliation reste au footer/mentions légales ; ne pas ajouter
une formule de commission à chaque bouton. Une grande zone cliquable ne doit pas
masquer les liens internes, créer des liens imbriqués ou rendre le clavier inutilisable.

Respecter le design system approuvé et soumettre ce placement à sa validation en
phase 1. Si la V1 nécessite un changement de composition, présenter l'ajustement
localisé demandé, sans étendre cette demande à une refonte graphique globale.
Sans produits et liens vérifiés disponibles, bloquer le module et la livraison
affiliée ; jamais de faux produit ou CTA décoratif pour remplir le premier écran.
Inclure la landing parmi les trois pilotes. En QA, captures desktop/mobile et test
réel des CTA démontrent visibilité précoce, destination exacte et images chargées.
Une landing sans mise en avant produit ou accès affilié utilisable échoue à la recette.

## Design : migrer avant de réinventer

Pour l'existant, avant tout code : crawl et inventaires contenu/produits, puis
captures desktop et mobile de huit pages types représentatives. Enregistrer URL,
date et dimensions. Si le site offre moins de huit types ou si la V1 est inaccessible,
documenter cette limite et demander la couverture adaptée ; ne pas inventer des pages.
Extraire dans `design-system.md` palette, typographies, espacements, compositions,
cartes produit, en-tête, pied de page, tableaux, ton et qualité perçue.
Lier ce document au PROJECT_SKIN.yaml existant ; ne pas créer de décisions concurrentes.
La V2 reprend ce système. Une rupture nécessite une demande explicite de l'utilisateur.
Une optimisation SEO ne vaut pas autorisation de changer le design.

Pour un nouveau site : deux directions visuelles avec références réelles consultées
et maquettes desktop/mobile, attente du choix utilisateur, puis gel du design system
avant le code des pages. Charger Design DNA avant la production visuelle.
Interdits : template générique, carte sans image réelle, mur de texte, absence de
hiérarchie visuelle. Les choix de détails restent conformes au système approuvé.

## Éditorial, architecture et migration

Conserver silos, maillage, pSEO pertinent, Astro/Cloudflare lorsqu'ils sont retenus,
et les URL existantes. Si une URL change, mapper puis tester sa redirection 301 vers
une destination pertinente, sans boucle ni chaîne inutile ni report global sur l'accueil.
Le pSEO complète l'éditorial. Piliers, verdicts et comparatifs reprennent le ton de
la V1, ou le ton approuvé du nouveau site. Interdire le texte répétitif en masse.
Une page programmatique indexable exige trois éléments propres et utiles : verdict
spécifique rédigé, comparaison chiffrée sourcée, critère d'usage spécifique.
Une substitution de noms ne suffit pas. Sinon noindex, retrait du sitemap indexable,
sans empêcher le crawl de la directive. Noindex n'autorise jamais des faits inventés.

## Six phases, intégrées aux gates existants

| Phase | Preuves à livrer avant transition |
|---|---|
| 0 — Audit | Crawl, contenu, produits, huit pages desktop/mobile et risques de migration ; pour un nouveau site, absence d'existant documentée et besoins sourcés. F0/F1, G0/G1. |
| 1 — Design | Design system, références ou directions, validation explicite de l'utilisateur liée à la version du document. G2/G3 et prérequis SERP conservés. |
| 2 — Produits | Base vérifiée, sources datées, produits non trouvés, contrôle prébuild branché et testé. Complète G3/G4 avant les pages pilotes. |
| 3 — Pilotes | Trois pages réelles représentatives, templates testés, produits réels, comparaison visuelle et contrôles éditoriaux. Pilote D0–D4. |
| 4 — Lots | Lots de 20 à 30 pages, contrôle de chaque lot avant le suivant ; dernier lot plus petit permis. D2/D3 itératifs. |
| 5 — QA | Recette, corrections et nouvelle vérification, preuves G5/G6 et D4 ; publication D5 autorisée séparément. |

Ne pas démarrer le code avant l'audit ni coder les pages avant validation du design
et de la base produits. Les maquettes de phase 1 sont des prototypes de conception,
pas une production anticipée des pages. Les pilotes peuvent couvrir plusieurs gates
documentaires ; la recette finale porte sur tout le corpus, pas seulement trois pages.
Consigner livrables, contrôles, résultats, versions et preuves à chaque porte.
Une modification invalide les preuves affectées. Ne pas avancer sans la preuve de
la phase précédente. La validation humaine de phase 1 ne peut être déléguée à un agent.
Terminer chaque phase par : **Ce qui est fait — Ce qui est vérifié — Ce qui manque.**

## QA et livraison

Chaque template : captures desktop/mobile, comparaison côte à côte avec V1 quand
elle existe, autocritique écrite (hiérarchie, densité, images, composants, lisibilité,
mobile), corrections puis nouvelles captures avant présentation finale.
Dans `11_QA.md`, rapporter : produits vérifiés/total prévu et total publié, liens
affiliés testés et destinations, images chargées, Lighthouse avec pages/conditions,
balisage validé avec périmètre du contrôle, redirections testées et anomalies,
captures, autocritique, corrections et résultats de nouvelle recette.
Appliquer les skills QA/sécurité/performance existants ; émulation mobile ne vaut
pas appareil réel, TBT ne vaut pas INP, validation partielle ne vaut pas certification.
Aucun outil payant obligatoire. Un outil absent ne devient pas un test réussi.

Démontrer le prébuild avec un produit valide (PASS), puis champ manquant, lien en
erreur, image absente, prix ancien sans avertissement (FAIL). Ajouter prix ancien
avec avertissement réellement affiché (PASS), variante erronée et source non lue (FAIL).
Les contrôles de ce package restent distincts de ce prébuild propre au site :
`studio.py validate` ne vérifie pas automatiquement ce catalogue ou le rendu.

Si un critère échoue : corriger puis rejouer ; ne pas livrer comme terminé en
reléguant le défaut en fin de message. Si un accès ou une donnée manque, maintenir
la phase BLOQUEE, expliquer ce qui manque et demander, sans fabriquer de réussite.
Une consigne ambiguë exige une question avant le travail qui en dépend ; poursuivre
les tâches indépendantes. Garder la mention commune d'affiliation footer/mentions
légales et les règles de liens existantes ; aucune répétition automatique par CTA.
