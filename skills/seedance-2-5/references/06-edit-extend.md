# 06 Éditer, étendre, relier

Deux opérations qui partent d'un clip existant. Ce qui les distingue tient au
verbe : un verbe d'édition **réécrit à l'intérieur** de la durée existante, un
verbe de continuation **ajoute de la durée** avant ou après.

**Presque tous les échecs d'édition sont des erreurs de mode, pas des erreurs de
prompt.** Donner sa vidéo finie comme matériel d'inspiration et redécrire la
scène entière produit exactement ce qu'on a demandé : une nouvelle vidéo inspirée
de la sienne, avec une autre pièce, une autre caméra, un autre visage.

| Mode | Tu as | Forme du prompt |
|---|---|---|
| **Référence** | Aucune vidéo finie | Brief de génération, plus les matériaux |
| **Édition** | Une vidéo finie à garder | Demande de changement, plus la source |
| **Extension** | Une vidéo finie à prolonger | Demande de continuation, plus la source |



## Sommaire

- Les mots déclencheurs sont obligatoires
- Les prompts d'édition sont courts
- Six commandes courtes
- Les opérations
- Éditer
- Étendre
- Transfert de caméra
- Ce qui se finit ailleurs
- Transition entre deux clips
- Assemblage multi-images

---

## Les mots déclencheurs sont obligatoires

Le modèle décide du type de tâche à partir des **assets fournis et de l'intention
lue dans le prompt**. Un prompt d'édition sans verbe d'édition n'est pas reconnu
comme une édition : il part en génération de référence, et le rendu est une
nouvelle vidéo inspirée de la source. Sur les surfaces qui valident les
contraintes, c'est une erreur franche.

| Tâche | Exemples anglais de verbes explicites |
|---|---|
| **Édition** | `edit video`, `add`, `insert`, `remove`, `delete`, `modify`, `replace`, `change to` |
| **Extension** | `extend forward`, `extend backward`, `continue`, `continue from`, `extend the story` |

Ces verbes expriment l'intention de tâche ; ce n'est pas une liste de mots
anglais réservés. Dans la langue choisie selon `10`, garder une instruction
d'édition ou de continuation tout aussi explicite, le maître et la portée.
Traductions de rédaction, sans test de rendu propre : `仅修改 @video1 中的…`
pour modifier seulement la portion nommée ; `从 @video1 的最后一帧继续生成 4s`
pour ajouter après la dernière frame. Pour une extension avant la source,
dire explicitement avant sa première frame ; ne pas inverser avant et après
avec une traduction ambiguë de « forward ».

Formulations officielles anglaises, à adapter à la langue retenue :

```
Add small animals to @video1
Replace the character in @video1 with @image1
Remove the background music from @video1
Extend @video1 backward: the character from @image1 falls from the sky
Continue the first 5 seconds of @video1: the woman from @video2 enters and says...
```

Le déclencheur ouvre le prompt. Le placer en fin de phrase après trois lignes de
décor affaiblit la lecture de l'intention : hypothèse cohérente avec la
pondération par position de `02b-perform-failures.md`, non testée seule.

## Les prompts d'édition sont courts

Le prompt long et détaillé appartient au mode référence. En édition, la longueur
vient de la **précision de la cible**, jamais de la redescription de la scène.

Trois étapes, et la troisième est celle qu'on saute :

1. **Pointer la source.**
2. **Nommer ce qui change et ce que ça devient.** Pour un remplacement, joindre
   l'image de la nouvelle apparence. Pour un ajout ou un retrait, décrire l'objet
   et où il est.
3. **Verrouiller le reste.** Un « everything else in the frame stays unchanged »
   explicite. Sans lui, le modèle considère les zones non citées comme libres.

```
Mauvais : Change the man's jacket to a leather one and make it look better.

Bon :     Replace the clothing of the man in dark clothes in @video1 with the
          clothing in @image2. Everything else in the frame stays unchanged.
```

Le second nomme la cible précisément, « the man in dark clothes » et pas « the
man », fournit la nouvelle apparence en référence, et verrouille le reste.

