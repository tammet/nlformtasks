# folio — run `ref-direct-answer_2026-06-12`

**Role:** reference — Reference: LLM answers the FOLIO question directly, no logic and no prover. Source of the Section-4 direct-answer percentages (incl. Fable-5).

Cases: **203**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 140 | 63 | 0 | 68.97% |
| claude | claude-sonnet-4-6 | 137 | 66 | 0 | 67.49% |
| gemini | gemini-2.5-flash | 175 | 28 | 0 | 86.21% |
| deepseek | deepseek-v4-flash | 174 | 29 | 0 | 85.71% |
| fable5 | claude-fable-5 | 178 | 25 | 0 | 87.68% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek | fable5 |
|---|---:|---:|---:|---:|---:|---:|
| None | 203 | 140 | 137 | 175 | 174 | 178 |
