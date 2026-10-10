# 09 Diagnostiquer

Un défaut visible ne désigne pas sa cause. Il peut venir du texte, des assets,
des réglages, du mode ou de l'exécution du modèle. Ce skill n'a pas de mesure
permettant d'attribuer « la plupart » des échecs au prompt.

## Classer avant de corriger

Partir du prompt **effectivement testé**, des entrées et réglages connus, puis
du rendu examiné ou du retour utilisateur attribué comme tel. Une réécriture
ultérieure ne prouve pas ce qui avait été envoyé. Si une pièce manque, limiter
la conclusion ; ne pas la reconstruire de mémoire comme une donnée exacte.

Pour chaque défaut, conserver cette chaîne de preuve : **attendu → observé →
clause exacte ou absence → classe → action et contrôle**.

| Classe | Test concret | Suite |
|---|---|---|
| **Consigne absente** | L'exigence utile n'est portée ni par le texte ni par le rôle confirmé d'une entrée | Ajouter la seule information manquante ; préserver les autres clauses |
| **Consigne ambiguë ou contradictoire** | Deux mises en scène incompatibles satisfont le texte, ou deux clauses imposent des états incompatibles | Nommer les deux lectures ou citer les deux clauses ; préciser référents, repères, portée ou chronologie |
| **Consigne présente mais non respectée** | Le défaut observé viole une consigne claire, compatible avec le reste et les entrées connues | Reconnaître l'écart d'exécution. Vérifier mode, paramètres, asset et phase de dérive ; proposer un contrôle ciblé. Ne pas ajouter la même consigne sous trois formulations |

Si les entrées ou le rendu manquent, dire **indéterminé** pour ce qui en dépend.
« Présente mais non respectée » ne prouve pas à elle seule une faute du moteur :
la cause peut rester inconnue. La classe s'établit exigence par exigence ; un
même prompt peut contenir une ambiguïté spatiale et un cadrage clairement écrit
mais non tenu. Ne pas déclarer l'ensemble mauvais à partir d'un seul défaut.

**Test spatial**, même avec un seul personnage : situer corps et orientation,
chaussée ou objet, entrée, caméra et cibles des regards dans un même lieu.
Projeter ensuite cette disposition dans chaque plan et au bout de chaque arc.
« Regarde à gauche » ne situe pas une cible dans le lieu. Un regard hors champ
n'est pas un défaut en soi ; vérifier vers quoi il pointe et si la caméra
permet cette relation.

**Témoin cohérent :** si aucun contre-exemple compatible ni contradiction ne
peut être établi, dire qu'aucune lacune matérielle n'est identifiée. Ne pas
modifier un texte pour produire artificiellement une correction.

Après un rendu, prioriser la première défaillance pertinente et ne changer
qu'une variable pour en tester la cause. Quand deux pannes coexistent et sont
visibles d'emblée, traiter d'abord celle qui rend l'autre injugeable : une
dérive d'identité ou un cadrage faux dès la première image se règlent avant un
détail de mouvement, parce qu'on ne lit pas une caméra sur un sujet qui change. Si plusieurs corrections sont
nécessaires dans la même version, les annoncer et ne pas revendiquer un test
causal isolé. En diagnostic seul, aucune nouvelle génération ni nouveau prompt.

## Vérifier le mode avant tout

Avant de chercher une correction de prompt, vérifier qu'on est dans le bon mode.
As-tu déjà une vidéo finie que tu veux garder ? Non : référence. Oui et tu changes
dedans : édition. Oui et tu en veux plus : extension.

Si une retouche change aussi décor, caméra et visage, vérifier si la vidéo
finie a été traitée comme référence d'inspiration plutôt que comme maître
d'édition. C'est une hypothèse à confirmer dans la requête ou l'interface,
pas une cause déduite des seules images.

## Vérifier le ratio, puis la première image, avant le mouvement

Deux contrôles pour localiser l'écart et vérifier les entrées avant de
modifier les beats ; ils ne démontrent pas à eux seuls la cause.

