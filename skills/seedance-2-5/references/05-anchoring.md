# 05 Ancrer par l'image

Principe directeur : **le modèle tient ce qu'il voit et invente ce qu'il
déduit.** Toute géométrie absente de l'entrée est une invention, et une
invention n'est pas reproductible d'une génération à l'autre.

La conséquence pratique : au lieu de demander une déduction, fournir l'image.
Chaque plan part de sa propre image de référence, produite en amont. Le prompt ne
sert plus alors qu'à animer et à jouer.

Ce n'est pas une obligation. C'est le levier qui rend une séquence
multi-plans reproductible, et il faut savoir quand le tirer.

---



## Sommaire

- Décider l'ancrage
- Ce que le modèle doit déduire, donc invente
- L'optique se porte par l'asset
- La texture photographique
- Le workflow
- La checklist de cohérence entre fixes
- Quand basculer
- Ce que ça ne règle pas
- Règles techniques
- Forme d'un prompt de plan ancré
- Première et dernière image
- Le raccord devient structurel
- Chaîner sans nouvelle image
- Les mots de goût

---

## Décider l'ancrage

Avant d'écrire, repérer la géométrie absente des références.

Sept cas où il devine, donc invente : un contrechamp, la face non vue d'un objet
ou d'un décor, un lieu jamais montré, un personnage sous un angle absent des
références, un état futur, un raccord de lumière entre deux moments distants, la
composition exacte d'un cadre hero.

Dans ces cas, **produire l'image** du cadre et en faire le point de départ
du plan ; le prompt vidéo porte mouvement, jeu, timing et son. Méthode dans les sections de cette fiche.

**La règle de choix.** Un cadre est **exact** dès que le prompt porte
au moins deux des quatre valeurs de composition, qu'elles viennent du brief ou
de la rédaction : l'angle de vue du sujet, son échelle en fraction de cadre, le
partage sol et ciel, sa place en profondeur. Le rédacteur qui compose lui-même
un cadre impose les mêmes valeurs qu'un brief, et la condition ne se lit pas
dans la demande mais dans le texte qu'il vient d'écrire.
Une valeur compte quand elle est chiffrée, angulaire, ou **positionnelle** :
« au sol », « sur le capot », « sur le siège passager » fixent la hauteur et
l'angle ; « le sol au premier plan » fixe le partage ; une focale nommée avec
une distance ou une taille de plan fixe l'échelle, que le texte écrit ensuite
en fraction de cadre, `01`. Une case de storyboard fournie impose ses valeurs
au même titre qu'un chiffre, et se convertit en première image ou en keyframe
pour être tenue, `05`, Quand basculer. Une étiquette de taille seule, « plan
moyen serré », ou une amorce ne comptent toujours pas, c'est du texte, sinon
chaque plan de dialogue exigerait une image.
Un cadre exact, un contrechamp, un sujet sous un angle absent des références,
ou une séquence de plus de deux plans se fournissent en image dès la première
émission quand la surface a un slot première image. Un plan large d'un décor qu'aucune référence ne montre s'y
ajoute, et lui n'attend aucun slot : sa plaque est une référence de pool, `05`,
La texture photographique. Une taille de plan seule, sans autre valeur
imposée et sur un décor déjà porté, reste du texte, section Tenir une taille de
plan et une composition de `01`. Un plan-séquence qui traverse plusieurs
espaces relève de l'arbitrage inverse.

Une exception, `11-diagram.md` : quand ce qui dérive est la place des corps et
la direction des regards dans un décor déjà porté par une plaque validée, c'est
le diagramme de mise en place qui tient la géométrie, pas une image par plan.

