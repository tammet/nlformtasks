#!/usr/bin/env python3
"""Summarize one run directory of LLM test outputs.

Self-contained: walks outputs/<benchmark>/<shape>/<date>/<llm>/case_*.json and
produces
  - a per-LLM pass/fail/error table (printed),
  - an optional per-subsection breakdown (when --tests points at the test file),
  - an optional subset re-score (when --subset points at a subset test file),
  - meta.json written into the run dir (with --write),
  - a markdown summary under summaries/<benchmark>/<shape>_<date>.md (with --write).

Provenance (pipeline tag/commit, role, per-LLM model + decoding, command,
prompts) is read from a `provenance.json` seed file in the run dir when present;
otherwise the legacy defaults below are used. No dependency on the pipeline
(llmpipe) code — it only reads the JSON outputs committed in this repository.

Usage:
  python3 eval/summarize.py outputs/core/two-stage/2026-06-03 \
      --tests tests/core/core_tests.py --write
  python3 eval/summarize.py outputs/core/single-full-examples/2026-06-08 \
      --subset tests/core/core_tests_challenging.py
"""
import argparse
import ast
import glob
import json
import os
import re

KNOWN_LLMS = ["claude", "gpt", "gemini", "deepseek", "fable5"]
PIPELINE_REPO = "https://github.com/tammet/nlpsolver"

# Legacy default provenance (the original 2026-06-03 core two-stage run), used
# only when a run dir has no provenance.json.
DEFAULT_PIPELINE = {
    "repo": PIPELINE_REPO,
    "tag": "core-2026-06-03",
    "commit": "585e8b04d36f3794990385dc955ef8facc4d3866",
    "note": "LLM answers served from the pipeline's SQLite cache; pipeline "
            "answer-logic as of this commit.",
}
DEFAULT_DECODING = {
    "_common": {
        "temperature": 0, "max_tokens": 8000, "thinking": "disabled",
        "seed": 1234, "http_timeout_s": 60,
        "retries": "3 HTTP + 2 empty-response + up to 7 rate-limit backoff",
    },
    "claude": {
        "model": "claude-sonnet-4-6", "api": "messages",
        "temperature": 0, "max_tokens": 8000, "extended_thinking": "off",
        "context_caching": "explicit: inline ephemeral cache_control on the system block",
    },
    "gpt": {
        "model": "gpt-5.1", "api": "/v1/responses",
        "reasoning_effort": "none", "text_verbosity": "low",
        "max_output_tokens": 8000,
        "temperature": "n/a (not sent on the gpt-5 responses path)",
        "context_caching": "automatic provider-side (OpenAI prompt caching for "
                           "prompts >=1024 tokens); not requested by the pipeline",
    },
    "gemini": {
        "model": "gemini-2.5-flash", "api": "generateContent",
        "temperature": 0, "max_output_tokens": 8000, "thinking_config": "not set",
        "context_caching": "explicit: server-side cachedContents object "
                           "(>=~16000-char system prompt, 30-min TTL, on by default)",
        "notes": "gemini-2.5-flash has default dynamic thinking that counts "
                 "against the output budget; on truncation the pipeline retries "
                 "with a doubled budget (>=16000).",
    },
    "deepseek": {
        "model": "deepseek-v4-flash", "api": "/v1/chat/completions",
        "temperature": 0, "max_tokens": 8000,
        "thinking": "none (non-reasoner; deepseek-reasoner not used)",
        "context_caching": "automatic provider-side (DeepSeek disk context "
                           "caching); not requested by the pipeline",
    },
}


def load_provenance(run_dir):
    p = os.path.join(run_dir, "provenance.json")
    if os.path.exists(p):
        return json.load(open(p))
    return {}


def parse_path(run_dir):
    """outputs/<benchmark>/<...>/<date> -> (benchmark, 'shape_date' label)."""
    parts = os.path.normpath(run_dir).split(os.sep)
    if "outputs" in parts:
        i = parts.index("outputs")
        benchmark = parts[i + 1] if i + 1 < len(parts) else parts[-1]
        label = "_".join(parts[i + 2:]) or benchmark
    else:
        benchmark, label = parts[-2], parts[-1]
    return benchmark, label


def discover_llms(run_dir, prov):
    listed = list((prov.get("llms") or {}).keys())
    present = [l for l in KNOWN_LLMS if os.path.isdir(os.path.join(run_dir, l))]
    return listed + [l for l in present if l not in listed] or present


def verdict(d):
    if d.get("correctness") is True:
        return "pass"
    return "error" if str(d.get("answer", "")).startswith("Error") else "fail"


def load_run(run_dir, llms, keep=None):
    """run_dir/<llm>/case_*.json -> (verdicts{cid:{llm:status}}, models{llm:ver}).
    keep, if given, is a set of case-ids to restrict scoring to."""
    verdicts, models = {}, {}
    for llm in llms:
        for fp in sorted(glob.glob(os.path.join(run_dir, llm, "case_*.json"))):
            d = json.load(open(fp))
            cid = d.get("case_id")
            if keep is not None and cid not in keep:
                continue
            verdicts.setdefault(cid, {})[llm] = verdict(d)
            models[llm] = d.get("llm_version")
    return verdicts, models


def _tests_list_node(src):
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "tests":
                    return node.value
    return tree.body[0].value


