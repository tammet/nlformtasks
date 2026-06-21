# core — run `t4-variant-typeenrich_2026-06-20`

**Role:** auxiliary — Table 4: Extra type/class atoms.

Cases: **1600**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 1430 | 168 | 2 | 89.38% |
| claude | claude-sonnet-4-6 | 1460 | 140 | 0 | 91.25% |
| gemini | gemini-2.5-flash | 1446 | 154 | 0 | 90.38% |
| deepseek | deepseek-v4-flash | 1452 | 147 | 1 | 90.75% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek |
|---|---:|---:|---:|---:|---:|
| FUNDAMENTAL TAXONOMY & TYPE LOGIC | 10 | 10 | 10 | 10 | 10 |
| LOGICAL CONNECTIVES | 13 | 13 | 13 | 12 | 13 |
| PROPERTIES & ADJECTIVAL LOGIC | 38 | 36 | 37 | 37 | 35 |
| NUMBER & PLURALITY | 14 | 14 | 14 | 14 | 14 |
| COREFERENCE & ANAPHORA | 95 | 94 | 92 | 95 | 93 |
| POSSESSION & HAVE | 45 | 45 | 45 | 45 | 45 |
| DEFINITE DESCRIPTIONS: X OF Y AND POSSESSIVES | 40 | 38 | 40 | 40 | 40 |
| POSSESSION INFERENCE FROM DESCRIPTIONS | 127 | 124 | 125 | 125 | 125 |
| SETS AND COUNTING | 28 | 28 | 28 | 28 | 28 |
| MEASURES | 96 | 96 | 96 | 94 | 94 |
| QUANTIFIERS: UNIVERSAL & EXISTENTIAL | 30 | 24 | 26 | 25 | 25 |
| QUANTIFIERS: PROPORTIONAL & NUMERIC | 10 | 10 | 10 | 10 | 10 |
| COMPARATIVES & EQUALITY | 8 | 7 | 7 | 8 | 8 |
| COORDINATION (NP, VP, CLAUSAL) | 19 | 16 | 17 | 19 | 17 |
| LISTS AND CONJUNCTIONS | 52 | 47 | 47 | 47 | 47 |
| INTERNAL MODIFICATION | 77 | 74 | 75 | 73 | 75 |
| RELATIVE CLAUSES | 269 | 237 | 249 | 246 | 249 |
| AMBIGUOUS MODIFIER SCOPE | 36 | 32 | 34 | 34 | 34 |
| PASSIVE VOICE | 48 | 48 | 48 | 47 | 47 |
| SUBORDINATE CLAUSES | 31 | 30 | 31 | 30 | 30 |
| ELLIPSIS & GAPPING | 10 | 10 | 9 | 10 | 10 |
| ACTION MODES & HABITS | 35 | 7 | 6 | 8 | 8 |
| TRANSFER OF POSSESSION (GIVE/TAKE) | 35 | 33 | 33 | 33 | 32 |
| TENSE, ASPECT & CHANGE OF STATE | 42 | 39 | 39 | 37 | 39 |
| SPATIAL LOGIC & WHERE QUERIES | 95 | 89 | 94 | 93 | 93 |
| ACTION AND WORLD STATE SEQUENCES | 12 | 7 | 7 | 6 | 6 |
| QUESTION LOGIC (WHO/WHAT/WHICH) | 26 | 22 | 24 | 22 | 21 |
| IF-THEN INFERENCE | 65 | 61 | 65 | 63 | 65 |
| DEFAULT & DEFEASIBLE REASONING | 62 | 36 | 35 | 32 | 30 |
| DEFAULTS WITH EXCEPTIONS (BLOCKING) | 11 | 5 | 4 | 4 | 5 |
| UNCERTAINTY & CONFIDENCE | 83 | 64 | 64 | 62 | 66 |
| ADVANCED SEMANTIC OPERATORS | 27 | 23 | 25 | 26 | 27 |
| COMPLEX REASONING CHAINS | 11 | 11 | 11 | 11 | 11 |
