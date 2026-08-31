# Routage et contrôle de livraison

## Sélectionner l’adaptateur de stack

Lire seulement la ligne correspondant à la stack validée dans le MASTER. Aucun adaptateur ne permet d’ajouter un framework non retenu.

| Stack validée | Skills et contrôles à charger | Limite |
| --- | --- | --- |
| Astro + TypeScript + CSS natif | `webapp-testing`, `web-design-guidelines`, skills de design validés | Aucun îlot par défaut ; ajouter Svelte seulement pour une interaction de preuve ou de contact déjà justifiée. |
| Astro + îlot Svelte | Adaptateur Astro, puis `svelte-ui-compose` ou `svelte-motion-effects` pour l’îlot concerné | L’îlot reste isolé et justifié dans le Toolbox snapshot. |
| SvelteKit | `svelte-ui-compose`, puis `svelte-data-tables` ou `svelte-motion-effects` seulement si le parcours l’exige | Réservé à l’état métier, à l’authentification ou au formulaire serveur confirmés. |
| Next.js + React | `webapp-testing`, `web-design-guidelines`, skills React/Next compatibles avec l’architecture retenue | Ne pas introduire Svelte. Documenter le besoin React ou serveur qui motive l’exception. |
| HTML/CSS de concept | Contrôles statiques, `web-design-guidelines` et revue manuelle | Prototype déclaré non livrable, sans dépendance ou interaction simulée. |

Le socle commun est le plus petit ensemble qui couvre la tranche verticale. Une bibliothèque d’interface ou de mouvement n’est jamais chargée pour imiter une esthétique.

## Contrat de la tranche verticale

Une tranche est prête à être étendue quand :

- son entrée et sa sortie sont compréhensibles sans explication externe ;
- l'action principale fonctionne au clavier et sur écran étroit ;
- les états importants sont présents ;
- le build et les contrôles statiques passent, ou les échecs sont attribués ;
- les textes visibles sont directs et cohérents ;
- les dépendances et ressources intégrées ont une provenance connue ;
- les écarts au MASTER sont consignés.

## Contrôle avant livraison

Vérifier au minimum :

1. Routes, liens, navigation et page introuvable.
2. Largeurs mobile, tablette et bureau utiles au projet.
3. Ordre des titres, libellés, focus visible et navigation clavier.
4. Chargement initial, images, polices et absence de déplacement de mise en page évitable.
5. Métadonnées de base, aperçu social et contenu indexable si le site est public.
6. Variables d'environnement, secrets absents du client et messages d'erreur non sensibles.
7. Comportement avec réduction des animations.
8. Build de production et démarrage local du résultat construit quand le projet le permet.
9. Mesure de l’action principale, ou déclaration explicite qu’elle est hors périmètre à ce stade.
10. Pour un formulaire ou une collecte : destinataire, transfert, consentement, durée de conservation, protection anti-abus et état d’échec réellement testés.
