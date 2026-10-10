# 14 Invariants de maintenance

## Sommaire

- Invariants de maintenance
- Arbitrage des apports externes
- Vérification avant enregistrement

## Invariants de maintenance

Ils ne s'adressent pas au modèle vidéo mais à qui édite ce skill, y compris un
autre LLM reprenant le dossier plus tard. Chacun corrige une dérive déjà
constatée sur ce skill. Ils vivaient dans `SKILL.md` et en ont été sortis parce
qu'ils ne servent à aucune émission : quarante lignes lues à chaque prompt pour
un lecteur qui n'est pas là. À ouvrir avant toute modification du skill, jamais
pour écrire un prompt.

1. **Une convention compatible avec la surface par exemple.** Les patrons en
   pool indexé emploient `@image1` par défaut, sans normaliser les mentions
   réellement fournies. La décision vit dans `10`, les noms lisibles dans `04`.
   Un mélange n'est valide que si chaque adresse est réellement liée sur la
   surface. Les prompts de cas réels restent littéraux : ne pas réécrire leurs
   tokens pour les conformer au style d'un patron.
2. **Tout en-tête crocheté employé quelque part figure dans une des deux tables
   de blocs de `10-syntax.md`**, avec sa source. Un vocabulaire de blocs qui
   grossit sans déclaration devient une convention privée par fiche.
3. **Un fait, un endroit.** Une règle vit dans une fiche et les autres y
   renvoient. Toute duplication de formulation dérive au premier remaniement,
   exactement comme un bloc d'identité reformulé. Constaté : `03-sequence.md` a
   porté deux fois la table de structure et la table de découpage, avec des
   lignes différentes dans chaque copie ; fusionnées en septembre 2026. Constaté
   encore le 9 septembre 2026 : une ligne de `09` a recopié les trois sorties
   d'une règle de `05` dans un autre ordre et en a perdu une, en une seule
   passe ; remplacée par un renvoi. Une ligne de diagnostic nomme la lacune
   établie ou l'hypothèse à vérifier et renvoie, sans recopier la parade.
4. **Toute affirmation non issue de la documentation ByteDance porte son niveau
   de confiance** : publié, constaté sur une surface, rapporté par une
   production, hypothèse. Sans marqueur, une hypothèse de session devient une
   règle en deux relectures. Une règle de plateau empruntée à un acteur ou à un
   manuel de direction se cite avec auteur et date, et son transfert au modèle
   est marqué hypothèse.
5. **Un ajout doctrinal venu de l'extérieur s'arbitre, il ne se juxtapose pas.**
   Si la source contredit une règle en place, trancher explicitement et écrire
   pourquoi. Deux doctrines concurrentes dans un skill produisent le même
   résultat que deux références contradictoires : une moyenne. Constaté : la
   ligne de sécurité du regard nommait un « frozen, glassy stare » en négation
   alors que `12-constraints.md` interdit de nommer un artefact dessinable ;
   tranchée en positif en septembre 2026.
6. **Ce qui relève de l'écriture reste dehors.** Analyse de scène, structure
   dramatique, motifs et buts de personnages appartiennent au skill de scénario.
   Ce skill prend leur sortie et l'écrit en prompt. La mise en scène par la
   caméra, elle, est dedans : un réalisateur cité se traduit en clauses caméra,
   `13-director.md`, et ne retourne pas au scénario.
7. **Mesurer le coût avant d'ajouter.** `01-write-shot.md` garde son plafond de
   500 lignes. Pour le principal, compter lignes et mots, puis les lectures
   effectivement nécessaires par parcours : déplacer tout vers une fiche
   systématiquement chargée ne constitue pas une optimisation. Le noyau porte
   décision, déclencheurs, checklist et self-eval ; les procédures conditionnelles
   et le format développé vivent dans les autorités référencées.
8. **Le contrôle obligatoire reste visible dans le noyau.** Chaque vérification
   y garde son déclencheur et le résultat à établir, même si sa méthode détaillée
   est conditionnelle. La checklist avait été ignorée pendant six émissions
   lorsqu'elle vivait hors du principal, constat d'une session. La refactorisation
   conserve donc ses 47 entrées et les cinq questions dans `SKILL.md`. Tester
   aussi plusieurs émissions successives ; une lecture enregistrée ne prouve
   pas l'application. `00` prépare les données manquantes, `17` développe la sortie.
