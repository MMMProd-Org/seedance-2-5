# 13 Traduire un réalisateur

Un nom de réalisateur, un titre de film, un « à la » dans un brief est un
**brief caméra compressé**. Ce n'est pas un adjectif de goût au sens de la règle
dure 4, et ce n'est pas une indication de jeu. Quand l'utilisateur écrit « à la
John Woo », il parle de mise en scène par le cadre : mouvement, angle, taille,
rythme de coupe, vitesse, disposition des corps.

Deux défaillances constatées, symétriques. Le nom tombe en silence, absorbé par
la règle 4, et le prompt sort sans rien de la signature demandée : c'est un
arbitrage silencieux, règle 11. Ou le nom est traduit en émotion, parce que le
jeu est ce que le skill sait le mieux écrire, et le prompt parle de ce que le
personnage ressent alors que le brief parlait de ce que la caméra fait.

Le nom sert à rechercher des traits de mise en scène, puis à les traduire en
choix visibles. Par défaut, le prompt repose sur ces clauses plutôt que sur le
nom seul. C'est une convention de précision, **pas une interdiction juridique
générale de citer un réalisateur vivant**. La demande explicite de l'utilisateur
reste prioritaire ; `07` distingue méthode et droits à vérifier selon l'usage.

À ouvrir dès que le brief cite un réalisateur, un chef opérateur, un film ou une
séquence comme référence de mise en scène. Puis `01` pour écrire la caméra.

---

## Sommaire

- Ce que porte un nom
- Le protocole
- La table de traduction
- Arbitrer avec les défauts du skill
- Ce qui ne se traduit pas
- Exemple daté : John Woo
- Exemple daté : Michael Bay
- Checklist

---

## Ce que porte un nom

Une signature de mise en scène se décompose en six canaux, et seuls ces six
s'écrivent dans un prompt :

1. **Mouvement de caméra** : type, vitesse, point d'arrivée.
2. **Angle et hauteur.**
3. **Tailles de plan** et leur enchaînement.
4. **Rythme de coupe et traitement de la vitesse** : ralenti, arrêt sur image,
   fondu, intercut.
5. **Mise en place des corps** : face à face, dos à dos, symétrie, miroir.
6. **Lumière et optique** : contre-jour, silhouette, profondeur de champ.

Tout le reste se trie en deux tas. Les **thèmes** et la morale des personnages
relèvent de l'écriture, invariant 6 de `14-maintenance.md`, et retournent au
brief de l'utilisateur. Les
**adjectifs**, « opératique », « lyrique », « élégant », se suppriment ; s'ils
cachent un trait technique, on retourne à la source pour le trouver.

Un **motif visuel récurrent**, colombes, lunettes noires, trench, n'est pas un
style : c'est un objet ou un événement. Il se traite comme tel, référence avec
rôle et exclusion dans `04-references.md`, compte et position à l'état final dans
`03-sequence.md`, quantité en fraction de cadre pour un vol ou une pluie dans la
section Fluides, tissus, cheveux, fumée, particules de
`01b-motion-physics.md`.

---

## Le protocole

1. **Lever l'ambiguïté en une question** si le brief ne le dit pas : le
   réalisateur en général, un film précis, ou une séquence précise ? Une
   séquence vaut mieux qu'une filmographie, parce qu'elle donne des plans et non
   une réputation.
2. **Chercher sur le web.** Deux ou trois sources qui nomment des techniques
   concrètes : analyses de plans, entretiens, notes de tournage, critiques
   techniques. Noter auteur, date et lien pour chacune. Une source qui dit
   « visuellement époustouflant » ne sert à rien ; une source qui dit « plusieurs
   caméras à des cadences différentes » sert. Ne jamais écrire un trait de
   mémoire : une signature est un fait vérifiable, et un trait inventé produit
   un plan qui ne ressemble à rien.
3. **Trier.** Pour chaque trait rapporté, décider dans lequel des six canaux il
   tombe, ou s'il est hors canal : thème, motif, adjectif.
