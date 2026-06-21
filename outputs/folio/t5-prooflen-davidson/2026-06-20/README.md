# Run `t5-prooflen-davidson` — folio, 2026-06-20

**Auxiliary run.** Table 5 FOLIO compact Davidsonian. Corrected clausify build.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/folio/folio_tests.py` (run against `llmpipe/tests/tests_folio_v2.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_folio_v2.py -llm <llm> -davidson -nocrossstage`
- Post-translation flags: `(none — default two-stage)` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| gpt | gpt-5.1 | 114 | 88 | 1 | 56.2% |
| claude | claude-sonnet-4-6 | 117 | 84 | 2 | 57.6% |
| gemini | gemini-2.5-flash | 104 | 93 | 6 | 51.2% |
| deepseek | deepseek-v4-flash | 44 | 35 | 13 | 47.8% |

Regenerate this table: `python3 eval/summarize.py outputs/folio/t5-prooflen-davidson/2026-06-20 --tests tests/folio/folio_tests.py`
