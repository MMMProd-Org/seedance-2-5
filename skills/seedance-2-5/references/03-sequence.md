# 03 Construire une séquence

Comment répartir une durée entre plusieurs événements : beats minutés, étages
avec états, contrat de continuité, chaînage au delà de trente secondes.

À ouvrir dès qu'il se passe plus d'une chose dans le plan.

---




## Sommaire

- Repère de montage
- Les beats minutés
- La forme courante
- Choisir la structure avant d'écrire
- Découper
- Plan unique ou multi-plans
- Montage elliptique
- Notation par étages
- Le contrat d'état de sortie
- L'état d'entrée d'un sujet qui arrive en cours de plan
- Le contrat de continuité
- Chaîner au-delà de trente secondes

---

## Repère de montage

**Repère de montage, pas limite technique :** environ 1,5 s par segment est
une hypothèse de lisibilité issue d'une session. Des coupes plus brèves peuvent
être voulues. Conserver durée et plans demandés ; si leur exécution précise
est incertaine, annoncer un découpage ou un traitement au montage, sans
allonger ni supprimer silencieusement.

---

## Les beats minutés

C'est le porteur par défaut dès qu'il se passe plus d'une chose. Plages
consécutives, non chevauchantes, départ à zéro, pas de trou. **L'unité usuelle
est la seconde entière** ; une demi-seconde s'écrit, mais elle tombe dans la
tolérance d'environ une seconde décrite plus bas, donc elle alloue du rythme,
jamais un point de coupe.

À noter si l'on compare des rendus entre générations : Seedance 2.0 ne répond pas
aux timestamps, il ne lit que les numéros de plan ; 2.5 répond aux timestamps
en secondes entières. Publié dans le guide ModelArk 2.5, Differences from
Seedance 2.0.

```
0-5s: [action], [caméra]
5-12s: [action qui repart de l'état laissé], [caméra]
12-22s: [action], [caméra]
22-30s: [payoff], [caméra qui se stabilise]
```

Trois règles portent tout le reste.

**Un seul job par beat.** Un changement de lieu, ou un basculement émotionnel, ou
un mouvement de caméra. Un beat qui tente trois choses produit de la bouillie.

**Chaque beat reprend l'état physique du précédent.** Si le casque est dans la
main gauche au beat 1, il y est encore au beat 4, et on l'écrit. C'est ce qui
empêche les objets de changer de main, de se dupliquer ou de se téléporter, bien
plus efficacement qu'une clause de continuité isolée.

L'état de sortie d'un beat est un contrat avec le suivant : **tout ce qu'on y
omet est libre de changer.** Les trois faits à y répéter, côté du cadre, main
qui possède, compte, sont dans Le contrat d'état de sortie, plus bas.

**Les transitions sont explicites.** « Inside the car » dit au modèle de couper.
Sans ça, on obtient un morph baveux entre deux lieux. À l'inverse, `no cuts` et
`one continuous shot` imposent le plan-séquence. Une transition qui n'est pas
une coupe franche porte **son instant et sa méthode**, exemple publié dans le
guide ModelArk : `At the 5-second mark, the camera quickly transitions leftward
using a left wipe combined with a natural dissolve.` Le déclencheur sans
méthode laisse le modèle choisir, la méthode sans instant dérive.

Les timestamps allouent du temps aux événements. Ce ne sont pas des points de
montage au frame près : la tolérance observée est de l'ordre de la seconde. Trop
peu de contenu dans une fenêtre et le modèle improvise ; trop et il coupe sec ou
abandonne un beat. Compter 2 à 3 secondes par action visible.

Le réglage de durée ne fabrique pas d'événements. Trente secondes sur un
mouvement unique produisent de l'attente, de la répétition ou du ralenti
involontaire. Le nombre de beats suit le nombre de changements, pas la durée.
Trente secondes écrites en un seul paragraphe se lisent comme un long flou.

---

## La forme courante

C'est celle des prompts publiés par ByteDance et des prompts testés par les
fournisseurs. Plages minutées, une ligne par beat, contrat de continuité en
clôture.

