# Legal Entity Naming Conventions: ERP_ALPHA

> **Last Updated:** 2024-03-12
> **Owner:** Data Governance Team

## Overview

This page documents the naming conventions used for legal entity entities
in the ERP_ALPHA system. Understanding these conventions is critical for proper
entity matching and data integration.

## Historical Context

Prior to the 2023 system consolidation, legal entity records existed in
multiple systems with different naming conventions. This document provides the
authoritative reference for ERP_ALPHA-specific conventions.

### System Characteristics


- **Type**: Global headquarters ERP (SAP-like)
- **Naming Style**: Formal English, structured format
- **Code Prefix**: PRD (products), SUP (suppliers), LE (legal entities)
- **Attribute Completeness**: 95%


## Naming Patterns

### Standard Format

`{Product Name} {Concentration}% {Grade}`

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
| Sodium Chloride 70% Grade B | LEGACY_SIGMA | SIG-30-PVA-ZMF8 | Yes |
| Sodium Chloride 70% Grade B | ERP_GAMMA | SO-CH-70-GR-B-821 | Yes |
| Sodium Chloride 70% Grade B | ERP_DELTA | sodium chloride 70% standard | Yes |
| Fructose Grade A | LEGACY_SIGMA | SIG-44-SRN-1MKF | Yes |
| Fructose Grade A | ERP_GAMMA | FR-GR-A-600 | Yes |
| Resistant Starch | LEGACY_SIGMA | SIG-41-SWO-23GD | Yes |
| Resistant Starch | ERP_GAMMA | RE-ST-223 | Yes |
| Resistant Starch | ERP_BETA | Resistente Stärke | Yes |
| Resistant Starch | ERP_DELTA | resistant starch | Yes |
| Casein 25% Pharma Grade | LEGACY_SIGMA | SIG-79-HZP-CLBR | Yes |


## Business Rules

> **IMPORTANT:** The following rules MUST be applied when matching entities:

- When maltodextrin product has dextrose_equivalent > 20 -> Classify under CN 1702.90, not CN 1702.30
- When glucose syrup has fructose content > 50% -> Reclassify as high-fructose corn syrup under HTS 1702.60
- When protein content >= 90% by dry weight -> Classify as isolate (CN 3504.00.90), not concentrate (CN 3504.00.10)


## Data Quality Considerations

### Common Issues

1. **Duplicate Detection**: ERP_ALPHA may contain duplicate records due to
   historical data entry issues. Always verify against product specifications.

2. **Missing Attributes**: Approximately 8% of records
   have incomplete attribute data. Use fallback matching rules.

3. **Code Reuse**: Some legacy codes were reused for different products over
   time. Check effective dates when matching.

### Quality Metrics

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Completeness | 75% | 95% | On Track |
| Accuracy | 94% | 99% | Met |
| Consistency | 87% | 95% | Met |

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2023-01-15 | Initial documentation | Data Governance |
| 2023-03-01 | Added mapping table | Integration Team |
| 2023-06-15 | Updated rules section | Compliance |
| 2023-09-01 | Quality metrics added | Data Quality |


## Related Pages

- [System Integration Guide](/wiki/integration-guide)
- [Regulatory Compliance Guide](/wiki/compliance)
- [Master Data Governance Overview](/wiki/mdm-overview)

---

*This page is maintained by the Data Governance team. For updates, contact
data-governance@company.com or submit a ticket via ServiceNow.*
