# 02a Diriger le jeu

C'est ce qui sépare un plan qui bouge d'un plan qui se regarde. Le modèle joue
ce qu'on lui décrit comme **observable**. Un adjectif d'émotion produit une
moyenne d'expression, jamais une intention. Le guide ModelArk 2.5 le dit à sa
manière : pour les expressions, des phrases descriptives plutôt que des
locutions figées ; « mange avec appétit » s'écrit « un sourire satisfait, de
grandes bouchées ».

Et le jeu n'est pas dans la réplique. Il est dans ce qui se passe **avant qu'elle
sorte**, dans ce qui reste **après qu'elle est tombée**, et dans ce que fait
celui qui n'a rien à dire.

---

## Sommaire

- Accorder le jeu au cadre
- Les silences : une pensée visible, la partition d'un silence, les trois
  temps, fermer les bouches, durée
- Les yeux sont le canal
- Intention et obstacle
- La direction partagée
- De la tactique aux verbes
- Le changement
- Le registre
- Les ressources, par rendement
- L'écoute et la carte des regards
- Anti-patterns
- Gabarits
- Lien avec l'ancrage

---

## Accorder le jeu au cadre

Choisir le canal que le cadre permet réellement de percevoir. Les règles de
regard ci-dessous s'appliquent quand les yeux sont visibles. Visage masqué,
de dos ou hors champ : porter l'intention et son changement par une réponse
corporelle dans le cadre, ou par la voix et le souffle si l'audio les prévoit.
En POV humain, le regard se traduit par l'orientation de la caméra, `15`.
Ne pas ajouter un gros plan, montrer un visage, faire parler ou introduire un
accessoire pour satisfaire une grille de jeu. Le self-eval cite le canal
effectivement visible ou audible, sans exiger un second canal inaccessible.

## Les silences

Le beat le plus rentable d'un clip court. Trois secondes de silence habité valent
mieux que deux répliques empilées.

### Un silence est une pensée visible

« Elle ne dit rien » est du vide, et le modèle remplit le vide avec un geste
générique, souvent un sourire ou un hochement. L'inverse est aussi faux :
« elle reste immobile, aucun changement d'expression » n'est pas un silence,
c'est une pose, et le modèle la rend comme un mannequin. C'est le robot constaté
en production sur les silences demandés.

Ce qu'un acteur joue pendant un silence, c'est une **tâche intérieure** :
décider, mesurer, retenir, se souvenir, chercher la suite. La caméra la lit dans
les yeux quand ils sont visibles, sinon le canal retenu selon la section
ci-dessus. Un silence se dirige donc en trois lignes :

1. **la tâche**, nommée comme telle : `he is deciding whether to answer`,
   `she is working out how much he knows` ;
2. **le canal qui la porte** : avec les yeux visibles, une trajectoire de
   regard, deux ou trois cibles à hauteur d'yeux, ordonnées dans le temps ;
3. **un micro-événement** qui marque où la pensée bascule : une déglutition, les
   lèvres qui se pressent, un seul clignement lent, une inspiration qui
   s'arrête.

Puis la bouche fermée et les mains posées. La tâche fait travailler les yeux, la
trajectoire les rend visibles, le micro-événement empêche l'immobilité.

| Vide | Habité |
|---|---|
| `she stays silent` | `she is deciding whether to believe him; her eyes hold his left eye, drop to his mouth on his last word, and come back up; one slow breath, lips pressed together` |
| `he waits` | `he holds the door handle without turning it, weight still on his back foot, eyes on the corridor beyond her` |
| `she is uncomfortable` | `she looks past him at the window, then to his collar, then back to the window; she swallows once` |
| `he holds still, no expression change` | `he is working out how much she knows; his eyes go from her left eye to her right and back, one slow blink on her last word, jaw set` |

### La partition d'un silence

Au delà de trois secondes, une tâche et une trajectoire ne suffisent plus : le
modèle les rend une fois, puis tient la pose, et le personnage se vide. C'est le
mode de défaillance le plus constaté sur les silences longs : un visage propre,
des yeux ouverts, et rien ne s'y passe. La cause est la même que pour une
réaction sans cause dans `01b-motion-physics.md` : **un silence sans stimulus
est une pose, parce que le modèle n'a rien à quoi réagir.**

