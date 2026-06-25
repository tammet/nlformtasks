# Run `t5-prooflen-existfold` — folio, 2026-06-20

**Auxiliary run.** Table 5 FOLIO existential collapse.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/folio/folio_tests.py` (run against `llmpipe/tests/tests_folio_v2.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_folio_v2.py -llm <llm> -existfold -nocrossstage`
- Post-translation flags: `-existfold -nocrossstage` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| claude | claude-sonnet-4-6 | 116 | 85 | 2 | 57.1% |

Regenerate this table: `python3 eval/summarize.py outputs/folio/t5-prooflen-existfold/2026-06-20 --tests tests/folio/folio_tests.py`
