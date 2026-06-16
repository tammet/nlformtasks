# Run `two-stage-abstracted` — folio, 2026-06-14

**Primary folio result.** This is the headline folio run.

Primary FOLIO pipeline result (two-stage, abstracted: -ultracoarse -prenorm).

## How this run was made

- Pipeline: `https://github.com/tammet/nlpsolver` @ tag `folio-2026-06-14` (commit `1d7b54a`)
- Test file: `tests/folio/folio_tests.py`
- Command:
  ```
  python3 runtests.py tests/tests_folio_v2.py -llms <llm> -ultracoarse -prenorm -tag ultracoarse_prenorm_v4 -sequential  (gemini/deepseek add -nocrossstage)
  ```
- System prompts assembled from `prompts/`:
  - `stage1_instructions_full.txt`
  - `stage1_examples.txt`
  - `stage1_checklist_full.txt`
  - `stage2_instructions_full.txt`
  - `stage2_examples.txt`
  - `stage2_checklist_full.txt`
  - `prenorm_full.txt`
- Static axioms: snapshot in `axioms_std.js`; encoding scheme in `ENCODINGS.md`.

## Results

| LLM | model | accuracy | pass / total |
|---|---|---:|---:|
| gpt | gpt-5.1 | 65.0% | 132 / 203 |
| claude | claude-sonnet-4-6 | 70.4% | 143 / 203 |
| gemini | gemini-2.5-flash | 67.0% | 136 / 203 |
| deepseek | deepseek-v4-flash | 53.2% | 108 / 203 |

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

Regenerate this run's tables: `python3 eval/summarize.py outputs/folio/two-stage-abstracted/2026-06-14 --write`.
