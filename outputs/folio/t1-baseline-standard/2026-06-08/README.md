# Run `t1-baseline-standard` — folio, 2026-06-08

**Auxiliary run.** Table 1: FOLIO baseline (standard two-stage).

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/folio/folio_tests.py` (run against `llmpipe/tests/tests_folio_v2.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_folio_v2.py -llm <llm>`
- Post-translation flags: `(none — default two-stage)` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| gpt | gpt-5.1 | 109 | 93 | 1 | 53.7% |
| claude | claude-sonnet-4-6 | 115 | 87 | 1 | 56.6% |
| gemini | gemini-2.5-flash | 104 | 91 | 8 | 51.2% |
| deepseek | deepseek-v4-flash | 95 | 69 | 39 | 46.8% |

Regenerate this table: `python3 eval/summarize.py outputs/folio/t1-baseline-standard/2026-06-08 --tests tests/folio/folio_tests.py`
