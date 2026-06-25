# Run `t3-variant-flat-guarddrop` — folio, 2026-06-20

**Auxiliary run.** Table 3: Lossy event simplification + guard removal.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/folio/folio_tests.py` (run against `llmpipe/tests/tests_folio_v2.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_folio_v2.py -llm <llm> -prenorm -flatevents -guarddrop`
- Post-translation flags: `-prenorm -flatevents -guarddrop` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| gpt | gpt-5.1 | 117 | 86 | 0 | 57.6% |
| claude | claude-sonnet-4-6 | 130 | 72 | 1 | 64.0% |
| gemini | gemini-2.5-flash | 118 | 81 | 4 | 58.1% |
| deepseek | deepseek-v4-flash | 101 | 73 | 29 | 49.8% |

Regenerate this table: `python3 eval/summarize.py outputs/folio/t3-variant-flat-guarddrop/2026-06-20 --tests tests/folio/folio_tests.py`
