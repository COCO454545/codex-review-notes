# 07_GitHub同步SOP

> 本文档规定 `D:\Workspace` 中哪些内容可以同步到 GitHub，用于在家里电脑、公司电脑之间复用同一套工作台成果。

## 一、同步目标

同步的是**沉淀层**，不是**项目层**。

目标：
1. 公司电脑克隆后，能第一时间继承同一套 Codex/Claude Code 使用习惯。
2. 保留全局复盘、踩坑日志、工作区规则、预览优先流程、skills 和协作偏好。
3. 避免把真实项目资料、题库、音视频、大文件、密钥或隐私数据传到 GitHub。
4. 无论家庭电脑还是公司电脑，最终都围绕同一个 `D:\Workspace` 沉淀模型工作，避免各自为战。

## 二、唯一真源原则

1. **`D:\Workspace` 是唯一沉淀真源。**
2. 本地真正长期维护的成果，只有：
   - Workspace 根目录全局 md
   - `D:\Workspace\skills\`
3. GitHub 仓库只是镜像，不是真源。
4. 旧本地仓库目录只是历史镜像缓存，不再作为正式工作位置。

## 三、允许同步的内容

默认允许同步：

```text
00_全局控制台.md
01_全局复利踩坑日志.md
02_全局项目索引.md
03_新项目创建SOP.md
04_ClaudeCode搭配Codex六种接线机制操作手册.md
05_Cyrus說AI视频_Claude自动化调教分析.md
06_工作区提示词.md
07_GitHub同步SOP.md
AGENTS.md
协作偏好_沟通复盘.md
.codex/hooks.json
.codex/hooks/*.py
.codex/hooks/*.md
skills/*/SKILL.md
skills/*/references/**
skills/*/assets/**
skills/*/scripts/**
skills/*/agents/**
```

说明：
- `02_全局项目索引.md` 可以同步，但只保留非敏感项目名称和状态；如果包含客户、账号或商业信息，应先脱敏。
- `skills/` 只同步自建或已经深度个人化的 skill，不同步未经整理的第三方完整仓库。
- 如果某个 skill 包含少量必要的预览图、小音频、模板、脚本，可一并同步；但必须是这个 skill 的组成资产，而不是项目输出物。

## 四、禁止同步的内容

默认禁止同步：

```text
Project_*/
*.env
*.key
*.pem
*.pfx
*.token
*.mp4
*.mp3
*.wav
*.pdf
*.docx
*.xlsx
*.zip
*.7z
*.rar
node_modules/
dist/
dist_*/
build/
99_temp/
__pycache__/
```

也禁止同步：
- API key、token、密码、cookie。
- 真实用户数据、客户数据、题库原始数据。
- 线上后台地址、管理密码、分享码密码。
- 未确认可公开的截图、聊天记录、课程资料。
- 普通 `Project_*` 的业务资产、素材、导出物、缓存和依赖目录。

## 五、同步流程

### 标准流程
1. 先在 `D:\Workspace` 完成沉淀层更新。
2. 检查 `git status`，确认只出现全局 md、hooks、skills 等沉淀层文件。
3. 检查 diff，确认没有密钥、密码、真实数据，也没有误把 `Project_*` 带进去。
4. commit 信息写清楚本次沉淀更新内容。
5. push 到 GitHub 仓库。
6. 公司电脑 pull 后，把这套仓库内容同步到本机 `D:\Workspace` 使用。

### 判断规则
- 如果某个改动属于规则、偏好、方法、SOP、skill → 同步
- 如果属于具体业务项目、项目文件、项目素材、项目导出物 → 不同步

## 六、公司电脑使用方式

推荐方式：

```powershell
git clone <你的仓库地址> D:\WorkspaceSync
```

然后：
1. 用它作为知识层镜像。
2. 把其中的全局 md 和 `skills/` 同步到公司电脑自己的 `D:\Workspace`。
3. 正常项目仍然放在公司电脑自己的 `D:\Workspace\Project_*` 下。

**不要**直接在旧镜像目录里长期工作；真正工作入口仍然应该是本机的 `D:\Workspace`。

## 七、skills 同步规则

1. 本地真源是 `D:\Workspace\skills\`。
2. 一个 skill = 一个文件夹 = 一个 `SKILL.md` 入口文件。
3. 不允许再使用 `skills\xxx.md` 这种平铺形式。
4. 项目目录里的 skill 草稿、副本不算正式技能，不应作为同步真源。
5. 同步时以 `D:\Workspace\skills\` 为准，而不是以旧镜像目录为准。

## 八、重要原则

1. 真正要同步的是**成果沉淀**，不是历史过程。
2. 合并沉淀时，应整理成最终版成果，而不是机械拼接旧文件。
3. 任何上传 GitHub 的动作，都必须先看 `git status` 和 diff。
4. 不确定是否敏感时，默认不同步。
5. 不确定结构归属时，先问，不擅自建立第二套体系。
6. 旧仓库中的有价值内容要先沉淀回 Workspace，再由 Workspace 镜像出去。

## 九、同步后的删除原则

在确认 Workspace 已经成为完整真源、远程仓库已经镜像完成之后，可以删除：
- 旧本地镜像仓库目录
- 项目目录中的 skills 副本目录

删除前提：
1. 真源内容已完整存在于 `D:\Workspace`。
2. 远程仓库已成功推送并校验结构正确。
3. 本地不再依赖旧镜像目录运行。

## 十、简短结论

> **先把成果沉淀到 `D:\Workspace`，再同步到远程。**
>
> **GitHub 是镜像，不是真源。**
>
> **`Project_*` 是项目层，不是沉淀层。**
