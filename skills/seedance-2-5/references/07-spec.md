# 07 Spécifications

Le contrat technique du modèle, les paramètres verrouillés par mode, la syntaxe
native, et les points juridiques.

À ouvrir pour vérifier une limite, un plafond, une écriture de token, ou avant de
livrer à un client.

## Sommaire

- **Publié par ByteDance** : table
  des capacités, durées, résolutions, plafonds d'assets, langues, codes
  d'erreur.
- **Publié aussi : recommandations d'entrée** : les volumes d'entrée de la
  table du guide, durées des clips de référence, ce qui est conseillé sans
  être imposé.
- **Constaté par surface** : outils de finition Dreamina, autorité du sélecteur
  de la surface, ce qui varie d'une interface à l'autre.
- **Contraintes des fichiers d'entrée** : formats, ratios, tailles, durées,
  plafonds de requête. Elles font échouer avant tout prompt.
- **Ratios et formats de sortie** : les six ratios et leurs définitions,
  `adaptive`, et les trois ratios à ne pas confondre.
- **Paramètres verrouillés par mode** : tâches verrouillées et tâches libres,
  ce que l'édition, l'extension et la première image figent.
- **Marketing à ne pas propager** : specs 2.0 recyclées sous l'étiquette 2.5.
- **Coût et arbitrage** : facturation à la seconde, coût par plan accepté.
- **Visages réels : upload direct refusé** : le blocage de modération et ses
  contournements légitimes.
- **Points juridiques** : noms de réalisateurs et d'artistes vivants, droits,
  mentions, rétention des URL.

---




Trois niveaux de confiance à tenir séparés en permanence : publié par ByteDance,
constaté sur une surface donnée, marketing de revendeur. Le marché autour de
Seedance 2.5 est plein de pages qui recyclent les specs de Seedance 2.0 sous
l'étiquette 2.5.

