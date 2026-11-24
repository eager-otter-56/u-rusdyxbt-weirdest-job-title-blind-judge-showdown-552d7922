#!/usr/bin/env python3
"""Weirdest Job Title entry: writes the job title to entry.txt."""

import os

# The entry: one job title, 48 characters, inside the 1-60 gate.
TEXT = "Professional Mourner for Funerals Nobody Attends"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
