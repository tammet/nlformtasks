# core test set

English reasoning problems for the nlpsolver semantic parser
(https://github.com/tammet/nlpsolver), in loose linguistic groups, roughly ordered from simple to
complex.

## Files

- `core_tests.py` — 1600 cases. A Python list of `[id, english_text, expected_answer]`.
  Organized into eight phases (FOUNDATIONS → REASONING) and finer `# == SUBSECTION ==` blocks;
  ids are sequential `1..1600`.
- `core_tests_100.py` — a curated 100-case subset of `core_tests.py`, balanced across the eight
  phases and answer types, chosen so that all four LLMs answer every case correctly in the
  published run. Each row keeps its `core_tests.py` id, so the subset is graded against the same
  `outputs/core/<run-id>/case_NNNN.json` files — no separate outputs. Its header comment records
  the per-phase type targets.
- `core_tests_challenging.py` — the 341-case **challenging subset**. A case is challenging if it
  is answered wrong at least twice across the 16 (pipeline-shape × LLM) cells of the experiment
  grid (shapes: two-stage, single-full-examples, single-minimal-examples, single-full-no-examples;
  models: gpt, claude, gemini, deepseek). It is the `≥2 total-errors` group of the difficulty
  distribution. Like the 100-subset it keeps the original ids and is graded against the same
  per-run `outputs/core/.../case_NNNN.json` files — no separate run. Regenerate any run's
  challenging-subset score with `eval/summarize.py --subset tests/core/core_tests_challenging.py`
  (or the second block of `eval/matrix.py outputs/core --subset …`).

## Expected-answer semantics

The third element of each row is the accepted answer:

| form | meaning |
|---|---|
| `True` | the question is entailed |
| `False` | the negation is entailed |
| `None` | unknown — neither the statement nor its negation is entailed |
| a string (e.g. `'Mary.'`, `'At noon.'`) | the expected concrete answer to a wh-question |
| a list of strings | any one of several acceptable surface phrasings |
| a confidence phrase (e.g. `'Probably true.'`, `'Likely false.'`) | the expected graded answer |

Grading compares the pipeline's answer against this value.

## Phases

`core_tests.py` begins with a table of contents listing the eight phases and their subsections
with case counts. In brief: I Foundations, II Reference & Possession, III Quantifiers &
Comparison, IV Modification & Structure, V Clause Alternations, VI Events & State, VII Questions,
VIII Reasoning.
