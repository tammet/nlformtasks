# core — run `t4-diag-typeenrich-noplural_2026-06-20`

**Role:** auxiliary — Section-5 diagnostic: with only the plural-to-singular sub-injector disabled, Claude goes 91.2% -> 98.1% on NLFT.

Cases: **1600**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| claude | claude-sonnet-4-6 | 1569 | 31 | 0 | 98.06% |

## Per-subsection pass counts

| subsection | cases | claude |
|---|---:|---:|
| FUNDAMENTAL TAXONOMY & TYPE LOGIC | 10 | 10 |
| LOGICAL CONNECTIVES | 13 | 13 |
| PROPERTIES & ADJECTIVAL LOGIC | 38 | 37 |
| NUMBER & PLURALITY | 14 | 14 |
| COREFERENCE & ANAPHORA | 95 | 92 |
| POSSESSION & HAVE | 45 | 45 |
| DEFINITE DESCRIPTIONS: X OF Y AND POSSESSIVES | 40 | 40 |
| POSSESSION INFERENCE FROM DESCRIPTIONS | 127 | 126 |
| SETS AND COUNTING | 28 | 28 |
| MEASURES | 96 | 96 |
| QUANTIFIERS: UNIVERSAL & EXISTENTIAL | 30 | 29 |
| QUANTIFIERS: PROPORTIONAL & NUMERIC | 10 | 10 |
| COMPARATIVES & EQUALITY | 8 | 7 |
| COORDINATION (NP, VP, CLAUSAL) | 19 | 17 |
| LISTS AND CONJUNCTIONS | 52 | 52 |
| INTERNAL MODIFICATION | 77 | 75 |
| RELATIVE CLAUSES | 269 | 267 |
| AMBIGUOUS MODIFIER SCOPE | 36 | 36 |
| PASSIVE VOICE | 48 | 48 |
| SUBORDINATE CLAUSES | 31 | 31 |
| ELLIPSIS & GAPPING | 10 | 9 |
| ACTION MODES & HABITS | 35 | 33 |
| TRANSFER OF POSSESSION (GIVE/TAKE) | 35 | 35 |
| TENSE, ASPECT & CHANGE OF STATE | 42 | 42 |
| SPATIAL LOGIC & WHERE QUERIES | 95 | 93 |
| ACTION AND WORLD STATE SEQUENCES | 12 | 11 |
| QUESTION LOGIC (WHO/WHAT/WHICH) | 26 | 24 |
| IF-THEN INFERENCE | 65 | 65 |
| DEFAULT & DEFEASIBLE REASONING | 62 | 62 |
| DEFAULTS WITH EXCEPTIONS (BLOCKING) | 11 | 10 |
| UNCERTAINTY & CONFIDENCE | 83 | 76 |
| ADVANCED SEMANTIC OPERATORS | 27 | 25 |
| COMPLEX REASONING CHAINS | 11 | 11 |
