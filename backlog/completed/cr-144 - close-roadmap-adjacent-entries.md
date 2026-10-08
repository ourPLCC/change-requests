---
id: CR-144
title: 'close-roadmap-adjacent-entries'
status: Done
assignee: []
created_date: '2026-07-06'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`bin/issues/close.bash`'s roadmap pass 2 reads the file in awk paragraph
mode (`RS = ""`), so consecutive Open Issues entries with no blank line
between them — the layout the conventions' two-line format produces —
form a single paragraph. Removing one issue's entry then deletes every
entry in that paragraph, and the now-"empty" `###` heading with it. The
follow-up `check.bash` catches the damage (open issue left without a
roadmap entry), but the operator has to repair the roadmap by hand.

Observed closing CR-142 while CR-143 sat directly below it in `### Fixes`:
both entries and the heading vanished. The `### Features` group
currently has CR-112 and CR-141 adjacent, so closing CR-112 would do the same
to CR-141.

### Steps to Reproduce

1. Have two Open Issues entries back-to-back (no blank line) under one
   `###` heading.
2. `bin/issues/close.bash` the first one.
3. Its internal `check.bash` fails: the second issue's entry was
   removed along with the first's.

### Notes

Either make close.bash operate on the two-line entry (match the bullet
line plus its indented continuation lines) instead of the paragraph, or
have new.bash/conventions put a blank line between entries so the
paragraph assumption holds. check.bash could also verify the blank-line
invariant if the latter.

Migrated from plcc-ng #144.
<!-- SECTION:DESCRIPTION:END -->
