# nlformtasks

Natural-language → formal-logic test cases, LLM pipeline results, and analysis for the
`nlpsolver` semantic parser.

Each test case is an English problem (premises + a question) paired with an expected answer. The
cases are run through the LLM parser in nlpsolver, which translates English into first-order logic
and calls the `gk` theorem prover. This repository holds the cases and the recorded outputs, not
the pipeline code.

The repository's focus is the in-house **core** suite (1600 cases). It also holds a second,
third-party benchmark — **FOLIO** — used in the paper as a contrast; FOLIO is not our data (see
[`tests/folio/README.md`](tests/folio/README.md) for authorship, the introducing publication, the
upstream source, and its MIT license).

- Pipeline (the code that produces these answers): https://github.com/tammet/nlpsolver — the parser
  lives under `llmpipe/`. The exact pipeline state for each run is marked with a git tag there; see
  [REPRODUCE.md](REPRODUCE.md).

## What's here

```
tests/
  core/
    core_tests.py              # 1600 cases: [id, english, expected]
    core_tests_100.py          # curated 100-case all-LLMs-correct subset
    core_tests_challenging.py  # 341-case challenging subset (>=2 errors across the 16 grid cells)
  folio/
    folio_tests.py             # 203 FOLIO v2 validation items (third-party; original gold)
    source/                    # upstream FOLIO jsonl, verbatim, + provenance + MIT license
outputs/
  core/
    two-stage/2026-06-03/      # PRIMARY core result (the full two-stage pipeline)
    ablations/                 # auxiliary single-call pipeline shapes
      single-full-examples/...  single-minimal-examples/...  single-full-no-examples/...
  folio/
    two-stage-abstracted/2026-06-14/   # PRIMARY FOLIO pipeline result
    direct-answer/2026-06-12/          # reference: LLM verdict, no logic, no prover
    two-stage-standard/...  single-full-examples-standard/...  single-full-examples-abstracted/...
eval/
  summarize.py   # one run dir -> per-LLM / per-subsection tables + meta.json (no pipeline needed)
  matrix.py      # cross-run shape-by-model matrix; regenerates the paper tables
summaries/       # one pasteable markdown table per run
REPRODUCE.md  CHANGELOG.md  LICENSE
```

Run folders are named `outputs/<benchmark>/<shape>/<date>/`. Each carries its own `README.md`,
`meta.json` (pipeline tag/commit, role, per-LLM model + totals + decoding), a `prompts/` snapshot,
and — where a prover is used — an `axioms_std.js` + `ENCODINGS.md` snapshot, since prompts, axioms
and the encoding scheme all change over time. Each run's `meta.json` carries a `role`: `primary`
(the headline result), `auxiliary` (an ablation / contrast), or `reference` (no-prover baseline).

## Core results (1600 cases)

Answer accuracy (%) by pipeline shape × LLM. **Two-stage is the primary result;** the three
single-call shapes are ablations. Regenerate with
`python3 eval/matrix.py outputs/core --subset tests/core/core_tests_challenging.py`.

| pipeline shape | role | GPT | Claude | Gemini | DeepSeek |
|---|---|---:|---:|---:|---:|
| two-stage | primary | 97 | 99 | 98 | 99 |
| single-full-examples | aux | 93 | 96 | 95 | 95 |
| single-minimal-examples | aux | 95 | 95 | 93 | 93 |
| single-full-no-examples | aux | 83 | 91 | 87 | 88 |

On the **challenging subset** (341 cases missed ≥2× across the 16 grid cells) the spread widens:

| pipeline shape | GPT | Claude | Gemini | DeepSeek |
|---|---:|---:|---:|---:|
| two-stage | 90 | 96 | 95 | 96 |
| single-full-examples | 72 | 83 | 80 | 81 |
| single-minimal-examples | 79 | 82 | 73 | 75 |
| single-full-no-examples | 44 | 67 | 66 | 69 |

The core suite was built during development with the design goal that no case is failed by more
than one of the four LLMs under the full two-stage pipeline; that holds in the primary run (every
case correct for at least three of four). The 100-subset is stricter (all four correct on every
case).

## FOLIO results (203 validation items, third-party data)

**Two-stage-abstracted is the primary FOLIO pipeline result.** FOLIO is scored against its original
v2 gold (72 True / 62 False / 69 Unknown). Regenerate with `python3 eval/matrix.py outputs/folio`.

| configuration | role | GPT | Claude | Gemini | DeepSeek | Fable-5 |
|---|---|---:|---:|---:|---:|---:|
| two-stage-abstracted | primary | 65 | **70** | **67** | 53 | |
| direct answer (no logic) | reference | 69 | 67 | 86 | 86 | 91* |
| two-stage-standard | aux | 54 | 57 | 51 | 47 | |
| single-full-examples-standard | aux | 61 | 59 | 58 | 54 | |
| single-full-examples-abstracted | aux | **66** | 67 | 62 | **55** | |

`*` Fable-5 direct answer excludes 8 content refusals from the denominator (178/195 = 91%); the raw
figure in `outputs/folio/direct-answer/.../fable5/` is 178/203 = 88%. "Abstracted" = the pipeline's
`-ultracoarse -prenorm` mode (strips defeasible blockers, tense/world senses, Davidsonian event
structure), designed to match FOLIO's flat first-order style. The "direct answer" reference (one
LLM verdict, no logic, no prover) beats every pipeline variant for GPT/Gemini/DeepSeek — on this
benchmark the formalization step is net-negative.

## How a run is produced

For each `(case, LLM)` the pipeline runs five stages:

1. Stage 1 (LLM): English → abstract semantic units.
2. Stage 2 (LLM): semantic units → first-order-logic JSON.
3. Stage 3 (pipeline code): the Stage-2 JSON is rewritten and extended — structural repair,
   context/tense injection, FOL→CNF clausification, dynamic axiom injection — before the prover.
4. Stage 4 (`gk` prover): the resulting clauses plus the static axioms (`axioms_std.js`) are run.
5. Stage 5 (pipeline code): the proof is post-processed into an English answer, graded against the
   case's expected value.

The single-call shapes collapse Stages 1–2 into one LLM call (no Stage-1 artifact); the direct-answer
reference is a single LLM call with no Stages 3–5. Only the LLM stages call an API, and those answers
are served from the pipeline's SQLite cache, so a run is deterministic for a given pipeline commit and
model set. Exact reproduction steps and the nlpsolver commit per run are in [REPRODUCE.md](REPRODUCE.md).

A new run goes into a new `outputs/<benchmark>/<shape>/<date>/` folder rather than overwriting an
existing one.

## License

Apache License 2.0 — see [LICENSE](LICENSE). Same license as the nlpsolver repository
(https://github.com/tammet/nlpsolver). The third-party FOLIO files under `tests/folio/` remain under
their upstream MIT license (`tests/folio/source/UPSTREAM_LICENSE`).
