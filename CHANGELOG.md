# Changelog

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
  - Pipeline: `nlpsolver` @ `585e8b0`.
- Added `eval/summarize.py` (per-LLM and per-subsection tables) and
  `summaries/core/2026-06-03_llmpipe.md`.
