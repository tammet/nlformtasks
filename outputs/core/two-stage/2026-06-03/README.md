# Run `two-stage` — core, 2026-06-03

**Primary core result.** This is the headline core run.

Headline core result (full two-stage pipeline).

## How this run was made

- Pipeline: `https://github.com/tammet/nlpsolver` @ tag `core-2026-06-03` (commit `585e8b0`)
- Test file: `tests/core/core_tests.py`
- Command:
  ```
  python3 runtests.py tests/tests_core.py -llms claude,gpt,gemini,deepseek -sequential
  ```
- System prompts assembled from `prompts/`:
  - `stage1_instructions_full.txt`
  - `stage1_examples.txt`
  - `stage1_checklist_full.txt`
  - `stage2_instructions_full.txt`
  - `stage2_examples.txt`
  - `stage2_checklist_full.txt`
- Static axioms: snapshot in `axioms_std.js`; encoding scheme in `ENCODINGS.md`.
- Re-scored on the challenging subset (`tests/core/core_tests_challenging.py`) via `eval/summarize.py --subset`.


## Results

| LLM | model | accuracy | pass / total |
|---|---|---:|---:|
| gpt | gpt-5.1 | 97.2% | 1555 / 1600 |
| claude | claude-sonnet-4-6 | 98.9% | 1582 / 1600 |
| gemini | gemini-2.5-flash | 97.9% | 1567 / 1600 |
| deepseek | deepseek-v4-flash | 98.6% | 1577 / 1600 |

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

Regenerate this run's tables: `python3 eval/summarize.py outputs/core/two-stage/2026-06-03 --write`.