4. **Traduire.** Chaque trait retenu devient une clause dans la grammaire du
   skill, table ci-dessous. Un trait, une clause, un endroit dans le prompt.
5. **Arbitrer et annoncer.** Les traits gardés, les traits supprimés et
   pourquoi, les traits qui contredisent un défaut du skill et comment ils sont
   tranchés, et les sources avec auteur, date et lien : tout cela va dans la
   ligne Sources du self-eval, prévue à cet effet dans le format de `17-delivery.md`.
   Règle 11. Le prompt, lui, ne porte que les clauses.

---

Un catalogue de techniques ne prouve pas une attribution à un réalisateur.
Les outils de [15-camera-techniques.md](15-camera-techniques.md) peuvent aider
à formuler un effet retenu ; ils ne remplacent pas les sources de ce protocole.

## La table de traduction

| Trait rapporté par les sources | Canal | Forme en prompt |
|---|---|---|
| « caméra constamment en mouvement », « caméra en 360 » | Mouvement | La règle dure 1 tient : un mouvement principal par plan. Un style à caméra multiple devient donc plusieurs plans courts, chacun avec son mouvement et son point d'arrivée, `Cut to` en tête de beat, `03-sequence.md` |
| « contre-plongée », « contre-plongée extrême », « plongée zénithale » | Angle | Deuxième point de la spec en cinq points de `01`, redéclaré à chaque coupe puisqu'une coupe recompose le cadre |
| « gros plans intercalés dans l'action » | Tailles | Une taille par plan, écrite en géométrie visible et tenue, section Tenir une taille de plan de `01` |
| « ralenti » | Vitesse | Autorisé seulement si le geste ralenti est l'événement du plan, ancré sur une image nommée, `slow motion starts on the exact frame [événement]`, `03-sequence.md`. Jamais dans un beat dialogué, mécanisme 4 de `02b`. Sur ce plan, `natural real-time speed` sort de la ligne de format et `no slow motion` sort de la queue |
| « intercut de plusieurs cadences » | Rythme | Une cadence par plan : un plan en vitesse réelle, une coupe, un plan en ralenti ancré. Un speed ramp interne peut être demandé et est cité par le guide ; borner ses phases et contrôler le rendu |
| « arrêt sur image », « fondu enchaîné » | Rythme | Présents dans les exemples du guide officiel 2.5, sections minutage et caméra. Nommer déclencheur, durée et arrivée ; la précision au photogramme reste à contrôler. Le montage est une option pour une durée exacte, pas la preuve d'une fonction absente |
| « face à face », « dos à dos », « symétrie », « miroir » | Mise en place | Places en direction d'écran et carte des regards, `02a-perform.md` ; diagramme dès trois personnages, `11-diagram.md` |
| « contre-jour », « silhouette », « faible profondeur de champ » | Lumière et optique | Source nommée et position, section Lumière de `01` ; la profondeur de champ se porte par la plaque de décor, `05-anchoring.md` |
| « téléobjectif », « compression », « parallaxe » | Optique, donc effet visible | Un caractère d'objectif ne se tient pas depuis le prompt, et une focale nommée seule est un terme que le modèle peut ignorer, `01`. S'écrit comme ce qu'elle produit : le fond dense qui glisse derrière le sujet plus vite qu'il ne tourne, les plans empilés à plat ; la plaque de décor porte la compression, `05-anchoring.md` |
| « angle hollandais », « cadre penché » | Angle | Chiffré et orienté, `the frame tilted about fifteen degrees, the horizon rising toward screen-right`, redéclaré à chaque coupe |
| « flare », « lumière dans l'objectif » **voulu** | Lumière | La règle des négations qui invoquent, `12-constraints.md`, interdit de le nommer en interdiction ; voulu, il s'écrit en positif comme un événement lumineux avec source, direction et instant, `as the searchlight crosses behind his head, a horizontal streak of light crosses the lens from screen-left for half a second`. Le verrou `clean crisp glass` sort alors du prompt |
| « avant-plan qui traverse », « trois couches » | Mise en place et profondeur | Objet en amorce avec trajectoire et taille relative, section Objets en amorce de `01` ; couche de fond dense fournie par la plaque, jamais déduite |
| « hélicoptère », « drone FPV », « caméra qui plonge » | Mouvement | Un trajet aérien par plan, trajectoire et obstacles frôlés, table des techniques de `01` ; `dive` est un terme lu directement, `07-spec.md` |
| « plans d'une fraction de seconde », « crash zoom » | Rythme | Les coupes très brèves sont difficiles à minuter précisément en génération ; 1,5 s est un repère de travail, pas une limite native. Pour un crash zoom, décrire l'agrandissement rapide à caméra immobile, la cible et l'arrêt. Contrôler le résultat ; proposer le montage si la précision l'exige |
| « colombes », « deux pistolets », « trench » | Motif, donc objet | Référence avec rôle et exclusion, compte à l'état final, quantité en fraction de cadre pour un vol |
| « opératique », « lyrique », « chorégraphié » | Adjectif | Supprimé. Retourner à la source chercher ce qu'il désigne concrètement |
| « thèmes de loyauté », « code d'honneur » | Écriture | Hors skill. Retourne au brief |