**Le ratio du fichier de sortie.** Le mesurer. S'il diffère du ratio voulu,
la conformité du cadrage à ce format n'est pas encore évaluable. Vérifier
sélecteur, `adaptive`, rôle de première image et source héritée selon `07`.
Ne pas déduire un réglage précis de la seule résolution observée. Ce rendu
ne compte pas comme un essai de composition au bon format ; ses autres
défauts visibles restent observables.

**La première image du rendu.** L'examiner pour localiser le début de l'écart.
Si elle est déjà fausse, contrôler ratio, ancre, rôle des références et
géométrie avant de retoucher les beats. Cela ne prouve pas que le reste du
prompt n'a eu aucune influence : la génération n'est pas une exécution
séquentielle des lignes. Si l'image initiale est juste puis dérive, examiner
trajet, maintien et occultations à cet instant. Une consigne déjà claire peut
être mal exécutée ; appliquer la classification ci-dessus. Si l'image n'est
pas accessible, demander la pièce utile ou rester sur une conclusion limitée.

Les deux contrôles séparent trois choses que le self-eval ne distingue pas :
ce qui a été écrit, ce qui a été examiné sur une image fixe, ce qui a été vu
dans un rendu. Ligne État de `17-delivery.md`.

## La règle de sortie

### Le compteur d'échecs

Après **deux rendus ratés sur le même point de géométrie ou de composition**,
arrêter la reformulation et basculer sur l'image fixe, la présente règle de sortie.
Tenir le compteur dans la ligne **Reporté**, sur toutes les émissions :

```
Reporté : <conservé sans relecture, ou "première émission">.
          Échecs sur ce point : N.
```

À la première émission, `N = 0`. Compter les rendus **réellement générés et
regardés** par l'utilisateur ou l'assistant, pas les prompts émis ni les
rendus supposés. Remettre à zéro si le symptôme change de nature ou si la
classe d'entrée change : texte vers première image, ou correction d'un réglage.
Un mauvais ratio ne compte pas comme échec de composition : corriger le réglage
d'abord, `09`.

À **N = 2**, ne pas livrer un troisième prompt sur le même point. Nommer les
cadres à fabriquer, proposer l'ancrage et attendre leur validation visuelle.
Le prompt vidéo porte ensuite le mouvement, le jeu, le timing et le son, `05`.
Relire aussi le sujet du brief : le choix des références ne doit pas le déplacer.

**Confiance :** l'absence de bascule après quatre échecs a été constatée sur une
session. L'efficacité du compteur explicite reste une hypothèse à tester en
situation ; un contrôle de texte ne prouve pas un résultat vidéo.


La boucle de correction doit avoir une fin. **À N = 2 rendus observés en
échec sur le même point, premier rendu compris**, appliquer le compteur ci-dessus et la
bascule décrite dans `05-anchoring.md`. Une réécriture non rendue n'incrémente pas N.
Ne pas compter « deux relances après le premier rendu » comme un seuil différent.

Le compteur empêche les relances textuelles aveugles ; il ne démontre pas une
cause. Une ancre peut aider si l'information visuelle manque. Choisir la suite
selon les preuves, les entrées disponibles et les instructions du projet, qui
peuvent exclure une bascule automatique ou imposer le texte seul. Ne pas
transformer N = 2 en preuve qu'une image résoudra le défaut.

Les symptômes marqués **[ancrage]** dans la table ci-dessous sont ceux où la
bascule s'impose plus vite que les autres. Méthode : `05-anchoring.md`.

**Cette règle ne se déclenche pas toute seule.** Elle dépend d'un compte des
échecs sur le même point, et un compte que personne ne tient reste à zéro
indéfiniment : chaque reformulation paraît meilleure que la précédente au moment
où on l'écrit. Le compteur est donc explicite, dans la ligne Reporté du gabarit
de sortie, et sa règle vit dans la présente section. Constaté sur une session : quatre
échecs consécutifs de composition, aucune bascule proposée.

