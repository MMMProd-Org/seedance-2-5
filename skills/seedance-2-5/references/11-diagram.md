# 11 Le diagramme de mise en place

Quand un plan compte plusieurs personnages, le texte cesse de tenir la mise en
place. Qui est où dans le cadre, dans quelle posture, tourné vers qui : ces trois
faits se décrivent bien et se rendent mal, parce qu'ils forment une géométrie et
que la prose n'en porte que la variance.

Le diagramme est la parade. On fournit au modèle un **schéma plat de la
disposition**, une figure par personnage, chacune dans sa couleur, et le prompt
lie chaque couleur à un personnage réel. Le modèle lit des positions, des poses
et des directions de face au lieu de les déduire.

Le principe qui fait fonctionner la méthode : **la carte n'est pas une image à
imiter, c'est un système de données spatiales.** Lignes, couleurs, orientations.
Tout ce qui la ferait ressembler à une esthétique est un parasite.

**Niveau de confiance.** Méthode rapportée par une production photoréaliste
longue, avec un gain qualitatif annoncé sur le taux de plans à mise en place
juste. Aucun test à variable unique, aucun chiffre mesuré ici. Le mécanisme est
cohérent avec la doctrine d'ancrage de `05-anchoring.md` : c'est de la géométrie
fournie plutôt que déduite.

---

## Sommaire

- Quand y aller
- Le workflow
- Le bloc connecteur
- Les trois gardes
- Éditer un diagramme
- Couverture, trajectoires, mouvements caméra
- Diagramme, maquette blanche, planche : lequel

---

## Quand y aller

- Trois personnages ou plus dans le même cadre.
- Deux personnages dont les places et les regards doivent tenir sur une série de
  plans, la scène de dialogue tenue dans un seul décor.
- Une mise en place précise que la prose a déjà ratée une fois.
- Un contrechamp ou une redécoupe dans un espace déjà établi.

### Diagramme ou ancrage image

Les deux répondent au même principe, fournir la géométrie plutôt que la faire
deviner, mais pas à la même question, et `05-anchoring.md` demande de basculer sur
l'image dès qu'une séquence dépasse deux plans. L'arbitrage :

| La question | L'outil |
|---|---|
| Le **cadre** doit être exactement juste : composition hero, contrechamp dans un espace jamais montré, face non vue d'un décor | Image d'ancrage. Chaque plan part de sa propre image |
| La **disposition des personnes** doit tenir, dans un espace déjà porté par une plaque de décor validée | Diagramme. Le plan se génère depuis les références, la carte tient les places |

Le cas courant d'une scène de dialogue tenue dans un décor unique tombe dans la
seconde colonne : l'espace ne change pas, il est déjà dans la plaque, et ce qui
dérive d'un plan à l'autre est la place des corps et la direction des regards.
Produire une image fixe par plan y coûterait une planche entière pour figer une
information que le schéma porte en une passe.

Les deux se combinent quand le doute persiste : générer le cadre depuis le
diagramme, valider l'image, puis l'employer comme première frame.

C'est le correctif direct du mécanisme 7 de `02b-perform-failures.md` : la
stabilité des scènes à plusieurs sujets en interaction est une faiblesse reconnue
du modèle. Sortir du cadre les personnages muets reste la parade la plus
économique ; le diagramme est ce qu'on emploie quand ils doivent rester.

---

## Le workflow

1. **Partir d'un cadre réel.** Un photogramme, une génération précédente, une
   composition de référence. C'est lui qui porte la géométrie.
2. **Écrire le prompt de diagramme.** Le cadre y est déclaré **guide de
   composition seulement** : cadrage, angle, recadrage, positions, poses. Rien de
   son rendu photographique. Les corps coupés par le bord restent coupés, et
   aucun élément absent du cadre n'est ajouté.
3. **Générer le schéma** dans un modèle d'image. Trait plat sur fond blanc, une
   figure par personnage en contour fin, chacune dans sa couleur sourde propre,
   le mobilier en formes de contour simples, une grille très faible. **Aucune
   lettre, aucune étiquette nulle part sur le dessin.**
4. **Joindre le schéma au prompt vidéo** et écrire le bloc connecteur, qui lie
   chaque couleur à un personnage réel et borne la portée de la carte.

Le prompt de plan reste ce qu'il était, avec ses références de décor, de
personnages et d'accessoires. Le diagramme s'ajoute, il ne remplace rien : il ne
porte ni visage, ni costume, ni lumière, ni matière.

---

## Le bloc connecteur

Une ligne par figure, couleur d'abord, puis le token du personnage, puis sa place
et sa direction de face. Puis une clause de portée.

