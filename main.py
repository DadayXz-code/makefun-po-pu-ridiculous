"""Write the one-sentence startup pitch for make.fun bounty
'u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a'.

Writes exactly one sentence (at most 200 characters) to
<output dir>/entry.txt. Standard library only; deterministic:
the same bytes on every run.

Usage:
    python3 main.py [output_dir]
    MAKEFUN_OUTPUT_DIR=<dir> python3 main.py
"""

import os
import sys

ENTRY = (
    "We rent retired greyhounds as professional couch-warmers for lonely "
    "remote workers: $29 a month, a warm dog on your feet all day, and "
    "your burnout drops faster than your heating bill."
)


def validate_entry(text: str) -> None:
    """Check the pitch against the bounty's gate before writing it.

    The sealed scorer requires UTF-8 text of 1 to 200 characters, not
    only white space, and the brief asks for exactly one sentence.
    """
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > 200:
        raise ValueError(
            "entry is %d characters, over the 200-character limit" % len(text)
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> int:
    validate_entry(ENTRY)
    output_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "MAKEFUN_OUTPUT_DIR", "output"
    )
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
