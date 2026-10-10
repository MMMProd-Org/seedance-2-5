# 04 Utiliser des références

La référence est l'endroit où une vidéo tient une identité ou dérive. C'est aussi
l'endroit où la plupart des prompts faibles s'écroulent, parce qu'uploader un
fichier n'est que la moitié de l'instruction.

Plafonds, volumes fiables et durées d'entrée : `07-spec.md`.

---

## Sommaire

- Le manifeste : quel fichier fait autorité sur quoi, rôles et exclusions
- Adresser par index, décrire par contenu
- Nommer les assets
- Retrouver les références dans un prompt traduit
- Le budget en couches : identité, monde, style, mouvement, son
- Le bloc d'identité
- Ne pas réécrire ce que la référence porte déjà
- Mémoire du fil
- Une référence ne se retire pas parce que l'angle change
- Choisir ses fichiers
- Fournir la structure : première et dernière image, keyframes, storyboard,
  maquette blanche

---
## Le manifeste

Avant les beats, un tableau mental : quel fichier fait autorité sur quoi.

| Token | Rôle | Hériter | Exclure |
|---|---|---|---|
| `@image1` | Courrier | Visage, cheveux, veste, proportions | Arrière-plan |
| `@image2` | Marché | Architecture, placement des stands, matières, lumière, caractère optique | Les personnes présentes |
| `@image3` | Tube | Forme et matière | Composition, angle de vue, reflets du studio |
| `@video1` | Démarche | Action corporelle et timing | Identité, vêtements, décor |
| `@image4` | Palette | Relations de couleur | Composition |

**Écrire une exclusion dès qu'une fuite est plausible, pas seulement quand elle
est certaine.** Le tutoriel ModelArk le demande dans les mêmes termes : dire ce
que chaque asset apporte, apparence, action ou timbre, « et ce qui ne doit pas
être référencé ». Une photo prise dans une cuisine amène la cuisine avec elle sauf
mention contraire. Une photo de trois quarts amène son angle de vue de la même
façon, et gagne contre un profil demandé en texte : l'exclusion,
`do not copy @image1's viewing angle or framing`, plus l'angle fourni, section
Tenir une taille de plan et une composition de `01-write-shot.md`.

Une plaque de décor porte davantage qu'un espace : elle porte aussi le
**caractère optique** du plan, compression, forme du bokeh, distorsion de bord.
C'est un rôle à assumer plutôt qu'à subir, parce qu'une optique demandée dans un
prompt vidéo ne tient pas d'un plan à l'autre. Voir `05-anchoring.md`.

Une fois le registre posé, chaque ligne du prompt doit s'y accorder. La règle
du rôle unique par token et ce qu'une instruction contradictoire y fait vivent
dans `10-syntax.md`, Un token porte exactement un rôle de production.

Traduit en prompt, une ligne par fichier, autorité puis exclusion :

```
@image1 defines the courier's face, hair, and rust-red jacket. Do not use the
image background.
@image2 defines the market architecture and stall placement. Do not use the
people in the image.
@video1 defines the walking pace and camera height only. Do not use its subject,
clothing, or setting.
```

**Si deux fichiers sont en désaccord, décider lequel gagne avant de générer.**

---

## Adresser par index, décrire par contenu

`@image1` seul est un pointeur nu. L'accoler à une courte description donne au
modèle l'adresse **et** quelque chose vers quoi revenir quand un rendu dérive :

> the matte off-white headphones reference @image1

Quatre notations utiles :

- **Rôle nommé** pour un casting : `<Conservator> corresponds to @image1`.
- **Priorité renforcée** pour le sujet critique : `the lead vocalist must
  strictly follow @image5`.
- **Groupe** pour une figuration interchangeable : `reference @image6 to @image10 for
  the rest of the orchestra`.
- **Conformité** en clôture de la ligne de description : `100% match to the
  reference image`, forme vue dans des prompts d'exemple d'une surface, absente
  des pages ModelArk.

