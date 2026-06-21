# folio — run `t3-variant-entitymerge_2026-06-20`

**Role:** auxiliary — Table 3: Entity merging.

Cases: **203**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 114 | 87 | 2 | 56.16% |
| claude | claude-sonnet-4-6 | 113 | 89 | 1 | 55.67% |
| gemini | gemini-2.5-flash | 104 | 94 | 5 | 51.23% |
| deepseek | deepseek-v4-flash | 97 | 77 | 29 | 47.78% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek |
|---|---:|---:|---:|---:|---:|
| None | 203 | 114 | 113 | 104 | 97 |
