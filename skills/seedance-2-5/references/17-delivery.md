# 17 Livrer le résultat

Lire avant toute livraison au format complet ou avec un cadre à fabriquer.
Le noyau `SKILL.md` garde les cinq questions et le contrôle relationnel ; les
appliquer avant ce gabarit. Les instructions utilisateur et les sorties sans
prompt restent prioritaires. Ce fichier est l'autorité du format développé.

## Format de sortie

Pour une émission de prompt, toujours ces trois blocs, plus la ligne de durée,
dans cet ordre, rien d'autre. La simple coupe au montage suit le parcours de `15-camera-techniques.md`.
**« Texte seul » exclut la fabrication d'images ou de vidéos ; il ne retire
pas à lui seul ce format de réponse.** Une demande explicite « seulement le
prompt », « prompt sans explication » ou un format imposé prime en revanche :
faire le contrôle en interne et livrer seulement le contenu demandé. Dans un
prompt chinois sans préambule, garder les associations nom-token dans le bloc.
Une question technique sans demande de prompt reçoit une réponse directe.
Trois exceptions. **La première** : un bloc QUESTIONS ouvre la sortie quand la
liste fermée de `00-quickref.md` en produit, et il est omis sinon, ce qui est le
cas normal. **La deuxième** : quand l'ancrage image est décidé, `05-anchoring.md`, Décider l'ancrage,
compteur à 2 lorsque la bascule est retenue, ou cadre jugé faible sur un rendu
conforme **et recomposition demandée**, `09-diagnose.md` : un bloc CADRE À
FABRIQUER prend place entre DURÉE et SELF-EVAL, parce que
le prompt vidéo dépend d'une image qui n'existe pas encore et qu'un prompt
d'image logé dans un préambule libre se perd. Absent dans tous les autres cas.
**La troisième** : en verdict MAUVAIS PLAN, PROMPT FINAL devient REDÉCOUPAGE et
POINTS DE RUPTURE est omis, table des verdicts ci-dessous.

**Un seul en-tête PROMPT FINAL, toujours.** Quand la réponse demande plusieurs
générations à assembler au montage, `13-director.md`, elles sont numérotées
**dans** ce bloc unique, `Génération 1 sur 3`, chacune dans son propre bloc de
code avec sa durée à générer. Plusieurs en-têtes PROMPT FINAL cassent tout ce
qui lit la sortie, l'œil comme le script. Constaté le 9 septembre 2026.

```
QUESTIONS                    <seulement si la liste fermée en donne, sinon omis>
<une à quatre questions, plafond de `00-quickref.md`, une ligne chacune, sur ce
 modèle exact, sans autre
 ponctuation de liaison : "1. <la question> Défaut appliqué : <X>." Le défaut
 est la valeur, pas son argumentaire ; la conséquence d'un autre choix va dans
 les points de rupture, pas ici. Sauf deux demandes qui se contredisent, qui
 s'écrit "je m'arrête ici" suivi des deux demandes, et remplace tous les blocs
 suivants. `00-quickref.md`, Questions de préparation>

DURÉE
<entier 4 à 30 s>, ou "héritée de la source, non réglable" selon le mode ;
plus le slot de l'image de départ en I2V, première image ou pool ; plus le
ratio à régler explicitement, jamais laissé en `adaptive`, dès que le format
de livraison compte en texte vers vidéo ou en référence

CADRE À FABRIQUER            <seulement en ancrage>
<le prompt d'image, anglais, un seul bloc, au ratio de livraison, sans le
 style graphique d'aucune carte ; puis les contrôles à l'œil : texture, angle, échelle,
 partage sol et ciel, profondeur, ratio, qui vérifient la conformité, plus la
 palette comparée à l'image de look quand il y en a une ; puis le
 jugement de force du cadre, `05`, item Force du cadre. Le prompt vidéo
 ci-dessous ne se lance qu'après les deux, et l'image va dans le slot déclaré
 en DURÉE>

SELF-EVAL
<les cinq questions, une ligne chacune, chacune citant sa clause>
<Corrigé : la liste de ce qui a été changé avant émission, ou "rien">
<Sources : seulement quand un réalisateur, un film ou une séquence a été
 traduit ; auteur, date, lien, et les traits supprimés avec leur raison>
<Reporté : sur toutes les émissions. Ce qui a été gardé de l'émission
 précédente sans être réexaminé, ou "première émission", puis toujours
 "Échecs sur ce point : N". "rien" est une réponse valide, mais elle signifie
 que tout a été relu, pas que rien n'a été copié. À N égale 2, pas de troisième
 reformulation aveugle du même défaut : la suite se choisit selon les preuves,
 les entrées disponibles et les instructions du projet, qui peuvent exclure la
 bascule d'ancrage ou imposer le texte seul, `09-diagnose.md`>
<État : prompt rédigé ; cadre examiné : oui ou non, c'est à dire une image
 fixe du cadre validée à l'œil sur texture, angle, échelle, partage,
 profondeur, ratio, et palette contre l'image de look, saturation des reflets
 comprise ; une fixe plus saturée que le look devient le look du plan ;
 rendus contrôlés : R regardés, dont N ratés sur ce
 point. Trois états
 distincts, et le self-eval n'atteste que le premier>
<Verdict>

PROMPT FINAL
<si prompt chinois avec références : tableau de repérage selon `04`, dans la
 langue de la conversation, hors du bloc de code à copier>
<texte dans la langue retenue, corrections déjà appliquées, un seul bloc collable ; un bloc
 par plan, numéroté, quand une séquence ancrée a plusieurs plans. Les blocs
 CADRE À FABRIQUER correspondants restent groupés à leur place unique, entre
 DURÉE et SELF-EVAL, numérotés dans le même ordre que les plans>

POINTS DE RUPTURE
<2 à 4 symptômes visibles, plus l'invite à rapporter>
```