---

## Table

Ces lignes sont des **pistes conditionnelles**, pas des causes prouvées.
Classer le défaut avant de les appliquer : si la clause proposée existe déjà
et n'est pas neutralisée, ne pas la réajouter. Un diagnostic ne conclut pas
« consigne absente » à partir du seul symptôme.

| Symptôme | Vérification ou correction conditionnelle |
|---|---|
| **Une réplique est écrite à l'écran** | `No subtitles.` en fin de prompt. Si la surface lit les crochets, passer la réplique en `{ }`. Vérifier qu'aucun `【 】` ne traîne |
| **Un effet sonore est prononcé par le sujet** | Le sortir de la phrase de dialogue, le mettre dans la clause Audio, ou en `< >` |
| **La langue parlée est fausse** | Vérifier la langue et le locuteur déjà écrits. Les préciser seulement s'ils sont absents ou ambigus ; sinon constater la consigne non suivie et contrôler audio/source |
| **Le débit est plat** | Nommer la variété régionale et le style de débit, pas seulement la langue |
| **La synchro labiale décroche** | Raccourcir la réplique, nommer le locuteur, la minuter, fermer les autres bouches. Envisager la voix enregistrée à part |
| **L'édition a produit une nouvelle vidéo au lieu de corriger** | Vérifier maître, mode et intention explicite d'édition dans la langue du prompt (`06`). Ajouter le déclencheur s'il manque ; s'il est déjà clair, contrôler l'exécution et les entrées |
| **L'extension a redémarré une scène** | Vérifier intention d'extension, source et frontière (`06`). Les préciser s'ils manquent ; ne pas attribuer le redémarrage à un verbe absent sans lire le prompt testé |
| **L'upload d'une référence est refusé** | Lire le message d'erreur et vérifier format, dimensions, poids, durée, droits d'accès et règles de la surface. Si le refus concerne un visage réel, utiliser la voie autorisée documentée dans `07`. Ne pas attribuer tout refus à un visage |
| **Erreur au moment de soumettre** | Contrainte de fichier : ratio hors [0,4 ; 2,5], côté hors [300 ; 6000] px, vidéo d'édition sous 4 s, ou cumul de références au delà de 30 s. Par l'API, à la soumission seulement si `omni_reference_task_type` vaut `edit` ou `extend`, sinon après le lancement : `InvalidParameter.TaskTypeMismatch` dit que l'intention du prompt ne correspond pas au type de tâche déclaré, `InvalidParameter.TaskTypeConstraint` que `ratio` ou `duration` contredisent le type détecté ; édition et extension exigent `adaptive`, l'édition exige aussi `-1`, `07-spec.md` |
| **Le modèle ignore une référence** [token] | Comparer le token au pointeur exact fourni par la surface, espaces compris ; `10`. Vérifier ensuite l'asset associé, l'index si positionnel et l'ordre des uploads. Ne pas normaliser un token injecté |
| **Le modèle ignorait une référence (autre cause)** | Slot non fourni ou index décalé. Vérifier l'ordre des uploads |
| **Une référence a amené son décor ou ses figurants** | Écrire l'exclusion : `Do not use the image background` |
| **Le fichier de sortie n'a pas le ratio écrit dans le prompt** | Le texte ne règle pas le ratio. En texte vers vidéo ou en référence, régler le paramètre explicitement au lieu d'`adaptive` ; en première image, édition ou extension, aligner l'asset source sur le ratio de livraison, `07-spec.md`. Ne compte pas dans le compteur de composition |
| **Le sujet sort sous l'angle de la photo de référence, pas sous l'angle demandé** [ancrage] | Vérifier si la référence apporte un angle contraire au rôle autorisé. Si l'exclusion manque, la préciser ; si elle est claire, constater son non-respect et envisager une référence d'angle ou une ancre selon le projet. `01` et `05` |
| **La composition est fausse dès la première image** [ancrage] | L'écart existe dès le départ. Vérifier ratio, ancre, rôles et géométrie ; ne pas en déduire une cause certaine. Voir les contrôles et la classification ci-dessus |
| **Le rendu ressemble à la première frame sans la reproduire, plus large ou recadré** | Vérifier ratio puis rôle réel de l'image, `04` et `05`. Une référence en pool peut expliquer une ressemblance sans reproduction, mais un slot déclaré peut aussi être mal exécuté ; ne pas présumer l'entrée à partir du seul rendu |
| **Le rendu est conforme et le plan est faible, sujet minuscule, moitié d'image vide** [ancrage] | Ce n'est pas le prompt, et le rendu n'entre pas dans le compteur. Si une recomposition est demandée, bloc CADRE À FABRIQUER et vérification du champ dans `01`, Le ratio vertical. Ne pas changer un angle ou une échelle conformes au brief par préférence esthétique |
| **Deux références se contredisent** | Vérifier leurs rôles et exclusions, puis annoncer l'arbitrage selon le brief. Toute suppression d'asset reste déclarée, `04` |
| **La prose contredit une référence** | Comparer le rôle autorisé à ce que l'image apporte. Une référence d'identité n'impose pas son décor ; préserver le brief et préciser l'exclusion ou proposer une ancre adaptée. Ne pas aligner automatiquement la demande sur l'image |
| **Quatre exemplaires du même objet** | Déclarer que toutes les images définissent un seul objet, et que la sortie ne doit en contenir qu'un |
| **Deux personnages échangent visage ou vêtements** | Rôles nommés, une ligne par correspondance, plus `Do not interchange their appearances, clothing, actions, or dialogue` |
| **Le personnage change au fil du clip** [ancrage] | Moins de références d'identité, supprimer les portraits conflictuels, verrouiller la formulation du bloc d'identité, raccourcir la scène pour diagnostiquer. En dernier recours, répéter les trois à cinq ancres d'identité dans chaque beat majeur, recommandation Dreamina, au prix du bruit que `03` signale |
| **Un objet change de main ou se téléporte** | Écrire l'invariant avant les beats et le rappeler dans le beat concerné : quelle main tient quoi |
| **Un objet disparaît derrière un obstacle** | Écrire la durée d'occultation et la liste de ce qui doit revenir identique |
| **Un objet apparaît des deux côtés à la fois** | `No person or object appears on both sides at once` |
| **La caméra ignore la direction** | Un mouvement principal. Supprimer les termes de style qui impliquent une autre grammaire caméra |
| **Un terme caméra n'a aucun effet** | Garder le terme et le traduire en changement visible |
| **Une clause caméra est ignorée, le mouvement n'apparaît pas** | La parade n'est **jamais** de supprimer le mouvement ni de verrouiller la caméra pour faire passer le plan : c'est rendre l'arbitrage au modèle. Vérifier d'abord que le sujet ne réclame pas le même cadre, auquel cas l'arbitrage se fait à l'écriture et s'annonce, section Séparer caméra et sujet de `01-write-shot.md` ; s'ils sont compatibles, appliquer la recette du travelling, ligne Travelling latéral de la table des techniques de `01-write-shot.md` |
| **Le rendu est plastique et on relance en définition supérieure** [ancrage] | Distinguer manque de détail et rendu des matériaux. La résolution seule ne prouve ni la cause ni la solution ; comparer plaque, éclairage, look et détails de sortie. `05`, La texture photographique |
| **Un travelling latéral sort en zoom, l'image s'élargit sur place** | Première image vérifiée d'abord, section ci-dessus. Sinon, parallaxe en trois couches à vitesses distinctes et `does not zoom`, section Techniques qui demandent une précision de plus de `01-write-shot.md` |
| **Une image de look a imposé son cadre** [ancrage] | Elle contient les sujets du plan. Trois sorties, par ordre de préférence, section La texture photographique de `05-anchoring.md` |
| **Le cadrage dérive** [ancrage] | Donner au sujet une position en tiers et un point d'arrivée au mouvement |
| **Le plan sort plus serré que demandé, le plan large devient un plan moyen** [ancrage] | Si la taille n'est qu'une étiquette ou est contredite, préciser géométrie et jeu à l'échelle du plan (`01`). Si « head to boots » et maintien sont déjà clairs, classer le non-respect ; ne pas diagnostiquer une absence. Décider du test d'entrée selon les preuves et les instructions du projet |
| **Le style de réalisateur demandé ne se voit pas** | Le nom a été supprimé comme adjectif de goût, ou traduit en émotion. Le déplier en clauses caméra sourcées, sans le nom dans le prompt. Voir `13-director.md` |
| **Un mouvement de caméra demandé dans une référence de mise en scène manque** | Comparer les traits effectivement retenus et les clauses de chaque plan. Restaurer le mouvement demandé ; garder les plans fixes voulus. Un nom de réalisateur n'impose pas une caméra mobile à tous les plans. `13`, Caméra immobile |
| **La caméra bouge trop tôt** | Attacher le mouvement à un événement visible : `does not pan until [événement]` |
| **La réaction précède la cause** | Séparer contact, mouvement, son, réaction. Ajouter `only after contact` |
| **Tout le monde réagit en même temps** | `at slightly different delays` |
| **Le mouvement humain est faux** | Décomposer en contacts : approche, contact, transfert de force, ordre d'atterrissage, encaissement, repos. Réduire vitesse et amplitude |
| **Le mouvement ne se termine pas** | Nommer l'état de repos. Sans lui le modèle enchaîne ou fige |
| **Un liquide monte ou flotte** | Nommer la direction de la force et l'état final. `does not flow uphill`, `breaks cleanly` |
| **Le produit ou le visage se déforme** | Réduire la quantité de mouvement et ajouter une clause de préservation de forme |
| **Ralenti involontaire** | Vérifier vitesse demandée, contenu des références, phases et durée. Une faible densité peut contribuer mais ne prouve pas la cause ; garder toute attente ou approche voulue et appliquer `01c` sans quota |
| **Répétition, attente, boucle** | Distinguer tenue intentionnelle et répétition non voulue. Vérifier état final et éventuel rejeu de la source ; ne pas ajouter un événement pour remplir la durée |
| **Une action est absente** | Vérifier si l'action est écrite, située et compatible avec les autres clauses. Une surcharge est une hypothèse ; si la consigne est claire, constater son non-respect avant de proposer une simplification annoncée |
| **L'action est dans le désordre** | Réduire le nombre de beats, rendre la fin explicite, séparer par plages temporelles |
| **Le modèle ignore un timestamp** | Trop de marqueurs. Élargir les fenêtres |
| **La transition est abrupte** | Ajouter `gradually`, `in one continuous shot`, ou `the lighting shifts smoothly`. Supprimer toute instruction de coupe contradictoire |
| **Morph baveux entre deux lieux** [ancrage] | La transition n'est pas déclarée. Ajouter `Cut to` ou nommer le nouveau lieu en tête de beat |
| **Le résultat est visuellement surchargé** [ancrage] | Réduire figurants, effets, accessoires et couleurs d'éclairage |
| **La lumière saute** [ancrage] | Une source nommée, cohérente spatialement. Ne pas empiler des grammaires lumineuses incompatibles |
| **La lumière change entre deux plans, surtout sur un gros plan ou un insert** [ancrage] | Elle n'a été écrite qu'en clause globale, ou le plan serré ne la voit plus : source hors cadre, donc déduite, donc réinventée. La redéclarer dans chaque plan comme son effet sur ce qui est dans le cadre, bloc recopié mot pour mot. Section Lumière de `01-write-shot.md` ; sur une séquence ancrée, la vérifier entre les fixes, `05-anchoring.md` |
| **L'optique dérive d'un plan à l'autre** : compression, bokeh, distorsion de bord [ancrage] | Une optique demandée en prompt vidéo ne tient pas. La générer dans l'image de décor et laisser le modèle la lire sur la plaque. Voir `05-anchoring.md` |
| **Un artefact interdit apparaît quand même** : flare, traînée, bille de bokeh, halo | La négation le nomme, donc l'invoque. Retirer le mot du prompt et décrire l'état propre en positif. Voir `12-constraints.md` |
| **La mise en place à plusieurs personnages est fausse, ou change à chaque relance** [ancrage] | La prose ne tient pas une géométrie. Fournir un diagramme de mise en place, une figure colorée par personnage. Voir `11-diagram.md`. Places et regards se corrigent alors ensemble, en une seule variable changée |
| **Un personnage regarde dans le vide, ou l'axe saute entre deux plans** | Écrire la carte des regards en direction d'écran, et déclarer aussi le côté où se trouve un personnage hors champ |
| **Le diagramme fourni dérive vers une illustration** | Il a été regénéré depuis le diagramme précédent au lieu du cadre source, ou son style graphique est nommé dans le prompt, même en interdiction |
| **Le jeu meurt dès que la réplique démarre** | Le comportement est dans un bloc séparé. L'écrire dans la clause de dialogue, raccourcir la réplique. Voir `02b-perform-failures.md` |
| **Le visage est monstrueux, veines et tendons saillants** | Symptôme physiologique prescrit. Écrire l'intention et l'effort à la place |
| **Le regard est perdu, sans objet** | Une négation de regard a été écrite. Toute direction de regard est positive |
| **Le regard est fixe et robotique** | Cible unique tenue trop longtemps. Écrire une trajectoire, pas une cible |
| **Le personnage regarde au sol, le visage est fermé** | Le regard a été écrit vers le bas, ou sans cible. Cible à hauteur d'yeux, trajectoire, retour. Section Les yeux sont le canal de `02a-perform.md` |
| **Le silence est joué en robot, visage figé** | Le silence a été écrit comme une pose, « holds still, no expression change ». Tâche intérieure, trajectoire de regard, micro-événement. Mécanisme 8 de `02b-perform-failures.md` |
| **Le personnage est vide pendant un silence long, rien ne se passe** | Aucun changement perceptible ni stimulus exploitable. Appliquer [02a-perform.md](02a-perform.md), Accorder le jeu au cadre et La partition d'un silence, y compris l'arbitrage sans activité d'objet prévue |
| **Le personnage prononce sa pensée pendant le silence** | La ligne intérieure était entre guillemets, donc lue comme une réplique. La réécrire en forme indirecte, `he is realising that`, et fermer la bouche |
| **Un geste anodin est joué comme un climax** | Une rampe ralenti est posée dessus. La retirer d'un plan dialogué |
| **Un élément de décor se déplace à chaque relance** | Vérifier sa présence et son rôle dans les entrées. S'il manque, une plaque peut préciser sa place ; s'il est déjà ancré, classer le non-respect et contrôler le mode avant de refaire l'asset |
| **Le son est générique** | Deux ou trois sons diégétiques précis, supprimer toute direction musicale vague |
| **La voix change de timbre entre deux clips** | Le bloc de voix a été reformulé. Le recopier mot pour mot, sans synonyme. Voir le verrou de voix dans `10-syntax.md`. Le verrouillage réduit la dérive, il ne la supprime pas |
| **Après une édition, le nouvel objet a le mauvais rythme** | Le bloc d'héritage de timeline manque. Exiger apparitions, trajectoires, occultations et sorties héritées |
| **Scintillement après édition** | Vérifier la zone réparée sur toute la timeline, pas seulement la fenêtre |
| **Une extension arrière fait apparaître un personnage trop tôt** | Déclarer quelles matières appartiennent uniquement au clip d'origine |
| **Une extension arrière ne se raccorde pas** | Énoncer la première frame de la source comme état final explicite |
| **La dernière image est étirée** | Première et dernière image n'ont pas le même ratio |
| **Un réglage refuse de changer** | Le mode le verrouille. Voir `07-spec.md` |
| **L'image est molle** | Vérifier la résolution. Repartir de la source la plus haute définition, cadrer plus serré, éclairage plus simple, moins de petits détails |
| **Le plan large sort en rendu 3D ou jeu vidéo alors que les plans serrés sont photo** [ancrage] | Le plan large montre ce qu'aucune référence ne montre, donc inventé avec la texture par défaut. Plaque du plan large fabriquée et validée sur sa texture, image de look dans le pool, ligne de look positive recopiée par plan, aucun rendu nommé en négation, moins de petits objets. `05-anchoring.md`, La texture photographique |
| **Un son tombe au mauvais moment** | Vérifier où le son est écrit. S'il est global sans instant, le lier au beat causal ; s'il est déjà situé, constater l'écart de synchronisation et tester cette seule variable |
| **Un accessoire devient deux** | Le compte manque dans les états de sortie. Écrire `exactly one [objet] is in frame` à chaque étage |
| **Une référence pilote deux choses à la fois** | Un token porte un seul rôle. Séparer, ou tout dire dans la ligne d'introduction |
| **Un sujet devient générique sur un plan de la série alors qu'il tenait avant** | Sa référence a été retirée du manifeste entre deux plans, souvent parce que l'angle du nouveau plan ne la montre pas. Reprendre le manifeste du plan précédent ; section Une référence ne se retire pas parce que l'angle change de `04-references.md` |
| **La dernière frame se déforme** | Ratio différent entre première et dernière image |
| **Le morphing warpe au milieu** | Les deux ancres sont trop éloignées. Rapprocher position et échelle, ou ajouter une keyframe intermédiaire |
| **La dernière frame n'est pas atteinte** | Raccourcir la durée, simplifier le prompt sur la transition, rapprocher les deux compositions. Elle est approchée, jamais garantie au pixel |
| **Le texte à l'écran est faux** | Attendu. Incruster en post. Si le logo doit être natif : référence stable, marque face caméra, moins de mouvement, cadre hero verrouillé sur les 3 dernières secondes, recommandation Dreamina |
| **Les crédits fondent** | Brouillon court en basse résolution, estimation du lot avant lancement, une variable par relance. Suivre le coût par plan accepté |

