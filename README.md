# TMS Codex Skill

Installable Codex skill for setting up a teacher's local Teaching Management System workspace.

This package is designed for teachers who already have Codex Desktop installed. The teacher installs the skill, opens an empty teaching folder in Codex, and asks Codex to get started. The skill creates the workspace structure, runs a guided setup interview, asks for source documents, marks missing inputs, and helps generate daily classroom workspaces. After setup, the same skill supports the recurring loop: plan, present, create student-facing artifacts, collect evidence in durable systems, log what happened, and plan again.

## What It Does

- Creates a local TMS OS folder structure.
- Asks for school, course, period, schedule, and source-document context.
- Builds source indexes, teacher defaults, class shells, class-memory templates, artifact templates, and student-artifact rules.
- Preserves missing context instead of guessing.
- Keeps student data boundaries visible.
- Produces daily workspaces with opening boards, student tasks, exit tickets, and teacher run notes.
- Supports live Google Forms exit tickets when authenticated Google access is available.
- Saves durable Form, responder, and response Sheet metadata in the local workspace registry.
- Supports ongoing daily planning and after-class continuity updates.

## Google Forms Workflow

When the teacher wants digital collection for an exit ticket, quiz, reflection, vocab check, or formative assessment, the current workflow is:

1. Generate the student-facing questions in the daily workspace.
2. Keep a printable fallback.
3. Create a live Google Form when a Forms API path or authenticated Chrome access is available.
4. Capture the teacher edit URL and student responder URL.
5. Link responses to a Google Sheet when possible.
6. Write those links back to the workspace, snapshot, artifact spec, and registry.
7. Keep raw student-identifiable responses in Google Forms or Sheets unless the teacher supplies an approved process.

If live Google Form creation is unavailable, the skill must create a Forms-ready spec and clearly mark the artifact as not yet created.

## Install From GitHub

Teachers can install the skill from Codex by asking:

```text
Install the TMS setup skill from https://github.com/diddypopdiddy/tms-codex-skill/tree/main/skills/tms-setup
```

Then restart Codex.

## First Teacher Run

1. Create an empty folder for the class or teacher workspace.
2. Open that folder as a Codex project.
3. Type:

```text
Use $tms-setup to get started.
```

Codex should create the starter workspace and begin the setup interview.

After setup, teachers can keep using commands like:

```text
Use $tms-setup to plan tomorrow.
Use $tms-setup to make an exit ticket.
Use $tms-setup to analyze exit ticket responses.
Use $tms-setup to log what happened today.
```

## Repository Layout

```text
skills/tms-setup/
  SKILL.md
  agents/openai.yaml
  scripts/create_tms_workspace.py
  references/
docs/
  index.html
.github/workflows/pages.yml
```

## Important Boundary

This is not an SIS, LMS, gradebook, IEP/504 system, or official student-record system. It is a local planning and teaching-management workspace. Student-identifiable data should only be handled under an approved school or district process. Public templates should not include a teacher's live Form links, response Sheet links, student emails, rosters, grades, or uploaded student work.