---

## Arbitrer avec les défauts du skill

Les défauts du skill sont calibrés pour la stabilité : un mouvement, vitesse
réelle, pas de coupe, quatre à huit références. Une signature de réalisateur les
contredit souvent, et c'est normal : c'est un choix esthétique contre un défaut
de sécurité. La règle : **le trait de la signature gagne quand l'utilisateur l'a
demandé, à condition de payer son prix dans la forme du prompt, et de le dire.**

- **Ralenti.** Voir la table. Le prix : un plan dont ce geste est l'événement,
  un ancrage sur une image nommée, et la queue qui ne contredit plus le corps.
- **Coupes.** Un style monté devient un multi-plans, pas un plan-séquence avec
  une caméra qui saute. Le prix : `no cuts` sort de la queue, chaque plan
  redéclare ce que `03-sequence.md` liste.
- **Mouvement multiple.** Un mouvement par plan, donc plus de plans. Le prix :
  vérifier la lisibilité au rythme demandé, `03-sequence.md`, Repère de montage. Annoncer toute
  proposition de regroupement ou de montage ; ne pas supprimer un plan par quota.
- **Caméra immobile.** Un cadre fixe peut être un trait de mise en scène ou
  une demande explicite. Nommer `locked-off` quand il est voulu. Ne demander
  un mouvement dans chaque plan que si ce choix appartient au brief ou à la
  signature retenue et sourcée. Si un mouvement demandé disparaît pour faciliter
  le cadrage, annoncer cet arbitrage ; ne pas généraliser les exemples Woo/Bay
  à tous les réalisateurs.

- **Ratio.** Un trait demandé dans un ratio qui ne le porte pas se signale
  avant d'écrire : le plan large au ras du sol des réalisateurs d'action est un
  cadre horizontal, et en 9:16 il vide la moitié basse de l'image. Le prix : le
  trait se garde, sa géométrie se recompose selon la section Le ratio vertical
  de `01-write-shot.md`, et l'écart va dans la ligne Sources. Les deux exemples
  de cette fiche sont en 16:9 ; en 9:16 leur premier plan se recompose.
  Constaté sur une session.

Le style conserve les blocs lumière et look par plan, `01-write-shot.md`,
l'attribution des rôles de référence et l'arbitrage d'ancrage de `05-anchoring.md`.
Pour la longueur, appliquer le repère de `SKILL.md`, sans plafond de mots propre
à cette fiche : ne pas supprimer un trait demandé pour rentrer sous 300 mots.

Le piège en réémission : une clause de style contredite par un défaut reporté.
`no slow motion` laissé en queue après qu'un ralenti signature a été écrit dans
un beat annule l'un des deux sans qu'on sache lequel. La checklist de réémission
de `SKILL.md` relit la queue contre le brief courant ; le style fait partie du
brief courant.

