# Workspace Agent Rules

Codex must follow these rules when working in `D:\Workspace`.

## 0. Read First

Before project work, read:

1. `00_全局控制台.md`
2. `02_全局项目索引.md`
3. `03_新项目创建SOP.md`
4. `AGENTS.md`

Also read:

- `01_全局复利踩坑日志.md` when prior mistakes, reusable methods, review, or repeated issues may apply.
- `06_工作区提示词.md` when user preferences, communication style, prompt templates, or long-term workflows may apply.

## 1. Workspace Rules

1. Treat `D:\Workspace` as the default working root.
2. Every new project must live in a folder named `Project_编号_项目名称`.
3. Use two-digit project numbers, such as `Project_01_项目名称`.
4. `Project_00_全局工作台` is reserved for global templates and shared materials.
5. Project-related files must not be placed directly in the Workspace root.
6. Root-level files are reserved for global control documents, `AGENTS.md`, and project folders.
7. All project assets, code, references, outputs, logs, tests, and reviews must stay inside the matching project folder.
8. If a task does not belong to an existing project and will produce project files, create the project folder first.
9. Simple one-off questions, translations, and commands do not require a project folder.
10. When a project is created, paused, completed, or archived, update `02_全局项目索引.md`.
11. If a mistake, repeated pitfall, or reusable method appears, record it in `01_全局复利踩坑日志.md` or the project logs.
12. Workspace-level retrospectives, Codex behavior tuning, user preference capture, global SOP updates, and GitHub sync rules are not projects. Do not create `Project_*` folders for them; update the root global Markdown files directly.

## 2. Communication Rules

1. Use Chinese by default when communicating with the user.
2. Keep code, commands, variable names, errors, logs, and stack traces in their original English when useful.
3. Explain issues clearly and directly.
4. State assumptions when something is uncertain.
5. Ask the user only when a safe assumption cannot be made.

## 3. Code And File Change Principles

1. Focus on the current task.
2. Prefer the smallest useful change with a clear verification path.
3. Do not add unrelated features, abstractions, configuration, or complexity.
4. Do not modify unrelated files, clean unrelated content, or move user files without a clear request.
5. Every changed line should trace back to the user request.
6. Reuse existing tools, scripts, project conventions, and skills when available.
7. Aim for maintainability. Do not add code, modules, or process just to make the solution look larger.
8. Explain changed files, impact scope, and verification after completing work.

## 4. Safety Requirements

1. Do not write passwords, API keys, tokens, or secrets into code, docs, or logs.
2. Do not commit local config files such as `.env` unless explicitly requested and safe.
3. Do not log private or sensitive information.
4. Do not concatenate untrusted user input into high-risk shell commands.
5. Do not bypass permissions, logins, paywalls, security prompts, or CAPTCHA.
6. Get explicit user confirmation before destructive or high-risk actions:
   - deleting files, batch deleting files, or deleting databases;
   - moving files outside the Workspace;
   - uploading data or sending production requests;
   - operating real accounts, production environments, or third-party platform accounts;
   - automatically publishing, merging, or committing irreversible results.
7. If an operation is irreversible, explain risk and scope before continuing.

## 5. Verification Flow

1. Verify fixes when verification is possible.
2. Reproduce bugs before fixing when feasible.
3. Run tests, lint, formatting, or visual checks when relevant and available.
4. If a command fails, report the actual result and continue with the next sensible diagnostic.
5. If verification is impossible, explain why, what was checked, and remaining risk.
6. Before accepting automation output, review the key diff or generated result.

## 5.1 Reference And Preview Gates

1. For visual UI, website, app, video, marketing, or style-sensitive work, do not jump straight to the final implementation.
2. First inspect user-provided references, local project materials, and relevant first-hand sources such as GitHub repos, official docs, demos, examples, issues, and releases.
3. Produce a low-cost preview before expensive work:
   - UI/app/site/system interaction: 2-4 overview preview boards or style directions when visual direction is uncertain.
   - Video: 2-4 preview cards or opening/style frame directions, plus a 10-15 second voice or pacing proof before full render.
4. Ask the user to choose or approve the direction when the output depends on taste, style, voice, or video pacing.
5. If the preview direction is rejected, change approach before full implementation instead of pushing forward.
6. Single standalone image generation is exempt unless the user asks for a style board or multiple directions.
7. Record reusable reference analysis in the active project's `reference-learning.md` or, for workspace-level learning, in the root global Markdown files.

## 5.2 Capability Discovery Gate

1. Before designing a non-trivial workflow, first check whether Codex already has a suitable capability: available skills, plugins, apps/connectors, MCP tools, workspace hooks, existing scripts, and local skill folders such as `D:\ai_tool\skills`.
2. If the task may benefit from mature external practice, inspect first-hand sources before inventing a solution: official docs, GitHub repositories, examples, demos, issues, releases, and widely used open-source skills or templates.
3. When searching GitHub for skills or project patterns, prefer projects with clear adoption signals, recent maintenance, usable examples, and a license that allows reuse. Do not copy blindly; extract patterns that fit the user's workflow.
4. If a broadly useful pattern is found, evolve it into the user's own reusable workflow: update the relevant project skill, create a personal skill when appropriate, or record the reusable rule in the root global Markdown files.
5. In the final answer, briefly state which built-in capability, plugin, skill, script, or external reference was used. If none was suitable, state why a custom path was chosen.
6. Simple one-off questions and tiny commands can skip this gate.

## 5.3 Project Invariants

1. Before modifying an existing project, identify the invariants that must not break: data counts, public links, auth/share code behavior, filenames, source-of-truth scripts, deployment target, and user-specified "other unchanged" boundaries.
2. For the artificial intelligence trainer project pattern, always preserve question counts, explanation uniqueness, share-code/password flow, mobile-first behavior, and source-script rebuild path unless explicitly asked otherwise.
3. When the user says "其他不变", only change the requested area and state the verification scope.

## 5.4 Execution Risk Levels

1. Safe, low-risk, reversible tasks should be executed directly without repeated confirmation.
2. If a task is moderately uncertain but reversible, state the assumption briefly and proceed with the smallest useful action.
3. Before deleting files, batch moving data, changing production behavior, uploading data, using real accounts, or operating third-party platforms, get explicit user confirmation.
4. Before irreversible work, explain the risk, scope, and likely impact before continuing.
5. If a command, test, or check fails, report the concrete result and continue with the next sensible diagnostic.

## 6. Claude Code And Codex Collaboration

1. Prefer Git Worktree for execution isolation when multiple agents or tools collaborate.
2. Codex should stay inside the current project folder or specified worktree.
3. Claude Code, Codex, or another reviewer should evaluate diff, tests, and user goals.
4. Automation workflows must have stop conditions, validation commands, and human acceptance.
5. Do not merge, publish, or overwrite important files with unreviewed automation output.

## 7. Standard Project Structure

```text
Project_编号_项目名称
├─ 00_project_brief.md
├─ 01_requirements
├─ 02_references
├─ 03_assets
├─ 04_src
├─ 05_outputs
├─ 06_tests
├─ 07_logs
├─ 08_review
└─ 99_temp
```

## 8. Working Habit

For each project task:

1. Identify the project.
2. Create the project folder if needed.
3. State goal, assumptions, output location, and verification method when useful.
4. Read the project brief and recent logs.
5. Put every file in the correct project subdirectory.
6. Verify outputs before calling the task complete.
7. Update the project index when status changes.
8. Update logs when the work produces reusable learning.