> 30-second continuous single take inside a small New York City bodega on a rainy
> morning, all action at natural real-time speed. The same bike messenger wears a
> yellow rain jacket and carries one red bicycle helmet in the left hand
> throughout. 0-5 seconds: the door bell rings as the messenger enters, closes the
> glass door with the right hand, and shakes rain from the shoulders without
> dropping the helmet. 5-10 seconds: the camera follows from behind at chest
> height as the messenger walks to the drink cooler, opens the cooler with the
> right hand, removes one clear bottle of seltzer, and closes the door. [...]
> Keep the same messenger, jacket, helmet, bottle, phone, clerk, counter, cooler,
> and store layout from first frame to last. No cuts, no slow motion, no repeated
> entrance, no duplicated bottle or helmet, no object teleportation.

Quatre choses à repérer : la ligne de format en tête, l'invariant d'objet posé
avant les beats, chaque beat qui reprend l'état du précédent, et la queue de
négations spécifiques.

---

## Choisir la structure avant d'écrire

Poser des étages sur un plan simple ajoute une rigidité inutile ; écrire en
prose libre une histoire à cinq événements laisse l'ordre au hasard.

| Contenu | Structure |
|---|---|
| Plan unique, un événement | Prose simple. Sujet, action, scène. Aucun en-tête d'étage |
| 10 à 30 s, plusieurs événements | Beats ou étages nommés, chacun avec état d'entrée, un événement, état de sortie |
| Un moment critique de rythme | Un timestamp, réservé aux entrées, sorties, passages de relais et repères sonores |
| Plus de 30 s en chaînage | Blocs grossiers. Le minutage fin sur un long clip provoque des coupes non demandées |

Les deux se mélangent : l'histoire tourne sur des étages nommés, et un timestamp
se pose sur le seul beat qui doit tomber à l'heure. La notation par étages,
blocs `[Stage N]`, est décrite plus bas.

## Découper

Repères de rédaction pour une scène continue, **pas des plafonds de plans**.
Un montage elliptique suit les changements demandés, section ci-dessous.

| Durée | Beats | Découpage type |
|---|---|---|
| 4 à 5 s | Aucun | Un seul mouvement tenu |
| 8 s | 2 à 3 | Établir, agir, poser |
| 15 s | 3 | Établir, développer, résoudre |
| 30 s | 3 à 5 | Établir, développer, tourner, résoudre |

La page Dreamina du 18 août 2026 donne le défaut officiel pour trente secondes :
« 6 à 8 secondes par beat, 3 à 4 secondes gardées pour la résolution », et une
structure en quatre temps, 0-6 s large d'ouverture, 6-14 s développement en
plan moyen serré, 14-24 s montée avec un mouvement ou un insert, 24-30 s
résolution. Un beat de 6 à 8 s porte toujours un seul changement principal ; le
reste du beat est l'action qui se pose, pas un second événement.

Un beat par changement, jamais par tranche de temps arbitraire. Un beat qui tente
trois choses produit de la bouillie. Une poursuite plus un changement de costume
plus une dispute plus une explosion plus un lever de soleil ne rentrent pas dans
trente secondes.

Prévoir du temps pour que le dernier beat se pose. Une génération longue a besoin
d'une destination : nommer la dernière image.

---

## Plan unique ou multi-plans

**Plan unique** quand le mouvement propre du sujet porte la durée. Ajouter
`one continuous shot` et `no cuts`.

**Multi-plans** quand l'histoire doit changer de point de vue. Ouvrir chaque beat
par une taille de plan et poser `Cut to` en tête des beats suivants, ce qui dit
au modèle de casser le cadre là plutôt que de faire passer la caméra.

> Shot 1 (0-10s, Wide establishing: the whole kayak small in frame, about a
> fifth of the frame width, the bay filling the rest): a sea kayaker paddles
> across a turquoise bay, low golden sun from screen-right. Shot 2 (10-20s, Mid
> tracking): cut to a low tracking mid-shot skimming beside the kayak, the far
> shore sliding past behind him more slowly than the near water, the camera does not
> zoom, the same low golden sun from screen-right on the paddler's side. Shot 3
> (20-30s, Hero
> close): cut to a low-angle hero close-up as the kayak lands on a pebble beach,
> the same low golden sun from screen-right on his face.

