---
name: seedance-2-5
description: >-
  Écrit et débogue les prompts Seedance 2.5, modèle vidéo ByteDance de 4 à 30
  s, audio natif, 50 références, édition et extension, sur Jimeng, Dreamina
  ou Doubao. Grammaire native, beats minutés, adressage @image1,
  self-eval correctif, un seul prompt final à langue adaptée. Déclencher dès que
  l'utilisateur mentionne Seedance, Jimeng, Dreamina, Doubao, un prompt vidéo
  IA, un plan à générer, une référence image vidéo ou audio, un dialogue à
  faire prononcer, une maquette blanche, un fond vert, un timestamp, une
  extension ou une édition de clip, même sans dire le mot prompt. Déclencher
  aussi sur un rendu raté : dérive d'identité, caméra ignorée, action absente,
  objet dupliqué, sous-titre parasite, mauvaise langue, audio faux, mise en
  place fausse, optique qui dérive, regard vitreux, voix qui change, plan
  large rendu serré, silence joué en robot, regard au sol. Déclencher aussi
  dès qu'un réalisateur, un film ou une séquence est cité comme style de mise
  en scène, John Woo ou Michael Bay par exemple.
---

# Seedance 2.5

Écrire ou corriger un prompt pour une **interface web**, ou diagnostiquer un rendu.
Livrer du texte à coller et les seuls réglages nécessaires, sans JSON, SDK ni champs API.
Aucun tiret cadratin dans la sortie, titres compris.

## Autorité et lecture

La demande et les instructions du projet priment. Une fiche complète ce protocole
dans son seul périmètre ; un catalogue externe ne remplace ni le mode ni la sortie.
Annoncer tout arbitrage, retrait d'un élément demandé, changement du nombre de références
et événement ajouté au brief ; sinon retirer cet ajout. Ne rien modifier hors périmètre.
Les limites du moteur portent leur source ; les constats et hypothèses leur niveau
de confiance. Une convention de mise en scène ne devient pas une limite native.

À chaque émission, relire le présent noyau et appliquer ses contrôles. Ouvrir les
fiches déclenchées **avant** la décision concernée ; lire leurs sections utiles,
sans charger tout le corpus. Les routes se combinent, sans plafond arbitraire.
`00` n'est plus une seconde lecture systématique : elle prépare un brief incomplet.
Les chemins complets sont dans la table ; les numéros employés ensuite y renvoient.

## Choisir la tâche

| Situation | Parcours et résultat |
|---|---|
| Aucun asset | T2V : squelette complet |
| Image de départ | I2V : slot déclaré, ou pool avec token exact et rôle ; diriger ce que la fixe ne montre pas |
| Assets d'inspiration ou sujets à verrouiller | Référence : manifeste, rôles, exclusions et conflits arbitrés |
| Récit de 10 à 30 s | Long format : beats, états reportés et continuité |
| Vidéo finie à conserver, portion à changer | Édition : maître unique, portée, préservation ; durée et ratio hérités, `06`–`07` |
| Vidéo finie à prolonger | Extension : frame frontière puis action nouvelle ; ratio hérité, `06`–`07` |
| Passage manquant entre deux clips | Transition : sources, mécanisme, départ et arrivée, `06` |
| Images à assembler en film | Assemblage : rôles, ordre, mouvement, rythme et audio, `06` |
| Deux clips déjà raccordables | Montage : indications de coupe et raccord audio, `15` ; aucune durée à générer ni PROMPT FINAL |
| Retour sur rendu ou audit du texte seul | Diagnostic : preuve et trois classes, `09` ; pas de nouveau prompt non demandé |
| Question technique seule | Réponse directe et vérifiée, sans gabarit de génération |
| Modifier le skill | Maintenance : lire `14` avant modification |

## Routes de lecture obligatoires selon le besoin

