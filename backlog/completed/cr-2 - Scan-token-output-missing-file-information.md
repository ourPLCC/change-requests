---
id: CR-2
title: 'Scan token output missing file information'
status: Done
assignee: []
created_date: '2026-05-07'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`plcc-scan` output includes position information (line/column) for both tokens
and errors, and errors include the source file. But tokens do not include the
file they came from. This is inconsistent and becomes a real problem when input
spans multiple files (or a mix of files and stdin): there is no way to tell
which file a token originated from.

Include the filename on every token (and error) line alongside the existing
position information. Each line is then self-contained, most IDEs can turn it
into a clickable link, and downstream parsers that need provenance get it
without extra context.

### Notes

- Consistency with how errors already emit file info should guide the output
  format for tokens.

Migrated from plcc-ng #002.
<!-- SECTION:DESCRIPTION:END -->
