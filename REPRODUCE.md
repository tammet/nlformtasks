# Reproducing a run

The outputs here are produced by the nlpsolver pipeline (https://github.com/tammet/nlpsolver),
which is not included in this repository. To regenerate a run you need a checkout of that pipeline
plus the LLM API keys it expects (or a warm response cache). LLM answers are served from the
pipeline's SQLite cache, so a run is deterministic for a given pipeline commit and model set.
**Never disable the cache (`-nollmcache`)** — it wastes API credits and is unnecessary for reproduction.

## Pipeline state per run

Each run records its pipeline state in `meta.json` (`pipeline.tag` / `pipeline.commit`). Three git
tags in the pipeline repo cover the tagged runs; two run groups are not separately tagged and carry
a "same generation as" note instead (their answer-affecting compiler, axioms and prover match the
referenced tagged run).

| run | pipeline tag | commit |
|---|---|---|
| `outputs/core/two-stage/2026-06-03` | `core-2026-06-03` | `585e8b0` |
| `outputs/folio/two-stage-abstracted/2026-06-14` | `folio-2026-06-14` | `1d7b54a` |
| `outputs/folio/single-full-examples-standard/2026-06-14` | `folio-2026-06-14` | `1d7b54a` |
| `outputs/folio/single-full-examples-abstracted/2026-06-14` | `folio-2026-06-14` | `1d7b54a` |
| `outputs/folio/direct-answer/2026-06-12` | `folio-2026-06-12` | `6831b29` |
| `outputs/core/ablations/*` | — (same generation as `core-2026-06-03`) † | — |
| `outputs/folio/two-stage-standard/2026-06-08` | — (same generation as `core-2026-06-03`) ‡ | — |

† The core single-call ablations use the same compiler/axioms/prover as `core-2026-06-03`; they
differ only in prompt assembly (one merged LLM call instead of two), an additive path added after
that tag. Their `prompts/` snapshots are taken from `folio-2026-06-14`, where the combined-prompt
files live.

‡ The FOLIO two-stage-standard run is the same two-stage pipeline, on an intermediate working tree
between `core-2026-06-03` and `folio-2026-06-14`, not separately tagged.

## Commands

Let `$LLMPIPE_DIR` be a checkout of nlpsolver, with its solver data and API keys in place (see that
repo's `llmpipe/CLAUDE.md`). Check out the tag for the run (e.g. `git -C "$LLMPIPE_DIR" checkout
folio-2026-06-14`), install the matching test file under the runner's expected name, and run. The
pipeline's batch runner writes `testresults/<set>[_<tag>]/<llm>/case_*.json`; the published dir names
here are the shape-renamed copies.

```bash
cd "$LLMPIPE_DIR/llmpipe"
# core test file installed as tests/tests_core.py; folio as tests/tests_folio_v2.py

# --- core ---
# two-stage (primary):
python3 runtests.py tests/tests_core.py -llms claude,gpt,gemini,deepseek -sequential
# single-full-examples:
python3 runtests.py tests/tests_core.py -llms <llm> -combined-instr prompts/combined_v2_instructions_full.txt -combined-examples prompts/combined_examples_pure.txt -combined-tag v2_pure
# single-minimal-examples:
python3 runtests.py tests/tests_core.py -llms <llm> -combined-instr prompts/combined_minimal_instructions_full.txt -combined-examples prompts/combined_examples_pure.txt -combined-tag minimal_pure -sequential
# single-full-no-examples:
python3 runtests.py tests/tests_core.py -llms <llm> -combined-instr prompts/combined_v2_instructions_full.txt -combined-tag v2_noexamples

# --- folio ---
# two-stage-abstracted (primary):  gemini/deepseek add -nocrossstage
python3 runtests.py tests/tests_folio_v2.py -llms <llm> -ultracoarse -prenorm -tag ultracoarse_prenorm_v4 -sequential
# direct-answer (reference):
python3 runtests.py tests/tests_folio_v2.py -llms <llm> -directanswer prompts/folio_directanswer_instructions.txt -tag directanswer
#   Fable-5 column: -llms claude -version claude-fable-5 -maxtokens 16000 -directanswer prompts/folio_directanswer_instructions.txt -tag directanswer_fable5 -sequential
# two-stage-standard:
python3 runtests.py tests/tests_folio_v2.py -llms <llm>
# single-full-examples-standard:
python3 runtests.py tests/tests_folio_v2.py -llms <llm> -combined-instr prompts/combined_v2_instructions_full.txt -combined-examples prompts/combined_examples_pure.txt -tag combinedfull_plain -sequential
# single-full-examples-abstracted:
python3 runtests.py tests/tests_folio_v2.py -llms <llm> -combined-instr prompts/combined_v2_instructions_full.txt -combined-examples prompts/combined_examples_pure.txt -ultracoarse -prenorm -tag combinedfull_ultracoarse_prenorm_v4 -sequential
```

## Ingesting and scoring

After a run, copy the per-LLM `case_*.json` + `summary.json` into a new
`outputs/<benchmark>/<shape>/<date>/<llm>/`, write a `provenance.json` seed (role, pipeline tag/commit,
command, prompts, models), then:

```bash
python3 eval/summarize.py outputs/<benchmark>/<shape>/<date> --write          # meta.json + summaries/
python3 eval/summarize.py outputs/<benchmark>/<shape>/<date> --tests tests/<benchmark>/<file>  # + per-subsection
python3 eval/matrix.py outputs/core --subset tests/core/core_tests_challenging.py   # full + challenging matrix
python3 eval/matrix.py outputs/folio
```

The 100-case and challenging core subsets are selections of the same 1600 cases by id, graded
against the same `outputs/core/.../case_*.json` files — there is no separate run for them.

## Notes

- The model identifiers for a run are in its `meta.json`. A different model snapshot is a different
  run — give it a new date folder.
- The challenging-subset DeepSeek `single-full-no-examples` figure here is the complete run (341
  cases); an earlier partial number circulated before all cases finished.