Les deux textes officiels de cette fiche : le « Dreamina Seedance 2.5 prompt
guide » (BytePlus ModelArk, docs.byteplus.com/en/docs/ModelArk/2607689, version
chinoise Volcengine 82379/2607689) et le « Dreamina Seedance 2.5 tutorial »
(ModelArk/2607688), relus le 10 septembre 2026. Tutoriel mis à jour le
9 septembre 2026 ; guide le 31 août 2026. « Publié » veut dire écrit dans
l'un des deux : [tutoriel](https://docs.byteplus.com/en/docs/ModelArk/2607688),
[guide](https://docs.byteplus.com/en/docs/ModelArk/2607689).

---



## Publié par ByteDance

Les anciennes dates de lancement et la liste de plateformes n'ont pas de
source primaire conservée ici. Elles ne sont pas reprises comme faits vérifiés.
La table ci-dessous décrit les deux pages ModelArk, pas toutes les interfaces
qui commercialisent le modèle ; leurs réglages propres restent à vérifier.

| Paramètre | Valeur |
|---|---|
| Durée | 4 à 30 s en une passe, sans stitching, ou `-1` : le modèle choisit un entier dans [4, 30] d'après le prompt et les assets. En édition, `-1` est obligatoire et hérite de la source |
| Résolution | 480p et 720p en 8 bits, **1080p en 10 bits, encodé H.265/HEVC**. Défaut 720p. Pas de 4K, contrairement à Seedance 2.0 |
| Ratio | `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `adaptive` qui est le défaut ; règles plus bas |
| Format de sortie | `mp4` par défaut, `mov` professionnel ; `watermark` optionnel, faux par défaut |
| Extension | Plusieurs tours d'extension |
| Références images | jusqu'à 30, jusqu'à 4K |
| Références vidéo | jusqu'à 10 |
| Références audio | jusqu'à 10 ; une génération à partir d'audio seul, sans image ni vidéo, est acceptée en 2.5 |
| Total | 50, soit 30 + 10 + 10, trois pools distincts |
| Adressage | `@image1`, `@video1`, `@audio1`. Les prompts de maquette publiés en 2.5 adressent la vidéo par `<video1>` ou `[Video 1]` ; `@clayrender1` vient de prompts publiés antérieurs, `10-syntax.md` |
| Langues | **11** : chinois, anglais, espagnol, indonésien, malais, thaï, arabe, portugais, vietnamien, japonais, coréen |
| Édition | par instruction, par image de référence, par plage temporelle, audio seul |
| Avancé | maquette blanche, édition de point de vue caméra, transition entre deux clips, assemblage multi-images. Le fond vert n'est pas nommé dans les pages 2.5 : c'est une édition de décor, `06-edit-extend.md` |
| Outil officiel | Un skill d'optimisation de prompt, `sd25-pe`, installable par `npx --yes skills@latest add "https://arkdocs-en.tos-ap-southeast-1.volces.com/skills/" --skill sd25-pe --yes`, usage `/sd25-pe` suivi du prompt. Non lu ici : rien de ce skill ne s'en réclame. La version chinoise du guide renvoie aussi à un document Lark de gabarits par tâche, bytedance.larkoffice.com/docx/OsiUdR1OxoDqvnxsK8LczYx7nPd |

Le ratio se règle par paramètre, jamais par le texte du prompt : une ligne
« 16:9 » dans le prompt oriente la composition, elle ne fixe pas le fichier de
sortie. Publié : le tutoriel liste `ratio` parmi les paramètres de sortie et
décrit ce que fait `adaptive`, détail dans Ratios et formats de sortie, plus
bas. La tolérance des timestamps, de l'ordre de la seconde, est une
observation, `03-sequence.md`.

Le 1080p en HEVC ne se lit pas partout : si la lecture échoue, VLC, mpv ou
QuickTime, dit la doc. À prévoir avant de livrer un fichier à un client.
INVÉRIFIABLE dans les deux pages : ce que produit `1080p` combiné à `mov`, dont
l'encodage publié est H.264 yuv444p. Lire les métadonnées du premier rendu avant
de promettre un codec.

**Risques de production, attribution non confirmée :** physique complexe et
interaction de plusieurs sujets. L'ancienne attribution de ces faiblesses à
ByteDance ne figure pas dans les deux pages relues ; sa source n'a pas été
retrouvée. Les traiter comme risques à contrôler, pas comme un aveu officiel
ni une raison de réduire automatiquement le brief.

---

## Publié aussi : recommandations d'entrée

Le guide ModelArk consacre une table aux volumes d'entrée. Ces chiffres sont
donc publiés, pas seulement constatés.

**Durées des clips de référence.** Un clip vidéo ou audio de référence dure de
2 à 30 secondes, et le **cumul par modalité** plafonne à 30 secondes. Pour un
sujet porté par une vidéo ou un audio, **5 à 10 secondes** ; plus long, la
stabilité baisse et il faut relancer.

**Édition d'un clip existant.** Garder la source sous 20 secondes et
l'accompagner de 1 à 5 images de référence, 6 à 8 seulement si l'édition l'exige.

**Volumes fiables.** Les plafonds sont des plafonds, pas des cibles.

| Pool | Bande fiable | Zone dégradée |
|---|---|---|
| Sujets image | 1 à 8 | 9 à 12, plus de tentatives |
| Sujets vidéo ou audio | 1 à 5 | 6 à 10, plus de tentatives |

**Vues multiples.** Jusqu'à cinq sujets, une image qui montre plusieurs vues du
même sujet est acceptée. Au delà de cinq sujets, une vue par image tient mieux ;
s'il faut plusieurs angles, les séparer en plusieurs images plutôt qu'une seule
image multi-vues. Seedance 2.0 déconseillait les vues multiples, 2.5 les
accepte.

Quatre à huit références font une génération solide : constat de trois pages
fournisseurs, pas un chiffre publié. Les bandes ci-dessus comptent des sujets,
pas des références, et partent de un.

---

## Constaté par surface

**Outils de finition Dreamina**, page du 18 août 2026 : Upscale, Interpolation,
Soundtrack Generation, Consistency Refinement. Ils s'appliquent après la
génération et n'entrent pas dans le prompt ; une livraison en définition ou en
cadence supérieure peut en venir. La même page ne liste que trois ratios dans
l'interface, 9:16, 16:9 et 1:1, là où l'API en expose six : le sélecteur de la
surface fait foi, pour le ratio comme pour la résolution.

Les entrées acceptent des définitions bien plus hautes que la sortie, jusqu'à 4K
en image. Une source propre sert donc à quelque chose même quand la sortie
plafonne.

**Le plafond de 50 références peut être bridé dans l'interface réelle.** Vérifier
le nombre de slots d'upload avant de bâtir un plan dessus.

---

## Contraintes des fichiers d'entrée

Elles font échouer une requête avant toute considération de prompt.

**Images.** Formats jpeg, png, webp, bmp, tiff, gif, heic, heif. Ratio largeur
sur hauteur entre **0,4 et 2,5**. Côtés entre **300 et 6000 px**. Moins de 30 Mo
par image. 1 à 30 images en référence, 1 en première frame, 2 en première et
dernière. Par l'API, le corps de requête plafonne à 64 Mo : pas de base64 pour
un gros fichier, une URL publique ou un asset id.

**Vidéos.** mp4 ou mov, H.264 ou H.265, audio AAC, MP3 ou PCM. 480p ou 720p.
Durée d'un clip entre **2 et 30 s**, jusqu'à 10 clips, **cumul plafonné à
30 s**. Mêmes bornes de ratio et de côtés que les images. Produit largeur par
hauteur entre 407 696 et 8 295 044 pixels, soit de 614×664 à 3326×2494. Moins de
200 Mo. Fréquence entre 24 et 60 fps.

**Audio.** wav ou mp3. Durée d'un clip entre **2 et 30 s**, jusqu'à 10 clips,
cumul plafonné à 30 s. Moins de 15 Mo.

**Cas particulier de l'édition** : la vidéo à éditer doit durer **entre 4 et
30 s**, pas 2. En dessous de 4 s, erreur.

## Ratios et formats de sortie

Ratios disponibles : **21:9, 16:9, 4:3, 1:1, 3:4, 9:16**, plus `adaptive` qui est
le défaut. En 720p cela donne 1470×630, 1280×720, 1112×834, 960×960, 834×1112,
720×1280 ; en 1080p, 2206×946, 1920×1080, 1664×1248, 1440×1440, 1248×1664,
1080×1920 ; en 480p, 992×432, 854×480, 752×560, 640×640, 560×752, 480×854.

**Trois ratios à ne pas confondre.** Le ratio **écrit** dans la ligne de format
est lu comme une intention de composition et ne règle rien à lui seul. Le ratio
**effectif** vient du paramètre, et `adaptive` n'a pas le même sens selon la
tâche, règles publiées dans le tutoriel ModelArk :

- **Texte vers vidéo et référence vers vidéo** : `adaptive` laisse le modèle
  **choisir** l'un des six ratios « d'après le prompt » (règle) et « d'après le
  prompt et les assets de référence » (description du défaut). C'est un choix
  du modèle, pas une règle qu'on peut prédire : la ligne de format y pèse sans
  garantir, et une référence verticale peut l'emporter. Dès que le ratio de
  livraison compte, le régler explicitement, ce qui est le seul cas où le
  paramètre est réglable.
- **Première image, première et dernière image** : `adaptive` obligatoire, la
  sortie prend le ratio de l'image en slot première frame.
- **Édition et extension** : `adaptive` obligatoire, la sortie prend le ratio
  de la vidéo que le modèle identifie comme source d'après le prompt.

Le **rôle de l'image** dépend donc du slot : première image, elle verrouille ;
référence en `adaptive`, elle entre dans un choix qu'on ne contrôle pas ;
référence avec ratio explicite, elle ne pèse plus sur le format. Un rendu
720×1280 sur un prompt écrit en 16:9 est un réglage laissé en `adaptive`, pas
une composition ratée, `09-diagnose.md`.

Corollaire publié, différence avec 2.0 : **n'importe quel ratio entre 0,4 et
2,5** est atteignable en sortie, non par le paramètre, mais par une tâche
verrouillée dont l'asset porte ce ratio. Une vidéo 5:4 éditée ressort en 5:4,
une image 1:1 en première frame donne du 1:1. C'est la voie pour un format hors
des six.

Deux formats de sortie. **mp4** par défaut, compatible partout. **mov** en
encodage professionnel, H.264 avec échantillonnage yuv444p et audio PCM, qui
tient mieux la couleur et la cohérence audiovisuelle. **Recommandé en entrée
comme en sortie pour l'édition et l'extension.** Certains lecteurs ne lisent pas
le mov ainsi encodé : VLC, mpv et ffplay le lisent sur les deux systèmes.

## Paramètres verrouillés par mode

Le modèle distingue deux familles de tâches, ce que Seedance 2.0 ne faisait pas.

**Verrouillées** : l'asset d'entrée est posé comme un segment sur la timeline de
sortie, donc le rendu s'adapte à lui. Édition, première image, première et
dernière image, extension. Ratio toujours `adaptive`, non spécifiable.

**Libres** : l'asset ne sert que de référence sémantique, donc ratio et durée
restent réglables. Référence classique, mais aussi **storyboard et keyframes**,
que l'on croit souvent verrouillés alors qu'ils ne le sont pas.

| Tâche | Ratio | Durée |
|---|---|---|
| Édition vidéo | Hérité de la source, non réglable | Héritée, `-1` obligatoire, sortie jusqu'à 0,4 s plus courte selon le tutoriel, « environ 0,3 s » selon le guide, et possiblement non entière. Aucun écart si la source vient de Seedance 2.5 |
| Première image, ou première et dernière | Hérité de la première image | Réglable, 4 à 30 ou `-1` |
| Extension | Hérité de la source, non réglable | Réglable, 4 à 30 ou `-1`. Que la durée soit celle du seul segment nouveau est déduit de l'exemple publié, « Extend @Video 1 by 5 seconds », dont la sortie de 5 s est montrée puis recollée à part ; le tutoriel écrit « output duration » sans trancher |

Piège sur le travail première et dernière image : **même ratio pour les deux**,
sinon la dernière est étirée pour coller à la première.

**Pool et slot première image, exclusifs ou non : INVÉRIFIABLE.** Par l'API,
ils coexistent, une image en `first_frame` et d'autres en `reference_image`
dans le même `content`, c'est publié. Sur une interface web, rien ne dit si le
slot laisse le pool disponible, ni si le slot consomme le premier index, auquel
cas la première référence s'adresserait `@image2`. Une observation contraire
existe sur une surface, une image en slot n'appartient à aucun pool et n'a pas
d'adresse, `10-syntax.md` ; elle ne vaut que pour cette surface. La question qui tranche, en
une observation avant d'écrire : charger une image dans le slot, puis regarder
si le sélecteur de références reste actif et sous quel numéro la première
référence s'adresse.

Quand plusieurs vidéos sont fournies, c'est le prompt qui désigne laquelle est
éditée ou étendue ; d'où le maître unique nommé en tête, `06-edit-extend.md`.

### Côté API ModelArk

Ce qui suit ne concerne que les appels directs, pas les interfaces web.

- Le type de tâche est déduit des assets et de l'intention du prompt. Le
  paramètre `omni_reference_task_type` (`auto`, `reference`, `edit`, `extend`)
  déclare l'intention. Déclaré `edit` ou `extend`, il fait vérifier les
  contraintes de paramètres **à la soumission** ; omis ou `auto`, tout se
  vérifie après le lancement. Deux erreurs asynchrones dans tous les cas : un
  prompt dont l'intention ne correspond pas au type déclaré,
  `InvalidParameter.TaskTypeMismatch` ; des paramètres incompatibles avec le
  type détecté, `InvalidParameter.TaskTypeConstraint`. Configuration
  recommandée quand on ne distingue pas : `auto`, `ratio` `adaptive`,
  `duration` `-1`, vidéos de 4 à 30 s.
- L'API sait **renvoyer la dernière frame** du rendu, ce qui évite de
  l'extraire soi-même pour chaîner, `03-sequence.md`.
- L'URL de la vidéo vit **24 heures** et **100 téléchargements** ; l'enregistrement
  de la tâche, 7 jours. Télécharger dans la foulée.

---

## Marketing à ne pas propager

**« 4K natif 10 bits. »** Absent de la table des capacités 2.5 ; c'est la ligne
de Seedance **2.0**, qui liste 4k en 10 bits là où 2.5 s'arrête au 1080p 10 bits.

**« 9 images, 3 vidéos, 3 audio »** et **« 4 à 15 secondes »**. Ce sont les
specs de Seedance 2.0. Elles circulent sur des pages étiquetées 2.5, notamment
des dépôts et comparatifs affiliés à des passerelles. Un tableau limité à
15 secondes ne suffit toutefois pas à prouver une confusion : une surface peut
imposer un plafond plus bas. Vérifier modèle exact, mode et interface avant de
reprendre ces valeurs comme limites de Seedance 2.5.

**« Édition au niveau région. »** L'édition ciblée existe et fonctionne, mais sa
précision n'est pas celle d'un masque. Traiter le premier rendu comme un ours.

---

## Coût et arbitrage

La facturation est à la seconde sur les surfaces consultées, point absent des
deux pages ModelArk. Maximiser la durée par défaut double le coût
d'une même idée sans rien améliorer. Valider un look sur un brouillon court en
basse résolution, estimer le lot avant de le lancer, une variable par relance.

Mesurer le **taux de plans exploitables** et le **coût par plan accepté**, pas le
coût par génération.

Passer sur 2.5 quand au moins un de ces quatre points supprime une étape réelle :
continuité sur 30 s, gros jeu de références, action minutée, édition sélective.
Pas sur le seul numéro de version.

---

## Visages réels : upload direct refusé

**Le modèle n'accepte pas l'upload direct d'images ou de vidéos de référence
contenant des visages humains réels.** La modération d'entrée bloque. C'est la
contrainte la plus structurante pour qui travaille avec des comédiens, et elle
n'a pas de contournement par le prompt.

Trois voies documentées :

| Voie | Ce que c'est |
|---|---|
| **Sorties du modèle réutilisées** | Les rendus contenant des visages produits par certains modèles du même compte se réutilisent comme assets d'entrée en création secondaire, sans déclencher le blocage |
| **Personnages numériques préréglés** | Bibliothèque fournie par la plateforme, gratuite, conforme, adaptée quand il faut un visage réaliste sans viser une personne précise |
| **Assets réels autorisés** | Portraits de personnes réelles avec autorisation, via la procédure de la plateforme |

Conséquence de production : une planche d'identité se fabrique **dans**
l'écosystème, par génération d'images, plutôt qu'à partir de photos de plateau.
La doctrine d'ancrage de `05-anchoring.md` reste valable, mais la première image
de la chaîne ne peut pas être une photo d'un comédien.

### Fabriquer la planche

Méthode en deux passes, indépendante du modèle d'image employé.

1. **Le visage d'abord, en gros plan, seul.** Générer l'identité au cadrage le
   plus serré possible, pour que le modèle capture le maximum de détail. Ce gros
   plan devient l'**ancre** : tous les autres assets du personnage sont vérifiés
   contre lui.
2. **Les silhouettes ensuite, en pied**, avec costume, matières et proportions,
   accordées au visage déjà verrouillé.
3. **L'assemblage préserve le portrait d'origine intact.** Il ne repasse jamais
   dans un modèle. Chaque état qui change, cicatrice, coupe, salissure, blessure,
   pièce de costume, s'intègre point par point **par masque autour de la base**,
   dans un outil d'édition, sans y toucher.

La raison tient en une phrase : la base reste les mêmes pixels, donc la texture
de peau qui porte l'identité survit à chaque nouvelle version du personnage. Une
base réencodée à chaque état dérive, et la dérive se compose.

Corollaire de nommage : chaque état est **un nouvel asset avec un nouveau nom**,
jamais un écrasement de l'ancien. Voir `04-references.md`.

**Niveau de confiance.** Méthode rapportée par une production photoréaliste
longue. Cohérente avec la contrainte de modération d'entrée ci-dessus et avec la
règle d'itération en image plutôt qu'en vidéo. Les modèles d'image nommés dans la
source sont propres à sa plateforme et ne sont pas repris ici.

## Points juridiques

Ils comptent dès qu'il y a un client au bout.

- **Références de style** : traduire un nom en propriétés visuelles selon `13`
  est une méthode d'écriture, pas une interdiction juridique générale portant
  sur les artistes vivants. Distinguer style demandé et reproduction d'éléments
  précis d'une œuvre ; ne pas inventer une règle de droit universelle.
- **Matériel de référence** : vérifier les droits nécessaires à l'usage prévu,
  y compris licence, autorisation ou domaine public applicable. Trouver une
  image sur le web ne fournit pas à lui seul cette information.

- **Autorisation de l'interprète** pour toute référence de performance ou de
  mouvement filmée sur une personne réelle.
- **Droit à l'image** pour tout portrait servant d'ancre d'identité.
- Les conditions commerciales varient par plateforme et par abonnement. Les
  vérifier sur la surface utilisée avant de livrer.


---
