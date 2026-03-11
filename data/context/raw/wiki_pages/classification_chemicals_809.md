# Classification Guidelines: Chemicals

> **Last Updated:** 2024-01-03
> **Owner:** Compliance Team

## Purpose

This document provides classification guidelines for chemicals products
as they relate to tariff codes, regulatory requirements, and internal categorization.

## Regulatory Background

Products in the chemicals category are subject to various regulatory
requirements depending on:
- Country of origin
- Country of destination
- Intended use (food grade vs technical grade)
- Concentration and purity levels

## Classification Rules

### Core Principles

1. **Concentration-Based Differentiation**: Products with different concentration
   values are considered DISTINCT entities for regulatory and pricing purposes.

2. **Grade-Based Separation**: Food Grade and Technical Grade variants must be
   maintained as separate master data records.

3. **Regional Variants**: Products with regional-specific formulations are
   tracked separately.

### Specific Rules

**classification**: When maltodextrin product has dextrose_equivalent > 20 → Classify under CN 1702.90, not CN 1702.30

**classification**: When glucose syrup has fructose content > 50% → Reclassify as high-fructose corn syrup under HTS 1702.60

**classification**: When protein content >= 90% by dry weight → Classify as isolate (CN 3504.00.90), not concentrate (CN 3504.00.10)

**regional_override**: Products with multiple concentration variants sold in Germany → Maintain separate master data records for each concentration variant even if global system consolidates them

**regional_override**: Food-grade vs technical-grade variants of same chemical compound → Treat as separate products regardless of chemical equivalence



### Examples

**Example 1: Concentration Differentiation**

`Citric Acid 70%` and `Citric Acid 99.5%` are DISTINCT products:
- Different pricing structures
- Different regulatory requirements
- Different storage/handling needs

**Example 2: Grade Differentiation**

`Maltodextrin Food Grade` and `Maltodextrin Technical Grade`:
- Separate FDA/regulatory tracking
- Cannot be merged even if same concentration

**Example 3: Regional Variant**

`Zitronensäure 70%` (DE) = `Citric Acid 70%` (US)
- These ARE the same product
- Name difference is purely language-based

## Cross-System References

The following table shows how entities in this category are represented
across different systems:

| ERP_ALPHA Code | Other System | Other Code | Notes |
|----------------|--------------|------------|-------|
| Coconut Oil 98% | ERP_BETA | Coconut Oil 98% | Verified |
| Sodium Benzoate 99.5% Grade A | LEGACY_SIGMA | SIG-13-JUR-FV2B | Verified |
| Sodium Benzoate 99.5% Grade A | ERP_GAMMA | SO-BE-99.5-GR-A-143 | Verified |
| Sodium Benzoate 99.5% Grade A | ERP_BETA | Natriumbenzoat 99.5% Qualitätsstufe I | Verified |
| Sodium Benzoate 99.5% Grade A | ERP_DELTA | sodium benzoate 99.5% premium | Verified |

### Important Exceptions

~~The following classifications were used prior to 2022-01-01 and are now deprecated:~~

| Old Classification | New Classification | Reason |
|-------------------|-------------------|--------|
| CN 1702.30 | CN 1702.90 | DE threshold change |
| Food-Industrial | Technical Grade | Regulatory update |

## Related Pages

- [Data Quality Standards](/wiki/data-quality)
- [Regulatory Compliance Guide](/wiki/compliance)
- [System Integration Guide](/wiki/integration-guide)

---

*For questions about classification, contact compliance@company.com*
