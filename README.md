# revise-sci-manuscript

A Codex skill for staged, review-gated, and versioned revision of SCI manuscripts and submission materials.

## What it covers

- Intake, source inventory, and immutable initial snapshots
- Foundational language revision with author review gates
- Scientific figure audits and reproducible plotting scripts
- Final DOCX integration, journal formatting, and visual quality checks
- Versioned delivery of text snapshots, manuscripts, raw data, scripts, and figures
- Iteration checklists, change notes, and overwrite protection

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

Or copy skills/revise-sci-manuscript into your Codex skills directory:

    ~/.codex/skills/revise-sci-manuscript

Start a new Codex task after installation.

## Example

    Use $revise-sci-manuscript to initialize and manage a staged SCI manuscript revision workflow.

## Included initializer

The initializer creates source_materials, project-state.json, and version folders such as v001 and v002. It refuses to overwrite a non-empty version directory.

    python skills/revise-sci-manuscript/scripts/initialize_revision_workspace.py <project-root> --project-name "My Manuscript" --version v001
