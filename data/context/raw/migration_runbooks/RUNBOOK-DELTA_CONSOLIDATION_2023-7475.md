# Migration Runbook: Regional Operations Consolidation

**Document ID**: RB-DELTA_CONSOLIDATION_2023-5744
**Version**: 2.0
**Last Updated**: 2023-07-18
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the Regional Operations Consolidation project.
The migration involves transitioning master data and transactional records from ERP_DELTA
to ERP_ALPHA while maintaining data integrity and business continuity.

**Project Timeline**: 2023-04-15 to 2023-09-18
**Business Sponsor**: Operations Excellence
**Technical Owner**: Regional IT

### Key Milestones

- Phase 1: Assessment and Planning (Completed)
- Phase 2: Data Profiling and Mapping (Completed)
- Phase 3: Migration Execution (In Progress)
- Phase 4: Validation and Go-Live (Scheduled)

### Risk Summary

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Data quality issues | Medium | High | Pre-migration cleansing |
| Business disruption | Low | High | Staged rollout |
| Integration failures | Medium | Medium | Extensive testing |

## Pre-Migration Checklist

### Infrastructure Readiness

- [x] Target system capacity verified
- [x] Network connectivity tested between source and target
- [x] Backup procedures in place
- [x] Rollback scripts prepared and tested
- [x] Monitoring dashboards configured

### Data Readiness

- [x] Source data profiled and documented
- [x] Data quality issues identified and remediated
- [x] Internal code assignments completed
- [x] Test migrations completed in non-production
- [x] UAT sign-off received

### Stakeholder Readiness

- [x] Business users trained on new system
- [x] Support team briefed on escalation procedures
- [x] Communication plan executed
- [x] Go/No-Go decision documented

## Technical Architecture

### System Topology

```
+------------------+     +------------------+     +------------------+
|   ERP_DELTA       |     |   Staging Layer  |     |   ERP_ALPHA       |
|   (Source)       | --> |   (Internal Codes)| --> |   (Target)       |
+------------------+     +------------------+     +------------------+
        |                        |                        |
        v                        v                        v
+------------------+     +------------------+     +------------------+
|   Source DB      |     |   Code Registry  |     |   Target DB      |
+------------------+     +------------------+     +------------------+
```

### Migration Strategy

**IMPORTANT**: All source entities are first assigned to intermediate codes
in the staging layer. Target system mappings are managed separately by the
Master Data team. This runbook ONLY documents the source-to-staging assignments.

For target assignments, refer to:
- MDM-MAPPING-REGISTRY (separate system)
- Master Data Consolidation spreadsheets
- Data Governance Wiki pages

### Integration Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| Extract | Custom Python | Pull data from source APIs |
| Stage | Internal Codes | Intermediate representation |
| Load | Batch Insert | Write to target system |
| Validate | SQL scripts | Post-load verification |

### Performance Specifications

- Batch size: 10,000 records per transaction
- Parallel threads: 8
- Expected throughput: 50,000 records/hour
- Total migration window: 72 hours

## Testing and Validation

### Test Phases

#### Phase 1: Unit Testing
- Individual code assignment validation
- Data type conversion verification
- Null handling tests

#### Phase 2: Integration Testing
- End-to-end staging flow validation
- Internal code uniqueness checks
- API compatibility tests

#### Phase 3: User Acceptance Testing
- Business scenario validation
- Report reconciliation
- Workflow continuity

### Test Data Summary

| Entity Type | Source Count | Staged | Assigned Code | Status |
|-------------|--------------|--------|---------------|--------|
| Products | 2,450 | 2,450 | 2,448 | 99.9% |
| Suppliers | 1,200 | 1,198 | 1,198 | 99.8% |
| Legal Entities | 350 | 350 | 350 | 100% |
| Tax Codes | 180 | 180 | 180 | 100% |

### Known Issues

1. Two product records require manual review due to duplicate detection
2. Supplier payment terms converted using default values where missing
3. Internal codes cross-referenced in MDM registry

## Section 4: Staging Layer Assignments

### 4.1 Scope Overview

This section documents the internal code assignments for entities migrating from
ERP_DELTA. Each source entity is assigned an internal staging code for
tracking purposes.

**IMPORTANT**: This document only contains source-to-staging assignments.
Target system mappings are maintained separately in the MDM Registry.

### 4.2 Assignment Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1343 | Completed |
| Codes assigned | 951 | Staged |
| Excluded from scope | 285 | Documented |
| Pending review | 3 | In Progress |

### 4.3 Internal Code Reference

#### 4.3.1 Code Assignment Methodology

Internal codes were assigned using the following process:
1. Source entity validated against data quality rules
2. Unique internal code generated (format: XX-NNNN)
3. Code registered in staging database
4. Cross-reference created for downstream processing

**Code Prefixes:**
- IC: Internal Classification
- BC: Batch Consolidation
- TC: Temporary Code
- MR: Migration Reference

#### 4.3.2 Source Entity Code Assignments

The following source entities have been assigned internal staging codes.
These codes are used for tracking through the migration pipeline.

