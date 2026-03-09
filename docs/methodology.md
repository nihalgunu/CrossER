# CrossER Benchmark Methodology

## Overview

CrossER benchmarks cross-system entity resolution on **only the hardest cases** — pairs where string matching and attribute heuristics fail, and institutional context is required.

## Patterns from Real Enterprise Systems

The synthetic data in CrossER is generated based on patterns observed across Fortune 500 enterprise deployments at [Phyvant](https://phyvant.com). While the data itself is synthetic (no real company data is included), the patterns are derived from real observations:

### Naming Inconsistencies Observed

| Pattern | Real-World Observation | CrossER Implementation |
|---------|------------------------|------------------------|
| Legacy codes | Decommissioned systems use cryptic codes (e.g., `SIG-44-MALTDEX`) that bear no resemblance to canonical names | LEGACY_SIGMA entities use generated codes with avg 0.29 similarity to canonical names |
| Regional naming | European subsidiaries use German product names (`Zitronensäure` vs `Citric Acid`) | ERP_BETA uses German formal naming conventions |
| Acquisition artifacts | Acquired companies retain abbreviated naming (`MLTDX-20-A`) | ERP_GAMMA uses heavy abbreviation patterns |
| Informal usage | Regional ops use casual names (`the usual corn stuff`) | ERP_DELTA uses informal/shortened names |

### Data Quality Patterns Observed

| Pattern | Real-World Observation | CrossER Implementation |
|---------|------------------------|------------------------|
| Attribute completeness | Varies 45-95% across systems in real deployments | Configured per system: ALPHA 95%, SIGMA 45% |
| Schema heterogeneity | Different systems track different attributes | Each system has different attribute schemas |
| Migration artifacts | System decommissions leave mapping tables | Migration records link LEGACY_SIGMA to other systems |

### Why These Patterns Make ER Hard

In real enterprise environments, we observed that:

1. **~30% of cross-system matches** have string similarity below 0.4 (names look completely unrelated)
2. **~25% of high-similarity pairs** are actually different entities (same name, different spec/grade/region)
3. **Simple heuristics fail** — string matching achieves near-0% recall on the hardest cases

CrossER isolates these hard cases to create a benchmark where context is required.

## Benchmark Design: 100% Hard Cases

Unlike benchmarks with mixed difficulty, CrossER includes **only** the cases where surface-level features are misleading:

| Pair Type | String Similarity | What This Means |
|-----------|-------------------|-----------------|
| **Match pairs** | avg 0.294 | Names look completely unrelated |
| **No-match pairs** | avg 0.936 | Names look nearly identical |

### Why No Easy Cases?

Easy cases (high-similarity matches, low-similarity no-matches) don't differentiate systems. Any reasonable approach solves them. Including easy cases would:

- Inflate scores without measuring capability
- Obscure the true performance gap between approaches
- Make the benchmark less useful for development

CrossER tests what matters: **can your system leverage institutional context?**

## Context Types

The benchmark includes 86,256 context items representing enterprise knowledge artifacts:

| Type | Count | Description | Based On |
|------|-------|-------------|----------|
| Migration Records | 10,250 | System-to-system entity mappings | Real MDM migration projects |
| Alias Table | 12,856 | Known alternative names | Enterprise alias management |
| Code Mappings | 988 | Legacy code translations | System decommission mappings |
| System Crosswalks | 18,112 | Multi-hop intermediate mappings | Master data crosswalks |
| Transaction Logs | 22,500 | Historical entity references | ERP transaction data |
| Data Quality Flags | 15,000 | Review notes and status | MDM data stewardship |

### Noise by Design

~75% of context items are **noise** — plausible-looking records that don't help resolve the specific pair. This reflects real enterprise environments where:

- Not all migration records are accurate
- Alias tables contain unverified suggestions
- Historical logs reference many entities

Simple RAG retrieval will pull irrelevant records. Effective systems must filter signal from noise.

### Multi-Hop Resolution

Some matches require **multi-hop reasoning**:

```
Entity A (LEGACY_SIGMA)
  → Crosswalk → Master Code XREF-00123
  → Crosswalk → Entity B (ERP_ALPHA)
```

Direct entity-to-entity lookup fails. The system must traverse intermediate mappings.

## Source System Simulation

| System | Real-World Analog | Naming Pattern | Attribute Completeness |
|--------|-------------------|----------------|------------------------|
| ERP_ALPHA | Global HQ (SAP) | Formal, complete | 95% |
| ERP_BETA | EU Subsidiary (Oracle) | German formal | 90% |
| ERP_GAMMA | Acquired Company | Heavy abbreviation | 60% |
| ERP_DELTA | Regional Ops | Informal | 50% |
| LEGACY_SIGMA | Decommissioned | Cryptic codes | 45% |

These patterns are based on real system archetypes observed in enterprise deployments.

## Evaluation

### Primary Metric: F1 Score

Binary classification (match vs no_match). Ambiguous pairs excluded.

### What the Baselines Show

| Method | F1 | Interpretation |
|--------|-----|----------------|
| String Matching | 0.000 | Complete failure — all matches have low similarity |
| Attribute Matching | 0.145 | Slightly better but fooled by adversarial no-matches |
| Claude Sonnet 4 (zero-shot) | 0.090 | LLM without context performs worse than heuristics |

**Key finding**: Raw model intelligence isn't enough. The benchmark requires institutional context.

### The Gap to Close

Expected with good context delivery: F1 0.70-0.85

This represents the **knowledge gap** — the performance improvement possible when systems properly leverage auxiliary context.

## Reproducibility

All generation uses:
- Fixed random seed: 42
- Python 3.10+ compatible

```bash
cd generate/
python generate_entities.py
python generate_pairs.py
python generate_context.py
python consolidate_dataset.py
```

## Limitations

1. **Synthetic data**: Patterns are realistic but actual enterprise data may have additional complexities
2. **English-centric**: Most names in English with some German
3. **Single domain**: Commodity trading/chemicals focus
4. **Four entity types**: Product, legal_entity, supplier, tax_code

## References

1. SWE-bench: [github.com/princeton-nlp/SWE-bench](https://github.com/princeton-nlp/SWE-bench) — Benchmark design inspiration
2. WDC Product Matching: [webdatacommons.org](https://webdatacommons.org/largescaleproductcorpus/)
3. Magellan Data Repository: [sites.google.com/site/anhaborisov/datasets](https://sites.google.com/site/anhaborisov/datasets)