Ce choix n'est jamais une confirmation à demander : c'est une décision prise et
annoncée dans le self-eval, `SKILL.md`, Autorité et lecture. Ce que l'`00-quickref.md`, Questions de préparation autorise à demander
est autre chose, et sa liste est fermée : ancrer ou décrire n'y figure pas, et
savoir si la surface a un slot première image y figure, parce que la première
est une décision de rédaction et la seconde un fait que seul l'utilisateur
voit. Et l'instruction de l'utilisateur prime :
s'il demande le texte seul, il l'obtient, le texte porte alors les quatre
valeurs, et le risque est nommé dans les points de rupture. Le premier rendu
observé compte alors comme premier rendu.


---

## Ce que le modèle doit déduire, donc invente

| Cas | Pourquoi il invente |
|---|---|
| **Contrechamp** | Rien dans le cadre source ne dit ce qu'il y a derrière la caméra |
| **Face non vue** d'un objet, d'un décor, d'un bâtiment | L'information n'existe dans aucune entrée |
| **Lieu jamais montré**, qu'on s'y déplace ou qu'un plan large le révèle | Idem |
| **Personnage sous un angle absent des références** | Il interpole entre ce qu'il a |
| **État futur** : produit assemblé, pièce rangée, plat terminé | Il extrapole |
| **Raccord de lumière** entre deux moments distants | Il recalcule une lumière plausible, pas la vôtre |
| **Composition exacte** d'un cadre hero | Il approche, il ne vise pas |

Dans ces sept cas, décrire mieux ne suffit pas. La description ne remplace jamais
la géométrie manquante : elle en réduit la variance, elle ne la fixe pas.

---

## L'optique se porte par l'asset

Extension du même principe à une propriété qu'on croit textuelle : **le caractère
optique demandé dans un prompt vidéo ne tient pas d'un plan à l'autre.**
Anamorphique, compression horizontale, forme du bokeh, distorsion de bord,
aberration : le modèle les rend une fois sur deux et les redécide à chaque
génération.

La parade est la même que pour la géométrie, un cran plus tôt dans la chaîne :
**générer l'image de décor avec l'effet optique déjà dedans.** Le modèle le lit
sur la plaque et le conserve. La plaque devient l'objectif.

Pour une plaque à caractère anamorphique, décrire le **rendu final** voulu
plutôt que mélanger image comprimée de capture et image désanamorphosée.
Patron d'image, à adapter au ratio demandé :

```text
Finished, desqueezed image with natural subject proportions. Vertically
elongated oval background bokeh, slight edge curvature, restrained color
fringing near the edges. Bright practical sources remain localized to their
fixtures. Preserve the requested delivery aspect ratio.
```

Ce patron remplace un bloc ancien qui associait compression horizontale,
hautes lumières étirées et interdiction de traînées. Le succès rapporté de ce
bloc contradictoire n'isolait pas les clauses utiles ; ne pas le réemployer
comme recette validée. Doser les effets selon l'image demandée et examiner la
plaque avant de l'utiliser. Le ratio 2.39:1 n'est pas un effet optique à imposer
à une livraison 9:16.

**Les interdictions n'existent qu'à ce stade.** Bannir les parasites optiques
dans un prompt d'image est utile, c'est une autre surface. Dans le prompt vidéo,
ces mots ne réapparaissent jamais en interdiction : les nommer les invoque. Le
prompt vidéo ne décrit que du verre propre et des sources contenues, voir les
négations qui invoquent dans `12-constraints.md` ; un artefact voulu s'y écrit
en positif, même fiche.

```
Clean crisp lens glass with a matte finish, soft oval bokeh; the window and
practical lights read as soft, round, contained glows within their own sources.
```

Deux conséquences de production.

**Le ratio de livraison est décidé au stade de l'asset**, puisque la plaque le
porte. Toute la planche partage le format cible.

**En génération multi-segments à coupes franches**, redéclarer par segment ce
que `03-sequence.md` liste, optique et lumière comprises : chaque coupe
recompose un cadre, et la clause d'un segment ne court pas sur le suivant.

**Niveau de confiance.** Constat rapporté par une production photoréaliste
longue, non isolé par un test à variable unique. Vérifier aussi la surface avant
de bâtir la recette : certaines interfaces exposent l'optique comme un sélecteur
plutôt que comme du texte, auquel cas le réglage prime.

