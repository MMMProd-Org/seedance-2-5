<p align="center">
  <img src="assets/seedance-banner.svg" width="100%" alt="Seedance 2.5 — une illustration originale pour diriger votre scène.">
</p>

<h1 align="center">Skill Seedance 2.5</h1>

<p align="center">
  <strong>Vous voyez la scène. Votre assistant vous aide à la diriger.</strong><br>
  Un skill de mise en scène pour transformer votre idée en prompt vidéo.
</p>

<p align="center">
  <a href="https://github.com/MMMProd-Org/seedance-2-5/releases"><img src="https://img.shields.io/github/v/release/MMMProd-Org/seedance-2-5?style=flat-square&amp;color=d1e987&amp;label=release" alt="Dernière version publiée"></a>
  <a href="https://github.com/MMMProd-Org/seedance-2-5/actions/workflows/check.yml"><img src="https://github.com/MMMProd-Org/seedance-2-5/actions/workflows/check.yml/badge.svg?branch=main" alt="Contrôles du skill"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-d1e987?style=flat-square" alt="Licence MIT"></a>
</p>

<p align="center">
  <strong><a href="https://github.com/MMMProd-Org/seedance-2-5/releases/latest/download/seedance-2-5.zip">↓ Télécharger le skill (ZIP)</a></strong>
  &nbsp; · &nbsp;
  <a href="https://github.com/MMMProd-Org/seedance-2-5/releases/latest/download/seedance-2-5.skill">.skill</a>
  &nbsp; · &nbsp;
  <a href="#votre-premier-prompt-en-quelques-étapes">Installer</a>
  &nbsp; · &nbsp;
  <a href="README.md">English</a>
</p>

<p align="center"><sub>Claude recommandé par l’auteur. Également conçu pour Codex.</sub></p>

