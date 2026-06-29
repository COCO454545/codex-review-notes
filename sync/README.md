# 跨设备同步操作指南

> codex-review-notes 仓库的标准同步流程。用于家庭电脑和公司电脑之间双向同步知识层资产。

---

## 目录

1. [首次同步](#首次同步)
2. [标准同步流程](#标准同步流程)
3. [冲突处理](#冲突处理)
4. [Skill 跨设备适配](#skill-跨设备适配)
5. [同步日志模板](#同步日志模板)

---

## 首次同步

### 家庭电脑（主端）

已经完成！本仓库就是主端的完整沉淀。

### 公司电脑（从端）

**步骤 1：克隆仓库**

```powershell
# 推荐直接克隆到 Workspace
git clone https://github.com/COCO454545/codex-review-notes.git D:\Workspace

# 或者克隆到临时目录，再按需复制
git clone https://github.com/COCO454545/codex-review-notes.git D:\codex-sync
```

**步骤 2：配置 Claude Code Skill 路径**

打开 Claude Code 设置 → 找到 Skill 路径配置，添加：

```json
{
  "skillPaths": [
    "D:/Workspace/claude/skills"
  ]
}
```

或者建立软链接（管理员 PowerShell）：

```powershell
New-Item -ItemType SymbolicLink `
  -Path "$env:USERPROFILE\.claude\skills" `
  -Target "D:\Workspace\claude\skills"
```

**步骤 3：配置 hooks（如需要）**

如果使用 Codex，将 `.codex/hooks/` 下的 hook 脚本复制或建立软链接到你的 Workspace。

---

## 标准同步流程

### 频率建议

- **正常工作**：每周日晚同步一次
- **重要沉淀**：有重大更新时随时同步
- **Skill 更新**：新增或修改 Skill 后立即同步

### 标准 6 步同步法

```bash
# ========== 两端通用流程 ==========

# 1. 先拉取最新
git pull origin main

# 2. 检查本地 Workspace 有哪些更新
# - 复利日志有新记录吗？
# - 有没有新增/修改的 Skill？
# - 全局规则有更新吗？
# - 复盘有新沉淀吗？

# 3. 把更新复制到仓库（如需要）
# 示例（手动复制，推荐用文件对比工具）：
# - 复利日志新增内容追加到 01_全局复利踩坑日志.md
# - 新 Skill 复制到 claude/skills/ 或 skills/
# - 全局规则更新对应 md 文件

# 4. 写入同步日志
# 编辑 sync/sync-log.md，记录本次同步内容

# 5. 提交
git add .
git commit -m "sync(home|work): yyyy-mm-dd 简要说明"

# 6. 推送
git push origin main
```

### 每周日检查清单

每次同步前检查：

- [ ] 本周新增的踩坑记录已写入复利日志
- [ ] 本周形成的优质做法已沉淀
- [ ] 可复用的流程已封装成 Skill
- [ ] 全局规则有更新
- [ ] `git status` 只显示知识层文件
- [ ] `git diff` 确认没有敏感数据
- [ ] 同步日志已更新

---

## 冲突处理

### 冲突类型与优先级

| 冲突类型 | 优先级 | 处理方式 |
|---------|--------|---------|
| **复利日志新增记录** | 🔴 最高 | 两边内容都保留，按日期追加，永不删除 |
| **Skill 文件不同** | 🟠 高 | 先都保留（加 -home/-work 后缀），下一次面对面 review 后合并 |
| **全局规则修改** | 🟡 中 | 以更新时间为准，或保留两个版本合并 |
| **同步日志冲突** | 🟢 低 | 都追加，按日期排序 |

### 硬规则 ⚠️

1. **复利日志永远只追加，不删除**
2. **Skill 冲突时，先两个版本都保留，不要随意删除**
3. **不确定如何合并时，先 commit 推送到 GitHub，下一次见面时一起看**
4. **删除任何内容前，先确认另一端不需要**

### 冲突解决步骤

```bash
# 1. pull 后发现冲突
git pull origin main
# → Auto-merging ...
# → CONFLICT ...

# 2. 不要慌，先看看冲突内容
git diff --name-only --diff-filter=U

# 3. 按上面的优先级处理
# - 复利日志冲突：手动编辑，两边内容都保留，按日期排序
# - Skill 冲突：重命名为 skill-name-home.md / skill-name-work.md
# - 规则冲突：看更新时间，或合并成更完整版本

# 4. 解决后提交
git add .
git commit -m "merge: resolved conflict in xxx"
git push
```

---

## Skill 跨设备适配

### Skill 编写规范

为了保证 Skill 在两端都能正常使用，请遵守：

1. **不要写死绝对路径**
   - ❌ `D:\ai_tool\workspace\Project_xx`
   - ✅ 相对路径或环境变量引用

2. **环境差异说明**
   - 如果 Skill 有路径依赖，在开头加"环境适配"章节
   - 说明两端可能的差异

3. **引用全局文档时用名称**
   - ❌ `D:\xxx\01_全局复利踩坑日志.md`
   - ✅ 参考 `01_全局复利踩坑日志.md` 的方法 003

4. **Skill 分层清晰**
   - `claude/skills/`：Claude Code 专用文本模板 Skill
   - `skills/xxx/`：Codex 专用带脚本的复杂 Skill

### 新增 Skill 检查清单

- [ ] Skill 名称清晰，见名知意
- [ ] 没有硬编码的绝对路径
- [ ] 开头有 frontmatter（name, description）
- [ ] 有明确的适用场景说明
- [ ] 有标准化的流程或模板
- [ ] 引用的全局文档名称正确
- [ ] 已同步到两端测试可用

---

## 同步日志模板

每次同步都更新 `sync/sync-log.md`，格式如下：

```markdown
## 2026-06-29 | home | 仓库初始化与首次合并

### 新增内容

#### global/
- 01_全局复利踩坑日志.md：新增 1 条踩坑 + 4 条优质做法
  - 坑 001：第一版不要追求大而全
  - 做法 001：7维度技术选型评估法
  - 做法 002：副业自动化边界设计哲学
  - 做法 003：一次性取件码状态机设计
  - 做法 004：四阶段系统分层实施路线

#### claude/skills/（新增 4 个通用 Skill）
- workspace-project-creator.md：标准化项目创建器
- research-framework.md：技术选型调研框架
- loop-engineering-designer.md：自动化流水线设计器
- project-retrospective.md：项目复盘沉淀模板

#### sync/
- README.md：本同步操作指南
- sync-log.md：同步日志

### 更新内容
- 全局文档统一路径：D:\ai_tool\workspace → D:\Workspace
- 复利日志 003 方法中的 hooks 路径已更新
- 06_工作区提示词.md 中的路径已更新

### 备注
- 首次完成家庭端知识沉淀与 GitHub 仓库架构合并
- 下一次同步在公司电脑执行，测试从端同步流程
```

---

## 最佳实践

### 1. 小步快跑
不要攒到很多内容才同步。有一条新记录、一个新 Skill，就可以单独同步一次。小同步冲突少，也好处理。

### 2. 同步日志要写清楚
不要只写 "update"。写清楚新增了什么、更新了什么，方便另一端了解变化。

### 3. 每周固定时间同步
养成习惯，比如周日晚上 9 点，两边电脑各花 5 分钟同步一次。

### 4. Skill 先在一端验证再同步
新增的 Skill 先在一端充分测试，确认好用再推送到仓库同步到另一端。

---

## 相关文档

- [07_GitHub同步SOP.md](../07_GitHub同步SOP.md) - 同步范围和安全规则
- [00_全局控制台.md](../00_全局控制台.md) - Workspace 最高规则
- [01_全局复利踩坑日志.md](../01_全局复利踩坑日志.md) - 经验沉淀入口
- [AGENTS.md](../AGENTS.md) - AI 行为规范