# core — run `t4-variant-flatevents_2026-06-20`

**Role:** auxiliary — Table 4: Lossy event simplification.

Cases: **1600**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 1458 | 141 | 1 | 91.13% |
| claude | claude-sonnet-4-6 | 1484 | 116 | 0 | 92.75% |
| gemini | gemini-2.5-flash | 1465 | 135 | 0 | 91.56% |
| deepseek | deepseek-v4-flash | 1456 | 143 | 1 | 91.00% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek |
|---|---:|---:|---:|---:|---:|
| FUNDAMENTAL TAXONOMY & TYPE LOGIC | 10 | 10 | 10 | 10 | 10 |
| LOGICAL CONNECTIVES | 13 | 13 | 13 | 10 | 13 |
| PROPERTIES & ADJECTIVAL LOGIC | 38 | 37 | 38 | 38 | 36 |
| NUMBER & PLURALITY | 14 | 14 | 14 | 14 | 14 |
| COREFERENCE & ANAPHORA | 95 | 94 | 91 | 95 | 91 |
| POSSESSION & HAVE | 45 | 45 | 45 | 45 | 45 |
| DEFINITE DESCRIPTIONS: X OF Y AND POSSESSIVES | 40 | 37 | 40 | 39 | 38 |
| POSSESSION INFERENCE FROM DESCRIPTIONS | 127 | 121 | 126 | 125 | 119 |
| SETS AND COUNTING | 28 | 28 | 28 | 27 | 28 |
| MEASURES | 96 | 96 | 96 | 94 | 95 |
| QUANTIFIERS: UNIVERSAL & EXISTENTIAL | 30 | 29 | 29 | 30 | 30 |
| QUANTIFIERS: PROPORTIONAL & NUMERIC | 10 | 10 | 10 | 10 | 10 |
| COMPARATIVES & EQUALITY | 8 | 7 | 7 | 8 | 8 |
| COORDINATION (NP, VP, CLAUSAL) | 19 | 18 | 19 | 19 | 19 |
| LISTS AND CONJUNCTIONS | 52 | 50 | 50 | 51 | 48 |
| INTERNAL MODIFICATION | 77 | 71 | 70 | 69 | 71 |
| RELATIVE CLAUSES | 269 | 245 | 257 | 252 | 251 |
| AMBIGUOUS MODIFIER SCOPE | 36 | 22 | 25 | 22 | 28 |
| PASSIVE VOICE | 48 | 47 | 45 | 46 | 43 |
| SUBORDINATE CLAUSES | 31 | 28 | 30 | 24 | 26 |
| ELLIPSIS & GAPPING | 10 | 9 | 9 | 10 | 9 |
| ACTION MODES & HABITS | 35 | 28 | 26 | 27 | 28 |
| TRANSFER OF POSSESSION (GIVE/TAKE) | 35 | 19 | 16 | 17 | 16 |
| TENSE, ASPECT & CHANGE OF STATE | 42 | 38 | 39 | 37 | 36 |
| SPATIAL LOGIC & WHERE QUERIES | 95 | 74 | 81 | 81 | 79 |
| ACTION AND WORLD STATE SEQUENCES | 12 | 2 | 2 | 2 | 2 |
| QUESTION LOGIC (WHO/WHAT/WHICH) | 26 | 25 | 26 | 25 | 24 |
| IF-THEN INFERENCE | 65 | 63 | 64 | 62 | 64 |
| DEFAULT & DEFEASIBLE REASONING | 62 | 59 | 59 | 56 | 54 |
| DEFAULTS WITH EXCEPTIONS (BLOCKING) | 11 | 10 | 8 | 9 | 10 |
| UNCERTAINTY & CONFIDENCE | 83 | 81 | 81 | 78 | 78 |
| ADVANCED SEMANTIC OPERATORS | 27 | 17 | 19 | 22 | 22 |
| COMPLEX REASONING CHAINS | 11 | 11 | 11 | 11 | 11 |