---

## Ce qui ne se traduit pas

Ce que le modèle ne sait pas rendre par le texte reste au montage : un arrêt sur
image au frame près, un fondu enchaîné exact, un changement de cadence à
l'intérieur d'un plan, un zoom optique. Ces traits se marquent INVÉRIFIABLE
dans la ligne Sources, et un style qui repose sur le montage, un intercut
multi-caméras par exemple, se reconstruit **au montage à partir de plusieurs
générations**, pas dans une seule. Le dire dans la même ligne, plutôt que de
promettre un plan qui ne peut pas exister ; les points de rupture, eux, ne
portent que des symptômes visibles.

---

## Exemple daté : John Woo

Recherche du 7 septembre 2026. Trois sources, du plus solide au plus faible.

- Jim Malakwen, « John Woo and his influence on action cinema », All The Right
  Movies, 8 septembre 2022 : ralenti appris de Sam Peckinpah ; plusieurs
  caméras tournant à des cadences différentes sur un même morceau d'action ;
  plan-séquence rare chez lui ; colombes ; standoff mexicain.
  https://alltherightmovies.com/feature/john-woo-and-his-influence-on-action-cinema/
- « The 165th Best Director of All-Time: John Woo », The Cinema Archives, 21
  mars 2020, avec des notes de plans de James Trapp, 2023 à 2025 : « slow-motion
  work, dissolves, jumps, freezes » ; contre-plongée et contre-plongée extrême ;
  plongée zénithale ; caméra en 360, caméra constamment en mouvement ;
  silhouettes ; faible profondeur de champ ; le plan des deux pistolets croisés.
  https://thecinemaarchives.com/2020/03/21/the-165th-best-director-of-all-time-john-woo/
- « John Woo: King of Gunfire, Trademarks », page de fans non datée, source
  faible à n'employer qu'en recoupement : arrêt sur image « pour capturer
  l'expression du protagoniste », dos à dos, miroir, juxtaposition.
  https://fabkid.tripod.com/wootrade.html

**Tri.** Canaux : ralenti (vitesse) ; cadences multiples (rythme, donc structure
de coupe) ; contre-plongée et zénithal (angle) ; caméra en 360 (mouvement) ;
silhouette (lumière) ; faible profondeur (optique) ; face à face, dos à dos,
miroir (mise en place) ; arrêt sur image et fondus (rythme, précision à contrôler).
Motifs, donc objets : colombes, deux pistolets, trench, lunettes. Hors canal :
honneur, loyauté, « opératique ».

**Traduction** pour un brief illustratif de 10 s : un homme en trench, un
pistolet dans chaque main, sort d'une église et se tourne vers la caméra ;
un vol de colombes est explicitement prévu. Ces motifs appartiennent à cet
exemple, ils ne s'ajoutent pas automatiquement à un brief « à la John Woo ». Seule la partie caméra et rythme est montrée ; identité,
bloc lumière par plan,
audio et queue suivent le squelette habituel.

```
10-second 16:9 piece of three connected shots.
Shot 1 (0-4s, low-angle wide): the camera sits near ground level at the foot of
the church steps, tilted up; his full figure is visible from head to feet,
about a third of the frame height, the doorway and facade filling the rest. He
pushes both doors open and walks straight down the steps toward the lens at a
steady pace, one black pistol in each hand, arms down. Camera: one slow
continuous rise of about half a metre, from ground level to knee height,
tilting down as it rises so his head stays in the upper third of the frame; it
ends there and does not push in. Natural real-time speed.
Shot 2 (4-7s, extreme low-angle medium): cut to a medium from knee height,
tilted up; he stops on the last step, plants his feet, and turns his upper body
to face the camera, both pistols rising until the arms cross at the wrists,
muzzles toward the lens. The camera performs one slow arc of about thirty
degrees to screen-right, ending on his three-quarter profile.
Shot 3 (7-10s, medium close-up, slow motion): cut to a medium close-up on his
face and shoulders, the doors still open behind him. Slow motion starts on the
exact frame the first dove clears the doorway, not before. About a dozen white
doves burst out of the open doorway across the frame, covering most of the
upper half at their widest, wings spread, and the last one leaves the top of
frame before the end. Strong backlight from the open doorway; his figure reads
as a dark silhouette rimmed with light. Camera: one slow continuous push in of
about half a metre, from this medium close-up to a tight close-up on his eyes,
starting on the same frame as the slow motion and ending with the last dove.
Ends on the doors open, the frame clear of doves, his eyes on the lens.
```

