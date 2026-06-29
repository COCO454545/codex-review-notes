# Workspace Hooks

These hooks protect `D:\Workspace` from the two most common failure modes:

1. Project files being written into the wrong place.
2. Video work being marked complete before proof, render, and quality evidence exist.
3. Codex inventing a workflow before checking available skills, plugins, scripts, and first-hand references.

## Installed Hooks

- `UserPromptSubmit`: reminds Codex to apply the workspace SOP, capability discovery gate, and video SOP when the prompt mentions project creation, skills, plugins, GitHub, scripts, automation, videos, narration, or skill capture.
- `PreToolUse`: blocks obvious workspace-root pollution, deletion outside the approved roots, and expensive full video renders before the proof gate.
- `Stop`: checks the active project folder before Codex ends a turn. If output files exist without quality/review evidence, it blocks completion.

## Trust Step

Codex requires non-managed hooks to be reviewed and trusted before they run. In CLI, use `/hooks` to review and trust the project hooks after restarting or opening a new session in this workspace.

## Intended Scope

These hooks are project-level hooks in `D:\Workspace\.codex`, not user-global hooks. They should affect this workspace without changing behavior in unrelated folders.
