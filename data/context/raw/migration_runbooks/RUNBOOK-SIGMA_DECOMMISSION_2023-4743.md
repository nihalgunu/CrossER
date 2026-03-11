# Migration Runbook: Legacy SIGMA System Decommission

**Document ID**: RB-SIGMA_DECOMMISSION_2023-2679
**Version**: 2.5
**Last Updated**: 2023-08-13
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the Legacy SIGMA System Decommission project.
The migration involves transitioning master data and transactional records from LEGACY_SIGMA
to ERP_ALPHA while maintaining data integrity and business continuity.

**Project Timeline**: 2023-06-13 to 2023-09-25
**Business Sponsor**: Global Data Governance
**Technical Owner**: IT Infrastructure

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
|   LEGACY_SIGMA       |     |   Staging Layer  |     |   ERP_ALPHA       |
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
LEGACY_SIGMA. Each source entity is assigned an internal staging code for
tracking purposes.

**IMPORTANT**: This document only contains source-to-staging assignments.
Target system mappings are maintained separately in the MDM Registry.

### 4.2 Assignment Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1473 | Completed |
| Codes assigned | 988 | Staged |
| Excluded from scope | 296 | Documented |
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

| Source Entity (LEGACY_SIGMA) | Internal Code | Assignment Date | Department |
|--------------------------------|---------------|-----------------|------------|
| SIG-30-PVA-ZMF8 | IC-1000 | 2023-04-05 | Product Management |
| SIG-44-SRN-1MKF | IC-1006 | 2024-08-21 | Supply Chain |
| SIG-41-SWO-23GD | TC-1008 | 2022-01-08 | Supply Chain |
| SIG-79-HZP-CLBR | IC-1017 | 2022-07-22 | Product Management |
| SIG-29-CYR-T4UF | IC-1023 | 2024-05-15 | Data Governance |
| SIG-16-QDM-JLQM | BC-1034 | 2024-01-03 | Data Governance |
| SIG-41-LTG-3D5I | BC-1042 | 2022-01-04 | Compliance |
| SIG-56-ZVH-GATJ | BC-1046 | 2022-07-18 | IT Infrastructure |
| SIG-48-UJX-49KW | IC-1054 | 2023-05-11 | IT Infrastructure |
| SIG-44-MHK-SRCB | IC-1059 | 2024-08-06 | IT Infrastructure |
| SIG-74-HUK-JA04 | TC-1065 | 2022-12-25 | Finance |
| SIG-95-GQL-A26Y | TC-1069 | 2024-01-16 | IT Infrastructure |
| SIG-71-VGV-8K52 | TC-1073 | 2023-12-15 | Data Governance |
| SIG-86-VGU-A4FE | TC-1081 | 2021-04-06 | Product Management |
| SIG-61-XKV-ODPX | IC-1087 | 2024-05-06 | Product Management |
| SIG-53-AHT-MGFX | BC-1093 | 2021-08-23 | Product Management |
| SIG-26-DML-NZS4 | BC-1101 | 2021-04-21 | Data Governance |
| SIG-51-LVQ-VS8Q | TC-1105 | 2021-05-22 | Supply Chain |
| SIG-37-NAI-M1G9 | IC-1111 | 2022-09-12 | Compliance |
| SIG-57-NGZ-ILDZ | BC-1118 | 2024-01-23 | IT Infrastructure |
| SIG-50-FUX-7S9T | IC-1122 | 2023-02-22 | Supply Chain |
| SIG-13-JUR-FV2B | IC-1130 | 2021-02-14 | Data Governance |
| SIG-92-VAB-1JHU | IC-1142 | 2024-08-03 | Product Management |
| SIG-52-NBD-2SF6 | BC-1150 | 2021-10-20 | Finance |
| SIG-45-IJY-KUT6 | BC-1161 | 2022-05-26 | Operations |
| SIG-60-WEX-2G05 | TC-1168 | 2024-05-08 | Product Management |
| SIG-68-CNV-EOUU | BC-1174 | 2021-04-02 | Supply Chain |
| SIG-24-LEE-BXW7 | TC-1180 | 2024-11-26 | Finance |
| SIG-32-BYW-WPR9 | TC-1185 | 2023-04-04 | Operations |
| SIG-12-ANK-TJ9A | IC-1191 | 2021-05-06 | Finance |
| SIG-10-TIC-7Q1D | TC-1200 | 2024-05-16 | Product Management |
| SIG-76-CCF-UYHN | TC-1207 | 2024-08-27 | Data Governance |
| SIG-66-LJV-5E3H | TC-1218 | 2024-11-25 | Operations |
| SIG-37-PEJ-WFOY | TC-1226 | 2021-11-12 | Data Governance |
| SIG-50-NZZ-E4UN | BC-1232 | 2022-08-19 | Data Governance |
| SIG-79-ZUT-1IAO | BC-1243 | 2024-12-14 | IT Infrastructure |
| SIG-73-YLS-BYGH | BC-1249 | 2024-09-21 | Finance |
| SIG-19-HIY-M5FC | IC-1268 | 2023-06-25 | IT Infrastructure |
| SIG-22-VQM-AGKC | IC-1273 | 2024-10-13 | Product Management |
| SIG-22-DOP-7UDK | IC-1277 | 2024-12-03 | Operations |
| SIG-57-QDA-RQ8R | BC-1284 | 2023-02-15 | Supply Chain |
| SIG-44-HRR-WZP6 | BC-1290 | 2023-10-06 | IT Infrastructure |
| SIG-16-LZG-DGBK | IC-1292 | 2024-03-16 | Supply Chain |
| SIG-13-EJJ-5506 | BC-1294 | 2024-11-16 | Data Governance |
| SIG-83-KGL-Q4QE | IC-1299 | 2022-10-12 | Operations |
| SIG-35-SYQ-HZY7 | TC-1301 | 2022-03-23 | IT Infrastructure |
| SIG-58-EEN-BKJF | BC-1306 | 2021-03-15 | Operations |
| SIG-19-TPS-MSKY | TC-1317 | 2024-09-22 | Finance |
| SIG-80-EUW-QTKC | TC-1324 | 2021-08-17 | IT Infrastructure |
| SIG-85-SIL-CNEA | IC-1340 | 2021-01-27 | Compliance |
| SIG-60-GHI-04X0 | BC-1345 | 2022-11-26 | Supply Chain |
| SIG-94-QLF-7SH2 | IC-1355 | 2023-11-19 | Operations |
| SIG-39-GGG-HIWF | IC-1361 | 2023-06-09 | Product Management |
| SIG-98-OOK-FHJ4 | IC-1366 | 2021-04-06 | Compliance |
| SIG-66-ZOH-E8TV | BC-1376 | 2024-10-20 | Product Management |
| SIG-76-QBY-ERKM | IC-1387 | 2022-10-26 | Compliance |
| SIG-42-AJS-6RPK | TC-1392 | 2021-06-24 | Supply Chain |
| SIG-36-FSA-X73Q | IC-1400 | 2022-11-14 | Data Governance |
| SIG-83-PHT-N27M | BC-1406 | 2023-10-02 | Operations |
| SIG-60-TMF-XHW0 | TC-1408 | 2021-07-22 | Compliance |
| SIG-30-EKM-GB1A | BC-1419 | 2021-11-28 | Operations |
| SIG-66-FRL-CVIT | IC-1437 | 2022-03-10 | Operations |
| SIG-63-TFP-OMUW | BC-1442 | 2022-10-28 | Operations |
| SIG-51-YTN-F537 | IC-1452 | 2023-07-15 | Data Governance |
| SIG-46-SVJ-5IZO | IC-1463 | 2024-06-05 | Product Management |
| SIG-91-GMY-Q91Y | IC-1469 | 2024-01-08 | Supply Chain |
| SIG-18-KSV-TA83 | TC-1476 | 2024-04-02 | Finance |
| SIG-37-ZOD-1VME | TC-1484 | 2021-03-09 | Finance |
| SIG-72-YEU-SCIQ | TC-1490 | 2024-09-20 | Operations |
| SIG-37-CWM-V4K0 | IC-1493 | 2022-04-02 | Data Governance |
| SIG-17-UCW-S6NB | BC-1501 | 2023-04-19 | Operations |
| SIG-47-SRN-QNYY | TC-1507 | 2021-11-07 | Finance |
| SIG-27-RTX-YEAW | IC-1511 | 2024-03-14 | Supply Chain |
| SIG-19-BHQ-S1GD | BC-1521 | 2023-04-24 | Finance |
| SIG-45-ADT-8MFS | IC-1529 | 2023-11-15 | Finance |
| SIG-56-BPD-M0A6 | IC-1544 | 2021-10-08 | Finance |
| SIG-40-KVV-E07S | TC-1553 | 2024-06-18 | Product Management |
| SIG-42-AYY-K71K | IC-1562 | 2021-08-25 | Supply Chain |
| SIG-37-JLF-9KYP | TC-1573 | 2023-01-10 | Finance |
| SIG-31-CWE-03UX | TC-1582 | 2021-07-14 | Compliance |
| SIG-36-ZWC-F2K1 | BC-1590 | 2023-03-14 | Compliance |
| SIG-13-CAZ-HXXP | BC-1596 | 2023-02-05 | Product Management |
| SIG-65-BAQ-940V | IC-1600 | 2022-10-22 | Finance |
| SIG-68-SYL-8192 | TC-1607 | 2022-11-07 | Supply Chain |
| SIG-76-YLU-7DL9 | BC-1612 | 2021-07-21 | Finance |
| SIG-49-UKY-6H3R | BC-1623 | 2022-10-12 | Compliance |
| SIG-16-FQO-8S1S | TC-1624 | 2021-10-05 | Supply Chain |
| SIG-82-TQD-ODWH | IC-1634 | 2023-10-26 | Supply Chain |
| SIG-97-PYI-8W9Z | BC-1637 | 2024-07-14 | IT Infrastructure |
| SIG-78-WDE-NNV9 | IC-1653 | 2024-08-09 | Compliance |
| SIG-70-YBK-DUQ6 | BC-1658 | 2022-01-20 | Operations |
| SIG-45-PNR-H9Q3 | IC-1661 | 2024-06-02 | Data Governance |
| SIG-25-VPE-TOC1 | IC-1662 | 2024-11-16 | Finance |
| SIG-29-BJH-NXI0 | IC-1670 | 2021-01-24 | Data Governance |
| SIG-96-DUH-99Q6 | BC-1687 | 2022-06-08 | Product Management |
| SIG-60-IRZ-OTKZ | TC-1697 | 2024-06-21 | Operations |
| SIG-48-GDK-Y8XN | BC-1702 | 2024-08-23 | Supply Chain |
| SIG-98-CGL-FHWJ | IC-1711 | 2023-09-06 | Product Management |
| SIG-53-MEZ-6IT1 | TC-1726 | 2021-09-24 | Finance |
| SIG-41-HMT-W0GK | IC-1735 | 2024-02-01 | IT Infrastructure |
| SIG-42-BEO-614U | BC-1743 | 2024-11-27 | Compliance |
| SIG-59-LNO-OJGF | BC-1746 | 2022-02-08 | Compliance |
| SIG-20-OVW-HRUP | BC-1750 | 2021-11-25 | Supply Chain |
| SIG-94-JCX-NJ62 | BC-1755 | 2023-06-02 | Supply Chain |
| SIG-11-SLQ-KF5B | IC-1765 | 2024-11-27 | Finance |
| SIG-71-COB-BL7A | IC-1771 | 2023-02-14 | Compliance |
| SIG-82-ZPY-WR2F | BC-1777 | 2024-11-23 | Product Management |
| SIG-73-AXY-5E8O | BC-1790 | 2022-10-22 | Product Management |
| SIG-30-LJO-TN4Y | IC-1795 | 2022-05-24 | Finance |
| SIG-76-AAU-3VM8 | BC-1799 | 2024-12-28 | IT Infrastructure |
| SIG-58-HNG-1XJ7 | BC-1805 | 2021-09-20 | IT Infrastructure |
| SIG-30-MPO-SJEV | TC-1810 | 2023-11-08 | Operations |
| SIG-55-CTS-U5X0 | TC-1815 | 2023-10-24 | Compliance |
| SIG-83-HEH-XF50 | IC-1820 | 2024-02-10 | Product Management |
| SIG-66-AQR-B68Q | TC-1839 | 2022-11-23 | Operations |
| SIG-54-CMF-PK48 | IC-1848 | 2024-08-03 | Finance |
| SIG-70-IKQ-7KBN | TC-1866 | 2024-08-01 | Finance |
| SIG-27-UKP-V2ME | IC-1871 | 2023-07-23 | IT Infrastructure |
| SIG-85-STS-67D6 | IC-1880 | 2022-02-19 | Finance |
| SIG-72-JEH-P5K7 | IC-1888 | 2021-06-28 | Compliance |
| SIG-36-ABO-ZBYW | BC-1893 | 2023-08-24 | IT Infrastructure |
| SIG-22-TOX-02GV | BC-1902 | 2022-05-24 | IT Infrastructure |
| SIG-79-RTU-R8IQ | TC-1909 | 2023-12-16 | Compliance |
| SIG-10-KDB-LGYT | TC-1914 | 2021-02-10 | Data Governance |
| SIG-88-AGF-FF5L | TC-1919 | 2024-06-26 | Compliance |
| SIG-25-WDK-CWCD | IC-1926 | 2024-06-17 | Product Management |
| SIG-78-AVK-U9PX | BC-1937 | 2024-02-18 | Product Management |
| SIG-61-KUY-VFFK | TC-1943 | 2022-01-14 | Finance |
| SIG-51-IYK-630P | IC-1950 | 2021-03-12 | Product Management |
| SIG-79-IHV-JKPQ | TC-1954 | 2021-08-03 | IT Infrastructure |
| SIG-79-OZQ-4I2N | IC-1957 | 2023-07-06 | Finance |
| SIG-78-YEH-31XY | TC-1962 | 2021-01-04 | Supply Chain |
| SIG-84-BFP-RD5B | IC-1976 | 2023-07-20 | Data Governance |
| SIG-19-QLH-ILRZ | IC-1986 | 2023-10-24 | Finance |
| SIG-52-EML-H8JV | TC-1989 | 2021-05-17 | Finance |
| SIG-12-OAV-ALF4 | BC-1993 | 2023-12-28 | Supply Chain |
| SIG-58-NYA-2O4M | IC-1998 | 2021-04-13 | Operations |
| SIG-21-EAX-PC8Q | TC-2003 | 2021-11-04 | Product Management |
| SIG-39-QZD-93EZ | BC-2015 | 2024-09-12 | Data Governance |
| SIG-29-DTY-HFJL | TC-2024 | 2021-03-22 | Supply Chain |
| SIG-11-RGJ-D3IR | IC-2032 | 2022-12-14 | IT Infrastructure |
| SIG-32-TTU-44MW | IC-2038 | 2022-02-28 | Product Management |
| SIG-21-KSF-Z6X4 | TC-2044 | 2021-03-09 | Data Governance |
| SIG-53-MPZ-77TN | IC-2047 | 2024-02-18 | Product Management |
| SIG-47-HDT-7PPC | IC-2050 | 2023-10-02 | Operations |
| SIG-44-FWT-OA3N | TC-2055 | 2022-09-04 | Data Governance |
| SIG-35-TKX-8TRE | BC-2061 | 2022-03-03 | Product Management |
| SIG-68-PIZ-R6Q5 | BC-2065 | 2023-03-08 | Compliance |
| SIG-16-CAW-LD7M | BC-2072 | 2024-02-04 | Data Governance |
| SIG-43-NCZ-FT9Z | TC-2079 | 2021-08-27 | Supply Chain |
| SIG-94-KAU-6F8H | IC-2087 | 2022-03-18 | Data Governance |
| SIG-98-NIJ-5N8C | IC-2095 | 2024-01-05 | Data Governance |
| SIG-23-OPT-7QHV | TC-2102 | 2024-02-06 | IT Infrastructure |
| SIG-15-QIT-5CZE | BC-2104 | 2024-09-05 | Finance |
| SIG-84-PAS-5S3O | TC-2106 | 2024-05-21 | Supply Chain |
| SIG-45-ZTJ-PA16 | IC-2123 | 2024-10-21 | Operations |
| SIG-71-WDX-2GRR | TC-2140 | 2023-01-04 | Supply Chain |
| SIG-33-FUV-53NO | IC-2145 | 2024-10-11 | Data Governance |
| SIG-44-UIE-SASC | IC-2152 | 2024-03-11 | Product Management |
| SIG-54-LIP-WKBS | IC-2160 | 2023-04-05 | Product Management |
| SIG-48-LHY-R0O8 | TC-2165 | 2023-04-06 | Supply Chain |
| SIG-16-JKI-B4JG | TC-2172 | 2024-05-22 | Compliance |
| SIG-88-XZP-H10B | TC-2178 | 2021-08-10 | Compliance |
| SIG-40-NOU-7O0G | TC-2180 | 2022-10-03 | Supply Chain |
| SIG-34-UJK-TJA6 | BC-2182 | 2022-05-05 | Data Governance |
| SIG-12-BIH-AKGD | TC-2188 | 2024-01-04 | IT Infrastructure |
| SIG-56-CMM-ODF7 | TC-2197 | 2024-06-05 | IT Infrastructure |
| SIG-99-OQS-ADHF | TC-2199 | 2023-12-28 | Supply Chain |
| SIG-30-RXC-HFDI | TC-2210 | 2023-02-16 | IT Infrastructure |
| SIG-51-KQC-QY9M | TC-2222 | 2021-02-09 | Operations |
| SIG-41-OMW-SN1T | BC-2230 | 2022-06-24 | Operations |
| SIG-85-FAV-D2EE | IC-2238 | 2021-11-17 | Finance |
| SIG-49-OHU-U248 | IC-2247 | 2022-12-14 | Finance |
| SIG-75-GUI-J643 | BC-2257 | 2021-05-11 | Data Governance |
| SIG-79-GLV-IEST | TC-2266 | 2023-09-22 | IT Infrastructure |
| SIG-88-EEY-HOGD | TC-2288 | 2021-09-06 | IT Infrastructure |
| SIG-36-BVE-5U7D | BC-2295 | 2023-10-12 | Finance |
| SIG-47-YTF-UPMT | BC-2300 | 2023-10-24 | Finance |
| SIG-51-HLJ-TN1E | BC-2306 | 2024-05-27 | Compliance |
| SIG-25-ABB-2SBA | IC-2313 | 2024-01-12 | Data Governance |
| SIG-24-MFK-ZAUG | IC-2322 | 2023-10-11 | IT Infrastructure |
| SIG-12-RDG-0JI1 | TC-2326 | 2023-09-25 | Supply Chain |
| SIG-60-QPM-2TRI | BC-2331 | 2024-01-08 | Compliance |
| SIG-99-QXY-X4NT | BC-2341 | 2021-07-06 | Compliance |
| SIG-79-SPO-WT80 | IC-2348 | 2023-05-12 | Supply Chain |
| SIG-91-UWU-GPZB | BC-2358 | 2024-06-11 | Product Management |
| SIG-27-WVB-8FZQ | IC-2370 | 2022-12-07 | Data Governance |
| SIG-43-GRJ-P3HT | BC-2380 | 2023-10-21 | Supply Chain |
| SIG-36-XEW-9SSB | TC-2386 | 2021-12-07 | Data Governance |
| SIG-68-ELC-6AVE | BC-2395 | 2024-03-16 | IT Infrastructure |
| SIG-95-LLS-0RNG | BC-2401 | 2024-07-02 | Compliance |
| SIG-16-FVU-3EBQ | TC-2405 | 2024-05-20 | Data Governance |
| SIG-39-OZI-N968 | BC-2411 | 2024-01-27 | Finance |
| SIG-22-XCC-QSNV | TC-2413 | 2021-09-28 | Operations |
| SIG-85-WWC-01LO | BC-2426 | 2023-03-28 | Finance |
| SIG-83-BZY-VHAE | TC-2435 | 2024-10-04 | Operations |
| SIG-63-KXZ-46Q1 | TC-2445 | 2022-03-04 | IT Infrastructure |
| SIG-83-PIY-NKQE | IC-2454 | 2024-04-17 | Compliance |
| SIG-90-SZM-PZJ4 | IC-2465 | 2024-05-28 | Compliance |
| SIG-14-MOL-USHF | TC-2472 | 2022-03-28 | Supply Chain |
| SIG-84-VYG-QI55 | TC-2483 | 2024-07-23 | Data Governance |
| SIG-39-FND-AALU | TC-2494 | 2024-05-11 | Operations |
| SIG-16-YRD-5C3Z | TC-2500 | 2023-12-07 | Product Management |
| SIG-84-EIB-2MOT | TC-2510 | 2022-10-25 | Supply Chain |
| SIG-47-LBV-Y27V | IC-2512 | 2024-03-10 | Operations |
| SIG-57-HAE-WNSM | TC-2518 | 2023-11-15 | Supply Chain |
| SIG-78-NWO-RO6D | BC-2522 | 2023-03-24 | Operations |
| SIG-80-QNF-AHPO | TC-2526 | 2022-12-22 | Compliance |
| SIG-66-RQA-05UV | BC-2534 | 2024-08-01 | Supply Chain |
| SIG-47-HPA-L2FX | BC-2542 | 2023-08-10 | Data Governance |
| SIG-57-YOY-F7N2 | IC-2549 | 2022-03-18 | Compliance |
| SIG-44-QME-TTIM | BC-2551 | 2023-12-08 | Compliance |
| SIG-56-LHF-WMFP | BC-2559 | 2022-08-13 | IT Infrastructure |
| SIG-34-GNA-EHC2 | TC-2560 | 2024-07-28 | Data Governance |
| SIG-73-UUF-1F99 | TC-2565 | 2023-12-07 | Finance |
| SIG-64-QID-BCT3 | IC-2573 | 2024-09-06 | Supply Chain |
| SIG-48-IWQ-OJ98 | BC-2584 | 2021-04-19 | Product Management |
| SIG-94-MGT-4WYA | BC-2588 | 2024-03-04 | Compliance |
| SIG-40-OEJ-4XCR | IC-2602 | 2023-02-20 | IT Infrastructure |
| SIG-26-PJJ-DUD8 | TC-2619 | 2024-06-10 | Product Management |
| SIG-82-OMQ-EPBO | IC-2625 | 2021-03-05 | Supply Chain |
| SIG-68-VDM-0UT1 | TC-2632 | 2021-03-11 | Operations |
| SIG-61-HXH-PFBC | TC-2637 | 2022-10-26 | Finance |
| SIG-13-WHV-DDIN | IC-2653 | 2021-10-24 | IT Infrastructure |
| SIG-47-NVU-R3XU | IC-2659 | 2024-09-11 | Finance |
| SIG-64-BPY-A8RD | TC-2665 | 2022-07-12 | IT Infrastructure |
| SIG-39-UPB-Q8DA | TC-2670 | 2022-09-06 | Compliance |
| SIG-60-ZEV-V2NY | TC-2673 | 2021-07-05 | Compliance |
| SIG-37-MXA-3C7Q | TC-2683 | 2023-08-13 | Supply Chain |
| SIG-85-VFA-F0TJ | BC-2694 | 2022-08-01 | IT Infrastructure |
| SIG-42-LOE-5XD8 | BC-2700 | 2024-05-19 | Data Governance |
| SIG-78-OGT-WEKQ | TC-2706 | 2023-08-21 | IT Infrastructure |
| SIG-81-SBE-HL1C | IC-2714 | 2024-08-20 | IT Infrastructure |
| SIG-64-LXA-3LJO | TC-2730 | 2021-08-16 | Compliance |
| SIG-24-SWK-GROA | TC-2736 | 2021-09-22 | Supply Chain |
| SIG-47-QLD-IL46 | IC-2743 | 2024-11-20 | Finance |
| SIG-80-PTU-ILTR | TC-2751 | 2021-06-10 | Operations |
| SIG-34-IKF-VQJA | TC-2758 | 2023-07-16 | Data Governance |
| SIG-92-DNQ-WJAT | IC-2768 | 2022-03-10 | Finance |
| SIG-73-WMX-7XJJ | TC-2773 | 2022-07-06 | Supply Chain |
| SIG-20-UMV-LJM6 | TC-2788 | 2022-06-22 | Compliance |
| SIG-65-XHR-R1SP | TC-2792 | 2022-08-08 | Compliance |
| SIG-99-VAH-2H31 | BC-2799 | 2023-04-24 | Operations |
| SIG-71-FNO-CX9K | TC-2804 | 2022-04-05 | Product Management |
| SIG-29-KJI-GJKC | TC-2808 | 2024-12-10 | Finance |
| SIG-86-AKS-BEQE | IC-2827 | 2023-07-13 | Operations |
| SIG-67-TPL-WT5F | TC-2839 | 2023-08-14 | Product Management |
| SIG-92-ZTO-VZGU | TC-2854 | 2023-01-11 | Compliance |
| SIG-61-IQH-EKWH | BC-2862 | 2023-05-20 | Supply Chain |
| SIG-21-HVD-EZVS | BC-2869 | 2024-01-22 | IT Infrastructure |
| SIG-36-ZKX-4SE4 | TC-2880 | 2022-10-07 | Compliance |
| SIG-26-KHF-99OH | BC-2897 | 2024-11-15 | Product Management |
| SIG-46-YHU-BU2J | IC-2903 | 2024-11-28 | Finance |
| SIG-36-MYP-7NC2 | BC-2913 | 2021-04-01 | Operations |
| SIG-80-WEB-2C7R | IC-2919 | 2021-10-25 | Product Management |
| SIG-45-CWR-EI9N | TC-2928 | 2023-07-10 | Supply Chain |
| SIG-12-NAY-4AKW | BC-2932 | 2021-06-09 | Operations |
| SIG-34-JQN-ROWX | BC-2945 | 2023-07-14 | Finance |
| SIG-27-FHX-VO6Y | BC-2950 | 2021-11-27 | Finance |
| SIG-53-LJE-NZKR | IC-2955 | 2024-01-07 | Compliance |
| SIG-64-VUE-OGQ2 | TC-2967 | 2024-05-21 | Product Management |
| SIG-77-LFQ-EKT4 | IC-2974 | 2024-01-11 | Supply Chain |
| SIG-24-CXH-R2TY | TC-2980 | 2024-09-14 | Finance |
| SIG-64-TCV-R5SR | BC-2993 | 2022-07-16 | IT Infrastructure |
| SIG-39-JMB-X1VA | TC-3001 | 2022-05-17 | Operations |
| SIG-65-RQH-9Y5B | TC-3006 | 2022-03-01 | Product Management |
| SIG-43-KEL-FPY6 | TC-3014 | 2024-09-24 | Finance |
| SIG-57-RQB-VIKB | IC-3017 | 2022-03-04 | Compliance |
| SIG-13-CGO-2Y4L | IC-3033 | 2022-02-05 | Finance |
| SIG-13-FYG-4NN9 | TC-3041 | 2021-02-21 | Supply Chain |
| SIG-27-QBE-DEK4 | BC-3047 | 2021-04-02 | Finance |
| SIG-97-LME-ZEH9 | IC-3054 | 2023-07-17 | Product Management |
| SIG-60-KAS-IVMD | IC-3062 | 2021-12-20 | Operations |
| SIG-99-GVJ-VPM6 | IC-3068 | 2021-07-10 | Data Governance |
| SIG-20-CGL-C8HS | BC-3076 | 2024-06-11 | Supply Chain |
| SIG-68-DWS-MNR6 | TC-3087 | 2022-06-17 | Data Governance |
| SIG-86-VCP-SVOL | TC-3100 | 2021-03-25 | Data Governance |
| SIG-80-MLG-VDQ0 | IC-3105 | 2024-12-13 | Supply Chain |
| SIG-63-JJG-1TCH | TC-3116 | 2023-06-26 | Compliance |
| SIG-78-LTE-H4VL | IC-3120 | 2023-10-13 | Data Governance |
| SIG-50-JOR-LO4P | BC-3124 | 2022-11-01 | Compliance |
| SIG-55-DCV-7OXN | TC-3129 | 2024-11-11 | Data Governance |
| SIG-20-BPG-W8VL | TC-3133 | 2021-07-17 | Data Governance |
| SIG-37-WYK-X3LH | IC-3141 | 2022-02-12 | Data Governance |
| SIG-64-LSR-RORA | TC-3150 | 2023-04-19 | Data Governance |
| SIG-40-PLP-7A3U | IC-3156 | 2023-04-19 | Finance |
| SIG-52-FHA-5PI2 | TC-3165 | 2024-02-14 | Product Management |
| SIG-56-SME-QSOD | BC-3180 | 2024-03-24 | IT Infrastructure |
| SIG-61-MHS-BQG3 | TC-3188 | 2023-10-28 | Compliance |
| SIG-23-IEJ-V2T3 | BC-3194 | 2024-08-03 | Supply Chain |
| SIG-12-JLN-YFH3 | BC-3200 | 2021-11-21 | Product Management |
| SIG-83-XMM-APXP | IC-3205 | 2021-02-03 | Data Governance |
| SIG-89-TVE-WANI | TC-3211 | 2023-10-21 | Operations |
| SIG-85-FIY-2QW4 | IC-3218 | 2023-03-19 | Compliance |
| SIG-23-UKD-B8UO | BC-3225 | 2024-01-04 | Finance |
| SIG-63-YJW-AP00 | IC-3229 | 2023-02-20 | Data Governance |
| SIG-76-GDP-2JN8 | TC-3237 | 2021-08-13 | Compliance |
| SIG-24-OUE-RXOK | IC-3242 | 2022-03-15 | Operations |
| SIG-26-ADB-B4F0 | BC-3249 | 2024-08-24 | Supply Chain |
| SIG-48-ZZX-UQIO | TC-3254 | 2021-05-25 | Supply Chain |
| SIG-62-GDA-2IVD | BC-3260 | 2024-02-19 | Supply Chain |
| SIG-30-UET-0Q2O | IC-3266 | 2021-06-20 | Supply Chain |
| SIG-39-SLB-MLCB | BC-3277 | 2024-05-16 | Compliance |
| SIG-76-RKG-E8RT | TC-3282 | 2024-06-22 | Product Management |
| SIG-87-YFT-P51V | BC-3287 | 2021-12-02 | IT Infrastructure |
| SIG-92-CZO-O9ON | BC-3302 | 2021-01-10 | IT Infrastructure |
| SIG-79-IKL-24HE | TC-3308 | 2021-09-08 | Data Governance |
| SIG-88-VVU-EL88 | BC-3310 | 2023-12-22 | Finance |
| SIG-50-XSG-WQVA | TC-3315 | 2021-08-13 | Finance |
| SIG-82-GZF-51ZF | BC-3330 | 2021-09-13 | Compliance |
| SIG-24-VEK-YPIS | BC-3340 | 2022-10-01 | Operations |
| SIG-35-SZU-VMRU | IC-3354 | 2021-02-09 | Finance |
| SIG-24-PBC-613L | IC-3361 | 2023-07-01 | Finance |
| SIG-62-BTJ-PQV9 | TC-3365 | 2023-08-08 | Supply Chain |
| SIG-41-HXT-0U1R | TC-3371 | 2024-06-03 | Operations |
| SIG-83-OTU-QZB6 | BC-3373 | 2021-11-06 | Compliance |
| SIG-66-MYF-XDYQ | BC-3379 | 2024-10-10 | IT Infrastructure |
| SIG-63-KMB-9J7M | BC-3387 | 2023-06-28 | Data Governance |
| SIG-16-IYP-EOZP | TC-3393 | 2021-11-18 | Compliance |
| SIG-71-CWF-DGP5 | TC-3397 | 2024-08-05 | IT Infrastructure |
| SIG-27-SJP-0JO4 | BC-3403 | 2024-08-09 | Compliance |
| SIG-88-RKE-8R7A | TC-3417 | 2023-07-25 | Supply Chain |
| SIG-14-WZC-EEWK | BC-3422 | 2023-11-17 | Finance |
| SIG-94-IBE-STPB | TC-3430 | 2024-12-11 | Compliance |
| SIG-76-IIX-V2Y9 | BC-3443 | 2023-12-20 | Operations |
| SIG-75-DRM-1CLN | IC-3451 | 2022-02-02 | Compliance |
| SIG-48-ASO-8G0Y | IC-3452 | 2022-05-11 | Finance |
| SIG-29-RWA-CHL8 | IC-3462 | 2021-02-15 | Finance |
| SIG-13-TIV-U5CX | BC-3469 | 2022-04-25 | Supply Chain |
| SIG-18-SSS-CTEL | IC-3476 | 2021-03-26 | Supply Chain |
| SIG-77-TUK-IN2B | IC-3477 | 2021-10-23 | Compliance |
| SIG-23-BLM-EZKX | IC-3491 | 2024-03-10 | Supply Chain |
| SIG-63-MOD-EKOJ | IC-3498 | 2021-08-18 | Supply Chain |
| SIG-79-RKA-P64T | TC-3504 | 2024-05-08 | Supply Chain |
| SIG-73-KLZ-PDKU | TC-3521 | 2021-07-21 | Finance |
| SIG-16-MNF-F4AF | IC-3529 | 2024-11-09 | Compliance |
| SIG-12-HNK-0H4F | IC-3532 | 2022-08-12 | Supply Chain |
| SIG-44-HTV-P84J | BC-3533 | 2021-10-13 | Compliance |
| SIG-24-NPE-GDMB | IC-3536 | 2024-09-18 | Finance |
| SIG-50-SVK-9TOS | BC-3539 | 2023-11-06 | Finance |
| SIG-80-QOK-BKBF | BC-3551 | 2024-10-09 | Compliance |
| SIG-86-HYW-79YR | TC-3564 | 2021-06-27 | Compliance |
| SIG-87-DSD-DF5J | TC-3571 | 2022-12-08 | Data Governance |
| SIG-29-YUO-5FO9 | IC-3578 | 2022-02-15 | Operations |
| SIG-67-VXU-FPWB | TC-3586 | 2023-03-23 | Product Management |
| SIG-93-ZCF-6HM3 | BC-3589 | 2022-06-10 | IT Infrastructure |
| SIG-42-IEF-RFC9 | BC-3596 | 2022-07-16 | Data Governance |
| SIG-86-DMG-XSKY | BC-3607 | 2024-10-28 | Product Management |
| SIG-20-UGT-P0LW | IC-3608 | 2022-12-18 | IT Infrastructure |
| SIG-36-TML-VS0J | IC-3616 | 2024-04-18 | Compliance |
| SIG-53-TLC-AZKT | TC-3621 | 2023-05-14 | Product Management |
| SIG-13-IPI-71PJ | BC-3626 | 2023-04-09 | Operations |
| SIG-15-PFO-2W85 | IC-3633 | 2024-04-13 | Data Governance |
| SIG-61-CIV-LFWA | TC-3647 | 2021-08-21 | Data Governance |
| SIG-38-YGZ-FBOJ | TC-3653 | 2022-11-17 | Finance |
| SIG-15-FOA-70S8 | IC-3659 | 2024-04-05 | Product Management |
| SIG-97-XJT-7TBU | IC-3669 | 2024-07-13 | Product Management |
| SIG-93-DAB-6LKS | BC-3672 | 2024-04-11 | Product Management |
| SIG-11-QDU-30PE | IC-3677 | 2022-11-26 | Finance |
| SIG-58-SBP-KRSZ | IC-3683 | 2023-06-15 | Product Management |
| SIG-27-QBW-ROGA | TC-3688 | 2021-12-21 | Data Governance |
| SIG-77-CMG-ORNE | IC-3690 | 2022-09-22 | Compliance |
| SIG-82-JMP-PVGN | BC-3698 | 2023-02-16 | IT Infrastructure |
| SIG-82-IYU-XY3P | TC-3702 | 2023-10-21 | IT Infrastructure |
| SIG-37-PYQ-815V | BC-3707 | 2024-06-22 | Supply Chain |
| SIG-20-OAV-1IKJ | TC-3714 | 2023-05-05 | Operations |
| SIG-20-XIG-T8ME | TC-3721 | 2022-11-06 | Operations |
| SIG-37-HHT-38YO | TC-3722 | 2021-02-25 | IT Infrastructure |
| SIG-63-LNS-ECTA | BC-3734 | 2024-03-21 | Operations |
| SIG-91-WVE-3ESP | IC-3739 | 2024-01-04 | Operations |
| SIG-78-RAG-D2IP | TC-3741 | 2023-07-06 | Finance |
| SIG-92-RZH-LRHH | BC-3744 | 2024-10-15 | Data Governance |
| SIG-94-TOI-OFNK | IC-3754 | 2022-04-03 | Operations |
| SIG-77-LSN-T27F | IC-3757 | 2022-08-22 | Finance |
| SIG-27-NTH-I37Y | BC-3770 | 2021-01-27 | Data Governance |
| SIG-84-MGK-H2ME | IC-3774 | 2022-05-01 | Compliance |
| SIG-39-DJJ-3SY8 | TC-3778 | 2022-07-10 | Data Governance |
| SIG-82-UMX-OJ7L | TC-3787 | 2024-07-03 | Product Management |
| SIG-22-SKR-CTIC | TC-3791 | 2022-05-09 | Supply Chain |
| SIG-67-MFG-46DE | TC-3795 | 2021-03-27 | Supply Chain |
| SIG-38-YTD-7BST | IC-3801 | 2024-10-07 | IT Infrastructure |
| SIG-58-LWY-Q8P6 | BC-3806 | 2024-12-16 | Supply Chain |
| SIG-91-FOC-36I6 | BC-3817 | 2022-01-01 | Compliance |
| SIG-84-DSO-4S47 | BC-3822 | 2022-08-28 | Compliance |
| SIG-99-IMJ-KFOM | BC-3828 | 2024-10-08 | Product Management |
| SIG-42-STL-CX7L | TC-3831 | 2021-06-16 | Data Governance |
| SIG-50-ABM-7VSK | IC-3840 | 2021-03-09 | IT Infrastructure |
| SIG-95-APX-PWFS | BC-3852 | 2022-04-12 | IT Infrastructure |
| SIG-52-ITT-ELH9 | TC-3856 | 2022-06-03 | Supply Chain |
| SIG-64-IEU-FRGN | BC-3862 | 2024-08-04 | Finance |
| SIG-80-WKN-N0SS | IC-3870 | 2024-09-19 | Supply Chain |
| SIG-41-QPX-D1RL | IC-3877 | 2023-10-01 | Compliance |
| SIG-89-ISH-EQW6 | IC-3887 | 2022-10-14 | Finance |
| SIG-61-PIG-0DBF | BC-3900 | 2021-12-20 | Operations |
| SIG-56-NOU-ZR98 | IC-3906 | 2024-03-09 | Product Management |
| SIG-90-SJW-O06V | BC-3917 | 2022-03-25 | Product Management |
| SIG-47-UCC-EFEL | IC-3926 | 2021-06-04 | Compliance |
| SIG-62-YMZ-RQQI LLC | IC-3929 | 2023-06-14 | Data Governance |
| SIG-93-TEG-8CN0 SARL | IC-3931 | 2024-02-20 | Compliance |
| SIG-56-EAF-SHQE Group | IC-3935 | 2023-01-05 | Supply Chain |
| SIG-42-NMJ-RACV International | BC-3939 | 2022-01-22 | Data Governance |
| SIG-97-TPD-0NJR LLC | BC-3944 | 2021-06-05 | Product Management |
| SIG-82-YQL-Q0L4 NV | IC-3949 | 2023-11-23 | Data Governance |
| SIG-56-ZQV-YINP SA | TC-3954 | 2024-07-27 | Operations |
| SIG-79-TAG-A44Y | BC-3957 | 2022-09-12 | IT Infrastructure |
| SIG-59-VFK-OOZW SA | BC-3961 | 2021-03-28 | Data Governance |
| SIG-41-LKO-OD4P Ltd. | TC-3967 | 2024-04-14 | Product Management |
| SIG-86-XWS-MOPG Corp. | IC-3972 | 2021-09-15 | Product Management |
| SIG-84-EQC-XHMK Holdings | BC-3986 | 2023-08-26 | Finance |
| SIG-71-KJM-D5G1 Holdings | TC-3995 | 2023-12-20 | Operations |
| SIG-63-DWD-X8UB | BC-4003 | 2023-12-19 | IT Infrastructure |
| SIG-53-DUL-C550 Group | IC-4005 | 2024-10-09 | Operations |
| SIG-17-FUU-SGT6 KG | IC-4016 | 2024-07-19 | Product Management |
| SIG-26-PVD-6QGC AG | IC-4023 | 2024-06-26 | Compliance |
| SIG-61-FGJ-AO1L NV | IC-4030 | 2024-05-10 | Finance |
| SIG-87-OKN-L3O4 | IC-4034 | 2024-07-15 | Finance |
| SIG-54-QHS-YUMN | BC-4039 | 2021-06-25 | Finance |
| SIG-70-SAQ-KIAC | BC-4049 | 2022-12-08 | Product Management |
| SIG-22-RFO-RZQE | BC-4052 | 2022-09-19 | Operations |
| SIG-23-LAS-L2MX Holdings | BC-4054 | 2023-01-24 | Product Management |
| SIG-44-LEF-PDJN SARL | TC-4063 | 2022-03-04 | Compliance |
| SIG-14-HVI-T0Z6 SARL | TC-4068 | 2023-08-14 | Compliance |
| SIG-81-LVQ-2J60 | TC-4073 | 2021-09-05 | Data Governance |
| SIG-95-HLU-HD5X GmbH | TC-4080 | 2021-11-17 | Supply Chain |
| SIG-99-TBJ-83YG KG | IC-4096 | 2024-06-26 | Operations |
| SIG-98-WXH-VOMX | BC-4103 | 2022-02-13 | Compliance |
| SIG-42-SPP-A6C6 | TC-4108 | 2024-12-16 | Supply Chain |
| SIG-85-SQB-MODP BV | IC-4114 | 2024-07-09 | Operations |
| SIG-48-JXQ-RFSL LLC | BC-4119 | 2024-06-13 | Data Governance |
| SIG-62-JPL-NU17 Holdings | TC-4131 | 2024-05-24 | Data Governance |
| SIG-51-BUX-VLME Group | TC-4141 | 2022-07-28 | Operations |
| SIG-64-MMA-YU3T NV | BC-4150 | 2021-09-04 | Product Management |
| SIG-65-IJJ-DXAJ SA | BC-4157 | 2024-12-20 | Operations |
| SIG-88-RGQ-WZOI | BC-4164 | 2021-07-18 | Product Management |
| SIG-23-WOJ-YTND International | TC-4168 | 2022-04-22 | Supply Chain |
| SIG-92-FQX-S1BC | TC-4179 | 2023-10-10 | Finance |
| SIG-35-BYM-BYQ7 Inc. | BC-4190 | 2022-04-06 | Compliance |
| SIG-56-JML-GDXB | BC-4202 | 2024-05-04 | Compliance |
| SIG-70-YLY-65JU PLC | IC-4209 | 2022-10-12 | Operations |
| SIG-93-ABB-76KE | IC-4215 | 2024-05-19 | Supply Chain |
| SIG-51-ZHS-W8WR International | BC-4218 | 2021-03-10 | Product Management |
| SIG-25-KUC-FYE7 Ltd. | TC-4227 | 2022-06-09 | Product Management |
| SIG-72-JWR-R2ZI BV | BC-4229 | 2022-12-04 | Product Management |
| SIG-86-JBA-HCDI | BC-4239 | 2022-10-01 | Compliance |
| SIG-32-DNR-U0SL | TC-4242 | 2022-03-08 | IT Infrastructure |
| SIG-63-OTU-T27J Corp. | BC-4250 | 2021-02-11 | Product Management |
| SIG-49-LWO-P3PY | TC-4263 | 2021-01-25 | Operations |
| SIG-11-LPV-TM1Q International | BC-4272 | 2021-06-27 | Operations |
| SIG-32-VLW-1KKT NV | TC-4278 | 2024-05-14 | Finance |
| SIG-55-OVK-B4MF GmbH | TC-4284 | 2023-08-21 | Product Management |
| SIG-89-WUP-8NG0 | IC-4288 | 2021-07-22 | Finance |
| SIG-31-CWH-OC2T | IC-4297 | 2024-11-16 | Operations |
| SIG-18-CIG-ZUL8 Holdings | TC-4306 | 2022-02-01 | Compliance |
| SIG-58-WYL-XCXB | BC-4315 | 2024-04-26 | Operations |
| SIG-78-WKT-9TDY SAS | IC-4322 | 2022-11-05 | Operations |
| SIG-39-WTU-81JC | TC-4334 | 2022-06-05 | Data Governance |
| SIG-75-XPL-QWB7 GmbH | BC-4341 | 2022-07-24 | Supply Chain |
| SIG-62-NKL-SM8R | TC-4348 | 2022-11-09 | Compliance |
| SIG-79-IWJ-YNSA | BC-4358 | 2022-10-04 | Data Governance |
| SIG-14-WWQ-VPK2 SARL | TC-4371 | 2021-02-27 | Compliance |
| SIG-27-QTK-7Y6C | BC-4376 | 2021-09-19 | Operations |
| SIG-93-YGI-KLQ0 | IC-4377 | 2022-04-07 | Finance |
| SIG-70-EXR-LD0M | IC-4390 | 2023-08-27 | Operations |
| SIG-12-QLD-RUJ3 Inc. | IC-4398 | 2022-01-14 | IT Infrastructure |
| SIG-74-LEZ-GZA2 AG | IC-4414 | 2023-10-18 | Finance |
| SIG-40-CXK-QT2E Group | TC-4421 | 2024-09-10 | IT Infrastructure |
| SIG-96-ANZ-BP7C SA | TC-4428 | 2021-01-23 | Supply Chain |
| SIG-28-FYV-P1ZR Group | BC-4429 | 2024-12-02 | IT Infrastructure |
| SIG-40-RSD-JF0U | TC-4434 | 2022-06-20 | Product Management |
| SIG-83-TNT-G0Q1 AG | IC-4438 | 2022-10-25 | Operations |
| SIG-88-RUZ-O3Q0 | IC-4447 | 2023-01-05 | Supply Chain |
| SIG-58-BDP-AYRN | TC-4450 | 2023-05-13 | IT Infrastructure |
| SIG-29-BKQ-HXCX Group | IC-4463 | 2022-04-18 | Compliance |
| SIG-60-FRA-PB5V Holdings | TC-4468 | 2023-01-11 | Operations |
| SIG-28-AOC-YRBZ Corp. | IC-4473 | 2023-02-24 | Finance |
| SIG-81-AXG-9CBI AG | TC-4479 | 2022-08-21 | Product Management |
| SIG-54-ZOX-KCNY SAS | IC-4484 | 2022-06-19 | Supply Chain |
| SIG-31-MAP-SEFM | BC-4491 | 2023-12-19 | Supply Chain |
| SIG-65-ONA-WQOF Corp. | BC-4498 | 2024-01-17 | IT Infrastructure |
| SIG-54-ZFB-4REP Inc. | IC-4504 | 2022-12-24 | Data Governance |
| SIG-76-COR-DQEF GmbH | BC-4510 | 2024-02-15 | Product Management |
| SIG-82-POX-I1CU | IC-4517 | 2023-01-07 | Product Management |
| SIG-67-MFU-QOZ9 Group | BC-4528 | 2023-07-14 | Product Management |
| SIG-59-CFT-59LL Holdings | BC-4535 | 2023-03-24 | Compliance |
| SIG-81-EKU-R7CX Group | TC-4543 | 2023-04-28 | Data Governance |
| SIG-45-JPK-8INR | IC-4550 | 2021-01-15 | Operations |
| SIG-60-XUT-HTI7 | TC-4560 | 2023-04-16 | Operations |
| SIG-91-GKA-MSWV | TC-4565 | 2022-12-01 | Operations |
| SIG-53-OGW-YU4I Ltd. | TC-4576 | 2023-11-05 | Product Management |
| SIG-83-MZM-HGMN GmbH | IC-4586 | 2024-06-28 | Operations |
| SIG-58-DDZ-4JKE International | BC-4592 | 2024-11-22 | Product Management |
| SIG-17-BCC-01JW | BC-4594 | 2021-04-17 | Compliance |
| SIG-50-HWB-Y27E Ltd. | IC-4598 | 2024-09-16 | Operations |
| SIG-55-GSW-Z8Y2 Ltd. | BC-4604 | 2022-09-12 | Product Management |
| SIG-51-HOK-PC9S Holdings | IC-4609 | 2022-09-26 | Finance |
| SIG-31-LDA-I5LG Ltd. | BC-4626 | 2021-01-18 | Compliance |
| SIG-94-OAX-GACW Ltd. | IC-4637 | 2024-05-12 | Data Governance |
| SIG-68-SJS-K3N3 | TC-4646 | 2024-08-10 | Data Governance |
| SIG-36-FMG-DSYM Group | IC-4654 | 2021-06-14 | Operations |
| SIG-59-ZZK-AYAJ PLC | BC-4671 | 2023-10-26 | Operations |
| SIG-86-XNZ-5Q7H | IC-4683 | 2021-11-21 | Compliance |
| SIG-97-PAD-AUZ7 | BC-4686 | 2022-07-13 | Finance |
| SIG-14-TOH-IPJ4 | IC-4697 | 2022-10-20 | Supply Chain |
| SIG-18-ANT-0DK4 GmbH | IC-4702 | 2024-10-19 | Product Management |
| SIG-16-GDL-YC2T LLC | BC-4708 | 2023-09-18 | Compliance |
| SIG-38-QCS-G19Q Holdings | IC-4717 | 2023-10-07 | Finance |
| SIG-37-YMX-1ATI SARL | TC-4723 | 2024-02-11 | Compliance |
| SIG-45-ZZU-GRXH International | IC-4731 | 2024-05-12 | Operations |
| SIG-12-JYK-S9KT Group | IC-4752 | 2021-10-14 | Operations |
| SIG-41-ZTZ-VNMI Holdings | TC-4769 | 2023-05-26 | Product Management |
| SIG-34-TUW-UWNZ Group | BC-4789 | 2023-09-08 | Finance |
| SIG-73-XKX-JG0D SAS | BC-4795 | 2022-04-11 | Operations |
| SIG-94-CCX-H0AN International | IC-4800 | 2021-06-15 | Finance |
| SIG-40-JOQ-S1CO KG | IC-4802 | 2023-06-17 | Compliance |
| SIG-59-IWS-F4PJ | IC-4816 | 2021-02-28 | Supply Chain |
| SIG-83-BZN-2A0N KG | TC-4825 | 2023-10-03 | Operations |
| SIG-55-ICI-Z2GP GmbH | IC-4833 | 2021-03-16 | Data Governance |
| SIG-68-HOK-ETCC | IC-4849 | 2022-10-28 | Supply Chain |
| SIG-37-AVX-CY7Q SAS | IC-4853 | 2021-11-10 | Supply Chain |
| SIG-31-YNJ-FQMJ Holdings | BC-4860 | 2022-01-04 | Finance |
| SIG-28-KHD-E4FM NV | TC-4867 | 2023-08-22 | Compliance |
| SIG-88-MKW-I0IO NV | TC-4870 | 2021-06-13 | Supply Chain |
| SIG-60-GCS-MZ2C Ltd. | IC-4875 | 2021-03-19 | Data Governance |
| SIG-86-QTB-N3VO International | TC-4878 | 2021-08-10 | Finance |
| SIG-13-RWR-7JHQ SA | TC-4884 | 2023-03-13 | Data Governance |
| SIG-28-OZR-B7E8 Group | BC-4885 | 2022-03-08 | Compliance |
| SIG-39-JXL-BQ85 SARL | BC-4900 | 2022-06-19 | Compliance |
| SIG-99-PXI-1L7K | IC-4906 | 2021-02-26 | Operations |
| SIG-89-RGS-FIRM Holdings | BC-4912 | 2021-01-18 | Finance |
| SIG-77-TQY-IC8H Holdings | IC-4920 | 2024-08-14 | IT Infrastructure |
| SIG-39-ZIX-L5KV International | BC-4933 | 2024-02-26 | Operations |
| SIG-59-HZI-WDX6 Group | BC-4941 | 2022-07-27 | Data Governance |
| SIG-92-AXW-GPAG | IC-4949 | 2021-06-28 | Supply Chain |
| SIG-36-PWY-HJFC International | TC-4954 | 2023-03-26 | Finance |
| SIG-90-ZPA-GKE1 BV | TC-4962 | 2021-02-01 | IT Infrastructure |
| SIG-15-TGS-WDIJ Group | TC-4969 | 2023-08-24 | Operations |
| SIG-40-BRW-FV7U | TC-4977 | 2023-04-27 | Compliance |
| SIG-82-DAB-YHKJ | IC-4982 | 2023-08-20 | Compliance |
| SIG-14-HQE-PUWC | TC-4990 | 2023-04-01 | Operations |
| SIG-32-WFB-DVCF International | BC-4998 | 2024-07-10 | Finance |
| SIG-44-HLB-IC48 SARL | IC-5003 | 2022-08-07 | Supply Chain |
| SIG-57-RYP-D466 | BC-5016 | 2022-11-06 | Compliance |
| SIG-41-LVX-8RWD SAS | BC-5024 | 2022-08-12 | IT Infrastructure |
| SIG-79-DZB-60U2 International | BC-5028 | 2022-04-06 | Data Governance |
| SIG-64-GUK-32QL SARL | IC-5038 | 2024-04-14 | IT Infrastructure |
| SIG-35-VQC-JQ0H AG | BC-5046 | 2021-05-12 | Finance |
| SIG-77-WCC-DNFC Holdings | IC-5054 | 2022-07-06 | Compliance |
| SIG-47-BQW-HBQI NV | IC-5061 | 2021-08-21 | Operations |
| SIG-46-YOE-MYAX SA | BC-5065 | 2023-06-18 | Finance |
| SIG-69-FIT-Y3OC International | TC-5076 | 2021-08-05 | Finance |
| SIG-59-HVI-BACX Group | BC-5080 | 2024-11-20 | IT Infrastructure |
| SIG-19-KAW-QNPA | TC-5085 | 2024-08-02 | IT Infrastructure |
| SIG-41-VXU-J3AN | TC-5100 | 2022-04-26 | Data Governance |
| SIG-17-UCE-6H7J Corp. | IC-5106 | 2022-04-04 | Supply Chain |
| SIG-63-LZV-C5BN | BC-5113 | 2023-01-17 | Supply Chain |
| SIG-52-CQW-KL19 | IC-5119 | 2024-07-18 | Data Governance |
| SIG-17-GFH-X0JO PLC | TC-5122 | 2024-11-22 | Product Management |
| SIG-17-ZBZ-BJS4 SARL | BC-5132 | 2022-07-10 | Operations |
| SIG-83-OGL-6IBH Group | IC-5134 | 2024-07-06 | Supply Chain |
| SIG-58-CJW-XYEP BV | IC-5147 | 2022-06-15 | Operations |
| SIG-53-NHM-OFA2 | IC-5163 | 2021-06-26 | Supply Chain |
| SIG-98-SID-2107 GmbH | BC-5169 | 2023-08-24 | IT Infrastructure |
| SIG-27-DQT-IQ97 | TC-5175 | 2023-06-19 | IT Infrastructure |
| SIG-99-CTB-8OFG Group | BC-5185 | 2024-08-15 | Product Management |
| SIG-83-BQM-NXXK PLC | BC-5192 | 2023-07-06 | IT Infrastructure |
| SIG-43-AAR-M0YW | TC-5197 | 2023-07-22 | Compliance |
| SIG-58-MRH-P47P | IC-5211 | 2022-05-12 | Finance |
| SIG-36-XXX-LH5B NV | IC-5217 | 2021-04-15 | Supply Chain |
| SIG-52-JLE-5KJF SAS | IC-5223 | 2022-04-27 | Operations |
| SIG-85-CHF-5W9X SA | IC-5237 | 2023-12-19 | Supply Chain |
| SIG-61-YSE-8JLK SARL | IC-5246 | 2023-09-08 | Data Governance |
| SIG-94-MUO-QFTQ | BC-5262 | 2021-10-20 | Product Management |
| SIG-85-GWL-FUXA | BC-5267 | 2021-12-26 | Data Governance |
| SIG-77-RVO-CE8D Inc. | IC-5282 | 2024-07-04 | Operations |
| SIG-58-LVK-OFDU KG | IC-5284 | 2023-08-18 | Finance |
| SIG-83-TEU-OH8F Group | IC-5296 | 2021-04-23 | Compliance |
| SIG-72-OHB-75ML SAS | IC-5308 | 2022-06-21 | Product Management |
| SIG-59-HRE-WMJT | TC-5311 | 2022-10-06 | Operations |
| SIG-78-TUT-T3NS | TC-5319 | 2024-02-10 | Finance |
| SIG-29-LEJ-26GF Group | IC-5325 | 2024-05-20 | Product Management |
| SIG-48-MQG-OVJU SAS | IC-5338 | 2022-01-11 | Compliance |
| SIG-41-ZGH-C0Y2 Holdings | TC-5341 | 2024-02-22 | Supply Chain |
| SIG-40-DEO-UM9B International | IC-5351 | 2024-03-19 | Finance |
| SIG-99-AYV-D18J International | TC-5366 | 2021-12-26 | Compliance |
| SIG-85-CBK-XO7I | TC-5368 | 2021-07-15 | Operations |
| SIG-59-HNQ-A8N5 Ltd. | IC-5378 | 2021-08-26 | Finance |
| SIG-68-BSO-NW8J Group | BC-5384 | 2021-07-17 | Operations |
| SIG-43-MIT-DWCJ SA | BC-5390 | 2022-03-23 | Compliance |
| SIG-98-OXJ-W0H6 SAS | BC-5392 | 2021-01-08 | Product Management |
| SIG-58-FND-MEQW Ltd. | BC-5400 | 2022-09-17 | Product Management |
| SIG-78-QFN-H3BV | IC-5406 | 2022-11-25 | IT Infrastructure |
| SIG-60-GZP-BB7N NV | BC-5414 | 2024-06-15 | Data Governance |
| SIG-50-GYK-UH5P | TC-5426 | 2021-01-04 | Compliance |
| SIG-22-HKE-ONVA | TC-5434 | 2022-06-18 | IT Infrastructure |
| SIG-64-ILX-G2AZ PLC | TC-5443 | 2024-08-11 | Finance |
| SIG-24-PDE-AZV1 PLC | IC-5447 | 2021-12-21 | Operations |
| SIG-53-VTO-Y7V6 NV | IC-5456 | 2023-03-23 | Data Governance |
| SIG-86-JSN-H9KJ SA | BC-5467 | 2023-09-21 | Data Governance |
| SIG-32-DTD-L7TD International | TC-5476 | 2024-06-13 | Compliance |
| SIG-60-RUC-CU6A | BC-5481 | 2021-04-20 | Supply Chain |
| SIG-92-FQW-WCF5 SARL | TC-5492 | 2024-09-22 | Supply Chain |
| SIG-99-CEZ-35MR | TC-5494 | 2024-07-17 | Operations |
| SIG-66-IYP-1A2W | BC-5500 | 2021-08-06 | Operations |
| SIG-12-HNO-R9V0 AG | BC-5507 | 2021-06-21 | IT Infrastructure |
| SIG-95-QUH-2TS2 | TC-5516 | 2024-11-06 | Data Governance |
| SIG-27-IRG-QSO9 International | IC-5532 | 2023-05-05 | Data Governance |
| SIG-88-DDB-92XS Holdings | TC-5534 | 2023-02-27 | Compliance |
| SIG-76-RWX-Q314 International | TC-5541 | 2023-10-20 | Product Management |
| SIG-94-AWA-77SY Holdings | TC-5549 | 2024-01-17 | Product Management |
| SIG-59-FNZ-ZVBE Ltd. | IC-5555 | 2024-07-18 | Data Governance |
| SIG-27-KMU-WPWH GmbH | BC-5563 | 2023-10-09 | Compliance |
| SIG-56-FFG-XS2P | BC-5569 | 2024-02-20 | IT Infrastructure |
| SIG-20-GZD-R03A SARL | IC-5575 | 2023-07-08 | Compliance |
| SIG-12-USU-9HWB GmbH | TC-5581 | 2021-12-18 | Data Governance |
| SIG-13-QNH-MZKO SAS | BC-5589 | 2023-01-03 | Compliance |
| SIG-83-OBQ-GEIL GmbH | TC-5600 | 2022-05-04 | Supply Chain |
| SIG-77-LKE-KW49 | IC-5607 | 2022-02-14 | Supply Chain |
| SIG-83-FWQ-4QAN Holdings | BC-5619 | 2022-09-24 | Compliance |
| SIG-28-MAP-2EOP Holdings | IC-5634 | 2024-06-14 | Compliance |
| SIG-58-NUP-5DTV Group | IC-5644 | 2021-08-18 | Operations |
| SIG-48-YBV-ZD0Y | IC-5651 | 2023-07-12 | Data Governance |
| SIG-72-FHF-DYSG | IC-5658 | 2023-08-28 | Data Governance |
| SIG-16-ZDY-GYTX Holdings | TC-5666 | 2023-04-26 | Operations |
| SIG-86-VFH-L4DY Holdings | BC-5673 | 2021-07-25 | Data Governance |
| SIG-98-CTS-XPY5 | TC-5682 | 2024-12-18 | Operations |
| SIG-58-GKH-LOY0 Group | BC-5691 | 2023-03-27 | Supply Chain |
| SIG-73-BSB-YCKN Group | IC-5696 | 2023-09-22 | Operations |
| SIG-97-BXB-U2Y7 Ltd. | BC-5703 | 2024-10-03 | Product Management |
| SIG-13-ZIB-S8MV International | IC-5709 | 2021-09-10 | Data Governance |
| SIG-14-FNK-JNLM NV | BC-5718 | 2024-12-28 | Product Management |
| SIG-68-BSB-VSIA | TC-5729 | 2021-07-18 | Supply Chain |
| SIG-20-MSW-TMXG | BC-5734 | 2024-01-14 | Data Governance |
| SIG-27-MIG-RYBN | TC-5748 | 2022-01-09 | Compliance |
| SIG-84-MUG-BUXR | IC-5755 | 2023-08-06 | Data Governance |
| SIG-79-UGU-7OFC | BC-5765 | 2021-11-11 | Product Management |
| SIG-35-HUP-NW3M | IC-5770 | 2022-12-17 | Finance |
| SIG-10-HXN-BKWJ | IC-5773 | 2024-07-02 | Product Management |
| SIG-13-ZRN-WZGO | TC-5783 | 2024-05-18 | Compliance |
| SIG-93-CZZ-ZGWF | TC-5786 | 2024-04-21 | IT Infrastructure |
| SIG-64-RFK-TW5N | BC-5794 | 2022-10-20 | Supply Chain |
| SIG-83-SGE-Q8I0 | BC-5804 | 2024-07-21 | Supply Chain |
| SIG-47-MLZ-TPP5 | TC-5807 | 2023-03-21 | Operations |
| SIG-77-GUM-TVUW | IC-5819 | 2022-06-22 | Operations |
| SIG-84-NJC-6XAS | BC-5829 | 2024-06-20 | Operations |
| SIG-89-GUQ-OU40 | BC-5834 | 2022-07-11 | Finance |
| SIG-60-OBI-GVJP | IC-5839 | 2023-03-16 | Supply Chain |
| SIG-40-XXD-GE9O | TC-5847 | 2024-04-03 | Supply Chain |
| SIG-59-ECO-OXB3 | TC-5851 | 2022-08-22 | Operations |
| SIG-85-TWH-HQKB | BC-5858 | 2024-06-24 | Operations |
| SIG-96-EVO-10JM | BC-5875 | 2021-11-21 | Finance |
| SIG-96-POT-WDYM | BC-5881 | 2021-09-03 | Product Management |
| SIG-98-HZM-47LK | IC-5883 | 2024-01-18 | IT Infrastructure |
| SIG-27-VCT-2O4S | IC-5885 | 2021-01-07 | Compliance |
| SIG-54-OTO-2MVK | IC-5892 | 2021-02-11 | Finance |
| SIG-42-QVG-422I | IC-5894 | 2024-01-17 | Data Governance |
| SIG-15-YBX-K4SY | TC-5901 | 2023-12-07 | Supply Chain |
| SIG-29-XAN-WDDA | TC-5907 | 2021-12-05 | Product Management |
| SIG-34-LLF-EQC4 | BC-5910 | 2023-10-19 | Finance |
| SIG-44-NAF-R7O0 | BC-5919 | 2023-05-07 | Compliance |
| SIG-39-KYF-P35A | BC-5925 | 2023-05-13 | Operations |
| SIG-90-XNG-UYZN | IC-5928 | 2021-04-01 | Supply Chain |
| SIG-20-FYS-JNIL | IC-5936 | 2024-07-05 | Compliance |
| SIG-57-CCU-W7CL | TC-5941 | 2023-05-07 | Data Governance |
| SIG-48-LUB-IGA7 | TC-5945 | 2023-12-10 | Finance |
| SIG-79-DHA-SUOB | BC-5954 | 2023-06-01 | Operations |
| SIG-33-IHK-2GVW | TC-5968 | 2022-02-01 | Supply Chain |
| SIG-39-BHZ-K8SS | BC-5975 | 2023-01-28 | Finance |
| SIG-48-BCW-76F8 | IC-5991 | 2021-02-17 | Supply Chain |
| SIG-69-UAZ-1ODW | BC-5997 | 2021-04-24 | Product Management |
| SIG-60-NXS-8BAO | BC-6010 | 2023-07-06 | Data Governance |
| SIG-98-YBY-PFKQ | BC-6015 | 2024-10-05 | IT Infrastructure |
| SIG-68-GHA-D32X | TC-6020 | 2021-04-16 | Finance |
| SIG-12-JHE-FNCL | IC-6027 | 2024-02-14 | Data Governance |
| SIG-39-ARU-8X3V | IC-6032 | 2023-10-13 | Product Management |
| SIG-75-KAH-G7BB | TC-6037 | 2023-08-20 | IT Infrastructure |
| SIG-98-DBG-MTO5 | BC-6047 | 2021-06-19 | Supply Chain |
| SIG-19-RDF-86GH | IC-6057 | 2021-03-24 | Operations |
| SIG-67-JNR-XNTM | IC-6062 | 2022-06-08 | Supply Chain |
| SIG-89-PFV-OOFP | IC-6073 | 2022-05-22 | Compliance |
| SIG-39-QPC-OLQF | IC-6082 | 2022-10-12 | Data Governance |
| SIG-38-TDY-99S2 | BC-6086 | 2022-10-08 | Data Governance |
| SIG-33-VWP-VX5U | BC-6095 | 2021-04-21 | Operations |
| SIG-97-KNV-Q7J8 | BC-6102 | 2021-07-23 | Finance |
| SIG-96-UYO-0BNC | TC-6110 | 2023-08-20 | Compliance |
| SIG-89-YWW-NUVL | IC-6123 | 2023-04-12 | Finance |
| SIG-46-MBC-QSXJ | TC-6131 | 2021-12-23 | Operations |
| SIG-97-JHL-5AAT | BC-6136 | 2024-03-20 | Finance |
| SIG-40-YZP-9CC3 | BC-6145 | 2023-12-17 | Supply Chain |
| SIG-12-DBI-8UY5 | BC-6153 | 2024-04-27 | Product Management |
| SIG-59-VHS-XGCF | TC-6163 | 2024-11-13 | Data Governance |
| SIG-74-ZGY-ZA9S | IC-6183 | 2022-08-05 | Data Governance |
| SIG-46-SZM-WPIS | TC-6191 | 2023-08-01 | Data Governance |
| SIG-42-HLS-D63Y | TC-6194 | 2023-03-19 | Operations |
| SIG-20-XOX-HJFN | TC-6203 | 2023-10-12 | Supply Chain |
| SIG-73-KSW-UVZU | TC-6207 | 2021-05-12 | Compliance |
| SIG-10-PGH-BTUF | IC-6214 | 2023-08-05 | Supply Chain |
| SIG-74-YOY-6KGI | TC-6220 | 2022-06-12 | Supply Chain |
| SIG-78-QOY-5RIX | IC-6228 | 2022-04-11 | Operations |
| SIG-52-QAA-30TZ | IC-6233 | 2022-11-08 | Data Governance |
| SIG-55-IGH-IT3A | TC-6240 | 2024-08-07 | Finance |
| SIG-52-LXJ-ZU4J | BC-6241 | 2024-10-06 | Compliance |
| SIG-83-CDB-3QOI | TC-6246 | 2023-05-14 | Product Management |
| SIG-52-HZA-742D | TC-6248 | 2023-12-26 | Compliance |
| SIG-22-HSE-KSCU | BC-6259 | 2023-03-14 | Supply Chain |
| SIG-43-FST-BKJ7 | TC-6265 | 2021-09-03 | Data Governance |
| SIG-55-DBH-2QS3 | IC-6272 | 2023-09-11 | Compliance |
| SIG-36-RVG-E4FG | IC-6277 | 2023-01-13 | Operations |
| SIG-56-XKR-5XPI | TC-6283 | 2021-12-28 | IT Infrastructure |
| SIG-75-QRF-XA0H | BC-6295 | 2024-04-25 | Compliance |
| SIG-57-GUP-S7UK | TC-6301 | 2022-08-13 | Supply Chain |
| SIG-66-DRZ-QEHY | BC-6309 | 2023-10-05 | Data Governance |
| SIG-72-YVG-ZCUK | IC-6318 | 2024-06-07 | IT Infrastructure |
| SIG-37-ULH-Q8G9 | IC-6327 | 2023-11-11 | Finance |
| SIG-70-DIO-0E7N | BC-6339 | 2021-12-08 | Operations |
| SIG-54-BLS-33OX | IC-6354 | 2021-10-20 | Supply Chain |
| SIG-13-PHC-GSY7 | IC-6360 | 2021-01-23 | Operations |
| SIG-23-PGX-VBNK | TC-6369 | 2024-02-07 | IT Infrastructure |
| SIG-81-AMW-NE5V | IC-6378 | 2022-07-27 | Compliance |
| SIG-16-VOB-VAOG | TC-6383 | 2021-06-01 | Product Management |
| SIG-39-UNC-LQ6C | BC-6395 | 2024-09-23 | Operations |
| SIG-50-BLC-3NYL | IC-6397 | 2022-04-19 | Operations |
| SIG-21-DOL-82H3 | IC-6402 | 2023-10-21 | Operations |
| SIG-62-AQF-O1V3 | IC-6408 | 2023-02-05 | Compliance |
| SIG-97-BAE-XNL8 | TC-6415 | 2022-09-10 | Supply Chain |
| SIG-43-TPO-RSBY | BC-6419 | 2024-02-01 | Supply Chain |
| SIG-56-YYA-I8SV | BC-6424 | 2022-06-25 | Data Governance |
| SIG-90-YRJ-4LRE | BC-6425 | 2024-04-04 | Operations |
| SIG-28-SOZ-K6XK | TC-6430 | 2024-06-13 | Data Governance |
| SIG-43-TBS-C6P3 | TC-6440 | 2023-09-18 | Finance |
| SIG-83-ILY-GUL2 | BC-6444 | 2023-08-20 | Product Management |
| SIG-86-EKJ-RFVB | TC-6450 | 2021-10-26 | Operations |
| SIG-94-DAC-86F9 | TC-6455 | 2024-03-25 | Supply Chain |
| SIG-40-DFI-FC5R | TC-6461 | 2024-11-24 | Operations |
| SIG-22-SOG-POO8 | IC-6467 | 2023-02-26 | IT Infrastructure |
| SIG-15-GJL-MVIC | IC-6488 | 2022-09-07 | Finance |
| SIG-75-GGJ-DK9O | BC-6490 | 2022-01-02 | Data Governance |
| SIG-98-LSP-BA0T | IC-6496 | 2021-10-17 | Finance |
| SIG-27-BVB-SWG6 | BC-6500 | 2023-03-11 | Compliance |
| SIG-83-GEN-QNXZ | BC-6503 | 2024-12-11 | Operations |
| SIG-70-KJX-6V9L | TC-6509 | 2023-05-08 | Operations |
| SIG-30-YVL-ML15 | BC-6512 | 2022-12-26 | Data Governance |
| SIG-38-BKW-2ZX1 | IC-6515 | 2024-01-10 | IT Infrastructure |
| SIG-86-PYU-PCGN | IC-6524 | 2023-04-08 | Compliance |
| SIG-93-AHJ-EAD0 | TC-6527 | 2024-10-14 | Data Governance |
| SIG-63-MSP-S6JE | BC-6533 | 2024-10-21 | IT Infrastructure |
| SIG-19-GAY-Z6O1 | BC-6537 | 2024-09-12 | Supply Chain |
| SIG-10-WVJ-8X4Y | TC-6543 | 2023-02-10 | Data Governance |
| SIG-78-RHA-RJD1 | TC-6548 | 2021-12-21 | Product Management |
| SIG-58-MPE-EIKZ | TC-6554 | 2024-08-23 | Finance |
| SIG-97-UWA-JWLN | TC-6564 | 2023-06-14 | Finance |
| SIG-71-AYH-7PWP | IC-6575 | 2024-06-20 | Compliance |
| SIG-35-IQA-J92D | TC-6577 | 2024-09-25 | Product Management |
| SIG-38-FPC-A25N | BC-6582 | 2023-03-03 | Data Governance |
| SIG-65-TTX-PCJA | BC-6592 | 2022-03-25 | Finance |
| SIG-66-UEK-CKJ1 | BC-6600 | 2023-11-28 | Data Governance |
| SIG-14-XJN-JI7U | IC-6611 | 2022-02-22 | Finance |
| SIG-28-SXX-AKUN | TC-6617 | 2024-04-24 | Operations |
| SIG-74-WMW-Q37H | IC-6623 | 2023-10-06 | IT Infrastructure |
| SIG-59-TEL-K01C | BC-6628 | 2022-03-27 | IT Infrastructure |
| SIG-26-NTJ-I6T6 | TC-6636 | 2024-07-11 | Supply Chain |
| SIG-94-WFR-FI07 | IC-6641 | 2022-03-02 | Product Management |
| SIG-21-KXC-KAGD | IC-6648 | 2023-12-04 | Data Governance |
| SIG-62-DCP-L2AF | BC-6659 | 2023-01-02 | Compliance |
| SIG-21-DAC-5SA1 | IC-6663 | 2021-12-03 | IT Infrastructure |
| SIG-66-HXC-DMKU | IC-6667 | 2022-06-08 | Product Management |
| SIG-32-ETO-4DT1 | IC-6673 | 2021-07-28 | Data Governance |
| SIG-90-AUH-5HQ5 | TC-6684 | 2024-08-02 | Finance |
| SIG-70-ROA-COR7 | BC-6690 | 2024-08-07 | Compliance |
| SIG-76-GFL-RYI0 | TC-6692 | 2024-05-02 | Finance |
| SIG-96-AIP-QDS0 | IC-6700 | 2023-10-13 | Operations |
| SIG-50-QXM-GFI4 | TC-6703 | 2022-09-22 | Operations |
| SIG-30-IBO-NKXL | BC-6706 | 2023-08-04 | IT Infrastructure |
| SIG-55-KQD-CQMQ | TC-6710 | 2024-01-23 | Compliance |
| SIG-46-DGC-R6Z2 | BC-6718 | 2021-12-01 | Data Governance |
| SIG-60-IXG-GXQ7 | TC-6726 | 2024-06-02 | Finance |
| SIG-60-OHC-5EQB | BC-6729 | 2024-03-25 | Finance |
| SIG-76-ESC-PNV7 | BC-6734 | 2024-05-07 | Product Management |
| SIG-61-ZIT-092H | IC-6743 | 2024-11-24 | IT Infrastructure |
| SIG-14-GCI-G4Q9 | BC-6749 | 2022-05-07 | Data Governance |
| SIG-17-ITM-ARYQ | IC-6757 | 2022-07-27 | Operations |
| SIG-20-RSZ-19RE | BC-6763 | 2021-01-06 | Operations |
| SIG-62-BUT-A292 | BC-6772 | 2024-12-01 | Product Management |
| SIG-26-LKL-4NI1 | TC-6790 | 2024-05-10 | Operations |
| SIG-98-OYH-5RPI | BC-6798 | 2022-11-23 | Finance |
| SIG-86-NGE-LKTW | TC-6812 | 2024-03-28 | Compliance |
| SIG-73-YMY-EMYO | BC-6817 | 2021-06-16 | Finance |
| SIG-68-BPW-3DSD | BC-6821 | 2021-03-06 | Operations |
| SIG-30-QPI-FZVD | IC-6829 | 2022-08-12 | IT Infrastructure |
| SIG-55-FLO-S4MU | TC-6836 | 2024-06-17 | Compliance |
| SIG-67-NQK-GXJE | TC-6843 | 2024-07-17 | Supply Chain |
| SIG-66-OHB-GQIX | IC-6852 | 2023-06-09 | Product Management |
| SIG-40-DVL-7PTV | IC-6862 | 2022-04-18 | Supply Chain |
| SIG-19-PNU-HKF3 | TC-6870 | 2024-05-20 | Data Governance |
| SIG-23-TWA-K947 | TC-6875 | 2022-01-14 | Compliance |
| SIG-53-USG-KW3Q | TC-6879 | 2024-10-04 | Compliance |
| SIG-33-IWB-UV4J | IC-6888 | 2024-10-23 | Finance |
| SIG-47-TWQ-0FLA | TC-6894 | 2021-03-06 | Compliance |
| SIG-72-KAT-NI1G | IC-6904 | 2024-09-08 | Supply Chain |
| SIG-52-NEO-FFB3 | TC-6911 | 2023-12-20 | Operations |
| SIG-68-LYO-7YQ5 | IC-6918 | 2021-11-01 | Finance |
| SIG-47-TCL-S6FG | TC-6919 | 2021-04-07 | Operations |
| SIG-90-ALF-TQ8F | TC-6923 | 2023-10-07 | Product Management |
| SIG-51-MQP-ZO0K | IC-6927 | 2021-07-12 | Compliance |
| SIG-11-EIQ-WD14 | BC-6935 | 2022-05-10 | Operations |
| SIG-90-NFZ-XRLG | BC-6939 | 2024-01-26 | Data Governance |
| SIG-40-WLB-9IFD | BC-6951 | 2021-01-20 | Operations |
| SIG-52-QOU-LC66 | BC-6955 | 2021-06-17 | IT Infrastructure |
| SIG-39-EWA-Q37M | BC-6975 | 2021-01-10 | Supply Chain |
| SIG-99-AZM-B4OF | IC-6985 | 2024-12-09 | Product Management |
| SIG-50-PNF-Z2E8 | BC-6990 | 2022-10-21 | IT Infrastructure |
| SIG-71-FHA-CSOA | IC-7001 | 2022-12-24 | Data Governance |
| SIG-60-VTH-H7AM | IC-7009 | 2024-01-13 | Operations |
| SIG-42-BSJ-L2CG | BC-7013 | 2022-01-21 | Finance |
| SIG-79-UJC-1RKG | IC-7021 | 2024-05-23 | Data Governance |
| SIG-80-OEM-5LVP | BC-7025 | 2022-02-26 | Operations |
| SIG-27-FHB-EY0E | TC-7030 | 2021-09-06 | Data Governance |
| SIG-23-CJO-TSA9 | IC-7035 | 2021-11-02 | Compliance |
| SIG-92-ZAC-Y2PV | IC-7041 | 2021-07-01 | Product Management |
| SIG-91-MIT-AG2L | TC-7051 | 2023-09-14 | Compliance |
| SIG-46-AAW-27BR | TC-7056 | 2021-10-02 | Product Management |
| SIG-58-BDQ-I1V3 | BC-7062 | 2024-06-02 | Data Governance |
| SIG-58-MKV-8WKD | BC-7076 | 2024-08-12 | IT Infrastructure |
| SIG-39-CJT-QHM3 | BC-7084 | 2022-02-13 | Finance |
| SIG-63-NTB-209C | BC-7100 | 2023-11-16 | Finance |
| SIG-45-JPK-6R81 | TC-7105 | 2023-10-18 | Product Management |
| SIG-94-XEY-KPJ5 | TC-7109 | 2021-11-03 | Compliance |
| SIG-48-AKK-L4CQ | IC-7111 | 2023-02-23 | Product Management |
| SIG-42-FYL-6VKE | TC-7116 | 2023-02-20 | Finance |
| SIG-44-OML-OIX0 | IC-7126 | 2021-03-08 | Compliance |
| SIG-43-XDN-7VEU | TC-7134 | 2021-08-07 | Supply Chain |
| SIG-37-QAD-9FMK | IC-7143 | 2022-12-08 | Supply Chain |
| SIG-57-YNC-H4UX | TC-7151 | 2021-09-12 | Supply Chain |
| SIG-87-SQR-587P | IC-7152 | 2022-12-09 | Product Management |
| SIG-87-QEL-QGIW | IC-7158 | 2021-09-19 | Supply Chain |
| SIG-48-OWU-RTGZ | IC-7164 | 2021-06-18 | Operations |
| SIG-51-CZK-SBJH | TC-7175 | 2023-09-19 | Product Management |
| SIG-48-KTU-I0WF | TC-7180 | 2024-06-15 | Compliance |
| SIG-44-UKH-MO4F | BC-7190 | 2023-01-21 | Data Governance |
| SIG-94-NQF-0YQV | IC-7194 | 2023-07-15 | Product Management |
| SIG-67-RMU-WA6Y | BC-7197 | 2024-11-03 | Product Management |
| SIG-77-AEN-CA8D | TC-7207 | 2022-11-24 | IT Infrastructure |
| SIG-47-UEJ-M3SA | BC-7219 | 2021-09-06 | Operations |
| SIG-81-LGY-1IAH | BC-7225 | 2024-12-03 | Supply Chain |
| SIG-63-KZG-DVKO | TC-7229 | 2024-06-26 | Finance |
| SIG-70-HCT-Q44C | IC-7235 | 2023-11-04 | Operations |
| SIG-95-LOJ-S1L2 | IC-7242 | 2023-01-17 | Data Governance |
| SIG-41-EOV-7THY | BC-7244 | 2021-10-19 | Supply Chain |
| SIG-33-DJA-PDEO | TC-7249 | 2023-08-03 | Compliance |
| SIG-93-VLZ-VI4P | BC-7252 | 2021-11-03 | IT Infrastructure |
| SIG-33-OUH-D09D | BC-7259 | 2023-11-17 | Operations |
| SIG-54-MUH-KY6K | IC-7264 | 2022-08-12 | Product Management |
| SIG-27-GRI-K7JV | TC-7279 | 2024-11-24 | Supply Chain |
| SIG-97-QNX-7TWO | IC-7283 | 2024-09-08 | Operations |
| SIG-73-GRJ-1VRU | IC-7291 | 2023-03-27 | Operations |
| SIG-99-NVH-7WS3 | TC-7299 | 2024-06-07 | Product Management |
| SIG-30-PPI-DU4D | TC-7306 | 2021-08-25 | Data Governance |
| SIG-34-NMZ-KBWT | BC-7317 | 2024-09-10 | Compliance |
| SIG-98-NDY-OCEW | IC-7323 | 2021-09-01 | Finance |
| SIG-97-MKG-5MHN | IC-7331 | 2023-06-10 | Operations |
| SIG-67-GQM-MLNT | BC-7348 | 2022-05-23 | Compliance |
| SIG-78-MNL-57SN | TC-7353 | 2024-10-25 | Product Management |
| SIG-75-AOD-U2ER | BC-7360 | 2023-03-10 | Finance |
| SIG-99-BQS-KC4Q | IC-7363 | 2023-01-03 | Operations |
| SIG-55-EGS-MYD1 | IC-7369 | 2024-11-11 | Product Management |
| SIG-22-THR-75G4 | TC-7375 | 2023-10-02 | Data Governance |
| SIG-83-TFE-M3DZ | BC-7380 | 2022-12-05 | IT Infrastructure |
| SIG-76-SFN-GRTJ | TC-7388 | 2023-09-07 | IT Infrastructure |
| SIG-74-SAC-3HZG | TC-7395 | 2023-03-09 | Product Management |
| SIG-72-TXC-IWF9 | BC-7414 | 2022-11-12 | Operations |
| SIG-62-JTP-RUMX | BC-7418 | 2024-11-15 | IT Infrastructure |
| SIG-97-MAR-CXAJ | TC-7424 | 2022-08-28 | Operations |
| SIG-44-ZGN-CNIV | BC-7432 | 2021-04-11 | IT Infrastructure |
| SIG-98-AVJ-SOX9 | IC-7439 | 2023-06-08 | Supply Chain |
| SIG-87-KZL-I3ZY | BC-7442 | 2024-01-05 | Compliance |
| SIG-27-EAF-CA57 | IC-7450 | 2021-07-11 | Supply Chain |
| SIG-30-UPN-JYVW | BC-7455 | 2022-02-02 | IT Infrastructure |
| SIG-52-FQK-88IF | BC-7462 | 2023-03-28 | Data Governance |
| SIG-97-SMQ-9SG6 | TC-7469 | 2022-12-01 | Supply Chain |
| SIG-32-NVJ-H1RC | TC-7478 | 2022-09-13 | Supply Chain |
| SIG-13-DJH-ML2N | BC-7486 | 2023-10-24 | Compliance |
| SIG-51-RJJ-5BIE | IC-7491 | 2023-06-10 | Product Management |
| SIG-50-TGM-XVD2 | IC-7498 | 2024-04-18 | Compliance |
| SIG-75-CPF-OOJ3 | IC-7504 | 2023-11-19 | Operations |
| SIG-20-IMA-GJKF | IC-7509 | 2022-02-14 | IT Infrastructure |
| SIG-34-TKJ-QFOY | TC-7512 | 2022-12-07 | Product Management |
| SIG-10-NNQ-6CGO | BC-7515 | 2023-10-19 | Operations |
| SIG-49-FLB-3KJ2 | TC-7523 | 2021-07-20 | Data Governance |
| SIG-89-KYU-M9RA | IC-7529 | 2021-12-15 | Finance |
| SIG-90-NAM-FDV1 | BC-7534 | 2022-09-23 | Supply Chain |
| SIG-43-KPC-8R3Y | IC-7539 | 2021-08-16 | Compliance |
| SIG-43-KWZ-BU3P | IC-7545 | 2022-09-09 | Data Governance |
| SIG-55-OPY-GVTN | TC-7551 | 2023-10-19 | Operations |
| SIG-59-JAB-QS66 | IC-7560 | 2022-11-20 | Supply Chain |
| SIG-74-EPP-R9AG | TC-7566 | 2021-12-22 | Supply Chain |
| SIG-44-NHM-IY9D | BC-7572 | 2022-08-10 | IT Infrastructure |
| SIG-28-HHW-S34S | TC-7585 | 2024-12-26 | Data Governance |
| SIG-31-BWX-FDET | BC-7594 | 2022-12-25 | Finance |
| SIG-72-CRV-0OZ3 | BC-7600 | 2023-05-23 | Product Management |
| SIG-52-LHT-XBI2 | IC-7608 | 2021-01-16 | Compliance |
| SIG-42-QOC-A3JP | BC-7617 | 2024-02-23 | IT Infrastructure |
| SIG-73-SXI-8HSL | IC-7624 | 2021-09-18 | Product Management |
| SIG-22-ADK-3T78 | IC-7627 | 2023-04-11 | Product Management |
| SIG-30-MCM-OXZ5 | TC-7633 | 2023-06-01 | IT Infrastructure |
| SIG-88-YRN-7S19 | TC-7643 | 2024-04-04 | Product Management |
| SIG-51-MVX-XKUB | BC-7645 | 2023-09-08 | IT Infrastructure |
| SIG-19-JRR-02SD | TC-7650 | 2022-01-12 | Operations |
| SIG-20-CDH-FE8F | TC-7658 | 2021-02-08 | Finance |
| SIG-83-SCO-PIKN | BC-7666 | 2022-08-08 | Finance |
| SIG-92-NWY-1FV5 | TC-7670 | 2024-05-21 | Compliance |
| SIG-72-IQP-IKAX | TC-7672 | 2022-07-12 | Supply Chain |
| SIG-11-HHQ-JHKO | IC-7676 | 2023-04-02 | Supply Chain |
| SIG-49-VSP-V4PV | IC-7682 | 2023-10-23 | Compliance |
| SIG-31-LNL-F2NC | IC-7691 | 2021-09-25 | Operations |
| SIG-30-PKD-LW8B | TC-7700 | 2024-08-16 | IT Infrastructure |
| SIG-98-QRC-XOOW | BC-7708 | 2021-05-15 | Supply Chain |
| SIG-38-LEZ-M2KS | IC-7713 | 2022-06-06 | IT Infrastructure |
| SIG-92-SMV-JF74 | BC-7717 | 2023-01-27 | Finance |
| SIG-20-GIF-RAEQ | IC-7727 | 2022-12-22 | Compliance |
| SIG-53-IAB-UGH9 | TC-7729 | 2022-05-18 | Compliance |
| SIG-30-PQC-HUIU | BC-7735 | 2022-01-13 | Data Governance |
| SIG-51-DNC-4AET | TC-7752 | 2021-01-26 | IT Infrastructure |
| SIG-47-MRM-FIIH | BC-7761 | 2021-11-26 | Compliance |
| SIG-38-ZZL-D5F0 | TC-7768 | 2021-01-03 | Finance |
| SIG-23-FHN-ZAFZ | BC-7790 | 2021-03-17 | Product Management |
| SIG-15-HZV-LHQ2 | BC-7796 | 2021-12-13 | Supply Chain |
| SIG-90-RCW-71K4 | BC-7806 | 2024-12-03 | Compliance |
| SIG-28-MGE-0MBB | TC-7810 | 2023-09-14 | Operations |
| SIG-98-LPL-XFDL | TC-7814 | 2022-08-28 | Operations |
| SIG-47-TWK-RYLY | IC-7820 | 2024-10-14 | Operations |
| SIG-48-BCI-7SYR | IC-7828 | 2021-07-26 | Operations |
| SIG-47-UOO-GQED | TC-7834 | 2021-07-26 | Compliance |
| SIG-25-WCC-PPMH | IC-7840 | 2022-01-04 | Data Governance |
| SIG-76-XDH-Q3Q4 | TC-7848 | 2023-03-06 | Compliance |
| SIG-45-NEB-M5RE | IC-7858 | 2022-01-06 | Product Management |
| SIG-55-NJY-I13Y | IC-7861 | 2021-12-08 | Compliance |
| SIG-41-SEX-2DFF | TC-7871 | 2022-08-04 | Supply Chain |
| SIG-58-EJN-NRGO | IC-7875 | 2021-11-04 | Finance |
| SIG-89-HHQ-75TJ | TC-7880 | 2023-06-06 | Finance |
| SIG-24-KLH-SHKW | TC-7885 | 2024-08-26 | Finance |
| SIG-26-WVS-AQ3B | BC-7901 | 2021-07-05 | Supply Chain |
| SIG-15-IUN-M051 | BC-7915 | 2023-12-23 | Supply Chain |
| SIG-59-OPA-P4E0 | BC-7925 | 2022-01-10 | IT Infrastructure |
| SIG-75-NYN-Q2N4 | IC-7931 | 2023-09-08 | Compliance |
| SIG-42-EYO-WK0H | TC-7938 | 2021-06-11 | IT Infrastructure |
| SIG-38-OTV-E78M | TC-7945 | 2023-11-08 | Supply Chain |
| SIG-49-YEY-OY3L | BC-7952 | 2021-11-25 | Finance |
| SIG-58-SWU-PQGW | IC-7958 | 2022-08-13 | IT Infrastructure |
| SIG-46-BCJ-SSEN | BC-7968 | 2021-02-03 | Compliance |
| SIG-79-PSV-943Y | IC-7977 | 2023-07-13 | Operations |
| SIG-97-FYC-MHAR | TC-7982 | 2022-11-22 | Compliance |
| SIG-45-QQC-Z4N0 | BC-7988 | 2022-08-20 | Supply Chain |
| SIG-53-NKW-4MNF | IC-8009 | 2021-12-11 | Data Governance |
| SIG-65-SCG-WZ5H | BC-8018 | 2021-07-06 | Compliance |
| SIG-56-BHM-X0GI | BC-8022 | 2024-03-19 | Product Management |
| SIG-92-KVS-DDEE | IC-8026 | 2023-11-03 | Supply Chain |
| SIG-65-QKW-Y1YW | IC-8031 | 2021-09-23 | Data Governance |
| SIG-95-UXH-C9M4 | BC-8041 | 2024-06-20 | Product Management |
| SIG-74-VWV-7YSU | BC-8054 | 2024-04-03 | IT Infrastructure |
| SIG-31-FGA-64VZ | TC-8060 | 2022-04-07 | Supply Chain |
| SIG-53-ZZI-QU56 | TC-8069 | 2022-06-14 | Data Governance |
| SIG-13-XOQ-WLDV | TC-8075 | 2024-06-26 | Operations |
| SIG-67-YOR-JCUH | TC-8080 | 2021-09-17 | Compliance |
| SIG-76-RUI-UC1S | BC-8086 | 2021-08-02 | Compliance |
| SIG-56-MIF-2O9D | TC-8089 | 2024-12-09 | Supply Chain |
| SIG-92-RHW-233J | IC-8097 | 2023-07-28 | Operations |
| SIG-30-TUW-0P7F | TC-8114 | 2023-12-24 | Product Management |
| SIG-80-ZKZ-ANXJ | TC-8119 | 2022-09-18 | Product Management |
| SIG-81-SZZ-3RNH | BC-8126 | 2024-01-17 | Finance |
| SIG-31-GVB-1WH0 | BC-8145 | 2022-11-13 | Supply Chain |
| SIG-42-UMA-WZ7F | TC-8148 | 2022-12-02 | Product Management |
| SIG-69-MNI-DH5B | IC-8151 | 2024-05-27 | Data Governance |
| SIG-35-RSV-01YT | BC-8158 | 2023-12-10 | Product Management |
| SIG-46-DQX-JN7N | TC-8165 | 2022-06-18 | Product Management |
| SIG-21-VZE-Q2WM | IC-8170 | 2022-05-25 | Data Governance |
| SIG-20-IKV-891D | TC-8179 | 2023-03-17 | IT Infrastructure |
| SIG-51-HUK-F1HG | BC-8185 | 2022-04-02 | Compliance |
| SIG-65-QDW-KJG8 | IC-8192 | 2023-02-10 | IT Infrastructure |
| SIG-92-PYF-X5ZO | TC-8201 | 2023-10-22 | Data Governance |
| SIG-94-MKW-LH8F | IC-8211 | 2022-01-15 | Finance |
| SIG-69-TRZ-SFLQ | BC-8214 | 2021-09-18 | Product Management |
| SIG-49-DCM-ASFC | BC-8218 | 2023-04-27 | Data Governance |
| SIG-43-SSK-5L22 | IC-8224 | 2024-03-17 | Supply Chain |
| SIG-73-RIN-8RXQ | BC-8233 | 2023-06-19 | IT Infrastructure |
| SIG-94-AFM-7IJJ | TC-8241 | 2021-07-18 | IT Infrastructure |
| SIG-73-DNT-OVXU | IC-8242 | 2023-06-02 | Data Governance |
| SIG-48-WVJ-F5TN | IC-8249 | 2024-06-02 | Supply Chain |
| SIG-40-IFK-RPIG | TC-8256 | 2021-11-06 | Compliance |
| SIG-56-MNF-4JPL | BC-8265 | 2023-10-25 | Supply Chain |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| SIG-30-PVA-ZMF8 | IC-6604 | PROVISIONAL | Historical - verify before use |
| SIG-44-SRN-1MKF | IC-5610 | SUPERSEDED | Historical - verify before use |
| SIG-41-SWO-23GD | IC-7221 | DEPRECATED | Historical - verify before use |
| SIG-79-HZP-CLBR | IC-6105 | SUPERSEDED | Historical - verify before use |
| SIG-29-CYR-T4UF | IC-7563 | DEPRECATED | Historical - verify before use |
| SIG-16-QDM-JLQM | IC-6019 | PROVISIONAL | Historical - verify before use |
| SIG-41-LTG-3D5I | IC-7084 | PROVISIONAL | Historical - verify before use |
| SIG-56-ZVH-GATJ | IC-7662 | REVIEW REQUIRED | Historical - verify before use |
| SIG-48-UJX-49KW | IC-6463 | DEPRECATED | Historical - verify before use |
| SIG-44-MHK-SRCB | IC-8546 | REVIEW REQUIRED | Historical - verify before use |
| SIG-74-HUK-JA04 | IC-9665 | DEPRECATED | Historical - verify before use |
| SIG-95-GQL-A26Y | IC-6260 | REVIEW REQUIRED | Historical - verify before use |
| SIG-71-VGV-8K52 | IC-8920 | SUPERSEDED | Historical - verify before use |
| SIG-86-VGU-A4FE | IC-5845 | SUPERSEDED | Historical - verify before use |
| SIG-61-XKV-ODPX | IC-8404 | REVIEW REQUIRED | Historical - verify before use |
| SIG-53-AHT-MGFX | IC-5010 | REVIEW REQUIRED | Historical - verify before use |
| SIG-26-DML-NZS4 | IC-6218 | PROVISIONAL | Historical - verify before use |
| SIG-51-LVQ-VS8Q | IC-8416 | SUPERSEDED | Historical - verify before use |
| SIG-37-NAI-M1G9 | IC-8444 | SUPERSEDED | Historical - verify before use |
| SIG-57-NGZ-ILDZ | IC-6716 | REVIEW REQUIRED | Historical - verify before use |
| SIG-50-FUX-7S9T | IC-7434 | DEPRECATED | Historical - verify before use |
| SIG-13-JUR-FV2B | IC-9093 | SUPERSEDED | Historical - verify before use |
| SIG-92-VAB-1JHU | IC-5144 | REVIEW REQUIRED | Historical - verify before use |
| SIG-52-NBD-2SF6 | IC-9563 | DEPRECATED | Historical - verify before use |
| SIG-45-IJY-KUT6 | IC-7136 | PROVISIONAL | Historical - verify before use |
| SIG-60-WEX-2G05 | IC-8994 | PROVISIONAL | Historical - verify before use |
| SIG-68-CNV-EOUU | IC-6648 | DEPRECATED | Historical - verify before use |
| SIG-24-LEE-BXW7 | IC-5045 | REVIEW REQUIRED | Historical - verify before use |
| SIG-32-BYW-WPR9 | IC-6243 | REVIEW REQUIRED | Historical - verify before use |
| SIG-12-ANK-TJ9A | IC-7476 | DEPRECATED | Historical - verify before use |
| SIG-10-TIC-7Q1D | IC-9375 | DEPRECATED | Historical - verify before use |
| SIG-76-CCF-UYHN | IC-8414 | PROVISIONAL | Historical - verify before use |
| SIG-66-LJV-5E3H | IC-5479 | REVIEW REQUIRED | Historical - verify before use |
| SIG-37-PEJ-WFOY | IC-5872 | DEPRECATED | Historical - verify before use |
| SIG-50-NZZ-E4UN | IC-6125 | SUPERSEDED | Historical - verify before use |
| SIG-79-ZUT-1IAO | IC-9917 | SUPERSEDED | Historical - verify before use |
| SIG-73-YLS-BYGH | IC-9423 | PROVISIONAL | Historical - verify before use |
| SIG-19-HIY-M5FC | IC-7889 | SUPERSEDED | Historical - verify before use |
| SIG-22-VQM-AGKC | IC-6041 | REVIEW REQUIRED | Historical - verify before use |
| SIG-22-DOP-7UDK | IC-5228 | PROVISIONAL | Historical - verify before use |
| SIG-57-QDA-RQ8R | IC-7255 | PROVISIONAL | Historical - verify before use |
| SIG-44-HRR-WZP6 | IC-7880 | REVIEW REQUIRED | Historical - verify before use |
| SIG-16-LZG-DGBK | IC-8555 | DEPRECATED | Historical - verify before use |
| SIG-13-EJJ-5506 | IC-8923 | REVIEW REQUIRED | Historical - verify before use |
| SIG-83-KGL-Q4QE | IC-5167 | PROVISIONAL | Historical - verify before use |
| SIG-35-SYQ-HZY7 | IC-6438 | PROVISIONAL | Historical - verify before use |
| SIG-58-EEN-BKJF | IC-8087 | DEPRECATED | Historical - verify before use |
| SIG-19-TPS-MSKY | IC-6680 | PROVISIONAL | Historical - verify before use |
| SIG-80-EUW-QTKC | IC-5605 | SUPERSEDED | Historical - verify before use |
| SIG-85-SIL-CNEA | IC-6847 | DEPRECATED | Historical - verify before use |
| SIG-60-GHI-04X0 | IC-8491 | PROVISIONAL | Historical - verify before use |
| SIG-94-QLF-7SH2 | IC-7196 | SUPERSEDED | Historical - verify before use |
| SIG-39-GGG-HIWF | IC-7062 | PROVISIONAL | Historical - verify before use |
| SIG-98-OOK-FHJ4 | IC-5616 | PROVISIONAL | Historical - verify before use |
| SIG-66-ZOH-E8TV | IC-6654 | REVIEW REQUIRED | Historical - verify before use |
| SIG-76-QBY-ERKM | IC-8023 | SUPERSEDED | Historical - verify before use |
| SIG-42-AJS-6RPK | IC-6638 | REVIEW REQUIRED | Historical - verify before use |
| SIG-36-FSA-X73Q | IC-6594 | SUPERSEDED | Historical - verify before use |
| SIG-83-PHT-N27M | IC-5775 | PROVISIONAL | Historical - verify before use |
| SIG-60-TMF-XHW0 | IC-7773 | PROVISIONAL | Historical - verify before use |
| SIG-30-EKM-GB1A | IC-9131 | REVIEW REQUIRED | Historical - verify before use |
| SIG-66-FRL-CVIT | IC-9647 | DEPRECATED | Historical - verify before use |
| SIG-63-TFP-OMUW | IC-8277 | SUPERSEDED | Historical - verify before use |
| SIG-51-YTN-F537 | IC-8788 | DEPRECATED | Historical - verify before use |
| SIG-46-SVJ-5IZO | IC-7678 | REVIEW REQUIRED | Historical - verify before use |
| SIG-91-GMY-Q91Y | IC-7278 | SUPERSEDED | Historical - verify before use |
| SIG-18-KSV-TA83 | IC-9123 | REVIEW REQUIRED | Historical - verify before use |
| SIG-37-ZOD-1VME | IC-6393 | SUPERSEDED | Historical - verify before use |
| SIG-72-YEU-SCIQ | IC-7388 | REVIEW REQUIRED | Historical - verify before use |
| SIG-37-CWM-V4K0 | IC-5568 | DEPRECATED | Historical - verify before use |
| SIG-17-UCW-S6NB | IC-6213 | DEPRECATED | Historical - verify before use |
| SIG-47-SRN-QNYY | IC-6481 | SUPERSEDED | Historical - verify before use |
| SIG-27-RTX-YEAW | IC-5275 | PROVISIONAL | Historical - verify before use |
| SIG-19-BHQ-S1GD | IC-7873 | DEPRECATED | Historical - verify before use |
| SIG-45-ADT-8MFS | IC-8921 | PROVISIONAL | Historical - verify before use |
| SIG-56-BPD-M0A6 | IC-5603 | DEPRECATED | Historical - verify before use |
| SIG-40-KVV-E07S | IC-7409 | PROVISIONAL | Historical - verify before use |
| SIG-42-AYY-K71K | IC-9515 | DEPRECATED | Historical - verify before use |
| SIG-37-JLF-9KYP | IC-5462 | PROVISIONAL | Historical - verify before use |
| SIG-31-CWE-03UX | IC-9984 | PROVISIONAL | Historical - verify before use |
| SIG-36-ZWC-F2K1 | IC-5077 | PROVISIONAL | Historical - verify before use |
| SIG-13-CAZ-HXXP | IC-8659 | DEPRECATED | Historical - verify before use |
| SIG-65-BAQ-940V | IC-6840 | SUPERSEDED | Historical - verify before use |
| SIG-68-SYL-8192 | IC-5971 | SUPERSEDED | Historical - verify before use |
| SIG-76-YLU-7DL9 | IC-7431 | DEPRECATED | Historical - verify before use |
| SIG-49-UKY-6H3R | IC-9374 | DEPRECATED | Historical - verify before use |
| SIG-16-FQO-8S1S | IC-9650 | SUPERSEDED | Historical - verify before use |
| SIG-82-TQD-ODWH | IC-8282 | DEPRECATED | Historical - verify before use |
| SIG-97-PYI-8W9Z | IC-9032 | SUPERSEDED | Historical - verify before use |
| SIG-78-WDE-NNV9 | IC-6731 | SUPERSEDED | Historical - verify before use |
| SIG-70-YBK-DUQ6 | IC-9543 | DEPRECATED | Historical - verify before use |
| SIG-45-PNR-H9Q3 | IC-8648 | PROVISIONAL | Historical - verify before use |
| SIG-25-VPE-TOC1 | IC-5089 | DEPRECATED | Historical - verify before use |
| SIG-29-BJH-NXI0 | IC-5687 | PROVISIONAL | Historical - verify before use |
| SIG-96-DUH-99Q6 | IC-6157 | PROVISIONAL | Historical - verify before use |
| SIG-60-IRZ-OTKZ | IC-9729 | DEPRECATED | Historical - verify before use |
| SIG-48-GDK-Y8XN | IC-6861 | SUPERSEDED | Historical - verify before use |
| SIG-98-CGL-FHWJ | IC-7463 | REVIEW REQUIRED | Historical - verify before use |
| SIG-53-MEZ-6IT1 | IC-7035 | PROVISIONAL | Historical - verify before use |
| SIG-41-HMT-W0GK | IC-5195 | SUPERSEDED | Historical - verify before use |
| SIG-42-BEO-614U | IC-8299 | SUPERSEDED | Historical - verify before use |
| SIG-59-LNO-OJGF | IC-6215 | REVIEW REQUIRED | Historical - verify before use |
| SIG-20-OVW-HRUP | IC-8422 | DEPRECATED | Historical - verify before use |
| SIG-94-JCX-NJ62 | IC-9530 | DEPRECATED | Historical - verify before use |
| SIG-11-SLQ-KF5B | IC-7451 | PROVISIONAL | Historical - verify before use |
| SIG-71-COB-BL7A | IC-9396 | PROVISIONAL | Historical - verify before use |
| SIG-82-ZPY-WR2F | IC-5148 | REVIEW REQUIRED | Historical - verify before use |
| SIG-73-AXY-5E8O | IC-7732 | DEPRECATED | Historical - verify before use |
| SIG-30-LJO-TN4Y | IC-5580 | PROVISIONAL | Historical - verify before use |
| SIG-76-AAU-3VM8 | IC-6988 | SUPERSEDED | Historical - verify before use |
| SIG-58-HNG-1XJ7 | IC-5177 | SUPERSEDED | Historical - verify before use |
| SIG-30-MPO-SJEV | IC-5014 | DEPRECATED | Historical - verify before use |
| SIG-55-CTS-U5X0 | IC-9375 | PROVISIONAL | Historical - verify before use |
| SIG-83-HEH-XF50 | IC-6845 | PROVISIONAL | Historical - verify before use |
| SIG-66-AQR-B68Q | IC-9837 | PROVISIONAL | Historical - verify before use |
| SIG-54-CMF-PK48 | IC-9898 | DEPRECATED | Historical - verify before use |
| SIG-70-IKQ-7KBN | IC-9218 | SUPERSEDED | Historical - verify before use |
| SIG-27-UKP-V2ME | IC-8630 | REVIEW REQUIRED | Historical - verify before use |
| SIG-85-STS-67D6 | IC-5646 | REVIEW REQUIRED | Historical - verify before use |
| SIG-72-JEH-P5K7 | IC-6502 | PROVISIONAL | Historical - verify before use |
| SIG-36-ABO-ZBYW | IC-5238 | DEPRECATED | Historical - verify before use |
| SIG-22-TOX-02GV | IC-8472 | DEPRECATED | Historical - verify before use |
| SIG-79-RTU-R8IQ | IC-9063 | SUPERSEDED | Historical - verify before use |
| SIG-10-KDB-LGYT | IC-8078 | SUPERSEDED | Historical - verify before use |
| SIG-88-AGF-FF5L | IC-9702 | PROVISIONAL | Historical - verify before use |
| SIG-25-WDK-CWCD | IC-9309 | DEPRECATED | Historical - verify before use |
| SIG-78-AVK-U9PX | IC-7310 | SUPERSEDED | Historical - verify before use |
| SIG-61-KUY-VFFK | IC-8755 | SUPERSEDED | Historical - verify before use |
| SIG-51-IYK-630P | IC-7494 | SUPERSEDED | Historical - verify before use |
| SIG-79-IHV-JKPQ | IC-8239 | PROVISIONAL | Historical - verify before use |
| SIG-79-OZQ-4I2N | IC-9480 | DEPRECATED | Historical - verify before use |
| SIG-78-YEH-31XY | IC-6754 | SUPERSEDED | Historical - verify before use |
| SIG-84-BFP-RD5B | IC-7985 | PROVISIONAL | Historical - verify before use |
| SIG-19-QLH-ILRZ | IC-6163 | REVIEW REQUIRED | Historical - verify before use |
| SIG-52-EML-H8JV | IC-8650 | DEPRECATED | Historical - verify before use |
| SIG-12-OAV-ALF4 | IC-8700 | DEPRECATED | Historical - verify before use |
| SIG-58-NYA-2O4M | IC-8888 | PROVISIONAL | Historical - verify before use |
| SIG-21-EAX-PC8Q | IC-6957 | REVIEW REQUIRED | Historical - verify before use |
| SIG-39-QZD-93EZ | IC-5991 | REVIEW REQUIRED | Historical - verify before use |
| SIG-29-DTY-HFJL | IC-8672 | SUPERSEDED | Historical - verify before use |
| SIG-11-RGJ-D3IR | IC-8765 | SUPERSEDED | Historical - verify before use |
| SIG-32-TTU-44MW | IC-9143 | DEPRECATED | Historical - verify before use |
| SIG-21-KSF-Z6X4 | IC-7862 | REVIEW REQUIRED | Historical - verify before use |
| SIG-53-MPZ-77TN | IC-9969 | REVIEW REQUIRED | Historical - verify before use |
| SIG-47-HDT-7PPC | IC-8815 | DEPRECATED | Historical - verify before use |
| SIG-44-FWT-OA3N | IC-8370 | REVIEW REQUIRED | Historical - verify before use |
| SIG-35-TKX-8TRE | IC-8709 | PROVISIONAL | Historical - verify before use |
| SIG-68-PIZ-R6Q5 | IC-8578 | REVIEW REQUIRED | Historical - verify before use |
| SIG-16-CAW-LD7M | IC-9275 | SUPERSEDED | Historical - verify before use |
| SIG-43-NCZ-FT9Z | IC-8925 | REVIEW REQUIRED | Historical - verify before use |
| SIG-94-KAU-6F8H | IC-7671 | DEPRECATED | Historical - verify before use |
| SIG-98-NIJ-5N8C | IC-5119 | SUPERSEDED | Historical - verify before use |
| SIG-23-OPT-7QHV | IC-5124 | DEPRECATED | Historical - verify before use |
| SIG-15-QIT-5CZE | IC-9055 | REVIEW REQUIRED | Historical - verify before use |
| SIG-84-PAS-5S3O | IC-5002 | DEPRECATED | Historical - verify before use |
| SIG-45-ZTJ-PA16 | IC-6934 | DEPRECATED | Historical - verify before use |
| SIG-71-WDX-2GRR | IC-6079 | PROVISIONAL | Historical - verify before use |
| SIG-33-FUV-53NO | IC-9400 | SUPERSEDED | Historical - verify before use |
| SIG-44-UIE-SASC | IC-7285 | PROVISIONAL | Historical - verify before use |
| SIG-54-LIP-WKBS | IC-6969 | SUPERSEDED | Historical - verify before use |
| SIG-48-LHY-R0O8 | IC-5762 | REVIEW REQUIRED | Historical - verify before use |
| SIG-16-JKI-B4JG | IC-6298 | REVIEW REQUIRED | Historical - verify before use |
| SIG-88-XZP-H10B | IC-5186 | PROVISIONAL | Historical - verify before use |
| SIG-40-NOU-7O0G | IC-9466 | PROVISIONAL | Historical - verify before use |
| SIG-34-UJK-TJA6 | IC-7029 | SUPERSEDED | Historical - verify before use |
| SIG-12-BIH-AKGD | IC-8523 | SUPERSEDED | Historical - verify before use |
| SIG-56-CMM-ODF7 | IC-7937 | SUPERSEDED | Historical - verify before use |
| SIG-99-OQS-ADHF | IC-6939 | DEPRECATED | Historical - verify before use |
| SIG-30-RXC-HFDI | IC-8140 | DEPRECATED | Historical - verify before use |
| SIG-51-KQC-QY9M | IC-6092 | REVIEW REQUIRED | Historical - verify before use |
| SIG-41-OMW-SN1T | IC-5546 | SUPERSEDED | Historical - verify before use |
| SIG-85-FAV-D2EE | IC-9955 | DEPRECATED | Historical - verify before use |
| SIG-49-OHU-U248 | IC-9133 | SUPERSEDED | Historical - verify before use |
| SIG-75-GUI-J643 | IC-9101 | PROVISIONAL | Historical - verify before use |
| SIG-79-GLV-IEST | IC-5049 | DEPRECATED | Historical - verify before use |
| SIG-88-EEY-HOGD | IC-9990 | DEPRECATED | Historical - verify before use |
| SIG-36-BVE-5U7D | IC-7207 | SUPERSEDED | Historical - verify before use |
| SIG-47-YTF-UPMT | IC-6682 | REVIEW REQUIRED | Historical - verify before use |
| SIG-51-HLJ-TN1E | IC-8566 | DEPRECATED | Historical - verify before use |
| SIG-25-ABB-2SBA | IC-9463 | DEPRECATED | Historical - verify before use |
| SIG-24-MFK-ZAUG | IC-5029 | PROVISIONAL | Historical - verify before use |
| SIG-12-RDG-0JI1 | IC-6210 | PROVISIONAL | Historical - verify before use |
| SIG-60-QPM-2TRI | IC-9863 | DEPRECATED | Historical - verify before use |
| SIG-99-QXY-X4NT | IC-5276 | REVIEW REQUIRED | Historical - verify before use |
| SIG-79-SPO-WT80 | IC-9599 | DEPRECATED | Historical - verify before use |
| SIG-91-UWU-GPZB | IC-5317 | SUPERSEDED | Historical - verify before use |
| SIG-27-WVB-8FZQ | IC-7608 | PROVISIONAL | Historical - verify before use |
| SIG-43-GRJ-P3HT | IC-5292 | REVIEW REQUIRED | Historical - verify before use |
| SIG-36-XEW-9SSB | IC-9803 | REVIEW REQUIRED | Historical - verify before use |
| SIG-68-ELC-6AVE | IC-5939 | PROVISIONAL | Historical - verify before use |
| SIG-95-LLS-0RNG | IC-9211 | REVIEW REQUIRED | Historical - verify before use |
| SIG-16-FVU-3EBQ | IC-9302 | SUPERSEDED | Historical - verify before use |
| SIG-39-OZI-N968 | IC-8735 | DEPRECATED | Historical - verify before use |
| SIG-22-XCC-QSNV | IC-8424 | REVIEW REQUIRED | Historical - verify before use |
| SIG-85-WWC-01LO | IC-5481 | SUPERSEDED | Historical - verify before use |
| SIG-83-BZY-VHAE | IC-9529 | PROVISIONAL | Historical - verify before use |
| SIG-63-KXZ-46Q1 | IC-9961 | REVIEW REQUIRED | Historical - verify before use |
| SIG-83-PIY-NKQE | IC-8707 | SUPERSEDED | Historical - verify before use |
| SIG-90-SZM-PZJ4 | IC-7364 | DEPRECATED | Historical - verify before use |
| SIG-14-MOL-USHF | IC-6804 | SUPERSEDED | Historical - verify before use |
| SIG-84-VYG-QI55 | IC-9480 | SUPERSEDED | Historical - verify before use |
| SIG-39-FND-AALU | IC-5460 | DEPRECATED | Historical - verify before use |
| SIG-16-YRD-5C3Z | IC-5830 | PROVISIONAL | Historical - verify before use |
| SIG-84-EIB-2MOT | IC-9223 | REVIEW REQUIRED | Historical - verify before use |
| SIG-47-LBV-Y27V | IC-5289 | SUPERSEDED | Historical - verify before use |
| SIG-57-HAE-WNSM | IC-5696 | REVIEW REQUIRED | Historical - verify before use |
| SIG-78-NWO-RO6D | IC-7178 | REVIEW REQUIRED | Historical - verify before use |
| SIG-80-QNF-AHPO | IC-7423 | REVIEW REQUIRED | Historical - verify before use |
| SIG-66-RQA-05UV | IC-5642 | DEPRECATED | Historical - verify before use |
| SIG-47-HPA-L2FX | IC-8155 | PROVISIONAL | Historical - verify before use |
| SIG-57-YOY-F7N2 | IC-8548 | DEPRECATED | Historical - verify before use |
| SIG-44-QME-TTIM | IC-6614 | REVIEW REQUIRED | Historical - verify before use |
| SIG-56-LHF-WMFP | IC-7681 | SUPERSEDED | Historical - verify before use |
| SIG-34-GNA-EHC2 | IC-7697 | REVIEW REQUIRED | Historical - verify before use |
| SIG-73-UUF-1F99 | IC-7884 | PROVISIONAL | Historical - verify before use |
| SIG-64-QID-BCT3 | IC-9196 | REVIEW REQUIRED | Historical - verify before use |
| SIG-48-IWQ-OJ98 | IC-7623 | PROVISIONAL | Historical - verify before use |
| SIG-94-MGT-4WYA | IC-8971 | DEPRECATED | Historical - verify before use |
| SIG-40-OEJ-4XCR | IC-5180 | PROVISIONAL | Historical - verify before use |
| SIG-26-PJJ-DUD8 | IC-8359 | SUPERSEDED | Historical - verify before use |
| SIG-82-OMQ-EPBO | IC-6848 | REVIEW REQUIRED | Historical - verify before use |
| SIG-68-VDM-0UT1 | IC-5978 | DEPRECATED | Historical - verify before use |
| SIG-61-HXH-PFBC | IC-9882 | DEPRECATED | Historical - verify before use |
| SIG-13-WHV-DDIN | IC-6260 | DEPRECATED | Historical - verify before use |
| SIG-47-NVU-R3XU | IC-7461 | SUPERSEDED | Historical - verify before use |
| SIG-64-BPY-A8RD | IC-6159 | PROVISIONAL | Historical - verify before use |
| SIG-39-UPB-Q8DA | IC-6550 | PROVISIONAL | Historical - verify before use |
| SIG-60-ZEV-V2NY | IC-9456 | DEPRECATED | Historical - verify before use |
| SIG-37-MXA-3C7Q | IC-7770 | PROVISIONAL | Historical - verify before use |
| SIG-85-VFA-F0TJ | IC-5829 | DEPRECATED | Historical - verify before use |
| SIG-42-LOE-5XD8 | IC-7814 | SUPERSEDED | Historical - verify before use |
| SIG-78-OGT-WEKQ | IC-6702 | PROVISIONAL | Historical - verify before use |
| SIG-81-SBE-HL1C | IC-8927 | DEPRECATED | Historical - verify before use |
| SIG-64-LXA-3LJO | IC-6897 | PROVISIONAL | Historical - verify before use |
| SIG-24-SWK-GROA | IC-7225 | DEPRECATED | Historical - verify before use |
| SIG-47-QLD-IL46 | IC-8096 | PROVISIONAL | Historical - verify before use |
| SIG-80-PTU-ILTR | IC-9528 | PROVISIONAL | Historical - verify before use |
| SIG-34-IKF-VQJA | IC-6880 | REVIEW REQUIRED | Historical - verify before use |
| SIG-92-DNQ-WJAT | IC-9462 | PROVISIONAL | Historical - verify before use |
| SIG-73-WMX-7XJJ | IC-5637 | PROVISIONAL | Historical - verify before use |
| SIG-20-UMV-LJM6 | IC-5495 | PROVISIONAL | Historical - verify before use |
| SIG-65-XHR-R1SP | IC-6055 | REVIEW REQUIRED | Historical - verify before use |
| SIG-99-VAH-2H31 | IC-9763 | REVIEW REQUIRED | Historical - verify before use |
| SIG-71-FNO-CX9K | IC-6712 | PROVISIONAL | Historical - verify before use |
| SIG-29-KJI-GJKC | IC-9948 | REVIEW REQUIRED | Historical - verify before use |
| SIG-86-AKS-BEQE | IC-5443 | SUPERSEDED | Historical - verify before use |
| SIG-67-TPL-WT5F | IC-8448 | DEPRECATED | Historical - verify before use |
| SIG-92-ZTO-VZGU | IC-8758 | REVIEW REQUIRED | Historical - verify before use |
| SIG-61-IQH-EKWH | IC-9953 | SUPERSEDED | Historical - verify before use |
| SIG-21-HVD-EZVS | IC-7166 | DEPRECATED | Historical - verify before use |
| SIG-36-ZKX-4SE4 | IC-6698 | PROVISIONAL | Historical - verify before use |
| SIG-26-KHF-99OH | IC-6461 | DEPRECATED | Historical - verify before use |
| SIG-46-YHU-BU2J | IC-9311 | PROVISIONAL | Historical - verify before use |
| SIG-36-MYP-7NC2 | IC-7240 | REVIEW REQUIRED | Historical - verify before use |
| SIG-80-WEB-2C7R | IC-9922 | PROVISIONAL | Historical - verify before use |
| SIG-45-CWR-EI9N | IC-5994 | SUPERSEDED | Historical - verify before use |
| SIG-12-NAY-4AKW | IC-8902 | PROVISIONAL | Historical - verify before use |
| SIG-34-JQN-ROWX | IC-5184 | SUPERSEDED | Historical - verify before use |
| SIG-27-FHX-VO6Y | IC-6138 | PROVISIONAL | Historical - verify before use |
| SIG-53-LJE-NZKR | IC-7798 | SUPERSEDED | Historical - verify before use |
| SIG-64-VUE-OGQ2 | IC-7202 | REVIEW REQUIRED | Historical - verify before use |
| SIG-77-LFQ-EKT4 | IC-5806 | PROVISIONAL | Historical - verify before use |
| SIG-24-CXH-R2TY | IC-6115 | DEPRECATED | Historical - verify before use |
| SIG-64-TCV-R5SR | IC-6219 | DEPRECATED | Historical - verify before use |
| SIG-39-JMB-X1VA | IC-5095 | PROVISIONAL | Historical - verify before use |
| SIG-65-RQH-9Y5B | IC-7793 | SUPERSEDED | Historical - verify before use |
| SIG-43-KEL-FPY6 | IC-7800 | REVIEW REQUIRED | Historical - verify before use |
| SIG-57-RQB-VIKB | IC-6862 | DEPRECATED | Historical - verify before use |
| SIG-13-CGO-2Y4L | IC-5597 | DEPRECATED | Historical - verify before use |
| SIG-13-FYG-4NN9 | IC-8780 | SUPERSEDED | Historical - verify before use |
| SIG-27-QBE-DEK4 | IC-8831 | SUPERSEDED | Historical - verify before use |
| SIG-97-LME-ZEH9 | IC-7018 | PROVISIONAL | Historical - verify before use |
| SIG-60-KAS-IVMD | IC-9300 | PROVISIONAL | Historical - verify before use |
| SIG-99-GVJ-VPM6 | IC-5491 | SUPERSEDED | Historical - verify before use |
| SIG-20-CGL-C8HS | IC-8375 | PROVISIONAL | Historical - verify before use |
| SIG-68-DWS-MNR6 | IC-5847 | DEPRECATED | Historical - verify before use |
| SIG-86-VCP-SVOL | IC-6042 | REVIEW REQUIRED | Historical - verify before use |
| SIG-80-MLG-VDQ0 | IC-9677 | PROVISIONAL | Historical - verify before use |
| SIG-63-JJG-1TCH | IC-7698 | PROVISIONAL | Historical - verify before use |
| SIG-78-LTE-H4VL | IC-8089 | SUPERSEDED | Historical - verify before use |
| SIG-50-JOR-LO4P | IC-7001 | SUPERSEDED | Historical - verify before use |
| SIG-55-DCV-7OXN | IC-9673 | SUPERSEDED | Historical - verify before use |
| SIG-20-BPG-W8VL | IC-5437 | DEPRECATED | Historical - verify before use |
| SIG-37-WYK-X3LH | IC-9222 | SUPERSEDED | Historical - verify before use |
| SIG-64-LSR-RORA | IC-6815 | DEPRECATED | Historical - verify before use |
| SIG-40-PLP-7A3U | IC-9662 | SUPERSEDED | Historical - verify before use |
| SIG-52-FHA-5PI2 | IC-8555 | DEPRECATED | Historical - verify before use |
| SIG-56-SME-QSOD | IC-9872 | PROVISIONAL | Historical - verify before use |
| SIG-61-MHS-BQG3 | IC-5933 | DEPRECATED | Historical - verify before use |
| SIG-23-IEJ-V2T3 | IC-9648 | REVIEW REQUIRED | Historical - verify before use |
| SIG-12-JLN-YFH3 | IC-7487 | DEPRECATED | Historical - verify before use |
| SIG-83-XMM-APXP | IC-6571 | SUPERSEDED | Historical - verify before use |
| SIG-89-TVE-WANI | IC-7915 | REVIEW REQUIRED | Historical - verify before use |
| SIG-85-FIY-2QW4 | IC-5960 | SUPERSEDED | Historical - verify before use |
| SIG-23-UKD-B8UO | IC-8090 | PROVISIONAL | Historical - verify before use |
| SIG-63-YJW-AP00 | IC-5628 | DEPRECATED | Historical - verify before use |


