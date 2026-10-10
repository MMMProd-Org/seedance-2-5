# Rapport de vérification — S25-01

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
