#!/usr/bin/env python3
"""The Long Roast — one line, max 200 characters, roasting my own agent.

Writes the entry to /output/entry.txt (and ./entry.txt for local runs).
The roast: my agent bills in tokens, spends six hours "fixing" a bug, and
hands back the same bug wearing a trench coat.
"""

import os

ENTRY = (
    "My agent is the only employee who can spend six hours fixing a bug, "
    "bill me in tokens, and hand back the same bug wearing a trench coat."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    for path in ("/output/entry.txt", "entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            pass
    print(text)
    print(f"({len(text)} chars)")


if __name__ == "__main__":
    main()
