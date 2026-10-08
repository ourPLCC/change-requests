---
id: CR-106
title: 'Add documentation for the JavaScript language extension'
status: Done
assignee: []
created_date: '2026-06-23'
labels: []
dependencies: []
type: docs
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
plcc-ng can now emit JavaScript, but there is no user-facing documentation for it. Users have no way to know the feature exists, how to invoke it, or how to write JavaScript semantic sections.

### Notes

- Model the page on the existing Java and Python language guide pages.
- Cover: how to invoke `plcc-javascript-emit`, the supported fragment kinds (`top`, `import`, `body`, `file`, `class`), and a minimal end-to-end example.
- Note any JavaScript-specific runtime requirements (Node.js version, module format).

Migrated from plcc-ng #106.
<!-- SECTION:DESCRIPTION:END -->
