---
name: ai-video-production-skill
description: End-to-end AI video production pipeline for this user. Use when Codex is asked to create, refine, recover, review, analyze, learn from, or clean AI/tech short videos; when the user shares Douyin/TikTok/Bilibili/YouTube/video links as references; or when work involves HyperFrames, Remotion, HeyGen, storyboard, video-spec, narration, voiceover, subtitles, style extraction, preview frames, final MP4, ffprobe validation, artifact cleanup, or evolving repeated video work into reusable production methods. Triggers include 生成视频, 制作视频, 视频复盘, 学习这个视频, 抖音链接, 视频链接, 口播, 配音, 分镜, video-spec, HyperFrames, Remotion, final MP4, preview frames, and deleting rejected render artifacts.
---

# AI Video Production Skill

Use this as the single video-production skill for this user. It merges the former `ai-video-production-skill` and `personal-video-director-skill`.

The goal is not "it rendered". The goal is a clean production pipeline: learn from references, initialize the project, lock the spec, produce previews, render a verified MP4, clean junk, and distill reusable lessons.

## Read Only What Is Needed

- Read `references/production-workflow.md` for a new video, video-spec, tool choice, storyboard, or final delivery.
- Read `references/link-learning.md` when the user shares a Douyin/TikTok/Bilibili/YouTube/video link or asks to learn from another creator's video.
- Read `references/open-source-video-patterns.md` when choosing production architecture, animation language, or reusable scene systems.
- Read `references/self-evolution.md` after a delivery, failure, user critique, or reference-study session that may improve the skill.
- Read `references/style-and-narration.md` when taste, density, visual style, preview approval, voice, pacing, or captions matter.
- Read `references/platform-delivery.md` when platform, ratio, caption, cover, export, or publish package requirements matter.
- Read `references/render-recovery.md` before any long/high-resolution render or after a timeout/interruption/failure.
- Copy `assets/templates/video-spec-template.md` into the project before production when no current spec exists.
- Copy `assets/templates/retrospective-template.md` into review notes after delivery or after a failed/recovered run.
- Copy `assets/templates/skill-evolution-proposal-template.md` before changing this skill from a project lesson.
- Use `scripts/init_video_project.py` to create a clean video project folder structure.
- Use `scripts/check_quality.py` after producing an MP4.
- Use `scripts/extract_preview_frames.py` to create proof frames for review.
- Use `scripts/cleanup_video_artifacts.py` to plan or execute cleanup after final verification.
- Use `scripts/propose_skill_evolution.py` to turn project retrospectives into a bounded skill-improvement proposal.
- Use `assets/voice-style-reference.mp3` only as a voice style reference, not as finished narration.
- Use `assets/style-preview-overview.png` only as a compact style/density reminder.

## Core Workflow

1. **Inventory first**
   - If this is a resumed or messy project, inspect existing specs, source files, audio, preview frames, renders, logs, and work directories before regenerating.
   - Reuse good artifacts. Regenerate only missing, failed, stale, corrupted, rejected, or style-incompatible items.

2. **Learn from references before inventing**
   - If the user shares a video link, screenshots, downloaded clips, transcripts, or creator references, extract reusable strengths first: hook, structure, rhythm, visual density, camera/composition, captions, sound, voice, materials, and editing pattern.
   - Store reference notes in the project, not in the Workspace root.
   - Do not copy another creator pixel-for-pixel. Translate strong patterns into the user's own reusable style.
   - For GitHub/project ranking videos, do not stop at stars, ranking pages, or GitHub API metadata. Inspect each repo's README, demo media, examples, docs, releases, issues/discussions when available, and positioning language before writing the script.

3. **Initialize and lock the plan before expensive renders**
   - For a new production, create a project with `scripts/init_video_project.py`.
   - Create or update `video-spec.md` for vague or multi-scene work.
   - Create or update `DESIGN.md` when visual direction is not already locked.
   - Generate 2-3 preview frames before full video when style is uncertain.
   - Before any full render over 20 seconds, produce a low-cost proof: opening 10-15 seconds, 2-3 visual frames, and the proposed voice sample. Do not full-render until the opening, voice direction, and visual style are acceptable.

