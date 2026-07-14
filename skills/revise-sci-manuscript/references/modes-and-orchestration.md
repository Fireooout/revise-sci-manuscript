# Modes and Orchestration

Use this reference to choose the interaction pattern, build the control artifacts, allocate available models, and decide when autonomous work must pause.

## Contents

- [Mode selection protocol](#mode-selection-protocol)
- [Gate matrix](#gate-matrix)
- [Assisted mode](#assisted-mode)
- [Command mode](#command-mode)
- [Unbounded mode](#unbounded-mode)
- [Build a model-routed execution plan](#build-a-model-routed-execution-plan)
- [Pause only for a real hard stop](#pause-only-for-a-real-hard-stop)
- [Keep approvals and plan changes explicit](#keep-approvals-and-plan-changes-explicit)

## Mode selection protocol

1. Honor an explicit mode request in Chinese or English.
2. Otherwise select `command` and state: “Using command mode by default; you may switch before approving the brief or plan.”
3. Record the selection in `control/mode-selection.md` with `explicit` or `defaulted`, the current version, and the next gate.
4. Do not ask a blocking mode question unless the user's instructions conflict with one another or would authorize materially different work.
5. Allow a mode switch only at a safe checkpoint: before substantive execution, after a stage has been validated, or after a candidate version has been sealed. Record the reason and which earlier approvals remain valid.

## Gate matrix

| Mode | Required before substantive execution | Routine execution interruptions | End of iteration |
|---|---|---|---|
| Assisted | Stage review and stage plan approval | Pause for user decisions and acceptance at every stage | User accepts the candidate or requests changes |
| Command | Confirmed project brief, then approved full execution plan | Continue across stages; pause only for a hard stop or material plan deviation | Deliver one sealed candidate for acceptance or replanning |
| Unbounded | Approved full execution plan | Continue through exactly one iteration; use conservative reversible assumptions when safe | Deliver one sealed candidate and ask whether to run another planned iteration |

## Assisted mode

Preserve the original author-led cycle:

1. Inventory and extract sources.
2. Present the intake report and resolve material missing information.
3. For each stage, produce findings before edits.
4. Ask the user for decisions, create or revise the stage plan, and obtain approval.
5. Execute only the approved stage plan, provide diffs and validation, and obtain acceptance.
6. Repeat within the open candidate until the user accepts the stage.
7. Seal the delivered candidate before opening a child version.

Use questions to surface author intent, not to offload routine analysis. Recommend a preferred option with reasons whenever a meaningful choice is required.

## Command mode

Use two pre-execution approval gates.

### Gate C1: Confirm the project brief

Perform a whole-project analysis first. Ask only for missing information that cannot be safely inferred and materially changes the scientific interpretation, scope, journal target, deliverables, confidentiality, or authorship constraints. Consolidate the result in `control/project-brief.md`:

- objective and success criteria;
- supplied materials and provenance gaps;
- target journal, article type, language, and formatting constraints;
- in-scope and out-of-scope work;
- non-negotiable scientific claims, terminology, data rules, and author judgments;
- AI recommendations and their rationale;
- assumptions the AI may use without further interruption;
- hard blockers and decisions reserved for the user;
- requested deliverables and iteration boundary.

Mark the brief `awaiting confirmation`. Do not create the final execution plan until the user confirms or edits the brief. Log confirmation in `decision-log.md`.

### Gate C2: Approve the full execution plan

After brief confirmation, create `control/execution-plan.md` for the entire iteration. Include every stage, task, dependency, difficulty, scientific risk, exact available model or runtime, reasoning level, specialist skill or tool, fallback, input, output, validation, and interruption condition. Explain model choices briefly and invite allocation changes.

Mark the plan `awaiting approval`. After approval, mark it `approved`, record the approval, and execute the complete plan without routine stage approval requests. Surface concise progress updates, but do not turn updates into hidden approval gates.

If execution must materially expand scope, change a scientific judgment, use an unapproved model without an approved fallback, or perform an irreversible action, pause and revise the plan.

## Unbounded mode

Use one pre-execution approval gate.

1. Analyze all available materials, workflow difficulty, dependencies, risks, and likely outputs.
2. Resolve optional gaps with explicit, conservative, reversible assumptions. Ask before planning only when a hard stop makes a safe plan impossible.
3. Create the full `execution-plan.md`, including exact model allocation and pre-approved fallback routing. Put key assumptions and user-editable judgments in the plan; keep `project-brief.md` as an AI-generated supporting summary and mark it `AI synthesized, not separately gated`.
4. Obtain plan confirmation. Treat user edits as the authoritative allocation and scope, subject to safety and availability checks.
5. Execute exactly one complete child-version iteration autonomously. Perform internal reviews, repairs, renders, and validation without requesting routine feedback.
6. Seal and deliver the candidate as `delivered-awaiting-user-decision`.
7. Ask whether to accept, stop, or run another iteration. For another iteration, open a new child version, re-analyze the latest candidate, generate a new plan, obtain confirmation, and repeat.

Do not continue into a second iteration merely because the mode is unbounded.

## Build a model-routed execution plan

Discover which models or deployments are actually available in the current environment when that capability exists. Do not hardcode a model catalog that may become stale and do not claim to have routed work to an unavailable model.

Use one task per row when a stage mixes difficulty levels. Include at least these columns:

| ID | Stage/task | Dependency | Difficulty | Scientific risk | Model/runtime | Reasoning | Specialist skill/tool | Fallback | Output | Validation | Pause condition | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Apply these allocation principles:

- Use the strongest available reasoning model for claim interpretation, cross-document reconciliation, experimental logic, high-risk reviewer responses, and final evidence-chain review.
- Use a balanced general model for ordinary language revision, structured drafting, caption work, and plan execution with moderate scientific risk.
- Use a lightweight model or deterministic script for inventory, file classification, format checks, manifest updates, and repetitive low-risk comparisons.
- Use vision-capable analysis for figure inspection and rendered-page quality control.
- Use code-capable execution plus deterministic tests for plotting, data transformations, document assembly, and validation scripts.
- Prefer the least costly model that safely satisfies the task, but never trade away scientific integrity or validation.
- Give every routed task a fallback. In unbounded mode, pre-approve fallbacks in the plan so temporary model unavailability does not create a routine interruption.

When the runtime exposes only one model, write its exact identifier if known or `current runtime model (single-model environment)` if not. Still allocate reasoning effort, specialist skills, deterministic scripts, and validation per task. Clearly label the plan as recommendations rather than pretending that separate model routing occurred.

If the user changes an allocation, check availability and task capability before execution. If the requested model is unavailable, propose the closest available substitute and update the plan before approval.

## Pause only for a real hard stop

The following conditions override every mode:

- required source files are corrupt, inaccessible, or cannot be copied safely;
- proceeding would require fabricating or guessing results, citations, methods, statistics, author statements, or journal requirements;
- an ambiguity could materially change scientific meaning and no conservative reversible treatment exists;
- raw data integrity, research ethics, authorship, confidentiality, legal rights, or human-subject protections are at risk;
- the requested action publishes, submits, messages a third party, deletes data, overwrites a sealed version, or otherwise creates an irreversible external effect without specific authorization;
- the approved plan is no longer executable and no approved fallback covers the deviation.

In command mode, pause with the minimum decision required and a recommended option. In unbounded mode, first try a documented conservative and reversible fallback; pause only if safe continuation is impossible.

Do not treat optional metadata, stylistic preferences, routine formatting choices, or low-risk reversible decisions as hard stops. Record assumptions and continue according to the mode.

## Keep approvals and plan changes explicit

Use these plan states: `draft`, `awaiting confirmation`, `awaiting approval`, `approved`, `executing`, `completed`, and `superseded`.

Record each approval with date, artifact, version, user instruction, and any conditions. After approval:

- update status rows as work proceeds;
- record actual model, fallback, or tool use when it differs;
- revise and re-approve the plan only for material scope, scientific, model-routing, or irreversible-action changes;
- keep the superseded plan or an auditable diff instead of silently rewriting history.
