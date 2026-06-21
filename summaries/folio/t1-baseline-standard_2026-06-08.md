# folio — run `t1-baseline-standard_2026-06-08`

**Role:** auxiliary — Table 1: FOLIO baseline (standard two-stage).

Cases: **203**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 109 | 93 | 1 | 53.69% |
| claude | claude-sonnet-4-6 | 115 | 87 | 1 | 56.65% |
| gemini | gemini-2.5-flash | 104 | 91 | 8 | 51.23% |
| deepseek | deepseek-v4-flash | 95 | 69 | 39 | 46.80% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek |
|---|---:|---:|---:|---:|---:|
| None | 203 | 109 | 115 | 104 | 95 |
