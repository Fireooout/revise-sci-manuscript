---
name: revise-sci-manuscript
description: Coordinate iterative, version-preserving revision of SCI manuscripts, supporting information, cover letters, figures, raw data, and submission files in assisted, command, or unbounded mode. Use when Codex needs to initialize or standardize an academic revision project; let an author direct each review gate; let the author approve a project brief and model-routed execution plan before AI-led work; run one approved autonomous revision iteration; polish or translate scientific prose; audit and rebuild publication figures; reconcile text, results, tables, and figures; format a manuscript for a target journal; compress long-running project context; or deliver a clean, traceable submission package from DOCX, PDF, Markdown, LaTeX, images, plotting scripts, spreadsheets, and tabular data.
---

# Revise SCI Manuscript

## Purpose

Run an end-to-end, reproducible manuscript revision while matching the user's preferred level of control. Preserve scientific meaning, source data, original files, and every handed-off version. Treat all work as an iteration that produces a new candidate version rather than overwriting its parent.

## Enforce non-negotiable safeguards

- Treat original manuscripts, raw data, source figures, and author-provided files as immutable. Copy them into the protected source snapshot; never edit, move, rename, or delete them in place.
- Never invent results, citations, methods, sample sizes, statistical values, author details, journal requirements, or missing source data. Record unresolved items and provenance.
- Preserve scientific meaning during language editing. Escalate or conservatively defer any change that could alter a claim, causal interpretation, uncertainty, scope, or numerical meaning.
- Keep one open candidate version at a time. Seal every baseline, accepted version, and delivered candidate before starting its child version. Never silently overwrite a sealed version.
- Use tracked changes, redlines, diffs, or a change table whenever practical. Make every substantive change auditable.
- Treat AI-detector scores as unreliable signals. Improve specificity, evidence alignment, natural scholarly prose, and authorship transparency; never optimize to evade detection.
- Use available document, PDF, spreadsheet, plotting, literature, and academic-writing skills when they materially improve fidelity. Read each selected skill before use.

## Select the operating mode first

Recognize Chinese or English mode names. If the user does not choose a mode, use **command mode** and state that default at the start. Do not block solely to ask for a mode; give the user an opportunity to switch before approving the next control artifact.

- **Assisted mode (辅助模式):** follow the original review-gated workflow. The user makes the main decisions; AI analyzes, drafts, edits, and verifies after each approval.
- **Command mode (指挥模式, default):** analyze the complete project, ask only for key missing facts or judgments, consolidate them in `control/project-brief.md`, obtain confirmation, then produce `control/execution-plan.md` with task-level model allocation. After plan approval, execute the approved iteration without routine stage gates. Pause only at a hard stop or material plan deviation.
- **Unbounded mode (无界模式):** analyze difficulty and assumptions, produce the complete model-routed execution plan, and obtain plan approval. Then complete exactly one candidate-version iteration autonomously. Return to the user only for a hard stop or after the iteration so the user can accept it or request another iteration.

Read [references/modes-and-orchestration.md](references/modes-and-orchestration.md) in full before asking intake questions, creating a project brief, allocating models, planning work, switching modes, or advancing a gate.

## Maintain control artifacts

Keep these Markdown files inside each active version's `control/` directory:

- `mode-selection.md`: selected mode, how it was selected, mode-switch history, and current gate policy;
- `project-brief.md`: confirmed facts, key user judgments, AI recommendations, assumptions, boundaries, risks, deliverables, and unresolved hard blockers;
- `execution-plan.md`: full task sequence, dependencies, difficulty, exact available model or runtime, reasoning level, specialist tools or skills, fallback, outputs, validation, and approval state;
- `decision-log.md`: append-only record of user decisions, AI assumptions, plan changes, mode changes, and scientific-risk resolutions;
- `context-summary.md`: compact, current recovery state for context compression and handoff.

Treat the brief, approved plan, decision log, manifests, and source files as authoritative. Treat `context-summary.md` only as a recoverable cache with pointers to those sources.

Read [references/workflow-checklists.md](references/workflow-checklists.md) before producing a brief, plan, review, stage report, or quality-control report. Read [references/versioning-and-delivery.md](references/versioning-and-delivery.md) before initializing folders, copying sources, opening or sealing a version, cleaning files, compressing context, resuming work, or preparing delivery.

## Launch the project safely

1. Perform a read-only inventory of supplied materials and existing project state. Do not ask for information already present in files.
2. Announce the selected or defaulted mode, summarize the immediate next gate, and record the mode.
3. Initialize the protected workspace with `scripts/initialize_revision_workspace.py`. Pass `--mode assisted`, `--mode command`, or `--mode unbounded`; default to `command`.
4. Copy source files into `source_materials/`, record origin and purpose in `SOURCE_MANIFEST.md`, extract faithful Markdown snapshots, and seal the initial baseline. Use `v001` unless an existing version convention must be preserved.
5. Before any substantive edit, open a new child candidate such as `v002` with `--parent v001`. Copy only the parent artifacts needed for the iteration; never mutate the parent.
6. Apply the selected mode's pre-execution gates. Do not begin substantive revision in command or unbounded mode until the required plan is approved.

