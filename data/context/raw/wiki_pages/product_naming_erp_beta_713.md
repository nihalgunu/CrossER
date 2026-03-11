# Product Naming Conventions: ERP_BETA

> **Last Updated:** 2023-10-10
> **Owner:** Data Governance Team

## Overview

This page documents the naming conventions used for product entities
in the ERP_BETA system. Understanding these conventions is critical for proper
entity matching and data integration.

## Historical Context

Prior to the 2023 system consolidation, product records existed in
multiple systems with different naming conventions. This document provides the
authoritative reference for ERP_BETA-specific conventions.

### System Characteristics


- **Type**: European subsidiary ERP (Oracle-like)
- **Naming Style**: German formal, EU conventions
- **Code Prefix**: EU
- **Attribute Completeness**: 90%
- **Special Notes**: Uses German product names (e.g., "Zitronensäure" for Citric Acid)


## Naming Patterns

### Standard Format

`{Produktname} {Konzentration}% {Qualität}`

### Common Variations

The following variations are commonly observed:

| Pattern | Example | Notes |
|---------|---------|-------|
| Full formal name | "Maltodextrin DE20 Grade A" | Standard ERP_ALPHA format |
| Abbreviated | "MLTDX-DE20-A" | Common in ERP_GAMMA |
| Legacy code | "SIG-44-XXX-YYYY" | LEGACY_SIGMA format |
| Regional | "Maltodextrin-Pulver" | German variant (ERP_BETA) |


## Cross-System Mapping Reference

The following table shows known mappings between this system and others:

| This System | Other System | Other Code | Verified |
|-------------|--------------|------------|----------|
| Kasein 25% Pharmazeutisch rein | ERP_ALPHA | Casein 25% Pharma Grade | Yes |
| Ascorbic Acid | ERP_ALPHA | Ascorbic Acid | Yes |


## Business Rules

> **IMPORTANT:** The following rules MUST be applied when matching entities:

- When maltodextrin product has dextrose_equivalent > 20 -> Classify under CN 1702.90, not CN 1702.30
- When glucose syrup has fructose content > 50% -> Reclassify as high-fructose corn syrup under HTS 1702.60
- When protein content >= 90% by dry weight -> Classify as isolate (CN 3504.00.90), not concentrate (CN 3504.00.10)


## Data Quality Considerations

### Common Issues

1. **Duplicate Detection**: ERP_BETA may contain duplicate records due to
   historical data entry issues. Always verify against product specifications.

2. **Missing Attributes**: Approximately 14% of records
   have incomplete attribute data. Use fallback matching rules.

3. **Code Reuse**: Some legacy codes were reused for different products over
   time. Check effective dates when matching.

### Quality Metrics

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Completeness | 79% | 95% | On Track |
| Accuracy | 97% | 99% | Met |
| Consistency | 91% | 95% | Met |

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2023-01-15 | Initial documentation | Data Governance |
| 2023-03-01 | Added mapping table | Integration Team |
| 2023-06-15 | Updated rules section | Compliance |
| 2023-09-01 | Quality metrics added | Data Quality |


## Related Pages

- [Regulatory Compliance Guide](/wiki/compliance)
- [Master Data Governance Overview](/wiki/mdm-overview)
- [Entity Lifecycle Management](/wiki/entity-lifecycle)

---

*This page is maintained by the Data Governance team. For updates, contact
data-governance@company.com or submit a ticket via ServiceNow.*
