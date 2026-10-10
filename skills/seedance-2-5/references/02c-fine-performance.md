# 02c Affiner le jeu sans le surcharger

Ouvrir pour une demande de microexpressions, de retenue, de dissimulation,
de réaction fine ou de correction locale du jeu. `02a-perform.md` reste
l'autorité pour intention, silence, regard, écoute et dialogue ; cette fiche
ajoute la **reprise de contrôle** et la **trace finale**.

**Statut : hypothèse de prompting.** Adaptation du chapitre 4 de « Film and
Television Script Microexpression Performance Enhancement », fourni par
l'utilisateur, auteur et date de publication inconnus. Aucun test vidéo
n'est fourni. « Microexpression » désigne ici une direction de jeu visible,
pas une inférence psychologique sur une personne réelle ni une mesure clinique.

## Sommaire

- Définir ce qui peut changer
- Fuite, contrôle, trace
- Régler la densité et la visibilité
- Exemple de jeu retenu
- Corriger après un rendu

## Définir ce qui peut changer

Dans une révision, relever le personnage et le passage visés. Le reste du
prompt est le contexte à préserver : identité, dialogue, décor, lumière,
durée, ratio, caméra et actions restent tels quels sauf demande contraire.
Intégrer la correction au prompt final complet, selon `SKILL.md` ; ne pas
renvoyer à l'utilisateur des annotations à recoller.

Prendre les motivations et connaissances dans le brief. Une photographie
porte l'apparence, pas la personnalité ni l'état psychologique. Ne pas
faire réagir le personnage à une information qu'il n'a pas encore reçue.

Ne pas reprendre les validations A0-A6 / B0-B5, le plan facial de 15 secondes
par défaut, ni les générations d'image et vidéo de la source. Le mode,
l'ancrage et les questions suivent les routes `05` et `00` de `SKILL.md`.

## Fuite, contrôle, trace

Pour un personnage qui **cherche à contenir** ce qu'il éprouve, préciser :

1. L'état qu'il essaie de maintenir, avec la tâche de `02a`.
2. Le stimulus déjà présent qui provoque une fuite observable.
3. L'effort visible de reprise de contrôle.
4. La trace qui persiste dans l'état final malgré cet effort.

Ce sont des fonctions de jeu, pas quatre beats obligatoires. Les regrouper
selon la durée. Ne pas imposer de dissimulation à un personnage dont le brief
demande une réaction ouverte, un éclat de joie ou un effondrement.

Le déclencheur peut être une **absence qui se confirme** : il vérifie la
même entrée et personne n'arrive. Le rendre lisible dans ce qui existe
déjà, sans inventer un bruit, une notification ou un figurant. Appliquer
l'arbitrage sans activité d'objet prévue de `02a`, La partition d'un silence ;
ne pas créer une deuxième règle d'activité dans cette fiche.

Exploiter un contraste entre canaux si le brief le justifie : le sourire
social tient pendant que l'inspiration se coupe, ou le corps reste droit
alors que le regard cherche une échappée. Un canal tient, l'autre change.
Ne pas demander à toutes les zones du visage de bouger simultanément.

## Régler la densité et la visibilité

**Choix de rédaction, pas limite du moteur :** viser un changement principal
de regard ou de visage par beat, accompagné si utile d'une seule réponse
corporelle. Garder les cibles, la vitesse du geste et sa sortie ; couper
l'inventaire anatomique et les tremblements ajoutés pour « faire subtil ».

| Ce que le cadre montre | Canal de jeu à privilégier |
|---|---|
| Corps entier, visage peu lisible | Appuis, orientation, geste interrompu, distance |
| Plan poitrine, yeux visibles | Regard, respiration, épaules, mâchoire |
| Gros plan | Cible du regard et une ou deux zones lisibles du visage |
| Visage caché ou hors champ | Corps ou voix déjà présents, sans inventer une réaction faciale visible |

Ne pas changer la taille du plan pour faire entrer une liste d'expressions.
La retenue se règle en amplitude et en durée, pas en « imperceptible » ou
en suppression de toute activité. Appliquer `02a`, Accorder le jeu au cadre,
puis le retour du regard quand les yeux sont visibles.

Pendant une réplique, conserver exactement les mots et leur langue. Placer
le jeu dans la clause de parole, `02a`, et éviter une fermeture des lèvres
ou une déglutition qui empiète sur les mots prononcés. Déplacer ce geste
dans la préparation ou l'atterrissage déjà prévus, sans changer le dialogue.

## Exemple de jeu retenu

Fragment pour un plan poitrine de 6 s, une femme qui attend devant l'entrée
visible du hall et cherche à rester digne. Aucun nouvel incident n'est requis.
Le format, les références et la caméra appartiennent au prompt complet.

```text
0-2 seconds: she is checking whether anyone is finally arriving; her eyes
move from the near edge of the hall entrance to its far edge at eye level.
2-4 seconds: the entrance remains empty; she realises the wait will continue.
Her inhale catches once and her jaw tightens while she watches the entrance.
4-6 seconds: she slowly releases that breath, trying to regain composure.
Her eyes return to the near edge of the entrance;
the tension in her jaw remains. She stays silent throughout.
```

La trace finale est la mâchoire restée tendue. Ne pas ajouter un sourire de
résolution, un effondrement ou un regard au sol si le brief ne les demande pas.
Les temps sont ceux de cet exemple, pas un gabarit à imposer à tout plan.

## Corriger après un rendu

Réaction trop forte : réduire l'amplitude de **la réponse ciblée**. Réaction
illisible : modifier sa visibilité ou sa durée. Jeu qui revient à zéro :
reporter la trace finale. Choisir une seule variable après observation,
`09-diagnose.md`, et livrer le prompt complet corrigé.

Un texte cohérent ne prouve pas un jeu réussi : garder la distinction entre
prompt rédigé, cadre examiné et rendu contrôlé du self-eval.
