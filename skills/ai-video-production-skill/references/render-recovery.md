# Render Recovery

Use this before rendering any long/high-resolution video and after any timeout, interruption, or failure.

## Trigger

Follow this when:

- Duration is over 30 seconds.
- Resolution is `1080x1920`, `1920x1080`, or higher.
- Render may take over 5 minutes.
- A render timed out, was interrupted, or partially failed.
- The renderer produced `work-*`, `tmp`, `frames`, `chunks`, `snapshots`, `recovered_frames`, or partial MP4 files.

## Before Rendering

1. Estimate frames: `duration_seconds * fps`.
2. Prefer segmented rendering for 30-90s videos.
3. Run a short proof render or still-frame set when the style or render cost is uncertain.
4. Name outputs clearly:
   - `name_part01.mp4`
   - `name_part02.mp4`
   - `name_final.mp4`

## After Failure

Do not immediately rerun from zero.

1. Check whether rendering processes are still active.
2. Inspect output directories for MP4s, frames, audio, logs, and work folders.
3. Count frames and compare to expected total.
4. Use `ffprobe` on partial MP4s.
5. Reuse valid clips/frames/audio.
6. Render only missing or failed segments.
7. Restart from zero only if no usable artifacts exist, artifacts are corrupt, source changed incompatibly, or user asks for a clean rerender.

## FFmpeg Patterns

Concat valid segments:

```bash
ffmpeg -y -f concat -safe 0 -i parts.txt -c copy joined.mp4
```

Add narration:

```bash
ffmpeg -y -i joined.mp4 -i narration.mp3 -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest final.mp4
```

Assemble frames:

```bash
ffmpeg -y -framerate 30 -i frames/frame_%06d.png -i narration.mp3 -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest final.mp4
```

## Cleanup

Delete temporary work only after the final MP4 is verified. Keep partial work while it can still save time.

## Windows Notes

- If `ffmpeg`/`ffprobe` are missing from PATH, install or use project-local binaries, prepend their folders to PATH for the render/check command, then clean `node_modules` after final verification when reproducibility files remain.
- Python wrappers around `ffmpeg`/`ffprobe` should decode subprocess output with `encoding="utf-8", errors="replace"` to avoid Windows GBK crashes on Unicode paths or metadata.
