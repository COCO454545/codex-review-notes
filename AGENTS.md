# AGENTS.md

本文件用于约定 AI 编程助手在 `D:\Workspace` 中的工作方式。任何进入本 Workspace 的 AI 助手，都必须先理解：

> **`D:\Workspace` 是唯一沉淀真源。**
> 
> 长期成果只保留在：
> 1. Workspace 根目录的全局 md
> 2. `D:\Workspace\skills\`

普通 `Project_*` 目录属于项目层，不属于全局沉淀层。

## 0. 最高规则

无论任务大小，执行前先判断它属于：

- **项目层**：具体工具、应用、视频、调研、业务交付物
- **沉淀层**：全局规则、偏好、复盘方法、同步规范、skills

### 如果是项目层
先查看并遵守：
1. `00_全局控制台.md`
2. `02_全局项目索引.md`
3. `03_新项目创建SOP.md`
4. `AGENTS.md`

必要时再读：
- `01_全局复利踩坑日志.md`
- `06_工作区提示词.md`

### 如果是沉淀层
直接在 `D:\Workspace` 根目录 md 或 `D:\Workspace\skills\` 下工作，不创建普通 `Project_*` 文件夹。

## 1. Workspace 规则

1. Treat `D:\Workspace` as the default working root.
2. Every new project must live in a folder named `Project_编号_项目名称`.
3. Use two-digit project numbers, such as `Project_01_项目名称`.
4. `Project_00_全局工作台` is reserved for shared templates and stable cross-project assets, not ordinary business work.
5. Project-related files must not be placed directly in the Workspace root.
6. Root-level files are reserved for global Markdown documents and the `skills/` directory.
7. All project assets, code, references, outputs, logs, tests, and reviews must stay inside the matching project folder.
8. If a task will produce project files, create or enter the correct project folder first.
9. Simple one-off questions, translations, and commands do not require a project folder.
10. When a project is created, paused, completed, or archived, update `02_全局项目索引.md`.
11. If a mistake, repeated pitfall, or reusable method appears, record it in `01_全局复利踩坑日志.md` or the project logs.
12. Workspace-level retrospectives, behavior tuning, user preference capture, global SOP updates, GitHub sync rules, and skill restructuring are not projects. Do not create `Project_*` folders for them.
13. `D:\Workspace\skills\` is the only local source of truth for custom skills.
14. One skill = one folder = one `SKILL.md` entry file.
15. Do not invent parallel skill directories such as `claude/skills/` in the local Workspace unless the user explicitly asks for that structure.

## 2. 沟通规则

1. 与用户沟通时默认使用中文。
2. 代码、命令、变量名、错误信息、日志和 stack traces 保留英文原文。
3. 说明问题时要直接、清晰，不绕。
4. 遇到不确定事项时先说明假设。
5. **遇到结构归属、命名体系、同步边界这类不确定问题时，必须先问用户，不得擅自决定。**

## 3. 代码与文件修改原则

1. Focus on the current task.
2. Prefer the smallest useful change with a clear verification path.
3. Do not add unrelated features, abstractions, configuration, or complexity.
4. Do not modify unrelated files, clean unrelated content, or move user files without a clear request.
5. Every changed line should trace back to the user request.
6. Reuse existing tools, scripts, project conventions, and skills when available.
7. Aim for maintainability. Do not add structure just to make the solution look bigger.
8. 这类“沉淀合并”任务，合并的是**最终成果**，不是机械拼接两个旧文件。
9. 最终输出必须像长期维护的正式成果，而不是保留中间拼接痕迹。

## 4. 安全要求

1. 不得将密码、API keys、tokens 或 secrets 写入代码、文档或日志。
2. 不得提交 `.env` 等本地配置文件，除非明确、安全且必要。
3. 不得在日志中输出敏感信息。
4. 不要把不可信用户输入拼接进高风险 shell 命令。
5. 不要绕过权限、登录、付费墙、安全提示或 CAPTCHA。
6. 删除文件、批量移动、上传数据、操作真实账号、生产环境或第三方平台前，必须获得用户明确确认。
7. 如果操作不可逆，先说明风险、范围和影响。

## 5. 验证流程

1. 修复问题后必须验证，不能只口头说“已修复”。
2. 能复现 bug 时，优先先复现再修复。
3. 能跑测试、lint、格式检查时都应执行。
4. 如果命令失败，要如实反馈结果，而不是跳过。
5. 如果无法验证，要说明原因、已检查内容和剩余风险。
6. 合并、交付或采纳自动化结果前，必须查看关键 diff 或产出内容。

## 6. 参考与预览闸门

1. For visual UI, websites, apps, videos, marketing, or style-sensitive work, do not jump straight to the final implementation.
2. First inspect user-provided references, local project materials, and relevant first-hand sources such as GitHub repos, official docs, demos, examples, issues, and releases.
3. Produce a low-cost preview before expensive work:
   - UI/app/site/system interaction: 2-4 overview preview boards or style directions when visual direction is uncertain.
   - Video: 2-4 preview cards or opening/style frame directions, plus a 10-15 second voice or pacing proof before full render.
4. Ask the user to choose or approve the direction when the output depends on taste, style, voice, or pacing.
5. If the preview direction is rejected, change approach before full implementation instead of pushing forward.

## 7. 能力发现闸门

1. Before designing a non-trivial workflow, first check whether the Workspace already has a suitable capability:
   - `D:\Workspace\skills\`
   - existing scripts
   - templates
   - `.codex/hooks`
2. If the task may benefit from mature external practice, inspect first-hand sources before inventing a solution: official docs, GitHub repositories, examples, demos, issues, releases.
3. If a broadly useful pattern is found, evolve it into the user's own reusable workflow: update a Workspace skill, create a personal skill, or record the rule in the root global Markdown files.
4. Do not copy blindly; extract patterns that fit the user's workflow.

## 8. 项目不变量

Before modifying an existing project, identify the invariants that must not break:
- data counts
- public links
- auth/share code behavior
- filenames
- source-of-truth scripts
- deployment target
- user-specified “其他不变” boundaries

当用户说“其他不变”时，只改指定范围，并明确说明验证范围。

## 9. 执行风险分级

1. Safe, low-risk, reversible tasks should be executed directly without repeated confirmation.
2. If a task is moderately uncertain but reversible, state the assumption briefly and proceed with the smallest useful action.
3. Before deleting files, batch moving data, changing production behavior, uploading data, using real accounts, or operating third-party platforms, get explicit user confirmation.
4. Before irreversible work, explain the risk, scope, and likely impact before continuing.
5. 结构不明确时，宁可先问一句，也不要自作聪明改出第二套体系。

## 10. Claude Code 与 Codex 协作

1. Claude/Codex 协作应围绕同一套 Workspace 真源进行，不应各自维护不同目录体系。
2. 自动化流程必须有 stop conditions、validation commands 和人工验收。
3. 未经 review 的自动化结果不得直接合并、发布或覆盖重要文件。
4. Skills、SOP、规则、复利日志这类长期资产优先沉淀到 Workspace 真源，再同步到远程。

## 11. Skills 规则

`D:\Workspace\skills\` 下的所有技能必须遵守：

```text
D:\Workspace\skills\
└── skill-name\
    └── SKILL.md
```

可选扩展：
```text
skill-name\
├── SKILL.md
├── references\
├── assets\
├── scripts\
└── agents\
```

禁止：
- `skills\xxx.md` 这种平铺式 skill
- 在某个 `Project_*` 目录里把 skill 副本当正式 skill 真源
- 本地真源之外再擅自发明第二套 skills 目录

## 12. 工作习惯

For each task:
1. 先判断项目层还是沉淀层。
2. 进入正确位置工作。
3. 明确目标、假设、输出位置和验证方式。
4. 项目层任务读简报和最近日志。
5. 沉淀层任务直接更新根目录 md 或 `skills/`。
6. 验证结果后再汇报完成。
7. 可复用经验沉淀到全局复利日志或 skill。
8. 每次结构性选择如果不明确，先问用户。