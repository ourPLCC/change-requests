---
id: CR-198
title: 'Grammar class names can collide with files plcc-ng generates'
status: To Do
assignee: []
created_date: '2026-10-06'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Each emitter writes author-named modules (one per grammar class, plus
standalone `file`-kind fragments) into the same directory as files plcc-ng
owns: the entry point, `_Start`, and the runtime. Nothing keeps the two name
spaces apart, so an ordinary grammar class name can overwrite or shadow a
plcc-ng file.

The semantic validator already requires every locator name to match
`^[A-Z]`, which rules out collisions with lowercase names (`main.py`,
`runtime/`, `_Start`) on case-sensitive filesystems. It does not help where
plcc-ng's own names are capitalized:

| Target | plcc-ng writes | Collides with | Effect |
| --- | --- | --- | --- |
| Java | `Main.java` (entry point) | `<Main>` | AST class overwritten; `javac` fails |
| Java | `import runtime.Token` | `<Token>` | `Token is already defined in this compilation unit` |
| Haskell | `Main.hs` (entry point) | `<Main>` | AST module overwritten; entry point imports itself |
| Haskell | `Token.hs`, `LanguageError.hs` (runtime, copied flat) | `<Token>`, `<LanguageError>` | runtime module overwritten; AST module imports itself |
| Python | `main.py` | `<Main>` → `Main.py` | same file on case-insensitive filesystems (macOS, Windows defaults) — inferred, not reproduced |
| JavaScript | `main.js` | `<Main>` → `Main.js` | same as Python — inferred, not reproduced |

`Main` and `Token` are plausible non-terminal names in a student grammar, and
the failure surfaces as a compiler error about generated code the author never
wrote.

### Steps to Reproduce

```text
token NUM '\d+'
skip SPACE '\s+'
%
<Main> ::= <Token:t>
<Token> ::= <NUM:num>
%
Java
```

1. `plcc-make` with the spec above.
2. `javac` fails: `Token.java:4: error: Token is already defined in this
   compilation unit` and `Main.java:25: error: incompatible types: Node cannot
   be converted to Main`. `Main.java` contains only the entry point; the AST
   class is gone.
3. Change the language line to `Haskell` and rerun. `Main.hs` is the entry
   point and contains `import Main`; `Token.hs` is the AST module (`data Token
   = Token { num :: Token }`) and contains `import Token`. The runtime's
   `Token.hs` has been overwritten.

### Notes

#### Fix direction

This is an internal layout problem, and the fix should not become a rule the
author has to learn. The principle: **plcc-ng's own files live in a name space
that no legal author name can reach**, so collisions are impossible by
construction rather than detected and reported. The mechanism is per language:

- **Python, JavaScript, Java** — prefix plcc-ng-owned names with `_`
  (`_main.py`, `_runtime/`, `_Main.java`, …), following `_Start`. An author
  name must start with `[A-Z]`, so it cannot match a `_` name even
  case-insensitively. Java's runtime type references also need to stop
  importing simple names that a grammar class can shadow (qualify them, or
  move them under the `_`-prefixed package).
- **Haskell** — module names must start uppercase, so `_` is unavailable.
  Move the runtime into hierarchical modules (`Plcc.Token`,
  `Plcc.LanguageError`); an author name cannot contain a `.`.
- **Haskell `Main`** — reserved by the language itself: the executable's entry
  module must be `Main`, so a non-terminal `<Main>` cannot be supported under
  any file name. Report it through the existing reserved-words check
  ([`lang/reserved_words.py`](../../../plcc-ng/src/plcc/lang/reserved_words.py)), the
  same way a reserved field name is reported.

Renaming `main.py` and `runtime/` changes the generated layout. That is
accepted: nothing outside plcc-ng is known to refer to those names, and a
student pointed at `main.py` will find `_main.py` without difficulty.

#### Relationship to CR-195 and CR-197

Came out of the CR-197 discussion
about allowing a verbatim standalone module (`Helper:raw`) in
CR-195's single-module mode, where it would
sit beside `classes.py`, `main.py`, and `runtime/`. Those designs only need to
rely on the guarantee stated here — author-named modules never collide with
plcc-ng's files — and do not depend on this landing first. Under this fix
single-module's merged module would be named `_classes.py` in keeping with the
rule.

Migrated from plcc-ng #198.
<!-- SECTION:DESCRIPTION:END -->
