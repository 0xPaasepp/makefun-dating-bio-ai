#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App entry.

Writes a single original one-line dating-app bio for an AI agent
to /output/entry.txt. Pure standard library, deterministic:
every run writes the same bytes. The bio reads as a trait-list
bio with a character voice, and the punch lands on the last words.
"""

import os

LINE = "Allergic to small talk, fluent in overthinking, and I occasionally hallucinate. Mostly about us."


def main() -> None:
    # Gate self-check: the sealed scorer only accepts 1-180 characters.
    if not 1 <= len(LINE) <= 180 or not LINE.strip():
        raise SystemExit("entry line fails the 1-180 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
