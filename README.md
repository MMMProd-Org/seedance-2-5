<p align="center">
  <img src="assets/seedance-banner.svg" width="100%" alt="Seedance 2.5 — an original illustrated director's board.">
</p>

<h1 align="center">Seedance 2.5 Skill</h1>

<p align="center">
  <strong>You see the scene. Your assistant helps you direct it.</strong><br>
  A directing skill that turns your idea into a video prompt.
</p>

<p align="center">
  <a href="https://github.com/MMMProd-Org/seedance-2-5/releases"><img src="https://img.shields.io/github/v/release/MMMProd-Org/seedance-2-5?style=flat-square&amp;color=d1e987&amp;label=release" alt="Latest published release"></a>
  <a href="https://github.com/MMMProd-Org/seedance-2-5/actions/workflows/check.yml"><img src="https://github.com/MMMProd-Org/seedance-2-5/actions/workflows/check.yml/badge.svg?branch=main" alt="Skill checks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-d1e987?style=flat-square" alt="MIT license"></a>
</p>

<p align="center">
  <strong><a href="https://github.com/MMMProd-Org/seedance-2-5/releases/latest/download/seedance-2-5.zip">↓ Download the skill (ZIP)</a></strong>
  &nbsp; · &nbsp;
  <a href="https://github.com/MMMProd-Org/seedance-2-5/releases/latest/download/seedance-2-5.skill">.skill</a>
  &nbsp; · &nbsp;
  <a href="#your-first-prompt-in-a-few-steps">Install</a>
  &nbsp; · &nbsp;
  <a href="README.fr.md">Français</a>
</p>

<p align="center"><sub>Claude recommended by the author. Also designed for Codex.</sub></p>

---

You can already see the scene: a woman outside a glass entrance, waiting for
someone who has not arrived. The interesting part is the wait.

Where does she look? What happens in six seconds? Does the camera need to move?
Seedance 2.5 gives your assistant a directing method for those choices:
framing, performance, movement and continuity.

**Describe the scene. Shape the shot. Take the prompt to your video tool.**

## One idea. Clear directing choices.

> A woman waits outside a glass entrance.

<p align="center">
  <img src="assets/seedance-direction.svg" width="100%" alt="Three numbered directing choices for the text example: 01 a fixed medium shot in 9:16 lasting six seconds; 02 one breath released; 03 hands staying together and the door staying closed.">
</p>

- **01 / Frame:** a locked medium shot lasting six seconds, in 9:16.
- **02 / Performance:** one breath released; fingers relax once.
- **03 / Continuity:** hands stay together, the door stays closed.

The brief becomes a set of visible decisions: a camera on the curb side,
a gaze held off-screen, a breath released, fingers relaxing once.
The door stays closed. No one arrives.

**From the included prompt (excerpt)**

```text
6-second video, 9:16, one continuous locked medium shot, real-time.

3-6 seconds: as the wait continues, she releases the breath and slightly relaxes her fingers once.

The door remains closed and the sidewalk unchanged.
```

<details>
<summary><strong>Read the complete example prompt</strong></summary>

```text
6-second video, 9:16, one continuous locked medium shot, real-time.

An adult woman waits on a sidewalk outside a closed glass entrance. The entrance is directly behind her. The road is in front of her, behind the camera, and stays outside the frame. The camera is on the curb side of the woman, looking toward her and the entrance. Her torso faces the camera throughout. Her gaze remains toward the same waiting point along the road, off-screen to the left at eye level.

Frame her from the waist to the top of the head, with both hands resting visibly together at waist height. Keep camera position, orientation, focal length and this framing unchanged.

0-3 seconds: she waits for someone to arrive from that off-screen point, taking one quiet breath while keeping her hands at rest. 3-6 seconds: as the wait continues, she releases the breath and slightly relaxes her fingers once. Her hands stay together; her gaze remains on the same point. The final state is the same waiting position with her fingers slightly less tense. No arrival or revelation occurs.

Soft entrance light illuminates her from behind, with a steady diffuse fill on her face. The door remains closed and the sidewalk unchanged. One woman only. No added props, no dialogue, no music, no sound, no cuts, no camera movement.
```

Source: [the included text case](skills/seedance-2-5/assets/cases/attente-coherente-temoin.txt).

</details>

*This is an illustration of the included prompt, not a generated video or a measured result.*

## Three ways to put it to work

### Start with the scene in your head

Give the assistant something to direct. A simple moment is enough to start.

```text
Use Seedance 2.5. Write a 6-second, 9:16 video prompt.
A woman waits outside a closed glass entrance. One locked medium shot.
Her hands stay together. She releases one breath; no one arrives.
Keep the prompt in English. Only the final prompt, no explanation.
```

### Carry the scene into the next shot

Bring your references and say what each one is for.

```text
Use Seedance 2.5 with the two images I uploaded.
The first defines the character; the second defines the location.
Write two connected shots of her entering the room and setting down a bag.
Keep her identity, the bag and the final object positions consistent.
```

### Bring back the take that missed

Bring the prompt and describe what happened. Give the assistant evidence to work with.

```text
Use Seedance 2.5 to diagnose this result.
I asked for a locked wide shot; the video moves closer and crops the feet.
Here is the prompt: [paste it here].
Explain what the text supports and what evidence you still need.
```

Tell the assistant your duration, aspect ratio, action and references. You can
ask in your preferred language and choose the final prompt's language.
Prompt text defaults to English when no language or existing prompt sets it.

## Your first prompt, in a few steps

