# Audit technique : preuves et critères

Un audit est une observation datée d'un périmètre, pas un certificat SEO. Adapter la
profondeur à la taille et aux enjeux. Prioriser modèles de pages et URL déjà utiles.

## Accès, découverte et indexabilité

Vérifier statuts HTTP réels, redirections/boucles, 4xx/5xx, robots.txt, meta robots,
X-Robots-Tag, accès anonyme aux ressources, liens HTML et sitemap. Comparer réponses
initiales et rendu si des fonctionnalités dépendent de JavaScript. [S05, S07]

Robots.txt contrôle le crawl : il n'est ni un dispositif de confidentialité ni une
méthode fiable de désindexation. Un robot empêché de lire une page peut ne pas voir
son noindex. Pour des données privées, utiliser une vraie protection d'accès. [S05]

Contrôler les canonicals et la cohérence avec redirections, liens et sitemap ; une
canonical est un signal, pas une garantie du choix de Google. Pas de canonical de
chaque page vers l'accueil ; pas de conflits vers une URL non indexable. [S06]

Vérifier l'indexation via les données moteur lorsqu'accessibles. Un 200, un sitemap,
un title, une requête site: ou un test d'accessibilité ne démontrent pas à eux seuls
l'indexation de toutes les URL. [S01, S02]

## Sites JavaScript et expériences immersives

Comparer HTML source, DOM rendu, texte essentiel, liens href, navigation et réponses
404. Identifier ce qui exige clic/scroll/connexion avant apparition. Ne pas conclure
que React est invisible ni qu'un moteur exécute toute interaction utilisateur. [S07]

Préserver l'animation, la 3D et la DA : rendre l'offre, les informations essentielles
et les liens accessibles dans une structure sémantique utilisable par tous. Une
expérience WebGL peut coexister avec des pages dédiées. Ne pas ajouter du texte
hors écran exclusivement destiné à manipuler les moteurs. [S04]

## Expérience et mesure des performances

Séparer un test laboratoire (Lighthouse et conditions simulées) et le vécu terrain
(CrUX/RUM si disponible). Consigner date, appareil, réseau, gabarit et nombre de tests.
Core Web Vitals : repères officiels consultés LCP <= 2,5 s, INP <= 200 ms, CLS <= 0,1 ;
analyser au 75e percentile et vérifier les définitions actuelles lors d'une exécution.
Un bon résultat n'assure pas un bon classement. [S08]

Contrôler aussi mobile, lisibilité, liens, formulaires/CTA, erreurs, obstruction par
popups, images/vidéos et navigation clavier. Distinguer bénéfice UX/accessibilité et
facteur de classement officiellement documenté. Ne pas attribuer un bonus SEO à tout.

## Métadonnées et données structurées

Titres descriptifs, adaptés aux pages ; descriptions utiles ; headings cohérents ;
alt pertinent (vide pour éléments purement décoratifs selon le cas), images de qualité.
Aucune longueur magique ; un title/meta proposé peut être réécrit dans le résultat.
Les données structurées décrivent le contenu visible et réel, avec type éligible
actuel. Le test valide du balisage ne garantit pas un résultat enrichi. [S02, S12]

## Migrations et refontes

Lire [le modèle migration](../assets/10-migration.md). Cartographier anciennes/nouvelles
URL ; décider conserver, mettre à jour, fusionner, rediriger vers un équivalent ou
retirer lorsque justifié. Pas de redirection en masse vers l'accueil. Réviser liens,
sitemaps, canonicals et versions linguistiques ; tester staging et production séparément.
Sauvegarder et prévoir rollback avant un changement engageant. Contrôler l'accès
après mise en ligne et surveiller les signaux sur une durée adaptée. [S10, S11]

La staging peut volontairement ne pas être indexable ; ne jamais la rendre publique
pour passer un test. La production ne doit pas hériter involontairement d'un blocage.

## Chutes de trafic

Vérifier collecte/mesure, disponibilité, indexation, changement technique, requêtes,
pages, pays, saison, SERP, sécurité et éventuels messages Search Console. Consulter
les annonces moteur pour la période. Une coïncidence avec une mise à jour n'établit
pas sa cause. Ne pas recommander un désaveu de liens ou une purge sans preuve. [S09]

Statuts des checks : PASS, FAIL, NON_VERIFIE, NON_APPLICABLE. Chaque FAIL possède
preuve, URL/environnement, impact, correction proposée et test d'acceptation.
Sources : [bibliographie](sources.md).
