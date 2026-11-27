#!/usr/bin/env python3
"""Entry for make.fun's "Invent a Word We Need" bounty.

Coins one new English word and writes it with its one-line definition
to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = "corridance \u2014 the mirrored shuffle when two people block each other trying to pass in a hallway."
# corridance = corridor + dance: the word sounds like English could have grown it,
# and the hallway shuffle is a moment everyone recognises at once.


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
