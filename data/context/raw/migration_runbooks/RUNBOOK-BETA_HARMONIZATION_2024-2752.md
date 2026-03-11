# Migration Runbook: European Subsidiary Harmonization

**Document ID**: RB-BETA_HARMONIZATION_2024-1353
**Version**: 2.0
**Last Updated**: 2023-06-10
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the European Subsidiary Harmonization project.
The migration involves transitioning master data and transactional records from ERP_BETA
to ERP_ALPHA while maintaining data integrity and business continuity.

**Project Timeline**: 2023-03-11 to 2023-08-01
**Business Sponsor**: Group Finance
**Technical Owner**: EU Operations

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
|   ERP_BETA       |     |   Staging Layer  |     |   ERP_ALPHA       |
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
ERP_BETA. Each source entity is assigned an internal staging code for
tracking purposes.

**IMPORTANT**: This document only contains source-to-staging assignments.
Target system mappings are maintained separately in the MDM Registry.

### 4.2 Assignment Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1384 | Completed |
| Codes assigned | 932 | Staged |
| Excluded from scope | 279 | Documented |
| Pending review | 2 | In Progress |

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

| Source Entity (ERP_BETA) | Internal Code | Assignment Date | Department |
|--------------------------------|---------------|-----------------|------------|
| Resistente Stärke | BC-1013 | 2022-01-24 | Data Governance |
| Kasein 25% Pharmazeutisch rein | IC-1019 | 2022-01-28 | Operations |
| Ascorbic Acid | TC-1027 | 2024-01-17 | Data Governance |
| Sonnenblumenöl 98% Premiumqualität | BC-1039 | 2024-05-06 | Compliance |
| Pea Protein 99.5% | TC-1050 | 2024-07-08 | IT Infrastructure |
| Lactic Acid | TC-1062 | 2022-03-16 | Operations |
| Ascorbic Acid Standardqualität | BC-1067 | 2024-07-06 | Product Management |
| Zitronensäure 70% | TC-1071 | 2024-09-25 | Compliance |
| Ascorbic Acid Pharmazeutisch rein | IC-1077 | 2021-08-16 | Supply Chain |
| Coconut Oil Lebensmittelrein | IC-1084 | 2022-10-24 | Product Management |
| Palmfett 98% | TC-1089 | 2024-08-03 | Compliance |
| Traubenzucker Lebensmittelrein | BC-1103 | 2023-07-05 | IT Infrastructure |
| Weizenklebereiweiß 98% Premiumqualität | IC-1107 | 2024-10-10 | Product Management |
| Natriumbenzoat 25% Standardqualität | TC-1115 | 2023-11-03 | Product Management |
| Coconut Oil 98% | TC-1128 | 2022-08-08 | Product Management |
| Natriumbenzoat 99.5% Qualitätsstufe I | BC-1134 | 2021-05-23 | Data Governance |
| Cyclodextrin 98% Pharmazeutisch rein | IC-1147 | 2022-03-25 | Compliance |
| Coconut Oil Qualitätsstufe I | TC-1155 | 2022-02-19 | Operations |
| Traubenzucker Standardqualität | BC-1165 | 2021-01-13 | Data Governance |
| Lactic Acid 99.5% Qualitätsstufe II | BC-1172 | 2021-04-24 | Data Governance |
| Coconut Oil 99.5% Pharmazeutisch rein | IC-1183 | 2022-07-11 | Data Governance |
| Kaliumsorbat | BC-1188 | 2023-09-05 | Product Management |
| Natriumbenzoat 99.5% | IC-1197 | 2023-06-28 | IT Infrastructure |
| Weizenklebereiweiß | IC-1201 | 2023-01-10 | Data Governance |
| Natriumbenzoat Pharmazeutisch rein | IC-1210 | 2024-07-17 | IT Infrastructure |
| Soja Isolate 70% | IC-1228 | 2022-08-05 | Finance |
| Soja Isolate 25% Technische Qualität | TC-1236 | 2022-02-06 | IT Infrastructure |
| Calcium Carbonate 25% | IC-1241 | 2022-04-27 | Supply Chain |
| Fructose | BC-1246 | 2021-01-09 | Compliance |
| Rapsöl | TC-1253 | 2024-03-24 | Operations |
| Resistente Stärke | TC-1260 | 2024-11-01 | Compliance |
| Fructose | BC-1266 | 2024-11-19 | Supply Chain |
| Glukosesirup Syrup | BC-1271 | 2023-08-05 | Product Management |
| Resistente Stärke Pharmazeutisch rein | TC-1280 | 2021-04-22 | Finance |
| Kasein Standardqualität | BC-1286 | 2024-04-26 | Operations |
| Calcium Carbonate 98% | BC-1297 | 2021-05-28 | Compliance |
| Palmfett Standardqualität | IC-1304 | 2024-07-27 | Compliance |
| Maltodextrin-Pulver DE5 Qualitätsstufe I | IC-1310 | 2023-07-23 | Product Management |
| Rapsöl 70% Qualitätsstufe II | TC-1315 | 2023-11-10 | Operations |
| Sorbinsäure Lebensmittelrein | TC-1319 | 2022-02-10 | Supply Chain |
| Ascorbic Acid | TC-1331 | 2023-06-01 | IT Infrastructure |
| Coconut Oil 25% Standardqualität | IC-1336 | 2022-03-15 | Finance |
| Zitronensäure Pharmazeutisch rein | BC-1349 | 2023-03-08 | Data Governance |
| Sonnenblumenöl 50% Qualitätsstufe I | BC-1370 | 2022-07-27 | IT Infrastructure |
| Sorbinsäure 98% | IC-1381 | 2022-05-23 | Finance |
| Zitronensäure 50% Qualitätsstufe I | TC-1394 | 2022-11-03 | Compliance |
| Dextrin | IC-1397 | 2022-06-14 | Compliance |
| Maltodextrin-Pulver DE20 | BC-1404 | 2023-03-26 | Operations |
| Natriumbenzoat | TC-1409 | 2021-02-26 | IT Infrastructure |
| Traubenzucker 25% Technische Qualität | TC-1415 | 2021-06-06 | Supply Chain |
| Lactic Acid Lebensmittelrein | BC-1421 | 2022-08-11 | Finance |
| Sorbinsäure | BC-1427 | 2023-01-06 | Supply Chain |
| Rapsöl Technische Qualität | BC-1432 | 2024-10-23 | Supply Chain |
| Dextrin Pharmazeutisch rein | TC-1440 | 2024-11-23 | IT Infrastructure |
| Zitronensäure 99.5% | TC-1446 | 2024-02-22 | Finance |
| Traubenzucker 25% | TC-1454 | 2021-11-10 | Product Management |
| Traubenzucker | BC-1459 | 2022-03-22 | Finance |
| Resistente Stärke Qualitätsstufe II | BC-1480 | 2021-07-13 | Finance |
| Fructose 25% | IC-1486 | 2023-06-04 | Compliance |
| Calcium Carbonate 50% Qualitätsstufe II | IC-1492 | 2024-10-21 | Operations |
| Soja Isolate 25% | IC-1497 | 2023-02-26 | Product Management |
| Zitronensäure Qualitätsstufe II | BC-1504 | 2023-10-28 | Supply Chain |
| Pea Protein Qualitätsstufe I | BC-1509 | 2023-07-09 | Operations |
| Rapsöl 99.5% | BC-1517 | 2023-12-09 | Compliance |
| Glukosesirup Syrup 98% Lebensmittelrein | TC-1525 | 2022-05-16 | Supply Chain |
| Traubenzucker 99.5% Qualitätsstufe II | IC-1527 | 2024-04-09 | Compliance |
| Soja Isolate 25% Pharmazeutisch rein | BC-1532 | 2023-12-26 | Data Governance |
| Soja Isolate | TC-1534 | 2022-08-08 | Operations |
| Traubenzucker Qualitätsstufe I | IC-1539 | 2024-11-20 | Operations |
| Resistente Stärke Technische Qualität | IC-1550 | 2022-02-24 | Finance |
| Dextrin 50% | IC-1557 | 2022-06-19 | Data Governance |
| Glukosesirup Syrup Technische Qualität | IC-1568 | 2022-03-25 | Data Governance |
| Soja Isolate 99.5% Premiumqualität | TC-1577 | 2023-01-18 | Product Management |
| Soja Isolate 98% | TC-1594 | 2022-09-13 | Compliance |
| Dextrin | TC-1603 | 2022-02-19 | Operations |
| Glukosesirup Syrup 70% | TC-1616 | 2023-03-25 | Operations |
| Sonnenblumenöl Qualitätsstufe II | IC-1619 | 2023-04-10 | Data Governance |
| Sonnenblumenöl Standardqualität | IC-1628 | 2023-05-18 | Finance |
| Ascorbic Acid 99.5% Premiumqualität | TC-1641 | 2021-12-08 | Finance |
| Dextrin Technische Qualität | TC-1646 | 2023-01-21 | Supply Chain |
| Palmfett | IC-1652 | 2021-08-13 | Compliance |
| Natriumbenzoat Qualitätsstufe I | BC-1664 | 2021-03-21 | Product Management |
| Traubenzucker 25% | TC-1669 | 2024-11-23 | Product Management |
| Kaliumsorbat | IC-1673 | 2021-08-21 | Operations |
| Natriumbenzoat | IC-1682 | 2022-09-04 | Compliance |
| Natriumbenzoat 25% | IC-1691 | 2023-11-20 | Compliance |
| Natriumchlorid 70% | TC-1696 | 2023-12-15 | Compliance |
| Kasein Premiumqualität | IC-1700 | 2021-03-11 | Compliance |
| Calcium Carbonate Standardqualität | BC-1704 | 2021-08-05 | Product Management |
| Natriumchlorid 99.5% | BC-1710 | 2022-05-12 | Supply Chain |
| Ascorbic Acid Technische Qualität | TC-1716 | 2024-08-11 | IT Infrastructure |
| Natriumchlorid | IC-1730 | 2023-01-05 | Product Management |
| Dextrin Standardqualität | IC-1734 | 2022-12-05 | IT Infrastructure |
| Kasein | TC-1736 | 2021-02-09 | Data Governance |
| Isoglucose 70% | IC-1758 | 2023-08-22 | Data Governance |
| Ascorbic Acid 50% Technische Qualität | TC-1763 | 2024-04-12 | Compliance |
| Traubenzucker Lebensmittelrein | IC-1769 | 2023-08-18 | IT Infrastructure |
| Natriumbenzoat | IC-1774 | 2022-08-14 | Supply Chain |
| Palmfett 50% | IC-1782 | 2021-04-21 | IT Infrastructure |
| Ascorbic Acid 98% Premiumqualität | TC-1787 | 2021-12-17 | IT Infrastructure |
| Sorbinsäure 70% | IC-1792 | 2023-08-12 | Finance |
| Dextrin Lebensmittelrein | BC-1796 | 2023-03-11 | Compliance |
| Natriumchlorid Standardqualität | TC-1803 | 2024-11-09 | Operations |
| Isoglucose Premiumqualität | TC-1809 | 2024-07-26 | Product Management |
| Calcium Carbonate Qualitätsstufe II | BC-1822 | 2021-01-04 | Operations |
| Kaliumsorbat | IC-1831 | 2022-05-11 | Supply Chain |
| Weizenklebereiweiß | IC-1837 | 2024-07-15 | IT Infrastructure |
| Zitronensäure | IC-1845 | 2024-10-24 | Compliance |
| Ascorbic Acid 70% | IC-1851 | 2023-10-28 | Finance |
| Cyclodextrin | BC-1859 | 2021-11-18 | IT Infrastructure |
| Traubenzucker 25% Technische Qualität | BC-1870 | 2024-11-07 | Operations |
| Isoglucose Lebensmittelrein | BC-1876 | 2022-02-15 | IT Infrastructure |
| Dextrin 70% | BC-1884 | 2021-04-11 | Product Management |
| Zitronensäure | TC-1897 | 2022-06-07 | Operations |
| Natriumbenzoat 98% Standardqualität | BC-1904 | 2023-09-26 | IT Infrastructure |
| Lactic Acid 98% Premiumqualität | IC-1910 | 2022-04-15 | Supply Chain |
| Ascorbic Acid Premiumqualität | BC-1915 | 2021-06-07 | Operations |
| Rapsöl Technische Qualität | BC-1931 | 2023-07-20 | IT Infrastructure |
| Soja Isolate Qualitätsstufe I | IC-1945 | 2021-11-11 | IT Infrastructure |
| Rapsöl | TC-1955 | 2022-09-03 | Operations |
| Calcium Carbonate | BC-1959 | 2022-05-13 | Product Management |
| Natriumbenzoat 99.5% Technische Qualität | TC-1965 | 2022-04-20 | Compliance |
| Natriumbenzoat Qualitätsstufe II | IC-1974 | 2021-04-17 | Finance |
| Palmfett | TC-1979 | 2023-04-20 | Product Management |
| Calcium Carbonate 70% Premiumqualität | BC-1988 | 2023-05-27 | Finance |
| Soja Isolate Premiumqualität | IC-2000 | 2024-01-19 | Operations |
| Palmfett Lebensmittelrein | IC-2002 | 2022-12-01 | Compliance |
| Weizenklebereiweiß Qualitätsstufe II | IC-2008 | 2022-05-28 | Finance |
| Kasein Technische Qualität | BC-2012 | 2024-10-08 | Data Governance |
| Glukosesirup Syrup 98% | TC-2018 | 2022-12-15 | Finance |
| Rapsöl 70% Premiumqualität | TC-2029 | 2022-06-01 | Data Governance |
| Palmfett | BC-2042 | 2021-06-09 | Data Governance |
| Zitronensäure | IC-2070 | 2024-11-22 | Supply Chain |
| Lactic Acid 70% Pharmazeutisch rein | BC-2077 | 2023-05-15 | Compliance |
| Kaliumsorbat Qualitätsstufe I | BC-2083 | 2023-12-08 | Finance |
| Natriumchlorid | TC-2091 | 2021-01-19 | Compliance |
| Fructose | BC-2098 | 2023-07-28 | Finance |
| Natriumbenzoat Qualitätsstufe I | BC-2112 | 2023-08-27 | Finance |
| Fructose Qualitätsstufe II | TC-2118 | 2024-08-24 | Finance |
| Ascorbic Acid | BC-2127 | 2023-04-21 | Compliance |
| Fructose | BC-2136 | 2024-09-13 | Operations |
| Glukosesirup Syrup 98% Qualitätsstufe I | TC-2143 | 2022-02-18 | Compliance |
| Rapsöl 98% | BC-2148 | 2021-08-20 | Product Management |
| Kasein | TC-2153 | 2022-11-16 | Data Governance |
| Rapsöl Qualitätsstufe I | BC-2166 | 2021-03-17 | IT Infrastructure |
| Pea Protein 98% Qualitätsstufe II | BC-2175 | 2024-05-10 | Data Governance |
| Calcium Carbonate | BC-2179 | 2022-05-26 | Supply Chain |
| Glukosesirup Syrup 70% | TC-2186 | 2023-07-05 | Product Management |
| Traubenzucker Qualitätsstufe I | TC-2193 | 2021-03-21 | Operations |
| Lactic Acid | BC-2203 | 2021-10-09 | Compliance |
| Kaliumsorbat | TC-2214 | 2023-04-16 | Product Management |
| Lactic Acid Technische Qualität | BC-2218 | 2022-08-04 | Supply Chain |
| Isoglucose 70% Lebensmittelrein | IC-2226 | 2022-11-25 | Compliance |
| Traubenzucker 25% | BC-2235 | 2022-08-01 | Supply Chain |
| Traubenzucker Qualitätsstufe II | TC-2241 | 2024-11-14 | Finance |
| Sorbinsäure Qualitätsstufe II | IC-2244 | 2022-11-03 | Operations |
| Resistente Stärke Qualitätsstufe II | TC-2252 | 2021-01-27 | IT Infrastructure |
| Lactic Acid Qualitätsstufe I | IC-2261 | 2021-09-18 | Compliance |
| Dextrin Qualitätsstufe I | TC-2269 | 2023-11-19 | Operations |
| Natriumchlorid 98% | TC-2277 | 2021-02-25 | Data Governance |
| Natriumchlorid | TC-2281 | 2022-05-24 | Compliance |
| Pea Protein 25% Pharmazeutisch rein | BC-2286 | 2022-01-16 | Operations |
| Maltodextrin-Pulver DE10 Premiumqualität | IC-2298 | 2022-09-15 | Product Management |
| Maltodextrin-Pulver DE20 | TC-2303 | 2023-04-06 | Compliance |
| Fructose Qualitätsstufe I | TC-2308 | 2021-11-12 | Compliance |
| Glukosesirup Syrup | IC-2317 | 2022-01-09 | Operations |
| Isoglucose | BC-2329 | 2021-06-10 | Product Management |
| Soja Isolate | IC-2334 | 2022-03-10 | Compliance |
| Calcium Carbonate 98% Standardqualität | IC-2335 | 2022-11-18 | IT Infrastructure |
| Resistente Stärke | BC-2338 | 2024-04-20 | Supply Chain |
| Kaliumsorbat Standardqualität | TC-2345 | 2023-03-14 | Data Governance |
| Zitronensäure | IC-2350 | 2022-07-09 | Compliance |
| Lactic Acid Lebensmittelrein | BC-2356 | 2022-05-15 | IT Infrastructure |
| Zitronensäure 25% Technische Qualität | IC-2362 | 2023-04-13 | Compliance |
| Dextrin 50% | IC-2368 | 2022-10-19 | Finance |
| Isoglucose | TC-2374 | 2021-08-27 | Compliance |
| Soja Isolate 50% Qualitätsstufe II | BC-2383 | 2022-09-12 | Product Management |
| Rapsöl | IC-2392 | 2022-05-19 | Product Management |
| Maltodextrin-Pulver DE18 Pharmazeutisch rein | IC-2407 | 2023-03-28 | Data Governance |
| Rapsöl Qualitätsstufe I | BC-2417 | 2024-10-12 | IT Infrastructure |
| Traubenzucker 70% Qualitätsstufe I | IC-2422 | 2021-09-19 | Data Governance |
| Calcium Carbonate 50% Pharmazeutisch rein | IC-2429 | 2024-05-13 | Supply Chain |
| Natriumbenzoat 25% Qualitätsstufe II | TC-2439 | 2024-04-15 | Operations |
| Rapsöl 99.5% Technische Qualität | IC-2443 | 2022-09-07 | Operations |
| Kaliumsorbat 98% Qualitätsstufe II | BC-2447 | 2023-12-10 | Finance |
| Natriumbenzoat 50% | BC-2451 | 2023-11-04 | Finance |
| Coconut Oil | BC-2457 | 2022-04-19 | Product Management |
| Fructose | IC-2463 | 2022-12-13 | Compliance |
| Sorbinsäure 50% Standardqualität | TC-2467 | 2023-07-20 | Data Governance |
| Rapsöl 99.5% | BC-2470 | 2021-04-27 | Product Management |
| Zitronensäure | BC-2475 | 2021-12-12 | Finance |
| Natriumchlorid Technische Qualität | TC-2482 | 2022-01-21 | Data Governance |
| Kaliumsorbat | TC-2487 | 2021-06-13 | IT Infrastructure |
| Dextrin Premiumqualität | TC-2490 | 2021-05-04 | Product Management |
| Zitronensäure 70% | IC-2498 | 2023-04-12 | Finance |
| Maltodextrin-Pulver DE25 | BC-2505 | 2021-03-22 | Data Governance |
| Maltodextrin-Pulver DE10 | TC-2525 | 2022-09-14 | IT Infrastructure |
| Dextrin 70% | TC-2528 | 2021-02-03 | Compliance |
| Lactic Acid Lebensmittelrein | BC-2539 | 2024-06-18 | Finance |
| Ascorbic Acid 98% Pharmazeutisch rein | BC-2543 | 2021-03-26 | IT Infrastructure |
| Natriumchlorid 70% | IC-2548 | 2024-08-10 | Finance |
| Fructose Technische Qualität | BC-2553 | 2021-06-19 | Supply Chain |
| Ascorbic Acid | BC-2562 | 2022-11-10 | IT Infrastructure |
| Lactic Acid | BC-2569 | 2023-09-05 | Supply Chain |
| Coconut Oil 98% Lebensmittelrein | IC-2579 | 2021-06-11 | Product Management |
| Kaliumsorbat Technische Qualität | BC-2592 | 2024-11-28 | Compliance |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | TC-2614 | 2024-12-20 | IT Infrastructure |
| Soja Isolate 98% Premiumqualität | IC-2622 | 2023-07-04 | Product Management |
| Lactic Acid 99.5% | TC-2631 | 2024-06-02 | Operations |
| Glukosesirup Syrup | BC-2633 | 2022-03-13 | IT Infrastructure |
| Maltodextrin-Pulver DE25 | TC-2643 | 2022-05-07 | Supply Chain |
| Calcium Carbonate Qualitätsstufe II | TC-2652 | 2023-02-24 | Operations |
| Lactic Acid Lebensmittelrein | BC-2655 | 2022-03-03 | Data Governance |
| Kasein 98% Qualitätsstufe II | IC-2661 | 2023-07-09 | Finance |
| Resistente Stärke Technische Qualität | BC-2667 | 2022-07-10 | Finance |
| Resistente Stärke Technische Qualität | BC-2676 | 2024-06-01 | IT Infrastructure |
| Kasein Qualitätsstufe I | TC-2681 | 2024-08-03 | Finance |
| Palmfett Qualitätsstufe II | TC-2685 | 2024-03-05 | Product Management |
| Maltodextrin-Pulver DE25 | BC-2689 | 2023-05-19 | IT Infrastructure |
| Soja Isolate Standardqualität | IC-2696 | 2023-10-11 | Data Governance |
| Natriumbenzoat 50% Technische Qualität | BC-2703 | 2022-11-11 | Operations |
| Traubenzucker 50% | BC-2711 | 2023-01-04 | Supply Chain |
| Resistente Stärke 70% Technische Qualität | IC-2717 | 2023-01-17 | Finance |
| Glukosesirup Syrup Lebensmittelrein | TC-2720 | 2023-11-10 | Product Management |
| Pea Protein Premiumqualität | IC-2725 | 2021-03-11 | Supply Chain |
| Weizenklebereiweiß 98% | IC-2740 | 2022-12-27 | Operations |
| Kaliumsorbat Qualitätsstufe II | IC-2755 | 2022-05-26 | Data Governance |
| Zitronensäure 70% Lebensmittelrein | TC-2761 | 2021-11-18 | IT Infrastructure |
| Natriumchlorid 98% Standardqualität | BC-2763 | 2022-06-08 | Compliance |
| Natriumbenzoat 50% | IC-2780 | 2023-01-02 | Operations |
| Lactic Acid 50% Premiumqualität | IC-2791 | 2021-05-27 | Operations |
| Kasein 98% Technische Qualität | BC-2796 | 2021-01-27 | Supply Chain |
| Sorbinsäure | BC-2801 | 2021-04-07 | Compliance |
| Rapsöl 50% Lebensmittelrein | TC-2805 | 2021-10-25 | Data Governance |
| Resistente Stärke 98% | IC-2812 | 2022-04-15 | Data Governance |
| Fructose 99.5% Lebensmittelrein | TC-2823 | 2021-05-19 | Finance |
| Lactic Acid Standardqualität | TC-2829 | 2022-09-24 | Operations |
| Resistente Stärke Technische Qualität | BC-2834 | 2021-04-26 | Supply Chain |
| Weizenklebereiweiß 99.5% Qualitätsstufe I | TC-2844 | 2023-04-07 | IT Infrastructure |
| Natriumbenzoat 99.5% Technische Qualität | BC-2849 | 2021-07-09 | IT Infrastructure |
| Natriumbenzoat 99.5% Qualitätsstufe I | IC-2859 | 2022-10-05 | Data Governance |
| Maltodextrin-Pulver DE10 | IC-2867 | 2024-11-18 | IT Infrastructure |
| Ascorbic Acid 50% | IC-2872 | 2021-07-06 | Finance |
| Traubenzucker Qualitätsstufe I | IC-2884 | 2023-03-05 | Supply Chain |
| Kaliumsorbat 50% Technische Qualität | TC-2886 | 2023-09-21 | Compliance |
| Coconut Oil 70% Qualitätsstufe I | BC-2892 | 2022-12-08 | Supply Chain |
| Kaliumsorbat 98% | TC-2908 | 2024-03-19 | Data Governance |
| Resistente Stärke 70% Lebensmittelrein | IC-2915 | 2021-11-19 | Supply Chain |
| Ascorbic Acid | BC-2923 | 2021-05-06 | Compliance |
| Glukosesirup Syrup | BC-2935 | 2023-07-27 | Compliance |
| Calcium Carbonate 99.5% | IC-2942 | 2024-02-23 | Product Management |
| Palmfett 70% Premiumqualität | TC-2951 | 2022-04-15 | Product Management |
| Lactic Acid Qualitätsstufe II | BC-2960 | 2022-09-12 | Compliance |
| Lactic Acid 98% | BC-2969 | 2021-09-11 | Supply Chain |
| Kaliumsorbat | IC-2977 | 2024-02-16 | IT Infrastructure |
| Pea Protein Premiumqualität | TC-2990 | 2021-03-08 | Product Management |
| Coconut Oil 98% Technische Qualität | TC-2996 | 2021-08-19 | Product Management |
| Coconut Oil 98% | IC-3009 | 2023-06-28 | Compliance |
| Traubenzucker | BC-3015 | 2024-08-04 | Product Management |
| Natriumchlorid | IC-3019 | 2021-04-06 | Finance |
| Coconut Oil 25% Technische Qualität | TC-3023 | 2022-06-10 | Data Governance |
| Lactic Acid 98% Qualitätsstufe I | TC-3028 | 2023-01-17 | Compliance |
| Calcium Carbonate 70% | BC-3045 | 2021-02-19 | Compliance |
| Palmfett 99.5% Qualitätsstufe I | BC-3050 | 2023-10-09 | Compliance |
| Resistente Stärke 50% | BC-3058 | 2023-02-12 | IT Infrastructure |
| Ascorbic Acid Pharmazeutisch rein | TC-3064 | 2023-01-06 | Supply Chain |
| Resistente Stärke Lebensmittelrein | IC-3072 | 2023-02-02 | Finance |
| Sorbinsäure 70% | BC-3079 | 2021-01-24 | Product Management |
| Natriumbenzoat Lebensmittelrein | TC-3091 | 2022-09-13 | Compliance |
| Weizenklebereiweiß | IC-3097 | 2022-08-12 | Supply Chain |
| Sorbinsäure Standardqualität | TC-3110 | 2023-11-05 | Operations |
| Weizenklebereiweiß Lebensmittelrein | BC-3122 | 2021-11-18 | Product Management |
| Traubenzucker Qualitätsstufe II | BC-3127 | 2023-01-04 | Compliance |
| Pea Protein | BC-3137 | 2022-09-20 | Supply Chain |
| Calcium Carbonate 98% | TC-3145 | 2022-03-24 | IT Infrastructure |
| Kasein Qualitätsstufe II | IC-3154 | 2021-01-26 | Product Management |
| Weizenklebereiweiß Lebensmittelrein | IC-3160 | 2023-02-20 | IT Infrastructure |
| Zitronensäure Premiumqualität | BC-3169 | 2022-12-12 | Supply Chain |
| Natriumchlorid 25% | TC-3174 | 2024-04-19 | Finance |
| Coconut Oil 25% Lebensmittelrein | IC-3177 | 2024-01-23 | Product Management |
| Sonnenblumenöl Qualitätsstufe II | BC-3186 | 2022-07-07 | IT Infrastructure |
| Natriumbenzoat | IC-3198 | 2023-02-26 | Operations |
| Kaliumsorbat Standardqualität | BC-3213 | 2023-05-15 | Finance |
| Traubenzucker Lebensmittelrein | BC-3221 | 2023-11-22 | IT Infrastructure |
| Fructose 99.5% Technische Qualität | IC-3232 | 2024-10-23 | Operations |
| Glukosesirup Syrup 99.5% Qualitätsstufe II | TC-3236 | 2022-06-18 | IT Infrastructure |
| Sorbinsäure 50% Qualitätsstufe I | IC-3239 | 2022-07-24 | Finance |
| Sorbinsäure 50% Lebensmittelrein | TC-3246 | 2024-09-23 | Operations |
| Soja Isolate 99.5% | IC-3250 | 2024-10-10 | Data Governance |
| Rapsöl Qualitätsstufe I | BC-3257 | 2023-04-01 | Product Management |
| Cyclodextrin | IC-3261 | 2023-08-18 | Finance |
| Traubenzucker Standardqualität | IC-3271 | 2021-12-27 | IT Infrastructure |
| Traubenzucker 99.5% | BC-3283 | 2023-06-24 | Finance |
| Palmfett 98% Qualitätsstufe I | BC-3293 | 2023-06-26 | Product Management |
| Natriumbenzoat 50% | IC-3296 | 2023-10-01 | Product Management |
| Traubenzucker 70% | BC-3311 | 2023-06-18 | Data Governance |
| Dextrin 70% Pharmazeutisch rein | IC-3320 | 2024-08-15 | Operations |
| Fructose 99.5% Technische Qualität | TC-3332 | 2021-06-15 | Data Governance |
| Pea Protein 25% | BC-3337 | 2023-07-02 | Compliance |
| Ascorbic Acid Technische Qualität | TC-3345 | 2024-04-15 | Finance |
| Palmfett Qualitätsstufe II | TC-3358 | 2023-04-14 | Data Governance |
| Traubenzucker Technische Qualität | BC-3368 | 2023-05-22 | Data Governance |
| Soja Isolate Lebensmittelrein | BC-3383 | 2023-06-09 | Operations |
| Isoglucose 70% | BC-3390 | 2022-12-24 | IT Infrastructure |
| Maltodextrin-Pulver DE15 | BC-3402 | 2022-04-13 | Finance |
| Resistente Stärke 50% | IC-3406 | 2021-01-07 | Finance |
| Palmfett | BC-3411 | 2022-09-03 | Compliance |
| Maltodextrin-Pulver DE20 | TC-3426 | 2024-07-22 | Finance |
| Calcium Carbonate 98% | BC-3434 | 2021-03-02 | Finance |
| Lactic Acid | BC-3435 | 2023-10-18 | Data Governance |
| Isoglucose | IC-3439 | 2021-04-15 | Data Governance |
| Cyclodextrin 70% Lebensmittelrein | BC-3444 | 2022-03-19 | Operations |
| Ascorbic Acid Lebensmittelrein | BC-3448 | 2024-03-02 | Compliance |
| Dextrin | BC-3466 | 2024-11-05 | Operations |
| Natriumchlorid 25% Lebensmittelrein | IC-3474 | 2022-03-28 | IT Infrastructure |
| Pea Protein 70% Premiumqualität | IC-3482 | 2021-01-17 | Data Governance |
| Natriumchlorid | IC-3494 | 2022-05-25 | Compliance |
| Weizenklebereiweiß 99.5% | BC-3508 | 2024-04-17 | Product Management |
| Glukosesirup Syrup 99.5% Lebensmittelrein | TC-3512 | 2024-07-13 | Product Management |
| Isoglucose Qualitätsstufe II | IC-3526 | 2023-11-21 | Product Management |
| Glukosesirup Syrup 25% | TC-3544 | 2022-09-28 | Supply Chain |
| Sonnenblumenöl Qualitätsstufe I | IC-3547 | 2023-04-10 | Compliance |
| Fructose 70% | BC-3554 | 2022-01-10 | Data Governance |
| Zitronensäure Standardqualität | BC-3560 | 2024-01-15 | Supply Chain |
| Kaliumsorbat | TC-3575 | 2023-09-02 | IT Infrastructure |
| Resistente Stärke Qualitätsstufe I | IC-3583 | 2021-07-08 | IT Infrastructure |
| Pea Protein 99.5% Premiumqualität | BC-3587 | 2022-10-21 | Data Governance |
| Ascorbic Acid Premiumqualität | IC-3593 | 2022-02-26 | Product Management |
| Natriumchlorid 99.5% Qualitätsstufe I | IC-3599 | 2021-12-15 | Product Management |
| Palmfett 70% Technische Qualität | TC-3603 | 2024-12-03 | Compliance |
| Weizenklebereiweiß Qualitätsstufe I | TC-3611 | 2021-06-27 | Operations |
| Dextrin Qualitätsstufe II | BC-3619 | 2024-09-06 | Supply Chain |
| Sonnenblumenöl Technische Qualität | TC-3623 | 2024-10-24 | Compliance |
| Pea Protein | IC-3625 | 2023-02-05 | Compliance |
| Cyclodextrin | IC-3629 | 2022-08-17 | Operations |
| Lactic Acid Technische Qualität | BC-3637 | 2024-09-26 | Operations |
| Maltodextrin-Pulver DE15 | TC-3642 | 2024-03-02 | Finance |
| Kaliumsorbat | BC-3645 | 2023-09-09 | Finance |
| Natriumbenzoat | TC-3657 | 2021-02-26 | Finance |
| Weizenklebereiweiß 70% | BC-3661 | 2023-12-18 | Finance |
| Sonnenblumenöl | TC-3675 | 2022-12-27 | Supply Chain |
| Coconut Oil 25% | TC-3694 | 2024-02-18 | Product Management |
| Kasein Technische Qualität | IC-3705 | 2023-11-09 | IT Infrastructure |
| Sonnenblumenöl 70% Lebensmittelrein | IC-3712 | 2023-02-09 | Product Management |
| Kasein 50% Premiumqualität | IC-3718 | 2021-03-01 | Data Governance |
| Isoglucose Qualitätsstufe II | BC-3725 | 2023-10-15 | Finance |
| Maltodextrin-Pulver DE18 | BC-3726 | 2022-03-24 | Compliance |
| Lactic Acid | TC-3731 | 2023-05-15 | Operations |
| Palmfett Lebensmittelrein | IC-3735 | 2023-04-22 | Operations |
| Weizenklebereiweiß Qualitätsstufe I | IC-3740 | 2024-10-07 | Product Management |
| Rapsöl Pharmazeutisch rein | IC-3743 | 2023-04-13 | Data Governance |
| Resistente Stärke | TC-3751 | 2021-01-28 | Finance |
| Natriumchlorid Technische Qualität | BC-3762 | 2023-02-23 | Supply Chain |
| Kaliumsorbat | TC-3773 | 2021-06-28 | IT Infrastructure |
| Sonnenblumenöl | TC-3781 | 2023-08-18 | Operations |
| Sonnenblumenöl Pharmazeutisch rein | IC-3793 | 2023-08-23 | Supply Chain |
| Cyclodextrin Standardqualität | BC-3808 | 2024-09-25 | Supply Chain |
| Kasein 25% Technische Qualität | TC-3813 | 2021-03-08 | Operations |
| Maltodextrin-Pulver DE30 Standardqualität | TC-3816 | 2023-07-08 | Compliance |
| Natriumbenzoat Qualitätsstufe I | TC-3818 | 2022-12-23 | Product Management |
| Weizenklebereiweiß | TC-3826 | 2022-01-14 | Product Management |
| Maltodextrin-Pulver DE18 | BC-3830 | 2023-03-05 | Product Management |
| Sonnenblumenöl Qualitätsstufe I | IC-3835 | 2024-11-05 | Data Governance |
| Kaliumsorbat 50% Lebensmittelrein | TC-3842 | 2021-04-17 | Operations |
| Fructose Standardqualität | BC-3847 | 2023-02-20 | Data Governance |
| Soja Isolate 50% Premiumqualität | BC-3854 | 2023-07-18 | Data Governance |
| Resistente Stärke 70% | TC-3858 | 2024-12-27 | Compliance |
| Isoglucose 25% Standardqualität | IC-3861 | 2022-03-07 | Operations |
| Resistente Stärke | BC-3867 | 2022-08-01 | IT Infrastructure |
| Kaliumsorbat Lebensmittelrein | BC-3874 | 2022-07-12 | Finance |
| Zitronensäure | IC-3882 | 2023-02-11 | Operations |
| Soja Isolate Premiumqualität | TC-3891 | 2023-02-24 | Product Management |
| Pea Protein Standardqualität | BC-3896 | 2021-09-12 | Data Governance |
| Resistente Stärke 70% | IC-3903 | 2021-11-02 | Compliance |
| Fructose Premiumqualität | BC-3911 | 2022-09-24 | Finance |
| Zitronensäure Lebensmittelrein | TC-3916 | 2021-09-09 | Compliance |
| Dextrin Technische Qualität | TC-3920 | 2021-06-01 | IT Infrastructure |
| Natriumbenzoat Pharmazeutisch rein | TC-3924 | 2024-11-12 | IT Infrastructure |
| Premier Rohstoffe Holdings | IC-3938 | 2023-04-03 | Product Management |
| Pinnacle Rohstoffe NV | TC-3951 | 2022-03-03 | IT Infrastructure |
| Atlas Handel SARL | IC-3956 | 2021-03-03 | Data Governance |
| Horizon Handel KG | BC-3959 | 2023-06-14 | Product Management |
| Stellar Vertrieb | IC-3963 | 2024-01-06 | Operations |
| Pinnacle Ingredients | TC-3968 | 2024-01-07 | Supply Chain |
| Stratos Ingredients | BC-3978 | 2023-03-24 | Finance |
| Pacific Logistik | BC-3990 | 2024-10-02 | Compliance |
| Stratos Versorgung | TC-3994 | 2022-01-23 | IT Infrastructure |
| Quantum Ingredients | BC-3999 | 2023-02-22 | Product Management |
| Core Chemicals International | TC-4009 | 2024-05-06 | Finance |
| Catalyst Manufacturing GmbH | BC-4018 | 2024-12-11 | Operations |
| Pacific Chemicals GmbH | BC-4026 | 2021-04-11 | Operations |
| Pacific Vertrieb NV | TC-4032 | 2024-08-23 | Compliance |
| Pacific Vertrieb Group | BC-4036 | 2023-10-12 | Product Management |
| Premier Enterprise Holdings | TC-4043 | 2021-05-15 | Operations |
| Vertex Enterprise Group | TC-4059 | 2023-10-26 | Operations |
| Prime Chemicals SAS | IC-4065 | 2023-02-07 | Supply Chain |
| Vanguard Logistik SA | TC-4070 | 2023-03-02 | Operations |
| Stratos Handel | IC-4076 | 2023-03-25 | IT Infrastructure |
| Baltic Enterprise | BC-4084 | 2024-04-17 | Product Management |
| Premier Logistik | BC-4092 | 2021-09-25 | Product Management |
| Quantum Manufacturing | BC-4099 | 2024-02-22 | IT Infrastructure |
| Atlas Ingredients Ltd. | IC-4109 | 2023-10-05 | Compliance |
| Vertex Vertrieb NV | BC-4115 | 2024-08-18 | Data Governance |
| Atlas Manufacturing Corp. | TC-4123 | 2024-02-02 | Supply Chain |
| Atlantic Manufacturing International | BC-4127 | 2022-03-18 | Data Governance |
| Zenith Manufacturing International | BC-4135 | 2023-08-18 | Operations |
| Stratos Versorgung BV | TC-4154 | 2022-04-11 | IT Infrastructure |
| Global Verarbeitung SAS | TC-4160 | 2022-05-21 | Product Management |
| Apex Solutions International | IC-4173 | 2022-06-14 | Supply Chain |
| Pinnacle Chemicals SAS | BC-4178 | 2024-06-25 | Compliance |
| Core Manufacturing | TC-4181 | 2023-08-14 | Data Governance |
| Pinnacle Industrien SAS | BC-4185 | 2021-07-24 | IT Infrastructure |
| Pinnacle Handel Inc. | BC-4192 | 2023-11-01 | Supply Chain |
| Elite Vertrieb International | BC-4207 | 2023-02-12 | Supply Chain |
| Prime Versorgung | TC-4212 | 2023-10-21 | Data Governance |
| Prism Vertrieb NV | TC-4216 | 2021-09-21 | Product Management |
| Prism Ingredients NV | TC-4232 | 2022-10-14 | Compliance |
| Core Rohstoffe | BC-4236 | 2023-08-17 | Supply Chain |
| Stellar Versorgung NV | TC-4241 | 2021-04-01 | IT Infrastructure |
| Meridian Solutions | BC-4246 | 2021-11-23 | Operations |
| Apex Chemicals | BC-4252 | 2021-03-28 | Product Management |
| Pinnacle Verarbeitung | TC-4254 | 2024-11-21 | Supply Chain |
| Elite Chemicals KG | BC-4256 | 2021-12-07 | Finance |
| Nordic Ingredients | BC-4259 | 2021-11-02 | Compliance |
| Global Enterprise NV | TC-4267 | 2023-04-10 | Operations |
| Vanguard Enterprise Group | BC-4273 | 2023-09-24 | Compliance |
| Continental Enterprise GmbH | IC-4286 | 2023-05-18 | Data Governance |
| Core Logistik Holdings | TC-4293 | 2021-01-11 | Operations |
| Core Chemicals Holdings | TC-4300 | 2023-03-27 | Data Governance |
| Baltic Handel NV | TC-4313 | 2022-11-13 | Data Governance |
| Vertex Solutions NV | IC-4318 | 2024-06-12 | Compliance |
| Nordic Ingredients SARL | IC-4327 | 2022-11-13 | IT Infrastructure |
| Catalyst Rohstoffe GmbH | IC-4344 | 2023-05-22 | Operations |
| Apex Handel International | IC-4353 | 2022-06-11 | Data Governance |
| Continental Ingredients | TC-4361 | 2024-01-22 | Supply Chain |
| Nexus Vertrieb KG | IC-4366 | 2023-08-21 | Supply Chain |
| Catalyst Industrien International | TC-4382 | 2024-09-25 | Product Management |
| Vanguard Werkstoffe Group | TC-4388 | 2021-10-23 | Compliance |
| Pinnacle Rohstoffe NV | IC-4394 | 2022-02-25 | IT Infrastructure |
| Premier Solutions | BC-4401 | 2021-03-28 | Product Management |
| Apex Chemicals Corp. | IC-4411 | 2021-10-13 | Compliance |
| Global Ingredients GmbH | BC-4418 | 2024-12-21 | Product Management |
| Nexus Enterprise Group | TC-4424 | 2024-04-03 | Product Management |
| Apex Chemicals International | BC-4431 | 2021-01-27 | Product Management |
| Pinnacle Solutions Corp. | BC-4437 | 2021-12-07 | Compliance |
| Atlas Chemicals | TC-4442 | 2024-05-24 | Supply Chain |
| Premier Industrien Group | BC-4454 | 2023-05-11 | Data Governance |
| Atlantic Rohstoffe GmbH | IC-4459 | 2021-01-22 | Data Governance |
| Prism Ingredients | TC-4465 | 2024-04-12 | Finance |
| Apex Rohstoffe Holdings | TC-4471 | 2024-07-18 | IT Infrastructure |
| Apex Ingredients KG | BC-4481 | 2023-10-01 | Operations |
| Nexus Vertrieb | IC-4506 | 2021-03-01 | Operations |
| Pinnacle Ingredients KG | IC-4513 | 2021-05-26 | Product Management |
| Continental Chemicals Inc. | TC-4523 | 2022-04-15 | IT Infrastructure |
| Pinnacle Chemicals Ltd. | TC-4532 | 2021-12-07 | Product Management |
| Catalyst Enterprise International | IC-4546 | 2024-07-05 | Data Governance |
| Global Solutions Group | IC-4556 | 2021-01-22 | Data Governance |
| Pacific Ingredients BV | IC-4562 | 2022-11-24 | Product Management |
| Atlas Solutions NV | TC-4567 | 2024-10-08 | Data Governance |
| Atlas Enterprise International | BC-4570 | 2023-07-11 | Product Management |
| Stratos Chemicals | TC-4574 | 2023-03-12 | Finance |
| Nordic Industrien PLC | IC-4579 | 2023-03-18 | IT Infrastructure |
| Horizon Partners Ltd. | IC-4582 | 2022-01-07 | IT Infrastructure |
| Horizon Industrien GmbH | TC-4589 | 2023-05-24 | Finance |
| Atlantic Partners NV | IC-4596 | 2024-10-20 | IT Infrastructure |
| Quantum Rohstoffe PLC | IC-4601 | 2022-09-15 | Operations |
| Prism Industrien | IC-4619 | 2021-02-11 | Supply Chain |
| Prism Werkstoffe Ltd. | IC-4631 | 2024-02-03 | IT Infrastructure |
| Core Werkstoffe | IC-4634 | 2022-11-20 | IT Infrastructure |
| Nexus Ingredients PLC | TC-4639 | 2021-05-24 | Operations |
| Vertex Ingredients | BC-4643 | 2022-02-10 | Supply Chain |
| Continental Solutions NV | TC-4650 | 2024-01-06 | IT Infrastructure |
| Stellar Rohstoffe | IC-4659 | 2024-04-03 | Data Governance |
| Nexus Rohstoffe Group | BC-4665 | 2023-04-18 | Data Governance |
| Pinnacle Handel | TC-4668 | 2024-04-03 | Supply Chain |
| Catalyst Industrien PLC | BC-4674 | 2021-01-25 | Supply Chain |
| Continental Rohstoffe GmbH | BC-4677 | 2023-08-14 | Finance |
| Global Werkstoffe BV | TC-4680 | 2022-09-15 | Compliance |
| Atlas Industrien International | TC-4690 | 2021-09-23 | Operations |
| Quantum Partners NV | TC-4695 | 2024-04-27 | Supply Chain |
| Atlantic Industrien GmbH | IC-4704 | 2022-06-17 | Supply Chain |
| Vertex Rohstoffe | IC-4714 | 2023-08-16 | Compliance |
| Atlantic Industrien Group | IC-4732 | 2024-09-15 | Finance |
| Nordic Werkstoffe | IC-4744 | 2021-03-28 | Finance |
| Atlantic Handel BV | BC-4748 | 2024-10-26 | Supply Chain |
| Elite Solutions Group | TC-4755 | 2023-04-11 | Supply Chain |
| Atlantic Logistik SAS | TC-4761 | 2023-08-09 | IT Infrastructure |
| Central Ingredients International | IC-4772 | 2022-11-22 | Operations |
| Premier Industrien SAS | IC-4778 | 2023-03-10 | Product Management |
| Global Handel Ltd. | TC-4780 | 2022-10-27 | Finance |
| Horizon Partners International | IC-4786 | 2022-04-22 | Finance |
| Premier Enterprise | IC-4793 | 2023-02-09 | Compliance |
| Zenith Handel | IC-4806 | 2024-04-26 | Product Management |
| Elite Logistik Group | BC-4811 | 2024-02-06 | Compliance |
| Stellar Vertrieb | BC-4820 | 2021-05-08 | Operations |
| Premier Handel AG | IC-4828 | 2023-01-22 | Finance |
| Quantum Rohstoffe | IC-4835 | 2024-02-04 | Operations |
| Nexus Vertrieb PLC | TC-4840 | 2024-04-12 | Data Governance |
| Prism Chemicals | TC-4845 | 2024-04-12 | Data Governance |
| Core Partners | BC-4851 | 2021-10-21 | Operations |
| Catalyst Rohstoffe SA | IC-4858 | 2024-04-25 | Data Governance |
| Nexus Partners | BC-4865 | 2022-11-08 | Compliance |
| Continental Werkstoffe BV | BC-4873 | 2021-11-20 | IT Infrastructure |
| Stellar Partners | TC-4881 | 2023-07-10 | Compliance |
| Meridian Vertrieb International | BC-4891 | 2021-12-26 | Compliance |
| Premier Handel Group | TC-4897 | 2021-08-12 | Finance |
| Horizon Handel PLC | TC-4903 | 2022-04-13 | Operations |
| Pinnacle Chemicals | BC-4908 | 2022-02-10 | Data Governance |
| Atlantic Industrien International | BC-4916 | 2022-01-14 | Supply Chain |
| Stellar Manufacturing Holdings | BC-4923 | 2023-12-17 | IT Infrastructure |
| Zenith Manufacturing Ltd. | IC-4927 | 2022-02-22 | Product Management |
| Core Chemicals AG | BC-4931 | 2024-12-17 | Compliance |
| Apex Werkstoffe | IC-4938 | 2022-08-25 | Compliance |
| Horizon Partners Holdings | BC-4946 | 2021-04-13 | Operations |
| Elite Handel Holdings | BC-4951 | 2024-02-27 | Compliance |
| Continental Verarbeitung Holdings | TC-4957 | 2024-06-09 | IT Infrastructure |
| Elite Werkstoffe | BC-4966 | 2021-03-12 | Operations |
| Vanguard Ingredients | IC-4971 | 2022-01-06 | IT Infrastructure |
| Nexus Versorgung | BC-4979 | 2021-08-25 | Operations |
| Pacific Industrien | BC-4986 | 2021-02-17 | IT Infrastructure |
| Stratos Partners SAS | BC-4993 | 2024-08-06 | Finance |
| Atlas Logistik International | BC-5001 | 2024-05-02 | Data Governance |
| Nexus Ingredients SAS | BC-5006 | 2024-01-19 | Compliance |
| Prism Ingredients | BC-5011 | 2021-05-10 | Operations |
| Central Manufacturing Ltd. | BC-5019 | 2024-08-03 | Product Management |
| Nordic Chemicals BV | BC-5022 | 2023-12-14 | Product Management |
| Prism Werkstoffe | TC-5033 | 2022-12-03 | Product Management |
| Quantum Verarbeitung SA | IC-5042 | 2022-02-13 | Operations |
| Global Verarbeitung Group | TC-5059 | 2021-01-23 | Supply Chain |
| Stratos Verarbeitung LLC | BC-5062 | 2022-09-02 | Product Management |
| Pacific Enterprise SARL | BC-5071 | 2021-11-25 | Supply Chain |
| Nordic Manufacturing NV | IC-5075 | 2023-07-10 | Compliance |
| Premier Vertrieb | BC-5081 | 2024-07-20 | Compliance |
| Continental Manufacturing | TC-5091 | 2022-02-18 | Finance |
| Nexus Enterprise BV | IC-5097 | 2021-08-06 | Supply Chain |
| Baltic Industrien NV | TC-5104 | 2021-06-28 | Operations |
| Atlas Partners | TC-5109 | 2024-10-01 | IT Infrastructure |
| Vertex Handel Holdings | IC-5121 | 2024-11-13 | Product Management |
| Vanguard Logistik International | TC-5138 | 2024-04-07 | Supply Chain |
| Atlantic Vertrieb Holdings | TC-5144 | 2024-05-15 | Operations |
| Global Chemicals SAS | TC-5160 | 2024-08-23 | Supply Chain |
| Meridian Ingredients | BC-5165 | 2021-06-28 | Data Governance |
| Prism Chemicals AG | IC-5172 | 2022-10-25 | Operations |
| Atlantic Verarbeitung Holdings | TC-5178 | 2024-01-09 | Product Management |
| Vertex Vertrieb Group | TC-5190 | 2021-01-05 | IT Infrastructure |
| Central Rohstoffe PLC | BC-5196 | 2021-10-12 | Finance |
| Atlantic Versorgung LLC | TC-5200 | 2024-10-22 | Supply Chain |
| Pinnacle Logistik BV | BC-5207 | 2021-06-24 | Compliance |
| Premier Manufacturing NV | IC-5219 | 2023-08-12 | Finance |
| Catalyst Industrien SARL | TC-5228 | 2023-01-07 | IT Infrastructure |
| Premier Partners SARL | TC-5234 | 2022-01-23 | Finance |
| Stellar Versorgung SA | IC-5242 | 2023-03-21 | Data Governance |
| Stratos Versorgung SA | TC-5245 | 2024-08-14 | IT Infrastructure |
| Pinnacle Werkstoffe SARL | IC-5251 | 2023-02-05 | IT Infrastructure |
| Vanguard Versorgung BV | TC-5254 | 2021-08-07 | Product Management |
| Continental Enterprise Holdings | IC-5265 | 2024-06-10 | IT Infrastructure |
| Apex Manufacturing | BC-5273 | 2022-03-24 | Supply Chain |
| Apex Verarbeitung | BC-5278 | 2021-11-10 | Operations |
| Pacific Werkstoffe GmbH | BC-5289 | 2024-01-07 | IT Infrastructure |
| Vanguard Vertrieb International | IC-5301 | 2021-09-14 | Compliance |
| Zenith Enterprise SARL | BC-5310 | 2023-05-24 | Compliance |
| Nordic Manufacturing Group | BC-5329 | 2023-08-12 | Supply Chain |
| Vertex Logistik Group | TC-5333 | 2024-09-21 | Finance |
| Global Ingredients NV | IC-5344 | 2022-03-28 | Finance |
| Quantum Verarbeitung PLC | TC-5345 | 2021-01-21 | Operations |
| Vanguard Vertrieb | IC-5355 | 2023-10-24 | Operations |
| Core Ingredients International | BC-5361 | 2022-03-19 | Finance |
| Baltic Versorgung | IC-5370 | 2022-02-15 | Data Governance |
| Premier Chemicals | IC-5375 | 2023-11-06 | IT Infrastructure |
| Premier Versorgung PLC | IC-5380 | 2024-11-13 | Compliance |
| Meridian Vertrieb International | IC-5386 | 2023-04-07 | Finance |
| Premier Logistik KG | BC-5409 | 2021-07-21 | Operations |
| Global Partners NV | BC-5418 | 2024-01-13 | Supply Chain |
| Nexus Partners SAS | BC-5422 | 2023-12-03 | IT Infrastructure |
| Core Manufacturing | TC-5429 | 2021-01-23 | Supply Chain |
| Nordic Vertrieb | TC-5437 | 2024-11-09 | Data Governance |
| Baltic Chemicals AG | IC-5439 | 2024-12-05 | Operations |
| Quantum Handel Ltd. | IC-5452 | 2022-07-17 | Product Management |
| Central Werkstoffe NV | BC-5460 | 2023-01-15 | Compliance |
| Central Logistik Holdings | IC-5464 | 2024-07-07 | Compliance |
| Elite Logistik | BC-5470 | 2024-07-13 | Finance |
| Continental Partners KG | IC-5473 | 2022-11-20 | Compliance |
| Horizon Vertrieb International | TC-5488 | 2021-01-15 | IT Infrastructure |
| Vanguard Chemicals SAS | IC-5489 | 2024-06-10 | Finance |
| Vertex Industrien NV | IC-5496 | 2022-06-13 | Compliance |
| Pinnacle Verarbeitung | IC-5503 | 2023-03-11 | Finance |
| Vertex Rohstoffe GmbH | BC-5512 | 2022-05-12 | Finance |
| Catalyst Versorgung International | BC-5522 | 2024-03-26 | Operations |
| Core Vertrieb | TC-5528 | 2021-12-27 | Finance |
| Nexus Verarbeitung Group | BC-5537 | 2022-05-02 | Finance |
| Catalyst Ingredients Holdings | BC-5550 | 2024-03-14 | Compliance |
| Prime Rohstoffe PLC | IC-5561 | 2022-10-15 | Data Governance |
| Stellar Vertrieb | BC-5571 | 2024-04-04 | Finance |
| Nordic Verarbeitung | BC-5578 | 2022-06-15 | Operations |
| Atlantic Chemicals SAS | BC-5585 | 2021-08-24 | Data Governance |
| Global Verarbeitung GmbH | TC-5603 | 2024-01-09 | Data Governance |
| Zenith Industrien LLC | IC-5611 | 2023-12-23 | Data Governance |
| Apex Handel | IC-5622 | 2023-10-09 | IT Infrastructure |
| Premier Partners | TC-5626 | 2022-07-21 | Data Governance |
| Vertex Vertrieb Holdings | IC-5639 | 2022-10-21 | Data Governance |
| Baltic Manufacturing | BC-5650 | 2021-01-12 | Product Management |
| Quantum Handel International | TC-5653 | 2022-12-18 | Supply Chain |
| Stellar Manufacturing Group | BC-5661 | 2021-09-09 | Product Management |
| Baltic Handel | TC-5670 | 2024-08-14 | Operations |
| Catalyst Versorgung International | TC-5679 | 2024-11-14 | Supply Chain |
| Atlantic Verarbeitung Group | IC-5695 | 2022-06-20 | Finance |
| Baltic Verarbeitung Group | BC-5700 | 2023-03-14 | Operations |
| Core Partners Ltd. | IC-5706 | 2021-02-19 | Compliance |
| Vertex Chemicals | TC-5712 | 2024-08-07 | Compliance |
| Vanguard Industrien | IC-5722 | 2024-02-26 | Data Governance |
| Prime Logistik | TC-5741 | 2021-12-08 | Supply Chain |
| Pinnacle Werkstoffe | BC-5746 | 2022-02-27 | Compliance |
| Atlantic Werkstoffe | BC-5752 | 2021-08-14 | Data Governance |
| Core Versorgung GmbH | IC-5756 | 2023-06-27 | Supply Chain |
| Catalyst Logistik | BC-5768 | 2021-02-10 | Product Management |
| Elite Logistik | IC-5771 | 2023-10-24 | Supply Chain |
| Baltic Versorgung GmbH | BC-5784 | 2024-07-02 | Operations |
| Stratos Logistik | IC-5790 | 2023-10-20 | Compliance |
| Core Werkstoffe | BC-5798 | 2021-09-06 | Finance |
| Vertex Werkstoffe | BC-5811 | 2021-08-03 | IT Infrastructure |
| Meridian Werkstoffe | IC-5815 | 2024-06-20 | Operations |
| Vertex Logistik | BC-5822 | 2024-01-02 | IT Infrastructure |
| Horizon Versorgung GmbH | TC-5826 | 2023-05-22 | Operations |
| Stellar Sourcing | IC-5833 | 2023-11-13 | Product Management |
| Nexus Sourcing | BC-5842 | 2023-03-04 | IT Infrastructure |
| Global Logistik | IC-5856 | 2021-01-23 | Compliance |
| Pinnacle Sourcing | BC-5862 | 2022-06-07 | Finance |
| Elite Sourcing | IC-5867 | 2023-08-02 | Product Management |
| Vanguard Werkstoffe | BC-5872 | 2023-02-26 | Compliance |
| Continental Sourcing | TC-5879 | 2021-02-20 | Product Management |
| Quantum Versorgung GmbH | TC-5888 | 2022-06-03 | IT Infrastructure |
| Zenith Versorgung GmbH | BC-5897 | 2022-08-07 | Product Management |
| Atlas Versorgung GmbH | TC-5902 | 2022-03-25 | Supply Chain |
| Catalyst Logistik | TC-5909 | 2023-03-06 | Compliance |
| Prism Werkstoffe | BC-5915 | 2024-11-21 | Operations |
| Global Sourcing | BC-5923 | 2022-09-04 | Compliance |
| Vertex Sourcing | IC-5927 | 2024-09-18 | Supply Chain |
| Atlas Versorgung GmbH | IC-5930 | 2021-08-20 | IT Infrastructure |
| Continental Versorgung GmbH | IC-5943 | 2021-07-17 | Supply Chain |
| Nexus Logistik | IC-5949 | 2023-02-13 | Operations |
| Stellar Logistik | IC-5957 | 2023-01-21 | Product Management |
| Premier Logistik | BC-5963 | 2022-04-25 | Compliance |
| Apex Werkstoffe | BC-5966 | 2024-06-02 | Operations |
| Vertex Logistik | BC-5973 | 2024-10-05 | Data Governance |
| Stellar Werkstoffe | BC-5980 | 2021-02-22 | Product Management |
| Quantum Versorgung GmbH | TC-5983 | 2023-04-14 | Operations |
| Nexus Logistik | IC-5987 | 2023-02-09 | Compliance |
| Elite Logistik | TC-5994 | 2021-08-05 | Operations |
| Prism Sourcing | BC-6001 | 2021-03-14 | Supply Chain |
| Stratos Sourcing | TC-6005 | 2023-07-19 | Data Governance |
| Premier Versorgung GmbH | IC-6013 | 2024-11-08 | IT Infrastructure |
| Continental Versorgung GmbH | IC-6018 | 2024-10-11 | Operations |
| Nexus Logistik | IC-6024 | 2021-06-15 | Supply Chain |
| Atlas Logistik | TC-6042 | 2024-04-15 | Supply Chain |
| Prime Versorgung GmbH | IC-6052 | 2022-07-17 | Operations |
| Quantum Versorgung GmbH | IC-6066 | 2022-08-27 | IT Infrastructure |
| Stellar Logistik | BC-6070 | 2022-11-14 | Operations |
| Quantum Sourcing | BC-6078 | 2023-12-12 | Finance |
| Prism Sourcing | BC-6090 | 2023-07-06 | Product Management |
| Central Logistik | TC-6097 | 2021-10-26 | Data Governance |
| Premier Versorgung GmbH | TC-6106 | 2022-05-04 | Product Management |
| Apex Versorgung GmbH | IC-6115 | 2022-02-04 | IT Infrastructure |
| Stratos Versorgung GmbH | TC-6129 | 2024-12-03 | Compliance |
| Apex Logistik | TC-6140 | 2024-07-08 | Finance |
| Premier Logistik | BC-6149 | 2023-07-04 | Operations |
| Central Werkstoffe | TC-6158 | 2021-04-18 | Product Management |
| Zenith Logistik | TC-6171 | 2021-02-14 | Data Governance |
| Nordic Sourcing | IC-6176 | 2021-08-26 | Compliance |
| Stellar Sourcing | BC-6181 | 2024-05-23 | Supply Chain |
| Pacific Sourcing | IC-6185 | 2021-03-07 | Product Management |
| Stratos Sourcing | TC-6190 | 2023-04-08 | Finance |
| Prism Logistik | BC-6197 | 2021-10-05 | Operations |
| Nexus Werkstoffe | TC-6206 | 2022-06-19 | Compliance |
| Meridian Logistik | IC-6210 | 2022-01-13 | Compliance |
| Prime Werkstoffe | BC-6212 | 2023-12-13 | Compliance |
| Horizon Sourcing | TC-6217 | 2023-01-25 | Finance |
| Central Sourcing | BC-6224 | 2021-08-26 | Operations |
| Atlantic Sourcing | IC-6238 | 2024-02-24 | IT Infrastructure |
| Horizon Werkstoffe | TC-6253 | 2022-11-13 | Operations |
| Vanguard Versorgung GmbH | IC-6256 | 2023-03-14 | Operations |
| Continental Logistik | BC-6263 | 2024-08-18 | Operations |
| Atlantic Sourcing | IC-6270 | 2021-05-02 | Data Governance |
| Catalyst Sourcing | BC-6273 | 2021-02-09 | Supply Chain |
| Zenith Versorgung GmbH | IC-6279 | 2022-01-15 | Operations |
| Nordic Logistik | BC-6288 | 2022-12-14 | Finance |
| Atlas Logistik | BC-6290 | 2021-11-12 | Compliance |
| Baltic Versorgung GmbH | IC-6306 | 2022-01-23 | IT Infrastructure |
| Prism Sourcing | BC-6314 | 2024-07-21 | Operations |
| Meridian Sourcing | BC-6323 | 2023-04-10 | Compliance |
| Stratos Werkstoffe | TC-6334 | 2021-11-16 | Data Governance |
| Baltic Versorgung GmbH | TC-6341 | 2024-12-16 | Data Governance |
| Vertex Versorgung GmbH | TC-6347 | 2024-03-19 | Product Management |
| Horizon Logistik | BC-6352 | 2024-08-02 | IT Infrastructure |
| Pacific Werkstoffe | BC-6358 | 2022-09-03 | IT Infrastructure |
| Quantum Versorgung GmbH | TC-6362 | 2024-08-13 | Supply Chain |
| Pacific Werkstoffe | IC-6366 | 2022-02-08 | Supply Chain |
| Stellar Versorgung GmbH | BC-6371 | 2022-12-24 | Data Governance |
| Horizon Sourcing | BC-6373 | 2024-01-08 | Product Management |
| Nexus Werkstoffe | IC-6387 | 2021-02-12 | Data Governance |
| Baltic Versorgung GmbH | TC-6393 | 2024-02-12 | Compliance |
| Apex Sourcing | IC-6400 | 2021-06-25 | Compliance |
| Atlas Sourcing | TC-6404 | 2021-04-23 | Data Governance |
| Pacific Versorgung GmbH | TC-6428 | 2024-06-11 | Product Management |
| Nexus Werkstoffe | IC-6436 | 2024-12-28 | Supply Chain |
| Apex Sourcing | BC-6445 | 2023-12-15 | Data Governance |
| Meridian Werkstoffe | BC-6452 | 2021-08-06 | IT Infrastructure |
| Stellar Logistik | TC-6457 | 2024-08-06 | Data Governance |
| Prism Werkstoffe | BC-6464 | 2022-03-04 | Compliance |
| Prism Versorgung GmbH | IC-6471 | 2023-11-19 | IT Infrastructure |
| Atlas Logistik | IC-6479 | 2023-04-11 | Compliance |
| Central Versorgung GmbH | IC-6485 | 2023-09-15 | Product Management |
| Zenith Logistik | BC-6493 | 2023-03-16 | IT Infrastructure |
| Horizon Sourcing | IC-6501 | 2024-06-04 | Compliance |
| Vertex Sourcing | BC-6504 | 2023-02-22 | Operations |
| Pacific Werkstoffe | BC-6518 | 2023-04-21 | Data Governance |
| Atlas Werkstoffe | TC-6521 | 2021-07-24 | Finance |
| Nexus Werkstoffe | TC-6529 | 2024-12-23 | Supply Chain |
| Meridian Versorgung GmbH | TC-6546 | 2024-04-12 | Compliance |
| Nordic Logistik | BC-6552 | 2024-11-27 | Finance |
| Atlantic Versorgung GmbH | IC-6556 | 2021-12-10 | IT Infrastructure |
| Zenith Logistik | BC-6560 | 2021-02-21 | Operations |
| Catalyst Werkstoffe | TC-6569 | 2022-04-19 | Compliance |
| Continental Sourcing | BC-6579 | 2024-04-23 | Data Governance |
| Stratos Sourcing | BC-6585 | 2024-08-14 | Product Management |
| Catalyst Werkstoffe | BC-6591 | 2022-06-01 | Finance |
| Pinnacle Logistik | IC-6596 | 2023-10-20 | Supply Chain |
| Premier Versorgung GmbH | BC-6604 | 2024-06-11 | Supply Chain |
| Atlantic Werkstoffe | BC-6614 | 2024-02-18 | Operations |
| Meridian Werkstoffe | IC-6620 | 2021-03-22 | Operations |
| Central Logistik | BC-6638 | 2023-09-08 | Product Management |
| Elite Logistik | TC-6645 | 2023-02-24 | Data Governance |
| Premier Logistik | IC-6653 | 2023-10-26 | IT Infrastructure |
| Core Sourcing | BC-6670 | 2022-05-24 | Finance |
| Elite Werkstoffe | IC-6675 | 2024-12-17 | Finance |
| Pinnacle Sourcing | BC-6681 | 2021-08-17 | Data Governance |
| Vertex Sourcing | BC-6687 | 2023-07-19 | Operations |
| Global Werkstoffe | BC-6691 | 2022-05-14 | Product Management |
| Vertex Werkstoffe | IC-6695 | 2021-03-25 | Operations |
| Baltic Logistik | BC-6701 | 2024-02-03 | Compliance |
| Quantum Versorgung GmbH | TC-6723 | 2024-02-26 | Product Management |
| Prism Sourcing | IC-6739 | 2021-08-17 | Finance |
| Vanguard Werkstoffe | BC-6745 | 2022-06-18 | Compliance |
| Stratos Logistik | IC-6750 | 2022-11-18 | Operations |
| Elite Sourcing | TC-6754 | 2022-02-25 | Compliance |
| Atlantic Werkstoffe | BC-6776 | 2022-04-11 | Compliance |
| Atlas Versorgung GmbH | BC-6782 | 2024-05-23 | Compliance |
| Nordic Versorgung GmbH | BC-6787 | 2021-06-24 | Data Governance |
| Stratos Werkstoffe | BC-6803 | 2023-07-02 | Finance |
| Horizon Logistik | IC-6807 | 2023-11-17 | Compliance |
| Baltic Werkstoffe | IC-6811 | 2022-11-05 | Product Management |
| Quantum Versorgung GmbH | TC-6813 | 2023-11-20 | Product Management |
| Baltic Werkstoffe | BC-6819 | 2024-11-15 | Finance |
| Pacific Werkstoffe | IC-6823 | 2024-07-26 | Supply Chain |
| Pacific Werkstoffe | IC-6833 | 2021-03-09 | Operations |
| Stratos Logistik | IC-6839 | 2024-10-13 | IT Infrastructure |
| Core Logistik | TC-6845 | 2022-03-09 | Product Management |
| Quantum Versorgung GmbH | IC-6848 | 2023-03-26 | Product Management |
| Elite Logistik | IC-6854 | 2024-07-24 | IT Infrastructure |
| Premier Logistik | IC-6865 | 2021-08-27 | Compliance |
| Baltic Sourcing | TC-6881 | 2021-07-21 | Product Management |
| Elite Werkstoffe | IC-6883 | 2024-04-10 | IT Infrastructure |
| Core Sourcing | TC-6890 | 2023-02-15 | Supply Chain |
| Premier Sourcing | TC-6899 | 2022-03-24 | Compliance |
| Central Werkstoffe | BC-6914 | 2023-09-16 | Data Governance |
| Baltic Sourcing | TC-6929 | 2022-04-17 | Finance |
| Vertex Logistik | BC-6933 | 2024-06-25 | Operations |
| Baltic Sourcing | IC-6943 | 2024-11-05 | Supply Chain |
| Atlantic Werkstoffe | BC-6947 | 2022-06-26 | IT Infrastructure |
| Prism Werkstoffe | TC-6958 | 2024-02-10 | Compliance |
| Atlas Werkstoffe | IC-6964 | 2021-11-09 | Compliance |
| Vertex Werkstoffe | TC-6971 | 2021-03-10 | Supply Chain |
| Stratos Versorgung GmbH | BC-6988 | 2024-01-15 | IT Infrastructure |
| Apex Versorgung GmbH | IC-6993 | 2024-12-07 | IT Infrastructure |
| Atlas Werkstoffe | TC-6996 | 2023-05-24 | Product Management |
| Apex Versorgung GmbH | TC-7003 | 2022-01-15 | Compliance |
| Vanguard Logistik | BC-7018 | 2021-08-23 | IT Infrastructure |
| Pinnacle Sourcing | BC-7028 | 2021-10-07 | Operations |
| Meridian Logistik | IC-7039 | 2023-05-02 | Compliance |
| Pinnacle Versorgung GmbH | TC-7046 | 2023-11-14 | Product Management |
| Pacific Logistik | BC-7055 | 2024-12-01 | Product Management |
| Stellar Logistik | BC-7058 | 2022-10-14 | Product Management |
| Stratos Werkstoffe | BC-7069 | 2024-04-25 | Supply Chain |
| Vanguard Versorgung GmbH | IC-7078 | 2024-12-24 | Operations |
| Vertex Versorgung GmbH | TC-7082 | 2023-06-17 | Compliance |
| Stellar Werkstoffe | IC-7087 | 2024-01-07 | Product Management |
| Atlas Versorgung GmbH | BC-7096 | 2024-06-05 | Product Management |
| Nexus Werkstoffe | BC-7107 | 2024-05-09 | Data Governance |
| Catalyst Werkstoffe | BC-7118 | 2022-12-07 | Data Governance |
| Prime Werkstoffe | IC-7130 | 2024-11-02 | IT Infrastructure |
| Vat Reduced GB 15% | IC-7137 | 2022-01-23 | Data Governance |
| Vat Standardqualität NL 25% | BC-7156 | 2023-12-20 | Data Governance |
| Customs Duty FR 7% | IC-7161 | 2024-09-22 | Operations |
| Withholding GB 5% | IC-7169 | 2023-03-02 | Product Management |
| Customs Duty CN 0% | BC-7179 | 2024-07-24 | Operations |
| Vat Standardqualität GB 21% | TC-7183 | 2022-08-25 | Product Management |
| Customs Duty BR 15% | TC-7189 | 2021-12-10 | Data Governance |
| Vat Standardqualität DE 19% | TC-7193 | 2024-09-22 | IT Infrastructure |
| Vat Standardqualität IN 0% | TC-7196 | 2021-03-03 | Supply Chain |
| Customs Duty GB 5% | IC-7201 | 2024-09-13 | Supply Chain |
| Customs Duty FR 19% | IC-7203 | 2024-08-01 | Product Management |
| Vat Standardqualität NL 20% | TC-7212 | 2022-10-24 | Data Governance |
| Withholding BR 0% | IC-7217 | 2023-06-14 | Supply Chain |
| Withholding BR 15% | BC-7221 | 2021-09-14 | IT Infrastructure |
| Vat Standardqualität NL 20% | BC-7227 | 2022-10-08 | Compliance |
| Withholding US 0% | BC-7232 | 2024-05-17 | Supply Chain |
| Vat Reduced CN 21% | IC-7237 | 2021-06-03 | Product Management |
| Vat Standardqualität DE 10% | TC-7256 | 2024-05-18 | IT Infrastructure |
| Vat Standardqualität US 5% | TC-7261 | 2021-05-12 | Supply Chain |
| Vat Standardqualität GB 5% | TC-7270 | 2021-08-21 | Data Governance |
| Vat Standardqualität GB 21% | TC-7293 | 2024-06-17 | IT Infrastructure |
| Excise IN 25% | BC-7301 | 2023-06-28 | Data Governance |
| Vat Reduced BR 21% | IC-7310 | 2024-10-06 | Compliance |
| Excise GB 19% | TC-7312 | 2024-08-16 | IT Infrastructure |
| Vat Standardqualität FR 25% | TC-7327 | 2021-07-05 | Product Management |
| Vat Standardqualität FR 19% | TC-7335 | 2024-11-13 | IT Infrastructure |
| Customs Duty FR 19% | TC-7341 | 2021-09-06 | Operations |
| Vat Reduced BR 10% | TC-7344 | 2022-01-15 | Finance |
| Vat Reduced BR 25% | TC-7356 | 2023-11-20 | Operations |
| Vat Standardqualität BR 0% | IC-7365 | 2023-04-25 | Data Governance |
| Vat Standardqualität GB 20% | BC-7372 | 2022-06-28 | IT Infrastructure |
| Customs Duty IN 5% | BC-7378 | 2024-11-09 | Data Governance |
| Customs Duty DE 5% | BC-7383 | 2024-02-20 | Finance |
| Vat Reduced GB 19% | TC-7392 | 2021-04-18 | Product Management |
| Excise BR 15% | TC-7400 | 2021-01-26 | Operations |
| Vat Reduced FR 25% | TC-7407 | 2024-10-04 | Data Governance |
| Vat Standardqualität US 10% | IC-7420 | 2024-04-13 | Compliance |
| Withholding NL 7% | TC-7427 | 2023-01-22 | Product Management |
| Excise NL 7% | IC-7435 | 2023-10-13 | Product Management |
| Customs Duty DE 15% | IC-7441 | 2021-06-28 | IT Infrastructure |
| Excise US 15% | IC-7447 | 2024-10-10 | Product Management |
| Withholding US 10% | TC-7459 | 2024-11-10 | Data Governance |
| Excise NL 21% | TC-7466 | 2023-01-13 | Compliance |
| Excise US 19% | BC-7472 | 2021-05-10 | Product Management |
| Vat Reduced GB 25% | TC-7477 | 2021-11-02 | Supply Chain |
| Withholding FR 19% | BC-7482 | 2024-04-20 | IT Infrastructure |
| Vat Reduced BR 7% | BC-7495 | 2024-12-08 | Product Management |
| Vat Reduced IN 20% | IC-7500 | 2021-05-14 | Compliance |
| Vat Reduced BR 0% | BC-7507 | 2023-05-10 | Supply Chain |
| Vat Reduced FR 0% | BC-7519 | 2023-02-02 | Finance |
| Customs Duty US 10% | IC-7526 | 2024-03-11 | IT Infrastructure |
| Customs Duty CN 10% | TC-7531 | 2021-02-05 | Finance |
| Vat Standardqualität DE 19% | TC-7547 | 2022-01-24 | Operations |
| Withholding CN 15% | IC-7549 | 2023-01-05 | Finance |
| Vat Reduced NL 19% | IC-7555 | 2021-06-09 | IT Infrastructure |
| Vat Reduced US 19% | BC-7567 | 2024-09-15 | Data Governance |
| Withholding FR 5% | TC-7576 | 2024-07-25 | Supply Chain |
| Excise BR 25% | BC-7580 | 2024-10-22 | Operations |
| Excise NL 20% | TC-7590 | 2024-11-12 | Compliance |
| Vat Standardqualität IN 10% | TC-7597 | 2022-12-02 | IT Infrastructure |
| Customs Duty CN 25% | TC-7603 | 2021-04-18 | Product Management |
| Customs Duty US 19% | BC-7610 | 2023-01-17 | Supply Chain |
| Vat Reduced DE 5% | TC-7613 | 2022-01-20 | Finance |
| Vat Standardqualität CN 10% | BC-7621 | 2024-06-04 | Supply Chain |
| Excise DE 10% | BC-7630 | 2021-05-27 | Supply Chain |
| Excise GB 25% | IC-7638 | 2023-06-03 | Data Governance |
| Vat Reduced CN 5% | IC-7644 | 2022-01-21 | Supply Chain |
| Customs Duty IN 25% | IC-7653 | 2022-04-04 | Data Governance |
| Withholding NL 5% | IC-7655 | 2024-06-19 | Compliance |
| Excise US 20% | IC-7662 | 2024-05-20 | Operations |
| Excise NL 15% | BC-7668 | 2022-12-10 | Supply Chain |
| Customs Duty BR 7% | IC-7679 | 2024-08-08 | Data Governance |
| Withholding BR 10% | IC-7687 | 2021-06-08 | Compliance |
| Vat Standardqualität NL 20% | TC-7693 | 2024-05-10 | Data Governance |
| Vat Standardqualität NL 19% | BC-7703 | 2023-08-23 | Product Management |
| Vat Reduced CN 19% | TC-7716 | 2023-08-25 | Finance |
| Vat Reduced NL 0% | IC-7719 | 2021-02-10 | Finance |
| Vat Standardqualität NL 5% | TC-7722 | 2024-07-18 | Finance |
| Excise DE 10% | BC-7728 | 2022-03-01 | Product Management |
| Customs Duty CN 25% | IC-7731 | 2022-02-23 | Product Management |
| Withholding FR 5% | BC-7740 | 2022-06-04 | Product Management |
| Vat Reduced BR 7% | TC-7743 | 2024-03-17 | Compliance |
| Excise BR 19% | TC-7750 | 2023-05-28 | Compliance |
| Vat Standardqualität IN 5% | IC-7756 | 2022-09-25 | Compliance |
| Customs Duty FR 15% | IC-7765 | 2023-02-06 | Product Management |
| Vat Reduced BR 10% | BC-7782 | 2022-08-24 | IT Infrastructure |
| Vat Standardqualität CN 0% | IC-7786 | 2024-03-28 | Operations |
| Customs Duty GB 5% | BC-7793 | 2023-12-05 | Supply Chain |
| Customs Duty CN 7% | TC-7799 | 2024-11-27 | Compliance |
| Customs Duty FR 7% | BC-7825 | 2023-01-16 | Data Governance |
| Vat Standardqualität IN 19% | BC-7830 | 2024-02-16 | Finance |
| Excise US 7% | TC-7843 | 2022-10-01 | Operations |
| Vat Standardqualität NL 5% | IC-7852 | 2024-05-12 | Finance |
| Vat Reduced CN 19% | BC-7866 | 2023-12-15 | Compliance |
| Customs Duty IN 20% | TC-7877 | 2023-07-10 | Data Governance |
| Excise GB 5% | TC-7882 | 2022-12-09 | IT Infrastructure |
| Customs Duty GB 15% | BC-7887 | 2023-06-24 | Compliance |
| Excise BR 19% | BC-7892 | 2024-08-27 | Data Governance |
| Vat Reduced NL 5% | BC-7897 | 2022-07-14 | Supply Chain |
| Vat Reduced FR 20% | BC-7903 | 2023-10-11 | IT Infrastructure |
| Vat Standardqualität GB 19% | BC-7908 | 2024-07-27 | Product Management |
| Vat Standardqualität US 21% | IC-7916 | 2022-05-01 | IT Infrastructure |
| Customs Duty BR 20% | TC-7920 | 2023-08-24 | Data Governance |
| Excise US 5% | BC-7927 | 2021-10-07 | Product Management |
| Customs Duty GB 5% | BC-7935 | 2023-10-17 | Product Management |
| Withholding CN 0% | BC-7949 | 2021-08-08 | Supply Chain |
| Customs Duty CN 0% | BC-7954 | 2023-07-09 | Supply Chain |
| Vat Reduced FR 10% | BC-7975 | 2023-11-09 | Compliance |
| Excise DE 21% | IC-7979 | 2024-05-16 | IT Infrastructure |
| Withholding IN 10% | BC-7986 | 2024-01-22 | Compliance |
| Excise CN 20% | IC-7993 | 2023-11-13 | Finance |
| Vat Reduced CN 15% | BC-8004 | 2022-03-15 | Compliance |
| Vat Reduced GB 15% | BC-8015 | 2024-08-03 | Product Management |
| Excise CN 25% | TC-8021 | 2022-05-07 | Operations |
| Vat Reduced NL 25% | TC-8037 | 2023-04-06 | Product Management |
| Customs Duty NL 7% | BC-8044 | 2023-04-14 | Operations |
| Withholding GB 15% | IC-8049 | 2022-09-02 | Supply Chain |
| Excise FR 19% | IC-8072 | 2023-07-18 | IT Infrastructure |
| Customs Duty GB 7% | BC-8093 | 2023-03-27 | Finance |
| Customs Duty IN 5% | IC-8101 | 2024-09-11 | Operations |
| Withholding NL 21% | IC-8105 | 2024-07-09 | Product Management |
| Vat Reduced US 21% | TC-8111 | 2024-11-26 | Compliance |
| Withholding NL 5% | TC-8124 | 2022-01-16 | Operations |
| Vat Standardqualität NL 19% | IC-8130 | 2024-09-21 | Supply Chain |
| Customs Duty NL 15% | IC-8135 | 2024-03-15 | Product Management |
| Vat Standardqualität NL 20% | BC-8141 | 2023-01-09 | Product Management |
| Customs Duty DE 15% | IC-8149 | 2023-07-09 | Supply Chain |
| Customs Duty BR 21% | TC-8156 | 2024-03-05 | IT Infrastructure |
| Vat Reduced GB 25% | TC-8160 | 2024-01-22 | Operations |
| Customs Duty BR 15% | BC-8166 | 2021-07-13 | Product Management |
| Vat Reduced FR 20% | BC-8175 | 2023-12-24 | Finance |
| Vat Standardqualität FR 25% | TC-8182 | 2022-03-07 | Operations |
| Customs Duty DE 20% | BC-8188 | 2021-09-17 | Compliance |
| Withholding NL 21% | BC-8197 | 2024-12-10 | Finance |
| Vat Reduced IN 25% | BC-8206 | 2022-05-01 | Supply Chain |
| Customs Duty CN 19% | BC-8212 | 2024-01-12 | Operations |
| Excise FR 21% | IC-8215 | 2021-08-03 | Compliance |
| Vat Standardqualität FR 0% | BC-8228 | 2021-10-17 | Operations |
| Customs Duty FR 25% | TC-8238 | 2023-11-15 | Data Governance |
| Withholding FR 15% | BC-8252 | 2022-02-23 | Compliance |
| Vat Standardqualität DE 7% | TC-8261 | 2024-08-22 | Product Management |
| Vat Standardqualität CN 19% | BC-8269 | 2022-09-10 | Operations |
| Vat Standardqualität IN 0% | IC-8274 | 2023-12-22 | Data Governance |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| Resistente Stärke | IC-6939 | REVIEW REQUIRED | Historical - verify before use |
| Kasein 25% Pharmazeutisch rein | IC-9368 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid | IC-7684 | SUPERSEDED | Historical - verify before use |
| Sonnenblumenöl 98% Premiumqualität | IC-5002 | REVIEW REQUIRED | Historical - verify before use |
| Pea Protein 99.5% | IC-7561 | DEPRECATED | Historical - verify before use |
| Lactic Acid | IC-5591 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid Standardqualität | IC-6520 | DEPRECATED | Historical - verify before use |
| Zitronensäure 70% | IC-5951 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid Pharmazeutisch rein | IC-7626 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil Lebensmittelrein | IC-6777 | REVIEW REQUIRED | Historical - verify before use |
| Palmfett 98% | IC-9309 | SUPERSEDED | Historical - verify before use |
| Traubenzucker Lebensmittelrein | IC-8000 | SUPERSEDED | Historical - verify before use |
| Weizenklebereiweiß 98% Premiumqualität | IC-9192 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat 25% Standardqualität | IC-6625 | PROVISIONAL | Historical - verify before use |
| Coconut Oil 98% | IC-9388 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat 99.5% Qualitätsstufe I | IC-8885 | SUPERSEDED | Historical - verify before use |
| Cyclodextrin 98% Pharmazeutisch rein | IC-7411 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil Qualitätsstufe I | IC-8663 | REVIEW REQUIRED | Historical - verify before use |
| Traubenzucker Standardqualität | IC-7445 | SUPERSEDED | Historical - verify before use |
| Lactic Acid 99.5% Qualitätsstufe II | IC-5103 | PROVISIONAL | Historical - verify before use |
| Coconut Oil 99.5% Pharmazeutisch rein | IC-5961 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat | IC-6127 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat 99.5% | IC-5553 | PROVISIONAL | Historical - verify before use |
| Weizenklebereiweiß | IC-9300 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat Pharmazeutisch rein | IC-8699 | SUPERSEDED | Historical - verify before use |
| Soja Isolate 70% | IC-8574 | PROVISIONAL | Historical - verify before use |
| Soja Isolate 25% Technische Qualität | IC-7947 | SUPERSEDED | Historical - verify before use |
| Calcium Carbonate 25% | IC-7974 | REVIEW REQUIRED | Historical - verify before use |
| Fructose | IC-9878 | REVIEW REQUIRED | Historical - verify before use |
| Rapsöl | IC-8282 | DEPRECATED | Historical - verify before use |
| Resistente Stärke | IC-7418 | REVIEW REQUIRED | Historical - verify before use |
| Fructose | IC-7436 | PROVISIONAL | Historical - verify before use |
| Glukosesirup Syrup | IC-9490 | SUPERSEDED | Historical - verify before use |
| Resistente Stärke Pharmazeutisch rein | IC-8265 | REVIEW REQUIRED | Historical - verify before use |
| Kasein Standardqualität | IC-7450 | PROVISIONAL | Historical - verify before use |
| Calcium Carbonate 98% | IC-5049 | DEPRECATED | Historical - verify before use |
| Palmfett Standardqualität | IC-7671 | REVIEW REQUIRED | Historical - verify before use |
| Maltodextrin-Pulver DE5 Qualitätsstufe I | IC-5028 | DEPRECATED | Historical - verify before use |
| Rapsöl 70% Qualitätsstufe II | IC-7917 | SUPERSEDED | Historical - verify before use |
| Sorbinsäure Lebensmittelrein | IC-6008 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid | IC-7173 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil 25% Standardqualität | IC-7717 | SUPERSEDED | Historical - verify before use |
| Zitronensäure Pharmazeutisch rein | IC-6660 | DEPRECATED | Historical - verify before use |
| Sonnenblumenöl 50% Qualitätsstufe I | IC-9601 | SUPERSEDED | Historical - verify before use |
| Sorbinsäure 98% | IC-9198 | DEPRECATED | Historical - verify before use |
| Zitronensäure 50% Qualitätsstufe I | IC-9933 | DEPRECATED | Historical - verify before use |
| Dextrin | IC-5703 | PROVISIONAL | Historical - verify before use |
| Maltodextrin-Pulver DE20 | IC-9448 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat | IC-9418 | PROVISIONAL | Historical - verify before use |
| Traubenzucker 25% Technische Qualität | IC-8612 | DEPRECATED | Historical - verify before use |
| Lactic Acid Lebensmittelrein | IC-6121 | SUPERSEDED | Historical - verify before use |
| Sorbinsäure | IC-7616 | REVIEW REQUIRED | Historical - verify before use |
| Rapsöl Technische Qualität | IC-5684 | PROVISIONAL | Historical - verify before use |
| Dextrin Pharmazeutisch rein | IC-7573 | REVIEW REQUIRED | Historical - verify before use |
| Zitronensäure 99.5% | IC-9787 | PROVISIONAL | Historical - verify before use |
| Traubenzucker 25% | IC-7919 | DEPRECATED | Historical - verify before use |
| Traubenzucker | IC-5870 | SUPERSEDED | Historical - verify before use |
| Resistente Stärke Qualitätsstufe II | IC-9628 | SUPERSEDED | Historical - verify before use |
| Fructose 25% | IC-8835 | SUPERSEDED | Historical - verify before use |
| Calcium Carbonate 50% Qualitätsstufe II | IC-5323 | DEPRECATED | Historical - verify before use |
| Soja Isolate 25% | IC-8542 | SUPERSEDED | Historical - verify before use |
| Zitronensäure Qualitätsstufe II | IC-8368 | SUPERSEDED | Historical - verify before use |
| Pea Protein Qualitätsstufe I | IC-8823 | REVIEW REQUIRED | Historical - verify before use |
| Rapsöl 99.5% | IC-7650 | PROVISIONAL | Historical - verify before use |
| Glukosesirup Syrup 98% Lebensmittelrein | IC-8965 | PROVISIONAL | Historical - verify before use |
| Traubenzucker 99.5% Qualitätsstufe II | IC-6008 | SUPERSEDED | Historical - verify before use |
| Soja Isolate 25% Pharmazeutisch rein | IC-6823 | PROVISIONAL | Historical - verify before use |
| Soja Isolate | IC-7919 | SUPERSEDED | Historical - verify before use |
| Traubenzucker Qualitätsstufe I | IC-7515 | DEPRECATED | Historical - verify before use |
| Resistente Stärke Technische Qualität | IC-7830 | SUPERSEDED | Historical - verify before use |
| Dextrin 50% | IC-9040 | REVIEW REQUIRED | Historical - verify before use |
| Glukosesirup Syrup Technische Qualität | IC-6294 | SUPERSEDED | Historical - verify before use |
| Soja Isolate 99.5% Premiumqualität | IC-9337 | DEPRECATED | Historical - verify before use |
| Soja Isolate 98% | IC-7058 | REVIEW REQUIRED | Historical - verify before use |
| Dextrin | IC-7468 | SUPERSEDED | Historical - verify before use |
| Glukosesirup Syrup 70% | IC-9739 | REVIEW REQUIRED | Historical - verify before use |
| Sonnenblumenöl Qualitätsstufe II | IC-6347 | SUPERSEDED | Historical - verify before use |
| Sonnenblumenöl Standardqualität | IC-5246 | PROVISIONAL | Historical - verify before use |
| Ascorbic Acid 99.5% Premiumqualität | IC-8211 | SUPERSEDED | Historical - verify before use |
| Dextrin Technische Qualität | IC-6449 | DEPRECATED | Historical - verify before use |
| Palmfett | IC-6720 | SUPERSEDED | Historical - verify before use |
| Natriumbenzoat Qualitätsstufe I | IC-7855 | DEPRECATED | Historical - verify before use |
| Traubenzucker 25% | IC-8065 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat | IC-6508 | DEPRECATED | Historical - verify before use |
| Natriumbenzoat | IC-8228 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat 25% | IC-9352 | REVIEW REQUIRED | Historical - verify before use |
| Natriumchlorid 70% | IC-7399 | DEPRECATED | Historical - verify before use |
| Kasein Premiumqualität | IC-6550 | DEPRECATED | Historical - verify before use |
| Calcium Carbonate Standardqualität | IC-8491 | SUPERSEDED | Historical - verify before use |
| Natriumchlorid 99.5% | IC-7875 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid Technische Qualität | IC-6819 | SUPERSEDED | Historical - verify before use |
| Natriumchlorid | IC-6409 | REVIEW REQUIRED | Historical - verify before use |
| Dextrin Standardqualität | IC-6284 | PROVISIONAL | Historical - verify before use |
| Kasein | IC-5468 | REVIEW REQUIRED | Historical - verify before use |
| Isoglucose 70% | IC-8136 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid 50% Technische Qualität | IC-9666 | PROVISIONAL | Historical - verify before use |
| Traubenzucker Lebensmittelrein | IC-9490 | DEPRECATED | Historical - verify before use |
| Natriumbenzoat | IC-8585 | REVIEW REQUIRED | Historical - verify before use |
| Palmfett 50% | IC-8952 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid 98% Premiumqualität | IC-7547 | PROVISIONAL | Historical - verify before use |
| Sorbinsäure 70% | IC-8463 | PROVISIONAL | Historical - verify before use |
| Dextrin Lebensmittelrein | IC-5297 | SUPERSEDED | Historical - verify before use |
| Natriumchlorid Standardqualität | IC-5088 | PROVISIONAL | Historical - verify before use |
| Isoglucose Premiumqualität | IC-9661 | DEPRECATED | Historical - verify before use |
| Calcium Carbonate Qualitätsstufe II | IC-6235 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat | IC-6580 | PROVISIONAL | Historical - verify before use |
| Weizenklebereiweiß | IC-9353 | PROVISIONAL | Historical - verify before use |
| Zitronensäure | IC-7341 | PROVISIONAL | Historical - verify before use |
| Ascorbic Acid 70% | IC-8947 | PROVISIONAL | Historical - verify before use |
| Cyclodextrin | IC-6952 | REVIEW REQUIRED | Historical - verify before use |
| Traubenzucker 25% Technische Qualität | IC-5387 | REVIEW REQUIRED | Historical - verify before use |
| Isoglucose Lebensmittelrein | IC-9435 | SUPERSEDED | Historical - verify before use |
| Dextrin 70% | IC-6775 | PROVISIONAL | Historical - verify before use |
| Zitronensäure | IC-5972 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat 98% Standardqualität | IC-6251 | DEPRECATED | Historical - verify before use |
| Lactic Acid 98% Premiumqualität | IC-5938 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid Premiumqualität | IC-8134 | REVIEW REQUIRED | Historical - verify before use |
| Rapsöl Technische Qualität | IC-8017 | DEPRECATED | Historical - verify before use |
| Soja Isolate Qualitätsstufe I | IC-6211 | REVIEW REQUIRED | Historical - verify before use |
| Rapsöl | IC-5123 | REVIEW REQUIRED | Historical - verify before use |
| Calcium Carbonate | IC-9049 | DEPRECATED | Historical - verify before use |
| Natriumbenzoat 99.5% Technische Qualität | IC-8928 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat Qualitätsstufe II | IC-5649 | SUPERSEDED | Historical - verify before use |
| Palmfett | IC-7122 | DEPRECATED | Historical - verify before use |
| Calcium Carbonate 70% Premiumqualität | IC-9333 | PROVISIONAL | Historical - verify before use |
| Soja Isolate Premiumqualität | IC-6599 | REVIEW REQUIRED | Historical - verify before use |
| Palmfett Lebensmittelrein | IC-5974 | SUPERSEDED | Historical - verify before use |
| Weizenklebereiweiß Qualitätsstufe II | IC-5174 | PROVISIONAL | Historical - verify before use |
| Kasein Technische Qualität | IC-6949 | DEPRECATED | Historical - verify before use |
| Glukosesirup Syrup 98% | IC-6551 | PROVISIONAL | Historical - verify before use |
| Rapsöl 70% Premiumqualität | IC-5914 | PROVISIONAL | Historical - verify before use |
| Palmfett | IC-7012 | PROVISIONAL | Historical - verify before use |
| Zitronensäure | IC-9127 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid 70% Pharmazeutisch rein | IC-7483 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat Qualitätsstufe I | IC-8382 | REVIEW REQUIRED | Historical - verify before use |
| Natriumchlorid | IC-5674 | SUPERSEDED | Historical - verify before use |
| Fructose | IC-9799 | SUPERSEDED | Historical - verify before use |
| Natriumbenzoat Qualitätsstufe I | IC-8267 | DEPRECATED | Historical - verify before use |
| Fructose Qualitätsstufe II | IC-9542 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid | IC-8424 | SUPERSEDED | Historical - verify before use |
| Fructose | IC-6411 | PROVISIONAL | Historical - verify before use |
| Glukosesirup Syrup 98% Qualitätsstufe I | IC-6786 | PROVISIONAL | Historical - verify before use |
| Rapsöl 98% | IC-5467 | PROVISIONAL | Historical - verify before use |
| Kasein | IC-8959 | REVIEW REQUIRED | Historical - verify before use |
| Rapsöl Qualitätsstufe I | IC-7699 | PROVISIONAL | Historical - verify before use |
| Pea Protein 98% Qualitätsstufe II | IC-5796 | REVIEW REQUIRED | Historical - verify before use |
| Calcium Carbonate | IC-5608 | PROVISIONAL | Historical - verify before use |
| Glukosesirup Syrup 70% | IC-9916 | PROVISIONAL | Historical - verify before use |
| Traubenzucker Qualitätsstufe I | IC-9127 | SUPERSEDED | Historical - verify before use |
| Lactic Acid | IC-8089 | DEPRECATED | Historical - verify before use |
| Kaliumsorbat | IC-8290 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid Technische Qualität | IC-9860 | REVIEW REQUIRED | Historical - verify before use |
| Isoglucose 70% Lebensmittelrein | IC-6657 | REVIEW REQUIRED | Historical - verify before use |
| Traubenzucker 25% | IC-7311 | DEPRECATED | Historical - verify before use |
| Traubenzucker Qualitätsstufe II | IC-8305 | DEPRECATED | Historical - verify before use |
| Sorbinsäure Qualitätsstufe II | IC-9291 | DEPRECATED | Historical - verify before use |
| Resistente Stärke Qualitätsstufe II | IC-5195 | DEPRECATED | Historical - verify before use |
| Lactic Acid Qualitätsstufe I | IC-9139 | REVIEW REQUIRED | Historical - verify before use |
| Dextrin Qualitätsstufe I | IC-8140 | REVIEW REQUIRED | Historical - verify before use |
| Natriumchlorid 98% | IC-6985 | SUPERSEDED | Historical - verify before use |
| Natriumchlorid | IC-6325 | DEPRECATED | Historical - verify before use |
| Pea Protein 25% Pharmazeutisch rein | IC-8753 | REVIEW REQUIRED | Historical - verify before use |
| Maltodextrin-Pulver DE10 Premiumqualität | IC-8210 | REVIEW REQUIRED | Historical - verify before use |
| Maltodextrin-Pulver DE20 | IC-9409 | DEPRECATED | Historical - verify before use |
| Fructose Qualitätsstufe I | IC-7380 | DEPRECATED | Historical - verify before use |
| Glukosesirup Syrup | IC-8421 | PROVISIONAL | Historical - verify before use |
| Isoglucose | IC-7012 | DEPRECATED | Historical - verify before use |
| Soja Isolate | IC-6295 | REVIEW REQUIRED | Historical - verify before use |
| Calcium Carbonate 98% Standardqualität | IC-9488 | REVIEW REQUIRED | Historical - verify before use |
| Resistente Stärke | IC-5153 | SUPERSEDED | Historical - verify before use |
| Kaliumsorbat Standardqualität | IC-9682 | SUPERSEDED | Historical - verify before use |
| Zitronensäure | IC-8480 | PROVISIONAL | Historical - verify before use |
| Lactic Acid Lebensmittelrein | IC-8457 | SUPERSEDED | Historical - verify before use |
| Zitronensäure 25% Technische Qualität | IC-6797 | DEPRECATED | Historical - verify before use |
| Dextrin 50% | IC-7065 | REVIEW REQUIRED | Historical - verify before use |
| Isoglucose | IC-8906 | DEPRECATED | Historical - verify before use |
| Soja Isolate 50% Qualitätsstufe II | IC-7723 | DEPRECATED | Historical - verify before use |
| Rapsöl | IC-5812 | PROVISIONAL | Historical - verify before use |
| Maltodextrin-Pulver DE18 Pharmazeutisch rein | IC-7220 | REVIEW REQUIRED | Historical - verify before use |
| Rapsöl Qualitätsstufe I | IC-8418 | DEPRECATED | Historical - verify before use |
| Traubenzucker 70% Qualitätsstufe I | IC-5167 | DEPRECATED | Historical - verify before use |
| Calcium Carbonate 50% Pharmazeutisch rein | IC-7061 | DEPRECATED | Historical - verify before use |
| Natriumbenzoat 25% Qualitätsstufe II | IC-9901 | DEPRECATED | Historical - verify before use |
| Rapsöl 99.5% Technische Qualität | IC-5594 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat 98% Qualitätsstufe II | IC-6755 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat 50% | IC-7665 | PROVISIONAL | Historical - verify before use |
| Coconut Oil | IC-6520 | REVIEW REQUIRED | Historical - verify before use |
| Fructose | IC-9842 | PROVISIONAL | Historical - verify before use |
| Sorbinsäure 50% Standardqualität | IC-8204 | DEPRECATED | Historical - verify before use |
| Rapsöl 99.5% | IC-9138 | REVIEW REQUIRED | Historical - verify before use |
| Zitronensäure | IC-7852 | PROVISIONAL | Historical - verify before use |
| Natriumchlorid Technische Qualität | IC-6996 | PROVISIONAL | Historical - verify before use |
| Kaliumsorbat | IC-5682 | PROVISIONAL | Historical - verify before use |
| Dextrin Premiumqualität | IC-5366 | REVIEW REQUIRED | Historical - verify before use |
| Zitronensäure 70% | IC-8404 | PROVISIONAL | Historical - verify before use |
| Maltodextrin-Pulver DE25 | IC-7373 | DEPRECATED | Historical - verify before use |
| Maltodextrin-Pulver DE10 | IC-8451 | PROVISIONAL | Historical - verify before use |
| Dextrin 70% | IC-9077 | DEPRECATED | Historical - verify before use |
| Lactic Acid Lebensmittelrein | IC-7327 | PROVISIONAL | Historical - verify before use |
| Ascorbic Acid 98% Pharmazeutisch rein | IC-9883 | PROVISIONAL | Historical - verify before use |
| Natriumchlorid 70% | IC-5016 | SUPERSEDED | Historical - verify before use |
| Fructose Technische Qualität | IC-9355 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid | IC-5314 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid | IC-5880 | DEPRECATED | Historical - verify before use |
| Coconut Oil 98% Lebensmittelrein | IC-9019 | PROVISIONAL | Historical - verify before use |
| Kaliumsorbat Technische Qualität | IC-5465 | DEPRECATED | Historical - verify before use |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | IC-5096 | REVIEW REQUIRED | Historical - verify before use |
| Soja Isolate 98% Premiumqualität | IC-5997 | SUPERSEDED | Historical - verify before use |
| Lactic Acid 99.5% | IC-9667 | REVIEW REQUIRED | Historical - verify before use |
| Glukosesirup Syrup | IC-5106 | SUPERSEDED | Historical - verify before use |
| Maltodextrin-Pulver DE25 | IC-8807 | DEPRECATED | Historical - verify before use |
| Calcium Carbonate Qualitätsstufe II | IC-5416 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid Lebensmittelrein | IC-6924 | SUPERSEDED | Historical - verify before use |
| Kasein 98% Qualitätsstufe II | IC-6655 | PROVISIONAL | Historical - verify before use |
| Resistente Stärke Technische Qualität | IC-6447 | SUPERSEDED | Historical - verify before use |
| Resistente Stärke Technische Qualität | IC-6139 | DEPRECATED | Historical - verify before use |
| Kasein Qualitätsstufe I | IC-9108 | REVIEW REQUIRED | Historical - verify before use |
| Palmfett Qualitätsstufe II | IC-6635 | SUPERSEDED | Historical - verify before use |
| Maltodextrin-Pulver DE25 | IC-8277 | SUPERSEDED | Historical - verify before use |
| Soja Isolate Standardqualität | IC-7913 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat 50% Technische Qualität | IC-8945 | DEPRECATED | Historical - verify before use |
| Traubenzucker 50% | IC-9673 | SUPERSEDED | Historical - verify before use |
| Resistente Stärke 70% Technische Qualität | IC-5828 | DEPRECATED | Historical - verify before use |
| Glukosesirup Syrup Lebensmittelrein | IC-7323 | PROVISIONAL | Historical - verify before use |
| Pea Protein Premiumqualität | IC-7862 | DEPRECATED | Historical - verify before use |
| Weizenklebereiweiß 98% | IC-7509 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat Qualitätsstufe II | IC-9949 | REVIEW REQUIRED | Historical - verify before use |
| Zitronensäure 70% Lebensmittelrein | IC-7698 | PROVISIONAL | Historical - verify before use |
| Natriumchlorid 98% Standardqualität | IC-6696 | DEPRECATED | Historical - verify before use |
| Natriumbenzoat 50% | IC-6574 | DEPRECATED | Historical - verify before use |
| Lactic Acid 50% Premiumqualität | IC-6928 | REVIEW REQUIRED | Historical - verify before use |
| Kasein 98% Technische Qualität | IC-8391 | DEPRECATED | Historical - verify before use |
| Sorbinsäure | IC-9340 | SUPERSEDED | Historical - verify before use |
| Rapsöl 50% Lebensmittelrein | IC-5958 | DEPRECATED | Historical - verify before use |
| Resistente Stärke 98% | IC-9612 | REVIEW REQUIRED | Historical - verify before use |
| Fructose 99.5% Lebensmittelrein | IC-8878 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid Standardqualität | IC-5691 | SUPERSEDED | Historical - verify before use |
| Resistente Stärke Technische Qualität | IC-7326 | SUPERSEDED | Historical - verify before use |
| Weizenklebereiweiß 99.5% Qualitätsstufe I | IC-5361 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat 99.5% Technische Qualität | IC-9564 | SUPERSEDED | Historical - verify before use |
| Natriumbenzoat 99.5% Qualitätsstufe I | IC-9625 | DEPRECATED | Historical - verify before use |
| Maltodextrin-Pulver DE10 | IC-8541 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid 50% | IC-6137 | REVIEW REQUIRED | Historical - verify before use |
| Traubenzucker Qualitätsstufe I | IC-6644 | PROVISIONAL | Historical - verify before use |
| Kaliumsorbat 50% Technische Qualität | IC-5481 | SUPERSEDED | Historical - verify before use |
| Coconut Oil 70% Qualitätsstufe I | IC-7368 | SUPERSEDED | Historical - verify before use |
| Kaliumsorbat 98% | IC-7644 | REVIEW REQUIRED | Historical - verify before use |
| Resistente Stärke 70% Lebensmittelrein | IC-7327 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid | IC-9294 | PROVISIONAL | Historical - verify before use |
| Glukosesirup Syrup | IC-8669 | SUPERSEDED | Historical - verify before use |
| Calcium Carbonate 99.5% | IC-7817 | DEPRECATED | Historical - verify before use |
| Palmfett 70% Premiumqualität | IC-7554 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid Qualitätsstufe II | IC-5053 | SUPERSEDED | Historical - verify before use |
| Lactic Acid 98% | IC-9381 | DEPRECATED | Historical - verify before use |
| Kaliumsorbat | IC-9851 | REVIEW REQUIRED | Historical - verify before use |
| Pea Protein Premiumqualität | IC-5392 | SUPERSEDED | Historical - verify before use |
| Coconut Oil 98% Technische Qualität | IC-9553 | PROVISIONAL | Historical - verify before use |
| Coconut Oil 98% | IC-7804 | DEPRECATED | Historical - verify before use |
| Traubenzucker | IC-5357 | DEPRECATED | Historical - verify before use |
| Natriumchlorid | IC-7037 | DEPRECATED | Historical - verify before use |
| Coconut Oil 25% Technische Qualität | IC-8960 | SUPERSEDED | Historical - verify before use |
| Lactic Acid 98% Qualitätsstufe I | IC-9278 | PROVISIONAL | Historical - verify before use |
| Calcium Carbonate 70% | IC-9037 | DEPRECATED | Historical - verify before use |
| Palmfett 99.5% Qualitätsstufe I | IC-5492 | PROVISIONAL | Historical - verify before use |
| Resistente Stärke 50% | IC-7822 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid Pharmazeutisch rein | IC-8811 | PROVISIONAL | Historical - verify before use |
| Resistente Stärke Lebensmittelrein | IC-9905 | PROVISIONAL | Historical - verify before use |
| Sorbinsäure 70% | IC-8864 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat Lebensmittelrein | IC-7074 | REVIEW REQUIRED | Historical - verify before use |
| Weizenklebereiweiß | IC-5591 | REVIEW REQUIRED | Historical - verify before use |
| Sorbinsäure Standardqualität | IC-6885 | SUPERSEDED | Historical - verify before use |
| Weizenklebereiweiß Lebensmittelrein | IC-8756 | SUPERSEDED | Historical - verify before use |
| Traubenzucker Qualitätsstufe II | IC-5747 | SUPERSEDED | Historical - verify before use |
| Pea Protein | IC-9663 | SUPERSEDED | Historical - verify before use |
| Calcium Carbonate 98% | IC-5126 | SUPERSEDED | Historical - verify before use |
| Kasein Qualitätsstufe II | IC-6113 | SUPERSEDED | Historical - verify before use |
| Weizenklebereiweiß Lebensmittelrein | IC-8781 | DEPRECATED | Historical - verify before use |
| Zitronensäure Premiumqualität | IC-5049 | SUPERSEDED | Historical - verify before use |
| Natriumchlorid 25% | IC-6688 | DEPRECATED | Historical - verify before use |