```
@image7 is a flat position map. It defines placement, pose, and facing direction
only.
The BLUE figure is the man defined by @image1: reclined along the couch, facing
frame-right.
The GREEN figure is the man defined by @image2: seated in the armchair at
frame-right, facing frame-left.
The AMBER figure is the man defined by @image3: seated in the armchair at
frame-left, facing frame-right.
The GREY figure is the man defined by @image4: seated in the near foreground
armchair at frame-right, back to camera.
Faces, wardrobe, materials, lighting, and photographic look come only from
@image1 to @image6.
```

**Une seule convention d'adressage par prompt.** Les exemples de cette fiche sont
en index, comme le reste du skill. Sur une surface qui lit les assets de projet
nommés, remplacer chaque `@imageN` par son nom et ne rien changer d'autre. Voir
`10-syntax.md`. Mélanger les deux formes dans un même prompt laisse au moins un
pointeur mort.

Deux points portent tout le bloc.

**La couleur est l'adresse.** Elle est lue dans le dessin sans risque
d'ambiguïté, là où « le personnage de gauche » dépend de qui regarde.

**La portée se borne en positif.** Dire ce que la carte définit, et d'où vient le
reste. Ne jamais écrire ce qu'elle ne doit pas apporter en nommant son style
graphique : voir la garde suivante.

---

## Les trois gardes

**Les lettres vivent dans le texte, jamais dans le dessin.** Nommer les figures A,
B, C dans le prompt si c'est commode, mais lier chaque lettre par sa couleur. Une
lettre dessinée sur la carte est un caractère que le modèle peut incruster dans
le plan rendu.

**Le connecteur s'écrit en forme positive seulement.** Ne jamais nommer le style
graphique de la carte, même dans une interdiction. « no flat illustration », « ne
pas rendre le style schématique » injectent les mots *flat* et *schématique* dans
un prompt qui décrit une image à fabriquer. C'est le cas particulier le plus net
de la règle générale sur les négations qui invoquent, `12-constraints.md`.

**La carte est une vue de face, depuis l'axe caméra.** Jamais un plan au sol vu de
dessus. Un modèle vidéo pense en cadres, pas en plans d'architecte : un plan
masse lui demande une projection, c'est à dire exactement la déduction qu'on
cherchait à supprimer.

---

## Éditer un diagramme

Les corrections se demandent dans la conversation où le prompt de diagramme
d'origine a été écrit : elle porte la clé des couleurs et la géométrie complète,
donc la retouche reste cohérente.

**Nommer par la couleur, jamais par la personne ou l'objet.** « déplacer la
figure BLEUE vers le bord gauche du canapé », pas « déplacer Rudy ». Les couleurs
sont la langue du diagramme ; les noms de personnages appartiennent au prompt
vidéo. Mélanger les deux registres est ce qui fait dériver la carte vers une
illustration.

**Regénérer toujours depuis le cadre source d'origine, jamais depuis le
diagramme précédent.** Un diagramme se dessine à partir d'un vrai plan. Donner un
dessin au modèle le fait copier les défauts du dessin au lieu de la géométrie du
cadre, et l'écart se compose à chaque tour.

---

## Couverture, trajectoires, mouvements caméra

Une fois qu'une scène a son diagramme, la couverture devient conversationnelle.
« La MCU sur le bleu », « le contrechamp du vert » : on redemande une carte
restaguée pour la nouvelle taille ou le nouvel angle, à partir du même cadre
source.

La convention s'étend à deux autres contenus, dans la même langue de couleurs.

| Contenu | Notation | Ce qu'il faut déclarer |
|---|---|---|
| Trajectoire d'un objet ou d'un déplacement | Chemin pointillé de la couleur de la figure | Départ, chemin, arrivée, et le beat qui la déclenche |
| Mouvement caméra | Flèche | Déclarée `camera path only` dans le bloc connecteur du prompt, jamais sur le dessin, sinon elle est rendue |

La pyramide de caméra, les axes et les lignes de trajectoire tracés sur une
maquette 3D posent le même problème et se retirent avant l'upload, voir
`04-references.md`.

---

## Diagramme, maquette blanche, planche : lequel

Trois entrées structurelles voisines, trois jobs différents. En choisir une par
plan.

| Entrée | Ce qu'elle porte | Quand |
|---|---|---|
| **Diagramme** | Un seul cadre. Positions, poses, directions de face | Une mise en place à figer, plusieurs personnages |
| **Maquette blanche**, vidéo de référence | Mouvement caméra, rythme, transitions de taille, trajectoires et blocking ; changements de lumière seulement s'ils sont présents et voulus, voir `04` | Un mouvement à porter, un espace à traverser |
| **Planche storyboard** | L'ordre des plans et une composition approximative | Un enchaînement à communiquer, sans exigence de cadre exact |

Le diagramme est plat, gratuit et immédiat, et il ne dit rien du mouvement. La
maquette coûte une modélisation et porte le temps. La planche ne verrouille aucun
cadre : si l'alignement doit être strict, ce sont des keyframes, pas une planche,
voir `05-anchoring.md`.
