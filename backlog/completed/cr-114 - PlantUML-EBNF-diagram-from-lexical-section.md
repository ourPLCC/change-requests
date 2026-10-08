---
id: CR-114
title: 'PlantUML EBNF diagram from lexical section'
status: Done
assignee: []
created_date: '2026-06-25'
labels:
  - wontdo
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Add `plcc-diagram-lexical`, a command that generates a PlantUML EBNF-style diagram from the lexical section of a PLCC spec file. This is the lexical counterpart to issue CR-109 (`plcc-diagram-syntactic`).

### Notes

- Input is the lexical section of the spec (token and skip rules), available from `plcc-spec` JSON output — no new parsing needed.
- Entry points follow the naming scheme established in issue CR-113:
  - `plcc-diagram-lexical` (orchestrator)
  - `plcc-diagram-lexical-plantuml-emit` (emitter)
- Reuses `plcc-diagram-plantuml-build` and `plcc-diagram-plantuml-run` unchanged.
- PlantUML EBNF (`@startebnf`) can represent lexical rules as named token definitions; skip rules may be included or omitted (TBD).
- Should be built after issue CR-109 (`plcc-diagram-syntactic`) since they share the same orchestrator pattern.

Migrated from plcc-ng #114.
<!-- SECTION:DESCRIPTION:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Abandoned before migration: abandoned — not a priority for v1.0; revisit if needed
<!-- SECTION:FINAL_SUMMARY:END -->
