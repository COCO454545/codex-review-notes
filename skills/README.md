# Workspace Skills 总览

本目录用于存放 `D:\Workspace` 的正式自建 skills。这里是 **本地唯一 skills 真源**。

## 一、唯一规则

### 1. skills 真源位置

正式 skills 统一存放在：

```text
D:\Workspace\skills\
```

### 2. 结构规则

**一个 skill = 一个独立文件夹，入口文件固定为 `SKILL.md`。**

正确结构：

```text
D:\Workspace\skills\
├── workspace-project-creator\
│   └── SKILL.md
├── research-framework\
│   └── SKILL.md
├── loop-engineering-designer\
│   └── SKILL.md
├── project-retrospective\
│   └── SKILL.md
├── ai-video-generator\
│   └── SKILL.md
└── ai-video-production-skill\
    ├── SKILL.md
    ├── references\
    ├── assets\
    ├── scripts\
    └── agents\
```

禁止结构：

```text
D:\Workspace\skills\workspace-project-creator.md
D:\Workspace\skills\research-framework.md
```

也禁止：
- 把正式 skill 放在某个 `Project_*` 目录里长期维护
- 本地再发明第二套 skills 真源目录

---

## 二、当前已沉淀的 Skills

| Skill 名称 | 定位 | 主要用途 |
|-----------|------|---------|
| **workspace-project-creator** | 项目创建 skill | 标准化新项目目录结构与基础说明文件 |
| **research-framework** | 调研/选型 skill | 技术选型、开源项目对比、方案调研 |
| **loop-engineering-designer** | 自动化设计 skill | 设计 Loop Engineering / 自动化流水线 |
| **project-retrospective** | 复盘沉淀 skill | 项目复盘、踩坑整理、经验沉淀 |
| **ai-video-generator** | 视频生产轻量 skill | 技术/知识类视频生成工作流 |
| **ai-video-production-skill** | 视频生产完整 skill | 端到端视频项目：参考学习、spec、proof、渲染、验收、清理、进化 |

---

## 三、使用方式

### 方式一：本机直接作为技能源

Claude Code / 其他工具如果支持 skills 目录，统一指向：

```text
D:\Workspace\skills
```

### 方式二：同步到 GitHub 仓库作为镜像

GitHub 里的 `skills/` 只是镜像副本，方便跨设备同步。

原则：
- 先在 `D:\Workspace\skills\` 维护
- 再同步到远程仓库
- 不反过来以 GitHub 镜像作为本地真源

---

## 四、什么样的内容应该沉淀成 Skill

适合沉淀成 skill：
- 跨项目反复使用的工作流程
- 需要固定触发条件、固定输出格式的操作
- 已经被验证过、不是临时想法的流程
- 能独立迁移到公司电脑和新电脑的能力

不适合直接沉淀成 skill：
- 单次项目里的过程性脚本
- 未稳定、尚未验证的方法
- 只适用于一个项目、无法跨场景复用的流程
- 依赖敏感数据、项目素材或大文件的内容

---

## 五、Skill 编写规范

### 最小结构

每个 skill 至少包含：

```text
skill-name\
└── SKILL.md
```

### 可扩展结构

如果 skill 需要更多内容，可以增加：

- `references/`：方法说明、参考规则、案例学习
- `assets/`：小型模板、预览图、必要的轻量素材
- `scripts/`：工具脚本、检查脚本、初始化脚本
- `agents/`：需要时的 agent 配置

### `SKILL.md` 建议内容

- frontmatter（name / description）
- 适用场景
- 核心规则
- 标准流程
- 输出要求
- 注意事项 / 边界条件

---

## 六、维护原则

1. 先把技能沉淀在 `D:\Workspace\skills\`。
2. 只有确认它已经稳定、可复用，才同步到 GitHub。
3. skill 的修改，应尽量是“升级成更完整的最终成果”，而不是不断堆临时补丁。
4. 如果某个项目里形成了可复用流程，应从项目里提炼后迁移进这里，而不是长期保留在项目目录中。

---

## 七、后续可补充方向

后续可以继续沉淀的 skill 方向：

- Git 工作树 / 分支整理
- 双模型互审
- bug 复盘模板
- 同步前检查清单
- 项目知识提取与回填
- 飞书 / 邮件 / 文档自动化助手

---

## 八、一句话说明

> **Workspace 根目录的 md 是规则真源，`D:\Workspace\skills\` 是技能真源。**
>
> **项目目录可以产出经验，但最终要把可复用成果沉淀回这里。**
