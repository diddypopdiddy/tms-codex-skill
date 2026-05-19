# TMS Setup Workflow

## Goal

Create a usable first version of a teacher's local TMS OS. It should be useful before every detail is perfect, but it must be honest about missing context.

## Phase 1: Initialize

Check whether these folders exist:

- `00_Start_Here`
- `01_School_Context`
- `02_Master_Curriculum`
- `03_Classes_And_Periods`
- `04_Units`
- `05_Teacher_Profile`
- `06_Class_Memory`
- `07_Artifact_Templates`
- `08_Student_Artifacts`
- `source_docs`
- `outputs`
- `skills`

If not, run the workspace creation script.

## Phase 2: Identify The Teacher Context

Ask:

```text
What school, grade band, and subject/course area should this TMS support first?
```

Write confirmed facts to `01_School_Context/school_profile.md`. If the teacher is unsure or the fact comes from memory, label the source as `Teacher supplied` or `Needed`.

## Phase 3: Add Courses And Periods

Ask for the smallest useful schedule:

```text
What courses or periods do you want to set up first? You can paste a schedule or list one class to start.
```

Update `03_Classes_And_Periods/period_status_snapshot.csv`.

Create timeline files only after period/course names are known.

## Phase 4: Gather Source Documents

Ask for uploads in this order:

1. Syllabus or course outline.
2. Curriculum map, pacing guide, or unit plan.
3. Bell schedule and school calendar.
4. Rubrics or assessment policies.
5. LMS assignment list or export, if available.
6. District AI/data-use rules, if available.

Each uploaded file should be placed under `source_docs/teacher_uploads/` or another clear subfolder. Update `source_docs/source_index.md` with filename, source, and use.

## Phase 5: Teacher Defaults

Ask:

```text
What should most of your lessons include by default: Do Now, agenda, mini lesson, student work, exit ticket, homework, Google Form exit ticket, or something else?
```

Update `05_Teacher_Profile/global_defaults.md`.

## Phase 6: Data Boundaries

Before rosters, grades, accommodations, behavior notes, Google Forms responses, uploaded student work, or image analysis are processed, read `privacy_and_policy.md`.

If policy is missing, planning and artifact creation can continue, but student-specific analysis should stay blocked.

## Phase 7: First Proof

Ask:

```text
What is the first class or topic you want to plan for?
```

Generate one daily workspace and snapshot in `outputs/`. Keep it practical and short.

If the first proof includes digital collection:

1. Create a durable artifact spec under `08_Student_Artifacts/`.
2. Create the live Google Form when authenticated Google access is available.
3. Capture teacher edit link, student responder link, and linked response Sheet URL when available.
4. Update the workspace, snapshot, registry, and artifact spec with the real links.
5. If live creation is unavailable, leave a Forms-ready spec and clear not-created status.

## Phase 8: Handoff

End setup by naming:

- Workspace created.
- Files updated.
- Missing inputs.
- Whether live Google Form creation is available.
- First planning command the teacher can use tomorrow.

## Ongoing Loop

After setup, use the same loop:

1. Plan next class from source docs, teacher defaults, and class memory.
2. Generate the daily workspace and snapshot.
3. Create student artifacts for print or digital collection.
4. Keep raw student responses in durable approved systems.
5. Summarize response patterns only when asked and only under the current data-use boundary.
6. Save teacher-approved aggregate evidence to class memory when the teacher asks to carry it forward.