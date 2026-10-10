# 02b Quand le jeu meurt

La fiche `02a-perform.md` dit comment écrire le jeu. Cette fiche traite du cas où
le prompt est bien formé, le rendu techniquement conforme, et le jeu
inexploitable malgré tout. Le rendu franchement raté relève de `09-diagnose.md`.

## Niveau de confiance

Sauf mention contraire dans le mécanisme, tout ce qui suit vient d'**une seule
session de production** sur Jimeng, une scène d'interrogatoire à trois
personnages, une quinzaine de générations. **Aucun de ces
mécanismes n'a été isolé par un test à variable unique.** Ce sont des hypothèses
de travail cohérentes avec les rendus observés, pas des constats reproduits.

Les traiter comme `07-spec.md` traite le constaté par rapport au publié : utiles
pour décider, insuffisants pour affirmer. Aucun seuil chiffré n'est donné ici,
parce qu'aucun n'a été mesuré.

## Le principe de pondération

**Le modèle pondère une clause par sa répétition et sa position, pas par la
hiérarchie qu'elle déclare.** Un bloc marqué ABSOLUTE PRIORITY placé au milieu
d'un prompt perd contre une clause anodine placée en tête. Écrire IMPORTANT,
CRITICAL ou MUST ne crée pas de priorité, ça crée du texte de plus.

Corollaire opérationnel, qui commande les huit mécanismes suivants : **ce qui
compte le plus s'écrit en premier, et une seule fois.**

## 1. Le dialogue mange le jeu

**Symptôme.** Le jeu est vivant pendant les silences et meurt dès qu'une réplique
démarre. Le visage cesse de jouer et devient un mécanisme d'articulation.

**Cause supposée.** La synchronisation labiale accapare le visage pendant la
durée de la parole. Une direction de jeu écrite dans un bloc séparé n'est plus
active à ce moment-là.

**Correctif.** Écrire le comportement **dans la clause de dialogue elle-même**,
pas dans un bloc de direction à part. Raccourcir la réplique. Surveiller le
rapport entre le temps parlé et le temps silencieux d'un plan : un plan où l'on
parle presque tout du long n'a pas de place pour jouer. Ce rapport se règle au
moment de découper les beats, pas après : compter 2 à 3 secondes par action
visible, section Les beats minutés de `03-sequence.md`.

| Faible | Fort |
|---|---|
| `The suspect is defensive and tense. He says: "I was not there."` | `He says, jaw tight and eyes on a point past the officer's shoulder, in a voice that barely carries: "I was not there."` |

## 2. La physiologie prescrite produit un visage inhumain

**Symptôme.** Écrire veines saillantes, nuque rouge, cordon du cou apparent donne
une exécution littérale et monstrueuse.

**Cause supposée.** Le modèle rend le symptôme comme un attribut d'apparence, au
même titre qu'une couleur de vêtement, et non comme la conséquence d'un état.

**Correctif.** Écrire ce que le personnage **veut** et l'**effort** qu'il
fournit, jamais le symptôme corporel. La physiologie est un résultat, pas une
consigne. Formule à retenir : un acteur à qui on prescrit un symptôme joue mal,
un modèle le fabrique.

| Faible | Fort |
|---|---|
| `Veins standing out on his neck, red flush up the nape, cords showing.` | `He tries to keep his voice level and does not manage it; the effort shows.` |

## 3. Le regard se dirige, il ne s'interdit pas, et il bouge

**Symptôme, deux erreurs symétriques.** Une négation, `does not look at him`, est
lue comme `look away` et produit un regard perdu, sans objet. Une cible unique
tenue pendant toute la durée du plan produit un regard fixe et robotique.

**Cause supposée.** Le modèle n'a pas de représentation du non-regard : il lui
faut une destination. Et une destination unique tenue longtemps n'a aucune raison
interne de varier.

