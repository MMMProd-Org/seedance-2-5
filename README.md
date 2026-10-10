<p align="center">
  <img src="assets/seedance-banner.svg" width="100%" alt="Seedance 2.5. Give your scene a plan: action, camera, performance and continuity.">
</p>

<h1 align="center">Seedance 2.5 Skill</h1>

<p align="center">
  <strong>Your idea. A clear prompt. A scene with intention.</strong><br>
  A downloadable directing and prompt-writing skill for Claude and Codex.
</p>

<p align="center">
  <a href="downloads/seedance-2-5.zip?raw=true"><strong>Download ZIP</strong></a>
  &nbsp; · &nbsp;
  <a href="downloads/seedance-2-5.skill?raw=true">Download .skill</a>
  &nbsp; · &nbsp;
  <a href="#install-in-a-few-steps">Install</a>
  &nbsp; · &nbsp;
  <a href="README.fr.md">Français</a>
  &nbsp; · &nbsp;
  <a href="LICENSE">MIT</a>
</p>

---

You have a scene in mind: someone waiting, a camera following a car, a gesture
that carries into the next shot. This skill helps your assistant turn that idea
into a prompt with visible action, clear camera choices and consistent states.

It also gives you a way to discuss a disappointing result: describe what you
expected, what appeared and which instruction mattered. Work from that evidence
to choose the next correction.

**Recommended host: Claude.** The author's best results have been with Claude.
The same skill files can be installed in Codex. This repository does not include
a controlled comparison between the two hosts.

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

## Install in a few steps

### Claude web or Desktop — the easiest start

1. [Download the ZIP](downloads/seedance-2-5.zip?raw=true). Keep it zipped.
2. In Claude, open **Customize → Skills → + Create skill → Upload a skill**.
3. Upload the ZIP, enable the skill and start a conversation about your scene.

If Skills is unavailable, check Claude's code execution setting or your
organization's settings. [Official installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Claude Code

Download and extract the ZIP. Put the whole `seedance-2-5` folder in your personal
skills directory:

| System | Folder to create |
| --- | --- |
| Linux, macOS or WSL | `~/.claude/skills/seedance-2-5/` |
| Native Windows | `%USERPROFILE%\.claude\skills\seedance-2-5\` |

`SKILL.md`, `references/`, `assets/`, `agents/` and `LICENSE` must stay together.
Open Claude Code and invoke the skill:

```text
/seedance-2-5 Write a 6-second scene in which a woman waits outside a glass entrance.
```

[Official Claude Code skill guide](https://code.claude.com/docs/en/skills).

### Codex

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

## Try it with your scene

**A quiet moment, with no references needed**

```text
Use Seedance 2.5. Write a 6-second, 9:16 video prompt.
A woman waits outside a closed glass entrance. One locked medium shot.
Her hands stay together. She releases one breath; no one arrives.
Keep the prompt in English.
```

**A sequence with your own uploaded images**

```text
Use Seedance 2.5 with the two images I uploaded.
The first defines the character; the second defines the location.
Write two connected shots of her entering the room and setting down a bag.
Keep her identity, the bag and the final object positions consistent.
```

**A result you want to understand**

```text
Use Seedance 2.5 to diagnose this result.
I asked for a locked wide shot; the video moves closer and crops the feet.
Here is the prompt: [paste it here].
Explain what the text supports and what evidence you still need.
```

Tell the assistant your intended duration, aspect ratio, action and references.
You can ask in your preferred language and choose the final prompt's language.
Prompt text defaults to English when no language or existing prompt sets it.

## What you receive

The skill's full delivery format calls for a duration, a text self-check, one
final prompt and a short list of visible failure symptoms. An image preparation
block appears when the chosen approach needs a starting frame.

Want just the prompt? Say **“Only the final prompt, no explanation.”**
The skill's instructions keep its checks internal for that request.

There are also two complete prompt cases in
[the examples folder](skills/seedance-2-5/assets/cases/). They are text examples;
this repository does not include generated clips or their reference images.

## Inside the download

```text
seedance-2-5/
├── SKILL.md             Core instructions and reading routes
├── references/          23 focused guides
├── agents/openai.yaml   Codex presentation metadata
├── assets/              Icon and two text cases
└── LICENSE              MIT license
```

The guides cover shot writing, performance, physics, references, sequences,
diagnosis, syntax, constraints and delivery. The assistant is instructed to open
the guides relevant to the current scene.

**2.5 identifies the skill's target model.** It is not a repository release number.
Video capabilities and available settings depend on the interface you use.
The assistant's self-check concerns the prompt text; generated footage still
needs to be viewed. Host imports and video quality have not been tested during
this bootstrap. See the [verification report](docs/verification.md).

## For maintainers

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

Have a case to improve? [Open an issue](https://github.com/mmmprod/seedance-2-5/issues)
with your brief, prompt and the result you observed.

Released under the [MIT license](LICENSE). README presentation inspired by
[Ponytail](https://github.com/DietrichGebert/ponytail), with original artwork.
