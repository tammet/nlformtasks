# Reproducing the LPAR runs

The recorded outputs in `outputs/` were produced by the `nlpsolver` pipeline at a fixed git
tag. The pipeline changes over time, so reproduction must pin that tag.

## 1. Get the pipeline at the right tag

```
git clone https://github.com/tammet/nlpsolver
cd nlpsolver
git checkout lpar-2026-06-22          # the exact state used for every run here
cd llmpipe
```

`lpar-2026-06-22` is the state used for all runs in this branch; `lpar-pre-2026-06-22` is the
state immediately before. Running against `main` will **not** reproduce these numbers.

Set up the pipeline as in `llmpipe/README.md` (the `gk` binary + data files, and an LLM API
key under `../secrets/`). LLM answers in the paper were served from the pipeline's SQLite
cache; a fresh run re-queries the LLM (temperature 0, non-reasoning configuration per the
paper) and should reproduce the same answers up to provider drift.

## 2. Run a single configuration

Each run folder's `meta.json` (and `README.md`) gives the exact command in its `command`
field. The pattern is:

```
python3 runtests.py <test-file> -llm <gpt|claude|gemini|deepseek> <flags>
```

- test file: `tests/tests_core.py` (NLFT) or `tests/tests_folio_v2.py` (FOLIO) — these are the
  pipeline-repo copies of the `tests/core/core_tests.py` / `tests/folio/folio_tests.py` here;
- flags: the post-translation abstraction flags for that configuration (see the table in
  `README.md` and `llmpipe/ENCODINGS.md` §6). For example:

```
# NLFT baseline (T1 / T4 full representation)
python3 runtests.py tests/tests_core.py -llm claude

# FOLIO abstraction (T3 best row)
python3 runtests.py tests/tests_folio_v2.py -llm claude -prenorm -ultracoarse

# FOLIO compact-Davidsonian proof-length run (T5)
python3 runtests.py tests/tests_folio_v2.py -llm claude -davidson -nocrossstage
```

The type-enrichment diagnostic `t4-diag-typeenrich-noplural` additionally sets the environment
variable `TE_SKIP=plural` (disables the plural-to-singular sub-injector):
`TE_SKIP=plural python3 runtests.py tests/tests_core.py -llm claude -typeenrich`.

`runtests.py` writes one JSON per (case, llm) under `testresults/<set>_<...>/<llm>/`, each with
`stage1`, `stage2`, `clauses`, `gk_command` and `proof` — the same fields recorded here.

## 3. Score the outputs

The evaluation scripts here read only the JSON outputs (no pipeline dependency):

```
python3 eval/summarize.py <run-dir> --tests tests/<bench>/<bench>_tests.py     # per-LLM accuracy
python3 eval/summarize.py <run-dir> --subset tests/core/core_tests_challenging.py
python3 eval/matrix.py outputs/folio                                           # cross-run matrix
```

Grading is the same matcher the pipeline uses (list-of-alternatives, case/punctuation/word-order
normalisation, preposition and unit tolerance, confidence-qualifier handling, `None`→Unknown),
applied to the stored `answer` vs. `expected_answer`; the per-case `correctness` field records
its verdict.