Un silence long s'écrit donc comme une **partition**, en beats de 1,5 à 3 s,
et chaque beat porte quatre choses :

1. **un stimulus**, ce qui déclenche le beat : extérieur, un son hors champ, un
   mouvement dans le décor, un objet qui entre dans le regard ; ou intérieur,
   un souvenir déclenché par un objet qu'il touche ou qu'il voit ;
2. **une ligne intérieure**, ce qu'il pense à ce moment, écrite en forme
   indirecte, `he is realising that she already knew`, et **jamais entre
   guillemets** : une phrase entre guillemets est une réplique, et le modèle la
   fait prononcer ;
3. **la réponse visible**, dans cet ordre de rendement : les yeux, le souffle,
   les mains ou l'objet, le corps, le visage en dernier ;
4. **un état de sortie** différent de l'état d'entrée, sinon le beat n'a pas
   eu lieu.

**L'activité.** Ce qui remplit un silence sur un plateau, c'est ce que le
personnage fait de ses mains pour une raison précise : retourner un téléphone
sans le déverrouiller, lever une tasse et la reposer sans boire, tordre une
alliance, plier et déplier une lettre. Meisner l'appelle l'activité
indépendante : une chose simple, spécifique et personnelle, faite parce qu'une
circonstance y oblige, et assez difficile pour pouvoir échouer. Uta Hagen fait
répéter seul, dans une pièce, deux minutes de vie avec des objets. Dans un
prompt, l'activité se nomme avec son objet, sa raison et son issue, réussie ou
manquée. Elle donne aux mains un travail sans les agiter, et au silence ses
événements. Les mains posées et immobiles restent justes pour celui qui
écoute ou qui se retient ; elles ne sont pas le défaut d'un personnage seul.

**Arbitrage pour un silence sans activité d'objet prévue.** L'activité avec
un objet reste une possibilité, pas une obligation d'ajouter une manipulation.
Si le brief porte déjà une action suffisante, vérifier une entrée vide,
chercher un visage, retenir une réponse, garder cette action avec sa raison,
son stimulus et son issue observable. L'absence qui se confirme peut être ce
stimulus ; les regards et la réponse corporelle en rendent l'issue visible.
Ne pas inventer un accessoire ou une activité de mains pour satisfaire la grille.
Cette alternative précise la règle d'activité pour les cas de `02c` ; son
efficacité sur Seedance reste une hypothèse de prompting, pas un résultat vidéo.

| Faible | Fort |
|---|---|
| `0-6 seconds: she sits alone at the kitchen table in silence, sad, waiting for a call that does not come. Her hands rest on the table. No expression change.` | `0-2 seconds: she is checking whether the phone is still on; she turns it face up, the screen lights her face for a second, no notification, and she turns it face down again. 2-4 seconds: a car passes outside, headlights sweep the wall; her eyes go to the window at eye level and stay there while the sound fades; she is deciding it was not him; one slow breath out. 4-6 seconds: her eyes come back to the phone, her hand moves toward it and stops short, fingers resting on the table beside it; her jaw sets, and her eyes go back up to the window. Ends with the phone face down, her hand beside it, eyes on the window.` |

La colonne forte n'écrit pas « triste » : elle écrit trois stimuli, trois
lignes intérieures en forme indirecte, une activité qui échoue deux fois, et
la tristesse est ce que le spectateur en déduit. C'est l'application de la
règle dure 5 à un silence, et c'est ce qui le rend regardable.

Le prix : une partition coûte des mots, de l'ordre de cinquante par beat. On
les prend sur le décor, la redescription du personnage et la queue, jamais sur
les beats ; un silence de dix secondes en partition dépasse la fourchette de
`SKILL.md` et c'est assumé, parce que la direction de jeu est la première
clause à disparaître quand le prompt est long, mécanisme 5 de
`02b-perform-failures.md`, donc c'est elle qui garde ses mots.

### Les trois temps d'une réplique

