# 01c Scène d'action

Vitesse perçue, densité utile et repères dans le cadre. Ouvrir avec
`01-write-shot.md` pour une poursuite, un coureur ou un projectile, ou lorsqu'un
rendu paraît lent malgré une vitesse demandée. Le simple fait qu'une voiture
bouge ne transforme pas un plan calme en poursuite.

## Sommaire

- Répartition avec les fiches voisines et niveau de confiance
- Budget d'événements
- Relations entre caméra et sujets
- Repères proches et périphérie
- Ratio et champ disponible
- Repères lointains
- Départ du plan et caméra nerveuse
- Exemple de poursuite
- Checklist

## Répartition et niveau de confiance

`01` gouverne caméra et composition ; `01b` causes, contacts et inertie ; `03`
porte les beats, **un changement principal par beat**. Un échange causal peut
réunir plusieurs gestes. Quatre changements indépendants demandent quatre beats,
pas une nouvelle définition du beat pour les ranger artificiellement en deux.

Les observations de cette fiche viennent d'une seule session du 9 septembre
2026 : une poursuite de 8 s en 9:16, quatre fenêtres écrites mais deux changements
visibles. Elles n'isolent ni le modèle ni la cause de chaque échec. Les seuils
de deux secondes, de moitié du cadre ou de ×1,3 sont des **repères de travail
non validés**, jamais des limites du moteur. La géométrie calculée ci-dessous
est distincte de ces hypothèses et ne garantit pas leur exécution par Seedance.

## Budget d'événements

Compter ce qui change réellement à l'image. Pour une action dense demandée,
environ un changement toutes les deux secondes peut servir de première maquette.
Adapter ensuite au geste, à sa conséquence et au rythme voulu. Une attente,
une accélération continue ou une approche lente peut légitimement durer davantage.
**Ne jamais ajouter un obstacle, un contact ou une coupe pour satisfaire un quota.**

Comparer les états de début et de fin de chaque beat. Une différence utile
peut être une entrée/sortie, une modification de distance ou de taille lisible,
un changement de direction, un contact, un déséquilibre ou son rattrapage.
Cette liste n'est pas exhaustive. Une respiration retenue ou une décision
visible peut aussi changer l'état ; `02a` gouverne le jeu.

| Cas observé comme trop faible dans la poursuite | Diagnostic à envisager |
|---|---|
| Distance tenue | Le sujet reste stable ; vérifier si l'environnement ou l'action porte déjà la vitesse |
| Faible réduction d'écart | Comparer les tailles d'ouverture et de fin ; pas de seuil perceptif universel |
| Décor défilant identiquement à chaque fenêtre | Un mouvement continu, pas quatre événements distincts ; conserver sa durée si c'est l'intention |
| Régime moteur montant seul | Événement sonore ; ne pas le compter comme changement visuel, sans pour autant le supprimer |

Une durée trop chargée perd des actions. Réduire le détail superflu ou proposer
un découpage, en annonçant toute suppression d'un élément demandé. Un repos
ou une conséquence physique n'est pas une seconde inutile.

## Relations entre caméra et sujets

Écrire séparément les trajectoires, puis nommer **chaque paire** dont on décrit
la distance : caméra–coupé, coupé–berline, caméra–berline. Une caméra peut garder
sa distance au coupé pendant que celui-ci rejoint la berline : ces clauses sont
compatibles. Si la caméra reste à distance constante du coupé, focale et angle
constants, sa taille projetée ne peut en même temps augmenter fortement.

Dans la session citée, « the camera holds that distance » et « the coupe closes
fast on a slower saloon » ont coïncidé avec un dépassement absent. La relation
de « that distance » était ambiguë ; cela ne prouve pas que deux mouvements
simultanés s'annulent toujours. Nommer les référents et l'état final, puis
tester une seule variable après un rendu. Le mécanisme de pondération de `02b`
reste une hypothèse explicative, pas une mesure des poids du modèle.

## Repères proches et périphérie

