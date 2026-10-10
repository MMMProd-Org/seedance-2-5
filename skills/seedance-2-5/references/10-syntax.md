# 10 Syntaxe

Comment s'écrivent les tokens, les sons, les répliques et les blocs. Sert à
**toutes** les tâches d'écriture, pas seulement à celles qui touchent un clip
existant.

Une partie de la syntaxe est universelle, une autre dépend de la surface. La
distinction compte : une convention appliquée là où elle n'est pas lue coûte
juste quelques caractères, mais une convention **absente** là où elle est lue
coûte une génération.

---

## Sommaire

- Contrat commun : adressage, tokens, plages temporelles, négations, direction
  d'écran, dialogue
- Dépendant de la surface : assets nommés, crochets typés, blocs de structure
- Langue et dialogue, dont le verrou de voix
- Audio
- Ce que Seedance 2.5 ne fait pas précisément

---

## Contrat commun, syntaxe de la surface prioritaire

**La surface fait autorité sur l'adressage.** Recopier exactement le token
qu'elle fournit, y compris majuscules, espaces, identifiants et délimiteurs.
`@Image 1`, `@image1`, `<<<img6>>>` et un identifiant nommé ne sont pas
interchangeables par décision de l'assistant. La documentation officielle
emploie plusieurs formes ; leur présence dans des exemples ne prouve pas
que toutes les interfaces les acceptent toutes.

Ordre de décision :

1. Token réellement injecté ou convention confirmée pour cette surface : le
   conserver littéralement. Ne jamais le traduire ni le couper par un retour
   à la ligne ; ne pas supprimer un espace qui en fait partie.
2. Pool indexé confirmé sans forme fournie : les patrons du skill emploient
   `@image1`, `@video1`, `@audio1` comme convention de travail. Adapter avant
   livraison si la surface attend une autre forme.
3. Slot première/dernière image : utiliser son nom ou son token **réellement
   exposé**. Ne pas inventer un index de pool pour ce slot. Sur une surface
   observée il n'avait pas d'adresse ; ce constat n'est pas universel.

La maquette blanche est une vidéo de référence dans le guide 2.5, adressée
notamment par `<video1>` ou `[Video 1]`. Les patrons utilisent donc `@video1`
quand la surface confirme cette forme. `@clayrender1` vient de prompts anciens :
ne le produire que si la surface l'expose ou le confirme, sans série d'essais
aveugles de tokens.

Une mauvaise adresse peut être ignorée ou interprétée comme du texte. Vérifier
l'association asset–token avant de diagnostiquer le contenu du fichier.

**Un token porte exactement un rôle de production sur tout le prompt.** `@image1`
ne peut pas désigner le personnage dans une ligne et le décor dans une autre. Si
un fichier doit apporter deux choses, les dire dans la ligne où le token est
introduit. Une instruction qui contredit le rôle déclaré d'un token est la cause
la plus fréquente de dérive de sujet.

Deux règles dures :

- **Ne jamais adresser un slot non fourni.** La clause qui portait le pointeur
  mort est silencieusement abandonnée.
- **Revérifier après réupload ou réordonnancement.** Dans un pool positionnel,
  déplacer l'asset du slot 3 au slot 5 change son index ; actualiser les tokens
  concernés sans altérer les identifiants nommés qui sont restés stables.

**Plages temporelles.** `0-5s:`, `5-12s:` ou `0–5 seconds:`. Consécutives, non
chevauchantes. Aussi acceptés : le point unique (« at 5 seconds, the camera
whip-pans left ») et le relatif (« three seconds after she sits, the lights
dim »).

**Négations.** En fin de prompt, en clair : `No cuts`, `no slow motion`,
`no subtitles`, `no music`. Toutes ne se valent pas : une négation qui nomme un
artefact visuel dessinable l'invoque au lieu de l'interdire. Voir la section
`12-constraints.md`.

**Direction d'écran.** `screen-left`, `screen-right`, `frame-left`,
`frame-right`, `toward camera`, `back to camera`, `in the left third of frame`.
C'est le repère à employer pour les places et les regards, parce qu'il est
indépendant du point de vue des personnages : « à sa gauche » demande au modèle
de savoir de qui on parle et de quel côté il est tourné, « screen-left » non.
C'est aussi ce qui tient l'axe entre deux générations séparées.

**Dialogue.** Guillemets droits autour de la réplique, avec locuteur et moment :

```
0-3 seconds: she looks into the camera and says, "I bought this for the commute."
```

---

## Dépendant de la surface

