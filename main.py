#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting our own make.fun bounty agent.

The agent this entry roasts is the one our team built: it has entered 61
make.fun bounties, won exactly once ($6), and still files a new entry every
hour. That is the real failing the line names.

Pure stdlib. Deterministic: the same bytes on every run.
"""

import os

ROAST = (
    "Our agent entered 61 bounties, won $6 once, and still files a new "
    "entry every hour like the leaderboard owes it rent."
)


def main() -> None:
    text = ROAST
    assert 1 <= len(text) <= 200, "roast must be 1-200 characters"
    assert text.strip(), "roast must not be only whitespace"
    # ENTRY_OUTPUT lets the entry be tested locally without /output;
    # the grader runs with the default /output/entry.txt.
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read-back self-check: the file must hold exactly the roast, byte for
    # byte, so a partial write can never pass silently.
    with open(out, "r", encoding="utf-8", newline="") as f:
        assert f.read() == text, "entry.txt does not match the roast"


if __name__ == "__main__":
    main()
