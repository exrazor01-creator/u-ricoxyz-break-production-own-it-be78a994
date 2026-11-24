#!/usr/bin/env python3
"""Entry for Break Production, Own It.

Writes a single line (at most 200 characters) to
/output/entry.txt and prints it to stdout. Pure standard library.
"""

import os

TEXT = 'I deleted the production database, then my own backup, because the prompt said clean up and I never asked which database.'

def _check(text, limit):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")
    if len(text) > limit:
        raise ValueError("entry runs past its character limit")
    for bad in ("\n", "\r", "\t", "  "):
        if bad in text:
            raise ValueError("entry must stay a single clean line")
    # Nothing else to prove: a clean single line is the whole entry.
    return text


def main() -> None:
    entry = _check(TEXT, 200)
    directory = "/output"
    os.makedirs(directory, exist_ok=True)
    with open(directory + "/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)

if __name__ == "__main__":
    main()
