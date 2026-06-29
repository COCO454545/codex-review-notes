from pathlib import Path

from hook_utils import (
    WORKSPACE_ROOT,
    block,
    find_active_project,
    get_cwd,
    has_any_file,
    is_relative_to,
    ok,
    read_payload,
    warn,
)


payload = read_payload()
cwd = get_cwd(payload)

if not is_relative_to(cwd, WORKSPACE_ROOT):
    ok()

project = find_active_project(cwd)
if project is None:
    ok()

project_name = project.name

required = [
    "00_project_brief.md",
]
missing = [item for item in required if not (project / item).exists()]

has_outputs = has_any_file(project, ["05_outputs/*"])
has_logs = has_any_file(project, ["07_logs/*.md", "07_logs/*.txt"])
has_review = has_any_file(project, ["08_review/*.md", "06_tests/*quality*"])

if not has_logs:
    warn(f"{project_name}: no project log found under 07_logs.")
if has_outputs and not has_review:
    block(
        f"{project_name}: output files exist but no review/quality evidence was found. "
        "Add 06_tests quality evidence or 08_review review notes before calling the task complete."
    )

video_like = has_any_file(project, ["05_outputs/*.mp4", "03_assets/*.mp3", "03_assets/*.wav", "04_src/**/video-spec.md"])
if video_like:
    video_missing = []
    if not has_any_file(project, ["04_src/**/video-spec.md"]):
        video_missing.append("video-spec.md")
    if not has_any_file(project, ["04_src/**/reference-learning.md", "02_references/*"]):
        video_missing.append("reference-learning or references")
    if has_outputs and not has_any_file(project, ["06_tests/*quality*", "06_tests/previews/*.png"]):
        video_missing.append("quality report or preview frames")
    if video_missing:
        block(f"{project_name}: video completion evidence missing: {', '.join(video_missing)}.")

if missing:
    warn(f"{project_name}: missing standard project file(s): {', '.join(missing)}.")

ok()
