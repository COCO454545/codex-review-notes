---
name: ai-video-generator
description: 基于 Remotion + HyperFrames 的 AI 高密度讲解视频生成流水线，支持从文档自动生成分镜、视觉设计、HTML 合成、渲染导出全流程。
---

# AI 视频生成器

遵循 Project_02 视频生产规范，将技术文档、方法论、项目复盘转化为高质量的垂直短视频。

## 何时使用

当用户说：
- "把这篇文章做成视频"
- "把这个方法论做成讲解视频"
- "生成一个 xx 主题的知识短视频"
- "把 Project_xx 的复盘做成视频"

不要用于：
- 需要真人出镜的视频
- 纯娱乐/搞笑内容
- 超过 3 分钟的长视频
- 不需要高密度信息传递的场景

## 核心能力

### 1. Spec 生成
输入：原始文档、截图、核心观点
输出：完整的 video-spec.md（目标、受众、视觉方向、分镜表、渲染要求）

### 2. 视觉设计
- 暗黑工程仪表盘风格
- 配色：近黑背景 + 青/蓝/紫渐变 + 克制的洋红（用于风险和能量）
- 高密度布局：每个场景必须包含 标题 + 视觉证明 + 微标签 + 底部学习字幕

### 3. HTML 合成
基于 HyperFrames 框架生成可渲染的 HTML 分镜文件

### 4. 渲染导出
使用 Playwright + FFmpeg 渲染成 1080x1920 30fps MP4

## 标准 5 步工作流

### 第 1 步：需求澄清（必须先做）

在开始前，向用户确认或推断：

| 项 | 说明 | 示例 |
|---|------|------|
| 视频主题 | 一句话讲清楚这个视频讲什么 | Loop Engineering 方法论 |
| 目标受众 | 给谁看 | 中文开发者和 AI 工具用户 |
| 时长 | 原始时长，最终导出加速 1.25x | 60-90 秒原始时长 |
| 平台 | 短视频/长视频 | 小红书/视频号（竖屏） |
| 核心观点 | 观众看完记住的一句话 | Loop 不是更好的提示词，而是目标、反馈、资源和边界 |

### 第 2 步：编写 video-spec.md

必须包含以下 6 个部分：

```markdown
## 1. Goal
- Purpose: 视频目标
- Audience: 目标受众
- Platform: 发布平台
- Aspect ratio: 1080x1920（竖屏）
- Target duration: XX 秒（1.25x 加速后）
- Core sentence: 核心观点一句话

## 2. Source Material
- Documents: 源文档路径
- Screenshots/images: 参考截图位置
- Audio/voice: Edge TTS zh-CN-YunxiNeural, rate +8%, pitch -2Hz
- Data and concepts: 关键概念列表
- Missing assets: 缺少的素材

## 3. Visual Direction
- Theme: 暗黑工程仪表盘风格
- Palette: near-black canvas, cyan/blue/violet accents, restrained magenta for risk
- Typography: 强层级中文标题，紧凑 UI 标签，等宽代码片段
- Density: every scene = headline + visual proof + micro labels + bottom learning caption
- Components: 用到的视觉组件列表
- Do not use: sparse slides, copied screenshots, low-end neon clutter, wall-of-text narration

## 4. Narration
- Voice: zh-CN-YunxiNeural
- Speed: generate naturally, final MP4 at 1.25x
- Tone: confident Chinese explainer, short spoken sentences
- Subtitle style: one concise learning caption per scene

## 5. Storyboard（分镜表，核心）
| # | Time | Scene goal | On-screen visuals | Narration | Motion/transition | Assets |
|---|------|------------|-------------------|-----------|-------------------|--------|
| 1 | 0-8s | Hook with point of view | ... | ... | slow push, scan lines | article draft |
| ... | ... | ... | ... | ... | ... | ... |
| 8 | 72-84s | Close with action question | ... | ... | final glow | generated UI |

## 6. Render Requirements
- Final format: MP4
- Resolution: 1080x1920
- FPS: 30
- Audio: AAC
- Quality checks: ffprobe stream validation, preview frames at 3s/38s/70s, text readability
```

### 第 3 步：HTML 开发（每个分镜独立文件）

基于 HyperFrames 框架，为每个分镜编写独立 HTML：

```
project/
├── frames/
│   ├── frame-01-hook.html
│   ├── frame-02-vs.html
│   ├── frame-03-blocks.html
│   ├── frame-04-ci.html
│   ├── frame-05-goal.html
│   ├── frame-06-risk.html
│   ├── frame-07-evolution.html
│   └── frame-08-close.html
└── assets/
    ├── css/
    └── fonts/
```

每个 HTML 文件必须遵守：
- 暗黑工程仪表盘 CSS 变量
- 微软雅黑 + 苹方中文字体配置
- 等宽代码字体（JetBrains Mono / Fira Code）
- 动效曲线：ease-in-out cubic-bezier(0.4, 0, 0.2, 1)

