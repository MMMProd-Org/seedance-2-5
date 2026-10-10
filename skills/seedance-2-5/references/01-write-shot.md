# 01 Écrire un plan

Tout ce qui sert à écrire un plan unique : la caméra et la composition. Le
mouvement du sujet et sa physique vivent dans `01b-motion-physics.md`, la queue
de contraintes qui protège le résultat dans `12-constraints.md`.

À ouvrir dès qu'on écrit un prompt de génération, quel que soit le mode.

---

## Sommaire

- La spécification en cinq points
- Vocabulaire lu directement
- Tenir une taille de plan et une composition
- Le ratio vertical
- Techniques qui demandent une précision de plus
- Traduire un terme que le modèle peut ignorer
- Objets en amorce
- Position dans le cadre et déclencheur
- Le verrou de présence du sujet
- Séparer caméra et sujet
- Plan caméra segmenté
- Lumière
- Variantes de campagne
- Faible contre fort

Le mouvement et la physique ont été scindés dans `01b-motion-physics.md`, la
queue terminale dans `12-constraints.md`. Ouvrir leurs sections selon le besoin
repéré dans la table de `SKILL.md`, sans chargement systématique des trois fiches pour un plan
qui ne comporte ni action physique à diriger ni contrainte à ajouter.

---

## Caméra

### La spécification en cinq points

Un mouvement caméra dirigé se compose de :

1. taille du plan de départ,
2. hauteur et angle de la caméra,
3. **un** mouvement principal,
4. taille du plan final,
5. le pas, ou ce qui règle la vitesse.

> Start on an eye-level wide shot, six meters ahead of the courier. The camera
> dollies backward at her walking pace, then makes a gentle arc to the right when
> she reaches the stall, ending on a stable tight medium. No cuts, no handheld
> shake, no orbit.

Le point d'arrivée est ce qui manque le plus souvent. « slow push in » ne dit pas
où ça s'arrête ; « slow push in from a mid-shot down to a tight close-up on the
laces » le dit.

**La queue de cet exemple lui appartient.** `No cuts, no handheld shake, no
orbit` verrouille la stabilité de ce travelling-là. Recopiée dans un plan qui
demande de la nervosité ou une caméra portée, elle l'interdit, et c'est un des
reports de queue que la checklist de réémission de `SKILL.md` traque. Section
Le plan nerveux de `01c-action.md`.

---

### Vocabulaire lu directement

**Tailles** : extreme wide, wide, medium wide, medium, medium close-up,
close-up, extreme close-up.

**Mouvements** : push in, dolly in, pull out, dolly out, truck left/right, pan,
tilt up/down, crane, boom, arc, orbit, follow, tracking, dive, handheld shake,
locked-off, static.

**Angles** : low angle, eye level, high angle, overhead, top-down, first person.

**Focus** : rack focus, slide focus, shallow depth of field.

| Terme | Effet | Intention |
|---|---|---|
| `static` / `locked-off` | Rien ne bouge côté caméra | Laisser l'action porter le plan |
| `push in` | La caméra avance | Finir sur un détail |
| `pull out` | La caméra recule | Révéler le contexte |
| `orbit` / `arc` | Trajectoire circulaire | Révéler une seconde face sans toucher la lumière |
| `truck left/right` | Déplacement latéral | Longer un espace ; précision de plus, table des techniques ci-dessous |
| `pan` / `tilt` | Pivot depuis un point fixe | Balayage, changement de direction du regard |
| `crane` | Montée ou descente dans l'espace | Changement d'échelle |
| `follow` / `tracking` | Épouse l'allure du sujet | Le monde dérive derrière |
| `handheld shake` | Instabilité délibérée et petite | Texture documentaire |
| `dive` | Plongée rapide vers ou dans le sujet | Entrée dans un espace |

---

### Tenir une taille de plan et une composition

Une taille nommée, `wide shot`, est lue, mais elle n'est pas tenue. Le modèle
cadre ce qu'on lui décrit, et il ramène la caméra sur l'élément le plus détaillé
du prompt : trois lignes sur les yeux dans un plan large produisent un plan
moyen. C'est le corollaire du verrou de présence appliqué à la distance : **la
longueur consacrée à un élément est aussi une consigne de taille de plan.**

Trois clauses tiennent une taille, et la troisième est celle qu'on oublie.

