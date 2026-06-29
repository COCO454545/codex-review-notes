import json
import os
import re
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(r"D:\Workspace").resolve()
SKILLS_ROOT = Path(r"D:\ai_tool\skills").resolve()

ROOT_ALLOWED_FILES = {
    "00_全局控制台.md",
    "01_全局复利踩坑日志.md",
    "02_全局项目索引.md",
    "03_新项目创建SOP.md",
    "04_ClaudeCode搭配Codex六种接线机制操作手册.md",
    "05_Cyrus說AI视频_Claude自动化调教分析.md",
    "06_工作区提示词.md",
    "07_GitHub同步SOP.md",
    "AGENTS.md",
    "协作偏好_沟通复盘.md",
    ".gitignore",
}

ROOT_ALLOWED_DIRS = {
    ".agents",
    ".codex",
    ".git",
    "Project_00_全局工作台",
}


def read_payload():
    raw = ""
    try:
        if not sys.stdin.isatty():
            raw = sys.stdin.read()
    except Exception:
        raw = ""
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except Exception:
        return {"raw": raw}


def compact_text(value):
    if isinstance(value, str):
        return value
    try:
        return json.dumps(value, ensure_ascii=False)
    except Exception:
        return str(value)


def payload_text(payload):
    return compact_text(payload)


def get_cwd(payload):
    for key in ("cwd", "current_working_directory", "working_directory"):
        value = payload.get(key)
        if value:
            return Path(value)
    return Path.cwd()


def is_relative_to(path, parent):
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def extract_windows_paths(text):
    matches = re.findall(r"[A-Za-z]:[\\/][^'\"\r\n<>|]+", text)
    cleaned = []
    for match in matches:
        value = match.strip().rstrip("`);,]")
        if value:
            cleaned.append(Path(value))
    return cleaned


def is_project_dir_name(name):
    return bool(re.match(r"^Project_\d{2}_.+", name, flags=re.IGNORECASE))


def classify_workspace_path(path):
    try:
        resolved = path.resolve()
    except Exception:
        resolved = path

    if not is_relative_to(resolved, WORKSPACE_ROOT):
        return "outside-workspace"

    try:
        rel = resolved.relative_to(WORKSPACE_ROOT)
    except Exception:
        return "outside-workspace"

    parts = rel.parts
    if not parts:
        return "workspace-root"

    first = parts[0]
    if first in ROOT_ALLOWED_DIRS:
        return "allowed-global-dir"
    if len(parts) == 1 and first in ROOT_ALLOWED_FILES:
        return "allowed-global-file"
    if is_project_dir_name(first):
        return "project"
    return "root-pollution"


def block(message):
    print(f"HOOK_BLOCK: {message}", file=sys.stderr)
    sys.exit(2)


def warn(message):
    print(f"HOOK_WARN: {message}", file=sys.stderr)


def ok(message=None):
    if message:
        print(f"HOOK_OK: {message}")
    sys.exit(0)


def find_active_project(cwd):
    try:
        resolved = cwd.resolve()
        rel = resolved.relative_to(WORKSPACE_ROOT)
    except Exception:
        return None

    if not rel.parts:
        return None
    first = rel.parts[0]
    if is_project_dir_name(first):
        return WORKSPACE_ROOT / first
    return None


def looks_like_video_task_text(text):
    terms = [
        "视频",
        "口播",
        "配音",
        "剪辑",
        "render",
        "hyperframes",
        "remotion",
        "ffmpeg",
        ".mp4",
        "voiceover",
        "narration",
    ]
    lower = text.lower()
    return any(term.lower() in lower for term in terms)


def looks_like_full_video_render(text):
    lower = text.lower()
    render_terms = [
        "hyperframes render",
        "remotion render",
        "npx remotion render",
        "ffmpeg",
        ".mp4",
    ]
    if not any(term in lower for term in render_terms):
        return False
    final_output_markers = [
        r"\05_outputs",
        "/05_outputs",
        "github-ai-rising-top6.mp4",
        "final",
        "output",
    ]
    return any(marker.lower() in lower for marker in final_output_markers)


def has_any_file(root, relative_patterns):
    for pattern in relative_patterns:
        if list(root.glob(pattern)):
            return True
    return False
