# Migration Runbook: System Migration: DATA_QUALITY_2022

**Document ID**: RB-DATA_QUALITY_2022-5191
**Version**: 2.3
**Last Updated**: 2023-06-07
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the System Migration: DATA_QUALITY_2022 project.
The migration involves transitioning master data and transactional records from SOURCE
to TARGET while maintaining data integrity and business continuity.

**Project Timeline**: 2023-03-04 to 2023-08-05
**Business Sponsor**: Business Operations
**Technical Owner**: IT Team

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
|   SOURCE       |     |   Staging Layer  |     |   TARGET       |
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
SOURCE. Each source entity is assigned an internal staging code for
tracking purposes.

**IMPORTANT**: This document only contains source-to-staging assignments.
Target system mappings are maintained separately in the MDM Registry.

### 4.2 Assignment Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1590 | Completed |
| Codes assigned | 1077 | Staged |
| Excluded from scope | 323 | Documented |
| Pending review | 9 | In Progress |

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

| Source Entity (SOURCE) | Internal Code | Assignment Date | Department |
|--------------------------------|---------------|-----------------|------------|
| PR-SU-935 Ltd. | IC-8336 | 2023-11-13 | IT Infrastructure |
| Kaliumsorbat | TC-8344 | 2023-08-25 | Compliance |
| Ascorbic Acid 50% Standardqualität | BC-8351 | 2024-10-24 | Supply Chain |
| Stellar Partners | IC-8373 | 2022-09-10 | Finance |
| Stratos Chemicals | TC-8384 | 2021-03-08 | Supply Chain |
| Global Solutions Group | IC-8386 | 2021-01-09 | Product Management |
| pinnacle ingredients GmbH | IC-8391 | 2023-12-23 | Finance |
| Atlantic Rohstoffe International | TC-8395 | 2023-11-14 | Finance |
| SIG-35-RSV-01YT | TC-8416 | 2021-02-20 | IT Infrastructure |
| Vanguard Logistik | BC-8438 | 2021-10-02 | Data Governance |
| Atlas Logistics | TC-8443 | 2021-03-25 | Supply Chain |
| Premier Rohstoffe Holdings | TC-8465 | 2024-08-01 | IT Infrastructure |
| Vat Standard CN 10% | BC-8492 | 2024-02-22 | Finance |
| customs duty fr 19% | BC-8501 | 2021-05-06 | Operations |
| ST-MA-670 Group | BC-8502 | 2021-01-02 | Finance |
| SIG-37-NAI-M1G9 | IC-8518 | 2022-07-10 | IT Infrastructure |
| SIG-22-ADK-3T78 | BC-8534 | 2022-01-22 | Data Governance |
| SIG-70-HGQ-WORL | TC-8547 | 2023-10-03 | Data Governance |
| AS-AC-GR-B-395 | IC-8557 | 2022-08-12 | Finance |
| vertex enterprise Group | IC-8565 | 2022-06-13 | Product Management |
| Baltic Enterprise KG | TC-8578 | 2022-01-05 | Supply Chain |
| sodium benzoate 99.5% tech grade | BC-8600 | 2024-06-06 | Finance |
| DE-GR-A-472 | TC-8615 | 2022-11-28 | Operations |
| PR-PA-643 | IC-8632 | 2021-05-22 | Supply Chain |
| Sorbinsäure 50% Standardqualität | BC-8672 | 2022-02-28 | Supply Chain |
| SIG-89-RGS-FIRM Holdings | BC-8680 | 2022-10-20 | Product Management |
| SIG-98-DBG-MTO5 | BC-8691 | 2023-05-02 | Compliance |
| RE-ST-GR-B-805 | BC-8712 | 2023-02-18 | Finance |
| SIG-26-WVS-AQ3B | IC-8723 | 2023-12-24 | Product Management |
| vat reduced cn 19% | IC-8735 | 2023-01-28 | Compliance |
| SIG-55-KQD-CQMQ | TC-8740 | 2023-02-11 | Supply Chain |
| Zitronensäure 70% | BC-8741 | 2021-02-22 | Operations |
| PR-SO-388 | IC-8750 | 2024-02-12 | IT Infrastructure |
| CU-DU-N-5-217 | BC-8755 | 2023-08-10 | Product Management |
| CA-GR-A-380 | BC-8780 | 2021-04-20 | IT Infrastructure |
| Traubenzucker Standardqualität | IC-8797 | 2023-10-03 | IT Infrastructure |
| Pea Protein Grade A | BC-8805 | 2021-02-19 | Product Management |
| SIG-75-DRM-1CLN | TC-8823 | 2021-03-26 | Product Management |
| NO-DI-582 AG | IC-8825 | 2024-06-02 | IT Infrastructure |
| Zitronensäure Qualitätsstufe I | TC-8848 | 2024-06-22 | Supply Chain |
| ST-LO-136 | TC-8853 | 2023-12-03 | Data Governance |
| SIG-81-FXX-6VPL | IC-8862 | 2023-04-18 | Operations |
| Sorbinsäure 98% | BC-8867 | 2021-10-24 | Operations |
| palm oil 99.5% | IC-8885 | 2021-04-24 | IT Infrastructure |
| Vat Reduced BR 25% | IC-8888 | 2021-11-06 | Compliance |
| SIG-35-HUP-NW3M | BC-8894 | 2023-02-25 | Finance |
| PO-SO-PR-101 | TC-8905 | 2024-03-01 | Finance |
| Rapsöl 99.5% Technische Qualität | TC-8911 | 2023-05-02 | Compliance |
| global materials | TC-8917 | 2023-08-12 | Data Governance |
| Nexus Commodities International | BC-8918 | 2023-04-26 | Compliance |
| Excise GB 25% | IC-8920 | 2021-04-22 | IT Infrastructure |
| Natriumchlorid 70% | IC-8941 | 2023-07-25 | Supply Chain |
| PR-MA-669 Ltd. | BC-8947 | 2023-01-05 | Product Management |
| calcium carbonate 99.5% | IC-8957 | 2022-09-28 | IT Infrastructure |
| MA-DE-933 | BC-8963 | 2023-04-08 | IT Infrastructure |
| Stellar Versorgung GmbH | BC-8966 | 2023-03-16 | Finance |
| SIG-27-FHX-VO6Y | IC-8973 | 2023-10-13 | Supply Chain |
| Baltic Sourcing | BC-8980 | 2024-03-04 | Product Management |
| Potassium Sorbate 70% | IC-9004 | 2022-09-10 | Supply Chain |
| Coconut Oil 98% | IC-9006 | 2022-07-18 | Compliance |
| SO-CH-70-GR-B-821 | BC-9009 | 2024-08-25 | Finance |
| Elite Materials | TC-9022 | 2023-09-27 | Compliance |
| vat standard nl 5% | TC-9027 | 2024-11-02 | Data Governance |
| Central Logistik Holdings | IC-9072 | 2022-12-23 | Product Management |
| Ascorbic Acid | TC-9083 | 2022-02-18 | Operations |
| SIG-91-XWQ-EANP | IC-9104 | 2021-07-27 | Supply Chain |
| Excise IN 19% | IC-9113 | 2021-07-27 | Data Governance |
| sorbic acid | TC-9131 | 2024-12-20 | IT Infrastructure |
| Vat Standardqualität IN 0% | IC-9134 | 2021-08-06 | Product Management |
| Zitronensäure Qualitätsstufe I | IC-9136 | 2021-06-22 | Finance |
| Excise IN 25% | TC-9146 | 2023-07-01 | Operations |
| Natriumchlorid Technische Qualität | IC-9170 | 2022-09-15 | Data Governance |
| SIG-30-PPI-DU4D | IC-9175 | 2023-02-16 | Finance |
| AP-SU-CO-814 | TC-9176 | 2022-01-12 | Data Governance |
| Withholding BR 5% | BC-9210 | 2022-04-08 | Product Management |
| apex chemicals Inc. | BC-9233 | 2023-05-17 | Compliance |
| meridian materials | TC-9237 | 2023-03-11 | Data Governance |
| wheat gluten 70% | TC-9278 | 2023-03-18 | Product Management |
| Dextrin 50% | BC-9334 | 2022-07-14 | Supply Chain |
| SIG-29-RWA-CHL8 | BC-9339 | 2022-06-20 | Supply Chain |
| Atlas Logistics | TC-9355 | 2021-04-14 | Supply Chain |
| Isoglucose 98% | BC-9366 | 2021-12-16 | Operations |
| Vat Reduced IN 20% | TC-9370 | 2024-12-20 | Operations |
| Baltic Versorgung | BC-9380 | 2021-02-16 | IT Infrastructure |
| nexus sourcing | BC-9384 | 2023-02-05 | Data Governance |
| Sorbinsäure | IC-9387 | 2023-06-26 | Supply Chain |
| RA-OI-FO-GR-269 | TC-9403 | 2024-03-04 | Data Governance |
| Nordic Logistik | IC-9417 | 2022-10-06 | Product Management |
| apex processing Ltd. | TC-9426 | 2022-10-16 | Finance |
| Vat Reduced BR 19% | IC-9435 | 2021-06-10 | Data Governance |
| Ascorbic Acid 70% | TC-9443 | 2023-06-02 | Supply Chain |
| Pea Protein | TC-9451 | 2022-06-23 | Product Management |
| AS-AC-165 | BC-9452 | 2023-07-23 | Compliance |
| elite materials | BC-9465 | 2023-12-10 | Operations |
| Ascorbic Acid 50% | IC-9468 | 2022-10-23 | IT Infrastructure |
| SIG-99-IZM-CYBY | IC-9536 | 2022-05-24 | IT Infrastructure |
| Dextrin 98% | BC-9543 | 2023-10-21 | IT Infrastructure |
| Apex Trading Holdings | BC-9548 | 2022-06-11 | Compliance |
| lactic acid 98% premium | BC-9549 | 2021-09-17 | Supply Chain |
| SIG-90-NFZ-XRLG | TC-9551 | 2024-06-09 | Data Governance |
| SIG-39-OZI-N968 | BC-9552 | 2024-02-10 | Data Governance |
| Fructose Premiumqualität | BC-9567 | 2023-08-07 | Data Governance |
| citric acid standard | BC-9574 | 2022-07-08 | Finance |
| Soja Isolate Premiumqualität | BC-9589 | 2022-08-17 | Finance |
| SIG-61-CIV-LFWA | IC-9592 | 2022-10-08 | Finance |
| Isoglucose Lebensmittelrein | BC-9597 | 2021-05-20 | Supply Chain |
| Fructose Standardqualität | TC-9601 | 2024-09-21 | Supply Chain |
| Prime Werkstoffe | BC-9639 | 2024-12-24 | IT Infrastructure |
| SIG-58-SVK-Z948 | IC-9655 | 2023-11-22 | Supply Chain |
| SO-AC-70-785 | BC-9660 | 2023-09-18 | Operations |
| Stratos Supply SAS | TC-9665 | 2022-06-17 | Compliance |
| Atlantic Verarbeitung Group | TC-9673 | 2023-09-03 | Compliance |
| Atlantic Logistics SAS | BC-9683 | 2023-09-18 | Finance |
| Customs Duty BR 21% | BC-9687 | 2024-05-21 | Data Governance |
| SIG-93-ZCF-6HM3 | BC-9702 | 2023-11-12 | Product Management |
| PR-SU-CO-591 | TC-9706 | 2023-06-15 | Data Governance |
| Vat Reduced CN 21% | BC-9707 | 2021-05-16 | Finance |
| CO-OI-ST-153 | BC-9730 | 2024-03-23 | Finance |
| ST-SO-673 | TC-9733 | 2021-07-04 | Operations |
| Glucose Syrup 70% | TC-9746 | 2021-08-10 | Finance |
| Elite Sourcing | BC-9777 | 2021-05-24 | Product Management |
| dextrose | TC-9778 | 2022-08-23 | Data Governance |
| CE-PA-586 SARL | IC-9779 | 2024-10-23 | Data Governance |
| CA-CA-648 | BC-9807 | 2022-06-08 | Supply Chain |
| PR-MA-161 | IC-9809 | 2024-12-07 | IT Infrastructure |
| pinnacle industries SAS | BC-9811 | 2023-12-24 | Compliance |
| PR-SO-469 | IC-9812 | 2022-09-06 | Compliance |
| Isoglucose | BC-9826 | 2023-02-02 | IT Infrastructure |
| SIG-93-ZCF-6HM3 | TC-9841 | 2024-02-06 | Operations |
| SIG-27-FHX-VO6Y | IC-9847 | 2024-11-11 | IT Infrastructure |
| SIG-88-XZP-H10B | IC-9853 | 2024-03-16 | Supply Chain |
| Casein 50% Premium | IC-9888 | 2022-07-06 | Supply Chain |
| SIG-43-OLC-OFCX | IC-9892 | 2024-10-12 | Operations |
| PA-OI-70-GR-B-781 | TC-9899 | 2021-10-26 | IT Infrastructure |
| Rapsöl 98% Standardqualität | IC-9909 | 2024-02-18 | Data Governance |
| Natriumbenzoat | BC-9915 | 2024-01-14 | Product Management |
| SIG-52-EML-H8JV | IC-9921 | 2024-06-18 | Supply Chain |
| Nordic Manufacturing Holdings | BC-9926 | 2022-01-26 | Product Management |
| PA-OI-TE-134 | TC-9929 | 2021-01-28 | IT Infrastructure |
| Global Werkstoffe | TC-9935 | 2022-02-04 | Product Management |
| Vertex Chemicals Holdings | IC-9979 | 2022-11-12 | Product Management |
| IS-FO-GR-555 | IC-9982 | 2023-10-13 | Product Management |
| PR-PA-269 AG | TC-9988 | 2022-09-11 | Supply Chain |
| SU-OI-FO-GR-778 | IC-9997 | 2021-07-11 | Data Governance |
| SIG-92-ZTO-VZGU | BC-10015 | 2022-03-05 | Data Governance |
| Stellar Sourcing | IC-10022 | 2021-06-04 | Operations |
| fructose 99.5% tech grade | BC-10042 | 2022-12-17 | Compliance |
| sorbic acid 25% pharma grade | BC-10054 | 2022-06-20 | Finance |
| CU-DU-G-0-770 | TC-10061 | 2022-10-13 | Operations |
| quantum supply | BC-10069 | 2024-01-09 | Finance |
| Calcium Carbonate 50% Food Grade | TC-10076 | 2023-07-14 | Product Management |
| sorbic acid premium | BC-10084 | 2021-12-22 | IT Infrastructure |
| SIG-92-RZH-LRHH | TC-10090 | 2022-11-01 | Finance |
| vat standard fr 5% | BC-10099 | 2023-11-05 | Operations |
| Sonnenblumenöl 70% Lebensmittelrein | IC-10105 | 2022-10-11 | Supply Chain |
| stratos commodities Holdings | TC-10138 | 2024-06-07 | Product Management |
| Pea Protein | IC-10139 | 2024-09-04 | IT Infrastructure |
| Sonnenblumenöl 70% Lebensmittelrein | BC-10152 | 2024-07-08 | Finance |
| SIG-56-JML-GDXB | IC-10156 | 2023-03-23 | Product Management |
| Lactic Acid 99.5% Grade B | IC-10171 | 2024-07-19 | Operations |
| Dextrose 25% | TC-10172 | 2023-12-08 | Supply Chain |
| SIG-50-JOR-LO4P | BC-10183 | 2022-08-05 | Data Governance |
| Coconut Oil 70% Qualitätsstufe I | TC-10190 | 2024-04-25 | Supply Chain |
| SIG-13-CGO-2Y4L | IC-10200 | 2023-08-16 | Finance |
| baltic supply | IC-10209 | 2021-10-06 | Operations |
| Traubenzucker Lebensmittelrein | IC-10211 | 2022-03-11 | Finance |
| Isoglucose 25% Lebensmittelrein | IC-10217 | 2021-01-25 | Compliance |
| Continental Werkstoffe NV | BC-10225 | 2022-12-17 | Operations |
| SIG-56-BPD-M0A6 | BC-10229 | 2023-05-12 | Data Governance |
| SIG-98-CGL-FHWJ | BC-10262 | 2022-07-21 | Finance |
| SIG-65-XHR-R1SP | IC-10287 | 2021-02-06 | Compliance |
| SIG-70-QGS-CCAF | TC-10292 | 2022-04-27 | IT Infrastructure |
| Pea Protein 70% Pharma Grade | IC-10306 | 2024-04-22 | Product Management |
| quantum logistics | BC-10311 | 2024-09-02 | IT Infrastructure |
| CA-CA-648 | BC-10352 | 2023-08-27 | Compliance |
| Premier Versorgung GmbH | TC-10371 | 2022-08-23 | Data Governance |
| apex logistics LLC | TC-10383 | 2023-10-05 | Finance |
| Lactic Acid | IC-10397 | 2021-04-01 | Product Management |
| Isoglucose 70% | BC-10422 | 2023-11-24 | Supply Chain |
| Fructose 99.5% Pharma Grade | IC-10432 | 2021-07-08 | Supply Chain |
| Excise US 19% | BC-10436 | 2024-06-25 | Supply Chain |
| Isoglucose Food Grade | BC-10443 | 2023-03-03 | Compliance |
| quantum ingredients Holdings | BC-10453 | 2022-03-20 | Compliance |
| Zitronensäure 98% | TC-10462 | 2024-11-13 | IT Infrastructure |
| LA-AC-ST-663 | BC-10473 | 2021-02-08 | Operations |
| CA-580 | TC-10483 | 2022-07-20 | Product Management |
| SO-BE-824 | TC-10510 | 2023-03-04 | IT Infrastructure |
| Lactic Acid Technical | IC-10512 | 2022-09-04 | Compliance |
| CE-MA-338 | IC-10526 | 2023-08-14 | IT Infrastructure |
| Wheat Gluten 25% Standard | BC-10530 | 2024-03-09 | Product Management |
| CO-OI-98-876 | IC-10534 | 2022-02-26 | IT Infrastructure |
| SO-IS-PH-GR-671 | IC-10553 | 2022-02-25 | Finance |
| dextrose 50% standard | IC-10555 | 2022-03-11 | Finance |
| PO-SO-339 | BC-10570 | 2024-04-06 | Data Governance |
| pea protein 70% premium | IC-10579 | 2024-12-17 | Operations |
| Global Chemicals | TC-10588 | 2022-02-15 | Finance |
| SIG-56-ZQV-YINP SA | BC-10602 | 2021-08-28 | Finance |
| SIG-98-HZM-47LK | IC-10603 | 2021-03-11 | Compliance |
| SIG-22-XCC-QSNV | TC-10609 | 2021-07-08 | Operations |
| SIG-42-HBL-L3KU International | BC-10638 | 2023-08-03 | Compliance |
| lactic acid standard | IC-10644 | 2021-12-15 | Compliance |
| Pea Protein 98% | TC-10646 | 2022-09-02 | Supply Chain |
| VE-IN-631 Ltd. | IC-10691 | 2023-08-02 | Finance |
| SIG-94-MKW-LH8F | TC-10695 | 2021-02-15 | Product Management |
| SIG-81-AXG-9CBI AG | TC-10705 | 2021-05-22 | Supply Chain |
| Isoglucose Grade B | IC-10751 | 2024-08-25 | Product Management |
| SIG-51-ZAY-11PM | BC-10752 | 2024-06-28 | Compliance |
| Catalyst Manufacturing GmbH | TC-10754 | 2023-06-14 | Product Management |
| maltodextrin de18 | TC-10760 | 2022-11-02 | IT Infrastructure |
| Sonnenblumenöl Standardqualität | IC-10764 | 2021-01-05 | IT Infrastructure |
| Meridian Solutions KG | BC-10769 | 2023-03-09 | IT Infrastructure |
| vanguard enterprise | TC-10795 | 2022-05-18 | Data Governance |
| Quantum Werkstoffe | TC-10833 | 2023-10-15 | Finance |
| Stellar Handel | IC-10836 | 2024-07-16 | Product Management |
| Customs Duty FR 25% | BC-10842 | 2022-05-16 | Data Governance |
| Natriumchlorid Lebensmittelrein | IC-10844 | 2024-11-16 | Supply Chain |
| SIG-76-AAU-3VM8 | BC-10851 | 2022-07-06 | Finance |
| Fructose | TC-10855 | 2024-07-06 | Supply Chain |
| Nordic Rohstoffe | TC-10870 | 2024-09-07 | Product Management |
| Coconut Oil 25% Technische Qualität | BC-10872 | 2022-09-23 | Data Governance |
| Traubenzucker Standardqualität | TC-10877 | 2024-04-28 | Supply Chain |
| Soja Isolate Premiumqualität | IC-10911 | 2022-06-05 | Operations |
| Baltic Processing PLC | BC-10920 | 2021-06-07 | Finance |
| Prism Logistik | BC-10932 | 2022-05-18 | Data Governance |
| SIG-97-SMQ-9SG6 | BC-10934 | 2023-06-23 | Supply Chain |
| Casein Standard | BC-10939 | 2024-08-28 | IT Infrastructure |
| Coconut Oil 70% Qualitätsstufe I | BC-10949 | 2022-01-06 | IT Infrastructure |
| Palm Oil 99.5% | IC-10973 | 2022-05-02 | Supply Chain |
| LA-AC-ST-663 | TC-10987 | 2022-02-19 | Compliance |
| PI-DI-618 NV | IC-11047 | 2023-04-22 | IT Infrastructure |
| SIG-50-FUX-7S9T | BC-11051 | 2021-04-12 | Product Management |
| Atlas Logistik | BC-11060 | 2021-12-22 | Operations |
| Ascorbic Acid | TC-11065 | 2021-07-01 | Supply Chain |
| CA-CA-436 | IC-11072 | 2022-03-11 | Compliance |
| Sodium Benzoate | BC-11076 | 2024-12-28 | Product Management |
| Pea Protein 99.5% | BC-11094 | 2022-06-02 | Data Governance |
| Core Sourcing | BC-11099 | 2024-09-10 | Operations |
| Potassium Sorbate | TC-11116 | 2024-08-27 | Data Governance |
| Lactic Acid Food Grade | IC-11124 | 2023-01-07 | Supply Chain |
| sorbic acid 98% | IC-11129 | 2021-01-02 | Supply Chain |
| SIG-99-CTB-8OFG Group | IC-11137 | 2023-11-02 | Supply Chain |
| WH-GL-923 | TC-11153 | 2023-10-08 | Finance |
| Nexus Versorgung GmbH | TC-11156 | 2024-05-14 | Supply Chain |
| PO-SO-339 | BC-11170 | 2022-02-12 | Compliance |
| sodium benzoate premium | TC-11177 | 2023-12-14 | Operations |
| Resistente Stärke Lebensmittelrein | TC-11178 | 2021-08-08 | Product Management |
| SIG-71-FSV-21LW | TC-11181 | 2023-11-03 | Compliance |
| Resistente Stärke | TC-11183 | 2021-05-20 | Product Management |
| customs duty us 15% | IC-11221 | 2023-04-14 | Finance |
| Stellar Manufacturing Holdings | BC-11230 | 2024-05-05 | Supply Chain |
| NE-MA-648 | BC-11233 | 2021-11-27 | Product Management |
| excise br 21% | TC-11236 | 2024-09-15 | Data Governance |
| Sunflower Oil Standard | BC-11241 | 2021-06-13 | Supply Chain |
| casein standard | BC-11244 | 2022-08-07 | Operations |
| SIG-75-GUI-J643 | IC-11249 | 2021-09-15 | Product Management |
| sunflower oil | TC-11257 | 2022-09-16 | Data Governance |
| Ascorbic Acid | IC-11291 | 2023-07-11 | Compliance |
| SIG-97-UWA-JWLN | TC-11295 | 2023-12-18 | Data Governance |
| NE-PA-358 | IC-11302 | 2024-04-09 | Product Management |
| Coconut Oil Grade A | TC-11304 | 2023-11-18 | Product Management |
| ST-IN-592 SA | IC-11309 | 2021-08-15 | Product Management |
| SIG-55-DBH-2QS3 | BC-11330 | 2021-11-17 | Data Governance |
| sodium benzoate premium | TC-11337 | 2024-12-04 | Operations |
| quantum supply | BC-11348 | 2022-10-09 | Finance |
| atlas partners | BC-11365 | 2024-07-16 | Compliance |
| vat standard de 0% | IC-11390 | 2022-01-16 | Product Management |
| BA-IN-547 | BC-11392 | 2023-10-16 | Operations |
| DE-70-769 | IC-11411 | 2024-04-19 | Compliance |
| AT-SU-CO-864 | BC-11421 | 2024-03-03 | Product Management |
| SIG-79-GKV-W8GA | IC-11426 | 2022-12-24 | Product Management |
| Dextrose 70% Grade A | BC-11446 | 2022-03-08 | Data Governance |
| Dextrin 98% | TC-11448 | 2022-08-08 | Supply Chain |
| dextrose standard | BC-11454 | 2023-02-16 | Data Governance |
| prime processing PLC | BC-11458 | 2022-02-17 | IT Infrastructure |
| Pea Protein | BC-11509 | 2024-07-15 | Finance |
| SO-AC-852 | BC-11517 | 2022-10-08 | Supply Chain |
| SIG-50-DEU-V25U | IC-11530 | 2024-08-13 | Product Management |
| meridian chemicals Holdings | BC-11533 | 2021-03-14 | Finance |
| stratos partners SA | IC-11538 | 2021-03-03 | Compliance |
| SIG-62-DCP-L2AF | TC-11551 | 2023-08-24 | Operations |
| PI-SU-CO-734 | BC-11558 | 2021-08-26 | Supply Chain |
| Casein Premium | IC-11561 | 2021-01-24 | Product Management |
| PE-PR-70-PR-387 | TC-11579 | 2023-10-16 | Product Management |
| SIG-83-CDB-3QOI | TC-11581 | 2021-06-16 | Operations |
| MA-DE-146 | IC-11600 | 2021-05-08 | Finance |
| Stellar Materials | BC-11602 | 2022-09-20 | Finance |
| SIG-44-MHK-SRCB | IC-11606 | 2023-09-07 | Finance |
| SIG-66-LJV-5E3H | IC-11608 | 2023-03-13 | Supply Chain |
| sodium benzoate | BC-11612 | 2023-02-10 | Operations |
| Vat Standardqualität BR 15% | TC-11613 | 2021-01-19 | Operations |
| Zitronensäure 50% Qualitätsstufe I | IC-11631 | 2023-12-14 | Compliance |
| Stellar Sourcing | IC-11648 | 2022-11-22 | Product Management |
| SIG-18-LLP-8GUU | TC-11653 | 2022-02-03 | Operations |
| Natriumbenzoat 99.5% Qualitätsstufe I | TC-11657 | 2023-02-10 | Product Management |
| lactic acid tech grade | TC-11663 | 2021-04-16 | Product Management |
| Coconut Oil 98% | IC-11670 | 2024-08-18 | IT Infrastructure |
| SIG-53-AHT-MGFX | IC-11703 | 2023-11-24 | IT Infrastructure |
| SIG-26-WVS-AQ3B | BC-11720 | 2021-07-07 | IT Infrastructure |
| RE-ST-25-TE-177 | TC-11725 | 2022-01-17 | IT Infrastructure |
| Sodium Benzoate 50% | IC-11726 | 2024-11-22 | Finance |
| Atlantic Trading BV | TC-11750 | 2024-10-24 | Product Management |
| Sodium Benzoate 99.5% | IC-11753 | 2024-04-02 | Compliance |
| SIG-86-DMG-XSKY | TC-11760 | 2023-07-17 | Operations |
| SO-CH-TE-304 | BC-11766 | 2022-03-01 | Product Management |
| vertex solutions | BC-11768 | 2024-02-26 | Supply Chain |
| Lactic Acid Lebensmittelrein | TC-11824 | 2021-12-14 | Finance |
| SIG-49-QVY-JMMU | BC-11835 | 2023-03-22 | Data Governance |
| Maltodextrin DE10 | BC-11875 | 2021-12-03 | Finance |
| SIG-84-HFZ-NPNZ | IC-11877 | 2022-02-22 | Operations |
| SIG-46-YOE-MYAX SA | TC-11910 | 2024-06-24 | Operations |
| Sonnenblumenöl Qualitätsstufe I | TC-11913 | 2024-05-09 | IT Infrastructure |
| ascorbic acid | TC-11917 | 2022-11-04 | Operations |
| SO-IS-FO-GR-334 | IC-11918 | 2022-11-17 | IT Infrastructure |
| SO-BE-FO-GR-650 | IC-11932 | 2021-02-16 | Product Management |
| LA-AC-ST-823 | IC-11939 | 2022-09-18 | IT Infrastructure |
| SIG-16-GDL-YC2T LLC | IC-11963 | 2021-01-22 | Operations |
| SIG-22-SKR-CTIC | IC-11967 | 2024-12-08 | IT Infrastructure |
| SO-IS-PR-242 | BC-11977 | 2022-04-01 | Operations |
| Sorbinsäure | BC-11996 | 2021-04-24 | Operations |
| SIG-69-CZY-YXFK | IC-12009 | 2021-10-18 | Supply Chain |
| palm oil pharma grade | BC-12014 | 2022-04-16 | Finance |
| Prime Materials Inc. | IC-12019 | 2023-09-03 | Compliance |
| Sodium Benzoate 99.5% Grade A | TC-12033 | 2021-02-23 | Supply Chain |
| Coconut Oil 70% | IC-12064 | 2024-03-27 | IT Infrastructure |
| SIG-73-OCH-3A8Y | BC-12067 | 2023-03-25 | Compliance |
| SIG-48-BCW-76F8 | TC-12077 | 2023-04-04 | Data Governance |
| Maltodextrin DE5 Food Grade | BC-12093 | 2024-02-10 | Data Governance |
| Ascorbic Acid Lebensmittelrein | IC-12122 | 2022-06-04 | Finance |
| Stellar Partners Ltd. | IC-12123 | 2022-06-03 | Product Management |
| IS-802 | TC-12136 | 2024-04-01 | Operations |
| ST-TR-590 | BC-12140 | 2021-08-09 | IT Infrastructure |
| Rapsöl | BC-12144 | 2023-12-02 | Finance |
| lactic acid standard | BC-12150 | 2022-04-27 | Data Governance |
| Sorbinsäure | IC-12152 | 2023-01-12 | Compliance |
| SIG-68-TVY-N4XJ | TC-12161 | 2021-05-19 | Product Management |
| DE-70-GR-A-741 | TC-12172 | 2023-12-25 | Compliance |
| Dextrin | BC-12182 | 2023-08-28 | Data Governance |
| SO-IS-PR-242 | TC-12184 | 2022-05-15 | Data Governance |
| SIG-35-FKH-6ZOM KG | BC-12187 | 2023-07-03 | Data Governance |
| PA-OI-50-PR-573 | TC-12188 | 2022-04-02 | Data Governance |
| fructose standard | TC-12203 | 2024-08-24 | Product Management |
| Maltodextrin DE5 Grade A | TC-12236 | 2023-11-03 | Supply Chain |
| SO-IS-PR-167 | IC-12243 | 2021-09-03 | Compliance |
| Dextrose 50% | BC-12252 | 2021-07-12 | Product Management |
| CA-580 | BC-12275 | 2023-07-14 | Finance |
| sodium chloride 98% | IC-12278 | 2023-06-03 | IT Infrastructure |
| Isoglucose | TC-12286 | 2024-06-05 | Operations |
| Glukosesirup Syrup | TC-12294 | 2023-03-25 | Finance |
| SIG-80-QOK-BKBF | IC-12323 | 2024-04-19 | Product Management |
| Dextrin 50% | IC-12329 | 2022-08-27 | Operations |
| Weizenklebereiweiß 99.5% Qualitätsstufe I | TC-12340 | 2023-06-23 | Supply Chain |
| Lactic Acid Grade A | BC-12347 | 2023-02-24 | Finance |
| AT-SO-658 | TC-12350 | 2023-11-02 | Finance |
| Elite Sourcing | TC-12353 | 2024-07-19 | Compliance |
| Resistant Starch | TC-12360 | 2024-05-02 | Compliance |
| Sodium Chloride 25% Food Grade | BC-12372 | 2024-02-05 | Data Governance |
| SIG-51-LVQ-VS8Q | TC-12393 | 2023-09-05 | Data Governance |
| Casein | TC-12443 | 2021-02-16 | Compliance |
| SO-BE-25-774 | TC-12447 | 2023-03-12 | Compliance |
| MA-DE-933 | IC-12486 | 2021-09-24 | Compliance |
| Central Materials SARL | BC-12489 | 2022-05-25 | Product Management |
| potassium sorbate | IC-12497 | 2021-05-17 | Operations |
| Fructose Qualitätsstufe II | IC-12511 | 2022-11-21 | Operations |
| Sorbic Acid 50% Grade A | TC-12538 | 2021-07-11 | Compliance |
| Catalyst Enterprise International | IC-12540 | 2021-06-19 | Product Management |
| CO-CO-290 BV | TC-12555 | 2022-08-15 | Compliance |
| SIG-89-PTG-ZQNK | TC-12568 | 2023-02-07 | Operations |
| SIG-87-QRK-668S | BC-12572 | 2024-12-05 | Finance |
| maltodextrin de20 | IC-12587 | 2022-09-17 | Operations |
| EL-SO-163 | IC-12595 | 2023-03-26 | Compliance |
| Calcium Carbonate 98% | BC-12600 | 2023-03-12 | Finance |
| Weizenklebereiweiß | IC-12618 | 2024-11-17 | Product Management |
| Ascorbic Acid Technische Qualität | BC-12649 | 2024-08-09 | Product Management |
| resistant starch 50% | IC-12659 | 2022-01-23 | Operations |
| Lactic Acid | TC-12660 | 2021-11-08 | IT Infrastructure |
| SIG-79-GLS-4ZZ9 | IC-12685 | 2023-04-05 | IT Infrastructure |
| Ascorbic Acid 98% Qualitätsstufe II | TC-12694 | 2024-02-08 | Data Governance |
| Vanguard Supply Co. | BC-12701 | 2021-03-23 | Compliance |
| Potassium Sorbate 98% | TC-12702 | 2023-01-02 | Compliance |
| SIG-70-YBK-DUQ6 | IC-12708 | 2024-09-18 | IT Infrastructure |
| Ascorbic Acid Qualitätsstufe II | TC-12713 | 2022-12-28 | Supply Chain |
| CO-OI-966 | IC-12722 | 2022-01-06 | Operations |
| palm oil 70% tech grade | BC-12729 | 2023-02-23 | Compliance |
| resistant starch 25% tech grade | TC-12735 | 2024-01-20 | Finance |
| horizon materials | TC-12768 | 2023-02-06 | Data Governance |
| SIG-23-PGX-VBNK | BC-12769 | 2023-11-18 | Compliance |
| Lactic Acid | TC-12811 | 2022-11-08 | Finance |
| SIG-35-HUP-NW3M | BC-12816 | 2021-01-18 | IT Infrastructure |
| Palm Oil Food Grade | IC-12832 | 2022-05-28 | Compliance |
| Stratos Processing | IC-12844 | 2021-07-15 | Compliance |
| RA-OI-745 | IC-12853 | 2021-10-20 | Operations |
| isoglucose 25% | TC-12882 | 2022-05-28 | Supply Chain |
| EX-N-19-830 | BC-12885 | 2024-03-18 | Data Governance |
| VE-DI-556 SA | TC-12909 | 2022-10-07 | Product Management |
| NE-DI-555 Corp. | IC-12940 | 2021-04-02 | IT Infrastructure |
| apex chemicals Inc. | BC-12948 | 2021-10-13 | IT Infrastructure |
| SIG-70-KJX-6V9L | IC-12973 | 2023-06-26 | IT Infrastructure |
| EX-D-7-904 | TC-12986 | 2024-04-26 | IT Infrastructure |
| sunflower oil standard | TC-12993 | 2023-12-25 | Compliance |
| Zenith Supply Co. | TC-13018 | 2023-06-04 | Compliance |
| AS-AC-99.5-619 | BC-13032 | 2021-02-15 | Data Governance |
| Quantum Chemicals | BC-13045 | 2024-07-02 | Supply Chain |
| Fructose Grade B | TC-13047 | 2021-02-18 | Finance |
| core processing Group | IC-13050 | 2022-01-01 | IT Infrastructure |
| Maltodextrin-Pulver DE5 Qualitätsstufe I | IC-13051 | 2023-10-18 | Supply Chain |
| SIG-16-GRX-X3AK | IC-13065 | 2022-08-03 | Supply Chain |
| atlantic industries International | IC-13066 | 2022-04-11 | Finance |
| Dextrin | IC-13081 | 2021-11-06 | Product Management |
| SIG-85-WWC-01LO | IC-13085 | 2024-12-10 | Operations |
| Isoglucose 50% Technical | IC-13098 | 2023-11-26 | Finance |
| Premier Vertrieb | BC-13108 | 2024-08-06 | Supply Chain |
| glucose syrup 98% food grade | IC-13136 | 2022-02-10 | Supply Chain |
| RE-ST-FO-GR-998 | IC-13156 | 2024-04-22 | Supply Chain |
| Zenith Trading | TC-13161 | 2021-06-02 | Product Management |
| nexus industries | IC-13218 | 2023-02-02 | Data Governance |
| Calcium Carbonate | TC-13228 | 2024-02-06 | IT Infrastructure |
| SIG-41-HXT-0U1R | BC-13236 | 2023-01-28 | Product Management |
| Catalyst Supply Co. | TC-13254 | 2021-07-28 | Supply Chain |
| PO-SO-GR-A-715 | TC-13261 | 2022-07-25 | Finance |
| Kasein | TC-13266 | 2022-12-07 | Data Governance |
| SIG-98-LSP-BA0T | IC-13267 | 2024-05-23 | Data Governance |
| SO-CH-70-317 | IC-13274 | 2022-11-24 | Finance |
| sodium chloride | BC-13276 | 2022-03-07 | Finance |
| continental supply | IC-13290 | 2022-12-02 | Supply Chain |
| Ascorbic Acid 50% Technische Qualität | IC-13304 | 2024-01-08 | Data Governance |
| Global Verarbeitung GmbH | IC-13305 | 2023-04-14 | Operations |
| Atlas Materials BV | IC-13308 | 2023-02-19 | Compliance |
| SIG-89-FBG-6HKF | BC-13314 | 2024-08-20 | Product Management |
| vat reduced cn 10% | TC-13318 | 2024-02-22 | IT Infrastructure |
| SO-IS-PH-GR-671 | TC-13329 | 2024-05-14 | Finance |
| Soja Isolate Pharmazeutisch rein | BC-13336 | 2023-04-23 | Finance |
| sodium benzoate 99.5% tech grade | IC-13341 | 2022-09-23 | IT Infrastructure |
| RE-ST-50-692 | BC-13348 | 2023-06-14 | Finance |
| continental manufacturing Inc. | BC-13358 | 2022-11-17 | Compliance |
| palm oil tech grade | BC-13365 | 2023-08-23 | Data Governance |
| nexus logistics | IC-13368 | 2022-09-19 | Operations |
| SIG-51-EYN-NILM LLC | TC-13376 | 2024-10-08 | Product Management |
| calcium carbonate 50% | TC-13409 | 2023-08-14 | Data Governance |
| vat standard br 7% | IC-13441 | 2023-05-17 | Data Governance |
| Sorbinsäure 50% | BC-13450 | 2021-12-07 | Compliance |
| SIG-16-FVU-3EBQ | BC-13453 | 2022-10-02 | Compliance |
| SO-AC-98-579 | BC-13455 | 2022-03-15 | Data Governance |
| ST-LO-927 | TC-13461 | 2021-04-04 | IT Infrastructure |
| SIG-73-YMY-EMYO | TC-13492 | 2022-09-13 | Product Management |
| QU-SO-556 | IC-13499 | 2021-07-21 | Data Governance |
| Withholding IN 20% | TC-13510 | 2021-03-25 | Data Governance |
| Fructose 70% | TC-13534 | 2022-03-17 | Finance |
| Dextrin Standardqualität | BC-13547 | 2024-11-07 | Operations |
| Traubenzucker 99.5% Standardqualität | BC-13555 | 2023-02-28 | Product Management |
| pinnacle supply | TC-13557 | 2023-02-16 | IT Infrastructure |
| RE-ST-50-232 | IC-13578 | 2021-01-24 | IT Infrastructure |
| SIG-54-LIP-WKBS | TC-13604 | 2021-03-09 | Operations |
| Natriumchlorid Standardqualität | IC-13610 | 2022-01-02 | Operations |
| SIG-51-IYK-630P | TC-13631 | 2022-05-14 | IT Infrastructure |
| prism industries Group | TC-13634 | 2022-06-25 | Supply Chain |
| SIG-20-XSP-FVHF | TC-13636 | 2024-05-05 | Supply Chain |
| quantum supply | IC-13643 | 2023-08-01 | IT Infrastructure |
| SIG-42-MEI-2SCI | TC-13650 | 2023-01-12 | Compliance |
| SIG-13-CZK-ACKX | IC-13659 | 2024-02-02 | Operations |
| catalyst logistics SA | TC-13662 | 2021-07-06 | Compliance |
| nexus logistics | IC-13666 | 2021-07-03 | Compliance |
| Stratos Ingredients | IC-13669 | 2021-01-06 | Operations |
| prime supply | IC-13675 | 2022-10-05 | Product Management |
| Isoglucose Food Grade | TC-13681 | 2023-07-26 | Finance |
| dextrose food grade | BC-13682 | 2024-05-18 | Compliance |
| Cyclodextrin | IC-13689 | 2023-02-03 | Finance |
| Vanguard Versorgung BV | TC-13693 | 2021-08-15 | Compliance |
| SIG-59-ECO-OXB3 | BC-13697 | 2023-07-20 | Product Management |
| Sodium Chloride Grade B | TC-13705 | 2022-03-22 | Data Governance |
| maltodextrin de5 standard | IC-13732 | 2024-02-13 | Finance |
| SIG-59-CFT-59LL Holdings | TC-13739 | 2023-04-28 | Operations |
| palm oil 50% | TC-13744 | 2021-10-03 | Operations |
| Premier Supply PLC | TC-13748 | 2022-05-03 | Data Governance |
| VA-RE-I-5-890 | IC-13753 | 2024-07-12 | IT Infrastructure |
| Citric Acid Grade B | IC-13760 | 2024-10-17 | Supply Chain |
| LA-AC-50-PR-288 | IC-13763 | 2022-05-03 | Compliance |
| Core Werkstoffe | TC-13781 | 2023-08-12 | IT Infrastructure |
| Zenith Versorgung GmbH | TC-13791 | 2023-12-16 | Compliance |
| Sunflower Oil Grade B | IC-13807 | 2022-12-14 | Finance |
| Atlantic Processing | TC-13812 | 2022-09-13 | Data Governance |
| Traubenzucker Qualitätsstufe I | BC-13824 | 2023-01-23 | Data Governance |
| CO-SU-CO-318 | BC-13826 | 2024-09-12 | IT Infrastructure |
| casein | IC-13838 | 2022-06-27 | IT Infrastructure |
| Lactic Acid 70% Pharma Grade | IC-13873 | 2024-01-27 | Compliance |
| WH-GL-99.5-557 | TC-13888 | 2024-03-26 | Compliance |
| PO-SO-98-216 | IC-13892 | 2022-12-26 | IT Infrastructure |
| Sodium Benzoate 70% | BC-13896 | 2021-04-13 | IT Infrastructure |
| Nordic Versorgung GmbH | IC-13898 | 2023-04-21 | Operations |
| Casein | BC-13900 | 2024-02-11 | Supply Chain |
| Nexus Partners GmbH | BC-13903 | 2022-10-24 | IT Infrastructure |
| Ascorbic Acid 99.5% Technische Qualität | BC-13904 | 2024-01-05 | Data Governance |
| AS-AC-99.5-619 | TC-13913 | 2023-07-12 | Finance |
| SIG-70-HGQ-WORL | TC-13921 | 2021-11-28 | Compliance |
| Wheat Gluten | BC-13930 | 2024-07-24 | Data Governance |
| Atlantic Manufacturing | BC-13969 | 2022-09-18 | Compliance |
| AS-AC-439 | TC-13983 | 2024-03-28 | Finance |
| Core Partners Ltd. | TC-13988 | 2023-01-19 | Compliance |
| glucose syrup | BC-14002 | 2022-11-23 | IT Infrastructure |
| sunflower oil 70% | IC-14007 | 2023-03-10 | Product Management |
| SIG-39-CJT-QHM3 | BC-14010 | 2021-06-08 | Supply Chain |
| vertex materials | TC-14020 | 2022-08-22 | Finance |
| elite trading Ltd. | TC-14031 | 2022-07-08 | Data Governance |
| Stellar Distribution | IC-14037 | 2024-10-15 | Product Management |
| Weizenklebereiweiß Qualitätsstufe II | TC-14040 | 2024-01-04 | Finance |
| PO-SO-50-GR-B-154 | IC-14053 | 2022-06-20 | Product Management |
| PO-SO-339 | BC-14086 | 2024-06-09 | Product Management |
| Calcium Carbonate 50% Pharmazeutisch rein | TC-14115 | 2022-08-02 | Finance |
| Elite Logistik Group | TC-14127 | 2022-11-17 | Compliance |
| ZE-PA-511 PLC | BC-14134 | 2024-08-17 | Finance |
| quantum logistics | IC-14143 | 2021-12-24 | Operations |
| PR-EN-764 Ltd. | IC-14157 | 2022-07-27 | Supply Chain |
| Fructose | IC-14159 | 2022-07-18 | Compliance |
| Rapsöl 50% Qualitätsstufe I | IC-14170 | 2024-07-16 | IT Infrastructure |
| Natriumbenzoat 25% Standardqualität | BC-14175 | 2022-01-02 | Compliance |
| VA-MA-537 Holdings | TC-14194 | 2022-11-04 | Compliance |
| SIG-89-JZC-1682 | TC-14243 | 2022-04-26 | Operations |
| SIG-45-CWR-EI9N | TC-14245 | 2024-08-13 | IT Infrastructure |
| Quantum Ingredients SARL | BC-14260 | 2024-04-07 | Data Governance |
| Nordic Manufacturing NV | IC-14271 | 2024-04-08 | Supply Chain |
| Horizon Sourcing | TC-14282 | 2022-03-12 | Data Governance |
| excise us 15% | IC-14291 | 2021-05-20 | Finance |
| SIG-92-FQX-S1BC | IC-14334 | 2021-09-07 | Supply Chain |
| CO-OI-ST-153 | IC-14350 | 2024-04-05 | Operations |
| Traubenzucker Qualitätsstufe I | BC-14363 | 2022-08-16 | Data Governance |
| SIG-29-LEJ-26GF Group | BC-14383 | 2024-01-07 | Compliance |
| SIG-52-LQX-X1DO | TC-14398 | 2024-10-01 | Operations |
| dextrose premium | TC-14412 | 2024-06-24 | Data Governance |
| Stratos Handel | TC-14415 | 2024-04-06 | Data Governance |
| Stratos Materials | TC-14418 | 2024-09-20 | Product Management |
| Soy Isolate 25% Technical | BC-14420 | 2021-06-22 | Finance |
| SO-IS-25-ST-345 | TC-14422 | 2024-07-23 | Product Management |
| sunflower oil 98% | BC-14426 | 2024-02-19 | IT Infrastructure |
| SIG-59-HZI-WDX6 Group | IC-14434 | 2022-02-19 | Supply Chain |
| maltodextrin de5 standard | BC-14442 | 2024-10-04 | Data Governance |
| SIG-57-YNC-H4UX | BC-14449 | 2022-03-15 | Supply Chain |
| Glukosesirup Syrup | BC-14458 | 2024-10-22 | Operations |
| lactic acid standard | IC-14465 | 2021-01-01 | Supply Chain |
| Sunflower Oil Standard | BC-14492 | 2021-06-20 | Operations |
| Resistant Starch Standard | IC-14497 | 2022-12-11 | IT Infrastructure |
| Resistente Stärke Technische Qualität | IC-14512 | 2023-06-01 | Finance |
| SIG-73-AXY-5E8O | BC-14515 | 2021-06-02 | IT Infrastructure |
| zenith logistics | IC-14535 | 2023-07-20 | Operations |
| prime commodities | BC-14538 | 2024-10-25 | IT Infrastructure |
| Global Versorgung GmbH | IC-14554 | 2021-02-22 | Data Governance |
| SIG-19-JRR-02SD | IC-14562 | 2021-08-10 | Supply Chain |
| soy isolate pharma grade | TC-14565 | 2021-08-24 | Finance |
| Ascorbic Acid 99.5% | IC-14567 | 2023-11-10 | Product Management |
| Excise US 7% | TC-14598 | 2021-11-12 | Operations |
| EL-SO-199 | TC-14609 | 2023-10-06 | Supply Chain |
| SIG-57-NGZ-ILDZ | BC-14613 | 2022-06-09 | Supply Chain |
| Lactic Acid 50% Premium | TC-14655 | 2021-07-03 | Finance |
| CA-CA-GR-B-162 | TC-14677 | 2024-12-15 | Product Management |
| casein pharma grade | IC-14680 | 2022-09-25 | Product Management |
| sunflower oil standard | IC-14705 | 2021-10-26 | IT Infrastructure |
| casein 98% premium | BC-14719 | 2023-04-25 | Operations |
| Ascorbic Acid 98% Premium | TC-14723 | 2022-11-14 | Operations |
| AS-AC-GR-B-395 | IC-14749 | 2021-08-25 | Operations |
| fructose premium | BC-14768 | 2023-05-17 | Data Governance |
| Sonnenblumenöl 98% Premiumqualität | TC-14779 | 2023-02-15 | Supply Chain |
| SIG-92-SMV-JF74 | IC-14788 | 2023-12-15 | Data Governance |
| customs duty br 7% | BC-14795 | 2023-11-28 | Supply Chain |
| vanguard supply NV | TC-14796 | 2021-11-23 | Supply Chain |
| citric acid standard | IC-14798 | 2022-02-09 | Compliance |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | TC-14800 | 2024-01-23 | Operations |
| ascorbic acid standard | BC-14806 | 2022-08-02 | Data Governance |
| Kaliumsorbat Technische Qualität | BC-14829 | 2024-11-26 | Finance |
| Pacific Materials | TC-14837 | 2022-06-07 | IT Infrastructure |
| SIG-70-MMO-95UC | TC-14856 | 2023-03-26 | IT Infrastructure |
| SIG-51-MVX-XKUB | IC-14859 | 2023-09-23 | Operations |
| Calcium Carbonate 70% Premium | IC-14867 | 2024-07-27 | Finance |
| Core Logistics | IC-14879 | 2024-05-14 | Product Management |
| SIG-32-DNR-U0SL | TC-14895 | 2023-06-13 | IT Infrastructure |
| Sorbinsäure Qualitätsstufe II | TC-14902 | 2023-06-20 | Finance |
| PA-OI-70-780 | TC-14903 | 2021-10-02 | Operations |
| BA-SU-CO-430 | BC-14912 | 2022-12-20 | Data Governance |
| Glukosesirup Syrup 70% Lebensmittelrein | TC-14923 | 2021-03-19 | Data Governance |
| Lactic Acid Qualitätsstufe II | BC-14928 | 2022-10-25 | Data Governance |
| SU-OI-251 | BC-14929 | 2024-02-25 | Operations |
| SIG-48-GDK-Y8XN | BC-14945 | 2022-07-28 | Product Management |
| SIG-40-YZP-9CC3 | IC-14950 | 2023-01-20 | IT Infrastructure |
| AT-LO-132 | TC-14959 | 2023-12-12 | Operations |
| Palmfett | TC-14975 | 2023-03-24 | Compliance |
| Atlas Sourcing | TC-14978 | 2021-02-17 | Data Governance |
| SIG-93-DAB-6LKS | BC-15005 | 2023-07-28 | Supply Chain |
| meridian materials | TC-15018 | 2021-06-12 | Compliance |
| Glukosesirup Syrup Technische Qualität | BC-15034 | 2022-12-09 | Compliance |
| Resistente Stärke 70% | IC-15050 | 2022-06-03 | Supply Chain |
| DE-TE-340 | IC-15057 | 2023-06-16 | Finance |
| premier solutions Corp. | IC-15065 | 2023-11-24 | Finance |
| Natriumbenzoat 50% Technische Qualität | IC-15083 | 2022-07-17 | Operations |
| AS-AC-99.5-TE-765 | IC-15085 | 2022-02-16 | IT Infrastructure |
| pinnacle sourcing | IC-15086 | 2024-11-19 | Finance |
| Central Werkstoffe | BC-15117 | 2021-11-16 | Data Governance |
| Pinnacle Chemicals PLC | BC-15119 | 2022-10-15 | Operations |
| VA-RE-I-20-892 | TC-15131 | 2021-04-02 | Product Management |
| MA-DE-951 | TC-15135 | 2023-11-20 | Finance |
| SIG-43-GRJ-P3HT | BC-15143 | 2022-06-11 | Finance |
| Nordic Ingredients | IC-15153 | 2021-09-23 | Compliance |
| Sorbic Acid Standard | BC-15180 | 2023-01-08 | Supply Chain |
| SIG-95-HRL-AO5O | TC-15185 | 2021-08-01 | Operations |
| Premier Partners Group | BC-15187 | 2023-09-07 | Data Governance |
| NO-IN-155 SA | IC-15211 | 2024-01-03 | Finance |
| Fructose 99.5% Technical | IC-15231 | 2024-02-28 | Compliance |
| Sonnenblumenöl Standardqualität | IC-15248 | 2021-02-10 | Finance |
| Stratos Materials Group | TC-15288 | 2021-10-01 | IT Infrastructure |
| Citric Acid | TC-15293 | 2024-03-16 | Data Governance |
| Rapsöl 50% Pharmazeutisch rein | IC-15299 | 2024-07-05 | Finance |
| CA-CA-99.5-FO-GR-839 | BC-15301 | 2024-11-25 | Compliance |
| Fructose 98% Premiumqualität | IC-15302 | 2022-07-23 | Product Management |
| CA-LO-415 | IC-15314 | 2022-05-23 | Finance |
| SIG-24-OUE-RXOK | TC-15339 | 2023-11-05 | Supply Chain |
| sodium benzoate 98% pharma grade | IC-15344 | 2023-10-25 | Product Management |
| AT-SU-CO-945 | TC-15354 | 2024-08-17 | Supply Chain |
| Ascorbic Acid Standard | TC-15365 | 2022-03-18 | Product Management |
| vertex commodities KG | TC-15382 | 2023-03-24 | Compliance |
| Apex Werkstoffe | BC-15400 | 2022-08-22 | Compliance |
| Quantum Materials | TC-15412 | 2021-01-15 | Data Governance |
| SIG-13-DJH-ML2N | IC-15413 | 2021-12-28 | Operations |
| SIG-75-PHG-NW65 | IC-15420 | 2021-08-18 | Compliance |
| Withholding NL 7% | TC-15427 | 2024-02-06 | IT Infrastructure |
| wheat gluten standard | BC-15429 | 2024-02-02 | Supply Chain |
| SIG-60-GZP-BB7N NV | TC-15442 | 2022-03-27 | IT Infrastructure |
| central partners Inc. | IC-15449 | 2021-01-07 | Data Governance |
| Apex Logistik | BC-15455 | 2024-05-19 | Finance |
| Palm Oil 50% | BC-15457 | 2022-07-11 | Product Management |
| pacific materials | TC-15489 | 2021-11-13 | Compliance |
| SIG-56-JML-GDXB | IC-15522 | 2023-01-14 | Supply Chain |
| sorbic acid 25% standard | BC-15523 | 2023-04-18 | IT Infrastructure |
| SIG-56-LHF-WMFP | BC-15530 | 2022-09-24 | Supply Chain |
| Sodium Benzoate | IC-15531 | 2023-03-22 | Supply Chain |
| CI-AC-70-265 | BC-15536 | 2021-11-17 | Data Governance |
| Vat Reduced NL 25% | BC-15539 | 2024-06-03 | Compliance |
| glucose syrup | TC-15556 | 2022-03-27 | Product Management |
| Withholding FR 5% | BC-15585 | 2023-09-16 | IT Infrastructure |
| SIG-90-NFZ-XRLG | TC-15603 | 2022-02-21 | Data Governance |
| SO-CH-354 | TC-15604 | 2021-11-10 | Compliance |
| Customs Duty DE 5% | IC-15607 | 2021-06-27 | Operations |
| quantum trading Holdings | IC-15610 | 2022-09-17 | Supply Chain |
| IS-50-GR-A-791 | BC-15612 | 2024-05-02 | Supply Chain |
| Coconut Oil 99.5% Pharmazeutisch rein | BC-15623 | 2023-01-11 | Supply Chain |
| Vat Standard IN 0% | TC-15625 | 2024-09-07 | Product Management |
| SIG-80-QOK-BKBF | BC-15653 | 2023-12-01 | Supply Chain |
| SO-AC-FO-GR-175 | IC-15679 | 2023-06-12 | IT Infrastructure |
| resistant starch standard | IC-15692 | 2023-07-28 | Product Management |
| pea protein pharma grade | TC-15693 | 2021-08-24 | Compliance |
| PR-PR-135 KG | TC-15706 | 2021-02-02 | Finance |
| AT-LO-927 Holdings | IC-15728 | 2023-07-04 | Supply Chain |
| vat reduced nl 20% | IC-15732 | 2023-10-16 | IT Infrastructure |
| vertex materials | TC-15746 | 2022-08-19 | Finance |
| Central Versorgung GmbH | BC-15761 | 2024-02-11 | Data Governance |
| wheat gluten standard | TC-15768 | 2024-03-23 | Operations |
| Core Partners Ltd. | TC-15841 | 2022-06-08 | Product Management |
| SIG-84-HBF-DDQL | BC-15859 | 2023-08-01 | Data Governance |
| citric acid | IC-15865 | 2022-09-14 | Compliance |
| CA-CA-GR-B-761 | IC-15893 | 2023-06-07 | Data Governance |
| Withholding GB 5% | BC-15896 | 2021-03-21 | Supply Chain |
| dextrin 70% pharma grade | BC-15918 | 2023-09-27 | IT Infrastructure |
| SIG-86-PYU-PCGN | BC-15921 | 2022-05-17 | Data Governance |
| Sorbic Acid 25% Pharma Grade | TC-15932 | 2023-07-21 | Data Governance |
| sorbic acid premium | IC-15940 | 2024-07-21 | Data Governance |
| ascorbic acid food grade | BC-15964 | 2023-06-18 | Product Management |
| SIG-52-CHY-4N5P | TC-15968 | 2022-06-09 | Operations |
| AT-CH-900 AG | IC-15992 | 2021-07-23 | IT Infrastructure |
| Resistant Starch 50% Standard | TC-15998 | 2023-06-04 | Data Governance |
| SU-OI-GR-B-259 | IC-15999 | 2024-11-23 | Finance |
| SIG-69-FIT-Y3OC International | TC-16001 | 2022-07-19 | IT Infrastructure |
| SIG-50-NZZ-E4UN | TC-16006 | 2022-06-25 | IT Infrastructure |
| Calcium Carbonate 98% Standard | IC-16032 | 2024-01-25 | Data Governance |
| continental ingredients | TC-16034 | 2021-10-23 | Product Management |
| elite trading Group | BC-16036 | 2021-06-02 | IT Infrastructure |
| Glukosesirup Syrup | BC-16051 | 2024-12-06 | Data Governance |
| SIG-66-FRL-CVIT | BC-16053 | 2021-05-20 | Data Governance |
| Meridian Versorgung GmbH | IC-16069 | 2022-04-25 | Operations |
| sunflower oil premium | IC-16078 | 2021-07-08 | Finance |
| SIG-71-FNO-CX9K | TC-16087 | 2022-02-23 | Product Management |
| Calcium Carbonate Standardqualität | BC-16096 | 2022-12-25 | Supply Chain |
| Central Enterprise | BC-16100 | 2023-07-14 | Product Management |
| MA-DE-859 | IC-16101 | 2024-12-20 | IT Infrastructure |
| SIG-61-CIV-LFWA | IC-16112 | 2023-04-18 | Operations |
| SIG-51-HOK-PC9S Holdings | IC-16116 | 2021-08-17 | Operations |
| stellar logistics | IC-16141 | 2023-04-22 | Product Management |
| Traubenzucker Qualitätsstufe I | BC-16147 | 2021-03-04 | Finance |
| SIG-64-BPY-A8RD | BC-16154 | 2022-12-24 | Product Management |
| Kaliumsorbat | BC-16161 | 2024-12-17 | IT Infrastructure |
| Atlas Logistik International | TC-16184 | 2023-02-18 | IT Infrastructure |
| SO-CH-115 | BC-16186 | 2023-12-26 | Operations |
| Sodium Chloride 25% Food Grade | TC-16192 | 2023-12-26 | Product Management |
| FR-124 | BC-16210 | 2023-04-26 | Operations |
| SIG-81-AMW-NE5V | TC-16219 | 2022-08-09 | Data Governance |
| SIG-62-BTJ-PQV9 | BC-16223 | 2022-11-16 | Data Governance |
| maltodextrin de20 | BC-16242 | 2023-02-13 | Finance |
| SIG-78-WKT-9TDY SAS | BC-16250 | 2021-07-14 | Operations |
| Palm Oil 50% | BC-16258 | 2021-02-26 | Compliance |
| ST-DI-183 Inc. | IC-16260 | 2021-08-13 | Finance |
| Core Werkstoffe | BC-16272 | 2024-05-23 | IT Infrastructure |
| Withholding NL 7% | BC-16287 | 2022-10-16 | IT Infrastructure |
| RE-ST-50-526 | IC-16295 | 2023-07-24 | Product Management |
| Dextrin Food Grade | TC-16306 | 2022-02-01 | IT Infrastructure |
| SIG-66-ZOH-E8TV | TC-16312 | 2021-07-23 | Product Management |
| Nexus Partners Group | IC-16317 | 2021-07-13 | Data Governance |
| SIG-48-DTM-5XF3 Corp. | BC-16323 | 2021-01-24 | IT Infrastructure |
| SIG-12-OAV-ALF4 | BC-16329 | 2022-04-14 | Finance |
| ascorbic acid pharma grade | BC-16333 | 2024-08-03 | IT Infrastructure |
| EX-N-21-216 | BC-16344 | 2023-12-12 | Data Governance |
| Ascorbic Acid 50% | IC-16345 | 2021-02-13 | Supply Chain |
| elite trading | TC-16348 | 2022-06-19 | Compliance |
| lactic acid standard | TC-16357 | 2024-10-10 | Finance |
| CO-OI-GR-A-370 | TC-16364 | 2024-02-19 | Compliance |
| IS-FO-GR-335 | TC-16367 | 2021-04-15 | Data Governance |
| SIG-70-MMO-95UC | TC-16374 | 2022-01-03 | Compliance |
| Pinnacle Materials | TC-16378 | 2023-06-05 | Operations |
| Pea Protein Premiumqualität | IC-16399 | 2023-10-04 | Finance |
| Lactic Acid Food Grade | TC-16403 | 2023-10-03 | Finance |
| GL-SY-70-549 | IC-16408 | 2022-04-10 | IT Infrastructure |
| potassium sorbate standard | TC-16421 | 2022-03-09 | Operations |
| soy isolate | BC-16437 | 2022-09-28 | Operations |
| Continental Chemicals Inc. | TC-16445 | 2022-07-09 | Compliance |
| PR-CH-565 SAS | TC-16476 | 2022-06-10 | Product Management |
| Potassium Sorbate Food Grade | TC-16503 | 2021-05-05 | IT Infrastructure |
| Lactic Acid Food Grade | IC-16507 | 2021-09-01 | Finance |
| SIG-72-FHF-DYSG | TC-16524 | 2021-02-26 | IT Infrastructure |
| Soy Isolate 25% Technical | IC-16533 | 2022-04-07 | Compliance |
| core partners BV | TC-16552 | 2024-03-22 | Finance |
| Sorbinsäure 50% Standardqualität | TC-16557 | 2022-04-01 | Data Governance |
| SIG-79-RTU-R8IQ | TC-16563 | 2023-07-26 | Data Governance |
| Natriumbenzoat 99.5% Qualitätsstufe I | TC-16573 | 2024-02-21 | IT Infrastructure |
| Cyclodextrin Lebensmittelrein | TC-16580 | 2023-12-11 | Operations |
| AS-AC-GR-B-855 | IC-16585 | 2022-12-27 | Operations |
| SO-BE-99.5-TE-213 | IC-16620 | 2022-08-05 | IT Infrastructure |
| SIG-68-DWS-MNR6 | BC-16625 | 2024-01-20 | Data Governance |
| Dextrin Technical | IC-16635 | 2024-04-10 | Data Governance |
| SIG-60-OHC-5EQB | IC-16642 | 2023-01-08 | Operations |
| excise in 20% | TC-16664 | 2024-05-20 | Product Management |
| SIG-67-MJH-V4Q5 | IC-16666 | 2024-09-22 | Product Management |
| Kasein Premiumqualität | BC-16675 | 2024-11-14 | Supply Chain |
| Ascorbic Acid Lebensmittelrein | BC-16680 | 2024-01-16 | Finance |
| SIG-63-MSP-S6JE | TC-16689 | 2024-01-11 | Data Governance |
| Nexus Werkstoffe | IC-16708 | 2024-03-11 | IT Infrastructure |
| Dextrose 25% | BC-16711 | 2023-12-20 | Operations |
| global distribution | TC-16737 | 2023-07-06 | Compliance |
| SIG-93-MGK-61BG | TC-16740 | 2022-09-03 | Product Management |
| CO-OI-25-TE-157 | TC-16745 | 2021-09-09 | Finance |
| Vertex Logistics | BC-16761 | 2024-12-21 | Data Governance |
| VA-RE-C-10-444 | TC-16767 | 2024-09-03 | Operations |
| SIG-92-AXW-GPAG | TC-16774 | 2021-08-20 | Data Governance |
| SIG-66-MYF-XDYQ | BC-16800 | 2021-03-26 | Supply Chain |
| Zenith Logistics | BC-16806 | 2022-08-21 | Supply Chain |
| SIG-86-XWS-MOPG Corp. | BC-16836 | 2024-11-08 | Finance |
| Lactic Acid | IC-16844 | 2023-09-02 | Supply Chain |
| Palmfett 50% | TC-16846 | 2021-07-20 | Finance |
| Vat Standardqualität US 21% | BC-16853 | 2024-07-22 | Finance |
| SIG-68-BSB-VSIA | BC-16862 | 2022-03-08 | Product Management |
| Rapsöl 70% Premiumqualität | IC-16866 | 2024-09-17 | Product Management |
| Vanguard Handel LLC | TC-16873 | 2023-04-26 | Finance |
| SIG-62-NKL-SM8R | IC-16896 | 2022-02-21 | Finance |
| Pinnacle Chemicals Ltd. | BC-16906 | 2024-05-18 | Compliance |
| dextrin | BC-16917 | 2023-10-14 | Product Management |
| Vat Reduced BR 21% | IC-16919 | 2022-01-10 | IT Infrastructure |
| SIG-64-IEU-FRGN | IC-16925 | 2022-08-18 | IT Infrastructure |
| Sorbic Acid Food Grade | IC-16932 | 2022-11-10 | Operations |
| Sodium Benzoate 99.5% Technical | BC-16934 | 2024-05-04 | IT Infrastructure |
| Isoglucose Qualitätsstufe II | TC-16938 | 2023-11-26 | Supply Chain |
| nexus sourcing | TC-16941 | 2022-12-19 | Product Management |
| Ascorbic Acid 70% | TC-16943 | 2021-07-10 | Product Management |
| Isoglucose Qualitätsstufe II | IC-16948 | 2021-10-28 | Compliance |
| Pinnacle Industries SAS | BC-16952 | 2021-12-05 | Compliance |
| Kaliumsorbat Qualitätsstufe II | TC-16956 | 2024-12-07 | Product Management |
| SIG-17-LVE-03G9 | IC-16968 | 2024-08-21 | Product Management |
| Natriumchlorid 98% Pharmazeutisch rein | BC-16984 | 2021-09-22 | Product Management |
| Ascorbic Acid | BC-16989 | 2022-09-04 | Supply Chain |
| SIG-86-VCP-SVOL | IC-16991 | 2021-12-01 | Data Governance |
| Maltodextrin-Pulver DE15 Standardqualität | IC-16999 | 2021-12-14 | IT Infrastructure |
| RA-OI-FO-GR-269 | BC-17009 | 2022-03-10 | Compliance |
| SIG-99-AYV-D18J International | IC-17022 | 2023-04-02 | Supply Chain |
| SIG-88-RGQ-WZOI | TC-17030 | 2021-02-10 | Data Governance |
| pacific logistics Holdings | TC-17037 | 2021-05-17 | Compliance |
| SIG-73-AXD-XIX9 | BC-17065 | 2024-12-06 | Data Governance |
| Glucose Syrup 98% | IC-17086 | 2022-01-08 | Supply Chain |
| Sodium Benzoate | BC-17091 | 2024-01-15 | Supply Chain |
| Resistant Starch | TC-17096 | 2022-10-09 | Product Management |
| Continental Manufacturing Inc. | TC-17121 | 2022-05-17 | Supply Chain |
| Citric Acid | IC-17135 | 2021-03-08 | Supply Chain |
| Weizenklebereiweiß Qualitätsstufe I | TC-17141 | 2024-09-16 | Supply Chain |
| Ascorbic Acid 50% Technische Qualität | BC-17143 | 2023-02-23 | IT Infrastructure |
| Fructose 99.5% Technical | TC-17146 | 2022-05-12 | Product Management |
| Vertex Logistik | TC-17162 | 2023-03-16 | IT Infrastructure |
| Rapeseed Oil | IC-17178 | 2022-04-10 | Supply Chain |
| Stellar Versorgung GmbH | IC-17186 | 2024-02-20 | Finance |
| palm oil food grade | TC-17214 | 2022-12-24 | IT Infrastructure |
| CY-PR-796 | IC-17232 | 2024-05-14 | Supply Chain |
| SIG-79-OZQ-4I2N | TC-17296 | 2022-03-27 | Compliance |
| Maltodextrin-Pulver DE10 Premiumqualität | TC-17297 | 2022-06-01 | Product Management |
| Vat Reduced NL 25% | TC-17309 | 2023-12-09 | IT Infrastructure |
| SIG-33-IHK-2GVW | TC-17347 | 2021-09-10 | Finance |
| SIG-44-UIE-SASC | BC-17351 | 2023-07-11 | Product Management |
| Palm Oil | BC-17355 | 2022-12-18 | Product Management |
| SIG-38-CEJ-1ISY | BC-17365 | 2021-10-27 | IT Infrastructure |
| SIG-18-WKH-NATG | TC-17373 | 2024-01-01 | Supply Chain |
| pinnacle logistics | IC-17379 | 2021-05-21 | Finance |
| Maltodextrin-Pulver DE10 | BC-17384 | 2021-06-01 | Operations |
| CA-MA-129 | IC-17389 | 2024-09-20 | IT Infrastructure |
| PA-SU-CO-173 | BC-17390 | 2024-10-23 | Compliance |
| ST-SO-965 | IC-17424 | 2021-03-17 | Compliance |
| Calcium Carbonate 98% Pharmazeutisch rein | TC-17428 | 2021-11-02 | IT Infrastructure |
| central materials | IC-17429 | 2022-08-27 | Finance |
| PR-CH-314 Group | TC-17438 | 2021-09-15 | Data Governance |
| zenith industries | IC-17453 | 2021-01-22 | IT Infrastructure |
| SU-OI-TE-705 | IC-17472 | 2021-10-28 | Product Management |
| Vat Standard GB 19% | IC-17475 | 2021-04-23 | Compliance |
| vanguard partners Ltd. | IC-17477 | 2024-08-24 | IT Infrastructure |
| VA-RE-F-25-707 | IC-17491 | 2024-09-28 | Operations |
| citric acid premium | IC-17505 | 2022-01-08 | Supply Chain |
| SIG-48-ASO-8G0Y | IC-17506 | 2021-01-20 | Supply Chain |
| Lactic Acid 70% Pharmazeutisch rein | IC-17515 | 2022-07-20 | Finance |
| Fructose | BC-17521 | 2024-11-10 | Finance |
| SO-AC-FO-GR-175 | TC-17536 | 2022-09-16 | Supply Chain |
| Pacific Sourcing | BC-17540 | 2021-10-04 | Data Governance |
| SIG-27-DQT-IQ97 | BC-17550 | 2023-08-15 | IT Infrastructure |
| rapeseed oil 98% | IC-17558 | 2023-09-17 | Operations |
| SO-AC-50-ST-563 | BC-17565 | 2021-02-25 | Supply Chain |
| fructose | IC-17610 | 2022-06-05 | Finance |
| Resistente Stärke 70% Lebensmittelrein | IC-17625 | 2022-10-27 | Product Management |
| CE-MA-338 | IC-17638 | 2023-05-17 | Supply Chain |
| Prime Partners | IC-17655 | 2021-04-15 | IT Infrastructure |
| nexus partners Group | IC-17659 | 2022-12-02 | Compliance |
| Withholding NL 21% | TC-17667 | 2022-11-25 | Compliance |
| Atlas Trading SA | IC-17691 | 2023-11-06 | Operations |
| Rapeseed Oil Technical | TC-17696 | 2022-05-01 | Supply Chain |
| Horizon Supply Co. | TC-17698 | 2024-01-19 | Compliance |
| PE-PR-TE-718 | BC-17703 | 2023-12-02 | Compliance |
| Calcium Carbonate 99.5% | TC-17706 | 2024-07-19 | Compliance |
| SIG-91-UWU-GPZB | IC-17717 | 2024-04-17 | Finance |
| Soy Isolate Grade A | TC-17753 | 2024-02-10 | Compliance |
| SIG-47-SRN-QNYY | IC-17766 | 2021-04-01 | Operations |
| Fructose | IC-17790 | 2022-07-15 | Operations |
| Quantum Supply Co. | TC-17819 | 2022-06-01 | Operations |
| Resistente Stärke 50% | BC-17824 | 2024-04-26 | IT Infrastructure |
| Dextrin Lebensmittelrein | TC-17825 | 2022-07-21 | Supply Chain |
| SIG-81-EUR-UFA2 | IC-17827 | 2021-07-05 | Supply Chain |
| FR-ST-953 | IC-17836 | 2024-12-09 | IT Infrastructure |
| NO-LO-302 | TC-17837 | 2022-07-11 | Operations |
| Glukosesirup Syrup | TC-17858 | 2022-01-21 | IT Infrastructure |
| Customs Duty DE 0% | TC-17871 | 2023-06-19 | Supply Chain |
| Coconut Oil 98% | BC-17883 | 2021-11-03 | Compliance |
| pinnacle ingredients GmbH | TC-17886 | 2021-01-11 | Data Governance |
| SIG-75-WDP-0BHF | BC-17890 | 2022-04-03 | Supply Chain |
| Quantum Handel Ltd. | TC-17898 | 2024-09-11 | Compliance |
| Central Logistics | IC-17901 | 2022-10-09 | Data Governance |
| sorbic acid 98% | TC-17926 | 2023-09-08 | Finance |
| AP-SO-576 | BC-17936 | 2022-06-04 | IT Infrastructure |
| SIG-46-SVJ-5IZO | TC-17947 | 2021-10-05 | Supply Chain |
| Soja Isolate 99.5% | TC-17964 | 2023-04-02 | Product Management |
| Dextrose | IC-17966 | 2024-01-27 | Finance |
| SIG-43-XDN-7VEU | BC-17970 | 2023-03-17 | Operations |
| Vanguard Supply Co. | IC-17975 | 2023-11-01 | Data Governance |
| sodium benzoate 99.5% tech grade | IC-17986 | 2021-10-23 | Compliance |
| GL-SU-CO-128 | TC-17991 | 2021-12-19 | Finance |
| Pinnacle Chemicals SA | IC-17993 | 2021-01-28 | IT Infrastructure |
| SIG-18-PCA-V46E | IC-18005 | 2022-04-25 | IT Infrastructure |
| Sorbinsäure | BC-18007 | 2022-03-15 | Supply Chain |
| central logistics Group | BC-18012 | 2021-12-27 | Data Governance |
| ST-DI-183 Inc. | TC-18022 | 2024-01-20 | Finance |
| Natriumchlorid Technische Qualität | TC-18062 | 2021-05-10 | Supply Chain |
| Nexus Logistik | BC-18075 | 2022-04-14 | Compliance |
| Coconut Oil 98% Technische Qualität | TC-18088 | 2023-06-11 | Data Governance |
| Fructose Pharmazeutisch rein | TC-18089 | 2023-09-02 | Compliance |
| SIG-81-EKU-R7CX Group | BC-18097 | 2023-05-11 | Operations |
| Pacific Enterprise International | IC-18098 | 2022-01-14 | Finance |
| SO-BE-98-PH-GR-434 | BC-18105 | 2023-07-12 | IT Infrastructure |
| isoglucose 70% | TC-18108 | 2024-11-04 | Product Management |
| pea protein 99.5% | IC-18109 | 2022-03-18 | Finance |
| FR-GR-B-231 | TC-18134 | 2022-12-13 | Supply Chain |
| Traubenzucker 25% | IC-18152 | 2024-04-27 | Finance |
| Apex Handel | BC-18165 | 2024-11-02 | Supply Chain |
| Apex Chemicals | BC-18166 | 2021-08-27 | Product Management |
| SIG-98-ZFI-37SU | BC-18169 | 2021-09-15 | IT Infrastructure |
| Resistente Stärke Pharmazeutisch rein | TC-18181 | 2022-01-04 | Data Governance |
| Casein 98% Technical | TC-18183 | 2024-08-16 | Data Governance |
| resistant starch standard | TC-18186 | 2022-03-25 | Data Governance |
| sorbic acid | BC-18212 | 2022-10-25 | Operations |
| EX-U-15-972 | IC-18225 | 2021-03-05 | IT Infrastructure |
| Vanguard Chemicals SAS | BC-18252 | 2023-10-26 | Data Governance |
| SIG-74-LEZ-GZA2 AG | TC-18263 | 2023-12-18 | Data Governance |
| SIG-26-KHF-99OH | TC-18266 | 2023-11-13 | Data Governance |
| Traubenzucker 25% | BC-18322 | 2023-01-14 | Finance |
| SIG-32-NVJ-H1RC | TC-18326 | 2022-05-12 | Operations |
| Traubenzucker Standardqualität | IC-18338 | 2024-07-17 | Operations |
| Prism Manufacturing LLC | TC-18346 | 2021-02-25 | Finance |
| SIG-59-HVI-BACX Group | IC-18351 | 2021-10-18 | Product Management |
| Elite Handel PLC | IC-18354 | 2024-11-12 | Compliance |
| SIG-47-LPF-7QXJ | TC-18382 | 2022-12-28 | Supply Chain |
| pinnacle logistics | TC-18394 | 2024-08-16 | Operations |
| VA-RE-C-21-484 | IC-18397 | 2021-03-05 | Data Governance |
| Weizenklebereiweiß 98% Premiumqualität | TC-18402 | 2022-02-11 | Data Governance |
| Withholding NL 10% | IC-18418 | 2021-04-20 | Supply Chain |
| Apex Werkstoffe | IC-18428 | 2023-03-12 | Finance |
| SIG-49-OHU-U248 | TC-18438 | 2024-03-12 | Operations |
| Fructose 99.5% Technical | TC-18441 | 2024-09-13 | Finance |
| Vertex Distribution AG | BC-18447 | 2023-02-01 | Product Management |
| LA-AC-690 | TC-18486 | 2022-04-24 | Data Governance |
| Glukosesirup Syrup | IC-18490 | 2021-06-25 | Supply Chain |
| CO-OI-98-TE-864 | IC-18492 | 2021-11-20 | Finance |
| Dextrin | TC-18495 | 2022-01-07 | Finance |
| RE-ST-575 | TC-18505 | 2021-03-15 | Operations |
| Sodium Chloride | IC-18514 | 2022-08-09 | IT Infrastructure |
| sorbic acid | IC-18540 | 2022-05-19 | IT Infrastructure |
| Coconut Oil 98% Grade A | TC-18548 | 2024-09-06 | Compliance |
| SO-CH-98-GR-B-961 | TC-18550 | 2023-01-08 | Compliance |
| SIG-23-NOR-OPI3 | IC-18552 | 2024-03-18 | Finance |
| Kaliumsorbat | TC-18556 | 2021-12-22 | Supply Chain |
| Rapeseed Oil Technical | BC-18574 | 2024-04-17 | Operations |
| Vertex Industrien NV | BC-18584 | 2022-09-13 | Operations |
| SIG-94-OAX-GACW Ltd. | BC-18607 | 2022-11-18 | Supply Chain |
| Horizon Sourcing | BC-18643 | 2024-03-26 | Product Management |
| SIG-42-IEF-RFC9 | IC-18646 | 2024-07-18 | Data Governance |
| SIG-14-GCI-G4Q9 | TC-18686 | 2022-12-13 | Operations |
| Glucose Syrup | TC-18713 | 2024-08-03 | Supply Chain |
| Customs Duty US 20% | BC-18726 | 2021-09-19 | Data Governance |
| Prism Industrien International | BC-18754 | 2022-06-12 | Data Governance |
| Resistente Stärke Technische Qualität | BC-18764 | 2024-02-13 | Supply Chain |
| WI-U-19-722 | IC-18817 | 2023-08-22 | Finance |
| dextrin 70% pharma grade | BC-18874 | 2023-11-10 | Data Governance |
| Horizon Logistik | IC-18876 | 2021-08-21 | Operations |
| Casein Grade B | TC-18891 | 2024-08-16 | IT Infrastructure |
| SIG-50-TGM-XVD2 | IC-18905 | 2021-05-17 | Compliance |
| WI-I-21-324 | BC-18913 | 2023-01-06 | Operations |
| SIG-22-XCC-QSNV | IC-18914 | 2023-07-16 | Operations |
| meridian materials | IC-18924 | 2021-07-07 | Operations |
| Dextrin 70% Pharma Grade | IC-18933 | 2024-09-05 | Compliance |
| Cyclodextrin 98% Premiumqualität | TC-18953 | 2021-03-12 | IT Infrastructure |
| SO-IS-GR-A-940 | BC-18977 | 2023-12-28 | Compliance |
| Weizenklebereiweiß Pharmazeutisch rein | IC-18978 | 2022-08-28 | Data Governance |
| Catalyst Commodities GmbH | IC-18981 | 2024-05-16 | Product Management |
| RA-OI-25-FO-GR-818 | BC-19033 | 2021-01-21 | Operations |
| Fructose | BC-19047 | 2022-05-10 | Product Management |
| PR-SO-362 | BC-19049 | 2024-06-02 | Supply Chain |
| Sorbic Acid Grade B | TC-19069 | 2021-11-05 | Compliance |
| ME-LO-731 | IC-19087 | 2023-01-20 | Operations |
| AS-AC-TE-342 | BC-19089 | 2022-09-23 | Compliance |
| Stratos Ingredients | IC-19091 | 2023-02-23 | IT Infrastructure |
| Withholding CN 0% | BC-19110 | 2021-07-15 | IT Infrastructure |
| PI-SU-CO-364 | BC-19113 | 2024-07-16 | Supply Chain |
| Soy Isolate 50% Grade B | IC-19117 | 2021-02-23 | Operations |
| AS-AC-130 | BC-19128 | 2022-04-12 | Compliance |
| Dextrin | TC-19132 | 2024-12-18 | Compliance |
| Vertex Werkstoffe | IC-19142 | 2024-03-22 | IT Infrastructure |
| fructose 99.5% pharma grade | TC-19144 | 2023-08-15 | Finance |
| SIG-37-ZOD-1VME | IC-19152 | 2022-05-22 | Operations |
| Pea Protein 99.5% Premium | IC-19172 | 2021-09-09 | Operations |
| MA-DE-161 | TC-19178 | 2021-09-10 | IT Infrastructure |
| Potassium Sorbate | IC-19194 | 2023-06-05 | Product Management |
| SIG-12-HNK-0H4F | BC-19198 | 2021-02-16 | Compliance |
| Dextrose Grade A | BC-19201 | 2021-11-25 | Data Governance |
| Coconut Oil Pharma Grade | IC-19202 | 2023-06-04 | Operations |
| RA-OI-745 | IC-19208 | 2024-06-27 | Compliance |
| glucose syrup 25% | IC-19209 | 2024-11-13 | Compliance |
| Catalyst Ingredients Holdings | IC-19224 | 2021-09-03 | Product Management |
| Sodium Benzoate 99.5% Grade A | IC-19242 | 2024-08-05 | Compliance |
| palm oil tech grade | BC-19245 | 2024-05-22 | Compliance |
| Excise IN 15% | IC-19251 | 2024-09-25 | Data Governance |
| PR-PA-779 PLC | TC-19254 | 2022-06-22 | Supply Chain |
| Vertex Logistics | BC-19256 | 2023-04-26 | Product Management |
| Potassium Sorbate Standard | IC-19264 | 2022-11-01 | Data Governance |
| VE-SO-701 | IC-19288 | 2022-09-20 | Product Management |
| Pea Protein | TC-19295 | 2021-07-13 | Operations |
| SO-AC-25-GR-B-198 | TC-19302 | 2021-07-28 | Data Governance |
| vat reduced br 21% | IC-19313 | 2021-11-10 | Product Management |
| GL-MA-770 | BC-19343 | 2021-01-14 | IT Infrastructure |
| SIG-20-LIK-8TZV Ltd. | BC-19348 | 2023-02-26 | Product Management |
| Atlantic Sourcing | TC-19356 | 2021-12-20 | Compliance |
| sodium benzoate 99.5% standard | TC-19383 | 2022-09-27 | Supply Chain |
| SIG-22-HSE-KSCU | IC-19396 | 2024-06-09 | Supply Chain |
| nexus partners SARL | BC-19398 | 2022-10-06 | Data Governance |
| prism materials | IC-19405 | 2024-01-06 | Product Management |
| sodium benzoate | TC-19410 | 2024-01-13 | Product Management |
| Global Distribution LLC | IC-19414 | 2024-04-17 | Data Governance |
| CI-AC-FO-GR-293 | BC-19421 | 2024-12-05 | IT Infrastructure |
| SIG-99-CEZ-35MR | IC-19445 | 2021-01-06 | IT Infrastructure |
| AT-CO-808 GmbH | IC-19457 | 2021-02-24 | Data Governance |
| CY-763 | BC-19464 | 2024-05-10 | Compliance |
| Sorbinsäure 99.5% | TC-19477 | 2023-06-23 | Product Management |
| Cyclodextrin Pharma Grade | BC-19485 | 2021-03-04 | Supply Chain |
| ascorbic acid 70% | IC-19492 | 2021-09-14 | Compliance |
| dextrose tech grade | IC-19505 | 2021-11-23 | Operations |
| SIG-44-DLM-CU63 | IC-19517 | 2022-08-14 | IT Infrastructure |
| Soy Isolate 99.5% Grade A | TC-19526 | 2023-11-12 | Compliance |
| Vanguard Logistics | TC-19530 | 2023-04-21 | Product Management |
| Soy Isolate 99.5% Grade A | TC-19535 | 2021-08-18 | Operations |
| SIG-27-QTK-7Y6C | IC-19551 | 2022-04-26 | Compliance |
| SO-IS-PR-309 | IC-19559 | 2024-05-09 | Data Governance |
| SO-CH-ST-522 | TC-19574 | 2021-06-24 | IT Infrastructure |
| Sodium Benzoate 98% | BC-19594 | 2023-08-18 | Data Governance |
| maltodextrin de5 premium | BC-19602 | 2021-01-05 | IT Infrastructure |
| Resistente Stärke 70% | BC-19619 | 2022-05-12 | Finance |
| Weizenklebereiweiß Qualitätsstufe II | TC-19630 | 2023-11-23 | Operations |
| Soja Isolate 98% Premiumqualität | IC-19634 | 2023-02-07 | IT Infrastructure |
| SIG-86-VCP-SVOL | TC-19654 | 2023-09-06 | IT Infrastructure |
| Zitronensäure | TC-19658 | 2023-06-15 | Data Governance |
| Atlas Logistik | BC-19659 | 2021-08-17 | Supply Chain |
| premier industries Holdings | TC-19660 | 2021-10-20 | Finance |
| SO-AC-340 | TC-19662 | 2022-09-03 | Operations |
| Lactic Acid 99.5% | TC-19665 | 2021-03-28 | Finance |
| SIG-16-QDW-AN2Z | BC-19666 | 2021-05-03 | Supply Chain |
| Soja Isolate 98% | BC-19680 | 2024-04-12 | Compliance |
| SIG-15-MKL-LGBK | IC-19696 | 2021-08-14 | Compliance |
| SO-AC-852 | BC-19709 | 2021-02-23 | Operations |
| SIG-93-DAB-6LKS | BC-19711 | 2022-05-22 | Operations |
| SIG-38-FPC-A25N | IC-19713 | 2022-04-27 | Finance |
| Nexus Materials | TC-19717 | 2022-04-02 | Supply Chain |
| Pea Protein 25% | TC-19722 | 2022-12-11 | Compliance |
| SIG-80-ZKZ-ANXJ | BC-19738 | 2021-07-08 | Data Governance |
| Coconut Oil 70% | IC-19764 | 2024-07-07 | Operations |
| CA-CA-FO-GR-685 | IC-19781 | 2021-07-15 | Compliance |
| Wheat Gluten Grade B | IC-19794 | 2024-03-18 | Operations |
| meridian supply | TC-19796 | 2024-04-03 | Data Governance |
| dextrin premium | IC-19803 | 2024-01-02 | Product Management |
| SIG-88-EEY-HOGD | BC-19819 | 2023-02-17 | Compliance |
| PA-OI-98-856 | TC-19823 | 2022-04-08 | Supply Chain |
| CO-SU-CO-635 | IC-19838 | 2024-12-16 | Product Management |
| Stratos Ingredients Group | TC-19858 | 2023-08-23 | IT Infrastructure |
| HO-PA-149 International | TC-19909 | 2024-07-25 | IT Infrastructure |
| VA-MA-502 | IC-19918 | 2021-08-03 | IT Infrastructure |
| Isoglucose | TC-19923 | 2024-11-02 | Finance |
| Stellar Versorgung NV | BC-19934 | 2024-03-11 | Operations |
| SIG-41-SWO-23GD | BC-19943 | 2024-10-05 | Data Governance |
| glucose syrup | BC-19955 | 2021-09-06 | Finance |
| nexus supply | TC-19969 | 2021-06-15 | Operations |
| PR-LO-351 | BC-19976 | 2022-06-25 | Operations |
| Premier Versorgung GmbH | TC-19985 | 2024-12-11 | Product Management |
| Citric Acid 50% | TC-19988 | 2023-01-24 | Product Management |
| SIG-42-SPP-A6C6 | IC-20012 | 2023-01-06 | IT Infrastructure |
| maltodextrin de20 | BC-20016 | 2023-01-23 | IT Infrastructure |
| Weizenklebereiweiß 99.5% Qualitätsstufe I | IC-20030 | 2021-03-04 | Data Governance |
| sodium benzoate | TC-20031 | 2023-12-19 | Product Management |
| Withholding FR 15% | BC-20061 | 2023-07-08 | Finance |
| CE-MA-604 | BC-20066 | 2022-01-02 | Data Governance |
| SIG-60-VTH-H7AM | IC-20078 | 2022-09-07 | Finance |
| soy isolate premium | TC-20099 | 2022-03-28 | Supply Chain |
| Rapsöl Technische Qualität | BC-20128 | 2021-01-28 | Product Management |
| vertex commodities KG | BC-20174 | 2023-07-10 | IT Infrastructure |
| Ascorbic Acid | TC-20176 | 2021-03-18 | Finance |
| ZE-TR-467 AG | BC-20183 | 2022-06-02 | Data Governance |
| Isoglucose 25% Lebensmittelrein | IC-20186 | 2021-01-09 | Supply Chain |
| Vanguard Partners PLC | BC-20208 | 2023-07-02 | Supply Chain |
| PE-PR-163 | IC-20214 | 2024-02-09 | IT Infrastructure |
| citric acid 70% | IC-20220 | 2021-10-05 | Operations |
| RE-ST-98-445 | IC-20227 | 2023-10-28 | Data Governance |
| Resistant Starch | IC-20263 | 2024-12-03 | Operations |
| SO-BE-50-TE-276 | IC-20272 | 2024-03-02 | IT Infrastructure |
| DE-99.5-720 | BC-20274 | 2024-06-21 | Compliance |
| PR-LO-104 KG | BC-20276 | 2022-06-18 | Data Governance |
| atlantic commodities | TC-20279 | 2024-04-16 | Compliance |
| Coconut Oil 25% Food Grade | TC-20282 | 2021-04-13 | Supply Chain |
| Rapsöl Qualitätsstufe I | IC-20284 | 2022-10-24 | Product Management |
| SIG-47-HPA-L2FX | BC-20290 | 2024-06-05 | Operations |
| Ascorbic Acid Premiumqualität | TC-20309 | 2022-02-27 | Operations |
| SIG-72-OHB-75ML SAS | IC-20313 | 2023-02-01 | Supply Chain |
| SIG-58-LVK-OFDU KG | TC-20320 | 2024-10-12 | Operations |
| Resistant Starch Technical | BC-20323 | 2023-08-21 | Finance |
| Ascorbic Acid 50% | BC-20334 | 2022-09-05 | Supply Chain |
| EL-SO-199 | BC-20336 | 2021-04-17 | Supply Chain |
| Ascorbic Acid | BC-20349 | 2021-04-04 | Compliance |
| CI-AC-GR-B-103 | TC-20357 | 2023-06-20 | Operations |
| Maltodextrin DE20 | BC-20360 | 2021-10-25 | Data Governance |
| SIG-83-CDB-3QOI | BC-20366 | 2022-09-04 | Supply Chain |
| Vanguard Logistics SARL | TC-20368 | 2022-09-01 | Finance |
| elite trading Ltd. | IC-20369 | 2022-07-17 | Compliance |
| SIG-92-KFT-DU1S | TC-20371 | 2024-10-19 | Supply Chain |
| SIG-11-SLQ-KF5B | BC-20374 | 2023-01-22 | Data Governance |
| Continental Enterprise GmbH | BC-20379 | 2021-10-01 | Data Governance |
| PA-OI-GR-B-326 | IC-20382 | 2023-03-16 | IT Infrastructure |
| CO-SU-CO-635 | BC-20383 | 2023-03-03 | IT Infrastructure |
| rapeseed oil | IC-20385 | 2022-01-19 | Product Management |
| VA-RE-B-10-482 | BC-20387 | 2022-03-04 | Data Governance |
| Prism Materials International | BC-20388 | 2022-07-05 | Finance |
| sodium benzoate | IC-20390 | 2024-12-21 | Operations |
| FR-278 | BC-20399 | 2023-02-17 | Operations |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| PR-SU-935 Ltd. | IC-6172 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat | IC-8185 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid 50% Standardqualität | IC-6161 | REVIEW REQUIRED | Historical - verify before use |
| Stellar Partners | IC-5753 | SUPERSEDED | Historical - verify before use |
| Stratos Chemicals | IC-8638 | SUPERSEDED | Historical - verify before use |
| Global Solutions Group | IC-7174 | REVIEW REQUIRED | Historical - verify before use |
| pinnacle ingredients GmbH | IC-7211 | PROVISIONAL | Historical - verify before use |
| Atlantic Rohstoffe International | IC-9656 | REVIEW REQUIRED | Historical - verify before use |
| SIG-35-RSV-01YT | IC-9317 | REVIEW REQUIRED | Historical - verify before use |
| Vanguard Logistik | IC-9303 | DEPRECATED | Historical - verify before use |
| Atlas Logistics | IC-8167 | PROVISIONAL | Historical - verify before use |
| Premier Rohstoffe Holdings | IC-9454 | PROVISIONAL | Historical - verify before use |
| Vat Standard CN 10% | IC-6979 | SUPERSEDED | Historical - verify before use |
| customs duty fr 19% | IC-7519 | SUPERSEDED | Historical - verify before use |
| ST-MA-670 Group | IC-5014 | PROVISIONAL | Historical - verify before use |
| SIG-37-NAI-M1G9 | IC-8371 | PROVISIONAL | Historical - verify before use |
| SIG-22-ADK-3T78 | IC-5717 | DEPRECATED | Historical - verify before use |
| SIG-70-HGQ-WORL | IC-6142 | SUPERSEDED | Historical - verify before use |
| AS-AC-GR-B-395 | IC-6764 | DEPRECATED | Historical - verify before use |
| vertex enterprise Group | IC-5152 | REVIEW REQUIRED | Historical - verify before use |
| Baltic Enterprise KG | IC-6312 | PROVISIONAL | Historical - verify before use |
| sodium benzoate 99.5% tech grade | IC-6153 | PROVISIONAL | Historical - verify before use |
| DE-GR-A-472 | IC-8762 | PROVISIONAL | Historical - verify before use |
| PR-PA-643 | IC-6437 | SUPERSEDED | Historical - verify before use |
| Sorbinsäure 50% Standardqualität | IC-7566 | SUPERSEDED | Historical - verify before use |
| SIG-89-RGS-FIRM Holdings | IC-7530 | REVIEW REQUIRED | Historical - verify before use |
| SIG-98-DBG-MTO5 | IC-8264 | PROVISIONAL | Historical - verify before use |
| RE-ST-GR-B-805 | IC-5074 | REVIEW REQUIRED | Historical - verify before use |
| SIG-26-WVS-AQ3B | IC-7804 | SUPERSEDED | Historical - verify before use |
| vat reduced cn 19% | IC-7514 | PROVISIONAL | Historical - verify before use |
| SIG-55-KQD-CQMQ | IC-9578 | REVIEW REQUIRED | Historical - verify before use |
| Zitronensäure 70% | IC-7203 | PROVISIONAL | Historical - verify before use |
| PR-SO-388 | IC-9474 | PROVISIONAL | Historical - verify before use |
| CU-DU-N-5-217 | IC-9620 | SUPERSEDED | Historical - verify before use |
| CA-GR-A-380 | IC-8644 | PROVISIONAL | Historical - verify before use |
| Traubenzucker Standardqualität | IC-9458 | PROVISIONAL | Historical - verify before use |
| Pea Protein Grade A | IC-9811 | REVIEW REQUIRED | Historical - verify before use |
| SIG-75-DRM-1CLN | IC-8234 | REVIEW REQUIRED | Historical - verify before use |
| NO-DI-582 AG | IC-8274 | DEPRECATED | Historical - verify before use |
| Zitronensäure Qualitätsstufe I | IC-5081 | PROVISIONAL | Historical - verify before use |
| ST-LO-136 | IC-8242 | SUPERSEDED | Historical - verify before use |
| SIG-81-FXX-6VPL | IC-6106 | PROVISIONAL | Historical - verify before use |
| Sorbinsäure 98% | IC-5621 | DEPRECATED | Historical - verify before use |
| palm oil 99.5% | IC-6482 | SUPERSEDED | Historical - verify before use |
| Vat Reduced BR 25% | IC-6498 | REVIEW REQUIRED | Historical - verify before use |
| SIG-35-HUP-NW3M | IC-9061 | PROVISIONAL | Historical - verify before use |
| PO-SO-PR-101 | IC-8196 | PROVISIONAL | Historical - verify before use |
| Rapsöl 99.5% Technische Qualität | IC-8944 | SUPERSEDED | Historical - verify before use |
| global materials | IC-7709 | DEPRECATED | Historical - verify before use |
| Nexus Commodities International | IC-6623 | PROVISIONAL | Historical - verify before use |
| Excise GB 25% | IC-5156 | REVIEW REQUIRED | Historical - verify before use |
| Natriumchlorid 70% | IC-6306 | PROVISIONAL | Historical - verify before use |
| PR-MA-669 Ltd. | IC-7697 | REVIEW REQUIRED | Historical - verify before use |
| calcium carbonate 99.5% | IC-5694 | PROVISIONAL | Historical - verify before use |
| MA-DE-933 | IC-8871 | REVIEW REQUIRED | Historical - verify before use |
| Stellar Versorgung GmbH | IC-9757 | SUPERSEDED | Historical - verify before use |
| SIG-27-FHX-VO6Y | IC-6183 | DEPRECATED | Historical - verify before use |
| Baltic Sourcing | IC-8663 | DEPRECATED | Historical - verify before use |
| Potassium Sorbate 70% | IC-7749 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil 98% | IC-9121 | PROVISIONAL | Historical - verify before use |
| SO-CH-70-GR-B-821 | IC-7783 | REVIEW REQUIRED | Historical - verify before use |
| Elite Materials | IC-5631 | REVIEW REQUIRED | Historical - verify before use |
| vat standard nl 5% | IC-8234 | REVIEW REQUIRED | Historical - verify before use |
| Central Logistik Holdings | IC-9144 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid | IC-9370 | SUPERSEDED | Historical - verify before use |
| SIG-91-XWQ-EANP | IC-9700 | PROVISIONAL | Historical - verify before use |
| Excise IN 19% | IC-7275 | DEPRECATED | Historical - verify before use |
| sorbic acid | IC-6562 | REVIEW REQUIRED | Historical - verify before use |
| Vat Standardqualität IN 0% | IC-7264 | PROVISIONAL | Historical - verify before use |
| Zitronensäure Qualitätsstufe I | IC-8563 | SUPERSEDED | Historical - verify before use |
| Excise IN 25% | IC-8718 | PROVISIONAL | Historical - verify before use |
| Natriumchlorid Technische Qualität | IC-9299 | SUPERSEDED | Historical - verify before use |
| SIG-30-PPI-DU4D | IC-6398 | SUPERSEDED | Historical - verify before use |
| AP-SU-CO-814 | IC-8900 | DEPRECATED | Historical - verify before use |
| Withholding BR 5% | IC-8327 | PROVISIONAL | Historical - verify before use |
| apex chemicals Inc. | IC-9204 | DEPRECATED | Historical - verify before use |
| meridian materials | IC-5576 | PROVISIONAL | Historical - verify before use |
| wheat gluten 70% | IC-9851 | DEPRECATED | Historical - verify before use |
| Dextrin 50% | IC-8896 | SUPERSEDED | Historical - verify before use |
| SIG-29-RWA-CHL8 | IC-6571 | PROVISIONAL | Historical - verify before use |
| Atlas Logistics | IC-8551 | SUPERSEDED | Historical - verify before use |
| Isoglucose 98% | IC-7306 | SUPERSEDED | Historical - verify before use |
| Vat Reduced IN 20% | IC-7916 | REVIEW REQUIRED | Historical - verify before use |
| Baltic Versorgung | IC-7849 | SUPERSEDED | Historical - verify before use |
| nexus sourcing | IC-9121 | DEPRECATED | Historical - verify before use |
| Sorbinsäure | IC-6572 | SUPERSEDED | Historical - verify before use |
| RA-OI-FO-GR-269 | IC-9450 | DEPRECATED | Historical - verify before use |
| Nordic Logistik | IC-7400 | REVIEW REQUIRED | Historical - verify before use |
| apex processing Ltd. | IC-7930 | PROVISIONAL | Historical - verify before use |
| Vat Reduced BR 19% | IC-8537 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid 70% | IC-9104 | PROVISIONAL | Historical - verify before use |
| Pea Protein | IC-8209 | DEPRECATED | Historical - verify before use |
| AS-AC-165 | IC-5658 | PROVISIONAL | Historical - verify before use |
| elite materials | IC-7913 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid 50% | IC-9412 | DEPRECATED | Historical - verify before use |
| SIG-99-IZM-CYBY | IC-5987 | SUPERSEDED | Historical - verify before use |
| Dextrin 98% | IC-6608 | PROVISIONAL | Historical - verify before use |
| Apex Trading Holdings | IC-6242 | SUPERSEDED | Historical - verify before use |
| lactic acid 98% premium | IC-9124 | DEPRECATED | Historical - verify before use |
| SIG-90-NFZ-XRLG | IC-6302 | REVIEW REQUIRED | Historical - verify before use |
| SIG-39-OZI-N968 | IC-7504 | REVIEW REQUIRED | Historical - verify before use |
| Fructose Premiumqualität | IC-8503 | DEPRECATED | Historical - verify before use |
| citric acid standard | IC-6901 | REVIEW REQUIRED | Historical - verify before use |
| Soja Isolate Premiumqualität | IC-8725 | DEPRECATED | Historical - verify before use |
| SIG-61-CIV-LFWA | IC-5931 | DEPRECATED | Historical - verify before use |
| Isoglucose Lebensmittelrein | IC-8676 | PROVISIONAL | Historical - verify before use |
| Fructose Standardqualität | IC-6075 | SUPERSEDED | Historical - verify before use |
| Prime Werkstoffe | IC-7390 | PROVISIONAL | Historical - verify before use |
| SIG-58-SVK-Z948 | IC-9338 | SUPERSEDED | Historical - verify before use |
| SO-AC-70-785 | IC-7438 | PROVISIONAL | Historical - verify before use |
| Stratos Supply SAS | IC-7994 | SUPERSEDED | Historical - verify before use |
| Atlantic Verarbeitung Group | IC-9844 | DEPRECATED | Historical - verify before use |
| Atlantic Logistics SAS | IC-6255 | SUPERSEDED | Historical - verify before use |
| Customs Duty BR 21% | IC-5112 | PROVISIONAL | Historical - verify before use |
| SIG-93-ZCF-6HM3 | IC-8324 | SUPERSEDED | Historical - verify before use |
| PR-SU-CO-591 | IC-6634 | SUPERSEDED | Historical - verify before use |
| Vat Reduced CN 21% | IC-6896 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-ST-153 | IC-8424 | REVIEW REQUIRED | Historical - verify before use |
| ST-SO-673 | IC-6006 | SUPERSEDED | Historical - verify before use |
| Glucose Syrup 70% | IC-9563 | PROVISIONAL | Historical - verify before use |
| Elite Sourcing | IC-5271 | SUPERSEDED | Historical - verify before use |
| dextrose | IC-9401 | SUPERSEDED | Historical - verify before use |
| CE-PA-586 SARL | IC-9834 | SUPERSEDED | Historical - verify before use |
| CA-CA-648 | IC-7741 | PROVISIONAL | Historical - verify before use |
| PR-MA-161 | IC-6642 | DEPRECATED | Historical - verify before use |
| pinnacle industries SAS | IC-8838 | PROVISIONAL | Historical - verify before use |
| PR-SO-469 | IC-9930 | SUPERSEDED | Historical - verify before use |
| Isoglucose | IC-8880 | REVIEW REQUIRED | Historical - verify before use |
| SIG-93-ZCF-6HM3 | IC-9999 | SUPERSEDED | Historical - verify before use |
| SIG-27-FHX-VO6Y | IC-7501 | DEPRECATED | Historical - verify before use |
| SIG-88-XZP-H10B | IC-6132 | REVIEW REQUIRED | Historical - verify before use |
| Casein 50% Premium | IC-7839 | DEPRECATED | Historical - verify before use |
| SIG-43-OLC-OFCX | IC-7664 | REVIEW REQUIRED | Historical - verify before use |
| PA-OI-70-GR-B-781 | IC-7856 | PROVISIONAL | Historical - verify before use |
| Rapsöl 98% Standardqualität | IC-9222 | SUPERSEDED | Historical - verify before use |
| Natriumbenzoat | IC-6866 | SUPERSEDED | Historical - verify before use |
| SIG-52-EML-H8JV | IC-7091 | DEPRECATED | Historical - verify before use |
| Nordic Manufacturing Holdings | IC-5958 | REVIEW REQUIRED | Historical - verify before use |
| PA-OI-TE-134 | IC-5457 | DEPRECATED | Historical - verify before use |
| Global Werkstoffe | IC-8224 | REVIEW REQUIRED | Historical - verify before use |
| Vertex Chemicals Holdings | IC-9622 | DEPRECATED | Historical - verify before use |
| IS-FO-GR-555 | IC-6484 | SUPERSEDED | Historical - verify before use |
| PR-PA-269 AG | IC-9287 | REVIEW REQUIRED | Historical - verify before use |
| SU-OI-FO-GR-778 | IC-5871 | SUPERSEDED | Historical - verify before use |
| SIG-92-ZTO-VZGU | IC-9922 | DEPRECATED | Historical - verify before use |
| Stellar Sourcing | IC-7737 | DEPRECATED | Historical - verify before use |
| fructose 99.5% tech grade | IC-7053 | DEPRECATED | Historical - verify before use |
| sorbic acid 25% pharma grade | IC-6549 | SUPERSEDED | Historical - verify before use |
| CU-DU-G-0-770 | IC-6022 | SUPERSEDED | Historical - verify before use |
| quantum supply | IC-5665 | REVIEW REQUIRED | Historical - verify before use |
| Calcium Carbonate 50% Food Grade | IC-6233 | PROVISIONAL | Historical - verify before use |
| sorbic acid premium | IC-5742 | DEPRECATED | Historical - verify before use |
| SIG-92-RZH-LRHH | IC-9732 | DEPRECATED | Historical - verify before use |
| vat standard fr 5% | IC-6702 | PROVISIONAL | Historical - verify before use |
| Sonnenblumenöl 70% Lebensmittelrein | IC-5638 | DEPRECATED | Historical - verify before use |
| stratos commodities Holdings | IC-9901 | DEPRECATED | Historical - verify before use |
| Pea Protein | IC-9763 | PROVISIONAL | Historical - verify before use |
| Sonnenblumenöl 70% Lebensmittelrein | IC-5290 | SUPERSEDED | Historical - verify before use |
| SIG-56-JML-GDXB | IC-9018 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid 99.5% Grade B | IC-7257 | REVIEW REQUIRED | Historical - verify before use |
| Dextrose 25% | IC-7013 | SUPERSEDED | Historical - verify before use |
| SIG-50-JOR-LO4P | IC-7458 | DEPRECATED | Historical - verify before use |
| Coconut Oil 70% Qualitätsstufe I | IC-7328 | REVIEW REQUIRED | Historical - verify before use |
| SIG-13-CGO-2Y4L | IC-9430 | REVIEW REQUIRED | Historical - verify before use |
| baltic supply | IC-7261 | PROVISIONAL | Historical - verify before use |
| Traubenzucker Lebensmittelrein | IC-5962 | REVIEW REQUIRED | Historical - verify before use |
| Isoglucose 25% Lebensmittelrein | IC-8505 | PROVISIONAL | Historical - verify before use |
| Continental Werkstoffe NV | IC-5629 | DEPRECATED | Historical - verify before use |
| SIG-56-BPD-M0A6 | IC-7417 | PROVISIONAL | Historical - verify before use |
| SIG-98-CGL-FHWJ | IC-8394 | REVIEW REQUIRED | Historical - verify before use |
| SIG-65-XHR-R1SP | IC-7909 | DEPRECATED | Historical - verify before use |
| SIG-70-QGS-CCAF | IC-9351 | REVIEW REQUIRED | Historical - verify before use |
| Pea Protein 70% Pharma Grade | IC-7952 | DEPRECATED | Historical - verify before use |
| quantum logistics | IC-6666 | REVIEW REQUIRED | Historical - verify before use |
| CA-CA-648 | IC-9132 | SUPERSEDED | Historical - verify before use |
| Premier Versorgung GmbH | IC-7275 | SUPERSEDED | Historical - verify before use |
| apex logistics LLC | IC-5765 | PROVISIONAL | Historical - verify before use |
| Lactic Acid | IC-6189 | REVIEW REQUIRED | Historical - verify before use |
| Isoglucose 70% | IC-5181 | PROVISIONAL | Historical - verify before use |
| Fructose 99.5% Pharma Grade | IC-8933 | DEPRECATED | Historical - verify before use |
| Excise US 19% | IC-6294 | SUPERSEDED | Historical - verify before use |
| Isoglucose Food Grade | IC-9257 | PROVISIONAL | Historical - verify before use |
| quantum ingredients Holdings | IC-9300 | REVIEW REQUIRED | Historical - verify before use |
| Zitronensäure 98% | IC-7276 | DEPRECATED | Historical - verify before use |
| LA-AC-ST-663 | IC-9006 | REVIEW REQUIRED | Historical - verify before use |
| CA-580 | IC-8494 | SUPERSEDED | Historical - verify before use |
| SO-BE-824 | IC-9856 | DEPRECATED | Historical - verify before use |
| Lactic Acid Technical | IC-9329 | SUPERSEDED | Historical - verify before use |
| CE-MA-338 | IC-7302 | REVIEW REQUIRED | Historical - verify before use |
| Wheat Gluten 25% Standard | IC-6939 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-98-876 | IC-8933 | SUPERSEDED | Historical - verify before use |
| SO-IS-PH-GR-671 | IC-7271 | DEPRECATED | Historical - verify before use |
| dextrose 50% standard | IC-8300 | REVIEW REQUIRED | Historical - verify before use |
| PO-SO-339 | IC-8512 | SUPERSEDED | Historical - verify before use |
| pea protein 70% premium | IC-7170 | DEPRECATED | Historical - verify before use |
| Global Chemicals | IC-6140 | PROVISIONAL | Historical - verify before use |
| SIG-56-ZQV-YINP SA | IC-9972 | REVIEW REQUIRED | Historical - verify before use |
| SIG-98-HZM-47LK | IC-6814 | REVIEW REQUIRED | Historical - verify before use |
| SIG-22-XCC-QSNV | IC-8643 | DEPRECATED | Historical - verify before use |
| SIG-42-HBL-L3KU International | IC-9182 | DEPRECATED | Historical - verify before use |
| lactic acid standard | IC-9235 | DEPRECATED | Historical - verify before use |
| Pea Protein 98% | IC-9918 | PROVISIONAL | Historical - verify before use |
| VE-IN-631 Ltd. | IC-7107 | SUPERSEDED | Historical - verify before use |
| SIG-94-MKW-LH8F | IC-5873 | REVIEW REQUIRED | Historical - verify before use |
| SIG-81-AXG-9CBI AG | IC-6576 | DEPRECATED | Historical - verify before use |
| Isoglucose Grade B | IC-9984 | PROVISIONAL | Historical - verify before use |
| SIG-51-ZAY-11PM | IC-8634 | REVIEW REQUIRED | Historical - verify before use |
| Catalyst Manufacturing GmbH | IC-9811 | SUPERSEDED | Historical - verify before use |
| maltodextrin de18 | IC-6305 | REVIEW REQUIRED | Historical - verify before use |
| Sonnenblumenöl Standardqualität | IC-8897 | DEPRECATED | Historical - verify before use |
| Meridian Solutions KG | IC-8562 | PROVISIONAL | Historical - verify before use |
| vanguard enterprise | IC-5807 | DEPRECATED | Historical - verify before use |
| Quantum Werkstoffe | IC-8023 | REVIEW REQUIRED | Historical - verify before use |
| Stellar Handel | IC-6964 | PROVISIONAL | Historical - verify before use |
| Customs Duty FR 25% | IC-7529 | REVIEW REQUIRED | Historical - verify before use |
| Natriumchlorid Lebensmittelrein | IC-8188 | SUPERSEDED | Historical - verify before use |
| SIG-76-AAU-3VM8 | IC-5214 | PROVISIONAL | Historical - verify before use |
| Fructose | IC-8999 | SUPERSEDED | Historical - verify before use |
| Nordic Rohstoffe | IC-8632 | DEPRECATED | Historical - verify before use |
| Coconut Oil 25% Technische Qualität | IC-8138 | PROVISIONAL | Historical - verify before use |
| Traubenzucker Standardqualität | IC-7261 | SUPERSEDED | Historical - verify before use |
| Soja Isolate Premiumqualität | IC-7760 | PROVISIONAL | Historical - verify before use |
| Baltic Processing PLC | IC-7059 | DEPRECATED | Historical - verify before use |
| Prism Logistik | IC-5798 | SUPERSEDED | Historical - verify before use |
| SIG-97-SMQ-9SG6 | IC-8166 | REVIEW REQUIRED | Historical - verify before use |
| Casein Standard | IC-8622 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil 70% Qualitätsstufe I | IC-5732 | REVIEW REQUIRED | Historical - verify before use |
| Palm Oil 99.5% | IC-8721 | PROVISIONAL | Historical - verify before use |
| LA-AC-ST-663 | IC-6718 | SUPERSEDED | Historical - verify before use |
| PI-DI-618 NV | IC-7963 | DEPRECATED | Historical - verify before use |
| SIG-50-FUX-7S9T | IC-9022 | PROVISIONAL | Historical - verify before use |
| Atlas Logistik | IC-7979 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid | IC-8123 | PROVISIONAL | Historical - verify before use |
| CA-CA-436 | IC-8212 | DEPRECATED | Historical - verify before use |
| Sodium Benzoate | IC-5501 | DEPRECATED | Historical - verify before use |
| Pea Protein 99.5% | IC-9816 | REVIEW REQUIRED | Historical - verify before use |
| Core Sourcing | IC-5350 | PROVISIONAL | Historical - verify before use |
| Potassium Sorbate | IC-5686 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid Food Grade | IC-5725 | SUPERSEDED | Historical - verify before use |
| sorbic acid 98% | IC-9945 | REVIEW REQUIRED | Historical - verify before use |
| SIG-99-CTB-8OFG Group | IC-9712 | SUPERSEDED | Historical - verify before use |
| WH-GL-923 | IC-7858 | SUPERSEDED | Historical - verify before use |
| Nexus Versorgung GmbH | IC-9095 | PROVISIONAL | Historical - verify before use |
| PO-SO-339 | IC-9603 | REVIEW REQUIRED | Historical - verify before use |
| sodium benzoate premium | IC-6029 | SUPERSEDED | Historical - verify before use |
| Resistente Stärke Lebensmittelrein | IC-7577 | SUPERSEDED | Historical - verify before use |
| SIG-71-FSV-21LW | IC-5573 | REVIEW REQUIRED | Historical - verify before use |
| Resistente Stärke | IC-9346 | PROVISIONAL | Historical - verify before use |
| customs duty us 15% | IC-7750 | PROVISIONAL | Historical - verify before use |
| Stellar Manufacturing Holdings | IC-8791 | SUPERSEDED | Historical - verify before use |
| NE-MA-648 | IC-9334 | PROVISIONAL | Historical - verify before use |
| excise br 21% | IC-5113 | REVIEW REQUIRED | Historical - verify before use |
| Sunflower Oil Standard | IC-9535 | SUPERSEDED | Historical - verify before use |
| casein standard | IC-6577 | SUPERSEDED | Historical - verify before use |
| SIG-75-GUI-J643 | IC-8332 | SUPERSEDED | Historical - verify before use |
| sunflower oil | IC-7388 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid | IC-9654 | SUPERSEDED | Historical - verify before use |
| SIG-97-UWA-JWLN | IC-9845 | SUPERSEDED | Historical - verify before use |
| NE-PA-358 | IC-8634 | PROVISIONAL | Historical - verify before use |
| Coconut Oil Grade A | IC-7146 | PROVISIONAL | Historical - verify before use |
| ST-IN-592 SA | IC-8621 | REVIEW REQUIRED | Historical - verify before use |
| SIG-55-DBH-2QS3 | IC-6727 | PROVISIONAL | Historical - verify before use |
| sodium benzoate premium | IC-5189 | REVIEW REQUIRED | Historical - verify before use |
| quantum supply | IC-7296 | DEPRECATED | Historical - verify before use |
| atlas partners | IC-5181 | REVIEW REQUIRED | Historical - verify before use |
| vat standard de 0% | IC-7407 | REVIEW REQUIRED | Historical - verify before use |
| BA-IN-547 | IC-5730 | REVIEW REQUIRED | Historical - verify before use |
| DE-70-769 | IC-5736 | PROVISIONAL | Historical - verify before use |
| AT-SU-CO-864 | IC-9865 | SUPERSEDED | Historical - verify before use |
| SIG-79-GKV-W8GA | IC-7807 | SUPERSEDED | Historical - verify before use |
| Dextrose 70% Grade A | IC-9435 | PROVISIONAL | Historical - verify before use |
| Dextrin 98% | IC-8615 | PROVISIONAL | Historical - verify before use |
| dextrose standard | IC-8222 | SUPERSEDED | Historical - verify before use |
| prime processing PLC | IC-7958 | DEPRECATED | Historical - verify before use |
| Pea Protein | IC-8943 | REVIEW REQUIRED | Historical - verify before use |
| SO-AC-852 | IC-7490 | DEPRECATED | Historical - verify before use |
| SIG-50-DEU-V25U | IC-7760 | SUPERSEDED | Historical - verify before use |
| meridian chemicals Holdings | IC-8963 | REVIEW REQUIRED | Historical - verify before use |
| stratos partners SA | IC-6762 | PROVISIONAL | Historical - verify before use |
| SIG-62-DCP-L2AF | IC-5097 | DEPRECATED | Historical - verify before use |
| PI-SU-CO-734 | IC-7259 | DEPRECATED | Historical - verify before use |
| Casein Premium | IC-7266 | REVIEW REQUIRED | Historical - verify before use |
| PE-PR-70-PR-387 | IC-7405 | PROVISIONAL | Historical - verify before use |
| SIG-83-CDB-3QOI | IC-5357 | SUPERSEDED | Historical - verify before use |
| MA-DE-146 | IC-5298 | REVIEW REQUIRED | Historical - verify before use |
| Stellar Materials | IC-7882 | SUPERSEDED | Historical - verify before use |
| SIG-44-MHK-SRCB | IC-6334 | PROVISIONAL | Historical - verify before use |
| SIG-66-LJV-5E3H | IC-9616 | DEPRECATED | Historical - verify before use |
| sodium benzoate | IC-9159 | PROVISIONAL | Historical - verify before use |
| Vat Standardqualität BR 15% | IC-9050 | SUPERSEDED | Historical - verify before use |
| Zitronensäure 50% Qualitätsstufe I | IC-9992 | SUPERSEDED | Historical - verify before use |
| Stellar Sourcing | IC-7542 | REVIEW REQUIRED | Historical - verify before use |
| SIG-18-LLP-8GUU | IC-9954 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat 99.5% Qualitätsstufe I | IC-6941 | DEPRECATED | Historical - verify before use |
| lactic acid tech grade | IC-6379 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil 98% | IC-8053 | DEPRECATED | Historical - verify before use |
| SIG-53-AHT-MGFX | IC-6278 | DEPRECATED | Historical - verify before use |
| SIG-26-WVS-AQ3B | IC-5660 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-25-TE-177 | IC-6958 | REVIEW REQUIRED | Historical - verify before use |
| Sodium Benzoate 50% | IC-5313 | SUPERSEDED | Historical - verify before use |
| Atlantic Trading BV | IC-5912 | REVIEW REQUIRED | Historical - verify before use |
| Sodium Benzoate 99.5% | IC-5131 | SUPERSEDED | Historical - verify before use |
| SIG-86-DMG-XSKY | IC-6573 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-TE-304 | IC-8375 | SUPERSEDED | Historical - verify before use |
| vertex solutions | IC-6195 | PROVISIONAL | Historical - verify before use |
| Lactic Acid Lebensmittelrein | IC-7589 | PROVISIONAL | Historical - verify before use |
| SIG-49-QVY-JMMU | IC-5042 | SUPERSEDED | Historical - verify before use |
| Maltodextrin DE10 | IC-5327 | PROVISIONAL | Historical - verify before use |
| SIG-84-HFZ-NPNZ | IC-8075 | DEPRECATED | Historical - verify before use |
| SIG-46-YOE-MYAX SA | IC-5370 | SUPERSEDED | Historical - verify before use |
| Sonnenblumenöl Qualitätsstufe I | IC-5964 | PROVISIONAL | Historical - verify before use |
| ascorbic acid | IC-7512 | SUPERSEDED | Historical - verify before use |
| SO-IS-FO-GR-334 | IC-7221 | REVIEW REQUIRED | Historical - verify before use |
| SO-BE-FO-GR-650 | IC-7136 | DEPRECATED | Historical - verify before use |
| LA-AC-ST-823 | IC-6933 | DEPRECATED | Historical - verify before use |
| SIG-16-GDL-YC2T LLC | IC-7985 | PROVISIONAL | Historical - verify before use |
| SIG-22-SKR-CTIC | IC-8980 | SUPERSEDED | Historical - verify before use |
| SO-IS-PR-242 | IC-8288 | DEPRECATED | Historical - verify before use |
| Sorbinsäure | IC-9903 | PROVISIONAL | Historical - verify before use |
| SIG-69-CZY-YXFK | IC-6177 | SUPERSEDED | Historical - verify before use |
| palm oil pharma grade | IC-5245 | SUPERSEDED | Historical - verify before use |
| Prime Materials Inc. | IC-5614 | DEPRECATED | Historical - verify before use |
| Sodium Benzoate 99.5% Grade A | IC-7156 | DEPRECATED | Historical - verify before use |


