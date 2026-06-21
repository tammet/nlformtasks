# folio — run `t3-variant-flatevents_2026-06-20`

**Role:** auxiliary — Table 3: Lossy event simplification.

Cases: **203**.  Pipeline: `https://github.com/tammet/nlpsolver` @ `lpar-2026-06-22`.

## Per-LLM accuracy

| LLM | model | pass | fail | error | accuracy |
|---|---|---:|---:|---:|---:|
| gpt | gpt-5.1 | 116 | 87 | 0 | 57.14% |
| claude | claude-sonnet-4-6 | 123 | 79 | 1 | 60.59% |
| gemini | gemini-2.5-flash | 111 | 88 | 4 | 54.68% |
| deepseek | deepseek-v4-flash | 97 | 77 | 29 | 47.78% |

## Per-subsection pass counts

| subsection | cases | gpt | claude | gemini | deepseek |
|---|---:|---:|---:|---:|---:|
| None | 203 | 116 | 123 | 111 | 97 |
