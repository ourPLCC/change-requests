---
id: CR-34
title: 'Add plcc-version command'
status: Done
assignee: []
created_date: '2026-05-23'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
There is no command to print the installed version of `plcc-ng`. A `plcc-version` command (or `plcc --version` flag) would let users and scripts confirm which version is installed.

### Notes

- Version string is available via `importlib.metadata.version("plcc-ng")` at runtime.
- Should print to stdout and exit 0.
- Consider whether this belongs as a standalone entry point (`plcc-version`) or as a flag on an existing orchestrator (`plcc-make --version`).

Migrated from plcc-ng #034.
<!-- SECTION:DESCRIPTION:END -->