**Correctif.** La direction est **toujours positive**, et elle est **multiple et
ordonnée dans le temps**. Écrire une trajectoire de regard, pas une cible.

| Faible | Fort |
|---|---|
| `She does not look at him.` | `Her eyes stay on the door behind him.` |
| `She holds his gaze for the whole shot.` | `Her eyes drop to his hands, escape to the door for a second, and come back to his face.` |

**Portée plus large que le regard.** Le même mécanisme vaut pour toute négation
qui nomme une chose que le modèle sait rendre : un artefact optique, un élément
de décor, un style graphique. Il n'a pas de représentation de leur absence, donc
le nom pèse et la négation s'efface. La règle générale et son test sont dans la
`12-constraints.md`.

## 4. Le ralenti fait d'un geste un climax

**Symptôme.** Une rampe de vitesse posée sur un geste anodin lui donne tout le
poids du plan, et déclenche des réactions parasites chez les autres personnages,
qui jouent l'événement que la rampe annonce.

**Cause supposée.** Le ralenti est lu comme un marqueur d'importance
dramatique, et le modèle rend la scène cohérente avec ce marqueur.

**Correctif.** Réserver la rampe à un plan dont ce geste **est** l'événement
principal. Jamais dans un plan dialogué. Voir aussi le traitement de la vitesse
dans `01b-motion-physics.md`.

| Faible | Fort |
|---|---|
| `He slides the photograph across in slow motion while she keeps talking.` | `He slides the photograph across at natural real-time speed while she keeps talking.` |

## 5. La longueur noie l'intention

**Symptôme.** Passé un certain volume, la clause la plus répétée l'emporte quel
que soit son statut déclaré, et **la direction de jeu est la première à
disparaître**, avant la caméra et avant le décor.

**Cause supposée.** Le principe de pondération posé plus haut, appliqué à
l'échelle du prompt entier.

**Correctif.** Se tenir à la fourchette de longueur donnée dans le SKILL.md. Si
le prompt doit grossir, la direction de jeu monte en tête plutôt que de rester au
milieu. Aucun seuil fiable n'a été mesuré ici.

| Faible | Fort |
|---|---|
| Trois paragraphes de décor, puis `IMPORTANT: he is barely holding it together` en fin de prompt | `He is barely holding it together.` en première ligne, puis le décor |

## 6. Toute prose qui double une référence la combat

Trois faces d'un même principe. La doctrine d'ancrage est dans `05-anchoring.md` ;
ce qui suit est ce que la session a fait apparaître côté jeu et mise en scène.

**Redécrire** ce qu'une référence montre déjà, physique d'un personnage ou décor,
crée une source concurrente et fait dériver le rendu. La lumière fait exception
par nécessité : la plaque la porte, mais elle ne survit pas à une coupe et un
plan serré ne voit plus sa source, donc elle s'écrit par plan comme son effet
sur ce qui est dans le cadre, section Lumière de `01-write-shot.md`.

**Contredire** une référence force un arbitrage silencieux et perd les deux. Cas
observé : une dalle fluorescente au plafond écrite dans le prompt, contre une
fenêtre à lamelles présente dans la planche décor. Le rendu n'a donné ni l'une ni
l'autre proprement.

**Omettre** est le troisième cas, symétrique et moins évident : tout élément de
mise en scène **absent des entrées visuelles** est inventé, donc instable d'une
génération à l'autre. Cas observé : une chaise isolée créée par le modèle, qui se
déplaçait à chaque relance. Un élément qui doit persister doit être dans l'image.

| Faible | Fort |
|---|---|
| `A fluorescent panel overhead, harsh light.` avec une planche décor à fenêtre à lamelles | `Light as in the set reference: from screen-left, on the left side of his face.` |
| `An empty chair sits apart from the table.` sans chaise dans la planche | La chaise est dans la planche décor, et la prose n'en parle pas |

## 7. Trois personnages qui parlent est déjà une scène à risque