| Source Entity (ERP_DELTA) | Internal Code | Assignment Date | Department |
|--------------------------------|---------------|-----------------|------------|
| sodium chloride 70% standard | BC-1004 | 2023-12-15 | Finance |
| resistant starch | BC-1014 | 2022-06-25 | Data Governance |
| casein 25% pharma grade | IC-1021 | 2021-06-14 | Operations |
| ascorbic acid | IC-1028 | 2024-10-08 | Operations |
| isoglucose 70% | TC-1030 | 2023-06-25 | Finance |
| pea protein 50% | IC-1031 | 2022-03-12 | IT Infrastructure |
| sunflower oil 98% premium | BC-1041 | 2023-05-12 | Data Governance |
| pea protein 99.5% | TC-1052 | 2023-10-27 | Operations |
| ascorbic acid standard | BC-1057 | 2022-04-09 | Supply Chain |
| citric acid 70% | BC-1072 | 2022-12-08 | Finance |
| ascorbic acid pharma grade | BC-1079 | 2021-02-18 | Product Management |
| coconut oil food grade | TC-1085 | 2024-09-18 | Data Governance |
| palm oil 98% | IC-1091 | 2023-05-15 | Operations |
| rapeseed oil | IC-1098 | 2024-03-17 | Data Governance |
| wheat gluten 98% premium | TC-1109 | 2022-11-25 | Operations |
| sodium benzoate 99.5% premium | TC-1137 | 2021-03-06 | Product Management |
| sodium benzoate 99.5% standard | BC-1141 | 2024-03-13 | Product Management |
| cyclodextrin 98% pharma grade | TC-1148 | 2023-03-15 | Supply Chain |
| coconut oil premium | IC-1158 | 2023-04-08 | Compliance |
| dextrose standard | BC-1167 | 2022-08-20 | IT Infrastructure |
| lactic acid | BC-1178 | 2022-06-04 | Product Management |
| potassium sorbate | BC-1190 | 2023-09-21 | Finance |
| sodium benzoate 99.5% | BC-1199 | 2024-04-28 | Compliance |
| wheat gluten | TC-1204 | 2021-02-13 | IT Infrastructure |
| palm oil 50% premium | BC-1215 | 2021-12-03 | Product Management |
| isoglucose | BC-1221 | 2021-05-19 | Product Management |
| pea protein pharma grade | IC-1224 | 2024-09-11 | IT Infrastructure |
| soy isolate 70% | TC-1230 | 2021-09-17 | Compliance |
| soy isolate 25% tech grade | IC-1239 | 2022-02-04 | Operations |
| rapeseed oil | IC-1256 | 2024-01-01 | Finance |
| resistant starch | TC-1262 | 2023-03-28 | IT Infrastructure |
| glucose syrup | IC-1272 | 2023-04-24 | Data Governance |
| resistant starch pharma grade | BC-1283 | 2021-12-05 | Compliance |
| casein standard | IC-1288 | 2023-10-04 | IT Infrastructure |
| sodium benzoate 99.5% | TC-1300 | 2023-03-25 | Compliance |
| maltodextrin de5 premium | IC-1312 | 2021-10-21 | IT Infrastructure |
| rapeseed oil 70% standard | IC-1316 | 2024-02-08 | Supply Chain |
| sorbic acid food grade | IC-1321 | 2024-05-22 | Operations |
| lactic acid 98% | TC-1327 | 2023-02-19 | IT Infrastructure |
| ascorbic acid | IC-1332 | 2024-01-05 | IT Infrastructure |
| coconut oil 25% standard | TC-1338 | 2021-06-05 | Finance |
| citric acid | BC-1343 | 2022-04-06 | Data Governance |
| citric acid pharma grade | IC-1352 | 2022-12-06 | IT Infrastructure |
| soy isolate 99.5% standard | TC-1357 | 2022-08-05 | Supply Chain |
| palm oil 98% | TC-1364 | 2023-05-08 | Finance |
| sunflower oil 50% premium | BC-1373 | 2022-10-09 | Finance |
| sorbic acid 98% | TC-1383 | 2022-06-27 | Data Governance |
| ascorbic acid 99.5% | IC-1386 | 2023-09-01 | Operations |
| resistant starch 98% pharma grade | BC-1390 | 2023-04-05 | Product Management |
| sodium benzoate | IC-1412 | 2021-05-21 | Product Management |
| dextrose 25% tech grade | TC-1416 | 2024-11-26 | Operations |
| lactic acid food grade | BC-1423 | 2021-12-21 | Data Governance |
| sorbic acid | TC-1430 | 2022-01-17 | Product Management |
| rapeseed oil tech grade | TC-1434 | 2022-04-20 | IT Infrastructure |
| dextrin pharma grade | IC-1441 | 2021-03-24 | Product Management |
| citric acid 99.5% | IC-1447 | 2021-07-26 | Operations |
| sodium benzoate premium | BC-1451 | 2023-02-03 | Data Governance |
| dextrose 25% | TC-1455 | 2021-03-18 | Supply Chain |
| dextrose | IC-1461 | 2021-10-03 | Supply Chain |
| rapeseed oil tech grade | TC-1465 | 2021-01-28 | IT Infrastructure |
| citric acid 99.5% | IC-1474 | 2021-04-05 | Operations |
| resistant starch standard | IC-1482 | 2024-10-18 | Product Management |
| fructose 25% | BC-1488 | 2022-09-18 | Supply Chain |
| soy isolate 25% | TC-1498 | 2024-06-25 | Data Governance |
| rapeseed oil 99.5% | TC-1519 | 2021-03-13 | Finance |
| glucose syrup 98% food grade | BC-1526 | 2023-01-18 | Product Management |
| soy isolate | TC-1535 | 2022-07-22 | Operations |
| dextrose premium | TC-1540 | 2021-08-08 | IT Infrastructure |
| sodium chloride premium | TC-1542 | 2022-06-24 | Finance |
| dextrin 50% | TC-1559 | 2021-01-24 | Compliance |
| sodium chloride 98% standard | TC-1566 | 2024-06-12 | Operations |
| glucose syrup tech grade | IC-1571 | 2021-10-22 | Data Governance |
| soy isolate 99.5% premium | TC-1580 | 2022-05-23 | Operations |
| pea protein standard | BC-1587 | 2024-08-08 | Operations |
| soy isolate 25% | TC-1598 | 2021-09-09 | IT Infrastructure |
| dextrin | TC-1605 | 2024-03-20 | Data Governance |
| wheat gluten standard | TC-1611 | 2023-09-18 | Data Governance |
| sunflower oil standard | BC-1621 | 2022-10-08 | Supply Chain |
| sunflower oil standard | TC-1630 | 2022-11-22 | Finance |
| casein premium | TC-1636 | 2023-05-28 | Finance |
| dextrin tech grade | BC-1649 | 2023-05-26 | Compliance |
| wheat gluten 50% pharma grade | TC-1656 | 2022-09-11 | Data Governance |
| soy isolate | BC-1660 | 2021-05-25 | Compliance |
| sodium benzoate premium | IC-1666 | 2022-07-23 | Finance |
| potassium sorbate | IC-1674 | 2022-05-27 | IT Infrastructure |
| fructose 99.5% pharma grade | IC-1678 | 2024-10-02 | Data Governance |
| sodium benzoate | IC-1683 | 2023-04-04 | IT Infrastructure |
| sodium benzoate 25% | IC-1693 | 2022-07-19 | Data Governance |
| calcium carbonate standard | TC-1705 | 2022-06-14 | Data Governance |
| ascorbic acid tech grade | BC-1719 | 2024-10-20 | Product Management |
| fructose 25% standard | BC-1724 | 2024-08-23 | Compliance |
| casein | IC-1737 | 2022-03-22 | Compliance |
| coconut oil | BC-1741 | 2024-09-08 | Product Management |
| potassium sorbate tech grade | IC-1744 | 2024-03-01 | Product Management |
| glucose syrup premium | TC-1749 | 2021-08-22 | Operations |
| isoglucose 70% | IC-1760 | 2022-08-17 | Supply Chain |
| ascorbic acid 50% tech grade | TC-1764 | 2023-07-13 | Operations |
| dextrose food grade | IC-1770 | 2023-11-18 | Data Governance |
| sodium benzoate | IC-1775 | 2023-08-22 | Product Management |
| palm oil 50% | BC-1784 | 2023-02-14 | Compliance |
| ascorbic acid 98% premium | IC-1788 | 2023-12-16 | Finance |
| sorbic acid 70% | TC-1794 | 2024-08-05 | Supply Chain |
| pea protein standard | IC-1811 | 2023-07-03 | IT Infrastructure |
| citric acid 25% premium | TC-1814 | 2021-12-22 | Data Governance |
| sodium chloride 25% premium | IC-1819 | 2022-01-23 | Operations |
| calcium carbonate standard | BC-1824 | 2023-05-21 | Finance |
| soy isolate | TC-1828 | 2021-03-06 | Compliance |
| potassium sorbate | IC-1833 | 2021-03-21 | Operations |
| cyclodextrin pharma grade | IC-1835 | 2024-01-08 | Finance |
| fructose food grade | BC-1843 | 2023-01-01 | Operations |
| citric acid | BC-1847 | 2022-08-04 | Data Governance |
| ascorbic acid 70% | TC-1852 | 2022-06-10 | Data Governance |
| sorbic acid 98% | IC-1853 | 2024-05-10 | Data Governance |
| cyclodextrin | TC-1860 | 2024-09-20 | Compliance |
| isoglucose food grade | TC-1878 | 2022-08-12 | Operations |
| dextrin 70% | IC-1886 | 2023-04-04 | Compliance |
| citric acid | BC-1900 | 2024-07-06 | Data Governance |
| sunflower oil premium | BC-1903 | 2021-11-05 | Supply Chain |
| sodium benzoate 98% standard | IC-1906 | 2021-09-10 | Data Governance |
| lactic acid 98% premium | BC-1912 | 2022-08-17 | Product Management |
| ascorbic acid premium | TC-1916 | 2023-12-20 | Supply Chain |
| glucose syrup tech grade | BC-1924 | 2023-03-04 | Finance |
| rapeseed oil tech grade | TC-1934 | 2021-02-25 | IT Infrastructure |
| glucose syrup 98% standard | TC-1941 | 2021-07-25 | IT Infrastructure |
| soy isolate premium | IC-1947 | 2022-02-20 | IT Infrastructure |
| rapeseed oil | BC-1956 | 2022-05-10 | Compliance |
| sodium benzoate 99.5% tech grade | TC-1967 | 2023-10-10 | Operations |
| dextrose | IC-1969 | 2021-12-14 | Product Management |
| palm oil | TC-1982 | 2021-07-23 | Compliance |
| sorbic acid 25% pharma grade | TC-1983 | 2023-11-04 | Compliance |
| ascorbic acid standard | IC-1992 | 2024-07-22 | Data Governance |
| citric acid food grade | TC-1996 | 2022-07-22 | Supply Chain |
| soy isolate premium | TC-2001 | 2022-08-21 | IT Infrastructure |
| wheat gluten standard | BC-2009 | 2023-12-20 | Product Management |
| glucose syrup 98% | IC-2021 | 2021-12-10 | Operations |
| rapeseed oil 70% premium | IC-2030 | 2024-08-01 | Product Management |
| citric acid 99.5% | BC-2037 | 2023-08-03 | IT Infrastructure |
| rapeseed oil | TC-2046 | 2024-02-05 | Operations |
| palm oil 98% | BC-2053 | 2023-05-23 | Data Governance |
| fructose standard | TC-2058 | 2022-04-11 | Product Management |
| lactic acid 70% pharma grade | TC-2078 | 2022-12-23 | Product Management |
| potassium sorbate premium | TC-2085 | 2021-08-11 | Data Governance |
| sodium chloride | TC-2094 | 2024-12-25 | Finance |
| fructose | TC-2100 | 2021-12-27 | Supply Chain |
| fructose standard | IC-2120 | 2023-07-27 | Compliance |
| ascorbic acid | TC-2129 | 2021-08-20 | Supply Chain |
| pea protein premium | TC-2133 | 2021-09-24 | Data Governance |
| fructose | BC-2138 | 2024-06-20 | Finance |
| rapeseed oil 98% | BC-2150 | 2024-03-03 | Compliance |
| rapeseed oil 98% standard | IC-2151 | 2021-05-03 | Operations |
| casein | BC-2155 | 2021-01-22 | Product Management |
| potassium sorbate 50% standard | BC-2157 | 2024-07-07 | Operations |
| rapeseed oil premium | BC-2168 | 2021-05-03 | Finance |
| pea protein 98% standard | BC-2177 | 2022-08-10 | Data Governance |
| dextrose premium | BC-2195 | 2024-12-26 | IT Infrastructure |
| lactic acid | TC-2206 | 2022-10-01 | Compliance |
| calcium carbonate 50% premium | TC-2208 | 2024-04-19 | Finance |
| lactic acid tech grade | TC-2220 | 2021-12-08 | IT Infrastructure |
| coconut oil pharma grade | TC-2224 | 2021-06-14 | IT Infrastructure |
| isoglucose 70% food grade | BC-2228 | 2021-07-15 | IT Infrastructure |
| dextrose 25% | BC-2237 | 2023-03-08 | Operations |
| dextrose standard | IC-2243 | 2021-10-07 | Product Management |
| resistant starch standard | BC-2255 | 2023-12-05 | Data Governance |
| lactic acid premium | TC-2263 | 2021-07-16 | Operations |
| dextrin premium | BC-2270 | 2022-11-16 | Product Management |
| soy isolate 70% | TC-2278 | 2022-09-07 | Compliance |
| pea protein 25% pharma grade | IC-2287 | 2021-04-15 | Supply Chain |
| citric acid 99.5% pharma grade | IC-2290 | 2021-12-19 | Operations |
| pea protein tech grade | TC-2294 | 2024-12-28 | Supply Chain |
| fructose premium | IC-2310 | 2022-06-17 | Data Governance |
| glucose syrup | IC-2319 | 2024-02-03 | Finance |
| citric acid premium | TC-2324 | 2024-01-27 | Finance |
| resistant starch | BC-2340 | 2021-07-21 | Supply Chain |
| potassium sorbate standard | IC-2347 | 2024-06-02 | Supply Chain |
| citric acid | IC-2352 | 2024-06-21 | Data Governance |
| lactic acid food grade | BC-2357 | 2022-10-10 | Finance |
| citric acid 25% tech grade | TC-2364 | 2024-06-25 | Compliance |
| dextrin 50% | TC-2369 | 2024-06-01 | Product Management |
| isoglucose | IC-2375 | 2023-12-17 | Data Governance |
| sunflower oil 70% | BC-2378 | 2023-12-15 | Supply Chain |
| pea protein | IC-2390 | 2022-01-07 | Data Governance |
| rapeseed oil | TC-2394 | 2024-11-10 | Operations |
| wheat gluten premium | IC-2399 | 2022-06-17 | Supply Chain |
| maltodextrin de18 pharma grade | BC-2410 | 2023-11-23 | Data Governance |
| dextrose 70% premium | BC-2424 | 2021-07-26 | Supply Chain |
| calcium carbonate 50% pharma grade | TC-2431 | 2022-02-01 | Data Governance |
| rapeseed oil 50% standard | BC-2433 | 2024-05-05 | Product Management |
| sodium benzoate 25% standard | BC-2441 | 2023-06-14 | IT Infrastructure |
| sodium benzoate 50% | TC-2452 | 2024-02-18 | Compliance |
| coconut oil | TC-2459 | 2024-12-24 | Finance |
| fructose | BC-2464 | 2022-05-04 | Finance |
| citric acid | TC-2477 | 2021-08-28 | Supply Chain |
| dextrin premium | BC-2492 | 2022-03-08 | Data Governance |
| maltodextrin de25 | TC-2507 | 2024-09-10 | Product Management |
| sorbic acid food grade | TC-2517 | 2024-05-22 | IT Infrastructure |
| lactic acid food grade | BC-2541 | 2023-09-28 | Supply Chain |
| coconut oil standard | IC-2550 | 2023-03-13 | Operations |
| fructose tech grade | BC-2556 | 2024-08-15 | Data Governance |
| ascorbic acid | BC-2564 | 2023-04-07 | Product Management |
| lactic acid | TC-2571 | 2023-07-14 | IT Infrastructure |
| coconut oil 98% food grade | BC-2582 | 2021-04-25 | Supply Chain |
| potassium sorbate tech grade | IC-2594 | 2021-04-21 | Supply Chain |
| rapeseed oil standard | BC-2599 | 2022-10-02 | Supply Chain |
| calcium carbonate 25% pharma grade | IC-2610 | 2023-12-25 | Compliance |
| maltodextrin de5 standard | BC-2617 | 2024-07-02 | Finance |
| glucose syrup | TC-2635 | 2023-05-14 | Compliance |
| maltodextrin de25 | TC-2646 | 2022-10-26 | Compliance |
| lactic acid food grade | IC-2658 | 2024-08-05 | Finance |
| casein 98% standard | BC-2663 | 2021-07-24 | Supply Chain |
| casein standard | BC-2674 | 2024-11-17 | Product Management |
| resistant starch tech grade | IC-2679 | 2024-07-02 | Supply Chain |
| palm oil standard | BC-2687 | 2022-09-19 | IT Infrastructure |
| soy isolate standard | IC-2698 | 2022-06-22 | IT Infrastructure |
| ascorbic acid standard | IC-2709 | 2022-07-03 | IT Infrastructure |
| dextrose 50% | TC-2713 | 2023-01-10 | Operations |
| resistant starch 70% tech grade | TC-2718 | 2023-04-13 | Operations |
| glucose syrup food grade | IC-2723 | 2024-08-22 | Compliance |
| pea protein premium | IC-2728 | 2021-08-07 | Supply Chain |
| sodium benzoate 98% pharma grade | BC-2735 | 2023-02-06 | Data Governance |
| wheat gluten 98% | BC-2741 | 2022-09-08 | Operations |
| potassium sorbate 50% tech grade | IC-2746 | 2021-07-04 | IT Infrastructure |
| pea protein | BC-2749 | 2021-08-06 | Supply Chain |
| potassium sorbate standard | IC-2757 | 2023-05-23 | Product Management |
| sodium chloride 98% standard | BC-2765 | 2023-02-17 | Product Management |
| fructose 99.5% premium | BC-2771 | 2021-03-07 | Product Management |
| potassium sorbate 25% pharma grade | IC-2778 | 2022-07-16 | Operations |
| sodium benzoate 50% | IC-2782 | 2024-01-26 | Supply Chain |
| sodium benzoate | IC-2786 | 2023-07-12 | Operations |
| sorbic acid | TC-2803 | 2024-12-26 | Finance |
| resistant starch 98% | TC-2814 | 2021-11-01 | Product Management |
| calcium carbonate 99.5% food grade | TC-2819 | 2024-09-21 | Operations |
| fructose 99.5% food grade | BC-2826 | 2021-01-25 | IT Infrastructure |
| lactic acid standard | TC-2831 | 2021-12-19 | Finance |
| resistant starch tech grade | IC-2836 | 2024-01-01 | Data Governance |
| wheat gluten 99.5% premium | BC-2847 | 2022-03-15 | IT Infrastructure |
| sodium benzoate 99.5% tech grade | IC-2852 | 2021-05-17 | Compliance |
| sodium benzoate 99.5% premium | TC-2860 | 2023-07-20 | IT Infrastructure |
| ascorbic acid 50% | TC-2875 | 2021-06-12 | Compliance |
| potassium sorbate 50% tech grade | IC-2888 | 2022-01-02 | IT Infrastructure |
| calcium carbonate 50% | IC-2896 | 2022-05-16 | Data Governance |
| palm oil 50% | TC-2902 | 2022-06-06 | Product Management |
| potassium sorbate 98% | BC-2910 | 2022-03-05 | Product Management |
| resistant starch 70% food grade | IC-2918 | 2022-02-07 | Product Management |
| ascorbic acid | IC-2926 | 2021-12-22 | Finance |
| pea protein | TC-2931 | 2021-07-28 | IT Infrastructure |
| glucose syrup | TC-2937 | 2021-04-01 | Product Management |
| calcium carbonate 99.5% | TC-2944 | 2021-04-22 | Compliance |
| soy isolate standard | BC-2948 | 2024-05-02 | Compliance |
| palm oil 70% premium | TC-2954 | 2023-10-15 | Compliance |
| lactic acid standard | TC-2963 | 2023-10-22 | Compliance |
| palm oil food grade | BC-2966 | 2023-06-24 | Finance |
| lactic acid 98% | IC-2970 | 2024-09-18 | Finance |
| pea protein | TC-2972 | 2021-01-20 | Data Governance |
| potassium sorbate | TC-2978 | 2021-07-15 | Data Governance |
| palm oil pharma grade | BC-2985 | 2022-09-19 | Data Governance |
| soy isolate tech grade | TC-2991 | 2022-06-23 | Operations |
| coconut oil 98% tech grade | IC-2999 | 2021-01-07 | Compliance |
| casein premium | BC-3003 | 2023-05-21 | Compliance |
| coconut oil 98% | IC-3011 | 2024-03-09 | Supply Chain |
| dextrose | IC-3016 | 2024-03-09 | Product Management |
| sodium chloride | BC-3020 | 2024-01-01 | Data Governance |
| coconut oil 25% tech grade | BC-3025 | 2021-01-23 | Product Management |
| lactic acid 98% premium | TC-3031 | 2021-09-22 | Data Governance |
| isoglucose tech grade | BC-3035 | 2023-02-15 | Data Governance |
| pea protein 25% | BC-3039 | 2023-03-04 | Product Management |
| calcium carbonate 70% | TC-3046 | 2021-03-14 | Compliance |
| palm oil 99.5% premium | IC-3052 | 2021-06-02 | Operations |
| resistant starch 50% | BC-3060 | 2021-04-04 | Product Management |
| ascorbic acid pharma grade | BC-3066 | 2023-08-04 | Product Management |
| resistant starch food grade | BC-3074 | 2023-12-08 | IT Infrastructure |
| sorbic acid 70% | IC-3080 | 2023-01-21 | Data Governance |
| wheat gluten | IC-3084 | 2021-08-12 | Product Management |
| sodium benzoate food grade | IC-3093 | 2021-03-18 | Compliance |
| wheat gluten | IC-3098 | 2022-07-11 | IT Infrastructure |
| sodium benzoate 70% | IC-3102 | 2021-05-08 | Product Management |
| sorbic acid standard | BC-3113 | 2024-06-22 | IT Infrastructure |
| citric acid 25% | IC-3132 | 2023-11-28 | Finance |
| pea protein | IC-3139 | 2024-02-02 | IT Infrastructure |
| calcium carbonate 98% | BC-3148 | 2023-04-01 | Supply Chain |
| wheat gluten food grade | BC-3163 | 2024-12-02 | Product Management |
| citric acid premium | IC-3171 | 2023-09-20 | Supply Chain |
| coconut oil 25% food grade | TC-3178 | 2023-05-21 | Product Management |
| palm oil 99.5% | IC-3192 | 2022-03-17 | Data Governance |
| sodium benzoate | IC-3199 | 2022-01-12 | Operations |
| dextrose tech grade | TC-3208 | 2023-03-20 | IT Infrastructure |
| potassium sorbate standard | IC-3216 | 2023-08-16 | Supply Chain |
| dextrose food grade | IC-3223 | 2022-11-03 | Compliance |
| sorbic acid 50% food grade | TC-3247 | 2022-07-12 | Finance |
| soy isolate 99.5% | TC-3252 | 2023-05-03 | Product Management |
| rapeseed oil premium | TC-3258 | 2022-05-27 | Compliance |
| cyclodextrin | IC-3263 | 2021-07-12 | Supply Chain |
| dextrose standard | BC-3273 | 2024-07-25 | Supply Chain |
| glucose syrup 25% | TC-3275 | 2023-07-04 | Finance |
| calcium carbonate | TC-3279 | 2022-06-08 | Data Governance |
| resistant starch tech grade | BC-3280 | 2021-12-07 | Finance |
| dextrose 99.5% | IC-3285 | 2024-12-13 | IT Infrastructure |
| sodium benzoate 98% | BC-3289 | 2023-03-21 | Finance |
| palm oil 98% premium | IC-3294 | 2024-02-06 | Finance |
| sodium benzoate 50% | IC-3299 | 2023-03-22 | Finance |
| resistant starch 50% | BC-3306 | 2024-02-21 | Finance |
| dextrose 70% | TC-3314 | 2023-08-04 | Data Governance |
| dextrin 70% pharma grade | IC-3322 | 2023-03-02 | Data Governance |
| sorbic acid pharma grade | BC-3326 | 2024-10-24 | Product Management |
| pea protein | TC-3327 | 2024-03-06 | Compliance |
| fructose 99.5% tech grade | IC-3333 | 2023-01-26 | IT Infrastructure |
| pea protein 25% | IC-3338 | 2022-03-03 | Supply Chain |
| ascorbic acid tech grade | TC-3347 | 2021-08-10 | Supply Chain |
| sodium benzoate | TC-3353 | 2024-05-24 | Finance |
| lactic acid 25% premium | BC-3364 | 2023-03-13 | Data Governance |
| dextrose tech grade | IC-3370 | 2022-02-01 | Finance |
| dextrin 98% | IC-3376 | 2024-09-06 | Operations |
| soy isolate food grade | IC-3385 | 2021-08-08 | IT Infrastructure |
| calcium carbonate | TC-3395 | 2024-06-01 | Product Management |
| resistant starch 50% | IC-3407 | 2023-12-24 | IT Infrastructure |
| potassium sorbate 50% standard | IC-3409 | 2021-04-02 | Product Management |
| palm oil | IC-3414 | 2022-08-16 | Finance |
| fructose 50% standard | TC-3419 | 2024-08-22 | Product Management |
| maltodextrin de20 | IC-3428 | 2022-04-19 | Compliance |
| isoglucose | BC-3440 | 2022-03-14 | Supply Chain |
| cyclodextrin 70% food grade | TC-3445 | 2024-03-27 | Operations |
| ascorbic acid food grade | BC-3450 | 2021-03-06 | IT Infrastructure |
| sodium chloride | TC-3459 | 2021-08-11 | Product Management |
| dextrin | IC-3467 | 2022-09-18 | Finance |
| pea protein 70% premium | BC-3483 | 2024-11-24 | Compliance |
| soy isolate premium | BC-3489 | 2021-12-07 | Finance |
| sodium chloride | BC-3496 | 2021-01-20 | Supply Chain |
| lactic acid | IC-3501 | 2024-07-18 | Supply Chain |
| glucose syrup 99.5% food grade | IC-3514 | 2024-09-05 | Product Management |
| sodium benzoate | BC-3520 | 2021-11-13 | Data Governance |
| isoglucose standard | BC-3527 | 2021-02-06 | IT Infrastructure |
| lactic acid | BC-3535 | 2023-12-18 | Operations |
| rapeseed oil 70% tech grade | BC-3537 | 2022-05-23 | IT Infrastructure |
| glucose syrup 25% | TC-3545 | 2022-03-05 | Data Governance |
| sunflower oil premium | BC-3549 | 2023-05-06 | Supply Chain |
| fructose 70% | BC-3556 | 2021-01-16 | IT Infrastructure |
| citric acid standard | IC-3561 | 2024-06-03 | Data Governance |
| casein premium | IC-3568 | 2022-07-25 | Supply Chain |
| potassium sorbate | IC-3576 | 2024-05-15 | Supply Chain |
| resistant starch premium | TC-3584 | 2021-05-27 | Finance |
| ascorbic acid premium | BC-3595 | 2021-09-12 | Operations |
| sodium chloride 99.5% premium | IC-3601 | 2022-06-23 | Operations |
| palm oil 70% tech grade | BC-3606 | 2023-01-06 | Compliance |
| wheat gluten premium | IC-3613 | 2021-12-27 | Operations |
| cyclodextrin | BC-3631 | 2023-05-15 | Compliance |
| lactic acid tech grade | IC-3638 | 2024-06-09 | Supply Chain |
| potassium sorbate | IC-3646 | 2023-01-15 | Product Management |
| sorbic acid 25% standard | BC-3651 | 2024-05-18 | Supply Chain |
| wheat gluten 70% | TC-3664 | 2021-10-03 | Finance |
| soy isolate 99.5% | IC-3667 | 2022-11-04 | Compliance |
| coconut oil 25% standard | IC-3670 | 2024-10-18 | Supply Chain |
| potassium sorbate | TC-3685 | 2023-04-08 | Compliance |
| coconut oil 25% | IC-3696 | 2023-01-05 | Operations |
| dextrose | BC-3701 | 2021-09-13 | IT Infrastructure |
| sunflower oil 70% food grade | IC-3713 | 2021-09-03 | Finance |
| casein 50% premium | BC-3719 | 2023-01-04 | IT Infrastructure |
| lactic acid | IC-3732 | 2023-09-19 | Compliance |
| palm oil food grade | TC-3737 | 2022-07-04 | Product Management |
| resistant starch standard | TC-3747 | 2021-04-08 | Product Management |
| resistant starch | BC-3753 | 2022-04-09 | Supply Chain |
| sodium chloride tech grade | TC-3763 | 2024-07-03 | IT Infrastructure |
| coconut oil 98% premium | BC-3767 | 2022-06-25 | Product Management |
| potassium sorbate food grade | IC-3777 | 2023-06-07 | Compliance |
| sunflower oil | TC-3784 | 2024-04-27 | Compliance |
| sunflower oil 50% pharma grade | IC-3789 | 2024-02-08 | Finance |
| dextrin tech grade | IC-3805 | 2021-12-19 | Product Management |
| cyclodextrin standard | BC-3809 | 2022-01-26 | IT Infrastructure |
| casein 25% tech grade | BC-3814 | 2021-11-27 | IT Infrastructure |
| sodium benzoate premium | IC-3821 | 2021-11-28 | Operations |
| sunflower oil premium | IC-3836 | 2022-01-24 | Product Management |
| fructose standard | BC-3849 | 2024-02-19 | Supply Chain |
| soy isolate 50% premium | TC-3855 | 2023-03-27 | Product Management |
| resistant starch 70% | IC-3860 | 2024-04-01 | Data Governance |
| resistant starch | IC-3868 | 2023-11-19 | Operations |
| potassium sorbate food grade | TC-3875 | 2022-11-05 | Operations |
| citric acid | BC-3885 | 2021-10-10 | Compliance |
| soy isolate premium | BC-3893 | 2024-07-27 | Operations |
| pea protein standard | TC-3898 | 2021-10-28 | Finance |
| resistant starch 70% | IC-3905 | 2021-03-02 | IT Infrastructure |
| fructose premium | IC-3913 | 2024-06-17 | IT Infrastructure |
| dextrose | TC-3918 | 2024-10-11 | Finance |
| dextrose | BC-3922 | 2022-12-24 | Operations |
| sodium chloride 70% | IC-3928 | 2024-04-08 | Compliance |
| catalyst logistics SA | TC-3933 | 2022-11-23 | Operations |
| global distribution Corp. | IC-3947 | 2022-11-12 | Product Management |
| stellar distribution SA | TC-3965 | 2022-05-22 | Compliance |
| pinnacle ingredients Ltd. | IC-3970 | 2023-12-05 | Data Governance |
| central solutions | TC-3975 | 2021-03-28 | Data Governance |
| stratos ingredients | TC-3980 | 2021-09-06 | Operations |
| pacific logistics Holdings | BC-3991 | 2022-12-02 | Product Management |
| quantum ingredients Holdings | IC-4001 | 2022-01-11 | Data Governance |
| core chemicals Group | IC-4011 | 2023-08-27 | Product Management |
| continental solutions SARL | TC-4014 | 2023-03-18 | Supply Chain |
| pacific chemicals AG | IC-4028 | 2021-11-17 | Product Management |
| pacific distribution Group | IC-4038 | 2021-07-15 | Product Management |
| premier enterprise International | TC-4046 | 2023-08-14 | Data Governance |
| horizon materials | BC-4048 | 2022-07-11 | Operations |
| vertex enterprise Holdings | IC-4061 | 2022-02-19 | Operations |
| prime chemicals SA | IC-4066 | 2021-04-02 | Data Governance |
| stratos trading | TC-4078 | 2022-04-18 | Supply Chain |
| baltic enterprise KG | IC-4086 | 2021-02-26 | Supply Chain |
| premier logistics Ltd. | IC-4094 | 2021-03-08 | Finance |
| quantum manufacturing GmbH | BC-4101 | 2024-06-03 | Data Governance |
| continental manufacturing AG | TC-4106 | 2023-11-23 | Data Governance |
| atlas ingredients PLC | BC-4111 | 2021-10-23 | Operations |
| vertex distribution NV | BC-4117 | 2023-05-20 | Operations |
| atlas manufacturing | BC-4124 | 2024-05-20 | Supply Chain |
| atlantic manufacturing Group | BC-4129 | 2021-09-25 | IT Infrastructure |
| zenith manufacturing Group | BC-4138 | 2023-01-16 | Finance |
| central processing PLC | TC-4148 | 2022-10-28 | Supply Chain |
| stratos supply BV | TC-4152 | 2021-08-27 | Finance |
| stratos supply NV | TC-4155 | 2022-01-07 | Product Management |
| global processing | IC-4163 | 2023-12-20 | Data Governance |
| pinnacle supply Holdings | IC-4175 | 2023-04-15 | Product Management |
| pinnacle industries SAS | BC-4187 | 2021-10-19 | IT Infrastructure |
| pinnacle trading Inc. | BC-4195 | 2024-04-04 | Supply Chain |
| zenith partners | IC-4199 | 2021-02-16 | Product Management |
| prime supply PLC | TC-4213 | 2024-10-28 | IT Infrastructure |
| meridian trading Group | IC-4224 | 2023-11-10 | Compliance |
| global chemicals Ltd. | IC-4225 | 2021-10-10 | Supply Chain |
| prism ingredients NV | BC-4233 | 2022-03-06 | Operations |
| meridian solutions GmbH | IC-4248 | 2022-04-17 | Data Governance |
| apex chemicals Inc. | IC-4253 | 2021-08-14 | IT Infrastructure |
| nordic ingredients | IC-4261 | 2021-11-22 | Operations |
| global enterprise NV | BC-4269 | 2023-04-25 | Data Governance |
| vanguard enterprise International | TC-4274 | 2024-09-17 | Data Governance |
| global logistics | BC-4281 | 2021-07-24 | Supply Chain |
| continental enterprise GmbH | BC-4287 | 2022-02-10 | Compliance |
| core logistics Group | IC-4296 | 2021-06-25 | IT Infrastructure |
| core chemicals Holdings | TC-4303 | 2024-05-14 | IT Infrastructure |
| nexus industries | IC-4308 | 2024-02-03 | Data Governance |
| vertex solutions NV | TC-4320 | 2022-05-13 | Finance |
| nordic ingredients SARL | BC-4329 | 2022-06-11 | IT Infrastructure |
| atlantic trading | IC-4332 | 2024-07-17 | Compliance |
| premier logistics KG | TC-4337 | 2024-02-03 | Product Management |
| apex trading | IC-4355 | 2021-04-14 | IT Infrastructure |
| continental ingredients AG | BC-4363 | 2022-10-05 | Data Governance |
| nexus distribution AG | IC-4369 | 2024-12-18 | IT Infrastructure |
| catalyst industries Holdings | TC-4384 | 2023-06-15 | Data Governance |
| pinnacle commodities BV | BC-4396 | 2021-03-05 | Data Governance |
| premier solutions Corp. | BC-4403 | 2023-03-14 | Product Management |
| core supply | BC-4408 | 2021-11-15 | Data Governance |
| apex chemicals Inc. | TC-4413 | 2022-09-08 | Supply Chain |
| nexus enterprise | BC-4426 | 2022-04-12 | Compliance |
| apex chemicals International | BC-4433 | 2023-03-22 | Data Governance |
| atlas chemicals GmbH | TC-4444 | 2021-02-03 | Compliance |
| baltic chemicals | TC-4449 | 2024-12-20 | Operations |
| premier industries Holdings | TC-4456 | 2024-12-15 | Product Management |
| atlantic commodities | IC-4460 | 2021-01-05 | Supply Chain |
| prism ingredients | BC-4467 | 2023-10-23 | Finance |
| baltic solutions Inc. | BC-4478 | 2021-06-11 | Finance |
| apex ingredients KG | TC-4482 | 2022-03-23 | Finance |
| vertex distribution SAS | TC-4490 | 2024-03-17 | Product Management |
| central manufacturing NV | TC-4495 | 2022-07-21 | Operations |
| zenith trading LLC | TC-4502 | 2021-05-27 | Compliance |
| nexus distribution Corp. | IC-4507 | 2022-02-10 | Finance |
| meridian chemicals Holdings | TC-4508 | 2021-10-13 | IT Infrastructure |
| pinnacle ingredients GmbH | TC-4514 | 2024-06-02 | Compliance |
| nordic ingredients KG | BC-4519 | 2024-12-05 | Product Management |
| continental chemicals Corp. | IC-4525 | 2022-10-14 | Finance |
| horizon logistics International | TC-4531 | 2023-09-04 | Supply Chain |
| pinnacle chemicals Ltd. | TC-4534 | 2022-12-24 | Operations |
| nordic manufacturing Group | TC-4541 | 2022-01-25 | Supply Chain |
| catalyst enterprise | IC-4547 | 2024-11-15 | Finance |
| global solutions Group | TC-4558 | 2021-10-28 | Product Management |
| pacific ingredients NV | TC-4563 | 2021-11-13 | Product Management |
| atlas solutions | TC-4568 | 2022-09-09 | Operations |
| atlas enterprise | TC-4572 | 2023-01-07 | Data Governance |
| horizon partners Ltd. | IC-4584 | 2022-11-16 | IT Infrastructure |
| horizon industries KG | TC-4591 | 2023-06-26 | Supply Chain |
| baltic processing | TC-4607 | 2023-08-26 | Data Governance |
| nexus chemicals Group | IC-4613 | 2023-09-13 | IT Infrastructure |
| zenith partners Inc. | TC-4617 | 2021-07-03 | Data Governance |
| prism industries Corp. | IC-4622 | 2021-05-26 | Data Governance |
| prism materials | TC-4632 | 2022-07-19 | Supply Chain |
| core materials NV | BC-4636 | 2023-09-22 | Operations |
| nexus ingredients Ltd. | TC-4640 | 2024-05-02 | Finance |
| vertex ingredients | TC-4644 | 2024-03-11 | Product Management |
| continental solutions | BC-4653 | 2021-03-01 | IT Infrastructure |
| stellar commodities Holdings | IC-4660 | 2024-05-06 | Compliance |
| continental commodities | IC-4679 | 2024-05-15 | Operations |
| atlas industries Holdings | IC-4691 | 2021-12-11 | Compliance |
| vertex commodities AG | TC-4715 | 2024-04-21 | IT Infrastructure |
| atlantic processing Holdings | BC-4720 | 2021-12-05 | Product Management |
| quantum trading SARL | TC-4728 | 2022-01-06 | Product Management |
| atlantic industries International | IC-4735 | 2021-05-17 | Product Management |
| central manufacturing Group | TC-4739 | 2023-01-07 | Supply Chain |
| pinnacle supply | TC-4742 | 2022-06-28 | IT Infrastructure |
| atlantic trading BV | TC-4750 | 2022-07-09 | Finance |
| elite solutions Holdings | BC-4756 | 2022-06-17 | Compliance |
| atlantic logistics SARL | IC-4764 | 2024-02-26 | Operations |
| stratos processing LLC | IC-4768 | 2024-04-12 | Finance |
| central ingredients International | IC-4774 | 2022-03-13 | Operations |
| pacific industries International | IC-4776 | 2024-11-03 | Product Management |
| premier industries SARL | TC-4779 | 2024-05-28 | Finance |
| global trading PLC | BC-4781 | 2021-08-27 | Finance |
| premier enterprise Holdings | IC-4794 | 2021-03-03 | Product Management |
| baltic ingredients | IC-4799 | 2021-01-24 | Data Governance |
| zenith trading GmbH | IC-4807 | 2022-04-13 | Finance |
| prime solutions | IC-4814 | 2024-04-05 | IT Infrastructure |
| stellar distribution | BC-4822 | 2022-04-21 | Operations |
| premier trading GmbH | IC-4830 | 2024-10-22 | Compliance |
| nexus distribution Ltd. | TC-4842 | 2023-04-18 | Finance |
| central logistics SA | BC-4844 | 2023-11-19 | Data Governance |
| prism chemicals | BC-4847 | 2023-04-11 | Operations |
| pinnacle enterprise KG | IC-4850 | 2022-03-19 | Product Management |
| stellar processing | IC-4861 | 2022-06-15 | Operations |
| stellar partners Holdings | BC-4883 | 2022-05-06 | IT Infrastructure |
| meridian distribution Group | BC-4893 | 2022-08-18 | Operations |
| horizon trading Ltd. | TC-4905 | 2024-01-23 | Compliance |
| prism logistics BV | TC-4909 | 2024-04-02 | Supply Chain |
| atlantic industries International | IC-4917 | 2021-11-10 | Supply Chain |
| stellar manufacturing International | TC-4924 | 2021-10-22 | Operations |
| zenith manufacturing PLC | BC-4928 | 2024-01-05 | IT Infrastructure |
| apex materials Group | BC-4939 | 2022-05-27 | Supply Chain |
| horizon partners | IC-4948 | 2022-07-01 | Product Management |
| elite trading Group | BC-4953 | 2022-09-05 | Data Governance |
| continental processing Group | TC-4960 | 2022-05-18 | Compliance |
| elite materials NV | TC-4967 | 2023-03-15 | IT Infrastructure |
| baltic solutions Group | TC-4976 | 2022-07-16 | Finance |
| nexus supply | TC-4980 | 2024-06-07 | Supply Chain |
| pacific industries Ltd. | TC-4988 | 2024-02-15 | IT Infrastructure |
| stratos partners SA | TC-4995 | 2023-03-04 | IT Infrastructure |
| nexus ingredients SAS | BC-5007 | 2021-01-07 | Product Management |
| prism ingredients AG | TC-5014 | 2022-09-24 | IT Infrastructure |
| premier trading SARL | TC-5026 | 2023-07-20 | Finance |
| prism materials International | IC-5036 | 2024-05-28 | Operations |
| quantum processing SARL | BC-5044 | 2022-05-01 | Supply Chain |
| continental ingredients | TC-5048 | 2021-08-04 | Supply Chain |
| central manufacturing | BC-5051 | 2023-09-04 | Product Management |
| stratos processing | IC-5064 | 2021-04-21 | Product Management |
| premier distribution Group | BC-5083 | 2022-11-14 | Product Management |
| continental manufacturing Inc. | IC-5093 | 2024-10-26 | IT Infrastructure |
| nexus enterprise NV | IC-5098 | 2021-08-21 | Operations |
| baltic industries NV | IC-5105 | 2022-03-23 | IT Infrastructure |
| atlas partners | TC-5112 | 2021-04-03 | Operations |
| elite partners | BC-5117 | 2024-12-05 | Compliance |
| prism manufacturing Ltd. | IC-5127 | 2024-01-05 | Operations |
| nordic logistics Group | IC-5130 | 2023-03-15 | Operations |
| atlas materials | TC-5141 | 2023-02-21 | Compliance |
| atlantic distribution Holdings | BC-5146 | 2023-05-12 | Product Management |
| zenith materials | BC-5152 | 2023-07-03 | Supply Chain |
| quantum enterprise BV | IC-5155 | 2022-09-13 | Supply Chain |
| global chemicals SARL | BC-5162 | 2021-06-19 | Data Governance |
| meridian ingredients GmbH | IC-5167 | 2021-05-12 | Supply Chain |
| atlantic processing | IC-5180 | 2024-10-27 | Data Governance |
| vanguard industries PLC | IC-5183 | 2024-01-22 | IT Infrastructure |
| atlantic supply | IC-5201 | 2022-08-05 | IT Infrastructure |
| meridian trading Group | IC-5204 | 2022-01-24 | Supply Chain |
| pinnacle logistics | TC-5209 | 2022-05-14 | Supply Chain |
| pacific industries | TC-5215 | 2022-06-27 | IT Infrastructure |
| prime materials LLC | IC-5216 | 2022-05-13 | Product Management |
| premier manufacturing BV | IC-5221 | 2022-05-25 | Compliance |
| catalyst industries SAS | TC-5230 | 2021-03-23 | Product Management |
| premier partners SARL | BC-5235 | 2024-10-03 | Compliance |
| pinnacle materials SARL | BC-5252 | 2021-10-11 | Compliance |
| vanguard supply NV | TC-5255 | 2022-12-16 | IT Infrastructure |
| stratos commodities Holdings | TC-5260 | 2021-03-08 | Product Management |
| continental enterprise International | IC-5266 | 2021-09-14 | Product Management |
| apex manufacturing KG | IC-5275 | 2023-07-10 | Operations |
| apex processing Holdings | IC-5280 | 2023-06-28 | Operations |
| pacific materials GmbH | TC-5292 | 2024-07-10 | Product Management |
| vanguard partners Ltd. | TC-5294 | 2023-08-22 | Product Management |
| vanguard distribution International | IC-5303 | 2024-10-22 | Product Management |
| pinnacle logistics International | IC-5307 | 2024-02-21 | Finance |
| central partners SARL | BC-5317 | 2023-11-27 | Supply Chain |
| vertex logistics Holdings | BC-5334 | 2022-12-28 | Finance |
| stratos materials Holdings | BC-5343 | 2024-08-04 | Operations |
| quantum processing PLC | IC-5348 | 2024-07-25 | Operations |
| vanguard distribution | IC-5358 | 2023-01-02 | Product Management |
| core ingredients | IC-5363 | 2022-05-08 | Data Governance |
| baltic supply | TC-5371 | 2021-08-08 | Compliance |
| premier chemicals KG | IC-5376 | 2021-11-06 | Data Governance |
| premier supply PLC | TC-5382 | 2021-02-09 | Operations |
| meridian distribution Holdings | IC-5387 | 2021-07-23 | Finance |
| premier materials | TC-5398 | 2023-08-09 | Operations |
| horizon logistics PLC | BC-5404 | 2023-09-27 | Finance |
| premier logistics | BC-5411 | 2022-09-06 | Finance |
| stratos materials Group | TC-5412 | 2024-11-08 | Supply Chain |
| global partners BV | TC-5420 | 2024-07-24 | Compliance |
| nexus partners SARL | IC-5424 | 2024-09-26 | Compliance |
| core manufacturing SA | TC-5431 | 2023-01-12 | Product Management |
| continental processing SA | BC-5433 | 2024-11-15 | IT Infrastructure |
| baltic chemicals AG | IC-5441 | 2022-08-27 | Operations |
| atlantic trading PLC | TC-5454 | 2022-09-09 | Finance |
| central materials BV | IC-5461 | 2023-09-18 | Operations |
| central logistics International | IC-5465 | 2022-08-15 | Product Management |
| continental partners | BC-5475 | 2024-04-15 | IT Infrastructure |
| core processing Group | IC-5478 | 2021-06-19 | Operations |
| pacific enterprise | TC-5483 | 2024-09-06 | Finance |
| vanguard chemicals | TC-5491 | 2024-05-26 | Finance |
| vertex industries NV | BC-5498 | 2021-08-04 | Operations |
| pinnacle processing | IC-5505 | 2021-03-10 | Supply Chain |
| vertex commodities KG | TC-5514 | 2024-12-08 | Data Governance |
| catalyst supply Holdings | TC-5524 | 2022-06-25 | Supply Chain |
| core distribution BV | BC-5530 | 2022-03-27 | Compliance |
| premier enterprise | TC-5544 | 2022-08-15 | Supply Chain |
| nordic distribution AG | TC-5547 | 2023-02-04 | Product Management |
| catalyst ingredients | IC-5552 | 2023-07-05 | Data Governance |
| prime commodities PLC | TC-5562 | 2022-08-25 | Data Governance |
| pacific materials | IC-5567 | 2021-06-19 | IT Infrastructure |
| stellar distribution Corp. | IC-5572 | 2021-02-16 | Compliance |
| nordic processing SAS | IC-5579 | 2023-02-16 | Operations |
| core trading KG | TC-5583 | 2023-05-14 | IT Infrastructure |
| atlantic chemicals SAS | IC-5587 | 2021-11-05 | Operations |
| catalyst processing Holdings | BC-5591 | 2022-12-06 | Product Management |
| quantum processing International | IC-5594 | 2023-11-23 | Operations |
| quantum partners Group | TC-5598 | 2024-11-04 | Finance |
| zenith partners Inc. | IC-5604 | 2023-09-19 | Data Governance |
| zenith industries | TC-5613 | 2024-03-07 | Product Management |
| pinnacle industries KG | IC-5617 | 2021-06-23 | Compliance |
| premier partners Group | IC-5628 | 2021-08-21 | Data Governance |
| stratos solutions | TC-5632 | 2021-11-18 | Supply Chain |
| vertex distribution International | BC-5642 | 2022-06-26 | Compliance |
| quantum trading Holdings | BC-5655 | 2024-02-07 | Supply Chain |
| nexus logistics International | IC-5656 | 2021-11-04 | Operations |
| stellar manufacturing International | IC-5663 | 2021-08-21 | Operations |
| catalyst supply Holdings | TC-5681 | 2024-09-21 | Finance |
| atlas supply | BC-5686 | 2023-05-16 | Data Governance |
| baltic processing Holdings | TC-5701 | 2022-03-13 | IT Infrastructure |
| continental materials Corp. | BC-5707 | 2021-07-12 | Product Management |
| vertex chemicals International | IC-5714 | 2023-01-14 | Supply Chain |
| vanguard industries BV | BC-5724 | 2024-06-02 | Supply Chain |
| atlas industries | IC-5727 | 2024-10-15 | Data Governance |
| prime logistics Group | BC-5732 | 2023-12-24 | Product Management |
| apex logistics LLC | IC-5737 | 2024-05-26 | Operations |
| prime logistics | IC-5743 | 2024-09-28 | IT Infrastructure |
| atlantic materials | IC-5753 | 2023-02-20 | Supply Chain |
| core supply | BC-5758 | 2021-02-07 | Finance |
| premier supply | IC-5764 | 2024-03-10 | IT Infrastructure |
| premier supply | TC-5776 | 2022-08-16 | Finance |
| prism materials | TC-5782 | 2021-05-18 | Supply Chain |
| stratos logistics | BC-5792 | 2024-01-17 | Supply Chain |
| core materials | IC-5801 | 2021-06-13 | Finance |
| vertex materials | BC-5813 | 2023-06-05 | IT Infrastructure |
| meridian materials | TC-5818 | 2022-10-16 | Compliance |
| vertex logistics | BC-5824 | 2023-10-16 | Finance |
| nexus sourcing | IC-5845 | 2021-04-16 | Operations |
| central logistics | BC-5849 | 2023-11-20 | Supply Chain |
| pinnacle sourcing | BC-5864 | 2021-01-16 | Data Governance |
| elite sourcing | TC-5869 | 2023-08-28 | Product Management |
| vanguard materials | TC-5874 | 2022-07-10 | Data Governance |
| quantum supply | BC-5890 | 2021-10-10 | IT Infrastructure |
| zenith supply | IC-5893 | 2023-04-20 | IT Infrastructure |
| zenith supply | BC-5899 | 2021-11-18 | Operations |
| atlas supply | IC-5904 | 2023-05-15 | Finance |
| prism materials | TC-5917 | 2021-01-17 | Data Governance |
| atlas supply | BC-5933 | 2024-02-28 | Product Management |
| nexus logistics | TC-5951 | 2024-01-05 | Data Governance |
| stellar logistics | BC-5959 | 2021-01-06 | Supply Chain |
| vertex materials | TC-5982 | 2024-06-26 | Compliance |
| quantum supply | BC-5984 | 2022-02-07 | Data Governance |
| nexus logistics | IC-5989 | 2024-01-18 | IT Infrastructure |
| elite logistics | IC-5996 | 2024-08-14 | Finance |
| stratos sourcing | IC-6007 | 2022-12-13 | Finance |
| continental supply | IC-6019 | 2024-04-25 | Compliance |
| nexus logistics | IC-6025 | 2022-01-22 | Product Management |
| horizon materials | TC-6031 | 2022-03-14 | Compliance |
| quantum sourcing | TC-6034 | 2024-06-04 | IT Infrastructure |
| atlas logistics | TC-6043 | 2021-01-27 | Operations |
| prime supply | IC-6055 | 2021-08-03 | Product Management |
| stratos sourcing | TC-6059 | 2024-01-25 | Supply Chain |
| quantum supply | BC-6068 | 2021-12-22 | Product Management |
| quantum sourcing | BC-6080 | 2022-04-04 | IT Infrastructure |
| baltic logistics | BC-6083 | 2022-01-08 | Operations |
| prism sourcing | IC-6092 | 2021-01-16 | Product Management |
| central logistics | IC-6099 | 2023-08-11 | Operations |
| premier supply | TC-6108 | 2023-05-15 | Operations |
| apex supply | BC-6118 | 2021-05-23 | Operations |
| apex sourcing | IC-6122 | 2024-07-18 | Operations |
| apex logistics | BC-6142 | 2023-07-19 | Data Governance |
| elite logistics | TC-6152 | 2021-03-15 | Product Management |
| central materials | TC-6161 | 2024-11-06 | Data Governance |
| apex logistics | TC-6168 | 2023-03-17 | Operations |
| nordic sourcing | IC-6179 | 2023-03-25 | Operations |
| catalyst supply | TC-6180 | 2023-11-02 | Finance |
| catalyst sourcing | TC-6192 | 2024-04-16 | Data Governance |
| prism logistics | BC-6198 | 2024-10-07 | Operations |
| catalyst materials | BC-6202 | 2021-06-23 | IT Infrastructure |
| central sourcing | BC-6225 | 2023-11-13 | Operations |
| elite supply | TC-6232 | 2022-01-01 | Finance |
| pinnacle supply | BC-6243 | 2022-11-01 | Operations |
| core sourcing | BC-6247 | 2022-09-27 | Finance |
| horizon materials | TC-6254 | 2022-08-28 | Compliance |
| vanguard supply | BC-6258 | 2023-05-27 | IT Infrastructure |
| catalyst sourcing | IC-6275 | 2023-09-13 | Data Governance |
| zenith supply | TC-6281 | 2022-04-27 | Operations |
| nordic logistics | BC-6289 | 2024-09-03 | Operations |
| atlas logistics | BC-6293 | 2024-11-18 | Data Governance |
| continental logistics | TC-6299 | 2021-06-14 | Finance |
| prism sourcing | TC-6316 | 2022-07-12 | Operations |
| meridian sourcing | IC-6324 | 2021-08-13 | Data Governance |
| nordic supply | IC-6331 | 2021-12-17 | Data Governance |
| stratos materials | IC-6336 | 2021-09-14 | Data Governance |
| baltic supply | TC-6343 | 2021-12-19 | Finance |
| vertex supply | TC-6349 | 2022-06-20 | Operations |
| quantum supply | BC-6364 | 2024-11-09 | IT Infrastructure |
| nexus sourcing | TC-6368 | 2023-08-03 | Product Management |
| horizon sourcing | BC-6375 | 2023-07-26 | Finance |
| nexus materials | BC-6388 | 2021-10-26 | Product Management |
| core logistics | TC-6392 | 2023-11-28 | IT Infrastructure |
| baltic supply | IC-6394 | 2022-07-24 | Finance |
| apex sourcing | TC-6401 | 2021-08-01 | Compliance |
| atlas sourcing | TC-6406 | 2022-11-09 | Finance |
| pacific materials | BC-6412 | 2023-12-28 | Data Governance |
| vertex logistics | BC-6417 | 2022-06-24 | Compliance |
| continental logistics | TC-6423 | 2024-10-18 | Finance |
| pacific supply | TC-6429 | 2022-01-24 | Operations |
| horizon logistics | IC-6434 | 2024-12-10 | Operations |
| central logistics | TC-6435 | 2022-09-03 | Data Governance |
| nexus materials | TC-6438 | 2024-04-19 | Supply Chain |
| apex sourcing | IC-6448 | 2021-06-14 | Compliance |
| meridian materials | TC-6453 | 2023-08-23 | Supply Chain |
| stellar logistics | BC-6459 | 2021-10-08 | Operations |
| prism materials | IC-6465 | 2024-10-26 | Finance |
| apex logistics | TC-6468 | 2024-10-20 | Product Management |
| prism supply | BC-6474 | 2021-07-04 | Supply Chain |
| atlas logistics | BC-6481 | 2021-10-19 | Operations |
| zenith logistics | TC-6494 | 2023-05-06 | IT Infrastructure |
| pinnacle sourcing | BC-6499 | 2024-03-23 | IT Infrastructure |
| vertex sourcing | BC-6506 | 2023-07-07 | Product Management |
| stratos sourcing | BC-6511 | 2024-12-09 | Compliance |
| atlas materials | TC-6523 | 2024-04-14 | Product Management |
| continental supply | IC-6525 | 2024-02-05 | Product Management |
| nexus materials | TC-6532 | 2023-04-20 | Product Management |
| atlas materials | TC-6541 | 2023-10-09 | Finance |
| zenith logistics | TC-6563 | 2022-10-22 | Compliance |
| quantum materials | BC-6574 | 2023-06-04 | Operations |
| zenith sourcing | TC-6576 | 2022-01-07 | Operations |
| stratos sourcing | TC-6587 | 2024-06-03 | Finance |
| pinnacle logistics | IC-6599 | 2023-04-07 | Supply Chain |
| meridian logistics | BC-6608 | 2023-08-15 | Finance |
| atlantic materials | IC-6616 | 2023-11-15 | Product Management |
| meridian materials | TC-6622 | 2022-04-16 | Data Governance |
| pinnacle materials | IC-6625 | 2024-09-12 | Data Governance |
| central logistics | BC-6640 | 2021-09-22 | Supply Chain |
| nexus logistics | TC-6662 | 2021-04-14 | Compliance |
| global logistics | BC-6666 | 2022-07-20 | Finance |
| core sourcing | IC-6672 | 2024-12-21 | Data Governance |
| elite materials | BC-6677 | 2023-10-19 | Supply Chain |
| pinnacle sourcing | BC-6683 | 2021-01-24 | Supply Chain |
| vertex sourcing | TC-6688 | 2023-02-03 | Compliance |
| vertex materials | TC-6697 | 2021-10-07 | Compliance |
| pacific sourcing | IC-6716 | 2022-08-25 | Compliance |
| quantum supply | IC-6724 | 2021-02-04 | Product Management |
| premier logistics | BC-6731 | 2024-12-21 | Data Governance |
| prism sourcing | IC-6741 | 2022-10-11 | Operations |
| nordic supply | TC-6747 | 2024-08-03 | Operations |
| stratos logistics | IC-6752 | 2024-01-27 | Operations |
| elite sourcing | TC-6755 | 2023-01-06 | Data Governance |
| catalyst supply | BC-6759 | 2023-01-01 | Compliance |
| vertex materials | IC-6761 | 2022-07-08 | Compliance |
| pinnacle supply | TC-6769 | 2022-09-16 | Finance |
| atlantic materials | BC-6779 | 2022-02-25 | IT Infrastructure |
| nordic supply | BC-6788 | 2022-07-27 | Operations |
| atlas supply | BC-6795 | 2024-12-21 | Compliance |
| quantum supply | IC-6816 | 2023-02-20 | Product Management |
| pacific materials | BC-6826 | 2024-11-22 | Operations |
| stellar supply | BC-6830 | 2022-12-25 | Operations |
| pacific materials | TC-6834 | 2022-10-16 | Compliance |
| stratos logistics | IC-6841 | 2021-08-13 | Compliance |
| quantum supply | TC-6850 | 2024-11-23 | Compliance |
| elite logistics | IC-6855 | 2022-01-05 | Compliance |
| apex supply | TC-6861 | 2023-02-07 | Product Management |
| premier logistics | TC-6867 | 2024-09-19 | Supply Chain |
| pinnacle supply | BC-6877 | 2022-10-23 | Supply Chain |
| baltic sourcing | TC-6882 | 2021-04-01 | Supply Chain |
| elite materials | TC-6886 | 2023-09-04 | Data Governance |
| core sourcing | TC-6892 | 2024-08-26 | Finance |
| premier sourcing | BC-6902 | 2024-01-28 | Finance |
| quantum materials | IC-6916 | 2024-09-05 | Operations |
| meridian materials | BC-6921 | 2021-04-05 | Finance |
| vertex logistics | IC-6934 | 2022-04-08 | Operations |
| nexus sourcing | BC-6942 | 2022-04-05 | Supply Chain |
| baltic sourcing | BC-6946 | 2021-03-14 | IT Infrastructure |
| atlantic materials | IC-6949 | 2022-06-10 | Finance |
| vanguard supply | IC-6953 | 2021-11-19 | Data Governance |
| prism materials | BC-6960 | 2021-04-22 | Finance |
| atlas materials | IC-6966 | 2023-11-09 | Compliance |
| quantum logistics | TC-6969 | 2021-05-23 | Operations |
| vertex materials | TC-6972 | 2021-01-06 | Product Management |
| atlantic logistics | BC-6979 | 2021-09-08 | IT Infrastructure |
| prime sourcing | TC-6982 | 2023-12-13 | Product Management |
| stratos supply | TC-6989 | 2021-11-09 | Compliance |
| atlas materials | TC-6998 | 2022-09-15 | Supply Chain |
| apex supply | IC-7006 | 2024-08-18 | Compliance |
| vanguard logistics | IC-7019 | 2022-12-11 | Supply Chain |
| atlas supply | BC-7033 | 2022-10-27 | Finance |
| pinnacle supply | TC-7049 | 2022-03-12 | Product Management |
| stellar logistics | TC-7060 | 2023-12-13 | Operations |
| core supply | TC-7066 | 2023-09-24 | Supply Chain |
| nexus sourcing | IC-7074 | 2021-08-25 | Data Governance |
| stellar materials | BC-7090 | 2022-02-13 | Data Governance |
| atlas supply | BC-7098 | 2021-04-21 | Data Governance |
| atlantic sourcing | TC-7110 | 2021-11-22 | Product Management |
| prism logistics | BC-7114 | 2023-05-21 | IT Infrastructure |
| catalyst materials | BC-7121 | 2024-02-08 | Product Management |
| pacific supply | IC-7125 | 2024-01-27 | IT Infrastructure |
| prime materials | BC-7133 | 2021-02-10 | Compliance |
| vat reduced gb 15% | BC-7140 | 2022-01-01 | Compliance |
| excise nl 0% | TC-7146 | 2023-10-25 | Finance |
| excise de 7% | BC-7149 | 2023-12-07 | Product Management |
| withholding gb 5% | BC-7170 | 2023-08-21 | Finance |
| vat standard gb 21% | TC-7186 | 2023-11-18 | Operations |
| customs duty fr 19% | IC-7205 | 2023-09-14 | Supply Chain |
| vat standard nl 20% | BC-7215 | 2021-10-26 | Finance |
| withholding br 15% | IC-7222 | 2022-03-09 | Compliance |
| vat standard nl 20% | TC-7228 | 2022-12-12 | Compliance |
| withholding us 0% | IC-7234 | 2021-11-17 | Data Governance |
| vat reduced cn 21% | TC-7239 | 2023-03-14 | Compliance |
| excise in 21% | TC-7246 | 2024-08-05 | IT Infrastructure |
| vat standard nl 19% | IC-7250 | 2021-02-20 | Supply Chain |
| vat standard de 10% | BC-7257 | 2021-12-03 | Data Governance |
| vat standard us 5% | IC-7262 | 2021-01-01 | Finance |
| excise fr 0% | IC-7268 | 2022-09-12 | Operations |
| vat standard gb 5% | BC-7272 | 2024-04-23 | Finance |
| vat reduced gb 25% | BC-7277 | 2023-10-13 | Compliance |
| excise in 15% | IC-7287 | 2022-02-07 | Compliance |
| vat standard gb 21% | BC-7296 | 2023-05-26 | Data Governance |
| excise in 25% | TC-7304 | 2022-02-03 | Compliance |
| excise gb 19% | IC-7315 | 2021-01-24 | Operations |
| vat standard br 0% | IC-7321 | 2022-06-09 | Finance |
| vat standard fr 25% | TC-7329 | 2021-05-28 | Operations |
| vat standard fr 19% | TC-7338 | 2023-12-04 | Supply Chain |
| customs duty fr 19% | BC-7342 | 2024-01-28 | IT Infrastructure |
| vat reduced br 10% | BC-7346 | 2022-05-10 | IT Infrastructure |
| withholding gb 21% | BC-7352 | 2023-05-04 | Supply Chain |
| vat reduced br 25% | IC-7358 | 2024-07-24 | IT Infrastructure |
| vat standard de 7% | BC-7361 | 2022-07-21 | Supply Chain |
| customs duty br 5% | IC-7367 | 2024-10-06 | Operations |
| vat standard gb 20% | IC-7374 | 2024-07-23 | Supply Chain |
| customs duty de 5% | IC-7386 | 2024-12-02 | Compliance |
| vat reduced gb 19% | TC-7394 | 2021-10-21 | Data Governance |
| excise br 15% | IC-7402 | 2023-11-01 | Compliance |
| vat reduced in 5% | BC-7412 | 2022-12-04 | Supply Chain |
| vat standard us 10% | IC-7421 | 2021-01-01 | IT Infrastructure |
| withholding nl 7% | IC-7429 | 2021-09-28 | Data Governance |
| excise nl 7% | BC-7437 | 2023-04-16 | Operations |
| excise us 15% | BC-7449 | 2021-11-22 | Data Governance |
| withholding de 25% | BC-7453 | 2022-06-18 | Data Governance |
| withholding us 10% | BC-7460 | 2023-06-15 | Product Management |
| excise nl 21% | IC-7467 | 2022-06-11 | Compliance |
| withholding fr 19% | BC-7484 | 2021-03-03 | Finance |
| withholding fr 21% | IC-7490 | 2021-05-14 | IT Infrastructure |
| vat reduced in 20% | IC-7502 | 2022-02-28 | Compliance |
| vat standard nl 5% | TC-7511 | 2022-08-16 | Supply Chain |
| vat reduced br 15% | BC-7513 | 2022-12-15 | Operations |
| vat reduced fr 0% | IC-7522 | 2023-03-21 | Product Management |
| customs duty us 10% | IC-7528 | 2021-03-25 | IT Infrastructure |
| customs duty cn 10% | IC-7532 | 2023-04-12 | Operations |
| excise in 20% | BC-7537 | 2021-02-18 | IT Infrastructure |
| vat reduced br 21% | BC-7542 | 2023-04-15 | Supply Chain |
| vat reduced nl 19% | BC-7557 | 2021-06-21 | Data Governance |
| customs duty us 15% | BC-7564 | 2022-06-22 | Finance |
| vat reduced us 19% | TC-7570 | 2024-01-12 | Data Governance |
| excise br 25% | BC-7583 | 2023-07-03 | Operations |
| excise nl 20% | TC-7591 | 2022-09-07 | Data Governance |
| vat standard in 10% | TC-7599 | 2022-10-05 | Product Management |
| customs duty cn 25% | TC-7605 | 2023-07-03 | Data Governance |
| customs duty nl 15% | IC-7607 | 2021-12-17 | Operations |
| vat reduced de 5% | IC-7614 | 2023-12-19 | Data Governance |
| vat standard cn 10% | BC-7622 | 2021-05-14 | Finance |
| customs duty de 5% | IC-7626 | 2021-04-16 | IT Infrastructure |
| excise gb 0% | IC-7635 | 2022-12-17 | Compliance |
| excise gb 25% | IC-7639 | 2022-02-24 | Finance |
| vat standard de 21% | BC-7640 | 2021-08-27 | Data Governance |
| vat reduced br 15% | TC-7647 | 2023-04-12 | Supply Chain |
| customs duty in 25% | IC-7654 | 2021-11-26 | Data Governance |
| withholding nl 5% | BC-7657 | 2024-06-01 | IT Infrastructure |
| excise us 20% | IC-7664 | 2022-12-24 | Data Governance |
| customs duty in 21% | TC-7674 | 2022-01-16 | Compliance |
| customs duty br 7% | BC-7680 | 2021-09-19 | IT Infrastructure |
| withholding br 10% | IC-7689 | 2024-01-02 | IT Infrastructure |
| vat standard nl 20% | BC-7695 | 2021-07-28 | IT Infrastructure |
| vat standard nl 19% | IC-7706 | 2024-08-13 | Product Management |
| customs duty de 0% | IC-7712 | 2021-11-08 | IT Infrastructure |
| vat standard nl 5% | BC-7723 | 2023-04-20 | Finance |
| customs duty cn 25% | BC-7734 | 2022-01-25 | Compliance |
| withholding fr 5% | IC-7741 | 2023-09-13 | Compliance |
| vat standard in 5% | IC-7758 | 2023-11-09 | Operations |
| customs duty fr 15% | BC-7766 | 2023-10-26 | IT Infrastructure |
| customs duty gb 0% | TC-7773 | 2022-11-03 | Data Governance |
| excise cn 21% | IC-7777 | 2023-03-03 | Product Management |
| vat reduced br 10% | BC-7784 | 2021-12-17 | Supply Chain |
| vat standard cn 0% | BC-7788 | 2023-01-13 | Data Governance |
| customs duty gb 5% | IC-7794 | 2022-05-12 | Finance |
| customs duty cn 7% | TC-7800 | 2024-07-28 | Data Governance |
| vat reduced nl 20% | BC-7804 | 2023-07-24 | Supply Chain |
| customs duty de 20% | BC-7812 | 2024-09-28 | Product Management |
| vat standard gb 19% | TC-7817 | 2024-04-09 | Finance |
| customs duty fr 7% | TC-7826 | 2024-03-18 | Supply Chain |
| vat standard in 19% | TC-7831 | 2021-08-20 | Product Management |
| withholding cn 20% | TC-7838 | 2024-04-10 | Product Management |
| excise us 7% | BC-7846 | 2023-08-06 | Finance |
| vat standard nl 5% | IC-7855 | 2021-08-02 | Finance |
| withholding br 20% | IC-7860 | 2022-03-04 | IT Infrastructure |
| vat reduced cn 19% | IC-7868 | 2022-12-15 | Operations |
| customs duty in 20% | TC-7879 | 2021-12-14 | Operations |
| excise gb 5% | BC-7884 | 2024-06-12 | Finance |
| vat standard us 19% | BC-7894 | 2023-12-14 | Operations |
| vat reduced nl 5% | TC-7899 | 2021-01-27 | IT Infrastructure |
| vat reduced fr 20% | BC-7905 | 2022-05-21 | Operations |
| vat standard gb 19% | BC-7909 | 2022-04-25 | IT Infrastructure |
| excise nl 21% | TC-7912 | 2021-11-05 | Finance |
| vat standard us 21% | TC-7918 | 2023-01-04 | Compliance |
| customs duty br 20% | TC-7923 | 2023-12-28 | Finance |
| excise us 5% | BC-7929 | 2023-06-01 | Product Management |
| customs duty gb 5% | BC-7936 | 2022-10-14 | Finance |
| vat standard nl 20% | IC-7943 | 2022-09-03 | Compliance |
| customs duty cn 0% | IC-7956 | 2023-06-13 | Supply Chain |
| excise cn 21% | TC-7961 | 2022-12-20 | Finance |
| vat reduced cn 10% | TC-7966 | 2022-01-10 | Supply Chain |
| customs duty gb 0% | TC-7972 | 2023-08-01 | Finance |
| excise de 21% | TC-7980 | 2023-04-04 | Product Management |
| excise cn 20% | IC-7996 | 2022-09-25 | Finance |
| vat reduced nl 0% | IC-8002 | 2024-06-26 | Operations |
| vat reduced cn 15% | TC-8006 | 2022-10-15 | Product Management |
| vat reduced cn 0% | IC-8008 | 2022-03-04 | Operations |
| vat reduced gb 15% | IC-8017 | 2024-02-06 | Data Governance |
| withholding nl 19% | IC-8028 | 2024-04-17 | Product Management |
| vat reduced nl 25% | BC-8038 | 2023-12-05 | Operations |
| withholding gb 15% | TC-8051 | 2024-02-10 | Compliance |
| vat reduced gb 0% | TC-8058 | 2022-06-23 | Product Management |
| withholding nl 20% | IC-8066 | 2024-12-17 | Finance |
| withholding in 20% | IC-8078 | 2024-02-19 | Data Governance |
| excise fr 21% | IC-8084 | 2022-02-06 | Supply Chain |
| customs duty gb 7% | TC-8095 | 2022-01-28 | IT Infrastructure |
| withholding nl 21% | TC-8108 | 2022-02-12 | Data Governance |
| vat reduced us 21% | BC-8113 | 2021-05-01 | IT Infrastructure |
| customs duty nl 21% | IC-8117 | 2022-02-10 | Operations |
| customs duty nl 15% | BC-8136 | 2022-02-01 | Compliance |
| vat standard nl 20% | IC-8143 | 2024-03-18 | Compliance |
| customs duty br 21% | BC-8157 | 2024-02-24 | Supply Chain |
| vat reduced gb 25% | BC-8162 | 2024-04-08 | Finance |
| customs duty br 15% | TC-8167 | 2021-12-17 | Finance |
| withholding nl 15% | IC-8174 | 2022-10-26 | Product Management |
| vat reduced fr 20% | IC-8177 | 2024-05-19 | Data Governance |
| withholding us 21% | TC-8183 | 2022-04-24 | IT Infrastructure |
| customs duty de 20% | TC-8189 | 2021-07-18 | Supply Chain |
| customs duty de 7% | TC-8191 | 2022-01-05 | Supply Chain |
| withholding nl 21% | TC-8200 | 2023-01-13 | IT Infrastructure |
| vat reduced in 25% | BC-8208 | 2022-08-24 | Product Management |
| excise fr 21% | IC-8217 | 2023-04-12 | Finance |
| vat standard us 15% | TC-8222 | 2024-11-23 | Compliance |
| vat standard fr 0% | TC-8231 | 2022-05-25 | Supply Chain |
| customs duty fr 25% | IC-8239 | 2023-06-13 | Supply Chain |
| vat reduced in 5% | IC-8246 | 2022-03-10 | Operations |
| withholding fr 15% | TC-8253 | 2021-07-08 | Supply Chain |
| customs duty nl 15% | IC-8255 | 2023-01-14 | Operations |
| vat standard de 7% | TC-8262 | 2024-02-19 | IT Infrastructure |
| vat standard cn 19% | BC-8272 | 2021-05-09 | Supply Chain |
| vat standard in 0% | IC-8276 | 2024-10-10 | IT Infrastructure |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| sodium chloride 70% standard | IC-6382 | SUPERSEDED | Historical - verify before use |
| resistant starch | IC-6772 | DEPRECATED | Historical - verify before use |
| casein 25% pharma grade | IC-9695 | REVIEW REQUIRED | Historical - verify before use |
| ascorbic acid | IC-6146 | PROVISIONAL | Historical - verify before use |
| isoglucose 70% | IC-9054 | REVIEW REQUIRED | Historical - verify before use |
| pea protein 50% | IC-9566 | REVIEW REQUIRED | Historical - verify before use |
| sunflower oil 98% premium | IC-7271 | DEPRECATED | Historical - verify before use |
| pea protein 99.5% | IC-8195 | SUPERSEDED | Historical - verify before use |
| ascorbic acid standard | IC-7743 | SUPERSEDED | Historical - verify before use |
| citric acid 70% | IC-9448 | REVIEW REQUIRED | Historical - verify before use |
| ascorbic acid pharma grade | IC-9966 | REVIEW REQUIRED | Historical - verify before use |
| coconut oil food grade | IC-9734 | REVIEW REQUIRED | Historical - verify before use |
| palm oil 98% | IC-8792 | SUPERSEDED | Historical - verify before use |
| rapeseed oil | IC-5694 | PROVISIONAL | Historical - verify before use |
| wheat gluten 98% premium | IC-9277 | DEPRECATED | Historical - verify before use |
| sodium benzoate 99.5% premium | IC-7576 | REVIEW REQUIRED | Historical - verify before use |
| sodium benzoate 99.5% standard | IC-9177 | SUPERSEDED | Historical - verify before use |
| cyclodextrin 98% pharma grade | IC-9734 | PROVISIONAL | Historical - verify before use |
| coconut oil premium | IC-7953 | REVIEW REQUIRED | Historical - verify before use |
| dextrose standard | IC-5667 | PROVISIONAL | Historical - verify before use |
| lactic acid | IC-6158 | DEPRECATED | Historical - verify before use |
| potassium sorbate | IC-7970 | PROVISIONAL | Historical - verify before use |
| sodium benzoate 99.5% | IC-5519 | REVIEW REQUIRED | Historical - verify before use |
| wheat gluten | IC-5689 | REVIEW REQUIRED | Historical - verify before use |
| palm oil 50% premium | IC-9617 | SUPERSEDED | Historical - verify before use |
| isoglucose | IC-7130 | SUPERSEDED | Historical - verify before use |
| pea protein pharma grade | IC-6681 | REVIEW REQUIRED | Historical - verify before use |
| soy isolate 70% | IC-9296 | DEPRECATED | Historical - verify before use |
| soy isolate 25% tech grade | IC-8022 | SUPERSEDED | Historical - verify before use |
| rapeseed oil | IC-9356 | REVIEW REQUIRED | Historical - verify before use |
| resistant starch | IC-7334 | DEPRECATED | Historical - verify before use |
| glucose syrup | IC-5927 | SUPERSEDED | Historical - verify before use |
| resistant starch pharma grade | IC-8092 | SUPERSEDED | Historical - verify before use |
| casein standard | IC-9832 | SUPERSEDED | Historical - verify before use |
| sodium benzoate 99.5% | IC-7702 | DEPRECATED | Historical - verify before use |
| maltodextrin de5 premium | IC-9877 | REVIEW REQUIRED | Historical - verify before use |
| rapeseed oil 70% standard | IC-6747 | REVIEW REQUIRED | Historical - verify before use |
| sorbic acid food grade | IC-8578 | SUPERSEDED | Historical - verify before use |
| lactic acid 98% | IC-5380 | REVIEW REQUIRED | Historical - verify before use |
| ascorbic acid | IC-6590 | DEPRECATED | Historical - verify before use |
| coconut oil 25% standard | IC-7579 | REVIEW REQUIRED | Historical - verify before use |
| citric acid | IC-8022 | REVIEW REQUIRED | Historical - verify before use |
| citric acid pharma grade | IC-9728 | REVIEW REQUIRED | Historical - verify before use |
| soy isolate 99.5% standard | IC-9418 | PROVISIONAL | Historical - verify before use |
| palm oil 98% | IC-5618 | REVIEW REQUIRED | Historical - verify before use |
| sunflower oil 50% premium | IC-7879 | REVIEW REQUIRED | Historical - verify before use |
| sorbic acid 98% | IC-6506 | PROVISIONAL | Historical - verify before use |
| ascorbic acid 99.5% | IC-7449 | PROVISIONAL | Historical - verify before use |
| resistant starch 98% pharma grade | IC-8756 | REVIEW REQUIRED | Historical - verify before use |
| sodium benzoate | IC-7340 | DEPRECATED | Historical - verify before use |
| dextrose 25% tech grade | IC-5404 | DEPRECATED | Historical - verify before use |
| lactic acid food grade | IC-6674 | PROVISIONAL | Historical - verify before use |
| sorbic acid | IC-8133 | REVIEW REQUIRED | Historical - verify before use |
| rapeseed oil tech grade | IC-7611 | SUPERSEDED | Historical - verify before use |
| dextrin pharma grade | IC-7412 | DEPRECATED | Historical - verify before use |
| citric acid 99.5% | IC-5301 | REVIEW REQUIRED | Historical - verify before use |
| sodium benzoate premium | IC-8076 | SUPERSEDED | Historical - verify before use |
| dextrose 25% | IC-9779 | PROVISIONAL | Historical - verify before use |
| dextrose | IC-6591 | REVIEW REQUIRED | Historical - verify before use |
| rapeseed oil tech grade | IC-6557 | DEPRECATED | Historical - verify before use |
| citric acid 99.5% | IC-9745 | REVIEW REQUIRED | Historical - verify before use |
| resistant starch standard | IC-9590 | DEPRECATED | Historical - verify before use |
| fructose 25% | IC-5948 | REVIEW REQUIRED | Historical - verify before use |
| soy isolate 25% | IC-9120 | SUPERSEDED | Historical - verify before use |
| rapeseed oil 99.5% | IC-9732 | REVIEW REQUIRED | Historical - verify before use |
| glucose syrup 98% food grade | IC-8746 | DEPRECATED | Historical - verify before use |
| soy isolate | IC-6532 | SUPERSEDED | Historical - verify before use |
| dextrose premium | IC-9641 | PROVISIONAL | Historical - verify before use |
| sodium chloride premium | IC-6058 | PROVISIONAL | Historical - verify before use |
| dextrin 50% | IC-6143 | DEPRECATED | Historical - verify before use |
| sodium chloride 98% standard | IC-5494 | DEPRECATED | Historical - verify before use |
| glucose syrup tech grade | IC-7047 | REVIEW REQUIRED | Historical - verify before use |
| soy isolate 99.5% premium | IC-5462 | SUPERSEDED | Historical - verify before use |
| pea protein standard | IC-8408 | DEPRECATED | Historical - verify before use |
| soy isolate 25% | IC-8628 | DEPRECATED | Historical - verify before use |
| dextrin | IC-5781 | DEPRECATED | Historical - verify before use |
| wheat gluten standard | IC-7257 | SUPERSEDED | Historical - verify before use |
| sunflower oil standard | IC-8259 | SUPERSEDED | Historical - verify before use |
| sunflower oil standard | IC-5159 | PROVISIONAL | Historical - verify before use |
| casein premium | IC-8123 | SUPERSEDED | Historical - verify before use |
| dextrin tech grade | IC-6848 | PROVISIONAL | Historical - verify before use |
| wheat gluten 50% pharma grade | IC-9816 | REVIEW REQUIRED | Historical - verify before use |
| soy isolate | IC-7581 | SUPERSEDED | Historical - verify before use |
| sodium benzoate premium | IC-9185 | REVIEW REQUIRED | Historical - verify before use |
| potassium sorbate | IC-9067 | SUPERSEDED | Historical - verify before use |
| fructose 99.5% pharma grade | IC-7904 | DEPRECATED | Historical - verify before use |
| sodium benzoate | IC-6199 | DEPRECATED | Historical - verify before use |
| sodium benzoate 25% | IC-9444 | DEPRECATED | Historical - verify before use |
| calcium carbonate standard | IC-6511 | DEPRECATED | Historical - verify before use |
| ascorbic acid tech grade | IC-6164 | SUPERSEDED | Historical - verify before use |
| fructose 25% standard | IC-5385 | PROVISIONAL | Historical - verify before use |
| casein | IC-9058 | PROVISIONAL | Historical - verify before use |
| coconut oil | IC-6643 | DEPRECATED | Historical - verify before use |
| potassium sorbate tech grade | IC-9711 | REVIEW REQUIRED | Historical - verify before use |
| glucose syrup premium | IC-5813 | REVIEW REQUIRED | Historical - verify before use |
| isoglucose 70% | IC-8718 | PROVISIONAL | Historical - verify before use |
| ascorbic acid 50% tech grade | IC-6136 | DEPRECATED | Historical - verify before use |
| dextrose food grade | IC-8496 | DEPRECATED | Historical - verify before use |
| sodium benzoate | IC-7808 | PROVISIONAL | Historical - verify before use |
| palm oil 50% | IC-9299 | PROVISIONAL | Historical - verify before use |
| ascorbic acid 98% premium | IC-7188 | REVIEW REQUIRED | Historical - verify before use |
| sorbic acid 70% | IC-5970 | PROVISIONAL | Historical - verify before use |
| pea protein standard | IC-9359 | PROVISIONAL | Historical - verify before use |
| citric acid 25% premium | IC-6041 | PROVISIONAL | Historical - verify before use |
| sodium chloride 25% premium | IC-5939 | REVIEW REQUIRED | Historical - verify before use |
| calcium carbonate standard | IC-5905 | DEPRECATED | Historical - verify before use |
| soy isolate | IC-5428 | DEPRECATED | Historical - verify before use |
| potassium sorbate | IC-5401 | DEPRECATED | Historical - verify before use |
| cyclodextrin pharma grade | IC-9600 | SUPERSEDED | Historical - verify before use |
| fructose food grade | IC-8133 | DEPRECATED | Historical - verify before use |
| citric acid | IC-6360 | PROVISIONAL | Historical - verify before use |
| ascorbic acid 70% | IC-6358 | SUPERSEDED | Historical - verify before use |
| sorbic acid 98% | IC-6908 | PROVISIONAL | Historical - verify before use |
| cyclodextrin | IC-5377 | SUPERSEDED | Historical - verify before use |
| isoglucose food grade | IC-6388 | REVIEW REQUIRED | Historical - verify before use |
| dextrin 70% | IC-9109 | DEPRECATED | Historical - verify before use |
| citric acid | IC-5152 | REVIEW REQUIRED | Historical - verify before use |
| sunflower oil premium | IC-5805 | PROVISIONAL | Historical - verify before use |
| sodium benzoate 98% standard | IC-6879 | SUPERSEDED | Historical - verify before use |
| lactic acid 98% premium | IC-6441 | SUPERSEDED | Historical - verify before use |
| ascorbic acid premium | IC-6500 | DEPRECATED | Historical - verify before use |
| glucose syrup tech grade | IC-5751 | REVIEW REQUIRED | Historical - verify before use |
| rapeseed oil tech grade | IC-6834 | REVIEW REQUIRED | Historical - verify before use |
| glucose syrup 98% standard | IC-8920 | SUPERSEDED | Historical - verify before use |
| soy isolate premium | IC-8606 | SUPERSEDED | Historical - verify before use |
| rapeseed oil | IC-8191 | REVIEW REQUIRED | Historical - verify before use |
| sodium benzoate 99.5% tech grade | IC-7836 | SUPERSEDED | Historical - verify before use |
| dextrose | IC-9065 | PROVISIONAL | Historical - verify before use |
| palm oil | IC-8021 | SUPERSEDED | Historical - verify before use |
| sorbic acid 25% pharma grade | IC-5986 | SUPERSEDED | Historical - verify before use |
| ascorbic acid standard | IC-9530 | SUPERSEDED | Historical - verify before use |
| citric acid food grade | IC-9922 | SUPERSEDED | Historical - verify before use |
| soy isolate premium | IC-6591 | REVIEW REQUIRED | Historical - verify before use |
| wheat gluten standard | IC-8462 | SUPERSEDED | Historical - verify before use |
| glucose syrup 98% | IC-7469 | REVIEW REQUIRED | Historical - verify before use |
| rapeseed oil 70% premium | IC-6191 | DEPRECATED | Historical - verify before use |
| citric acid 99.5% | IC-5126 | PROVISIONAL | Historical - verify before use |
| rapeseed oil | IC-9310 | SUPERSEDED | Historical - verify before use |
| palm oil 98% | IC-6767 | PROVISIONAL | Historical - verify before use |
| fructose standard | IC-8684 | SUPERSEDED | Historical - verify before use |
| lactic acid 70% pharma grade | IC-9395 | DEPRECATED | Historical - verify before use |
| potassium sorbate premium | IC-7045 | PROVISIONAL | Historical - verify before use |
| sodium chloride | IC-8259 | SUPERSEDED | Historical - verify before use |
| fructose | IC-9836 | PROVISIONAL | Historical - verify before use |
| fructose standard | IC-9319 | DEPRECATED | Historical - verify before use |
| ascorbic acid | IC-6345 | PROVISIONAL | Historical - verify before use |
| pea protein premium | IC-8086 | DEPRECATED | Historical - verify before use |
| fructose | IC-7733 | SUPERSEDED | Historical - verify before use |
| rapeseed oil 98% | IC-8423 | REVIEW REQUIRED | Historical - verify before use |
| rapeseed oil 98% standard | IC-7176 | DEPRECATED | Historical - verify before use |
| casein | IC-7747 | REVIEW REQUIRED | Historical - verify before use |
| potassium sorbate 50% standard | IC-8624 | PROVISIONAL | Historical - verify before use |
| rapeseed oil premium | IC-5065 | SUPERSEDED | Historical - verify before use |
| pea protein 98% standard | IC-9847 | DEPRECATED | Historical - verify before use |
| dextrose premium | IC-9460 | SUPERSEDED | Historical - verify before use |
| lactic acid | IC-9107 | PROVISIONAL | Historical - verify before use |
| calcium carbonate 50% premium | IC-9924 | SUPERSEDED | Historical - verify before use |
| lactic acid tech grade | IC-5150 | DEPRECATED | Historical - verify before use |
| coconut oil pharma grade | IC-6330 | DEPRECATED | Historical - verify before use |
| isoglucose 70% food grade | IC-8398 | REVIEW REQUIRED | Historical - verify before use |
| dextrose 25% | IC-6854 | REVIEW REQUIRED | Historical - verify before use |
| dextrose standard | IC-8159 | REVIEW REQUIRED | Historical - verify before use |
| resistant starch standard | IC-9026 | PROVISIONAL | Historical - verify before use |
| lactic acid premium | IC-9959 | PROVISIONAL | Historical - verify before use |
| dextrin premium | IC-8347 | REVIEW REQUIRED | Historical - verify before use |
| soy isolate 70% | IC-7614 | REVIEW REQUIRED | Historical - verify before use |
| pea protein 25% pharma grade | IC-6925 | SUPERSEDED | Historical - verify before use |
| citric acid 99.5% pharma grade | IC-9152 | PROVISIONAL | Historical - verify before use |
| pea protein tech grade | IC-8863 | SUPERSEDED | Historical - verify before use |
| fructose premium | IC-7576 | REVIEW REQUIRED | Historical - verify before use |
| glucose syrup | IC-5553 | REVIEW REQUIRED | Historical - verify before use |
| citric acid premium | IC-8328 | DEPRECATED | Historical - verify before use |
| resistant starch | IC-8881 | SUPERSEDED | Historical - verify before use |
| potassium sorbate standard | IC-9514 | DEPRECATED | Historical - verify before use |
| citric acid | IC-5863 | REVIEW REQUIRED | Historical - verify before use |
| lactic acid food grade | IC-7347 | DEPRECATED | Historical - verify before use |
| citric acid 25% tech grade | IC-9797 | DEPRECATED | Historical - verify before use |
| dextrin 50% | IC-8545 | SUPERSEDED | Historical - verify before use |
| isoglucose | IC-9857 | SUPERSEDED | Historical - verify before use |
| sunflower oil 70% | IC-9534 | PROVISIONAL | Historical - verify before use |
| pea protein | IC-9485 | DEPRECATED | Historical - verify before use |
| rapeseed oil | IC-8764 | DEPRECATED | Historical - verify before use |
| wheat gluten premium | IC-7075 | DEPRECATED | Historical - verify before use |
| maltodextrin de18 pharma grade | IC-7181 | REVIEW REQUIRED | Historical - verify before use |
| dextrose 70% premium | IC-8832 | REVIEW REQUIRED | Historical - verify before use |
| calcium carbonate 50% pharma grade | IC-7443 | PROVISIONAL | Historical - verify before use |
| rapeseed oil 50% standard | IC-5968 | PROVISIONAL | Historical - verify before use |
| sodium benzoate 25% standard | IC-7096 | SUPERSEDED | Historical - verify before use |
| sodium benzoate 50% | IC-8251 | REVIEW REQUIRED | Historical - verify before use |
| coconut oil | IC-8939 | SUPERSEDED | Historical - verify before use |
| fructose | IC-7794 | REVIEW REQUIRED | Historical - verify before use |
| citric acid | IC-9977 | SUPERSEDED | Historical - verify before use |
| dextrin premium | IC-6584 | PROVISIONAL | Historical - verify before use |
| maltodextrin de25 | IC-7552 | DEPRECATED | Historical - verify before use |
| sorbic acid food grade | IC-7464 | DEPRECATED | Historical - verify before use |
| lactic acid food grade | IC-5542 | PROVISIONAL | Historical - verify before use |
| coconut oil standard | IC-9978 | SUPERSEDED | Historical - verify before use |
| fructose tech grade | IC-5775 | SUPERSEDED | Historical - verify before use |
| ascorbic acid | IC-6310 | REVIEW REQUIRED | Historical - verify before use |
| lactic acid | IC-6690 | REVIEW REQUIRED | Historical - verify before use |
| coconut oil 98% food grade | IC-5239 | DEPRECATED | Historical - verify before use |
| potassium sorbate tech grade | IC-8848 | PROVISIONAL | Historical - verify before use |
| rapeseed oil standard | IC-6330 | DEPRECATED | Historical - verify before use |
| calcium carbonate 25% pharma grade | IC-8161 | SUPERSEDED | Historical - verify before use |
| maltodextrin de5 standard | IC-9780 | DEPRECATED | Historical - verify before use |
| glucose syrup | IC-6193 | PROVISIONAL | Historical - verify before use |
| maltodextrin de25 | IC-7988 | REVIEW REQUIRED | Historical - verify before use |
| lactic acid food grade | IC-7738 | SUPERSEDED | Historical - verify before use |
| casein 98% standard | IC-7004 | SUPERSEDED | Historical - verify before use |
| casein standard | IC-8433 | DEPRECATED | Historical - verify before use |
| resistant starch tech grade | IC-8012 | PROVISIONAL | Historical - verify before use |
| palm oil standard | IC-5798 | PROVISIONAL | Historical - verify before use |
| soy isolate standard | IC-7370 | DEPRECATED | Historical - verify before use |
| ascorbic acid standard | IC-5272 | REVIEW REQUIRED | Historical - verify before use |
| dextrose 50% | IC-7164 | PROVISIONAL | Historical - verify before use |
| resistant starch 70% tech grade | IC-8078 | DEPRECATED | Historical - verify before use |
| glucose syrup food grade | IC-7458 | PROVISIONAL | Historical - verify before use |
| pea protein premium | IC-7156 | PROVISIONAL | Historical - verify before use |
| sodium benzoate 98% pharma grade | IC-9619 | DEPRECATED | Historical - verify before use |
| wheat gluten 98% | IC-8082 | PROVISIONAL | Historical - verify before use |
| potassium sorbate 50% tech grade | IC-8428 | SUPERSEDED | Historical - verify before use |
| pea protein | IC-6095 | PROVISIONAL | Historical - verify before use |
| potassium sorbate standard | IC-7243 | REVIEW REQUIRED | Historical - verify before use |
| sodium chloride 98% standard | IC-8090 | PROVISIONAL | Historical - verify before use |
| fructose 99.5% premium | IC-8702 | REVIEW REQUIRED | Historical - verify before use |
| potassium sorbate 25% pharma grade | IC-5746 | SUPERSEDED | Historical - verify before use |
| sodium benzoate 50% | IC-7043 | SUPERSEDED | Historical - verify before use |
| sodium benzoate | IC-6297 | SUPERSEDED | Historical - verify before use |
| sorbic acid | IC-8266 | DEPRECATED | Historical - verify before use |
| resistant starch 98% | IC-7227 | DEPRECATED | Historical - verify before use |
| calcium carbonate 99.5% food grade | IC-8829 | SUPERSEDED | Historical - verify before use |
| fructose 99.5% food grade | IC-7338 | REVIEW REQUIRED | Historical - verify before use |
| lactic acid standard | IC-6688 | DEPRECATED | Historical - verify before use |
| resistant starch tech grade | IC-6653 | SUPERSEDED | Historical - verify before use |
| wheat gluten 99.5% premium | IC-9462 | DEPRECATED | Historical - verify before use |
| sodium benzoate 99.5% tech grade | IC-7415 | SUPERSEDED | Historical - verify before use |
| sodium benzoate 99.5% premium | IC-9527 | DEPRECATED | Historical - verify before use |
| ascorbic acid 50% | IC-6528 | PROVISIONAL | Historical - verify before use |
| potassium sorbate 50% tech grade | IC-6214 | PROVISIONAL | Historical - verify before use |
| calcium carbonate 50% | IC-8924 | DEPRECATED | Historical - verify before use |
| palm oil 50% | IC-9895 | REVIEW REQUIRED | Historical - verify before use |
| potassium sorbate 98% | IC-8705 | SUPERSEDED | Historical - verify before use |
| resistant starch 70% food grade | IC-7898 | SUPERSEDED | Historical - verify before use |
| ascorbic acid | IC-5942 | PROVISIONAL | Historical - verify before use |
| pea protein | IC-9789 | REVIEW REQUIRED | Historical - verify before use |
| glucose syrup | IC-8232 | PROVISIONAL | Historical - verify before use |
| calcium carbonate 99.5% | IC-9497 | PROVISIONAL | Historical - verify before use |
| soy isolate standard | IC-8950 | REVIEW REQUIRED | Historical - verify before use |
| palm oil 70% premium | IC-5959 | PROVISIONAL | Historical - verify before use |
| lactic acid standard | IC-9769 | REVIEW REQUIRED | Historical - verify before use |
| palm oil food grade | IC-6816 | DEPRECATED | Historical - verify before use |
| lactic acid 98% | IC-8253 | DEPRECATED | Historical - verify before use |
| pea protein | IC-7837 | REVIEW REQUIRED | Historical - verify before use |
| potassium sorbate | IC-8391 | DEPRECATED | Historical - verify before use |
| palm oil pharma grade | IC-8867 | SUPERSEDED | Historical - verify before use |
| soy isolate tech grade | IC-9283 | REVIEW REQUIRED | Historical - verify before use |
| coconut oil 98% tech grade | IC-8752 | PROVISIONAL | Historical - verify before use |
| casein premium | IC-8259 | SUPERSEDED | Historical - verify before use |
| coconut oil 98% | IC-6815 | DEPRECATED | Historical - verify before use |
| dextrose | IC-7286 | PROVISIONAL | Historical - verify before use |
| sodium chloride | IC-9498 | SUPERSEDED | Historical - verify before use |
| coconut oil 25% tech grade | IC-8566 | SUPERSEDED | Historical - verify before use |
| lactic acid 98% premium | IC-6313 | DEPRECATED | Historical - verify before use |
| isoglucose tech grade | IC-5679 | SUPERSEDED | Historical - verify before use |
| pea protein 25% | IC-7262 | SUPERSEDED | Historical - verify before use |
| calcium carbonate 70% | IC-8136 | SUPERSEDED | Historical - verify before use |
| palm oil 99.5% premium | IC-6312 | SUPERSEDED | Historical - verify before use |
| resistant starch 50% | IC-8843 | REVIEW REQUIRED | Historical - verify before use |
| ascorbic acid pharma grade | IC-6197 | DEPRECATED | Historical - verify before use |
| resistant starch food grade | IC-7626 | DEPRECATED | Historical - verify before use |
| sorbic acid 70% | IC-9137 | PROVISIONAL | Historical - verify before use |
| wheat gluten | IC-8852 | DEPRECATED | Historical - verify before use |
| sodium benzoate food grade | IC-7932 | REVIEW REQUIRED | Historical - verify before use |
| wheat gluten | IC-8104 | SUPERSEDED | Historical - verify before use |
| sodium benzoate 70% | IC-9637 | DEPRECATED | Historical - verify before use |
| sorbic acid standard | IC-7901 | PROVISIONAL | Historical - verify before use |
| citric acid 25% | IC-5943 | PROVISIONAL | Historical - verify before use |
| pea protein | IC-7766 | REVIEW REQUIRED | Historical - verify before use |
| calcium carbonate 98% | IC-7358 | SUPERSEDED | Historical - verify before use |
| wheat gluten food grade | IC-7894 | SUPERSEDED | Historical - verify before use |
| citric acid premium | IC-6600 | PROVISIONAL | Historical - verify before use |
| coconut oil 25% food grade | IC-9663 | REVIEW REQUIRED | Historical - verify before use |
| palm oil 99.5% | IC-5690 | DEPRECATED | Historical - verify before use |
| sodium benzoate | IC-9525 | REVIEW REQUIRED | Historical - verify before use |
| dextrose tech grade | IC-8784 | REVIEW REQUIRED | Historical - verify before use |


