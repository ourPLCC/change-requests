---
id: CR-1009
title: Set up plcc-ng-devcontainer to use the central tracker
status: To Do
assignee: []
created_date: '2026-10-09 12:36'
updated_date: '2026-10-10 19:15'
labels: []
milestone: m-0
dependencies:
  - CR-1013
references:
  - ../../../plcc-ng/dev-docs/specs/2026-10-08-199-central-tracker-design.md
type: chore
project: plcc-ng-devcontainer
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
plcc-ng-devcontainer has no legacy issues, but work in it is tracked here, and its contributors and agents cannot reach the tracker from its container. It needs the same setup as the other code repos (design: plcc-ng dev-docs/specs/2026-10-08-199-central-tracker-design.md, "Setup in each code repo").

Carry over from plcc-ng: give the ~/.claude named volume a per-repo name (not plcc-ng-claude), and make any containerEnv GIT_CONFIG_* safe.directory entries name this repo's own path.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The devcontainer clones the tracker beside the repo if missing, bind-mounts it at /workspaces/dev, sets BACKLOG_CWD, and installs the backlog version pinned in .backlog-version
- [ ] #2 Creating the container fails loudly if git refuses the repo or the tracker (dubious ownership)
- [ ] #3 After a rebuild on the host, backlog task list --project plcc-ng-devcontainer --plain works inside the container
- [ ] #4 CLAUDE.md and contributing docs point to the tracker README for tracking work
<!-- AC:END -->