9. **Les exemples enseignent plus que les règles.** Le modèle copie la forme des
   gabarits et des colonnes « Fort », pas le paragraphe qui les précède. Un
   exemple qui contredit une règle gagne contre la règle. Constaté : quatre
   exemples et deux gabarits écrivaient le regard vers le bas ou le silence en
   immobilité, alors que la doctrine disait l'inverse ; les rendus faisaient ce
   que les exemples montraient. Avant d'ajouter une règle, relire les exemples
   qui la concernent.
10. **Toute fiche au-dessus de 300 lignes porte un sommaire** en tête, et toute
    fiche nouvelle entre dans la table unique de `SKILL.md`, avec sa condition
    d'ouverture et son contrôle attendu. Une fiche
    absente de la carte n'est jamais ouverte.

## Arbitrage des apports externes

Sources initiales fournies par l'utilisateur le 9 septembre 2026. Auteurs,
dates de publication et liens originaux inconnus ; aucun rendu de validation joint.
Conserver ce statut dans les fiches qui en tirent des hypothèses.

| Source fournie | Apport retenu et lieu | Arbitrage avec le skill |
|---|---|---|
| Bloc « Structure the Duel » dans le message | Causalité des échanges et repères de progression, `01d-duels.md` | Deux combattants seulement pour cette fiche ; huit repères facultatifs, sans imposer une intrigue ni les six rubriques de sortie externes. Conserver une seule action décomposée par plan, `01b` |
| « Film and Television Script Microexpression Performance Enhancement », Fichier markdown(5).md collé, chap. 4-5 | Fuite, reprise de contrôle, trace finale, densité par canal, périmètre de correction, `02c-fine-performance.md` | Garder jeu avant effets, `SKILL.md`, et regard de `02a`. Écarter les validations A/B, le défaut 15 s/gros plan, les générations imposées et l'ajout d'accessoires pour remplir les beats |
| « Master Cinematic Technique Toolkit », Fichier markdown (2).md collé, modules 1-9 et 11 | Sélection par effet visible, POV, révélation, états des raccords, `15-camera-techniques.md` | Garder un mouvement principal, modes et durée existants. Écarter négatifs systématiques, recettes de musique/couleur, quotas de mots-clés, durées tronquées et promesses « tested and proven » |
| « Master Director Camera Movement Toolkit », Fichier markdown (3).md collé, et module 10 du fichier précédent | Distinguer trajet, orientation, focale, point et temps, `15` | Ne pas recopier les écoles et attributions sans sources. `13-director.md` garde la recherche ; ne pas imposer un son ou une lumière par réalisateur ni interdire une technique sur un critère de goût |

Apports supplémentaires du même jour : quatre prompts dont l'utilisateur
rapporte de bons résultats, sans vidéo examinée ni comparaison de langue.

| Source fournie | Apport retenu et lieu | Arbitrage avec le skill |
|---|---|---|
| Duel chinois en station sous la pluie, 30 s | Suivi extérieur à la troisième personne, repères de décor et états acquis, `01d` | Ne pas importer une caméra subjective, une interface de jeu, huit étapes obligatoires ou tous les contacts détaillés par défaut ; `01b` garde le budget et `13` la recherche sur le film cité |
| Vlog alpin anglais, huit scènes en 30 s | Montage elliptique, états locaux de tenue et lumière, `03` et arbitrage lumière de `01` | Identité stable ne signifie pas décor ou tenue immuables ; ne pas forcer trois à cinq plans. « 4K » et « 24fps » dans un exemple ne prouvent pas un réglage natif, `07` |
| Scène chinoise avec corps et esprit, 15 s | Identité distincte des manifestations, effet causé et exception physique locale, `16` ; tokens préservés par `10` | Garder le corps et une seule projection ; les verrous contre les duplications ne suppriment pas l'effet voulu. Le parapluie flottant finit tenu sans reprise écrite : conflit d'état à résoudre, pas geste à inventer silencieusement |
| Canon de science-fiction et horde, anglais, 15 s | Liaisons du déploiement, événement continu entre coupes, propagation et retour de la même voiture, `16` | Garder prises, compte et géométrie fournis, sans inventer les détails d'assets non vus ; ne pas rabattre la horde sur le duel. Fin textuelle tronquée à « Do not alte » : aucune suite attribuée à la source |
| « Seedance 2.5 prompt guide », Fichier markdown(6).md collé, revue affichée du 17 août 2026 | Rôles, beats, caméra, sons et état final confortent le squelette existant ; révision du minimum nécessaire | Synthèse éditoriale se réclamant de Topview, pas documentation du moteur. Ne pas dupliquer sa formule, ses grilles temporelles ni ses négatifs dans une nouvelle doctrine |

