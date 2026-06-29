#!/usr/bin/env python3
"""Plan or delete common video-production junk inside a project directory."""

import argparse
import shutil
from pathlib import Path


JUNK_DIR_NAMES = {
    ".git",
    ".cache",
    ".next",
    ".video_refs",
    "node_modules",
    "tmp",
    "temp",
    "frames",
    "work",
    "recovered_frames",
    "snapshots",
}

JUNK_FILE_SUFFIXES = {
    ".log",
    ".tmp",
}


def is_inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def find_candidates(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for path in root.rglob("*"):
        name = path.name.lower()
        if path.is_dir() and (name in JUNK_DIR_NAMES or name.startswith("work-")):
            candidates.append(path)
        elif path.is_file() and path.suffix.lower() in JUNK_FILE_SUFFIXES:
            candidates.append(path)
        elif path.is_file() and (name.startswith("draft_") or name.startswith("old_")) and path.suffix.lower() == ".mp4":
            candidates.append(path)
    return candidates


def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan or delete common video-production junk.")
    parser.add_argument("root", help="Project/export directory to clean")
    parser.add_argument("--execute", action="store_true", help="Actually delete candidates. Default is dry-run.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"ERROR: root is not a directory: {root}")

    candidates = [p for p in find_candidates(root) if is_inside(p, root)]
    mode = "DELETE" if args.execute else "DRY-RUN"
    print(f"{mode}: {len(candidates)} cleanup candidates under {root}")
    for path in candidates:
        print(path)
    if args.execute:
        for path in sorted(candidates, key=lambda p: len(p.parts), reverse=True):
            if path.exists() and is_inside(path, root):
                remove_path(path)
        print("Cleanup complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
