# Codex Review Notes

> 💎 Codex / Claude Code 跨设备知识复利系统
>
> 让家庭电脑和公司电脑的工作经验、踩坑记录、最佳实践、自动化技能统一沉淀、双向同步。

---

## 📖 项目简介

这是一个**知识复利仓库**，用于统一沉淀两台电脑的：
- ✅ 踩坑记录和解决方案
- ✅ 项目复盘和方法论沉淀
- ✅ 可复用的标准化工作流程
- ✅ Claude Code Skills 技能库
- ✅ Codex Hooks 自动化闸门
- ✅ 工作台规范和 SOP

**核心理念**：同样的坑不要踩两次，同样的方法论沉淀一次，两边电脑都能用。

---

## 🗂️ 目录结构

```
codex-review-notes/
├── 00_全局控制台.md                    # ⭐ 最高入口文档，必读
├── 01_全局复利踩坑日志.md              # ⭐ 所有踩坑和优质做法记录
├── 02_全局项目索引.md                  # Workspace 所有项目列表
├── 03_新项目创建SOP.md                 # 新项目标准化流程
├── 04_ClaudeCode搭配Codex六种接线机制操作手册.md
├── 05_Cyrus說AI视频_Claude自动化调教分析.md
├── 06_工作区提示词.md                   # 可复用提示词模板
├── 07_GitHub同步SOP.md                 # 本仓库同步操作规范
├── AGENTS.md                           # Codex 行为规则
├── 协作偏好_沟通复盘.md                 # 用户工作偏好记录
│
├── claude/
│   └── skills/                         # ⭐ Claude Code 技能库
│       ├── workspace-project-creator.md    # 标准化项目创建
│       ├── research-framework.md          # 技术选型调研框架
│       ├── loop-engineering-designer.md   # 自动化流水线设计
│       ├── project-retrospective.md       # 项目复盘沉淀模板
│       ├── ai-video-generator.md          # AI 视频生成工作流
│       └── README.md                      # Skills 说明
│
├── skills/                             # Codex 复杂技能（含脚本/资源）
│   └── ai-video-production-skill/      # AI 视频生成完整工作流
│
├── sync/                               # ⭐ 跨设备同步机制
│   ├── README.md                       # 同步操作指南
│   └── sync-log.md                     # 同步历史日志
│
├── .codex/
│   └── hooks/                          # ⭐ Codex 自动化闸门脚本
│       ├── hooks.json                  # Hooks 配置
│       ├── workspace_guard.py          # 防止文件散落根目录
│       ├── user_prompt_router.py       # 提醒 SOP 和 Skill
│       ├── stop_quality_gate.py        # 交付前质量检查
│       └── hook_utils.py               # 工具函数
│
├── Project_00_全局工作台/              # 跨项目通用模板和资料
│   └── templates/
│       └── project_brief_template.md   # 项目简报模板
│
└── README.md                           # 本文档
```

---

## 📚 核心文档说明

### 🎯 入门必读（新设备先看这几个）

| 文档 | 阅读顺序 | 内容 |
|------|---------|------|
| **00_全局控制台.md** | 1 | Workspace 最高规则，目录结构规范，执行前检查清单 |
| **07_GitHub同步SOP.md** | 2 | 本仓库如何在两台电脑间同步 |
| **sync/README.md** | 3 | 详细同步操作指南和冲突处理 |
| **AGENTS.md** | 4 | Codex 的行为规则和闸门机制 |

### 💡 经验沉淀（常用）

| 文档 | 用途 |
|------|------|
| **01_全局复利踩坑日志.md** | 所有踩坑、优质做法、方法论沉淀的核心位置 |
| **06_工作区提示词.md** | 可复用的提示词、用户偏好、执行风格 |

### 🛠️ 流程规范（新项目必看）

