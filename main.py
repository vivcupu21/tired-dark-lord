"""Write the villain monologue to the grader's output directory.

Stdlib only. The monologue lives in entry.txt next to this file; this
program copies it byte-identical to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    dest = Path(out_dir) / "entry.txt"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
