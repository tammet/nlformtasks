# Run `2026-06-03_llmpipe` — core test set

One run of the 1600-case core set through the nlpsolver pipeline
(https://github.com/tammet/nlpsolver), with all four LLMs. This folder carries the exact inputs
that produced these answers (prompts, axioms, encoding scheme) alongside the outputs, because all
of those change over time.

The core set was built and curated during development and debugging of the parser. One design
goal was that no case should be failed by more than one of the four LLMs; in this run that holds —
every case is answered correctly by at least three of the four models.

## Contents

| path | what |
|---|---|
| `claude/ gpt/ gemini/ deepseek/` | per-case results: `case_NNNN.json` (input, expected, answer, correctness, stage-1/2 JSON, clauses, prover command, proof) + `summary.json` |
| `meta.json` | machine-readable provenance: pipeline commit, per-LLM model + totals, decoding config |
| `ENCODINGS.md` | snapshot of the logic-encoding scheme used for this run |
| `axioms_std.js` | snapshot of the prover's static axiom file used for this run |
| `prompts/` | snapshot of the six prompt components fed to the LLMs (see "Prompts" below) |
| `README.md` | this file |

## How this run was created

- Pipeline: nlpsolver @ `585e8b04d36f3794990385dc955ef8facc4d3866`
  (https://github.com/tammet/nlpsolver, parser under `llmpipe/`).
- Test file: `tests/core/core_tests.py` (1600 cases `[id, english, expected]`).
- Command (the pipeline's batch runner):
  `python3 runtests.py tests/tests_core.py -llms claude,gpt,gemini,deepseek -sequential`

For each `(case, LLM)` the pipeline runs five stages:

1. Stage 1 (LLM): English → abstract semantic units.
2. Stage 2 (LLM): semantic units → first-order-logic JSON.
3. Stage 3 (pipeline code): the Stage-2 JSON is heavily rewritten and extended before anything
   reaches the prover — structural repair, context/tense injection, FOL→CNF clausification, and
   dynamic axiom injection. This is a substantial transformation, not a thin compile, and much of
   what the prover sees is added here rather than emitted by the LLM.
4. Stage 4 (`gk` prover): the resulting clauses plus the static axioms (`axioms_std.js`) are run.
5. Stage 5 (pipeline code): the proof is post-processed into an English answer, graded against
   the case's expected value (`correctness`).

Only Stages 1 and 2 call the LLM. Those answers were served from the pipeline's SQLite response
cache, so the run is deterministic for this pipeline commit and these model snapshots. The full
step-by-step reproduction recipe is in the repository-root `REPRODUCE.md`.

## Prompts

Each LLM call uses a system prompt (the parsing instructions) plus a user message (the case's
English text). The two system prompts are assembled from the files in `prompts/`:

```
stage-1 system prompt = stage1_instructions_full.txt
                        + "\n\nExamples:\n\n" + stage1_examples.txt
                        + "\n\n" + stage1_checklist_full.txt
stage-2 system prompt = stage2_instructions_full.txt
                        + "\n\nExamples:\n\n" + stage2_examples.txt
                        + "\n\n" + stage2_checklist_full.txt
```

So `case_NNNN.json` `answer` is what the LLM produced when given the matching stage prompt above
as the system message and the case text (Stage 1) / the Stage-1 output (Stage 2) as the user
message. If a sanity check fails, the pipeline re-calls the LLM with a short corrective prompt
(up to two retries per stage); these are reflected in the recorded stage outputs.

## LLMs — how they were called

All four ran with thinking / reasoning disabled (the parser calls them with `think=False`).
Exact values are also in `meta.json` (`llms.<llm>.decoding`, `decoding_common`).

| LLM | model | temperature | max output tokens | thinking / reasoning | context caching |
|---|---|---|---|---|---|
| claude | claude-sonnet-4-6 | 0 | 8000 | off | inline ephemeral `cache_control` on the system block |
| gpt | gpt-5.1 | n/a* | 8000 | `reasoning.effort=none`, `text.verbosity=low` | — |
| gemini | gemini-2.5-flash | 0 | 8000 | `thinkingConfig` not set** | on — server-side `cachedContents` |
| deepseek | deepseek-v4-flash | 0 | 8000 | none (non-reasoner) | — |

\* The gpt-5 `/v1/responses` path does not send `temperature` or `seed`.
\** gemini-2.5-flash has default dynamic thinking that counts against the output budget; on a
truncated response the pipeline retries with a doubled budget (≥16000).

Gemini context caching uses different machinery from the others: when the system prompt is large
(≥ ~16000 chars, true here), the pipeline uploads it to Google as a `cachedContents` object with a
30-minute TTL and references it by name in each `generateContent` call (created via
`POST /v1beta/cachedContents`). This is on by default. Claude instead caches the system block
inline via ephemeral `cache_control`; gpt and deepseek use no context caching here.

Common to all: seed 1234 (part of the cache key), HTTP timeout 60s, retry policy
3 HTTP + 2 empty-response + up to 7 rate-limit backoff.

## Results

| LLM | accuracy (of 1600) |
|---|---|
| claude | 1582 — 98.9% |
| deepseek | 1577 — 98.6% |
| gemini | 1567 — 97.9% |
| gpt | 1555 — 97.2% |

Per-subsection breakdown: `summaries/core/2026-06-03_llmpipe.md`. Regenerate any table with
`python3 eval/summarize.py outputs/core/2026-06-03_llmpipe --tests tests/core/core_tests.py`.
