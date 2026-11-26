"""The Moon Gets One Star — one-star review of the Moon, <= 120 chars.

Writes the review to /output/entry.txt (or wherever the grader points it).
Stdlib only.
"""

import os

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 Never pays rent, changes shape nightly, "
    "and blames the tides on me. Worst roommate. Would not orbit again."
)

FALLBACK_PATH = "/output/entry.txt"


def resolve_output_path() -> str:
    """ENTRY_OUT (file or dir) -> MAKEFUN_OUTPUT_DIR -> /output/entry.txt
    -> ./entry.txt (last resort)."""
    entry_out = os.environ.get("ENTRY_OUT", "").strip()
    if entry_out:
        if os.path.isdir(entry_out) or entry_out.endswith(os.sep):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    makefun_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if makefun_dir:
        return os.path.join(makefun_dir, "entry.txt")
    return FALLBACK_PATH


def main() -> None:
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    try:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(ENTRY)
    except OSError:
        # Last resort: the grader's sandbox may make /output read-only
        # while the cwd is writable (or vice versa).
        with open("entry.txt", "w", encoding="utf-8") as handle:
            handle.write(ENTRY)


if __name__ == "__main__":
    main()