**Ce qui a été gardé** : contre-plongée sur les trois plans, la caméra en
mouvement sur les trois plans et un seul mouvement par plan, trait sourcé
« caméra constamment en mouvement », ralenti ancré sur un événement dans le
seul plan dont il est l'événement, pistolets croisés en mise en place,
colombes en objet quantifié, silhouette par contre-jour, structure montée en
trois plans.

**Ce qui n'est pas retenu dans cet exemple** : l'arrêt sur image et le fondu,
pour garder les trois actions lisibles dans les 10 s choisies ; si le brief
les demande, les écrire ou proposer leur réalisation au montage. La
caméra en 360 est remplacée ici par un arc de trente degrés pour cette
composition ; 10 s n'est pas une impossibilité physique générale pour une orbite ; « opératique », adjectif.

**Ce qui a été retiré du squelette par défaut** : `natural real-time speed` ne
porte que sur les plans 1 et 2, et `no slow motion` ne figure pas dans la queue.

**Niveau de confiance.** Les traits sont sourcés et datés. La traduction en
clauses est une application des fiches existantes. Que le modèle rende un
ralenti ancré sur une image nommée est un constat de session, `03-sequence.md`,
non isolé par un test. L'exemple est illustratif : sur un vrai brief, la
recherche se refait, parce qu'une signature est un fait et qu'un fait se
vérifie.

---

## Exemple daté : Michael Bay

Recherche du 9 septembre 2026. Six sources, du plus précis au plus faible.

- Johnathan Paul, « How to Craft an Epic Tracking Shot Like Michael Bay »,
  PremiumBeat, 18 novembre 2015 : le plan héros, « the camera will move from
  left to right as the character rotates from right to left » ; « Bay will
  always use a telephoto lens », qui « forces the background to pass by at an
  incredible rate » ; « the lens is almost always placed at a low angle » ;
  fonds chargés en information visuelle pour renforcer la parallaxe ; les
  acteurs « moving vertically and turning in a horizontal motion that
  contrasts that of the camera » ; « he slows it down slightly ».
  https://www.premiumbeat.com/blog/how-to-craft-an-epic-tracking-shot-like-michael-bay/
- SC Lannom, « What is Bayhem? Michael Bay Directing Style Explained »,
  StudioBinder, 10 mars 2019, mis à jour le 28 mai 2025 : caméra rapide sur
  l'axe Z autant que sur l'axe Y ; travelling latéral à distance fixe ; angles
  hollandais ; contre-plongée « so that both the object and both the actors
  are in the frame » ; silhouettes par couches de lumière ; profondeur par
  panneaux, véhicules, bâtiments, lampadaires ; tailles de plan qui changent à
  chaque coupe ; « progressively quicker cuts » ; l'action en plan large, la
  réaction en plan serré ; le plan héros en 360.
  https://www.studiobinder.com/blog/what-is-bayhem-michael-bay-directing-style/
- Bruce Bennett, « The Cinema of Michael Bay: An Aesthetic of Excess », Senses
  of Cinema, dossier 2015, page sans signature visible, auteur établi par le
  dépôt de l'université de Lancaster, eprints 73962 : caméra « carousel-like »
  qui tourne sans arrêt
  autour des interprètes ; grue et hélicoptère ; caméra portée, crash zooms,
  whip pans ; plongées et contre-plongées, dont l'avion qui passe au-dessus
  en ralenti ; cadre penché ; contre-jour diffusé dans la fumée ; plans qui
  durent « a fraction of a second » ; palette saturée non naturaliste, bleu,
  jaune, vert.
  https://www.sensesofcinema.com/2015/michael-bay-dossier/cinema-of-michael-bay/
