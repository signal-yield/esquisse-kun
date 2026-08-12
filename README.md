# エスキスクン / Esquisse-kun

**Esquisse-kun — AI Architecture Design Review** is a skills-only plugin for architecture students. It reviews studio assignments and drawings as an early esquisse partner, then highlights the next concrete moves before a critique.

## What It Does

- Reviews assignment requirements, plans, site plans, sections, elevations, diagrams, perspectives, and model photos when the host model can read them.
- Separates values into explicit, readable, estimated, and unknown so it does not invent drawing facts.
- Screens building-code issues as a learning-oriented first pass: FAR, BCR, roads, setbacks, fire districts, height limits, daylight, evacuation notes, slant-plane controls, and shadow regulation.
- Supports Reference Architect Mode. v0.1 includes a curated Vincent Van Duysen reference card and can also organize other architects through design principles.

## Who It's For

Architecture students preparing for studio desk crits, esquisses, and review sessions.

## Install

For repo-hosted Codex testing:

```bash
codex plugin marketplace add signal-yield/esquisse-kun
```

Then open `/plugins`, select the `signal-yield` marketplace, install `esquisse-kun`, and start a new conversation.

## Examples

```text
明日エスキスです。この課題文と図面をレビューしてください。
```

```text
Vincent Van Duysenの設計原理を参考に、もう一度レビューしてください。
```

```text
建築法規も一次チェックしてください。日影規制と斜線制限も見てください。
```

## Disclaimer

This plugin is a preliminary design-learning and screening aid. It does not replace studio instructors, architects, licensed professionals, latest laws and ordinances, local government materials, or building confirmation review.

## Author

Signal Yield Advisory / Koichi Matsuda  
signalYield@gmail.com  
https://signal-yield.github.io/esquisse-kun/

## License

MIT