Une transition non déclarée produit un morph baveux entre deux lieux. « Inside
the car » suffit à demander la coupe.

Chaque coupe franche recompose un cadre, donc **ce qui décrit l'image se
redéclare par plan**, et cette liste est la seule : taille, hauteur et angle,
optique, place de chacun, lumière écrite comme son effet sur ce qui est dans le
cadre et recopiée mot pour mot, ligne de look photographique, section Lumière
de `01-write-shot.md` et `05-anchoring.md`. Une clause posée dans le
premier plan ne court pas sur les suivants, et les gros plans sont ceux qui
perdent la lumière en premier. Seuls le contrat de continuité et la nappe
audio, qui portent sur toute la durée, restent globaux.

---

## Montage elliptique

Pour un vlog, un voyage ou une suite de moments, une coupe peut avancer dans
le temps et changer de lieu. Déclarer ces ellipses ; ne pas inventer un trajet
continu ou un morph entre chalet, piste, café et intérieur du soir. Conserver
les scènes demandées et leur ordre, sans les réduire à trois beats par défaut.

Séparer les invariants **globaux**, identité et look voulu, des états **locaux**,
tenue prévue pour l'activité, objets présents, lieu, moment et lumière. Une
personne reste la même en retirant un manteau ou en passant de la lumière du
jour au feu du soir, si le brief prévoit ces changements. Le verrou global
ne doit pas les interdire. Recopier chaque bloc local dans les plans de ce
même état ; règle lumière dans `01`, contrat de continuité ci-dessous.

Un plan garde une action lisible et une caméra principale ; des plans différents
peuvent alterner suivi, insert et regard caméra. Mettre chaque réplique et son
dans son beat, puis vérifier qu'il laisse le temps de les jouer. Les inserts
d'ambiance appartiennent au montage quand le brief les demande, sans ajouter
le personnage dans chacun pour satisfaire un verrou de présence non demandé.

Terminer sur l'état final demandé : pose tenue, geste encore en cours ou
occultation physique de la caméra. Une fin lisible n'impose pas un arrêt de
l'action ni un fondu au noir. Pour la continuité d'un objet qui revient,
voir [16-effects-mechanisms.md](16-effects-mechanisms.md).

Statut : hypothèse de prompting tirée notamment du montage alpin fourni par
l'utilisateur le 9 septembre 2026, réussite rapportée sans rendu examiné.

## Notation par étages

Alternative plus verbeuse, utile quand un récit enchaîne plusieurs lieux ou
plusieurs opérateurs, et que les états intermédiaires sont critiques. Même
discipline, présentation en blocs.

```
[Generation Goal]
Generate an instructional video showing a flower shop's order-packing process.

[Stage 1]
Initial state: <Florist> stands behind the workbench. Loose stems, scissors, and
wrapping paper lie on the tabletop.
Primary event: <Florist> arranges the stems and trims them to length.
End state: <Florist> holds the bouquet in the left hand, scissors back on the
right of the workbench.

[Stage 2]
Continue from the previous stage: both characters keep the same identities and
clothing.
Primary event: <Store Assistant> unfolds the wrapping paper, <Florist> places the
bouquet inside and ties it.
End state: the wrapped bouquet lies flat in the center of the workbench, bow
facing camera.

[Maintain Consistency]
Keep character identities, clothing, prop ownership, and workbench orientation
consistent.
```

L'état final est spatial et vérifiable : « le bouquet est au centre du plan de
travail, le nœud face caméra » se contrôle au visionnage, « elle a fini » non.

La reprise explicite en tête d'étage est ce qui empêche la dérive de personnage
au changement de bloc.

---

## Le contrat d'état de sortie

L'état de sortie d'un étage est un **contrat avec l'étage suivant** : tout ce
qu'on y omet est libre de changer.

Trois faits dérivent avant les autres et doivent figurer dans **chaque** état de
sortie :

1. **Qui se tient de quel côté du cadre.**
2. **Quelle main possède quel objet.**
3. **Combien il y en a dans le cadre.**

Le troisième est celui qu'on oublie, et c'est celui qui transforme une tasse en
deux. L'écrire littéralement : `Exactly one mug is in frame`, puis
`Still exactly one mug in frame` à l'étage suivant.

