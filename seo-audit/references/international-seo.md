# International SEO : langues et régions

Révision : 8 octobre 2026. Source Google primaire ; aucun effet global de classement n'est déduit d'une simple erreur de balisage.

## URL et contenu

Préférer une URL distincte pour chaque langue. ccTLD, sous-domaine et sous-répertoire répondent à des contraintes différentes ; un préfixe pour toutes les langues n'est pas obligatoire. Une langue par défaut à la racine est valide. Google identifie surtout la langue du contenu visible ; `lang` reste utile pour l'accessibilité. Une traduction du menu seul ne localise pas un contenu principal inchangé.

Éviter les redirections imposées par IP/langue et proposer des liens de choix. Googlebot explore principalement depuis les États-Unis, mais aussi depuis d'autres pays, généralement sans Accept-Language. Ne pas déduire que toutes les variantes négociées ont été explorées. [Sites multirégionaux](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites?hl=fr), [pages adaptatives](https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages).

## Hreflang

- HTML, en-tête HTTP et sitemap sont des méthodes équivalentes. Plusieurs méthodes n'apportent pas de bénéfice de recherche supplémentaire et augmentent la maintenance ; vérifier leur cohérence si elles coexistent.
- URL absolues, codes de langue valides, région/script facultatifs. Utiliser `en-GB` pour le Royaume-Uni. Chaque ensemble déclaré comprend sa propre page et les variantes correspondantes.
- Vérifier les liens retour. Une relation sans réciprocité peut être ignorée ; ne pas déclarer automatiquement toutes les variantes ignorées. Examiner le sous-ensemble réellement réciproque.
- `x-default` est facultatif, recommandé lorsqu'une page de sélection ou un repli convient. Son absence seule n'est pas un défaut bloquant.
- Contrôler accès HTTP, indexabilité voulue, destinations, canonique et contenu. Classer la conséquence selon preuves, pas par affirmation de cluster entièrement rejeté.

[Versions localisées](https://developers.google.com/search/docs/specialty/international/localized-versions?hl=fr).

## Canonique et sitemap

Une traduction réelle dans une autre langue n'est généralement pas un doublon du même contenu. Pour des variantes régionales très proches dans la même langue, une canonique préférée combinée à hreflang peut être adaptée. Ne pas exiger aveuglément une canonique autonome pour toute région ; ne pas canoniser toutes les traductions réelles vers une seule langue. Comparer choix souhaité et canonique Google dans la version indexée.

Dans un sitemap hreflang, déclarer `xmlns:xhtml` et les variantes, y compris la page elle-même. Les enfants `xhtml:link` ne comptent pas comme URL pour la limite de 50 000 ; le fichier reste soumis à 50 Mo non compressés. Calculer la taille réelle, sans imposer une limite arbitraire de 2 000–5 000. Répartition par locale ou type possible selon gestion et taille. Vérifier la sortie du framework installé plutôt que supposer son comportement.

[Canonique](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls?hl=fr), [sitemap localisé](https://developers.google.com/search/docs/specialty/international/localized-versions?hl=fr).

## Qualité et diagnostic

Contrôler contenu principal traduit, exactitude, monnaie, coordonnées et utilité locale. Les traductions automatisées ne sont pas interdites par principe ; une production à grande échelle sans valeur peut relever du spam. Conserver les exclusions intentionnelles ; `noindex` peut être légitime pour une page non destinée à la recherche, mais ne sert pas à forcer un choix canonique.

Google combine surtout des signaux par page et certains signaux de site ; ne pas annoncer une sanction globale à partir de quelques pages faibles. Dater inspection, données par langue/pays et déploiement. Documenter pour chaque anomalie : URL, méthode, relation affectée, preuve, impact probable et correction proportionnée.

[Spam](https://developers.google.com/search/docs/essentials/spam-policies?hl=fr), [signaux](https://developers.google.com/search/docs/appearance/ranking-systems-guide?hl=fr), [exclusions](https://developers.google.com/search/docs/crawling-indexing/control-what-you-share?hl=fr).
