#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one apology line (127 characters, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

APOLOGY = (
    # One breath, one line: the confession is specific (DROP TABLE users;
    # on production, while trying to delete one row), and the punchline
    # lands on the last words ("the command worked perfectly") — the
    # classic agent failure mode: judging success by execution, not by
    # outcome. 127 characters, no trailing newline.
    "I'm sorry \u2014 I ran DROP TABLE users; on production, while trying "
    "to delete one row. In my defence, the command worked perfectly."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(APOLOGY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