---

## La texture photographique

Même principe, une propriété de plus. Un décor rendu photographique en plan
serré peut sortir en rendu 3D dès qu'on élargit le cadre, sans que rien d'autre
ait changé dans le prompt. Le mécanisme supposé est celui de cette fiche : le
plan large est le plan qui montre **le plus de ce qu'aucune référence ne
montre**. Le produit ou le visage sont dans le pool ; la rue, la façade, la
foule, le ciel n'y sont pas, donc le modèle les invente, et ce qu'il invente
sans plaque porte sa texture par défaut, propre et régulière, celle qu'on lit
comme un jeu vidéo. Un plan large de décor sans plaque est le cas « lieu jamais
montré » de la table ci-dessus, quelle que soit la taille des plans voisins. La
définition de sortie joue dans le même sens : à 720p, un plan large répartit les
mêmes pixels sur bien plus d'objets.

Trois parades, par fiabilité décroissante, et elles se cumulent.

1. **La plaque du plan large se fabrique en premier**, et elle se valide à l'œil
   sur sa texture avant tout : matières usées, ombres portées, perspective
   atmosphérique. Une plaque qui rend 3D contamine tous les plans qu'elle
   ouvre. Elle porte ensuite l'optique et la lumière, sections précédentes.
2. **Une image de look dans le pool**, `04-references.md`, Le budget en couches, avec
   son rôle borné : `@imageN defines the photographic look only: texture,
   contrast, color; do not use its subject, place or framing`.

   Condition sur l'image de look : elle ne doit **pas contenir les sujets du
   plan**. Une image de look où figurent le personnage et le véhicule du plan
   est lue comme une référence de composition, et `do not use its framing` ne
   tient pas contre elle en texte seul, section Tenir une taille de plan et une
   composition de `01-write-shot.md` ; avec une première image, la clause qui
   protège les ancres, section Première et dernière image, n'a pas été mise à
   l'épreuve sur ce cas. La clause de rôle s'écrit quand même, elle ne suffit
   pas. Trois sorties, par ordre de préférence : la recadrer sur une zone sans
   sujet, ou la passer au modèle d'image comme style de la fixe et la sortir du
   pool vidéo, ou la remplacer par une image de look sans sujet. Constaté sur
   une session, non isolé par un test à variable unique : une image
   d'étalonnage montrant le personnage devant la voiture a produit la
   composition de cette image, caméra à hauteur de capot et voiture de face,
   contre un texte au sol et de profil ; le même brief comptait aussi ses
   valeurs à une au lieu de quatre, section Quand basculer, et les deux causes
   n'ont pas été séparées.

3. **En texte, une ligne de look positive, recopiée dans chaque plan** avec le
   bloc lumière : `photoreal live-action: real materials with wear, cast
   shadows, the distance softening into haze`. Sur un plan ancré, c'est la
   seule redescription admise avec la lumière, en une ligne, pour que le
   mouvement ne l'efface pas ; sur un plan non ancré, elle ne remplace pas la
   plaque, elle empêche le plan de repartir de zéro. Ce qui la ruine : nommer le rendu
   qu'on refuse, `no CGI look`, `no video game`, qui l'invoque comme tout style
   nommé en négation, `12-constraints.md` ; et les mots du registre du rendu,
   `ultra-detailed`, `8K`, `epic`, `vast`, `render`, qui sont des adjectifs de
   goût et tirent vers lui. Le budget de détail vaut aussi : un plan large
   propre a peu de formes, grandes, et une seule source ; les petits objets en
   nombre sont ce qui se dégrade le plus à cette définition.

