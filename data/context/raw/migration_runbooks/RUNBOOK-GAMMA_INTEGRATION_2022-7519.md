# Migration Runbook: ERP Gamma Acquisition Integration

**Document ID**: RB-GAMMA_INTEGRATION_2022-8425
**Version**: 2.4
**Last Updated**: 2023-04-24
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the ERP Gamma Acquisition Integration project.
The migration involves transitioning master data and transactional records from ERP_GAMMA
to ERP_ALPHA while maintaining data integrity and business continuity.

**Project Timeline**: 2023-01-10 to 2023-05-16
**Business Sponsor**: Corporate Development
**Technical Owner**: M&A Integration Team

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
|   ERP_GAMMA       |     |   Staging Layer  |     |   ERP_ALPHA       |
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
ERP_GAMMA. Each source entity is assigned an internal staging code for
tracking purposes.

**IMPORTANT**: This document only contains source-to-staging assignments.
Target system mappings are maintained separately in the MDM Registry.

### 4.2 Assignment Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1440 | Completed |
| Codes assigned | 972 | Staged |
| Excluded from scope | 291 | Documented |
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

| Source Entity (ERP_GAMMA) | Internal Code | Assignment Date | Department |
|--------------------------------|---------------|-----------------|------------|
| SO-CH-70-GR-B-821 | BC-1002 | 2022-10-09 | Product Management |
| FR-GR-A-600 | BC-1007 | 2021-09-24 | Supply Chain |
| RE-ST-223 | IC-1011 | 2021-03-21 | Product Management |
| AS-AC-782 | IC-1025 | 2022-01-13 | Operations |
| SU-OI-98-PR-692 | TC-1036 | 2022-06-19 | Data Governance |
| CY-763 | BC-1045 | 2023-06-13 | Product Management |
| PE-PR-99.5-863 | BC-1048 | 2023-04-22 | Data Governance |
| AS-AC-GR-B-395 | IC-1055 | 2022-07-14 | IT Infrastructure |
| LA-AC-690 | TC-1061 | 2021-04-21 | IT Infrastructure |
| AS-AC-PH-GR-192 | TC-1075 | 2023-04-10 | Data Governance |
| CO-OI-FO-GR-162 | TC-1082 | 2024-01-08 | Operations |
| RA-OI-258 | BC-1096 | 2023-08-11 | Product Management |
| SO-BE-25-ST-520 | BC-1113 | 2023-07-01 | Operations |
| CO-OI-966 | IC-1119 | 2023-01-13 | Data Governance |
| CO-OI-98-890 | IC-1125 | 2023-11-01 | Operations |
| SO-BE-99.5-GR-A-143 | TC-1133 | 2023-05-19 | Operations |
| SO-BE-99.5-ST-342 | IC-1139 | 2023-09-22 | Finance |
| CY-98-PH-GR-614 | BC-1145 | 2023-04-11 | Operations |
| CO-OI-GR-A-370 | BC-1152 | 2021-12-03 | Operations |
| SO-AC-PH-GR-274 | TC-1159 | 2021-10-05 | IT Infrastructure |
| DE-ST-385 | BC-1163 | 2021-06-18 | Compliance |
| LA-AC-99.5-GR-B-756 | BC-1171 | 2021-07-28 | Supply Chain |
| LA-AC-393 | TC-1176 | 2023-02-26 | Product Management |
| PO-SO-560 | TC-1187 | 2022-09-08 | Compliance |
| SO-BE-99.5-195 | IC-1194 | 2021-11-25 | Product Management |
| SO-BE-PH-GR-647 | TC-1209 | 2024-11-08 | Product Management |
| PA-OI-50-PR-573 | BC-1212 | 2023-10-16 | Supply Chain |
| IS-878 | TC-1220 | 2021-07-27 | IT Infrastructure |
| SO-IS-25-TE-320 | TC-1235 | 2024-07-15 | Operations |
| FR-108 | BC-1244 | 2022-05-28 | Finance |
| RA-OI-745 | TC-1251 | 2022-01-09 | IT Infrastructure |
| RE-ST-463 | IC-1258 | 2022-06-09 | Product Management |
| FR-278 | IC-1265 | 2023-06-01 | IT Infrastructure |
| GL-SY-371 | TC-1269 | 2024-01-03 | Data Governance |
| SO-AC-25-GR-B-198 | TC-1274 | 2022-06-20 | IT Infrastructure |
| CA-ST-375 | TC-1285 | 2021-06-21 | IT Infrastructure |
| CA-CA-98-785 | IC-1295 | 2023-05-08 | Finance |
| PA-OI-ST-879 | BC-1303 | 2024-06-19 | Operations |
| MA-DE-GR-A-871 | TC-1308 | 2022-07-21 | Data Governance |
| SO-AC-FO-GR-175 | BC-1318 | 2022-01-26 | Operations |
| LA-AC-98-226 | BC-1325 | 2021-04-24 | IT Infrastructure |
| AS-AC-279 | IC-1328 | 2024-08-28 | Finance |
| CO-OI-25-ST-613 | TC-1334 | 2021-11-05 | Compliance |
| CI-AC-634 | TC-1341 | 2021-02-01 | Data Governance |
| CI-AC-PH-GR-209 | IC-1347 | 2021-01-26 | Data Governance |
| LA-AC-GR-A-486 | IC-1359 | 2021-07-15 | Product Management |
| PA-OI-98-587 | BC-1363 | 2022-02-11 | Finance |
| SU-OI-50-GR-A-521 | BC-1368 | 2024-03-15 | Supply Chain |
| SO-AC-98-741 | TC-1379 | 2021-03-10 | Operations |
| RE-ST-98-PH-GR-372 | BC-1388 | 2022-05-22 | Finance |
| DE-635 | TC-1396 | 2021-04-17 | Data Governance |
| MA-DE-641 | IC-1402 | 2022-05-05 | Data Governance |
| DE-25-TE-737 | IC-1414 | 2021-11-21 | Finance |
| LA-AC-FO-GR-553 | BC-1420 | 2024-09-20 | Compliance |
| SO-AC-852 | BC-1425 | 2023-04-28 | Operations |
| DE-PH-GR-282 | IC-1438 | 2021-08-04 | Finance |
| CI-AC-99.5-638 | IC-1443 | 2022-10-02 | Finance |
| SO-BE-PR-691 | TC-1450 | 2022-02-07 | Operations |
| DE-515 | IC-1457 | 2021-10-20 | Operations |
| CO-OI-ST-153 | TC-1466 | 2023-11-25 | Compliance |
| CI-AC-99.5-440 | IC-1471 | 2023-12-17 | Finance |
| RE-ST-GR-B-598 | BC-1478 | 2021-08-20 | Compliance |
| CA-CA-50-GR-B-200 | IC-1491 | 2022-10-14 | Supply Chain |
| SO-IS-25-323 | IC-1495 | 2021-02-18 | IT Infrastructure |
| RA-OI-99.5-602 | BC-1514 | 2023-07-04 | Supply Chain |
| GL-SY-98-FO-GR-198 | IC-1522 | 2021-06-28 | Product Management |
| SO-IS-25-PH-GR-832 | BC-1530 | 2021-01-18 | Supply Chain |
| DE-GR-A-250 | IC-1537 | 2022-06-01 | Compliance |
| SO-CH-GR-A-776 | BC-1541 | 2023-05-02 | Operations |
| CO-OI-98-GR-A-763 | IC-1546 | 2021-03-28 | IT Infrastructure |
| RE-ST-TE-614 | IC-1548 | 2021-11-16 | Data Governance |
| DE-50-891 | BC-1555 | 2021-05-20 | Supply Chain |
| SO-CH-98-GR-B-961 | BC-1564 | 2022-08-18 | Finance |
| GL-SY-TE-803 | BC-1567 | 2022-10-27 | Data Governance |
| SO-IS-99.5-PR-187 | IC-1574 | 2023-10-18 | Product Management |
| PE-PR-GR-B-793 | TC-1585 | 2023-07-16 | IT Infrastructure |
| SO-IS-98-430 | IC-1592 | 2022-10-23 | Supply Chain |
| DE-840 | IC-1601 | 2021-06-12 | Data Governance |
| WH-GL-GR-B-926 | IC-1609 | 2022-06-27 | Operations |
| GL-SY-70-549 | IC-1615 | 2021-09-01 | Supply Chain |
| SU-OI-ST-338 | TC-1626 | 2023-08-16 | Supply Chain |
| SO-IS-25-ST-345 | TC-1632 | 2024-08-21 | Compliance |
| AS-AC-99.5-PR-761 | IC-1639 | 2024-03-03 | Finance |
| SO-IS-GR-A-940 | IC-1642 | 2024-02-19 | Operations |
| DE-TE-380 | TC-1644 | 2021-10-02 | Finance |
| PA-OI-632 | IC-1650 | 2023-03-20 | Compliance |
| PO-SO-763 | TC-1672 | 2021-02-07 | Finance |
| FR-99.5-PH-GR-378 | TC-1676 | 2024-02-22 | Compliance |
| SO-BE-700 | BC-1680 | 2022-03-21 | IT Infrastructure |
| PA-OI-70-GR-B-781 | BC-1685 | 2021-12-02 | Product Management |
| SO-BE-25-774 | BC-1689 | 2023-08-24 | Supply Chain |
| SO-CH-70-365 | TC-1695 | 2021-04-05 | Data Governance |
| CA-PR-568 | IC-1698 | 2023-05-23 | Supply Chain |
| SO-CH-99.5-618 | BC-1708 | 2021-06-10 | Finance |
| AS-AC-TE-342 | BC-1714 | 2021-10-27 | Supply Chain |
| FR-25-GR-B-641 | TC-1722 | 2024-05-27 | Operations |
| SO-CH-758 | TC-1728 | 2023-05-10 | IT Infrastructure |
| DE-ST-213 | TC-1732 | 2021-08-03 | Supply Chain |
| CO-OI-358 | IC-1739 | 2022-05-06 | Finance |
| CO-OI-99.5-PH-GR-944 | IC-1752 | 2024-06-28 | Data Governance |
| IS-70-838 | IC-1757 | 2022-11-10 | Data Governance |
| DE-FO-GR-588 | BC-1767 | 2024-06-28 | Supply Chain |
| PA-OI-50-273 | BC-1779 | 2023-01-09 | Operations |
| AS-AC-98-PR-217 | IC-1786 | 2021-10-14 | Supply Chain |
| SO-AC-70-785 | BC-1791 | 2024-12-13 | Data Governance |
| SO-CH-ST-522 | TC-1801 | 2022-02-08 | Data Governance |
| IS-PR-125 | TC-1807 | 2022-05-16 | Finance |
| CI-AC-25-GR-A-669 | BC-1813 | 2024-08-22 | Finance |
| SO-CH-25-PR-784 | IC-1816 | 2022-12-20 | Data Governance |
| CA-CA-GR-B-761 | IC-1821 | 2022-08-16 | Supply Chain |
| SO-IS-275 | BC-1826 | 2022-10-22 | Operations |
| DE-602 | BC-1829 | 2023-04-18 | Supply Chain |
| WH-GL-830 | BC-1836 | 2023-06-21 | Product Management |
| FR-FO-GR-823 | IC-1841 | 2024-11-13 | Data Governance |
| AS-AC-70-133 | BC-1849 | 2024-12-14 | IT Infrastructure |
| SO-IS-50-GR-B-983 | TC-1855 | 2022-09-21 | Compliance |
| CY-926 | IC-1857 | 2024-11-03 | Operations |
| AS-AC-165 | TC-1863 | 2022-10-11 | Product Management |
| DE-25-TE-949 | TC-1868 | 2022-06-18 | Product Management |
| IS-FO-GR-555 | BC-1873 | 2022-10-11 | Product Management |
| DE-70-856 | TC-1882 | 2021-07-28 | Finance |
| PE-PR-50-128 | BC-1889 | 2024-02-22 | Product Management |
| SO-CH-PR-862 | TC-1891 | 2021-11-22 | Supply Chain |
| CI-AC-215 | IC-1895 | 2024-10-11 | Finance |
| GL-SY-TE-601 | BC-1921 | 2021-11-27 | Product Management |
| RA-OI-TE-584 | BC-1928 | 2024-03-20 | Operations |
| GL-SY-98-ST-578 | IC-1939 | 2021-11-09 | IT Infrastructure |
| IS-50-TE-886 | IC-1952 | 2024-01-08 | IT Infrastructure |
| SO-BE-99.5-TE-213 | BC-1964 | 2021-11-23 | Finance |
| SO-BE-GR-B-914 | TC-1972 | 2021-02-10 | Data Governance |
| DE-TE-414 | IC-1984 | 2021-07-23 | IT Infrastructure |
| AS-AC-ST-243 | IC-1990 | 2024-12-13 | IT Infrastructure |
| CI-AC-FO-GR-293 | IC-1995 | 2022-12-07 | Compliance |
| WH-GL-GR-B-129 | IC-2005 | 2021-09-10 | Data Governance |
| CA-TE-562 | IC-2010 | 2024-02-09 | IT Infrastructure |
| GL-SY-98-939 | TC-2017 | 2022-03-13 | Operations |
| RA-OI-70-PR-405 | TC-2027 | 2024-05-21 | Compliance |
| CI-AC-99.5-469 | BC-2035 | 2024-02-04 | Supply Chain |
| PA-OI-383 | BC-2040 | 2022-07-01 | Product Management |
| RA-OI-431 | IC-2045 | 2022-06-24 | Operations |
| PA-OI-98-856 | IC-2052 | 2021-10-07 | Operations |
| FR-GR-B-231 | BC-2057 | 2022-03-09 | Supply Chain |
| AS-AC-70-347 | IC-2064 | 2021-12-03 | Product Management |
| CI-AC-857 | TC-2068 | 2021-03-04 | Data Governance |
| LA-AC-70-PH-GR-221 | TC-2074 | 2023-11-08 | Finance |
| PO-SO-GR-A-715 | TC-2081 | 2023-07-24 | Data Governance |
| SO-CH-881 | BC-2090 | 2022-07-24 | Product Management |
| FR-113 | TC-2097 | 2024-08-09 | Finance |
| SO-BE-GR-A-760 | BC-2109 | 2024-12-14 | Compliance |
| FR-GR-B-311 | IC-2115 | 2024-07-14 | Compliance |
| AS-AC-130 | BC-2126 | 2021-01-20 | Operations |
| PE-PR-PR-428 | BC-2131 | 2021-11-03 | Operations |
| FR-124 | IC-2135 | 2022-05-16 | Finance |
| RA-OI-98-679 | TC-2147 | 2021-08-04 | Supply Chain |
| PO-SO-50-GR-B-154 | IC-2156 | 2023-12-15 | IT Infrastructure |
| MA-DE-944 | IC-2163 | 2022-01-02 | Finance |
| PA-OI-70-780 | IC-2170 | 2021-05-26 | Operations |
| PE-PR-98-GR-B-195 | BC-2174 | 2021-11-22 | Operations |
| SO-IS-FO-GR-334 | TC-2181 | 2024-07-04 | Finance |
| GL-SY-70-655 | BC-2184 | 2023-06-14 | Data Governance |
| DE-GR-A-351 | IC-2191 | 2021-04-04 | Data Governance |
| LA-AC-554 | TC-2201 | 2023-02-02 | Operations |
| CA-CA-50-GR-A-195 | IC-2207 | 2023-10-18 | Operations |
| PO-SO-339 | BC-2211 | 2023-12-12 | Finance |
| LA-AC-TE-651 | TC-2216 | 2023-08-10 | Data Governance |
| DE-25-260 | BC-2233 | 2021-09-10 | Supply Chain |
| DE-GR-B-942 | IC-2239 | 2023-01-22 | IT Infrastructure |
| RE-ST-GR-B-677 | IC-2249 | 2022-11-19 | Supply Chain |
| LA-AC-GR-A-949 | TC-2258 | 2022-09-09 | Supply Chain |
| DE-GR-A-512 | IC-2267 | 2022-08-05 | IT Infrastructure |
| AS-AC-99.5-619 | BC-2273 | 2024-11-08 | IT Infrastructure |
| SO-CH-98-657 | IC-2275 | 2023-12-08 | Product Management |
| SO-CH-752 | TC-2280 | 2021-08-02 | IT Infrastructure |
| PE-PR-25-PH-GR-591 | TC-2283 | 2022-12-19 | Compliance |
| PE-PR-TE-718 | TC-2292 | 2021-07-23 | IT Infrastructure |
| MA-DE-PR-303 | TC-2296 | 2023-08-15 | Finance |
| GL-SY-533 | IC-2315 | 2021-11-28 | Data Governance |
| SO-IS-354 | TC-2333 | 2023-02-10 | Product Management |
| RE-ST-676 | BC-2336 | 2024-08-22 | Product Management |
| PO-SO-ST-111 | BC-2343 | 2024-08-21 | Supply Chain |
| LA-AC-FO-GR-469 | IC-2354 | 2021-10-16 | Operations |
| CI-AC-25-TE-484 | TC-2360 | 2021-09-12 | Supply Chain |
| DE-50-727 | BC-2366 | 2024-03-13 | Operations |
| IS-230 | IC-2372 | 2023-04-15 | Data Governance |
| SO-IS-50-GR-B-346 | IC-2382 | 2023-10-01 | Finance |
| PE-PR-929 | IC-2388 | 2023-12-21 | Operations |
| WH-GL-GR-A-583 | IC-2397 | 2022-04-07 | Product Management |
| PA-OI-25-GR-A-241 | BC-2403 | 2023-04-20 | Data Governance |
| RA-OI-GR-A-272 | BC-2415 | 2024-01-13 | Compliance |
| DE-70-GR-A-741 | BC-2419 | 2023-11-07 | Supply Chain |
| SO-BE-25-GR-B-233 | IC-2437 | 2021-11-02 | IT Infrastructure |
| SO-BE-50-924 | BC-2450 | 2021-05-05 | Product Management |
| CO-OI-977 | BC-2456 | 2023-11-27 | Data Governance |
| FR-194 | IC-2460 | 2024-11-01 | Supply Chain |
| CI-AC-538 | TC-2474 | 2022-12-08 | Operations |
| SO-CH-TE-286 | BC-2479 | 2022-05-18 | Finance |
| PO-SO-202 | BC-2486 | 2021-09-02 | Data Governance |
| CI-AC-70-265 | TC-2496 | 2024-08-26 | Compliance |
| MA-DE-569 | TC-2503 | 2023-11-24 | Compliance |
| SO-AC-FO-GR-286 | TC-2515 | 2022-06-02 | Product Management |
| GL-SY-98-749 | BC-2520 | 2023-01-15 | Compliance |
| MA-DE-951 | IC-2524 | 2024-09-21 | IT Infrastructure |
| SO-CH-201 | IC-2531 | 2022-07-04 | Finance |
| LA-AC-FO-GR-687 | TC-2537 | 2024-06-28 | Data Governance |
| SO-CH-70-317 | IC-2546 | 2022-12-03 | Product Management |
| FR-TE-414 | IC-2552 | 2021-06-24 | Compliance |
| LA-AC-893 | IC-2567 | 2023-09-16 | Product Management |
| SO-BE-PH-GR-831 | IC-2575 | 2021-06-18 | Compliance |
| CO-OI-98-FO-GR-748 | IC-2577 | 2023-10-25 | Operations |
| SO-BE-GR-B-936 | TC-2586 | 2023-09-12 | Compliance |
| PO-SO-TE-239 | IC-2590 | 2023-09-01 | Compliance |
| RA-OI-GR-B-834 | TC-2597 | 2023-01-23 | Operations |
| CO-OI-70-701 | BC-2605 | 2021-03-11 | Compliance |
| CA-CA-25-PH-GR-684 | IC-2607 | 2022-12-13 | Finance |
| MA-DE-GR-B-565 | IC-2613 | 2022-11-03 | Product Management |
| SO-IS-98-PR-717 | BC-2621 | 2024-05-19 | Supply Chain |
| SO-BE-99.5-TE-953 | TC-2628 | 2023-07-17 | IT Infrastructure |
| MA-DE-437 | BC-2640 | 2023-05-28 | Finance |
| CA-CA-GR-B-162 | BC-2649 | 2024-09-19 | Supply Chain |
| SO-CH-TE-223 | TC-2672 | 2023-08-08 | IT Infrastructure |
| PA-OI-GR-B-690 | IC-2684 | 2021-08-14 | Compliance |
| RE-ST-PR-679 | BC-2691 | 2024-01-19 | Finance |
| SO-BE-50-TE-276 | BC-2701 | 2022-08-20 | Compliance |
| AS-AC-ST-686 | IC-2707 | 2021-07-06 | Product Management |
| GL-SY-FO-GR-600 | TC-2719 | 2024-06-21 | IT Infrastructure |
| SO-BE-98-PH-GR-434 | BC-2733 | 2021-02-16 | Data Governance |
| WH-GL-98-511 | BC-2737 | 2021-05-24 | Finance |
| PO-SO-50-TE-282 | IC-2745 | 2021-11-13 | Finance |
| PE-PR-302 | IC-2747 | 2023-07-13 | IT Infrastructure |
| PO-SO-GR-B-511 | BC-2752 | 2024-03-16 | Compliance |
| CI-AC-70-FO-GR-198 | IC-2760 | 2021-04-14 | Product Management |
| FR-99.5-GR-A-438 | IC-2770 | 2022-07-01 | IT Infrastructure |
| PO-SO-25-PH-GR-260 | TC-2776 | 2022-09-06 | Data Governance |
| SO-BE-667 | BC-2784 | 2023-09-25 | Finance |
| LA-AC-50-PR-288 | TC-2790 | 2024-01-25 | Data Governance |
| CA-98-TE-238 | BC-2794 | 2022-07-10 | Compliance |
| RE-ST-98-445 | IC-2810 | 2021-02-18 | Finance |
| CA-CA-99.5-FO-GR-839 | IC-2816 | 2022-09-07 | Data Governance |
| FR-99.5-FO-GR-963 | IC-2820 | 2022-09-01 | Supply Chain |
| LA-AC-ST-823 | TC-2828 | 2024-07-21 | Operations |
| WH-GL-99.5-GR-A-933 | BC-2841 | 2024-07-06 | Product Management |
| SO-BE-99.5-TE-484 | IC-2848 | 2023-05-19 | IT Infrastructure |
| SO-BE-99.5-GR-A-930 | IC-2856 | 2024-01-12 | IT Infrastructure |
| MA-DE-933 | BC-2864 | 2024-08-07 | Product Management |
| AS-AC-50-321 | BC-2871 | 2023-11-08 | Compliance |
| SO-IS-432 | IC-2878 | 2022-10-08 | IT Infrastructure |
| DE-GR-A-472 | IC-2881 | 2022-08-28 | Supply Chain |
| CO-OI-70-GR-A-836 | IC-2891 | 2023-05-28 | Finance |
| CA-CA-50-260 | IC-2895 | 2022-11-10 | Operations |
| PA-OI-50-497 | IC-2899 | 2023-10-03 | Finance |
| PO-SO-98-216 | TC-2906 | 2024-03-26 | Finance |
| AS-AC-439 | TC-2921 | 2024-04-20 | Finance |
| GL-SY-609 | BC-2933 | 2021-01-04 | Finance |
| CA-CA-99.5-291 | TC-2939 | 2023-02-05 | Operations |
| LA-AC-GR-B-700 | TC-2958 | 2024-02-03 | Finance |
| PO-SO-604 | IC-2975 | 2024-12-01 | Product Management |
| PA-OI-PH-GR-124 | IC-2983 | 2024-04-23 | Data Governance |
| PE-PR-PR-775 | BC-2987 | 2022-05-13 | Product Management |
| CO-OI-98-TE-864 | TC-2994 | 2021-01-04 | Data Governance |
| CO-OI-98-876 | IC-3007 | 2021-10-26 | Supply Chain |
| RE-ST-99.5-242 | TC-3013 | 2021-11-22 | Finance |
| SO-CH-354 | TC-3018 | 2022-09-28 | IT Infrastructure |
| CO-OI-25-TE-157 | TC-3022 | 2023-11-08 | Supply Chain |
| LA-AC-98-GR-A-841 | IC-3027 | 2022-01-26 | Finance |
| PE-PR-25-472 | TC-3037 | 2022-02-20 | Supply Chain |
| CA-CA-70-883 | BC-3044 | 2022-03-14 | Product Management |
| RE-ST-50-692 | TC-3056 | 2023-06-26 | IT Infrastructure |
| RE-ST-FO-GR-727 | TC-3070 | 2023-02-18 | Supply Chain |
| SO-AC-70-542 | BC-3078 | 2023-10-02 | Compliance |
| WH-GL-944 | IC-3083 | 2024-03-13 | Operations |
| SO-BE-FO-GR-650 | TC-3089 | 2021-10-24 | Operations |
| WH-GL-123 | TC-3095 | 2022-02-14 | IT Infrastructure |
| SO-AC-ST-392 | BC-3108 | 2022-04-05 | Product Management |
| WH-GL-50-865 | IC-3119 | 2021-10-10 | Compliance |
| DE-GR-B-244 | IC-3125 | 2022-02-12 | Supply Chain |
| CI-AC-25-863 | BC-3131 | 2023-01-01 | IT Infrastructure |
| PE-PR-746 | TC-3135 | 2021-10-24 | IT Infrastructure |
| CA-CA-98-928 | BC-3142 | 2024-09-28 | Supply Chain |
| CA-GR-B-950 | BC-3152 | 2021-12-09 | Product Management |
| WH-GL-FO-GR-876 | BC-3158 | 2022-10-25 | Product Management |
| CI-AC-PR-827 | BC-3167 | 2022-10-24 | IT Infrastructure |
| SO-CH-25-556 | BC-3172 | 2022-06-25 | Operations |
| CO-OI-25-FO-GR-778 | TC-3175 | 2022-04-02 | Finance |
| AS-AC-573 | BC-3182 | 2024-06-19 | Product Management |
| SU-OI-GR-B-259 | BC-3184 | 2022-02-08 | Supply Chain |
| PA-OI-99.5-867 | BC-3190 | 2021-04-18 | IT Infrastructure |
| SO-BE-824 | IC-3195 | 2024-03-25 | Operations |
| PO-SO-70-899 | TC-3203 | 2023-07-25 | Operations |
| PO-SO-ST-914 | TC-3212 | 2022-05-10 | Finance |
| DE-FO-GR-183 | TC-3220 | 2022-03-27 | Product Management |
| SO-BE-98-410 | TC-3227 | 2024-11-17 | Supply Chain |
| FR-99.5-TE-579 | IC-3231 | 2021-12-16 | Compliance |
| GL-SY-99.5-GR-B-358 | IC-3234 | 2021-01-12 | Finance |
| SO-AC-50-FO-GR-250 | BC-3244 | 2022-11-18 | Compliance |
| RA-OI-GR-A-980 | BC-3256 | 2021-07-10 | IT Infrastructure |
| DE-ST-999 | TC-3268 | 2023-01-09 | Supply Chain |
| CA-CA-947 | BC-3278 | 2023-08-04 | Supply Chain |
| PA-OI-98-GR-A-940 | TC-3291 | 2023-09-24 | Data Governance |
| RE-ST-50-232 | BC-3304 | 2021-12-12 | Supply Chain |
| DE-70-PH-GR-978 | BC-3317 | 2024-08-04 | Operations |
| LA-AC-25-819 | TC-3323 | 2023-08-05 | Data Governance |
| SO-AC-PH-GR-620 | TC-3325 | 2021-10-16 | IT Infrastructure |
| FR-99.5-TE-779 | TC-3331 | 2023-07-26 | Supply Chain |
| PE-PR-25-185 | BC-3335 | 2021-08-05 | Supply Chain |
| AS-AC-TE-868 | BC-3343 | 2021-02-04 | Finance |
| SO-BE-708 | IC-3350 | 2022-04-19 | Product Management |
| PA-OI-GR-B-326 | IC-3355 | 2024-04-05 | Operations |
| LA-AC-25-PR-377 | BC-3362 | 2023-07-15 | Finance |
| DE-TE-956 | TC-3367 | 2022-02-18 | IT Infrastructure |
| DE-98-512 | BC-3374 | 2021-10-03 | Product Management |
| SO-IS-FO-GR-437 | TC-3382 | 2024-09-05 | Compliance |
| MA-DE-873 | TC-3399 | 2024-08-16 | Supply Chain |
| RE-ST-50-526 | TC-3404 | 2023-07-20 | Compliance |
| FR-50-ST-938 | IC-3418 | 2021-04-02 | Product Management |
| MA-DE-516 | BC-3424 | 2022-08-03 | Operations |
| CA-CA-98-485 | IC-3432 | 2024-03-02 | IT Infrastructure |
| IS-641 | TC-3437 | 2021-05-06 | Compliance |
| AS-AC-FO-GR-835 | IC-3446 | 2024-09-21 | Product Management |
| MA-DE-161 | TC-3455 | 2022-03-27 | IT Infrastructure |
| SO-CH-257 | IC-3457 | 2021-04-16 | Product Management |
| DE-706 | IC-3465 | 2022-10-21 | Compliance |
| SO-CH-25-FO-GR-400 | BC-3471 | 2023-12-18 | Compliance |
| PE-PR-70-PR-387 | TC-3479 | 2023-04-06 | Data Governance |
| SO-CH-115 | BC-3485 | 2022-05-14 | IT Infrastructure |
| SO-IS-PR-309 | BC-3487 | 2021-05-05 | Supply Chain |
| SO-CH-892 | BC-3493 | 2024-04-17 | Finance |
| LA-AC-471 | TC-3500 | 2024-09-25 | Product Management |
| WH-GL-99.5-557 | BC-3506 | 2022-07-16 | Operations |
| GL-SY-99.5-FO-GR-825 | BC-3510 | 2023-11-21 | Operations |
| MA-DE-799 | BC-3517 | 2023-02-10 | Product Management |
| SO-BE-964 | IC-3518 | 2023-04-01 | IT Infrastructure |
| IS-GR-B-640 | IC-3523 | 2024-01-15 | Operations |
| IS-99.5-305 | TC-3531 | 2023-05-06 | Finance |
| CO-OI-70-GR-A-633 | IC-3540 | 2022-10-20 | Product Management |
| GL-SY-25-722 | TC-3542 | 2022-06-25 | Finance |
| SU-OI-GR-A-224 | IC-3546 | 2024-03-27 | Operations |
| CI-AC-ST-565 | TC-3558 | 2021-09-16 | IT Infrastructure |
| CA-GR-A-380 | BC-3566 | 2021-05-01 | Supply Chain |
| PO-SO-480 | TC-3573 | 2024-10-06 | Compliance |
| RE-ST-GR-A-614 | IC-3580 | 2022-12-25 | IT Infrastructure |
| AS-AC-PR-778 | IC-3591 | 2023-06-13 | Compliance |
| SO-CH-99.5-GR-A-206 | BC-3597 | 2021-03-06 | IT Infrastructure |
| WH-GL-GR-A-924 | IC-3610 | 2023-03-07 | Finance |
| DE-GR-B-157 | IC-3618 | 2024-12-02 | Operations |
| SU-OI-TE-705 | TC-3622 | 2024-02-17 | Compliance |
| PE-PR-251 | TC-3624 | 2022-07-25 | IT Infrastructure |
| LA-AC-TE-761 | BC-3635 | 2024-05-11 | Compliance |
| MA-DE-640 | BC-3639 | 2021-05-01 | Product Management |
| SO-IS-99.5-GR-A-499 | TC-3648 | 2021-11-14 | IT Infrastructure |
| SO-BE-355 | TC-3655 | 2024-03-15 | IT Infrastructure |
| SO-IS-99.5-141 | TC-3665 | 2024-07-27 | Finance |
| SU-OI-251 | BC-3674 | 2024-06-05 | Finance |
| SU-OI-ST-194 | TC-3680 | 2023-07-17 | Finance |
| PO-SO-768 | TC-3684 | 2024-12-02 | Supply Chain |
| CO-OI-25-252 | BC-3692 | 2022-08-10 | Product Management |
| CA-TE-336 | BC-3703 | 2024-02-10 | Compliance |
| SU-OI-70-FO-GR-432 | IC-3710 | 2024-11-14 | Operations |
| CA-50-PR-226 | BC-3716 | 2022-01-13 | Data Governance |
| IS-GR-B-649 | IC-3723 | 2022-06-06 | IT Infrastructure |
| LA-AC-891 | BC-3728 | 2024-06-23 | Compliance |
| RE-ST-ST-711 | TC-3745 | 2022-06-08 | Product Management |
| RE-ST-575 | BC-3748 | 2024-11-09 | Compliance |
| SO-CH-TE-789 | TC-3759 | 2021-07-16 | Supply Chain |
| CO-OI-98-PR-329 | IC-3764 | 2024-02-01 | Operations |
| DE-98-FO-GR-211 | TC-3776 | 2023-10-26 | Operations |
| SU-OI-423 | BC-3780 | 2023-05-03 | Compliance |
| CA-25-GR-A-885 | IC-3798 | 2024-01-09 | IT Infrastructure |
| DE-TE-340 | IC-3802 | 2022-04-19 | Compliance |
| CY-ST-539 | BC-3807 | 2022-01-10 | Operations |
| CA-25-TE-580 | BC-3811 | 2022-11-25 | Compliance |
| WH-GL-403 | BC-3824 | 2023-10-16 | Supply Chain |
| SU-OI-GR-A-704 | TC-3833 | 2022-04-15 | Operations |
| CA-CA-FO-GR-685 | TC-3837 | 2022-04-14 | Compliance |
| FR-ST-953 | BC-3844 | 2021-06-07 | Operations |
| RE-ST-796 | IC-3865 | 2021-03-06 | Product Management |
| PO-SO-FO-GR-989 | IC-3872 | 2023-08-19 | Operations |
| CI-AC-596 | TC-3879 | 2022-10-23 | Data Governance |
| SO-IS-PR-242 | BC-3889 | 2024-11-01 | Product Management |
| PE-PR-ST-174 | BC-3895 | 2023-08-15 | Compliance |
| FR-PR-267 | TC-3909 | 2024-06-21 | Supply Chain |
| CI-AC-FO-GR-977 | TC-3914 | 2024-11-27 | Compliance |
| AT-IN-327 | BC-3930 | 2021-09-04 | Data Governance |
| PR-PA-823 International | IC-3942 | 2021-04-27 | Finance |
| GL-DI-615 Corp. | BC-3946 | 2021-03-01 | Product Management |
| ST-DI-782 SA | BC-3962 | 2024-09-08 | IT Infrastructure |
| ST-IN-505 SA | IC-3977 | 2023-04-04 | Finance |
| ME-SO-413 | BC-3983 | 2023-01-10 | Operations |
| PA-LO-382 Group | IC-3987 | 2023-07-06 | Compliance |
| ST-SU-323 Group | IC-3993 | 2022-04-14 | IT Infrastructure |
| QU-IN-923 International | BC-3997 | 2023-03-10 | Operations |
| CO-CH-289 Group | IC-4007 | 2022-07-07 | Supply Chain |
| CE-TR-144 International | TC-4020 | 2022-05-23 | Finance |
| PA-CH-795 | BC-4025 | 2023-11-14 | IT Infrastructure |
| PA-DI-201 NV | TC-4031 | 2024-04-04 | IT Infrastructure |
| PR-EN-361 International | TC-4041 | 2022-12-10 | Finance |
| HO-MA-349 | BC-4047 | 2024-11-21 | Finance |
| PI-DI-518 | IC-4051 | 2023-04-03 | Supply Chain |
| VE-EN-393 Group | BC-4056 | 2023-04-03 | Operations |
| PR-CH-565 SAS | IC-4064 | 2021-02-17 | Supply Chain |
| ST-TR-340 BV | BC-4074 | 2023-03-21 | Data Governance |
| BA-EN-363 KG | TC-4083 | 2023-07-23 | Product Management |
| PR-LO-245 Ltd. | TC-4089 | 2023-02-19 | Compliance |
| QU-MA-180 | BC-4098 | 2023-11-26 | Operations |
| AT-MA-796 LLC | BC-4121 | 2024-06-28 | Data Governance |
| AT-MA-324 International | BC-4126 | 2023-05-04 | IT Infrastructure |
| ZE-MA-359 Group | BC-4133 | 2021-08-01 | Data Governance |
| AT-LO-410 Holdings | TC-4143 | 2021-08-22 | Product Management |
| CE-PR-134 | BC-4146 | 2024-02-26 | Data Governance |
| GL-PR-596 | IC-4158 | 2024-02-16 | Finance |
| HO-PA-330 Holdings | BC-4166 | 2022-01-05 | Operations |
| AP-SO-704 | IC-4171 | 2022-02-19 | Finance |
| PI-CH-997 SAS | BC-4177 | 2024-02-21 | IT Infrastructure |
| CO-MA-845 Holdings | BC-4180 | 2024-06-28 | Product Management |
| PI-IN-244 | TC-4183 | 2024-03-13 | Supply Chain |
| PR-MA-826 Corp. | BC-4189 | 2022-02-05 | Operations |
| ZE-PA-511 PLC | BC-4197 | 2022-06-26 | Finance |
| EL-DI-554 International | TC-4205 | 2021-12-16 | Data Governance |
| PR-SU-935 Ltd. | BC-4211 | 2023-10-05 | Data Governance |
| ME-TR-587 | BC-4221 | 2023-11-10 | Product Management |
| PR-IN-608 BV | BC-4231 | 2022-04-11 | IT Infrastructure |
| ME-SO-760 GmbH | IC-4244 | 2022-06-02 | IT Infrastructure |
| EL-CH-346 GmbH | IC-4255 | 2024-09-02 | Data Governance |
| GL-EN-914 NV | BC-4265 | 2021-07-17 | Data Governance |
| CE-SU-700 Group | IC-4276 | 2021-10-03 | Finance |
| GL-LO-196 NV | BC-4280 | 2024-01-06 | IT Infrastructure |
| CO-EN-642 AG | IC-4285 | 2024-10-11 | IT Infrastructure |
| CO-LO-919 Holdings | IC-4291 | 2023-07-18 | Data Governance |
| BA-TR-377 NV | TC-4311 | 2023-03-08 | Data Governance |
| NO-IN-155 SA | IC-4325 | 2023-02-14 | Supply Chain |
| VE-DI-139 KG | TC-4335 | 2022-10-09 | Supply Chain |
| PR-LO-104 KG | TC-4336 | 2024-05-10 | Operations |
| QU-TR-219 International | TC-4339 | 2021-12-06 | Data Governance |
| CA-CO-549 GmbH | IC-4342 | 2021-10-11 | Operations |
| BA-IN-777 Inc. | IC-4347 | 2021-09-02 | Operations |
| AP-TR-571 Group | IC-4351 | 2021-01-18 | Compliance |
| CO-IN-915 KG | BC-4359 | 2024-12-22 | Compliance |
| NE-DI-555 | IC-4364 | 2024-02-24 | Compliance |
| ST-IN-592 SA | IC-4374 | 2021-08-19 | Supply Chain |
| CA-IN-566 International | TC-4380 | 2024-08-04 | Compliance |
| VA-MA-537 Holdings | BC-4386 | 2023-05-25 | Product Management |
| PI-CO-717 | IC-4392 | 2024-07-19 | Operations |
| PR-SO-769 LLC | TC-4400 | 2022-11-05 | Data Governance |
| CO-SU-445 LLC | TC-4405 | 2021-11-27 | IT Infrastructure |
| AP-CH-159 LLC | BC-4410 | 2024-02-13 | IT Infrastructure |
| GL-IN-218 | IC-4415 | 2024-03-06 | Product Management |
| NE-EN-400 Group | IC-4422 | 2024-12-21 | Product Management |
| AP-CH-166 International | TC-4430 | 2023-10-13 | Data Governance |
| PI-SO-581 Inc. | TC-4435 | 2023-10-14 | Compliance |
| AT-CH-900 AG | IC-4440 | 2024-10-22 | Operations |
| PR-IN-695 Holdings | IC-4451 | 2024-11-16 | Product Management |
| AT-CO-808 GmbH | TC-4458 | 2023-02-03 | Operations |
| PR-IN-149 Holdings | BC-4464 | 2021-07-03 | Compliance |
| BA-SO-835 Corp. | IC-4475 | 2022-08-16 | Supply Chain |
| VE-DI-556 SA | BC-4487 | 2021-03-18 | Finance |
| CE-MA-931 | TC-4493 | 2021-02-10 | Finance |
| ZE-TR-981 | IC-4500 | 2022-04-10 | IT Infrastructure |
| NE-DI-555 Corp. | TC-4505 | 2024-08-14 | Product Management |
| PI-IN-388 | BC-4511 | 2021-02-01 | Data Governance |
| ZE-PR-190 BV | BC-4515 | 2024-04-03 | Product Management |
| CO-CH-401 Inc. | IC-4522 | 2021-06-18 | Operations |
| HO-LO-514 International | BC-4530 | 2023-03-19 | Data Governance |
| QU-SO-509 | TC-4537 | 2023-06-28 | Data Governance |
| NO-MA-529 | IC-4539 | 2024-05-22 | Compliance |
| GL-SO-534 Holdings | IC-4553 | 2023-03-26 | IT Infrastructure |
| NO-IN-797 | IC-4577 | 2023-08-25 | Compliance |
| HO-PA-675 | IC-4581 | 2022-12-23 | Operations |
| HO-IN-142 AG | BC-4588 | 2021-04-23 | Finance |
| NE-PR-315 Holdings | BC-4593 | 2024-08-03 | IT Infrastructure |
| QU-CO-993 | TC-4600 | 2022-12-13 | Operations |
| NE-CH-574 Group | TC-4612 | 2024-07-26 | Supply Chain |
| ZE-PA-718 LLC | IC-4615 | 2023-07-20 | Supply Chain |
| CA-CO-939 | TC-4623 | 2021-12-21 | Finance |
| PR-MA-669 Ltd. | IC-4628 | 2022-02-25 | IT Infrastructure |
| VE-IN-644 Ltd. | BC-4641 | 2023-07-01 | Compliance |
| CO-SO-525 BV | IC-4648 | 2024-01-25 | Compliance |
| ST-CO-650 International | TC-4656 | 2023-12-08 | Operations |
| NE-CO-575 Holdings | BC-4662 | 2022-04-25 | Operations |
| PI-DI-618 NV | IC-4669 | 2023-07-05 | Operations |
| CA-IN-236 PLC | BC-4672 | 2022-02-20 | Operations |
| AT-IN-931 | BC-4689 | 2022-01-28 | Operations |
| QU-PA-832 NV | BC-4694 | 2024-09-16 | IT Infrastructure |
| ST-DI-517 Holdings | BC-4699 | 2023-12-07 | IT Infrastructure |
| PA-SU-946 Group | IC-4706 | 2024-01-04 | Finance |
| PR-SO-362 | BC-4711 | 2024-06-20 | Product Management |
| VE-CO-558 | BC-4712 | 2024-10-21 | Supply Chain |
| AT-PR-442 | BC-4719 | 2021-01-24 | Supply Chain |
| QU-TR-490 SARL | IC-4726 | 2022-01-14 | Supply Chain |
| CE-MA-604 | BC-4736 | 2023-05-09 | Finance |
| NO-MA-994 | TC-4743 | 2021-05-26 | Product Management |
| AT-TR-553 | BC-4745 | 2021-05-05 | Data Governance |
| EL-SO-163 | TC-4754 | 2023-12-28 | Supply Chain |
| AT-LO-568 SA | TC-4758 | 2024-05-12 | Operations |
| ST-PR-265 Corp. | BC-4766 | 2021-11-27 | Supply Chain |
| CE-IN-169 Group | IC-4770 | 2023-02-16 | Product Management |
| HO-PA-995 Group | IC-4783 | 2023-02-26 | Supply Chain |
| PR-EN-954 Holdings | IC-4791 | 2021-06-03 | Operations |
| BA-IN-585 SARL | IC-4797 | 2021-04-06 | Product Management |
| ZE-TR-467 AG | IC-4804 | 2022-02-13 | Compliance |
| EL-LO-432 Holdings | IC-4809 | 2021-07-21 | Operations |
| PR-SO-102 | BC-4813 | 2023-12-19 | Supply Chain |
| ST-DI-556 Holdings | TC-4818 | 2022-07-07 | Product Management |
| NE-DI-240 Ltd. | BC-4837 | 2024-10-27 | Compliance |
| CA-CO-128 SAS | BC-4855 | 2022-10-09 | Finance |
| NE-PA-401 | IC-4863 | 2021-05-27 | Supply Chain |
| CO-MA-726 NV | TC-4871 | 2021-05-04 | Product Management |
| ST-PA-504 | TC-4879 | 2023-10-17 | Finance |
| ME-DI-790 Group | BC-4888 | 2024-02-02 | Compliance |
| PR-TR-294 | BC-4894 | 2022-06-15 | Finance |
| NE-SO-511 | TC-4902 | 2023-12-23 | Supply Chain |
| AT-IN-899 Group | IC-4914 | 2021-10-20 | Operations |
| ST-MA-670 Group | BC-4922 | 2022-05-17 | Supply Chain |
| ZE-MA-316 | IC-4925 | 2023-06-17 | Operations |
| CO-CH-610 | TC-4929 | 2023-01-22 | Supply Chain |
| AP-MA-145 International | TC-4935 | 2024-08-03 | IT Infrastructure |
| HO-PA-149 International | IC-4944 | 2024-10-03 | IT Infrastructure |
| CO-PR-215 Group | IC-4955 | 2023-12-07 | Finance |
| EL-MA-344 NV | TC-4964 | 2022-11-24 | Finance |
| BA-SO-682 International | BC-4973 | 2024-11-12 | Product Management |
| NE-SU-335 | BC-4978 | 2022-12-19 | Data Governance |
| PA-IN-447 | IC-4984 | 2022-11-12 | Finance |
| ST-PA-980 | TC-4991 | 2024-06-22 | Supply Chain |
| AT-LO-132 | IC-5000 | 2024-06-22 | Product Management |
| NE-IN-874 SA | BC-5004 | 2022-03-28 | Compliance |
| PR-IN-195 KG | BC-5009 | 2024-12-16 | Data Governance |
| CE-MA-338 | TC-5017 | 2022-06-19 | Operations |
| PR-MA-359 | IC-5031 | 2023-03-19 | Supply Chain |
| QU-PR-732 SA | TC-5040 | 2024-02-05 | Data Governance |
| CO-IN-363 AG | TC-5047 | 2024-03-09 | Data Governance |
| CE-MA-847 | IC-5049 | 2022-08-21 | Supply Chain |
| GL-PR-906 | TC-5057 | 2023-08-22 | Compliance |
| PA-EN-915 | TC-5068 | 2024-02-11 | Data Governance |
| NO-MA-484 BV | IC-5073 | 2022-02-24 | Finance |
| PR-SO-400 | IC-5078 | 2023-03-18 | Operations |
| CO-MA-993 Corp. | TC-5088 | 2024-09-27 | IT Infrastructure |
| NE-EN-710 NV | IC-5095 | 2021-03-07 | Operations |
| BA-IN-897 BV | IC-5103 | 2021-05-21 | IT Infrastructure |
| AT-PA-546 Corp. | TC-5108 | 2021-08-17 | Compliance |
| EL-PA-851 | IC-5115 | 2021-01-21 | Supply Chain |
| NE-TR-634 International | IC-5120 | 2024-02-03 | Compliance |
| PR-MA-448 | TC-5125 | 2024-08-14 | Finance |
| NO-LO-598 Holdings | IC-5129 | 2022-10-12 | Finance |
| VA-LO-190 International | IC-5135 | 2022-01-13 | Product Management |
| AT-MA-694 Holdings | IC-5140 | 2021-02-15 | Finance |
| AT-DI-544 | BC-5143 | 2023-11-20 | IT Infrastructure |
| ZE-MA-924 | BC-5150 | 2024-02-24 | Operations |
| QU-EN-736 NV | IC-5154 | 2021-01-06 | IT Infrastructure |
| GL-CH-617 SARL | TC-5157 | 2021-02-09 | Product Management |
| PR-CH-121 KG | BC-5170 | 2023-06-03 | Finance |
| AT-PR-500 International | TC-5176 | 2023-06-08 | IT Infrastructure |
| VA-IN-954 PLC | TC-5181 | 2021-02-26 | IT Infrastructure |
| VE-DI-822 Group | IC-5188 | 2023-04-08 | Operations |
| CE-CO-433 | IC-5194 | 2024-08-06 | IT Infrastructure |
| AT-SU-132 | IC-5198 | 2021-05-03 | Compliance |
| ME-TR-366 International | TC-5203 | 2024-05-23 | IT Infrastructure |
| PI-LO-710 NV | BC-5205 | 2022-06-10 | Compliance |
| PA-IN-136 | TC-5213 | 2024-09-10 | IT Infrastructure |
| PR-MA-114 BV | BC-5218 | 2021-03-06 | Supply Chain |
| CA-IN-146 SA | TC-5225 | 2021-11-06 | Compliance |
| PR-PA-671 SA | BC-5231 | 2024-02-19 | IT Infrastructure |
| ST-SU-125 SA | BC-5239 | 2024-12-08 | Supply Chain |
| ST-SU-950 SAS | BC-5243 | 2022-01-23 | IT Infrastructure |
| PI-MA-367 SA | IC-5248 | 2024-08-02 | IT Infrastructure |
| ST-CO-827 Holdings | BC-5258 | 2022-11-03 | Compliance |
| AP-MA-984 | IC-5270 | 2023-11-06 | Data Governance |
| PA-MA-742 KG | TC-5286 | 2022-09-25 | Supply Chain |
| VA-PA-407 | TC-5293 | 2022-01-19 | Finance |
| VA-DI-229 | TC-5298 | 2022-04-04 | IT Infrastructure |
| PI-LO-946 | IC-5304 | 2023-02-01 | Finance |
| CE-PA-586 SARL | BC-5314 | 2021-12-08 | Finance |
| ME-CH-956 KG | TC-5322 | 2021-05-10 | Data Governance |
| PR-EN-809 Holdings | BC-5323 | 2021-05-28 | Operations |
| NO-MA-452 | IC-5328 | 2023-05-07 | Product Management |
| VE-LO-902 Group | IC-5330 | 2022-07-07 | Supply Chain |
| PR-CO-800 Corp. | BC-5337 | 2023-06-19 | Product Management |
| ZE-DI-241 | IC-5339 | 2021-05-26 | Finance |
| VA-DI-105 | TC-5353 | 2022-02-26 | Product Management |
| CO-IN-421 | BC-5359 | 2024-03-16 | IT Infrastructure |
| PR-SO-284 Group | IC-5367 | 2022-01-23 | Compliance |
| BA-SU-479 | IC-5369 | 2022-03-21 | Supply Chain |
| PR-CH-334 GmbH | TC-5372 | 2024-06-11 | Data Governance |
| PR-MA-844 | TC-5395 | 2024-11-04 | Finance |
| HO-LO-534 PLC | IC-5402 | 2024-12-06 | IT Infrastructure |
| PR-LO-801 AG | TC-5407 | 2022-02-27 | Data Governance |
| GL-PA-520 BV | IC-5416 | 2022-12-25 | Compliance |
| CO-MA-371 | BC-5427 | 2021-03-11 | Finance |
| NO-DI-180 Ltd. | IC-5435 | 2023-10-03 | Data Governance |
| PR-PA-794 PLC | IC-5444 | 2023-11-20 | IT Infrastructure |
| QU-TR-440 | TC-5450 | 2021-02-06 | Supply Chain |
| CE-MA-423 BV | BC-5457 | 2022-11-05 | IT Infrastructure |
| CE-LO-195 | BC-5462 | 2021-09-04 | Data Governance |
| EL-LO-712 SA | IC-5468 | 2021-01-11 | IT Infrastructure |
| HO-DI-531 Group | BC-5485 | 2022-10-16 | Compliance |
| PI-PR-193 | BC-5501 | 2024-06-12 | Operations |
| VE-CO-290 AG | BC-5509 | 2023-01-21 | Product Management |
| CA-SU-512 Holdings | TC-5519 | 2023-10-04 | Data Governance |
| CO-DI-629 BV | BC-5527 | 2022-12-20 | Operations |
| AP-CH-617 LLC | TC-5538 | 2022-07-16 | IT Infrastructure |
| PR-EN-875 Group | BC-5542 | 2022-07-17 | Product Management |
| NO-DI-582 AG | BC-5546 | 2023-03-08 | Compliance |
| PR-CO-156 PLC | TC-5558 | 2024-07-26 | IT Infrastructure |
| PA-MA-412 GmbH | TC-5565 | 2023-05-27 | Data Governance |
| ST-DI-183 Inc. | BC-5570 | 2022-07-02 | Operations |
| NO-PR-828 SA | TC-5577 | 2024-02-02 | Product Management |
| QU-PR-593 International | BC-5593 | 2023-12-03 | Supply Chain |
| QU-PA-830 Group | IC-5596 | 2021-05-19 | Data Governance |
| GL-PR-599 | BC-5601 | 2022-05-23 | Product Management |
| ZE-IN-456 LLC | IC-5608 | 2024-12-16 | Finance |
| PI-IN-444 | IC-5614 | 2021-12-05 | Product Management |
| AP-TR-161 International | TC-5621 | 2022-02-01 | Compliance |
| PR-PA-998 Holdings | TC-5624 | 2024-12-19 | Product Management |
| ST-SO-965 | BC-5630 | 2023-01-15 | Supply Chain |
| VE-DI-578 International | IC-5636 | 2024-04-03 | Data Governance |
| BA-MA-518 Group | IC-5647 | 2023-01-21 | Operations |
| QU-TR-981 Group | BC-5652 | 2021-05-23 | Finance |
| ST-MA-621 International | IC-5660 | 2022-02-19 | IT Infrastructure |
| BA-TR-619 | BC-5668 | 2024-10-16 | IT Infrastructure |
| CA-SU-681 Group | BC-5676 | 2021-06-24 | Supply Chain |
| AT-SU-661 Corp. | BC-5684 | 2023-11-25 | Supply Chain |
| PR-PA-624 PLC | BC-5688 | 2022-01-04 | Finance |
| AT-PR-985 International | BC-5694 | 2021-07-12 | Operations |
| BA-PR-950 | BC-5697 | 2022-07-08 | Operations |
| CO-PA-308 | BC-5705 | 2024-02-22 | Supply Chain |
| VE-CH-841 Group | BC-5711 | 2023-01-26 | Data Governance |
| ST-TR-590 | BC-5717 | 2022-12-04 | Compliance |
| VA-IN-429 | TC-5721 | 2023-02-25 | Data Governance |
| AT-IN-716 Corp. | BC-5726 | 2021-06-27 | Finance |
| PR-LO-109 Group | IC-5730 | 2022-07-14 | Supply Chain |
| AP-LO-197 Corp. | TC-5736 | 2022-06-06 | Product Management |
| PR-LO-105 | IC-5739 | 2023-03-02 | Operations |
| PI-MA-680 | BC-5745 | 2023-09-01 | Product Management |
| AT-MA-457 | TC-5750 | 2022-06-20 | Product Management |
| PR-SU-CO-624 | IC-5761 | 2022-08-14 | Finance |
| CA-LO-967 | TC-5767 | 2023-12-20 | Finance |
| PR-SU-CO-176 | IC-5775 | 2022-04-28 | Finance |
| PR-MA-609 | TC-5778 | 2022-07-18 | Product Management |
| PR-MA-665 | BC-5780 | 2024-09-01 | IT Infrastructure |
| ST-LO-181 | TC-5789 | 2024-12-03 | Operations |
| CO-MA-245 | BC-5796 | 2024-03-20 | IT Infrastructure |
| EL-SO-358 | IC-5805 | 2021-01-20 | Compliance |
| VE-MA-298 | TC-5809 | 2024-01-16 | Product Management |
| ME-MA-977 | BC-5814 | 2023-02-14 | Finance |
| VE-LO-437 | TC-5820 | 2021-08-15 | Supply Chain |
| ST-SO-491 | IC-5830 | 2022-11-04 | Supply Chain |
| VE-MA-260 | BC-5836 | 2024-03-23 | Product Management |
| GL-LO-669 | BC-5854 | 2022-08-12 | Compliance |
| PI-SO-922 | IC-5860 | 2022-04-02 | IT Infrastructure |
| VA-MA-502 | TC-5871 | 2022-01-19 | Supply Chain |
| CO-SO-101 | BC-5877 | 2021-12-08 | Product Management |
| VE-SO-401 | TC-5884 | 2021-10-21 | Product Management |
| QU-SU-CO-774 | BC-5886 | 2021-06-19 | Operations |
| ME-LO-192 | IC-5912 | 2023-02-02 | IT Infrastructure |
| PR-MA-295 | TC-5914 | 2023-02-25 | IT Infrastructure |
| GL-SO-841 | IC-5921 | 2021-11-17 | Supply Chain |
| VE-SO-701 | IC-5926 | 2021-09-04 | Operations |
| AT-SU-CO-707 | TC-5931 | 2022-04-18 | Operations |
| BA-SU-CO-569 | BC-5938 | 2021-04-22 | IT Infrastructure |
| NE-LO-499 | TC-5947 | 2021-12-01 | Data Governance |
| ST-LO-422 | IC-5955 | 2024-05-16 | IT Infrastructure |
| PR-LO-420 | IC-5960 | 2021-05-24 | IT Infrastructure |
| AP-MA-498 | BC-5965 | 2023-05-24 | Product Management |
| VE-LO-665 | IC-5971 | 2021-04-01 | Operations |
| ST-MA-282 | IC-5978 | 2024-03-23 | IT Infrastructure |
| NE-LO-300 | TC-5986 | 2023-07-06 | Product Management |
| PR-SO-441 | IC-5999 | 2022-04-13 | Operations |
| ST-SO-673 | IC-6003 | 2024-10-21 | Compliance |
| PR-SU-CO-232 | IC-6011 | 2022-08-14 | Operations |
| CO-SU-CO-318 | IC-6017 | 2023-06-01 | Operations |
| NE-LO-735 | IC-6022 | 2024-08-28 | Data Governance |
| AT-SU-CO-864 | TC-6029 | 2024-09-03 | Compliance |
| AT-LO-592 | BC-6040 | 2021-05-04 | Product Management |
| AT-MA-704 | BC-6045 | 2021-11-13 | Finance |
| PR-SU-CO-920 | BC-6050 | 2022-05-02 | IT Infrastructure |
| QU-SU-CO-959 | IC-6064 | 2022-06-05 | Data Governance |
| QU-SO-233 | TC-6075 | 2021-12-17 | Product Management |
| PR-SO-277 | IC-6088 | 2021-08-06 | IT Infrastructure |
| NO-SU-CO-376 | BC-6101 | 2021-03-03 | Compliance |
| PR-SU-CO-573 | IC-6105 | 2024-07-15 | Finance |
| AP-SU-CO-755 | IC-6112 | 2023-01-09 | Compliance |
| AP-SO-122 | BC-6119 | 2024-02-04 | Product Management |
| ST-SU-CO-731 | IC-6126 | 2022-11-21 | Supply Chain |
| PR-MA-581 | IC-6133 | 2024-06-14 | Finance |
| AP-LO-246 | TC-6138 | 2021-06-09 | Product Management |
| PR-LO-745 | BC-6147 | 2022-06-20 | Supply Chain |
| EL-LO-372 | TC-6150 | 2021-11-04 | Operations |
| CE-MA-213 | TC-6155 | 2022-10-21 | Finance |
| AP-LO-406 | IC-6166 | 2023-12-13 | Supply Chain |
| NO-SO-478 | IC-6173 | 2024-09-09 | Finance |
| PA-SO-658 | TC-6184 | 2024-05-21 | Data Governance |
| ST-SO-771 | TC-6188 | 2024-05-17 | Compliance |
| PR-LO-704 | IC-6196 | 2021-08-23 | Product Management |
| CA-MA-370 | TC-6200 | 2023-09-10 | Supply Chain |
| ME-LO-901 | BC-6209 | 2022-08-23 | Product Management |
| PR-MA-367 | IC-6211 | 2022-11-14 | IT Infrastructure |
| CE-SO-153 | TC-6222 | 2021-06-23 | Finance |
| EL-SU-CO-921 | TC-6230 | 2021-01-23 | Supply Chain |
| AT-SO-915 | BC-6236 | 2021-08-19 | Supply Chain |
| PI-SU-CO-207 | TC-6242 | 2021-09-11 | Finance |
| HO-MA-854 | BC-6250 | 2024-04-06 | Product Management |
| CO-LO-944 | TC-6260 | 2022-02-12 | Data Governance |
| AT-SO-165 | IC-6268 | 2023-10-03 | IT Infrastructure |
| NO-LO-302 | BC-6285 | 2022-12-11 | Product Management |
| CO-LO-285 | BC-6297 | 2023-09-21 | Operations |
| BA-SU-CO-430 | BC-6303 | 2024-10-27 | Product Management |
| PR-SO-388 | IC-6312 | 2021-06-16 | Product Management |
| ME-SO-242 | IC-6321 | 2024-08-13 | Operations |
| NO-SU-CO-153 | BC-6329 | 2021-10-23 | Operations |
| BA-SU-CO-583 | BC-6340 | 2022-11-08 | Product Management |
| VE-SU-CO-237 | BC-6345 | 2021-04-10 | Data Governance |
| HO-LO-699 | BC-6351 | 2024-06-17 | Finance |
| PA-MA-664 | TC-6356 | 2024-09-23 | Operations |
| NE-SO-810 | BC-6367 | 2024-02-12 | Finance |
| HO-SO-924 | BC-6372 | 2024-06-25 | Finance |
| ST-MA-641 | BC-6380 | 2024-04-21 | Finance |
| NE-MA-103 | TC-6386 | 2022-05-07 | Product Management |
| CO-LO-520 | TC-6390 | 2022-01-19 | Data Governance |
| AP-SO-687 | IC-6398 | 2024-08-15 | Data Governance |
| AT-SO-658 | BC-6403 | 2024-04-09 | Data Governance |
| PA-MA-602 | IC-6410 | 2021-09-08 | Product Management |
| CO-LO-137 | TC-6421 | 2023-12-26 | IT Infrastructure |
| PA-SU-CO-864 | IC-6427 | 2022-05-14 | Supply Chain |
| HO-LO-886 | TC-6432 | 2024-04-19 | Data Governance |
| QU-LO-333 | BC-6443 | 2023-01-05 | Finance |
| ST-LO-927 | TC-6456 | 2022-01-06 | Data Governance |
| PR-SU-CO-333 | IC-6462 | 2024-10-09 | Compliance |
| PR-SU-CO-832 | BC-6469 | 2022-01-03 | Compliance |
| AT-LO-914 | BC-6476 | 2024-12-13 | Operations |
| CE-SU-CO-752 | BC-6483 | 2021-06-20 | Compliance |
| PR-SU-CO-187 | BC-6489 | 2024-07-21 | Finance |
| ZE-LO-372 | IC-6492 | 2022-08-26 | Data Governance |
| PI-SO-251 | IC-6498 | 2023-06-27 | Finance |
| PI-MA-133 | TC-6513 | 2021-05-15 | Data Governance |
| PA-MA-102 | BC-6516 | 2022-04-03 | Operations |
| AT-MA-739 | BC-6519 | 2022-01-13 | Compliance |
| CO-MA-295 | IC-6535 | 2022-02-07 | IT Infrastructure |
| AT-MA-510 | TC-6540 | 2023-06-07 | Product Management |
| ME-SU-CO-314 | BC-6544 | 2021-08-27 | Finance |
| NO-LO-524 | BC-6550 | 2021-10-05 | Data Governance |
| AT-SU-CO-755 | IC-6555 | 2024-04-07 | Compliance |
| ZE-LO-524 | TC-6558 | 2023-04-12 | Product Management |
| CA-MA-271 | TC-6566 | 2024-05-26 | Operations |
| QU-MA-886 | IC-6572 | 2022-09-12 | Data Governance |
| CO-SO-442 | BC-6578 | 2024-06-04 | Data Governance |
| VA-MA-951 | IC-6581 | 2021-04-10 | Finance |
| CA-MA-129 | TC-6589 | 2024-01-28 | Product Management |
| PI-LO-142 | TC-6593 | 2023-12-27 | IT Infrastructure |
| PR-SU-CO-552 | TC-6602 | 2023-02-01 | Operations |
| ME-LO-583 | IC-6605 | 2021-08-12 | Compliance |
| AT-MA-246 | BC-6612 | 2021-08-07 | Finance |
| ME-MA-989 | BC-6619 | 2022-02-20 | Finance |
| PI-MA-112 | BC-6624 | 2021-07-17 | Operations |
| PR-MA-428 | BC-6630 | 2023-10-05 | Finance |
| AT-SO-790 | IC-6633 | 2021-06-14 | Compliance |
| CE-LO-713 | IC-6637 | 2024-03-03 | Operations |
| EL-LO-188 | TC-6643 | 2024-04-08 | Finance |
| PR-LO-351 | IC-6650 | 2021-11-24 | Product Management |
| CO-SO-534 | IC-6656 | 2021-10-15 | Product Management |
| NE-LO-125 | BC-6660 | 2023-10-25 | Operations |
| GL-LO-494 | BC-6664 | 2021-08-22 | Compliance |
| EL-MA-832 | TC-6674 | 2023-03-09 | Operations |
| PI-SO-767 | BC-6679 | 2023-09-09 | Compliance |
| VE-SO-366 | BC-6685 | 2021-11-21 | Compliance |
| VE-MA-682 | IC-6694 | 2024-01-17 | Data Governance |
| NE-MA-849 | BC-6704 | 2024-10-27 | IT Infrastructure |
| PA-LO-674 | BC-6708 | 2024-12-26 | Finance |
| PA-SO-568 | TC-6713 | 2023-06-21 | Supply Chain |
| QU-SU-CO-890 | IC-6720 | 2022-04-10 | Supply Chain |
| PA-SO-999 | TC-6727 | 2023-06-15 | Data Governance |
| PR-LO-393 | BC-6730 | 2024-09-01 | IT Infrastructure |
| PR-SO-270 | TC-6737 | 2024-03-26 | Supply Chain |
| PI-SU-CO-216 | IC-6766 | 2022-05-16 | IT Infrastructure |
| AT-MA-363 | TC-6774 | 2022-09-04 | Compliance |
| AT-SU-CO-808 | IC-6781 | 2024-10-14 | Supply Chain |
| NO-SU-CO-498 | BC-6784 | 2023-06-02 | IT Infrastructure |
| AT-SU-CO-945 | IC-6792 | 2023-10-24 | Operations |
| AT-SU-CO-645 | TC-6800 | 2023-01-01 | Data Governance |
| ST-MA-342 | TC-6802 | 2024-06-28 | IT Infrastructure |
| HO-LO-948 | TC-6806 | 2022-05-21 | Operations |
| BA-MA-998 | TC-6808 | 2023-02-06 | Compliance |
| PA-MA-435 | TC-6832 | 2023-08-14 | Finance |
| ST-LO-136 | TC-6837 | 2021-06-06 | Data Governance |
| QU-SU-CO-890 | TC-6846 | 2023-10-18 | IT Infrastructure |
| AP-SU-CO-787 | IC-6858 | 2022-08-11 | Product Management |
| PR-LO-862 | BC-6864 | 2022-02-21 | Compliance |
| QU-SO-261 | IC-6869 | 2021-03-21 | Operations |
| AT-SO-226 | IC-6872 | 2023-09-15 | Product Management |
| PI-SU-CO-998 | BC-6876 | 2021-10-01 | Product Management |
| BA-SO-776 | IC-6880 | 2023-05-22 | Data Governance |
| PR-SO-757 | TC-6897 | 2022-11-07 | Product Management |
| PR-MA-605 | TC-6906 | 2022-02-12 | Finance |
| CE-SO-204 | BC-6909 | 2022-02-27 | Product Management |
| CE-MA-981 | BC-6913 | 2023-05-19 | Compliance |
| AT-SO-339 | TC-6925 | 2024-12-01 | Supply Chain |
| BA-SO-633 | BC-6928 | 2023-07-02 | Compliance |
| VE-LO-693 | BC-6931 | 2024-03-20 | Product Management |
| AT-MA-893 | IC-6937 | 2023-06-28 | Compliance |
| NE-SO-476 | IC-6941 | 2022-02-23 | Data Governance |
| PR-MA-686 | IC-6956 | 2022-01-05 | Finance |
| AT-MA-245 | IC-6962 | 2023-04-04 | Operations |
| QU-LO-616 | IC-6967 | 2022-07-10 | Supply Chain |
| VE-MA-908 | TC-6970 | 2024-11-06 | Finance |
| AT-LO-628 | BC-6977 | 2022-04-01 | Product Management |
| AP-SO-576 | BC-6987 | 2023-03-07 | Data Governance |
| AP-SU-CO-722 | IC-6991 | 2021-07-09 | Product Management |
| AP-SU-CO-814 | IC-7002 | 2021-04-28 | Compliance |
| AT-SO-260 | TC-7010 | 2023-10-17 | IT Infrastructure |
| VA-LO-248 | IC-7015 | 2021-12-17 | Data Governance |
| NO-MA-958 | TC-7023 | 2023-02-18 | Data Governance |
| PI-SO-952 | BC-7027 | 2021-09-19 | Finance |
| ME-LO-731 | TC-7037 | 2023-05-26 | Finance |
| PI-SU-CO-364 | TC-7044 | 2022-09-09 | Data Governance |
| PA-LO-434 | IC-7054 | 2022-07-12 | Supply Chain |
| ST-LO-637 | TC-7057 | 2021-09-25 | Compliance |
| CO-SU-CO-353 | BC-7065 | 2021-03-01 | Compliance |
| ST-MA-703 | BC-7068 | 2022-04-08 | Supply Chain |
| NE-SO-394 | TC-7071 | 2021-07-15 | Finance |
| VA-SU-CO-459 | BC-7077 | 2022-10-23 | Data Governance |
| VE-SU-CO-566 | IC-7079 | 2023-03-08 | Product Management |
| ST-MA-730 | IC-7085 | 2023-02-18 | Supply Chain |
| AT-SU-CO-811 | BC-7093 | 2024-02-21 | Compliance |
| ZE-SU-CO-723 | BC-7103 | 2022-10-26 | Product Management |
| PR-LO-360 | TC-7113 | 2024-08-08 | IT Infrastructure |
| PA-SU-CO-905 | IC-7124 | 2021-04-28 | Product Management |
| PR-MA-161 | BC-7128 | 2021-10-27 | Operations |
| VA-RE-G-15-665 | IC-7136 | 2022-01-05 | Product Management |
| EX-N-0-751 | TC-7145 | 2021-01-12 | Product Management |
| EX-D-7-182 | IC-7147 | 2023-03-13 | Supply Chain |
| VA-ST-N-25-114 | BC-7153 | 2022-08-22 | Supply Chain |
| WI-G-5-718 | TC-7166 | 2022-10-27 | IT Infrastructure |
| VA-RE-N-7-243 | TC-7172 | 2022-05-27 | Data Governance |
| CU-DU-C-0-728 | TC-7177 | 2021-12-22 | Finance |
| VA-ST-G-21-683 | BC-7181 | 2023-08-14 | Product Management |
| CU-DU-B-15-379 | IC-7187 | 2023-08-13 | Finance |
| VA-ST-D-19-529 | BC-7192 | 2021-02-14 | Supply Chain |
| VA-ST-I-0-862 | IC-7195 | 2021-06-23 | Compliance |
| CU-DU-G-5-599 | BC-7198 | 2021-07-27 | Data Governance |
| VA-ST-N-20-984 | TC-7210 | 2021-04-08 | IT Infrastructure |
| VA-ST-N-20-275 | IC-7226 | 2023-10-10 | Supply Chain |
| WI-U-0-465 | BC-7231 | 2022-01-10 | Supply Chain |
| VA-ST-D-10-295 | IC-7253 | 2023-09-15 | Supply Chain |
| EX-F-0-883 | BC-7266 | 2023-01-26 | Finance |
| VA-RE-G-25-207 | TC-7274 | 2021-09-28 | Product Management |
| EX-B-10-648 | BC-7281 | 2023-05-21 | Data Governance |
| EX-I-15-456 | BC-7285 | 2022-10-21 | Data Governance |
| WI-B-5-537 | BC-7290 | 2021-04-08 | Supply Chain |
| VA-RE-B-21-369 | TC-7308 | 2021-10-11 | Compliance |
| VA-ST-B-0-553 | IC-7319 | 2021-03-13 | IT Infrastructure |
| VA-ST-F-25-272 | IC-7326 | 2023-06-01 | Data Governance |
| VA-RE-C-19-228 | IC-7333 | 2023-01-18 | Operations |
| VA-ST-F-19-413 | IC-7334 | 2022-03-23 | Product Management |
| CU-DU-F-19-568 | BC-7340 | 2022-01-14 | Supply Chain |
| VA-RE-B-10-727 | TC-7343 | 2023-06-01 | Data Governance |
| WI-G-21-298 | IC-7350 | 2024-12-18 | Finance |
| VA-RE-B-25-739 | IC-7354 | 2022-11-07 | Finance |
| VA-ST-G-20-932 | IC-7370 | 2021-12-06 | Compliance |
| CU-DU-I-5-731 | BC-7376 | 2022-11-01 | Compliance |
| CU-DU-D-5-375 | IC-7381 | 2023-07-28 | Compliance |
| VA-RE-G-19-221 | BC-7390 | 2024-06-17 | Operations |
| EX-B-15-715 | BC-7398 | 2024-06-04 | Supply Chain |
| VA-RE-F-25-555 | TC-7405 | 2021-12-12 | Operations |
| VA-RE-I-5-252 | TC-7409 | 2021-09-13 | Product Management |
| VA-RE-F-25-707 | IC-7416 | 2022-08-15 | Product Management |
| VA-ST-U-10-638 | TC-7419 | 2024-02-14 | Finance |
| WI-N-7-197 | TC-7425 | 2023-08-06 | Supply Chain |
| EX-N-7-638 | IC-7433 | 2022-01-24 | IT Infrastructure |
| EX-U-15-972 | BC-7445 | 2023-08-15 | Operations |
| WI-D-25-711 | TC-7452 | 2022-02-03 | Operations |
| WI-U-10-721 | IC-7456 | 2023-11-19 | Supply Chain |
| EX-N-21-396 | BC-7464 | 2022-07-25 | IT Infrastructure |
| CU-DU-B-7-760 | TC-7468 | 2021-10-08 | Finance |
| EX-U-19-672 | TC-7471 | 2021-01-01 | Product Management |
| VA-RE-G-25-615 | TC-7475 | 2022-02-19 | Product Management |
| WI-F-19-763 | BC-7480 | 2024-03-04 | Operations |
| WI-F-21-666 | IC-7488 | 2021-01-21 | Operations |
| VA-RE-B-7-231 | TC-7492 | 2024-03-06 | Supply Chain |
| VA-RE-I-20-892 | IC-7499 | 2024-05-17 | Operations |
| VA-RE-F-0-158 | TC-7517 | 2023-10-17 | Product Management |
| CU-DU-U-10-283 | IC-7524 | 2023-07-18 | Compliance |
| EX-I-20-615 | BC-7536 | 2023-09-10 | Product Management |
| VA-RE-N-19-835 | IC-7553 | 2024-10-10 | Finance |
| CU-DU-U-15-275 | TC-7563 | 2022-05-09 | Compliance |
| WI-F-5-421 | TC-7574 | 2023-02-18 | Supply Chain |
| EX-B-25-579 | TC-7578 | 2023-10-01 | Data Governance |
| EX-N-20-817 | IC-7588 | 2022-10-15 | IT Infrastructure |
| VA-ST-I-10-511 | BC-7596 | 2022-01-08 | Operations |
| CU-DU-C-25-424 | TC-7601 | 2021-04-20 | Finance |
| CU-DU-U-19-893 | TC-7609 | 2024-12-15 | Finance |
| VA-ST-C-10-748 | TC-7619 | 2021-02-23 | Data Governance |
| CU-DU-D-5-294 | IC-7625 | 2023-02-08 | Operations |
| EX-D-10-430 | IC-7628 | 2023-01-17 | Product Management |
| EX-G-25-188 | TC-7636 | 2021-03-01 | Finance |
| CU-DU-I-25-812 | TC-7652 | 2023-06-19 | Product Management |
| EX-U-20-144 | BC-7660 | 2023-03-18 | Compliance |
| CU-DU-I-21-633 | IC-7673 | 2022-05-11 | Product Management |
| CU-DU-B-7-411 | IC-7677 | 2023-09-13 | Data Governance |
| WI-B-10-184 | TC-7684 | 2022-12-16 | Data Governance |
| VA-RE-B-19-480 | IC-7698 | 2024-06-01 | Operations |
| VA-ST-N-19-482 | TC-7701 | 2021-07-09 | Finance |
| CU-DU-D-0-383 | IC-7710 | 2024-09-02 | Data Governance |
| VA-RE-C-19-648 | BC-7715 | 2021-02-03 | Supply Chain |
| VA-ST-N-5-804 | BC-7720 | 2021-07-20 | Compliance |
| EX-N-19-830 | TC-7726 | 2024-04-08 | Data Governance |
| CU-DU-C-25-616 | IC-7730 | 2021-08-21 | Compliance |
| WI-F-5-977 | TC-7737 | 2022-10-17 | Data Governance |
| VA-ST-F-20-240 | IC-7746 | 2022-11-18 | IT Infrastructure |
| EX-B-19-908 | TC-7747 | 2023-05-15 | Compliance |
| VA-ST-I-5-735 | BC-7754 | 2024-06-05 | IT Infrastructure |
| CU-DU-F-15-864 | IC-7763 | 2021-02-15 | Operations |
| CU-DU-G-0-297 | TC-7771 | 2022-03-25 | Product Management |
| EX-C-21-240 | IC-7774 | 2024-07-01 | Supply Chain |
| VA-RE-B-10-482 | IC-7780 | 2021-08-06 | Operations |
| CU-DU-G-5-181 | IC-7791 | 2021-10-13 | IT Infrastructure |
| CU-DU-C-7-106 | IC-7797 | 2023-11-09 | Operations |
| VA-RE-N-20-326 | BC-7801 | 2023-07-26 | Finance |
| CU-DU-D-0-955 | TC-7808 | 2022-04-01 | Compliance |
| VA-ST-G-19-277 | TC-7815 | 2023-04-25 | Product Management |
| CU-DU-F-7-469 | TC-7823 | 2024-07-15 | Data Governance |
| VA-ST-I-19-287 | BC-7829 | 2022-02-17 | IT Infrastructure |
| WI-C-20-252 | IC-7836 | 2024-10-19 | Finance |
| EX-U-7-320 | IC-7841 | 2021-06-28 | Product Management |
| VA-ST-N-5-192 | TC-7851 | 2022-06-23 | IT Infrastructure |
| VA-RE-C-19-810 | BC-7864 | 2021-12-02 | Product Management |
| CU-DU-N-5-217 | IC-7873 | 2024-06-09 | IT Infrastructure |
| EX-G-5-484 | BC-7881 | 2023-04-23 | IT Infrastructure |
| EX-B-19-306 | BC-7889 | 2021-07-17 | IT Infrastructure |
| VA-RE-N-5-825 | IC-7896 | 2023-05-03 | Finance |
| VA-ST-G-19-945 | IC-7907 | 2022-03-02 | Operations |
| EX-N-21-216 | IC-7910 | 2023-12-09 | Operations |
| CU-DU-B-20-301 | TC-7919 | 2023-05-06 | Compliance |
| EX-U-5-517 | TC-7926 | 2023-12-02 | Supply Chain |
| CU-DU-G-5-714 | TC-7933 | 2021-05-06 | Operations |
| VA-ST-N-20-162 | TC-7941 | 2021-08-24 | Compliance |
| WI-C-0-413 | BC-7946 | 2022-12-17 | Operations |
| WI-B-20-331 | BC-7957 | 2021-01-25 | Supply Chain |
| EX-C-21-179 | TC-7959 | 2023-09-16 | IT Infrastructure |
| VA-RE-C-10-444 | BC-7964 | 2023-01-19 | Data Governance |
| CU-DU-G-0-770 | TC-7970 | 2024-01-17 | IT Infrastructure |
| VA-RE-F-10-219 | BC-7974 | 2022-09-04 | IT Infrastructure |
| WI-I-10-242 | BC-7984 | 2023-04-04 | Finance |
| EX-C-20-948 | IC-7991 | 2023-12-09 | Supply Chain |
| VA-RE-N-0-932 | BC-7999 | 2022-07-06 | IT Infrastructure |
| VA-RE-G-15-592 | BC-8012 | 2021-08-21 | Data Governance |
| EX-C-25-332 | TC-8019 | 2022-12-06 | IT Infrastructure |
| EX-N-0-354 | BC-8024 | 2021-01-10 | IT Infrastructure |
| VA-RE-N-25-962 | BC-8034 | 2022-06-16 | Product Management |
| CU-DU-N-7-394 | TC-8042 | 2024-01-11 | Data Governance |
| WI-G-15-758 | TC-8047 | 2023-05-03 | Product Management |
| VA-RE-G-0-937 | IC-8055 | 2022-04-09 | Product Management |
| WI-N-20-376 | BC-8063 | 2021-04-22 | Data Governance |
| EX-F-19-312 | IC-8071 | 2023-09-06 | Supply Chain |
| WI-I-20-664 | TC-8077 | 2023-11-06 | Supply Chain |
| EX-F-21-883 | BC-8082 | 2021-11-05 | Supply Chain |
| CU-DU-N-25-811 | IC-8088 | 2023-04-25 | Finance |
| CU-DU-G-7-636 | TC-8091 | 2023-03-28 | Compliance |
| CU-DU-I-5-886 | IC-8099 | 2021-07-13 | Product Management |
| WI-N-21-538 | IC-8104 | 2024-10-19 | Data Governance |
| CU-DU-N-21-524 | BC-8115 | 2022-06-08 | IT Infrastructure |
| WI-N-5-784 | IC-8121 | 2023-10-22 | Data Governance |
| VA-ST-N-19-883 | BC-8128 | 2023-11-05 | Data Governance |
| CU-DU-N-15-558 | TC-8132 | 2024-05-24 | Product Management |
| VA-ST-N-20-254 | BC-8139 | 2022-10-15 | Finance |
| EX-N-10-872 | BC-8154 | 2024-03-24 | Finance |
| WI-N-15-362 | IC-8172 | 2023-06-27 | Data Governance |
| CU-DU-D-20-742 | IC-8186 | 2024-03-01 | Operations |
| WI-N-21-724 | BC-8195 | 2024-11-25 | Supply Chain |
| VA-RE-I-25-366 | IC-8204 | 2024-11-02 | Compliance |
| VA-ST-U-15-204 | TC-8220 | 2021-02-05 | Finance |
| VA-ST-F-0-740 | TC-8226 | 2023-07-23 | Product Management |
| CU-DU-F-25-387 | TC-8235 | 2024-05-28 | Finance |
| VA-RE-I-5-890 | IC-8244 | 2021-06-22 | Data Governance |
| WI-F-15-675 | TC-8250 | 2021-02-02 | Operations |
| VA-ST-D-7-855 | BC-8258 | 2024-07-23 | Product Management |
| VA-ST-C-19-533 | TC-8266 | 2022-09-03 | Operations |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| SO-CH-70-GR-B-821 | IC-8389 | PROVISIONAL | Historical - verify before use |
| FR-GR-A-600 | IC-7776 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-223 | IC-8715 | PROVISIONAL | Historical - verify before use |
| AS-AC-782 | IC-8266 | DEPRECATED | Historical - verify before use |
| SU-OI-98-PR-692 | IC-8407 | SUPERSEDED | Historical - verify before use |
| CY-763 | IC-5778 | PROVISIONAL | Historical - verify before use |
| PE-PR-99.5-863 | IC-7560 | SUPERSEDED | Historical - verify before use |
| AS-AC-GR-B-395 | IC-8496 | PROVISIONAL | Historical - verify before use |
| LA-AC-690 | IC-7560 | PROVISIONAL | Historical - verify before use |
| AS-AC-PH-GR-192 | IC-7088 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-FO-GR-162 | IC-8066 | DEPRECATED | Historical - verify before use |
| RA-OI-258 | IC-6250 | SUPERSEDED | Historical - verify before use |
| SO-BE-25-ST-520 | IC-8885 | SUPERSEDED | Historical - verify before use |
| CO-OI-966 | IC-5549 | SUPERSEDED | Historical - verify before use |
| CO-OI-98-890 | IC-5747 | REVIEW REQUIRED | Historical - verify before use |
| SO-BE-99.5-GR-A-143 | IC-5699 | SUPERSEDED | Historical - verify before use |
| SO-BE-99.5-ST-342 | IC-5763 | SUPERSEDED | Historical - verify before use |
| CY-98-PH-GR-614 | IC-8537 | SUPERSEDED | Historical - verify before use |
| CO-OI-GR-A-370 | IC-5791 | PROVISIONAL | Historical - verify before use |
| SO-AC-PH-GR-274 | IC-8052 | REVIEW REQUIRED | Historical - verify before use |
| DE-ST-385 | IC-6065 | PROVISIONAL | Historical - verify before use |
| LA-AC-99.5-GR-B-756 | IC-9557 | DEPRECATED | Historical - verify before use |
| LA-AC-393 | IC-5491 | REVIEW REQUIRED | Historical - verify before use |
| PO-SO-560 | IC-9804 | REVIEW REQUIRED | Historical - verify before use |
| SO-BE-99.5-195 | IC-9600 | DEPRECATED | Historical - verify before use |
| SO-BE-PH-GR-647 | IC-9601 | SUPERSEDED | Historical - verify before use |
| PA-OI-50-PR-573 | IC-7700 | SUPERSEDED | Historical - verify before use |
| IS-878 | IC-6001 | PROVISIONAL | Historical - verify before use |
| SO-IS-25-TE-320 | IC-8365 | PROVISIONAL | Historical - verify before use |
| FR-108 | IC-7896 | PROVISIONAL | Historical - verify before use |
| RA-OI-745 | IC-8464 | SUPERSEDED | Historical - verify before use |
| RE-ST-463 | IC-5421 | DEPRECATED | Historical - verify before use |
| FR-278 | IC-7356 | DEPRECATED | Historical - verify before use |
| GL-SY-371 | IC-9918 | REVIEW REQUIRED | Historical - verify before use |
| SO-AC-25-GR-B-198 | IC-7559 | PROVISIONAL | Historical - verify before use |
| CA-ST-375 | IC-7880 | SUPERSEDED | Historical - verify before use |
| CA-CA-98-785 | IC-5848 | SUPERSEDED | Historical - verify before use |
| PA-OI-ST-879 | IC-9734 | SUPERSEDED | Historical - verify before use |
| MA-DE-GR-A-871 | IC-9156 | SUPERSEDED | Historical - verify before use |
| SO-AC-FO-GR-175 | IC-6742 | SUPERSEDED | Historical - verify before use |
| LA-AC-98-226 | IC-6267 | PROVISIONAL | Historical - verify before use |
| AS-AC-279 | IC-8950 | PROVISIONAL | Historical - verify before use |
| CO-OI-25-ST-613 | IC-6837 | PROVISIONAL | Historical - verify before use |
| CI-AC-634 | IC-5886 | SUPERSEDED | Historical - verify before use |
| CI-AC-PH-GR-209 | IC-7868 | DEPRECATED | Historical - verify before use |
| LA-AC-GR-A-486 | IC-9556 | DEPRECATED | Historical - verify before use |
| PA-OI-98-587 | IC-8011 | PROVISIONAL | Historical - verify before use |
| SU-OI-50-GR-A-521 | IC-5941 | PROVISIONAL | Historical - verify before use |
| SO-AC-98-741 | IC-7282 | PROVISIONAL | Historical - verify before use |
| RE-ST-98-PH-GR-372 | IC-9703 | SUPERSEDED | Historical - verify before use |
| DE-635 | IC-6852 | DEPRECATED | Historical - verify before use |
| MA-DE-641 | IC-8515 | SUPERSEDED | Historical - verify before use |
| DE-25-TE-737 | IC-9595 | REVIEW REQUIRED | Historical - verify before use |
| LA-AC-FO-GR-553 | IC-9560 | REVIEW REQUIRED | Historical - verify before use |
| SO-AC-852 | IC-5215 | DEPRECATED | Historical - verify before use |
| DE-PH-GR-282 | IC-9988 | PROVISIONAL | Historical - verify before use |
| CI-AC-99.5-638 | IC-7190 | SUPERSEDED | Historical - verify before use |
| SO-BE-PR-691 | IC-5237 | SUPERSEDED | Historical - verify before use |
| DE-515 | IC-6477 | SUPERSEDED | Historical - verify before use |
| CO-OI-ST-153 | IC-7238 | SUPERSEDED | Historical - verify before use |
| CI-AC-99.5-440 | IC-7531 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-GR-B-598 | IC-7783 | DEPRECATED | Historical - verify before use |
| CA-CA-50-GR-B-200 | IC-7875 | PROVISIONAL | Historical - verify before use |
| SO-IS-25-323 | IC-5050 | DEPRECATED | Historical - verify before use |
| RA-OI-99.5-602 | IC-6486 | SUPERSEDED | Historical - verify before use |
| GL-SY-98-FO-GR-198 | IC-6173 | DEPRECATED | Historical - verify before use |
| SO-IS-25-PH-GR-832 | IC-9639 | PROVISIONAL | Historical - verify before use |
| DE-GR-A-250 | IC-8283 | PROVISIONAL | Historical - verify before use |
| SO-CH-GR-A-776 | IC-5570 | SUPERSEDED | Historical - verify before use |
| CO-OI-98-GR-A-763 | IC-6162 | DEPRECATED | Historical - verify before use |
| RE-ST-TE-614 | IC-5251 | SUPERSEDED | Historical - verify before use |
| DE-50-891 | IC-5751 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-98-GR-B-961 | IC-9345 | DEPRECATED | Historical - verify before use |
| GL-SY-TE-803 | IC-6762 | DEPRECATED | Historical - verify before use |
| SO-IS-99.5-PR-187 | IC-8081 | DEPRECATED | Historical - verify before use |
| PE-PR-GR-B-793 | IC-8439 | SUPERSEDED | Historical - verify before use |
| SO-IS-98-430 | IC-8716 | REVIEW REQUIRED | Historical - verify before use |
| DE-840 | IC-7792 | REVIEW REQUIRED | Historical - verify before use |
| WH-GL-GR-B-926 | IC-6289 | PROVISIONAL | Historical - verify before use |
| GL-SY-70-549 | IC-8031 | DEPRECATED | Historical - verify before use |
| SU-OI-ST-338 | IC-7552 | DEPRECATED | Historical - verify before use |
| SO-IS-25-ST-345 | IC-7657 | DEPRECATED | Historical - verify before use |
| AS-AC-99.5-PR-761 | IC-9649 | DEPRECATED | Historical - verify before use |
| SO-IS-GR-A-940 | IC-9884 | PROVISIONAL | Historical - verify before use |
| DE-TE-380 | IC-5695 | PROVISIONAL | Historical - verify before use |
| PA-OI-632 | IC-5430 | REVIEW REQUIRED | Historical - verify before use |
| PO-SO-763 | IC-6274 | PROVISIONAL | Historical - verify before use |
| FR-99.5-PH-GR-378 | IC-6289 | PROVISIONAL | Historical - verify before use |
| SO-BE-700 | IC-5407 | SUPERSEDED | Historical - verify before use |
| PA-OI-70-GR-B-781 | IC-5668 | DEPRECATED | Historical - verify before use |
| SO-BE-25-774 | IC-7229 | SUPERSEDED | Historical - verify before use |
| SO-CH-70-365 | IC-8629 | SUPERSEDED | Historical - verify before use |
| CA-PR-568 | IC-8473 | DEPRECATED | Historical - verify before use |
| SO-CH-99.5-618 | IC-8978 | SUPERSEDED | Historical - verify before use |
| AS-AC-TE-342 | IC-9973 | DEPRECATED | Historical - verify before use |
| FR-25-GR-B-641 | IC-8621 | PROVISIONAL | Historical - verify before use |
| SO-CH-758 | IC-8392 | REVIEW REQUIRED | Historical - verify before use |
| DE-ST-213 | IC-7237 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-358 | IC-6765 | PROVISIONAL | Historical - verify before use |
| CO-OI-99.5-PH-GR-944 | IC-9197 | PROVISIONAL | Historical - verify before use |
| IS-70-838 | IC-5932 | SUPERSEDED | Historical - verify before use |
| DE-FO-GR-588 | IC-7827 | REVIEW REQUIRED | Historical - verify before use |
| PA-OI-50-273 | IC-8521 | REVIEW REQUIRED | Historical - verify before use |
| AS-AC-98-PR-217 | IC-5908 | PROVISIONAL | Historical - verify before use |
| SO-AC-70-785 | IC-7320 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-ST-522 | IC-9858 | DEPRECATED | Historical - verify before use |
| IS-PR-125 | IC-8986 | PROVISIONAL | Historical - verify before use |
| CI-AC-25-GR-A-669 | IC-9316 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-25-PR-784 | IC-7526 | PROVISIONAL | Historical - verify before use |
| CA-CA-GR-B-761 | IC-5372 | REVIEW REQUIRED | Historical - verify before use |
| SO-IS-275 | IC-6806 | SUPERSEDED | Historical - verify before use |
| DE-602 | IC-8237 | REVIEW REQUIRED | Historical - verify before use |
| WH-GL-830 | IC-9909 | DEPRECATED | Historical - verify before use |
| FR-FO-GR-823 | IC-5448 | DEPRECATED | Historical - verify before use |
| AS-AC-70-133 | IC-5062 | DEPRECATED | Historical - verify before use |
| SO-IS-50-GR-B-983 | IC-6674 | PROVISIONAL | Historical - verify before use |
| CY-926 | IC-7469 | DEPRECATED | Historical - verify before use |
| AS-AC-165 | IC-6730 | SUPERSEDED | Historical - verify before use |
| DE-25-TE-949 | IC-6124 | REVIEW REQUIRED | Historical - verify before use |
| IS-FO-GR-555 | IC-7093 | SUPERSEDED | Historical - verify before use |
| DE-70-856 | IC-7371 | REVIEW REQUIRED | Historical - verify before use |
| PE-PR-50-128 | IC-7687 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-PR-862 | IC-5982 | DEPRECATED | Historical - verify before use |
| CI-AC-215 | IC-5063 | PROVISIONAL | Historical - verify before use |
| GL-SY-TE-601 | IC-9074 | PROVISIONAL | Historical - verify before use |
| RA-OI-TE-584 | IC-8527 | PROVISIONAL | Historical - verify before use |
| GL-SY-98-ST-578 | IC-6439 | PROVISIONAL | Historical - verify before use |
| IS-50-TE-886 | IC-6058 | SUPERSEDED | Historical - verify before use |
| SO-BE-99.5-TE-213 | IC-8114 | PROVISIONAL | Historical - verify before use |
| SO-BE-GR-B-914 | IC-9362 | SUPERSEDED | Historical - verify before use |
| DE-TE-414 | IC-6885 | SUPERSEDED | Historical - verify before use |
| AS-AC-ST-243 | IC-9098 | PROVISIONAL | Historical - verify before use |
| CI-AC-FO-GR-293 | IC-9577 | PROVISIONAL | Historical - verify before use |
| WH-GL-GR-B-129 | IC-7901 | DEPRECATED | Historical - verify before use |
| CA-TE-562 | IC-5590 | REVIEW REQUIRED | Historical - verify before use |
| GL-SY-98-939 | IC-8252 | SUPERSEDED | Historical - verify before use |
| RA-OI-70-PR-405 | IC-5346 | REVIEW REQUIRED | Historical - verify before use |
| CI-AC-99.5-469 | IC-8573 | SUPERSEDED | Historical - verify before use |
| PA-OI-383 | IC-5153 | REVIEW REQUIRED | Historical - verify before use |
| RA-OI-431 | IC-8766 | SUPERSEDED | Historical - verify before use |
| PA-OI-98-856 | IC-5637 | DEPRECATED | Historical - verify before use |
| FR-GR-B-231 | IC-7564 | SUPERSEDED | Historical - verify before use |
| AS-AC-70-347 | IC-9716 | PROVISIONAL | Historical - verify before use |
| CI-AC-857 | IC-8516 | SUPERSEDED | Historical - verify before use |
| LA-AC-70-PH-GR-221 | IC-9697 | DEPRECATED | Historical - verify before use |
| PO-SO-GR-A-715 | IC-8313 | DEPRECATED | Historical - verify before use |
| SO-CH-881 | IC-8421 | DEPRECATED | Historical - verify before use |
| FR-113 | IC-7371 | PROVISIONAL | Historical - verify before use |
| SO-BE-GR-A-760 | IC-5943 | SUPERSEDED | Historical - verify before use |
| FR-GR-B-311 | IC-8318 | REVIEW REQUIRED | Historical - verify before use |
| AS-AC-130 | IC-5170 | SUPERSEDED | Historical - verify before use |
| PE-PR-PR-428 | IC-7660 | DEPRECATED | Historical - verify before use |
| FR-124 | IC-6407 | REVIEW REQUIRED | Historical - verify before use |
| RA-OI-98-679 | IC-8769 | DEPRECATED | Historical - verify before use |
| PO-SO-50-GR-B-154 | IC-7964 | REVIEW REQUIRED | Historical - verify before use |
| MA-DE-944 | IC-5721 | PROVISIONAL | Historical - verify before use |
| PA-OI-70-780 | IC-8577 | REVIEW REQUIRED | Historical - verify before use |
| PE-PR-98-GR-B-195 | IC-5867 | REVIEW REQUIRED | Historical - verify before use |
| SO-IS-FO-GR-334 | IC-6993 | DEPRECATED | Historical - verify before use |
| GL-SY-70-655 | IC-8569 | PROVISIONAL | Historical - verify before use |
| DE-GR-A-351 | IC-9824 | SUPERSEDED | Historical - verify before use |
| LA-AC-554 | IC-8280 | DEPRECATED | Historical - verify before use |
| CA-CA-50-GR-A-195 | IC-9292 | SUPERSEDED | Historical - verify before use |
| PO-SO-339 | IC-5644 | DEPRECATED | Historical - verify before use |
| LA-AC-TE-651 | IC-8242 | SUPERSEDED | Historical - verify before use |
| DE-25-260 | IC-7541 | SUPERSEDED | Historical - verify before use |
| DE-GR-B-942 | IC-7781 | SUPERSEDED | Historical - verify before use |
| RE-ST-GR-B-677 | IC-6815 | SUPERSEDED | Historical - verify before use |
| LA-AC-GR-A-949 | IC-7728 | PROVISIONAL | Historical - verify before use |
| DE-GR-A-512 | IC-6377 | PROVISIONAL | Historical - verify before use |
| AS-AC-99.5-619 | IC-5625 | DEPRECATED | Historical - verify before use |
| SO-CH-98-657 | IC-9181 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-752 | IC-5934 | PROVISIONAL | Historical - verify before use |
| PE-PR-25-PH-GR-591 | IC-9346 | DEPRECATED | Historical - verify before use |
| PE-PR-TE-718 | IC-9177 | SUPERSEDED | Historical - verify before use |
| MA-DE-PR-303 | IC-6588 | PROVISIONAL | Historical - verify before use |
| GL-SY-533 | IC-7862 | SUPERSEDED | Historical - verify before use |
| SO-IS-354 | IC-7876 | SUPERSEDED | Historical - verify before use |
| RE-ST-676 | IC-6209 | PROVISIONAL | Historical - verify before use |
| PO-SO-ST-111 | IC-6935 | SUPERSEDED | Historical - verify before use |
| LA-AC-FO-GR-469 | IC-5842 | REVIEW REQUIRED | Historical - verify before use |
| CI-AC-25-TE-484 | IC-6199 | REVIEW REQUIRED | Historical - verify before use |
| DE-50-727 | IC-7096 | SUPERSEDED | Historical - verify before use |
| IS-230 | IC-6616 | SUPERSEDED | Historical - verify before use |
| SO-IS-50-GR-B-346 | IC-6421 | SUPERSEDED | Historical - verify before use |
| PE-PR-929 | IC-9934 | SUPERSEDED | Historical - verify before use |
| WH-GL-GR-A-583 | IC-6252 | REVIEW REQUIRED | Historical - verify before use |
| PA-OI-25-GR-A-241 | IC-5617 | REVIEW REQUIRED | Historical - verify before use |
| RA-OI-GR-A-272 | IC-6451 | REVIEW REQUIRED | Historical - verify before use |
| DE-70-GR-A-741 | IC-9047 | REVIEW REQUIRED | Historical - verify before use |
| SO-BE-25-GR-B-233 | IC-8800 | SUPERSEDED | Historical - verify before use |
| SO-BE-50-924 | IC-9618 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-977 | IC-9747 | REVIEW REQUIRED | Historical - verify before use |
| FR-194 | IC-8677 | REVIEW REQUIRED | Historical - verify before use |
| CI-AC-538 | IC-9624 | DEPRECATED | Historical - verify before use |
| SO-CH-TE-286 | IC-7647 | SUPERSEDED | Historical - verify before use |
| PO-SO-202 | IC-7589 | REVIEW REQUIRED | Historical - verify before use |
| CI-AC-70-265 | IC-6236 | PROVISIONAL | Historical - verify before use |
| MA-DE-569 | IC-8602 | SUPERSEDED | Historical - verify before use |
| SO-AC-FO-GR-286 | IC-5559 | REVIEW REQUIRED | Historical - verify before use |
| GL-SY-98-749 | IC-8841 | DEPRECATED | Historical - verify before use |
| MA-DE-951 | IC-8622 | PROVISIONAL | Historical - verify before use |
| SO-CH-201 | IC-7480 | PROVISIONAL | Historical - verify before use |
| LA-AC-FO-GR-687 | IC-7250 | DEPRECATED | Historical - verify before use |
| SO-CH-70-317 | IC-9844 | REVIEW REQUIRED | Historical - verify before use |
| FR-TE-414 | IC-5460 | PROVISIONAL | Historical - verify before use |
| LA-AC-893 | IC-7883 | SUPERSEDED | Historical - verify before use |
| SO-BE-PH-GR-831 | IC-9156 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-98-FO-GR-748 | IC-5607 | SUPERSEDED | Historical - verify before use |
| SO-BE-GR-B-936 | IC-7542 | PROVISIONAL | Historical - verify before use |
| PO-SO-TE-239 | IC-8782 | PROVISIONAL | Historical - verify before use |
| RA-OI-GR-B-834 | IC-8702 | PROVISIONAL | Historical - verify before use |
| CO-OI-70-701 | IC-5308 | SUPERSEDED | Historical - verify before use |
| CA-CA-25-PH-GR-684 | IC-5466 | SUPERSEDED | Historical - verify before use |
| MA-DE-GR-B-565 | IC-8020 | REVIEW REQUIRED | Historical - verify before use |
| SO-IS-98-PR-717 | IC-7351 | REVIEW REQUIRED | Historical - verify before use |
| SO-BE-99.5-TE-953 | IC-5628 | DEPRECATED | Historical - verify before use |
| MA-DE-437 | IC-5739 | PROVISIONAL | Historical - verify before use |
| CA-CA-GR-B-162 | IC-9866 | SUPERSEDED | Historical - verify before use |
| SO-CH-TE-223 | IC-9153 | DEPRECATED | Historical - verify before use |
| PA-OI-GR-B-690 | IC-8149 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-PR-679 | IC-8790 | SUPERSEDED | Historical - verify before use |
| SO-BE-50-TE-276 | IC-9754 | DEPRECATED | Historical - verify before use |
| AS-AC-ST-686 | IC-9540 | REVIEW REQUIRED | Historical - verify before use |
| GL-SY-FO-GR-600 | IC-5336 | SUPERSEDED | Historical - verify before use |
| SO-BE-98-PH-GR-434 | IC-8684 | REVIEW REQUIRED | Historical - verify before use |
| WH-GL-98-511 | IC-9683 | DEPRECATED | Historical - verify before use |
| PO-SO-50-TE-282 | IC-6542 | SUPERSEDED | Historical - verify before use |
| PE-PR-302 | IC-7633 | REVIEW REQUIRED | Historical - verify before use |
| PO-SO-GR-B-511 | IC-9956 | DEPRECATED | Historical - verify before use |
| CI-AC-70-FO-GR-198 | IC-8896 | PROVISIONAL | Historical - verify before use |
| FR-99.5-GR-A-438 | IC-9107 | SUPERSEDED | Historical - verify before use |
| PO-SO-25-PH-GR-260 | IC-6235 | SUPERSEDED | Historical - verify before use |
| SO-BE-667 | IC-5506 | REVIEW REQUIRED | Historical - verify before use |
| LA-AC-50-PR-288 | IC-8690 | DEPRECATED | Historical - verify before use |
| CA-98-TE-238 | IC-5847 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-98-445 | IC-7813 | REVIEW REQUIRED | Historical - verify before use |
| CA-CA-99.5-FO-GR-839 | IC-5690 | REVIEW REQUIRED | Historical - verify before use |
| FR-99.5-FO-GR-963 | IC-9133 | PROVISIONAL | Historical - verify before use |
| LA-AC-ST-823 | IC-6413 | SUPERSEDED | Historical - verify before use |
| WH-GL-99.5-GR-A-933 | IC-5320 | DEPRECATED | Historical - verify before use |
| SO-BE-99.5-TE-484 | IC-7029 | PROVISIONAL | Historical - verify before use |
| SO-BE-99.5-GR-A-930 | IC-8586 | REVIEW REQUIRED | Historical - verify before use |
| MA-DE-933 | IC-8599 | REVIEW REQUIRED | Historical - verify before use |
| AS-AC-50-321 | IC-9293 | PROVISIONAL | Historical - verify before use |
| SO-IS-432 | IC-9282 | PROVISIONAL | Historical - verify before use |
| DE-GR-A-472 | IC-9995 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-70-GR-A-836 | IC-6300 | SUPERSEDED | Historical - verify before use |
| CA-CA-50-260 | IC-7981 | DEPRECATED | Historical - verify before use |
| PA-OI-50-497 | IC-8054 | REVIEW REQUIRED | Historical - verify before use |
| PO-SO-98-216 | IC-7317 | PROVISIONAL | Historical - verify before use |
| AS-AC-439 | IC-8173 | PROVISIONAL | Historical - verify before use |
| GL-SY-609 | IC-8348 | REVIEW REQUIRED | Historical - verify before use |
| CA-CA-99.5-291 | IC-7771 | DEPRECATED | Historical - verify before use |
| LA-AC-GR-B-700 | IC-9897 | DEPRECATED | Historical - verify before use |
| PO-SO-604 | IC-5428 | PROVISIONAL | Historical - verify before use |
| PA-OI-PH-GR-124 | IC-7741 | DEPRECATED | Historical - verify before use |
| PE-PR-PR-775 | IC-5539 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-98-TE-864 | IC-7700 | PROVISIONAL | Historical - verify before use |
| CO-OI-98-876 | IC-5774 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-99.5-242 | IC-9570 | SUPERSEDED | Historical - verify before use |
| SO-CH-354 | IC-8166 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-25-TE-157 | IC-7327 | PROVISIONAL | Historical - verify before use |
| LA-AC-98-GR-A-841 | IC-7064 | SUPERSEDED | Historical - verify before use |
| PE-PR-25-472 | IC-9937 | REVIEW REQUIRED | Historical - verify before use |
| CA-CA-70-883 | IC-6231 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-50-692 | IC-7730 | PROVISIONAL | Historical - verify before use |
| RE-ST-FO-GR-727 | IC-5667 | SUPERSEDED | Historical - verify before use |
| SO-AC-70-542 | IC-9773 | REVIEW REQUIRED | Historical - verify before use |
| WH-GL-944 | IC-6158 | SUPERSEDED | Historical - verify before use |
| SO-BE-FO-GR-650 | IC-7865 | PROVISIONAL | Historical - verify before use |
| WH-GL-123 | IC-7541 | DEPRECATED | Historical - verify before use |
| SO-AC-ST-392 | IC-8210 | SUPERSEDED | Historical - verify before use |
| WH-GL-50-865 | IC-6056 | PROVISIONAL | Historical - verify before use |
| DE-GR-B-244 | IC-9874 | SUPERSEDED | Historical - verify before use |
| CI-AC-25-863 | IC-5694 | DEPRECATED | Historical - verify before use |
| PE-PR-746 | IC-7536 | REVIEW REQUIRED | Historical - verify before use |
| CA-CA-98-928 | IC-9578 | PROVISIONAL | Historical - verify before use |
| CA-GR-B-950 | IC-8085 | DEPRECATED | Historical - verify before use |
| WH-GL-FO-GR-876 | IC-7690 | PROVISIONAL | Historical - verify before use |
| CI-AC-PR-827 | IC-6046 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-25-556 | IC-9312 | SUPERSEDED | Historical - verify before use |
| CO-OI-25-FO-GR-778 | IC-5765 | REVIEW REQUIRED | Historical - verify before use |
| AS-AC-573 | IC-8468 | REVIEW REQUIRED | Historical - verify before use |
| SU-OI-GR-B-259 | IC-9165 | PROVISIONAL | Historical - verify before use |
| PA-OI-99.5-867 | IC-7964 | SUPERSEDED | Historical - verify before use |
| SO-BE-824 | IC-5149 | DEPRECATED | Historical - verify before use |
| PO-SO-70-899 | IC-7970 | PROVISIONAL | Historical - verify before use |
| PO-SO-ST-914 | IC-7530 | DEPRECATED | Historical - verify before use |
| DE-FO-GR-183 | IC-6476 | PROVISIONAL | Historical - verify before use |
| SO-BE-98-410 | IC-6754 | SUPERSEDED | Historical - verify before use |