Chaque réplique se découpe en trois fenêtres. En sauter une fait tomber la ligne
à froid.

```
PRÉPARATION   ce qui se passe pendant qu'il décide de parler
RÉPLIQUE      la ligne, avec son débit
ATTERRISSAGE  ce que la ligne fait à celui qui l'entend, ou à celui qui l'a dite
```

> 0-2 seconds: she is deciding whether to ask; her eyes rest on the door behind
> him, one slow breath, mouth closed. 2-6 seconds: her eyes come to his and she
> says in calm conversational French: "Tu savais depuis quand ?" 6-8 seconds:
> her eyes drop to his hands, escape to the window for a second, and come back
> to his face; her jaw sets and she does not move.

L'atterrissage est celui qu'on coupe en premier quand on manque de secondes.
C'est une erreur : c'est là que la scène existe.

### Fermer les bouches

Pendant un silence, le dire. Sans ça, le modèle produit du marmonnement ou
invente une réplique.

```
Her mouth stays closed and still during the silence.
Her mouth moves only during her own line.
He does not speak at any point.
```

### Durée

En dessous d'une seconde, un silence ne se lit pas. Jusqu'à trois secondes,
une tâche, une trajectoire de regard et un micro-événement le tiennent. Au
delà, il devient une partition, section ci-dessus, sinon le modèle comble ou
fige.

---

## Les yeux sont le canal

À l'image, l'émotion se lit dans les yeux avant tout le reste. Un regard baissé
les cache : le modèle rend alors un visage fermé, et rien de ce qui a été écrit
pour le jeu ne se voit. La cible d'un regard est donc **à hauteur d'yeux par
défaut** : le visage du partenaire, un point au-delà de son épaule, la porte, la
fenêtre, l'objectif si le plan s'y adresse.

Regarder le sol, la table ou ses mains n'est pas interdit. C'est un **choix** qui
porte un sens, honte, évitement, ou un objet manipulé, et il s'écrit comme un
choix : demandé par le brief, court, et suivi de son **retour** vers une cible à
hauteur d'yeux. `Her eyes drop to his hands, escape to the door for a second,
and come back to his face` est une trajectoire ; `eyes down` tenu trois secondes
est un visage absent.

Trois leviers du regard que la caméra lit, d'après Michael Caine, masterclass BBC
« Acting in Film », 1987 :

- **Ne pas cligner** pendant une ligne donne de la force au personnage ; cligner
  souvent le rend faible ou troublé. Le clignement est un réglage :
  `she does not blink during her line` pour la fermeté, `one slow blink on his
  last word` pour marquer un temps, cadence naturelle sinon.
- **Tenir un seul œil** du partenaire lit comme de l'assurance ; passer d'un œil
  à l'autre lit comme du trouble. Le verbe « vérifier les deux yeux de l'autre »
  du répertoire plus bas décrit donc un personnage qui cherche, pas un
  personnage qui tient. Choisir selon la tactique.
- **La caméra lit la pensée**, pas l'expression. Judith Weston le formule ainsi :
  pour que les pensées des personnages soient transparentes à la caméra, l'acteur
  doit être dans l'instant. Un visage qui pense sans rien montrer est plus
  vivant qu'un visage qui montre sans penser.

Sources : Michael Caine, masterclass BBC 1987, rapportée par Dominic Smithers,
LADbible, 26 décembre 2022, et par E. M. Taboada, No Film School, 31 mars 2012.
Judith Weston, « Directing Actors », 1996, et sa page « Top 10 ideas », non
datée ; « les acteurs ne peuvent pas jouer des adjectifs, il leur faut des
verbes », rapporté par Peter D. Marshall, Raindance, 6 mars 2013. Activité
indépendante de Meisner : Charlie Sandlan, Maggie Flanigan Studio, 26 mai 2022,
mis à jour 3 février 2025, « simple, specific, and personal », « a very
personal previous circumstance that compels you to do what you're doing now ».
Exercices d'objets d'Uta Hagen, « Respect for Acting », 1973, pages 81 à 90.
Ce sont des règles de plateau constatées sur des acteurs ; leur transfert à
Seedance est une hypothèse de travail, cohérente avec le mécanisme 3 de
`02b-perform-failures.md` et avec le robot constaté sur les silences écrits en
immobilité.

---

## Intention et obstacle

Le vocabulaire du plateau marche parce qu'il produit du comportement. Un
personnage **veut** quelque chose, et quelque chose l'en **empêche**. Le jeu est
la trace visible de ce conflit.

Traduire, toujours :

| Intention et obstacle | Ce qui se voit |
|---|---|
| Elle veut partir mais elle reste | La main sur la poignée, le corps immobile, aucun pas |
| Il veut avouer mais il n'ose pas | Il ouvre la bouche, la referme, détourne les yeux vers la fenêtre, revient sur elle, recommence |
| Elle veut l'aider sans le vexer | Elle avance la main vers l'outil, s'arrête à dix centimètres, la retire |

C'est aussi la parade contre la biographie invisible. « Elle regrette d'avoir
quitté sa ville natale » n'est pas filmable. « Elle hésite devant l'ancien
panneau de gare, touche son bord rayé, puis repart sans se retourner » l'est.

---

## La direction partagée

Dès qu'il y a plusieurs personnages, l'intention et l'obstacle de chacun ne
suffisent pas : trois personnages dirigés séparément produisent trois plans qui
cohabitent dans le même cadre. Ce qui les relie est un niveau au-dessus.

Nommer, avant les tactiques individuelles, **l'unique événement que tous
traversent**, puis le canal physique par lequel chacun le traverse. L'événement
est le même pour tout le monde et n'est jamais dit ; le canal est propre à chacun
et c'est lui qui s'écrit dans le prompt.

```
DIRECTION PARTAGÉE (non dite) : la recherche du pardon de soi.
  A la revit, il la rejoue devant eux.
  B se réfugie dans une procédure sans faille.
  C soigne le patient au delà de la fiche.
