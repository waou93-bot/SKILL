# Inventaire local HTML

`python scripts/inventory.py CHEMIN_EXPORT` lit récursivement les fichiers `.html` et `.htm` sous un dossier local et écrit un rapport JSON sur la sortie standard ; rediriger vers un fichier dans le dossier du projet si souhaité. `--max-files` et `--max-bytes` bornent le traitement. Python 3.10+ suffit ; aucune installation ni réseau.

Le script utilise `<main>` ou `<article>` lorsqu'il y en a ; sinon le `<body>` hors nav/header/footer/scripts. Il extrait titre, H1/H2, mots, liens et chemins de fichiers. Il ne rend pas JavaScript, ne reconstitue pas les routes du framework, ne crawl pas les sitemaps et ne détecte pas tous les éléments masqués. Contrôler manuellement l'extraction sur chaque type de gabarit. Les liens sont des href bruts et non un graphe d'URL résolues ; ne pas déduire d'orphelines. Les paires les plus proches utilisent Jaccard sur ensembles de mots : c'est une similarité lexicale exploratoire, pas la preuve d'une intention commune, d'un doublon pénalisé ou d'un problème SEO. Les pages trop courtes restent marquées ; les modèles et seuils ne sont pas des règles Google.

Les fichiers qui dépassent la limite, illisibles ou symboliques sont signalés ; une limite de fichiers atteinte indique une couverture partielle. Aucune page non extraite ne devient une page vide réussie. Sortie JSON sur stdout : chemin source, portée, pages, erreurs, couverture et paires candidates. L'outil ne modifie pas le site ; les données de sortie peuvent contenir du texte et nécessitent un stockage adapté à leur confidentialité.

