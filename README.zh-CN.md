[English](README.md) | 简体中文

# revise-sci-manuscript

一个用于 SCI 论文手稿及投稿材料分阶段、可审阅、可追溯修改的 Codex 技能。

## 功能范围

- 材料清点、来源登记和不可变初始快照
- 设置用户审阅门的语言基础润色
- 科研配图审查、优化和可复现绘图脚本管理
- DOCX 合稿、期刊排版和整体视觉质量检查
- 版本化交付纯文本、手稿、原始数据、脚本和配图
- 自动维护迭代清单、修改说明并防止覆盖既有版本

该工作流保护科学含义和原始数据，不虚构结果、引用、方法、统计值或期刊要求。AI 检测分数被视为不可靠指标，技能重点关注写作质量、证据一致性和作者署名诚信。

## 仓库结构

    skills/
      revise-sci-manuscript/
        SKILL.md
        agents/
        references/
        scripts/

## 安装到 Codex

使用 Codex 技能安装器：

    python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Fireooout/revise-sci-manuscript --path skills/revise-sci-manuscript

也可以将 skills/revise-sci-manuscript 复制到 Codex 技能目录：

    ~/.codex/skills/revise-sci-manuscript

安装后请开启新的 Codex 任务。

## 使用示例

    使用 $revise-sci-manuscript 初始化并管理一套分阶段 SCI 手稿修改流程。

## 内置初始化脚本

初始化脚本会创建 source_materials、project-state.json 以及 v001、v002 等版本目录，并拒绝覆盖非空版本目录。

    python skills/revise-sci-manuscript/scripts/initialize_revision_workspace.py <project-root> --project-name "我的论文" --version v001

## 许可证

本项目采用 MIT License，详见 LICENSE。
