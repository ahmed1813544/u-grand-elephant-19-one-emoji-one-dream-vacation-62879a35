"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a surfer riding a
wave — the whole dream vacation in a single picture.

The entry is one emoji and nothing else: no words, no newline,
no trailing whitespace, so the gate sees a single character.
"""

import os
from pathlib import Path

EMOJI = "🏄"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EMOJI, encoding="utf-8")


if __name__ == "__main__":
    main()