def load_ids(tests_path):
    src = open(tests_path).read()
    return set(ast.literal_eval(e.elts[0]) for e in _tests_list_node(src).elts)


def load_subsections(tests_path):
    src = open(tests_path).read()
    sub_at, cur = {}, None
    hdr = re.compile(r"^# == (.+?) ==")
    for i, ln in enumerate(src.split("\n"), 1):
        m = hdr.match(ln)
        if m:
            cur = m.group(1)
        sub_at[i] = cur
    out = {}
    for e in _tests_list_node(src).elts:
        out[ast.literal_eval(e.elts[0])] = sub_at[e.lineno]
    return out


def per_llm_table(verdicts, llms):
    rows = {}
    for llm in llms:
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


def per_subsection_table(verdicts, subs, llms):
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
        for llm in llms:
            row[llm] = sum(verdicts.get(cid, {}).get(llm) == "pass" for cid in ids)
        table.append(row)
    return table


def build_meta(run_dir, benchmark, label, verdicts, models, llms, prov):
    rows = per_llm_table(verdicts, llms)
    decoding = prov.get("decoding") or DEFAULT_DECODING
    pipeline = prov.get("pipeline") or DEFAULT_PIPELINE
    meta = dict(
        benchmark=benchmark,
        shape=prov.get("shape"),
        date=prov.get("date"),
        run_label=label,
        role=prov.get("role"),
        role_note=prov.get("role_note"),
        primary_result=prov.get("primary_result"),
        pipeline=pipeline,
        command=prov.get("command"),
        prompts=prov.get("prompts"),
        cases=len(verdicts),
        llms={llm: dict(model=models.get(llm) or (prov.get("llms") or {}).get(llm),
                        **rows[llm],
                        decoding=decoding.get(llm, {})) for llm in llms},
        decoding_common=decoding.get("_common", {}),
        generated_by="eval/summarize.py",
    )
    return {k: v for k, v in meta.items() if v is not None}


def md_summary(benchmark, label, verdicts, models, llms, subs, prov):
    rows = per_llm_table(verdicts, llms)
    pipe = prov.get("pipeline") or DEFAULT_PIPELINE
    tagstr = pipe.get("tag") or ("untagged (" + pipe.get("note", "")[:60] + "…)")
    out = [f"# {benchmark} — run `{label}`", ""]
    if prov.get("role"):
        out.append(f"**Role:** {prov['role']}"
                   + (f" — {prov['role_note']}" if prov.get("role_note") else ""))
        out.append("")
    out += [f"Cases: **{len(verdicts)}**.  Pipeline: `{PIPELINE_REPO}` @ `{tagstr}`.", "",
            "## Per-LLM accuracy", "",
            "| LLM | model | pass | fail | error | accuracy |",
            "|---|---|---:|---:|---:|---:|"]
    for llm in llms:
        r = rows[llm]
        acc = f"{r['accuracy']:.2%}" if r["accuracy"] is not None else "n/a"
        out.append(f"| {llm} | {models.get(llm)} | {r['passed']} | {r['failed']} "
                   f"| {r['errored']} | {acc} |")
    if subs:
        out += ["", "## Per-subsection pass counts", "",
                "| subsection | cases | " + " | ".join(llms) + " |",
                "|---|---:|" + "|".join(["---:"] * len(llms)) + "|"]
        for row in per_subsection_table(verdicts, subs, llms):
            cells = " | ".join(str(row[llm]) for llm in llms)
            out.append(f"| {row['subsection']} | {row['cases']} | {cells} |")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_dir", help="outputs/<benchmark>/<shape>/<date>")
    ap.add_argument("--tests", default=None, help="test file for per-subsection breakdown")
    ap.add_argument("--subset", default=None, help="subset test file: restrict scoring to its ids")
    ap.add_argument("--write", action="store_true", help="write meta.json + summaries/<...>.md")
    args = ap.parse_args()

    run_dir = args.run_dir.rstrip("/")
    benchmark, label = parse_path(run_dir)
    prov = load_provenance(run_dir)
    llms = discover_llms(run_dir, prov)
    keep = load_ids(args.subset) if args.subset else None
    verdicts, models = load_run(run_dir, llms, keep=keep)
    subs = load_subsections(args.tests) if args.tests else None

    rows = per_llm_table(verdicts, llms)
    scope = f" (subset {len(verdicts)})" if keep is not None else ""
    print(f"{benchmark} / {label}: {len(verdicts)} cases{scope}")
    for llm in llms:
        r = rows[llm]
        print(f"  {llm:9s} {str(models.get(llm)):20s} "
              f"{r['passed']}/{r['cases']}  acc={r['accuracy']}  "
              f"(fail {r['failed']}, err {r['errored']})")

    if args.write:
        if keep is not None:
            raise SystemExit("refuse to --write a subset score into meta.json; "
                             "run --write on the full set, use --subset for ad-hoc reports")
        meta = build_meta(run_dir, benchmark, label, verdicts, models, llms, prov)
        json.dump(meta, open(os.path.join(run_dir, "meta.json"), "w"), indent=2)
        sumdir = os.path.join("summaries", benchmark)
        os.makedirs(sumdir, exist_ok=True)
        path = os.path.join(sumdir, label + ".md")
        open(path, "w").write(md_summary(benchmark, label, verdicts, models, llms, subs, prov))
        print(f"wrote {os.path.join(run_dir, 'meta.json')}, {path}")


if __name__ == "__main__":
    main()
