#!/usr/bin/env python3
"""Initialize a clean video production project."""

import argparse
import shutil
from pathlib import Path


DEFAULT_DIRS = [
    "assets",
    "previews",
    "exports",
    "logs",
    "review",
    "scripts",
    "src",
]


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_if_missing(src: Path, dst: Path) -> None:
    if src.exists() and not dst.exists():
        shutil.copy2(src, dst)


def init_project(path: Path, title: str | None = None) -> list[Path]:
    path.mkdir(parents=True, exist_ok=True)
    created = [path]
    for name in DEFAULT_DIRS:
        target = path / name
        target.mkdir(exist_ok=True)
        created.append(target)

    templates = skill_root() / "assets" / "templates"
    copy_if_missing(templates / "video-spec-template.md", path / "video-spec.md")
    copy_if_missing(templates / "retrospective-template.md", path / "review" / "video-retrospective.md")

    design = path / "DESIGN.md"
    if not design.exists():
        design.write_text(f"# DESIGN\n\n- Title: {title or path.name}\n- Style:\n- Layout:\n- Motion:\n", encoding="utf-8")

    learning = path / "reference-learning.md"
    if not learning.exists():
        learning.write_text(
            "# reference-learning\n\n| Source | Strength | Reuse | Do not copy |\n|---|---|---|---|\n",
            encoding="utf-8",
        )
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a clean video production project.")
    parser.add_argument("path", help="Project directory to create or update")
    parser.add_argument("--title", help="Human-readable video title")
    args = parser.parse_args()

    project = Path(args.path).resolve()
    init_project(project, args.title)
    print(f"Initialized video project: {project}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
