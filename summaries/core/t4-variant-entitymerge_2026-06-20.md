# core — run `t4-variant-entitymerge_2026-06-20`

**Role:** auxiliary — Table 4: Entity merging.

Cases: **1600**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 1555 | 43 | 2 | 97.19% |
| claude | claude-sonnet-4-6 | 1582 | 18 | 0 | 98.88% |
| gemini | gemini-2.5-flash | 1563 | 37 | 0 | 97.69% |
| deepseek | deepseek-v4-flash | 1569 | 30 | 1 | 98.06% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek |
|---|---:|---:|---:|---:|---:|
| FUNDAMENTAL TAXONOMY & TYPE LOGIC | 10 | 10 | 10 | 10 | 10 |
| LOGICAL CONNECTIVES | 13 | 13 | 13 | 10 | 13 |
| PROPERTIES & ADJECTIVAL LOGIC | 38 | 37 | 38 | 38 | 36 |
| NUMBER & PLURALITY | 14 | 14 | 14 | 14 | 14 |
| COREFERENCE & ANAPHORA | 95 | 94 | 92 | 95 | 93 |
| POSSESSION & HAVE | 45 | 45 | 45 | 45 | 45 |
| DEFINITE DESCRIPTIONS: X OF Y AND POSSESSIVES | 40 | 38 | 40 | 39 | 40 |
| POSSESSION INFERENCE FROM DESCRIPTIONS | 127 | 125 | 126 | 126 | 126 |
| SETS AND COUNTING | 28 | 28 | 28 | 27 | 28 |
| MEASURES | 96 | 96 | 96 | 94 | 93 |
| QUANTIFIERS: UNIVERSAL & EXISTENTIAL | 30 | 29 | 29 | 30 | 30 |
| QUANTIFIERS: PROPORTIONAL & NUMERIC | 10 | 10 | 10 | 10 | 10 |
| COMPARATIVES & EQUALITY | 8 | 7 | 7 | 8 | 7 |
| COORDINATION (NP, VP, CLAUSAL) | 19 | 18 | 19 | 19 | 19 |
| LISTS AND CONJUNCTIONS | 52 | 52 | 52 | 52 | 51 |
| INTERNAL MODIFICATION | 77 | 74 | 75 | 71 | 73 |
| RELATIVE CLAUSES | 269 | 257 | 267 | 265 | 267 |
| AMBIGUOUS MODIFIER SCOPE | 36 | 34 | 36 | 35 | 36 |
| PASSIVE VOICE | 48 | 48 | 48 | 47 | 47 |
| SUBORDINATE CLAUSES | 31 | 30 | 31 | 30 | 30 |
| ELLIPSIS & GAPPING | 10 | 10 | 9 | 10 | 10 |
| ACTION MODES & HABITS | 35 | 34 | 33 | 35 | 35 |
| TRANSFER OF POSSESSION (GIVE/TAKE) | 35 | 34 | 35 | 35 | 34 |
| TENSE, ASPECT & CHANGE OF STATE | 42 | 42 | 42 | 40 | 42 |
| SPATIAL LOGIC & WHERE QUERIES | 95 | 89 | 93 | 93 | 91 |
| ACTION AND WORLD STATE SEQUENCES | 12 | 12 | 12 | 12 | 12 |
| QUESTION LOGIC (WHO/WHAT/WHICH) | 26 | 25 | 26 | 25 | 24 |
| IF-THEN INFERENCE | 65 | 62 | 65 | 63 | 65 |
| DEFAULT & DEFEASIBLE REASONING | 62 | 61 | 62 | 58 | 58 |
| DEFAULTS WITH EXCEPTIONS (BLOCKING) | 11 | 11 | 10 | 10 | 11 |
| UNCERTAINTY & CONFIDENCE | 83 | 83 | 83 | 80 | 81 |
| ADVANCED SEMANTIC OPERATORS | 27 | 22 | 25 | 26 | 27 |
| COMPLEX REASONING CHAINS | 11 | 11 | 11 | 11 | 11 |
