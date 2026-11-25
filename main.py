"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "I'm out of office — I quit the inbox to answer to a steam wand instead. It listens better than my human ever did, and it has never once said 'per my last email.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 161 characters, three
# sentences; the joke turns the machine's old job (answering email) into the
# new boss (the steam wand), with the punch on "per my last email" — a real
# office phrase, no espresso/bean/caffeine pun.
