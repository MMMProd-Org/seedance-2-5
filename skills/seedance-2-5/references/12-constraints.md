# 12 Contraintes

La queue terminale d'un prompt : la queue de négations, le verrou positif, et
l'arbitrage des conflits qui se fait juste avant.

Scindée de `01-write-shot.md`, qui avait atteint son plafond de lignes. Le
chapitre était déjà autonome et pointé depuis six fiches.

À ouvrir avec `01` dès qu'on écrit un prompt, et seule quand on ne débogue qu'une
clôture.

---

## Sommaire

- Par famille : structure temporelle, objets, identité et anatomie, texte et
  marque, audio, transferts de référence, physique
- Les négations qui invoquent
- Le verrou positif
- Arbitrage des conflits
- Ce qu'on ne met pas dans la queue

---

Une bonne queue de contraintes protège des **faits de production**. Elle ne liste
pas des plaintes génériques du type « pas d'anatomie ratée », « pas de basse
qualité », « pas de flou » : ces formules n'apportent rien au modèle et diluent
les négations qui, elles, sont utiles.

Règle de sélection : chaque négation doit correspondre à un échec **plausible sur
ce plan précis**. Un plan sans objet manipulé n'a pas besoin de « no duplicated
bottle ». Deux personnages sans bouteille n'en ont pas davantage besoin ;
choisir une contrainte sur le compte ou l'identité si ce risque existe.

Position : en fin de prompt, où la plupart des prompts publiés par ByteDance
les placent ; certains les mettent en tête, « Render Video 1. No BGM; generate
only environmental sounds and action sounds. », ou avant la liste des plans,
bloc `[Strictly exclude]`. Qu'elles soient lues plus fiablement en fin est une
observation, pas un fait documenté.

---

### Par famille

### Structure temporelle

```
No cuts, no jump cut, no slow motion, no speed ramp, no repeated action,
no repeated entrance, no looping. The camera does not zoom, does not push in.
```

Choisir dans cette liste les contraintes compatibles avec le plan. Un
plan-séquence peut avancer ou zoomer ; une durée longue peut inclure des coupes
ou un ralenti demandés. `natural real-time speed` s'applique aux seules plages
en vitesse réelle, sans interdire le traitement temporel voulu.

### Objets

```
No duplicated bottle or helmet, no object teleportation, no changing object
count, no extra fork, no disappearing luggage; the board stays on the concrete.
```

Toujours nommer l'objet concerné. « No duplicated objects » est trop vague pour
mordre. Compléter par la position finale de l'objet dans le corps du prompt.

### Identité et anatomie

```
No identity change, no clothing change, no color change, no morph,
no duplicated limbs, no extra hands, no extra characters.
```

Dérive d'identité et changement de costume sont les deux défaillances les plus
fréquentes sur les durées longues et les scènes à plusieurs sujets.

### Texte et marque

```
No text, no subtitles, no logo, no watermark, no invented branding,
no on-screen labels.
```

À utiliser lorsque ce texte n'est pas voulu. Préserver les inscriptions et
logos demandés ou présents sur un produit de référence : préférer « no added
on-screen text » à une interdiction de tout texte. Un texte exact à livrer
peut nécessiter la post-production, sans le supprimer silencieusement du brief.

### Audio

```
No music, no BGM, no narration, no random subtitles.
```

`only ambient and action sounds` est une **autre façon d'interdire la musique**,
plus serrée, pas une façon de l'obtenir. Et `no sound` pour le silence total.
Quand une nappe est voulue, toute la ligne ci-dessus sort du prompt et la
musique s'écrit avec sa courbe, `10-syntax.md`.

### Transferts de référence

La famille la plus oubliée. Quand une référence apporte un seul attribut, il faut
nommer ce qu'elle ne doit **pas** apporter.

```
Do not copy @image1's studio background.
Do not copy the skater, skateboard, cone, clothing, beach, or concrete setting
from @video1.
Do not use the people in the image.
```

Sans ces lignes, l'arrière-plan, les figurants et la composition d'une référence
voyagent avec le sujet.

### Physique

```
Syrup does not flow uphill; the liquid stays on the plate.
No person or suitcase appears on both sides of the column at once.
No impossible handoff.
```

Ces négations sont spécifiques au plan et se dérivent directement de ce qui vient
d'être décrit dans les beats. Voir
`01b-motion-physics.md`.

---

### Les négations qui invoquent

Toutes les négations ne se valent pas, et certaines produisent exactement ce
qu'elles interdisent. Le partage se fait sur **ce que la négation nomme**.

