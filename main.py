#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — MakeFun entry.

Writes exactly one number in digits and nothing else to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Standard library only, no network, deterministic.
"""

import os
import sys

NUMBER = "73"


def main() -> int:
    if not NUMBER.isdigit():
        print("entry is not digits only", file=sys.stderr)
        return 1
    if not 1 <= len(NUMBER) <= 5:
        print("entry must be 1 to 5 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(NUMBER)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != NUMBER or not written.isdigit():
        print("verification failed: entry.txt is not the digits", file=sys.stderr)
        return 1
    # The gate counts bytes: exactly the digits, no newline, no padding.
    if os.path.getsize(path) != len(NUMBER.encode("ascii")):
        print("verification failed: entry.txt has unexpected size", file=sys.stderr)
        return 1
    print(NUMBER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
