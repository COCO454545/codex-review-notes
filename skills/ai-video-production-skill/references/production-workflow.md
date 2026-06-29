# Production Workflow

## Startup

1. Identify deliverable: platform, aspect ratio, duration, language, voice, final path.
2. Check whether this is a fresh build, revision, or recovery from existing artifacts.
3. Gather references before designing: screenshots, GitHub examples, previous outputs, brand assets, voice samples.
4. If a project already has `video-spec.md`, `*分镜*.md`, `*storyboard*.md`, or `DESIGN.md`, treat the work as iteration.
5. If this is a new production, run `scripts/init_video_project.py` and copy `assets/templates/video-spec-template.md` into the project.

## `video-spec.md`

Use this compact shape:

```markdown
# video-spec

## 1. Goal
- Purpose:
- Audience:
- Platform:
- Aspect ratio:
- Target duration:
- Core sentence:

## 2. Source Material
- Documents:
- Screenshots/images:
- Audio/voice:
- Data:
- Missing assets:

## 3. Visual Direction
- Theme:
- Palette:
- Typography:
- Density:
- Components:
- Do not use:

## 4. Narration
- Voice:
- Speed:
- Tone:
- Subtitle style:

## 5. Storyboard
| # | Time | Scene goal | On-screen visuals | Narration | Motion/transition | Assets |
|---|------|------------|-------------------|-----------|-------------------|--------|

## 6. Render Requirements
- Final format: MP4
- Resolution:
- FPS:
- Audio:
- Quality checks:
```

## Story Patterns

### Dense Tech Explainer

1. Hook or first-screen overview map.
2. Definition or old-vs-new comparison.
3. Mechanism breakdown.
4. Concrete demo or process animation.
5. Value shift or impact.
6. Risks and pitfalls.
7. Evolution or closing sentence.

### GitHub / Ranking / Data Video

1. Source and total landscape.
2. Top item deep dive.
3. Second and third item contrast.
4. Fast sweep through the rest.
5. Pattern insight.
6. Practical takeaway.

### Pitfall / Retrospective Video

1. Hook: the visible mistake or wasted cost.
2. Context: what the creator tried to do.
3. Failure chain: where the process drifted.
4. Correct workflow: the repeatable fix.
5. Before/after contrast.
6. Checklist or reusable rule.

### Product / Tool Demo

1. Promise: the result users care about.
2. Input: raw material or starting state.
3. Workflow: 3-5 clear steps.
4. Proof: generated output, metric, or visual comparison.
5. Best use case and limitation.
6. Call to action or next experiment.

## Tool Routing

- HyperFrames: HTML/CSS/GSAP motion systems, caption-heavy videos, UI explainers, preview/lint/render loops.
- Remotion: React scene systems, frame-accurate reusable components, data-driven animation, brand openings.
- HeyGen: presenter, avatar, lip-sync, translation, or video-agent workflows.
- Canva: visual ideation or template-based assets.
- FFmpeg: assembly, speed, trim, audio mix, preview extraction, final validation.

## Final Delivery

1. Export one final MP4.
2. Include final preview frames when useful.
3. Run `scripts/check_quality.py`.
4. Run `scripts/extract_preview_frames.py`.
5. Check at least opening, middle, ending, and segment boundaries.
6. Save a short review note from `assets/templates/retrospective-template.md`.
7. Delete stale render artifacts after final verification.
