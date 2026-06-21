# Run `t4-variant-flat-guarddrop` — core, 2026-06-20

**Auxiliary run.** Table 4: Lossy event simplification + guard removal.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/core/core_tests.py` (run against `llmpipe/tests/tests_core.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_core.py -llm <llm> -flatevents -guarddrop`
- Post-translation flags: `(none — default two-stage)` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| gpt | gpt-5.1 | 1457 | 142 | 1 | 91.1% |
| claude | claude-sonnet-4-6 | 1483 | 117 | 0 | 92.7% |
| gemini | gemini-2.5-flash | 1465 | 135 | 0 | 91.6% |
| deepseek | deepseek-v4-flash | 1455 | 144 | 1 | 90.9% |

Regenerate this table: `python3 eval/summarize.py outputs/core/t4-variant-flat-guarddrop/2026-06-20 --tests tests/core/core_tests.py`
