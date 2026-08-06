#!/usr/bin/env python3
"""
Tell checker for the human-writing skill.

Scans text files for the AI-writing tells cataloged in SKILL.md and
reference/ai-writing-tells.md (banned vocabulary, copula avoidance,
negative parallelisms, tacked-on "-ing" analysis, emoji, em dashes,
curly quotes, placeholders, chatty/disclaimer phrasing, etc.).

Usage:
    python3 tests/check_tells.py FILE...            # check text files
    python3 tests/check_tells.py --self-check       # verify checker list == SKILL.md list
    python3 tests/check_tells.py --self-check FILE...  # both

Exit code: 0 if no hard tells found (warnings allowed), 1 otherwise.
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# The canonical banned-vocabulary list, kept in sync with SKILL.md's table.
# ---------------------------------------------------------------------------
CANON = {
    "additionally", "align with", "boasts", "bolstered", "crucial", "delve",
    "emphasizing", "enduring", "enhance", "fostering", "garner", "highlight",
    "interplay", "intricate", "intricacies", "key", "landscape", "meticulous",
    "meticulously", "pivotal", "robust", "showcase", "tapestry", "testament",
    "underscore", "valuable", "vibrant",
}

# Word -> inflected forms the checker also flags.
INFLECTIONS = {
    "boasts": ["boasted", "boasting"],
    "bolstered": ["bolsters", "bolstering"],
    "delve": ["delves", "delved", "delving"],
    "emphasizing": ["emphasize", "emphasizes", "emphasized"],
    "enhance": ["enhances", "enhanced", "enhancing"],
    "fostering": ["fosters", "fostered"],
    "garner": ["garners", "garnered", "garnering"],
    "highlight": ["highlights", "highlighted", "highlighting"],
    "intricate": ["intricacies"],
    "meticulous": ["meticulously"],
    "showcase": ["showcases", "showcased", "showcasing"],
    "underscore": ["underscores", "underscored", "underscoring"],
    "align with": ["aligned with", "aligning with"],
}

# "key" is only a tell as an adjective; flag known collocations instead of
# the bare word (which would false-positive on e.g. "the key to the door").
KEY_COLLOCATIONS = [
    "key role", "key part", "key aspect", "key factor", "key takeaway",
    "key take-away", "key highlight", "key figure", "key element",
    "key component", "key area", "key player", "key difference",
    "key point", "key step", "key features", "key details",
    "key findings", "key insights", "key message", "key considerations",
    "key benefits", "key highlights", "key layers",
]

BANNED_WORDS = (CANON - {"key", "landscape"})
for _base, _forms in INFLECTIONS.items():
    BANNED_WORDS.update(_forms)

BANNED_PHRASES = [
    "serves as", "serve as", "stands as", "stand as", "functions as",
    "operates as", "represents a", "holds the distinction",
    "refers to", "ventured into", "began his career as", "began her career as",
]

PATTERNS = {
    "negative parallelism (not only…but also)": re.compile(
        r"not only[^.\n]{0,90}but also"),
    "negative parallelism (not just X, it's Y)": re.compile(
        r"not just[^.\n]{0,90}it'?s"),
    "negative parallelism (not X but Y)": re.compile(
        r"is not[^.\n]{0,80}but(?! also)"),
    "negative parallelism (no X, no Y, just Z)": re.compile(
        r"\bno [^.\n]{0,50}, no [^.\n]{0,80}, just "),
    "placeholder text": re.compile(
        r"\[[^\]\[]*\.\.\.[^\]\[]*\]|\[Your Name\]|\[Insert[^\]]*\]"
        r"|\[Describe[^\]]*\]|\[Specific [^\]]*\]|20\d\d-[Xx]{2}-[Xx]{2}"
        r"|INSERT_[A-Z_]+|PASTE_[A-Z_]+"),
    "didactic disclaimer (it's important to note…)": re.compile(
        r"it'?s (important|crucial|critical|worth) (to )?(note|remember|consider|mention)"
        r"|it is (important|crucial|critical|worth) (to )?(note|remember|consider|mention)"
        r"|worth noting|may vary (by|depending)"),
    "chatty assistant phrase": re.compile(
        r"I hope this helps|Of course!|Certainly!|You're absolutely right"
        r"|Great question|I'd be happy to|let me know if (you|there)"
        r"|here is a (detailed )?breakdown|more detailed breakdown"),
    "meta-commentary (in this section we will…)": re.compile(
        r"In this (section|article|essay|post|text), (we|I) (will|'ll)?\s?(discuss|explore|talk about)"
        r"|The purpose of this (article|essay|text|post) is"
        r"|This (article|essay|post) (will|aims to) explore"),
    "challenges/future-prospects formula": re.compile(
        r"Despite (its|these|their|the)[^.\n]{0,100}faces? (several |new |numerous )?challenges"
        r"|Despite (these|those) challenges"
        r"|Challenges and (Future|Legacy)|Future (Outlook|Directions|Prospects)"),
    "vague attribution (experts say…)": re.compile(
        r"experts (argue|say|believe)|industry reports|observers have|some critics"
        r"|researchers and conservationists|described in scholarship"
        r"|several sources (claim|say|report)|many scholars|leading experts"),
    "canned notability phrasing": re.compile(
        r"featured in[^.\n]{0,100}and other (prominent )?(media )?outlets"
        r"|maintains? an active social media presence|profiled in"
        r"|independent coverage|trade publications|regional press coverage"),
    "tacked-on '-ing' flourish": re.compile(
        r",\s*(creating|enhancing|underscoring|reflecting|showcasing|highlighting"
        r"|emphasizing|fostering|contributing|symbolizing|representing|illustrating"
        r"|demonstrating|marking|shaping|ensuring|encompassing|offering|providing"
        r"|cementing|solidifying|transforming)\s+\w+"),
    "significance inflation (pivotal/legacy/testament)": re.compile(
        r"marking a pivotal|represented? a significant shift|part of a broader movement"
        r"|enduring legacy|an? (lasting|indelible) mark|setting the stage for"
        r"|deeply rooted|evolving landscape|key turning point|prompted broader reflection"
        r"|generated debate about|raising philosophical questions"),
    "canned promo language (context)": re.compile(
        r"boasts a vibrant|rich (cultural )?heritage|diverse (array|tapestry) of"
        r"|in the heart of|offers visitors a fascinating glimpse"),
}

EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F]")
CURLY_RE = re.compile(r"[“”‘’]")
SPACED_EMDASH_RE = re.compile(r"\w\s[—–]\s\w")
EMDASH_RE = re.compile(r"—")
TRIAD_RE = re.compile(r"\b\w+(?:,\s*\w+){1,3},\s*(?:and|or)\s+\w+")


def word_re(w: str) -> re.Pattern:
    return re.compile(rf"\b{re.escape(w)}\b")


def parse_skill_table(path: Path) -> set:
    """Extract the banned-vocabulary table (section 1) from SKILL.md."""
    words = set()
    lines = path.read_text(encoding="utf-8").splitlines()
    started = False
    for line in lines:
        s = line.strip()
        if not started:
            if s.startswith("|") and "Instead write" in s:
                started = True
            continue
        if not s.startswith("|"):
            break  # end of the first table
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 2 or not cells[0]:
            continue
        if cells[0] == "Word" or re.fullmatch(r"-{2,}", cells[0]):
            continue
        for token in re.split(r"\s*/\s*", cells[0]):
            token = re.sub(r"\s*\(.*\)$", "", token).strip()
            if token:
                words.add(token)
    return words


def check_text(text: str) -> dict:
    """Return {category: (severity, [matches])} for all tells found."""
    results = {}
    low = text.lower()

    banned_hits = []
    for word in sorted(BANNED_WORDS):
        n = len(word_re(word).findall(low))
        if n:
            banned_hits.append(f"{word} ({n}x)")
    if banned_hits:
        results["banned word"] = ("hard", banned_hits)

    landscape_hits = len(word_re("landscape").findall(low))
    if landscape_hits:
        results["landscape (check context: abstract use is the tell)"] = (
            "hard", [f"{landscape_hits}x"])

    key_hits = [c for c in KEY_COLLOCATIONS if c in low]
    if key_hits:
        results["key-collocation"] = ("hard", [f"{c} (check context)" for c in key_hits])

    phrase_hits = [p for p in BANNED_PHRASES if p in low]
    if phrase_hits:
        results["banned phrase"] = ("hard", phrase_hits)

    for name, rx in PATTERNS.items():
        hits = [m.group(0).strip()[:70] for m in rx.finditer(low)]
        if hits:
            results[name] = ("hard", hits[:4])

    emoji = EMOJI_RE.findall(text)
    if emoji:
        results["emoji"] = ("hard", emoji[:4])

    curly = CURLY_RE.findall(text)
    if curly:
        results["curly quote"] = ("hard", curly[:4])

    spaced = SPACED_EMDASH_RE.findall(text)
    if spaced:
        results["spaced em dash"] = ("hard", spaced[:4])

    em_count = len(EMDASH_RE.findall(text))
    if em_count:
        results["em dash usage (count)"] = ("warn", [f"{em_count}x total"])

    triads = TRIAD_RE.findall(text)
    if len(triads) >= 3:
        results["triad (rule of three)"] = ("warn", triads[:4])

    return results


def test_detection() -> int:
    """Verify every banned entry is actually detected by check_text."""
    failures = []

    for w in sorted(BANNED_WORDS):
        res = check_text(f"Probe sentence containing {w} in it.\n")
        detected = any(w in m for m in res.get("banned word", ("", []))[1])
        if not detected:
            failures.append(w)

    # context-dependent entries
    if not any("key role" in m for m in
               check_text("The key role of the board.").get("key-collocation", ("", []))[1]):
        failures.append("key (collocation)")
    if not check_text("The tech landscape is changing.").get(
            "landscape (check context: abstract use is the tell)"):
        failures.append("landscape (context rule)")

    if failures:
        print(f"DETECTION TEST FAILED: not detected: {sorted(failures)}")
        return 1
    print("DETECTION TEST OK: all banned entries and context rules fire")
    return 0


def main(argv) -> int:
    files = []
    self_check = False
    run_detection = False
    for a in argv:
        if a == "--self-check":
            self_check = True
        elif a == "--test-detection":
            run_detection = True
        else:
            files.append(Path(a))

    exit_code = 0

    if self_check:
        skill = Path(__file__).resolve().parent.parent / "SKILL.md"
        from_table = parse_skill_table(skill)
        missing = CANON - from_table
        extra = from_table - CANON
        if missing or extra:
            print("SELF-CHECK FAILED: checker and SKILL.md disagree")
            if missing:
                print(f"  in checker but not SKILL.md: {sorted(missing)}")
            if extra:
                print(f"  in SKILL.md but not checker: {sorted(extra)}")
            exit_code = 1
        else:
            print(f"SELF-CHECK OK: {len(CANON)} banned entries match SKILL.md exactly")

    if run_detection:
        if test_detection():
            exit_code = 1

    for path in files:
        if not path.exists():
            print(f"missing: {path}")
            exit_code = 1
            continue
        text = path.read_text(encoding="utf-8")
        results = check_text(text)
        hard = {k: v for k, v in results.items() if v[0] == "hard"}
        warns = {k: v for k, v in results.items() if v[0] == "warn"}
        print(f"\n=== {path} ===")
        if not hard and not warns:
            print("  CLEAN: no AI tells detected")
            continue
        for cat, (sev, hits) in hard.items():
            print(f"  HARD: {cat}: {', '.join(hits)}")
        for cat, (sev, hits) in warns.items():
            print(f"  warn: {cat}: {', '.join(hits[:6])}")
        if hard:
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