Ne pas confondre les deux dernières. La **conformité** dit que ce qui est décrit
doit ressembler à sa référence, et rien n'empêche de la poser sur chacune. La
**priorité** dit lequel gagne quand deux références se disputent un attribut, et
la poser sur tout le monde la supprime.

Ne jamais grouper des **sujets nommés distincts**. « Les images 1 à 4 définissent
quatre personnages respectivement » ne dit jamais quelle image est quel
personnage, et le modèle interpole.

Lier l'identité **dans le texte, jamais dans l'image** : un nom écrit sur une
référence est lu comme du contenu d'image et finit imprimé dans le cadre.
Constaté sur une surface, et publié : le guide ModelArk déconseille de porter
le mapping « seulement dans l'image », écrire « John » sur le portrait puis
« John est à l'école » dans le prompt confond ou duplique le personnage.

---

## Nommer les assets

L'index est l'adresse dans un prompt. Le nom est l'identité de l'asset dans le
projet, et sur une série de plans c'est lui qui empêche la bibliothèque de
pourrir. Sans convention, un projet un peu long fabrique des doublons, le même
canapé vit sous trois noms, et personne ne sait laquelle des trois références est
la vraie.

**Un élément, un nom.** Le même nom sur l'asset, dans le prompt, et dans le
tableau de suivi.

```
type + projet + nom + scène + version

@loc_ON_dorm_commonroom_front_s2
@char_ON_rudy_s2_v1
@prop_ON_pizza
```

**Le suffixe de scène** rattache l'asset à l'endroit où il vit. **Le suffixe de
version** apparaît quand un état change, et un changement d'état est **un nouvel
asset avec un nouveau nom, jamais un écrasement.** Un personnage a autant
d'assets que d'états traversés : le même homme assis dans la salle commune et
allongé sur un lit d'hôpital sont deux assets.

**Dépendance de surface, à trancher avant de bâtir dessus.** Certaines
plateformes gèrent des assets de projet nommés, sauvegardés une fois et
rappelés par leur nom dans le prompt sans réupload ; le nom est alors le token.
Ailleurs, l'adressage reste positionnel, `@image1`, et le nom n'est qu'une
étiquette côté projet qu'il faut **mapper vers l'index au moment d'écrire**. Dans
ce second cas, la règle de réassignation s'applique en plein : réordonner les
uploads change toutes les adresses. Voir `10-syntax.md`.

---

## Retrouver les références dans un prompt traduit

Quand les instructions sont en chinois, conserver les **noms de projet et de fichiers fournis dans
leur écriture d'origine**, sans traduction ni translittération. Associer chaque
nom lisible à son token exact dans le manifeste du prompt. Réutiliser ce nom
dans les beats qui mettent ce sujet en jeu, sans le remplacer uniquement par
un nom ou rôle chinois. Une courte description française peut distinguer des
vues ou versions ; elle ne renomme pas l'asset.

Sous PROMPT FINAL, **avant le bloc de code à copier**, afficher un tableau dans
la langue de la conversation : **Token exact | Nom lisible / fichier source
connu | Rôle**. Une ligne par référence utilisée. Pour une première image sans
token, indiquer son slot réel. Ne pas inventer de nom de fichier : si aucun nom
n'est fourni, proposer un libellé descriptif, le marquer « libellé proposé »
puis le conserver. Si l'utilisateur exige exclusivement le prompt collable,
omettre le tableau extérieur et garder les associations nom-token dans le texte.

Le nom est un repère humain, **pas une nouvelle adresse** : `Ophélie (@image1)`
ne devient pas `@Ophélie` sur une surface à index. Pour un token nommé ou injecté,
conserver sa forme exacte selon `10-syntax.md`, sans fabriquer d'alias avec `@`.

Fragment pour un exemple dont les références sont nommées **Ophélie** et
**Avenue_La_Defense**, adressées respectivement par `@image1` et `@image2` :

```text
Ophélie (@image1)：仅用于人物身份和服装；不采用背景、光线或构图。
Avenue_La_Defense (@image2)：仅用于街道布局和照明；不采用人物或构图。
0-3s：Ophélie 沿人行道向画面右侧行走。
```

