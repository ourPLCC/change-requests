---
id: CR-88
title: 'Make `token` or `skip` required in lexical rules'
status: Done
assignee: []
created_date: '2026-06-08'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Lexical rules should require an explicit `token` or `skip` keyword. Rules
without either keyword should be a syntax error.

### Desired Behavior

Valid:

```text
token NUM '\d+'
skip  SPACE '\s+'
```

Invalid (syntax error):

```text
NUM '\d+'
```

### Rationale

Requiring an explicit keyword makes the intent of each rule unambiguous and
improves readability. It also makes the grammar file format easier to parse
and to explain to students.

Migrated from plcc-ng #088.
<!-- SECTION:DESCRIPTION:END -->
