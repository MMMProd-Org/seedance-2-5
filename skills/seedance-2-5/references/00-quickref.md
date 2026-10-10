# 00 Préparer un brief incomplet

Ouvrir cette fiche lorsqu'une donnée nécessaire au prompt manque. Le routage,
la checklist et le self-eval restent dans `SKILL.md` ; cette fiche n'est pas
une seconde entrée obligatoire. Le gabarit de réponse vit dans `17-delivery.md`.

## Questions de préparation

**Questionner un manque quand sa réponse change le prompt d'une façon qu'une
relance ne rattrape pas et que l'utilisateur est seul à l'avoir.** Les deux
conditions s'appliquent, sous réserve de ses instructions explicites.

La liste borne les questions de brief. En diagnostic, une pièce manquante
indispensable au contrôle (rendu, première image ou message d'erreur) peut être
demandée selon `09`, sans prétendre l'avoir examinée. **Plafond : trois questions,
quatre quand l'état du fil en fait partie**, ce trou-là étant le seul qui porte
sur plusieurs plans à la fois. Ce plafond est le même partout, checklist et
gabarit de sortie compris.

| Trou | Pourquoi il ne se rattrape pas |
|---|---|
| La forme d'adressage de la surface | Un pointeur mort ne lève aucune erreur, la clause tombe en silence et l'émission est perdue, `10-syntax.md` |
| Le slot première image existe ou non | Il décide entre reproduire un cadre et lui ressembler, donc entre deux prompts différents, `05` |
| Le ratio de livraison | Il change l'arithmétique de la composition, pas une formulation, `01`, Le ratio vertical |
| Deux demandes de l'utilisateur qui se contredisent | Choisir à sa place est exactement la liberté qu'il ne veut pas |
| Un élément inventé assez gros pour devenir un sujet du plan | Il déplace le sujet du plan, ce qu'aucune relance ne défait |
| Un réalisateur, un film ou une séquence, quand le brief ne dit pas lequel | Une séquence donne des plans, une filmographie une réputation, `13` |
| L'état du fil, quand le plan en continue d'autres et que la conversation ne porte pas le manifeste, les formulations verrouillées, la ligne de look, le ratio et la lumière des plans précédents | Repartir d'une page blanche casse l'identité d'un plan à l'autre, et aucune relance ne recolle une série déjà divergente, `04-references.md`, Mémoire du fil |

**Deux comportements, et un seul bloque.** Six des sept trous se posent en
question **et reçoivent quand même un défaut annoncé**, de sorte que le prompt
est livré et que l'utilisateur peut le lancer sans répondre. Le septième, deux
demandes qui se contredisent, **arrête l'émission** : aucun prompt n'est
livré, parce que le défaut y serait précisément l'arbitrage silencieux que la
`SKILL.md`, Autorité et lecture interdit. C'est la seule condition d'arrêt **avant écriture** ; le compteur de `09`
et le verdict de livraison de `17` restent applicables ensuite.

Le bloc QUESTIONS de `17-delivery.md` ouvre la sortie, avant DURÉE. Il est **omis quand la liste
est vide**, ce qui est le cas normal d'un brief complet. Un bloc QUESTIONS qui
apparaît sur un brief déjà complet est une panne, pas une précaution.

Ce que cette étape ne couvre pas : le décor, la lumière, le cadrage, le
détail, le goût. Tout cela reste décidé, écrit et déclaré dans le self-eval,
`SKILL.md`, Autorité et lecture. Poser une question sur du cosmétique coûte un aller-retour pour
quelque chose que la passe suivante corrigeait gratuitement.

## Vérifier la bonne autorité

- Visage réel à uploader, limites de fichiers, résolution, ratio, paramètres
  hérités ou recommandation MOV : `07-spec.md`, sections applicables au mode.
- Édition et extension : intention explicite et formulations dans la langue
  du prompt, `06-edit-extend.md` ; ne pas supposer le mode d'après un seul mot.
- Forme d'adresse inconnue : `10-syntax.md` ; conserver celle de la surface.
- Lisibilité des segments : `03-sequence.md`, Repère de montage ; ce n'est pas
  une limite native ni une permission de supprimer des plans demandés.

## Anciennes règles numérotées : chemins de compatibilité

Les numéros ci-dessous permettent de retrouver les anciens renvois. Ils ne
constituent plus un deuxième ensemble de règles. Le contenu normatif vit dans
le noyau et les autorités indiquées ; la table de routage unique est dans `SKILL.md`.

| Ancienne règle | Autorité actuelle |
|---|---|
| 1, mouvement caméra principal | `SKILL.md`, Checklist ; `01-write-shot.md`, Caméra |
| 2, clauses caméra et sujet distinctes | `SKILL.md`, Checklist ; `01-write-shot.md`, Séparer caméra et sujet |
| 3, un changement par beat | `SKILL.md`, Checklist ; `03-sequence.md`, Les beats minutés |
| 4, mots de goût et réalisateur cité | `05-anchoring.md`, Les mots de goût ; `13-director.md` |
| 5, émotion jouée | `02a-perform.md` ; `SKILL.md`, self-eval |
| 6, silence dirigé | `02a-perform.md`, Les silences ; `SKILL.md`, Checklist |
| 7, biographie invisible | `02a-perform.md` ; `SKILL.md`, Checklist |
| 8, écoute | `02a-perform.md` ; `SKILL.md`, self-eval |
| 9, une variable après rendu | `09-diagnose.md`, La règle de sortie ; `SKILL.md`, En réémission |
| 10, token exact | `10-syntax.md` ; `SKILL.md`, Checklist |
| 11, arbitrages annoncés | `SKILL.md`, Autorité et lecture |
| 12, mémoire de la série et prompt autonome | `04-references.md`, Mémoire du fil ; `SKILL.md`, Le squelette |
