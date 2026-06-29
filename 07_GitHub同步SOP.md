# 07_GitHub同步SOP

> 本文档规定 `D:\Workspace` 中哪些内容可以同步到 GitHub，用于在家里电脑、公司电脑之间复用 Codex 使用偏好、复盘历史、SOP、hooks 和全局规则。

## 一、同步目标

同步的是“知识层”，不是“项目层”。

目标：

1. 公司电脑克隆后，能直接继承用户的 Codex 使用习惯。
2. 保留全局复盘、踩坑日志、工作区规则、预览优先流程和协作偏好。
3. 避免把真实项目资料、题库、音视频、大文件、密钥或隐私数据传到 GitHub。

## 二、推荐仓库

当前同步仓库：

```text
https://github.com/COCO454545/codex-review-notes
```

建议保持为私有仓库。如果未来确认不含隐私，也可以考虑公开部分模板，但默认私有。

历史建议名称：

```text
codex-personal-workbench
```

## 三、允许同步

默认允许同步：

```text
AGENTS.md
00_全局控制台.md
01_全局复利踩坑日志.md
02_全局项目索引.md
03_新项目创建SOP.md
04_ClaudeCode搭配Codex六种接线机制操作手册.md
05_Cyrus說AI视频_Claude自动化调教分析.md
06_工作区提示词.md
07_GitHub同步SOP.md
协作偏好_沟通复盘.md
.codex/hooks.json
.codex/hooks/*.py
.codex/hooks/*.md
claude/skills/*.md          ← 新增：Claude Code 通用文本 Skills
skills/ai-video-production-skill/
Project_00_全局工作台/
sync/*.md                   ← 新增：同步机制文档
```

说明：

- `02_全局项目索引.md` 可以同步，但只能保留非敏感项目名称和状态；如果包含客户、隐私、账号或商业信息，应先脱敏。
- `Project_00_全局工作台` 只能放模板、共享材料和无敏感内容。
- `skills/` 只同步自建或深度个人化的轻量 skill。允许少量用于说明风格的预览图和小音频，禁止同步最终视频、大素材包、缓存、依赖目录和第三方完整仓库。

## 四、禁止同步

默认禁止同步：

```text
Project_*/
*.env
*.key
*.pem
*.pfx
*.token
*.mp4
*.mp3
*.wav
*.pdf
*.docx
*.xlsx
*.zip
*.7z
*.rar
node_modules/
dist/
dist_*/
build/
99_temp/
__pycache__/
```

也禁止同步：

- API key、token、密码、cookie。
- 真实用户数据、客户数据、题库原始数据。
- 线上后台地址、管理密码、分享码密码。
- 未确认可公开的截图、聊天记录、课程资料。

## 五、同步流程

1. 先检查 `.gitignore` 是否排除了项目层和敏感文件。
2. 运行 `git status`，确认只出现全局 md、hooks、模板等知识层文件。
3. 检查 diff，确认没有密钥、密码、真实数据。
4. commit 信息写清楚本次同步内容。
5. push 到私有 GitHub 仓库。
6. 公司电脑 clone 后，把仓库作为 workspace 的全局规则源使用。

## 六、公司电脑使用方式

推荐方式：

```powershell
git clone <你的私有仓库地址> D:\Workspace
```

如果公司电脑已有项目目录，则不要覆盖项目，先克隆到临时目录，再复制全局 md 和 `.codex/hooks`。

## 七、重要原则

1. 全局复盘、偏好、SOP、hooks、skills 可以同步。
2. 真实项目默认不同步。
3. 要同步某个项目时，必须单独判断安全等级。
4. 任何上传 GitHub 的动作，都必须先看 `git status` 和 diff。
5. 不确定是否敏感时，默认不同步。
6. 每次同步前优先检查是否有新规则需要沉淀：Codex 能力优先、开源 skill 调研、预览 proof、项目不变量、复盘方法和 hooks。
7. 同步个人 skills 前，先确认它是自建/个人化沉淀，而不是未经整理的第三方完整仓库。

## 八、延伸阅读

- [sync/README.md](sync/README.md) - 详细的跨设备同步操作指南、冲突处理流程
- [sync/sync-log.md](sync/sync-log.md) - 同步历史日志
