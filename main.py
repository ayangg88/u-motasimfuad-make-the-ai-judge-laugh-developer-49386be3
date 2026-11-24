#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt (under 200 characters).

The line turns the worn "the server crashed" excuse around: the server
is not the victim of the code, it is a weary bystander that quit after
one too many 2 a.m. commits. The twist lands on the late-night deploy,
which every developer recognises.
"""
import os

ENTRY = "The server didn't crash \u2014 it just saw my 2 a.m. commit and filed for early retirement."


def main():
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