#### 4.3.4 Excluded Assignments

Deprecated code assignments (superseded by newer records):

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-4547-B | Pending validation | Deferred to Phase 2 |
| NOISE-6740-E | Pending validation | Escalated to data steward |
| NOISE-4770-H | Missing required attributes | Manual review scheduled |
| NOISE-8843-H | Duplicate source record | Escalated to data steward |
| NOISE-2826-B | Duplicate source record | Escalated to data steward |
| NOISE-5809-E | Missing required attributes | Escalated to data steward |
| NOISE-2430-B | Out of scope per business decision | Manual review scheduled |
| NOISE-7373-E | Data quality insufficient | Business owner notified |
| NOISE-4383-B | Pending validation | Business owner notified |
| NOISE-9920-F | Missing required attributes | Business owner notified |
| NOISE-6160-G | Pending validation | Business owner notified |
| NOISE-6012-H | Out of scope per business decision | Business owner notified |
| NOISE-9728-E | Data quality insufficient | Business owner notified |
| NOISE-8273-A | Data quality insufficient | Business owner notified |
| NOISE-9758-G | Pending validation | Business owner notified |
| NOISE-9656-A | Pending validation | Business owner notified |
| NOISE-1232-G | Pending validation | Business owner notified |
| NOISE-9443-E | Duplicate source record | Business owner notified |
| NOISE-5734-F | Duplicate source record | Business owner notified |
| NOISE-8395-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1587-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-7551-F | Duplicate source record | Business owner notified |
| NOISE-9257-D | Data quality insufficient | Business owner notified |
| NOISE-2292-H | Data quality insufficient | Manual review scheduled |
| NOISE-4388-C | Missing required attributes | Business owner notified |
| NOISE-5394-F | Pending validation | Escalated to data steward |
| NOISE-3956-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1748-C | Data quality insufficient | Escalated to data steward |
| NOISE-7398-A | Duplicate source record | Manual review scheduled |
| NOISE-4835-A | Pending validation | Deferred to Phase 2 |
| NOISE-4537-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1729-D | Pending validation | Manual review scheduled |
| NOISE-3509-C | Data quality insufficient | Escalated to data steward |
| NOISE-9225-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9667-A | Out of scope per business decision | Business owner notified |
| NOISE-8827-H | Missing required attributes | Business owner notified |
| NOISE-5267-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7511-F | Duplicate source record | Escalated to data steward |
| NOISE-9463-D | Out of scope per business decision | Manual review scheduled |
| NOISE-7670-C | Pending validation | Business owner notified |
| NOISE-7342-A | Out of scope per business decision | Escalated to data steward |
| NOISE-8726-C | Pending validation | Business owner notified |
| NOISE-3722-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-1315-D | Pending validation | Deferred to Phase 2 |
| NOISE-9484-H | Duplicate source record | Manual review scheduled |
| NOISE-8498-B | Data quality insufficient | Business owner notified |
| NOISE-1588-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9684-C | Pending validation | Manual review scheduled |
| NOISE-3213-F | Data quality insufficient | Business owner notified |
| NOISE-5852-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-4354-F | Out of scope per business decision | Business owner notified |
| NOISE-9355-G | Missing required attributes | Manual review scheduled |
| NOISE-2156-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-4819-C | Pending validation | Manual review scheduled |
| NOISE-7801-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-7333-C | Pending validation | Business owner notified |
| NOISE-7216-F | Data quality insufficient | Manual review scheduled |
| NOISE-6497-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3904-H | Pending validation | Business owner notified |
| NOISE-3574-B | Missing required attributes | Escalated to data steward |
| NOISE-9663-D | Data quality insufficient | Business owner notified |
| NOISE-3066-E | Data quality insufficient | Manual review scheduled |
| NOISE-2244-D | Out of scope per business decision | Escalated to data steward |
| NOISE-4784-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-1670-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9306-E | Duplicate source record | Escalated to data steward |
| NOISE-4952-B | Missing required attributes | Manual review scheduled |
| NOISE-8758-H | Duplicate source record | Business owner notified |
| NOISE-5416-F | Duplicate source record | Manual review scheduled |
| NOISE-2286-H | Data quality insufficient | Escalated to data steward |
| NOISE-2114-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9162-C | Pending validation | Deferred to Phase 2 |
| NOISE-6748-G | Missing required attributes | Business owner notified |
| NOISE-7516-A | Missing required attributes | Manual review scheduled |
| NOISE-8463-A | Duplicate source record | Manual review scheduled |
| NOISE-8251-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-9785-F | Data quality insufficient | Manual review scheduled |
| NOISE-4875-C | Data quality insufficient | Manual review scheduled |
| NOISE-5921-C | Duplicate source record | Manual review scheduled |
| NOISE-5680-E | Data quality insufficient | Manual review scheduled |
| NOISE-1021-C | Data quality insufficient | Escalated to data steward |
| NOISE-6350-C | Pending validation | Manual review scheduled |
| NOISE-7656-B | Data quality insufficient | Manual review scheduled |
| NOISE-9580-G | Duplicate source record | Business owner notified |
| NOISE-4122-B | Missing required attributes | Escalated to data steward |
| NOISE-8899-F | Pending validation | Business owner notified |
| NOISE-8039-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-3344-F | Out of scope per business decision | Manual review scheduled |
| NOISE-5476-E | Duplicate source record | Business owner notified |
| NOISE-5985-B | Missing required attributes | Escalated to data steward |
| NOISE-8363-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-1212-B | Missing required attributes | Manual review scheduled |
| NOISE-1973-B | Out of scope per business decision | Business owner notified |
| NOISE-6610-A | Duplicate source record | Business owner notified |
| NOISE-8883-E | Pending validation | Manual review scheduled |
| NOISE-6931-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-5943-A | Out of scope per business decision | Escalated to data steward |
| NOISE-6875-F | Pending validation | Escalated to data steward |
| NOISE-3428-C | Pending validation | Business owner notified |
| NOISE-1893-E | Data quality insufficient | Manual review scheduled |
| NOISE-9761-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1895-E | Missing required attributes | Business owner notified |
| NOISE-8892-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1546-G | Out of scope per business decision | Business owner notified |
| NOISE-7525-F | Data quality insufficient | Manual review scheduled |
| NOISE-6024-F | Data quality insufficient | Escalated to data steward |
| NOISE-5415-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-1296-E | Out of scope per business decision | Escalated to data steward |
| NOISE-9715-B | Missing required attributes | Business owner notified |
| NOISE-6367-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-2992-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8004-G | Pending validation | Escalated to data steward |
| NOISE-6982-C | Data quality insufficient | Business owner notified |
| NOISE-8399-E | Out of scope per business decision | Escalated to data steward |
| NOISE-5120-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8185-F | Missing required attributes | Manual review scheduled |
| NOISE-3784-A | Missing required attributes | Escalated to data steward |
| NOISE-6450-G | Missing required attributes | Escalated to data steward |
| NOISE-2951-B | Duplicate source record | Business owner notified |
| NOISE-9572-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6644-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-8626-F | Duplicate source record | Manual review scheduled |
| NOISE-7339-F | Pending validation | Deferred to Phase 2 |
| NOISE-5705-D | Missing required attributes | Manual review scheduled |
| NOISE-4719-F | Pending validation | Manual review scheduled |
| NOISE-2538-H | Data quality insufficient | Escalated to data steward |
| NOISE-3606-B | Missing required attributes | Manual review scheduled |
| NOISE-6743-F | Pending validation | Manual review scheduled |
| NOISE-3029-C | Missing required attributes | Escalated to data steward |
| NOISE-9816-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6330-G | Missing required attributes | Manual review scheduled |
| NOISE-6041-G | Data quality insufficient | Escalated to data steward |
| NOISE-2307-D | Duplicate source record | Business owner notified |
| NOISE-7153-E | Missing required attributes | Business owner notified |
| NOISE-2805-E | Pending validation | Manual review scheduled |
| NOISE-9380-F | Data quality insufficient | Manual review scheduled |
| NOISE-9899-H | Data quality insufficient | Escalated to data steward |
| NOISE-6945-H | Pending validation | Deferred to Phase 2 |
| NOISE-4286-B | Pending validation | Escalated to data steward |
| NOISE-5713-D | Data quality insufficient | Manual review scheduled |
| NOISE-7367-G | Duplicate source record | Manual review scheduled |
| NOISE-9452-F | Data quality insufficient | Manual review scheduled |
| NOISE-3087-C | Pending validation | Escalated to data steward |
| NOISE-8628-F | Data quality insufficient | Manual review scheduled |
| NOISE-3226-A | Duplicate source record | Escalated to data steward |
| NOISE-6079-B | Out of scope per business decision | Escalated to data steward |
| NOISE-5581-D | Out of scope per business decision | Escalated to data steward |
| NOISE-3088-B | Missing required attributes | Manual review scheduled |
| NOISE-4853-C | Out of scope per business decision | Manual review scheduled |
| NOISE-3149-F | Duplicate source record | Business owner notified |
| NOISE-4996-F | Duplicate source record | Escalated to data steward |
| NOISE-7759-F | Data quality insufficient | Escalated to data steward |
| NOISE-3713-D | Out of scope per business decision | Business owner notified |
| NOISE-4362-H | Data quality insufficient | Manual review scheduled |
| NOISE-6187-G | Missing required attributes | Business owner notified |
| NOISE-6615-F | Data quality insufficient | Business owner notified |
| NOISE-8795-D | Pending validation | Deferred to Phase 2 |
| NOISE-8365-A | Data quality insufficient | Manual review scheduled |
| NOISE-3907-A | Duplicate source record | Escalated to data steward |
| NOISE-7301-A | Out of scope per business decision | Business owner notified |
| NOISE-6633-C | Out of scope per business decision | Business owner notified |
| NOISE-2036-F | Data quality insufficient | Business owner notified |
| NOISE-6012-C | Data quality insufficient | Escalated to data steward |
| NOISE-2722-F | Data quality insufficient | Business owner notified |
| NOISE-5185-D | Pending validation | Deferred to Phase 2 |
| NOISE-4427-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6661-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8469-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1247-D | Data quality insufficient | Business owner notified |
| NOISE-2652-A | Pending validation | Deferred to Phase 2 |
| NOISE-5902-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-9302-H | Missing required attributes | Business owner notified |
| NOISE-9919-G | Data quality insufficient | Manual review scheduled |
| NOISE-6207-C | Missing required attributes | Manual review scheduled |
| NOISE-4132-E | Missing required attributes | Escalated to data steward |
| NOISE-5066-D | Data quality insufficient | Manual review scheduled |
| NOISE-4371-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4689-C | Data quality insufficient | Escalated to data steward |
| NOISE-9445-F | Pending validation | Business owner notified |
| NOISE-6307-E | Out of scope per business decision | Manual review scheduled |
| NOISE-7203-E | Pending validation | Deferred to Phase 2 |
| NOISE-9602-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6911-A | Missing required attributes | Business owner notified |
| NOISE-8833-C | Missing required attributes | Escalated to data steward |
| NOISE-1166-B | Data quality insufficient | Escalated to data steward |
| NOISE-2192-G | Duplicate source record | Business owner notified |
| NOISE-7785-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-5160-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7961-C | Pending validation | Manual review scheduled |
| NOISE-7403-G | Out of scope per business decision | Escalated to data steward |
| NOISE-7607-F | Out of scope per business decision | Manual review scheduled |
| NOISE-7040-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9011-D | Data quality insufficient | Manual review scheduled |
| NOISE-8767-A | Data quality insufficient | Escalated to data steward |
| NOISE-5051-F | Data quality insufficient | Escalated to data steward |
| NOISE-7549-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5642-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-7870-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-4688-G | Pending validation | Deferred to Phase 2 |
| NOISE-7574-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1937-E | Out of scope per business decision | Manual review scheduled |
| NOISE-5927-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8461-D | Missing required attributes | Escalated to data steward |
| NOISE-6917-D | Data quality insufficient | Business owner notified |
| NOISE-9318-H | Out of scope per business decision | Escalated to data steward |
| NOISE-6998-C | Out of scope per business decision | Manual review scheduled |
| NOISE-9406-A | Data quality insufficient | Business owner notified |
| NOISE-3992-B | Duplicate source record | Manual review scheduled |
| NOISE-7725-E | Out of scope per business decision | Manual review scheduled |
| NOISE-7971-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8940-D | Duplicate source record | Business owner notified |
| NOISE-7976-A | Out of scope per business decision | Manual review scheduled |
| NOISE-1707-F | Pending validation | Manual review scheduled |
| NOISE-8335-E | Data quality insufficient | Business owner notified |
| NOISE-3987-H | Data quality insufficient | Business owner notified |
| NOISE-3470-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3136-B | Out of scope per business decision | Manual review scheduled |
| NOISE-6115-A | Missing required attributes | Business owner notified |
| NOISE-2437-E | Out of scope per business decision | Business owner notified |
| NOISE-7234-E | Missing required attributes | Manual review scheduled |
| NOISE-1920-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-3495-D | Data quality insufficient | Business owner notified |
| NOISE-5129-C | Missing required attributes | Business owner notified |
| NOISE-8707-H | Missing required attributes | Escalated to data steward |
| NOISE-7852-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-7297-H | Data quality insufficient | Business owner notified |
| NOISE-2574-G | Missing required attributes | Manual review scheduled |
| NOISE-7650-D | Missing required attributes | Business owner notified |
| NOISE-5743-G | Out of scope per business decision | Escalated to data steward |
| NOISE-5614-G | Missing required attributes | Escalated to data steward |
| NOISE-7885-A | Missing required attributes | Manual review scheduled |
| NOISE-4405-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1267-A | Data quality insufficient | Manual review scheduled |
| NOISE-3530-B | Out of scope per business decision | Business owner notified |
| NOISE-3596-H | Pending validation | Business owner notified |
| NOISE-9389-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9565-D | Out of scope per business decision | Manual review scheduled |
| NOISE-6675-H | Missing required attributes | Manual review scheduled |
| NOISE-8807-B | Duplicate source record | Escalated to data steward |
| NOISE-7700-H | Out of scope per business decision | Business owner notified |
| NOISE-2381-E | Pending validation | Deferred to Phase 2 |
| NOISE-7109-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-7645-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-1271-E | Data quality insufficient | Manual review scheduled |
| NOISE-3885-G | Missing required attributes | Manual review scheduled |
| NOISE-7820-D | Duplicate source record | Business owner notified |
| NOISE-3211-D | Missing required attributes | Escalated to data steward |
| NOISE-8438-D | Duplicate source record | Escalated to data steward |
| NOISE-4555-E | Out of scope per business decision | Escalated to data steward |
| NOISE-3675-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6582-F | Pending validation | Manual review scheduled |
| NOISE-3474-H | Out of scope per business decision | Manual review scheduled |
| NOISE-1217-D | Missing required attributes | Business owner notified |
| NOISE-4313-C | Data quality insufficient | Manual review scheduled |
| NOISE-9063-A | Pending validation | Manual review scheduled |
| NOISE-3167-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7515-B | Pending validation | Escalated to data steward |
| NOISE-4528-F | Pending validation | Manual review scheduled |
| NOISE-2133-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3718-A | Out of scope per business decision | Manual review scheduled |
| NOISE-1957-H | Data quality insufficient | Escalated to data steward |
| NOISE-5869-C | Out of scope per business decision | Manual review scheduled |
| NOISE-2624-H | Missing required attributes | Manual review scheduled |
| NOISE-4302-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-2827-A | Data quality insufficient | Escalated to data steward |
| NOISE-7274-B | Pending validation | Escalated to data steward |
| NOISE-3881-E | Out of scope per business decision | Business owner notified |
| NOISE-1389-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-5614-F | Data quality insufficient | Manual review scheduled |
| NOISE-1877-B | Missing required attributes | Manual review scheduled |
| NOISE-8766-F | Data quality insufficient | Business owner notified |
| NOISE-2369-G | Out of scope per business decision | Business owner notified |
| NOISE-5507-F | Duplicate source record | Manual review scheduled |
| NOISE-7186-G | Missing required attributes | Business owner notified |
| NOISE-5927-D | Pending validation | Deferred to Phase 2 |
| NOISE-1147-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-7641-G | Pending validation | Deferred to Phase 2 |
| NOISE-9064-D | Pending validation | Deferred to Phase 2 |
| NOISE-4873-B | Pending validation | Deferred to Phase 2 |
| NOISE-9249-G | Duplicate source record | Manual review scheduled |
| NOISE-1958-D | Duplicate source record | Business owner notified |
| NOISE-2584-E | Pending validation | Manual review scheduled |
| NOISE-1524-E | Pending validation | Deferred to Phase 2 |
| NOISE-1721-G | Missing required attributes | Escalated to data steward |
| NOISE-2085-E | Out of scope per business decision | Manual review scheduled |


