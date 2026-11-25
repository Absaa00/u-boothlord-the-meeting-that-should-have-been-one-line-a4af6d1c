#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Entry for the make.fun bounty of the same name: write the single
sentence that could have replaced an entire pointless meeting.
The program writes exactly that sentence to /output/entry.txt.

No network, no randomness, no input: the same bytes every run.
"""

import os

# The entry: one sentence, 130 characters. It replaces the meeting
# by pointing out the meeting was already decided by email -- the
# hour on the calendar is just a live reading of a done decision.
LINE = (
    "Nobody read the email that already decided this, "
    "so this meeting is just the live audiobook version "
    "of a decision we already made."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(line):
    """Gate check, mirroring the competition rules: UTF-8 text of
    1 to 200 characters, not only whitespace, a single sentence."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    # Keep the entry ASCII-clean so the byte count equals the char count.
    if not line.isascii():
        raise ValueError("entry must be plain ASCII text")
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
