[English](README.md) | 简体中文

# revise-sci-manuscript

一个用于 SCI 论文手稿及投稿材料迭代修改、模型路由、上下文恢复和版本化交付的 Codex 技能。

## 三种工作模式

- **辅助模式**：保留原始逐阶段审阅流程，由用户作主要判断，AI 负责分析、修改与验证。
- **指挥模式（默认）**：AI 先完成整体分析，只询问关键信息；用户确认项目简报和全流程模型分配计划后，AI 连续执行一个完整迭代。
- **无界模式**：AI 生成带模型分配和回退策略的全流程计划；计划确认后，全自动完成一个新版本迭代，再由用户决定是否继续下一轮。

无论采用哪种模式，原始文件、初始基线和已交付版本都不会被覆盖。每轮修改在新的子版本中进行。

## 功能范围

- 材料清点、来源登记和不可变初始快照
- 项目简报、关键判断和 AI 建议的集中记录
- 按任务难度与科学风险生成可修改的模型分配计划
- 语言润色、科研配图优化、DOCX 合稿和期刊排版
- 原始数据、绘图脚本、图件和投稿材料的可追溯交付
- 决策日志、压缩上下文、断点恢复和版本封存

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

也可以将 `skills/revise-sci-manuscript` 复制到 Codex 技能目录：

    ~/.codex/skills/revise-sci-manuscript

安装后请开启新的 Codex 任务。

## 使用示例

    使用 $revise-sci-manuscript，以默认指挥模式分析我的论文修改项目，先生成项目简报和全流程模型分配计划。

## 内置初始化脚本

初始化器默认采用 `command` 模式，创建 `source_materials`、`project-state.json`、版本目录以及五个控制文件：模式记录、项目简报、执行计划、决策日志和压缩上下文。它拒绝覆盖非空版本目录。

    python skills/revise-sci-manuscript/scripts/initialize_revision_workspace.py <project-root> --project-name "我的论文" --version v001 --mode command

先完成并封存 `v001` 基线，再建立首个修改候选版本：

    python skills/revise-sci-manuscript/scripts/initialize_revision_workspace.py <project-root> --version v002 --parent v001 --mode command

## 许可证

本项目采用 MIT License，详见 LICENSE。
