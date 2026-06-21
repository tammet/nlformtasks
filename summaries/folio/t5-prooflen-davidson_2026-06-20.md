# folio — run `t5-prooflen-davidson_2026-06-20`

**Role:** auxiliary — Table 5 FOLIO compact Davidsonian. Corrected clausify build.

Cases: **203**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 114 | 88 | 1 | 56.16% |
| claude | claude-sonnet-4-6 | 117 | 84 | 2 | 57.64% |
| gemini | gemini-2.5-flash | 104 | 93 | 6 | 51.23% |
| deepseek | deepseek-v4-flash | 44 | 35 | 13 | 47.83% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek |
|---|---:|---:|---:|---:|---:|
| None | 203 | 114 | 117 | 104 | 44 |