1. **La géométrie visible**, pas l'étiquette seule : ce qu'on voit du corps, la
   part de cadre qu'il occupe, l'air autour, ce que le décor remplit. Même
   bascule que pour un terme caméra rare : garder le terme et le traduire en
   changement visible.
2. **Le niveau de détail accordé à la taille.** En plan large, le jeu s'écrit
   dans le corps : poids, allure, distance, orientation des épaules, ce que les
   mains portent. Les yeux ne se lisent pas à cette distance, et les écrire tire
   la caméra vers eux. En plan serré, l'inverse : les yeux portent, le décor se
   tait. Voir la section Les yeux sont le canal de `02a-perform.md`.
3. **La clause de maintien**, si l'échelle doit rester constante : nommer la
   distance caméra–sujet tenue et la taille finale. Si le sujet s'éloigne d'une
   caméra fixe, sa taille diminue ; conserver alors ce changement voulu et
   garantir seulement qu'il reste entier. Une taille de plan ne verrouille
   pas automatiquement toutes les distances.

| Faible | Fort |
|---|---|
| `Wide shot of a woman in an empty warehouse. Her eyes search the darkness and a flicker of fear crosses her face as she walks to the door.` | `Wide shot: her full figure is visible from head to feet, about a third of the frame height, small against the warehouse that fills the rest of the frame, empty floor below her and roof trusses above. She walks away from the camera toward the far door at a steady pace, shoulders squared, arms still at her sides. The camera is locked off and does not move or push in; she grows smaller as she recedes and ends about a quarter of the frame height, near the door, still whole.` |

`does not push in` est une négation de structure temporelle : elle mord, voir
`12-constraints.md`. Elle ne remplace pas la géométrie, elle la protège.

**Une composition se décrit en quatre valeurs**, et une composition imposée par
le brief les porte toutes les quatre, chacune en positif :

| Valeur | Faible | Fort |
|---|---|---|
| Angle de vue du sujet et hauteur caméra | `side view` | `the car is seen in exact side profile, its long axis parallel to the frame edges, the lens twenty centimetres above the asphalt, level` |
| Échelle en fraction de cadre | `the whole car` | `the entire car from front bumper to rear bumper, about half the frame width, both bumpers well inside the frame` |
| Partage sol et ciel | `low camera` | `wet asphalt fills the lower half of the frame; the horizon sits at mid-height` |
| Place en profondeur | `in the background` | `the car stands in the middle ground, about ten metres from the lens, the road in front of it empty` |

Trois faits qui commandent ces quatre lignes.

- **Elles se vérifient contre le ratio effectif**, pas contre celui qu'on a
  écrit. Un profil entier occupant la moitié de la largeur est possible en
  9:16 si le champ et le recul le permettent. Vérifier la géométrie avant de
  déclarer le cadre impossible ; ne pas remplacer un profil demandé par un
  trois-quarts pour satisfaire une préférence de composition. Le ratio se
  règle dans l'interface, `07-spec.md`.
