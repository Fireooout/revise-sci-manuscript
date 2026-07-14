# Versioning and Delivery

## Recommended structure

    <project-root>/
      source_materials/
        SOURCE_MANIFEST.md
        <immutable source copies>
      project-state.json
      versions/
        v001/
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

Keep reviews/ and working/ for traceability. Exclude them from a publisher-facing upload package unless requested.

## Version rules

- Use v001, v002, and so on unless an existing convention must be preserved.
- Make v001 the immutable initialized baseline.
- Create a new version after a user-accepted revision cycle or before a risky transformation.
- Record the parent version. Never reuse a version number for materially different content.
- Keep filenames stable across versions where practical.
- Use names such as Manuscript_clean.docx and Manuscript_tracked.docx only when both are needed.
- Do not label a file final until the user accepts it. Prefer version numbers over final2 or latest.

## Source and data protection

- Copy sources; do not move them from user-controlled locations.
- Record source filename, origin, date received, role, and notes in SOURCE_MANIFEST.md.
- Preserve raw data byte-for-byte. If standardization changes representation, keep the original and place transformed data in a clearly named processed location.
- Document transformations in scripts and change-notes.md.
- Never delete uncertain duplicates automatically. Archive and report them.

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

Record version, parent version, date, scope, input files, source snapshot status, Stage 0 through Stage 4 status, user approvals, validation methods, deliverables, unresolved queries, known limitations, and next action.

## Change notes

For each material change, record artifact or location, category, rationale, whether scientific meaning changed, supporting user decision or source, affected figures or citations, and validation.

Summarize trivial grammar changes. Log every change that affects interpretation, data presentation, methods, claims, structure, or submission compliance.

## Clean-delivery checks

- Required folders and files exist or are marked not applicable.
- DOCX files open and render without corruption.
- Figures open at expected dimensions and resolution; SVG files contain real vector content where claimed.
- Plotting scripts are paired with documented inputs and do not alter raw data.
- Figure, table, equation, section, and citation numbering agree.
- No TODO, FIXME, placeholder citation, unresolved comment, hidden text, or accidental tracked change remains unless listed.
- Journal-specific claims are supported by current official instructions or labeled provisional.
- Inventory, iteration checklist, and change notes match actual files.
