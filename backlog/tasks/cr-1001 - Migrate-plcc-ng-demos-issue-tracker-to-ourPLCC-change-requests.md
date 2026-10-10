---
id: CR-1001
title: Migrate plcc-ng-demo's issue tracker to ourPLCC/dev
status: To Do
assignee: []
created_date: '2026-10-09 01:55'
updated_date: '2026-10-10 19:25'
labels: []
milestone: m-0
dependencies:
  - CR-1005
  - CR-1006
  - CR-1007
  - CR-1008
  - CR-1013
  - CR-1014
references:
  - ../../../plcc-ng/dev-docs/specs/2026-10-08-199-central-tracker-design.md
type: chore
project: plcc-ng-demo
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
plcc-ng-demo keeps a 5-issue copy of the old plcc-ng tracker. Design: plcc-ng dev-docs/specs/2026-10-08-199-central-tracker-design.md.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Legacy issues converted at offset +800 (CR-8xx)
- [ ] #2 plcc-ng-demo's devcontainer, AGENTS.md, and CONTRIBUTING.md follow plcc-ng's layout: the devcontainer clones and mounts ../dev at /workspaces/dev with BACKLOG_CWD set, AGENTS.md imports ../dev/ORG-AGENTS.md, ../dev/CONTRIBUTING.md, then CONTRIBUTING.md, and CONTRIBUTING.md opens with the link to the org developer guide; its old tracker is removed
<!-- AC:END -->
