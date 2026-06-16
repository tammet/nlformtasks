# FOLIO test set (third-party data)

**FOLIO is not our dataset.** It is the Yale FOLIO benchmark, redistributed here unmodified for
reproducibility of the FOLIO results in our paper. Authorship, the introducing publication, the
upstream source, and the license are below; full detail in [`source/PROVENANCE.md`](source/PROVENANCE.md).

## Files

- `folio_tests.py` — the **203 FOLIO v2 validation items**, as `[id, input, expected]`. `id` is the
  validation-split file order (`1..203`); `input` is the premises followed by the conclusion phrased
  as a question; `expected` is FOLIO's original v2 gold label (`True.` / `False.` / `Unknown.`).
- `source/folio_v2_validation.jsonl` — the upstream validation split, verbatim (203 records, the
  scored set). Each record carries `story_id`, `premises`, `premises-FOL`, `conclusion`,
  `conclusion-FOL`, `label`, `example_id`.
- `source/folio_v2_train.jsonl` — the upstream train split, verbatim (included for completeness;
  not used for any number in the paper).
- `source/UPSTREAM_LICENSE` — the upstream MIT license.

## Attribution

- **Dataset:** FOLIO (First-Order Logic with Natural Language).
- **Authors:** Simeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell, Wenfei Zhou,
  James Coady, David Peng, Yujie Qiao, Luke Benson, Lucy Sun, Alex Wardle-Solano, Hannah Szabo,
  Ekaterina Zubova, Matthew Burtell, Jonathan Fan, Yixin Liu, Brian Wong, Malcolm Sailor, Ansong Ni,
  Linyong Nan, Jungo Kasai, Tao Yu, Rui Zhang, Alexander R. Fabbri, Wojciech Kryściński, Semih Yavuz,
  Ye Liu, Xi Victoria Lin, Shafiq Joty, Yingbo Zhou, Caiming Xiong, Rex Ying, Arman Cohan, Dragomir Radev.
- **Introduced in:** *FOLIO: Natural Language Reasoning with First-Order Logic*, arXiv:2209.00840
  (2022; v2 2024), published at EMNLP 2024.
- **Obtained from:** the HuggingFace dataset **`yale-nlp/FOLIO`** (not GitHub). The dataset card
  declares `license: mit`. Retrieved 2026-06-07.
- **License:** MIT (upstream) — see `source/UPSTREAM_LICENSE`. This repository is Apache-2.0; the
  FOLIO files under `tests/folio/` remain under their upstream MIT license.

## Gold label distribution (validation, 203 items)

72 `True.` / 62 `False.` / 69 `Unknown.` (FOLIO's original v2 gold).

## What we changed

Nothing about the data. We only **repackaged** each validation record into a `[id, input, expected]`
triple (id = file order; `input` = premises + conclusion-as-question; `expected` = the upstream
`label`). The gold labels are unmodified. We score against this original gold throughout; the paper
uses no relabeled variant.
