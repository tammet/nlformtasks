# Changelog

## 2026-06-04 — initial repository

- Created the repository structure: `tests/`, `outputs/`, `eval/`, `summaries/`.
- Added the **core** test set: `tests/core/core_tests.py` (1600 cases) and the curated
  `tests/core/core_tests_100.py` (100-case all-LLMs-correct subset).
- Added run **`2026-06-03_llmpipe`** under `outputs/core/`: per-case JSONs for claude, gpt,
  gemini, deepseek, with `meta.json` and `MANIFEST.json`.
  - Accuracy on 1600 cases: claude 98.9%, deepseek 98.6%, gemini 97.9%, gpt 97.2%.
  - Pipeline: `nlpsolver` @ `585e8b0`.
- Added `eval/summarize.py` (per-LLM and per-subsection tables) and
  `summaries/core/2026-06-03_llmpipe.md`.
- Copied `ENCODINGS.md` from the pipeline repo (synced from `llmpipe@585e8b0`).