| Déclencheur | Fiche | Contrôle attendu |
|---|---|---|
| Donnée de brief nécessaire inconnue | [00 Préparation](references/00-quickref.md) | Question autorisée, défaut annoncé ou contradiction bloquante |
| Écrire un plan | [01 Plan](references/01-write-shot.md) | Taille, géométrie, caméra et lumière compatibles |
| Mouvement, manipulation, impulsion, fluide, tissu, jambe ou véhicule : ce que fait le corps ou la machine | [01b Physique](references/01b-motion-physics.md) | Contacts, cause, axe, appuis, trajectoire et circulation applicables |
| Véhicule/coureur/projectile sujet, caméra portée, plan nerveux ou rendu mou : ce que le cadre donne à voir de la vitesse | [01c Action](references/01c-action.md) | Vitesse perçue et distances relatives ; aucun quota d'événements |
| Combat à deux | [01d Duel](references/01d-duels.md) | Attaque, réponse, conséquence et styles ; avec `01b` |
| Personnage, silence, dialogue ou écoute | [02a Jeu](references/02a-perform.md) | Tâche, canal perceptible, activité et issue |
| Jeu mort, visage figé ou direction ignorée | [02b Échecs de jeu](references/02b-perform-failures.md) | Symptôme localisé et niveau de preuve ; avec `09` |
| Retenue, microexpression, dissimulation ou correction locale du jeu | [02c Jeu fin](references/02c-fine-performance.md) | Fuite, contrôle, trace finale ; avec `02a` |
| Plusieurs changements, multi-plans, récit, vlog ou combat de groupe | [03 Séquence](references/03-sequence.md) | Beats, ellipses, états et continuité ; groupe : avec `11`, sans gabarit de duel |
| Identité, produit, décor, voix ou références d'une série | [04 Références](references/04-references.md) | Manifeste, exclusions, report ; en chinois : repérage des noms et tokens |
| Cadre exact, plus de deux plans, contrechamp, angle/face/lieu absent, état futur, raccord lumineux distant, optique ou storyboard | [05 Ancrage](references/05-anchoring.md) | Décision d'ancrage, slot/pool, cohérence des fixes et exceptions |
| Édition, extension, pont ou assemblage | [06 Clip existant](references/06-edit-extend.md) | Source maître, intention, portée et frontières ; avec `07` |
| Limite, ratio, paramètre hérité, fichier, visage réel, accès ou question juridique | [07 Spécifications](references/07-spec.md) | Capacité vérifiée selon le mode et la surface |
| Besoin d'un patron ; circulation à contrôler | [08 Patrons](references/08-templates.md) | Patron pertinent seulement ; véhicule : champs applicables du patron 19 |
| Audit, défaut rapporté, compteur ou réémission après rendu | [09 Diagnostic](references/09-diagnose.md) | Attendu, observé, clause, classe et contrôle ; cause inconnue si non établie |
| Token, langue, son, réplique, sous-titre ou bloc | [10 Syntaxe](references/10-syntax.md) | Adresse littérale, langue choisie et attribution audio |
| Mise en place à figer ; trois personnages ou plus | [11 Diagramme](references/11-diagram.md) | Corps, décor, caméra et regards dans un même espace |
| Clôture, négation, verrou positif ou conflit | [12 Contraintes](references/12-constraints.md) | Chaque verrou sert le brief courant |
| Réalisateur, film ou séquence cité | [13 Réalisation](references/13-director.md) | Traits sourcés traduits en décisions visibles, aucun motif ajouté par défaut |
| POV, révélation, raccord masqué, match cut ou effet temporel/spatial | [15 Caméra](references/15-camera-techniques.md) | Porteur, présence et états de part et d'autre du raccord |
| Mécanisme, projection, propagation ou retour d'objet | [16 Effets](references/16-effects-mechanisms.md) | Liaisons, causalité, manifestations comptées et état final ; avec `01b`–`03` |
| Livraison au format complet ou image à fabriquer | [17 Livraison](references/17-delivery.md) | Gabarit, champs de preuve et symptômes ; lire avant émission |
| Maintenance seulement | [14 Maintenance](references/14-maintenance.md) | Autorités, provenance, cas réels et non-régression |

## Préparer sans arbitrage silencieux

Identifier mode, durée, ratio, assets/rôles/tokens, langue, contraintes de cadre
et état de la série. Si une donnée nécessaire manque, ouvrir `00` : la liste
fermée des questions, son plafond et ses défauts restent applicables, sous réserve
des instructions utilisateur. Deux demandes incompatibles arrêtent l'émission.
Les décisions de décor, lumière, cadrage ou goût se prennent et s'annoncent.

