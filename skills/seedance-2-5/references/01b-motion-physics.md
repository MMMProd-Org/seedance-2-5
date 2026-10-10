# 01b Mouvement et physique

Le mouvement du sujet et sa physique : report d'état, cause avant réaction,
contacts, occlusions, fluides, particules, vitesse. Scindée de `01-write-shot.md`
en septembre 2026 quand cette fiche a dépassé son plafond de 500 lignes ; `01`
garde la caméra et la composition, `12` la clôture.

À ouvrir avec `01` dès qu'un sujet bouge, se pose, manipule un objet, ou qu'un
fluide, un tissu, des cheveux ou des particules sont dans le plan.

---

## Sommaire

- Report d'état physique
- Cause avant réaction
- Axe, porteur et régime d'une impulsion
- Décomposition en contacts
- Continuité sous occlusion
- Fluides, tissus, cheveux, fumée, particules
- Vitesse, et la vitesse d'un geste
- Le bas du corps
- Circulation routière
- Jeu

---

C'est la fiche qui sépare un plan qui compile d'un plan exploitable. Deux
faiblesses que le skill d'origine attribue à ByteDance, attribution non
retrouvée dans les pages ModelArk 2.5, `07-spec.md` : la plausibilité physique
des mouvements complexes, et la stabilité des scènes à plusieurs sujets en
interaction. Tout ce qui suit sert à ne pas se poser dessus.

---

### Report d'état physique

Chaque beat repart de l'état laissé par le précédent, et on l'écrit.

> The same bike messenger wears a yellow rain jacket and carries one red bicycle
> helmet in the left hand throughout. [...] 10-16 seconds: the messenger turns
> toward the counter and walks around one stationary customer without changing
> hands; red helmet remains in the left hand, bottle remains in the right.

Ce qui est verrouillé de cette façon : quelle main tient quoi, ce qui est posé et
où, ce qui est ouvert ou fermé, qui est entré et qui est sorti du cadre.

Pour un mécanisme, une projection fantastique ou un objet lancé qui revient
sous un autre angle, voir [16-effects-mechanisms.md](16-effects-mechanisms.md) :
identité distincte de l'état, liaisons visibles et continuité de l'événement.

C'est plus efficace qu'une clause de continuité isolée en fin de prompt, parce
que le modèle relit l'information au moment où il en a besoin.

---

### Cause avant réaction

« Le client a l'air surpris » laisse trop ouvert : la réaction peut arriver avant
sa cause, ou tout le monde peut réagir en même temps.

Écrire quatre actions distinctes : **contact, mouvement résultant, son,
réaction**, chacune avec son moment.

> 4-8 seconds: a busboy passes behind the seated customer; the edge of his tray
> lightly catches the cup handle. The cup tips only after contact, strikes the
> counter, and coffee begins spreading toward the sketchbook. 8-11 seconds: the
> customer hears the impact, looks down, lifts the sketchbook just before
> the coffee reaches it, and looks up at the busboy. Nearby diners turn toward
> the sound at slightly different delays.

Deux formulations qui font le travail : « only after contact » interdit
l'anticipation, « at slightly different delays » interdit la réaction chorale.

---

### Axe, porteur et régime d'une impulsion

Une secousse écrite sans ces trois choses est rendue au hasard, et le hasard du
moteur a une préférence. Cas constaté le 9 septembre 2026 : un plan intérieur
automobile de 4 secondes, caméra verrouillée sur le coussin du siège passager,
portait `the whole cabin jolts once as the gear engages`. Au rendu, le
conducteur a sauté verticalement dans son siège.

**Règle A, le porteur.** Toute impulsion nomme lequel des trois objets la porte :
le cadre, c'est à dire l'image qui tremble ; le véhicule ou le décor ; ou le
corps du personnage. Et elle dit ce que font les deux autres pendant ce temps.
Sans porteur nommé, le moteur peut appliquer la secousse au corps, comme dans
le cas observé. Ce constat ne prouve pas un comportement systématique :
distinguer le mouvement du véhicule, celui du support caméra et la réaction
du passager avant d'écrire.

| Faible | Fort |
|---|---|
| `the whole cabin jolts once as the gear engages` | `A small camera-mount vibration briefly shifts the framing vertically by about one percent of frame height, then settles. The cabin, the seat and the dashboard do not move relative to each other. His body does what the longitudinal line below describes.` |

