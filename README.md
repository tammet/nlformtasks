# nlformtasks

Natural-language → formal-logic **test cases**, **LLM pipeline results**, and **analysis**
for the `nlpsolver` semantic parser.

Each test case is an English problem (premises + a question) paired with an expected answer.
The cases are run through the two-stage LLM parser in `nlpsolver/llmpipe`, which translates
English into first-order logic and calls the `gk` theorem prover. This repository holds the
**cases and the recorded outputs** — not the pipeline code.

- **Pipeline (the code that produces these answers):** https://github.com/tammet/nlpsolver
  (the parser lives under `llmpipe/`). *A back-link from that repository to this one is planned.*

## What's here

```
tests/
  core/
    core_tests.py        # 1600 cases: [id, english_text, expected_answer]
    core_tests_100.py    # curated 100-case subset (all four LLMs correct on every case)
    README.md            # what the set covers; expected-value semantics
outputs/
  core/
    2026-06-03_llmpipe/  # one immutable run
      meta.json          # pipeline commit, LLM model strings, per-LLM totals
      MANIFEST.json      # compact case_id -> [claude, gpt, gemini, deepseek] verdicts
      claude/  gpt/  gemini/  deepseek/
        case_NNNN.json   # input, expected, answer, correctness, stage1/stage2, clauses, proof
        summary.json
eval/
  summarize.py           # self-contained: run dir -> per-LLM / per-subsection tables (no pipeline needed)
summaries/
  core/
    2026-06-03_llmpipe.md  # the pasteable results table for this run
ENCODINGS.md             # logic-encoding reference, synced from the pipeline repo
REPRODUCE.md             # pinned commit + exact commands to regenerate a run
CHANGELOG.md  LICENSE
```

## Results at a glance (run `2026-06-03_llmpipe`, 1600 core cases)

| LLM | model | accuracy |
|---|---|---:|
| claude | claude-sonnet-4-6 | 98.9% |
| deepseek | deepseek-v4-flash | 98.6% |
| gemini | gemini-2.5-flash | 97.9% |
| gpt | gpt-5.1 | 97.2% |

See `summaries/core/2026-06-03_llmpipe.md` for the full per-subsection breakdown, or regenerate
any table with `python3 eval/summarize.py outputs/core/<run-id> --tests tests/core/core_tests.py`.

## How a run is produced

For each `(case, LLM)` the pipeline parses the English to logic and runs the prover; the answer
is graded against the case's expected value. The recorded LLM answers come from the pipeline's
SQLite response cache, so a run is deterministic for a given pipeline commit and model set.
Exact reproduction steps and the pinned pipeline commit are in [REPRODUCE.md](REPRODUCE.md).

Runs are **immutable**: a new run goes into a new `outputs/<set>/<run-id>/` folder, never a
rewrite of an existing one. Test-set versions are tracked with **git tags**, not directories.

## License

Apache License 2.0 — see [LICENSE](LICENSE). Same license as the `nlpsolver` repository.