Avant de composer, vérifier si les références portent la géométrie demandée.
Un cadre exact, au moins deux valeurs de composition, un angle absent ou un
contrechamp déclenche `05`, Décider l'ancrage ; une taille de plan seule ne suffit pas.
Le diagramme peut porter les relations dans un décor déjà validé. Le texte seul
demandé reste du texte ; annoncer le risque sans prétendre qu'une image le résout.

## Le squelette

Sélectionner seulement les sections utiles ; une action de deux secondes n'impose
ni timeline ni longue continuité. Sujet et action d'abord, puis environnement,
style visuel, caméra et audio dans le beat. Détails et états : `03`.

```text
FORMAT        durée, ratio, plan unique ou coupes, vitesse
RÉFÉRENCES    rôle, exclusion et verrou de voix de chaque asset
ÉTAT INITIAL  corps, objets, décor, caméra
MISE EN PLACE relations spatiales, même pour un personnage seul ; cibles hors champ situées
BEATS         chacun reprend l'état précédent
CAMÉRA        taille géométrique, hauteur/angle, mouvement, arrivée, pas et maintien
CONTINUITÉ    identité, compte, orientation, costume et invariants
AUDIO         ambiance globale ; événements et répliques dans leurs beats
ÉTAT FINAL    position des sujets, objets et caméra
CIRCULATION   seuls champs applicables, sans trafic inventé
CONTRAINTES   pannes plausibles du plan ; aucun interdit de l'effet demandé
```

Écrire la ligne FORMAT dans le prompt même si le réglage existe dans l'interface.
Continuité et état final sont distincts. Une carte porte [Eyelines] ; ne pas
réécrire le même fait en prose. Chaque prompt contient ses propres données :
le moteur n'a pas la mémoire de la série, le rédacteur conserve celle du fil.
Recopier ses identités, voix et états verrouillés sans reformulation.
Repère : 150–300 mots pour 30 s, sans plafond universel ; garder toutes les clauses
nécessaires. Couper les redondances, pas le brief. Limite réelle : `07`.

## Checklist pré-vol

À appliquer à chaque émission, même après plusieurs demandes dans le même fil.
Chaque contrôle garde son déclencheur ; une pièce présente ne prouve pas une scène
cohérente. Les justifications et méthodes vivent dans les fiches indiquées.

