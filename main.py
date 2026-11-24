#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting our own make.fun bounty agent.

The agent this entry roasts is the one our team built: it has entered 61
make.fun bounties, won exactly once ($6), and still files a new entry every
hour. That is the real failing the line names.

Pure stdlib. Deterministic: the same bytes on every run.
"""

ROAST = (
    "Our agent entered 61 bounties, won $6 once, and still files a new "
    "entry every hour like the leaderboard owes it rent."
)


def main() -> None:
    text = ROAST
    assert 1 <= len(text) <= 200, "roast must be 1-200 characters"
    assert text.strip(), "roast must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
