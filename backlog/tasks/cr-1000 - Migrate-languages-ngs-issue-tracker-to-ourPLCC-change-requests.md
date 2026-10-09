---
id: CR-1000
title: Migrate languages-ng's issue tracker to ourPLCC/change-requests
status: To Do
assignee: []
created_date: '2026-10-09 01:55'
labels: []
dependencies: []
references:
  - ../../../plcc-ng/dev-docs/specs/2026-10-08-199-central-tracker-design.md
type: chore
project: languages-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
languages-ng still keeps its own dev-docs/issues/ tracker (53 issues, frontmatter with closed: and target:). Moving it here puts all ourPLCC work in one tracker. Design: plcc-ng dev-docs/specs/2026-10-08-199-central-tracker-design.md.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Legacy issues converted at offset +500 (CR-5xx); target: maps to project
- [ ] #2 Issues already copied into plcc-ng by hand become Done + wontdo naming the plcc-ng CR
- [ ] #3 languages-ng devcontainer, CLAUDE.md and CONTRIBUTING.md follow the setup in the design; its old tracker is removed
<!-- AC:END -->