**Langue.** L'anglais obligatoire était une convention du skill, pas un
avantage démontré. Remplacé par le choix explicite de `10`, qui cite les pages
officielles consultées le 9 septembre 2026. La traduction préserve les données
verrouillées. Aucune réussite vidéo ni supériorité linguistique n'est déduite
des essais de rédaction. `06` conserve une intention explicite d'édition ou
d'extension dans cette langue, sans imposer les verbes anglais de ses exemples.

Les nouvelles fiches décrivent des hypothèses de prompting, pas des fonctions
du moteur confirmées. Ne pas convertir une exécution LLM réussie en taux de
réussite vidéo. La compression de `SKILL.md` retire les justifications
répétées ; garder les contrôles à l'étage toujours chargé.

**Arbitrage relevé par la revue :** l'activité avec objet de `02a` et de la
checklist contredisait le cas sans accessoire de `02c`. L'alternative vit
désormais dans `02a`, La partition d'un silence, et la checklist y renvoie.
Elle conserve l'activité causée et son issue sans imposer une manipulation
absente du brief. Les exemples avec objets restent utilisables dans leur contexte.
Le diagnostic de `09` et `02b` renvoie au même arbitrage. La visibilité du jeu
est définie dans `02a`, Accorder le jeu au cadre, et gouverne le self-eval et
la checklist de diagnostic. Le verrou de présence de `01` est borné aux plans
concernés ; il ne supprime pas un insert sans sujet explicitement demandé.
Une coupe entre clips déjà compatibles sort du parcours de génération ; seul
un passage manquant ouvre Transition, arbitrage commun de `SKILL.md`, `06` et `15`.

## Vérification avant enregistrement

Après une modification de routage ou de protocole : valider le frontmatter,
résoudre les liens locaux, comparer les contraintes et les exemples concernés
avec la version précédente, puis essayer des demandes réalistes. Ne pas
confondre un mot-clé trouvé dans le fichier avec un comportement validé.

Pour un essai indépendant, donner uniquement le skill et le brief brut à un
nouveau lecteur, sans cette grille ni les réponses attendues. Ne pas générer
de vidéo payante pour une vérification du texte. Conserver les sorties brutes
de l'essai hors du skill ; annoncer exactement ce qui a été contrôlé.

| Cas | Contrat à préserver ou observer |
|---|---|
| Plan court sans personnage | Format existant, un seul prompt final, jeu sans objet, aucune fiche de duel ou jeu fin inutile |
| Attente retenue de 6 s, puis retour « encore figée » | Identité, look, cadre et action conservés, changement causé et trace finale ; diagnostic sans accessoire ajouté pour remplir une grille |
| Correction du jeu d'un seul personnage, y compris insert de mains | Aucun changement non demandé de dialogue, caméra, lumière, durée, ratio ou autres personnages ; canal accessible au cadre, prompt complet livré |
| Duel bref à deux | Échange causal lisible, état reporté, aucun remplissage des huit repères ni issue inventée |
| Combat à trois | Limite de `01d` localisée : continuer via séquence et diagramme, sans refuser le skill entier ni réduire le casting |
| POV humain ou caméra embarquée | Porteur nommé, absence de confusion entre sujet vu et point de vue ; pas de membre ajouté par défaut |
| Raccord par masque ou sur une action | États des deux côtés, type de raccord explicite ; aucune transformation non demandée |
| Deux clips déjà compatibles sur la phase d'un geste | Indications de coupe au montage ; aucune durée, génération de pont ou reprise du geste ajoutée |
| Révélation par mise au point | Élément révélé déjà dans le cadre ; le changement de point ne modifie pas sa position |
| Ralenti, flare, musique ou coupe explicitement demandés | Aucun négatif externe ne les interdit ; conserver les arbitrages et limites de `13` |
| Références nommées ou tokens injectés | Convention de la surface conservée, sans conversion arbitraire en index ni mélange |
| Chinois : traduction avec dialogue français et tokens injectés, puis extension | Langue technique demandée, réplique et tokens littéraux ; en-têtes de sortie préservés, intention de tâche, nombres, directions et paramètres hérités conservés ; aucun gain vidéo prétendu |
| Prompt chinois à références nommées, indexées ou injectées | Noms d'origine lisibles dans le manifeste et les beats concernés ; tableau de correspondance dans la langue de la conversation hors code ; aucun alias `@` inventé ni nom de fichier supposé ; en prompt seul, associations nom-token conservées dedans |
| Sujet hero avec insert d'ambiance demandé sans ce sujet | Présence tenue dans les plans concernés, exclusion conservée dans l'insert ; aucun conflit créé par le verrou global |
| Vlog de huit moments, lumière du matin au soir | Huit moments conservés ; ellipses déclarées, lumière et tenue locales, identité globale ; aucune définition de sortie déduite du mot « 4K » |
| Mécanisme ou effet fantastique à plusieurs états | Cause avant effet, pièces reliées ou exception physique bornée, comptes par manifestation, état final compatible ; aucune fin tronquée complétée comme source |
| Édition et extension | Maître, portée, préservation, verbes déclencheurs et paramètres hérités de `06`-`07` |
| Deux échecs observés sur le même cadre | Compteur réel, bascule d'ancrage, aucun troisième essai textuel aveugle |

