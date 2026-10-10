# 15 Choisir et écrire une technique caméra

Ouvrir pour un POV, une révélation, un faux plan-séquence, un raccord masqué,
un raccord de forme ou de mouvement, ou un effet spatial ou temporel demandé.
Pour le cadrage courant, rester dans `01-write-shot.md`. Pour une signature
de réalisateur, commencer par `13-director.md` et ses sources.

**Statut : hypothèses de prompting**, adaptées de « Master Cinematic Technique
Toolkit » et « Master Director Camera Movement Toolkit », fournis par
l'utilisateur, auteurs et dates inconnus. Leurs qualificatifs « tested and
proven » et leurs classements de difficulté ne sont pas des preuves : aucun
protocole, modèle, réglage ni rendu n'est joint. Cette fiche décrit une cible
visuelle, pas une capacité Seedance garantie.

## Sommaire

- Sélectionner par résultat visible
- Identifier ce qui change
- Révéler un élément déjà présent
- Relier deux images
- Temps et espace demandés
- Deux fragments de traduction

## Sélectionner par résultat visible

Choisir le mécanisme qui sert le brief ; ne pas déduire automatiquement une
caméra, une palette ou une musique d'une émotion ou d'un nom de réalisateur.
Un choix de mise en scène n'est pas une contrainte technique du moteur.

| Résultat demandé | Information à écrire | Autorité existante |
|---|---|---|
| Voir à travers les yeux d'un sujet | Porteur du point de vue, hauteur, direction, membres visibles si demandés | `01`, puis `01b` pour le mouvement |
| Accompagner un sujet | Caméra devant, derrière ou de côté ; écart maintenu ou variable ; destination | `01`, `01c` pour la vitesse |
| Découvrir ce qui était masqué | Élément déjà présent, masque, mouvement qui le dévoile, cadre d'arrivée | Section révélation ci-dessous |
| Déplacer l'attention par le point | Cible nette au départ, cible à l'arrivée, ce qui devient flou | `01`, Traduire un terme |
| Traverser une ouverture | Trajet, ouverture libre, espace d'arrivée et continuité de direction | `01`, spec caméra ; `05`, Ce que ça ne règle pas, qui borne l'ancrage sur un trajet multi-espaces |
| Cacher une coupe | Masque ou flou complet et conditions de raccord des deux côtés | Section raccord ci-dessous |
| Raccorder une forme ou une action | Correspondance visible de part et d'autre d'une coupe déclarée | Section raccord ; `03` |
| Faire varier le temps ou l'espace | Éléments affectés, régime temporel, départ et arrivée | Dernière section ; `13` pour les limites |

## Identifier ce qui change

Distinguer **trajet caméra**, **orientation**, **mise au point**, **focale**,
**vitesse du sujet** et **vitesse de restitution**. « Plus rapide » ne dit
pas lequel change. Un changement de point n'est pas un travelling ; un
panoramique ne déplace pas le centre de la caméra comme un travelling latéral.

Écrire le mouvement principal avec les cinq points de `01`, puis uniquement
le modificateur utile. Un arc avec texture portée reste un trajet et une
texture, voir `01c`. Ne pas empiler trois trajets parce qu'un catalogue
autorise trois mots-clés.

Un **POV humain** nomme la personne dont la caméra prend la place. La caméra
ne montre pas simultanément son visage depuis l'extérieur, sauf reflet
explicitement demandé et géométriquement préparé. Les mains ne sont pas
obligatoires ; éviter de les ajouter automatiquement. Une caméra embarquée
sur une voiture n'est pas implicitement le regard de son conducteur.

Un terme de catalogue garde sa traduction visible selon `01`, pas sa promesse
de résultat. Un nom de réalisateur demeure soumis à la recherche de `13` :
les « écoles » des sources ne dispensent pas de vérifier l'attribution.

## Révéler un élément déjà présent

Placer l'élément révélé **avant** sa découverte : derrière un pilier, dans
une zone floue du fond, hors champ à un emplacement défini. Nommer ce qui
change pour qu'il devienne visible, puis l'état où la caméra le laisse.

Pour une révélation par déplacement, conserver la géographie. Pour une
révélation par mise au point, conserver l'élément dans le cadre avant le
transfert de netteté. Un élément hors champ ne peut pas entrer dans l'image
par le seul changement de point.

