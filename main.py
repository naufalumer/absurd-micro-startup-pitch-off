"""Absurd Micro-Startup Pitch-Off entry: write one pitch to /output/entry.txt.

Fully deterministic: the pitch is hardcoded, no randomness, no clock, no network.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The pitch is a literal on purpose: the grader runs the program twice and
# both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
LINE = (
    "TokenDiet is a $5-a-month service that shrinks a lazy AI agent's own "
    "40,000-token chat history into a 200-token cheat sheet before each run, "
    "so it stops paying to re-read words it already wrote."
)


def main() -> None:
    text = LINE.strip()
    # Gate: the sealed scorer accepts 1 to 200 characters. Fail loudly here
    # rather than shipping an invalid entry if the pitch is ever edited.
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, gate allows 1-200")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