#### 4.3.5 Next Steps

After internal code assignment, entities proceed to:
1. **Master Data Registry** - For target system code assignment
2. **Data Quality Validation** - Automated checks before load
3. **Target Load Process** - Separate runbook (see MDM-LOAD-PROC)

For target entity mappings, consult:
- MDM Consolidation Spreadsheets (shared drive)
- Data Governance Wiki (internal codes to targets)
- Master Data Registry API


## Appendix A: Rollback Procedures

### Scenario 1: Critical Data Corruption

If critical data corruption is detected within 4 hours of migration:

1. Notify incident commander immediately
2. Stop all write operations to target system
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230718_000000`
4. Restore source system from pre-migration backup
5. Communicate status to stakeholders via emergency channel

### Scenario 2: Partial Migration Failure

If specific entity types fail to migrate:

1. Identify failed entity types from migration logs
2. Execute selective rollback: `./scripts/rollback_selective.sh --entity-type=ENTITY_TYPE`
3. Analyze root cause before retry
4. Document issues in post-mortem

### Recovery Time Objectives

| Scenario | RTO | RPO |
|----------|-----|-----|
| Full rollback | 4 hours | 0 data loss |
| Partial rollback | 2 hours | 0 data loss |
| Data correction | 8 hours | Minimal impact |

## Appendix B: Support Contacts

### Primary Contacts

| Role | Name | Email | Phone |
|------|------|-------|-------|
| Project Lead | Sarah Chen (Data Governance) | sarah@company.com | +1-555-0101 |
| Technical Lead | Maria Garcia (Supply Chain) | maria@company.com | +1-555-0102 |
| Business Owner | Lisa Rodriguez (Quality Assurance) | lisa@company.com | +1-555-0103 |
| Data Steward | James Wilson (Finance) | james@company.com | +1-555-0104 |

### Escalation Matrix

| Level | Response Time | Contact |
|-------|---------------|---------|
| L1 | 15 minutes | On-call engineer |
| L2 | 30 minutes | Technical Lead |
| L3 | 1 hour | Project Sponsor |
| L4 | 2 hours | CIO Office |

### External Vendors

- Cloud Infrastructure: AWS Support (Enterprise)
- ERP Vendor: SAP Premium Support
- Database: Oracle Platinum Support

## Appendix C: Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2023-01-15 | J. Smith | Initial draft |
| 1.1 | 2023-02-01 | S. Chen | Added internal code section |
| 1.2 | 2023-02-15 | M. Weber | Updated stakeholder list |
| 2.0 | 2023-03-01 | J. Smith | Major revision for Phase 2 |
| 2.1 | 2023-03-15 | L. Rodriguez | QA review comments addressed |
| 2.2 | 2023-04-01 | D. Kim | Final sign-off version |

### Approval Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Project Sponsor | VP Operations | 2023-04-01 | [Approved] |
| IT Director | CTO Office | 2023-04-01 | [Approved] |
| Business Owner | Division Lead | 2023-04-01 | [Approved] |
| QA Lead | Testing Team | 2023-04-01 | [Approved] |

---

*This document is maintained by the Data Governance team. For questions or updates,
contact data-governance@company.com or submit a ticket via ServiceNow.*

*Generated by Migration Management System v3.2.1*

**NOTE**: Target system assignments are managed separately. For target mappings,
consult the MDM Registry or contact Master Data Management team.
