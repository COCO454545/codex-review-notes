#!/usr/bin/env python3
"""Extract representative preview frames from a video with ffmpeg."""

import argparse
import json
import subprocess
from pathlib import Path


def duration_seconds(video: Path) -> float:
    cmd = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        str(video),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True)
    except FileNotFoundError:
        raise SystemExit("ERROR: ffprobe not found. Install ffmpeg first.")
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"ERROR: ffprobe failed: {exc.stderr}")
    data = json.loads(result.stdout)
    return float(data.get("format", {}).get("duration", 0) or 0)


def extract_frame(video: Path, output: Path, at_seconds: float) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-ss",
        f"{at_seconds:.3f}",
        "-i",
        str(video),
        "-frames:v",
        "1",
        "-q:v",
        "2",
        str(output),
    ]
    try:
        subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True)
    except FileNotFoundError:
        raise SystemExit("ERROR: ffmpeg not found. Install ffmpeg first.")
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"ERROR: ffmpeg failed: {exc.stderr}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract representative preview frames from a video.")
    parser.add_argument("input", help="Input MP4 path")
    parser.add_argument("output_dir", help="Directory for PNG preview frames")
    parser.add_argument("--count", type=int, default=5, help="Number of frames to extract, default 5")
    args = parser.parse_args()

    video = Path(args.input).resolve()
    output_dir = Path(args.output_dir).resolve()
    if not video.exists():
        raise SystemExit(f"ERROR: input does not exist: {video}")
    total = duration_seconds(video)
    if total <= 0:
        raise SystemExit("ERROR: duration is zero or unreadable")

    count = max(1, args.count)
    if count == 1:
        points = [min(total * 0.5, max(total - 0.1, 0))]
    else:
        points = [max(0.1, total * i / (count - 1)) for i in range(count)]
        points[-1] = max(0.1, total - 0.2)

    for idx, point in enumerate(points, 1):
        extract_frame(video, output_dir / f"preview_{idx:02d}_{point:.1f}s.png", point)
    print(f"Extracted {len(points)} preview frames to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
