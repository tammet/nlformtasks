# Run `t5-prooflen-davidson-existfold` — core, 2026-06-20

**Auxiliary run.** Table 5 NLFT both folds.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/core/core_tests.py` (run against `llmpipe/tests/tests_core.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_core.py -llm <llm> -davidson -existfold -nocrossstage`
- Post-translation flags: `-davidson -existfold -nocrossstage` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| claude | claude-sonnet-4-6 | 1558 | 42 | 0 | 97.4% |

Regenerate this table: `python3 eval/summarize.py outputs/core/t5-prooflen-davidson-existfold/2026-06-20 --tests tests/core/core_tests.py`
