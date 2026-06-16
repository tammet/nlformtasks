# Run `single-minimal-examples` — core, 2026-06-07

**Auxiliary run.** Primary core result: `outputs/core/two-stage/2026-06-03`.

Ablation; headline core result is outputs/core/two-stage/2026-06-03.

## How this run was made

- Pipeline: `https://github.com/tammet/nlpsolver` — **not separately tagged**. Not separately tagged. The answer-affecting compiler, axioms and prover are identical to core-2026-06-03 (585e8b0). These single-call shapes differ only in prompt assembly — one merged LLM call instead of two, an additive path added after that tag; the combined prompt files are snapshotted from folio-2026-06-14.
- Test file: `tests/core/core_tests.py`
- Command:
  ```
  python3 runtests.py tests/tests_core.py -llms <llm> -combined-instr prompts/combined_minimal_instructions_full.txt -combined-examples prompts/combined_examples_pure.txt -combined-tag minimal_pure -sequential
  ```
- System prompts assembled from `prompts/`:
  - `combined_minimal_instructions_full.txt`
  - `combined_examples_pure.txt`
- Static axioms: snapshot in `axioms_std.js`; encoding scheme in `ENCODINGS.md`.
- Re-scored on the challenging subset (`tests/core/core_tests_challenging.py`) via `eval/summarize.py --subset`.


## Results

| LLM | model | accuracy | pass / total |
|---|---|---:|---:|
| gpt | gpt-5.1 | 94.9% | 1519 / 1600 |
| claude | claude-sonnet-4-6 | 95.4% | 1527 / 1600 |
| gemini | gemini-2.5-flash | 93.0% | 1488 / 1600 |
| deepseek | deepseek-v4-flash | 93.2% | 1492 / 1600 |

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

Regenerate this run's tables: `python3 eval/summarize.py outputs/core/ablations/single-minimal-examples/2026-06-07 --write`.
