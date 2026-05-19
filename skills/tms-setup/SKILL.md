---
name: tms-setup
description: Set up and operate a teacher's local TMS OS workspace in Codex. Use when a teacher wants to get started with a Teaching Management System, initialize a TMS folder, upload school/course documents, create class shells, define teacher defaults, preserve missing inputs, set student-data boundaries, generate daily classroom workspaces, create live Google Forms or student artifact specs, analyze collected response summaries, or log what happened after class.
---

# TMS Setup

## Purpose

Use this skill to turn a blank folder into a local Teaching Management System workspace for one teacher.

The result is not a traditional app. Codex chat is the control layer, project files are the source of truth, generated HTML is a present/print/edit shell, and student evidence stays in approved durable systems such as Google Forms, Google Sheets, Drive, LMS exports, or teacher-approved local files.

## When To Use

Use when the teacher says:

- "Get started."
- "Set up my TMS."
- "Create my teaching management system."
- "Set up my classes."
- "I want to use Codex for lesson planning."
- "Build the folder for my school/course."
- "Run the TMS setup interview."
- "Plan tomorrow."
- "Make the board."
- "Make an exit ticket."
- "Make it a Google Form."
- "Analyze exit ticket responses."
- "Log what happened today."

## Core Setup Flow

1. Inspect the current folder.
2. If no TMS structure exists, run `scripts/create_tms_workspace.py` against the current folder.
3. Ask one setup question at a time.
4. Request source documents in batches, not all at once.
5. Write only confirmed information into project files.
6. Mark missing inputs as `Needed` instead of guessing.
7. Create course and period shells once the teacher supplies schedule/class context.
8. Create or refine teacher defaults.
9. Define student-data and AI/data-use boundaries before handling student-identifiable evidence.
10. Generate one first daily workspace as the proof that setup works.

## Read As Needed

- `references/setup_workflow.md` for the full setup sequence.
- `references/document_checklist.md` for what to ask teachers to upload.
- `references/privacy_and_policy.md` before handling student-identifiable data, Google Forms responses, rosters, grades, accommodations, or uploaded student work.
- `references/daily_workspace_contract.md` before generating the first classroom workspace.
- `references/google_forms_student_artifacts.md` before creating live Google Forms, response Sheets, or response summaries.

## Workspace Creation

When the target folder is blank or missing the TMS structure, run:

```bash
python3 <skill_dir>/scripts/create_tms_workspace.py .
```

Resolve `<skill_dir>` to this skill folder. The script is safe by default and will not overwrite existing files unless called with `--force`.

After creation, read:

1. `00_Start_Here/README.md`
2. `00_Start_Here/setup_status.md`
3. `00_Start_Here/codex_native_daily_workspace_spec.md`
4. `06_Class_Memory/missing_inputs_for_live_use.md`
5. `08_Student_Artifacts/student_artifact_delivery_spec.md`

Then continue the setup interview.

## Setup Interview Rules

Ask at most one short question at a time unless the teacher asks for a checklist.

Prefer this order:

1. School and teaching context.
2. Courses and periods.
3. Schedule and calendar.
4. Curriculum and unit sources.
5. Teacher defaults.
6. Artifact preferences.
7. Student-data boundaries.
8. First class/day to plan.

Do not invent:

- School policy.
- Course approval status.
- Period schedule.
- Rosters.
- Grades.
- Accommodations.
- Student names.
- Media-release status.
- AI/data-use permission.
- Google Forms, response Sheet, or LMS links.

## Required Write Targets

Update or create these files during setup:

- `00_Start_Here/setup_status.md`
- `00_Start_Here/codex_native_daily_workspace_spec.md`
- `01_School_Context/school_profile.md`
- `01_School_Context/source_claims_and_limits.md`
- `02_Master_Curriculum/course_index.md`
- `03_Classes_And_Periods/period_status_snapshot.csv`
- `05_Teacher_Profile/global_defaults.md`
- `06_Class_Memory/missing_inputs_for_live_use.md`
- `07_Artifact_Templates/daily_workspace_template.md`
- `08_Student_Artifacts/student_artifact_delivery_spec.md`
- `08_Student_Artifacts/student_artifact_registry.csv`
- `source_docs/source_index.md`

Create class-specific files only when enough course/period context exists:

- `05_Teacher_Profile/course_profile_<course-slug>.md`
- `06_Class_Memory/period-<period>-<course-slug>-timeline.md`

Use lowercase hyphen slugs.

## First Daily Workspace

Once one course and class-use date are known, generate:

- `outputs/daily-workspace-YYYY-MM-DD-<short-topic>.html`
- `outputs/daily-workspace-YYYY-MM-DD-<short-topic>-snapshot.md`

The workspace should include:

- Opening board.
- Agenda or learning target.
- Student task.
- Exit ticket.
- Teacher run notes.
- Source mode.
- Missing-context note.
- Print and present controls.
- Student artifact links or placeholders when relevant.

If the teacher wants digital collection, create the live Google Form when an authenticated Google path is available. Capture the teacher edit link, student responder link, and response Sheet link, then write them back into the workspace, snapshot, artifact spec, and registry. Only mark a live form as created after real links exist.

If live Google Form creation is unavailable, create a Google Forms-ready artifact spec and clearly mark the live form as not created.

## Ongoing Daily Use

After setup, keep using this skill for the recurring teacher loop:

1. Plan the next class from source docs, teacher defaults, and class memory.
2. Generate a daily workspace and snapshot in `outputs/`.
3. Create printable or digital student artifacts when useful.
4. For `google_form_collect`, create the live Google Form when Chrome/authenticated Google access or a Forms API path is available.
5. Keep durable student-artifact metadata in `08_Student_Artifacts/`.
6. Analyze responses only when asked and summarize aggregate patterns by default.
7. After class, update class memory only when the teacher asks to save or carry forward what happened.

For "plan tomorrow" or similar requests, do not answer with only a Markdown lesson unless the teacher explicitly asks for text-only output. Create the daily workspace files first.

For "log what happened" requests, append to the right class timeline when the period/course is known. Ask one short clarifying question if the class cannot be identified.

## Final Response Shape

Keep setup updates short:

1. What was created or updated.
2. What the teacher should upload or answer next.
3. Whether the workspace is ready for first planning.
4. If a live Google Form was created, include the teacher edit link, student responder link, and response Sheet link.

Do not paste raw student data in chat.