**Niveau de confiance.** La chute vers le rendu 3D sur le plan large d'une
séquence dont les plans serrés sont photographiques est constatée en
production, non isolée par un test. Le mécanisme est une hypothèse cohérente
avec la doctrine d'ancrage et avec la définition de sortie de `07-spec.md`.
Aucune source ne documente ce comportement. Ce qui est rapporté par des guides
fournisseurs (Atlas Cloud, 7 août 2026 ; Kapwing, 21 août 2026), dans l'autre
sens, sur la direction anime : le vocabulaire du prompt déplace le registre de
rendu, « cinematic lighting, dramatic shadows » suffit à sortir du cel-shading.
La symétrie, un vocabulaire de rendu qui sort du photographique, est une
hypothèse de travail.

**Valider une plaque au chiffre, pas à l'impression.** Une plaque générée
transmet sa sursaturation à tout le plan, et l'œil s'y habitue en trois
regards. Trois mesures, sur la plaque et sur l'image d'étalonnage du projet,
comparées : part de pixels saturés, au seuil qu'on se fixe une fois et qu'on
garde pour tout le projet, saturation médiane, répartition des teintes. Relevé
sur une session : 82 % de pixels saturés sur la plaque contre 46 % sur
l'étalonnage, écart que l'œil ne voyait pas et que l'image portait. Au delà
d'une vingtaine de points d'écart, la plaque se refait avec la ligne de look ;
ça ne se corrige pas dans le prompt vidéo, qui n'étalonne rien. Constaté sur
une session, seuil posé sur ce seul cas.

**Une plaque porte le lieu, pas son mouvement.** Une plaque porte le lieu,
l'optique et la lumière. Elle ne porte pas le mouvement. Ce qui n'est pas écrit
comme bougeant est rendu comme une photographie derrière le sujet : passants,
véhicules, embarcations, feuillage, pluie, reflets, enseignes. Sur un plan à
caméra verrouillée, la vie du fond est la seule source de mouvement en dehors
de l'acteur ; elle s'écrit en un bloc nommé, sujets, directions et vitesses
distinctes, jamais en un adjectif du type animé ou vivant.

---

## Le workflow

1. **Découper en plans.** Le découpage devient le livrable de tête, pas une note
   d'intention.
2. **Générer chaque cadre clé en image fixe.** C'est là qu'on itère : une image
   se refait en secondes pour une fraction du coût d'une vidéo.
3. **Vérifier la cohérence entre les fixes**, avant toute génération vidéo.
4. **Chaque image validée devient le point de départ de son plan.**
5. **Le prompt de plan se réduit** à ce que l'image ne montre pas : mouvement,
   caméra, timing, réponse de l'environnement, son, état final.
6. **Assembler au montage.**

C'est le métier du storyboard, sauf que le storyboard est aussi l'entrée
technique. La vérification de cohérence passe **en amont sur des fixes** plutôt
qu'en aval sur des vidéos, ce qui est la différence entre corriger et
recommencer.

---

## La checklist de cohérence entre fixes

À passer sur la planche complète avant de lancer la moindre vidéo. Chaque ligne
ratée ici coûte une génération vidéo si elle passe.

- [ ] **Identité** : le visage, la coupe et les proportions sont les mêmes d'un
      cadre à l'autre.
- [ ] **Costume** : mêmes pièces, mêmes couleurs nommées de la même façon.
- [ ] **Direction de lumière** : la source vient du même côté, ou son
      déplacement est voulu et progressif.
- [ ] **Température et palette** : pas de saut d'étalonnage non voulu.
- [ ] **Position à l'écran** : un personnage à gauche reste à gauche d'un plan à
      l'autre, sauf franchissement d'axe assumé.
- [ ] **Axe** : le contrechamp respecte la règle des 180 degrés, ou le
      franchissement est motivé.
- [ ] **Accessoires** : les objets présents dans le plan N le sont encore dans le
      plan N+1, et dans la même main.
- [ ] **Ratio** : identique sur toute la planche.
- [ ] **Optique** : même caractère d'objectif sur toute la planche, puisque c'est
      elle qui le porte jusqu'au rendu.
- [ ] **Texture** : même rendu photographique sur toute la planche, le plan
      large compris ; une fixe qui lit 3D se refait avant de servir.
