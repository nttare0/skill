# skill — human-writing

A skill that makes LLM output read as naturally human by avoiding the tells cataloged in
Wikipedia's [**Signs of AI writing**](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
field guide (WP:AISIGNS) — the same page featured in the @yatesvids
"Signs of AI writing" Instagram reel.

The field guide exists to help editors *detect* AI-generated text. This skill runs it in
reverse: instead of detecting the tells, it stops the model from producing them —
the AI-vocabulary words ("delve", "vibrant", "tapestry", "pivotal"…), the significance
inflation, the "not only X but also Y" constructions, the em-dash and boldface tics,
the chatbot residue ("I hope this helps!", "it's important to note", "[Your Name]").
The result is prose with the documented *signs of human writing*: plain "is/has"
constructions, plain verbs, natural word repetition, and specific facts instead of
filler analysis.

## Contents

| File | Purpose |
|---|---|
| `SKILL.md` | The skill itself — operational rules plus a pre-delivery self-check |
| `reference/ai-writing-tells.md` | Full catalog: vocabulary by LLM era, construction patterns, real captured examples, sources |

## Install

Works with any agent that supports Anthropic-style skills (Claude Code, Claude.ai skills,
Cursor, and other SKILL.md-based agents):

- **Claude Code / repo skills:** put this repo's folder in `~/.claude/skills/human-writing/`
  (or copy `SKILL.md` into a `skills/` folder of a project), then ask for anything and the
  model will apply it when relevant.
- **Any other agent:** point it at `SKILL.md`, or paste the contents as instructions.
- **Plain prompt use:** the SKILL.md body works standalone as a system prompt.

## Usage

Trigger naturally with requests like:

- "write this essay so it doesn't sound like ChatGPT"
- "make it sound human / remove the AI tone / humanize this"
- "rewrite my article and avoid the Wikipedia signs of AI writing"

The skill also includes a mandatory **self-check pass**: before delivering, the model scans
its own draft for the tell list (banned vocabulary, "serves as", negative parallelisms,
tacked-on "-ing" analysis, emoji, spaced em dashes, placeholders…) and fixes any hits.

## License

MIT (see `LICENSE`). The reference catalog draws on
[Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
(CC BY-SA 4.0); attribution and links in `reference/ai-writing-tells.md`.
