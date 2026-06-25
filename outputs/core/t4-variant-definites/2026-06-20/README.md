# Run `t4-variant-definites` — core, 2026-06-20

**Auxiliary run.** Table 4: Definite-description terms.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/core/core_tests.py` (run against `llmpipe/tests/tests_core.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_core.py -llm <llm> -definites`
- Post-translation flags: `-definites` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| gpt | gpt-5.1 | 1554 | 44 | 2 | 97.1% |
| claude | claude-sonnet-4-6 | 1581 | 19 | 0 | 98.8% |
| gemini | gemini-2.5-flash | 1568 | 32 | 0 | 98.0% |
| deepseek | deepseek-v4-flash | 1576 | 23 | 1 | 98.5% |

Regenerate this table: `python3 eval/summarize.py outputs/core/t4-variant-definites/2026-06-20 --tests tests/core/core_tests.py`
