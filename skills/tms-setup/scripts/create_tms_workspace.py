#!/usr/bin/env python3
"""Create a generic TMS OS starter workspace.

The script is intentionally conservative. It creates the standard folder and
file skeleton but does not invent school, course, roster, policy, or schedule
details. Existing files are preserved unless --force is supplied.
"""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path


FOLDERS = [
    "00_Start_Here",
    "01_School_Context",
    "02_Master_Curriculum",
    "03_Classes_And_Periods",
    "04_Units",
    "05_Teacher_Profile",
    "06_Class_Memory",
    "07_Artifact_Templates",
    "08_Student_Artifacts",
    "source_docs/teacher_uploads",
    "outputs",
]


def write(path: Path, content: str, force: bool = False) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return False
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    return True


def write_csv(path: Path, rows: list[list[str]], force: bool = False) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return False
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a TMS OS starter workspace.")
    parser.add_argument("target", nargs="?", default=".", help="Target folder to initialize")
    parser.add_argument("--force", action="store_true", help="Overwrite existing starter files")
    args = parser.parse_args()

    root = Path(args.target).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        (root / folder).mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()
    created: list[str] = []

    files: dict[str, str] = {
        "README.md": f"""# TMS OS

Local Teaching Management System workspace.

Status: starter workspace
Created: {today}

## Operating Model

- Codex chat is the control layer.
- Project files are the source of truth.
- Generated HTML workspaces are temporary present/print/edit shells.
- Student-facing collection records must live in approved durable systems.
- Missing inputs are marked as `Needed` instead of guessed.

## Start Here

1. Read `00_Start_Here/README.md`.
2. Update `00_Start_Here/setup_status.md` during setup.
3. Add uploaded documents to `source_docs/teacher_uploads/`.
4. Keep `source_docs/source_index.md` current.
5. Generate daily workspaces into `outputs/`.
""",
        "00_Start_Here/README.md": """# Start Here

This is the front door for the local TMS OS workspace.

## First Setup Path

1. Identify school, grade band, subject, and course.
2. Add one class period or section.
3. Upload the syllabus, curriculum map, pacing guide, calendar, schedule, and rubrics when available.
4. Define teacher defaults.
5. Define student-data boundaries.
6. Generate one daily workspace to prove the setup works.

## Default Command

Ask Codex:

```text
Use $tms-setup to continue setup.
```

After setup, keep using the same skill:

```text
Use $tms-setup to plan tomorrow.
Use $tms-setup to make an exit ticket.
Use $tms-setup to log what happened today.
```
""",
        "00_Start_Here/setup_status.md": """# Setup Status

## Current Status

Starter workspace created.

## Confirmed

- Teacher: Needed
- School: Needed
- Grade band: Needed
- Course or subject: Needed
- Period schedule: Needed
- Source documents: Needed
- Student-data boundary: Needed

## Next Step

Ask the teacher for school, grade band, and the first course or period to set up.
""",
        "01_School_Context/school_profile.md": """# School Profile

## Confirmed Context

| Field | Value | Source |
| --- | --- | --- |
| School | Needed | Needed |
| District | Needed | Needed |
| Grade band | Needed | Needed |
| Schedule type | Needed | Needed |
| Bell schedule source | Needed | Needed |
| Calendar source | Needed | Needed |

## Notes

Do not add school-specific claims without a source.
""",
        "01_School_Context/source_claims_and_limits.md": """# Source Claims And Limits

## Source Rule

Every school-specific claim should trace to one of:

- Official school or district source.
- Teacher-uploaded document.
- Teacher-supplied statement.
- Public source explicitly checked during setup.

## Missing Means Needed

If a fact is unavailable, mark it as `Needed` instead of guessing.
""",
        "02_Master_Curriculum/course_index.md": """# Course Index

| Course | Grade/level | Source document | Current unit | Status |
| --- | --- | --- | --- | --- |
| Needed | Needed | Needed | Needed | Needed |
""",
        "04_Units/unit_index.md": """# Unit Index

| Course | Unit | Source | Status |
| --- | --- | --- | --- |
| Needed | Needed | Needed | Needed |
""",
        "05_Teacher_Profile/global_defaults.md": """# Global Teacher Defaults

Status: starter profile

## Planning Defaults

- Default period length: Needed
- Default lesson style: practical classroom-ready draft.
- Default source behavior: use available files first and mark missing context.
- Default clarification behavior: ask one short question when a missing detail would materially change output.

## Lesson Rhythm

Most lessons should include:

- Opening board.
- Do Now or entry routine.
- Objective or target.
- Agenda.
- Student task.
- Evidence check.
- Exit ticket or closure prompt.

## Output Defaults

- Projectable workspace when content should go on the board.
- Printable version when useful.
- Google Forms-ready spec when digital collection is requested and live Google access is not available.

## Safety Defaults

- Do not invent rosters, grades, accommodations, attendance, media-release status, or student-specific patterns.
- Keep student information de-identified unless an approved process is supplied.
""",
        "05_Teacher_Profile/course_profile_template.md": """# Course Profile Template

## Course

- Course name: Needed
- Grade/level: Needed
- Period length: Needed
- Official/source status: Needed

## Defaults

- Typical lesson rhythm: Needed
- Common artifact types: Needed
- Common evidence types: Needed
- Equipment/materials: Needed

## Missing Inputs

- Needed
""",
        "06_Class_Memory/class_timeline_template.md": """# Class Timeline Template

| Date | Lesson / focus | What happened | Evidence collected | Student pattern | Next move | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Needed | Needed | Needed | Needed | Needed | Needed | Needed |
""",
        "06_Class_Memory/missing_inputs_for_live_use.md": """# Missing Inputs For Live Use

The workspace can support planning before it has every live input. Missing context should be surfaced clearly.

## Required For Accurate Class Memory

| Input | Current status | Impact |
| --- | --- | --- |
| Period schedule | Missing | Cannot say where each real class period left off. |
| Roster or de-identified roster policy | Missing | Cannot summarize student-level patterns. |
| Gradebook export or gradebook policy | Missing | Cannot provide grade status or intervention groups. |
| Assignment list | Missing | Cannot connect evidence to real submissions. |
| Current class timeline | Missing | Cannot answer what happened last class from live history. |
| Student-data policy | Missing | Cannot process student-identifiable evidence. |
| Media-release process | Missing | Cannot safely generate public-facing publication instructions. |

## Safe Work That Can Continue Now

- Unit planning from uploaded documents.
- Opening boards, agendas, activities, and exit tickets.
- Teacher-only planning documents.
- Daily workspace artifacts without student-specific claims.
""",
        "07_Artifact_Templates/daily_workspace_template.md": """# Daily Workspace Template

## Metadata

- Prepared date:
- Class-use date:
- Course:
- Period:
- Unit/topic:
- Source mode:
- Missing context:

## Artifacts

1. Opening board
2. Student task
3. Exit ticket
4. Teacher run notes
""",
        "07_Artifact_Templates/opening_board.md": """# Opening Board Template

## Title

Needed

## Do Now

Needed

## Objective

Needed

## Agenda

1. Needed
2. Needed
3. Needed
""",
        "07_Artifact_Templates/exit_ticket.md": """# Exit Ticket Template

## Purpose

Needed

## Questions

1. Needed
2. Needed
3. Needed

## Teacher Look-For

Needed
""",
        "08_Student_Artifacts/student_artifact_delivery_spec.md": """# Student Artifact Delivery Spec

## Delivery Modes

- `print`: paper handout or response sheet.
- `digital_reference`: student-facing link with no response collection.
- `google_form_collect`: Google Form collects responses.
- `platform_collect`: future hosted platform collects responses.

## Rule

Collected student data is not temporary. Keep durable links and metadata here, and keep raw identifiable responses in approved systems.
""",
        "08_Student_Artifacts/google_forms_exit_ticket_template.md": """# Google Forms Exit Ticket Template

## Form

- Title: Needed
- Description: Needed
- Status: Planned
- Teacher edit link: Needed
- Student responder link: Needed
- Response Sheet link: Needed
- Data sensitivity: Needed

## Questions

| Order | Question | Type | Required | Teacher look-for |
| --- | --- | --- | --- | --- |
| 1 | Needed | Short answer | Yes | Needed |
""",
        "source_docs/source_index.md": """# Source Index

Add every uploaded or referenced source here.

| Local file | Source | Use | Status |
| --- | --- | --- | --- |
| Needed | Needed | Needed | Needed |

## Source Rule

Do not add school-specific or course-specific claims unless they trace to a source here, a teacher-supplied statement, or an explicitly verified public source.
""",
        "outputs/README.md": """# Outputs

Generated daily workspaces and readable snapshots go here.

Do not treat outputs as the source of truth. Important continuity should be written back into class memory or source files.
""",
    }

    for relative_path, content in files.items():
        if write(root / relative_path, content, args.force):
            created.append(relative_path)

    csv_rows = [
        [
            "period",
            "course",
            "section",
            "room",
            "meeting_pattern",
            "current_unit",
            "last_lesson",
            "evidence_source",
            "class_status",
            "needed_next_input",
        ],
        ["Needed", "Needed", "Needed", "Needed", "Needed", "Needed", "Needed", "Needed", "setup_needed", "teacher schedule"],
    ]
    if write_csv(root / "03_Classes_And_Periods/period_status_snapshot.csv", csv_rows, args.force):
        created.append("03_Classes_And_Periods/period_status_snapshot.csv")

    registry_rows = [
        [
            "artifact_id",
            "date",
            "course",
            "period",
            "artifact_type",
            "delivery_mode",
            "status",
            "student_link",
            "response_location",
            "data_sensitivity",
            "notes",
        ],
    ]
    if write_csv(root / "08_Student_Artifacts/student_artifact_registry.csv", registry_rows, args.force):
        created.append("08_Student_Artifacts/student_artifact_registry.csv")

    print(f"TMS workspace initialized at {root}")
    print(f"Created or updated {len(created)} files.")
    for path in created:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
