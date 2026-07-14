#!/usr/bin/env python3
"""Initialize a mode-aware, versioned SCI manuscript revision workspace."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

VERSION_RE = re.compile(r"v\d{3,}")
MODES = ("assisted", "command", "unbounded")
VERSION_DIRS = (
    "control",
    "text_snapshot",
    "manuscript",
    "raw_data",
    "scripts",
    "figures",
    "reviews",
    "working",
)

MODE_LABELS = {
    "assisted": "Assisted mode (辅助模式)",
    "command": "Command mode (指挥模式, default)",
    "unbounded": "Unbounded mode (无界模式)",
}

MODE_GATES = {
    "assisted": "stage review, stage-plan approval, and stage acceptance",
    "command": "project-brief confirmation followed by full execution-plan approval",
    "unbounded": "full execution-plan approval for exactly one autonomous iteration",
}


def write_new(path: Path, content: str) -> None:
    """Create a UTF-8 text file only when it does not already exist."""
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def write_json_atomic(path: Path, value: dict) -> None:
    """Replace project state atomically after writing a valid temporary file."""
    temporary = path.with_name(f"{path.name}.tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a protected, mode-aware, versioned SCI manuscript revision "
            "workspace without overwriting a non-empty version."
        )
    )
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--project-name", default=None)
    parser.add_argument("--version", default="v001")
    parser.add_argument("--parent", default=None)
    parser.add_argument(
        "--mode",
        choices=MODES,
        default="command",
        help="Interaction mode; defaults to command.",
    )
    parser.add_argument(
        "--mode-source",
        choices=("explicit", "defaulted"),
        default=None,
        help="Whether the user selected the mode or the command default was used.",
    )
    return parser.parse_args()


def validate_version(value: str, label: str) -> None:
    if not VERSION_RE.fullmatch(value):
        raise SystemExit(f"{label} must match vNNN, for example v001: {value!r}")


def detect_mode_source(args: argparse.Namespace) -> str:
    if args.mode_source:
        return args.mode_source
    mode_was_passed = any(
        value == "--mode" or value.startswith("--mode=") for value in sys.argv[1:]
    )
    return "explicit" if mode_was_passed else "defaulted"


def load_state(path: Path, project_name: str, now: str) -> dict:
    if not path.exists():
        return {
            "project_name": project_name,
            "created_at": now,
            "versions": [],
            "version_metadata": {},
            "mode_history": [],
        }
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise SystemExit(f"Cannot safely read existing {path}: {exc}") from exc
    if not isinstance(state, dict):
        raise SystemExit(f"Cannot safely use non-object project state: {path}")
    return state


def main() -> int:
    args = parse_args()
    validate_version(args.version, "--version")
    if args.parent:
        validate_version(args.parent, "--parent")
        if args.parent == args.version:
            raise SystemExit("--parent must differ from --version")

    root = args.project_root.expanduser().resolve()
    project_name = args.project_name or root.name
    source_dir = root / "source_materials"
    versions_root = root / "versions"
    version_dir = versions_root / args.version
    mode_source = detect_mode_source(args)

    if args.parent and not (versions_root / args.parent).is_dir():
        raise SystemExit(
            f"Parent version does not exist: {versions_root / args.parent}. "
            "Create and seal the parent before opening a child candidate."
        )
    if version_dir.exists() and any(version_dir.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty version directory: {version_dir}")

    source_dir.mkdir(parents=True, exist_ok=True)
    version_dir.mkdir(parents=True, exist_ok=True)
    for name in VERSION_DIRS:
        (version_dir / name).mkdir(exist_ok=True)

    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    lifecycle_state = "open-candidate" if args.parent else "open-baseline"
    state_path = root / "project-state.json"
    state = load_state(state_path, project_name, now)

    versions = state.setdefault("versions", [])
    if args.version not in versions:
        versions.append(args.version)
    version_metadata = state.setdefault("version_metadata", {})
    version_metadata[args.version] = {
        "parent": args.parent,
        "mode": args.mode,
        "mode_source": mode_source,
        "lifecycle_state": lifecycle_state,
        "initialized_at": now,
    }
    mode_history = state.setdefault("mode_history", [])
    mode_history.append(
        {
            "version": args.version,
            "mode": args.mode,
            "source": mode_source,
            "recorded_at": now,
        }
    )
    state["project_name"] = state.get("project_name") or project_name
    state["current_version"] = args.version
    state["current_mode"] = args.mode
    state["current_lifecycle_state"] = lifecycle_state
    state["updated_at"] = now
    write_json_atomic(state_path, state)

    write_new(
        source_dir / "SOURCE_MANIFEST.md",
        "# Source Manifest\n\n"
        "| Source file | Origin | Date received | Role | Immutable copy verified | Notes |\n"
        "|---|---|---|---|---|---|\n",
    )

    control = version_dir / "control"
    write_new(
        control / "mode-selection.md",
        "# Mode Selection\n\n"
        f"- Version: {args.version}\n"
        f"- Parent version: {args.parent or 'none (initial baseline)'}\n"
        f"- Mode: {MODE_LABELS[args.mode]}\n"
        f"- Selection source: {mode_source}\n"
        f"- Gate policy: {MODE_GATES[args.mode]}\n"
        "- Current gate: intake and source protection\n"
        f"- Recorded: {now}\n\n"
        "## Mode switch history\n\n"
        "| Date | From | To | Safe checkpoint | Reason | Earlier approvals retained |\n"
        "|---|---|---|---|---|---|\n",
    )
    write_new(
        control / "project-brief.md",
        "# Project Brief\n\n"
        f"- Version: {args.version}\n"
        f"- Parent version: {args.parent or 'none (initial baseline)'}\n"
        f"- Mode: {args.mode}\n"
        "- Status: draft\n"
        "- Confirmation: pending or not separately gated\n\n"
        "## Objective and success criteria\n\n"
        "## Evidence and supplied materials\n\n"
        "## Target journal and article type\n\n"
        "## Scope and exclusions\n\n"
        "## Scientific and terminology invariants\n\n"
        "## Key user judgments\n\n"
        "## AI recommendations and rationale\n\n"
        "## Approved assumptions\n\n"
        "## Risks, hard blockers, and reserved decisions\n\n"
        "## Deliverables and iteration boundary\n",
    )
    write_new(
        control / "execution-plan.md",
        "# Full Execution Plan\n\n"
        f"- Version: {args.version}\n"
        f"- Parent version: {args.parent or 'none (initial baseline)'}\n"
        f"- Mode: {args.mode}\n"
        "- Plan revision: 1\n"
        "- Status: draft\n"
        "- Approval: pending\n"
        "- Available model/deployment inventory: pending discovery\n"
        "- Single-model runtime limitation, if any: pending\n\n"
        "| ID | Stage/task | Dependency | Difficulty | Scientific risk | Model/runtime | Reasoning | Specialist skill/tool | Fallback | Output | Validation | Pause condition | Status |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|\n\n"
        "## Model allocation rationale and user modifications\n\n"
        "## Approval record\n",
    )
    write_new(
        control / "decision-log.md",
        "# Decision Log\n\n"
        "Append entries; do not silently rewrite prior decisions.\n\n"
        "| Date | Version | Actor | Decision or assumption | Rationale/source | Affected plan tasks | Status |\n"
        "|---|---|---|---|---|---|---|\n"
        f"| {now} | {args.version} | AI | Initialized {args.mode} mode ({mode_source}) | Workspace initialization | Stage 0 | active |\n",
    )
    write_new(
        control / "context-summary.md",
        "# Compact Context Summary\n\n"
        f"- Project: {project_name}\n"
        f"- Active version: {args.version}\n"
        f"- Parent: {args.parent or 'none (initial baseline)'}\n"
        f"- Lifecycle state: {lifecycle_state}\n"
        f"- Mode: {args.mode}\n"
        "- Current gate: intake and source protection\n"
        "- Approved scope: pending\n"
        "- Plan revision/status: 1 / draft\n"
        f"- Last updated: {now}\n\n"
        "## Immutable constraints\n\n"
        "## Key decisions and authoritative pointers\n\n"
        "## Completed outputs and validation\n\n"
        "## Open risks or hard blockers\n\n"
        "## Exact next action and required files\n",
    )

    write_new(
        version_dir / "reviews" / "intake-checklist.md",
        "# Intake Checklist\n\n"
        f"- Project: {project_name}\n"
        f"- Version: {args.version}\n"
        f"- Parent version: {args.parent or 'none (initial baseline)'}\n"
        f"- Mode: {args.mode}\n"
        "- Target journal/article type: \n"
        "- Supplied materials: \n"
        "- Missing or unreadable materials: \n"
        "- Assumptions and risks: \n"
        "- Requested stages: \n"
        "- Required user decisions under this mode: \n",
    )
    write_new(
        version_dir / "iteration-checklist.md",
        "# Iteration Checklist\n\n"
        f"- Version: {args.version}\n"
        f"- Parent version: {args.parent or 'none (initial baseline)'}\n"
        f"- Lifecycle state: {lifecycle_state}\n"
        f"- Mode: {args.mode}\n"
        f"- Initialized: {now}\n"
        "- Baseline seal status: pending\n"
        "- Project brief status: draft\n"
        "- Execution plan revision/status: 1 / draft\n"
        "- Stage 0 - intake, baseline, and iteration setup: pending\n"
        "- Stage 1 - foundational language revision: pending\n"
        "- Stage 2 - scientific figure optimization: pending\n"
        "- Stage 3 - final manuscript integration: pending\n"
        "- Stage 4 - verification, sealing, and delivery: pending\n"
        "- Required user approvals: \n"
        "- Planned and actual model routing: \n"
        "- Validation performed: \n"
        "- Context summary freshness: initialized\n"
        "- Unresolved items: \n"
        "- Next action: \n",
    )
    write_new(
        version_dir / "change-notes.md",
        "# Change Notes\n\n"
        f"- Version: {args.version}\n"
        f"- Parent version: {args.parent or 'none'}\n"
        f"- Mode: {args.mode}\n\n"
        "| Artifact/location | Category | Rationale | Meaning affected? | Model/tool | Validation |\n"
        "|---|---|---|---|---|---|\n",
    )
    write_new(
        version_dir / "status.md",
        "# Project Status\n\n"
        f"- Project: {project_name}\n"
        f"- Current version: {args.version}\n"
        f"- Parent version: {args.parent or 'none (initial baseline)'}\n"
        f"- Lifecycle state: {lifecycle_state}\n"
        f"- Mode: {args.mode}\n"
        "- Current stage: Stage 0 - intake, baseline, and iteration setup\n"
        "- Current gate: intake and source protection\n"
        "- State: awaiting source inventory and control-artifact preparation\n"
        f"- Last updated: {now}\n",
    )

    print(f"Initialized {project_name} at {root}")
    print(f"Created {lifecycle_state} {args.version} at {version_dir}")
    print(f"Selected {MODE_LABELS[args.mode]} ({mode_source})")
    if args.parent:
        print("Copy required parent artifacts into this child; never edit the parent version.")
    else:
        print("Copy original files into source_materials, verify snapshots, and seal the baseline before editing.")
    print(f"Next approval policy: {MODE_GATES[args.mode]}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
