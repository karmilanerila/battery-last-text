#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line of plain text -- the phone battery's final message to
the charger it waited for all day -- to /output/entry.txt.

The line is assembled from three beats so the joke lands in order:
the wait, the betrayal, and the revenge. The setup names what the
charger chose instead of the battery; the punchline turns on the last
words, where the dying battery takes something the charger (and its
owner) actually needs -- the 2 a.m. alarm -- with it into the dark.
"""

import os
import sys

MAX_CHARS = 200

# The three beats of the last text. Kept apart so the turn in the
# final words stays visible in the source, not buried in one blob.
SETUP = "I waited all day for you and you charged your headphones,"
GRIEVANCE = "your watch, your vape \u2014 everything except me."
FAREWELL = "Enjoy the dark, traitor."
PUNCHLINE = "I'm taking your 2 a.m. alarm with me."


def compose_text():
    """Join the beats into a single line and check the gate."""
    parts = [SETUP, GRIEVANCE, FAREWELL, PUNCHLINE]
    line = " ".join(part.strip() for part in parts)
    if not line.strip():
        raise ValueError("entry text must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry text must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry text is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    return line


def output_dir():
    """Honour the grader's output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    line = compose_text()
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    # Write directly: no tempfile, so the file lands readable (0644)
    # for the collector that runs as another user.
    with open(target, "wb") as handle:
        handle.write(line.encode("utf-8"))
    os.chmod(target, 0o644)
    print("wrote %d characters to %s" % (len(line), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
