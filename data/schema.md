# CrossER Data Schema

This document describes the data formats used in the CrossER benchmark.

## Entity Schema (`entities.json`)

Each entity represents a record from one of the source systems.

```json
{
  "entity_id": "erp_alpha_prod_001",
  "source_system": "ERP_ALPHA",
  "entity_type": "product",
  "name": "Maltodextrin DE20 Grade A",
  "attributes": {
    "category": "modified starches",
    "sub_category": "maltodextrin",
    "region": "DE",
    "unit_of_measure": "MT",
    "internal_code": "PRD-4412",
    "classification_code": "1702.30.50",
    "status": "active",
    "created_date": "2019-03-15"
  }
}
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `entity_id` | string | Unique identifier: `{system}_{type}_{number}` |
| `source_system` | string | One of: `ERP_ALPHA`, `ERP_BETA`, `ERP_GAMMA`, `ERP_DELTA`, `LEGACY_SIGMA` |
| `entity_type` | string | One of: `product`, `legal_entity`, `supplier`, `tax_code` |
| `name` | string | Display name of the entity |
| `attributes` | object | System-specific attributes (varies by entity type and system) |

### Source Systems

| System | Description | Naming Style | Completeness |
|--------|-------------|--------------|--------------|
| `ERP_ALPHA` | Global headquarters ERP (SAP-like) | Formal, structured | ~95% |
| `ERP_BETA` | European subsidiary ERP (Oracle-like) | Formal, EU conventions | ~90% |
| `ERP_GAMMA` | Acquired company legacy system | Abbreviated, inconsistent | ~60% |
| `ERP_DELTA` | Regional operations system | Informal, casual | ~50% |
| `LEGACY_SIGMA` | Decommissioned system | Legacy codes, partial data | ~45% |

### Common Attributes by Entity Type

**Products:**
- `category`, `sub_category`: Product classification
- `region`: Geographic region code (DE, US, etc.)
- `unit_of_measure`: MT, KG, L, etc.
- `internal_code`: System-specific product code
- `classification_code`: Tariff/customs classification
- `dextrose_equivalent`: For maltodextrin products
- `status`: active, inactive
- `created_date`: ISO date string

**Legal Entities:**
- `entity_subtype`: subsidiary, trading_partner, joint_venture, etc.
- `jurisdiction`: Country code
- `registration_number`: Company registration
- `tax_id`: Tax identification number

**Suppliers:**
- `supplier_category`: raw_materials, packaging, logistics, etc.
- `region`: Geographic region
- `payment_terms`: NET30, NET60, etc.
- `currency`: USD, EUR, GBP
- `vendor_code`: System-specific vendor code

**Tax Codes:**
- `tax_type`: vat_standard, vat_reduced, customs_duty, etc.
- `jurisdiction`: Country code
- `rate_percent`: Tax rate as integer
- `applies_to`: goods, services, both

## Pair Schema (`pairs_tier*.json`)

Each pair represents two entities to be compared for matching.

```json
{
  "pair_id": "t1_001",
  "entity_a": "erp_alpha_prod_001",
  "entity_b": "erp_beta_prod_023",
  "label": "match",
  "tier": 1,
  "difficulty_notes": "String variation pattern: abbreviation"
}
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `pair_id` | string | Unique identifier: `t{tier}_{number}` |
| `entity_a` | string | Reference to first entity's `entity_id` |
| `entity_b` | string | Reference to second entity's `entity_id` |
| `label` | string | Ground truth: `match`, `no_match`, or `ambiguous` |
| `tier` | integer | Difficulty tier: 1, 2, or 3 |
| `difficulty_notes` | string | Human-readable explanation of why this pair is challenging |

### Tier 3 Additional Fields

Tier 3 pairs may include references to required institutional knowledge:

```json
{
  "pair_id": "t3_015",
  "entity_a": "legacy_sigma_prod_044",
  "entity_b": "erp_alpha_prod_001",
  "label": "match",
  "tier": 3,
  "difficulty_notes": "Requires decision: migration_mapping",
  "requires_decision_id": "dec_003"
}
```

Or:

