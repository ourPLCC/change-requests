---
id: CR-69
title: 'Improve output of plcc-parse --trace'
status: Done
assignee: []
created_date: '2026-06-05'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The output of `plcc-parse --trace` is hard to read. Improve it to make parse tracing more useful for debugging grammars.

### Notes

- Consider indentation to reflect parse depth, rule entry/exit labeling, or token consumption markers.
- Look at what information is most useful when diagnosing parse failures or ambiguities.

Migrated from plcc-ng #069.
<!-- SECTION:DESCRIPTION:END -->