C'est une convention de repérage demandée par l'utilisateur, pas une promesse
de meilleure génération. Le tableau reste hors du texte à coller ; les noms
et tokens utiles au modèle restent dedans. Rôles et exclusions suivent le
manifeste canonique ci-dessus.

## Le budget en couches

Cinquante slots ne veut pas dire cinquante opinions. Chaque référence est une
instruction, et des références contradictoires se combattent.

| Couche | Volume | Contenu |
|---|---|---|
| Identité | 3 à 6 images | Le personnage sous plusieurs angles. Une planche de tournette, face, profil, trois quarts, bat six selfies, jusqu'à cinq sujets ; au delà, une vue par image, `07-spec.md` |
| Monde | 2 à 5 images | Plaques de décor, accessoires clés, costume |
| Style | 1 à 3 images | Une image d'étalonnage ou un photogramme qui définit le look, sans les sujets du plan, condition dans `05-anchoring.md`, La texture photographique |
| Mouvement | 0 à 2 vidéos | Une chorégraphie ou un trajet caméra à suivre |
| Son | 0 à 2 audios | La musique à caler, ou une voix de référence |

**Quatre à huit références** font une génération solide. Ajouter une référence
seulement pour combler un manque diagnostiqué, pas par principe.

**L'ordre est une priorité.** Les index les plus bas tiennent l'identité le plus
fermement, constat rapporté par des fournisseurs, non isolé par un test. Le
visage ou le produit hero en premier.

Au-delà de cinq sujets, préférer **une vue propre par sujet**. Des angles séparés
tiennent mieux qu'une planche contact, que le modèle lit comme une seule image
chargée.

---

## Le bloc d'identité

Quand un personnage réapparaît, trois à cinq ancres visibles, recopiées **à
l'identique** dans chaque scène.

> Clearly adult woman in her thirties; square face, short black bob with a silver
> streak above the left eyebrow; rust-red courier jacket; narrow navy trousers;
> brass message tube across her back.

Ne pas dire rouge rouille dans un prompt, orange brûlée dans le suivant et cuir
cuivré plus loin, sauf si on veut de la variation.

**Ne jamais contredire une référence dans la prose.** Si l'image montre un
costume marine, ne pas écrire smoking noir : le modèle coupe la poire en deux et
perd les deux.

---

## Ne pas réécrire ce que la référence porte déjà

Quand une vidéo de référence porte le mouvement et le travail caméra, nommer
**seulement les attributs à hériter**. Redire l'action en mots combat la
référence attachée.

Même logique en image to video : la source fournit apparence, composition,
couleurs, souvent la lumière. Diriger ce qu'une image fixe ne peut pas montrer :
mouvement, caméra, timing, réponse de l'environnement, son, image finale.

C'est l'étape la plus souvent sautée et la plus déterminante. Sans direction de
mouvement, le résultat est soit imprévisible, soit quasi immobile.

Découpage propre entre une image et une vidéo de référence, chacune son job :

> @image1 controls only the exact fictional silver sports car: preserve its body
> shape, silver paint, front light signature, black roof, wheel-spoke design,
> proportions, vents, and ride height. Do not copy @image1's sunny San Francisco
> waterfront or parked composition. @video1 controls only the low side-tracking
> camera height, parallel motion, subject framing, and real-time movement rhythm.
> Do not copy the skater, skateboard, cone, clothing, beach, or concrete setting
> from @video1.

Deux contrôles spécifiques à l'image to video au visionnage : **distorsion du
sujet** et **dérive d'identité en fin de clip**. Si l'un lâche, renforcer la
préservation et **réduire la quantité de mouvement demandée**. C'est dans les
mouvements amples et rapides que le gauchissement s'installe.

---

## Mémoire du fil