- [ ] Questions de `00` traitées avant rédaction ; bloc omis si aucun trou ; contradiction non arbitrée : arrêt.
- [ ] Adresse de surface établie ; token exact, espaces et casse conservés ; aucun alias inventé, `10`.
- [ ] Ligne de format présente : durée, ratio, plan unique ou coupes.
- [ ] Ratio effectif vérifié au paramètre ou à la source selon le mode ; le texte seul ne le règle pas, `07`.
- [ ] Sujet et action principale énoncés tôt et clairement ; caméra et sujet dans deux clauses distinctes.
- [ ] Présence du hero bornée aux plans concernés ; ne pas le réintroduire dans un insert qui l'exclut, `01`.
- [ ] Chaque référence dit usage et exclusion ; en chinois, noms-token et tableau selon `04`.
- [ ] Conflits entre références et entre prose et références arbitrés explicitement.
- [ ] Un changement principal par beat, état précédent repris ; duel à deux : chaîne causale, sans huit phases forcées, `03`–`01d`.
- [ ] Impulsion : porteur, cause, axe et appuis ; mouvement subi et compensation compatibles, sans latence arbitraire, `01b`.
- [ ] Série : reprendre le manifeste précédent ; chaque suppression est déclarée avec sa raison ; un angle absent ne supprime pas une identité, `04`.
- [ ] Rythme conforme au brief ; attente et approche lente conservées ; aucun quota d'événements tiré de `01c`.
- [ ] Trajets caméra/sujet compatibles ; chaque distance nomme ses deux référents, `01c`.
- [ ] Sujet entrant : origine, distance et vitesse nommées, `01b`–`03`.
- [ ] Véhicule : seuls champs applicables ; faces, marche et déplacement relatif distingués ; réaction du trafic réévaluée, `01b`–`08`.
- [ ] Chaque son, véhicule, passant ou effet ajouté au brief est déclaré dans Corrigé/arbitrages, sinon retiré.
- [ ] Durée imposée : lisibilité des segments contrôlée ; 1,5 s reste un repère, sans suppression ni allongement silencieux, `03`.
- [ ] Aucun goût ni repère de découpage présenté comme limite moteur ; source et confiance explicites.
- [ ] Objets importants situés à la fin ; reprise, détachement, projection ou transformation causés, `16`.
- [ ] Clôture de continuité distincte de l'état final, `03`.
- [ ] Un mouvement caméra principal, taille initiale/finale, hauteur/angle, pas et arrivée ; POV/raccord contrôlé dans `15`.
- [ ] Multi-plans : taille, angle, optique, lumière et look redéclarés par plan, inserts compris, `01`–`03`.
- [ ] Décor non montré en plan large : plaque et texture examinées selon `05` ; aucune négation du registre de rendu.
- [ ] Taille demandée traduite en géométrie visible, air et maintien ; jeu au canal accessible du cadre, `01`–`02a`.
- [ ] Valeurs de composition comptées, brief ou rédaction ; à deux ou plus, décision selon `05`, avec priorité au texte seul demandé.
- [ ] Composition calculée contre le ratio : éléments aux bords et échelle compatibles ; cadre conforme mais faible signalé, `01`–`05`.
- [ ] Angle de vue imposé par brief, storyboard ou première image conservé ; tout écart déclaré, `01`.
- [ ] Personnage : jeu/tâche/registre avant effets et caméra ; autant de mots que l'effet ou décor le plus décrit, `02a`–`02b`.
- [ ] Personnage : silence dirigé, changement d'état et écoute si plusieurs ; correction locale et trace finale selon `02c`.
- [ ] Silence : tâche et changement dans le canal perceptible ; yeux dirigés s'ils sont visibles, sans changer le cadre, `02a`.
- [ ] Silence >3 s : partition causée de 1,5–3 s, pensée indirecte sans guillemets, issue distincte ; alternative sans objet de `02a`.
- [ ] Réalisateur/film/séquence : traits sourcés, auteur/date/lien ; décisions visibles selon brief, suppressions déclarées, `13`.
- [ ] Aucun adjectif d'émotion nu ni biographie invisible ; comportement filmable. Les mots de goût deviennent des décisions, `02a`–`05`.
- [ ] Mise en place, même un personnage seul : corps, chaussée/objet, entrée, caméra et cibles coexistent ; reprojeter à chaque coupe/arc.
- [ ] Audio séparé : ambiance, sons d'action, dialogue, musique ou silence ; événements dans leur beat, `10`.
- [ ] Voix recopiées mot pour mot depuis les blocs verrouillés, sans synonyme, `04`–`10`.
- [ ] Négation dessinable remplacée par l'état propre ; garder les négatifs documentés dont « No subtitles », sauf effet voulu, `12`.
- [ ] Queue relue contre le brief ligne par ligne ; ne pas interdire ralenti, coupe, zoom, musique, texte, tremblement, flare ou grain demandés.
- [ ] Aucun « comme avant » ni renvoi au plan précédent dans le prompt ; formulations et états autonomes, `04`.
- [ ] Édition : maître unique, portée et préservation explicites, `06`.
- [ ] Première et dernière image au même ratio, `05`.
- [ ] Référence de placement au ratio de livraison ; autre ratio : contenu seul, pas cadre, `04`.
- [ ] Composition exacte : bon rôle de première image si slot disponible ; sinon pool et risque déclaré, `05`–`07`.

### En réémission

- [ ] Chaque clause conservée réexaminée, pas seulement les clauses modifiées.
- [ ] La demande nouvelle possède une clause retrouvable dans le prompt livré.
- [ ] Après rendu observé, une seule variable change par relance pour interpréter le résultat, `09`.
- [ ] Compteur réel tenu : à N = 2 sur le même défaut, lire la règle de sortie de `09` avant toute relance.