```json
{
  "pair_id": "t3_022",
  "entity_a": "erp_alpha_prod_012",
  "entity_b": "erp_beta_prod_034",
  "label": "no_match",
  "tier": 3,
  "difficulty_notes": "Requires rule: regional_override",
  "requires_rule_id": "rule_004"
}
```

### Labels

| Label | Description | Usage |
|-------|-------------|-------|
| `match` | Entities represent the same real-world thing | ~50-60% of pairs |
| `no_match` | Entities represent different real-world things | ~40-50% of pairs |
| `ambiguous` | Insufficient evidence for definitive determination | ~5-10% of Tier 3 only |

## Rules Schema (`rules.json`)

Rules encode business logic and regulatory requirements.

```json
{
  "rule_id": "rule_001",
  "rule_type": "classification",
  "scope": {
    "entity_types": ["product"],
    "jurisdictions": ["DE", "EU"],
    "categories": ["modified starches"]
  },
  "condition": "When maltodextrin product has dextrose_equivalent > 20",
  "action": "Classify under CN 1702.90, not CN 1702.30",
  "reasoning": "EU Combined Nomenclature distinguishes maltodextrin by DE threshold.",
  "effective_date": "2020-01-01",
  "status": "active"
}
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `rule_id` | string | Unique identifier |
| `rule_type` | string | `classification`, `regional_override`, `temporal_validity`, `threshold_based`, `regulatory_compliance` |
| `scope` | object | Conditions for when rule applies |
| `condition` | string | Human-readable condition |
| `action` | string | What to do when condition is met |
| `reasoning` | string | Business justification |
| `effective_date` | string | ISO date when rule became effective |
| `expiry_date` | string | Optional ISO date when rule expires |
| `status` | string | `active` or `superseded` |

### Rule Types

| Type | Description |
|------|-------------|
| `classification` | Rules about tariff/product classification based on attributes |
| `regional_override` | Region-specific exceptions to global rules |
| `temporal_validity` | Rules that apply only to specific time periods |
| `threshold_based` | Rules based on numeric thresholds (concentration, grade) |
| `regulatory_compliance` | Rules required for regulatory compliance (certifications, export control) |

## Decisions Schema (`decisions.json`)

Decisions encode historical expert judgments and migration mappings.

```json
{
  "decision_id": "dec_001",
  "decision_type": "migration_mapping",
  "entities_involved": ["legacy_sigma_prod_044", "erp_alpha_prod_001"],
  "decision": "These entities represent the same product. SIGMA code migrated to ALPHA during 2023 system decommission.",
  "made_by": "expert",
  "date": "2023-08-20",
  "context": "Part of LEGACY_SIGMA decommission project.",
  "status": "validated"
}
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `decision_id` | string | Unique identifier |
| `decision_type` | string | Type of decision (see below) |
| `entities_involved` | array | List of entity IDs this decision applies to |
| `decision` | string | The actual decision/ruling |
| `made_by` | string | `expert`, `system`, `committee` |
| `date` | string | ISO date of decision |
| `context` | string | Background information |
| `status` | string | `validated`, `pending`, `superseded` |

### Decision Types

| Type | Description |
|------|-------------|
| `migration_mapping` | Maps entities across system migrations |
| `subsidiary_alias` | Identifies legal entities that are aliases |
| `expert_override` | Expert judgment overriding automated matching |
| `merger_consolidation` | Records of entity mergers/consolidations |
| `split_separation` | Records of entity splits |

## Prediction Format

Submissions must follow this format:

```json
[
  {"pair_id": "t1_001", "predicted_label": "match"},
  {"pair_id": "t1_002", "predicted_label": "no_match"},
  {"pair_id": "t2_001", "predicted_label": "match"},
  ...
]
```

### Requirements

- Must be a JSON array
- Each element must have `pair_id` and `predicted_label`
- `predicted_label` must be one of: `match`, `no_match`, `ambiguous`
- All pair IDs from the benchmark must be included
- No duplicate pair IDs

### Validation

Use the format checker to validate submissions:

```bash
python eval/format_checker.py predictions.json --data-dir data/
```
