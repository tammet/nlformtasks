# FOLIO — provenance of the upstream data in this directory

The files `folio_v2_validation.jsonl` and `folio_v2_train.jsonl` are the FOLIO v2 dataset,
redistributed here unmodified. FOLIO is third-party data; it is not part of the nlpsolver /
nlformtasks work.

## Source

- **Dataset:** `yale-nlp/FOLIO` on the HuggingFace Hub (https://huggingface.co/datasets/yale-nlp/FOLIO).
  This is where we obtained the data — not a GitHub repository.
- **Files taken:** the `validation` split (203 records — the set scored in our paper) and the
  `train` split (1001 records — included for completeness only).
- **Retrieved:** 2026-06-07. Stored at `/opt/nlpsolver/llmpipe/tests/FOLIO_yale/` in the pipeline
  repo, copied here verbatim.
- **License (upstream):** MIT, as declared on the dataset card (`license: mit`). Reproduced in
  `UPSTREAM_LICENSE`. The authoritative license is the dataset card itself.

## Record schema (both splits)

```
story_id, premises, premises-FOL, conclusion, conclusion-FOL, label, example_id
```

`label` ∈ {True, False, Uncertain} (we render `Uncertain` as `Unknown.` in `folio_tests.py`).

## Citation

Simeng Han, Hailey Schoelkopf, Yilun Zhao, Zhenting Qi, Martin Riddell, Wenfei Zhou, James Coady,
David Peng, Yujie Qiao, Luke Benson, Lucy Sun, Alex Wardle-Solano, Hannah Szabo, Ekaterina Zubova,
Matthew Burtell, Jonathan Fan, Yixin Liu, Brian Wong, Malcolm Sailor, Ansong Ni, Linyong Nan,
Jungo Kasai, Tao Yu, Rui Zhang, Alexander R. Fabbri, Wojciech Kryściński, Semih Yavuz, Ye Liu,
Xi Victoria Lin, Shafiq Joty, Yingbo Zhou, Caiming Xiong, Rex Ying, Arman Cohan, Dragomir Radev.
*FOLIO: Natural Language Reasoning with First-Order Logic.* arXiv:2209.00840, 2022 (v2 2024);
EMNLP 2024.

## How it maps into this repository

- `folio_tests.py` (id 1..203) ⇔ `folio_v2_validation.jsonl` line N → id N.
- The paper's FOLIO results in `outputs/folio/` were produced by running `folio_tests.py` through
  the pipeline; see each run's `README.md` / `meta.json` for the command and pipeline tag.
