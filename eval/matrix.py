#!/usr/bin/env python3
"""Cross-run accuracy matrix for one benchmark — regenerates the paper tables.

Walks outputs/<benchmark>/**/provenance.json, scores every run per LLM, and
prints a shape-by-model matrix. With --subset, also prints the same matrix
restricted to the subset's case-ids (e.g. the challenging core subset).

Self-contained: reads only the committed JSON outputs + each run's
provenance.json. No pipeline dependency.

Usage:
  python3 eval/matrix.py outputs/core --subset tests/core/core_tests_challenging.py
  python3 eval/matrix.py outputs/folio
"""
import argparse
import glob
import json
import os

import summarize as S  # same directory

# Display order of shapes (runs not listed here are appended in path order).
SHAPE_ORDER = [
    "two-stage", "single-full-examples", "single-minimal-examples",
    "single-full-no-examples",
    "two-stage-abstracted", "direct-answer", "two-stage-standard",
    "single-full-examples-standard", "single-full-examples-abstracted",
]
COL_ORDER = ["gpt", "claude", "gemini", "deepseek", "fable5"]


def find_runs(benchmark_dir):
    runs = []
    for p in glob.glob(os.path.join(benchmark_dir, "**", "provenance.json"),
                       recursive=True):
        runs.append(os.path.dirname(p))
    # also accept runs without provenance.json (legacy): any dir with <llm>/summary.json
    for p in glob.glob(os.path.join(benchmark_dir, "**", "summary.json"),
                       recursive=True):
        rd = os.path.dirname(os.path.dirname(p))
        if rd not in runs and os.path.normpath(rd).startswith(os.path.normpath(benchmark_dir)):
            runs.append(rd)
    return sorted(set(runs))


def run_key(run_dir, prov):
    shape = prov.get("shape") or S.parse_path(run_dir)[1]
    idx = SHAPE_ORDER.index(shape) if shape in SHAPE_ORDER else len(SHAPE_ORDER)
    return (idx, run_dir)


def score(run_dir, keep=None):
    prov = S.load_provenance(run_dir)
    llms = S.discover_llms(run_dir, prov)
    verdicts, _ = S.load_run(run_dir, llms, keep=keep)
    rows = S.per_llm_table(verdicts, llms)
    return prov, llms, rows, len(verdicts)


def fmt_pct(r):
    if not r or r["accuracy"] is None:
        return "—"
    return f"{round(100 * r['accuracy'])}"


def print_matrix(benchmark_dir, runs, keep, title):
    cols = COL_ORDER
    print(f"\n### {title}")
    print("| shape (role) | cases | " + " | ".join(cols) + " |")
    print("|---|---:|" + "|".join(["---:"] * len(cols)) + "|")
    for run_dir in runs:
        prov, llms, rows, n = score(run_dir, keep=keep)
        shape = prov.get("shape") or S.parse_path(run_dir)[1]
        role = prov.get("role", "")
        cells = []
        for c in cols:
            cells.append(fmt_pct(rows.get(c)) if c in rows else "")
        label = f"{shape} ({role})" if role else shape
        print(f"| {label} | {n} | " + " | ".join(cells) + " |")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("benchmark_dir", help="outputs/<benchmark>")
    ap.add_argument("--subset", default=None, help="subset test file (e.g. challenging)")
    args = ap.parse_args()

    runs = find_runs(args.benchmark_dir)
    runs.sort(key=lambda rd: run_key(rd, S.load_provenance(rd)))
    benchmark = os.path.basename(os.path.normpath(args.benchmark_dir))

    print(f"# {benchmark} accuracy matrix  ({len(runs)} runs)")
    print_matrix(args.benchmark_dir, runs, None, "Full set (% accuracy)")
    if args.subset:
        keep = S.load_ids(args.subset)
        print_matrix(args.benchmark_dir, runs, keep,
                     f"Subset: {os.path.basename(args.subset)} ({len(keep)} cases, % accuracy)")


if __name__ == "__main__":
    main()
