---
id: CR-83
title: 'plcc-diagram is misclassified as a Level 0 command'
status: Done
assignee: []
created_date: '2026-06-07'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`plcc-diagram` is currently classified as a Level 0 (primitive) command, but it is a user-facing Level 2 (orchestrator) command. The misclassification causes it to appear in the wrong section of the docs and be deprioritized relative to its actual importance.

### Desired Behavior

Reclassify `plcc-diagram` as a Level 2 command everywhere it is described — in the docs, in any architectural references, and in the command reference pages.

### Notes

Related to issue 082, which reorders Level 2 commands above Level 1 in the docs. Fixing the classification here ensures `plcc-diagram` ends up in the right place once that reordering is done.

See also: CR-82

Migrated from plcc-ng #083.
<!-- SECTION:DESCRIPTION:END -->
