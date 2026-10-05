# Protocole de recette

## Matrice et preuves

Réutiliser le registre de QA existant. Une ligne par route/gabarit, état, plateforme et environnement : URL finale, version servie ou commit local, navigateur/version, appareil/OS, méthode réelle/émulée/resize, portrait/paysage, viewport, date, critère, observation, statut, preuve/capture et prochaine action. Une dimension inconnue reste inconnue. Pour un correctif, garder référence avant/après et critères rejoués, ne pas écraser l'historique.

Choisir les pages représentant chaque gabarit important et les parcours de conversion ; expliciter routes non couvertes. États pertinents : navigation ouverte/fermée, consentement initial/refus/acceptation/retrait, formulaire vide/invalide/envoi/erreur/succès, tableau large, contenu long, chargement et erreur. Ne pas envoyer un formulaire réel ni déclencher achat/message pour tester sans mandat adapté ; test sandbox ou inspection limitée signalée.

## Contrôles observables

- Rendu : textes lisibles, retour des mots/lignes, titres/CTA sans clipping, espacement, contraste, images/proportions, chargement fontes et absence de saut gênant. Vérifier tableaux/comparaisons : en-têtes, unités, alignement, défilement voulu, contenu accessible et absence de débordement de page involontaire. No Slop/Design DNA servent à préserver les décisions, pas à appliquer un redesign automatique.
- Interaction : toucher/clic, focus clavier desktop, navigation et retour, liens, états busy/disabled, erreurs et succès, menus/chevrons, absence de double action. Le tactile ne se vérifie pas par hover desktop. Inspecter écran et comportement, pas seulement DOM.
- Mobile : portrait et paysage lorsque utiles, zones sûres, barres du navigateur, éléments fixed/sticky, défilement, zoom lisibilité, ouverture du clavier et champ/CTA visible, fermeture/reprise, orientation et conservation de l'état. Tester safe areas/clavier réel uniquement avec plateforme capable ; sinon marquer la limite et étapes manuelles.
- Motion : entrée/sortie, hover/tap distincts, défilement, refresh versus retour home selon politique validée ; reduced motion quand accessible ; animations sans masquer texte/actions ni concurrence gênante. Capture statique ≠ temporalité vérifiée ; conserver séquence/vidéo/observations datées si disponible.
- Consentement/mesure : vérifier mécanisme et réseau/stockage accessible dans contexte autorisé pour choix/refus/retrait et absence de doublons. Classer événements du plan (clic, succès réel, revenu) séparément. Carte Analytics, code/tag présent, requête envoyée, réception DebugView/rapport et lien GA4–GSC sont des preuves différentes. Lecture réseau impossible = observation réseau BLOCKED, pas absence de collecte. Une réception corrélée dans DebugView ou un autre rapport autorisé peut prouver la livraison ; donner un statut séparé à chaque preuve disponible. Ne pas installer un second tracker pour compenser l'outil manquant.

## Comparaison et reprise

Baseline comparable : même route/état/version de contenu, viewport, zoom, fonte et données ; documenter ce qui diffère avant d'attribuer une régression au code. Une différence normale de plateforme n'est pas automatiquement un défaut ; vérifier conséquence pour l'utilisateur. Ne pas accepter un pixel diff seul ni déclarer Human Reading accompli sans inspection des pixels.

Correctif local autorisé → contrôle existant pertinent/build → captures et interaction affectées → relecture comparative → statut. Une correction partagée CSS/menu/consentement invalide les preuves de tous les gabarits/plateformes concernés. Si appareil réel indisponible, fournir étapes, états, résultat attendu et preuve à rapporter ; le manuel en attente reste BLOCKED. Un appareil physique distant fourni par un service peut être `real_device` : vérifier et consigner la session, le modèle/OS et ses capacités réelles. Un simulateur reste simulé ; le nom du service seul ne prouve pas la méthode.

Production : relever URL finale et version effectivement servie, vérifier les parcours autorisés et la politique consentement de cette cible. Diff/version locale ne prouve pas publication ; ancienne version servie = résultat pour cette ancienne version, pas validation du correctif. Préproduction privée/noindex reste protégée.
