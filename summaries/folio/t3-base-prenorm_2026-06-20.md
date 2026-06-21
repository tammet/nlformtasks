# folio — run `t3-base-prenorm_2026-06-20`

**Role:** auxiliary — Table 3 reference row: Pre-normalized base. The (+/-) gains/losses in Table 3 are measured against this run.

Cases: **203**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 114 | 87 | 2 | 56.16% |
| claude | claude-sonnet-4-6 | 116 | 86 | 1 | 57.14% |
| gemini | gemini-2.5-flash | 105 | 93 | 5 | 51.72% |
| deepseek | deepseek-v4-flash | 96 | 78 | 29 | 47.29% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek |
|---|---:|---:|---:|---:|---:|
| None | 203 | 114 | 116 | 105 | 96 |
