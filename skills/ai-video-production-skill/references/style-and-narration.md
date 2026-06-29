# Style And Narration

## Taste Profile

The user prefers:

- Dense, structured, technical visual systems.
- Apple/keynote-like information hierarchy with real UI detail.
- Dark premium technology palettes for explainers.
- Glass panels, metric cards, terminal fragments, code snippets, process diagrams, badges, status pills, data bars, grids, HUD micro-details.
- Rich but controlled density, not messy clutter.
- References used for composition and density, not copied pixel-for-pixel.

Reject:

- Sparse slides with one title and a few bullets.
- Generic purple-gradient AI layouts.
- Low-end e-commerce poster aesthetics.
- Over-saturated neon clutter.
- Robotic narration or manuscript reading.
- Full-screen screenshots used as lazy backgrounds.

## Default Visual Direction

Use this for AI/tech explainers unless another style is approved:

- Background: `#05070d`, `#07182e`
- Text: `#f8fbff`, `#b7c9ec`, `#7890bd`
- Accents: `#39f2d0`, `#5aa7ff`, `#8c66ff`, `#ff5aa7`, `#ff547d`
- Easing: `cubic-bezier(.25, 1, .5, 1)`
- Chinese font stack: `"Microsoft YaHei", "PingFang SC", "Segoe UI", sans-serif`
- Code font stack: `"Cascadia Code", "Consolas", monospace`

Useful CSS variables:

```css
:root {
  --bg: #05070d;
  --ink: #f8fbff;
  --soft: #b7c9ec;
  --muted: #7890bd;
  --line: rgba(132, 181, 255, .28);
  --cyan: #39f2d0;
  --blue: #5aa7ff;
  --violet: #8c66ff;
  --magenta: #ff5aa7;
  --red: #ff547d;
  --ease: cubic-bezier(.25, 1, .5, 1);
}
```

## Vertical Layout

For `1080x1920`:

- Safe side margin: 42-54px.
- Top status/progress area.
- Large headline area.
- Hero visual area.
- Main information grid or process diagram.
- Bottom takeaway/caption area.

No empty frames. Every scene longer than 4 seconds must carry a concept, metric, proof, step, emotional beat, or deliberate pause.

## Narration

- Use short spoken Chinese sentences.
- Split narration by scene.
- Keep captions concise; captions should summarize, not duplicate the full narration.
- Preferred voice reference: `assets/voice-style-reference.mp3`.
- Previous preferred TTS style: `zh-CN-YunxiNeural`, rate `+8%`, pitch `-2Hz`.
- Use about `1.25x` final pacing when the user wants a tighter short-video feel.
- Probe actual audio durations before locking scene lengths.
- Male口播 is the default direction when the user wants creator-style delivery or has not approved another voice.
- Generate a 10-20 second voice proof before a full narrated render. The proof must include the opening hook and one analytical sentence.
- If available voices sound stiff, robotic, or like system narration, do not ship them as final. Use a labeled placeholder, ask for a better voice path/sample, or render a silent visual proof instead.
- Voice quality is a hard acceptance gate: gender/style fit, natural pauses, sentence stress, and non-scripted delivery matter more than merely having an audio stream.

Bad narration:

- More than 50 Chinese characters in one scene.
- Reading visible text word-for-word.
- Dense jargon without explanation.
- No pauses or emotional contour.
- Windows SAPI/system TTS shipped as final口播.
- Female generic assistant voice when the requested direction is male creator narration.
- Perfectly grammatical but emotionally flat script reading.

## Opening Hook Style

For analysis/ranking videos, write the opening like spoken content, not a report title:

- Start with conflict or surprise: "这 6 个项目不是星最多，而是最近涨得最猛。"
- Add a why-care line: "它们暴涨，不是因为概念新，而是因为解决了 AI 工作者每天都烦的问题。"
- Avoid formal report phrasing such as "本视频将介绍" or "以下是排名".
- Keep the first spoken sentence under 18 Chinese characters when possible.

## Preview Discipline

Generate previews before expensive final renders when style is uncertain. Do not keep rechecking tiny details after the user accepts a direction. Move to render once style, narration, and spec are coherent.

## Short-Video Card Poster Opening

Use this when the user shares a Douyin/Xiaohongshu-style screenshot, tool list poster, ranking cover, or asks for a punchier creator-style opening.

- Build the first frame around one oversized promise: subject + number + benefit, for example "近30天 GitHub 暴涨的 6 个 AI 项目".
- Use a large colored number as the visual anchor. Keep colors controlled: dark base, white title, one hot accent such as yellow, plus per-card rank colors.
- Use stacked ranked cards. Each card needs: index, compact visual/icon area, name, role tag, use-case line, and a proof/preview area.
- Add a bottom decision strip such as "推荐优先级", "适合谁看", or "先看这三个". This helps the viewer know what to do with the list.
- Pair the visual with a natural male creator hook, not a report opening. Example: "GitHub 最近暴涨的 6 个 AI 项目，不是星最多，而是涨得最猛。"
- Translate the reference structure into the user's topic. Do not copy the source poster, icons, creator identity, or exact copy.
- Before full render, produce an opening-frame style proof and a 10-15 second male voice proof when this style is requested or clearly implied.