## Assets nommés de projet

Certaines surfaces permettent d'enregistrer un personnage, un décor ou un
accessoire comme **élément de projet** : sauvegardé une fois, rappelé par son nom
dans le prompt, sans réupload à chaque clip. Le nom devient alors le token, et
l'adresse ne dépend plus de l'ordre des uploads.

```
@char_ON_rudy_s2_v1 : tall lean man, ~190 cm, short dark curly hair...
@loc_ON_dorm_commonroom_front_s2 : the warm cluttered student common room,
front angle. Controls architecture, materials, clutter, and light only.
```

La convention de nommage et la discipline de versionnage sont dans
`04-references.md`. Ce qui relève de la syntaxe est plus court :

- Le token nommé obéit au même contrat : forme exacte de la surface, sans
  traduction, normalisation ni retour à la ligne interne.
- **Vérifier que la surface les lit** avant de bâtir une série dessus. Là où
  l'adressage reste positionnel, un token nommé est un pointeur mort et sa clause
  tombe en silence, exactement comme un slot non fourni.
- Sur une surface positionnelle, le nom reste utile côté projet, mais le prompt
  doit **mapper nom vers index** au moment de l'écriture, et tout réordonnancement
  des uploads redéfinit toutes les adresses.

## Crochets typés

Convention documentée côté ByteDance, dans le tutoriel API ModelArk 2.5 comme
sur **Jimeng, Dreamina et Doubao**. Non utilisée dans les exemples des
fournisseurs API tiers, où le dialogue passe en guillemets droits.

| Contenu | Marqueur | Exemple |
|---|---|---|
| Musique | `( )` | `(Soft, rhythmic piano music plays in the background)` |
| Effet sonore | `< >` | `<A bell rings in the distance>` |
| Dialogue | `{ }` | `{Hello, welcome back.}` |
| Sous-titre à l'écran | `【 】` | `【Chapter One: Departure】` |

Leur intérêt : lever l'ambiguïté sur le **type**. Sans eux, deux accidents
classiques, une réplique dessinée à l'écran en légende, et un effet sonore
prononcé à voix haute par le sujet.

**Test en un coup pour savoir si ta surface les lit.** Générer un clip de 5
secondes avec une réplique en accolades et rien d'autre. Si la réplique est
parlée et non écrite, la convention passe. Si elle apparaît à l'écran, revenir
aux guillemets droits plus `No subtitles`.

Corollaire : pour zéro texte incrusté, ne jamais utiliser `【 】` et ajouter
`No subtitles.` en fin de prompt.

## Blocs de structure

Le modèle lit des en-têtes entre crochets simples comme des sections. Utile pour
un brief long et multi-personnages, superflu pour un plan simple.

| Bloc | Rôle |
|---|---|
| `[Generation Goal]` | Une phrase disant ce que la vidéo doit montrer |
| `[Characters]` `[Props]` `[Scenes]` | Groupement des références par type |
| `[Stage N]` | Un étage, avec état initial, événement, état final |
| `[Maintain Consistency]` | Ce qui reste constant sur toute la durée |
| `[Edit Goal]` `[Source Video Role]` `[Edit Scope]` `[Content to Preserve]` | Les quatre blocs d'une édition |
| `[Material Roles]` `[Image Order]` `[Motion Amount]` `[Final Style]` `[Audio]` | Les cinq blocs d'un assemblage multi-images, voir `06-edit-extend.md` |
| `[Subject settings]` `[Overall style]` `[Strictly exclude]` `[Shot list]` | Les quatre blocs de l'exemple storyboard du guide ModelArk 2.5 ; le troisième est une liste de négations de style, arbitrage dans `12-constraints.md` |

Trois blocs supplémentaires sont employés par ce skill. Ils ne figurent pas dans
la documentation ByteDance : ce sont des en-têtes libres, lus comme des sections
au même titre que les autres, et employés parce que le contenu qu'ils portent n'a
pas de bloc documenté.

| Bloc | Rôle | Source |
|---|---|---|
| `[Position Map]` | Lie chaque couleur d'un schéma de mise en place à un personnage, et borne sa portée aux positions | Ce skill, voir `11-diagram.md` |
| `[Eyelines]` | Direction d'écran de chaque regard, y compris vers un personnage hors champ | Ce skill |
| `[Positive Locks]` | Clôture positive : ce qui doit être vrai de l'image finie | Production tierce, voir la `12-constraints.md` |