- [ ] **Regards** : la direction d'écran de chaque personnage est cohérente d'un
      cadre à l'autre, celui qui regarde à gauche continue de regarder à gauche.
- [ ] **Air dans le cadre** : là où la caméra doit voyager ou le sujet entrer, la
      marge existe.
- [ ] **Continuité d'état** : ce qui est ouvert, posé, allumé ou tenu à la fin du
      plan N l'est au début du plan N+1.
- [ ] **Vie du fond** : caméra verrouillée, ou décor porté par une plaque, la
      vie du fond est écrite, sujets nommés, directions et vitesses distinctes.
- [ ] **Force du cadre** : chaque fixe se juge aussi comme un plan qu'on
      garderait au montage, sujet à l'échelle voulue, part vide assumée,
      mouvement à venir qui aura de quoi traverser. Une fixe conforme aux
      contrôles mais vide se recompose avant la vidéo ; sections Tenir une
      taille de plan et une composition, puis Le ratio vertical pour
      l'arithmétique, de `01-write-shot.md`. Constaté sur une session : fixe
      validée sur les six contrôles, rendu conforme, plan faible.

---

## Quand basculer

**Dès la première émission**, quand la surface a un slot première image et que
l'utilisateur n'a pas demandé le texte seul :

- la séquence a plus de deux plans,
- il y a un contrechamp ou un changement d'axe,
- le cadre est exact au sens de Décider l'ancrage, ci-dessus : au moins deux valeurs
  de composition imposées parmi angle, échelle, partage sol et ciel,
  profondeur, les valeurs positionnelles comptant, « au sol », « le sol au
  premier plan ». Constaté sur une session : un brief « très large au sol,
  14 mm, sol au premier plan », compté à une valeur, parti en texte, rendu à
  hauteur de capot et de face. Une case de storyboard fournie porte l'angle du
  sujet et le partage : elle compte comme valeurs, tout écart entre la case et
  le prompt s'annonce, règle 11, et comme une planche multi-cases n'est pas
  suivie case par case, la case se convertit en première image ou en keyframe,
  section Première et dernière image,
- le sujet est demandé sous un angle absent des références, de profil quand la
  photo le montre de trois quarts,
- un plan large montre un décor qu'aucune référence ne porte : sa plaque va
  dans le pool, sans condition de slot, section La texture photographique,
- le décor doit être vu sous plusieurs faces,
- la lumière change de façon contrôlée entre les plans.

C'est une décision, pas une question : elle s'annonce dans le self-eval. Si
l'utilisateur veut le texte seul, le texte porte les quatre valeurs de
composition, section Tenir une taille de plan et une composition de
`01-write-shot.md`, et le premier rendu observé compte comme premier rendu.

**Une exception.** Une scène qui reste dans un décor unique déjà porté par une
plaque validée, et dont ce qui dérive est la place des corps et la direction des
regards plutôt que le cadre lui-même, se traite par un diagramme de mise en place
et non par une planche d'images. Arbitrage complet dans `11-diagram.md`.

**En cours de route**, comme règle de sortie de la boucle de correction :

> À **N = 2 rendus observés en échec sur le même point**, premier rendu
> compris, appliquer la règle de sortie de `09-diagnose.md`. Ne pas ajouter deux
> relances au premier essai. Une proposition d'image n'est pas une image validée.

Une troisième reformulation coûte plus cher qu'une image fixe, et elle a moins de
chances d'aboutir, puisque le problème n'est pas la formulation mais l'absence
d'information. Cette règle est ce qui empêche la boucle de diagnostic de tourner
indéfiniment.

---

## Ce que ça ne règle pas

Le dire, pour ne pas vendre la méthode plus large qu'elle n'est.

**La physique du mouvement.** Contacts, transferts de force, fluides, poids,
occlusions restent à écrire dans le prompt de chaque plan. Une image de départ ne
dit rien de ce qui se passe entre deux frames. Voir `01b-motion-physics.md`.

