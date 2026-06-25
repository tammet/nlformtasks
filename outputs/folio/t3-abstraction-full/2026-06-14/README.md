# Run `t3-abstraction-full` — folio, 2026-06-14

**Primary run.** Table 3: FOLIO abstraction (best row); primary FOLIO result.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/folio/folio_tests.py` (run against `llmpipe/tests/tests_folio_v2.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_folio_v2.py -llm <llm> -prenorm -ultracoarse`
- Post-translation flags: `-prenorm -ultracoarse` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| gpt | gpt-5.1 | 132 | 71 | 0 | 65.0% |
| claude | claude-sonnet-4-6 | 143 | 58 | 2 | 70.4% |
| gemini | gemini-2.5-flash | 136 | 63 | 4 | 67.0% |
| deepseek | deepseek-v4-flash | 108 | 65 | 30 | 53.2% |

Regenerate this table: `python3 eval/summarize.py outputs/folio/t3-abstraction-full/2026-06-14 --tests tests/folio/folio_tests.py`
