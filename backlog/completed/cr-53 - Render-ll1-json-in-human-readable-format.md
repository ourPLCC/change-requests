---
id: CR-53
title: 'Render ll1.json in human-readable format'
status: Done
assignee: []
created_date: '2026-06-01'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Add a command that renders `ll1.json` in a human-readable format — likely a Markdown file using tables. The output should also include explanations of how to interpret each structure in the file (e.g. the parse table, FIRST/FOLLOW sets, or whatever top-level keys are present).

### Notes

- Markdown with tables is a likely output format, but consider whether plain text or HTML might also be useful.
- Each section of `ll1.json` should be accompanied by a short explanation of what it represents and how to read it.
- Diagrams may be appropriate for some structures (e.g. parse trees, automata, relationships between rules). PlantUML is already used in the project and should be considered where it adds clarity.
- This would help users understand and debug their grammars without having to read raw JSON.

Migrated from plcc-ng #053.
<!-- SECTION:DESCRIPTION:END -->
