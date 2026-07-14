---
name: revise-sci-manuscript
description: Coordinate a staged, review-gated revision of SCI manuscripts, supporting information, cover letters, figures, raw data, and submission files. Use when Codex needs to initialize or standardize an academic revision project; polish or translate scientific prose; audit and rebuild publication figures; reconcile text, results, tables, and figures; format a manuscript for a target journal; manage iterative author review; or deliver a clean, versioned submission package from DOCX, PDF, Markdown, LaTeX, images, plotting scripts, spreadsheets, and tabular data.
---

# Revise SCI Manuscript

## Purpose

Run an end-to-end, reproducible manuscript revision with explicit author review gates. Preserve scientific meaning and source data while producing traceable text, figure, document, and delivery revisions.

## Operating rules

- Treat original manuscripts, raw data, source figures, and author-provided files as immutable. Copy them into the project snapshot; never edit or delete them in place.
- Never invent results, citations, methods, sample sizes, statistical values, author details, journal requirements, or missing source data. Record unresolved items as queries.
- Preserve scientific meaning during language editing. Escalate any change that could alter a claim, causal interpretation, uncertainty, scope, or numerical meaning.
- Keep author decisions explicit. Do not advance past a review gate until the user approves, unless the user explicitly requests autonomous continuation. Even then, pause for scientific ambiguity, unsupported claims, missing data, or irreversible choices.
- Maintain one authoritative working version and immutable accepted versions. Do not silently overwrite an accepted version.
- Use tracked changes, redlines, diffs, or a change table whenever practical. Make every substantive change auditable.
- Treat AI-detector scores as unreliable signals. Improve specificity, evidence alignment, natural scholarly prose, and authorship transparency; never optimize to evade detection.
- Use available document, PDF, spreadsheet, plotting, and Nature or academic-writing skills when they materially improve fidelity. Read their instructions before use.

## Select the scope

Default to the full pipeline. If the user requests only one stage, run that stage but still perform intake, source protection, versioning, and final checks relevant to the requested output.

Read these references as needed:

- Read references/workflow-checklists.md before producing an intake report, stage review, revision plan, or quality-control report.
- Read references/versioning-and-delivery.md before initializing folders, advancing a version, cleaning files, or preparing final delivery.

## Stage 0: Intake and initialization

1. Inventory all supplied files and classify them as manuscript, supporting information, cover letter, journal instructions or template, figures, tables, raw data, plotting scripts, references, or other source material.
2. Ask only for missing information that materially affects the work. Prioritize:
   - manuscript and supporting files;
   - target journal and article type, if known;
   - journal template or author instructions, if provided;
   - raw or processed data and existing plotting scripts;
   - current figures in the highest-quality available format;
   - cover letter and reviewer or editor correspondence, if relevant;
   - preferred English variety, deadline, authorship constraints, and whether tracked changes are required.
3. State available materials, missing items, assumptions, proposed scope, and expected outputs in reviews/intake-checklist.md. Obtain user confirmation when missing materials could change the workflow.
4. Initialize the project with scripts/initialize_revision_workspace.py. Use v001 for the initial snapshot unless an existing version scheme must be preserved.
5. Copy source files into source_materials/, record origin and purpose in SOURCE_MANIFEST.md, and create an immutable initial version before editing.
6. Extract editable text snapshots:
   - manuscript: title, abstract, keywords when present, main text, headings, captions, table text, acknowledgements, declarations, and data or code statements; exclude the reference list unless citation work is in scope;
   - supporting information: title or metadata and substantive body, including captions and tables; exclude reference lists unless needed;
   - cover letter: complete body and metadata needed for revision.
7. Save one Markdown snapshot per source file in text_snapshot/. Preserve section order and label omitted content. Do not merge independent documents without clear boundaries.
8. Ask the user to review or directly edit the snapshots. Reconcile user edits before planning Stage 1.

## Stage 1: Foundational language revision