## Run the common revision stages

Use the same scientific workflow in every mode; vary only who decides, when approval is required, and how interruptions are handled. Apply the current mode's gate policy after each stage.

### Stage 0: Intake, baseline, and iteration setup

1. Classify files as manuscript, supporting information, cover letter, journal instructions or template, figures, tables, raw data, plotting scripts, references, correspondence, or other source material.
2. Verify file readability, source provenance, confidentiality constraints, article type, target journal when known, requested scope, figure-data links, and deliverables.
3. Extract manuscript, supporting-information, and cover-letter text into separate Markdown snapshots while preserving order, headings, captions, tables, equations, symbols, units, and citation markers. Label omissions and uncertain extraction.
4. Compare snapshots with their sources. Seal the baseline before revision and open a child candidate.
5. Create or update the mode-specific brief and execution plan. Record assumptions instead of repeatedly querying optional information.

### Stage 1: Foundational language revision

1. Audit approved inputs for scientific meaning, claim strength, grammar, syntax, terminology, consistency, tone, paragraph logic, cross-section coherence, redundancy, ambiguity, and unsupported emphasis.
2. Produce `reviews/language-review.md` and an actionable language-revision section in the execution plan. In assisted mode, also use `reviews/language-revision-plan.md` as the stage approval artifact.
3. Revise line by line. Preserve terminology, tense, abbreviations, symbols, units, numerical values, citations, and claim strength.
4. Compare revised text against the source, brief, and plan. Save revised snapshots and an auditable diff or change table. Route scientific-risk items according to the current mode.

### Stage 2: Scientific figure optimization

1. Map each figure and panel to source data, plotting script, caption, manuscript callout, and scientific claim. Identify missing provenance.
2. Audit integrity, hierarchy, panel structure, typography, units, labels, legends, color accessibility, statistical notation, resolution, dimensions, and journal constraints.
3. Produce `reviews/figure-improvement-recommendations.md` and a per-figure execution plan. In assisted mode, obtain approval through `reviews/figure-revision-plan.md`.
4. Modify or rewrite plotting scripts without modifying raw data. Preserve reproducible scripts and document unavoidable manual steps.
5. Export publication-quality figures in technically valid formats, visually inspect them, and verify data, labels, cropping, font handling, panel order, captions, and manuscript references.

### Stage 3: Final manuscript integration

1. Confirm journal requirements from user-supplied or current official instructions. Label unsupported formatting assumptions as provisional.
2. Merge revised text, tables, captions, and figures into the required DOCX or other deliverables. Preserve templates, styles, numbering, references, tracked changes, and supplementary-document separation.
3. Render and inspect the documents. Check language flow, argument structure, claim-evidence alignment, cross-file numerical consistency, citations, units, numbering, typography, spacing, pagination, image quality, and readability.
4. Produce `reviews/final-manuscript-review.md`. In assisted mode, obtain approval through `reviews/final-revision-plan.md`; in command or unbounded mode, resolve in-plan items autonomously and record any hard stop.

### Stage 4: Verification, sealing, and delivery

1. Run the full inventory and validation checklist. Verify that files open, figures render, scripts point to documented data, expected formats exist, numbering agrees, and no accidental TODO markers, comments, or tracked changes remain.
2. Update `iteration-checklist.md`, `change-notes.md`, the decision log, and the compact context summary. Record actual model and tool use when it differs from the plan.
3. Mark the candidate `accepted`, `rejected`, or `delivered-awaiting-user-decision` as appropriate, then seal it against further editing.
4. Present the version path, parent, mode, completed checks, material changes, unresolved limitations, and recommended next action.

## Apply iteration semantics

- Treat one pass through the approved scope as one iteration and one new candidate version.
- In assisted mode, repeat a stage within the open candidate only while the user is reviewing that stage. After a candidate is accepted or delivered, open a new child version for any further change.
- In command mode, finish the approved cross-stage plan, deliver the sealed candidate, and ask whether to accept or start a new planned iteration.
- In unbounded mode, stop after exactly one sealed autonomous candidate. Ask whether the user wants another iteration; if yes, analyze the prior candidate, create a new plan and child version, obtain plan confirmation, and repeat.
- Never interpret “continue automatically” as permission to publish, submit, message third parties, delete sources, or perform irreversible external actions.

## Compress and restore context

Update `control/context-summary.md` after every stage, before a long tool run or likely context rollover, after any material decision, and before handoff. Keep it concise and include only current mode and gate state, version lineage, approved scope, immutable constraints, key decisions with pointers, completed outputs and validation, open risks, and the exact next action.

On resume, read `project-state.json`, the active version's `status.md`, `mode-selection.md`, `project-brief.md`, `execution-plan.md`, `decision-log.md`, `context-summary.md`, and relevant manifests before continuing. Re-check source artifacts for any scientific or numerical claim; never rely on compressed memory alone.

## Completion criteria

Declare an iteration complete only when its approved scope is executed, required deliverables exist, source data and prior versions remain unchanged, validation and actual model routing are recorded, context is recoverable, the candidate is sealed, and the user receives a clear versioned handoff.