Le téléchargement ne démarre pas ? [Téléchargement direct du ZIP](https://raw.githubusercontent.com/MMMProd-Org/seedance-2-5/refs/heads/main/downloads/seedance-2-5.zip).

---

## Votre premier prompt, en quelques étapes

1. [Téléchargez le ZIP](https://github.com/MMMProd-Org/seedance-2-5/releases/latest/download/seedance-2-5.zip). Gardez-le compressé.
2. Dans Claude, ouvrez **Customize → Skills → + Create skill → Upload a skill**.
3. Importez le ZIP, activez le skill et démarrez une conversation sur votre scène.

Si Skills n’apparaît pas, vérifiez l’activation de l’exécution de code ou les
réglages de votre organisation. [Guide officiel d’installation](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

<details>
<summary><strong>Claude Code</strong></summary>

Téléchargez et décompressez le ZIP. Placez le dossier `seedance-2-5` entier dans
votre dossier personnel de skills :

| Système | Dossier à créer |
| --- | --- |
| Linux, macOS ou WSL | `~/.claude/skills/seedance-2-5/` |
| Windows natif | `%USERPROFILE%\.claude\skills\seedance-2-5\` |

`SKILL.md`, `references/`, `assets/`, `agents/`, `VERSION` et `LICENSE` restent ensemble.
Ouvrez Claude Code et appelez le skill :

```text
/seedance-2-5 Écris une scène de 6 secondes où une femme attend devant une entrée vitrée.
```

[Guide officiel des skills Claude Code](https://code.claude.com/docs/en/skills).

</details>

<details>
<summary><strong>Codex</strong></summary>

Téléchargez et décompressez le même ZIP. Placez le dossier `seedance-2-5` entier
dans votre dossier personnel de skills :

| Système | Dossier à créer |
| --- | --- |
| Linux, macOS ou WSL | `~/.agents/skills/seedance-2-5/` |
| Windows natif | `%USERPROFILE%\.agents\skills\seedance-2-5\` |

Ouvrez Codex et sélectionnez le skill avec `/skills`, ou appelez-le directement :

```text
$seedance-2-5 Écris une scène de 6 secondes où une femme attend devant une entrée vitrée.
```

Redémarrez Codex si le nouveau skill n’apparaît pas.
[Guide officiel des skills Codex](https://learn.chatgpt.com/docs/build-skills).

**Vous utilisez WSL ?** Installez dans le dossier personnel Linux lorsque votre
assistant tourne dans WSL. **Vous faites une mise à jour ?** Conservez votre
dossier de skill actuel avant de le remplacer.

Le téléchargement `.skill` contient les mêmes données ZIP. Pour le parcours
d’import documenté par Claude, utilisez le fichier qui se termine par `.zip`.

</details>

## Une idée. Des choix de mise en scène.

« Une femme attend devant une entrée vitrée. » Un exemple de brief à donner à votre assistant :

| Votre intention | Une direction concrète |
| --- | --- |
| Une attente contenue | Mains jointes, un souffle relâché, personne n’arrive |
| Un cadre qui tient | Un plan moyen fixe, six secondes, sans coupe |
| Une scène cohérente | La porte reste fermée, le personnage reste à sa place |

**Un moment calme, sans référence nécessaire**

```text
Utilise Seedance 2.5. Écris un prompt vidéo de 6 secondes en 9:16.
Une femme attend devant une entrée vitrée fermée. Plan moyen fixe, sans coupe.
Ses mains restent ensemble. Elle relâche un souffle ; personne n’arrive.
Rédige le prompt en anglais.
```

**Une séquence avec vos propres images importées**

```text
Utilise Seedance 2.5 avec les deux images que j’ai importées.
La première définit le personnage ; la seconde définit le lieu.
Écris deux plans raccordés : elle entre dans la pièce et pose un sac.
Conserve son identité, le sac et les positions finales des objets.
```

**Un résultat que vous voulez comprendre**

```text
Utilise Seedance 2.5 pour diagnostiquer ce résultat.
J’ai demandé un plan large fixe ; la vidéo se rapproche et coupe les pieds.
Voici le prompt : [collez-le ici].
Explique ce que le texte permet d’établir et quelles preuves te manquent.
```

Indiquez votre durée, le format de l’image, l’action et vos références. Vous
pouvez parler dans votre langue et choisir celle du prompt final. À défaut de
langue demandée ou de prompt existant qui la fixe, le prompt est rédigé en anglais.

## Ce qu’il vous aide à diriger

| Votre scène demande… | Les fiches du skill couvrent… |
| --- | --- |
| Un plan lisible | Cadre, placement, optique, mouvement de caméra et lumière |
| Un personnage présent | Tâche de jeu, écoute, dialogue et silence dirigé |
| Une action compréhensible | Contacts, mouvement, cause et conséquence, duels et mécanismes |
| Plusieurs plans raccordés | Temps de l’action, coupes, états des objets et continuité |
| Des références bien utilisées | Personnage, lieu, look, voix et ancrage par l’image |
| Un diagnostic utile | Consigne absente, contradictoire ou ignorée, avec ses preuves |

Le skill rédige du texte à coller dans votre interface vidéo. Vous y générez la
vidéo, puis vous pouvez rapporter le résultat pour l’examiner avec l’assistant.

## Ce que vous recevez

Le format complet du skill prévoit une durée, un contrôle du texte, un seul
prompt final et une courte liste de symptômes visibles à surveiller. Un bloc de
préparation d’image apparaît lorsque l’approche retenue demande une image de départ.

Vous voulez uniquement le prompt ? Dites **« Seulement le prompt final, sans
explication. »** Les instructions du skill gardent alors ses contrôles internes.

Deux cas complets de prompts sont également disponibles dans
[le dossier d’exemples](skills/seedance-2-5/assets/cases/). Ce sont des textes ;
ce dépôt ne contient ni clips générés ni images de référence pour ces cas.

## Quelle version avez-vous ?

**2.5 désigne le modèle ciblé. Le numéro du skill est distinct.**
Ouvrez le fichier `VERSION` dans le dossier installé pour connaître votre version exacte.

- [Dernière release](https://github.com/MMMProd-Org/seedance-2-5/releases/latest) : fichiers et résumé des changements.
- [Toutes les versions](https://github.com/MMMProd-Org/seedance-2-5/releases) : retrouvez un ancien téléchargement.
- `SHA256SUMS`, fourni avec chaque release, permet de vérifier les fichiers reçus.

Le ZIP est recommandé pour l’import Claude. Le fichier `.skill` contient les mêmes données.
Avant une mise à jour, conservez votre dossier actuel.

<details>
<summary><strong>Dans le téléchargement</strong></summary>

```text
seedance-2-5/
├── SKILL.md             Instructions centrales et parcours de lecture
├── references/          23 fiches ciblées
├── agents/openai.yaml   Métadonnées de présentation pour Codex
├── assets/              Icône et deux cas textuels
├── VERSION              Version du skill installé
└── LICENSE              Licence MIT
```

Les fiches couvrent l’écriture du plan, le jeu, la physique, les références,
les séquences, le diagnostic, la syntaxe, les contraintes et la livraison.
Le skill demande à l’assistant d’ouvrir les fiches utiles à la scène courante.

</details>

<details>
<summary><strong>Pour maintenir le skill</strong></summary>

Les sources modifiables sont dans [skills/seedance-2-5/](skills/seedance-2-5/).
Les deux téléchargements sont fabriqués avec la bibliothèque standard de Python.
Pour les refaire et les vérifier :

```sh
python3 -B scripts/package_skill.py
python3 -B -m unittest discover -s tests -v
python3 -B scripts/package_skill.py --check
```

Les contrôles couvrent les liens locaux, les métadonnées nécessaires, la licence,
les chemins sûrs et l’identité entre sources et archives. Les tests utilisent
des dossiers temporaires. La CI lance les mêmes tests et la vérification du
paquet en lecture seule. Les règles de travail partagées sont dans
[AGENTS.md](AGENTS.md), avec un renvoi depuis [CLAUDE.md](CLAUDE.md).

</details>

[Publication automatisée](docs/releasing.md) : changez le numéro du skill dans une PR. Après les contrôles et la fusion sur main, la release est publiée.

L’import Claude/Codex et la qualité vidéo ne sont pas attestés par les tests de packaging. [Rapport de vérification](docs/verification.md).

Un cas à améliorer ? [Ouvrez une issue](https://github.com/MMMProd-Org/seedance-2-5/issues)
avec votre demande, le prompt et le résultat observé.

Distribué sous [licence MIT](LICENSE). Présentation du README inspirée de
[Ponytail](https://github.com/DietrichGebert/ponytail), avec une illustration originale.