```

La surface, ici une visite de routine, n'est que le terrain que l'événement
traverse. C'est ce qui fait qu'une réplique anodine, « le pauvre, il n'arrive pas
à se pardonner », désigne les trois hommes à la fois sans que personne ne le
sache.

**Le test qui dit si l'événement est bien nommé : il doit contenir tous les
personnages présents, y compris ceux qui se taisent et celui qui est
inconscient.** Si l'un d'eux reste dehors, l'événement est mal nommé, et le plan
se paiera par un personnage qui n'a rien à jouer. C'est aussi le meilleur
diagnostic quand un figurant ou un troisième rôle fige : ce n'est pas un défaut
de prompt, c'est qu'il n'a pas été inclus dans l'événement.

Effet pratique sur le prompt : la direction partagée ne s'écrit pas, elle décide
les verbes. Elle est ce qui empêche d'attribuer à chaque personnage un
comportement générique quand on manque d'idées, et elle donne à celui qui ne
parle pas une raison interne d'écouter comme il écoute.

L'analyse qui produit cet événement, les motifs et les buts individuels relève de
l'écriture, pas du prompt. Ici on n'en garde que la sortie : un canal physique
par personnage, et les verbes qui en découlent.

---

## De la tactique aux verbes

La tactique est ce que le personnage **fait à son partenaire**, et elle s'écrit
en verbes adressés, avec le travail du regard nommé comme action. Pas en
adverbes, pas en chorégraphie de visage.

Répertoire de verbes de regard qui portent, parce qu'ils décrivent une opération
mentale visible :

```
vérifier les deux yeux de l'autre  |  enregistrer si le point est passé
voler un regard et le reprendre avant d'être vu  |  mesurer
comparer ce qu'il ressent à ce que l'autre montre  |  guetter le moment de parler
```

**La tactique s'attache aux mots de la réplique**, pas au plan en général. Une
ligne, un verbe, ce que les yeux vérifient pendant qu'elle sort. Et quand le
carburant du personnage s'épuise, marquer l'endroit exact où la ligne casse :
c'est souvent là que la scène a lieu.

```
préparation      "..."                → [verbe adressé] + [ce que les yeux vérifient]
réplique 1       "[mots exacts]"      → [verbe] + [regard]
réplique 2       "[mots exacts]"      → [verbe] + [regard]
rupture          "[mots exacts]"      → le carburant lâche, la ligne tombe autrement
```

**Où ce travail atterrit dans le prompt.** Pas dans un bloc de direction séparé.
Le mécanisme 1 de `02b-perform-failures.md` est formel sur ce point : pendant la
parole, la synchronisation labiale accapare le visage, et une direction de jeu
posée ailleurs dans le prompt n'est plus active à ce moment. Le tableau ci-dessus
est un **document de préparation** dont on extrait les verbes pour les écrire
**dans la clause de dialogue elle-même**.

| Faible | Fort |
|---|---|
| Un bloc de direction en fin de prompt, puis `He says: "I was not there."` | `He says, checking both of her eyes for a flicker of belief and finding none: "I was not there."` |

Si une surface se comporte autrement et tient un bloc séparé, c'est une
observation qui prime sur cette règle : la noter et la garder.

---

## Le changement

Pour affiner un jeu retenu ou corriger un seul passage, lire
[02c-fine-performance.md](02c-fine-performance.md) : reprise de contrôle,
trace finale, densité adaptée au cadre et périmètre de révision.

Un plan de jeu réussi montre un avant et un après. Nommer l'**état d'entrée** et
l'**état de sortie du personnage**, pas seulement des objets. C'est le report
d'état appliqué à l'intérieur.

```
Entrée: fermé, bras croisés, regard qui fuit.
Sortie: bras décroisés, une main à plat sur la table, regard soutenu.
```

Sans changement nommé, le modèle tient une expression constante pendant toute la
durée et le plan n'a pas de dramaturgie.

Forme longue, pour un basculement unique :

```
The emotion shifts from [départ] to [arrivée].
After [déclencheur], [sujet] first shows [réaction immédiate observable].
Then, [yeux, sourcils, bouche, respiration, regard, mains] gradually [change].
Finally, [sujet] expresses [émotion cible] through [comportement extérieur].
```

Pour plusieurs basculements, les chaîner aux **événements** plutôt qu'aux
secondes : chaque nouvelle chose que le personnage voit ou entend fait avancer le
jeu d'un cran. Plus robuste qu'une liste de timestamps émotionnels.

---

## Le registre

Le défaut du modèle est le jeu appuyé : expression pleine, sourcils actifs,
sourire de sécurité. Si on veut de la retenue, il faut la demander.

| Registre | Formulation |
|---|---|
| Contenu | `minimal expression change, she does not perform the emotion` |
| Retenu | `the change reads only in the eyes and the breathing` |
| Ordinaire | `natural everyday behavior, no acting` |
| Appuyé | `a full open reaction` |

Deux interdits utiles quand ils ne sont pas voulus :

```
No default smile. No nodding.
```

« Minimal » veut dire petit, pas nul. Un registre contenu garde la tâche
intérieure et la trajectoire de regard ; ce qui se réduit, c'est l'amplitude du
visage, jamais l'activité des yeux. Sans cette distinction, le registre contenu
redevient la pose.

---

## Les ressources, par rendement

**Le regard.** La moins chère et la plus efficace. Où il regarde, quand ça
change, s'il soutient ou s'il lâche. Un changement de regard vaut une réplique.

> Her eyes go from his hands to his face on the word "quand", then to the door
> and back.

Deux pièges le neutralisent, la négation et la cible unique tenue. Détail au
mécanisme 3 de `02b-perform-failures.md`.

Le regard n'est pas un ornement du jeu, c'est le jeu : **ce qui rend un visage
vivant, c'est un esprit visiblement occupé à une tâche.** Un personnage qui
argumente vérifie les deux yeux de son partenaire, cherche une lueur d'adhésion,
enregistre après chaque point si ça a pris, et ajuste à ce qu'il trouve. Ce
mouvement d'yeux **est** l'action.

Corollaire : **un regard mort ne se répare jamais par la lumière.** Poser un
catchlight sur un œil qui n'a rien à faire donne un œil mort brillant. On lui
donne une tâche.

**Une ligne de sécurité, une seule.** Le modèle produit spontanément le regard
fixe, sans objet, et des visages qui ne clignent pas de tout le plan. Cette
pathologie est propre à la génération, elle n'a pas d'équivalent sur un plateau,
donc elle se traite par une clause explicite et courte, en clôture du bloc de
jeu, et **en positif seulement** : nommer le regard vitreux pour l'interdire le
dessine, comme tout artefact visuel nommé en négation, `12-constraints.md`. La
première version de cette ligne le nommait ; elle a été réécrite.

```
His eyes keep working at the task, moving between the targets named above,
with a natural blink cadence throughout.
```

Une fois par prompt, pas une fois par personnage. Répétée, elle devient du bruit
et retombe sous le principe de pondération de `02b-perform-failures.md`. C'est la
seule direction de jeu qui s'écrit en externe plutôt qu'en tâche, et elle est
tolérée parce qu'elle corrige un défaut de modèle, pas un défaut d'écriture.

**La respiration.** Audible et visible. Une inspiration avant de parler, une
expiration après. C'est ce qui rend vivant.

**Le corps avant le visage.** Poids, appuis, orientation des épaules, distance à
l'autre. Un demi pas en arrière dit plus qu'un froncement de sourcils, et le
modèle le rend mieux.

**Les mains.** Elles ont une activité ou une position de repos écrite, selon
La partition d'un silence et son arbitrage sans objet. Dire ce qu'elles font
si elles sont visibles, sans inventer une manipulation pour un personnage seul
dont l'action est déjà portée par le regard et le corps.

> Both hands rest flat on the table and do not move.

**Le visage en dernier.** Deux à quatre indices suffisent : yeux, sourcils,
bouche, mâchoire. Lister tout le visage sature le beat sans rien gagner.

---

## L'écoute

La moitié du jeu appartient à celui qui ne parle pas. Non nommé, le modèle le met
en pause : il fige, ou il hoche la tête en boucle.

Nommer, pour chaque personnage présent, ce qu'il fait **pendant** la réplique de
l'autre.

> While she speaks, he keeps his hands on the table, his eyes on hers, and his
> jaw tightens once on the last word. He does not nod and does not speak.

Trois écoutes différentes, trois scènes différentes : celui qui soutient le
regard, celui qui le fuit, celui qui regarde ailleurs et revient trop tard.

**L'écoute est une tâche, pas un comportement.** Nommer le comportement seul
donne une pose tenue ; nommer ce que celui qui écoute cherche à obtenir donne des
yeux qui travaillent. « Décider s'il est sérieux », « attendre la chute »,
« protéger l'ambiance », « vérifier si l'autre a compris avant lui » sont des
tâches. Le comportement en découle et n'a plus besoin d'être choréographié.

| Faible | Fort |
|---|---|
| `He listens, hands on the table, nodding occasionally.` | `He is deciding whether the other man is serious; his eyes check both of his, and he keeps his hands flat on the table while he decides.` |

Et pour la figuration, la réaction chorale est le mode de défaillance par
défaut : `nearby diners turn toward the sound at slightly different delays`.

### La carte des regards

Sur une scène couverte en plusieurs générations, l'écoute ne suffit plus : il
faut que les regards se croisent d'un plan à l'autre. Écrire dans chaque prompt,
en **direction d'écran** et pas en « à sa gauche », qui regarde vers quoi.

```
Eyelines: <A> looks screen-left toward <C> on the couch; <B> looks screen-right
toward <A>. <D> is seen from behind and faces away from camera.
```

C'est ce qui tient l'axe entre deux générations qui ne se connaissent pas. Un
personnage hors champ se déclare quand même, sinon celui qui reste dans le cadre
regarde dans le vide : `<C> is off-screen for this shot, heard only; <A> keeps
his eyes toward screen-left where <C> sits.`

Quand la scène a plus de deux personnages, la carte de regards écrite atteint sa
limite et devient une géométrie à fournir plutôt qu'à décrire : `11-diagram.md`.

---

## Anti-patterns

- **L'adjectif d'émotion seul.** « triste », « en colère », « surpris » donnent
  une moyenne d'expression.
- **La biographie invisible.** Ce qui n'est pas dans le cadre n'existe pas.
- **Deux émotions dans la même fenêtre.** Un basculement par beat.
- **La réaction avant sa cause.** Voir `01b-motion-physics.md`, cause avant réaction.
- **Parler et agir en même temps** dans le même beat. Une chose à la fois : elle
  parle, puis elle tourne le couvercle, puis elle repose la tasse.
- **Le dialogue long.** Une ou deux répliques par clip. Au delà, la synchro
  labiale, le timbre et l'attribution décrochent ensemble.
- **Oublier de fermer les bouches.**
- **Le silence joué en pose.** « Immobile, aucun changement d'expression » donne
  un mannequin. Un silence a une tâche, une trajectoire de regard et un
  micro-événement ; au delà de trois secondes, une partition avec des stimuli
  et une activité.
- **La ligne intérieure entre guillemets.** Elle devient une réplique, et le
  modèle la fait prononcer. Toujours en forme indirecte.
- **Le regard baissé par défaut.** Il cache le seul canal qui porte l'émotion.
  Cible à hauteur d'yeux, sauf choix demandé, et toujours avec son retour.

---

## Gabarits

### Silence habité, 3 s

> 0-3 seconds: [sujet] is [tâche intérieure : deciding whether to / working out
> how / holding back what]; eyes on [cible 1 à hauteur d'yeux], then to [cible
> 2] on [événement ou seconde], and back to [cible 1]; one slow breath;
> [micro-événement : a swallow / lips pressed together / one slow blink]. Both
> hands rest where they were. Mouth closed and still. Ends [état de sortie :
> jaw set / shoulders dropped].

### Silence en partition, 6 s, personnage seul

> 0-2 seconds: [sujet] is [ligne intérieure 1, forme indirecte]; [activité :
> objet, geste, issue], eyes on [cible 1 à hauteur d'yeux]. 2-4 seconds:
> [stimulus : son hors champ, mouvement, objet aperçu]; [sujet] is [ligne
> intérieure 2]; eyes go to [cible 2] and stay there while [le stimulus
> s'éteint]; [souffle]. 4-6 seconds: eyes come back to [cible 1]; [activité
> reprise ou abandonnée : la main s'arrête, l'objet est reposé]; [micro-événement].
> Ends [état de sortie différent de l'entrée]. Mouth closed and still
> throughout.

### Réplique en trois temps, 8 s

> 0-2 seconds: [préparation observable], mouth closed. 2-5 seconds: [sujet] looks
> at [cible] and says in [langue et variété]: "[réplique]". 5-8 seconds:
> [atterrissage : ce que la ligne laisse]. Mouth moves only during the line.

### Réaction sans dialogue, 6 s

> 0-2 seconds: [sujet] is [état d'entrée observable]. 2-4 seconds: [déclencheur
> hors champ, son ou événement]; [réaction immédiate : un seul indice]. 4-6
> seconds: [changement progressif : trajectoire de regard à hauteur d'yeux,
> respiration, épaules]; ends [état de sortie]. Minimal expression change, no
> default smile, no nodding.

### Basculement d'intention, 10 s

> [SUJET] wants [INTENTION] but [OBSTACLE]. 0-4 seconds: [comportement de
> l'obstacle qui gagne]. 4-7 seconds: [déclencheur]; [premier signe que
> l'intention reprend]. 7-10 seconds: [l'intention l'emporte ou non, en un geste];
> ends [état de sortie]. The change reads only in the eyes and the breathing.

---

## Lien avec l'ancrage

Le **contrechamp de réaction** est précisément un cas où le modèle doit déduire
une géométrie qu'il n'a pas. Sur une scène de dialogue à deux, fournir l'image du
contrechamp plutôt que de la faire deviner, et vérifier direction de lumière et
axe sur les fixes. Voir `05-anchoring.md`.

---

Quand le prompt est bien formé, le rendu techniquement conforme et le jeu
inexploitable malgré tout : `02b-perform-failures.md`.
