#!/usr/bin/env python3
"""Create a generic TMS OS starter workspace.

The script is intentionally conservative. It creates the standard folder and
file skeleton but does not invent school, course, roster, policy, schedule,
Google Forms links, or student-data details. Existing files are preserved unless
--force is supplied.
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
    "skills/tms-os-daily-workspace",
    "skills/tms-os-workspace-renderer",
    "skills/tms-os-student-artifact-delivery",
    "skills/tms-os-revise-workspace",
    "skills/tms-os-after-class-logger",
    "skills/tms-os-class-setup",
    "skills/tms-os-source-refresh",
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


DAILY_WORKSPACE_SKILL = '''---
name: tms-os-daily-workspace
description: Generate Codex-native daily workspace artifacts for TMS OS. Use when the teacher asks to plan tomorrow, make an opening board, generate an exit ticket, build classroom slides, create a handout, or produce a presentable/printable classroom resource from TMS OS project context.
---

# TMS OS Daily Workspace

## Purpose

Use Codex chat as the control layer and project files as the source of truth. Generate presentable, printable, or student-deliverable classroom artifacts only when useful.

The generated UI is temporary. It does not own teaching memory. It renders, edits, presents, prints, and returns artifact snapshots back to the project.

Collected student responses are not temporary. If a generated artifact collects student data, use durable Google Drive/Forms/Sheets storage or a teacher-approved project evidence path, and save only metadata or teacher-approved summaries in TMS OS by default.

## Non-Negotiable Default

For planning and classroom-material prompts, generate the daily workspace UI first.

If the teacher says "plan tomorrow," "plan next class," "make tomorrow's lesson," "make something for the board," "make the activity," "make an exit ticket," or "give me slides," do not respond with only a Markdown lesson. Create the workspace files in `outputs/`, then open or link the HTML workspace for review.

## Source Order

Read only what is needed:

1. `00_Start_Here/codex_native_daily_workspace_spec.md`
2. `05_Teacher_Profile/global_defaults.md`
3. `source_docs/source_index.md`
4. `02_Master_Curriculum/course_index.md`
5. `03_Classes_And_Periods/period_status_snapshot.csv`
6. `06_Class_Memory/*timeline*.md` when real timeline files exist
7. `06_Class_Memory/missing_inputs_for_live_use.md` when live class context is missing
8. `07_Artifact_Templates/` for artifact shape
9. `08_Student_Artifacts/` when an artifact is student-facing or collects responses

## Default Behavior

1. Check relevant context automatically.
2. Generate the most informed draft possible.
3. Ask one short clarifying question only when a missing detail would materially change the output.
4. Mark missing context without turning it into a blocker.
5. Determine whether student-facing artifacts are `print`, `digital_reference`, `google_form_collect`, or `platform_collect`.
6. Write an interactive daily workspace HTML file to `outputs/`.
7. Write an adjacent readable Markdown snapshot to `outputs/`.
8. For collected student artifacts, create a durable registry/spec entry under `08_Student_Artifacts/`.
9. If the mode is `google_form_collect` and authenticated Google access is available, create the live Google Form and linked response Sheet, then write the edit/responder/sheet links back to the workspace, snapshot, registry, and artifact spec.
10. If live Google Form creation is unavailable, leave a Forms-ready spec and mark the artifact clearly as not created.

## Output Rules

Default full daily plan artifacts:

- Opening board.
- Student task or activity directions.
- Exit ticket.
- Teacher run notes when useful.

Required HTML UI features:

- Split layout with artifact navigation.
- Workspace metadata: course, period if known, date, unit/topic, source mode, missing-context note.
- Present, print, edit text, and revision/request-change controls.
- Student controls when relevant: open Google Form, copy LMS link, open responses.
- Print CSS.

## Write-Back Rules

Save the HTML workspace and Markdown snapshot to `outputs/` immediately for planning/material generation prompts. These files are the review draft.

For student-facing artifacts that collect responses, save durable metadata in `08_Student_Artifacts/`. The daily workspace can point to the collection surface, but it should not be the only record of a collected-data artifact.

After class, save continuity to `06_Class_Memory/` only when the teacher asks to log, update, save, or carry forward what happened.

Do not save student-specific evidence unless an approved de-identification and data-use process has been supplied.
'''


WORKSPACE_RENDERER_SKILL = '''---
name: tms-os-workspace-renderer
description: Render TMS OS lesson/activity content into the standard interactive daily workspace HTML plus readable snapshot with split navigation, metadata, present/print/edit controls, and project-safe write-back.
---

# TMS OS Workspace Renderer

## Purpose

Render classroom content into the TMS OS daily workspace UI.

This skill owns the output shell. It does not decide curriculum scope or class evidence.

## Required Inputs

Before rendering, identify:

- Class-use date.
- Course.
- Period, if known.
- Unit or topic.
- Source mode.
- Missing-context notes.
- Artifact list.
- Student artifact delivery mode and link/status metadata, when relevant.

## Output Files

Write both files immediately:

- `outputs/daily-workspace-YYYY-MM-DD-<short-topic>.html`
- `outputs/daily-workspace-YYYY-MM-DD-<short-topic>-snapshot.md`

## Required HTML Features

- Standalone local HTML with no external network assets.
- Split layout with artifact navigation.
- Workspace metadata.
- Present control.
- Print control.
- Edit text control.
- Revision/request-change note.
- Student-facing link controls when relevant, such as `Open Google Form`, `Copy LMS Link`, and `Open Responses`.
- Print CSS.
- Responsive layout for small screens.

## Snapshot Requirements

The Markdown snapshot must include artifact text, source mode, missing context, class-use date, workspace path, student artifact delivery mode, durable storage link/status, collection settings, and data sensitivity label when an artifact collects responses.

Do not place raw identifiable student responses in a daily workspace snapshot unless the teacher explicitly supplied an approved storage and data-use process.
'''


STUDENT_ARTIFACT_SKILL = '''---
name: tms-os-student-artifact-delivery
description: Prepare student-facing TMS OS artifacts for print, digital reference, Google Forms collection, or future platform collection while preserving durable records for any collected student data.
---

# TMS OS Student Artifact Delivery

## Purpose

Turn generated classroom content into a student-facing delivery plan.

Use this when the teacher asks for a Google Form exit ticket, digital exit ticket, short quiz, formative assessment, vocab check, student reflection, LMS link, or student-facing artifact that collects responses.

## Core Rule

Temporary UI is allowed.

Collected student data is not temporary.

If an artifact collects responses, store durable metadata under `08_Student_Artifacts/` and keep raw identifiable responses in Google Forms, Google Sheets, or another approved storage location unless the teacher explicitly supplies a compliant project storage process.

## Delivery Modes

- `print`: printable handout or paper response.
- `digital_reference`: student-facing link with no response collection.
- `google_form_collect`: Google Form collects responses.
- `platform_collect`: future hosted platform collects responses.

## Google Forms Exit Ticket Requirements

- Form title.
- Form description.
- Question list.
- Recommended question types.
- Collection settings.
- Teacher edit link slot.
- Student responder link slot for LMS posting.
- Response sheet/location slot.
- Data sensitivity label.
- Status.

## Automatic Live Google Form Creation

When the artifact mode is `google_form_collect`, create the live Google Form automatically if a direct Forms API path or authenticated Chrome access is available.

If no direct Forms API tool is available, use the `Chrome` plugin.

Chrome creation flow:

1. Read the current artifact spec.
2. Open `https://forms.new` in Chrome.
3. Create the title and description.
4. Add the required questions and question types.
5. Apply allowed settings only.
6. Capture the teacher edit URL.
7. Capture the student responder URL.
8. Link responses to a Google Sheet when possible and capture the Sheet URL.
9. Update the daily workspace, snapshot, registry, and artifact spec.
10. Keep the completed form tab open for teacher review.

Do not mark an artifact as `created` until real Google Form links have been captured.

## Registry Rule

Create or update `08_Student_Artifacts/student_artifact_registry.csv` whenever a student-facing artifact collects data.

Do not paste raw student responses into the registry.
'''


REVISE_WORKSPACE_SKILL = '''---
name: tms-os-revise-workspace
description: Revise an existing TMS OS daily workspace HTML and snapshot when the teacher asks to change, shorten, expand, add artifacts, adjust level, or make a workspace more projectable/printable.
---

# TMS OS Revise Workspace

## Purpose

Modify an existing generated daily workspace without starting over.

## Target Selection

Use the explicitly provided HTML/snapshot path when available. If no path is provided, find the newest `outputs/daily-workspace-*.html` and matching snapshot.

## Revision Rules

Preserve source mode, missing-context notes, artifact navigation, present/print/edit controls, student artifact durable links, and collection metadata.

Update both the HTML workspace and Markdown snapshot.

## Common Revision Patterns

- "Shorter": reduce teacher prose, preserve student-facing steps.
- "More printable": add or refine a handout artifact and print CSS.
- "Make it a Google Form": create the live Google Form and linked response Sheet when authenticated Google access is available; otherwise add Google Forms-ready metadata, link slots, printable fallback, and a durable registry/spec entry.
'''


AFTER_CLASS_SKILL = '''---
name: tms-os-after-class-logger
description: Log what happened after a TMS OS class, update class timeline memory, preserve evidence/next-move continuity, and prepare tomorrow planning context without inventing student or grade details.
---

# TMS OS After-Class Logger

## Purpose

Turn a teacher's after-class note into durable class memory that tomorrow planning can use.

## Core Rule

Only write class memory when the teacher asks to log, save, update, or carry forward what happened.

If Google Forms or Sheets responses exist, summarize only with teacher approval and follow the current data-use rules. Prefer aggregate patterns, completion counts, misconceptions, and next instructional move over raw identifiable responses.

## Write Targets

Preferred timeline path once period is known:

`06_Class_Memory/period-<period>-<course-slug>-timeline.md`

If no period is known but the teacher explicitly asks to save anyway, use:

`06_Class_Memory/unassigned-<course-slug>-timeline.md`

## Timeline Entry Shape

| Date | Lesson / production focus | What happened | Evidence collected | Student pattern | Next move | Source |
| --- | --- | --- | --- | --- | --- | --- |
'''


CLASS_SETUP_SKILL = '''---
name: tms-os-class-setup
description: Set up real TMS OS class sections, period mappings, course profiles, and timeline files from teacher-supplied schedule/context without fabricating rosters, grades, or policies.
---

# TMS OS Class Setup

## Purpose

Convert the TMS OS source-backed course shells into usable class sections.

## Setup Discipline

Ask at most one short question at a time when a setup detail is missing.

Do not invent period number, meeting pattern, room, roster, student count, gradebook policy, intervention/watchlist policy, media-release policy, or AI/data-use policy.

## Write Targets

Update `03_Classes_And_Periods/period_status_snapshot.csv`.

Create as needed:

- `05_Teacher_Profile/course_profile_<course-slug>.md`
- `06_Class_Memory/period-<period>-<course-slug>-timeline.md`
'''


SOURCE_REFRESH_SKILL = '''---
name: tms-os-source-refresh
description: Check, refresh, or audit TMS OS source materials, source index entries, calendar/schedule references, and curriculum/source alignment before planning or demos.
---

# TMS OS Source Refresh

## Purpose

Keep the TMS OS source layer trustworthy.

Use official or teacher-supplied sources first. Calendar, schedule, policy, and course-link claims are date-sensitive. Verify against official pages when asked for a current refresh.

## Modes

### Report-Only

Output what was checked, what still appears usable, what is stale or uncertain, and planning consequences. Do not edit files.

### Refresh And Save

Fetch or open only official/teacher-approved source URLs, save updated local copies into `source_docs/`, and update `source_docs/source_index.md` for changed files or new source facts.
'''


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
6. Use `08_Student_Artifacts/` for durable metadata when students submit responses.
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

After setup:

```text
Use $tms-setup to plan tomorrow.
Use $tms-setup to make an exit ticket.
Use $tms-setup to analyze exit ticket responses.
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
- Google access for live Forms: Needed

## Next Step

Ask the teacher for school, grade band, and the first course or period to set up.
""",
        "00_Start_Here/codex_native_daily_workspace_spec.md": """# TMS OS Codex-Native Daily Workspace Spec

## Core Direction

TMS OS behaves like a source-backed teacher copilot and lesson factory inside Codex.

The teacher gives direction in Codex chat. Codex reads project files, checks available teaching context, generates the most informed draft it can, and produces classroom-ready artifacts when useful.

Generated UI is temporary. Student-facing artifacts that collect responses are not temporary. Collected student evidence must live in Google Drive, Google Forms, Google Sheets, or another teacher-approved durable storage layer.

## Desired Default Behavior

For prompts like `plan tomorrow`, `make the board`, `make the activity`, `make an exit ticket`, or `give me slides`, Codex should create a daily workspace HTML file plus a readable snapshot in `outputs/`.

Do not answer these requests with only a Markdown lesson unless the teacher explicitly asks for text-only output.

## Student Artifact Modes

- `print`: paper handout or response sheet.
- `digital_reference`: student-facing link with no data collection.
- `google_form_collect`: Google Form responder link for exit tickets, checks for understanding, reflections, vocab checks, and short quizzes.
- `platform_collect`: future hosted student activity that collects responses directly.

## Google Forms Exit Ticket Pattern

When the teacher wants digital collection:

1. Generate questions in the daily workspace.
2. Include a printable fallback.
3. Create the live Google Form through a Forms API path or through Chrome with the teacher's signed-in Google account when available.
4. Link responses to a Google Sheet when possible.
5. Save teacher edit link, student responder link, response location, collection settings, and data sensitivity in the workspace, snapshot, registry, and artifact spec.
6. Treat raw responses as durable student evidence, not temporary output.

If Google Forms creation is unavailable, generate the Forms-ready spec and registry placeholder instead of pretending the live form exists.
""",
        "01_School_Context/school_profile.md": """# School Profile

| Field | Value | Source |
| --- | --- | --- |
| School | Needed | Needed |
| District | Needed | Needed |
| Grade band | Needed | Needed |
| Schedule type | Needed | Needed |
| Bell schedule source | Needed | Needed |
| Calendar source | Needed | Needed |

Do not add school-specific claims without a source.
""",
        "01_School_Context/source_claims_and_limits.md": """# Source Claims And Limits

Every school-specific claim should trace to one of:

- Official school or district source.
- Teacher-uploaded document.
- Teacher-supplied statement.
- Public source explicitly checked during setup.

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
- Live Google Form exit ticket when digital response collection is desired and Google access is available.

## Output Defaults

- Projectable workspace when content should go on the board.
- Printable version when useful.
- Generate the live Google Form, LMS responder link, and linked response Sheet when the teacher wants an exit ticket, quiz, reflection, or formative check collected digitally and Chrome or a Google Forms API path is available.
- Fall back to Google Forms-ready metadata only when live Google Form creation is unavailable in the current session.

## Safety Defaults

- Do not invent rosters, grades, accommodations, attendance, media-release status, or student-specific patterns.
- Keep student information de-identified unless an approved process is supplied.
- Do not treat collected student responses as temporary output.
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
| Student-data policy | Missing | Cannot process student-identifiable evidence beyond aggregate summaries. |
| Google Forms/Drive collection setup | Missing | Cannot automatically create account-linked exit tickets or store responder links until authenticated access is available. |
| Media-release process | Missing | Cannot safely generate public-facing publication instructions. |

## Safe Work That Can Continue Now

- Unit planning from uploaded documents.
- Opening boards, agendas, activities, and exit tickets.
- Teacher-only planning documents.
- Daily workspace artifacts without student-specific claims.
- Google Forms-ready specs and registry placeholders.
""",
        "07_Artifact_Templates/daily_workspace_template.md": """# Daily Workspace Template

Use this shape when Codex generates a classroom-ready UI artifact.

## Trigger Rule

Use this template immediately for planning and classroom-material prompts, including `plan tomorrow`, `make an activity`, `make an exit ticket`, and `give me slides`.

The generated UI is the primary draft. A plain Markdown lesson in chat is not the primary output unless the teacher explicitly asks for text only.

## Workspace Metadata

- Course.
- Period, if known.
- Date.
- Unit/topic.
- Source mode.
- Missing context notes.
- Student artifact delivery mode, when relevant.
- Student artifact durable record link or status, when relevant.

## Minimum UI Controls

- Present.
- Print.
- Edit text.
- Revision/request-change note.
- Copy student link, when a student-facing digital artifact exists.
- Open Google Form, when a Google Form artifact exists.
- Open Responses, when a response Sheet exists.

## Student Data Rule

Daily workspace HTML can be temporary. Collected student responses are not temporary.

For Google Forms exit tickets, include link slots for teacher edit link, student responder link for the LMS, response location, collection settings, and data sensitivity label.
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

Use this when the teacher asks for an exit ticket, closure, quick check, reflection, evidence check, or next-class readiness check.

## Required Fields

- Prompt title.
- Student-facing directions.
- 2 to 4 questions or tasks.
- What the teacher should look for.
- How the response informs the next class.

## Output Modes

- Projectable version for board display.
- Print-friendly version when students need a physical response sheet.
- Google Forms-ready or live Google Form version when responses should be collected digitally.

## Google Forms Mode

When collected digitally, generate form title, description, questions with recommended types, collection setting recommendation, data sensitivity label, teacher edit link slot, student responder link slot, and response location slot.

If the Google Form has not been created yet, label the status clearly and preserve the printable fallback.
""",
        "08_Student_Artifacts/README.md": """# Student Artifacts

This folder tracks student-facing artifacts, especially anything that collects responses.

Student response data is not temporary.

Use this folder for:

- Artifact specs.
- Registry entries.
- Durable metadata.
- Teacher-approved aggregate summaries.

Do not store raw student-identifiable response exports here unless an approved process exists.
""",
        "08_Student_Artifacts/student_artifact_delivery_spec.md": """# Student Artifact Delivery Spec

## Principle

TMS OS can generate temporary interfaces. It cannot treat collected student evidence as temporary.

## Required Registry Fields

- Artifact ID.
- Date.
- Course.
- Period.
- Lesson workspace path.
- Artifact type.
- Delivery mode.
- Storage location.
- Teacher edit URL.
- Student responder URL.
- Response sheet URL.
- Collection settings.
- Data sensitivity.
- Evidence summary path.
- Status.
- Notes.

## Google Forms Exit Ticket Flow

1. Generate questions in the daily workspace.
2. Prepare a Google Forms artifact spec.
3. If Google Forms creation is available, create the form in the teacher's Google Drive automatically for `google_form_collect` artifacts.
4. Configure collection settings according to teacher/school policy.
5. Store the teacher edit link, student responder link, and response Sheet link in the daily workspace snapshot and artifact registry.
6. Teacher posts the student responder link to the LMS.
7. Responses remain in Google Forms or the linked Google Sheet.
8. After class, Codex may summarize results only when the teacher asks and only under active data-use rules.

## Chrome Creation Fallback

When direct Google Forms API creation is not available, use Chrome with the teacher's signed-in Google account.

1. Open Chrome through the `Chrome` plugin.
2. Open `https://forms.new`.
3. Build the form from the saved artifact spec.
4. Configure approved settings.
5. Capture the teacher edit URL.
6. Capture the student responder link.
7. Link responses to a Google Sheet when possible.
8. Update the daily workspace HTML, snapshot, registry, and artifact spec.

Do not claim a live Google Form exists until the edit and responder links have been captured.
""",
        "08_Student_Artifacts/google_forms_exit_ticket_template.md": """# Google Forms Exit Ticket Template

## Form Metadata

- Form title: `[Date] [Course] Exit Ticket - [Topic]`
- Form description: Short student-facing purpose statement.
- Linked lesson workspace: `outputs/daily-workspace-YYYY-MM-DD-<topic>.html`
- Delivery mode: `google_form_collect`
- Data sensitivity: `student_identifiable_when_submitted` if email collection or names are enabled.

## Recommended Question Types

- Multiple choice for quick misconception checks.
- Short answer for concept explanation.
- Paragraph only when richer reflection is needed.
- Checkbox when more than one idea may apply.

## Default Settings

Use only when allowed by school policy:

- Collect verified email addresses for signed-in school accounts.
- Limit to one response when accountable completion is desired.
- Keep response editing off by default.
- Do not publish response summaries to students by default.
- Do not use file upload unless explicitly requested.

## Daily Workspace Link Slots

- `Open Google Form` for the teacher edit URL.
- `Copy LMS Link` for the student responder URL.
- `Open Responses` for the linked Sheet or Forms responses view.
- `Print Exit Ticket` fallback for paper collection.
""",
        "source_docs/source_index.md": """# Source Index

Add every uploaded or referenced source here.

| Local file | Source | Use | Status |
| --- | --- | --- | --- |
| Needed | Needed | Needed | Needed |

Do not add school-specific or course-specific claims unless they trace to a source here, a teacher-supplied statement, or an explicitly verified public source.
""",
        "outputs/README.md": """# Outputs

Generated daily workspaces and readable snapshots go here.

Do not treat outputs as the source of truth. Important continuity should be written back into class memory, source files, or student artifact metadata.
""",
        "skills/tms-os-daily-workspace/SKILL.md": DAILY_WORKSPACE_SKILL,
        "skills/tms-os-workspace-renderer/SKILL.md": WORKSPACE_RENDERER_SKILL,
        "skills/tms-os-student-artifact-delivery/SKILL.md": STUDENT_ARTIFACT_SKILL,
        "skills/tms-os-revise-workspace/SKILL.md": REVISE_WORKSPACE_SKILL,
        "skills/tms-os-after-class-logger/SKILL.md": AFTER_CLASS_SKILL,
        "skills/tms-os-class-setup/SKILL.md": CLASS_SETUP_SKILL,
        "skills/tms-os-source-refresh/SKILL.md": SOURCE_REFRESH_SKILL,
    }

    for relative_path, content in files.items():
        if write(root / relative_path, content, args.force):
            created.append(relative_path)

    period_rows = [
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
    if write_csv(root / "03_Classes_And_Periods/period_status_snapshot.csv", period_rows, args.force):
        created.append("03_Classes_And_Periods/period_status_snapshot.csv")

    registry_header = [
        "artifact_id",
        "date",
        "course",
        "period",
        "lesson_workspace_path",
        "artifact_type",
        "delivery_mode",
        "storage_location",
        "teacher_edit_url",
        "student_responder_url",
        "response_sheet_url",
        "collection_settings",
        "data_sensitivity",
        "evidence_summary_path",
        "status",
        "notes",
    ]
    if write_csv(root / "08_Student_Artifacts/student_artifact_registry.csv", [registry_header], args.force):
        created.append("08_Student_Artifacts/student_artifact_registry.csv")

    registry_template = [
        registry_header,
        [
            "YYYY-MM-DD-course-topic-exit-ticket",
            "YYYY-MM-DD",
            "TBD",
            "TBD",
            "outputs/daily-workspace-YYYY-MM-DD-topic.html",
            "exit_ticket",
            "google_form_collect",
            "google_drive",
            "",
            "",
            "",
            "collect_verified_email; limit_one_response",
            "student_identifiable_when_submitted",
            "",
            "planned",
            "Replace with real form metadata after creation",
        ],
    ]
    if write_csv(root / "08_Student_Artifacts/student_artifact_registry_template.csv", registry_template, args.force):
        created.append("08_Student_Artifacts/student_artifact_registry_template.csv")

    print(f"TMS workspace initialized at {root}")
    print(f"Created or updated {len(created)} files.")
    for path in created:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())