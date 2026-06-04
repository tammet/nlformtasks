# nlformtasks

Natural-language → formal-logic test cases, LLM pipeline results, and analysis for the
`nlpsolver` semantic parser.

Each test case is an English problem (premises + a question) paired with an expected answer.
The cases are run through the LLM parser in nlpsolver, which translates English into first-order
logic and calls the `gk` theorem prover. This repository holds the cases and the recorded
outputs, not the pipeline code.

- Pipeline (the code that produces these answers): https://github.com/tammet/nlpsolver — the
  parser lives under `llmpipe/`.

## What's here

```
tests/
  core/
    core_tests.py        # 1600 cases: [id, english_text, expected_answer]
    core_tests_100.py    # curated 100-case subset (all four LLMs correct on every case)
    README.md            # what the set covers; expected-value semantics
outputs/
  core/
    2026-06-03_llmpipe/  # one run, self-describing
      README.md          # how the run was made + how each LLM was called + prompt mechanism
      meta.json          # pipeline commit, LLM model strings, per-LLM totals + decoding config
      ENCODINGS.md       # snapshot of the logic-encoding scheme used for this run
      axioms_std.js      # snapshot of the prover axiom file used for this run
      prompts/           # snapshot of the six prompt components fed to the LLMs
      claude/  gpt/  gemini/  deepseek/
        case_NNNN.json   # input, expected, answer, correctness, stage1/stage2, clauses, proof
        summary.json
eval/
  summarize.py           # self-contained: run dir -> per-LLM / per-subsection tables (no pipeline needed)
summaries/
  core/
    2026-06-03_llmpipe.md  # the pasteable results table for this run
REPRODUCE.md             # the nlpsolver commit used + exact commands to regenerate a run
CHANGELOG.md  LICENSE
```

A run folder carries its own `ENCODINGS.md`, `axioms_std.js`, and `prompts/` snapshot — the
encoding scheme, axioms, and prompts all change over time, so each run records the exact inputs
that produced its answers. See the run's own `README.md` for the rest.

## Results at a glance (run `2026-06-03_llmpipe`, 1600 core cases)

| LLM | model | accuracy |
|---|---|---:|
| claude | claude-sonnet-4-6 | 98.9% |
| deepseek | deepseek-v4-flash | 98.6% |
| gemini | gemini-2.5-flash | 97.9% |
| gpt | gpt-5.1 | 97.2% |

The core set was built during development and debugging of the parser, with one of the design
goals being that no case should be failed by more than one of the four LLMs. That holds in this
run — every case is answered correctly by at least three of the four. The 100-case subset is
stricter: all four are correct on every case.

See `summaries/core/2026-06-03_llmpipe.md` for the full per-subsection breakdown, or regenerate
any table with `python3 eval/summarize.py outputs/core/<run-id> --tests tests/core/core_tests.py`.

## How a run is produced

For each `(case, LLM)` the pipeline runs five stages:

1. Stage 1 (LLM): English → abstract semantic units.
2. Stage 2 (LLM): semantic units → first-order-logic JSON.
3. Stage 3 (pipeline code): the Stage-2 JSON is rewritten and extended — structural repair,
   context/tense injection, FOL→CNF clausification, dynamic axiom injection — before reaching the
   prover. Much of what the prover sees is added here, not emitted by the LLM.
4. Stage 4 (`gk` prover): the resulting clauses plus the static axioms (`axioms_std.js`) are run.
5. Stage 5 (pipeline code): the proof is post-processed into an English answer, which is graded
   against the case's expected value.

Only Stages 1 and 2 call the LLM. The recorded LLM answers come from the pipeline's SQLite
response cache, so a run is deterministic for a given pipeline commit and model set. Exact
reproduction steps and the nlpsolver commit used are in [REPRODUCE.md](REPRODUCE.md).

A new run goes into a new `outputs/<set>/<run-id>/` folder rather than overwriting an existing
one. Test-set versions are tracked with git tags, not directories.

## License

Apache License 2.0 — see [LICENSE](LICENSE). Same license as the nlpsolver repository
(https://github.com/tammet/nlpsolver).
