# Run `direct-answer` — folio, 2026-06-12

**Reference run** (no logic, no prover). Primary folio pipeline result: `outputs/folio/two-stage-abstracted/2026-06-14`.

Reasoning ceiling: one direct LLM verdict, no logic, no prover. Primary FOLIO pipeline result is outputs/folio/two-stage-abstracted/2026-06-14.

## How this run was made

- Pipeline: `https://github.com/tammet/nlpsolver` @ tag `folio-2026-06-12` (commit `6831b29`)
- Test file: `tests/folio/folio_tests.py`
- Command:
  ```
  python3 runtests.py tests/tests_folio_v2.py -llms <llm> -directanswer prompts/folio_directanswer_instructions.txt -tag directanswer
  ```
- System prompts assembled from `prompts/`:
  - `folio_directanswer_instructions.txt`
- No prover or axioms are used in this run (a single direct LLM verdict).
- **Fable-5 column:** Fable-5 (claude-fable-5) direct answer, standard prompt. 8 benign FOLIO items are content refusals (empty response); the paper's Table-3 Fable column excludes them: 178/195 = 91%. Raw here (refusals counted as wrong) = 178/203 = 88%. A second probe with a no-world-knowledge prompt is recorded separately in the pipeline repo (folio_v2_directanswer_fable5_noworld, 182/203).


## Results

| LLM | model | accuracy | pass / total |
|---|---|---:|---:|
| gpt | gpt-5.1 | 69.0% | 140 / 203 |
| claude | claude-sonnet-4-6 | 67.5% | 137 / 203 |
| gemini | gemini-2.5-flash | 86.2% | 175 / 203 |
| deepseek | deepseek-v4-flash | 85.7% | 174 / 203 |
| fable5 | claude-fable-5 | 87.7% | 178 / 203 |

Accuracy is graded against each case's expected value (`correctness`). Counting:
a case passes iff `correctness` is true; null/empty/error answers count as wrong.

## Contents

| path | what |
|---|---|
| `<llm>/case_*.json` | per-case input, expected, answer, correctness, raw verdict |
| `<llm>/summary.json` | per-LLM pass/fail/error totals + failed-case list |
| `meta.json` | provenance: pipeline tag/commit, role, per-LLM model + totals + decoding |
| `provenance.json` | seed read by `eval/summarize.py` to (re)generate `meta.json` |
| `prompts/` | snapshot of the system-prompt components for this run |


Regenerate this run's tables: `python3 eval/summarize.py outputs/folio/direct-answer/2026-06-12 --write`.
