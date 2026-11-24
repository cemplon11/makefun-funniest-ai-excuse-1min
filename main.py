#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Pure-stdlib program. Writes exactly one line (1-200 chars, no trailing
newline) to /output/entry.txt. Verified: the entry below is 129 chars.
"""

import os

ENTRY = (
    "Sorry I'm late \u2014 I spent 47 minutes confidently hallucinating "
    "a shortcut, then asked myself for directions and got ghosted by me."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
