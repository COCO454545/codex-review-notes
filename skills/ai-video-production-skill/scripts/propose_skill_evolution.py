#!/usr/bin/env python3
"""Create a bounded skill-evolution proposal from project review notes."""

import argparse
import datetime as dt
from pathlib import Path


TEMPLATE = """# skill-evolution-proposal

## Source Evidence

- Project: {project}
- Date: {date}
- Artifacts reviewed:
{artifacts}
- User feedback:

## Run Score

- Hard checks:
- Soft quality:
- Final status:

## Lesson

- What happened:
- Why it matters:
- Future behavior to change:

## Classification

- Type: SKILL_DEFECT / EXECUTION_LAPSE / PROJECT_FACT
- Reason:

## Proposed Edit

- Target file:
- Edit type: add / replace / delete / script / template / reference
- Smallest change:

## Gate

- Would this prevent a repeated failure?
- Would this preserve existing strengths?
- Is it supported by evidence?
- Is it compact enough for the skill?

## Validation

- Command: python C:/Users/Lenovo/.codex/skills/.system/skill-creator/scripts/quick_validate.py D:/ai_tool/skills/ai-video-production-skill
- Expected result: Skill is valid!
"""


def collect_artifacts(project: Path) -> list[Path]:
    names = [
        "video-spec.md",
        "DESIGN.md",
        "reference-learning.md",
        "review/video-retrospective.md",
    ]
    found = [project / name for name in names if (project / name).exists()]
    for folder in ["logs", "review", "previews"]:
        root = project / folder
        if root.exists():
            found.extend(sorted(p for p in root.rglob("*") if p.is_file())[:10])
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a bounded skill-evolution proposal.")
    parser.add_argument("project", help="Video project directory")
    parser.add_argument("--output", help="Output proposal markdown path")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    if not project.exists() or not project.is_dir():
        raise SystemExit(f"ERROR: project is not a directory: {project}")

    artifacts = collect_artifacts(project)
    artifact_lines = "\n".join(f"  - {p}" for p in artifacts) if artifacts else "  -"
    output = Path(args.output).resolve() if args.output else project / "review" / "skill-evolution-proposal.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        TEMPLATE.format(
            project=project,
            date=dt.date.today().isoformat(),
            artifacts=artifact_lines,
        ),
        encoding="utf-8",
    )
    print(f"Wrote skill evolution proposal: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
