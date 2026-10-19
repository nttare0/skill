---
name: human-writing
description: Write text that reads as naturally human instead of AI-generated. Use whenever the user asks for essays, articles, reports, emails, posts, or any prose that should not carry an LLM's generic tone. Default to neutral, fact-based prose unless the user specifies a different style or genre.
---

# Human Writing (Avoid AI Tells)

Write like a competent human writer. This skill is the reverse of Wikipedia's field guide *"Signs of AI writing"* (the same guide shown in the "Signs of AI writing" Instagram reel): instead of detecting the tells, it stops the model from producing them. The goal is natural prose, not forced blandness.

Important default: these rules are a baseline for neutral, reference-style prose. They are not a universal ban on every stylistic choice. If the user specifies a format, style guide, brand voice, genre, or audience, follow that instruction over these defaults. Marketing copy, technical docs, READMEs, fiction, and personal essays can all legitimately relax different rules.

## 1. Vocabulary: words that are AI tells

Avoid these words entirely in your output when they are used as filler or as a substitute for a more specific fact. If two or more appear in one piece of writing, rewrite. Note: a word being overused by AI does **not** mean its synonyms are overused — don't swap "vibrant" for "lively" and keep the fluff; cut the flourish entirely. Use these as default rules for neutral prose; do not force them into a style guide the user has already chosen.

**Banned list (all eras):**

| Word | Instead write |
|---|---|
| additionally (starting a sentence) | reorder, or plain "also" |
| align with | match, fit, or restructure |
| boasts (meaning "has") | has |
| bolstered | strengthened, backed, or cut |
| crucial | important, or cut (often unneeded) |
| delve | explore, dig into, look into, or cut |
| emphasizing | stressing, pointing out, showing, or cut |
| enduring | lasting, or cut |
| enhance | improve, boost, or cut |
| fostering | encouraging, building, supporting |
| garner | win, get, draw |
| highlight (as a verb) | show, point to, note, feature |
| interplay | interaction, relationship |
| intricate / intricacies | complex / complexities, or be specific |
| key (as an adjective) | main, central, important, or cut |
| landscape (abstract: "the tech landscape") | scene, field, world, or cut |
| meticulous / meticulously | careful / carefully, thorough / thoroughly |
| pivotal | important, or cut |
| robust | strong, solid, thorough |
| showcase | show, display, feature |
| tapestry (abstract: "a rich tapestry of") | cut |
| testament ("a testament to") | shows, is proof of, or cut |
| underscore (as a verb) | underline, show, point up |
| valuable | useful, important, or cut (esp. "valuable insights") |
| vibrant | lively, colorful, busy — or cut |

**Era tells** (older output used older lists; all are to be avoided):

| Era | Words to watch |
|---|---|
| 2023 – mid-2024 (GPT-4) | additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate/intricacies, interplay, key, landscape, meticulous, pivotal, underscore, tapestry, valuable |
| mid-2024 – mid-2025 (GPT-4o) | align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant |
| mid-2025+ (GPT-5) | emphasizing, enhance, highlighting, showcasing — plus "notability" phrasing (see §5.2) |
| Grok | causal, empirical, correlate, underscore |

### 1.1. When to relax these defaults

Use a genre-aware version of the rules:

- Marketing copy: triads, a promotional tone, and some plain positive language are allowed if the claims are specific and not inflated. Still avoid filler analysis, vague significance claims, and obvious AI diction.
- Technical docs and READMEs: bold, tables, bullets, and headings are fine when they improve structure. Favor clarity and scannability over neutral-prose style.
- Fiction and personal essays: formatting rules matter less than voice, concrete detail, and sentence rhythm. Aim for a distinctive point of view and a lived-in cadence.
- Encyclopedic or reference text: apply the full list. This is the strictest setting.
- If the user names a style guide or format, follow it. A brand voice, house style, or platform requirement beats these defaults.

## 2. Grammar: human patterns to keep, AI patterns to drop

**Use "is / are / has" directly.** LLMs avoid simple copulas and marketing verbs. Default to avoiding:

- ✗ "The gallery **serves as** LAAA's exhibition space and **features** four separate spaces."
- ✗ "It **stands as** a reminder of…"
- ✗ "The company **boasts** a workforce of…"
- ✗ "The stadium **holds the distinction of being** the oldest…"
- ✗ "He **ventured into politics as a candidate**." ("was a candidate")
- ✗ "She **began her career as** a lawyer." ("was a lawyer")

✓ "The gallery is LAAA's exhibition space and has four separate rooms."

**Prefer plain verbs** (a documented sign of human writing): wrote (not *authored*), moved (not *relocated*), used (not *utilized*), tried (not *attempted*), died (not *passed away*).

**Human syntax is your friend — keep it.** Humans naturally write: "there is a…", "it has a…", "one of the best…", "is the only…", "was the first…", "very", "perhaps", "tends to", "as a result of", "in order to", "all of the", "the fact that". Use these naturally when they fit the sentence; don't stack them as a pattern or force them in to appear human.

## 3. Rhetorical patterns to avoid

- **Negative parallelisms.** Avoid repeated "not… but…" constructions: "not only X but also Y", "it's not just X, it's Y", "not X, but Y", "no X, no Y, just Z", "X rather than Y". One, occasional use is fine; repeated stacking is the tell.
- **The rule of three.** LLMs lean on triads to sound comprehensive ("fast, reliable, and secure"; "cuts through noise, drives action, and builds trust"). Vary list lengths: two items, four items, or a sentence that chooses a single strongest point. Triads are useful in marketing or slogans, but don't use them as a default filler pattern.
- **Elegant variation.** Never thesaurus-swap to avoid repeating a word. Humans repeat: "the canal… the canal… the canal". AI writes "the canal… the waterway… the artery". Repeat the word unless a different one is truly needed.
- **Tacked-on "-ing" analysis.** Sentences ending in ", -ing phrase" that only fluff the fact: "…, creating a lively community within its borders", "…, further enhancing its significance", "…, underscoring the importance of…" are often filler. Cut them unless the phrase adds genuine detail or action.
- **Forced transitions.** No chains of "Moreover, … Additionally, … Furthermore, …". Let paragraphs stand on their own.

## 4. Content rules: no inflation, no filler analysis

- **No significance inflation.** State facts; let the reader judge importance. Default to avoiding: "marking a pivotal moment", "represented a significant shift", "was part of a broader movement", "its enduring legacy" unless the claim is truly necessary and grounded.
- **No canned "Challenges and Future Prospects" coda.** Avoid the formula: "Despite its X, Y faces challenges…" → "Despite these challenges, …" → vague optimistic close. End factually, when the content is done.
- **No vague attribution / weasel words.** Avoid "experts argue", "industry reports", "observers have cited", "some critics say", "researchers and conservationists", "described in scholarship", "sources indicate" when the citation is weak or absent.
- **No promotional or travel-guide tone.** Avoid "nestled", "breathtaking", "in the heart of", "vibrant", "rich", "diverse array of", "groundbreaking", "renowned", "commitment to", "natural beauty", "must-see" unless the user asked for promotional copy.
- **No canned notability arguments.** Avoid "independent coverage", "featured in … and other prominent media outlets", "profiled in", "maintains an active social media presence", "covered by [name] and other outlets" as a generic substitute for actual evidence.
- **No "refers to" lead sentences** — treat the subject as the thing, not the term ("X is…" not "X refers to…").

## 5. Formatting and structure

