[English](README.md) | [简体中文](README.zh-CN.md)

# revise-sci-manuscript

A Codex skill for iterative, model-routed, context-recoverable, and version-preserving revision of SCI manuscripts and submission materials.

## Three operating modes

- **Assisted mode:** preserve the original stage-by-stage review workflow; the user makes the main judgments while AI analyzes, edits, and validates.
- **Command mode (default):** AI analyzes the whole project and asks only for key information. After the user confirms the project brief and full model-routed plan, AI executes one complete iteration continuously.
- **Unbounded mode:** AI proposes a complete plan with model allocation and fallbacks. After plan approval, AI completes one new-version iteration autonomously, then asks whether to run another iteration.

Every mode protects original files, the initial baseline, and all delivered versions. Each revision iteration runs in a new child version.

## What it covers

- Intake, source inventory, and immutable initial snapshots
- A consolidated project brief with key judgments and AI recommendations
- User-editable model allocation based on task difficulty and scientific risk
- Language revision, scientific figure optimization, DOCX integration, and journal formatting
- Traceable delivery of raw data, scripts, figures, manuscripts, and submission materials
- Decision logs, compact context checkpoints, safe resumption, and version sealing

The workflow preserves scientific meaning and raw data. It does not fabricate results, citations, methods, statistics, or journal requirements. AI-detector scores are treated as unreliable; the skill focuses on writing quality, evidence alignment, and authorship integrity.

## Repository layout

    skills/
      revise-sci-manuscript/
        SKILL.md
        agents/
        references/
        scripts/

## Install for Codex

Using the Codex skill installer:

    python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Fireooout/revise-sci-manuscript --path skills/revise-sci-manuscript

Or copy `skills/revise-sci-manuscript` into your Codex skills directory:

    ~/.codex/skills/revise-sci-manuscript

Start a new Codex task after installation.

## Example

    Use $revise-sci-manuscript in the default command mode to analyze my revision project and prepare the project brief and full model-routed plan first.

## Included initializer

The initializer defaults to `command` mode and creates `source_materials`, `project-state.json`, the version directory, and five control artifacts: mode selection, project brief, execution plan, decision log, and compact context summary. It refuses to overwrite a non-empty version directory.

    python skills/revise-sci-manuscript/scripts/initialize_revision_workspace.py <project-root> --project-name "My Manuscript" --version v001 --mode command

Complete and seal the `v001` baseline before opening the first revision candidate:

    python skills/revise-sci-manuscript/scripts/initialize_revision_workspace.py <project-root> --version v002 --parent v001 --mode command

## License

Released under the MIT License. See LICENSE.