### Réglages et langue

Pas de bloc de réglages supplémentaire : mode, résolution, audio et ordre des
uploads ne se répètent pas à chaque sortie. Trois exceptions dans DURÉE :
la durée issue du découpage ; les paramètres hérités ou le ratio à régler
explicitement ; le slot première image ou pool en I2V.

Les limites de fiabilité vont dans POINTS DE RUPTURE. **Émettre uniquement le
prompt corrigé**, jamais un brouillon suivi de retouches à appliquer soi-même :
une seule version finale, dans le format de réponse défini ci-dessus.
Choisir la langue selon [10-syntax.md](10-syntax.md), Langue et
dialogue : demande explicite, sinon langue du prompt fourni à améliorer,
sinon anglais par défaut. Garder les répliques dans leur langue demandée et
les tokens intacts. Une langue acceptée n'est pas une langue supérieure.
Ce choix porte sur le texte à coller, pas sur les en-têtes du format de sortie :
garder notamment SELF-EVAL et PROMPT FINAL tels quels. Les explications restent
dans la langue de la conversation, sauf demande contraire.

### La ligne Reporté

**Reporté** nomme ce qui a été gardé sans relecture, et porte le compteur
de `09-diagnose.md`. « Rien » signifie que tout a été réexaminé, pas que rien n'a été
copié. À la première émission : « première émission » et `N = 0`.

Puis un verdict parmi deux, jamais trois :

| Verdict | Sens |
|---|---|
| **PRÊT** | Les corrections sont intégrées. Le texte du bloc de code sous PROMPT FINAL se copie tel quel ; le tableau de repérage reste hors du prompt |
| **MAUVAIS PLAN** | Aucune correction ne sauve celui-ci. Le découpage, la durée ou le mode sont mal choisis. On ne livre pas de prompt, on redécoupe : le bloc PROMPT FINAL devient REDÉCOUPAGE, un plan par ligne avec sa durée et son mode, et POINTS DE RUPTURE est omis |

« À RESSERRER » n'est plus un verdict, c'est une étape interne. Un prompt qui
mérite ce mot repart en réécriture et ressort corrigé, ou bascule en MAUVAIS PLAN
si le défaut tient au découpage plutôt qu'à la formulation.

## Points de rupture

Lister **deux à quatre symptômes visibles**, spécifiques au plan, en une
ligne chacun. Partir du risque de la question 5 et décrire ce que l'œil ou
l'oreille constatera, sans demander de revérifier toutes les promesses.

La répartition du travail explique la forme : **le rédacteur tient le prompt,
l'utilisateur a les yeux.** Lui demander de contrôler point par point ce qui
avait été promis lui fait refaire un travail de mémoire que le texte fait
mieux, et l'éloigne du seul apport qu'il est seul à avoir, le jugement visuel
immédiat. Une formulation utile nomme donc une chose qu'on voit ou qu'on ne
voit pas en une seconde, sans relire le prompt.

| Formulation à éviter | Formulation utile |
|---|---|
| La voix off est-elle bien attribuée au bon personnage ? | Les lèvres du second personnage bougent pendant la réplique du premier |
| Le jeu est-il dirigé ? | Elle hoche la tête en boucle pendant le silence |
| La caméra respecte-t-elle la clause de maintien ? | Le plan finit plus serré qu'il n'a commencé |
Une panne possible n'établit pas sa cause : écrire « le cadre coupe le sujet »,
pas « faute de première image verrouillée » sans essai qui l'établit.

```
POINTS DE RUPTURE
- <symptôme visible 1, en une ligne>
- <symptôme visible 2>
- <symptôme visible 3>
Dis lequel se produit, ou décris ce que tu vois, pour cibler le contrôle suivant.
```

Exemple : « Il articule pendant la voix off » est un symptôme ;
« vérifier l'attribution de la voix » est une tâche à ne pas déléguer au spectateur.

**Un symptôme rapporté déclenche la classification de `09-diagnose.md`.**
Si une correction du texte est demandée et justifiée, l'appliquer et livrer le
PROMPT FINAL complet selon la `SKILL.md`, Autorité et lecture. Si le texte est déjà clair et compatible,
conserver ses clauses et cibler le contrôle des entrées ou de l'exécution ;
ne pas inventer une cause pour imposer une réécriture. Un diagnostic seul
reste un diagnostic, sans nouveau prompt.

Archiver le prompt à côté du rendu. Un journal de prompts vaut plus qu'un dossier
de clips réussis qu'on ne sait pas reproduire.
