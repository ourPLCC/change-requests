---
id: CR-124
title: 'Drop Mermaid diagram support'
status: Done
assignee: []
created_date: '2026-06-28'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Remove the Mermaid diagram extension from plcc-ng. The `plcc-diagram-mermaid-*` commands are broken (the run command does not work even with Node.js installed) and the redesign proposed in CR-111 was abandoned. PlantUML covers the diagram use cases we need today. If a future diagram type is identified that PlantUML cannot produce but Mermaid can, Mermaid support can be re-added at that point.

### Notes

- Remove all `plcc-diagram-mermaid-*` entry points from `pyproject.toml`
- Remove the Mermaid extension source under `src/plcc/`
- Remove or archive Mermaid-related bats tests in `tests/bats/commands/`
- Remove Mermaid from any user-facing docs or CLI help text
- This is a breaking change for users using `--format=mermaid`; note it in CHANGELOG

Migrated from plcc-ng #124.
<!-- SECTION:DESCRIPTION:END -->
