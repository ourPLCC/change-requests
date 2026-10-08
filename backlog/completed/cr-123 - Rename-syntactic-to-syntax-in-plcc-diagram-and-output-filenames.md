---
id: CR-123
title: 'Rename syntactic to syntax in plcc-diagram-* and output filenames'
status: Done
assignee: []
created_date: '2026-06-27'
labels: []
dependencies: []
type: refactor
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The `plcc-diagram-*` commands and the filenames they produce use the word "syntactic" (e.g. `syntactic-diagram`). This should be renamed to "syntax" for consistency and clarity.

### Notes

- Affects command names under `plcc-diagram-*` that include "syntactic"
- Affects the names of output files those commands produce
- A breaking change for users relying on the current output filenames

Migrated from plcc-ng #123.
<!-- SECTION:DESCRIPTION:END -->
