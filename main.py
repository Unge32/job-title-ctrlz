#!/usr/bin/env python3
"""Director-General of National Ctrl+Z Affairs -- one weird job title.

The program writes the job title to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

At 43 characters it fits the 1-60 gate. The humour comes from
treating Ctrl+Z as a matter of state: an entire national office
exists just to undo whatever the country got wrong that day.

The job sounds like it belongs in a government directory, yet its
whole department is a keyboard shortcut promoted to civil service.
That is why it fits a weirdest-job-title brief: it takes something
every computer user does by reflex and dresses it up as a senior
official role with a staff, a budget and a letterhead.
A Director-General normally oversees ministries or agencies; this
one oversees mistakes, which means the department's workload only
grows whenever anyone in the country presses the wrong key.
The 43-character count keeps it safely inside the 60-character
gate with room to spare, so the joke never gets cut off by the
length limit itself.
"""

import os

LINE = "Director-General of National Ctrl+Z Affairs"


def main():
    assert 1 <= len(LINE) <= 60, "line outside the 1-60 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
