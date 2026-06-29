#!/usr/bin/env python3
"""Check final MP4 quality with ffprobe and optional ffmpeg audio analysis."""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run_ffprobe(filepath: Path) -> dict:
    cmd = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(filepath),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True)
    except FileNotFoundError:
        raise SystemExit("ERROR: ffprobe not found. Install ffmpeg first.")
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"ERROR: ffprobe failed: {exc.stderr}")

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: ffprobe returned invalid JSON: {exc}")


def run_audio_loudness(filepath: Path) -> dict:
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-nostats",
        "-i",
        str(filepath),
        "-filter:a",
        "volumedetect",
        "-f",
        "null",
        "-",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    except FileNotFoundError:
        return {"error": "ffmpeg not found"}

    output = result.stderr or ""
    parsed = {"mean_volume_db": None, "max_volume_db": None, "raw": output[-2000:]}
    for line in output.splitlines():
        line = line.strip()
        if "mean_volume:" in line:
            parsed["mean_volume_db"] = line.split("mean_volume:", 1)[1].strip()
        elif "max_volume:" in line:
            parsed["max_volume_db"] = line.split("max_volume:", 1)[1].strip()
    return parsed


def parse_fps(rate: str) -> float:
    if "/" in rate:
        num, den = rate.split("/", 1)
        return float(num) / float(den) if float(den) else 0.0
    return float(rate or 0)


def check_quality(
    filepath: Path,
    expected_resolution: str | None = None,
    require_audio: bool = True,
    expected_video_codec: str | None = "h264",
    expected_audio_codec: str | None = "aac",
    analyze_audio: bool = False,
) -> dict:
    findings = {
        "file": str(filepath),
        "file_exists": filepath.exists(),
        "video_stream": False,
        "audio_stream": False,
        "resolution": None,
        "fps": None,
        "video_codec": None,
        "audio_codec": None,
        "pixel_format": None,
        "bitrate_kbps": None,
        "duration": None,
        "file_size_mb": None,
        "audio_loudness": None,
        "errors": [],
        "warnings": [],
    }

    if not filepath.exists():
        findings["errors"].append(f"File does not exist: {filepath}")
        return findings

    findings["file_size_mb"] = round(filepath.stat().st_size / (1024 * 1024), 2)
    data = run_ffprobe(filepath)
    streams = data.get("streams", [])

    video_streams = [s for s in streams if s.get("codec_type") == "video"]
    if not video_streams:
        findings["errors"].append("Missing video stream")
    else:
        findings["video_stream"] = True
        video = video_streams[0]
        width = video.get("width")
        height = video.get("height")
        findings["resolution"] = f"{width}x{height}"
        findings["fps"] = round(parse_fps(video.get("r_frame_rate", "0/1")), 2)
        findings["video_codec"] = video.get("codec_name")
        findings["pixel_format"] = video.get("pix_fmt")

        if expected_resolution and findings["resolution"] != expected_resolution:
            findings["errors"].append(
                f"Resolution mismatch: expected {expected_resolution}, got {findings['resolution']}"
            )
        if expected_video_codec and findings["video_codec"] != expected_video_codec:
            findings["warnings"].append(
                f"Unexpected video codec: expected {expected_video_codec}, got {findings['video_codec']}"
            )
        if findings["pixel_format"] and findings["pixel_format"] != "yuv420p":
            findings["warnings"].append(f"Pixel format may reduce compatibility: {findings['pixel_format']}")
        if findings["fps"] < 24:
            findings["warnings"].append(f"FPS is low: {findings['fps']}")

    audio_streams = [s for s in streams if s.get("codec_type") == "audio"]
    findings["audio_stream"] = bool(audio_streams)
    if audio_streams:
        findings["audio_codec"] = audio_streams[0].get("codec_name")
        if expected_audio_codec and findings["audio_codec"] != expected_audio_codec:
            findings["warnings"].append(
                f"Unexpected audio codec: expected {expected_audio_codec}, got {findings['audio_codec']}"
            )
    if require_audio and not audio_streams:
        findings["errors"].append("Missing audio stream")
    elif not audio_streams:
        findings["warnings"].append("Missing audio stream")

    bitrate = data.get("format", {}).get("bit_rate")
    if bitrate:
        findings["bitrate_kbps"] = round(float(bitrate) / 1000, 1)

    duration = float(data.get("format", {}).get("duration", 0) or 0)
    findings["duration"] = round(duration, 2)
    if duration <= 0:
        findings["errors"].append("Duration is zero or unreadable")
    elif duration < 3:
        findings["warnings"].append(f"Duration is very short: {duration:.2f}s")

    if analyze_audio and audio_streams:
        findings["audio_loudness"] = run_audio_loudness(filepath)
        mean = findings["audio_loudness"].get("mean_volume_db")
        if mean:
            try:
                mean_value = float(mean.replace(" dB", ""))
                if mean_value < -28:
                    findings["warnings"].append(f"Audio may be too quiet: mean volume {mean}")
                elif mean_value > -8:
                    findings["warnings"].append(f"Audio may be too loud: mean volume {mean}")
            except ValueError:
                pass

    return findings


def print_report(findings: dict) -> int:
    print("Video quality report")
    print("====================")
    print(f"File: {findings['file']}")
    print(f"Exists: {findings['file_exists']}")
    print(f"Video stream: {findings['video_stream']}")
    print(f"Audio stream: {findings['audio_stream']}")
    print(f"Resolution: {findings['resolution']}")
    print(f"FPS: {findings['fps']}")
    print(f"Video codec: {findings['video_codec']}")
    print(f"Audio codec: {findings['audio_codec']}")
    print(f"Pixel format: {findings['pixel_format']}")
    print(f"Bitrate: {findings['bitrate_kbps']} kbps")
    print(f"Duration: {findings['duration']}s")
    print(f"File size: {findings['file_size_mb']} MB")
    if findings["audio_loudness"]:
        print(f"Audio loudness: {findings['audio_loudness']}")

    if findings["errors"]:
        print("\nErrors:")
        for item in findings["errors"]:
            print(f"- {item}")
    if findings["warnings"]:
        print("\nWarnings:")
        for item in findings["warnings"]:
            print(f"- {item}")

    if findings["errors"]:
        print("\nFAILED")
        return 1

    print("\nPASSED")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Check final MP4 quality with ffprobe.")
    parser.add_argument("input", help="Input MP4 path")
    parser.add_argument("--resolution", help="Expected resolution, for example 1080x1920")
    parser.add_argument("--allow-no-audio", action="store_true", help="Do not fail when the audio stream is missing")
    parser.add_argument("--video-codec", default="h264", help="Expected video codec, default h264")
    parser.add_argument("--audio-codec", default="aac", help="Expected audio codec, default aac")
    parser.add_argument("--analyze-audio", action="store_true", help="Run ffmpeg volumedetect and warn on rough loudness issues")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    args = parser.parse_args()

    findings = check_quality(
        Path(args.input),
        expected_resolution=args.resolution,
        require_audio=not args.allow_no_audio,
        expected_video_codec=args.video_codec,
        expected_audio_codec=args.audio_codec,
        analyze_audio=args.analyze_audio,
    )
    if args.json:
        print(json.dumps(findings, indent=2, ensure_ascii=False))
        return 0 if not findings["errors"] else 1
    return print_report(findings)


if __name__ == "__main__":
    sys.exit(main())