## Six commandes courtes

```
Retirer     Remove the drone and the foreground rail from @video1. Fill the
            removed areas naturally. Everything else stays unchanged.

Ajouter     Keep the people, environment, and composition in @video1 unchanged.
            [OBJET] appears in the character's hands.

Décor       Replace the setting in @video1 with [NOUVEAU DÉCOR] @image1. Keep
            the choreography exactly as it is; do not change the original rhythm.

Relight     Change the lighting in @video1 from [ÉTAT ACTUEL] to [ÉTAT CIBLE].

Restyle     Keep the camera movement and rhythm of @video1. Change the visual
            style to [STYLE].

Audio       Keep the picture and camera movement in @video1 unchanged. Replace
            the background music with @audio1.
```

Sur le relight, nommer **l'état actuel et l'état cible**. « Make the lighting
better » ne donne rien : le modèle ignore ce qui déplaît.

Une plage temporelle se glisse dans n'importe laquelle de ces commandes :
`between 0:02 and 0:05`. C'est la différence entre un correctif ciblé et un
re-roll complet.

Paramètres hérités et non réglables : `07-spec.md`.

---

## Les opérations

| Opération | Ce qu'elle fait |
|---|---|
| Édition par instruction | Ajoute, retire ou change du contenu par le texte, avec plage optionnelle |
| Édition par image de référence | Échange un élément pour coller à une image fournie |
| Ajout de sujet | Insère une personne, un accessoire, un effet, reste inchangé |
| Suppression de sujet | Efface un objet, un filigrane, un logo, puis comble le trou |
| Édition de point de vue | Garde personnages, actions et style, ne change que la caméra |
| Édition fond vert | Remplace le décor en gardant le sujet et sa physique |
| Édition audio | Remplace la musique, ajoute des effets, change la voix |
| Extension | Continue en avant, génère l'instant d'avant, ou relie deux clips |

---

## Éditer

Forme longue, quatre blocs. Nommer le clip source comme **maître unique**,
énoncer la portée, lister ce qui ne doit pas bouger.

```
[Edit Goal]
Edit @video1. Only from 4-7 seconds, change the cool blue light on the right
wall to warm orange light.

[Source Video Role]
@video1 is the sole editing master. It defines the character, room layout,
actions, composition, camera movement, audio, and event order.

[Edit Scope]
Change only the light color on the right wall and the area it illuminates. Allow
skin tone to respond naturally.

[Content to Preserve]
Keep the character's identity, clothing, expression, position, motion, room
structure, camera movement, dialogue, and ambience from @video1.
```

Forme courte, une phrase, reprise d'un prompt publié antérieur, non retrouvée
dans les pages 2.5 :

> Edit @video1. Keep the characters, actions, and visual style unchanged. Adjust
> only the camera movement. [PLAN CAMÉRA SEGMENTÉ]. Keep the entire sequence
> smooth, continuous, and stable.

Les deux fonctionnent. La forme longue vaut quand la portée est ambiguë ou qu'il
y a beaucoup à geler.

Le bloc de préservation est celui que tout le monde bâcle. Ce qui n'y est pas
nommé est réinterprétable.

### Échanger un sujet

Un bloc de plus, celui qu'on oublie : le remplaçant **hérite de la timeline de
l'original**. Chaque apparition, chaque mouvement, chaque occultation, chaque
sortie, avec le même timing, la même trajectoire, la même vitesse. Sans ça, le
nouvel objet est au bon endroit et au mauvais rythme.

Le remplacement d'arrière-plan fonctionne pareil, avec une portée définie comme
tout ce qui est en dehors de la silhouette du sujet.

### Fond vert

Le décor change et le sujet reste, mais il doit **répondre à la physique du
nouvel environnement** : direction de flottement des vêtements, état des cheveux,
rythme de la foulée, interaction avec la lumière.

