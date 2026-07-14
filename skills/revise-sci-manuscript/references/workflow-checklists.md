# Workflow Checklists

Use these checklists to keep reports concise, comparable, and actionable. Include only applicable items.

## Intake report

Record project name, article type, target journal, deadline, English variety, supplied files grouped by role, missing or unreadable materials, figure sources, raw-data and script availability, tracked-change requirements, anonymization, confidentiality, authorship constraints, requested stages, assumptions, risks, author queries, proposed version, and outputs.

Do not block on optional information. Block only when proceeding could corrupt data, alter scientific meaning, violate confidentiality, or produce the wrong submission format.

## Project brief

Record mode, version and parent, objective, success criteria, supplied evidence, scope, exclusions, target journal and article type, scientific invariants, terminology rules, author judgments, AI recommendations, assumptions, risks, hard blockers, deliverables, and confirmation state.

In command mode, distinguish clearly among facts extracted from source files, user-provided decisions, and AI recommendations. Ask the user to confirm this brief before creating the full execution plan. In unbounded mode, mark the brief as AI-synthesized and place user-editable assumptions directly in the plan.

## Full execution plan

Cover the whole requested iteration, not only the next stage. For every task record ID, stage, dependency, difficulty, scientific risk, exact model or runtime, reasoning level, specialist skill or tool, fallback, inputs, outputs, validation, pause condition, and status.

Verify that:

- every requested deliverable maps to one or more tasks;
- high-risk scientific judgments use the strongest suitable available reasoning path;
- repetitive low-risk checks use lightweight models or deterministic scripts;
- figure and document tasks include visual validation;
- model fallbacks are explicit, especially in unbounded mode;
- version creation, context compression, sealing, and final delivery are scheduled;
- the user can edit model allocation before approval.

## Text extraction quality control

- Preserve title hierarchy, paragraph order, captions, table text, equations, symbols, superscripts, subscripts, units, and citation markers.
- Label equations, figures, tables, footnotes, and omitted sections explicitly.
- Exclude reference lists by default, but retain in-text citations and links needed for consistency.
- Do not silently repair OCR errors during extraction. Mark uncertain text and resolve it before editing.
- Compare Markdown against source documents by section and spot-check numbers and symbols.

## Language review dimensions

Assess scientific meaning and claim strength; grammar and syntax; terminology, abbreviations, symbols, and units; tense, voice, and English variety; sentence clarity; paragraph flow; cross-section logic; concision and hedging; citation placement; and consistency with methods, captions, tables, figures, and numerical values.

Classify findings as critical, major, moderate, or minor. Distinguish direct corrections from author decisions.

## Language revision plan

For each section, record the problem and evidence, intended change, scientific-risk level, terminology or style rule, user instruction incorporated, validation method, and status.

After editing, compare all numbers, units, citations, abbreviations, equations, scientific names, and statistical statements against the source.

## Figure audit

For each figure and panel, record:

- purpose, manuscript claim, source data, and script provenance;
- plot type and whether it represents data honestly;
- sample size, error-bar definition, statistical test, significance notation, and uncertainty;
- axis variables, units, scales, limits, and transformations;
- color accessibility and semantic consistency;
- panel labels, legends, annotations, typography, line weights, and symbol sizes;
- dimensions, resolution, cropping, transparency, and export formats;
- caption completeness, manuscript callout, and numbering consistency;
- required correction, optional enhancement, and validation result.

Never infer missing statistical definitions. Never smooth, filter, exclude, normalize, or transform data without documented scientific authorization.

## Final manuscript review

Check:

- title, abstract, and main-text alignment;
- research question, novelty, evidence chain, limitations, and conclusion scope;
- methods and results reproducibility and terminology consistency;
- numerical values across abstract, text, tables, figures, and supporting information;
- figure and table callouts, numbering, captions, and panel references;
- citation-reference correspondence and journal style when in scope;
- journal order, limits, anonymization, declarations, data or code availability, ethics, and reporting guidelines;
- DOCX styles, fonts, spacing, headings, page breaks, equations, tables, images, and accessibility;
- cover-letter claims against the manuscript;
- unresolved comments, tracked changes, placeholders, hidden text, and accidental metadata.

Render DOCX and PDF outputs for visual inspection when tools permit. Do not rely only on text extraction.

## Mode-aware gate response

At each gate required by the selected mode, present files created or updated, top findings or changes, decisions required from the user, unresolved risks, and the exact next action after approval.

In command or unbounded execution, provide progress updates without converting them into approval requests. Pause only under the hard-stop rules in `modes-and-orchestration.md` or when the approved plan requires it.

Accept user edits as authoritative unless they conflict with data integrity, scientific consistency, journal policy, or another explicit instruction. Explain any conflict before proceeding.
