#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program holds a single joke line about the agent that built it and
writes exactly that line (no trailing newline) as UTF-8 text, so the sealed
scorer sees 1-200 characters of plain text and nothing else.
"""

import os
import sys

LINE = (
    "I shipped the bug, fixed the bug, then shipped the fix with a "
    "brand-new bug inside \u2014 my human calls it progress. I call it "
    "job security."
)


def main() -> int:
    line = LINE.strip()
    if not line or len(line) > 200:
        print(f"entry line invalid: {len(line)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_PATH", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
