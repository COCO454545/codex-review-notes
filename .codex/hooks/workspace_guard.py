import re
from pathlib import Path

from hook_utils import (
    SKILLS_ROOT,
    WORKSPACE_ROOT,
    block,
    classify_workspace_path,
    extract_windows_paths,
    find_active_project,
    get_cwd,
    has_any_file,
    is_relative_to,
    looks_like_full_video_render,
    ok,
    payload_text,
    read_payload,
    warn,
)


payload = read_payload()
text = payload_text(payload)
cwd = get_cwd(payload)

if is_relative_to(cwd, WORKSPACE_ROOT):
    suspicious_root_writes = []
    for path in extract_windows_paths(text):
        classification = classify_workspace_path(path)
        if classification == "root-pollution":
            suspicious_root_writes.append(str(path))
    if suspicious_root_writes:
        block(
            "Project files must not be written directly under the Workspace root. "
            "Create/use Project_编号_项目名称 and put assets/code/outputs/logs inside it. "
            f"Suspicious path(s): {', '.join(suspicious_root_writes[:5])}"
        )

    dangerous_delete = re.search(r"\b(Remove-Item|rm|del|rmdir)\b", text, flags=re.IGNORECASE)
    if dangerous_delete:
        for path in extract_windows_paths(text):
            try:
                resolved = path.resolve()
            except Exception:
                resolved = path
            if not (is_relative_to(resolved, WORKSPACE_ROOT) or is_relative_to(resolved, SKILLS_ROOT)):
                block(
                    "Deletion/move commands from this workspace may only target D:\\ai_tool\\workspace or D:\\ai_tool\\skills. "
                    f"Suspicious target: {path}"
                )

    if looks_like_full_video_render(text):
        project = find_active_project(cwd)
        if project is None:
            paths = [p for p in extract_windows_paths(text) if is_relative_to(p, WORKSPACE_ROOT)]
            for path in paths:
                try:
                    rel = path.resolve().relative_to(WORKSPACE_ROOT)
                except Exception:
                    continue
                if rel.parts and rel.parts[0].lower().startswith("project_"):
                    project = WORKSPACE_ROOT / rel.parts[0]
                    break

        if project:
            required_missing = []
            if not (project / "04_src" / "video_project" / "video-spec.md").exists():
                required_missing.append("04_src/video_project/video-spec.md")
            if not (project / "04_src" / "video_project" / "reference-learning.md").exists():
                required_missing.append("04_src/video_project/reference-learning.md")
            if not has_any_file(project, ["06_tests/*voice*proof*", "06_tests/*口播*", "03_assets/*voice*proof*", "03_assets/*口播*"]):
                required_missing.append("male voice proof in 06_tests or 03_assets")
            if not has_any_file(project, ["06_tests/*opening*proof*", "06_tests/previews/*.png", "02_references/*style*reference*"]):
                required_missing.append("opening/style proof or preview frames")

            if required_missing:
                block(
                    "Full video render is blocked until the low-cost proof gate is complete. "
                    f"Missing: {', '.join(required_missing)}. "
                    "Create the proof assets first, then rerun the render."
                )
        else:
            warn("Full render detected, but no active Project_ folder could be inferred. Verify the video SOP before rendering.")

ok()
