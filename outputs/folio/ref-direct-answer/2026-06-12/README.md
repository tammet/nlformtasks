# Run `ref-direct-answer` — folio, 2026-06-12

**Reference run.** Reference: LLM answers the FOLIO question directly, no logic and no prover. Source of the Section-4 direct-answer percentages (incl. Fable-5).

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/folio/folio_tests.py` (run against `llmpipe/tests/tests_folio_v2.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_folio_v2.py -llm <llm> -directanswer <prompt-file>`
- Post-translation flags: `(none — default two-stage)` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| gpt | gpt-5.1 | 140 | 63 | 0 | 69.0% |
| claude | claude-sonnet-4-6 | 137 | 66 | 0 | 67.5% |
| gemini | gemini-2.5-flash | 175 | 28 | 0 | 86.2% |
| deepseek | deepseek-v4-flash | 174 | 29 | 0 | 85.7% |
| fable5 | claude-fable-5 | 178 | 25 | 0 | 87.7% |

Regenerate this table: `python3 eval/summarize.py outputs/folio/ref-direct-answer/2026-06-12 --tests tests/folio/folio_tests.py`