#### 4.3.4 Excluded Assignments

Provisional assignments pending business validation:

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-6598-H | Duplicate source record | Escalated to data steward |
| NOISE-3538-B | Pending validation | Deferred to Phase 2 |
| NOISE-9843-A | Data quality insufficient | Manual review scheduled |
| NOISE-3147-G | Pending validation | Manual review scheduled |
| NOISE-3712-H | Duplicate source record | Business owner notified |
| NOISE-4891-H | Pending validation | Deferred to Phase 2 |
| NOISE-8355-D | Pending validation | Escalated to data steward |
| NOISE-8684-D | Data quality insufficient | Business owner notified |
| NOISE-8564-E | Data quality insufficient | Business owner notified |
| NOISE-9641-G | Data quality insufficient | Manual review scheduled |
| NOISE-3267-E | Missing required attributes | Business owner notified |
| NOISE-2680-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5469-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2502-D | Out of scope per business decision | Business owner notified |
| NOISE-1436-G | Missing required attributes | Manual review scheduled |
| NOISE-7126-D | Missing required attributes | Business owner notified |
| NOISE-4678-A | Data quality insufficient | Manual review scheduled |
| NOISE-6493-C | Out of scope per business decision | Manual review scheduled |
| NOISE-8740-C | Duplicate source record | Manual review scheduled |
| NOISE-1086-B | Missing required attributes | Business owner notified |
| NOISE-3449-G | Pending validation | Escalated to data steward |
| NOISE-5934-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-8489-B | Data quality insufficient | Business owner notified |
| NOISE-9782-A | Data quality insufficient | Escalated to data steward |
| NOISE-4963-C | Missing required attributes | Manual review scheduled |
| NOISE-6780-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2402-F | Missing required attributes | Escalated to data steward |
| NOISE-9312-A | Pending validation | Deferred to Phase 2 |
| NOISE-7338-F | Pending validation | Business owner notified |
| NOISE-2106-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-6447-C | Duplicate source record | Business owner notified |
| NOISE-6546-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-8840-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8498-A | Duplicate source record | Manual review scheduled |
| NOISE-4268-A | Data quality insufficient | Escalated to data steward |
| NOISE-7524-H | Duplicate source record | Manual review scheduled |
| NOISE-4131-E | Out of scope per business decision | Business owner notified |
| NOISE-6438-E | Out of scope per business decision | Escalated to data steward |
| NOISE-7553-H | Pending validation | Manual review scheduled |
| NOISE-9129-H | Data quality insufficient | Manual review scheduled |
| NOISE-2353-G | Data quality insufficient | Escalated to data steward |
| NOISE-3956-E | Data quality insufficient | Manual review scheduled |
| NOISE-6372-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7981-C | Out of scope per business decision | Escalated to data steward |
| NOISE-8325-A | Out of scope per business decision | Business owner notified |
| NOISE-8126-E | Duplicate source record | Escalated to data steward |
| NOISE-7655-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3339-H | Out of scope per business decision | Business owner notified |
| NOISE-4866-F | Duplicate source record | Manual review scheduled |
| NOISE-1530-C | Out of scope per business decision | Escalated to data steward |
| NOISE-7095-H | Out of scope per business decision | Escalated to data steward |
| NOISE-3255-F | Pending validation | Escalated to data steward |
| NOISE-5566-D | Duplicate source record | Manual review scheduled |
| NOISE-4048-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-2929-E | Out of scope per business decision | Business owner notified |
| NOISE-8311-D | Pending validation | Business owner notified |
| NOISE-9047-D | Data quality insufficient | Manual review scheduled |
| NOISE-8406-C | Pending validation | Manual review scheduled |
| NOISE-6236-F | Pending validation | Escalated to data steward |
| NOISE-9882-E | Missing required attributes | Escalated to data steward |
| NOISE-3852-F | Data quality insufficient | Business owner notified |
| NOISE-4292-C | Pending validation | Manual review scheduled |
| NOISE-6912-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-2412-B | Pending validation | Business owner notified |
| NOISE-8842-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2208-C | Missing required attributes | Manual review scheduled |
| NOISE-8632-F | Pending validation | Deferred to Phase 2 |
| NOISE-3981-C | Duplicate source record | Escalated to data steward |
| NOISE-3034-C | Duplicate source record | Escalated to data steward |
| NOISE-6286-D | Data quality insufficient | Business owner notified |
| NOISE-2292-E | Data quality insufficient | Escalated to data steward |
| NOISE-3050-E | Pending validation | Manual review scheduled |
| NOISE-9234-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-3804-F | Out of scope per business decision | Escalated to data steward |
| NOISE-1464-B | Pending validation | Escalated to data steward |
| NOISE-4453-G | Data quality insufficient | Manual review scheduled |
| NOISE-9938-E | Pending validation | Manual review scheduled |
| NOISE-5012-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-1981-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8609-D | Pending validation | Escalated to data steward |
| NOISE-6121-F | Data quality insufficient | Manual review scheduled |
| NOISE-3142-F | Pending validation | Escalated to data steward |
| NOISE-6228-D | Data quality insufficient | Manual review scheduled |
| NOISE-8366-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-5754-G | Pending validation | Manual review scheduled |
| NOISE-5067-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-6123-D | Missing required attributes | Escalated to data steward |
| NOISE-9433-H | Missing required attributes | Manual review scheduled |
| NOISE-1379-B | Missing required attributes | Escalated to data steward |
| NOISE-4944-D | Missing required attributes | Business owner notified |
| NOISE-1828-E | Pending validation | Manual review scheduled |
| NOISE-8710-E | Missing required attributes | Escalated to data steward |
| NOISE-8060-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6995-A | Duplicate source record | Manual review scheduled |
| NOISE-4189-F | Out of scope per business decision | Business owner notified |
| NOISE-7329-H | Pending validation | Escalated to data steward |
| NOISE-2946-C | Missing required attributes | Escalated to data steward |
| NOISE-6555-F | Pending validation | Escalated to data steward |
| NOISE-9341-G | Duplicate source record | Business owner notified |
| NOISE-1637-C | Pending validation | Manual review scheduled |
| NOISE-9508-H | Missing required attributes | Manual review scheduled |
| NOISE-3290-F | Pending validation | Business owner notified |
| NOISE-7438-E | Pending validation | Manual review scheduled |
| NOISE-9351-H | Data quality insufficient | Business owner notified |
| NOISE-8780-A | Data quality insufficient | Business owner notified |
| NOISE-2795-G | Missing required attributes | Escalated to data steward |
| NOISE-1436-H | Data quality insufficient | Escalated to data steward |
| NOISE-4728-A | Duplicate source record | Manual review scheduled |
| NOISE-9589-G | Pending validation | Manual review scheduled |
| NOISE-2800-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-7861-C | Duplicate source record | Escalated to data steward |
| NOISE-9221-H | Missing required attributes | Manual review scheduled |
| NOISE-3262-D | Out of scope per business decision | Escalated to data steward |
| NOISE-8837-G | Missing required attributes | Escalated to data steward |
| NOISE-9734-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5331-H | Pending validation | Manual review scheduled |
| NOISE-5890-D | Pending validation | Deferred to Phase 2 |
| NOISE-4396-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-5480-E | Out of scope per business decision | Escalated to data steward |
| NOISE-9899-G | Data quality insufficient | Escalated to data steward |
| NOISE-5758-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8247-E | Out of scope per business decision | Escalated to data steward |
| NOISE-4310-E | Data quality insufficient | Manual review scheduled |
| NOISE-2789-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-9700-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-2641-G | Data quality insufficient | Escalated to data steward |
| NOISE-3252-A | Missing required attributes | Business owner notified |
| NOISE-8793-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-6262-E | Out of scope per business decision | Escalated to data steward |
| NOISE-4804-A | Out of scope per business decision | Manual review scheduled |
| NOISE-1595-G | Missing required attributes | Escalated to data steward |
| NOISE-5742-A | Missing required attributes | Business owner notified |
| NOISE-2758-F | Pending validation | Deferred to Phase 2 |
| NOISE-9901-H | Data quality insufficient | Escalated to data steward |
| NOISE-5470-D | Missing required attributes | Escalated to data steward |
| NOISE-3662-H | Pending validation | Deferred to Phase 2 |
| NOISE-4050-A | Data quality insufficient | Escalated to data steward |
| NOISE-4164-C | Missing required attributes | Escalated to data steward |
| NOISE-9442-F | Pending validation | Escalated to data steward |
| NOISE-2562-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-5064-A | Data quality insufficient | Escalated to data steward |
| NOISE-8319-E | Data quality insufficient | Business owner notified |
| NOISE-1187-E | Duplicate source record | Escalated to data steward |
| NOISE-4871-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6026-C | Out of scope per business decision | Manual review scheduled |
| NOISE-6095-B | Duplicate source record | Escalated to data steward |
| NOISE-4618-D | Pending validation | Deferred to Phase 2 |
| NOISE-8454-F | Missing required attributes | Manual review scheduled |
| NOISE-9806-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-2341-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-2838-A | Pending validation | Business owner notified |
| NOISE-4312-C | Data quality insufficient | Manual review scheduled |
| NOISE-8239-B | Out of scope per business decision | Business owner notified |
| NOISE-9008-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-8429-C | Pending validation | Manual review scheduled |
| NOISE-1945-H | Pending validation | Business owner notified |
| NOISE-1356-G | Out of scope per business decision | Manual review scheduled |
| NOISE-4570-B | Data quality insufficient | Escalated to data steward |
| NOISE-2044-A | Duplicate source record | Business owner notified |
| NOISE-5703-G | Out of scope per business decision | Escalated to data steward |
| NOISE-7887-F | Data quality insufficient | Business owner notified |
| NOISE-7154-B | Out of scope per business decision | Manual review scheduled |
| NOISE-6697-B | Data quality insufficient | Business owner notified |
| NOISE-9664-C | Missing required attributes | Escalated to data steward |
| NOISE-1372-E | Missing required attributes | Business owner notified |
| NOISE-9715-G | Out of scope per business decision | Escalated to data steward |
| NOISE-8546-F | Out of scope per business decision | Manual review scheduled |
| NOISE-2848-A | Duplicate source record | Business owner notified |
| NOISE-1256-D | Duplicate source record | Manual review scheduled |
| NOISE-1550-H | Missing required attributes | Escalated to data steward |
| NOISE-1724-G | Out of scope per business decision | Manual review scheduled |
| NOISE-4559-A | Out of scope per business decision | Escalated to data steward |
| NOISE-4836-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-6253-D | Data quality insufficient | Business owner notified |
| NOISE-9540-D | Out of scope per business decision | Business owner notified |
| NOISE-1998-C | Data quality insufficient | Business owner notified |
| NOISE-9120-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6222-G | Data quality insufficient | Escalated to data steward |
| NOISE-7167-C | Missing required attributes | Escalated to data steward |
| NOISE-4948-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1944-G | Pending validation | Escalated to data steward |
| NOISE-3196-G | Pending validation | Business owner notified |
| NOISE-6411-B | Duplicate source record | Escalated to data steward |
| NOISE-9775-D | Out of scope per business decision | Escalated to data steward |
| NOISE-1647-B | Out of scope per business decision | Manual review scheduled |
| NOISE-4555-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1251-D | Data quality insufficient | Business owner notified |
| NOISE-8846-D | Out of scope per business decision | Escalated to data steward |
| NOISE-4350-G | Out of scope per business decision | Escalated to data steward |
| NOISE-5637-G | Out of scope per business decision | Escalated to data steward |
| NOISE-6886-E | Pending validation | Manual review scheduled |
| NOISE-9147-H | Out of scope per business decision | Manual review scheduled |
| NOISE-4328-F | Pending validation | Deferred to Phase 2 |
| NOISE-4625-C | Pending validation | Business owner notified |
| NOISE-7841-E | Missing required attributes | Manual review scheduled |
| NOISE-4768-G | Out of scope per business decision | Business owner notified |
| NOISE-6530-E | Data quality insufficient | Manual review scheduled |
| NOISE-9037-H | Duplicate source record | Manual review scheduled |
| NOISE-3293-H | Out of scope per business decision | Manual review scheduled |
| NOISE-1962-A | Data quality insufficient | Business owner notified |
| NOISE-1794-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-4791-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-4583-H | Duplicate source record | Business owner notified |
| NOISE-8916-H | Pending validation | Manual review scheduled |
| NOISE-7739-A | Data quality insufficient | Business owner notified |
| NOISE-5501-E | Data quality insufficient | Escalated to data steward |
| NOISE-8054-C | Data quality insufficient | Manual review scheduled |
| NOISE-3439-D | Pending validation | Deferred to Phase 2 |
| NOISE-5135-F | Out of scope per business decision | Escalated to data steward |
| NOISE-7112-G | Pending validation | Business owner notified |
| NOISE-4700-E | Data quality insufficient | Manual review scheduled |
| NOISE-1519-B | Out of scope per business decision | Escalated to data steward |
| NOISE-8798-A | Out of scope per business decision | Business owner notified |
| NOISE-3807-B | Pending validation | Deferred to Phase 2 |
| NOISE-6427-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4463-H | Duplicate source record | Business owner notified |
| NOISE-5593-A | Missing required attributes | Business owner notified |
| NOISE-4394-C | Missing required attributes | Business owner notified |
| NOISE-5903-C | Pending validation | Manual review scheduled |
| NOISE-7375-F | Pending validation | Manual review scheduled |
| NOISE-2284-F | Data quality insufficient | Manual review scheduled |
| NOISE-4803-B | Missing required attributes | Business owner notified |
| NOISE-7499-F | Data quality insufficient | Escalated to data steward |
| NOISE-9038-D | Data quality insufficient | Manual review scheduled |
| NOISE-8075-C | Out of scope per business decision | Escalated to data steward |
| NOISE-7227-B | Duplicate source record | Escalated to data steward |
| NOISE-5037-B | Missing required attributes | Business owner notified |
| NOISE-7225-C | Data quality insufficient | Manual review scheduled |
| NOISE-6909-B | Pending validation | Manual review scheduled |
| NOISE-8286-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3170-B | Duplicate source record | Business owner notified |
| NOISE-9395-G | Out of scope per business decision | Business owner notified |
| NOISE-6798-B | Out of scope per business decision | Business owner notified |
| NOISE-7311-A | Pending validation | Escalated to data steward |
| NOISE-2387-D | Data quality insufficient | Business owner notified |
| NOISE-7237-C | Missing required attributes | Business owner notified |
| NOISE-5397-H | Out of scope per business decision | Manual review scheduled |
| NOISE-8121-E | Duplicate source record | Manual review scheduled |
| NOISE-2260-F | Data quality insufficient | Escalated to data steward |
| NOISE-9123-D | Data quality insufficient | Escalated to data steward |
| NOISE-5991-A | Duplicate source record | Escalated to data steward |
| NOISE-7224-F | Pending validation | Business owner notified |
| NOISE-3230-E | Data quality insufficient | Escalated to data steward |
| NOISE-4290-H | Pending validation | Escalated to data steward |
| NOISE-6228-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4971-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6980-B | Out of scope per business decision | Manual review scheduled |
| NOISE-9939-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8563-D | Out of scope per business decision | Manual review scheduled |
| NOISE-2133-G | Pending validation | Deferred to Phase 2 |
| NOISE-5961-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-7932-G | Duplicate source record | Manual review scheduled |
| NOISE-8851-G | Pending validation | Manual review scheduled |
| NOISE-7853-A | Data quality insufficient | Escalated to data steward |
| NOISE-9796-B | Data quality insufficient | Escalated to data steward |
| NOISE-6816-C | Pending validation | Manual review scheduled |
| NOISE-7547-F | Duplicate source record | Escalated to data steward |
| NOISE-1172-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9499-D | Pending validation | Deferred to Phase 2 |
| NOISE-8586-C | Pending validation | Manual review scheduled |
| NOISE-2712-E | Missing required attributes | Manual review scheduled |
| NOISE-3321-F | Duplicate source record | Business owner notified |
| NOISE-4389-H | Missing required attributes | Business owner notified |
| NOISE-8178-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-1732-B | Out of scope per business decision | Manual review scheduled |
| NOISE-2791-C | Pending validation | Escalated to data steward |
| NOISE-3858-C | Data quality insufficient | Business owner notified |
| NOISE-8570-D | Pending validation | Business owner notified |
| NOISE-4022-C | Pending validation | Business owner notified |
| NOISE-1478-D | Missing required attributes | Manual review scheduled |
| NOISE-7370-A | Out of scope per business decision | Manual review scheduled |
| NOISE-5560-B | Pending validation | Escalated to data steward |
| NOISE-4063-F | Data quality insufficient | Business owner notified |
| NOISE-2867-E | Pending validation | Escalated to data steward |
| NOISE-6134-G | Pending validation | Escalated to data steward |
| NOISE-2871-F | Out of scope per business decision | Manual review scheduled |
| NOISE-3826-E | Out of scope per business decision | Escalated to data steward |
| NOISE-3194-F | Pending validation | Manual review scheduled |
| NOISE-2916-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-7364-G | Duplicate source record | Manual review scheduled |
| NOISE-7286-G | Missing required attributes | Manual review scheduled |
| NOISE-9804-C | Pending validation | Business owner notified |
| NOISE-5732-C | Duplicate source record | Manual review scheduled |
| NOISE-1878-F | Pending validation | Business owner notified |
| NOISE-4196-G | Pending validation | Escalated to data steward |
| NOISE-9109-G | Duplicate source record | Escalated to data steward |
| NOISE-8272-H | Duplicate source record | Business owner notified |
| NOISE-1505-D | Duplicate source record | Escalated to data steward |
| NOISE-4683-E | Duplicate source record | Escalated to data steward |
| NOISE-9115-B | Data quality insufficient | Manual review scheduled |
| NOISE-9898-F | Out of scope per business decision | Manual review scheduled |


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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230424_000000`
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
| Project Lead | Michael Weber (Business Operations) | michael@company.com | +1-555-0101 |
| Technical Lead | Lisa Rodriguez (Quality Assurance) | lisa@company.com | +1-555-0102 |
| Business Owner | Maria Garcia (Supply Chain) | maria@company.com | +1-555-0103 |
| Data Steward | John Smith (IT Infrastructure) | john@company.com | +1-555-0104 |

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