- **Une référence apporte son angle de vue avec elle.** Une photo de trois
  quarts et une demande de profil se battent, et la photo gagne, parce que le
  profil est un angle absent des références, donc à inventer, `05-anchoring.md`.
  Écrire l'exclusion, `do not copy @image1's viewing angle or framing`, et
  fournir l'angle, par une référence de profil ou par la première image.
- **Les majuscules ne pèsent rien.** `ENTIRE`, `LOWER HALF` sont lus comme des
  mots ; c'est la position et la répétition qui pèsent, mécanisme 5 de
  `02b-perform-failures.md`. Une composition imposée s'écrit en tête, une fois,
  en géométrie.

Deux valeurs imposées ou plus font un cadre exact au sens de `05-anchoring.md`, Décider
l'ancrage : il se fournit en image dès la première émission quand la surface le
permet. Ce qui reste du texte : une taille seule, ou une composition que
l'utilisateur veut tenter en texte, auquel cas le premier rendu observé compte.
À deux rendus ratés sur la même composition, l'image n'est plus une option,
`05-anchoring.md`, et le compteur de `09-diagnose.md` s'applique.

Un plan large a un second risque, propre à sa taille : il montre le plus de ce
qu'aucune référence ne montre, et ce que le modèle invente sans plaque sort
avec sa texture par défaut, lue comme un rendu 3D. Plaque du plan large en
premier, ligne de look recopiée par plan : `05-anchoring.md`, La texture
photographique.

Niveau de confiance : la dérive vers le plan serré sur un plan large demandé est
constatée en production, non isolée par un test à variable unique. La forme
positive en pied, `keep his full body centered`, est celle des guides publiés
côté fournisseur (fal.ai, 7 août 2026). Le mécanisme supposé, la caméra suit le
détail, est cohérent avec la pondération par longueur du verrou de présence.

### Le ratio vertical

Le 9:16 réduit le champ horizontal à focale et distance identiques ; il
n'interdit ni le profil d'une voiture ni un sujet entier. Distinguer **rotation
du capteur** et **recadrage de livraison**. Un 24×36 tourné donne 24×36 mm,
soit 2:3. Le recadrer en 9:16 en gardant 36 mm de hauteur donne **20,25×36 mm**.

Pour une projection rectilinéaire, largeur de champ approximative
`W = d × largeur utile / focale`, et angle horizontal
`2 × atan(largeur utile / (2 × focale))`. À 14 mm :

| Modèle de cadre | Champ horizontal | Largeur à 6 m | Voiture de profil de 4,8 m |
|---|---|---|---|
| Capteur tourné, 2:3 | 81,2° | 10,29 m | 46,7 % de la largeur |
| Recadrage 9:16, 20,25×36 mm | 71,7° | 8,68 m | 55,3 % de la largeur |
| Même 9:16, distance 4 m | 71,7° | 5,79 m | 83,0 % de la largeur |

Dans ce modèle, placer la voiture à environ **6,64 m** donne 50 % de largeur.
Un objectif horizontal place l'horizon à mi-hauteur. Ces deux contraintes sont
compatibles en 9:16. La perte de largeur par rapport à 36 mm utiles est
**43,75 %** ; la simple rotation en 2:3 en perd un tiers.

Partir de la fraction de cadre demandée et vérifier les marges aux deux bouts
du mouvement. Ajuster d'abord distance, champ et trajet compatibles avec le
brief. L'inclinaison change la répartition sol/fond ; tourner le sujet change
son angle et doit être annoncé comme arbitrage. Ni une largeur inférieure à
la moitié, ni une grande part de sol ne prouvent à elles seules un cadre faible.

La formule provient de Gregory Hollows et Nicholas James,
[Edmund Optics, Understanding Focal Length and Field of View](https://www.edmundoptics.com/knowledge-center/application-notes/imaging/understanding-focal-length-and-field-of-view/),
consulté le 10 septembre 2026, sans date affichée. Valeurs calculées ici dans
un modèle rectilinéaire simplifié : elles dimensionnent une image de travail,
pas un capteur ou une focale que Seedance garantirait.

---

### Techniques qui demandent une précision de plus

Pour choisir et articuler un POV, une révélation ou un raccord :
[15-camera-techniques.md](15-camera-techniques.md). Garder les règles ci-dessous.

| Technique | Ce qu'il faut ajouter |
|---|---|
| Plan-séquence | Les espaces traversés, dans l'ordre |
| Dolly zoom, Vertigo | Que la taille du sujet reste constante, et dans quel sens le fond fuit |
| Bullet time | Que l'action se fige, et le sens de l'orbite |
| Speed ramp | Où ça accélère, où ça se repose |
| Whip pan | Ce qui est révélé à l'arrivée |
| FPV | La trajectoire et les obstacles frôlés |
| Poursuite, course, projectile | Le budget d'événements, les bords peuplés objet par objet, et la place laissée aux repères de vitesse : `01c-action.md` |
| Caméra portée, plan nerveux | Le tremblement est une texture, pas un mouvement : amplitude, fréquence, cause, et il ne recadre pas. Il se pose sur un mouvement unique au plus, règle dure 1. Sortir les verrous de stabilité de la queue : `01c-action.md`, Le plan nerveux |
| Travelling latéral, truck | Trois couches de profondeur nommées, avant-plan, sujet, fond, et leur vitesse de traversée du cadre, la plus proche la plus vite ; ces couches existent dans une entrée, plaque ou référence, `05-anchoring.md`, le texte ne fait que nommer leur vitesse ; le sujet qui dérive dans le cadre en restant entier ; `does not zoom` en négation de structure temporelle, `12-constraints.md`. Recette du mouvement qui tient, les trois ensemble : un objet d'avant-plan nommé qui traverse le cadre et porte la parallaxe, la distance au sujet tenue par une clause de maintien, le point d'arrivée du mouvement nommé. Constaté sur une session, tenu au troisième essai avec les trois. Sans parallaxe écrite, le modèle rend un zoom sur place, constaté sur une session ; la parade est une hypothèse non isolée par un test. La course se lit à l'ordre de grandeur de la distance au sujet : trois mètres à six mètres glissent, cinq mètres à quatre mètres traversent, constaté sur une session, seuil hypothèse. Avec une vidéo de référence qui porte le mouvement, ne rien réécrire, `04-references.md` |

Un travelling latéral se dimensionne par ses **cadres de départ et d'arrivée**.
Pour un sujet immobile, centré au départ, une translation parallèle à son plan
et sans panoramique, la course maximale vers un côté vaut `(W − L) / 2`, où W
est le champ à sa distance et L sa largeur projetée. À 4 m, 14 mm, en vrai
9:16, W ≈ 5,79 m : une voiture de 4,8 m ne laisse qu'environ **0,49 m** de
course depuis le centre. W − L est la course totale entre les deux bords,
pas la marge disponible de chaque côté. Si le sujet bouge aussi, calculer le
déplacement relatif. Un panoramique d'accompagnement change cette géométrie.

Il n'existe pas de course minimale universelle égale à la moitié du recul pour
voir de la parallaxe. Sa lisibilité dépend des profondeurs, du déplacement,
du cadrage et des textures. Nommer les couches pertinentes déjà présentes,
puis vérifier le rendu ; ne pas ajouter d'objet au brief pour remplir un seuil.

---

### Traduire un terme que le modèle peut ignorer

Pour un terme rare ou instable dans le métier, garder le terme **et** le traduire
en changement visible.

```
Rack focus: shift focus smoothly from the leaves in the foreground to the person
in the background. The leaves gradually blur while the person's face changes
from soft to sharp.
```

Ouverture, focale et obturation sont acceptées, mais le résultat visible voulu
est presque toujours l'instruction la plus claire.

**Un caractère d'objectif ne se tient pas depuis le prompt.** Anamorphique,
compression, forme de bokeh, distorsion de bord dérivent d'un plan à l'autre
quand on les demande en texte. Ils se portent par l'image de décor, qui devient
l'objectif. Recette et arbitrage dans `05-anchoring.md`. Le prompt vidéo ne
décrit alors que du verre propre et des sources contenues, et ne nomme jamais un
parasite optique, même pour l'interdire.

---

### Objets en amorce

Décrire **la trajectoire et la taille relative** des objets d'avant-plan, jamais
leur seule présence au premier plan. Une amorce nommée par son contenu, « trois
photographies en amorce », fait fabriquer les photographies en grand et détruit
le mouvement prévu : le modèle traite l'amorce comme le sujet du plan.

| Faible | Fort |
|---|---|
| `Three photographs in the foreground.` | `Three small photographs lie flat at the bottom edge of frame, each about a fifth of the frame height, and stay there as the camera pushes past them.` |

Hypothèse de travail issue d'une session de production, non isolée par un test à
variable unique.

### Position dans le cadre et déclencheur

Un mouvement décrit sans composition laisse le cadrage au hasard. Trois éléments
à ajouter dès qu'un sujet bouge :

- **où le sujet se tient** dans l'image, en tiers,
- **quel événement déclenche** le mouvement caméra,
- **si l'axe peut être franchi**.

> The camera trucks parallel to the court and keeps the red player in the left
> third of frame, with the hoop visible on the right; the stands slide across
> the background more slowly than the nearer court lines, and the camera does not zoom. The
> camera does not pan until the ball has fully left both hands. Keep the basket
> on the same side of frame and never cross the court axis.

---

### Le verrou de présence du sujet

Une composition dit où le sujet se tient **quand il est là**. Elle ne dit jamais
qu'il doit y être en permanence. Sur un plan à plusieurs segments caméra, c'est
le trou par lequel le sujet sort du film.

Dès que le brief nomme un sujet hero, un objet ou une personne dont l'absence
viderait le plan, définir les plans concernés puis écrire leur clause de
présence **avant les beats** et la reprendre dans la clôture. Un insert de
paysage ou d'objet explicitement demandé peut en être exclu, notamment en
montage elliptique, `03` ; il n'autorise pas d'autres absences non demandées.

> The cleaver fills the frame from the first frame to the last, edge down and
> spine up, never lying flat.

Puis relire chaque segment caméra soumis à ce verrou : **le sujet est-il
dans ce cadre ?** S'il répond non sans exclusion demandée, il se réécrit.
Ne pas supprimer un insert prévu ni y réintroduire le sujet pour satisfaire
un verrou global trop large.

Le mode de défaillance qu'elle attrape est spécifique et coûteux. Un brief
demande un très gros plan sur un objet ; le prompt décrit consciencieusement le
décor, la table, les accessoires, parce que ce sont eux qui portent les
références ; la caméra part visiter ce qui a été le mieux décrit, et le sujet
n'entre qu'à la fin. Le rendu est propre, obéissant, et hors sujet. Constaté sur
une session : cinq secondes sur huit sans le sujet à l'image.

Corollaire d'écriture : **la longueur consacrée à un élément est une consigne de
temps d'écran.** Trois lignes sur le décor et une demi-ligne sur l'objet hero
produisent un plan qui parle du décor, même si la clause caméra dit le
contraire. Ce n'est pas une règle documentée par ByteDance, c'est une régularité
observée, cohérente avec la pondération par répétition et position du mécanisme 5
de `02b-perform-failures.md`.

---

### Séparer caméra et sujet

Deux axes indépendants, deux clauses. Les fusionner force le modèle à arbitrer et
il aplatit les deux.

Deux axes indépendants ne veulent pas dire deux axes compatibles. Un travelling
latéral et un sujet qui vient vers l'objectif se disputent le même cadre,
parallaxe contre croissance d'échelle, et le modèle tranche en supprimant la
caméra. Un travelling latéral se paie avec un sujet latéral ou immobile ; un
sujet qui vient vers l'objectif se paie avec une caméra verrouillée.

> A model in a flowing camel-tan trench coat walks slowly toward a locked, static
> camera down a clean sunlit studio runway, then stops and makes a half-turn so
> the coat flares and settles around her. The camera does not move at all; every
> bit of motion is the model's walk, the turn, and the drift of the fabric.

Quand les deux évoluent, les minuter séparément :

```
0-3s: subject holds still, camera pushes in.
3-6s: subject turns to face the light, camera begins a slow clockwise orbit.
```

Éviter deux mouvements simultanés sauf si leur relation est le sujet du plan.

---

### Plan caméra segmenté

Un cas particulier utile : garder personnages, actions et style intacts et ne
diriger **que** la caméra, beat par beat. C'est aussi le motif d'une édition de
point de vue.

> A 15-second segmented camera plan: 0–4s, a micro-FPV move skims tightly past
> the pan, then follows the popping toast and whip-pans to the coffee; 4–7s, push
> in and track laterally along the rim of the pan, following the fried egg as it
> flips up and lands back in place; 7–11s, rapidly rise to a top-down view, then
> descend at a steady pace, sweeping across the plate and keys; 11–15s, use a
> handheld close-up to follow the hands with a fast lateral whip, then push in on
> the breakfast and pull back to a medium two-shot. Keep the sequence continuous,
> with no cut between segments; the handheld texture belongs to the last segment
> only.

---

### Lumière

La lumière est un événement, pas un adjectif. Elle vient d'une source et reste
cohérente spatialement.

Six informations utiles : heure du jour, position de la source, dureté,
contraste de couleur, effet atmosphérique, évolution prévue dans le temps.

> Cool overcast daylight from the open market roof; warm tungsten bulbs inside
> the flower stall. As she approaches, the warm light gradually reaches the right
> side of her face while the left stays cool. The light stays steady, with no
> unexplained color shift.

Ne pas empiler « cinematic, volumetric, neon, golden hour, moonlight, studio
light » dans une même scène : ce sont des grammaires lumineuses incompatibles.

La lumière sert aussi de canal de transition entre deux beats sans changer de
lieu. Ajouter `gradually` pour que le modèle fasse un pont plutôt qu'une coupe.

**Le raccord lumière entre plans.** Une coupe recompose un cadre, et la lumière
ne survit pas plus à la coupe que la taille ou l'optique, `03-sequence.md`. Là
où elle décroche le plus, ce sont les gros plans et les inserts : dans un plan
large, la source est dans le cadre ou lisible par ses ombres, le modèle la
tient ; dans un gros plan de mains ou de visage, la source est hors cadre, donc
déduite, donc réinventée, même si le plan large qui précède l'a bien posée.
C'est le mécanisme d'ancrage appliqué à la lumière : il tient ce qu'il voit.

Trois règles en découlent.

1. **La lumière se redéclare dans chaque plan**, jamais dans une seule clause
   globale « consistent lighting across all shots », qui ne court pas sur les
   coupes.
2. **Dans un plan serré, elle s'écrit comme son effet sur ce qui est dans le
   cadre**, pas comme une source qu'on ne voit pas : la direction en direction
   d'écran, ce qu'elle touche, ce qui reste dans l'ombre, la couleur de chaque
   côté. `warm window light from screen-left on the left side of his face, the
   right side a stop darker, cool` se tient ; `the same light as the wide` est
   une mémoire que le modèle n'a pas.
3. **Le bloc lumière se recopie mot pour mot** entre les plans du même état
   lumineux, comme un bloc d'identité ou de voix, `04-references.md` et
   `10-syntax.md` : seule
   change la surface qu'il touche, visage, mains, objet. Deux formulations de
   la même lumière sont deux lumières. La ligne de look photographique voyage
   avec lui, `05-anchoring.md`, La texture photographique.

Si le brief change de lieu, de moment ou de lumière, écrire un nouvel état
local au lieu de recopier l'ancien. Conserver les blocs propres à chaque état,
selon `03-sequence.md`, Montage elliptique.

| Faible | Fort |
|---|---|
| `Shot 2 (close-up on his hands placing the screw). Consistent lighting across all shots.` | `Shot 2 (close-up on his hands placing the screw): warm late-afternoon window light from screen-left lights the backs of his hands and the left face of the brass mechanism; the right side falls a stop darker and cool.` |

Sur une séquence ancrée par images, `05-anchoring.md`, la lumière est portée
par les fixes et se vérifie entre elles avant toute vidéo ; le prompt de chaque
plan la nomme quand même en une ligne, pour que le mouvement ne la déplace pas.

Niveau de confiance : la dérive de lumière sur les gros plans et inserts d'une
séquence multi-plans est constatée en production, non isolée par un test à
variable unique ; le mécanisme, source hors cadre donc déduite, est une
hypothèse cohérente avec la doctrine d'ancrage.

---

### Variantes de campagne

Faire tourner un seul sujet à travers plusieurs mouvements donne des variantes
qui se lisent comme un même tournage. Changer autre chose que la clause caméra,
et elles se lisent comme trois clips sans rapport.

Base, seule la clause caméra bouge :

```
5-second product shot, 16:9. A single white-and-mint running sneaker centered on
a smooth pale concrete pedestal in a bright minimalist studio, clean soft
daylight from the left. [CLAUSE CAMÉRA]. Clean commercial product
cinematography. Audio: low studio room tone, no music. No cuts, no text, no logo.
```

| Variante | Clause |
|---|---|
| Hero | `The camera performs a slow steady push in from a mid-shot to a tight close-up on the laces and knit upper; the sneaker stays centered and grows as the edges of the studio leave the frame` |
| Tour produit | `The camera performs a smooth ninety-degree orbit from a front three-quarter angle to a full side profile; the sneaker stays centered as the light slides across the knit and the sole` |
| Isolation | `The camera performs a subtle dolly zoom: it pushes forward while the lens zooms out, so the sneaker holds its size while the studio backdrop warps and stretches outward around it` |

---

### Faible contre fort

| Point | Faible | Fort |
|---|---|---|
| Caméra | `A city skyline at dusk` | `Low aerial gliding over a skyline at dusk, one unbroken push toward a single lit tower` |
| Mouvement dans le temps | `A climber on a ridge` | `A climber hauls over the ridge, stands, and turns to the valley as the camera pulls back` |
| Continuité | `Use these references` | `@image1 defines the detective's coat and face, do not use its background` |
| Vitesse | `fast pan` | `whip pan left, settling on the doorway` |
| Taille de plan | `Wide shot of a man on the church steps` | `Wide shot: his full figure visible from head to feet, about a third of the frame height, the facade filling the rest; the camera holds this distance for the entire shot` |
| Réalisateur nommé | `in the style of John Woo` | Le nom se déplie en clauses caméra sourcées, contre-plongée, ralenti ancré sur une image, mise en place, et n'entre jamais dans le prompt : `13-director.md` |

---

Le mouvement du sujet, la physique, les fluides, la vitesse et le report d'état
vivent dans `01b-motion-physics.md`, scindée de cette fiche en septembre 2026
quand elle a dépassé son plafond de 500 lignes. À ouvrir avec `01` dès qu'un
sujet bouge, se pose, manipule, ou qu'un fluide, un tissu ou des particules sont
dans le plan.
