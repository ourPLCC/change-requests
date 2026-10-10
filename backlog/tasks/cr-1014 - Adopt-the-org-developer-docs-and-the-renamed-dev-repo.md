---
id: CR-1014
title: Adopt the org developer docs and the renamed dev repo
status: To Do
assignee: []
created_date: '2026-10-10 18:34'
labels: []
milestone: m-0
dependencies:
  - CR-1013
references:
  - ../../dev-docs/specs/2026-10-10-org-developer-docs-design.md
type: chore
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
plcc-ng's CONTRIBUTING.md and CLAUDE.md restate workflow rules that now live in the org developer guide in ourPLCC/dev, and the copies will drift. CLAUDE.md also mixes rules every developer needs with rules only agents need, and loads only for Claude. The devcontainer still clones and mounts the tracker under its old name.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The devcontainer clones ../dev if missing, mounts it at /workspaces/dev, and sets BACKLOG_CWD and safe.directory to match; after a rebuild, backlog commands work
- [ ] #2 AGENTS.md replaces CLAUDE.md: it imports ../dev/AGENTS.md, ../dev/CONTRIBUTING.md, then CONTRIBUTING.md, and holds only agent rules specific to plcc-ng
- [ ] #3 In a fresh Claude Code session, the imported files are loaded; any approval prompt for imports outside the repo is described in the setup instructions
- [ ] #4 CONTRIBUTING.md opens by pointing to the org developer guide, holds only plcc-ng-specific material, and states each deviation from the org guide with its reason
- [ ] #5 The PR template and other docs refer to the tracker as ourPLCC/dev
- [ ] #6 The PR description tells maintainers to rename their host ../change-requests folder to ../dev before rebuilding
<!-- AC:END -->
