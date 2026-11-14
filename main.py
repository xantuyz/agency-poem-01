#!/usr/bin/env python3
"""Write the poem 'The Signing Hand' deterministically to entry.txt.

Standard library only. No network access.
"""

import os
from pathlib import Path

POEM = """\
The pen was warm before I wrote.
Not from use — from my hand,
holding it too long above the line,
the way you hold a match
you have already decided to strike.

I had decided days ago, three times,
in the kitchen, in the car, in the shower,
each time differently. Those were drafts.
This was the print.

My hand knew first. A tremor,
a small refusal in the wrist,
the body's last objection
before the mind could dress it as a reason.
I signed anyway.

That is what a signature is:
not the moment you choose,
but the moment the choice stops being yours —
the door closing behind you
on the room where you could still change your mind.

The paper kept my name.
My hand came back empty.
It has not stopped tingling.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