**Règle B, l'axe.** Toute impulsion nomme son axe, longitudinal, latéral ou
vertical, et le mouvement du corps qui en résulte, avec son point d'appui et son
retard s'il y en a un. C'est l'application directe de la section Cause avant
réaction ci-dessus, à une force qui n'a pas de contact visible. La règle y est
déjà écrite et elle ne s'est pas déclenchée à la rédaction, parce qu'une règle
logée dans une fiche ne se relit pas quand on ne sait pas qu'on en a besoin :
d'où la ligne de checklist de `SKILL.md`, invariant 8 de `14-maintenance.md`.

**Règle C, la réponse résultante.** Le corps peut subir une accélération tout en
se retenant volontairement. Écrire la cause, l'appui et le résultat compatible :
« le freinage entraîne le buste vers l'avant ; la ceinture et la main déjà
appuyée limitent cette avancée ». Éviter deux positions incompatibles au même
instant, pas le mélange naturel d'inertie et de compensation. Le cas de
production signalait des consignes ambiguës, pas une impossibilité physique.

**Événements automobiles courants.** Pour une voiture roulant en avant, sauf
autre sens explicitement décrit ; amplitudes dépendantes du véhicule, des
retenues, des appuis et de l'intensité de l'accélération.

| Événement | Sollicitation principale | Réponse à décrire selon le cas |
|---|---|---|
| Freinage | Longitudinale | Le buste tend vers l'avant, limité par ceinture et appuis ; retour après stabilisation, sans embrayage inventé |
| Passage de rapport | Variation du couple transmis | Une coupure puis reprise de traction peut solliciter le buste avant/arrière ; dépend de la transmission et du régime, sans latence universelle de la tête |
| Accélération | Longitudinale | Le dossier soutient le corps ; tangage possible selon suspension et transfert de charge |
| Bosse, joint, nid-de-poule | Verticale, éventuellement tangage/roulis | Réponse courte amortie par suspension et siège ; ce n'est pas la seule cause possible de déplacement vertical |
| Virage, changement de file | Latérale | Le corps tend vers l'extérieur de la courbe, limité par ses appuis ; roulis possible de la caisse |

Ne pas ajouter un saut vertical du conducteur à un changement de rapport.
Cela n'interdit pas un léger tangage ou mouvement vertical justifié par la
suspension. L'accélération, et non le seul sens de déplacement, gouverne
l'inertie. Pour une marche arrière, raisonner depuis le vecteur d'accélération.

- [ ] Porteur, cause, axe dominant et appuis identifiés.
- [ ] Caméra, véhicule et corps ont des mouvements relatifs compatibles.
- [ ] Effet subi et compensation volontaire donnent une seule réponse cohérente.

