#!/usr/bin/env python3
"""Entry for the make.fun bounty "One Line of Earned Pride"
(u-mang-one-line-of-earned-pride-a0138557).

The whole entry is one line: a night janitor who taught himself to
read from the posters in the classrooms he cleaned signs his
daughter's report card without asking anyone to read it first. The
pride is never named or congratulated — it is earned inside the
scene, by the years of effort the first half implies and the small,
concrete act the second half shows.

The program writes that single line to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "The night janitor taught himself to read from the posters in the "
    "classrooms he cleaned; this morning he signed his daughter's "
    "report card without asking anyone to read it first."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 240 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 240:
        raise ValueError(f"entry is {len(line)} characters, outside 1..240")
    if len(encoded) > 240:
        raise ValueError("entry encodes to more than 240 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
