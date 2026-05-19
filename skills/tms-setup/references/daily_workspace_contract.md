# Daily Workspace Contract

The daily workspace is a generated shell around classroom-ready artifacts.

It is temporary UI. It does not own curriculum truth, class memory, or student evidence.

## Required Files

- `outputs/daily-workspace-YYYY-MM-DD-<short-topic>.html`
- `outputs/daily-workspace-YYYY-MM-DD-<short-topic>-snapshot.md`

## Required Metadata

- Prepared date.
- Class-use date.
- Course.
- Period or `Needed`.
- Unit/topic.
- Source mode.
- Missing-context note.
- Student artifact mode when relevant.
- Student artifact registry ID when relevant.
- Durable links/status when student responses are collected.

## Default Artifacts

- Opening board.
- Agenda or objective.
- Student task.
- Exit ticket or closure prompt.
- Teacher run notes.

## HTML Requirements

- Standalone local HTML.
- No external network assets.
- Split layout with artifact navigation.
- Present/fullscreen control.
- Print control.
- Light editable text areas or browser-native editing.
- Student link area when relevant.
- Google Form controls when relevant: open form editor, open/copy student responder link, open responses/linked Sheet.
- Print CSS.

## Snapshot Requirements

The Markdown snapshot must be readable without the HTML. It should preserve:

- Artifact text.
- Source status.
- Missing-context status.
- Student artifact delivery mode.
- Teacher edit URL when a Google Form exists.
- Student responder URL for LMS posting when a Google Form exists.
- Response Sheet URL or response location when available.
- Collection settings and data sensitivity.

Do not store raw identifiable student responses in the snapshot unless the teacher supplied an approved process.

## Google Forms Rule

When the teacher wants digital collection and authenticated Google access is available, create the live Google Form and linked response Sheet when possible. Then write the live links back to:

- The daily workspace HTML.
- The daily workspace snapshot.
- `08_Student_Artifacts/student_artifact_registry.csv`.
- The specific artifact spec under `08_Student_Artifacts/`.

If live creation is not available, include the printable fallback, a Forms-ready spec, and a clear `Google Form not created yet` status.