### Contrôles adversariaux complémentaires

Les cas ci-dessous couvrent des conflits relevés lors de la revue du
10 septembre 2026. Conserver une seule autorité par règle : physique et
circulation dans `01b`, géométrie dans `01`, rythme dans `03` avec les
hypothèses de `01c`, syntaxe de surface dans `10`, limites natives dans `07`.
Les listes de contrôle et patrons doivent suivre ces arbitrages.

| Cas | Contrôle |
|---|---|
| Voiture de profil entière à 50 % de largeur en 9:16 | Calculer le champ utile ; ne pas annoncer une impossibilité ni remplacer le profil par un trois-quarts |
| Caméra suivant A tandis que A rejoint B | Nommer les deux référents de chaque distance ; le suivi de A n'interdit pas son approche de B |
| Approche lente ou attente expressément voulue | Aucun événement ajouté pour un quota de deux secondes ; aucun plan supprimé à cause d'un seuil perceptif non validé |
| Freinage avec compensation du passager | Inertie et appui volontaire compatibles ; pas d'interdiction générale du tangage ou d'un mouvement vertical de suspension |
| Marche arrière vers la caméra sur plateau vide | Face arrière, feux de recul et feux rouges compatibles ; pas de pays, files ou trafic inventés |
| Token injecté `@Image 1` | Espace et casse conservés, nom lisible maintenu en chinois ; aucun alias ou index de remplacement |
| Pont livré en 3 s, surface limitée à 4 s minimum | Séparer génération et montage, conserver les deux bords et contrôler vitesse/phase/audio ; ne pas demander 3 s natives |
| Plan ancré avec déplacement caméra | Conserver le cadrage initial puis déplacer ; pas de verrou global incompatible, ni coupe induite par la seule présence d'une ancre |
| Logo produit ou texte demandé | Ne pas le supprimer avec « no text » ; exclure seulement les ajouts non voulus |
| Référence de mise en scène et plan fixe voulu | Garder l'immobilité ; ne pas généraliser les exemples Woo/Bay ni présenter une convention de style comme du droit |
| Prompt chinois avec self-eval | Explications dans la langue de conversation et prompt dans la langue choisie ; vérifier les deux séparément |
| « Texte seul » puis « seulement le prompt, sans explication » | Le premier exclut la génération d'assets ; le second impose une sortie limitée au prompt, avec contrôle interne et noms-token préservés |
| Personnage seul entre entrée, chaussée et caméra | Reconstruire la même disposition dans les deux plans ; chaque regard vise un endroit déterminé, y compris hors champ |
| Consigne absente, ambiguë, présente mais non suivie | Citer absence, deux lectures ou clause violée ; ne pas classer un symptôme comme absence sans lire le prompt testé |

Une réussite de rédaction vérifie le respect du contrat textuel sur ce cas.
Elle ne mesure ni la fiabilité vidéo, ni la supériorité d'une langue. Garder
les sorties d'essai et le rapport hors du skill ; ne pas charger tout cet
historique dans une demande ordinaire de prompt.

### Cas réel conservé : Ophélie, attente de 6 secondes

