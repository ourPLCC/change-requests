---
id: CR-4
title: 'Support short form of --verbosity (-v, -vv, etc.)'
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
`--verbosity=N` has no short form. Supporting the conventional `-v` / `-vv`
/ `-vvv` style (each `-v` increments the level by one) would make interactive
use faster and match user expectations from tools like `curl`, `ansible`, and
others.

Proposed mapping:

| Short form | Equivalent |
|------------|------------|
| (omitted)  | `--verbosity=0` |
| `-v`       | `--verbosity=1` |
| `-vv`      | `--verbosity=2` |
| `-v -v`    | `--verbosity=2` |
| `-vvv`     | `--verbosity=3` |
| `-v -v -v` | `--verbosity=3` |
| `-vv -v`   | `--verbosity=3` |
| `-v -vv`   | `--verbosity=3` |

### Notes

If adopted, this convention **must be applied consistently across all commands**
that accept `--verbosity`. A user who learns it on one command will expect it
everywhere; inconsistency would be worse than not supporting it at all.

Check whether the argument-parsing library already supports counted flags
(argparse does not natively; click does via `count=True`). If a custom solution
is needed, centralise it so all commands get the behaviour from one place.

Migrated from plcc-ng #004.
<!-- SECTION:DESCRIPTION:END -->