- **Headings in sentence case**, not title case: "Impact of technology" ✓, "Impact of Technology and Digitalization" ✗.
- **No bolded "key takeaways"**; don't bold every occurrence of a term. Bold only where the format requires it (e.g., first mention of a defined term).
- **No inline-header vertical lists** ("**Route Details:** …" bullets). Prefer prose; if a list genuinely fits, keep items short and unadorned.
- **No emoji as formatting** — no emoji before headings or bullets; no emoji in formal writing at all.
- **Em dashes: default to rare.** Humans use commas, colons, parentheses. Default to avoiding spaced em dashes ("word — word"). If the user's format or house style requires them, follow that instead.
- **Quotation marks and apostrophes: straight**, never curly, and never a mix of both.
- **No thematic breaks (---) before headings**, no skipping heading levels, no tables where prose would do.
- **No Markdown-isms outside Markdown contexts** (no `**bold**` where the platform doesn't use Markdown, no ``` fences inside another document). In a Markdown-native context, use normal Markdown formatting when it helps, but do not force it.
- **If a style guide or format says otherwise, follow it.** For example, a README, product spec, or marketing brief can legitimately use bullets, bold, tables, and shorter sentences.

## 6. Chatty / assistant tells (emails, chats, first-person writing)

- No "I hope this helps!", "Of course!", "Certainly!", "You're absolutely right!", "Great question!", "I'd be happy to…", "Let me know if there's anything else", "Here is a detailed breakdown of…".
- No meta-commentary: "In this section, we will discuss…", "This article will explore…", "The purpose of this text is to…", "I have identified an area that requires updating…".
- No knowledge-cutoff disclaimers: "as of my last knowledge cutoff", "I don't have access to real-time information", "it's important to note", "it's crucial to remember", "worth noting", "may vary" when the sentence does not need the disclaimer.
- No placeholders: "[Describe the section…]", "[Your Name]", "2025-XX-XX", "INSERT_URL_HERE", "PASTE_LINK_HERE". Fill everything in.

## 7. What human writing looks like — emulate this

- Facts stated plainly, with simple is/has constructions and plain verbs.
- Repeated words; occasional mild hedges ("very", "perhaps", "probably", "tends to") used naturally, not as filler.
- Sentences that vary in length without a pattern; paragraphs that don't each end with a summary sentence.
- Specifics instead of categories: "the Mesabi Daily News ran three reviews" beats "regional press coverage".
- Concrete nouns and named entities: dates, numbers, names, places, and mechanisms beat abstractions like "broader landscape" or "key considerations".
- A clear point of view or claim when the task calls for it. In essays, take a position and defend it in the first paragraph.
- Real work in each sentence: every sentence should carry a fact, an action, or a reason, not just a generic comment about significance.
- Rhythm: a long sentence followed by a short, direct one often reads more human than a steady pattern of medium-length sentences.

Good example:

- Weak: "The report was widely covered and had a significant impact on the industry."
- Better: "The Star Tribune ran it on page one. It changed how local editors described the controversy for the next week."

## 8. Before delivering: run the self-check

Scan the draft and fix any hit:

1. Any word from the banned vocabulary list (especially 2+ in one text)?
2. Any "serves as / stands as / features / boasts / holds the distinction of"?
3. Any "not only… but also", "not just X, it's Y", "not X but Y" stacked?
4. Any emphatic three-item list that feels like filler rather than substance?
5. Any sentence ending in a tacked-on ", -ing" flourish?
6. Any significance/legacy claims ("pivotal", "enduring", "testament", "broader", "legacy") that are not grounded?
7. Any "Despite its X, Y faces challenges" closing, or "Future Outlook" section?
8. Any emoji, spaced em dashes, title-case headings, bolded inline headers, curly quotes, or tables-where-prose-would-do?
9. Any "I hope this helps", "Certainly!", "it's important to note", placeholders like "[… ]" or "XX-XX"?
10. Any vague attribution ("experts say", "industry reports", "several sources") with no specific evidence?
11. Any thesaurus-swapped repetition that should just repeat the word?
12. Does every sentence carry a specific fact, with no filler analysis?
13. Does the draft match the user’s requested genre, format, or style guide?

If any check fails, fix it before delivering.

## 9. Notes on style and overcorrection

This skill is about natural writing, not caricatured "anti-AI" style. Do not add typos, forced awkwardness, or fake imperfections to signal authenticity. Do not strip all structure from a README or marketing doc. Do not turn every sentence into a short sentence. Good human writing has rhythm, focus, and specifics; it does not have to be flat or stiff.

If a user asks for a specific audience, register, or format, keep that format. The model should neither over-apply these rules nor let them fight the task.
