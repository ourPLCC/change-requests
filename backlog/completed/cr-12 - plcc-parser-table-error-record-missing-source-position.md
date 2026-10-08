---
id: CR-12
title: 'plcc-parser-table error record missing source position'
status: Done
assignee: []
created_date: '2026-05-13'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
When `plcc-parser-table` encounters a parse error it emits:

```json
{"kind": "error", "message": "...", "stage": "plcc-parser-table"}
```

The record has no source position (`file`, `line`, `column`). Downstream tools that display
parse errors (e.g. `plcc-parse`, `plcc-rep`) cannot point the user to the offending token.

### Desired behaviour

The error record should include a `source` field derived from the token that triggered the
parse error, matching the shape used by lex error records from `plcc-tokens`:

```json
{
  "kind": "error",
  "message": "...",
  "stage": "plcc-parser-table",
  "source": {"file": "...", "line": 1, "column": 5}
}
```

### Notes

Adding position requires `ParseError` (or `IncompleteInputError`) to carry the offending
token's source metadata. This is a non-trivial change to `predictive_parser.py`: the
exception currently holds only the message string. Deferred from the source-runner
refactor to keep that PR focused.

Related to issue CR-17, which
addresses the same pattern in `plcc-tokens`: unrecognized-character errors omit both
the offending character and its source position.

Related to issue CR-19, which addresses the
student-facing presentation of parse errors. The sample error in that issue shows
`"pos": {}` — confirming the structured position field is still empty and that the
position appears only as a Python-dict substring inside `message`. Issues 012 and 019
are complementary: 012 fixes the structured record, 019 fixes the human-readable output.

Migrated from plcc-ng #012.
<!-- SECTION:DESCRIPTION:END -->