**Règle de maintenance : tout en-tête crocheté employé quelque part dans le skill
figure dans l'une de ces deux tables.** Un vocabulaire de blocs qui grossit sans
être déclaré ici devient une convention privée par fiche, et les patrons cessent
d'être interchangeables.

Ne pas confondre `[Bloc]` et `【Sous-titre】` : le second est en crochets pleine
chasse et produit du texte à l'écran.

---

## Langue et dialogue

### Choisir la langue des instructions

La demande explicite prime. Pour améliorer un prompt existant sans demande
de traduction, garder sa langue d'instructions, chinois compris. Pour un
nouveau brief sans préférence établie, garder l'anglais par défaut du skill ;
ce défaut est une convention, pas une supériorité mesurée. La langue de la
conversation, des répliques et des instructions vidéo sont trois choix distincts.
La traduction des instructions vidéo ne traduit pas les en-têtes de sortie,
dont la liste complète vit dans `17-delivery.md` ; les conserver tels quels,
sauf demande explicite contraire.
Le contenu du self-eval, les réglages et les explications restent dans la
langue de la conversation. « Prompt en chinois » ne demande pas un audit en
chinois ; « prompt seul » retire ces explications selon le contrat de sortie.

**Publié :** le [tutoriel BytePlus 2.5](https://docs.byteplus.com/en/docs/ModelArk/2607688#2.5_multi_language)
dit accepter les prompts et la génération audiovisuelle en chinois et en
anglais, entre autres langues. Le [guide de prompts](https://docs.byteplus.com/en/docs/ModelArk/2607689)
contient des exemples anglais. Pages consultées le 9 septembre 2026 ; aucune
comparaison contrôlée chinois contre anglais identifiée dans ces pages.
Les réussites chinoises et anglaises rapportées par l'utilisateur ne permettent
pas d'isoler l'effet de langue de celui du découpage, des assets ou des réglages.

**Traduire sans réécrire la scène.** Garder tels quels les tokens de la surface,
y compris ceux qu'elle injecte, noms verrouillés, nombres, unités, plages
temporelles et répliques exactes. Traduire les instructions autour de ces
éléments ; vérifier en particulier gauche et droite d'écran, membre utilisé,
ordre causal, états, exclusions de référence et régime temporel. Ne pas convertir
une langue de dialogue par simple traduction de la direction technique.
Les blocs d'identité et de voix déjà verrouillés restent littéraux, sauf
demande de traduction de ces blocs ; toute nouvelle version se verrouille à son tour.

**Références repérables sans lire le chinois :** appliquer
[04-references.md](04-references.md), Retrouver les références dans un prompt
traduit, pour les noms visibles dans le prompt et leur correspondance destinée
à l'utilisateur. Un token préservé sans nom lisible ne suffit pas.

En chinois, employer des phrases et des titres simples, par exemple `场景：`
et `镜头 1（0-4s）：`. Ne pas copier les crochets `【 】` des exemples importés
comme titres techniques : voir Crochets typés. Garder une seule version finale,
sauf demande de variantes linguistiques.

**Si l'utilisateur demande quelle langue donne le meilleur rendu :** proposer
une comparaison de deux traductions sémantiquement équivalentes, mêmes assets,
mode, durée, ratio, réglages et graine si la surface l'expose. Comparer identité,
actions, continuité, caméra et audio sur plusieurs rendus ; ne pas réécrire la
chorégraphie d'une version ni conclure sur un seul succès. Ce protocole est une
méthode de comparaison, pas un test déjà effectué ni un lancement automatique.

Pour une édition ou une extension, préserver l'intention de tâche dans la
langue choisie selon `06`, Les mots déclencheurs sont obligatoires ; les verbes
anglais de ses exemples ne sont pas des tokens à conserver littéralement.

### Diriger la langue parlée

**Nommer la langue avant toute réplique.** La doc ne le recommande que hors chinois ;
ce skill la déclare toujours, parce que ça coûte un mot. La nommer de
nouveau si le modèle part sur la mauvaise. Le patron complet :

```
langue → variété régionale ou accent → style de débit → locuteur → réplique
```

```
Dialogue language: American English. The girl says in natural, conversational
American English: "I thought you weren't coming."
```

Nommer la **variété régionale** est ce qui donne un débit spécifique. « authentic
Los Angeles English » produit autre chose que « English », qui donne une lecture
neutre.

Quatre disciplines de dialogue :

**Court et attribué.** Une ou deux répliques par clip. Les longs dialogues
augmentent les risques sur la synchro labiale, le timbre, le timing et
l'attribution.

**Bloqué comme du mouvement.** Dire ce qui se passe avant, pendant et après la
réplique, sinon le modèle empile plusieurs actions par-dessus la parole. Et
fermer les autres bouches : « Her mouth moves only during her own lines. »

**Minuté.** Donner un début et une fin à la réplique, comme à n'importe quelle
action.

**Externalisé quand les mots comptent.** Quand la formulation exacte est
contractuelle, enregistrer la voix à part et la poser au montage.

Pour une série multilingue, respécifier à chaque clip langue, ton, identité du
locuteur et contexte de marché. Pour une voix fournie en référence, la lier au
bon locuteur.

### Le verrou de voix

Une voix dérive d'un clip à l'autre tant qu'elle n'est pas écrite. Elle se décide
**une fois**, sous forme d'un bloc, et ce bloc se recopie dans chaque génération
**mot pour mot, sans même changer un synonyme.** C'est la discipline du bloc
d'identité de `04-references.md`, appliquée à l'oreille : « baryton chaleureux »
et « voix grave et chaude » décrivent la même chose pour un lecteur humain et
deux voix différentes pour le modèle.

Cinq champs suffisent, et il vaut mieux s'y tenir que d'écrire un paragraphe.

```
registre et tessiture → timbre et grain → débit → manière et dynamique →
langue et variété
```

```
BOB voice: warm boisterous baritone, big dynamic range, theatrical comedic
enthusiasm, a gravelly edge; bursts loud then drops to a mock-confidential
murmur, punches key words, laughs mid-line. American.
```

Tenir ces blocs dans un document à part, un par personnage, et y puiser sans
reformuler. Sur une série, c'est le seul moyen de garantir que le texte collé au
clip 30 est identique à celui du clip 1.

Le verrouillage réduit la dérive, il ne garantit pas un timbre identique. C'est
un point de rupture à écouter, pas un réglage.

---

## Audio

Séparer cinq catégories, ne pas les mélanger dans une phrase fourre-tout :

```
ambiance | son d'action | dialogue | musique | silence
```

**Placer chaque son dans le beat qui le cause**, pas dans une clause audio de
fin ; seules l'ambiance et la nappe musicale vont dans une ligne globale. Règle
et raison dans `SKILL.md`, Le squelette.

```
[Stage 1]
Primary event: <Barista> fills the mug and seats the black lid.
Audio: <The espresso machine hisses, then a soft click as the lid seats>.
```

À défaut, les sons d'action peuvent être **horodatés** :

```
Audio: light rain on the glass roof, distant tram engine, soft market footsteps,
a clear brass bell at 6 seconds, the tube touching the wooden counter at 25
seconds. No music, no narration, no random subtitles.
```

Nommer deux ou trois sons diégétiques précis bat toute direction musicale vague.
Avec une référence musicale, dire ce qui se cale dessus : « cuts land on the
beat, final pose on the last hit ». Pour une nappe native, dire si elle monte,
tient ou se résout, et à quel beat : « music holds under the walk, rises on the
door, resolves on the last frame », recommandation Dreamina du 18 août 2026. Les
patrons de ce skill disent `no music` par défaut parce que la nappe se pose au
montage, où elle se choisit et se cale ; le guide 2.0 listait « audio négligé »
parmi les erreurs courantes, et les exemples 2.5 écrivent leur BGM et leurs
bruitages dans le prompt. Quand la livraison est
native, l'écrire avec sa courbe.

L'audio est généré dans la même passe et coûte du temps de rendu. L'éteindre
pendant qu'on itère sur la structure, le rallumer pour la livraison.


---

## Ce que Seedance 2.5 ne fait pas précisément

- **Les timestamps allouent du temps**, ils ne coupent pas au frame près.
- **Une édition** augmente les chances d'alignement sur la source, elle ne
  garantit pas un recouvrement image par image.
- **Sous-titres, formules, signalétique, spécifications** qui doivent être exacts
  restent un travail de post-production.
- **Micro-contrôle haute fréquence** : plusieurs actions distinctes dans une
  seconde risquent de se mélanger ; aucun seuil précis d'échec n'est établi
  ici. Un timestamp n'est pas un pilotage image par image.
- **Risques de production** : physique complexe et interactions de plusieurs
  sujets. Diagnostiquer l'écart avant de simplifier ; annoncer toute réduction
  du brief. L'attribution ancienne de ces faiblesses à ByteDance n'a pas été
  retrouvée dans les pages officielles, `07-spec.md`.

---
