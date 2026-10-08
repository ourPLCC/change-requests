---
id: CR-186
title: 'plcc-rep deadlocks on a partial stdout line'
status: To Do
assignee: []
created_date: '2026-08-11'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A semantic action that writes a partial line (no trailing newline) to
stdout deadlocks `plcc-rep` with no diagnostic: no stdout, no stderr, no
exit.

`plcc-rep` runs the generated program as a subprocess and treats its stdout
as a private, line-oriented JSON channel.
[`_read_response`](../../../plcc-ng/src/plcc/cmd/rep.py) reads one line at a time; a
line that fails to parse as JSON (or parses to something without a `kind`)
is printed verbatim and the loop continues, waiting for the next line:

```python
line = raw.decode('utf-8', errors='replace').rstrip('\n')
try:
    record = json.loads(line)
except json.JSONDecodeError:
    print(line)
    continue
```

That works when the stray text ends in a newline — the result record
arrives intact on the next `readline()`. It does not work for a partial
line: the unterminated text merges with the following JSON result line into
one unparseable line, which is printed (destroying the result record), and
`readline()` then blocks forever waiting for a result that will never come.

Measured in both the Python and JavaScript targets, via stdin and via a
`SOURCE` file: `timeout` reports exit 124, with no stdout and no stderr —
the worst available failure mode, since nothing tells the caller what
happened. A student who puts a `print` (or the target-language equivalent)
in a semantic action and forgets the trailing newline gets a hang with no
message, indistinguishable from an infinite loop in their own program.

Note that the newline-terminated case survives only through the
unparseable-line fallback above, which is an accident of the implementation
rather than a supported output channel. It happens to print the raw line
before the real result, which fakes the interleaving a language's `display`
would want.

### Steps to Reproduce

1. A spec whose semantic action for some expression writes a partial line,
   e.g. `sys.stdout.write("7")` with no trailing `\n`.
2. `echo '<partial-write expression>' | timeout 5 plcc-rep`
3. Actual: exit 124, no output at all. Expected: either the partial write is
   surfaced, or `plcc-rep` reports the malformed channel — anything other
   than hanging silently.

### Notes

The narrow fix is for `_read_response` to stop treating an unbounded
`readline()` as acceptable: read incrementally, or bound the wait, or at
minimum detect that the subprocess has gone idle with unterminated data
buffered and report it. Whatever the mechanism, the requirement is that a
partial-line write produce a message rather than a hang.

The wider fix is issue CR-187:
give semantic actions a supported `output` record kind, so nothing they emit
travels as raw stdout in the first place. That would close this off at the
source, but the defensive handling here is still worth having on its own —
user code can always write to stdout directly.

Found while migrating a course language whose `display`, `display#`, `putc`,
`puts`, and `newline` primitives are partial-line writers by design (a
trailing newline is exactly what its separate `newline` expression is for).
That port works around this by buffering all output and returning it as part
of `_run()`'s result rather than writing it directly — a workaround with its
own cost, described in CR-187.

Migrated from plcc-ng #186.
<!-- SECTION:DESCRIPTION:END -->
