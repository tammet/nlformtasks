# folio — run `t3-variant-flat-guarddrop_2026-06-20`

**Role:** auxiliary — Table 3: Lossy event simplification + guard removal.

Cases: **203**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 117 | 86 | 0 | 57.64% |
| claude | claude-sonnet-4-6 | 130 | 72 | 1 | 64.04% |
| gemini | gemini-2.5-flash | 118 | 81 | 4 | 58.13% |
| deepseek | deepseek-v4-flash | 101 | 73 | 29 | 49.75% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek |
|---|---:|---:|---:|---:|---:|
| None | 203 | 117 | 130 | 118 | 101 |