Pour une translation, les repères proches peuvent produire plus de déplacement
apparent que les repères lointains. Localement et près de l'axe,
la vitesse angulaire est de l'ordre de `vitesse transversale / profondeur`.
Elle dépend du trajet et de la profondeur, pas de la focale seule. À géométrie
identique, une courte focale n'accélère pas le mouvement angulaire ; elle peut
permettre une caméra plus proche, ce qui change alors la géométrie.

Prendre des repères **déjà présents ou déclarés comme choix**. Pour ceux qui
portent la vitesse, nommer bord d'entrée, trajet et sortie. Ne pas ajouter un
objet à chaque bord par obligation. Dans une translation latérale ordinaire,
les lignes de terrain proches défilent plus vite que les tribunes éloignées.

Laisser des zones lisibles autour du sujet peut aider une poursuite. Une
occupation de la moitié de la largeur n'est pas un plafond : un gros plan peut
porter l'intensité par ses vibrations, ses contacts ou un autre repère.
La composition imposée par l'utilisateur demeure prioritaire.

| Vague | Plus précis, si ces éléments appartiennent au brief |
|---|---|
| `The car speeds down the road.` | `Painted lane dashes grow out of the distance and leave the bottom edge; the far treeline barely shifts. The coupe holds its size in the moving camera's frame.` |
| `The background rushes past.` | `The near guardrail posts cross screen-right to screen-left more quickly than the distant buildings; the camera tracks laterally alongside the car.` |

## Ratio et champ disponible

Hypothèse rectilinéaire de `01`, section Le ratio vertical. À hauteur de 36 mm,
une rotation donne 24 mm de largeur (2:3) ; un vrai 9:16 donne 20,25 mm.
Ne pas confondre pertes d'angle et pertes de largeur linéaire.

| Focale | Largeur utile 36 mm | Rotation, 24 mm (2:3) | Recadrage, 20,25 mm (9:16) |
|---|---|---|---|
| 14 mm | 104,3° | 81,2° | 71,7° |
| 18 mm | 90,0° | 67,4° | 58,7° |
| 24 mm | 73,7° | 53,1° | 45,7° |

Angles calculés avec `2 × atan(largeur utile / (2 × focale))`.
À distance et focale identiques, passer de 36 à 20,25 mm utiles réduit la
largeur de champ de 43,75 %. Cela ne rend pas une poursuite verticale impossible.
Adapter les repères au cadre et vérifier les marges plutôt que changer l'angle.

Dans une caméra **avançant et regardant vers l'avant**, les marques au sol
s'approchent et sortent par le bas, un portique franchi au-dessus par le haut.
En regardant vers l'arrière depuis une caméra qui s'en éloigne, les repères
convergent vers le lointain. Vérifier le trajet réel : « vertical » ne signifie
pas automatiquement une traversée de haut en bas.

## Repères lointains

Pour une approche sur l'axe à focale fixe, un repère de taille constante à
distance D grossit d'un facteur `D / (D − d)` après une avancée d, avec d < D.
À 100 km/h pendant 8 s, d ≈ 222,2 m :

| Distance initiale | Grossissement calculé |
|---|---|
| 300 m | ×3,86 |
| 600 m | ×1,59 |
| 1 000 m | ×1,29 |
| 1 500 m | ×1,17 |

Un changement de ×1,17 peut être perceptible : cela dépend de la taille initiale,
du contraste, de l'écran et du mouvement environnant. Le seuil ×1,3 employé
dans la session n'est pas une loi de perception. Si l'on choisit ce seuil comme
objectif de travail, `D ≤ (1,3 / 0,3) × d`, soit environ 963 m dans cet exemple.
Un repère au-delà ne devient pas immobile ; il porte simplement un changement
plus faible. Ne pas interdire son grossissement ni annoncer son invisibilité.

## Le plan nerveux : départ et caméra

Pour une attaque immédiate demandée, placer caméra et sujet dès la première
image et commencer l'action sans entrée héroïque ajoutée. Une entrée, une mise
en place ou une attente expressément demandée garde son temps. Le premier
événement avant une seconde est un choix de rythme, pas une règle générale.

« Nerveux » peut désigner trois choses distinctes :

