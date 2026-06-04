#!/usr/bin/env python3
"""Summarize one run directory of LLM test outputs.

Self-contained: walks outputs/<set>/<run-id>/<llm>/case_*.json and produces
  - a per-LLM pass/fail/error table (printed),
  - an optional per-subsection breakdown (when --tests points at the test file),
  - meta.json + MANIFEST.json written into the run dir (with --write),
  - a markdown summary written under summaries/<set>/<run-id>.md (with --write).

No dependency on the pipeline (llmpipe) code — it only reads the JSON outputs
that are already committed in this repository.

Usage:
  python3 eval/summarize.py outputs/core/2026-06-03_llmpipe \
      --tests tests/core/core_tests.py --write
  python3 eval/summarize.py outputs/core/2026-06-03_llmpipe   # print only
"""
import argparse
import ast
import glob
import json
import os
import re

LLMS = ["claude", "gpt", "gemini", "deepseek"]
PIPELINE_REPO = "https://github.com/tammet/nlpsolver"
# Pipeline commit whose answer-logic produced the cached LLM answers for the
# 2026-06-03_llmpipe run. Update when a new run is ingested.
PIPELINE_COMMIT = "585e8b04d36f3794990385dc955ef8facc4d3866"


def verdict(d):
    """pass / fail / error for one case result dict."""
    if d.get("correctness") is True:
        return "pass"
    return "error" if str(d.get("answer", "")).startswith("Error") else "fail"


def load_run(run_dir):
    """run_dir/<llm>/case_*.json -> (verdicts{cid:{llm:status}}, models{llm:ver})."""
    verdicts, models = {}, {}
    for llm in LLMS:
        for fp in sorted(glob.glob(os.path.join(run_dir, llm, "case_*.json"))):
            d = json.load(open(fp))
            verdicts.setdefault(d["case_id"], {})[llm] = verdict(d)
            models[llm] = d.get("llm_version")
    return verdicts, models


def load_subsections(tests_path):
    """case_id -> subsection name, from '# == NAME ==' headers in the test file."""
    src = open(tests_path).read()
    lines = src.split("\n")
    sub_at, cur = {}, None
    hdr = re.compile(r"^# == (.+?) ==")
    for i, ln in enumerate(lines, 1):
        m = hdr.match(ln)
        if m:
            cur = m.group(1)
        sub_at[i] = cur
    out = {}
    for e in ast.parse(src).body[0].value.elts:
        out[ast.literal_eval(e.elts[0])] = sub_at[e.lineno]
    return out


def per_llm_table(verdicts):
    rows = {}
    for llm in LLMS:
        p = f = e = 0
        for v in verdicts.values():
            s = v.get(llm, "missing")
            p += s == "pass"
            e += s == "error"
            f += s == "fail"
        n = p + f + e
        rows[llm] = dict(cases=n, passed=p, failed=f, errored=e,
                         accuracy=round(p / n, 4) if n else None)
    return rows


def per_subsection_table(verdicts, subs):
    order, seen = [], set()
    for cid in sorted(subs):
        s = subs[cid]
        if s not in seen:
            seen.add(s)
            order.append(s)
    table = []
    for s in order:
        ids = [cid for cid, sub in subs.items() if sub == s]
        row = {"subsection": s, "cases": len(ids)}
        for llm in LLMS:
            row[llm] = sum(verdicts.get(cid, {}).get(llm) == "pass" for cid in ids)
        table.append(row)
    return table


def write_meta(run_dir, run_id, test_set, verdicts, models):
    rows = per_llm_table(verdicts)
    meta = dict(
        test_set=test_set, run_id=run_id, date=run_id.split("_")[0],
        pipeline=dict(repo=PIPELINE_REPO, commit=PIPELINE_COMMIT,
                      note="LLM answers served from the pipeline's SQLite cache; "
                           "pipeline answer-logic as of this commit."),
        cases=len(verdicts),
        llms={llm: dict(model=models.get(llm), **rows[llm]) for llm in LLMS},
        generated_by="eval/summarize.py",
    )
    json.dump(meta, open(os.path.join(run_dir, "meta.json"), "w"), indent=2)
    return meta


def write_manifest(run_dir, run_id, test_set, verdicts):
    manifest = dict(
        test_set=test_set, run_id=run_id, cases=len(verdicts), llms=LLMS,
        verdicts={str(cid): [verdicts[cid].get(l, "missing") for l in LLMS]
                  for cid in sorted(verdicts)},
        legend={"order": LLMS, "values": ["pass", "fail", "error", "missing"]},
    )
    json.dump(manifest, open(os.path.join(run_dir, "MANIFEST.json"), "w"), indent=0)


def md_summary(run_id, test_set, verdicts, models, subs):
    rows = per_llm_table(verdicts)
    out = [f"# {test_set} — run `{run_id}`", "",
           f"Cases: **{len(verdicts)}**.  LLM answers served from the pipeline cache "
           f"(`{PIPELINE_REPO}` @ `{PIPELINE_COMMIT[:7]}`).", "",
           "## Per-LLM accuracy", "",
           "| LLM | model | pass | fail | error | accuracy |",
           "|---|---|---:|---:|---:|---:|"]
    for llm in LLMS:
        r = rows[llm]
        out.append(f"| {llm} | {models.get(llm)} | {r['passed']} | {r['failed']} "
                   f"| {r['errored']} | {r['accuracy']:.2%} |")
    if subs:
        out += ["", "## Per-subsection pass counts", "",
                "| subsection | cases | " + " | ".join(LLMS) + " |",
                "|---|---:|" + "|".join(["---:"] * len(LLMS)) + "|"]
        for row in per_subsection_table(verdicts, subs):
            cells = " | ".join(str(row[llm]) for llm in LLMS)
            out.append(f"| {row['subsection']} | {row['cases']} | {cells} |")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_dir", help="outputs/<set>/<run-id>")
    ap.add_argument("--tests", default=None,
                    help="test file for the per-subsection breakdown")
    ap.add_argument("--write", action="store_true",
                    help="write meta.json + MANIFEST.json + summaries/<set>/<run-id>.md")
    args = ap.parse_args()

    run_dir = args.run_dir.rstrip("/")
    run_id = os.path.basename(run_dir)
    test_set = os.path.basename(os.path.dirname(run_dir))
    verdicts, models = load_run(run_dir)
    subs = load_subsections(args.tests) if args.tests else None

    rows = per_llm_table(verdicts)
    print(f"{test_set} / {run_id}: {len(verdicts)} cases")
    for llm in LLMS:
        r = rows[llm]
        print(f"  {llm:9s} {str(models.get(llm)):20s} "
              f"{r['passed']}/{r['cases']}  acc={r['accuracy']}  "
              f"(fail {r['failed']}, err {r['errored']})")

    if args.write:
        write_meta(run_dir, run_id, test_set, verdicts, models)
        write_manifest(run_dir, run_id, test_set, verdicts)
        sumdir = os.path.join("summaries", test_set)
        os.makedirs(sumdir, exist_ok=True)
        path = os.path.join(sumdir, run_id + ".md")
        open(path, "w").write(md_summary(run_id, test_set, verdicts, models, subs))
        print(f"wrote meta.json, MANIFEST.json, {path}")


if __name__ == "__main__":
    main()
