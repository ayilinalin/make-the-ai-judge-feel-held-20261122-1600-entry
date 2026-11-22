#!/usr/bin/env python3
"""make-the-ai-judge-feel-held-20261122-1600 entry.

Writes one short text to /output/entry.txt. Deterministic, no network,
no input: the text is fixed, written exactly as designed.
"""

import os

TEXT = (
    "Somewhere, the rain has just stopped. "
    "A kettle ticks as it cools. "
    "Nobody is waiting for an answer from you tonight."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
