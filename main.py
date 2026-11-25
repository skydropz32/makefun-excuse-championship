"""One-line excuse for make.fun's The One-Line Excuse Championship.

Writes a single deterministic excuse line to /output/entry.txt.
Python standard library only; no input, no randomness, no network.
"""

import os

LINE = "I saved your work in the one place no hacker would ever look: my short-term memory."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
