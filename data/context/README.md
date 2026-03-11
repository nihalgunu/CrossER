# CrossER Context Data

This directory contains context data in two formats for different evaluation modes.

## Evaluation Modes

| Mode | Directory | Description |
|------|-----------|-------------|
| **No Context** | — | Entity pairs only (zero-shot baseline) |
| **Raw Context** | `raw/` | Messy enterprise documents (realistic, multi-hop) |
| **Oracle Context** | `structured/` | Clean structured JSON (upper bound) |

## `structured/` - Oracle Context

Clean, structured JSON with direct entity mappings. This represents an idealized
scenario where all institutional knowledge is perfectly organized and directly accessible.

**File:** `oracle_context.json`

Contains:
- `migration_records` — Direct source-to-target entity mappings
- `alias_table` — Known alternative names
- `code_mappings` — Legacy code translations
- `business_rules` — Domain classification logic

## `raw/` - Raw Enterprise Documents

Messy, realistic enterprise documents designed to break simple RAG approaches.
The key challenge is **multi-hop reasoning**: mappings are split across documents
using intermediate codes.

### Multi-Hop Challenge

To resolve `SIG-30-PVA-ZMF8` → `Sodium Chloride 70% Grade B`, you need:

1. **Runbook**: `SIG-30-PVA-ZMF8` → `IC-1000` (source to intermediate code)
2. **Email**: `IC-1000` → `Sodium Chloride 70% Grade B` (intermediate to target)

Simple keyword-based RAG cannot connect these. Knowledge graphs or multi-hop
retrieval strategies are required.

### Document Types

| Folder | Count | Format | Description |
|--------|-------|--------|-------------|
| `migration_runbooks/` | 10 | Markdown | Source → Intermediate Code mappings |
| `email_threads/` | 70 | Text | IC → Target mappings + temporal contradictions |
| `wiki_pages/` | 10 | Markdown | Implicit relationships (30% outdated) |
| `slack_exports/` | 5 | JSON | Informal messages (only 10% relevant) |
| `policy_documents/` | 2 | Markdown | Dense compliance docs |

**Total: 97 documents**

### Key Characteristics

- **Multi-hop required**: No direct source→target mappings in documents
- **Temporal contradictions**: Emails contain wrong info then corrections
- **~70% noise**: Most content is irrelevant to entity resolution
- **Intermediate codes**: IC-*, BC-*, MR-*, MG-* codes link documents
- **96% entity coverage**: Some pairs require attribute-only reasoning

### Adversarial Features

| Feature | Description |
|---------|-------------|
| **Hop chains** | 2-4 intermediate codes between source and target |
| **Temporal contradictions** | Earlier emails have wrong mappings, later ones correct |
| **Implicit rules** | Relationships implied but not stated directly |
| **Noise documents** | 26 documents with no useful mappings |

### hop_chains.json

Contains the multi-hop structure for each entity mapping:

```json
{
  "source_entity_id": "legacy_sigma_prod_001",
  "target_entity_id": "erp_alpha_prod_001",
  "source_code": "SIG-30-PVA-ZMF8",
  "target_code": "Sodium Chloride 70% Grade B",
  "hop_count": 3,
  "intermediate_codes": [
    {"code": "IC-1000", "code_type": "ic"},
    {"code": "MG-1001", "code_type": "mg"}
  ]
}
```

### manifest.json

Index of all documents with metadata:

```json
{
  "document_id": "doc_0001",
  "type": "runbook",
  "filename": "migration_runbooks/RUNBOOK-SIGMA_DECOMMISSION_2023-1234.md",
  "entity_ids": ["legacy_sigma_prod_001", ...],
  "has_valid_mappings": true
}
```

## Usage

### Baseline Approaches

```bash
# No context (zero-shot)
python baselines/llm_baseline.py --mechanism no_context

# Raw context with RAG (realistic)
python baselines/llm_rag_raw_baseline.py --api-key $ANTHROPIC_API_KEY

# Oracle context (upper bound)
python baselines/llm_baseline.py --mechanism rag
```

### Key Metrics

- **Oracle - No Context** = Maximum possible improvement from context
- **Raw - No Context** = Actual improvement from realistic context extraction
- **Oracle - Raw** = Room for improvement in context extraction / multi-hop reasoning

## Regenerating Raw Documents

```bash
cd generate/
python generate_raw_documents.py --seed 42
```

This reads from `structured/oracle_context.json` and generates new raw documents.