1. [Download the ZIP](https://github.com/MMMProd-Org/seedance-2-5/releases/latest/download/seedance-2-5.zip). Keep it zipped.
2. In Claude, open **Customize → Skills → + Create skill → Upload a skill**.
3. Upload the ZIP, enable the skill and start a conversation about your scene.

If Skills is unavailable, check Claude's code execution setting or your
organization's settings. [Official installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

<details>
<summary><strong>Claude Code</strong></summary>

Download and extract the ZIP. Put the whole `seedance-2-5` folder in your personal
skills directory:

| System | Folder to create |
| --- | --- |
| Linux, macOS or WSL | `~/.claude/skills/seedance-2-5/` |
| Native Windows | `%USERPROFILE%\.claude\skills\seedance-2-5\` |

`SKILL.md`, `references/`, `assets/`, `agents/`, `VERSION` and `LICENSE` must stay together.
Open Claude Code and invoke the skill:

```text
/seedance-2-5 Write a 6-second scene in which a woman waits outside a glass entrance.
```

[Official Claude Code skill guide](https://code.claude.com/docs/en/skills).

</details>

<details>
<summary><strong>Codex</strong></summary>

Download and extract the same ZIP. Put the whole `seedance-2-5` folder in your
personal skills directory:

| System | Folder to create |
| --- | --- |
| Linux, macOS or WSL | `~/.agents/skills/seedance-2-5/` |
| Native Windows | `%USERPROFILE%\.agents\skills\seedance-2-5\` |

Open Codex and select the skill with `/skills` or mention it directly:

```text
$seedance-2-5 Write a 6-second scene in which a woman waits outside a glass entrance.
```

Restart Codex if the new skill does not appear.
[Official Codex skill guide](https://learn.chatgpt.com/docs/build-skills).

**Using WSL?** Install in the Linux home directory when your agent runs there.
**Updating?** Save your existing skill folder before replacing it.

The `.skill` download contains the same ZIP data. For Claude's documented upload
path, use the file ending in `.zip`.

</details>

## Which version do you have?

**2.5 identifies the target model. The skill has its own version number.**
Open `VERSION` in your installed skill folder to see your exact version.

- [Latest release](https://github.com/MMMProd-Org/seedance-2-5/releases/latest): downloads and a summary of changes.
- [All versions](https://github.com/MMMProd-Org/seedance-2-5/releases): find an earlier download.
- `SHA256SUMS`, included in each release, lets you verify the downloaded files.

The ZIP is recommended for Claude's upload flow. The `.skill` file contains the same data.
Save your current skill folder before updating.

<details>
<summary><strong>What the skill covers and what you receive</strong></summary>

## What it helps you direct

| Your scene needs… | The skill's guidance covers… |
| --- | --- |
| A readable shot | Framing, placement, lens choices, camera movement and lighting |
| A person who feels present | Acting tasks, listening, dialogue and purposeful silence |
| Action you can follow | Contacts, motion, cause and consequence, duels and mechanisms |
| Several connected shots | Beats, cuts, object states and continuity |
| References that keep their role | Character, location, look, voice and image anchoring |
| A useful diagnosis | Missing, conflicting or ignored instructions, with the evidence kept separate |

The skill writes text to paste into your video interface. You generate the video
there, then bring back the result if you want help reviewing it.

## What you receive

The skill's full delivery format calls for a duration, a text self-check, one
final prompt and a short list of visible failure symptoms. An image preparation
block appears when the chosen approach needs a starting frame.

Want just the prompt? Say **“Only the final prompt, no explanation.”**
The skill's instructions keep its checks internal for that request.

There are also two complete prompt cases in
[the examples folder](skills/seedance-2-5/assets/cases/). They are text examples;
this repository does not include generated clips or their reference images.
</details>

<details>
<summary><strong>Inside the download</strong></summary>

```text
seedance-2-5/
├── SKILL.md             Core instructions and reading routes
├── references/          23 focused guides
├── agents/openai.yaml   Codex presentation metadata
├── assets/              Icon and two text cases
├── VERSION              Installed skill version
└── LICENSE              MIT license
```

The guides cover shot writing, performance, physics, references, sequences,
diagnosis, syntax, constraints and delivery. The assistant is instructed to open
the guides relevant to the current scene.

</details>

<details>
<summary><strong>For maintainers</strong></summary>

The editable source is [skills/seedance-2-5/](skills/seedance-2-5/). Both download
files are built from it with Python's standard library. To rebuild and check:

```sh
python3 -B scripts/package_skill.py
python3 -B -m unittest discover -s tests -v
python3 -B scripts/package_skill.py --check
```

The checks cover local links, required metadata, license inclusion, safe paths
and source/archive equality. Tests use temporary directories. CI runs the same
tests and read-only package check. Shared development rules are in
[AGENTS.md](AGENTS.md), with [CLAUDE.md](CLAUDE.md) pointing to them.

</details>
<details>
<summary><strong>Downloads and automated releases</strong></summary>

Download unavailable? [Direct ZIP download](https://raw.githubusercontent.com/MMMProd-Org/seedance-2-5/refs/heads/main/downloads/seedance-2-5.zip).

[Automated releases](docs/releasing.md): change the skill version in a PR. Checks pass; merging into main publishes the release.

Package tests do not attest Claude/Codex imports or video quality. [Verification report](docs/verification.md).

</details>

Have a scene that needs another look? [Open an issue](https://github.com/MMMProd-Org/seedance-2-5/issues)
with your brief, prompt and the result you observed.

Released under the [MIT license](LICENSE). README presentation inspired by
[Ponytail](https://github.com/DietrichGebert/ponytail), with original illustrations.
