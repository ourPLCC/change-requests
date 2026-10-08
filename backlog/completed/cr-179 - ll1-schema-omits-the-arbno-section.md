---
id: CR-179
title: 'll1 schema omits the arbno section'
status: Done
assignee: []
created_date: '2026-07-29'
labels: []
dependencies: []
type: fix
project: plcc-ng
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
`plcc-ll1` always emits a top-level `arbno` key — an object keyed by
repetition-rule (`**=`) nonterminal, `{}` when the grammar has none —
but [ll1.schema.json](../../../plcc-ng/src/plcc/schemas/ll1.schema.json) never
mentions it. It is absent from both `required` and `properties`.

Because no schema in `src/plcc/schemas/` sets
`additionalProperties: false`, the undeclared key is silently accepted.
Every `check-jsonschema --schemafile ll1.schema.json` call in the test
suite therefore validates the whole `arbno` section as "anything goes":
a malformed, truncated, or entirely wrong-shaped `arbno` passes.

This is the section that carries repetition-rule parse data — the `rhs`
symbol list, the separator, and the computed `lookahead`. Issue CR-174's
bug lived precisely there (a non-capturing terminal dropped from `rhs`,
and a `lookahead` computed from the wrong symbol), and schema validation
could not have caught it.

### Steps to Reproduce

1. Run a grammar with a repetition rule through the pipeline:
   ```bash
   plcc-spec tests/fixtures/arbno-mid-body-terminal.plcc | plcc-ll1
   ```
2. Observe the top-level `arbno` key in the output:
   ```json
   "arbno": {
     "Decls": {
       "rhs": [
         { "field": "symbolList", "symbol": "SYMBOL", "is_terminal": true },
         { "field": null, "symbol": "EQUALS", "is_terminal": true },
         { "field": "expList", "symbol": "Exp", "is_terminal": false }
       ],
       "separator": null,
       "lookahead": ["SYMBOL"]
     }
   }
   ```
3. Grep `src/plcc/schemas/ll1.schema.json` for `arbno` — no match.
4. Delete `arbno.Decls.lookahead` from the output and validate it against
   the schema. It still passes.

### Notes

- Shape to declare: `arbno` is an object whose additional properties are
  objects with `rhs`, `separator`, and `lookahead`. `rhs` is an array of
  `{symbol: string, field: string|null, is_terminal: boolean}`;
  `separator` is `string|null`; `lookahead` is an array of strings.
- `arbno` is always emitted (as `{}` for non-repetition grammars), so it
  belongs in the top-level `required` list alongside the other keys, not
  as an optional property.
- Do **not** add `additionalProperties: false` while fixing this. None of
  the five schemas in `src/plcc/schemas/` use it; adding it here would be
  an unrelated tightening with its own blast radius.
- Whatever fix lands needs a negative test — feed real `plcc-ll1` output
  with a required `arbno` field removed to `check-jsonschema` and assert
  it is rejected. Without that, the new schema clause has no proof it
  constrains anything.
- Split out of CR-176,
  which stays test-only. See CR-180
  for the same class of gap in the `conflicts` section.

Migrated from plcc-ng #179.
<!-- SECTION:DESCRIPTION:END -->