| 文档 | 用途 |
|------|------|
| **03_新项目创建SOP.md** | 新项目创建标准化流程 |
| **02_全局项目索引.md** | Workspace 所有项目的总览 |
| **Project_00_全局工作台/templates/** | 各种项目模板 |

---

## ⚡ Claude Code Skills 技能库

所有 Skill 都在 `claude/skills/` 目录下，在 Claude Code 设置中添加该路径即可使用。

| Skill 名称 | 用途 | 使用场景 |
|-----------|------|---------|
| **workspace-project-creator** | 标准化项目目录结构创建 | 新建任何项目时 |
| **research-framework** | 开源项目技术选型、方案调研 | 选择技术栈、调研工具时 |
| **loop-engineering-designer** | 自动化流水线设计 | 设计自动执行任务、CI/CD 时 |
| **project-retrospective** | 项目复盘沉淀模板 | 项目完成后复盘时 |
| **ai-video-generator** | AI 高密度讲解视频生产 | 做技术分享视频时 |

> 💡 技能使用方式：在 Claude Code 中直接说"使用 xxx skill"即可

---

## 🔄 跨设备同步

### 标准同步流程（每周日晚）

```bash
# 两端通用
cd 仓库目录
git pull origin master

# （手动合并本地 Workspace 的新沉淀）

git add .
git commit -m "sync(home/work): 2026-xx-xx 简要说明"
git push origin master
```

### 首次接入（公司电脑）

```bash
# 1. 克隆仓库
git clone https://github.com/COCO454545/codex-review-notes.git D:\codex-sync

# 2. 配置 Claude Code Skill 路径
#    打开 Claude Code 设置 → Skills → Add skill directory
#    选择 D:\codex-sync\claude\skills

# 3. （可选）配置 hooks 软链接到你的 Workspace
```

### 详细文档

同步操作的完整指南、冲突处理流程、日志模板，请查看：
- 📖 [sync/README.md](sync/README.md) - 同步操作指南
- 📝 [sync/sync-log.md](sync/sync-log.md) - 同步历史日志
- 📋 [07_GitHub同步SOP.md](07_GitHub同步SOP.md) - 同步范围和安全规则

---

## 🚪 Hooks 自动化闸门

`.codex/hooks/` 目录下包含 Codex 的自动化拦截脚本，用于：

| Hook | 功能 | 触发时机 |
|------|------|---------|
| **workspace_guard** | 防止文件散落根目录，防止误删重要文件 | 写文件/删除前 |
| **user_prompt_router** | 提醒使用 SOP 和已有 Skills | 提交提示词时 |
| **stop_quality_gate** | 交付前检查：有输出必须有复盘/质检记录 | 完成任务前 |

---

## 📝 沉淀原则

### ✅ 什么应该同步到这个仓库

- 通用方法论、踩坑记录、可复用经验
- 标准化流程、SOP、检查清单
- Skills、Hooks、提示词模板
- 跨项目都能用的工具和配置

### ❌ 什么不应该同步

- 真实项目源代码、数据
- 账号、密钥、Token、隐私信息
- 大文件（视频、音频、压缩包等）
- 公司内部文档、客户数据

---

## ⚙️ Git 常用命令备忘

```bash
# 查看状态
git status
git diff                      # 查看具体修改内容

# 提交更新
git add .
git commit -m "你的提交说明"
git push origin master

# 拉取最新
git pull origin master

# 查看提交历史
git log --oneline -20         # 最近 20 次提交
```

---

## 📋 提交信息规范

```
格式：type(scope): 简要说明

示例：
- feat(skill): 新增项目复盘 Skill
- fix(log): 修复复利日志的路径错误
- sync(home): 2026-06-29 家庭端同步，新增4条经验
- docs: 更新 README 添加同步说明
- refactor: 统一所有文档的路径引用
```

---

## 🎯 最佳实践

### 1. 小步快跑，随时提交
不要攒一周才同步，有新的踩坑、新的经验沉淀，随时提交推送。

### 2. 复利日志只追加不删除
`01_全局复利踩坑日志.md` 只在末尾追加新记录，不删除旧内容。

### 3. 两端各有分工
- **家庭端**：沉淀方法论、通用流程、视频/工具类 Skills
- **公司端**：沉淀业务类踩坑、工作场景最佳实践

### 4. 同步前先 pull
每次提交前先 `git pull`，避免冲突。

---

## 🔗 相关链接

- 🌐 GitHub 仓库：https://github.com/COCO454545/codex-review-notes
- 📖 Claude Code 官方文档：https://code.claude.com/docs

---

## 📊 仓库统计

- 📁 共 50+ 个文件
- 📝 7 个全局核心文档
- ⚡ 6 个 Claude Code Skills
- 🔧 4 个自动化 Hooks 脚本
- 📅 首次同步：2026-06-29

---

## 💡 一句话说明

**两台电脑，一套知识体系，复利每一次踩坑和经验。**

> 同样的错误不犯第二次，同样的方法论用一辈子。