- Scott Macaulay, « What is Bayhem? The Secret of Michael Bay's Shots »,
  Filmmaker Magazine, 3 juillet 2014, sur l'essai vidéo de Tony Zhou :
  « parallax, off-screen space, compression and speed ».
  https://filmmakermagazine.com/86534-what-is-bayhem-the-secret-of-michael-bays-shots/
- V Renée, « The 6 Ingredients Needed to Make a Film like Michael Bay », No
  Film School, 8 mars 2017 : bouger la caméra beaucoup, plans héros en 360,
  contre-plongées extrêmes, travelling porté.
  https://nofilmschool.com/2017/03/watch-6-ingredients-needed-make-film-michael-bay
- Academy, A.frame, « Cinematographer Roberto De Angelis Levels Up for Michael
  Bay's Chaotic Ambulance », 7 avril 2022 : drones FPV qui plongent et
  tournent depuis les toits, plus de cent installations par jour en
  multi-caméras.
  https://newsletter.oscars.org/news/post/cinematographer-roberto-de-angelis-levels-up-for-michael-bays-chaotic

**Tri.** Canaux : arc latéral autour du sujet, caméra en 360, grue,
hélicoptère, FPV (mouvement) ; contre-plongée, cadre penché (angle) ; tailles
qui changent à chaque coupe, action en large et réaction en serré (tailles) ;
ralenti léger sur le plan héros, coupes de plus en plus courtes, crash zoom,
whip pan (rythme et vitesse) ; le sujet qui se relève et tourne à contresens de
la caméra, l'avant-plan qui traverse (mise en place) ; contre-jour dans la
fumée, silhouette, palette saturée bleu et jaune (lumière) ; téléobjectif et
parallaxe (optique, donc effet visible). Motifs, donc objets : explosions,
véhicules, hélicoptère. Hors canal : « spectacle », « excès », « adrénaline ».

**Traduction** pour un brief de 10 s, 16:9, une femme accroupie derrière le
capot d'une voiture sur un boulevard de nuit se relève et se retourne quand un
hélicoptère passe. Seule la partie caméra et rythme est montrée ; identité,
bloc lumière et look par plan, audio et queue suivent le squelette habituel.
Le boulevard vient d'une plaque validée, `05-anchoring.md`, parce que la
parallaxe a besoin d'un fond dense qu'on ne laisse pas au modèle.

```
10-second 16:9 piece of three connected shots.
Shot 1 (0-3s, low-angle wide, dutch): the camera sits at knee height on the
far kerb, tilted up, the frame tilted about fifteen degrees with the horizon
rising toward screen-right; she is crouched behind the hood of the parked
car, her whole figure visible, about a quarter of the frame height, the
boulevard's lit shopfronts, signs and light poles filling the rest. Traffic drives on
the right; from this kerb the near lane runs screen-left to screen-right and
the far lane the other way, both seen in flank so no lamp faces the lens. A
dark sedan sweeps through the near lane in the foreground from screen-left to
screen-right, filling the lower third of the frame for about one second, and
clears. The traffic holds its lanes. Camera:
one slow continuous truck of about one metre to its left along the kerb, the
parked car's rear wing sweeping across the near foreground and out of frame,
the lit shopfronts sliding much less behind her; it does not push in. Natural
real-time speed.
Shot 2 (3-8s, low-angle medium, slow motion): cut to a medium from waist
height, tilted up, three metres from her. Camera: one continuous arc of
about ninety degrees from screen-left to screen-right around her, at a
steady pace, holding this distance. Subject: she rises from the crouch to
standing and turns her upper body the opposite way, from screen-right to
screen-left, until she faces the lens; the two turns cross. Slow motion
starts on the exact frame her knees leave the ground, not before. Behind
her the lit shopfronts, signs and light poles slide across the frame faster
than she turns, stacked flat and close behind her, the far end of the
boulevard softening into haze.
Shot 3 (8-10s, low-angle medium close-up): cut to a medium close-up from
chest height, tilted up, her face and shoulders about half the frame
height, the night sky filling the upper third. A helicopter crosses the sky
behind her head from screen-left to screen-right, about a fifth of the
frame width, and exits before the end; as its searchlight crosses behind
her head, a horizontal streak of light crosses the lens from screen-left
for about half a second. Backlight from the searchlight through the street
haze rims her hair and shoulders; her figure reads as a near silhouette
with her eyes lit. Camera: one slow continuous rise of about thirty
centimetres, tilting down as it rises so her eyes stay on the upper third
line, ending as the helicopter leaves the frame. Natural real-time speed. Ends
on her eyes on the lens, the sky clear.
```

