---
id: CR-1000
title: Migrate languages-ng's issue tracker to ourPLCC/dev
status: To Do
assignee: []
created_date: '2026-10-09 01:55'
updated_date: '2026-10-10 19:15'
labels: []
milestone: m-0
dependencies:
  - CR-1005
  - CR-1006
  - CR-1007
  - CR-1013
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

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Notes for whoever migrates languages-ng:
- The devcontainer named volume for ~/.claude is called plcc-ng-claude; use a per-repo name (e.g. languages-ng-claude) when copying the devcontainer setup.
- The containerEnv GIT_CONFIG_* safe.directory entries must name that repo's own path.
- migrate/ caveats before reuse: plcc_ng.assign_ids hardcodes the 400-499 range guard although offset is a parameter (generalize per repo); _remove_previous matches the provenance prefix anywhere in a file (anchor it to the last line); verify crashes with AttributeError if a migrated file lacks id:; type_overrides keyed by legacy number applies to both files of a duplicate-number pair.

Correction to the _remove_previous caveat above: the provenance line ends the description section (before SECTION:DESCRIPTION:END), not the file. Tracked as CR-1006.
<!-- SECTION:NOTES:END -->
