---
id: CR-103
title: 'Fix `__run__` → `_run` in Language Guide Overview examples'
status: Done
assignee: []
created_date: '2026-06-22'
labels: []
dependencies: []
type: docs
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The example code on the Language Guide Overview page uses `__run__` (double underscores) instead of the correct `_run` (single underscore) in both the Java and Python examples.

### Steps to Reproduce

1. Open the Language Guide → Overview page.
2. Look at the example code for Java and Python.
3. Observe `__run__` where `_run` should appear.

### Notes

Both language variants are affected. A simple find-and-replace in the overview source file should fix it.

Migrated from plcc-ng #103.
<!-- SECTION:DESCRIPTION:END -->
