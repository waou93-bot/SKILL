# Routeur de stack

## Décision

Choisir la stack après le Contrat de conversion. Noter le besoin qui justifie la décision, les options écartées et les dépendances admises dans le Toolbox snapshot.

| Situation observée | Stack | Décision |
| --- | --- | --- |
| Site vitrine, portfolio, démonstrateur, pages éditoriales | Astro + TypeScript + CSS natif | Défaut |
| Interaction isolée qui facilite une preuve ou le contact | Astro + îlot Svelte | Ajout ciblé |
| Authentification, état complexe, étapes métier, formulaires serveur | SvelteKit | Sur preuve de besoin |
| Écosystème React existant ou besoin serveur/CMS validé | Next.js | Exception justifiée |
| Concept interne très court | HTML/CSS | Prototype déclaré non livrable |

Astro peut rendre des pages statiques et hydrater seulement les composants interactifs nécessaires. Référence : https://docs.astro.build/en/concepts/islands/

## Règles

- Pas de React et Svelte dans le même projet sans besoin documenté.
- CSS natif avant dépendance visuelle.
- Une bibliothèque de composants ne sert pas de point de départ. Vérifier sa compatibilité, sa licence, son état de maintenance et son adaptation locale avant intégration.
- Les versions ne sont figées qu'au moment où le projet installe réellement ses dépendances.
- Un concept HTML ne devient pas un site de production par simple changement de nom.

## Mouvement

- CSS ou Web Animations API est le choix courant.
- Utiliser une bibliothèque de mouvement seulement si l'interaction ne peut pas rester simple et testable.
- Charger svelte-motion-effects seulement pour un mouvement Svelte utile.
- Un mouvement explique une hiérarchie, une séquence, un retour d'action ou un changement d'état.
- Toute animation a un état réduit sous prefers-reduced-motion. Référence : https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion

## Cas de refus

Revenir au cadrage si :

- la stack est choisie pour imiter une esthétique ;
- l'interaction ne facilite ni preuve ni contact ;
- le projet ajoute plusieurs frameworks pour une page simple ;
- une dépendance n'a pas de licence, de raison ou de propriétaire identifié.