1. Audit approved snapshots for grammar, syntax, terminology, consistency, scientific tone, paragraph logic, cross-section coherence, redundancy, ambiguity, and unsupported emphasis.
2. Produce reviews/language-review.md with prioritized findings and author queries. Do not edit the manuscript yet.
3. Ask the user to review findings and supply corrections or constraints.
4. Produce reviews/language-revision-plan.md, integrating user comments and manual edits. Specify sections, change types, scientific-risk points, and verification steps. Obtain approval.
5. Revise line by line. Use natural, concise SCI prose; maintain terminology, tense, abbreviations, symbols, units, numerical values, citations, and claim strength consistently.
6. Compare revised text against the source and approved plan. Flag changes that require scientific confirmation. Save revised snapshots and an auditable diff or change table.
7. Ask the user to review. If changes are requested, update the plan and repeat the edit-review cycle. Mark Stage 1 complete only after acceptance.

## Stage 2: Scientific figure optimization

1. Map every figure and panel to its source data, plotting script, caption, manuscript callout, and scientific claim. Identify missing provenance.
2. Audit data integrity, visual hierarchy, panel structure, typography, units, labels, legends, color accessibility, statistical notation, resolution, dimensions, and journal constraints.
3. Produce reviews/figure-improvement-recommendations.md. Separate mandatory corrections from optional aesthetic improvements and obtain user feedback.
4. Produce reviews/figure-revision-plan.md with per-figure actions, source files, output formats, and validation checks. Obtain approval.
5. Modify or rewrite plotting scripts without modifying raw data. Keep a reproducible script for each data-derived figure in scripts/; document unavoidable manual steps. User-supplied image-only figures may retain a provenance note instead of a script.
6. Export each figure to figures/ as publication-quality PNG and SVG where technically valid. Keep a lossless raster alternative when SVG is inappropriate. Do not create misleading vector wrappers around low-resolution raster images.
7. Visually inspect exported files and verify labels, cropping, font embedding, panel order, data values, captions, manuscript references, and consistency across the figure set.
8. Ask the user to review. Repeat the approved plan-edit-review cycle until accepted, then mark Stage 2 complete.

## Stage 3: Final manuscript integration

1. Confirm target journal and article type. If requirements are not supplied, retrieve current official instructions when internet access is allowed; otherwise label formatting assumptions as provisional.
2. Merge accepted text, tables, captions, and figures into DOCX deliverables. Preserve or implement the requested template, styles, section order, numbering, references, tracked changes, and supplementary-document separation.
3. Render and inspect documents visually. Check language flow, argument structure, claim-evidence alignment, figure or table and text consistency, numbering, citations, units, typography, spacing, pagination, image quality, and overall readability.
4. Produce reviews/final-manuscript-review.md, including unresolved author queries and journal-compliance gaps. Discuss AI-authorship or detector concerns only as integrity and writing-quality issues, not as a detector-evasion target.
5. Obtain user feedback, then produce reviews/final-revision-plan.md. Apply approved changes dimension by dimension and keep them traceable.
6. Repeat review and revision until accepted. Mark Stage 3 complete only after final DOCX files and rendered appearance pass validation.

## Stage 4: Versioned delivery

1. Advance the version after an accepted revision cycle. Preserve previous accepted versions and update project state.
2. Organize the version root with these required deliverables:
   - text_snapshot/: extracted and final Markdown text snapshots;
   - manuscript/: Manuscript, Cover Letter, and Supporting Information in DOCX as applicable;
   - raw_data/: standardized copies of unmodified source data plus a data manifest;
   - scripts/: reproducible plotting and processing scripts;
   - figures/: final PNG and SVG figures, with justified alternatives where needed.
3. Include iteration-checklist.md and change-notes.md. Record version, parent version, date, stage status, files changed, substantive decisions, unresolved items, validation performed, and final deliverables.
4. Remove only generated temporary files and demonstrably redundant copies from the delivery version. Archive uncertain files; never delete original user material.
5. Run a final inventory. Check that files open, figures render, scripts point to documented data, expected formats exist, internal links and numbering agree, and no TODO markers or accidental comments remain.
6. Present the delivery path, version, completed checks, unresolved limitations, and recommended next action.

## Completion criteria

Declare the workflow complete only when requested stages are accepted, required deliverables exist, source data remain unchanged, validation is recorded, and the user receives a clear versioned handoff.
