# Rapport de vérification — S25-01

Dernière phase locale : [S25-08 — présentation et releases](#s25-08--présentation-et-releases-11-octobre-2026).
Les sections précédentes conservent leur état historique.

État constaté le **10 octobre 2026**, à la fin de la phase PATCH et avant le
premier commit. Ce rapport décrit cette phase ; il ne certifie aucune publication
future. Autorisation : `GO PATCH S25-01`, items I1 à I4. Licence MIT choisie
explicitement par l’utilisateur.

## Décision et résultat local

Créer un dépôt documentaire dédié, préserver le skill fourni et ajouter ce qui
sert sa distribution : licence, téléchargements, README bilingue, bannière,
contrôles et règles de travail communes. Le harnais reprend les principes
Mustang utiles ici, avec un périmètre local de session et les mêmes commandes de
tests en local et en CI. Il ne reproduit pas ses hooks, registres distants,
merge queue ni mécanismes de release.

Les **28 fichiers originaux sont identiques octet par octet**. La seule addition
au dossier du skill est `LICENSE`. Les deux téléchargements contiennent donc
**29 fichiers**. Le contenu du skill et ses déclencheurs n’ont pas été réécrits.

### Provenance et intégrité

| Objet | Preuve |
| --- | --- |
| Original `seedance-2-5.skill` | 177 522 octets, 28 entrées, CRC ZIP valide |
| SHA-256 de l’original | `b7690ab4a27a4f0eaa3b49252a51729b67eabb10a4cb2049b1e0b9b270d001cd` |
| Import | Comparaison des 28 entrées à leurs fichiers locaux : aucune différence |
| Chaque téléchargement | 419 506 octets, 29 entrées, CRC ZIP valide |
| SHA-256 du `.skill` et du `.zip` | `d5e2d8aee7ac26126dfa60e6027fcfd8705608bc39f216c8547be8b8ff5839f1` |
| Licence embarquée | Identique au `LICENSE` du dépôt |
| Reproductibilité | Deux fabrications fixées avant exécution, ordre d’entrée inversé : mêmes octets et même SHA-256 |

La comparaison d’import lit l’archive originale avec `zipfile.ZipFile` et
compare chaque `archive.read(name)` à `(root / 'skills' / name).read_bytes()`.
Elle a retourné `ORIGINAL_FILES 28 CHANGED []`. Le fichier original est resté
intact. Les archives nouvelles utilisent des dates fixes et des entrées ZIP
sans compression, pour éviter une dépendance au résultat d’une version de zlib.

## Fichiers créés

Les 42 fichiers ci-dessous sont les candidats exacts à versionner. Les fichiers
de session et les caches ignorés sont exclus du lot.

| Fichier | Rôle |
| --- | --- |
| `.gitignore` | Exclut état de session, secrets, caches et worktrees |
| `LICENSE` | Licence MIT autorisée |
| `README.md` | Présentation anglaise, téléchargement et trois parcours d’installation |
| `README.fr.md` | Version française équivalente |
| `assets/seedance-banner.svg` | Bannière originale avec texte alternatif et titre SVG |
| `AGENTS.md` | Règles communes de périmètre, confiance, validation et livraison |
| `CLAUDE.md` | Renvoi aux règles communes |
| `.github/workflows/check.yml` | Tests et contrôle du paquet, permissions de lecture, actions figées par SHA |
| `scripts/package_skill.py` | Fabrication ou contrôle en lecture seule des téléchargements |
| `tests/test_package_skill.py` | Dix tests déterministes dans des dossiers temporaires |
| `docs/verification.md` | Ce rapport, ses preuves et ses limites |
| `downloads/seedance-2-5.skill` | Archive installable avec licence |
| `downloads/seedance-2-5.zip` | Même archive, extension documentée pour l’import Claude |
| `skills/seedance-2-5/LICENSE` | Licence ajoutée au téléchargement |
| `skills/seedance-2-5/SKILL.md` | Noyau original, inchangé |
| `skills/seedance-2-5/agents/openai.yaml` | Métadonnées originales, inchangées |
| `skills/seedance-2-5/assets/icon.svg` | Icône originale, inchangée |
| `skills/seedance-2-5/assets/cases/attente-coherente-temoin.txt` | Cas original, inchangé |
| `skills/seedance-2-5/assets/cases/ophelie-la-defense-6s-original.txt` | Cas original, inchangé |
| `skills/seedance-2-5/references/00-quickref.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/01-write-shot.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/01b-motion-physics.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/01c-action.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/01d-duels.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/02a-perform.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/02b-perform-failures.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/02c-fine-performance.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/03-sequence.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/04-references.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/05-anchoring.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/06-edit-extend.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/07-spec.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/08-templates.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/09-diagnose.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/10-syntax.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/11-diagram.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/12-constraints.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/13-director.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/14-maintenance.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/15-camera-techniques.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/16-effects-mechanisms.md` | Fiche originale, inchangée |
| `skills/seedance-2-5/references/17-delivery.md` | Fiche originale, inchangée |

`.session-scope.json` conserve localement le plan, la session, la branche et les
chemins autorisés. Il est ignoré, comme les caches de Python et du linter.
Aucun fichier de Mustang ni de configuration personnelle n’a été édité par ce lot.

## Vérifications exécutées

| Commande ou contrôle | Résultat | Classe |
| --- | --- | --- |
| Tests avant implémentation | Échec attendu : module `package_skill` encore absent | EXÉCUTÉ_CONCLUANT pour l’absence initiale de l’outil, pas pour le comportement du skill |
| `python3 -B -m unittest discover -s tests -v` | 10/10, Python 3.14.3 | EXÉCUTÉ_CONCLUANT |
| `/usr/bin/python3 -B -m unittest discover -s tests -v` | 10/10, Python 3.12.3 | EXÉCUTÉ_CONCLUANT |
| `python3 -B scripts/package_skill.py` | Deux téléchargements fabriqués | EXÉCUTÉ_CONCLUANT |
| `python3 -B scripts/package_skill.py --check` | 29 sources, 59 liens locaux, deux archives conformes | EXÉCUTÉ_CONCLUANT |
| `/usr/bin/python3 -B scripts/package_skill.py --check` | Même résultat avec Python 3.12.3 | EXÉCUTÉ_CONCLUANT |
| `ruff check --no-cache scripts/package_skill.py tests/test_package_skill.py` | `All checks passed!`, Ruff 0.15.5 | EXÉCUTÉ_CONCLUANT |
| `ruff format --check scripts/package_skill.py tests/test_package_skill.py` | Deux fichiers déjà au format attendu | EXÉCUTÉ_CONCLUANT |
| `mypy --cache-dir /tmp/seedance-s25-mypy --strict scripts/package_skill.py tests/test_package_skill.py` | Aucun problème dans les deux fichiers, mypy 1.20.0 | EXÉCUTÉ_CONCLUANT |
| `compile()` des deux fichiers Python | Syntaxe valide, sans génération de fichier | EXÉCUTÉ_CONCLUANT |
| Lecture YAML avec PyYAML système et assertions | Déclencheurs CI, permissions, commandes, SHA et métadonnées conformes | EXÉCUTÉ_CONCLUANT pour les points vérifiés |
| `git diff --no-index --check /dev/null <fichier>` pour les 40 textes candidats | Aucun diagnostic d’espacement ; code 1 attendu car chaque fichier est nouveau | EXÉCUTÉ_CONCLUANT pour les diagnostics recherchés |
| Analyse XML de la bannière et capture locale avec Chromium headless shell | SVG valide, capture 1200 × 440 examinée | EXÉCUTÉ_CONCLUANT pour cette prévisualisation locale |
| Première tentative avec Chromium complet | Aucune capture produite ; processus de cette tentative arrêté | EXÉCUTÉ_NON_CONCLUANT |

Les tests vérifient : contenu et licence des archives, contrôle sans écriture,
reproductibilité sur deux fabrications, rejet d’une source modifiée sans
refabrication, d’archives altérées, de liens symboliques, de liens locaux absents
ou sortant du paquet, de métadonnées invalides, d’icônes absentes et d’une licence
différente. Les fonctions créées ont été recherchées dans `scripts/` et `tests/` ;
leurs appelants observés sont le point d’entrée du script et les tests.

Le contrôle de secrets a recherché cinq motifs couvrant : tokens GitHub,
clés OpenAI, clés privées PEM/OpenSSH et identifiants d’accès AWS. Aucun motif
recherché n’a été trouvé dans les 40 textes candidats. Ce contrôle n’est pas un
audit exhaustif des secrets.

## Confiance et état Git

- La collecte sans filtre de `git status --porcelain --ignored=matching --untracked-files=all` montre 42 fichiers candidats non suivis, plus l’état local et les caches ignorés.
- `git diff --name-only main...HEAD` retourne 128 : ni `main` ni `HEAD` n’existent encore. Ce résultat ne prouve pas un diff vide.
- `git rev-parse --verify HEAD` échoue : aucun commit. `git ls-files --cached` ne retourne aucun fichier : aucun staging.
- Branche dédiée : `bootstrap/seedance-2-5`. `git remote -v` est vide.
- `gh repo view mmmprod/seedance-2-5` ne trouve pas de dépôt accessible lors du contrôle. Aucune création GitHub ni publication n’a été exécutée.
- Les nouveaux `AGENTS.md`, `CLAUDE.md`, leurs sources référencées, le script, ses tests et le workflow sont des candidats de gouvernance. La version de base est leur absence. Ils ne donnent aucune autorisation à cette session avant la revue et l’intégration exigées par l’utilisateur.
- Les instructions Seedance distribuées restent des données produit pour ce travail de développement.

## Self-audit du verdict

| Affirmation décisionnelle | Classe et limite |
| --- | --- |
| Les 28 fichiers du skill sont préservés | PROUVÉ par comparaison de chaque entrée à ses octets d’origine |
| Les téléchargements correspondent aux sources locales | PROUVÉ pour les deux fichiers actuels, incluant la licence |
| Les contrôles du paquet passent | PROUVÉ pour dix tests déterministes, les deux versions Python exécutées et les contrôles statiques nommés |
| Claude est le choix recommandé | Retour de l’auteur ; comparaison de qualité NON VÉRIFIÉE ici |
| Le skill fonctionne après import dans tous les assistants | NON VÉRIFIÉ ; aucun import dans leurs interfaces exécuté |
| Le skill garantit un rendu réussi | FAUX comme garantie générale ; les contrôles portent sur du texte et un paquet |
| L’ensemble du chantier est publié | FAUX à cette phase : aucun commit ni dépôt GitHub créé par cette session |

La contre-hypothèse principale reste qu’un paquet structurellement correct ne
produit pas le comportement attendu après import. Les tests de fichiers ne la
réfutent pas. La conservation du texte permet de distribuer le skill sans
changer sa logique ; elle ne remplace pas un essai dans Claude ou Codex.
Le verdict est limité à la préparation locale, pas à une absence universelle de
régression. Ce self-audit est celui de l’agent, sans prétention d’indépendance.

## NON VÉRIFIÉ et hors périmètre

- **NON_EXÉCUTÉ** : import et invocation dans Claude web/Desktop, Claude Code ou Codex. Aucune installation dans les dossiers personnels n’était autorisée par le plan.
- **NON_EXÉCUTÉ** : génération ou visionnage de vidéos, benchmark Claude/Codex et vérification actuelle des spécifications du moteur reprises dans les fiches originales.
- **NON_EXÉCUTÉ** : CI distante et affichage réel sur GitHub, avant création/publication du dépôt.
- **NON_EXÉCUTÉ** : `actionlint`, outil absent. La syntaxe YAML et les invariants nommés ont été contrôlés avec l’outil système disponible ; cela ne certifie pas un run GitHub.
- Le script valide la forme YAML actuelle de `SKILL.md`, les champs nécessaires et les chemins d’icônes. Il ne remplace pas tous les schémas des assistants. Les commentaires `shortcut:` indiquent quand étendre ce contrôle.
- Les 59 liens contrôlés sont les chemins locaux des liens Markdown en ligne et HTML utilisés ici. Les ancres et la disponibilité des liens externes ne sont pas validées par ce script.
- Le harnais documente les frontières de travail ; aucun hook technique universel n’est installé par ce lot.

### Hook Git global préexistant

La configuration Git pointe vers `/home/mmmpr/.git-templates/hooks`. Son
`post-commit` a été lu, sans exécution ni modification. Il lance
`/home/mmmpr/.local/bin/cr review --type committed --base HEAD~1 --plain`, écrit
un journal temporaire, puis essaie d’en copier le contenu dans le presse-papiers
avec `wl-copy` ou `xclip`, et peut envoyer une notification locale si l’outil
correspondant est disponible.

Ce hook pourra donc lancer CodeRabbit et remplacer le presse-papiers lors de la
phase COMMIT. Il suppose aussi une base `HEAD~1`, qui n’existera pas pour le
premier commit d’un dépôt neuf. Son résultat est **NON VÉRIFIÉ** ; aucun bypass
ni correction globale n’est proposé dans ce périmètre.

## Lot de commits proposé, sans push

1. `chore: initialize repository foundation` : uniquement `.gitignore` et `LICENSE`.
2. Créer la référence locale `main` sur ce premier commit, en conservant la branche de session courante. Cette base minimale permettra une véritable Draft PR pour le contenu du skill.
3. `feat: publish Seedance skill and installation guide` : les 40 autres fichiers du catalogue, avec staging explicite de chaque chemin.

Ce lot n’a pas été exécuté. Il attend `GO COMMIT`, frontière COMMIT de V6.5.
Création du dépôt public, push et Draft PR seront une phase distincte. Aucun
merge, release, déploiement ni cleanup implicite.

## Sources de présentation et d’installation

- [Anthropic, installation des skills Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude), consulté le 10 octobre 2026.
- [Anthropic, skills Claude Code](https://code.claude.com/docs/en/skills), consulté le 10 octobre 2026.
- [OpenAI, skills Codex](https://learn.chatgpt.com/docs/build-skills), consulté le 10 octobre 2026.
- [Dietrich Gebert, Ponytail](https://github.com/DietrichGebert/ponytail), inspiration de présentation ; README consulté au commit `9b58c1ffb790c075ca32e70a89cf1d80588f4abf`. Aucun chiffre de benchmark ni image de Ponytail n’a été repris.


---

## Publication GitHub — constat du 10 octobre 2026

Autorisation : `GO DRAFT PR`. Les deux pushes normaux et la création de la
Draft PR ont été exécutés. Aucun merge, sortie de Draft, release ou cleanup.

### État publié et preuves

- Dépôt public : [mmmprod/seedance-2-5](https://github.com/mmmprod/seedance-2-5).
- [Draft PR #1](https://github.com/mmmprod/seedance-2-5/pull/1) : OPEN, `isDraft: true`, titre prévu, aucun label, 40 fichiers.
- Branche : `bootstrap/seedance-2-5`, HEAD `e804680e51275e2dc9aad50f28726aafc36e98aa`.
- Base : `main`, SHA `43d950dfaf4a6d7b4f79eb1a51d91dfbb0edd040`.
- `git ls-remote --heads origin` retourne exactement ces deux refs et SHA.
- `git status --porcelain --ignored=matching --untracked-files=all` : uniquement caches et état de session ignorés ; fichiers suivis propres.

### Vérifications exécutées

| Contrôle | Résultat | Classe et couverture |
| --- | --- | --- |
| `gh pr view 1 --repo mmmprod/seedance-2-5 --json ...` | Draft, base et HEAD exacts, 40 fichiers, labels vides | EXÉCUTÉ_CONCLUANT |
| [CI push, run 38075713510](https://github.com/mmmprod/seedance-2-5/actions/runs/38075713510) | `success`, SHA exact ; logs : `Ran 10 tests` et `OK: 29 source files; 59 local links; .skill and .zip checked` | EXÉCUTÉ_CONCLUANT |
| [CI pull_request, run 38075718508](https://github.com/mmmprod/seedance-2-5/actions/runs/38075718508) | Même résultat au même HEAD | EXÉCUTÉ_CONCLUANT |
| GET des deux archives, des deux README et de la bannière via raw.githubusercontent.com au SHA publié | HTTP 200 et octets identiques aux cinq fichiers locaux | EXÉCUTÉ_CONCLUANT |
| Contrôle ZIP des archives téléchargées | 419 506 octets chacune, 29 entrées, CRC valide | EXÉCUTÉ_CONCLUANT |
| Chromium headless sur la page GitHub de la branche, capture examinée | Bannière, titre, introduction, boutons et première table visibles | EXÉCUTÉ_CONCLUANT pour cette fenêtre 1440 × 2200, pas pour toutes les tailles |
| Lecture des commentaires et reviews de la PR | `reviews: []` ; CodeRabbit : `Draft PR not reviewed` | EXÉCUTÉ_CONCLUANT pour le skip observé, pas une revue réussie |

SHA-256 commun des deux archives publiques :
`d5e2d8aee7ac26126dfa60e6027fcfd8705608bc39f216c8547be8b8ff5839f1`.

La capture locale est `/tmp/seedance-s25-github-readme.png`. Elle ne constitue
pas un fichier publié dans le dépôt.

### Écart bloquant pour le téléchargement depuis les boutons

Le DOM GitHub confirme que les liens de `README.md:13`, `README.md:15`,
`README.md:56` et leurs équivalents `README.fr.md:13`, `README.fr.md:15`,
`README.fr.md:57` passent par `/blob/<référence>/...` et `?raw=true`.

Deux campagnes discriminantes de quatre routes ont été fixées avant chaque
exécution, avec un seul GET par route, sans relance jusqu'au premier vert :

| Route observée | Résultat |
| --- | --- |
| Les deux boutons réels, référence `bootstrap/seedance-2-5` | HTTP 503, page d'erreur GitHub, en-tête `Server: github.com` et identifiant de requête GitHub |
| Même ZIP via `/blob/e804680…/…?raw=true` | HTTP 200, redirection vers le service brut, mêmes octets |
| Même ZIP via raw.githubusercontent.com avec `/refs/heads/bootstrap/seedance-2-5/…` | HTTP 200, mêmes octets |
| Même `LICENSE` via `/blob/bootstrap/seedance-2-5/…?raw=true` et `/blob/main/…?raw=true` | HTTP 503 dans les deux cas |
| Page du ZIP via `/blob/bootstrap/seedance-2-5/…`, sans requête raw | HTTP 503 |
| ZIP via GitHub `/raw/refs/heads/bootstrap/seedance-2-5/…` | HTTP 200, mêmes octets |

Ces GET prouvent les réponses observées. La comparaison avec `main` réfute
l'hypothèse que le slash du nom de branche suffit à expliquer l'erreur ; la
page sans requête raw réfute aussi une explication limitée à `?raw=true`.
La cause interne du service GitHub est **NON TRANCHÉE** : ses logs ne sont pas
accessibles. Aucun défaut de contenu de l'archive n'est établi.


### Adresses de distribution

Les liens de téléchargement ciblent directement le service brut de la branche
`main`. Les archives ne sont pas encore sur cette branche au constat ci-dessus.
Le contrôle final sera deux GET, un par archive, après une fusion autorisée :
HTTP 200, CRC valide et octets exacts. Ce contrôle reste NON EXÉCUTÉ.

Imports Claude/Codex, vidéos et review CodeRabbit restent NON VÉRIFIÉS.

## Patch S25-03 — application locale

Autorisation reçue : `GO PATCH S25-03`, ITEM I6. Les trois changements locaux
sont les six URL des deux README et les preuves ajoutées à ce rapport. Les
URL ciblent désormais le service brut et la distribution de `main` ; elles
ne passent plus par le visualiseur `/blob/`.

| Vérification exécutée | Résultat | Classe et limite |
| --- | --- | --- |
| `python3 -B scripts/package_skill.py --check` | 29 sources, 53 liens locaux, deux archives conformes | EXÉCUTÉ_CONCLUANT pour la structure et les chemins locaux |
| Comparaison des deux README à `git show HEAD:<fichier>` | Exactement trois remplacements par README ; aucun autre texte changé | EXÉCUTÉ_CONCLUANT |
| Comparaison à l'archive Windows et contrôle SHA-256 | Les 28 fichiers originaux et le fichier fourni sont inchangés | EXÉCUTÉ_CONCLUANT |
| SHA-256 et CRC des deux téléchargements locaux | SHA-256 approuvé conservé, 29 entrées ZIP valides par archive | EXÉCUTÉ_CONCLUANT |
| `git diff --name-only` et `git diff --check` | Exactement `README.md`, `README.fr.md`, `docs/verification.md` ; aucun diagnostic d'espacement | EXÉCUTÉ_CONCLUANT |

Les six liens devenus externes expliquent le passage de 59 à 53 chemins locaux
contrôlés. Le script ne vérifie pas la disponibilité HTTP de ces nouveaux liens.
Tests unitaires, lint et vérification des types : **NON_EXÉCUTÉ** pour ce patch
documentaire ; aucun fichier Python, test ou workflow n'est modifié.

Le self-audit distingue la modification des adresses, **PROUVÉE** par le diff,
de leur disponibilité future sur `main`, **NON VÉRIFIÉE** avant fusion. Il
conserve la cause interne GitHub comme **NON TRANCHÉE** et ne conclut pas à une
correction du service GitHub ni à une absence universelle de régression.

Lot proposé : un commit `docs: use direct archive download URLs`, contenant
uniquement les trois documents nommés. Aucun staging, commit ou push exécuté
pour ce patch. Il attend `GO COMMIT`. Le contrôle HTTP final des deux archives
reste NON EXÉCUTÉ, avec le risque de liens indisponibles tant que `main` ne
contient pas les téléchargements.

---

## Patch S25-04 — compatibilité et validation, 10 octobre 2026

Autorisation : `GO PATCH S25-04`, items I7 et I8. Cette section décrit le
patch local ; les constats S25-01 et S25-03 ci-dessus sont des snapshots
historiques, avec leurs anciennes empreintes. Aucun commit, staging, push,
commentaire de review ou résolution de fil n'est exécuté dans cette phase.

### Causes établies avant correction

**P2 — présentation Codex ignorée.** La ligne `  - api` venait du fichier
fourni, à `agents/openai.yaml:10` au HEAD `f419b71`. Le contrôle du paquet ne
vérifiait pas les produits. OpenAI, version `rust-v0.162.1` publiée le
9 octobre 2026, commit `092d3acd6bec3e3a14bdc7e7a2810ab628ab759d` :
[Product](https://github.com/openai/codex/blob/092d3acd6bec3e3a14bdc7e7a2810ab628ab759d/codex-rs/protocol/src/protocol.rs#L3852)
admet seulement `chatgpt`, `codex`, `atlas` et leurs alias majuscules. Le
[chargeur](https://github.com/openai/codex/blob/092d3acd6bec3e3a14bdc7e7a2810ab628ab759d/codex-rs/ext/skills/src/loader/metadata.rs#L130)
retourne les métadonnées par défaut si cette désérialisation échoue.
Ces sources ont été consultées le 10 octobre 2026 ; la version du binaire
local inspecté est `codex-cli 0.162.1`. Les instructions `SKILL.md` restent
chargeables : le défaut porte sur les métadonnées facultatives, pas sur
l'intégralité du skill.

La correction retire exactement cette ligne et contrôle les produits déclarés
dans la forme YAML actuelle. La liste distribuée respecte l'énumération
inspectée ; cela ne prouve pas un import réel dans l'application.

**P3 — cible de lien tronquée.** L'expression régulière de `check_links:29`
au HEAD précédent arrêtait la destination au premier `)`. Deux fichiers
complets existants, avec parenthèses simples et imbriquées, étaient rejetés.
Une cible complète manquante était acceptée si son préfixe tronqué existait.
Le correctif compte les parenthèses dans la destination avant de vérifier
le chemin complet. [CommonMark 0.31.2](https://spec.commonmark.org/0.31.2/#links),
John MacFarlane, 28 janvier 2024, autorise ces destinations équilibrées.

Le helper partagé reste appelé par `collect_source:70` pour les Markdown du
skill et par `run:165` pour les deux README et ce rapport. La recherche
`rg --no-config -n --hidden` a aussi recensé le point d'entrée du script, les
tests, la commande CI, les commandes des README et le guide de gouvernance
proposé. Les signatures existantes et le format ZIP restent inchangés ;
aucune dépendance ni API exposée n'est ajoutée.

### Fichiers modifiés

| Fichier | Modification |
| --- | --- |
| [agents/openai.yaml](../skills/seedance-2-5/agents/openai.yaml#L6) | Retrait de la seule valeur `api` ; icônes et invocation implicite conservées |
| [scripts/package_skill.py](../scripts/package_skill.py#L26) | Contrôle des produits à partir de la ligne 96 et destinations complètes à partir de la ligne 26 |
| [tests/test_package_skill.py](../tests/test_package_skill.py#L158) | Six tests ajoutés ; les dix tests existants restent identiques dans leur arbre syntaxique Python |
| [downloads/seedance-2-5.skill](../downloads/seedance-2-5.skill) | Archive reconstruite avec la seule ligne Codex corrigée et la licence existante |
| [downloads/seedance-2-5.zip](../downloads/seedance-2-5.zip) | Même archive, mêmes octets |
| `docs/verification.md` | Preuves, limites et constats hors périmètre ajoutés dans cette section |

Le fichier `.session-scope.json`, ignoré, enregistre I7/I8 et leurs chemins
exacts. AGENTS/CLAUDE et les sources de gouvernance proposées dans la branche
restent sans autorité avant la revue et l'intégration exigées par l'utilisateur.
Aucune autre modification suivie n'est incluse dans ce patch.

### Vérifications exécutées

Les six tests ont été ajoutés avant toute modification du validateur. Un run
fixé contre le code précédent donne `Ran 16 tests`,
`FAILED (failures=5, errors=2)` : les dix tests existants passent ; deux
produits inconnus et deux formes YAML non couvertes sont acceptés à tort,
le préfixe existant masque la cible absente, et les deux fichiers complets
existants produisent une erreur. Le journal local est
`/tmp/seedance-S25-04-before-tests.log`. Aucun run-until-green.

| Commande ou contrôle | Résultat | Classe et couverture |
| --- | --- | --- |
| `python3 -B -m unittest discover -s tests -v`, avant correctif | Rouge discriminant décrit ci-dessus | EXÉCUTÉ_CONCLUANT pour les défauts du validateur |
| `python3 -B -m unittest discover -s tests -v`, après correctif | 16/16, Python 3.14.3 | EXÉCUTÉ_CONCLUANT |
| `/usr/bin/python3 -B -m unittest discover -s tests -v` | 16/16, Python 3.12.3 | EXÉCUTÉ_CONCLUANT |
| `ruff check --no-cache scripts/package_skill.py tests/test_package_skill.py` | `All checks passed!`, Ruff 0.15.5 | EXÉCUTÉ_CONCLUANT |
| `ruff format --check scripts/package_skill.py tests/test_package_skill.py` | Deux fichiers au format attendu | EXÉCUTÉ_CONCLUANT |
| `mypy --cache-dir /tmp/seedance-s25-mypy --strict scripts/package_skill.py tests/test_package_skill.py` | Aucun problème dans les deux fichiers, mypy 1.20.0 | EXÉCUTÉ_CONCLUANT |
| `python3 -B scripts/package_skill.py`, exactement deux builds fixés | Même SHA-256 aux deux builds | EXÉCUTÉ_CONCLUANT |
| `python3 -B scripts/package_skill.py --check` | 29 sources et deux archives conformes ; chemins locaux du skill et des trois documents contrôlés | EXÉCUTÉ_CONCLUANT pour ce paquet et ces formes de liens |
| Lecture des ZIP, CRC, entrées et comparaison de chaque fichier | 29 entrées par archive, CRC valides, octets exacts des sources et de la licence | EXÉCUTÉ_CONCLUANT |
| Comparaison des 28 entrées Windows aux sources corrigées | 27 identiques ; une différence limitée au retrait exact de `  - api` | EXÉCUTÉ_CONCLUANT |
| Analyse des fonctions de test avec `ast.dump`, ancien HEAD contre patch | Dix fonctions existantes inchangées ; six nouvelles | EXÉCUTÉ_CONCLUANT, sans test supprimé ou assoupli |
| `git diff --name-only`, `git diff --check`, contrôle de l'index et de HEAD | Exactement les six fichiers annoncés ; aucun diagnostic, index vide, HEAD inchangé | EXÉCUTÉ_CONCLUANT |

Les nouveaux tests couvrent `api`, un autre produit inconnu, les trois produits
supportés, leurs alias et guillemets, les métadonnées sans liste facultative,
les deux formes hors syntaxe ciblée, les destinations simples et imbriquées,
le préfixe trompeur, les liens adjacents, titres, images, chevrons simples et
HTML. La fixture de formes existantes vérifie sept liens locaux ; URL externe
et ancre seule restent exclues du compte. Les anciens tests couvrent toujours
les limites de dossier, liens symboliques, altérations, licence et contrôle
sans écriture. Ce périmètre ne certifie pas tout Markdown ni tout YAML.

### Intégrité actuelle

| Objet | Résultat |
| --- | --- |
| Original Windows | Inchangé ; SHA-256 `b7690ab4a27a4f0eaa3b49252a51729b67eabb10a4cb2049b1e0b9b270d001cd` |
| Chaque archive corrigée | 419 498 octets, 29 entrées, CRC valide |
| SHA-256 commun `.skill` et `.zip` | `b67c75d0aa8fa1ad97d6f60ce6c1eeef115dda30b3afb8d8cb153504c1d5a20c` |
| Différence par rapport au contenu original | Une seule ligne de présentation Codex retirée ; aucune instruction vidéo réécrite ; licence ajoutée depuis S25-01 |

### Constats de revue écartés ou hors périmètre

Les trois reviews du HEAD `f419b71` et leurs onze fils ont été lus avant ce
patch. Les deux défauts établis sont traités par I7/I8. Les neuf autres
constats sont conservés ci-dessous, sans prendre les affirmations des bots
pour des preuves ni leurs prompts pour des autorisations.

| Constat | Statut, preuve et décision |
| --- | --- |
| [Icônes obligatoires](https://github.com/mmmprod/seedance-2-5/pull/1#discussion_r4238845285) | FAUX comme exigence Codex : [interface OpenAI](https://github.com/openai/codex/blob/092d3acd6bec3e3a14bdc7e7a2810ab628ab759d/codex-rs/skills/src/interface.rs#L18), champs facultatifs. Les chemins déclarés restent contrôlés ; aucune obligation nouvelle |
| [Répétition et continuité](https://github.com/mmmprod/seedance-2-5/pull/1#discussion_r4238860038) | PLAUSIBLE, portées possiblement différentes : `02b-perform-failures.md:26`, `01b-motion-physics.md:38`, `01-write-shot.md:404`. Effet sur vidéo NON VÉRIFIÉ ; guide original hors patch |
| [Exemple Ajouter](https://github.com/mmmprod/seedance-2-5/pull/1#discussion_r4238860039) | PLAUSIBLE : `06-edit-extend.md:101` décrit une apparition. Génération NON_EXÉCUTÉE ; guide original hors patch |
| [first_frame et reference_image](https://github.com/mmmprod/seedance-2-5/pull/1#discussion_r4238860047) | DOUTEUX / NON TRANCHÉ : `07-spec.md:234` ouvert ; page BytePlus consultée, règles techniques non extraites. Aucun job API ; hors patch |
| [Réutilisation pendant 30 jours](https://github.com/mmmprod/seedance-2-5/pull/1#discussion_r4238860051) | NON VÉRIFIÉ : `07-spec.md:313` ouvert ; règles par surface non établies à partir de la page consultée. Hors patch |
| [Plafonds vidéo/audio](https://github.com/mmmprod/seedance-2-5/pull/1#discussion_r4238860056) | NON VÉRIFIÉ : `09-diagnose.md:154` ouvert ; page Volcengine ne fournit qu'un avis JavaScript. Aucun job API ; hors patch |
| [Chevrons de rôles](https://github.com/mmmprod/seedance-2-5/pull/1#discussion_r4238860063) | PLAUSIBLE dans `10-syntax.md:320` et `12-constraints.md:220`, priorité au token réel donnée dans `10-syntax.md:27`. Les identifiants allégués sont absents des lignes `08-templates.md:405–413` citées. Effet NON VÉRIFIÉ ; hors patch |
| [Compteur sans symptôme](https://github.com/mmmprod/seedance-2-5/pull/1#discussion_r4238860066) | PLAUSIBLE : `17-delivery.md:65` et `09-diagnose.md:93–100`. Le contexte peut contenir le symptôme ; aucune session applicative exécutée. Hors patch |
| [Paragraphe après tableau](https://github.com/mmmprod/seedance-2-5/pull/1#discussion_r4238860070) | PLAUSIBLE : `17-delivery.md:146`, pas de ligne vide ; rendu de cette référence NON_EXÉCUTÉ. Pas de markdownlint exécuté ici ; hors patch |

Sources consultées le 10 octobre 2026 pour les constats API :
[BytePlus](https://docs.byteplus.com/zh-CN/docs/modelark/create-video-generation-task-api),
page datée du 8 octobre 2026, et
[Volcengine](https://docs.volcengine.com/docs/ark/seedance-2-5?lang=zh).
Leur contenu extrait n'établit pas les restrictions alléguées.

### Self-audit et limites

| Affirmation décisionnelle | Classe et couverture |
| --- | --- |
| La liste corrigée respecte Product de Codex 0.162.1 | PROUVÉ pour l'énumération officielle inspectée et les octets distribués ; import applicatif NON_EXÉCUTÉ |
| Un produit inconnu est rejeté | PROUVÉ pour les valeurs et la forme YAML testées ; pas un parseur YAML complet |
| Le préfixe existant ne masque plus la cible complète absente | PROUVÉ par un test discriminant rouge puis vert ; deux cibles complètes existantes également acceptées |
| Les dix tests antérieurs sont conservés et passent | PROUVÉ par comparaison syntaxique et les deux suites exécutées |
| Les 28 fichiers originaux sont tous inchangés après S25-04 | FAUX : 27 sont identiques, la ligne `api` du 28e est retirée explicitement |
| Aucune régression sur toutes les surfaces Claude/Codex | INVÉRIFIABLE avec cette couverture ; aucune telle garantie n'est revendiquée |
| Le patch S25-04 est déjà publié sur main | FAUX à cette phase : HEAD distant et base restent ceux constatés avant patch |

La contre-hypothèse d'un vert obtenu en assouplissant les tests est réfutée par
les dix fonctions antérieures inchangées et les nouveaux cas rouges avant
correctif. Celle d'une réécriture silencieuse du skill est réfutée par la
comparaison des 28 entrées à l'original. La contre-hypothèse d'un défaut à
l'import reste ouverte : un paquet conforme à l'énumération et aux fichiers
ne remplace pas un essai dans chaque assistant. Ce self-audit est celui de
l'agent, sans prétention d'indépendance.

**NON_EXÉCUTÉ / NON VÉRIFIÉ** : imports et invocations Claude/Codex, vidéos,
benchmark, règles API des guides, rendu mobile et du tableau signalé, CI du
nouveau patch local et deux GET finaux sur `main`. Les CI déjà vertes portent
sur `f419b71`, pas sur ces nouvelles modifications. Le contrôle HTTP reste
exactement deux GET après une fusion autorisée, un par archive, sans retry,
avec la nouvelle empreinte ci-dessus.

Limites ciblées : le contrôle produit attend `policy` à la racine,
`products` indenté de deux espaces et des éléments `  - valeur`. Une syntaxe
avec commentaires intercalés, ancres, doublons ou autres formes exige
l'extension du contrôle avant d'en revendiquer la couverture. Les liens
Markdown gérés sont en ligne, sans échappements ni définitions de référence ;
les ancres et la disponibilité des URL externes ne sont pas validées.
Aucun parseur général ni dépendance n'est ajouté.

### Phase suivante

Un seul commit atomique proposé : `fix: validate Codex metadata and Markdown links`,
avec uniquement les six fichiers du tableau. Il attend `GO COMMIT`, frontière
COMMIT de V6.5. Aucun push couvert par ce token. La PR #1 reste ouverte et
sortie de Draft au HEAD précédent ; la fusion reste différée. Après publication
du nouveau HEAD, elle doit être réévaluée avec ce nouveau contenu.
Les téléchargements de `main` restent indisponibles tant que les archives ne
sont pas fusionnées ; le contrôle HTTP final n'a pas été exécuté.

## S25-05 — transfert vers MMMProd-Org — 10 octobre 2026

Instantané après transfert et correction locale, avant le commit et la publication
sur `main`. Autorisation directe : `GO PATCH S25-05`, items I9 et I10, contrat
NORMAL. Les phases précédentes restent des instantanés datés : la PR #1 est
maintenant fusionnée et les téléchargements de `main` sont disponibles.

### Propriétaire, historique et raccordement local

Un seul POST a été exécuté, sans second essai :

```sh
gh api --method POST repos/mmmprod/seedance-2-5/transfer -f new_owner=MMMProd-Org
```

Réponse HTTP 202 à 20:55:48 UTC ; transfert confirmé par GET à 20:56:13 UTC.
L'API retourne l'ID **1413525906**, `full_name: MMMProd-Org/seedance-2-5`,
`owner.type: Organization`, `private: false` et la branche par défaut `main`.
[Identité actuelle du dépôt](https://api.github.com/repos/MMMProd-Org/seedance-2-5).

| Contrôle avant / après | Résultat observé |
| --- | --- |
| `main` | `c6c0db03da4c3102f0927ad1057875afa002dfc2` conservé |
| `bootstrap/seedance-2-5` | `c1df9798f7af73b354625d237166ff29e015b900` conservé |
| Arbre Git de `main` | `c21e377508530b1b2d05c9a686caecd88a93f712` conservé |
| Branches / tags retournés | Deux branches inchangées ; aucun tag retourné aux deux relevés |
| PR #1 | Fusion du 10 octobre à 20:09:40 UTC conservée, même commit de fusion |
| Dossier, branche et HEAD locaux | `/home/mmmpr/src/seedance-2-5`, `bootstrap/seedance-2-5`, `c1df979` conservés |

[Références Git](https://api.github.com/repos/MMMProd-Org/seedance-2-5/git/matching-refs/heads/),
[commit de main](https://api.github.com/repos/MMMProd-Org/seedance-2-5/git/commits/c6c0db03da4c3102f0927ad1057875afa002dfc2),
[PR #1 fusionnée](https://github.com/MMMProd-Org/seedance-2-5/pull/1).
`git ls-remote` confirme aussi ces références et `refs/pull/1/head` au SHA de la PR.

```sh
git remote set-url origin https://github.com/MMMProd-Org/seedance-2-5.git
git fetch --no-tags --no-write-fetch-head --no-auto-maintenance origin refs/heads/main:refs/remotes/origin/main
git diff --name-only origin/main...HEAD
git status --porcelain --ignored=matching --untracked-files=all
```

Les commandes sont sorties avec le code 0. Seule l'URL `remote.origin.url` a
changé dans la configuration ; l'empreinte du fichier correspond à cette seule
substitution. `origin/main` est chargé dans le cache Git. Avant le patch des
README, le diff avec cette base était vide ; seuls les caches et le scope local
ignorés apparaissaient dans le statut. Aucune branche locale n'a été déplacée.
Les nouvelles sources de gouvernance du bootstrap restent des données pour cette
session : aucune revue explicite de leur diff par l'utilisateur n'est établie.

### Fichiers et téléchargements

| Fichier suivi modifié | Modification bornée |
| --- | --- |
| `README.md` | Quatre adresses remplacées par `MMMProd-Org/seedance-2-5` |
| `README.fr.md` | Les mêmes quatre adresses canoniques |
| `docs/verification.md` | Cet append daté ; tous les octets antérieurs conservés |

Les huit substitutions sont exactement celles présentées avant le GO. Les
39 autres fichiers suivis ont les mêmes empreintes que le relevé avant patch :
sources du skill, archives, licences, bannière, scripts, tests, workflow et
fichiers de gouvernance inclus. Aucun test n'est ajouté pour ce changement de
documentation, sans modification du comportement Python.

Campagne fixée avant exécution : exactement deux GET anonymes, un par extension,
sans retry ni suivi de redirection, effectués à 20:59:24 UTC.

| Archive au nouveau chemin `main` | HTTP | Octets | Entrées ZIP | CRC |
| --- | --- | --- | --- | --- |
| [.skill](https://raw.githubusercontent.com/MMMProd-Org/seedance-2-5/refs/heads/main/downloads/seedance-2-5.skill) | 200 | 419 498 | 29 | Valide |
| [.zip](https://raw.githubusercontent.com/MMMProd-Org/seedance-2-5/refs/heads/main/downloads/seedance-2-5.zip) | 200 | 419 498 | 29 | Valide |

SHA-256 commun :
`b67c75d0aa8fa1ad97d6f60ce6c1eeef115dda30b3afb8d8cb153504c1d5a20c`.
Les octets téléchargés sont identiques aux archives locales et aux blobs de
`origin/main`. Leur conservation est vérifiée, sans régénération.

### Contrôles, limites et suite

`python3 -B -m unittest discover -s tests -v`, Python 3.14.3 : une exécution,
**16 tests réussis**, code de sortie 0. Log local :
`/tmp/seedance-S25-05-unittest.log`.

Les endpoints Actions du dépôt transféré retournent `enabled: true`,
`allowed_actions: all`, `default_workflow_permissions: read` et
`can_approve_pull_request_reviews: false`. L'endpoint des rulesets retourne une
liste vide ; ce relevé ne couvre pas toutes les éventuelles politiques
d'entreprise. Les applications de l'Org configurées pour tous ses dépôts étaient
explicitement incluses dans I9 ; aucun réglage global ni installation d'application
n'a été effectué par l'agent.

[CodeQL Setup #38085672177](https://github.com/MMMProd-Org/seedance-2-5/actions/runs/38085672177),
événement `dynamic` après transfert sur `c6c0db0` : SUCCESS. Le workflow du skill
sur `main` avait déjà réussi avant transfert :
[Skill checks #38082642373](https://github.com/MMMProd-Org/seedance-2-5/actions/runs/38082642373).
La nouvelle CI du patch README attend un push autorisé par `GO DRAFT PR` ; elle
reste NON_EXÉCUTÉE à cet instantané.

NON_EXÉCUTÉ / NON VÉRIFIÉ : lint et contrôle de types pour S25-05 (aucun Python
modifié), imports/invocations Claude et Codex, génération et qualité vidéo,
benchmark comparatif, règles API des guides et nouvelle revue complète des bots.
Les huit constats historiques sur les guides restent hors périmètre. La liste
d'installations de l'Org n'inclut pas CodeRabbit ; son fonctionnement futur reste
NON VÉRIFIÉ. Aucune garantie générale d'absence de régression n'est déduite de
cette couverture des fichiers, du paquet, des liens et des tests existants.

Le transfert est effectif ; la correction des README est encore locale.
Un seul commit de documentation sera proposé, puis une Draft PR sous l'Org.
Les gates COMMIT et DRAFT PR restent requis ; aucune fusion, suppression de
branche ou transfert inverse n'est autorisé par ce GO PATCH. Recréer un dépôt
au chemin personnel supprimerait les redirections décrites par GitHub.
Sources : GitHub Docs, consulté le 10 octobre 2026,
[transfert de dépôt](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)
et [réponse REST asynchrone](https://docs.github.com/en/rest/repos/repos#transfer-a-repository).

Contrôle final du paquet après ajout de cet append :
`python3 -B scripts/package_skill.py --check`. Son résultat est consigné ci-dessous
après exécution, sans résultat anticipé.

Résultat exécuté le 2026-10-10T21:01:43.150172+00:00, code de sortie 0,
une seule exécution :

```text
OK: 29 source files; 58 local links; .skill and .zip checked
```

## S25-08 — Présentation et releases, 11 octobre 2026

Contrat **NORMAL**. Autorisation directe de l’utilisateur : **GO PATCH S25-08**,
items **I13, I14, I15, I16**. Cette phase prépare le code et la configuration ;
aucun commit, push, merge ou lancement manuel de release n’est autorisé ici.
La permission contents: write du seul job publish est l’item explicite I15.

### Cause établie et décision

Avant ce patch, le paquet avait 29 entrées sans VERSION et le workflow exécutait
uniquement les tests et la comparaison du paquet. Les liens de téléchargement
des README pointaient sur main. Le numéro 2.5 identifiait le modèle, pas une
distribution conservée. Le code lu avant modification et la photo locale
S25-08 établissent cette absence ; elle n’est pas déduite d’un badge.

La version du skill est maintenant **1.0.0**, enregistrée dans
[VERSION](../skills/seedance-2-5/VERSION) et contrôlée par
[parse_version](../scripts/package_skill.py#L16). Le test déterministe avant
correction a produit sept échecs : absence de VERSION et six formes invalides
acceptées. Les mêmes cas passent après correction, sans assouplir leurs assertions.

La présentation reprend de Ponytail une bannière originale, une entrée courte,
des badges et des exemples visibles. Les parcours Claude, Claude Code, Codex,
Windows et WSL sont conservés. Le lien de release devient le téléchargement
principal ; le lien direct vers le ZIP de main reste visible comme secours.
Le bouton principal est du texte et fonctionne sans son hébergeur de badges.
L’amélioration esthétique reste un jugement de design, pas une mesure.

### Fichiers modifiés

| Fichier | Changement |
| --- | --- |
| [README.md](../README.md) | Présentation anglaise, installations repliables, version, téléchargement et secours |
| [README.fr.md](../README.fr.md) | Même présentation et parcours en français |
| [assets/seedance-banner.svg](../assets/seedance-banner.svg) | Illustration originale avec titre et description accessibles |
| [skills/seedance-2-5/VERSION](../skills/seedance-2-5/VERSION) | Source unique du numéro 1.0.0, ajoutée au dossier installé |
| [scripts/package_skill.py](../scripts/package_skill.py) | Validation obligatoire de VERSION, contrat run et noms d’archives conservés |
| [tests/test_package_skill.py](../tests/test_package_skill.py) | Trois tests de version ; fixture complétée ; seize tests antérieurs conservés |
| [downloads/seedance-2-5.skill](../downloads/seedance-2-5.skill) | Archive reconstruite, ajout de VERSION |
| [downloads/seedance-2-5.zip](../downloads/seedance-2-5.zip) | Mêmes octets que le fichier .skill |
| [.github/workflows/check.yml](../.github/workflows/check.yml) | Contrôle du numéro et publication après les checks, sur main de cette Org |
| [scripts/release_skill.py](../scripts/release_skill.py) | Harnais de contrôle, brouillon, fichiers, publication et preuve finale |
| [tests/test_release_skill.py](../tests/test_release_skill.py) | Vingt-quatre tests de publication avec GitHub simulé et Git temporaire |
| [docs/releasing.md](releasing.md) | Procédure de préparation, publication automatique et reprise d’une interruption |
| docs/verification.md | Résultats et limites de cette phase |
| .session-scope.json, ignoré | Périmètre des quatorze chemins et preuve du GO ; aucun staging |

Les scripts et le workflow modifiés sont des propositions de gouvernance,
pas une nouvelle autorisation. AGENTS.md et CLAUDE.md sont inchangés.
Le scope ne remplace jamais une instruction de l’utilisateur.

### Publication prévue par le code

Le [contrôle de transition](../scripts/release_skill.py#L214) refuse un numéro
en recul ou réutilisé après changement du skill ou des archives. Le contrôle
local --check ne publie rien et n’appelle pas le réseau. Sur une PR, la base
est fournie par le workflow ; sur main, la comparaison utilise le premier parent.

Le [job publish](../.github/workflows/check.yml#L37) dépend du succès du job
check. Il est réservé à un push sur main de MMMProd-Org/seedance-2-5, avec
contents: write pour ce job seulement, le jeton natif et le checkout du SHA testé.
La concurrence conserve les commits main distincts et sérialise par version.
Aucune permission globale, dépendance ou nouveau secret n’est ajouté.

Le [publisher](../scripts/release_skill.py#L293) prépare un brouillon ciblant ce
commit, téléverse ZIP, .skill et SHA256SUMS, puis compare les fichiers téléchargés
avant et après publication. Un tag seul ou un brouillon ne suffit pas à annoncer
une publication. La demande utilise la politique native make_latest: legacy.
Les tests prouvent cette demande, pas le choix distant effectivement effectué.

Une release publique identique est contrôlée sans écriture. Un brouillon du
même commit reprend uniquement les fichiers manquants. Un contenu contradictoire,
une erreur de permission, un fichier incomplet ou un autre commit provoque un
échec explicite ; aucun fichier ou tag existant n’est remplacé.

### Vérifications exécutées

| Commande ou contrôle | Résultat et couverture | Classe |
| --- | --- | --- |
| python3 -B -m unittest discover -s tests -p test_package_skill.py -v, avant correction | 19 tests, 7 échecs attendus : validation de VERSION absente | EXÉCUTÉ_CONCLUANT pour la reproduction |
| python3 -B -m unittest discover -s tests -v, avant le dernier test sans écriture | 42 tests passent : 19 paquet, 23 publication ; aucune mutation GitHub | EXÉCUTÉ_CONCLUANT pour ces cas |
| /usr/bin/python3 -B -m unittest discover -s tests -v | 43 tests passent sous Python 3.12.3, version majeure/mineure du workflow | EXÉCUTÉ_CONCLUANT pour ces cas |
| python3 -B -m unittest discover -s tests -p test_release_skill.py -k never_changes -v | Contrôle de version sans changement des octets ni mtimes, index Git inclus, sur le dépôt temporaire | EXÉCUTÉ_CONCLUANT pour ce cas |
| python3 -B scripts/package_skill.py | Deux archives reconstruites avec VERSION ; 30 sources | EXÉCUTÉ_CONCLUANT |
| python3 -B scripts/package_skill.py --check, avant cet append | 30 sources, 60 liens locaux, archives conformes ; résultat final ci-dessous | EXÉCUTÉ_CONCLUANT |
| python3 -B scripts/release_skill.py --check --base 7329444a2652a35741497c2299f87e875a7aa7f2 | 1.0.0 ; contrôle local sans publication | EXÉCUTÉ_CONCLUANT |
| ruff check --no-cache, sur les quatre fichiers Python | All checks passed! | EXÉCUTÉ_CONCLUANT |
| ruff format --no-cache --check, sur les mêmes fichiers | 4 files already formatted | EXÉCUTÉ_CONCLUANT |
| mypy --strict --cache-dir /tmp/seedance-S25-08-mypy, sur les mêmes fichiers | Success: no issues found in 4 source files | EXÉCUTÉ_CONCLUANT |
| Comparaison SHA-256 des 42 fichiers suivis initiaux | Les 29 anciennes sources du skill sont identiques ; aucun écart suivi hors périmètre | EXÉCUTÉ_CONCLUANT pour cette couverture |
| Comparaison des arbres syntaxiques des seize tests antérieurs | Les seize corps de tests sont identiques | EXÉCUTÉ_CONCLUANT |
| Inspection ZIP et .skill | 419620 octets chacun ; 30 entrées ; CRC valide ; VERSION = 1.0.0 | EXÉCUTÉ_CONCLUANT |
| YAML 1.2 avec la bibliothèque yaml déjà installée | Syntaxe, dépendance des jobs, garde Org/main/push, permissions, concurrence et actions épinglées contrôlées | EXÉCUTÉ_CONCLUANT pour ces assertions ; aucun run Actions |
| API Markdown GitHub, les deux README finaux | Deux rendus HTML, quatre blocs details chacun, lien texte et secours présents | EXÉCUTÉ_CONCLUANT sur le balisage |
| Playwright installé, trois captures finales | Sombre anglais et clair français à 1100 px, sombre français à 390 px ; bannière chargée ; pas de dépassement de page, Codex ouvert compris | EXÉCUTÉ_CONCLUANT sur le rendu local |
| GitHub.release et GitHub.tag_sha du nouveau harnais, lectures réelles de v1.0.0 | Release et tag absents, réponses traitées sans écriture | EXÉCUTÉ_CONCLUANT pour ces lectures |
| gh api repos/MMMProd-Org/seedance-2-5/commits/main | main reste 7329444a2652a35741497c2299f87e875a7aa7f2 | EXÉCUTÉ_CONCLUANT pour cette lecture |
| gh pr list --repo MMMProd-Org/seedance-2-5 --state open | Liste vide | EXÉCUTÉ_CONCLUANT pour cette lecture |

SHA-256 identique des deux archives :
4a99dd7a593fe468663d35f18325d9617f8084b119d284dff41ca62b9c32d51b.
SKILL.md conserve 0aebf227b9d33cb3ef3e513b7e3b4539a5f1c4583de6131636ce576ff65f22bb.

### NON VÉRIFIÉ, risques et hors périmètre

- Publication réelle v1.0.0, téléversement/API en écriture, réception binaire
  distante, sélection de latest et CI du nouveau patch : intégration future
  nécessaire. Aucun tag, release ni mutation de PR n’a été exécuté ici.
- Affichage public GitHub et badges distants : captures à CSS local ; images
  externes bloquées pour ces captures. Les tentatives antérieures renvoyaient
  HTTP 403, dont la cause n’est pas établie. Aucun badge vert fictif n’est ajouté.
- actionlint n’est pas installé ; le contrôle YAML et les assertions locales
  ne remplacent pas son analyse ni une exécution GitHub Actions.
- Import réel Claude/Codex et qualité vidéo : non testés ; les vingt-trois guides
  et les deux cas source restent hors périmètre. Les huit questions historiques
  de S25-04 ne sont pas réauditées et ne sont pas déclarées résolues.

Risques restants : la future publication écrit des tags/releases avec le jeton
du job ; une erreur API peut laisser un brouillon. La reprise contrôlée et le
téléchargement direct de secours limitent les conséquences. La configuration
doit encore être intégrée et le résultat réel prouvé ; ce patch ne certifie
aucune absence générale de régression dans les assistants ou le moteur vidéo.

Le dépôt ciblé reste sur bootstrap/seedance-2-5 à
31c8000eb404d1709426652b17199a0ed9a5fc66 ; l’index de ce dépôt est vide.
Les commits créés par les fixtures de tests concernent uniquement leurs dépôts
temporaires, pas ce dépôt. Le contrôle final et son résultat sont enregistrés
après cet append.

Contrôle final exécuté le 2026-10-10T22:57:40.577232+00:00, sorties 0 :

```text
python3 -B -m unittest discover -s tests -v
Ran 43 tests — OK (Python 3.14.3)
/usr/bin/python3 -B -m unittest discover -s tests -v
Ran 43 tests — OK (Python 3.12.3)
python3 -B scripts/package_skill.py --check
OK: 30 source files; 77 local links; .skill and .zip checked
python3 -B scripts/release_skill.py --check --base 7329444a2652a35741497c2299f87e875a7aa7f2
1.0.0
ruff check --no-cache — All checks passed!
ruff format --no-cache --check — 4 files already formatted
mypy --strict — Success: no issues found in 4 source files
```

Prochaine frontière NORMAL : un seul commit atomique
`feat: add versioned Seedance releases` portant les treize fichiers
suivis annoncés ci-dessus. Le scope ignoré reste exclu. Aucun push avec ce gate.
