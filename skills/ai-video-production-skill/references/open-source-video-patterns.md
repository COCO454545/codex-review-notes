# Open Source Video Patterns

Use this when choosing architecture or trying to make a video feel more polished than a basic render.

## Source-Inspired Tool Matrix

| Tool/project pattern | Strong use | Production lesson |
|---|---|---|
| Remotion | React-based programmatic video, reusable components, parameterized templates, frame-accurate renders | Build scenes as components with props; use `Sequence`, `useCurrentFrame`, `spring`, and `interpolate`; keep data separate from layout |
| Motion Canvas | TypeScript generator scenes, vector explainers, real-time preview, voice-over synchronization | Express each animation as a timed generator; use preview loops before final render; good for mechanism explanations |
| Revideo | Library-first programmatic editing, dynamic inputs, browser preview/player, API rendering | Treat video as a template plus input data; useful for repeated Shorts, ads, and user-generated variants |
| Manim | Precise explanatory animations, graphs, formulas, step-by-step mechanisms | Use for visual proofs, math, graphs, and abstract mechanism scenes where precision matters |
| FFmpeg | Assembly, filtergraphs, concat, audio mix, loudness, extraction, final packaging | Keep it as the deterministic finishing layer; validate streams and produce proof frames |
| GSAP | Web animation timelines, staggers, easing, rich UI motion | Use timelines/staggers for polished entrances; animate transforms/opacity instead of layout-heavy properties |

## Architecture Rules

1. **Template before render**: design a reusable composition with input props/data instead of hardcoding every scene.
2. **Voice-first timing**: for narrated videos, script and synthesize/import audio before final timing.
3. **Scene contract**: each scene needs `goal`, `duration`, `visual`, `narration`, `motion`, and `assets`.
4. **Preview gate**: produce stills or a short proof render before full export when style is uncertain.
5. **Data/layout split**: keep facts, copy, screenshots, and timings in JSON/Markdown; keep visual code focused on rendering.
6. **Finishing pass**: assemble, normalize, validate, extract preview frames, and cleanup with deterministic scripts.
7. **HyperFrames scene timing**: make each major scene a `.clip` with `data-start`, `data-duration`, and `data-track-index`; use GSAP for internal motion only. Do not rely on parent scene opacity as the main visibility controller.

## Wow-Factor Recipe

For AI/tech videos, add at least three layers:

- **Narrative layer**: hook, stakes, reveal, takeaway.
- **Information layer**: overview map, metrics, code/UI fragments, diagrams, progress/status.
- **Motion layer**: staggered entrances, camera/zoom moves, trace lines, highlight sweeps, tasteful parallax.
- **Audio layer**: natural voice, aligned captions, light sound hits or music bed when appropriate.
- **Proof layer**: real screenshots, source references, before/after, final output evidence.

Avoid one flat slide per scene. A polished scene usually has one dominant idea, one supporting proof, and one motion beat.

## Selection Guide

- Choose HyperFrames/GSAP when the video is a dense tech UI explainer with HTML/CSS motion.
- Choose Remotion when the project benefits from React components, data-driven variations, and frame-accurate rendering.
- Choose Motion Canvas/Revideo patterns when vector explanation, generator timing, editor-like preview, or API-rendered templates are central.
- Choose Manim when the idea is mathematical, graph-based, proof-like, or needs geometric precision.
- Choose FFmpeg alone only for finishing, assembly, trims, audio, metadata, or simple edits.

## Reusable Scene Patterns

### Overview Map

- First screen lists the whole structure.
- Highlight one section at a time as narration progresses.
- Keep completed sections visible as dimmed context.

### Data Reveal

- Show total landscape first.
- Bring in top item with larger scale and proof.
- Use staggered cards for second/third items.
- End with pattern insight, not just a list.

### Workflow Trace

- Show input on the left, process in the middle, output on the right.
- Animate packets, lines, or status markers through the system.
- Add one failure/pitfall branch when teaching a method.

### Code/UI Transformation

- Start with messy or old state.
- Highlight the changed lines or UI regions.
- Morph to the improved state.
- End with a user-visible result.

## Anti-Patterns

- Building visuals directly in Python/PIL when a web animation or video framework would be more expressive.
- Rendering a full video before checking preview frames.
- Trusting ffprobe success when preview frames have not been checked; a technically valid MP4 can still be visually blank.
- Treating a video link as inspiration without writing `reference-learning.md`.
- Shipping a final MP4 without audio checks when narration was requested.
- Copying another creator's exact layout, script, or pacing without transformation.

## Source Links

- Remotion docs: https://www.remotion.dev/docs/api
- Remotion dataset rendering: https://www.remotion.dev/docs/dataset-render
- Remotion timing: https://www.remotion.dev/docs/use-current-frame
- Motion Canvas GitHub: https://github.com/motion-canvas/motion-canvas
- Motion Canvas quickstart mirror: https://motion-canvas-docs.vercel.app/docs/quickstart
- Revideo docs: https://docs.re.video/
- Manim docs: https://docs.manim.community/en/stable/
- Manim quickstart: https://docs.manim.community/en/stable/tutorials/quickstart.html