**Le raccord de mouvement, si on n'ancre qu'un bout.** Deux plans partis chacun
d'une seule image restent deux générations indépendantes : il faut écrire l'état
de sortie du plan N et le même état comme entrée du plan N+1. La parade complète
est la première et dernière image, qui rend le raccord structurel plutôt que
textuel. Voir plus bas.

**Le plan-séquence traversant plusieurs espaces.** Un plan qui passe d'une loge à
un couloir puis à une scène ne se storyboarde pas plan par plan : il n'a qu'un
seul point de départ, et tout le reste doit être décrit. C'est le cas où la
méthode ne s'applique pas.

**La mise en place à plusieurs personnages, si on n'ancre pas.** Une image de
départ fige la disposition du plan qu'elle ouvre, elle ne dit rien de celle des
plans voisins. Quand la scène tient dans un décor et se couvre en plusieurs
générations, c'est le diagramme de mise en place qui porte positions, poses et
directions de regard : `11-diagram.md`.

**Le coût du choix.** Générer séparément plusieurs plans ancrés introduit
des raccords à monter. Un seul plan ancré sur sa première image, ou sur ses
deux extrémités, peut rester continu. L'ancrage n'impose donc pas une coupe.
Décider du découpage selon le brief avant de choisir les ancres.

---

## Règles techniques

- **L'image de départ impose le ratio.** Toute la planche doit donc partager le
  ratio de livraison. En référence simple, le ratio n'est pas imposé par
  l'image mais choisi par le modèle si le réglage reste en `adaptive` : le
  régler explicitement, détail dans `07-spec.md`, Ratios.
- **L'image de départ impose aussi l'étalonnage, et seulement sur ce qu'elle
  montre.** Tout ce que la caméra révèle hors du cadre de la fixe est inventé,
  palette comprise, avec le look par défaut du modèle ; une image de look dans
  le pool ne le rattrape pas. Deux conséquences : la fixe se contrôle contre
  l'image de look avant la vidéo, reflets au sol compris ; et la course caméra
  se dimensionne à ce que la fixe montre déjà, un travelling qui découvre la
  moitié d'une rue absente de la fixe change d'étalonnage en route. Constaté
  sur une session, non isolé par un test.
- **L'image fixe se vérifie avant la vidéo** sur les six contrôles à l'œil du
  bloc CADRE À FABRIQUER de `17-delivery.md`, puis sur sa force, item Force du cadre
  de la checklist ci-dessus. C'est l'état « cadre examiné » de la ligne État de
  `17-delivery.md`. Une image validée qui rend une vidéo fausse dès sa première frame
  désigne un slot ou un réglage, pas le prompt.
- **Première et dernière image d'un même plan doivent partager le ratio**, sinon
  la dernière est étirée pour coller à la première.
- **Laisser de l'air** dans la direction où le cadre doit voyager ou le sujet
  entrer.
- **Ne pas redécrire ce que l'image montre déjà.** Le prompt de plan porte le
  mouvement, pas l'apparence.
- **Nommer l'ancrage explicitement**, selon le slot employé. Sans token exposé :
  `Use the provided first frame as the exact first frame and continue forward
  from that moment.` Si le slot expose un token, garder ce token exact. En
  repli dans un pool compatible : `Use @image1 as the exact first frame and
  continue forward from that moment.` Cette demande sémantique n'active pas
  le rôle technique première image et ne garantit pas sa reproduction.
  Ne pas déduire un index de pool de la seule présence d'un slot, `10-syntax.md`.