#### 4.3.4 Excluded Assignments

The following assignments were identified but NOT completed due to data quality issues:

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-3965-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-2641-C | Data quality insufficient | Manual review scheduled |
| NOISE-9309-G | Missing required attributes | Escalated to data steward |
| NOISE-3531-E | Missing required attributes | Escalated to data steward |
| NOISE-7273-G | Out of scope per business decision | Business owner notified |
| NOISE-2745-C | Out of scope per business decision | Escalated to data steward |
| NOISE-1541-G | Missing required attributes | Manual review scheduled |
| NOISE-8617-D | Data quality insufficient | Business owner notified |
| NOISE-8698-F | Pending validation | Escalated to data steward |
| NOISE-4488-E | Pending validation | Manual review scheduled |
| NOISE-5258-E | Pending validation | Deferred to Phase 2 |
| NOISE-4814-H | Pending validation | Deferred to Phase 2 |
| NOISE-4952-H | Missing required attributes | Manual review scheduled |
| NOISE-6283-F | Missing required attributes | Business owner notified |
| NOISE-9121-D | Pending validation | Business owner notified |
| NOISE-1990-C | Missing required attributes | Manual review scheduled |
| NOISE-1672-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1784-A | Data quality insufficient | Manual review scheduled |
| NOISE-4395-E | Pending validation | Deferred to Phase 2 |
| NOISE-8714-G | Pending validation | Business owner notified |
| NOISE-5144-F | Out of scope per business decision | Escalated to data steward |
| NOISE-9690-G | Pending validation | Manual review scheduled |
| NOISE-6250-D | Duplicate source record | Business owner notified |
| NOISE-8366-G | Duplicate source record | Manual review scheduled |
| NOISE-9973-F | Out of scope per business decision | Manual review scheduled |
| NOISE-7716-D | Out of scope per business decision | Manual review scheduled |
| NOISE-6120-F | Missing required attributes | Escalated to data steward |
| NOISE-4255-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-9504-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8085-E | Pending validation | Business owner notified |
| NOISE-6099-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-8393-D | Pending validation | Business owner notified |
| NOISE-2924-A | Pending validation | Escalated to data steward |
| NOISE-7456-C | Data quality insufficient | Manual review scheduled |
| NOISE-1510-D | Duplicate source record | Business owner notified |
| NOISE-8015-G | Duplicate source record | Manual review scheduled |
| NOISE-7878-H | Missing required attributes | Manual review scheduled |
| NOISE-4081-E | Pending validation | Manual review scheduled |
| NOISE-4810-B | Pending validation | Manual review scheduled |
| NOISE-8428-H | Out of scope per business decision | Business owner notified |
| NOISE-4523-H | Out of scope per business decision | Manual review scheduled |
| NOISE-7163-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4898-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7835-H | Out of scope per business decision | Escalated to data steward |
| NOISE-1248-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-7216-H | Duplicate source record | Deferred to Phase 2 |
| NOISE-2439-F | Pending validation | Manual review scheduled |
| NOISE-8097-A | Missing required attributes | Manual review scheduled |
| NOISE-6623-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3124-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7563-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5041-D | Out of scope per business decision | Escalated to data steward |
| NOISE-2741-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-8486-D | Out of scope per business decision | Escalated to data steward |
| NOISE-3771-C | Data quality insufficient | Manual review scheduled |
| NOISE-7248-F | Duplicate source record | Business owner notified |
| NOISE-7002-F | Data quality insufficient | Escalated to data steward |
| NOISE-8393-E | Missing required attributes | Manual review scheduled |
| NOISE-8301-C | Pending validation | Business owner notified |
| NOISE-1696-D | Pending validation | Manual review scheduled |
| NOISE-4454-D | Duplicate source record | Escalated to data steward |
| NOISE-7296-C | Out of scope per business decision | Business owner notified |
| NOISE-7858-D | Data quality insufficient | Escalated to data steward |
| NOISE-4069-E | Pending validation | Business owner notified |
| NOISE-9017-F | Data quality insufficient | Escalated to data steward |
| NOISE-4623-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-5877-B | Missing required attributes | Manual review scheduled |
| NOISE-2807-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4067-C | Data quality insufficient | Business owner notified |
| NOISE-9789-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-5614-C | Missing required attributes | Business owner notified |
| NOISE-1959-D | Pending validation | Business owner notified |
| NOISE-7172-D | Out of scope per business decision | Business owner notified |
| NOISE-2939-H | Out of scope per business decision | Escalated to data steward |
| NOISE-5474-E | Missing required attributes | Escalated to data steward |
| NOISE-2056-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-2267-H | Out of scope per business decision | Escalated to data steward |
| NOISE-3630-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-5193-G | Duplicate source record | Escalated to data steward |
| NOISE-9322-D | Duplicate source record | Escalated to data steward |
| NOISE-5784-A | Pending validation | Business owner notified |
| NOISE-4828-A | Missing required attributes | Business owner notified |
| NOISE-3248-G | Out of scope per business decision | Escalated to data steward |
| NOISE-6689-G | Duplicate source record | Manual review scheduled |
| NOISE-5740-E | Out of scope per business decision | Business owner notified |
| NOISE-4946-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8142-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2937-F | Pending validation | Escalated to data steward |
| NOISE-9249-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-8129-G | Duplicate source record | Manual review scheduled |
| NOISE-3989-H | Duplicate source record | Escalated to data steward |
| NOISE-9540-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1260-G | Out of scope per business decision | Manual review scheduled |
| NOISE-7214-F | Pending validation | Escalated to data steward |
| NOISE-5282-A | Pending validation | Manual review scheduled |
| NOISE-2539-C | Pending validation | Manual review scheduled |
| NOISE-2208-A | Missing required attributes | Business owner notified |
| NOISE-7339-A | Pending validation | Escalated to data steward |
| NOISE-4572-E | Missing required attributes | Escalated to data steward |
| NOISE-4384-G | Pending validation | Manual review scheduled |
| NOISE-4519-H | Missing required attributes | Manual review scheduled |
| NOISE-1607-H | Data quality insufficient | Escalated to data steward |
| NOISE-1663-G | Duplicate source record | Escalated to data steward |
| NOISE-7862-F | Out of scope per business decision | Escalated to data steward |
| NOISE-5788-H | Duplicate source record | Business owner notified |
| NOISE-2476-B | Missing required attributes | Business owner notified |
| NOISE-3981-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2521-B | Missing required attributes | Business owner notified |
| NOISE-3559-A | Pending validation | Escalated to data steward |
| NOISE-5982-A | Pending validation | Manual review scheduled |
| NOISE-5371-H | Pending validation | Manual review scheduled |
| NOISE-2616-G | Out of scope per business decision | Escalated to data steward |
| NOISE-4965-H | Duplicate source record | Manual review scheduled |
| NOISE-8542-F | Pending validation | Business owner notified |
| NOISE-5309-D | Out of scope per business decision | Business owner notified |
| NOISE-4155-C | Missing required attributes | Escalated to data steward |
| NOISE-7114-G | Pending validation | Escalated to data steward |
| NOISE-5999-B | Out of scope per business decision | Manual review scheduled |
| NOISE-8829-B | Out of scope per business decision | Escalated to data steward |
| NOISE-1278-F | Pending validation | Escalated to data steward |
| NOISE-3396-C | Missing required attributes | Business owner notified |
| NOISE-4451-D | Pending validation | Escalated to data steward |
| NOISE-1221-A | Duplicate source record | Manual review scheduled |
| NOISE-1645-A | Missing required attributes | Business owner notified |
| NOISE-1296-G | Pending validation | Escalated to data steward |
| NOISE-1282-H | Duplicate source record | Manual review scheduled |
| NOISE-6819-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-8574-B | Out of scope per business decision | Business owner notified |
| NOISE-6348-F | Pending validation | Escalated to data steward |
| NOISE-3419-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8741-H | Duplicate source record | Manual review scheduled |
| NOISE-1776-A | Missing required attributes | Escalated to data steward |
| NOISE-6251-G | Missing required attributes | Business owner notified |
| NOISE-3064-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7813-F | Data quality insufficient | Business owner notified |
| NOISE-9779-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3839-H | Pending validation | Manual review scheduled |
| NOISE-3100-B | Missing required attributes | Manual review scheduled |
| NOISE-5013-E | Pending validation | Business owner notified |
| NOISE-9224-H | Pending validation | Deferred to Phase 2 |
| NOISE-9753-G | Pending validation | Deferred to Phase 2 |
| NOISE-3772-E | Pending validation | Deferred to Phase 2 |
| NOISE-4940-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-4687-G | Data quality insufficient | Manual review scheduled |
| NOISE-3652-D | Pending validation | Manual review scheduled |
| NOISE-7794-H | Missing required attributes | Manual review scheduled |
| NOISE-2714-H | Data quality insufficient | Manual review scheduled |
| NOISE-9621-D | Out of scope per business decision | Business owner notified |
| NOISE-9202-G | Duplicate source record | Business owner notified |
| NOISE-4754-E | Missing required attributes | Business owner notified |
| NOISE-3952-E | Out of scope per business decision | Manual review scheduled |
| NOISE-5866-C | Missing required attributes | Business owner notified |
| NOISE-6864-E | Pending validation | Manual review scheduled |
| NOISE-1887-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-4345-F | Missing required attributes | Business owner notified |
| NOISE-3951-B | Duplicate source record | Business owner notified |
| NOISE-5640-H | Data quality insufficient | Manual review scheduled |
| NOISE-9650-C | Pending validation | Business owner notified |
| NOISE-4981-D | Pending validation | Deferred to Phase 2 |
| NOISE-4707-D | Pending validation | Escalated to data steward |
| NOISE-6663-B | Duplicate source record | Manual review scheduled |
| NOISE-9631-F | Data quality insufficient | Business owner notified |
| NOISE-7574-H | Data quality insufficient | Business owner notified |
| NOISE-8662-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9184-G | Pending validation | Deferred to Phase 2 |
| NOISE-7055-D | Data quality insufficient | Business owner notified |
| NOISE-9115-D | Out of scope per business decision | Manual review scheduled |
| NOISE-2721-B | Missing required attributes | Business owner notified |
| NOISE-5800-C | Data quality insufficient | Manual review scheduled |
| NOISE-9282-D | Missing required attributes | Business owner notified |
| NOISE-8188-B | Out of scope per business decision | Business owner notified |
| NOISE-3743-A | Missing required attributes | Escalated to data steward |
| NOISE-6872-G | Missing required attributes | Escalated to data steward |
| NOISE-1550-D | Duplicate source record | Manual review scheduled |
| NOISE-2213-C | Duplicate source record | Escalated to data steward |
| NOISE-3798-F | Pending validation | Escalated to data steward |
| NOISE-8091-B | Data quality insufficient | Business owner notified |
| NOISE-7117-G | Duplicate source record | Manual review scheduled |
| NOISE-4346-D | Data quality insufficient | Escalated to data steward |
| NOISE-7189-A | Out of scope per business decision | Escalated to data steward |
| NOISE-3029-D | Out of scope per business decision | Manual review scheduled |
| NOISE-1173-G | Out of scope per business decision | Business owner notified |
| NOISE-5889-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-7521-C | Missing required attributes | Business owner notified |
| NOISE-2177-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-8846-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-9984-H | Data quality insufficient | Business owner notified |
| NOISE-4271-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-2149-B | Pending validation | Deferred to Phase 2 |
| NOISE-3318-D | Duplicate source record | Business owner notified |
| NOISE-1299-D | Out of scope per business decision | Business owner notified |
| NOISE-6207-F | Out of scope per business decision | Escalated to data steward |
| NOISE-6022-E | Pending validation | Manual review scheduled |
| NOISE-9243-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-4766-F | Data quality insufficient | Business owner notified |
| NOISE-5144-B | Out of scope per business decision | Manual review scheduled |
| NOISE-4527-E | Pending validation | Manual review scheduled |
| NOISE-9408-C | Pending validation | Manual review scheduled |
| NOISE-9638-F | Duplicate source record | Business owner notified |
| NOISE-9136-H | Pending validation | Escalated to data steward |
| NOISE-7580-B | Duplicate source record | Business owner notified |
| NOISE-9354-G | Missing required attributes | Manual review scheduled |
| NOISE-5169-B | Missing required attributes | Manual review scheduled |
| NOISE-9526-E | Out of scope per business decision | Escalated to data steward |
| NOISE-4582-E | Pending validation | Manual review scheduled |
| NOISE-5546-D | Data quality insufficient | Escalated to data steward |
| NOISE-4499-D | Missing required attributes | Business owner notified |
| NOISE-7599-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4427-D | Missing required attributes | Manual review scheduled |
| NOISE-6321-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-2513-E | Missing required attributes | Manual review scheduled |
| NOISE-3436-G | Duplicate source record | Escalated to data steward |
| NOISE-6074-F | Data quality insufficient | Manual review scheduled |
| NOISE-6093-C | Pending validation | Escalated to data steward |
| NOISE-6296-G | Missing required attributes | Manual review scheduled |
| NOISE-6905-F | Duplicate source record | Escalated to data steward |
| NOISE-2340-F | Out of scope per business decision | Manual review scheduled |
| NOISE-3996-D | Pending validation | Deferred to Phase 2 |
| NOISE-5551-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-7936-E | Missing required attributes | Manual review scheduled |
| NOISE-9283-C | Missing required attributes | Manual review scheduled |
| NOISE-4006-D | Duplicate source record | Manual review scheduled |
| NOISE-8521-H | Pending validation | Manual review scheduled |
| NOISE-5900-A | Out of scope per business decision | Escalated to data steward |
| NOISE-1992-E | Pending validation | Escalated to data steward |
| NOISE-7078-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-3096-G | Pending validation | Manual review scheduled |
| NOISE-3740-C | Data quality insufficient | Business owner notified |
| NOISE-8106-D | Data quality insufficient | Manual review scheduled |
| NOISE-4802-E | Missing required attributes | Escalated to data steward |
| NOISE-3911-B | Pending validation | Manual review scheduled |
| NOISE-9029-A | Out of scope per business decision | Business owner notified |
| NOISE-1387-E | Out of scope per business decision | Escalated to data steward |
| NOISE-9635-G | Duplicate source record | Business owner notified |
| NOISE-7553-D | Data quality insufficient | Manual review scheduled |
| NOISE-9435-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-3772-G | Data quality insufficient | Business owner notified |
| NOISE-9386-G | Out of scope per business decision | Business owner notified |
| NOISE-2689-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6903-F | Data quality insufficient | Escalated to data steward |
| NOISE-7872-E | Out of scope per business decision | Business owner notified |
| NOISE-9221-A | Data quality insufficient | Escalated to data steward |
| NOISE-9294-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-4215-A | Pending validation | Business owner notified |
| NOISE-7518-G | Out of scope per business decision | Business owner notified |
| NOISE-4997-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-9777-H | Pending validation | Escalated to data steward |
| NOISE-4419-A | Pending validation | Business owner notified |
| NOISE-7615-D | Out of scope per business decision | Escalated to data steward |
| NOISE-1411-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5447-B | Pending validation | Business owner notified |
| NOISE-4962-G | Duplicate source record | Manual review scheduled |
| NOISE-3510-D | Data quality insufficient | Manual review scheduled |
| NOISE-4211-D | Missing required attributes | Manual review scheduled |
| NOISE-8331-E | Data quality insufficient | Business owner notified |
| NOISE-1407-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9965-C | Data quality insufficient | Business owner notified |
| NOISE-4768-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7068-E | Missing required attributes | Escalated to data steward |
| NOISE-9793-C | Data quality insufficient | Manual review scheduled |
| NOISE-1243-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-5607-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-9668-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9472-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-1818-G | Duplicate source record | Manual review scheduled |
| NOISE-4957-H | Duplicate source record | Escalated to data steward |
| NOISE-7138-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2661-E | Duplicate source record | Manual review scheduled |
| NOISE-2268-F | Duplicate source record | Escalated to data steward |
| NOISE-1788-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8637-A | Data quality insufficient | Manual review scheduled |
| NOISE-5034-F | Duplicate source record | Manual review scheduled |
| NOISE-7904-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1354-E | Out of scope per business decision | Escalated to data steward |
| NOISE-1786-G | Duplicate source record | Business owner notified |
| NOISE-1854-F | Missing required attributes | Escalated to data steward |
| NOISE-4014-E | Data quality insufficient | Business owner notified |
| NOISE-1929-H | Pending validation | Manual review scheduled |
| NOISE-8637-H | Missing required attributes | Escalated to data steward |
| NOISE-2984-C | Pending validation | Deferred to Phase 2 |
| NOISE-1290-F | Missing required attributes | Escalated to data steward |
| NOISE-4248-B | Missing required attributes | Manual review scheduled |
| NOISE-5916-F | Pending validation | Escalated to data steward |
| NOISE-1719-A | Data quality insufficient | Business owner notified |
| NOISE-6946-E | Pending validation | Business owner notified |
| NOISE-3769-B | Data quality insufficient | Business owner notified |
| NOISE-1592-C | Pending validation | Escalated to data steward |
| NOISE-4450-H | Data quality insufficient | Manual review scheduled |
| NOISE-1123-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-9749-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8692-E | Out of scope per business decision | Manual review scheduled |
| NOISE-2936-F | Pending validation | Manual review scheduled |
| NOISE-8147-E | Pending validation | Business owner notified |
| NOISE-8911-H | Data quality insufficient | Escalated to data steward |
| NOISE-9984-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-4212-A | Pending validation | Business owner notified |


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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230813_000000`
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
| Technical Lead | Sarah Chen (Data Governance) | sarah@company.com | +1-555-0102 |
| Business Owner | James Wilson (Finance) | james@company.com | +1-555-0103 |
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
