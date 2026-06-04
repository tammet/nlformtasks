# Models & decoding — run `2026-06-03_llmpipe`

Configuration actually used, recorded from `llmpipe/solver/llmcall.py` @ `585e8b0`. All four LLMs ran with **thinking/reasoning disabled**.

| LLM | model | temperature | max output tokens | thinking | notes |
|---|---|---|---|---|---|
| claude | claude-sonnet-4-6 | 0 | 8000 | off | System prompt sent with ephemeral prompt caching. |
| gpt | gpt-5.1 | n/a (not sent on the gpt-5 responses path) | 8000 | none | reasoning.effort=none, text.verbosity=low. |
| gemini | gemini-2.5-flash | 0 | 8000 | not set | gemini-2.5-flash has default dynamic thinking that counts against the output budget; on truncation the pipeline retries with a doubled budget (>=16000). Server-side context caching off. |
| deepseek | deepseek-v4-flash | 0 | 8000 | none (non-reasoner; deepseek-reasoner not used) |  |

## Common

- temperature: 0 (where the provider accepts it)
- max tokens: 8000
- thinking/reasoning: disabled
- seed: 1234 (part of the cache key)
- HTTP timeout: 60s; retries: 3 HTTP + 2 empty-response + up to 7 rate-limit backoff