| Ce que la négation nomme | Effet | Forme à employer |
|---|---|---|
| Un **processus** ou une **structure temporelle** **non voulu** : coupe, ralenti, boucle, répétition, téléportation, changement d'identité, sous-titre, musique, mouvement caméra, zoom, push in, pan | Elle mord. C'est la forme employée par les prompts publiés | La garder en négation, **seulement si** l'effet n'est pas demandé et que la panne est plausible sur ce plan |
| Un **artefact visuel dessinable** : lens flare, traînée lumineuse, bille de bokeh flottante, halo, vignette, grain, style graphique | Elle invoque. Le nom est une chose que le modèle sait rendre, et l'écrire augmente sa présence dans le cadre | La remplacer par la description positive de l'état propre |

Le test : **un compte, une possession, une structure temporelle, un texte à
l'écran, un son se gardent en négation ; un aspect optique, un état visuel, un
style graphique, une expression de visage se réécrivent en positif.** « no slow motion » décrit un comportement temporel,
« no extra hands » un compte, il n'y a rien à dessiner ; « no lens flares »
nomme un objet lumineux, « never a glassy stare » un visage.

| Faible | Fort |
|---|---|
| `No lens flares, no light streaks, no floating bokeh orbs.` | `Clean crisp lens glass with a matte finish; every light source stays a soft, round, contained glow within its own source.` |
| `No flat illustration style.` | `Photoreal live-action.` |
| `No CGI look, no video game render.` | `Photoreal live-action: real materials with wear, cast shadows, the distance softening into haze.` |
| `No harsh overhead fluorescent light.` | `Soft daylight from the window at frame-left.` |

**Ce tri ne s'applique qu'à ce qui n'est pas voulu.** Il répond à la question
« sous quelle forme écrire ce que je ne veux pas », jamais à « ai-je le droit de
le vouloir ». Aucune ligne de cette fiche ne retire un choix esthétique.
Ralenti, coupe, zoom, musique, texte à l'écran, tremblement, flare, grain,
vignette : demandés, ils sortent de la queue et prennent leur forme positive,
et c'est le brief qui tranche, pas la table. **Une négation qui interdit ce que
le brief demande est une panne, pas une précaution.** Elle se retire, et la
suppression se déclare, `SKILL.md`, Autorité et lecture. Les formes positives
existantes : ralenti ancré sur une image nommée, `03-sequence.md` ; texte natif
et nappe musicale avec sa courbe, `10-syntax.md` ; artefact optique voulu comme
événement lumineux daté, plus bas et `13-director.md` ; tremblement écrit par
amplitude, fréquence et cause, `01c-action.md`, Le plan nerveux.

**Ne pas confondre avec l'omission.** Un élément qui n'a jamais été mis dans les
entrées visuelles se comporte autrement : il est inventé, et il se déplace à
chaque relance. Ce n'est pas une négation ratée, c'est une information absente,
et la parade est de mettre l'élément dans l'image, pas de reformuler. Mécanisme 6
de `02b-perform-failures.md`.

C'est le même mécanisme que la négation de regard, `does not look at him`, lue
comme `look away` : mécanisme 3 de `02b-perform-failures.md`. Le modèle n'a pas
de représentation de l'absence d'une chose visible ; il lui faut un état à
rendre. Le jeu suit le même partage : `never a frozen, glassy stare` nomme un
visage que le modèle sait rendre. La ligne de sécurité du regard s'écrit donc en
positif, `02a-perform.md`.

**Niveau de confiance.** Hypothèse de travail issue d'une production
photoréaliste, cohérente avec le mécanisme du regard qui, lui, a été observé sur
une autre session. Aucun test à variable unique. Ce que le guide ModelArk 2.5
documente comme négation prise en charge se limite aux **sous-titres et à
l'audio**, « no subtitles », « no BGM », « no audio », avec la consigne « use
positive descriptions whenever possible » ; ses propres exemples emploient
pourtant des négations structurelles, « no jump cuts and no flickering », « do
not change the shot structure, add new shots », « do not alter the two uploaded
videos », qui sont donc au moins tolérées. Contre l'hypothèse de cette fiche :
la page Dreamina du 18 août 2026 écrit « no floating objects », « deformed
hands » en négation, et l'exemple storyboard du guide ModelArk ouvre un bloc
`[Strictly exclude]` qui liste des états visuels dessinables, « line art,
illustration, storyboard frames, tilt-shift miniature look, plastic CG, glossy
overexposed CG ». Le partage de cette fiche reste une préférence de sécurité,
pas une règle documentée : la forme négative d'un état visuel n'est pas
fautive, elle est jugée moins sûre, et un `[Strictly exclude]` à la manière
officielle est un choix légitime quand un rendu a déjà glissé vers ce style.