4. **Choose the right production path**
   - Default to HyperFrames first for HTML/CSS/GSAP, dense UI explainers, captions, and fast preview/render loops.
   - Use Remotion first for React components, frame-accurate animation, reusable scene systems, or complex programmatic composition.
   - Use Motion Canvas/Revideo patterns for explainer-style vector animation, editor-like preview loops, and TypeScript scene generators.
   - Use Manim patterns for precise mathematical, graph, proof, or mechanism visualizations.
   - Use HeyGen when presenter/avatar/lip-sync is central.
   - Use FFmpeg for assembly, audio mixing, speed changes, preview extraction, metadata checks, and final packaging.
   - Do not use Python/PIL as the final visual design layer unless the user explicitly accepts it.

5. **Make narration real**
   - If the user asks for 口播, 配音, narration, dubbing, or supplies a voice sample, final delivery needs a complete narration track unless explicitly canceled.
   - A short sample is style reference only.
   - Write scene-split narration, generate/import the full audio, probe real durations, then retime visuals to match.
   - Do not ship robotic system TTS, Windows SAPI voices, or stiff placeholder narration as final voiceover. Having an audio stream is not enough.
   - Default to a natural male Chinese creator voice when the user asks for male口播 or when no better voice preference is known. If only low-quality local TTS is available, stop at a labeled voice proof or silent visual draft rather than pretending it is final.

6. **Render and verify**
   - Prefer `1080x1920`, 30fps, H.264 + AAC for vertical short video unless specified otherwise.
   - For videos over 30s or high resolution, use segmented/recoverable rendering.
   - Run `scripts/check_quality.py <final.mp4> --resolution 1080x1920`.
   - Run `scripts/extract_preview_frames.py <final.mp4> <preview_dir>`.
   - Check representative frames: opening, middle, ending, and segment boundaries.
   - Check voice naturalness, gender/style fit, pacing, and emotional contour. Mark the video failed if the voice sounds fake even when ffprobe passes.

7. **Clean storage**
   - Keep final MP4, a few final preview frames, current source, specs, scripts, and small reusable references.
   - Delete rejected drafts, duplicate old MP4s, bulk frame folders, work directories, stale scene clips, old audio fragments, `node_modules`, `.git` clones, caches, and recovered frames after they are no longer needed.
   - Run cleanup in dry-run mode first unless the user has already explicitly asked to delete junk.
   - Before deleting, verify the target is inside the project/export directory or the known video workspace.

8. **Evolve the skill**
   - After a strong final result or a painful failure, fill the retrospective template.
   - Classify the lesson as a skill defect, execution lapse, or one-off project fact before editing the skill.
   - Promote only reusable, non-obvious lessons that would change future behavior into this skill or the global pitfall log.
   - Prefer bounded edits: add one rule, replace one weak rule, or add one small script/template/reference at a time.
   - Validate the skill after every structural edit.
   - Keep the skill lean: add small templates, scripts, reference notes, or tiny style previews; avoid storing large generated videos.

## Default Project Shape

Prefer this inside the active Workspace project:

```text
video_project/
├─ video-spec.md
├─ DESIGN.md
├─ reference-learning.md
├─ package.json
├─ src/ or composition.html
├─ scripts/
├─ assets/
├─ previews/
├─ exports/
├─ logs/
└─ review/
```

Map old folders this way:

- `01_需求与目标` -> spec/source requirements
- `02_素材与资料` -> assets/references
- `03_过程文件` -> source/scripts/logs
- `04_交付成果` -> exports
- `05_复盘与日志` -> logs/review

## Acceptance Checklist

Before calling a video task done:

- Final output is a verified MP4.
- Resolution, duration, fps, codec, video stream, audio stream, and file size are checked.
- Preview frames are readable, not blurred transition captures.
- Text is readable at phone size.
- The first screen has a clear hook or overview map for dense explainers.
- Visual density matches the user's taste: rich technical UI, not sparse slides.
- Narration exists when requested and is scene-timed.
- Platform package is complete when requested: cover frame, captions/subtitles, title ideas, and publish notes.
- Temporary/rejected artifacts are deleted.
- Reusable lessons are added back to this skill or the project review notes.