#### 4.3.4 Excluded Assignments

Assignments excluded from scope per stakeholder decision:

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-3530-C | Missing required attributes | Business owner notified |
| NOISE-5247-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-7734-H | Pending validation | Escalated to data steward |
| NOISE-8543-C | Missing required attributes | Manual review scheduled |
| NOISE-7991-A | Pending validation | Manual review scheduled |
| NOISE-7292-G | Data quality insufficient | Escalated to data steward |
| NOISE-8725-C | Out of scope per business decision | Manual review scheduled |
| NOISE-6805-B | Data quality insufficient | Business owner notified |
| NOISE-7109-A | Pending validation | Manual review scheduled |
| NOISE-4203-C | Data quality insufficient | Escalated to data steward |
| NOISE-8918-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-7362-F | Out of scope per business decision | Manual review scheduled |
| NOISE-8445-B | Data quality insufficient | Business owner notified |
| NOISE-1166-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-7616-D | Out of scope per business decision | Business owner notified |
| NOISE-2479-C | Out of scope per business decision | Business owner notified |
| NOISE-9449-H | Missing required attributes | Manual review scheduled |
| NOISE-6546-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-5968-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8759-B | Duplicate source record | Business owner notified |
| NOISE-4916-D | Out of scope per business decision | Business owner notified |
| NOISE-1669-G | Pending validation | Escalated to data steward |
| NOISE-7613-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-4645-H | Out of scope per business decision | Escalated to data steward |
| NOISE-2488-B | Data quality insufficient | Escalated to data steward |
| NOISE-5547-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-4976-A | Pending validation | Business owner notified |
| NOISE-5668-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2223-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-8212-F | Out of scope per business decision | Escalated to data steward |
| NOISE-9390-F | Duplicate source record | Manual review scheduled |
| NOISE-3380-B | Out of scope per business decision | Business owner notified |
| NOISE-2029-E | Out of scope per business decision | Manual review scheduled |
| NOISE-8424-B | Duplicate source record | Escalated to data steward |
| NOISE-6608-E | Pending validation | Manual review scheduled |
| NOISE-4711-G | Data quality insufficient | Escalated to data steward |
| NOISE-4854-G | Pending validation | Deferred to Phase 2 |
| NOISE-3958-A | Missing required attributes | Business owner notified |
| NOISE-4757-G | Out of scope per business decision | Business owner notified |
| NOISE-4210-A | Duplicate source record | Escalated to data steward |
| NOISE-8848-A | Duplicate source record | Escalated to data steward |
| NOISE-4129-B | Duplicate source record | Manual review scheduled |
| NOISE-8799-B | Missing required attributes | Manual review scheduled |
| NOISE-8848-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-5690-C | Duplicate source record | Escalated to data steward |
| NOISE-9150-E | Pending validation | Escalated to data steward |
| NOISE-8133-D | Missing required attributes | Escalated to data steward |
| NOISE-9864-H | Pending validation | Escalated to data steward |
| NOISE-5782-H | Out of scope per business decision | Escalated to data steward |
| NOISE-7821-D | Out of scope per business decision | Business owner notified |
| NOISE-8101-D | Duplicate source record | Business owner notified |
| NOISE-5195-D | Out of scope per business decision | Business owner notified |
| NOISE-6968-A | Pending validation | Manual review scheduled |
| NOISE-5980-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-1335-F | Missing required attributes | Manual review scheduled |
| NOISE-7193-H | Missing required attributes | Manual review scheduled |
| NOISE-8280-F | Pending validation | Business owner notified |
| NOISE-8809-C | Out of scope per business decision | Business owner notified |
| NOISE-2037-C | Duplicate source record | Business owner notified |
| NOISE-9818-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8691-D | Data quality insufficient | Manual review scheduled |
| NOISE-4734-F | Data quality insufficient | Business owner notified |
| NOISE-8743-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-2541-F | Out of scope per business decision | Business owner notified |
| NOISE-9613-A | Pending validation | Deferred to Phase 2 |
| NOISE-1066-E | Data quality insufficient | Business owner notified |
| NOISE-7011-E | Duplicate source record | Business owner notified |
| NOISE-9686-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-7196-G | Out of scope per business decision | Escalated to data steward |
| NOISE-6577-D | Missing required attributes | Manual review scheduled |
| NOISE-7433-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5746-F | Pending validation | Escalated to data steward |
| NOISE-5785-D | Out of scope per business decision | Business owner notified |
| NOISE-8914-H | Pending validation | Escalated to data steward |
| NOISE-5716-B | Pending validation | Manual review scheduled |
| NOISE-1651-E | Pending validation | Manual review scheduled |
| NOISE-5470-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-5017-F | Missing required attributes | Manual review scheduled |
| NOISE-1631-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5354-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2183-C | Duplicate source record | Business owner notified |
| NOISE-8801-B | Pending validation | Business owner notified |
| NOISE-7388-E | Duplicate source record | Escalated to data steward |
| NOISE-6826-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-5552-H | Out of scope per business decision | Escalated to data steward |
| NOISE-6689-C | Missing required attributes | Business owner notified |
| NOISE-3375-B | Pending validation | Manual review scheduled |
| NOISE-2031-A | Data quality insufficient | Business owner notified |
| NOISE-4080-E | Data quality insufficient | Business owner notified |
| NOISE-5667-E | Out of scope per business decision | Manual review scheduled |
| NOISE-4944-B | Data quality insufficient | Business owner notified |
| NOISE-4423-A | Out of scope per business decision | Escalated to data steward |
| NOISE-9133-C | Data quality insufficient | Escalated to data steward |
| NOISE-3469-D | Pending validation | Manual review scheduled |
| NOISE-5578-E | Duplicate source record | Escalated to data steward |
| NOISE-6466-A | Data quality insufficient | Escalated to data steward |
| NOISE-4052-C | Out of scope per business decision | Business owner notified |
| NOISE-1736-F | Data quality insufficient | Business owner notified |
| NOISE-8439-D | Data quality insufficient | Manual review scheduled |
| NOISE-8538-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-7147-F | Pending validation | Business owner notified |
| NOISE-4376-C | Missing required attributes | Business owner notified |
| NOISE-3661-C | Data quality insufficient | Escalated to data steward |
| NOISE-8895-A | Data quality insufficient | Business owner notified |
| NOISE-2502-D | Out of scope per business decision | Manual review scheduled |
| NOISE-4778-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-7143-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4369-H | Out of scope per business decision | Escalated to data steward |
| NOISE-6978-F | Out of scope per business decision | Manual review scheduled |
| NOISE-2103-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3138-B | Pending validation | Escalated to data steward |
| NOISE-7609-E | Data quality insufficient | Business owner notified |
| NOISE-5408-C | Duplicate source record | Manual review scheduled |
| NOISE-8899-B | Missing required attributes | Manual review scheduled |
| NOISE-3368-D | Pending validation | Business owner notified |
| NOISE-6824-F | Out of scope per business decision | Business owner notified |
| NOISE-9425-B | Missing required attributes | Escalated to data steward |
| NOISE-9843-F | Duplicate source record | Manual review scheduled |
| NOISE-3507-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7831-A | Out of scope per business decision | Manual review scheduled |
| NOISE-1956-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7031-B | Pending validation | Business owner notified |
| NOISE-9581-C | Data quality insufficient | Business owner notified |
| NOISE-6005-A | Duplicate source record | Business owner notified |
| NOISE-7831-D | Data quality insufficient | Business owner notified |
| NOISE-5750-C | Pending validation | Deferred to Phase 2 |
| NOISE-4305-A | Missing required attributes | Manual review scheduled |
| NOISE-1550-B | Pending validation | Manual review scheduled |
| NOISE-7605-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-5520-E | Duplicate source record | Escalated to data steward |
| NOISE-5710-G | Duplicate source record | Business owner notified |
| NOISE-7787-A | Pending validation | Manual review scheduled |
| NOISE-9449-B | Out of scope per business decision | Business owner notified |
| NOISE-9698-F | Missing required attributes | Escalated to data steward |
| NOISE-2583-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9870-H | Missing required attributes | Escalated to data steward |
| NOISE-7777-G | Pending validation | Deferred to Phase 2 |
| NOISE-9119-G | Out of scope per business decision | Escalated to data steward |
| NOISE-9057-G | Duplicate source record | Manual review scheduled |
| NOISE-7371-D | Missing required attributes | Escalated to data steward |
| NOISE-9224-A | Data quality insufficient | Business owner notified |
| NOISE-2451-C | Data quality insufficient | Manual review scheduled |
| NOISE-9534-G | Data quality insufficient | Business owner notified |
| NOISE-3423-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-6300-B | Data quality insufficient | Escalated to data steward |
| NOISE-1434-D | Pending validation | Deferred to Phase 2 |
| NOISE-5493-B | Data quality insufficient | Business owner notified |
| NOISE-3944-D | Out of scope per business decision | Business owner notified |
| NOISE-3768-G | Pending validation | Escalated to data steward |
| NOISE-1560-F | Pending validation | Manual review scheduled |
| NOISE-7179-E | Out of scope per business decision | Escalated to data steward |
| NOISE-8802-E | Missing required attributes | Escalated to data steward |
| NOISE-4241-B | Out of scope per business decision | Business owner notified |
| NOISE-1726-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-1621-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-4197-H | Missing required attributes | Manual review scheduled |
| NOISE-7864-B | Data quality insufficient | Manual review scheduled |
| NOISE-3103-E | Missing required attributes | Business owner notified |
| NOISE-3693-E | Missing required attributes | Escalated to data steward |
| NOISE-2899-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3218-E | Duplicate source record | Business owner notified |
| NOISE-6908-G | Duplicate source record | Escalated to data steward |
| NOISE-9321-A | Data quality insufficient | Business owner notified |
| NOISE-1555-F | Out of scope per business decision | Escalated to data steward |
| NOISE-2236-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4826-F | Out of scope per business decision | Business owner notified |
| NOISE-1368-G | Out of scope per business decision | Escalated to data steward |
| NOISE-9511-A | Pending validation | Business owner notified |
| NOISE-2404-H | Pending validation | Manual review scheduled |
| NOISE-9291-H | Data quality insufficient | Manual review scheduled |
| NOISE-1405-D | Duplicate source record | Escalated to data steward |
| NOISE-9354-C | Missing required attributes | Business owner notified |
| NOISE-9242-B | Out of scope per business decision | Manual review scheduled |
| NOISE-2319-A | Pending validation | Manual review scheduled |
| NOISE-1993-C | Missing required attributes | Manual review scheduled |
| NOISE-3722-H | Pending validation | Manual review scheduled |
| NOISE-7975-E | Duplicate source record | Business owner notified |
| NOISE-1388-D | Duplicate source record | Manual review scheduled |
| NOISE-4795-H | Out of scope per business decision | Manual review scheduled |
| NOISE-9313-G | Data quality insufficient | Escalated to data steward |
| NOISE-7091-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-1024-H | Data quality insufficient | Business owner notified |
| NOISE-3580-C | Duplicate source record | Manual review scheduled |
| NOISE-6154-H | Pending validation | Business owner notified |
| NOISE-1124-C | Out of scope per business decision | Business owner notified |
| NOISE-3089-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-1163-H | Pending validation | Manual review scheduled |
| NOISE-1851-B | Out of scope per business decision | Business owner notified |
| NOISE-4003-H | Duplicate source record | Escalated to data steward |
| NOISE-6946-E | Out of scope per business decision | Manual review scheduled |
| NOISE-1731-E | Pending validation | Deferred to Phase 2 |
| NOISE-9927-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7177-G | Data quality insufficient | Manual review scheduled |
| NOISE-1574-F | Pending validation | Deferred to Phase 2 |
| NOISE-1864-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-3684-B | Duplicate source record | Escalated to data steward |
| NOISE-7758-B | Duplicate source record | Escalated to data steward |
| NOISE-4372-C | Missing required attributes | Escalated to data steward |
| NOISE-8120-H | Duplicate source record | Deferred to Phase 2 |
| NOISE-7438-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5206-A | Missing required attributes | Business owner notified |
| NOISE-4685-C | Pending validation | Deferred to Phase 2 |
| NOISE-3872-H | Out of scope per business decision | Business owner notified |
| NOISE-7234-D | Data quality insufficient | Manual review scheduled |
| NOISE-5262-H | Missing required attributes | Business owner notified |
| NOISE-8556-F | Pending validation | Escalated to data steward |
| NOISE-8420-C | Missing required attributes | Escalated to data steward |
| NOISE-4296-D | Pending validation | Manual review scheduled |
| NOISE-7446-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1863-F | Pending validation | Deferred to Phase 2 |
| NOISE-3377-A | Out of scope per business decision | Business owner notified |
| NOISE-3672-E | Data quality insufficient | Escalated to data steward |
| NOISE-4262-H | Data quality insufficient | Business owner notified |
| NOISE-1346-D | Missing required attributes | Business owner notified |
| NOISE-3811-E | Data quality insufficient | Escalated to data steward |
| NOISE-6628-H | Pending validation | Deferred to Phase 2 |
| NOISE-2553-B | Out of scope per business decision | Manual review scheduled |
| NOISE-8425-F | Duplicate source record | Escalated to data steward |
| NOISE-6800-F | Missing required attributes | Escalated to data steward |
| NOISE-6622-C | Pending validation | Deferred to Phase 2 |
| NOISE-6484-E | Pending validation | Manual review scheduled |
| NOISE-8595-F | Missing required attributes | Business owner notified |
| NOISE-3979-F | Duplicate source record | Manual review scheduled |
| NOISE-8033-D | Out of scope per business decision | Manual review scheduled |
| NOISE-5705-C | Out of scope per business decision | Manual review scheduled |
| NOISE-5828-F | Out of scope per business decision | Business owner notified |
| NOISE-3536-A | Out of scope per business decision | Escalated to data steward |
| NOISE-6591-C | Out of scope per business decision | Escalated to data steward |
| NOISE-6916-C | Data quality insufficient | Business owner notified |
| NOISE-8276-H | Out of scope per business decision | Escalated to data steward |
| NOISE-7684-G | Duplicate source record | Business owner notified |
| NOISE-7645-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-1593-H | Pending validation | Manual review scheduled |
| NOISE-5810-B | Duplicate source record | Escalated to data steward |
| NOISE-5892-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-6283-G | Data quality insufficient | Escalated to data steward |
| NOISE-2448-G | Pending validation | Manual review scheduled |
| NOISE-5097-D | Missing required attributes | Escalated to data steward |
| NOISE-8333-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9008-D | Data quality insufficient | Escalated to data steward |
| NOISE-6925-F | Missing required attributes | Manual review scheduled |
| NOISE-8843-D | Out of scope per business decision | Manual review scheduled |
| NOISE-1019-G | Duplicate source record | Escalated to data steward |
| NOISE-9537-B | Data quality insufficient | Business owner notified |
| NOISE-4059-G | Duplicate source record | Escalated to data steward |
| NOISE-1200-E | Out of scope per business decision | Manual review scheduled |
| NOISE-1501-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-5714-G | Data quality insufficient | Escalated to data steward |
| NOISE-4873-B | Missing required attributes | Escalated to data steward |
| NOISE-3965-C | Data quality insufficient | Escalated to data steward |
| NOISE-7032-F | Pending validation | Deferred to Phase 2 |
| NOISE-4735-A | Pending validation | Manual review scheduled |
| NOISE-9586-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-2801-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-8989-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4717-D | Pending validation | Manual review scheduled |
| NOISE-8809-G | Pending validation | Business owner notified |
| NOISE-4034-A | Data quality insufficient | Business owner notified |
| NOISE-2060-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-4262-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5262-H | Duplicate source record | Escalated to data steward |
| NOISE-2262-C | Pending validation | Escalated to data steward |
| NOISE-3342-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-8082-D | Duplicate source record | Escalated to data steward |
| NOISE-2211-A | Missing required attributes | Manual review scheduled |
| NOISE-2766-B | Missing required attributes | Escalated to data steward |
| NOISE-9206-D | Duplicate source record | Manual review scheduled |
| NOISE-2497-H | Pending validation | Manual review scheduled |
| NOISE-5991-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7585-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-4065-F | Data quality insufficient | Manual review scheduled |
| NOISE-1687-F | Pending validation | Business owner notified |
| NOISE-3317-F | Pending validation | Escalated to data steward |
| NOISE-3511-E | Pending validation | Deferred to Phase 2 |
| NOISE-2598-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6936-C | Missing required attributes | Business owner notified |
| NOISE-6550-G | Pending validation | Deferred to Phase 2 |
| NOISE-9289-A | Out of scope per business decision | Business owner notified |
| NOISE-8589-B | Pending validation | Manual review scheduled |
| NOISE-2029-E | Duplicate source record | Manual review scheduled |
| NOISE-8018-F | Pending validation | Manual review scheduled |
| NOISE-9854-F | Data quality insufficient | Business owner notified |
| NOISE-5546-C | Missing required attributes | Escalated to data steward |
| NOISE-9802-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2922-F | Data quality insufficient | Manual review scheduled |
| NOISE-4267-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5894-A | Missing required attributes | Business owner notified |
| NOISE-1709-E | Out of scope per business decision | Manual review scheduled |
| NOISE-6040-B | Missing required attributes | Business owner notified |
| NOISE-5365-A | Missing required attributes | Escalated to data steward |
| NOISE-9465-G | Data quality insufficient | Business owner notified |
| NOISE-2202-F | Pending validation | Deferred to Phase 2 |
| NOISE-1179-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3694-B | Out of scope per business decision | Business owner notified |
| NOISE-4211-A | Duplicate source record | Business owner notified |
| NOISE-8058-G | Missing required attributes | Business owner notified |
| NOISE-8337-A | Missing required attributes | Manual review scheduled |
| NOISE-2848-C | Data quality insufficient | Manual review scheduled |
| NOISE-4544-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8554-E | Out of scope per business decision | Manual review scheduled |
| NOISE-2451-F | Pending validation | Business owner notified |
| NOISE-8135-F | Missing required attributes | Manual review scheduled |
| NOISE-2665-E | Data quality insufficient | Manual review scheduled |
| NOISE-7448-C | Data quality insufficient | Escalated to data steward |
| NOISE-6579-D | Missing required attributes | Manual review scheduled |
| NOISE-7923-A | Data quality insufficient | Business owner notified |
| NOISE-5169-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6317-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7334-H | Duplicate source record | Business owner notified |
| NOISE-2647-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9481-D | Out of scope per business decision | Business owner notified |
| NOISE-5854-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-4058-F | Missing required attributes | Escalated to data steward |
| NOISE-5408-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-7334-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6028-H | Duplicate source record | Manual review scheduled |
| NOISE-2844-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-2186-H | Pending validation | Escalated to data steward |
| NOISE-4298-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9556-H | Missing required attributes | Manual review scheduled |
| NOISE-9978-H | Data quality insufficient | Escalated to data steward |
| NOISE-8255-F | Missing required attributes | Escalated to data steward |
| NOISE-6524-H | Data quality insufficient | Deferred to Phase 2 |


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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230607_000000`
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
| Technical Lead | Sarah Chen (Data Governance) | sarah@company.com | +1-555-0102 |
| Business Owner | James Wilson (Finance) | james@company.com | +1-555-0103 |
| Data Steward | David Kim (Project Management) | david@company.com | +1-555-0104 |

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
