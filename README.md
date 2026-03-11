# CrossER: Cross-System Entity Resolution Benchmark

[![Website](https://img.shields.io/badge/Website-crosser--bench.vercel.app-blue.svg)](https://crosser-bench.vercel.app/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-green.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Maintained by Phyvant](https://img.shields.io/badge/Maintained%20by-Phyvant-purple.svg)](https://phyvant.com)

**CrossER** is a hard benchmark for cross-system entity resolution. Synthetically generated based on patterns observed across Fortune 500 enterprise systems at [Phyvant](https://phyvant.com).

LLMs fail on this benchmark without institutional context. String matching gets 0%. The benchmark measures how well systems can leverage auxiliary context to resolve entities across enterprise systems.

## Key Statistics

| Metric | Value |
|--------|-------|
| Total Pairs | 7,603 |
| Test Pairs | 1,141 |
| Total Entities | 7,162 |
| Source Systems | 5 |
| Raw Documents | 237 |

## Why CrossER is Hard

| | Match Pairs | No-Match Pairs |
|---|---|---|
| **Avg String Similarity** | **0.294** | **0.936** |
| **What this means** | Look completely unrelated | Look nearly identical |

- Matches have low similarity — models predict no_match — wrong
- No-matches have high similarity — models predict match — wrong
- Context required to resolve most pairs

## Baselines

| Method | F1 | Precision | Recall |
|--------|-----|-----------|--------|
| Attribute Matching | 0.145 | 0.080 | 0.783 |
| Claude Sonnet 4 + BM25 RAG | 0.091 | 0.077 | 0.111 |
| Claude Sonnet 4 (zero-shot) | 0.090 | 0.143 | 0.065 |
| String Matching | 0.000 | 0.000 | 0.000 |

## Quick Start

```bash
git clone https://github.com/nihalgunu/CrossER
cd CrossER

# Run baselines
python baselines/run_baselines.py

# Evaluate your predictions
python eval/evaluate.py your_predictions.json
```

## Repository Structure

```
CrossER/
├── data/
│   ├── entities.json
│   ├── pairs.json
│   └── context/
│       └── raw/                  # 97 enterprise documents
│           ├── migration_runbooks/
│           ├── email_threads/
│           ├── wiki_pages/
│           ├── slack_exports/
│           └── policy_documents/
├── eval/
└── baselines/
```

## Prediction Format

```json
[
  {"pair_id": "pair_0001", "predicted_label": "match"},
  {"pair_id": "pair_0002", "predicted_label": "no_match"}
]
```

## Citation

```bibtex
@misc{crosser2026,
  author       = {Gunukula, Nihal and Murthy, Sameer},
  title        = {{CrossER: Cross-System Entity Resolution Benchmark}},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/nihalgunu/CrossER}
}
```

## License

- **Code**: Apache 2.0
- **Data**: CC BY 4.0

---

[Phyvant](https://phyvant.com) · [@nihalgunu](https://github.com/nihalgunu) · [Issues](https://github.com/nihalgunu/CrossER/issues)
