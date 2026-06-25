# Run `t4-diag-typeenrich-noplural` — core, 2026-06-20

**Auxiliary run.** Section-5 diagnostic: with only the plural-to-singular sub-injector disabled, Claude goes 91.2% -> 98.1% on NLFT.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/core/core_tests.py` (run against `llmpipe/tests/tests_core.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_core.py -llm <llm> -typeenrich  (env TE_SKIP=plural)`
- Post-translation flags: `-typeenrich  (env TE_SKIP=plural)` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| claude | claude-sonnet-4-6 | 1569 | 31 | 0 | 98.1% |

Regenerate this table: `python3 eval/summarize.py outputs/core/t4-diag-typeenrich-noplural/2026-06-20 --tests tests/core/core_tests.py`