#### 4.3.4 Excluded Assignments

Deprecated code assignments (superseded by newer records):

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-1669-E | Data quality insufficient | Manual review scheduled |
| NOISE-5264-D | Out of scope per business decision | Escalated to data steward |
| NOISE-3903-G | Duplicate source record | Manual review scheduled |
| NOISE-5743-G | Pending validation | Deferred to Phase 2 |
| NOISE-3710-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-6233-G | Missing required attributes | Business owner notified |
| NOISE-8420-H | Pending validation | Escalated to data steward |
| NOISE-8520-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-2312-E | Duplicate source record | Manual review scheduled |
| NOISE-4982-F | Pending validation | Manual review scheduled |
| NOISE-8462-G | Missing required attributes | Escalated to data steward |
| NOISE-1539-D | Pending validation | Escalated to data steward |
| NOISE-3671-D | Data quality insufficient | Manual review scheduled |
| NOISE-4008-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-7540-G | Data quality insufficient | Business owner notified |
| NOISE-2981-A | Pending validation | Escalated to data steward |
| NOISE-4338-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4913-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4054-B | Pending validation | Manual review scheduled |
| NOISE-3588-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-4111-H | Pending validation | Manual review scheduled |
| NOISE-3628-E | Missing required attributes | Business owner notified |
| NOISE-9207-H | Missing required attributes | Business owner notified |
| NOISE-2934-A | Duplicate source record | Business owner notified |
| NOISE-1639-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4120-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-8959-E | Pending validation | Escalated to data steward |
| NOISE-6810-C | Data quality insufficient | Manual review scheduled |
| NOISE-4018-B | Missing required attributes | Escalated to data steward |
| NOISE-7845-H | Missing required attributes | Manual review scheduled |
| NOISE-8222-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-4860-B | Out of scope per business decision | Manual review scheduled |
| NOISE-6643-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-5157-D | Data quality insufficient | Escalated to data steward |
| NOISE-7832-C | Data quality insufficient | Manual review scheduled |
| NOISE-8368-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5429-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1985-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-4588-C | Data quality insufficient | Business owner notified |
| NOISE-7625-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8063-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-3723-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7916-F | Duplicate source record | Business owner notified |
| NOISE-1751-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7425-E | Pending validation | Escalated to data steward |
| NOISE-4112-H | Out of scope per business decision | Escalated to data steward |
| NOISE-2346-E | Out of scope per business decision | Escalated to data steward |
| NOISE-2345-F | Duplicate source record | Manual review scheduled |
| NOISE-2267-D | Missing required attributes | Manual review scheduled |
| NOISE-4431-H | Pending validation | Escalated to data steward |
| NOISE-9317-A | Missing required attributes | Escalated to data steward |
| NOISE-9774-E | Pending validation | Manual review scheduled |
| NOISE-8483-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-3996-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-7720-F | Missing required attributes | Business owner notified |
| NOISE-7897-D | Out of scope per business decision | Manual review scheduled |
| NOISE-3919-A | Data quality insufficient | Business owner notified |
| NOISE-1247-B | Duplicate source record | Manual review scheduled |
| NOISE-8710-F | Duplicate source record | Business owner notified |
| NOISE-4314-H | Data quality insufficient | Escalated to data steward |
| NOISE-5445-A | Duplicate source record | Business owner notified |
| NOISE-9075-B | Data quality insufficient | Business owner notified |
| NOISE-7609-F | Missing required attributes | Manual review scheduled |
| NOISE-6349-H | Missing required attributes | Escalated to data steward |
| NOISE-9557-H | Pending validation | Manual review scheduled |
| NOISE-5409-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8665-B | Data quality insufficient | Business owner notified |
| NOISE-3005-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4508-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-3721-E | Missing required attributes | Escalated to data steward |
| NOISE-6271-B | Pending validation | Escalated to data steward |
| NOISE-9708-F | Pending validation | Business owner notified |
| NOISE-8545-H | Duplicate source record | Escalated to data steward |
| NOISE-8319-F | Out of scope per business decision | Business owner notified |
| NOISE-1688-F | Duplicate source record | Escalated to data steward |
| NOISE-7979-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5917-F | Pending validation | Business owner notified |
| NOISE-4452-F | Data quality insufficient | Escalated to data steward |
| NOISE-6869-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-6720-B | Missing required attributes | Manual review scheduled |
| NOISE-9895-G | Duplicate source record | Business owner notified |
| NOISE-2511-E | Pending validation | Manual review scheduled |
| NOISE-7912-A | Duplicate source record | Escalated to data steward |
| NOISE-2583-H | Missing required attributes | Escalated to data steward |
| NOISE-3659-E | Duplicate source record | Business owner notified |
| NOISE-1293-G | Data quality insufficient | Manual review scheduled |
| NOISE-8126-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2847-A | Duplicate source record | Manual review scheduled |
| NOISE-9636-F | Out of scope per business decision | Escalated to data steward |
| NOISE-6176-H | Duplicate source record | Business owner notified |
| NOISE-1935-F | Duplicate source record | Manual review scheduled |
| NOISE-7972-E | Duplicate source record | Manual review scheduled |
| NOISE-3282-E | Pending validation | Deferred to Phase 2 |
| NOISE-5209-H | Pending validation | Manual review scheduled |
| NOISE-2763-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3031-A | Missing required attributes | Manual review scheduled |
| NOISE-4914-C | Data quality insufficient | Manual review scheduled |
| NOISE-4267-E | Out of scope per business decision | Escalated to data steward |
| NOISE-8814-A | Out of scope per business decision | Manual review scheduled |
| NOISE-7686-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-7896-F | Pending validation | Escalated to data steward |
| NOISE-9177-H | Duplicate source record | Deferred to Phase 2 |
| NOISE-8998-C | Duplicate source record | Manual review scheduled |
| NOISE-9498-E | Duplicate source record | Business owner notified |
| NOISE-5454-E | Data quality insufficient | Business owner notified |
| NOISE-5704-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-9093-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3163-E | Data quality insufficient | Business owner notified |
| NOISE-8080-F | Duplicate source record | Manual review scheduled |
| NOISE-6486-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9670-F | Pending validation | Deferred to Phase 2 |
| NOISE-8511-E | Missing required attributes | Escalated to data steward |
| NOISE-8120-F | Missing required attributes | Manual review scheduled |
| NOISE-7481-H | Pending validation | Business owner notified |
| NOISE-4487-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-6338-H | Data quality insufficient | Manual review scheduled |
| NOISE-4541-A | Out of scope per business decision | Manual review scheduled |
| NOISE-8924-E | Pending validation | Escalated to data steward |
| NOISE-2605-F | Pending validation | Deferred to Phase 2 |
| NOISE-1055-C | Missing required attributes | Manual review scheduled |
| NOISE-3500-F | Pending validation | Manual review scheduled |
| NOISE-7321-B | Data quality insufficient | Escalated to data steward |
| NOISE-4308-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9883-D | Duplicate source record | Manual review scheduled |
| NOISE-7460-B | Data quality insufficient | Escalated to data steward |
| NOISE-7318-D | Duplicate source record | Manual review scheduled |
| NOISE-8296-A | Data quality insufficient | Business owner notified |
| NOISE-7474-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1692-G | Out of scope per business decision | Escalated to data steward |
| NOISE-7681-C | Missing required attributes | Business owner notified |
| NOISE-4601-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-2487-C | Duplicate source record | Escalated to data steward |
| NOISE-7798-F | Pending validation | Escalated to data steward |
| NOISE-4310-D | Pending validation | Manual review scheduled |
| NOISE-3967-H | Out of scope per business decision | Business owner notified |
| NOISE-6236-C | Out of scope per business decision | Escalated to data steward |
| NOISE-9408-B | Pending validation | Business owner notified |
| NOISE-6876-H | Missing required attributes | Business owner notified |
| NOISE-3254-H | Data quality insufficient | Business owner notified |
| NOISE-8130-E | Duplicate source record | Business owner notified |
| NOISE-9078-B | Missing required attributes | Escalated to data steward |
| NOISE-2877-B | Duplicate source record | Escalated to data steward |
| NOISE-5406-E | Missing required attributes | Manual review scheduled |
| NOISE-7210-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-9224-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5145-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-5592-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8676-A | Duplicate source record | Manual review scheduled |
| NOISE-2894-C | Data quality insufficient | Business owner notified |
| NOISE-2979-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4964-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-9141-F | Duplicate source record | Business owner notified |
| NOISE-2073-D | Missing required attributes | Business owner notified |
| NOISE-8553-B | Out of scope per business decision | Manual review scheduled |
| NOISE-8204-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-5810-H | Pending validation | Manual review scheduled |
| NOISE-8788-E | Pending validation | Deferred to Phase 2 |
| NOISE-3655-C | Duplicate source record | Escalated to data steward |
| NOISE-2241-B | Duplicate source record | Escalated to data steward |
| NOISE-4198-D | Duplicate source record | Escalated to data steward |
| NOISE-8557-F | Data quality insufficient | Escalated to data steward |
| NOISE-3598-A | Pending validation | Escalated to data steward |
| NOISE-6985-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3779-E | Missing required attributes | Escalated to data steward |
| NOISE-7331-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4605-E | Duplicate source record | Manual review scheduled |
| NOISE-8419-E | Missing required attributes | Escalated to data steward |
| NOISE-2893-E | Missing required attributes | Escalated to data steward |
| NOISE-2173-G | Out of scope per business decision | Escalated to data steward |
| NOISE-8759-D | Pending validation | Business owner notified |
| NOISE-5029-E | Duplicate source record | Business owner notified |
| NOISE-9342-D | Pending validation | Manual review scheduled |
| NOISE-1189-A | Data quality insufficient | Escalated to data steward |
| NOISE-7785-C | Missing required attributes | Manual review scheduled |
| NOISE-2576-A | Duplicate source record | Escalated to data steward |
| NOISE-7894-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3060-B | Duplicate source record | Business owner notified |
| NOISE-5542-C | Missing required attributes | Business owner notified |
| NOISE-3785-B | Pending validation | Business owner notified |
| NOISE-6588-D | Pending validation | Deferred to Phase 2 |
| NOISE-3413-A | Out of scope per business decision | Business owner notified |
| NOISE-3116-H | Duplicate source record | Business owner notified |
| NOISE-1089-F | Duplicate source record | Manual review scheduled |
| NOISE-9995-A | Out of scope per business decision | Escalated to data steward |
| NOISE-7766-G | Data quality insufficient | Manual review scheduled |
| NOISE-3283-B | Out of scope per business decision | Escalated to data steward |
| NOISE-6879-G | Out of scope per business decision | Business owner notified |
| NOISE-6448-A | Duplicate source record | Escalated to data steward |
| NOISE-5529-E | Missing required attributes | Business owner notified |
| NOISE-6140-H | Pending validation | Business owner notified |
| NOISE-1177-E | Missing required attributes | Manual review scheduled |
| NOISE-4229-B | Pending validation | Business owner notified |
| NOISE-3699-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3193-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-8901-C | Pending validation | Deferred to Phase 2 |
| NOISE-3604-C | Out of scope per business decision | Business owner notified |
| NOISE-7948-E | Out of scope per business decision | Escalated to data steward |
| NOISE-7899-B | Data quality insufficient | Manual review scheduled |
| NOISE-2458-A | Missing required attributes | Escalated to data steward |
| NOISE-9373-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2008-E | Duplicate source record | Manual review scheduled |
| NOISE-2797-B | Out of scope per business decision | Manual review scheduled |
| NOISE-6244-A | Missing required attributes | Manual review scheduled |
| NOISE-2688-D | Data quality insufficient | Business owner notified |
| NOISE-3818-C | Pending validation | Business owner notified |
| NOISE-4313-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4620-F | Out of scope per business decision | Escalated to data steward |
| NOISE-4777-F | Data quality insufficient | Business owner notified |
| NOISE-2670-E | Missing required attributes | Escalated to data steward |
| NOISE-9441-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6605-D | Duplicate source record | Manual review scheduled |
| NOISE-4784-G | Pending validation | Deferred to Phase 2 |
| NOISE-5814-B | Duplicate source record | Manual review scheduled |
| NOISE-5494-F | Out of scope per business decision | Manual review scheduled |
| NOISE-2492-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6541-H | Data quality insufficient | Business owner notified |
| NOISE-6254-B | Pending validation | Business owner notified |
| NOISE-4275-E | Pending validation | Manual review scheduled |
| NOISE-3175-C | Data quality insufficient | Business owner notified |
| NOISE-1763-G | Pending validation | Business owner notified |
| NOISE-8675-F | Data quality insufficient | Escalated to data steward |
| NOISE-7573-F | Duplicate source record | Manual review scheduled |
| NOISE-6958-D | Missing required attributes | Escalated to data steward |
| NOISE-5069-F | Duplicate source record | Business owner notified |
| NOISE-6673-D | Missing required attributes | Escalated to data steward |
| NOISE-1766-C | Missing required attributes | Manual review scheduled |
| NOISE-3242-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4759-A | Pending validation | Deferred to Phase 2 |
| NOISE-8762-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-8262-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-4305-A | Pending validation | Deferred to Phase 2 |
| NOISE-8636-D | Duplicate source record | Manual review scheduled |
| NOISE-4166-C | Missing required attributes | Manual review scheduled |
| NOISE-1786-F | Out of scope per business decision | Manual review scheduled |
| NOISE-5048-H | Duplicate source record | Deferred to Phase 2 |
| NOISE-6507-H | Out of scope per business decision | Business owner notified |
| NOISE-1640-G | Out of scope per business decision | Escalated to data steward |
| NOISE-3445-A | Missing required attributes | Escalated to data steward |
| NOISE-3169-F | Missing required attributes | Business owner notified |
| NOISE-9260-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5755-D | Data quality insufficient | Escalated to data steward |
| NOISE-7725-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2591-A | Pending validation | Deferred to Phase 2 |
| NOISE-3982-A | Data quality insufficient | Business owner notified |
| NOISE-2280-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8770-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1024-F | Missing required attributes | Escalated to data steward |
| NOISE-3091-F | Out of scope per business decision | Business owner notified |
| NOISE-7689-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-3042-E | Duplicate source record | Escalated to data steward |
| NOISE-2846-A | Out of scope per business decision | Manual review scheduled |
| NOISE-8372-D | Missing required attributes | Escalated to data steward |
| NOISE-2126-F | Pending validation | Manual review scheduled |
| NOISE-2638-G | Data quality insufficient | Escalated to data steward |
| NOISE-2205-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6496-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9785-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-3989-H | Pending validation | Escalated to data steward |
| NOISE-3030-F | Missing required attributes | Escalated to data steward |
| NOISE-4713-C | Missing required attributes | Manual review scheduled |
| NOISE-5873-G | Out of scope per business decision | Escalated to data steward |
| NOISE-2966-B | Pending validation | Manual review scheduled |
| NOISE-9955-H | Out of scope per business decision | Manual review scheduled |
| NOISE-2769-F | Pending validation | Manual review scheduled |
| NOISE-6215-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-2238-E | Missing required attributes | Business owner notified |
| NOISE-9355-A | Data quality insufficient | Business owner notified |
| NOISE-9866-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1681-C | Duplicate source record | Business owner notified |
| NOISE-8251-F | Data quality insufficient | Escalated to data steward |
| NOISE-6392-G | Duplicate source record | Manual review scheduled |
| NOISE-5262-D | Data quality insufficient | Manual review scheduled |
| NOISE-1199-B | Out of scope per business decision | Escalated to data steward |
| NOISE-2554-C | Pending validation | Manual review scheduled |
| NOISE-5054-E | Data quality insufficient | Manual review scheduled |
| NOISE-2933-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2145-D | Duplicate source record | Business owner notified |
| NOISE-1450-C | Out of scope per business decision | Escalated to data steward |
| NOISE-6989-G | Duplicate source record | Manual review scheduled |


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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230610_000000`
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
| Project Lead | David Kim (Project Management) | david@company.com | +1-555-0101 |
| Technical Lead | John Smith (IT Infrastructure) | john@company.com | +1-555-0102 |
| Business Owner | Michael Weber (Business Operations) | michael@company.com | +1-555-0103 |
| Data Steward | Anna Mueller (EU Compliance) | anna@company.com | +1-555-0104 |

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
