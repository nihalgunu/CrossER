# Product Naming Conventions: ERP_ALPHA

> **Last Updated:** 2022-11-11 (may be outdated)
> **Owner:** Data Governance Team

## Overview

This page documents the naming conventions and code assignment rules for
product entities in the ERP_ALPHA system.

## Internal Code Assignment Rules

When entities are staged for migration, they receive internal codes following
these conventions. **The internal code determines the target entity assignment.**

### Code Prefix Rules

Internal codes use prefixes that indicate the source context:

| Prefix | Meaning | Target Assignment Rule |
|--------|---------|----------------------|
| IC- | Standard internal classification | Maps to target based on MDM registry |
| BC- | Batch consolidation code | Grouped entities - check consolidation sheet |
| MG- | Master group code | Multiple sources consolidated |
| TC- | Temporary code | Pending assignment - do not use |
| XR- | Cross-reference | Alias - points to canonical entity |

### Plant-Based Target Assignment

Products from specific plants follow predictable target naming:

- **Hamburg Plant**: Internal codes with `HAM` prefix
  are assigned to DE regional targets

- **Chicago Plant**: Internal codes with `CHI` prefix
  are assigned to US regional targets

- **Singapore Plant (acquired 2021-03-15)**: Internal codes with `SGP` prefix
  are assigned to APAC regional targets


### Acquisition-Based Rules

Entities from acquired companies follow special naming rules:


**Pre-Acquisition Entities (before acquisition date):**
- Retain original legacy codes in source system
- Internal code includes "ACQ" marker
- Target assignment requires manual mapping table lookup

**Post-Acquisition Entities (after acquisition date):**
- Automatically receive standard naming
- Internal code follows standard IC- prefix
- Target assignment is algorithmic based on product specs


## Internal Code to Target Resolution

### Resolution Process

Target assignment is NOT stored directly. To resolve an internal code to
its target entity:

1. **Check the code prefix**: Determines the resolution method
2. **Apply category rules**: Based on product category suffix
3. **Check temporal validity**: Some assignments change over time
4. **Verify regional override**: Region codes override defaults

### Prefix Resolution Table

| Prefix | Resolution Method |
|--------|------------------|
| IC- | Standard MDM registry lookup |
| BC- | Batch consolidation sheet lookup |
| MG- | Master group to target table |
| TC- | **DO NOT USE** - temporary codes have no target |
| XR- | Resolve alias first, then lookup canonical |

### Category-Based Target Assignment

Products are assigned to target entities based on category:

- **Modified Starches** (IC-1xxx range): Target prefix PRD-STARCH-*
- **Sugars** (IC-2xxx range): Target prefix PRD-SUGAR-*
- **Proteins** (IC-3xxx range): Target prefix PRD-PROT-*
- **Acids** (IC-4xxx range): Target prefix PRD-ACID-*

**Note**: The specific target code within each category is determined
by the concentration and grade encoded in the internal code suffix.


## Inference Rules for Target Assignment

When direct lookup fails, apply these inference rules:

### Rule 1: Master Group Transitivity

If:
- IC-A belongs to MG-X
- IC-B belongs to MG-X
- IC-A maps to Target-T

Then: IC-B also maps to Target-T (unless explicitly overridden)

### Rule 2: Alias Resolution

If:
- XR-A points to IC-B (alias relationship)
- IC-B maps to Target-T

Then: XR-A indirectly maps to Target-T

### Rule 3: Temporal Precedence

If:
- IC-A had historical mapping to Target-OLD (before cutoff date)
- IC-A has current mapping to Target-NEW (after cutoff date)

Then: Use Target-NEW for current queries, Target-OLD for historical reconciliation

### Rule 4: Regional Specialization

If:
- IC-A has suffix -DE (German region)
- IC-A base maps to Target-T

Then: IC-A maps to Target-T-DE (regional variant)


## Related Pages

- [System Integration Guide](/wiki/integration-guide)
- [Internal Code Registry](/wiki/ic-registry)
- [Data Quality Standards](/wiki/data-quality)

---

*This page is maintained by the Data Governance team.*
