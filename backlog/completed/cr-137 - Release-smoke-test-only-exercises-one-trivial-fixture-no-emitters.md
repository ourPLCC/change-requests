---
id: CR-137
title: 'Release smoke test only exercises one trivial fixture, no emitters'
status: Done
assignee: []
created_date: '2026-07-03'
labels: []
dependencies: []
type: test
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The "Smoke test TestPyPI install" step in `.github/workflows/release.yml` installs the published package into a clean venv and runs `plcc-make --spec=tests/fixtures/trivial.plcc`, checking only that `plcc-ng/spec.json` is written. It doesn't exercise any of the four emitters (Python, Java, Haskell, JavaScript).

Issue 112 (first major release) requires all four emitters to be v1-supported. A real installability problem in a published package — e.g. missing runtime package data needed by the Haskell or JavaScript emitter — would not be caught by this smoke test, since it never invokes emission for any target language.

### Notes

- Found while writing the release SOP (issue 130), which needs to describe post-release verification (per issue 130's notes: "smoke test, docs site, PyPI install").
- Possible fix: extend the smoke test to run `plcc-make` (or equivalent) against a fixture for each of the four emitters, confirming generated output at least builds/runs, not just that `spec.json` exists.
- Related to issue 112's v1.0 criteria around emitter parity.

Migrated from plcc-ng #137.
<!-- SECTION:DESCRIPTION:END -->