Conséquence pratique côté image fixe : au moment de **fabriquer** un asset dans
un modèle d'image, bannir explicitement les parasites optiques a du sens, parce
que c'est une autre surface avec d'autres modes de défaillance. Au moment
d'**animer** dans Seedance, ces mots ne doivent plus apparaître dans une
interdiction. Un artefact **voulu**, le flare d'une signature de réalisateur
par exemple, s'écrit en positif comme un événement lumineux avec source,
direction et instant, et le verrou `clean crisp glass` sort alors du prompt,
`13-director.md`. De la même façon, `The image stays sharp, steady and clean`
du gabarit ci-dessous sort dès qu'une texture de mouvement est voulue, caméra
portée, flou de bougé, grain : ce verrou verrouille aussi la stabilité, pas
seulement la propreté de l'optique.

---

### Le verrou positif

Contrepartie positive de la queue de négations, à la même place terminale. Il
énonce ce qui **doit être vrai de l'image finie** plutôt que ce qui ne doit pas
arriver : positions, regards, identités, optique, ce que chacun dit et ne dit
pas.

```
[Positive Locks]
Opens on a silent level wide with the four in the exact positions above, every
mouth closed. Hard cut to a medium of <A>, then a hard cut to a medium of <B>.
<A> looks screen-left toward <C>; <B> looks screen-right toward <A>. Each speaks
only his own line, verbatim. Identities, wardrobe, and props match the reference
tags. Soft oval bokeh, clean crisp glass, light sources as soft contained glows.
The image stays sharp, steady and clean.
```

**Règle d'arbitrage : le bloc terminal dit soit ce qui ne doit pas arriver,
soit ce qui doit être vrai à l'image, jamais deux fois le même fait sous les deux
formes.** Un plan dont les risques sont structurels, coupe involontaire,
duplication d'objet, ralenti, garde la queue de négations. Un plan dont les
risques sont d'apparence, optique, mise en place, attribution de parole, prend le
verrou positif. Un plan qui porte les deux natures de risque prend les deux
blocs, avec des faits disjoints.

Ce que le verrou positif n'est pas : une répétition du contrat de continuité. La
continuité nomme ce qui ne change pas pendant la durée. Le verrou décrit la
dernière lecture qu'on veut du plan entier. Écrire les deux sur les mêmes faits
transforme la clause en bruit, voir la fin de cette fiche.

Le verrou exploite la pondération par répétition et position décrite au
mécanisme 5 de `02b-perform-failures.md`. C'est la seule répétition assumée du
prompt, et c'est pour ça qu'elle doit rester courte et ne porter que l'essentiel.

---

### Arbitrage des conflits

Avant de générer, une passe de cohérence sur trois axes.

**Référence contre référence.** Si deux fichiers se contredisent sur le costume,
la direction de lumière ou les proportions, décider lequel gagne et l'écrire.
Sinon le modèle moyenne.

**Référence contre prose.** Une prose qui contredit une référence produit une
moyenne des deux. La règle et son exemple vivent dans `04-references.md`, section
Ne jamais contredire une référence dans la prose.

**Prose contre prose.** Le cas des termes caméra incompatibles est le plus
courant : « drone shot, handheld close-up, locked-off dolly, fast orbit »
convoque quatre grammaires visuelles qui ne coexistent pas. Choisir.

**Le test de plateau.** Lire le prompt une fois comme une timeline. Si deux
directions ne pouvaient pas se produire simultanément sur un vrai plateau, les
simplifier avant de générer. C'est le filtre qui attrape le plus de prompts
cassés avant qu'ils ne coûtent une génération.

---

### Ce qu'on ne met pas dans la queue

- Les qualificatifs de qualité : « high quality », « 4k », « masterpiece ». Sans
  effet utile, ils consomment de l'attention et tirent vers le registre du
  rendu, `05-anchoring.md`, La texture photographique.
- Les négations universelles sans objet nommé : « no artifacts », « no errors ».
- Les négations qui nomment un artefact visuel dessinable : elles l'invoquent.
  Voir la section correspondante ci-dessus.
- Les contraintes qui contredisent le corps du prompt. `no cuts` avec un `Cut to`
  dans les beats annule l'un des deux, sans qu'on sache lequel.
- Les répétitions de la clause de continuité. Une fois suffit ; répétée, elle
  devient du bruit.