Un quatrième s'ajoute dès qu'il y a du dialogue ou plus d'un personnage :
**vers quoi va chaque regard**, en direction d'écran. C'est ce qui tient l'axe
d'un étage à l'autre, et d'une génération à l'autre quand la scène est couverte
en plusieurs plans. Voir la carte des regards dans `02a-perform.md`.

Ajouter la direction de face des personnes et des objets quand elle porte le
raccord.

Relire un long prompt à l'envers en cherchant uniquement ces trois faits dans
chaque état de sortie est le contrôle le plus rentable avant génération.

## L'état d'entrée d'un sujet qui arrive en cours de plan

Le contrat d'état de sortie couvre ce qui est déjà là. Il ne couvre pas le sujet
qui **n'existait pas au beat précédent** : le bras qui entre au cadre, la voiture
qui arrive, l'objet qu'une main pose. Pour celui-là, il n'y a pas d'état laissé
d'où repartir, et le beat ouvre sur un trou.

Ce trou ne produit pas une erreur, il produit une paresse. **Le modèle place le
sujet au plus près de sa destination et remplit le temps alloué par de
l'attente.** Le beat dure la bonne durée, l'action arrive, et elle n'a aucune
énergie parce qu'elle n'a parcouru aucune distance.

Trois valeurs à écrire, toujours les trois :

1. **D'où.** La position de départ dans l'espace, pas seulement hors champ.
2. **Quelle distance.** En unités du monde, ou en hauteurs de cadre.
3. **À quelle vitesse**, et si le mouvement a le droit de s'interrompre.

| Faible | Fort |
|---|---|
| `the arm is already dropping` | `the cleaver is already high above the block, raised at arm's length well above the shoulder, about a metre clear of the wood, and it is falling` |
| `a car enters frame` | `the car enters from behind the left building at full speed, forty metres out, closing without slowing` |

La troisième valeur porte une négation utile, parce que l'attente est le mode par
défaut : `moves downward without stopping, without hovering and without slowing,
at full striking speed, all the way to the wood`. C'est une négation de
**structure temporelle**, elle mord, à la différence d'une négation qui nommerait
un artefact dessinable. Partage dans `12-constraints.md`.

Cas jumeau, la rampe de vitesse. Un ralenti demandé sur l'impact seul se
déclenche sur une image nommée, `slow motion starts on the exact frame the edge
touches the wood, not before`. Sans ce point d'ancrage, la rampe remonte dans le
beat précédent et avale précisément la chute qu'on venait de doter d'une
distance.

Constaté sur une session, corrigé, non revérifié par un test à variable unique.

---

## Le contrat de continuité

Une clause, en clôture, jamais répétée dans chaque beat où elle devient du bruit.
Elle nomme ce qui reste constant.

> Keep the same messenger, jacket, helmet, bottle, phone, clerk, counter, cooler,
> and store layout from first frame to last.

Ordre de priorité de ce qu'on épingle quand il faut choisir :

```
identité du sujet → lieu et costume → lumière et palette → design sonore
```

Tout ce qui n'est pas épinglé est réinterprétable, et la petite dérive se compose
sur trente secondes.

---

## Chaîner au-delà de trente secondes

Deux méthodes.

**Extension** : le clip validé devient la source de la génération suivante. Voir
`06-edit-extend.md`.

**Dernière image comme référence** : extraire la dernière image du clip et la
passer comme première image de la génération suivante. Ça donne au second prompt
un état de départ réel au lieu de demander au modèle de s'en souvenir. Ne pas
raconter le premier clip dans le second prompt : décrire ce qui est déjà terminé,
ce qui reste fixe, et la première action nouvelle.

> Use the provided first frame as the exact first frame and continue forward
> from that moment. Preserve the same stack of three buttermilk pancakes,
> softened square of butter,
> six blueberries, white ceramic plate, amber syrup pool, counter, warm diner
> light, 21:9 framing, macro lens, and camera position. Do not replay or recreate
> the syrup pour that happened before this frame.

Forme slot. En pool, l'image porte un token : « Use @image1 as the exact first
frame », et le rendu ressemble au cadre sans le reproduire. Voir
`05-anchoring.md`, Règles techniques.