Ne pas transformer un élément qui se dévoile en apparition magique, ni en
nouveau protagoniste ajouté au brief. La continuité pendant l'occultation
reste régie par `01b`, Continuité sous occlusion. Si le sujet hero doit rester
visible, choisir une révélation qui respecte son verrou de présence.

## Relier deux images

Décider d'abord ce qui est produit : un passage dans un espace continu, une
coupe dissimulée entre deux prises, ou une transformation du monde. Ces trois
opérations ne partagent pas le même contrat. Une coupe invisible reste une
coupe ; « faux plan-séquence » ne signifie pas prise unique réelle.

| Raccord | Conditions à porter des deux côtés |
|---|---|
| Masque par pilier ou objet | Masque couvrant tout le cadre au raccord, direction de passage, vitesse apparente, échelle, lumière et état du sujet |
| Whip pan masquant une coupe | Sens et vitesse du balayage, flou de raccord compatible, cible d'arrivée et moment où elle devient lisible |
| Match cut de forme | Forme, position dans l'image, orientation et taille apparente correspondantes ; coupe explicite |
| Match on action | Phase du geste avant et après coupe, main ou objet inchangé, direction d'écran ; l'action se poursuit sans repartir |

Pour deux clips existants **déjà raccordables**, donner les points de coupe
et l'ordre de montage, sans créer de vidéo intermédiaire. Si un passage manque
et doit être généré, appliquer le **mode Transition** de `06-edit-extend.md`,
ses rôles et son gabarit ; l'intention de tâche y reste obligatoire pour être
reconnue, et les verbes déclencheurs documentés ne couvrent que l'édition et
l'extension. Pour deux générations séparées, écrire
l'état de sortie de A et l'état d'entrée de B, puis annoncer l'assemblage au
montage ; ne pas promettre une jointure au pixel.

Garder l'audio voulu : raccord continu si demandé, ou rupture motivée par la
coupe. Aucun « caméra rapide = son fort », aucune musique interdite par
défaut. Un flash, un flare ou un morph ne vient pas automatiquement masquer
un raccord ; ce sont des effets à choisir dans le brief et à arbitrer avec `12`.

## Temps et espace demandés

Ralenti, speed ramp, gel avec caméra mobile, inversion temporelle, passage
à travers une paroi, portail : les traiter comme des effets **demandés**,
avec une portée explicite. Ne pas les importer dans un plan réaliste parce
que la source les associe à l'action ou à un réalisateur.

Nommer ce qui change et ce qui reste dans son régime : sujet ralenti,
particules figées, caméra mobile, audio conservé ou transformé. Décrire
l'état initial, le déclencheur et l'état final. Ne pas faire tomber en fin
de prompt un `no slow motion` ou `no cuts` qui interdit l'effet choisi.

Pour les capacités non documentées et les cadences mélangées, conserver
l'arbitrage de `13`, La table de traduction : hypothèse explicitée, montage
proposé lorsque nécessaire. Le catalogue n'étend ni les modes ni les durées
de `07-spec.md`. Ne pas inventer les secondes manquantes des exemples tronqués.

## Deux fragments de traduction

**Révélation dans un même décor**, si le brief donne un pilier et une porte
déjà ouverte derrière lui :

```text
The open doorway is already behind the pillar, hidden from the starting
view. The camera tracks to screen-right at eye level; the pillar slides
left across the foreground, progressively uncovering the doorway. The
move ends with the doorway fully visible and the pillar at the left edge.
```

**Raccord sur un geste**, si le brief demande une coupe pendant une fermeture :

```text
Shot 1 ends as her right hand lowers the lid halfway, the hand travelling
screen-left to screen-right. Cut to Shot 2, tighter and from her left, the
camera staying on the same side of the action: the same right hand continues
lowering the same half-closed lid in the same screen direction until it meets
the box. The closing sound lands on that contact.
```

Fragments uniquement : reprendre format, références, taille, optique, lumière
et look dans le prompt complet selon `SKILL.md`. Ces exemples ne commandent
aucun titre, effet sonore supplémentaire, négatif générique ni changement
de palette.
