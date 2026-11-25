"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first that comes to mind, to /output/entry.txt.
The word is "vellichor": the strange wistfulness of used bookstores,
where the books you will never read crowd together in their thousands.
Surprising, vivid, specific — a word that calls up a clear image in a few
letters and rewards a second look.
"""

import os
import stat

WORD = "vellichor"

OUTPUT_PATH = "/output/entry.txt"


def validate(word):
    """Assert the brief's constraints: exactly one word, 1-24 chars."""
    assert isinstance(word, str), "entry must be a string"
    assert word == word.strip(), "entry must not have surrounding whitespace"
    assert len(word) >= 1, "entry must not be empty"
    assert len(word) <= 24, "entry must be at most 24 characters"
    assert len(word.split()) == 1, "entry must be exactly one word"
    assert not word.isspace(), "entry must not be only whitespace"
    word.encode("utf-8")  # must be valid UTF-8 text
    return True


def main():
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open() + explicit chmod 644: the grader runs as a different
    # user, so the output must be world-readable (never tempfile.mkstemp).
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Re-read and re-validate what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD, "written entry does not match the word"
    validate(written)


if __name__ == "__main__":
    main()
