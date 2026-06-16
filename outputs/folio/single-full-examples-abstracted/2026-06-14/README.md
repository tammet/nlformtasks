# Run `single-full-examples-abstracted` — folio, 2026-06-14

**Auxiliary run.** Primary folio result: `outputs/folio/two-stage-abstracted/2026-06-14`.

Contrast; primary FOLIO pipeline result is outputs/folio/two-stage-abstracted/2026-06-14.

## How this run was made

- Pipeline: `https://github.com/tammet/nlpsolver` @ tag `folio-2026-06-14` (commit `1d7b54a`)
- Test file: `tests/folio/folio_tests.py`
- Command:
  ```
  python3 runtests.py tests/tests_folio_v2.py -llms <llm> -combined-instr prompts/combined_v2_instructions_full.txt -combined-examples prompts/combined_examples_pure.txt -ultracoarse -prenorm -tag combinedfull_ultracoarse_prenorm_v4 -sequential
  ```
- System prompts assembled from `prompts/`:
  - `combined_v2_instructions_full.txt`
  - `combined_examples_pure.txt`
  - `prenorm_full.txt`
- Static axioms: snapshot in `axioms_std.js`; encoding scheme in `ENCODINGS.md`.

## Results

| LLM | model | accuracy | pass / total |
|---|---|---:|---:|
| gpt | gpt-5.1 | 66.0% | 134 / 203 |
| claude | claude-sonnet-4-6 | 67.0% | 136 / 203 |
| gemini | gemini-2.5-flash | 61.6% | 125 / 203 |
| deepseek | deepseek-v4-flash | 55.2% | 112 / 203 |

Accuracy is graded against each case's expected value (`correctness`). Counting:
a case passes iff `correctness` is true; null/empty/error answers count as wrong.

## Contents

| path | what |
|---|---|
| `<llm>/case_*.json` | per-case input, expected, answer, correctness, stage1/2 JSON, clauses, prover command, proof |
| `<llm>/summary.json` | per-LLM pass/fail/error totals + failed-case list |
| `meta.json` | provenance: pipeline tag/commit, role, per-LLM model + totals + decoding |
| `provenance.json` | seed read by `eval/summarize.py` to (re)generate `meta.json` |
| `prompts/` | snapshot of the system-prompt components for this run |
| `axioms_std.js`, `ENCODINGS.md` | prover axiom + encoding-scheme snapshot |

Regenerate this run's tables: `python3 eval/summarize.py outputs/folio/single-full-examples-abstracted/2026-06-14 --write`.
