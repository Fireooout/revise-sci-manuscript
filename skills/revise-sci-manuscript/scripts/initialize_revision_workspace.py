#!/usr/bin/env python3
"""Initialize a versioned SCI manuscript revision workspace without overwriting files."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

VERSION_RE = re.compile(r"v\d{3,}")
VERSION_DIRS = (
    "text_snapshot", "manuscript", "raw_data", "scripts",
    "figures", "reviews", "working",
)


def write_new(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a protected, versioned SCI manuscript revision workspace."
    )
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--project-name", default=None)
    parser.add_argument("--version", default="v001")
    parser.add_argument("--parent", default=None)
    return parser.parse_args()


def validate_version(value: str, label: str) -> None:
    if not VERSION_RE.fullmatch(value):
        raise SystemExit(f"{label} must match vNNN, for example v001: {value!r}")


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
    version_dir = root / "versions" / args.version

    if version_dir.exists() and any(version_dir.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty version directory: {version_dir}")

    source_dir.mkdir(parents=True, exist_ok=True)
    version_dir.mkdir(parents=True, exist_ok=True)
    for name in VERSION_DIRS:
        (version_dir / name).mkdir(exist_ok=True)

    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    state_path = root / "project-state.json"
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            raise SystemExit(f"Cannot safely read existing {state_path}: {exc}") from exc
    else:
        state = {"project_name": project_name, "created_at": now, "versions": []}

    versions = state.setdefault("versions", [])
    if args.version not in versions:
        versions.append(args.version)
    state["current_version"] = args.version
    state["updated_at"] = now
    state_path.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    write_new(
        source_dir / "SOURCE_MANIFEST.md",
        "# Source Manifest\n\n"
        "| Source file | Origin | Date received | Role | Immutable copy verified | Notes |\n"
        "|---|---|---|---|---|---|\n",
    )
    write_new(
        version_dir / "reviews" / "intake-checklist.md",
        "# Intake Checklist\n\n"
        f"- Project: {project_name}\n"
        f"- Version: {args.version}\n"
        "- Target journal/article type: \n"
        "- Supplied materials: \n"
        "- Missing or unreadable materials: \n"
        "- Assumptions and risks: \n"
        "- Requested stages: \n"
        "- Required user decisions: \n",
    )
    write_new(
        version_dir / "iteration-checklist.md",
        "# Iteration Checklist\n\n"
        f"- Version: {args.version}\n"
        f"- Parent version: {args.parent or 'none (initial baseline)'}\n"
        f"- Initialized: {now}\n"
        "- Stage 0 - intake and initialization: pending\n"
        "- Stage 1 - foundational language revision: pending\n"
        "- Stage 2 - scientific figure optimization: pending\n"
        "- Stage 3 - final manuscript integration: pending\n"
        "- Stage 4 - versioned delivery: pending\n"
        "- User approvals: \n"
        "- Validation performed: \n"
        "- Unresolved items: \n"
        "- Next action: \n",
    )
    write_new(
        version_dir / "change-notes.md",
        "# Change Notes\n\n"
        f"- Version: {args.version}\n"
        f"- Parent version: {args.parent or 'none'}\n\n"
        "| Artifact/location | Category | Rationale | Meaning affected? | Validation |\n"
        "|---|---|---|---|---|\n",
    )
    write_new(
        version_dir / "status.md",
        "# Project Status\n\n"
        f"- Project: {project_name}\n"
        f"- Current version: {args.version}\n"
        "- Current stage: Stage 0 - intake and initialization\n"
        "- State: awaiting source inventory and user confirmation\n"
        f"- Last updated: {now}\n",
    )

    print(f"Initialized {project_name} at {root}")
    print(f"Created version {args.version} at {version_dir}")
    print("Copy original source files into source_materials without modification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
