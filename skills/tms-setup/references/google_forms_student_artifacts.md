# Google Forms Student Artifacts

Use this reference when a TMS OS workspace needs a student-facing digital artifact that collects responses.

## Supported Uses

- Exit ticket.
- Short quiz.
- Vocab check.
- Reflection.
- Formative assessment.
- Readiness check.
- Photo or file upload workflow, only when explicitly approved.

## Delivery Mode

Use `google_form_collect` when Google Forms collects responses.

Every `google_form_collect` artifact needs durable metadata under `08_Student_Artifacts/`.

## Required Durable Fields

- Artifact ID.
- Date.
- Course.
- Period, if known.
- Lesson workspace path.
- Artifact type.
- Delivery mode.
- Storage location.
- Teacher edit URL.
- Student responder URL for LMS posting.
- Response Sheet URL or response location.
- Collection settings.
- Data sensitivity.
- Evidence summary path, if created.
- Status.
- Notes.

## Live Creation Path

When authenticated Google access is available:

1. Generate questions in the daily workspace.
2. Save a Google Forms artifact spec under `08_Student_Artifacts/`.
3. Open `https://forms.new` through Chrome if no direct Forms API tool is available.
4. Build the form from the saved spec.
5. Configure only approved/default settings.
6. Publish or enable responder access as appropriate.
7. Capture the teacher edit URL.
8. Capture the student responder URL.
9. Link responses to a Google Sheet when possible and capture the Sheet URL.
10. Update the HTML workspace, Markdown snapshot, registry, and artifact spec.

Do not mark the artifact as `created` until real links have been captured.

## Default Settings

Use these only when allowed by school policy:

- Collect verified email addresses.
- Limit to one response for accountable completion.
- Keep response editing off.
- Do not show response summaries to students.
- Do not use file upload unless explicitly approved.
- Link responses to a Google Sheet for recurring review.

## File Upload / Photo Evidence

Google Forms file upload can support photos of student work, sketches, storyboards, worksheets, or project artifacts, but it has extra data implications.

Before using file upload:

1. Confirm the teacher wants file upload.
2. Confirm the storage and data-use boundary.
3. Confirm whether student work can be processed by AI.
4. Capture only aggregate or teacher-approved summaries in the project by default.

If file upload cannot be created through an API path, use Chrome automation when approved. If neither is available, produce a Forms-ready spec and mark file upload as manual setup needed.

## Response Analysis Path

When the teacher asks to analyze responses:

1. Read the registry entry to find the response Sheet.
2. Read the Sheet metadata and the relevant response tab.
3. Exclude obvious teacher/test rows when the teacher identifies them.
4. Summarize aggregate patterns by default:
   - completion count
   - common misconception
   - readiness split
   - next instructional move
5. Save a summary only when the teacher asks to save/carry forward evidence.
6. Do not paste raw rows, student emails, or identifiable response text into project files unless an approved process exists.

## Failure State

If live form creation is unavailable, the workspace must still include:

- Printable fallback.
- Google Forms-ready spec.
- Registry placeholder.
- Clear status: `Google Form not created yet` or `planned`.
- Next action for the teacher or Codex to create the form later.