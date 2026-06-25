# nlformtasks — LPAR experiment data

Recorded pipeline outputs for the LPAR paper *"Representation Abstraction and Proof Search
for English-to-Logic Question Answering"*. This branch (`lpar`) holds the test sets, the
per-case pipeline outputs (generated logic, clauses, prover input and prover output), the
evaluation scripts, and a snapshot of the prompts and axioms — everything needed to match
and reproduce the numbers in the paper.

This is **data only**; the pipeline code lives in the `nlpsolver` repository under `llmpipe/`:
<https://github.com/tammet/nlpsolver>.

## Pipeline version — read this first

Every run here was produced by the pipeline at git tag **`lpar-2026-06-22`** (the state
just before this tag is `lpar-pre-2026-06-22`). The pipeline is under active development, so
`main` will behave differently. **To reproduce, check out the `nlpsolver` repo at tag
`lpar-2026-06-22`** and run the per-run command. The post-translation abstraction flags used
below are documented in `llmpipe/ENCODINGS.md` §6 (a snapshot is in `pipeline-snapshot/`).

```
git clone https://github.com/tammet/nlpsolver && cd nlpsolver
git checkout lpar-2026-06-22
cd llmpipe   # then run the per-run commands below
```

## Layout

```
tests/
  core/   core_tests.py (1600), core_tests_challenging.py (341 subset), core_tests_100.py
  folio/  folio_tests.py (203 FOLIO v2 validation items; third-party, MIT — see tests/folio/README.md)
outputs/
  core/   <run>/<date>/<llm>/case_NNNN.json   + meta.json + README.md + provenance.json
  folio/  <run>/<date>/<llm>/case_NNNN.json   + ...
eval/
  summarize.py   one run dir -> per-LLM table + meta.json (no pipeline needed)
  matrix.py      cross-run shape-by-model matrix
summaries/       one markdown table per run
pipeline-snapshot/   prompts/ + axioms_std.js + ENCODINGS.md, as used by every run here
```

Each `case_NNNN.json` carries the full record per case: `input_text`, `expected_answer`,
`answer`, `correctness`, `stage1` (ASUs), `stage2` (logic JSON), `clauses` (generated
clauses), `gk_command` (prover input) and `proof` (prover output). Run folders are named
`t<N>-...` after the paper table they feed.

## Paper table → folder map

Run names carry a `t<N>-` prefix for the paper table plus a descriptive part. Proof-length
tables (5, 6) are Claude-only, matching the paper; the abstraction tables (3, 4) and the
baselines use all four backends.

| Paper | row / use | folder | flags |
|---|---|---|---|
| **T1** | NLFT baseline (full) | `outputs/core/t1-baseline-full` | *(none)* |
| **T1** | NLFT challenging subset | same folder, scored with `tests/core/core_tests_challenging.py` | *(none)* |
| **T1** | FOLIO baseline (standard) | `outputs/folio/t1-baseline-standard` | *(none)* |
| **T4** | NLFT, lossy event simplification | `outputs/core/t4-variant-flatevents` | `-flatevents` |
| **T4** | NLFT, extra type/class atoms | `outputs/core/t4-variant-typeenrich` | `-typeenrich` |
| **T4** | NLFT, entity merging | `outputs/core/t4-variant-entitymerge` | `-entitymerge` |
| **T4** | NLFT, definite-description terms | `outputs/core/t4-variant-definites` | `-definites` |
| **T4** | NLFT, + guard removal | `outputs/core/t4-variant-flat-guarddrop` | `-flatevents -guarddrop` |
| **T4** | NLFT, + extra bridges | `outputs/core/t4-variant-flat-bridges` | `-flatevents -bridges` |
| **§5** | NLFT type-enrich diagnostic (91.2→98.1) | `outputs/core/t4-diag-typeenrich-noplural` | `-typeenrich` + `TE_SKIP=plural` |
| **T3** | FOLIO, pre-normalized base (reference) | `outputs/folio/t3-base-prenorm` | `-prenorm` |
| **T3** | FOLIO, lossy event simplification | `outputs/folio/t3-variant-flatevents` | `-prenorm -flatevents` |
| **T3** | FOLIO, extra type/class atoms | `outputs/folio/t3-variant-typeenrich` | `-prenorm -typeenrich` |
| **T3** | FOLIO, entity merging | `outputs/folio/t3-variant-entitymerge` | `-prenorm -entitymerge` |
| **T3** | FOLIO, definite-description terms | `outputs/folio/t3-variant-definites` | `-prenorm -definites` |
| **T3** | FOLIO, + guard removal | `outputs/folio/t3-variant-flat-guarddrop` | `-prenorm -flatevents -guarddrop` |
| **T3** | FOLIO, + extra bridges | `outputs/folio/t3-variant-flat-bridges` | `-prenorm -flatevents -bridges` |
| **T3** | FOLIO abstraction (best row) | `outputs/folio/t3-abstraction-full` | `-prenorm -ultracoarse` |
| **T5** | NLFT proof-length base / davidson / existfold / both | `outputs/core/t1-baseline-full`, `t5-prooflen-davidson`, `t5-prooflen-existfold`, `t5-prooflen-davidson-existfold` | *(none)* / `-davidson` / `-existfold -nocrossstage` / `-davidson -existfold -nocrossstage` |
| **T5** | FOLIO proof-length base / davidson / existfold / both | `outputs/folio/t5-prooflen-base`, `t5-prooflen-davidson`, `t5-prooflen-existfold`, `t5-prooflen-davidson-existfold` | `-nocrossstage` / `-davidson -nocrossstage` / `-existfold -nocrossstage` / `-davidson -existfold -nocrossstage` |
| **T6** | NLFT long cases (864, 618, 785) | core `t1-baseline-full` + `t5-prooflen-davidson` + `t5-prooflen-existfold` | as T5 |
| **T6** | FOLIO 198 (abstracted base / +dav / +exist / +both) | `outputs/folio/t6-abstract-base`, `t6-abstract-davidson`, `t6-abstract-existfold`, `t6-abstract-davidson-existfold` | `-prenorm -ultracoarse2 -nocrossstage` / `-prenorm -ultracoarse -davidson -nocrossstage` / `-prenorm -ultracoarse2 -existfold -nocrossstage` / `-prenorm -ultracoarse -davidson -existfold -nocrossstage` |
| **§4** | FOLIO direct-answer (incl. Fable-5) | `outputs/folio/ref-direct-answer` | direct-answer mode (`-directanswer`) |

Table 2 is definitions only (no data). Each folder's `meta.json`/`README.md` repeats its exact
command, flags, role and per-LLM accuracy. Note the davidson runs (`t5-prooflen-davidson*`,
`t6-abstract-davidson*`) are the corrected-clausify builds; at tag `lpar-2026-06-22` the fix is
in the code, so the plain flags above reproduce them.

## Regenerate the numbers (no pipeline needed)

```
# one run's per-LLM accuracy + per-subsection breakdown
python3 eval/summarize.py outputs/core/t1-baseline-full/2026-06-03 --tests tests/core/core_tests.py

# T1 NLFT challenging-subset column
python3 eval/summarize.py outputs/core/t1-baseline-full/2026-06-03 --subset tests/core/core_tests_challenging.py

# cross-run matrices (T3 / T4 style)
python3 eval/matrix.py outputs/folio
python3 eval/matrix.py outputs/core
```

## Reproducing from scratch

See [REPRODUCE.md](REPRODUCE.md): check out `nlpsolver` at tag `lpar-2026-06-22`, then run the
`runtests.py` command from each folder's `meta.json` (`command` field).
