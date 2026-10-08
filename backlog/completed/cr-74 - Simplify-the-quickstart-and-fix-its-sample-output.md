---
id: CR-74
title: 'Simplify the quickstart and fix its sample output'
status: Done
assignee: []
created_date: '2026-06-07'
labels: []
dependencies: []
type: docs
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The quickstart has two problems:

1. It tells users to run `plcc-make` directly, which is unnecessary — users should not need to invoke it by hand.
2. The sample output shown in the quickstart is inaccurate and does not match what the tool actually produces.

### Desired Behavior

- Remove the `plcc-make` step (or replace it with whatever the correct simplified flow is).
- Replace all sample output blocks with real, verified output copied from an actual run.

### Notes

When fixing the output, run the quickstart steps from scratch in a clean environment to capture genuine output rather than editing by hand.

Migrated from plcc-ng #074.
<!-- SECTION:DESCRIPTION:END -->
