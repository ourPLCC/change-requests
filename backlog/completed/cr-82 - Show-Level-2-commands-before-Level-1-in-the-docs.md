---
id: CR-82
title: 'Show Level 2 commands before Level 1 in the docs'
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
The docs currently present Level 1 (primitive) commands before Level 2 (orchestrator) commands. Most users only need the Level 2 commands, so leading with Level 1 buries the content they actually care about.

### Desired Behavior

Reverse the order: present Level 2 commands first, then Level 1. Level 1 can remain documented for users who need low-level access, but it should not be the first thing a user encounters.

### Notes

This is a navigation and information-architecture change only — no command behavior changes.

Migrated from plcc-ng #082.
<!-- SECTION:DESCRIPTION:END -->
