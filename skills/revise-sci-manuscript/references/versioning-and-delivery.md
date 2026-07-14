# Versioning and Delivery

## Contents

- [Recommended structure](#recommended-structure)
- [Version lifecycle](#version-lifecycle)
- [Mode and plan versioning](#mode-and-plan-versioning)
- [Source and data protection](#source-and-data-protection)
- [Context compression and recovery](#context-compression-and-recovery)
- [Required delivery filenames](#required-delivery-filenames)
- [Iteration checklist](#iteration-checklist)
- [Change notes](#change-notes)
- [Clean-delivery checks](#clean-delivery-checks)

## Recommended structure

    <project-root>/
      source_materials/
        SOURCE_MANIFEST.md
        <immutable source copies>
      project-state.json
      versions/
        v001/
          control/
            mode-selection.md
            project-brief.md
            execution-plan.md
            decision-log.md
            context-summary.md
          text_snapshot/
          manuscript/
          raw_data/
          scripts/
          figures/
          reviews/
          working/
          iteration-checklist.md
          change-notes.md
          status.md
        v002/
          ...

Keep `control/`, `reviews/`, and `working/` for traceability. Exclude them from a publisher-facing upload package unless requested.

## Version lifecycle

Use these states:

- `open-baseline`: source copies and faithful text snapshots are being assembled; no substantive revision is allowed;
- `sealed-baseline`: the initial source-derived version is immutable;
- `open-candidate`: one planned iteration is in progress;
- `delivered-awaiting-user-decision`: the candidate is validated, handed off, and sealed against edits;
- `accepted`: the user accepts the sealed candidate;
- `rejected`: the candidate remains preserved but is not the accepted basis unless the user later restores it;
- `superseded`: a preserved version has a newer accepted descendant.

Use `v001`, `v002`, and so on unless an existing convention must be preserved. Make `v001` the baseline. Complete and seal it before opening `v002` for substantive edits.

Create every revision iteration as a new child version. Record the parent, mode, plan, and source basis. Never reuse a version number for materially different content. Never reopen or edit a sealed or handed-off version; open a new child instead.

Within an `open-candidate`, allow temporary working-file changes and repeated internal repairs. On handoff, move or copy only validated deliverables to their required locations, update logs, seal the version, and stop editing it.

## Mode and plan versioning

- Store the selected mode in both `project-state.json` and the active version's `control/mode-selection.md`.
- Preserve the confirmed project brief and approved execution plan with the version they govern.
- Record plan approval, mode switches, model changes, and deviations in `decision-log.md`.
- If a material plan change is needed after approval, preserve the old plan as `control/execution-plan-superseded-<timestamp>.md` or save an auditable diff before writing the replacement.
- Switch modes only at a safe checkpoint. A mode switch never grants permission to overwrite earlier versions or perform external irreversible actions.

## Source and data protection

- Copy sources; do not move them from user-controlled locations.
- Record source filename, origin, date received, role, immutable-copy verification, and notes in `SOURCE_MANIFEST.md`.
- Preserve raw data byte-for-byte. If standardization changes representation, keep the original and place transformed data in a clearly named processed location.
- Document transformations in scripts and `change-notes.md`.
- Never delete uncertain duplicates automatically. Archive and report them.
- Compare hashes when tools permit. At minimum, compare size and modification-independent content checks before calling a source copy verified.

## Context compression and recovery

Use `control/context-summary.md` as a compact recovery checkpoint, not as a replacement for evidence. Keep it concise enough to reload quickly, normally under 1,500 words, and include:

- project, active version, parent, lifecycle state, mode, and current gate;
- approved scope and success criteria;
- immutable scientific, terminology, authorship, confidentiality, and data constraints;
- key decisions with pointers to `project-brief.md` or `decision-log.md`;
- approved plan revision and current task IDs;
- completed outputs and validation evidence;
- unresolved risks or hard blockers;
- exact next action and files that must be read before it.

Update the summary after each stage, every material decision or plan change, before a likely context rollover or long-running operation, and before handoff. Keep detailed history in the append-only decision log and change notes instead of bloating the summary.

Before replacing a materially different summary, copy the prior summary to `reviews/context-summary-<stage-or-timestamp>.md` when it contains recovery information not already captured in logs. Do not create snapshots for trivial edits.

To resume safely:

1. Read `project-state.json` and identify the active open version.
2. Read `status.md`, all five `control/` files, and the relevant manifests.
3. Verify the current plan state and next task against actual files.
4. Re-read source artifacts for scientific claims, numbers, citations, equations, and data transformations.
5. Continue only if the version is open and the planned task is authorized. Otherwise open a child version or request the minimum required decision.

## Required delivery filenames

Use these names when applicable unless journal or user rules differ:

    manuscript/Manuscript.docx
    manuscript/Manuscript_tracked.docx
    manuscript/Supporting_Information.docx
    manuscript/Cover_Letter.docx
    text_snapshot/Manuscript.md
    text_snapshot/Supporting_Information.md
    text_snapshot/Cover_Letter.md
    raw_data/DATA_MANIFEST.md
    scripts/SCRIPT_MANIFEST.md
    figures/FIGURE_MANIFEST.md
    iteration-checklist.md
    change-notes.md

## Iteration checklist

Record version, parent, lifecycle state, mode, brief status, plan revision and approval, scope, input files, baseline seal status, Stage 0 through Stage 4 status, required user approvals, planned and actual model routing, validation methods, context-summary freshness, deliverables, unresolved queries, known limitations, and next action.

## Change notes

For each material change, record artifact or location, category, rationale, whether scientific meaning changed, supporting user decision or source, affected figures or citations, model or tool used, and validation.

Summarize trivial grammar changes. Log every change that affects interpretation, data presentation, methods, claims, structure, or submission compliance.

## Clean-delivery checks

- Required folders and files exist or are marked not applicable.
- The parent and all earlier sealed versions remain unchanged.
- DOCX files open and render without corruption.
- Figures open at expected dimensions and resolution; SVG files contain real vector content where claimed.
- Plotting scripts are paired with documented inputs and do not alter raw data.
- Figure, table, equation, section, and citation numbering agree.
- No TODO, FIXME, placeholder citation, unresolved comment, hidden text, or accidental tracked change remains unless listed.
- Journal-specific claims are supported by current official instructions or labeled provisional.
- The mode, brief, approved plan, actual model routing, decision log, context summary, inventory, iteration checklist, and change notes match actual files.
- The candidate is sealed before handoff, and any subsequent work starts in a new child version.
