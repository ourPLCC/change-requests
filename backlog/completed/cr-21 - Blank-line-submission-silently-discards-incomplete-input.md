---
id: CR-21
title: 'Blank-line submission silently discards incomplete input'
status: Done
assignee: []
created_date: '2026-05-14'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
When a blank line is used to submit a multi-line buffer and the accumulated
input is incomplete (the grammar cannot parse it into a tree), the session
silently returns to the `>>>` prompt with no error message. The user has no
way to know whether their input was accepted, rejected, or simply dropped.

### Steps to Reproduce

Grammar:

```
skip WS '\s+'
token A 'a'
token AA 'aa'
token ID '\w+'
%
<prog> ::= <A> <AA> <ID>
```

Session:

```
>>> a
... 
>>> 
```

1. Type `a`, press Enter → `...` continuation (grammar needs `AA` and `ID`).
2. Press Enter on the blank `...` line to submit the buffer.
3. Observe: `>>>` reappears with no output and no error.

**Expected:** an error message indicating that `a` alone is not a complete
program.

**Actual:** silent return to `>>>`.

### Notes

The bug is in `SourceRunner._run_interactive`
([source_runner.py:56–60](../../../plcc-ng/src/plcc/cmd/source_runner.py#L56)). The blank-line
branch calls `_evaluate` but discards the return value; `buffer` and `prompt`
are unconditionally reset regardless of whether evaluation succeeded:

```python
elif not line.strip():                # blank line
    if buffer:
        self._evaluate(handler, buffer + line)  # return value ignored
        buffer = b""
        prompt = self._prompt
```

The normal-line branch (lines 63–67) correctly checks the return value and
keeps the continuation prompt when evaluation returns `False`. The blank-line
branch should do the same — or at minimum surface an error to the user when
evaluation fails.

- Same test grammar as issues CR-19
  and CR-20.
- Related to issue CR-19: even once
  this issue is fixed and an error is shown, the error message itself may be
  the unfriendly JSON-format output described there.

Migrated from plcc-ng #021.
<!-- SECTION:DESCRIPTION:END -->
