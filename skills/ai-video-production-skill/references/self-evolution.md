# Self Evolution

Use this after a delivery, failed attempt, user critique, reference-study session, or repeated workflow pain.

This is a lightweight adaptation of SkillOpt-style evolution: learn from real runs, propose bounded edits, gate changes, and keep the skill compact.

Local reference used for this adaptation: `D:\ai_tool\skills\SkillOpt-main`.

## Loop

1. **Harvest**: collect the project brief, video-spec, reference-learning notes, preview frames, final validation output, user feedback, cleanup notes, and retrospective.
2. **Score**: rate the run on hard checks and soft quality:
   - Hard: final MP4 exists, correct resolution, audio present when required, preview frames extracted, cleanup done.
   - Soft: hook strength, visual density, phone readability, narration naturalness, reference alignment, platform readiness.
   - Cost: token/额度 spent before the first user-visible proof, render time spent before voice/style approval, and duplicated work that could have been avoided.
3. **Reflect**: compare good and bad evidence. Find the smallest reusable lesson.
4. **Classify**:
   - `SKILL_DEFECT`: the skill was missing, wrong, or too vague. Edit the skill.
   - `EXECUTION_LAPSE`: the skill already had the right rule but Codex ignored it. Add a short reminder to the retrospective or global pitfall log; avoid bloating the skill body.
   - `PROJECT_FACT`: useful only for one project. Keep it in the project folder.
5. **Propose**: use `scripts/propose_skill_evolution.py` or `assets/templates/skill-evolution-proposal-template.md`.
6. **Gate**: accept only if the edit would have prevented the failure or repeated the success in at least two plausible future video tasks.
7. **Patch**: make a bounded edit, then run skill validation.

## Promotion Rules

Promote into this skill only when a lesson is:

- Reusable across future videos.
- Concrete enough to change execution.
- Not already covered by the skill.
- Small enough to keep the skill fast to load.
- Supported by an artifact: user feedback, preview frame, ffprobe output, final MP4 issue, or reference analysis.

Do not promote:

- One-off topic facts.
- Large generated videos.
- Unverified taste guesses.
- Temporary file paths.
- Generic advice that Codex already knows.

## Gate Checklist

Before editing the skill, answer:

- What failed or worked?
- Which exact future behavior should change?
- Is this a missing rule, weak rule, missing script/template, or execution lapse?
- What is the smallest edit?
- What file should receive the edit: `SKILL.md`, a reference, a script, a template, or project notes?
- How will the edit be validated?

## Slow Update

Every few video projects, compare multiple retrospectives:

- Repeated failures become stronger guardrails.
- Repeated successes become reusable production patterns.
- Rare one-offs stay in project review notes.
- Conflicting lessons become decision rules instead of absolute rules.