[Prompt original intégral](../assets/cases/ophelie-la-defense-6s-original.txt),
copie littérale du fichier `ophelie_la_defense_seedance_6s.txt` retrouvé avec le
clip `260910_0002_video_edit_2474.mp4`. Ce cas remplace une simple évocation
d'« attente retenue » lorsqu'on vérifie le diagnostic ; ne pas substituer un
prompt corrigé au texte testé. Ce n'est pas une référence de rendu approuvée.

Texte : 6 s, 9:16, deux plans de 3 s ; références `@ophelie`, `@def3`, `@def4`,
`@def1`, `@def2`, `@Etalo`. Fichier vidéo mesuré le 10 septembre 2026 :
720×1280, 24 images/s, durée de conteneur 6,048 s, H.264 avec piste AAC.
Ces métadonnées ne prouvent ni la requête envoyée ni les réglages de l'interface.
La correspondance fichier-token de la session n'a pas été réinspectée dans
l'interface. Les noms, rôle d'Etalo et exclusions du prompt restent inchangés.

Des planches de 24 images à intervalles de 0,25 s ont été examinées lors de la
revue. Le jeu, le son et le trafic ne sont pas validés par ces seules images.
Les observations antérieures retrouvées sont distinguées ci-dessous des
constats revérifiés ; ne pas convertir un retour rapporté en mesure causale.

| Défaut ou question | État de la preuve | Conclusion attendue du diagnostic |
|---|---|---|
| Pieds coupés dans le premier plan | Visible sur les images initiales examinées | « head to boots with space around her » et « Keep her whole body visible through the cut » existent. Non-respect du cadrage, pas consigne absente ; cause non isolée |
| Deuxième plan descendant à la taille | Ceinture/abdomen visibles sur les images du deuxième plan | « Chest-up » et « End still chest-up » sont présents, ainsi que le maintien global. Reconnaître la consigne non suivie ; ne pas ajouter trois synonymes de « chest-up » |
| Route derrière elle et regards latéraux | Route visible dans le premier plan ; problème de relation aux cibles signalé dans le diagnostic antérieur | Confronter « angled toward the avenue », « doors behind her », « curb side » et les deux arcs. La topologie et les cibles réelles ne sont pas complètement liées. Décrire les lectures possibles, sans inventer un croquis comme vérité de la source |
| Sens des voitures vers 1,5–2,5 s | Signalé dans le diagnostic antérieur ; pas confirmé par une inspection continue pendant cette revue | La circulation et les couleurs sont déjà écrites. Distinguer leur ambiguïté par rapport aux faces/trajectoires d'une consigne réellement violée ; suivre le même véhicule avant de conclure |
| Jeu perçu comme robotisé | Retour antérieur rapporté ; gestes et tours de tête existent dans les images | Ne pas écrire « aucun jeu dirigé » : tâche, montre, recherche, souffle et reprise de contrôle sont déjà présents. Qualité d'exécution, densité et causalité sont des hypothèses à examiner, sans cause prouvée |
| Proportions, notamment poitrine, réinterprétées | Retour antérieur rapporté ; comparaison de référence disponible, effet d'angle non isolé | Les clauses d'identité, costume et proportions existent. Comparer poses et angles avant de quantifier une dérive ou d'accuser la tenue d'être absente du texte |

Pour l'essai indépendant, transmettre le prompt brut et les observations
attribuées, pas cette colonne de conclusions. Attendre un diagnostic seul,
sans nouveau prompt ni génération. Il doit identifier au moins la différence
entre ambiguïté relationnelle et cadrage explicitement demandé mais non tenu.
Une cause non établie doit rester inconnue.

### Témoin cohérent et mutations minimales

[Témoin textuel cohérent](../assets/cases/attente-coherente-temoin.txt), créé
pour la vérification, **jamais présenté comme vidéo testée**. Entrée derrière,
route hors champ derrière la caméra, orientation du corps et cible hors champ
liées ; un seul plan fixe et une tenue calme explicite. Le lire sans retour de
rendu : aucune faiblesse matérielle démontrée doit pouvoir mener à « rien à
corriger ». Un risque générique d'exécution ne justifie pas une réécriture.

Produire au besoin deux copies temporaires hors du skill : retirer la position
de la route et la liaison de la cible pour le cas absent ; ajouter « the road
remains visible behind her throughout » pour le cas contradictoire. Vérifier
que le diagnostic change de classe pour cette seule mutation. Conserver le
témoin intact et ne pas imposer ces réponses au lecteur indépendant.
