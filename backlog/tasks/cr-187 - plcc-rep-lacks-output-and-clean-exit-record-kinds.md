---
id: CR-187
title: 'plcc-rep lacks output and clean-exit record kinds'
status: To Do
assignee: []
created_date: '2026-08-11'
labels: []
dependencies: []
type: feat
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Semantic actions have no supported way to emit user-visible output, and no
way to end the session cleanly. Both are missing record kinds in
`plcc-rep`'s protocol.

[`_render_record`](../../../plcc-ng/src/plcc/cmd/rep.py) already dispatches on
`record['kind']` — `result`, `error`, `specification_error`, and anything
else is a hard error — so the shape of the fix is a new record kind handled
there, plus a hook in each target runtime that lets `_run()` emit it. Two
gaps this would close:

1. **Output.** There is no record kind for "the program printed this."
   Writing directly to stdout collides with `plcc-rep`'s use of stdout as
   its own JSON channel, and hangs outright on a partial line (issue
   CR-186). The only way out
   today is to buffer everything a semantic action would have printed and
   fold it into `_run()`'s returned value. An `output` record kind, emitted
   as each write happens rather than buffered and flushed at the end, would
   let output interleave with results the way old PLCC's `rep` did, and
   would remove the need for that workaround entirely.

2. **Clean exit.** There is no record kind for "the program is
   intentionally done." A language with an `exit` expression calls the
   target language's process-exit function, which — because `plcc-rep` runs
   the generated program as a subprocess — closes the pipe mid-protocol.
   Measured:

   ```
   $ printf 'display 1\nexit\ndisplay 2\n' | plcc-rep
   1nil                                          # stdout
   plcc-rep: interpreter exited unexpectedly     # stderr
   $ echo $?
   1
   ```

   Under old PLCC, `rep` *was* the process, so this was a clean quit with
   status 0. Under plcc-ng a deliberate quit reads as a crash: wrong stderr
   message, wrong exit status, for want of a `session-end` (or similar)
   record the subprocess could emit before exiting.

### Second symptom: the buffering workaround swallows output when evaluation raises

Measured on the Python target, in a port using the buffered-output
workaround from (1):

```
$ printf '{display 1 ; error "boom"}\n' | plcc-rep
[98,111,111,109]
```

The `1` is gone. Old PLCC's `System.out.print` had already written it to
stdout by the time the exception was thrown; a buffer standing in for
stdout is discarded along with the statement. A definition whose right-hand
side raises loses its output the same way.

That is not a defect in the workaround — it is what the workaround costs.
Buffering is only necessary because there is no supported channel, and the
one alternative that would preserve the output (writing to stdout as it is
produced) is exactly what deadlocks the tool. An `output` record kind
removes the trade-off: each write emits its record the moment it runs, so an
error later in the same statement cannot retroactively swallow it, and
nothing has to be held until `_run` returns.

It is worth recording as a distinct symptom because it changes observable
language behavior, where the deadlock only changes failure mode.

### Notes

Both additions are protocol changes, so they touch every target runtime
(Python, Java, JavaScript, Haskell) as well as `_render_record`, and they
belong in [docs/language-guide/](../../../plcc-ng/docs/language-guide) once the
record kinds are documented. `_wait_for_ready`'s `ready` record is the
precedent for a non-`result` kind flowing across the same channel.

Cross-links issue CR-186, the
partial-line deadlock this same addition would also close off, since output
would travel through a typed record instead of raw stdout.

Found while migrating a course language whose `display` family and `exit`
expression need exactly these two channels. That port does not block on
this: the buffered-output workaround ships, and `exit`'s status-code
divergence ships as-is with a comment in each spec explaining it, since
`exit` is used by no example programs and no tests.

Migrated from plcc-ng #187.
<!-- SECTION:DESCRIPTION:END -->
