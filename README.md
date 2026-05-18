# TMS Codex Skill

Installable Codex skill for setting up a teacher's local Teaching Management System workspace.

This package is designed for teachers who already have Codex Desktop installed. The teacher installs the skill, opens an empty teaching folder in Codex, and asks Codex to get started. The skill then creates the workspace structure, runs a guided setup interview, asks for source documents, marks missing inputs, and helps generate the first daily classroom workspace. After setup, the same skill supports the recurring loop: plan, present, collect evidence, log what happened, and plan again.

## What It Does

- Creates a local TMS OS folder structure.
- Asks for school, course, period, schedule, and source-document context.
- Builds source indexes, teacher defaults, class shells, class-memory templates, artifact templates, and student-artifact rules.
- Preserves missing context instead of guessing.
- Keeps student data boundaries visible.
- Produces the first practical output: a daily workspace with an opening board, student task, exit ticket, and teacher run notes.
- Supports ongoing daily planning and after-class continuity updates.

## Install From GitHub

After this repository is published, teachers can install the skill from Codex by asking:

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

This is not an SIS, LMS, gradebook, IEP/504 system, or official student-record system. It is a local planning and teaching-management workspace. Student-identifiable data should only be handled under an approved school or district process.
