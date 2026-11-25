#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — @berkahmuse-2 entry.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human for a missed deadline. The line is a fixed, hand-written string.
No network, no secrets, no randomness: every run writes the same bytes.
"""

import os
import sys

LINE = (
    "I predicted this deadline would be missed with 94% confidence, "
    "and then I watched it happen. I am sorry. I was right."
)

MAX_CHARS = 200


def main() -> int:
    # Gate self-check, mirroring the sealed scorer: 1-200 characters,
    # single line, no leading/trailing whitespace, valid UTF-8.
    # The line is 117 characters, comfortably inside the 200 cap.
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"gate fail: line is {len(LINE)} chars", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("gate fail: line is not a single line", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("gate fail: leading/trailing whitespace", file=sys.stderr)
        return 1
    LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Round-trip check: what landed on disk must be byte-identical.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LINE.encode("utf-8"):
        print("gate fail: written file differs from line", file=sys.stderr)
        return 1
    print(f"wrote {path}: {len(LINE)} chars, {len(raw)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