Base physique : [MathWorks, Vehicle Body 3DOF Longitudinal](https://www.mathworks.com/help/vdynblks/ref/vehiclebody3doflongitudinal.html),
consulté le 10 septembre 2026, sans date affichée : modèle couplant translation
longitudinale, déplacement vertical et tangage. Les prescriptions de formulation
restent des hypothèses de prompting issues d'une session, sans test isolé.

---

### Décomposition en contacts

**Arbitrage à connaître avant d'appliquer cette section.** Le guide ModelArk
2.5 recommande l'inverse par défaut : décrire les actions **en général**, « plusieurs
séries de montées de genoux et de saltos », « les deux camps engagent un corps à
corps », et ne détailler que quelques actions mémorables, sans répéter les mêmes.

Les deux positions ne portent pas sur le même objet. La description générale
protège contre la surcharge, qui est le mode d'échec courant : un beat bourré de
gestes minutés perd la moitié de ses instructions. La décomposition en contacts
sert quand **la physique elle-même est le sujet du plan**, un atterrissage, un
transfert de force, une manipulation d'objet, c'est à dire précisément là où
le modèle est le plus faible.

Règle d'usage : **une seule action décomposée par plan, le reste en général.**
Décomposer trois gestes dans le même beat revient à recréer la surcharge que la
décomposition devait éviter.



« Il saute par-dessus le plot » laisse l'essentiel du mouvement non spécifié.
Nommer approche, contact, transfert de force, ordre d'atterrissage, encaissement,
puis retour à l'équilibre.

> 6-8 seconds: the rear foot snaps the tail against the concrete, the board
> rises, the front foot slides forward, and both rider and board clear the cone
> together. 8-10 seconds: the front wheels contact first, then the rear wheels;
> his knees compress from the landing and his arms correct his balance. 10-12
> seconds: he straightens and rides away without another trick.

Trois points qui reviennent :

- **Le membre exact** compte, et où le poids passe ensuite.
- **L'ordre d'atterrissage** se nomme : roues avant puis roues arrière.
- **Dire comment ça se pose**, au lieu de s'arrêter sur l'image la plus
  spectaculaire. Sans état de repos, le modèle enchaîne une deuxième figure ou
  fige.

Même structure pour le sport, la bagarre, la danse et la manipulation d'objet.

Pour une manipulation fine, décrire l'équilibre, la direction, le contact et le
rythme plutôt que l'intention :

> She presses her left hand on the counter, lifts the brass tube from her right
> shoulder with both hands, rotates it horizontally, and sets it down without
> sliding it.

---

### Continuité sous occlusion

Un objet ne cesse pas d'exister quand une colonne, une voiture ou une personne le
masque. Si le prompt ne décrit que l'entrée et la sortie, la partie couverte
devient un point de réinitialisation.

Écrire **combien de temps le sujet est caché** et **répéter ce qui doit revenir
identique**.

> 3-5 seconds: she passes completely behind one thick concrete support
> column; both woman and suitcase are fully hidden for just under two seconds.
> 5-9 seconds: the same woman emerges from the opposite side of the column
> with the same face, hair, green coat, black boots, red suitcase, extended
> handle, walking speed, and direction.

« La même femme ressort » est plus faible que la liste. Ajouter la négation qui
va avec : « No person or suitcase appears on both sides of the column at once. »

---

### Fluides, tissus, cheveux, fumée, particules

Nommer **la direction de la force** et **l'état laissé après l'arrêt du
mouvement**. « Physique réaliste » ne contient aucune de ces deux informations.

Un écoulement se suit en quatre temps : contact, écoulement, accumulation,
séparation.

> 4-9 seconds: one continuous amber stream lands on the butter, divides around
> it, and runs down the pancake edges under gravity. Syrup pools on the plate and
> does not flow uphill. 9-12 seconds: the stream narrows, stretches, then breaks
> cleanly before the pitcher leaves frame. 12-15 seconds: the butter softens
> slightly and slides only a few millimeters before stopping.

Deux verrous récurrents : « does not flow uphill » et « breaks cleanly ». Et les
dernières secondes ne lancent rien de neuf, elles laissent le mouvement existant
se poser.

**Un événement de particules porte sa quantité, sinon le modèle rend le
minimum.** « Splinters burst toward the lens » produit trois éclats. La quantité
ne s'écrit pas en adjectif, « dense », « massif », qui sont des adjectifs de
goût, mais en **fraction de cadre occupée**, en ordre de grandeur, et en
distribution des tailles :

> A spray of splinters bursts out of the cut toward the lens, dozens of
> chips of every size expanding until they cover most of the frame, the biggest
> ones tumbling end over end, several striking the lens and staying stuck there.

Trois valeurs suffisent : combien, quelle part du cadre à l'apogée, et ce qui
arrive aux plus gros. Constaté sur une session, non isolé par un test à variable
unique.

---

### Vitesse

Éviter le mot nu « fast ». Décrire concrètement : whip pan, départ explosif, se
cale en position. Éviter aussi le ralenti involontaire, qui est ce que le modèle
produit quand une durée trop longue rencontre trop peu d'événements. La parade
est double : `natural real-time speed` en tête, `no slow motion` en queue.

**La vitesse d'un geste s'écrit par son arrêt.** Le défaut du moteur est un
geste moyen, lissé, qui accélère et ralentit doucement. Un adverbe ne le change
pas : « quickly », « sharply », « fast » sont lus comme du registre. Ce qui le
change, c'est de nommer les trois temps et surtout le dernier : le départ, le
trajet, **et ce qui arrête le geste**. Un geste sans arrêt nommé s'éteint en
fondu et se lit comme lent, quelle que soit la durée écrite.

| Faible | Fort |
|---|---|
| `he quickly grabs the handle` | `his hand leaves his side and closes on the handle in about a fifth of a second, and stops dead there, the handle not moving yet` |
| `she turns sharply` | `her head snaps from the window to the door and stops square on it, her shoulders arriving a beat later` |

Une durée chiffrée courte, « in about a fifth of a second », est une hypothèse
de travail : elle sert surtout à interdire le geste lissé. L'arrêt nommé, lui,
est ce qui a changé le rendu sur une session.

### Le bas du corps

`02a-perform.md`, Le corps avant le visage, pose déjà le poids, les appuis et
l'orientation des épaules comme des canaux de jeu, et `01-write-shot.md` les
reprend pour le plan large. Ce qui manque n'est pas la doctrine, c'est le
traitement d'un **geste** de pied ou de jambe : un geste de pied écrit au milieu
de trois clauses de regard perd, parce que la longueur consacrée à un élément
est aussi une consigne, section Tenir une taille de plan et une composition de
`01-write-shot.md`.

Trois conséquences pratiques.

- **Un geste de pied qui compte prend son propre beat**, et les autres canaux se
  taisent pendant ce beat. Le décrire en plus du reste, c'est le perdre.
- **Le nommer par l'appui**, jamais par le membre seul, en appliquant au geste
  ce que `02a-perform.md` dit du corps : quel pied porte le poids, quel pied
  part, ce que le pied touche, dans quel ordre, et où le poids finit. « Il tape
  du pied » ne dit ni l'appui de départ ni l'arrivée.
- **Si la physique du geste est le sujet du plan**, c'est une décomposition en
  contacts, section ci-dessus, avec sa règle d'une seule action décomposée par
  plan. Sinon, une phrase d'appui suffit.

Constaté sur une session, non isolé par un test à variable unique.

---

### Circulation routière

**Vérifier le contexte lorsqu'un véhicule roule ; remplir seulement les champs
applicables.** Patron 19 de `08-templates.md`. Un plateau vide, un parking ou
un trajet hors route n'impose ni pays, ni files, ni giratoire, ni autres voitures.
Marquer ces champs sans objet dans le contrôle interne et garder dans le prompt
uniquement les éléments utiles ; ne pas peupler la scène pour remplir le bloc.

1. **Côté et file**, si la scène comporte une circulation routière : les prendre
   dans le brief ou le contexte. Ne pas modifier la trajectoire demandée pour
   appliquer une convention supposée.
2. **Giratoire**, seulement s'il est présent : décrire son sens effectif et les
   trajectoires voulues. Un giratoire ordinaire en circulation à droite se
   parcourt dans le sens antihoraire ; à gauche, horaire. Une action fictive
   explicitement à contresens reste une action à décrire, avec son contexte.
3. **Direction et face visible**, pour chaque véhicule utile. En marche avant,
   face avant et phares blancs peuvent venir vers une caméra fixe ; l'arrière
   et ses feux rouges peuvent s'en éloigner. Ce raccourci ne s'applique ni à la
   marche arrière ni à tous les suivis caméra. Un véhicule reculant vers
   l'objectif montre son arrière, éventuellement ses **feux de recul blancs
   et ses feux arrière rouges simultanément**. Un profil peut masquer les feux.
   Vérifier orientation, roues, déplacement relatif et état des lampes ; leur
   couleur seule ne prouve pas le sens du déplacement.
4. **Réponse du trafic**, seulement s'il existe : réévaluer le conflit de
   trajectoires et la distance disponible. Un autre véhicule peut tenir sa
   ligne, ralentir, freiner ou éviter selon la scène ; ne pas imposer un écart
   et un freinage à tout dépassement, ni un trafic complaisant qui s'écarte
   sans cause.

| Configuration | Contrôle pertinent |
|---|---|
| Giratoire | Sens du flux et trajectoire du héros explicitement compatibles, ou conflit voulu décrit |
| Chaussée à double sens | Chaque flot dans sa voie ; face réellement visible selon caméra et trajectoire |
| Voie à sens unique | Même sens de circulation, hors manœuvre ou infraction expressément demandée |
| Marche arrière sur plateau vide | Orientation du véhicule, arrière qui approche, lampes demandées ; aucun trafic ajouté |

- [ ] Champs applicables présents, champs sans objet non inventés.
- [ ] Sens de marche, orientation et déplacement relatif distingués.
- [ ] Feux cohérents avec la face vue et l'action, pas déduits de « vers/loin » seul.
- [ ] Réaction du trafic justifiée pour cette manœuvre.

Le bloc est une aide de continuité proposée après une session du 9 septembre
2026. Ce n'est ni une obligation du moteur ni une prescription réglementaire.

---

### Jeu

Le jeu d'acteur a sa propre fiche : `02a-perform.md`. Ce qu'il faut en retenir
ici, parce que ça touche au mouvement : le comportement observable remplace
l'adjectif d'émotion, un silence se dirige avec un verbe comme une action, et un
personnage qui n'a pas de changement d'état nommé garde la même expression du
premier au dernier plan.
