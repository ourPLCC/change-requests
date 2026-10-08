---
id: CR-128
title: 'Update command reference pages for Options/Output/Diagnostics help restructuring'
status: Done
assignee: []
created_date: '2026-06-30'
labels: []
dependencies: []
type: docs
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Issue 115 restructured the `--help` output of all five main commands (`plcc-scan`, `plcc-parse`, `plcc-rep`, `plcc-make`, `plcc-diagram`) to split flags into three named sections: Options, Output, and Diagnostics. Any command reference pages that embed or reproduce help output will be stale.

### Notes

- Audit `docs/cli/commands/plcc-scan.md`, `plcc-parse.md`, `plcc-rep.md`, `plcc-make.md`, and `plcc-diagram.md` for embedded help output and update to match the new sectioned format.
- If the pages don't embed raw help text but describe flags in prose, verify the groupings still match.

Migrated from plcc-ng #128.
<!-- SECTION:DESCRIPTION:END -->
