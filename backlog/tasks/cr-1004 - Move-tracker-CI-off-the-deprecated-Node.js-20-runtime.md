---
id: CR-1004
title: Move tracker CI off the deprecated Node.js 20 runtime
status: To Do
assignee: []
created_date: '2026-10-09 11:39'
labels: []
dependencies: []
type: chore
project: change-requests
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
GitHub Actions annotates every run of the `check` workflow ([check.yml](../../.github/workflows/check.yml)) with a warning: the actions it uses target Node.js 20, which is deprecated, and are being forced onto a newer runtime. The workflow also pins `node-version: "20"` for installing the `backlog` CLI. Once Node.js 20 support is removed, CI could break or silently run on an untested runtime.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 `actions/checkout`, `actions/setup-python`, and `actions/setup-node` are on releases that run on a supported Node.js runtime
- [ ] #2 `setup-node` installs a supported Node.js LTS, and the version pinned in `.backlog-version` still installs and passes `backlog doctor` on it
- [ ] #3 The `check` workflow passes with no Node.js deprecation annotation
<!-- AC:END -->