**Chaque prompt est un îlot.** Le modèle n'a pas d'avant. « comme au plan
précédent », « même veste que tout à l'heure », « elle est toujours assise
au même endroit » désignent une mémoire qui n'existe pas, et la clause tombe.
Sur une série de plans, tout se réécrit intégralement à chaque fois :
positions, poses, costumes, accessoires, optique, lumière, voix. C'est ce qui
rend le verrouillage des formulations et des blocs de voix payant, parce
qu'on les recopie et qu'on ne les reformule jamais.
**Cette règle porte sur la mémoire du moteur, pas sur celle du rédacteur.**
Le moteur n'a pas d'avant ; la conversation, elle, en a un. Confondre les
deux fait repartir d'une page blanche à chaque plan et perdre le manifeste,
les formulations verrouillées et la ligne de look. Le rédacteur tient le
fil, il réécrit tout dans le prompt et ne redécide rien : `04-references.md`,
Une référence ne se retire pas parce que l'angle change. Quand le fil n'est
pas dans la conversation, il se demande, Questions de préparation de `00-quickref.md`.

---

## Une référence ne se retire pas parce que l'angle change

**Une référence ne sort du manifeste que sur instruction de l'utilisateur, ou
sur un conflit diagnostiqué**, dérive d'identité constatée à l'écran,
`09-diagnose.md`. Jamais sur le jugement du rédacteur qu'elle ne servira pas.

Cas constaté : sur une série de plans, un plan en vue de dessus d'une voiture,
et la référence de la voiture retirée du manifeste au motif qu'on ne la
distinguerait pas sous cet angle. C'est un contresens sur ce que porte une
référence.

**Ce qu'une référence d'objet porte encore sous un angle qu'elle ne montre
pas** : les proportions, la couleur exacte, la ligne de toit, le dessin des
jantes, les baguettes et les jointures, la garde au sol, l'usure et l'état de
la peinture. L'exemple de la section précédente le dit déjà, il énumère
`black roof`, `proportions` et `ride height` : trois attributs qu'une vue de
dessus utilise directement. Une photo de trois quarts avant ne montre pas le
toit en entier, elle en donne la couleur, la largeur et la courbure, et sans
elle le modèle rend une voiture de sport générique.

**Un angle que la référence ne couvre pas est un manque à combler, pas une
raison de la retirer.** La parade est celle de `05-anchoring.md` : le sujet
demandé sous un angle absent des références est un des cas où l'on bascule sur
l'image, la référence d'identité restant dans le pool à côté. Retirer plutôt
qu'ajouter transforme une géométrie manquante en identité manquante, et on perd
les deux.

**Le piège vient de la règle dure 12.** Chaque prompt est un îlot, donc le
manifeste se réécrit intégralement à chaque plan. Réécrire n'est pas
redécider : le manifeste du plan précédent est le point de départ du suivant,
et chaque référence qui n'y figure plus est une suppression qui se déclare,
`SKILL.md`, Autorité et lecture. « On ne la verra pas » n'est pas une raison de
suppression recevable ; « elle contredit la référence d'identité et le visage a
dérivé au rendu » en est une.

Constaté sur une session de production, non isolé par un test à variable unique.

---

## Choisir ses fichiers

- Références propres et isolées. Un packshot sur fond neutre et un portrait sur
  fond uni résolvent mieux qu'une photo lifestyle, qui traîne son arrière-plan.
- Une référence dont on veut le cadre, placement caméra, échelle, composition,
  doit être au ratio de livraison. Une image 16:9 donnée comme référence de
  placement pour une sortie 9:16 ne peut pas être reproduite ; le modèle en
  conserve le sujet, un visage derrière une vitre par exemple, et recompose le
  cadre seul, en général plus large. Recadrer la référence au ratio cible avant
  de l'uploader, ou la fabriquer directement au bon ratio comme première frame,
  `05-anchoring.md`. Même au ratio de livraison, une référence en pool ne donne
  qu'une ressemblance ; la reproduction exacte n'existe qu'en slot première
  image, `05-anchoring.md`, Première et dernière image. Constaté sur une
  session, non isolé par un test à variable unique.
- Pas de références qui se contredisent sur le costume, la direction de lumière
  ou les proportions.
- Verrouiller le jeu. Dès qu'un jeu donne un bon résultat, le réutiliser tel quel
  pour toute la série. C'est ce qui rend une séquence cohérente de plan en plan.
