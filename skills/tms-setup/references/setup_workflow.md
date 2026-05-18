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
What should most of your lessons include by default: Do Now, agenda, mini lesson, student work, exit ticket, homework, or something else?
```

Update `05_Teacher_Profile/global_defaults.md`.

## Phase 6: Data Boundaries

Before rosters, grades, accommodations, behavior notes, or Google Forms responses are processed, read `privacy_and_policy.md`.

If policy is missing, planning can continue, but student-specific analysis should stay blocked.

## Phase 7: First Proof

Ask:

```text
What is the first class or topic you want to plan for?
```

Generate one daily workspace and snapshot in `outputs/`. Keep it practical and short.

## Phase 8: Handoff

End setup by naming:

- Workspace created.
- Files updated.
- Missing inputs.
- First planning command the teacher can use tomorrow.