- **Texture caméra** : petites corrections, vibration ou pas de l'opérateur.
  Les décrire par cause et amplitude lisible. Une cadence écrite est une
  direction donnée au moteur, pas une fréquence qu'il garantit.
- **Trajet** : un mouvement principal, avec ses états initial et final.
  Une vibration peut se superposer ; elle ne remplace pas le trajet.
- **Densité** : changements utiles et conséquences lisibles, sans quota imposé.

| Faible | Fort |
|---|---|
| `nervous handheld shot, fast and gritty` | `Handheld: the frame drifts and corrects continuously, about a degree of tilt and a few centimetres of travel at a time, at the pace of an operator walking behind her; it never reframes her, she stays in the left third throughout.` |
| `shaky cam` | `Shoulder-rig texture: a small constant vertical bounce on the operator's steps, one per half second, and a short correction to the right each time she changes direction.` |

Les amplitudes chiffrées de ces deux exemples servent à interdire le geste
lissé, pas à promettre une fréquence tenue : hypothèse de rédaction.

Relire la queue de contraintes selon `12`. Retirer `no handheld shake` si
la caméra portée est voulue. Un support fixe reste compatible avec une texture
de vibration demandée : préciser ce qui reste fixe et ce qui vibre, sans
effacer tous les mots « stable » indépendamment de leur objet.

## Exemple de poursuite

Exemple illustratif de 8 s, quatre changements, avec voitures, glissières et
portique déjà prévus au brief. Le rythme ne s'impose pas aux autres scènes.

```text
8-second single continuous take, 9:16 vertical, natural real-time speed.

The dark coupe and a slower saloon travel forward on the same straight road
in France, with right-hand traffic. Both start in the right lane; the left
overtaking lane is empty. The saloon holds its lane throughout.

Opening: a chase camera is behind both cars, one metre above the road, looking
forward and level. The entire coupe is centered, with space beside both ends
of its rear silhouette; the smaller saloon is visible ahead in the same lane, its rear silhouette centered on the coupe's.
Their rear faces and red tail lights are visible. Wet asphalt occupies the
lower third; the glancing light stays constant.

0-2s: the nearby guardrail posts approach along the right edge and leave frame
as the rig advances. The coupe keeps its lane and its distance from the camera.
2-4s: the coupe moves left into the empty overtaking lane and draws alongside
the slower saloon. The chase vehicle follows the coupe into that lane while
keeping its distance from it. The saloon stays in the right lane.
4-6s: the coupe pulls ahead of the saloon. The chase vehicle briefly travels
faster than the coupe and closes its gap, so the coupe grows in frame while
remaining entirely visible. The saloon moves toward the lower-right edge as
the camera also passes it; it leaves frame to the right.
6-8s: the chase vehicle matches the coupe's speed again at the shorter gap.
An overhead gantry grows near the top of frame and passes out above it.

Camera: mounted on the chase vehicle, at the same height and facing forward
throughout, fixed focal length. The rig changes lane and closes the gap only
as timed above; it does not orbit or zoom. Keep the coupe entirely in frame,
including at the closest camera position.
Audio: engine note and tyre roar on wet asphalt.
No cuts, no slow motion, no subtitles, no music.
```

Le rapprochement caméra–coupé de 4 à 6 s est explicite. Il ne coexiste pas avec
une clause de distance constante sur cette même paire. Le trafic est traité
selon les seuls champs applicables de `01b`, patron 19 de `08`.

## Checklist

- [ ] Le rythme demandé prime ; aucune nouvelle action n'a été ajoutée pour un quota.
- [ ] Chaque beat a un changement principal ou une tenue intentionnelle justifiée.
- [ ] Chaque distance et variation d'échelle nomme ses deux référents.
- [ ] Cadres de début et de fin compatibles avec trajet, angle et focale.
- [ ] Repères proches/lointains et sens de traversée physiquement cohérents.
- [ ] Le calcul de champ emploie le ratio livré, pas seulement un capteur tourné.
- [ ] Le brief décide de l'échelle du sujet, du temps d'entrée et de la stabilité.
- [ ] Observations, hypothèses perceptives et géométrie ne sont pas présentées
      comme des limitations mesurées de Seedance.
