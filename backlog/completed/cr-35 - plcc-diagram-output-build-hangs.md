---
id: CR-35
title: 'plcc-diagram --output=build hangs'
status: Done
assignee: []
created_date: '2026-05-24'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Running `plcc-diagram --output=build` hangs indefinitely and never returns.

### Steps to Reproduce

1. Run `plcc-diagram --output=build` on any grammar file.
2. Observe that the command does not exit.

### Notes

The hang appears specific to the `--output=build` flag. Investigate whether the issue is in how the output path is resolved, whether the command blocks waiting on a subprocess or file handle, or whether the build directory triggers a different code path from the default output.

Migrated from plcc-ng #035.
<!-- SECTION:DESCRIPTION:END -->