**Symptôme.** Instabilité générale du jeu et des identités.

**Cause.** La stabilité des scènes à sujets multiples en interaction est une
faiblesse du modèle ; le guide ModelArk 2.5 en publie une version chiffrée,
la stabilité baisse au delà de cinq sujets portés par vidéo ou audio et de huit
portés par image, et l'attribution plus large à ByteDance vient du skill
d'origine, `07-spec.md`. Le dialogue s'y ajoute.

**Correctif.** Réduire l'ambition avant de relancer. **Sortir du cadre** les
personnages qui ne parlent pas, plutôt que de les maintenir en profondeur de
champ. Préférer plusieurs plans courts ancrés à un plan long peuplé, ce qui
renvoie au découpage de `05-anchoring.md`.

Quand ils doivent rester, la prose ne tient plus la disposition et il faut la
fournir comme géométrie : diagramme de mise en place, une figure colorée par
personnage, `11-diagram.md`.

| Faible | Fort |
|---|---|
| `Three people around the table, the two others watching in the background as he answers.` | `He answers alone in frame; the second officer is heard off screen and never seen.` |

## 8. Le silence écrit comme une pose produit un mannequin

**Symptôme.** Pendant un silence demandé, le visage se tient, les yeux restent
fixes ou baissés, et le personnage a l'air d'un robot. Le prompt est conforme :
bouche fermée, mains posées, aucune réplique.

**Cause supposée.** Le silence a été écrit comme une immobilité, « holds still,
no expression change », avec une cible de regard unique ou un regard baissé. Le
modèle n'a aucune tâche intérieure à rendre, donc il rend une pose tenue ; et un
regard baissé retire le seul canal par lequel une pensée se lirait. Cas voisin du
mécanisme 3, où une cible unique tenue produit le regard fixe.

**Correctif.** Appliquer [02a-perform.md](02a-perform.md), sections Accorder le
jeu au cadre et Les silences, puis La partition d'un silence au delà de trois
secondes, y compris son arbitrage sans activité d'objet prévue. Le diagnostic
ne crée ni accessoire ni canal de jeu absent du cadre pour remplir la grille.

| Faible | Fort |
|---|---|
| `0-3s: he holds still, eyes down on the table, no expression change, mouth closed.` | `0-3s: he is deciding whether to answer; his eyes hold her left eye, go to the door behind her on her last word, and come back; one slow breath, lips pressed together; mouth closed.` |

**Niveau de confiance.** Constaté sur plusieurs sessions de production, sur des
silences demandés explicitement. Non isolé par un test à variable unique,
cohérent avec le mécanisme 3.

## Checklist de jeu

Appliquer le périmètre de `02a`, Accorder le jeu au cadre, à tous les contrôles
de regard ci-dessous ; ils ne demandent pas de montrer un visage hors cadre.

- [ ] Le jeu est écrit avant la caméra dans le prompt.
- [ ] Aucun symptôme physiologique prescrit.
- [ ] Aucune négation de regard, chaque regard a une direction positive.
- [ ] Aucun regard verrouillé sur une cible unique pour toute la durée.
- [ ] Chaque silence porte une tâche intérieure et un changement perceptible
      dans le canal retenu selon `02a`, Accorder le jeu au cadre et Les silences.
- [ ] Aucun regard baissé qui ne soit demandé par le brief, et chacun a son
      retour vers une cible à hauteur d'yeux.
- [ ] Aucune rampe ralenti dans un plan dialogué.
- [ ] Rien de ce qu'une référence montre n'est redécrit ni contredit dans la prose.
- [ ] Aucun élément de mise en scène persistant n'est absent des entrées visuelles.
- [ ] S'il y a plus de deux personnages dans le cadre : la disposition est
      fournie comme géométrie, pas décrite en prose.
- [ ] Chaque regard est écrit en direction d'écran, y compris vers un personnage
      hors champ.
