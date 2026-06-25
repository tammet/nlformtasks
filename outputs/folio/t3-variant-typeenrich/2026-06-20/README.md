# Run `t3-variant-typeenrich` — folio, 2026-06-20

**Auxiliary run.** Table 3: Extra type/class atoms.

## How this run was made
- Pipeline: `nlpsolver` @ git tag **`lpar-2026-06-22`** (reproduce at this tag; `main` will have moved on)
- Test file: `tests/folio/folio_tests.py` (run against `llmpipe/tests/tests_folio_v2.py` in the pipeline repo)
- Command: `python3 runtests.py tests/tests_folio_v2.py -llm <llm> -prenorm -typeenrich`
- Post-translation flags: `-prenorm -typeenrich` — see `../../../pipeline-snapshot/ENCODINGS.md` §6
- Prompts: default two-stage, snapshot in `../../../pipeline-snapshot/prompts/`
- Static axioms + encoding scheme: `../../../pipeline-snapshot/axioms_std.js`, `../../../pipeline-snapshot/ENCODINGS.md`

Each `<llm>/case_NNNN.json` holds the full record: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1`, `stage2`, `clauses` (generated clauses),
`gk_command` (prover input) and `proof` (prover output).

## Results
| LLM | model | pass | fail | err | accuracy |
|---|---|--:|--:|--:|--:|
| gpt | gpt-5.1 | 132 | 68 | 3 | 65.0% |
| claude | claude-sonnet-4-6 | 124 | 78 | 1 | 61.1% |
| gemini | gemini-2.5-flash | 117 | 82 | 4 | 57.6% |
| deepseek | deepseek-v4-flash | 103 | 71 | 29 | 50.7% |

Regenerate this table: `python3 eval/summarize.py outputs/folio/t3-variant-typeenrich/2026-06-20 --tests tests/folio/folio_tests.py`