> Using @video1, render the green-screen background, obstacles, wardrobe, and
> supporting characters. 0–4s: outdoor training, replace the obstacles with
> rocks, bricks, tires, and wooden crates. 4–10s: locker room, friends offering
> encouragement. 10–15s: international match, replace the training poles with
> defenders and a goalkeeper, and the protagonist scores. Overall photorealistic,
> cinematic quality.

Exemple repris du skill d'origine comme prompt publié, non retrouvé dans les
pages 2.5, où le fond vert n'est pas nommé : « cinematic quality » n'est pas à
reprendre, règle dure 4. Conditions : sujet **uniformément éclairé** et
détourage propre.

### Éditer l'audio

Séparé du visuel. Nommer le locuteur ou la catégorie de son, le changement, et ce
qui reste. « Retirer la musique en gardant dialogue, lip-sync, ambiance et
effets » tient en une instruction.

### Vérification après édition

Contrôler la zone réparée **sur toute la timeline**, pas seulement dans la
fenêtre éditée : les scintillements apparaissent souvent aux frontières.

---

## Étendre

L'extension greffe de la matière neuve sur une **frame frontière**. Décrire cette
frame **avant** l'action nouvelle. C'est l'ordre qui compte.

En avant, la première frame du segment continue la dernière frame de la source.
En arrière, la dernière frame du segment doit **arriver sur** la première frame de
la source.

> @video1 is the source video to extend forward. Extend @video1 forward. The
> first frame of the extended segment directly continues from the last frame of
> @video1. Maintain the same locked-off medium shot, the paper airplane's
> position and orientation, the classroom-window background, the afternoon
> lighting, and its movement toward frame right.
>
> Then, the paper airplane continues gliding right and exits the frame while the
> curtain beside the window sways slightly.

Forme d'enchaînement narratif reprise du skill d'origine, non retrouvée dans
les pages 2.5, dont les extensions publiées sont « Extend @Video 1 by 5
seconds. A bee flies in... » et « Extend @Video 1. After the window opens,
move into the art gallery interior shown in @Video 2... » :

> Extend the video. Continue from the visuals and subjects in @video1 and
> generate another 30-second clip, keeping the character subjects, scene, visual
> style, and sound effects consistent. [ACTION NOUVELLE].

Ordre de priorité de ce qu'on maintient :

```
identité du sujet → lieu et costume → lumière et palette → design sonore
```

Si la continuité casse, renforcer la référence ou la clause de maintien **avant**
de réécrire l'action.

### Extension en arrière : deux gardes

**Dire quelles matières appartiennent seulement au clip d'origine**, sinon des
personnages ou accessoires censés arriver plus tard apparaissent trop tôt.

**« Se raccorder à la source » ne suffit pas.** Énoncer la première frame de la
source comme état final explicite, sinon l'image continue de changer après être
déjà arrivée.

### Chaînage

Chaque clip validé redevient la source de l'extension suivante, sujet, décor et
audio nommés comme continus. Plusieurs tours sont possibles.

Selon la surface, une extension peut renvoyer **uniquement le nouveau segment** :
c'est le cas de l'API ModelArk, dont l'exemple publié montre le segment de 5 s
puis le film recollé à part. Le vérifier au premier essai sur une interface web :
si c'est le cas, concaténer soi-même et livrer les morceaux dans un format à
faible perte pour que la jointure reste propre.

Point de rupture publié : le **volume sonore** du segment étendu peut différer
de la source ; l'écart est plus faible quand la source vient elle-même de
Seedance 2.5. À écouter à la jointure, et à égaliser au montage.

Alternative sans extension : extraire la dernière image du clip, ou la demander
à l'API, qui sait renvoyer la dernière frame, et la passer comme première image
de la génération suivante. Voir `03-sequence.md`.

---

## Transfert de caméra

Une vidéo fournit **le mouvement seulement**, une image fournit l'identité.

> @video1 provides camera movement only. Do not use its subject, clothing, or
> setting. @image1 defines the exact character. Recreate the same camera path
> around the character in a bright modern studio, with stable identity and one
> continuous motion.

