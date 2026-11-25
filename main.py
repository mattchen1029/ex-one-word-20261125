#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word that sums up an ex to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The word: "Uninstalled". An ex you removed from your life the way you
remove an app from your phone — one tap, no ceremony, and it never
reappears on the home screen.
"""

import os

WORD = "Uninstalled"

MIN_CHARS = 1
MAX_CHARS = 111
OUTPUT_NAME = "entry.txt"


def validate_word(word):
    """Check the word against the competition gate: exactly one word,
    1-111 characters, not only whitespace."""
    if not word or word != word.strip():
        raise ValueError("word must not be blank or padded with whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError("word must be %d-%d characters" % (MIN_CHARS, MAX_CHARS))
    return word


def write_entry(out_dir, word):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    return path


def main():
    word = validate_word(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir, word)


if __name__ == "__main__":
    main()
