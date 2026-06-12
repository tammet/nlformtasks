# Reproducing a run

The outputs in this repository are produced by the nlpsolver pipeline
(https://github.com/tammet/nlpsolver), which is not included here. To regenerate a run you need a
checkout of that pipeline plus the LLM API keys it expects (or a warm response cache).

## nlpsolver commit used

Each run was produced with one specific nlpsolver commit, recorded here and in the run's
`meta.json`, and marked with a git tag in the pipeline repository. To reproduce, check out
exactly that commit (or its tag).

| run-id | pipeline repo | tag | commit |
|---|---|---|---|
| `2026-06-03_llmpipe` | https://github.com/tammet/nlpsolver | `core-2026-06-03` | `585e8b04d36f3794990385dc955ef8facc4d3866` |

The recorded answers were served from the pipeline's SQLite response cache; the commit above is
the state of the answer-affecting pipeline logic for this run. (Later edits to test files or docs
in the pipeline repo do not change cached LLM answers.)

## Steps

Let `$LLMPIPE_DIR` be a checkout of nlpsolver at that commit, with its solver data and API keys
in place (see that repo's `llmpipe/CLAUDE.md`). From this repository:

```bash
# 1. Check out the exact pipeline state (the tag points at commit 585e8b04...)
git -C "$LLMPIPE_DIR" checkout core-2026-06-03

# 2. Install this repo's core test file under the name the runner expects
cp tests/core/core_tests.py "$LLMPIPE_DIR/llmpipe/tests/tests_core.py"

# 3. Run all four LLMs, cache-served, sequentially. NEVER pass -nollmcache.
cd "$LLMPIPE_DIR/llmpipe"
python3 runtests.py tests/tests_core.py -llms claude,gpt,gemini,deepseek -sequential
# -> writes testresults/core/<llm>/case_NNNN.json + summary.json

# 4. Ingest into a fresh run dir here (new date -> new RUN_ID)
cd -                                   # back to this repo
RUN_ID=2026-06-03_llmpipe              # do not overwrite an existing run dir
for llm in claude gpt gemini deepseek; do
  mkdir -p "outputs/core/$RUN_ID/$llm"
  cp "$LLMPIPE_DIR/llmpipe/testresults/core/$llm/"case_*.json "outputs/core/$RUN_ID/$llm/"
  cp "$LLMPIPE_DIR/llmpipe/testresults/core/$llm/summary.json" "outputs/core/$RUN_ID/$llm/"
done

# 5. Regenerate meta.json and the summary table
python3 eval/summarize.py "outputs/core/$RUN_ID" --tests tests/core/core_tests.py --write
```

The 100-case subset (`tests/core/core_tests_100.py`) is a selection of the same 1600 cases by id,
so it is graded against the same `outputs/core/<run-id>/` JSONs — there is no separate run for it.

## Notes

- Never disable the LLM cache (`-nollmcache`): it wastes API credits and is unnecessary for
  reproduction.
- The model identifiers for a run are recorded in `outputs/core/<run-id>/meta.json`. A different
  model snapshot is a different run — give it a new run-id.