- Itérer l'image hero dans un modèle d'image, puis l'animer. Quand un cadre doit
  être exactement juste, le générer d'abord en image : une image itère en
  secondes, une vidéo non.
- Ancrer les rôles principaux par référence et décrire la figuration en prose :
  le modèle traite le jeu ancré comme fixe et remplit l'arrière-plan.
- Un prompt ne sauve pas un visage indéfini ni une tenue qui change entre les
  images sources. Construire les assets avant les prompts.

---

## Fournir la structure

Par contrôle croissant.

### Première et dernière image

Dire **dès la première ligne** qu'une image est la première frame et l'autre la
dernière, puis décrire l'unique action continue entre les deux. Décrire chaque
ancre séparément : un « ces deux images sont la première et la dernière » groupé
n'en lie aucune.

Contrainte dure : **même ratio pour les deux**, sinon la dernière est étirée.

### Keyframes

Ouvrir par « use @image1 through @imageN as keyframes in this order », puis
donner l'état clé que représente chaque image. Les keyframes contrôlent l'ordre
des étapes, pas la reproduction de chaque frame.

### Planche storyboard

Communique l'ordre des plans et la composition approximative, pas le détail.
Rester sous une quinzaine de cases, trait propre, texte minimal, sens de lecture
indiqué, et **exclure le style de la planche** pour que le trait ne finisse pas
dans le rendu. Publié dans le guide ModelArk : au delà de quinze cases, images
figées et ordre faux ; une planche IA sur-accentuée ou chargée est déconseillée,
le trait simple, façon bonhomme bâton, est recommandé ; et le prompt fait le
reste en trois temps, le mapping des assets, un résumé de l'histoire, puis
l'intrigue case par case en comblant au minimum ce que la planche ne montre
pas, actions, caméra, style, avec des timestamps si l'ordre des événements
compte. Une planche de concept ou de keyframes se contente d'un prompt court,
« construire l'histoire complète dans l'ordre de la planche, plans cohérents ».

### Maquette blanche

Un modèle 3D non texturé porte la structure spatiale, la pose des sujets, les
trajectoires et le placement caméra, et le modèle pose le style par-dessus. Elle
porte aussi le timing : trajets, découpage, points de coupe, changements de
lumière, rythme sonore.

Bénéfice supplémentaire rapporté par le skill d'origine, non retrouvé dans les
pages ModelArk 2.5, qui ne parlent que d'hériter les changements de lumière
contenus dans la maquette : à partir de l'information spatiale, le modèle
génèrerait un éclairage cohérent, direction de source, température, intensité,
projection des ombres. À traiter comme un constat, pas comme une promesse.

Patron adapté à un pool vidéo compatible avec `@video1` ; garder le token
réel de la surface selon `10-syntax.md` :

> Refer to @video1 for camera movement, pacing, shot-size transitions,
> subject trajectory, and blocking. Refer to @image2 for character design, scene,
> materials, lighting, color, and atmosphere, and render the white model as a
> [STYLE CIBLE].

Mapper chaque volume gris à son sujet final par son nom, « the red model in
@video1 becomes the man in grey from @image1 ». Dire ce qui est hérité de
la maquette et rien d'autre : caméra et mouvement, plus les changements de
lumière seulement si la maquette en contient et qu'on les veut. Décrire malgré
tout le contenu voulu en détail, en accord avec ce que montre la maquette, et
l'apparence de tout sujet qui n'a pas de référence. Sur une maquette fine,
**retirer d'abord les lignes de trajectoire, les axes et les pyramides de
caméra**, sinon ils sont rendus eux aussi. Les volumes se limitent au tronc :
des membres ou des ailes qui impliquent un mouvement fin sortent raides, sauf
si leur séquence de mouvement est complète dans la maquette. Tout ce paragraphe
est publié dans le guide ModelArk, la note sur les membres dans sa version
chinoise seulement.

Enregistrer une référence de performance avec les membres complets dans le cadre,
un contact visible, une caméra stable et le ratio cible. Et l'autorisation de
l'interprète.
