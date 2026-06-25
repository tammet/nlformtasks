# Run `t4-variant-entitymerge` — core, 2026-06-20

**Auxiliary run.** Table 4: Entity merging.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/core/core_tests.py` (run against `llmpipe/tests/tests_core.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_core.py -llm <llm> -entitymerge`
- Post-translation flags: `-entitymerge` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| gpt | gpt-5.1 | 1555 | 43 | 2 | 97.2% |
| claude | claude-sonnet-4-6 | 1582 | 18 | 0 | 98.9% |
| gemini | gemini-2.5-flash | 1563 | 37 | 0 | 97.7% |
| deepseek | deepseek-v4-flash | 1569 | 30 | 1 | 98.1% |

Regenerate this table: `python3 eval/summarize.py outputs/core/t4-variant-entitymerge/2026-06-20 --tests tests/core/core_tests.py`