---

## Les cinq erreurs classiques

1. **Décrire une image fixe.** Un modèle vidéo a besoin de mouvement dans le
   temps, pas d'une photographie en mots.
2. **Caméra vague.** « cinematic » ne dit rien. Nommer le plan, un mouvement, un
   point d'arrivée.
3. **Entasser une séquence dans un seul bloc**, si bien que les événements se
   percutent au lieu de se suivre.
4. **Laisser les références sans job**, ou les étiqueter en groupe. Les entrées
   non attribuées sont moyennées, et la moyenne est l'origine de la dérive
   d'identité.
5. **Oublier les exclusions**, et hériter de l'arrière-plan ou des figurants
   d'une référence en même temps que du sujet.

Deux erreurs de gestion à ajouter : traiter l'audio comme une case à cocher, ce
qui produit une ambiance générique, et maximiser la durée par défaut, ce qui
double le coût d'une même idée.

---

## Le test de plateau

Deux directions qui ne pouvaient pas se produire en même temps sur un vrai
plateau sont un conflit de simultanéité : méthode de lecture, arbitrage et
exemples dans `12-constraints.md`, Arbitrage des conflits.

---

## La limite utile

Elle est atteinte quand un beat contient plus d'une action principale, plus d'une
instruction caméra, ou plus d'un changement de scène.

Si le prompt se lit comme une liste de plans complète compressée dans cinq
secondes : le découper en générations séparées, ou allonger le clip si le
brief le permet et si chaque beat garde un seul changement. Jamais garder tous
les segments en les compressant, `03-sequence.md`, Repère de montage.