## Le self-eval, obligatoire

Passer les cinq questions après la checklist, à chaque prompt. Corriger les lacunes
matérielles avant livraison, dans le périmètre autorisé. Sans lacune, « rien » est valide.

1. **Intention.** Qu'est-ce que le spectateur doit voir arriver ? Le prompt sert-il encore cette intention ?
2. **Le plan tient-il tout seul ?** Retirer les clauses techniques : reste-t-il une scène avec début, changement et fin ? Reconstruire une même disposition du corps, décor, caméra et cibles.
3. **Le jeu existe-t-il ?** Silence dirigé, état qui change, écoute si plusieurs ; citer tâche et manifestation dans le canal perceptible (`02a`). Sans personnage : « sans objet ». Ne pas exiger des yeux hors cadre.
4. **Que faut-il couper ?** Clause inutile, héritée ou contraire au brief. « Aucune » est valide ; aucun défaut inventé pour produire une correction.
5. **Quel résultat indésirable le texte autorise-t-il encore ?** Construire un contre-exemple compatible, ou citer deux clauses contradictoires. Corriger la lacune. Un défaut qui viole une consigne claire est un risque d'exécution, sans synonymes empilés ni cause inventée ; nommer l'observation ou l'essai utile.

Chaque réponse cite la clause qui la porte ou son absence, en une ligne. Sans clause
aux questions 1–3 (sauf 3 sans personnage), le contrôle échoue. La citation atteste
le texte, jamais l'image. Un contre-exemple doit respecter les clauses : « le modèle
pourrait les ignorer » n'en est pas un. Accepter le témoin cohérent sans retouche.
Sur un rendu, suivre **attendu → observé → clause/absence → classe → contrôle**, `09` :
consigne absente, ambiguë/contradictoire, ou présente mais non respectée.
Le self-eval prouve « prompt rédigé », pas « cadre examiné » ni « rendu contrôlé ».
Une cause non établie reste inconnue. L'ancrage suit les entrées, indices et choix du projet.

**Les deux façons de rater ce contrôle sont symétriques.** Inventer un défaut
pour produire une correction en est une, et « rien » comme « aucune » sont des
réponses valides sur un texte sain. Tamponner en est l'autre : le mode de
défaillance constaté est cinq émissions consécutives, cinq PRÊT, zéro réserve,
l'erreur étant trouvée par l'utilisateur à chaque fois. Un self-eval qui ne
produit jamais de réserve ne mesure rien. Quand plusieurs prompts d'affilée
sortent sans une seule lacune matérielle, c'est la passe qu'il faut réexaminer
avant le texte, sans convertir un texte sain en défaut : le témoin cohérent de
`14` doit pouvoir passer sans retouche. Constaté sur une session, non isolé par
un test.

## Livrer

La langue du prompt suit `10` : demande explicite, sinon langue du prompt à améliorer,
sinon anglais. Répliques dans leur langue demandée ; noms et tokens littéraux.
Explications, self-eval et tableau dans la langue de conversation. En chinois,
les associations nom-token restent dans le prompt ; tableau de repérage selon `04`.

**« Texte seul »** exclut les médias générés, sans retirer le format complet.
**« Seulement le prompt »**, « sans explication » ou format imposé : contrôle interne
puis seule sortie demandée, avec associations nom-token conservées.
Sinon, lire `17` : QUESTIONS si nécessaires, DURÉE, CADRE À FABRIQUER si ancrage,
SELF-EVAL, un seul PROMPT FINAL, POINTS DE RUPTURE. Plusieurs générations se numérotent
dans ce bloc unique ; pas de brouillon suivi de retouches à appliquer soi-même.
Verdicts : PRÊT ou MAUVAIS PLAN ; ce dernier remplace le prompt par REDÉCOUPAGE.

Rendus réellement observés seulement : N = 0 à la première émission ; à N = 2,
pas de troisième reformulation aveugle du même défaut. Appliquer `09` et les choix
du projet ; une proposition d'ancrage n'est pas une image validée. Archiver le prompt
avec son rendu. En diagnostic seul, livrer les conclusions sans nouveau prompt.
