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
| `tests/check_tells.py` | Tell checker: scans text for the tells and verifies the lists stay in sync with SKILL.md |
| `tests/samples/ai_style.txt` | "Before" sample — a typical LLM-flavored draft, full of tells |
| `tests/samples/human_style.txt` | "After" sample — the same content rewritten by applying the skill |

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

## Testing

The repo ships a tell checker that encodes the skill's rules as regexes, so the skill's
claims are verifiable:

```bash
# 1. List sync: the checker's banned vocabulary must match SKILL.md's table exactly
# 2. Detection: every banned entry and context rule must actually fire
python3 tests/check_tells.py --self-check --test-detection

# 3. "Before/after" demonstration:
#    ai_style.txt    -> should FAIL (it's the un-skilled, LLM-flavored draft)
#    human_style.txt -> should be CLEAN (the same content after applying the skill)
python3 tests/check_tells.py tests/samples/ai_style.txt tests/samples/human_style.txt
```

Expected: the self-check and detection test pass, `ai_style.txt` reports hard tells
(banned words, "not only…but also", emoji, spaced em dashes, "it's important to note",
tacked-on "-ing" flourishes…), and `human_style.txt` reports **CLEAN**. The checker is a
supporting tool, not a detector to trust blindly — like Wikipedia's own caveats, no
automated check is definitive; it exists to catch regressions in the skill's examples.

## License

MIT (see `LICENSE`). The reference catalog draws on
[Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
(CC BY-SA 4.0); attribution and links in `reference/ai-writing-tells.md`.