### 第 4 步：质量检查（必须做）

渲染前检查：
- [ ] 所有文字可读，没有溢出或截断
- [ ] 颜色对比度符合 WCAG 标准
- [ ] 布局在 1080x1920 下正确
- [ ] 关键信息不被安全区遮挡
- [ ] 动效时长和分镜时间匹配

渲染后检查：
- [ ] ffprobe 验证视频流和音频流
- [ ] 提取关键帧（3s、中间、结尾）人工检查
- [ ] 检查字幕和口播同步
- [ ] 1.25x 加速后节奏自然

### 第 5 步：导出交付

最终交付物：
1. 最终 MP4 视频（1.25x 加速版）
2. 原始速度 MP4（存档用）
3. 分镜截图集
4. video-spec.md 文件
5. 所有 HTML 源文件

## 内置模板和最佳实践

### 8 场景标准分镜结构（可复用）

| 场景 | 时长 | 目标 | 常用手法 |
|------|------|------|---------|
| 1 钩子 | 0-8s | 抓住注意力 | 数据冲击、极端案例、反常识观点 |
| 2 概念对比 | 8-17s | 讲清是什么 | 左右分屏对比、旧方式 vs 新方式 |
| 3 核心框架 | 17-27s | 展示方法论骨架 | 卡片扫过、流程图动画、组件拆解 |
| 4 案例演示 | 27-39s | 展示真实运作 | 第一人称视角、屏幕录制、前后对比 |
| 5 核心技能 | 39-50s | 观众能学到什么 | 好坏对比仪表盘、技巧拆解 |
| 6 风险提醒 | 50-61s | 建立专业可信度 | 暗色调、警示面板、边界列表 |
| 7 演进地图 | 61-72s | 定位现在和未来 | 时间轴穿梭、阶段高亮 |
| 8 结尾行动 | 72-84s | 留下深刻印象 | 金句定格、反问、行动号召 |

### 3 秒钩子模板（开头最重要）

❌ 坏的开头：直接讲概念
> "今天我们来讲 Loop Engineering..."

✅ 好的开头：数据冲击 + 认知反差
> "有个人提交了 259 个 PR，里面**没有一行代码是他自己写的**。"

### 口播文案写作原则

1. **短句子**：每句不超过 15 个字，断句要适合口语
2. **对比优先**："不是...而是..."结构比纯定义更有力
3. **具象化**：把抽象概念变成可感知的场景
4. **节奏变化**：快的地方给信息，慢的地方给思考

### 暗黑科技风 CSS 变量（可直接复制）

```css
:root {
  --bg-canvas: #05070d;
  --bg-panel: rgba(10, 15, 30, 0.85);
  --border-glow: rgba(80, 200, 255, 0.3);
  --accent-cyan: #50c8ff;
  --accent-blue: #6b8cff;
  --accent-violet: #9d6bff;
  --accent-magenta: #ff6b9d;
  --text-primary: #e8f4ff;
  --text-secondary: #8fa4c2;
  --text-mono: #50ffaa;
  --font-sans: "Microsoft YaHei", "PingFang SC", -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", "Fira Code", monospace;
}
```

## 常见坑和避坑指南

### 坑 1：信息密度不够
- 每个场景必须至少有 4 层信息：大标题 + 视觉核心 + 微标签 + 底部字幕
- 不要做"大字报"风格的 PPT 式视频

### 坑 2：念稿子
- 口播不要把屏幕上所有文字都念出来
- 口播是屏幕信息的补充和延展，不是复读机

### 坑 3：颜色太乱
- 严格控制在 3 个主色 + 1 个强调色（风险用）
- 不要用彩虹渐变和饱和度过高的颜色

### 坑 4：节奏不对
- 每个场景 8-12 秒，不要太长也不要太短
- 最终导出必须 1.25x 加速，原始速度太拖沓

### 坑 5：表格直接念
- 观众不可能在 3 秒内看完一个 6 列表格
- 表格必须可视化：动画、拆解、比喻

## 质量检查清单（交付前必须过一遍）

- [ ] 开头 3 秒有钩子，不是直接讲概念
- [ ] 所有文字可读，字号不小于 24px
- [ ] 颜色对比度足够，暗色背景下文字清晰
- [ ] 每个场景信息密度足够，不是只有大标题
- [ ] 口播文案是短句，适合口语表达
- [ ] 口播不是在念屏幕上的文字
- [ ] 视频时长在 60-90 秒（加速后）
- [ ] 1.25x 加速后节奏自然
- [ ] ffprobe 验证通过
- [ ] 3 个关键帧截图检查通过

## 参考资源

- 视觉风格参考：Project_02 视频生成项目的 6 张微信/小红书截图
- 分镜规范参考：video-spec.md 标准模板
- CSS 变量参考：暗黑工程仪表盘主题