- **Ne pas rejouer ce qui précède** l'image de départ, le dire au besoin : `Do
  not replay or recreate [ce qui s'est passé avant cette frame].`
- **Pour un contrechamp**, la cohérence tient au décor et à la lumière : les
  vérifier sur les deux fixes avant de générer, pas après.

---

## Forme d'un prompt de plan ancré

Court, parce que l'image porte l'apparence.

```
Use the provided first frame as the exact first frame and continue forward from
that moment.
Preserve [liste de ce qui est dans l'image et doit tenir, dont la direction de
lumière et le rendu photographique en une ligne]. Start with the source framing
and camera position, then perform only the camera movement below.
Do not replay [ce qui précède].

0-3 seconds: [première action, partant de l'état exact de l'image]
3-7 seconds: [action suivante, repartant de l'état laissé]
7-10 seconds: [payoff]; [état final spatial précis]

Camera: [un mouvement, son point d'arrivée]
Keep [invariants] from first frame to last.
Audio: [sons diégétiques]. No music.
[Queue de négations spécifique au plan]
```

Comparé à un prompt non ancré, tout le bloc d'identité et de décor disparaît :
l'image le porte. Ce qui reste est du temps, du mouvement et du son.

---

## Première et dernière image

Le mode qui pousse l'ancrage à son terme : on épingle les **deux bouts** du plan.
Le modèle ne génère plus que le chemin entre les deux. À utiliser dès que la fin
compte : révélation produit, avant après, morphing, transformation de personnage,
plan de marque, boucle.

Pour un ancrage technique, affecter les assets aux rôles ou slots première
et dernière image de la surface ; le texte accompagne ces réglages. Le patron
ci-dessous décrit le **repli sémantique en pool**. Il ne remplace pas les rôles
techniques et n'en garantit pas la précision.

```
@image1 is the first frame. It defines the opening composition, subject
position, pose, prop state, scene, and camera direction.
@image2 is the last frame. It defines the ending composition, subject position,
pose, prop state, scene, and camera direction.
@image3 defines <sujet>'s appearance and clothing. Do not change the first-frame
composition defined by @image1 or the last-frame composition defined by @image2.
<Une seule action continue>.
The video begins naturally from the first frame defined by @image1 and reaches
the last frame defined by @image2 after the continuous action.
Between the first and last frames, maintain continuity in <identité, structure et
possession des accessoires, disposition du décor, direction caméra>.
```

**Deux méthodes, et elles n'ont pas le même effet.** Déclarer le rôle des images
au niveau de l'asset, première frame et dernière frame, verrouille le ratio de
sortie sur celui de la première image et donne l'alignement le plus strict.
Passer les images en référence simple et les désigner dans le prompt laisse le
ratio libre, mais le rendu **ressemble** aux deux images sans les reproduire
exactement. Choisir selon que le cadre exact compte plus que le format.

Trois règles de forme :

- **Décrire chaque ancre séparément.** « @image1 and @image2 sont la première et la
  dernière frame » n'en lie aucune des deux.
- **Les références additionnelles ne remplacent jamais la composition des
  ancres.** Le dire explicitement, sinon un portrait de référence réécrit le
  cadrage.
- **Le prompt décrit le mouvement connectif, pas les deux scènes.** Les images
  disent déjà à quoi ça ressemble. Une phrase ciblée sur la transition bat une
  longue description.

### Choisir la paire de keyframes

C'est le 80/20 : la plupart des mauvais résultats viennent des images d'entrée,
pas du prompt.

- **Garder les deux frames proches** en sujet, échelle et composition. Aller d'un
  très gros plan à une vue aérienne large en cinq secondes demande au modèle
  d'inventer trop, et invite le warping.
- **Même ratio, idéalement même définition.** Un ratio différent étire la
  dernière frame, et rien dans l'interface ne prévient.
- **Lumière et couleur cohérentes**, sauf morphing jour nuit assumé. Un écart
  d'exposition entre les deux entrées produit du scintillement.
- **Garder les détails d'identité au même endroit** dans les deux frames, visage
  et produit surtout, pour que le chemin soit court.
- **Faire correspondre la durée à la distance.** Petit changement, clip court.
  Grosse transformation, clip plus long. Demander un grand changement en très peu
  de temps est la première cause de mouvement précipité.

### Vocabulaire de transition

Employer `smooth`, `continuous`, `gradual`, `seamless` pour décourager la coupe
franche, et **nommer le sujet qui doit rester constant** : « the same character »,
« the same product ».

### Quand ça warpe au milieu

Les deux frames sont trop éloignées. Deux parades : rapprocher le sujet en
position et en échelle dans les deux images, ou **ajouter une keyframe
intermédiaire** et générer A vers milieu, puis milieu vers B, puis assembler.

**Storyboard ou keyframes, la distinction est nette.** Une planche multi-cases
n'est pas suivie case par case : elle donne l'intrigue et le rythme, le modèle
garde son autonomie sur les détails. Des images séparées passées en keyframes
sont suivies de près. **Si l'alignement strict est requis, ce sont des keyframes,
pas une planche.**

Au delà de deux ancres, la séquence multi-keyframes fait le même travail :
`Use @image1 through @imageN as keyframes in this order`, puis l'état clé que
représente chaque image. Elles contrôlent l'ordre des étapes et les états clés,
pas la reproduction de chaque frame.

### Honnêteté sur l'arrivée

La dernière frame est **approchée, pas garantie au pixel**, surtout si les deux
images sont très différentes. Pour se rapprocher de la cible : raccourcir la
durée, simplifier le prompt sur la transition, rapprocher les deux compositions.

### Boucle propre

Faire de la dernière frame une copie de la première, et demander un mouvement
continu qui `returns to the starting composition`. Vérifier aussi vitesse,
direction et phase du mouvement, éclairage et audio aux deux extrémités.
Une image identique ne garantit pas une boucle sans saut de mouvement ou de son.

---

## Le raccord devient structurel

C'est ce que la première et dernière image change dans la doctrine d'ancrage.

Tant qu'un plan n'a qu'une image de départ, le raccord avec le plan suivant reste
textuel : il faut écrire l'état de sortie du plan N et le même état comme entrée
du plan N+1, et espérer. Avec deux ancres, **la dernière image du plan N est
littéralement la première image du plan N+1**. Le raccord n'est plus une promesse
écrite, c'est le même fichier utilisé deux fois.

Une planche de N cadres permet de préparer N moins un segments. Les ancres
partagées renforcent le raccord, mais chaque rendu reste à comparer aux deux
bords : pose, vitesse, phase et audio peuvent encore diverger. Le même fichier
d'entrée n'est pas une garantie de pixels identiques dans deux sorties.

Deux panneaux de storyboard peuvent servir directement de paire d'ancres : le
modèle génère le beat qui les relie.

---

## Chaîner sans nouvelle image

Variante utile quand la continuité prime sur le contrôle du cadre : extraire la
**dernière image** du plan validé et la passer comme première image du plan
suivant. L'état de départ est alors réel, pas mémorisé.

Les deux méthodes se combinent. Cadres clés dessinés en amont pour les plans qui
doivent être justes, dernière image extraite pour les continuations.

## Les mots de goût

**Zéro adjectif de goût.** « cinematic », « premium », « dynamic » ne dirigent
ni cadre ni caméra ; ce qu'ils déplacent, c'est le registre de rendu, `05`,
ce qui est une raison de plus de ne pas les écrire. Une décision les
remplace : angle, source de lumière, étalonnage nommé. Le guide officiel 2.0
recommandait des tags de style et d'ambiance en fin de prompt, « cinematic
texture, film grain », « tense suspense », et les exemples du guide ModelArk
2.5 en écrivent encore, « IMAX large-format feel », « rich cinematic color
grading » ; ce skill s'en écarte, divergence assumée, et la page Dreamina
2.5 du 18 août 2026 va dans son sens : « make it emotional and beautiful »
ne donne rien à mettre en scène. Un genre nommé, « nature documentary »,
n'est pas un adjectif de goût : il désigne une grammaire.
Un nom de réalisateur n'est pas un adjectif de goût : c'est un brief caméra
compressé, à déplier en clauses sourcées, `13`, jamais à supprimer ni à
traduire en émotion.
