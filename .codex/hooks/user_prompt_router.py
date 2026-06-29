from hook_utils import ok, read_payload, payload_text, warn


payload = read_payload()
text = payload_text(payload)

if any(term in text for term in ("新项目", "创建项目", "项目文件", "生成视频", "口播", "复盘", "沉淀skill", "沉淀 skills")):
    warn(
        "Workspace SOP applies: identify/create Project_编号_项目名称 first, keep files inside the project folder, "
        "and update 02_全局项目索引.md when status changes."
    )

if any(term in text.lower() for term in ("skill", "skills", "插件", "plugin", "github", "开源", "脚本", "script", "自动化", "工作流")):
    warn(
        "Capability discovery gate applies: check available Codex skills/plugins/apps/MCP tools/hooks/scripts and "
        "D:\\ai_tool\\skills first; if insufficient, inspect first-hand GitHub/official references and capture reusable patterns."
    )

if any(term in text.lower() for term in ("生成视频", "口播", "hyperframes", "remotion", "ffmpeg", "mp4")):
    warn(
        "Video SOP applies: learn references first, create video-spec/reference-learning, make opening proof "
        "and male voice proof before expensive full render, then run final quality checks."
    )

ok()
