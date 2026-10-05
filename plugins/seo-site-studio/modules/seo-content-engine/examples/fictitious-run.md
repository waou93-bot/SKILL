# Exemple intégral en mode draft

Atelier Vélo est une entreprise fictive de Lyon. Toutes les observations, coûts, sources internes, domaines et chiffres ci-dessous sont fictifs; aucune donnée n'a été collectée et aucun CMS n'a été utilisé.

Le fichier run.json et les fichiers JSON individuels contiennent configuration et neuf sorties conformes aux contrats. Audit partiel: inventaire pédagogique, contrôles techniques et vitesse inconnus. Opportunité: préparation d'une visite atelier, aucune métrique SEO disponible. Même intention déjà couverte: mettre à jour /entretien. Calendrier du 5 octobre au 3 novembre 2026: rédaction/revue le 8, bilan le 29, coût fictif 180 EUR sur 200 EUR disponibles. Brief B1: checklist atelier et conversion vers diagnostic; étude concurrentielle indisponible.

ArticlePackage.json contient l'article complet avec titre, meta, slug, liens, CTA, image/alt et registre des affirmations. Sa preuve E1 est fictive. ValidationReport est bloqué: preuve fictive, liens non vérifiés, revue du mécanicien absente. PublicationRecord indique local_draft, zéro tentative distante, aucun identifiant ni URL publique. BacklinkOpportunity est une suggestion fictive auprès d'une association, sans contact et sans réseau de sites.

PerformanceReport simule 100 puis 130 sessions mais aucune publication réelle; campagne simultanée et périodes imparfaitement alignées empêchent une conclusion causale. Visibilité, conversions et IA sont inconnues. Prochaine action: recueillir sources réelles, auditer le site et connecter les services autorisés avant de passer de la démonstration au programme réel.

Pour contrôler: node scripts/validate.cjs ArticlePackage examples/ArticlePackage.json. Le contrôle éditorial node scripts/check-package.cjs examples/ArticlePackage.json examples/Config.json doit échouer sur la preuve fictive: c'est le comportement attendu.
