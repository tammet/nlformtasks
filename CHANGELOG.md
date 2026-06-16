# Changelog

## 2026-06-16 — pipeline-shape ablations, FOLIO benchmark, challenging subset

- **Run-folder layout** is now `outputs/<benchmark>/<shape>/<date>/`. Renamed the existing core run
  `outputs/core/2026-06-03_llmpipe` → `outputs/core/two-stage/2026-06-03` (and its summary). Each run
  now carries a `role` (`primary` / `auxiliary` / `reference`) in `meta.json` and a `provenance.json`
  seed read by `eval/summarize.py`.
- **Core ablations** (single-call pipeline shapes, 1600 cases each) under `outputs/core/ablations/`:
  `single-full-examples` (93/96/95/95), `single-minimal-examples` (95/95/93/93),
  `single-full-no-examples` (83/91/87/88) for gpt/claude/gemini/deepseek. The two-stage run stays the
  primary core result.
- **Challenging subset** `tests/core/core_tests_challenging.py` (341 cases missed ≥2× across the 16
  shape×model cells). Scored from the existing per-run JSONs via `eval/summarize.py --subset` /
  `eval/matrix.py --subset`; no separate run.
- **FOLIO benchmark** (third-party; Yale FOLIO v2 validation, 203 items, original gold) under
  `tests/folio/` and `outputs/folio/`. Attribution, upstream HuggingFace source and MIT license in
  `tests/folio/README.md` + `tests/folio/source/`. Runs: `two-stage-abstracted` (primary, 65/70/67/53),
  `direct-answer` (reference, 69/67/86/86 + Fable-5 91), `two-stage-standard` (54/57/51/47),
  `single-full-examples-standard` (61/59/58/54), `single-full-examples-abstracted` (66/67/62/55).
- **eval/**: `summarize.py` extended for the nested layout, per-run `provenance.json`, a variable LLM
  set (picks up the Fable-5 backend), and `--subset` scoring. Added `eval/matrix.py` (cross-run
  shape-by-model matrix; regenerates the paper tables).
- Pipeline tags referenced: `core-2026-06-03` (585e8b0), `folio-2026-06-12` (6831b29),
  `folio-2026-06-14` (1d7b54a). The core ablations and FOLIO two-stage-standard are not separately
  tagged (same pipeline generation as `core-2026-06-03`); see REPRODUCE.md.

## 2026-06-04 — initial repository

- Created the repository structure: `tests/`, `outputs/`, `eval/`, `summaries/`.
- Added the core test set: `tests/core/core_tests.py` (1600 cases) and the curated
  `tests/core/core_tests_100.py` (100-case all-LLMs-correct subset).
- Added run `2026-06-03_llmpipe` under `outputs/core/` as a self-describing folder:
  per-case JSONs for claude, gpt, gemini, deepseek; `meta.json` (totals + decoding config);
  a run `README.md` (how it was made, how each LLM was called, prompt-assembly mechanism); and
  snapshots of the exact inputs — `ENCODINGS.md`, `axioms_std.js`, and the six `prompts/` files —
  since those evolve over time.
  - All four LLMs ran with thinking disabled; Gemini used server-side `cachedContents` context
    caching (distinct from Claude's inline ephemeral caching).
  - Accuracy on 1600 cases: claude 98.9%, deepseek 98.6%, gemini 97.9%, gpt 97.2%.
  - Pipeline: `nlpsolver` @ `585e8b0` (later tagged `core-2026-06-03`).
- Added `eval/summarize.py` (per-LLM and per-subsection tables) and
  `summaries/core/2026-06-03_llmpipe.md`.