La négation explicite empêche la référence vidéo de traîner son décor.

---

## Ce qui se finit ailleurs

Sous-titres exacts, logos, typographie de marque, coupes au frame près,
étalonnage final, mixage multipiste : dans un monteur. Une édition augmente les
chances que les événements se calent sur la source, elle ne garantit pas un
recouvrement image par image. Une transition sans couture vise la continuité
visuelle et sonore, pas la préservation au pixel.


---

## Transition entre deux clips

Mode à part entière : générer le pont manquant entre deux vidéos existantes.
Deux clips déjà compatibles se joignent par une coupe au montage, sans pont
à générer. Pour choisir le mécanisme du passage réellement manquant,
lire [15-camera-techniques.md](15-camera-techniques.md). Dans le gabarit
ci-dessous, la transformation graduelle s'emploie si elle est demandée ; sinon
la remplacer par le mécanisme de raccord choisi, sans modifier les portions sources.

```
Clip avant → clip après → déclencheur → mouvement caméra → transformation
visuelle → état d'arrivée → transition audio
```

```
@video1 is the before-transition clip. Use its <sujet de fin, action,
composition, direction caméra, audio>.
@video2 is the after-transition clip. Use its <sujet d'ouverture, composition,
direction caméra, audio>.
Keep <identité, structure produit, décor, action principale> stable in the
original portions of both.

At the end of @video1, <sujet ou objet d'avant-plan> triggers the transition
through <action>. The camera <direction et changement de vitesse>, while <forme,
matière, lumière ou espace> gradually transforms into <élément correspondant> at
the start of @video2. The transition ends naturally at @video2's opening
composition, preserving continuity in <position, direction caméra, tendance de
mouvement>. Audio transitions smoothly from <avant> to <après>.
```

| Méthode | Ce qu'il faut préciser |
|---|---|
| Plongée ou marche arrière | Direction caméra, changement de vitesse, quand la scène suivante commence |
| Rotation du personnage | Pose, sens de rotation, comment vêtement et fond changent en continu |
| Occultation par l'avant-plan | Quand l'objet remplit le cadre, et la composition qui suit |
| Morphing d'objet | Formes correspondantes, matières, et le processus de transformation |
| Point ou mise au point | Mouvement caméra, cible de focus, relation spatiale continue |

Un pont généré vise la continuité visuelle et sonore, pas un raccord au pixel.

Forme minimale, quand le contexte suffit :
`Generate a 4-second transition between @video1 and @video2, seamlessly
matching picture, color, and camera movement.`

La génération native reste dans la plage **4–30 s**, `07`. Si le pont livré
doit durer 3 s, distinguer 4 s générées et 3 s montées. Une remise à durée du
segment entier conserve les deux extrémités mais accélère le mouvement :
vérifier les phases et vitesses aux raccords, traiter l'audio séparément ou
adapter sa durée. Un simple rognage peut supprimer une ancre ; ne le proposer
que si les états de raccord survivent. Ne pas réécrire les clips sources.

---

## Assemblage multi-images

Organiser plusieurs images, éventuellement avec une vidéo de style, en un film
court au rythme cohérent. Ne jamais écrire seulement « fais-en une vidéo ».

```
Rôles des matériaux → ordre des images → quantité de mouvement → rythme de
montage → traitement visuel → audio
```

```
[Material Roles]
@image1 to @imageN provide <scènes, sujets ou produits>.
@video1 provides <rythme de montage, caméra ou style> only. Do not use its
subjects or scene.

[Image Order]
Use the images in <l'ordre donné, ou groupées par thème>.

[Motion Amount]
Apply <slight, moderate, strong> motion to each image.

[Final Style]
Use <rythme, méthode de transition, traitement visuel>.

[Audio]
Include <dialogue, ambiance, effets, musique>.
```

Si l'ordre compte, l'énoncer exactement. S'il peut être libre, dire que le modèle
peut regrouper par thème. Avec plusieurs personnages ou produits, continuer à les
nommer et à les lier un par un.