**Ce qui a été gardé** : contre-plongée sur les trois plans, la caméra en
mouvement sur les trois plans et un seul mouvement par plan, trait sourcé
« bouger la caméra beaucoup », l'arc latéral contre la rotation du sujet qui
se relève, le ralenti ancré
sur le seul plan dont le geste est l'événement, la parallaxe écrite comme
effet visible, l'avant-plan qui traverse avec sa trajectoire et sa durée,
le cadre penché chiffré, le contre-jour dans la brume, le flare écrit en
positif comme événement lumineux daté, la structure montée en trois plans de
tailles différentes, l'hélicoptère en objet quantifié.

**Ce qui a été adapté dans cet exemple** : les plans d'une fraction de seconde
et le montage de plus en plus court sont proposés au montage pour leur précision,
sans présenter 1,5 s comme une limite native ; le crash zoom et le whip pan
ne sont pas retenus dans ce découpage, mais peuvent être décrits s'ils sont
demandés, selon `01` et `15` ; le 360
complet, remplacé par un arc de quatre-vingt-dix degrés en 5 s, ce qui tient la
règle 1 et la lisibilité ; le téléobjectif en tant que focale, non tenable
depuis le prompt, remplacé par son effet ; la palette saturée bleu et jaune,
absente du brief et du look de la plaque, non ajoutée ; « spectacle »,
« adrénaline », adjectifs.

**Ce qui a été retiré du squelette par défaut** : `natural real-time speed`
ne porte que sur les plans 1 et 3, `no slow motion` ne figure pas dans la
queue, et le verrou `clean crisp glass` de `12-constraints.md` ne figure pas
non plus, puisque le flare du plan 3 est voulu.

**Niveau de confiance.** Les traits sont sourcés et datés ; deux d'entre eux,
la parallaxe et le sujet qui se relève à contresens, viennent d'une seule
source détaillée et se recoupent avec l'essai de Tony Zhou par la mention de
la parallaxe. Que le modèle rende deux rotations croisées, caméra et sujet,
dans un même plan n'a pas été observé sur un rendu : point de rupture à
regarder en premier, avec le flare, que le modèle peut étaler sur tout le plan
au lieu d'une demi-seconde.

---

## Checklist

- [ ] Le nom seul ne remplace pas les décisions visibles ; la convention par
      défaut de traduction respecte toute demande explicite contraire.
- [ ] Chaque trait retenu a un canal et une clause qu'on peut citer.
- [ ] Les traits supprimés sont nommés dans la ligne Sources, avec la raison.
- [ ] Les sources sont datées dans la ligne Sources du self-eval, jamais dans le
      prompt.
- [ ] Les défauts contredits par le style, ralenti, coupes, mouvement, sont
      retirés de la ligne de format et de la queue, pas laissés à côté.
- [ ] Ce qui est prévu au montage est annoncé comme tel. Une exécution native
      non testée n'est pas présentée comme fonction absente de la documentation.
