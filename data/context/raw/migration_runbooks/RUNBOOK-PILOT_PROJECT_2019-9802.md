# Migration Runbook: System Migration: PILOT_PROJECT_2019

**Document ID**: RB-PILOT_PROJECT_2019-2395
**Version**: 2.4
**Last Updated**: 2023-07-30
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the System Migration: PILOT_PROJECT_2019 project.
The migration involves transitioning master data and transactional records from SOURCE
to TARGET while maintaining data integrity and business continuity.

**Project Timeline**: 2023-05-08 to 2023-09-09
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
| Total entities assessed | 1473 | Completed |
| Codes assigned | 1033 | Staged |
| Excluded from scope | 309 | Documented |
| Pending review | 5 | In Progress |

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
| Apex Chemicals Corp. | BC-8287 | 2022-07-12 | Data Governance |
| CO-OI-98-890 | IC-8289 | 2023-03-08 | Finance |
| SIG-70-MMO-95UC | BC-8308 | 2024-05-20 | Finance |
| SO-IS-25-323 | TC-8314 | 2021-05-25 | Compliance |
| rapeseed oil tech grade | IC-8324 | 2022-08-03 | Product Management |
| Nordic Distribution | TC-8346 | 2023-11-25 | Product Management |
| Excise IN 25% | BC-8348 | 2021-11-22 | Compliance |
| PO-SO-50-GR-B-154 | BC-8363 | 2024-09-12 | Product Management |
| Pinnacle Werkstoffe SARL | BC-8377 | 2022-11-22 | Product Management |
| citric acid 99.5% | BC-8404 | 2023-08-20 | IT Infrastructure |
| SIG-40-CXK-QT2E Group | BC-8410 | 2021-11-09 | Supply Chain |
| PE-PR-PR-564 | TC-8432 | 2021-11-05 | Operations |
| Zitronensäure Technische Qualität | TC-8455 | 2024-04-12 | Data Governance |
| SIG-26-WVS-AQ3B | IC-8468 | 2021-05-18 | Finance |
| citric acid | TC-8493 | 2022-03-26 | Product Management |
| Vat Standard CN 10% | TC-8498 | 2023-03-15 | Data Governance |
| PO-SO-50-TE-497 | TC-8506 | 2023-05-14 | Compliance |
| Continental Solutions | BC-8511 | 2021-08-12 | Data Governance |
| Customs Duty FR 19% | IC-8513 | 2022-08-01 | Finance |
| SIG-67-MFU-QOZ9 Group | TC-8530 | 2024-06-27 | Data Governance |
| Fructose Grade A | BC-8553 | 2022-10-15 | Operations |
| SIG-44-FWT-OA3N | BC-8564 | 2022-07-10 | Operations |
| CA-CA-947 | BC-8573 | 2023-10-25 | Supply Chain |
| Elite Handel Corp. | IC-8576 | 2021-07-24 | Data Governance |
| SIG-13-SXA-38WM | IC-8590 | 2024-07-14 | Product Management |
| Nordic Distribution | IC-8599 | 2024-05-09 | Supply Chain |
| vat standard us 19% | IC-8606 | 2022-11-19 | Product Management |
| prism ingredients | IC-8625 | 2021-07-06 | Finance |
| SIG-25-VPE-TOC1 | TC-8628 | 2023-06-12 | Compliance |
| CY-577 | IC-8634 | 2021-01-28 | IT Infrastructure |
| Cyclodextrin Premiumqualität | IC-8642 | 2021-01-22 | Product Management |
| Cyclodextrin Qualitätsstufe I | IC-8678 | 2021-08-03 | Data Governance |
| PR-IN-149 Holdings | BC-8709 | 2021-06-24 | Product Management |
| Pinnacle Rohstoffe NV | IC-8778 | 2024-10-18 | Supply Chain |
| SIG-76-GDP-2JN8 | BC-8782 | 2022-06-10 | IT Infrastructure |
| Atlas Versorgung GmbH | BC-8822 | 2023-11-05 | Product Management |
| CO-SO-101 | BC-8839 | 2024-04-05 | Product Management |
| Resistente Stärke Pharmazeutisch rein | IC-8851 | 2024-09-19 | Operations |
| GL-LO-935 | TC-8902 | 2023-06-05 | Finance |
| SIG-40-CXK-QT2E Group | IC-8915 | 2023-10-23 | Supply Chain |
| DE-PH-GR-173 | BC-8924 | 2022-08-07 | Product Management |
| SO-IS-50-GR-B-983 | TC-8991 | 2021-09-19 | Supply Chain |
| VA-ST-N-5-192 | TC-9012 | 2023-12-10 | Product Management |
| Citric Acid 70% Food Grade | IC-9017 | 2024-07-15 | Finance |
| SIG-13-ZIB-S8MV International | IC-9025 | 2021-10-25 | Operations |
| Isoglucose 70% | TC-9031 | 2024-11-27 | Finance |
| SIG-56-CMM-ODF7 | BC-9053 | 2022-09-14 | Operations |
| Vat Reduced GB 21% | BC-9058 | 2023-10-15 | Data Governance |
| atlantic supply | IC-9085 | 2021-07-23 | IT Infrastructure |
| Dextrin 50% | IC-9090 | 2022-05-08 | Operations |
| Lactic Acid 50% Premiumqualität | BC-9106 | 2024-05-22 | Operations |
| GL-IN-746 LLC | TC-9119 | 2022-11-13 | Compliance |
| Baltic Versorgung GmbH | TC-9158 | 2024-01-06 | Data Governance |
| PR-IN-409 LLC | IC-9161 | 2024-01-12 | Product Management |
| atlas logistics | IC-9164 | 2021-08-12 | Compliance |
| SIG-64-VUE-OGQ2 | IC-9165 | 2023-02-08 | Finance |
| Kasein 98% | IC-9202 | 2023-05-11 | Data Governance |
| CI-AC-PH-GR-209 | BC-9211 | 2023-05-16 | Compliance |
| Soja Isolate Premiumqualität | BC-9213 | 2021-12-01 | Data Governance |
| ST-LO-637 | TC-9215 | 2021-01-13 | Data Governance |
| Soja Isolate Lebensmittelrein | IC-9231 | 2022-09-21 | Data Governance |
| Apex Chemicals | IC-9235 | 2023-05-07 | Compliance |
| Prime Enterprise Holdings | TC-9249 | 2023-08-07 | IT Infrastructure |
| Kaliumsorbat | IC-9267 | 2024-12-10 | Product Management |
| Quantum Commodities PLC | IC-9269 | 2024-10-28 | Data Governance |
| Glukosesirup Syrup 99.5% Qualitätsstufe II | IC-9280 | 2022-02-04 | Compliance |
| Central Partners Corp. | IC-9284 | 2021-10-04 | Compliance |
| Lactic Acid | IC-9289 | 2021-02-12 | Compliance |
| SIG-87-SQR-587P | IC-9300 | 2024-02-03 | Operations |
| Elite Logistics Holdings | IC-9314 | 2021-10-02 | Data Governance |
| Coconut Oil 25% | TC-9316 | 2021-02-03 | IT Infrastructure |
| SIG-50-CEU-F5QB | BC-9333 | 2024-06-08 | Data Governance |
| LA-AC-70-781 | IC-9344 | 2021-02-04 | Finance |
| SIG-79-HKV-T268 | BC-9353 | 2022-10-28 | Data Governance |
| CO-OI-98-876 | TC-9374 | 2023-09-26 | Product Management |
| Pinnacle Supply International | IC-9375 | 2024-10-17 | IT Infrastructure |
| SIG-29-KJI-GJKC | BC-9413 | 2023-07-23 | Supply Chain |
| Excise NL 20% | BC-9414 | 2022-12-16 | Finance |
| Sorbinsäure 50% Lebensmittelrein | IC-9460 | 2023-01-23 | Operations |
| Elite Versorgung SA | IC-9461 | 2021-05-27 | Supply Chain |
| Coconut Oil Pharma Grade | BC-9490 | 2024-09-23 | Finance |
| maltodextrin de25 | TC-9518 | 2024-05-23 | Supply Chain |
| Pinnacle Logistics International | IC-9534 | 2021-10-27 | IT Infrastructure |
| Traubenzucker Qualitätsstufe I | BC-9544 | 2022-05-28 | Supply Chain |
| wheat gluten food grade | IC-9559 | 2021-01-11 | Compliance |
| DE-99.5-ST-905 | BC-9578 | 2024-11-22 | IT Infrastructure |
| nexus enterprise | IC-9580 | 2022-08-17 | Operations |
| catalyst enterprise | IC-9582 | 2024-06-04 | Finance |
| Catalyst Materials | IC-9593 | 2022-03-28 | Data Governance |
| prime supply | BC-9602 | 2023-09-21 | Operations |
| potassium sorbate 50% tech grade | IC-9624 | 2021-11-17 | Finance |
| Lactic Acid 98% | BC-9627 | 2021-11-12 | Data Governance |
| SU-OI-98-462 | BC-9630 | 2021-01-16 | IT Infrastructure |
| Global Versorgung | BC-9643 | 2022-08-27 | Finance |
| SIG-84-DSO-4S47 | TC-9685 | 2022-03-07 | Operations |
| SIG-58-SVK-Z948 | TC-9689 | 2023-02-17 | Supply Chain |
| SIG-96-FYH-4ROJ SARL | TC-9697 | 2023-06-15 | Compliance |
| SIG-66-ZOH-E8TV | TC-9700 | 2023-06-23 | Finance |
| nordic sourcing | IC-9717 | 2024-12-13 | Operations |
| Vat Standardqualität DE 25% | TC-9737 | 2024-11-18 | Finance |
| Ascorbic Acid 70% | BC-9782 | 2021-12-06 | Supply Chain |
| SIG-69-OFZ-JW34 | IC-9795 | 2021-04-28 | Data Governance |
| SIG-20-UMV-LJM6 | IC-9798 | 2024-10-16 | Supply Chain |
| PA-OI-25-GR-A-241 | IC-9800 | 2023-06-10 | Supply Chain |
| Vanguard Werkstoffe | TC-9824 | 2024-11-28 | Supply Chain |
| SIG-68-KHP-8RTJ | TC-9828 | 2024-01-02 | Data Governance |
| Zitronensäure Standardqualität | BC-9838 | 2022-12-01 | Compliance |
| SU-OI-FO-GR-778 | TC-9845 | 2024-05-18 | Compliance |
| ZE-PA-511 PLC | TC-9883 | 2023-08-05 | Data Governance |
| SIG-29-XAN-WDDA | TC-9885 | 2021-11-15 | Product Management |
| SIG-13-WHV-DDIN | TC-9887 | 2021-03-16 | Data Governance |
| casein | IC-9894 | 2022-11-10 | IT Infrastructure |
| SIG-39-BHZ-K8SS | TC-9903 | 2023-07-07 | Finance |
| SIG-95-HLU-HD5X GmbH | TC-9945 | 2022-10-01 | Data Governance |
| Wheat Gluten | IC-9947 | 2022-12-04 | Product Management |
| SIG-53-MHB-8KZX | IC-9950 | 2022-02-20 | Compliance |
| SO-IS-PR-242 | BC-9955 | 2021-05-01 | Supply Chain |
| Vat Reduced BR 10% | BC-9972 | 2022-10-25 | Product Management |
| SIG-52-JJF-4GXO International | TC-9975 | 2024-04-18 | IT Infrastructure |
| Dextrose | TC-9995 | 2021-09-01 | Data Governance |
| GL-SY-98-FO-GR-198 | TC-10021 | 2021-05-07 | Finance |
| pea protein standard | BC-10040 | 2024-01-06 | Operations |
| PA-LO-382 Group | TC-10065 | 2021-01-04 | Data Governance |
| Pacific Vertrieb Group | IC-10068 | 2022-01-05 | Supply Chain |
| Casein Grade A | TC-10078 | 2022-02-09 | IT Infrastructure |
| dextrose standard | TC-10081 | 2023-01-24 | Supply Chain |
| Fructose | IC-10094 | 2022-04-28 | Product Management |
| EX-I-19-464 | TC-10107 | 2021-06-23 | Product Management |
| SIG-99-TBJ-83YG KG | IC-10109 | 2023-01-02 | IT Infrastructure |
| Sorbinsäure 98% | BC-10118 | 2021-02-05 | Supply Chain |
| central sourcing | IC-10128 | 2022-12-13 | Compliance |
| nexus supply | BC-10135 | 2022-10-27 | Product Management |
| Weizenklebereiweiß | TC-10158 | 2021-12-25 | Product Management |
| QU-TR-440 | IC-10166 | 2021-09-09 | Product Management |
| sunflower oil standard | BC-10182 | 2023-03-07 | Compliance |
| SO-CH-98-GR-B-961 | TC-10192 | 2023-08-23 | Compliance |
| SIG-92-RHW-233J | TC-10194 | 2022-02-08 | Product Management |
| Casein | IC-10198 | 2023-03-06 | Operations |
| ME-LO-731 | IC-10202 | 2021-09-23 | IT Infrastructure |
| SIG-60-RUC-CU6A | IC-10207 | 2021-11-05 | Finance |
| pinnacle supply | TC-10264 | 2021-12-21 | Finance |
| SIG-69-UAZ-1ODW | IC-10267 | 2022-09-20 | Finance |
| SIG-43-GRJ-P3HT | IC-10270 | 2022-10-14 | Finance |
| SIG-89-HLJ-NILC | IC-10274 | 2023-05-19 | Operations |
| lactic acid 70% | TC-10296 | 2023-11-27 | Compliance |
| Palmfett | TC-10301 | 2021-08-21 | Operations |
| Sonnenblumenöl 70% | BC-10356 | 2022-05-28 | Data Governance |
| SIG-35-SZU-VMRU | BC-10379 | 2021-12-03 | IT Infrastructure |
| SIG-83-TNT-G0Q1 AG | IC-10386 | 2022-07-28 | Finance |
| SIG-39-BAT-DD7R | IC-10405 | 2024-05-15 | IT Infrastructure |
| Vanguard Logistik | BC-10407 | 2023-04-15 | Finance |
| maltodextrin de10 | IC-10444 | 2021-05-17 | Supply Chain |
| Soy Isolate | BC-10451 | 2022-04-10 | Data Governance |
| LA-AC-471 | IC-10455 | 2022-01-06 | Finance |
| Natriumchlorid 98% | BC-10458 | 2022-07-14 | Supply Chain |
| SIG-42-BEO-614U | TC-10468 | 2022-10-24 | Operations |
| Maltodextrin DE15 | TC-10477 | 2023-06-25 | Operations |
| Palmfett | IC-10485 | 2021-03-26 | Data Governance |
| nexus logistics | IC-10489 | 2023-03-26 | Data Governance |
| fructose standard | IC-10501 | 2021-04-17 | Data Governance |
| DE-GR-A-351 | BC-10505 | 2024-02-05 | Product Management |
| Natriumbenzoat 99.5% | TC-10528 | 2021-12-12 | Data Governance |
| FR-GR-A-600 | TC-10537 | 2022-01-09 | Finance |
| casein 98% standard | IC-10545 | 2021-02-25 | IT Infrastructure |
| lactic acid standard | BC-10551 | 2021-07-17 | Finance |
| SIG-47-HDT-7PPC | BC-10557 | 2024-11-05 | Operations |
| PA-SO-270 | IC-10561 | 2023-01-14 | Supply Chain |
| SIG-85-PGT-NQA4 | BC-10576 | 2023-07-12 | Operations |
| Stellar Werkstoffe | IC-10582 | 2024-09-15 | Supply Chain |
| SIG-47-NVU-R3XU | BC-10592 | 2021-06-01 | Operations |
| CU-DU-N-15-558 | TC-10607 | 2024-09-18 | Finance |
| Natriumchlorid Technische Qualität | TC-10612 | 2021-12-17 | IT Infrastructure |
| ST-CO-650 International | BC-10616 | 2021-03-07 | Operations |
| PO-SO-50-GR-B-154 | BC-10631 | 2022-06-22 | IT Infrastructure |
| Atlas Industrien International | IC-10636 | 2021-03-14 | Operations |
| Premier Logistik KG | BC-10642 | 2022-05-26 | Finance |
| Customs Duty FR 25% | BC-10648 | 2024-01-05 | Supply Chain |
| SIG-82-ZXL-FF30 International | TC-10656 | 2021-04-08 | Operations |
| vanguard supply NV | IC-10675 | 2021-09-23 | Finance |
| Soy Isolate 99.5% Standard | IC-10683 | 2023-11-23 | Data Governance |
| AP-TR-161 International | TC-10700 | 2024-12-13 | Supply Chain |
| Fructose Qualitätsstufe II | TC-10704 | 2023-04-24 | IT Infrastructure |
| QU-TR-219 International | TC-10715 | 2023-08-23 | Supply Chain |
| ascorbic acid | IC-10724 | 2023-08-13 | Finance |
| Atlantic Materials | BC-10726 | 2021-12-07 | Compliance |
| Sodium Chloride | BC-10728 | 2024-02-04 | Finance |
| SIG-41-OMW-SN1T | IC-10730 | 2022-05-16 | Finance |
| CE-PR-134 | TC-10732 | 2021-03-11 | Product Management |
| withholding gb 21% | IC-10762 | 2021-04-16 | Compliance |
| sunflower oil 98% | IC-10766 | 2022-06-19 | Supply Chain |
| SO-BE-GR-B-936 | BC-10771 | 2022-09-24 | Finance |
| Vat Standard FR 20% | BC-10772 | 2024-07-16 | Product Management |
| SIG-35-SZU-VMRU | IC-10773 | 2023-05-25 | Operations |
| Isoglucose Technical | IC-10778 | 2021-06-09 | Product Management |
| SIG-35-BYM-BYQ7 Inc. | TC-10783 | 2022-04-22 | Product Management |
| Pea Protein Premiumqualität | BC-10787 | 2021-08-27 | Operations |
| Customs Duty FR 15% | IC-10789 | 2023-10-20 | Data Governance |
| Cyclodextrin 70% Food Grade | BC-10791 | 2024-10-08 | Data Governance |
| Sodium Benzoate 25% | TC-10801 | 2021-10-02 | Supply Chain |
| SIG-73-AXD-XIX9 | BC-10818 | 2022-08-16 | Finance |
| SO-CH-GR-B-273 | IC-10825 | 2021-10-24 | Compliance |
| palm oil 99.5% | BC-10830 | 2023-05-05 | Finance |
| Vanguard Sourcing | IC-10838 | 2022-02-04 | Operations |
| CO-CH-401 Inc. | BC-10864 | 2023-03-26 | Finance |
| Atlantic Industrien International | BC-10868 | 2022-09-19 | Supply Chain |
| SIG-44-UKH-MO4F | TC-10880 | 2023-08-16 | Compliance |
| Fructose Qualitätsstufe II | BC-10889 | 2024-03-06 | Compliance |
| SIG-75-GGJ-DK9O | TC-10897 | 2021-10-11 | Operations |
| SO-IS-50-568 | IC-10900 | 2022-12-09 | Operations |
| ST-SU-125 SA | BC-10921 | 2022-05-11 | Operations |
| Calcium Carbonate 99.5% Food Grade | TC-10968 | 2023-06-18 | Compliance |
| continental manufacturing Inc. | TC-10976 | 2021-09-13 | Supply Chain |
| Soja Isolate 98% Premiumqualität | BC-10981 | 2023-12-10 | IT Infrastructure |
| HO-LO-699 | TC-10985 | 2021-01-21 | Finance |
| WI-G-15-758 | TC-10990 | 2023-10-10 | Compliance |
| Ascorbic Acid 99.5% | IC-10993 | 2023-01-06 | Finance |
| SIG-57-GUP-S7UK | IC-11012 | 2024-08-25 | Data Governance |
| SIG-44-HTV-P84J | BC-11019 | 2022-09-11 | Data Governance |
| Premier Enterprise International | IC-11026 | 2023-04-28 | Data Governance |
| NE-EN-710 NV | IC-11040 | 2023-11-20 | IT Infrastructure |
| ST-SU-950 SAS | IC-11049 | 2023-04-16 | Finance |
| SIG-89-ISH-EQW6 | TC-11055 | 2024-10-27 | Supply Chain |
| calcium carbonate 50% pharma grade | TC-11067 | 2024-09-16 | Product Management |
| VA-ST-D-21-476 | TC-11080 | 2023-02-10 | Operations |
| SO-BE-99.5-ST-342 | TC-11083 | 2022-05-18 | Compliance |
| Vanguard Logistik International | IC-11085 | 2023-03-26 | Operations |
| Dextrin Qualitätsstufe II | IC-11096 | 2023-06-16 | IT Infrastructure |
| SIG-78-WDE-NNV9 | TC-11119 | 2021-06-10 | IT Infrastructure |
| Customs Duty BR 21% | TC-11162 | 2022-11-25 | Data Governance |
| GL-SY-371 | TC-11185 | 2022-07-07 | Compliance |
| Traubenzucker 99.5% | TC-11192 | 2024-12-28 | Compliance |
| sodium benzoate | IC-11194 | 2021-10-14 | Data Governance |
| palm oil standard | IC-11197 | 2022-08-15 | Data Governance |
| SO-AC-PR-928 | IC-11200 | 2022-03-21 | Data Governance |
| RA-OI-GR-A-980 | IC-11215 | 2022-07-04 | Data Governance |
| central materials BV | TC-11223 | 2024-12-12 | Operations |
| Palmfett 70% Technische Qualität | IC-11231 | 2023-11-10 | Compliance |
| Calcium Carbonate 98% | BC-11260 | 2021-08-15 | Supply Chain |
| Fructose Premiumqualität | BC-11280 | 2023-07-10 | IT Infrastructure |
| CI-AC-GR-A-813 | BC-11283 | 2021-01-06 | Operations |
| Baltic Rohstoffe Ltd. | IC-11284 | 2024-10-24 | Data Governance |
| LA-AC-FO-GR-469 | BC-11305 | 2023-02-28 | Compliance |
| SIG-65-RQH-9Y5B | IC-11313 | 2021-10-06 | Operations |
| EX-B-25-579 | TC-11338 | 2023-04-07 | Operations |
| Continental Solutions NV | TC-11345 | 2024-04-17 | Supply Chain |
| SIG-25-WCC-PPMH | TC-11359 | 2022-06-13 | Product Management |
| SIG-24-PBC-613L | TC-11363 | 2023-10-24 | Operations |
| SIG-49-UKY-6H3R | BC-11369 | 2021-08-09 | Data Governance |
| lactic acid 98% | IC-11400 | 2021-09-18 | Compliance |
| Soja Isolate 99.5% | TC-11407 | 2021-03-26 | Supply Chain |
| dextrin premium | IC-11409 | 2021-06-19 | Finance |
| customs duty fr 15% | TC-11440 | 2023-10-12 | Data Governance |
| QU-PR-732 SA | BC-11441 | 2024-05-11 | Operations |
| Sodium Benzoate 98% | IC-11449 | 2021-03-16 | Product Management |
| Maltodextrin DE15 Premium | BC-11480 | 2023-09-08 | Supply Chain |
| Customs Duty CN 10% | TC-11492 | 2023-04-10 | Compliance |
| SIG-99-IZM-CYBY | IC-11498 | 2021-09-18 | Operations |
| DE-PH-GR-173 | BC-11500 | 2023-02-08 | IT Infrastructure |
| Wheat Gluten 25% Food Grade | BC-11516 | 2021-08-02 | Compliance |
| citric acid | BC-11521 | 2021-06-13 | Compliance |
| Premier Trading Group | TC-11543 | 2024-08-21 | Compliance |
| Weizenklebereiweiß Qualitätsstufe II | BC-11564 | 2024-10-19 | IT Infrastructure |
| Soja Isolate Lebensmittelrein | BC-11574 | 2021-04-20 | Compliance |
| Sonnenblumenöl 50% Qualitätsstufe I | IC-11594 | 2024-04-01 | Data Governance |
| PE-PR-557 | TC-11598 | 2022-06-06 | Operations |
| Stratos Materials | TC-11604 | 2021-06-05 | Compliance |
| SIG-10-BLC-3L38 | TC-11625 | 2024-01-22 | IT Infrastructure |
| Baltic Industrien NV | BC-11640 | 2021-10-07 | Compliance |
| Glucose Syrup Technical | BC-11646 | 2022-06-15 | Data Governance |
| Calcium Carbonate | BC-11684 | 2024-11-28 | Finance |
| SIG-45-ZHK-QWIG | BC-11688 | 2023-07-04 | Compliance |
| SIG-15-VIS-079C | IC-11692 | 2024-05-28 | Finance |
| SIG-76-GDP-2JN8 | IC-11695 | 2023-04-14 | Compliance |
| SIG-83-TEU-OH8F Group | IC-11698 | 2023-07-22 | Finance |
| Fructose Technische Qualität | TC-11701 | 2023-02-07 | Compliance |
| Potassium Sorbate Standard | IC-11732 | 2024-06-19 | Data Governance |
| SIG-19-TLQ-1P5Z | IC-11736 | 2021-08-14 | Finance |
| SIG-44-NHM-IY9D | TC-11738 | 2023-04-28 | Supply Chain |
| SO-AC-GR-A-997 | TC-11740 | 2024-06-16 | Supply Chain |
| Rapeseed Oil Grade A | BC-11742 | 2022-12-18 | Product Management |
| cyclodextrin 70% food grade | BC-11746 | 2021-01-12 | IT Infrastructure |
| WI-F-10-935 | TC-11761 | 2023-12-23 | IT Infrastructure |
| CI-AC-ST-565 | IC-11764 | 2023-07-25 | Data Governance |
| Pinnacle Materials SA | IC-11773 | 2022-07-09 | Finance |
| excise in 7% | TC-11786 | 2022-11-14 | Compliance |
| Sodium Chloride | TC-11790 | 2021-08-21 | Compliance |
| SIG-71-OEX-5BRF | BC-11791 | 2022-11-15 | Compliance |
| SIG-16-YRD-5C3Z | IC-11807 | 2023-06-18 | Product Management |
| SIG-43-TPO-RSBY | BC-11808 | 2024-02-17 | Operations |
| SIG-92-CZO-O9ON | IC-11814 | 2022-04-21 | Compliance |
| Pacific Vertrieb International | TC-11818 | 2023-01-01 | Operations |
| SIG-76-PYX-S5PY | IC-11840 | 2023-06-07 | Supply Chain |
| Ascorbic Acid Premiumqualität | IC-11851 | 2023-09-14 | Operations |
| Cyclodextrin | IC-11855 | 2023-11-10 | IT Infrastructure |
| Resistant Starch Pharma Grade | TC-11886 | 2023-07-05 | Product Management |
| calcium carbonate | BC-11919 | 2024-09-15 | Operations |
| Global Logistics | TC-11954 | 2022-03-24 | Data Governance |
| SIG-58-JZY-SBU1 | IC-12006 | 2021-12-22 | Finance |
| Vertex Sourcing | TC-12022 | 2021-01-01 | Compliance |
| coconut oil 70% | TC-12047 | 2021-06-09 | Compliance |
| Kaliumsorbat | BC-12048 | 2024-02-24 | Product Management |
| SO-CH-GR-B-273 | IC-12055 | 2022-02-21 | Finance |
| dextrin standard | TC-12057 | 2023-07-22 | IT Infrastructure |
| Sorbinsäure Qualitätsstufe II | IC-12060 | 2022-05-03 | Compliance |
| SIG-86-VGU-A4FE | TC-12065 | 2021-04-25 | IT Infrastructure |
| Lactic Acid 25% | IC-12076 | 2024-11-02 | Supply Chain |
| SIG-46-SVJ-5IZO | BC-12091 | 2024-01-26 | Data Governance |
| Wheat Gluten 50% Pharma Grade | IC-12100 | 2024-03-02 | IT Infrastructure |
| SIG-64-ILX-G2AZ PLC | IC-12102 | 2021-09-18 | Finance |
| Nordic Chemicals BV | IC-12104 | 2024-11-27 | Data Governance |
| Sodium Chloride 25% Food Grade | IC-12107 | 2024-07-16 | Compliance |
| SIG-32-UBB-EMYO | BC-12121 | 2023-09-04 | Product Management |
| CA-98-TE-238 | TC-12126 | 2023-09-07 | Operations |
| SIG-79-DVU-H9H4 | TC-12128 | 2023-05-05 | Supply Chain |
| wheat gluten 70% | BC-12132 | 2021-04-24 | Data Governance |
| ST-LO-635 LLC | TC-12135 | 2024-06-26 | Finance |
| CY-763 | IC-12139 | 2024-08-11 | Product Management |
| SIG-39-OZI-N968 | BC-12143 | 2024-03-28 | IT Infrastructure |
| Lactic Acid Lebensmittelrein | BC-12145 | 2024-06-22 | Supply Chain |
| Maltodextrin-Pulver DE30 | BC-12153 | 2023-09-06 | IT Infrastructure |
| WH-GL-FO-GR-876 | TC-12155 | 2023-09-06 | Operations |
| Lactic Acid 98% Grade A | TC-12162 | 2021-05-24 | Data Governance |
| SIG-35-TKX-8TRE | BC-12163 | 2023-10-08 | Product Management |
| catalyst supply Holdings | IC-12166 | 2022-07-12 | Compliance |
| SIG-78-QOY-5RIX | IC-12193 | 2022-08-25 | Supply Chain |
| SIG-30-NQN-ZENP | BC-12228 | 2022-06-07 | IT Infrastructure |
| Rapeseed Oil | BC-12239 | 2024-08-27 | IT Infrastructure |
| Natriumchlorid Technische Qualität | BC-12280 | 2022-05-02 | Data Governance |
| SIG-99-TBJ-83YG KG | IC-12293 | 2024-05-16 | Product Management |
| Weizenklebereiweiß Qualitätsstufe II | BC-12330 | 2024-07-16 | Data Governance |
| Vertex Materials | BC-12357 | 2023-04-14 | Finance |
| SIG-27-UKP-V2ME | TC-12364 | 2024-11-09 | Finance |
| CA-CA-98-PH-GR-242 | IC-12377 | 2024-04-04 | IT Infrastructure |
| Withholding BR 20% | BC-12386 | 2021-09-22 | Supply Chain |
| resistant starch 70% food grade | BC-12391 | 2024-09-04 | Compliance |
| Ascorbic Acid | IC-12407 | 2022-11-14 | IT Infrastructure |
| Isoglucose Grade B | BC-12415 | 2024-06-27 | Finance |
| AS-AC-ST-686 | TC-12428 | 2024-01-15 | Supply Chain |
| sorbic acid premium | TC-12430 | 2024-04-08 | Data Governance |
| CO-MA-127 Group | TC-12444 | 2024-12-13 | IT Infrastructure |
| Palm Oil Grade B | TC-12449 | 2022-04-16 | Data Governance |
| glucose syrup food grade | BC-12464 | 2021-11-27 | Finance |
| Global Enterprise NV | TC-12471 | 2022-02-09 | Operations |
| RA-OI-GR-B-834 | BC-12475 | 2023-12-06 | Operations |
| Sorbinsäure 50% Standardqualität | BC-12491 | 2024-12-10 | Supply Chain |
| Horizon Rohstoffe PLC | TC-12494 | 2022-02-11 | Operations |
| cyclodextrin | TC-12504 | 2024-04-25 | Data Governance |
| SIG-71-PGT-OFPC | BC-12506 | 2022-12-06 | Compliance |
| prism ingredients NV | TC-12525 | 2024-11-16 | Finance |
| Catalyst Enterprise International | IC-12526 | 2021-06-05 | Supply Chain |
| Nexus Materials | TC-12531 | 2023-04-12 | IT Infrastructure |
| Core Werkstoffe | BC-12544 | 2023-02-13 | Compliance |
| Vat Reduced CN 19% | BC-12558 | 2023-05-14 | Supply Chain |
| Vertex Sourcing | BC-12561 | 2022-09-05 | Data Governance |
| SIG-29-KJI-GJKC | IC-12578 | 2022-10-28 | Supply Chain |
| Horizon Materials | BC-12604 | 2023-10-18 | Operations |
| Baltic Verarbeitung Group | IC-12605 | 2022-01-26 | Supply Chain |
| Soy Isolate | BC-12623 | 2023-03-12 | Supply Chain |
| Prime Versorgung | IC-12627 | 2022-10-22 | Compliance |
| coconut oil 25% tech grade | IC-12634 | 2022-12-15 | Product Management |
| SIG-17-LVE-03G9 | BC-12637 | 2022-12-14 | Supply Chain |
| LA-AC-554 | BC-12639 | 2023-12-03 | Finance |
| Global Chemicals Ltd. | BC-12650 | 2021-12-02 | Data Governance |
| vertex ingredients PLC | BC-12665 | 2021-09-18 | Operations |
| Central Sourcing | TC-12678 | 2022-10-06 | Finance |
| SO-AC-25-GR-B-198 | BC-12684 | 2022-10-12 | Supply Chain |
| SIG-76-GST-OWGM | BC-12705 | 2023-01-13 | Supply Chain |
| Natriumbenzoat 50% | IC-12719 | 2021-09-20 | Compliance |
| Isoglucose | IC-12763 | 2024-06-06 | IT Infrastructure |
| Natriumbenzoat | TC-12767 | 2023-04-12 | Finance |
| ME-MA-989 | BC-12770 | 2024-06-19 | Finance |
| SIG-23-OPT-7QHV | TC-12771 | 2023-07-14 | IT Infrastructure |
| Pea Protein | BC-12776 | 2022-03-22 | Operations |
| SIG-36-BVE-5U7D | BC-12796 | 2021-07-16 | Finance |
| PR-SO-102 | IC-12802 | 2024-10-16 | Compliance |
| Pacific Supply Co. | BC-12803 | 2024-08-20 | Finance |
| Core Partners | IC-12815 | 2021-12-12 | Finance |
| SO-CH-70-GR-B-821 | BC-12822 | 2021-02-10 | Finance |
| nexus chemicals Group | TC-12849 | 2023-06-08 | Supply Chain |
| Vanguard Handel LLC | IC-12872 | 2024-11-25 | Compliance |
| resistant starch 50% | IC-12876 | 2021-01-02 | Product Management |
| SIG-58-NYA-2O4M | TC-12879 | 2023-08-11 | Product Management |
| SO-AC-25-GR-B-198 | TC-12894 | 2021-06-09 | Finance |
| sorbic acid pharma grade | TC-12895 | 2024-03-25 | Data Governance |
| SIG-98-CGL-FHWJ | IC-12898 | 2021-04-22 | Finance |
| Baltic Versorgung GmbH | BC-12917 | 2021-07-06 | Compliance |
| PR-SO-632 | IC-12920 | 2023-01-11 | IT Infrastructure |
| Central Versorgung GmbH | TC-12929 | 2021-03-12 | Finance |
| dextrose 99.5% | BC-12938 | 2024-08-25 | IT Infrastructure |
| SIG-55-OPY-GVTN | BC-12944 | 2022-05-10 | IT Infrastructure |
| Sodium Benzoate 50% Technical | BC-12958 | 2024-09-09 | Supply Chain |
| SIG-62-GUN-FTYL | TC-12964 | 2021-04-08 | Compliance |
| EX-B-21-936 | BC-12968 | 2024-09-15 | Product Management |
| DE-99.5-720 | IC-12970 | 2021-03-16 | Product Management |
| SIG-94-TOI-OFNK | BC-12989 | 2021-08-05 | Compliance |
| CA-CA-70-883 | BC-13014 | 2023-01-01 | Product Management |
| casein standard | BC-13023 | 2021-02-15 | Product Management |
| SU-OI-ST-338 | IC-13027 | 2024-07-06 | IT Infrastructure |
| SIG-56-ZVH-GATJ | TC-13055 | 2023-10-03 | Finance |
| FR-99.5-FO-GR-963 | IC-13060 | 2022-12-26 | Supply Chain |
| baltic trading NV | BC-13064 | 2023-08-22 | Compliance |
| Stratos Werkstoffe | IC-13070 | 2024-10-15 | IT Infrastructure |
| SIG-75-QRF-XA0H | TC-13092 | 2022-02-13 | Supply Chain |
| Glukosesirup Syrup Premiumqualität | BC-13095 | 2021-09-16 | Operations |
| Zenith Versorgung GmbH | TC-13110 | 2024-12-25 | Operations |
| DE-TE-406 | BC-13114 | 2024-11-14 | Data Governance |
| Dextrin Technische Qualität | IC-13119 | 2024-03-07 | Data Governance |
| SIG-55-DCV-7OXN | BC-13124 | 2022-03-08 | Operations |
| SIG-61-HXH-PFBC | TC-13131 | 2021-07-02 | Compliance |
| SIG-12-IYC-8W63 Holdings | TC-13134 | 2022-04-10 | IT Infrastructure |
| Citric Acid Grade B | TC-13152 | 2024-03-16 | IT Infrastructure |
| SIG-74-EPP-R9AG | TC-13157 | 2024-04-09 | Data Governance |
| Palmfett Standardqualität | BC-13163 | 2023-08-25 | Finance |
| Catalyst Supply Holdings | BC-13168 | 2022-05-06 | IT Infrastructure |
| sorbic acid 50% | TC-13169 | 2023-10-09 | Product Management |
| Horizon Partners Ltd. | BC-13176 | 2021-11-03 | Data Governance |
| Elite Logistics Holdings | TC-13191 | 2023-02-07 | Product Management |
| Potassium Sorbate 50% | TC-13194 | 2021-08-16 | Finance |
| SIG-23-BLM-EZKX | BC-13209 | 2022-08-03 | Product Management |
| BA-SU-CO-430 | IC-13214 | 2024-02-28 | Data Governance |
| Sodium Benzoate 98% | BC-13225 | 2024-02-12 | Operations |
| Premier Supply Co. | IC-13233 | 2024-03-08 | Operations |
| SIG-78-WDE-NNV9 | BC-13249 | 2023-01-08 | Finance |
| RA-OI-FO-GR-269 | TC-13272 | 2021-09-25 | Data Governance |
| Traubenzucker Qualitätsstufe I | TC-13300 | 2022-07-01 | Supply Chain |
| Baltic Verarbeitung Group | BC-13302 | 2023-05-08 | Data Governance |
| fructose | IC-13309 | 2022-02-01 | Product Management |
| Pea Protein 99.5% | TC-13320 | 2021-04-17 | Product Management |
| SIG-37-JCQ-RB0M | BC-13326 | 2024-09-06 | Finance |
| SIG-92-FQW-WCF5 SARL | TC-13332 | 2024-07-20 | Product Management |
| Pea Protein Technical | BC-13334 | 2023-10-27 | Compliance |
| Casein 98% Technical | IC-13339 | 2023-09-10 | Compliance |
| Prism Manufacturing | IC-13382 | 2024-04-12 | Data Governance |
| SIG-38-BKW-2ZX1 | IC-13383 | 2023-01-28 | Supply Chain |
| maltodextrin de25 | IC-13414 | 2021-12-04 | Operations |
| Baltic Versorgung GmbH | BC-13418 | 2023-04-23 | IT Infrastructure |
| Resistente Stärke Pharmazeutisch rein | IC-13419 | 2022-07-20 | Data Governance |
| Dextrin | IC-13430 | 2024-02-28 | Compliance |
| Customs Duty DE 0% | BC-13432 | 2024-09-05 | Product Management |
| Fructose 50% Standard | IC-13445 | 2023-08-16 | Finance |
| Meridian Materials | BC-13466 | 2023-03-04 | Product Management |
| calcium carbonate | BC-13472 | 2023-12-02 | Finance |
| NE-DI-555 | IC-13483 | 2023-07-03 | Finance |
| CU-DU-N-21-524 | TC-13495 | 2023-10-15 | Operations |
| Vat Standardqualität CN 0% | BC-13496 | 2021-02-08 | Finance |
| Natriumchlorid 25% Premiumqualität | TC-13497 | 2022-03-15 | Product Management |
| SO-IS-99.5-PR-187 | IC-13501 | 2023-11-10 | Operations |
| SIG-16-JKI-B4JG | BC-13512 | 2022-11-06 | Data Governance |
| Glukosesirup Syrup 98% | BC-13517 | 2023-12-08 | Compliance |
| SIG-16-YRD-5C3Z | BC-13529 | 2022-05-07 | Product Management |
| ascorbic acid tech grade | BC-13546 | 2023-02-12 | Operations |
| SIG-49-QVY-JMMU | BC-13563 | 2021-08-12 | Product Management |
| Zitronensäure Standardqualität | IC-13567 | 2023-06-20 | Finance |
| Central Werkstoffe | IC-13580 | 2021-02-04 | Data Governance |
| PA-OI-383 | IC-13587 | 2021-04-21 | Supply Chain |
| Fructose Qualitätsstufe I | BC-13593 | 2021-05-13 | Data Governance |
| Palmfett | IC-13597 | 2021-03-26 | Operations |
| SIG-19-TPS-MSKY | TC-13645 | 2022-04-22 | Operations |
| PO-SO-632 | TC-13661 | 2023-12-13 | Supply Chain |
| Pacific Versorgung GmbH | IC-13664 | 2023-01-06 | Finance |
| Rapsöl 98% Standardqualität | TC-13668 | 2022-03-15 | Finance |
| Prism Distribution BV | IC-13672 | 2022-01-27 | Data Governance |
| fructose 99.5% tech grade | IC-13686 | 2022-05-22 | Finance |
| Palmfett | BC-13691 | 2021-09-03 | Compliance |
| SIG-84-PAS-5S3O | IC-13701 | 2021-01-05 | Supply Chain |
| PI-LO-710 NV | IC-13707 | 2021-01-08 | Product Management |
| Cyclodextrin Standard | TC-13709 | 2024-02-07 | Product Management |
| Weizenklebereiweiß 25% Premiumqualität | BC-13717 | 2023-11-26 | Data Governance |
| Atlantic Materials | BC-13757 | 2023-07-07 | Operations |
| SIG-13-ZRN-WZGO | TC-13766 | 2022-08-20 | Product Management |
| Dextrose 99.5% | BC-13796 | 2022-10-26 | Data Governance |
| SIG-16-FQO-8S1S | BC-13818 | 2023-06-15 | Supply Chain |
| SIG-48-UJX-49KW | TC-13820 | 2024-06-13 | Compliance |
| ST-MA-342 | BC-13831 | 2021-04-28 | Product Management |
| AP-SU-CO-314 | BC-13843 | 2022-09-09 | Data Governance |
| Premier Rohstoffe Holdings | IC-13855 | 2023-04-03 | Supply Chain |
| Calcium Carbonate Qualitätsstufe II | BC-13858 | 2022-07-03 | Data Governance |
| Global Chemicals SAS | TC-13861 | 2021-10-09 | IT Infrastructure |
| Sorbic Acid Standard | BC-13874 | 2021-06-17 | Product Management |
| Central Logistik | BC-13884 | 2023-09-22 | Product Management |
| Resistant Starch Technical | BC-13886 | 2021-02-01 | Compliance |
| Stellar Supply Co. | BC-13915 | 2024-07-01 | Supply Chain |
| Apex Verarbeitung | TC-13957 | 2022-03-26 | Product Management |
| Atlas Supply Co. | TC-13971 | 2024-09-26 | Supply Chain |
| dextrose | TC-13986 | 2021-05-15 | Data Governance |
| Global Trading Ltd. | IC-14049 | 2023-05-26 | IT Infrastructure |
| Vanguard Logistics | BC-14050 | 2023-05-25 | IT Infrastructure |
| potassium sorbate 50% tech grade | TC-14077 | 2023-12-01 | Operations |
| sorbic acid | BC-14078 | 2022-11-16 | Data Governance |
| casein 25% tech grade | IC-14081 | 2024-12-04 | Operations |
| core chemicals Group | IC-14082 | 2021-11-23 | Data Governance |
| Atlantic Vertrieb Holdings | BC-14101 | 2022-07-09 | Supply Chain |
| vanguard enterprise | BC-14118 | 2021-01-24 | Product Management |
| SIG-97-XJT-7TBU | IC-14132 | 2024-08-04 | Product Management |
| Traubenzucker 99.5% | TC-14135 | 2022-09-16 | Product Management |
| ST-PR-265 Corp. | IC-14145 | 2023-01-14 | Compliance |
| CU-DU-D-20-742 | BC-14160 | 2023-10-28 | Product Management |
| Maltodextrin DE15 | IC-14191 | 2024-05-27 | Operations |
| GL-SY-GR-B-331 | TC-14206 | 2023-06-07 | Data Governance |
| Maltodextrin-Pulver DE15 Standardqualität | TC-14222 | 2024-07-02 | Operations |
| Pea Protein 25% Pharmazeutisch rein | IC-14223 | 2024-08-24 | Compliance |
| Horizon Materials | TC-14241 | 2022-03-13 | Supply Chain |
| sorbic acid 50% standard | TC-14251 | 2024-07-02 | Finance |
| LA-AC-70-PH-GR-221 | BC-14258 | 2022-06-13 | IT Infrastructure |
| prime processing AG | TC-14285 | 2022-12-11 | Product Management |
| Ascorbic Acid Premiumqualität | BC-14286 | 2023-11-07 | Operations |
| Catalyst Ingredients Holdings | TC-14294 | 2021-09-01 | Finance |
| CA-CA-GR-B-162 | TC-14307 | 2023-05-19 | Product Management |
| SIG-56-ZVH-GATJ | IC-14309 | 2022-09-01 | Finance |
| CO-OI-70-701 | TC-14315 | 2023-01-10 | IT Infrastructure |
| apex trading BV | BC-14317 | 2024-03-28 | Compliance |
| dextrose premium | TC-14321 | 2024-10-18 | Supply Chain |
| BA-IN-547 | IC-14340 | 2024-12-18 | IT Infrastructure |
| Global Chemicals Ltd. | BC-14352 | 2022-03-09 | Operations |
| Sodium Chloride | IC-14357 | 2021-12-16 | Operations |
| SIG-61-PIG-0DBF | IC-14365 | 2023-12-10 | Data Governance |
| Premier Logistics | IC-14373 | 2021-05-24 | Supply Chain |
| Pacific Werkstoffe | IC-14377 | 2024-10-25 | Supply Chain |
| Quantum Vertrieb Holdings | IC-14379 | 2021-02-23 | Operations |
| baltic sourcing | BC-14385 | 2021-12-15 | IT Infrastructure |
| dextrose 50% | TC-14406 | 2024-02-26 | Supply Chain |
| Glucose Syrup Food Grade | TC-14410 | 2021-06-24 | Operations |
| WH-GL-GR-A-924 | BC-14427 | 2021-05-22 | Finance |
| Dextrose | BC-14431 | 2023-01-24 | Operations |
| Rapsöl | BC-14437 | 2023-12-08 | Compliance |
| Natriumbenzoat 99.5% Qualitätsstufe I | BC-14441 | 2024-08-25 | Finance |
| Zitronensäure 70% | BC-14463 | 2022-04-08 | Finance |
| continental processing Group | IC-14478 | 2022-11-15 | Supply Chain |
| Casein | BC-14482 | 2024-06-25 | Finance |
| SO-IS-324 | BC-14484 | 2023-01-07 | Data Governance |
| Customs Duty GB 5% | TC-14493 | 2024-05-25 | Data Governance |
| prism chemicals | IC-14524 | 2021-06-24 | Compliance |
| Glucose Syrup 99.5% Grade B | TC-14530 | 2022-07-28 | Supply Chain |
| nexus distribution Corp. | TC-14546 | 2022-07-04 | IT Infrastructure |
| sodium benzoate | BC-14555 | 2021-11-02 | Compliance |
| DE-ST-712 | IC-14564 | 2023-12-05 | Data Governance |
| vat reduced nl 25% | TC-14592 | 2022-05-05 | Data Governance |
| SU-OI-GR-A-704 | TC-14630 | 2022-08-26 | Supply Chain |
| Vanguard Distribution | IC-14643 | 2022-09-15 | Product Management |
| GL-SY-533 | TC-14669 | 2023-07-16 | Product Management |
| SO-IS-PR-309 | TC-14703 | 2022-06-19 | Supply Chain |
| FR-PH-GR-146 | IC-14707 | 2023-11-11 | IT Infrastructure |
| Soy Isolate 50% Food Grade | TC-14720 | 2021-09-05 | Supply Chain |
| premier partners Group | BC-14730 | 2021-12-27 | IT Infrastructure |
| Soy Isolate 50% Grade B | BC-14733 | 2022-03-11 | Supply Chain |
| Global Enterprise NV | IC-14736 | 2022-03-04 | Supply Chain |
| Soja Isolate Premiumqualität | BC-14739 | 2021-03-18 | Operations |
| Global Ingredients NV | TC-14756 | 2021-10-03 | Product Management |
| Atlas Materials | BC-14780 | 2021-04-01 | Operations |
| palm oil | IC-14782 | 2023-06-23 | Finance |
| PR-SU-CO-333 | TC-14794 | 2021-09-28 | Supply Chain |
| Meridian Versorgung | TC-14834 | 2023-04-05 | Operations |
| Ascorbic Acid 98% Qualitätsstufe II | IC-14842 | 2023-01-18 | Compliance |
| Isoglucose 50% Qualitätsstufe I | IC-14846 | 2021-12-25 | Compliance |
| DE-FO-GR-588 | BC-14851 | 2022-05-23 | Data Governance |
| Fructose | IC-14891 | 2022-04-16 | Supply Chain |
| Coconut Oil 70% | TC-14905 | 2022-03-16 | Compliance |
| Lactic Acid Technical | BC-14916 | 2022-07-20 | Operations |
| Fructose Technical | IC-14921 | 2022-02-21 | Finance |
| SIG-92-VAB-1JHU | IC-14922 | 2022-11-26 | Operations |
| Weizenklebereiweiß | TC-14926 | 2022-05-13 | Operations |
| premier solutions Corp. | TC-14930 | 2023-06-14 | Data Governance |
| SIG-41-OMW-SN1T | TC-14935 | 2021-05-17 | IT Infrastructure |
| VA-RE-C-10-242 | TC-14937 | 2022-12-21 | IT Infrastructure |
| Dextrose | TC-14956 | 2021-07-23 | Product Management |
| PO-SO-70-GR-A-581 | IC-14980 | 2022-07-01 | Data Governance |
| palm oil | IC-14982 | 2022-08-07 | Compliance |
| SIG-40-PLP-7A3U | BC-14992 | 2024-10-11 | Product Management |
| SIG-86-VCP-SVOL | TC-14994 | 2022-09-10 | IT Infrastructure |
| Meridian Logistik | IC-15001 | 2024-04-02 | IT Infrastructure |
| Soy Isolate | TC-15003 | 2024-05-11 | Compliance |
| SIG-71-VGV-8K52 | TC-15007 | 2024-09-27 | IT Infrastructure |
| sorbic acid premium | IC-15009 | 2022-04-03 | Supply Chain |
| atlas supply | BC-15022 | 2022-03-22 | Supply Chain |
| ST-SU-323 Group | IC-15031 | 2022-05-05 | Data Governance |
| Coconut Oil 99.5% Pharma Grade | IC-15046 | 2021-03-06 | Compliance |
| Prime Logistik | TC-15052 | 2022-09-28 | Finance |
| Potassium Sorbate 50% Food Grade | IC-15064 | 2022-05-24 | Operations |
| SIG-37-HHT-38YO | TC-15082 | 2023-02-13 | Finance |
| GL-SY-99.5-GR-B-358 | TC-15106 | 2024-09-10 | Supply Chain |
| Rapsöl 25% Lebensmittelrein | IC-15108 | 2024-05-18 | Compliance |
| SIG-86-AKS-BEQE | IC-15130 | 2024-05-05 | Compliance |
| SIG-88-KUG-5ITD | TC-15137 | 2022-09-09 | Operations |
| Calcium Carbonate 50% | IC-15144 | 2022-06-20 | Finance |
| SIG-39-BAT-DD7R | TC-15148 | 2022-01-04 | Operations |
| Isoglucose | BC-15157 | 2024-03-18 | Data Governance |
| AT-SO-915 | BC-15167 | 2023-02-16 | Operations |
| PI-DI-543 Ltd. | TC-15176 | 2022-04-09 | Finance |
| Sodium Chloride 25% Premium | IC-15200 | 2022-01-09 | Supply Chain |
| SIG-24-NPE-GDMB | BC-15210 | 2022-08-25 | Finance |
| SIG-58-DDZ-4JKE International | IC-15222 | 2024-02-21 | Supply Chain |
| Fructose | BC-15224 | 2023-03-03 | Operations |
| citric acid 99.5% | TC-15254 | 2022-04-28 | Supply Chain |
| SIG-66-UEK-CKJ1 | IC-15255 | 2023-08-12 | Finance |
| SIG-65-MYR-QISO | TC-15264 | 2024-10-13 | Data Governance |
| SIG-12-RDG-0JI1 | TC-15266 | 2021-04-09 | IT Infrastructure |
| SIG-35-IQA-J92D | IC-15271 | 2022-01-13 | Supply Chain |
| Apex Logistik | TC-15273 | 2021-11-17 | IT Infrastructure |
| Horizon Sourcing | TC-15278 | 2021-07-01 | Supply Chain |
| Stratos Sourcing | BC-15279 | 2023-11-19 | Data Governance |
| SIG-87-SQR-587P | BC-15305 | 2023-02-14 | Operations |
| sunflower oil premium | IC-15322 | 2024-10-10 | Operations |
| PR-IN-695 Holdings | IC-15330 | 2023-12-22 | Supply Chain |
| Catalyst Versorgung International | TC-15334 | 2024-09-17 | Finance |
| VA-ST-I-20-301 | TC-15345 | 2021-08-01 | Finance |
| Quantum Ingredients | IC-15359 | 2024-11-02 | Supply Chain |
| palm oil 98% | IC-15406 | 2024-11-12 | Compliance |
| AS-AC-PH-GR-192 | TC-15424 | 2021-07-17 | IT Infrastructure |
| Dextrin Pharma Grade | BC-15432 | 2023-01-19 | Finance |
| ST-PR-265 Corp. | TC-15450 | 2023-09-23 | IT Infrastructure |
| Atlantic Partners | BC-15461 | 2024-10-09 | Operations |
| Baltic Versorgung | TC-15472 | 2021-11-02 | Finance |
| SIG-81-SBE-HL1C | TC-15498 | 2023-01-15 | IT Infrastructure |
| GL-SY-70-655 | TC-15512 | 2021-11-15 | Operations |
| Pea Protein Premiumqualität | TC-15525 | 2022-09-08 | Product Management |
| Natriumbenzoat | TC-15534 | 2023-03-12 | Supply Chain |
| PR-SU-CO-920 | BC-15541 | 2022-11-19 | Supply Chain |
| Maltodextrin DE30 Standard | BC-15544 | 2024-01-19 | Product Management |
| withholding fr 5% | TC-15546 | 2023-07-17 | Compliance |
| PA-SU-CO-454 | TC-15553 | 2024-04-03 | Supply Chain |
| Maltodextrin-Pulver DE10 | TC-15558 | 2021-02-07 | Product Management |
| SIG-56-ZQV-YINP SA | IC-15572 | 2022-11-05 | Product Management |
| ascorbic acid food grade | TC-15595 | 2022-06-26 | Finance |
| Vanguard Vertrieb | BC-15621 | 2024-01-25 | Supply Chain |
| stellar distribution Corp. | IC-15639 | 2021-04-20 | Compliance |
| palm oil 50% premium | IC-15660 | 2024-06-16 | Operations |
| Stellar Logistik | TC-15667 | 2022-08-13 | Data Governance |
| Sodium Chloride 98% | TC-15714 | 2021-07-14 | Data Governance |
| SIG-58-FIB-X69X | IC-15739 | 2023-05-16 | IT Infrastructure |
| Sorbinsäure Qualitätsstufe I | BC-15741 | 2022-03-11 | Operations |
| PR-SU-CO-805 | TC-15757 | 2024-12-02 | Compliance |
| Resistant Starch Premium | TC-15769 | 2022-06-12 | IT Infrastructure |
| Fructose 99.5% Technical | TC-15776 | 2021-12-02 | Compliance |
| Pacific Materials | IC-15778 | 2024-03-03 | Supply Chain |
| Vanguard Logistik | TC-15785 | 2022-05-08 | Data Governance |
| SIG-64-IEU-FRGN | TC-15791 | 2022-08-18 | Data Governance |
| Calcium Carbonate 50% Grade B | TC-15793 | 2024-11-19 | Finance |
| prism chemicals GmbH | IC-15794 | 2024-11-13 | Operations |
| BA-SO-835 Corp. | IC-15806 | 2024-08-01 | Product Management |
| Calcium Carbonate 99.5% | BC-15823 | 2023-09-08 | Finance |
| SIG-69-TRZ-SFLQ | BC-15833 | 2022-12-27 | Operations |
| SO-BE-98-410 | TC-15889 | 2023-02-13 | IT Infrastructure |
| SIG-82-ZPY-WR2F | TC-15901 | 2021-01-22 | IT Infrastructure |
| Vat Reduced IN 20% | TC-15923 | 2023-08-01 | Supply Chain |
| SIG-30-RXC-HFDI | IC-15930 | 2024-06-24 | Supply Chain |
| Coconut Oil | IC-15946 | 2023-02-08 | Product Management |
| Excise CN 20% | TC-15951 | 2021-08-10 | Finance |
| global materials | IC-15955 | 2023-08-17 | Data Governance |
| RE-ST-50-232 | BC-15966 | 2021-10-13 | Operations |
| SIG-17-IQV-FES7 | IC-15971 | 2024-10-09 | Finance |
| meridian solutions GmbH | BC-15972 | 2023-11-22 | Supply Chain |
| SIG-29-CYR-T4UF | IC-15976 | 2022-09-24 | Finance |
| sodium chloride 70% standard | TC-15979 | 2021-09-22 | Data Governance |
| PA-OI-98-587 | IC-15984 | 2021-02-23 | Product Management |
| SIG-20-RSZ-19RE | BC-15989 | 2022-07-13 | Operations |
| PR-CO-481 International | BC-15990 | 2022-01-10 | IT Infrastructure |
| Fructose Standardqualität | TC-15993 | 2022-01-16 | Supply Chain |
| global logistics | BC-16012 | 2024-04-03 | Data Governance |
| Ascorbic Acid Technische Qualität | TC-16028 | 2021-06-16 | Supply Chain |
| Potassium Sorbate 50% Technical | IC-16029 | 2021-10-02 | Supply Chain |
| SIG-72-JEH-P5K7 | IC-16045 | 2021-05-28 | Supply Chain |
| vat standard nl 5% | BC-16055 | 2023-06-12 | Finance |
| Citric Acid 70% Grade B | TC-16060 | 2023-11-03 | Product Management |
| DE-70-769 | IC-16089 | 2021-11-19 | IT Infrastructure |
| prime commodities | IC-16106 | 2021-08-14 | IT Infrastructure |
| SO-CH-TE-223 | TC-16157 | 2023-09-04 | Product Management |
| AT-LO-592 | BC-16162 | 2022-04-01 | Product Management |
| Premier Materials | TC-16169 | 2023-02-28 | Supply Chain |
| Rapsöl 98% Standardqualität | BC-16170 | 2022-07-01 | Product Management |
| Nexus Sourcing | IC-16194 | 2022-11-22 | Compliance |
| pea protein 99.5% | IC-16197 | 2021-05-12 | Product Management |
| Sorbinsäure Qualitätsstufe II | IC-16205 | 2023-07-13 | Compliance |
| Elite Chemicals AG | IC-16215 | 2021-08-03 | Data Governance |
| PE-PR-70-PR-387 | TC-16218 | 2021-01-18 | Supply Chain |
| nexus distribution AG | BC-16222 | 2022-02-02 | IT Infrastructure |
| SIG-82-VDF-0XQT | TC-16225 | 2024-05-25 | IT Infrastructure |
| Customs Duty US 20% | TC-16231 | 2024-07-27 | Finance |
| Global Werkstoffe | IC-16282 | 2021-12-17 | Product Management |
| CO-IN-915 KG | IC-16283 | 2024-04-25 | Data Governance |
| Nordic Manufacturing Holdings | TC-16293 | 2021-12-14 | Supply Chain |
| Citric Acid Pharma Grade | BC-16297 | 2024-08-16 | Data Governance |
| vanguard logistics | BC-16300 | 2024-01-03 | Supply Chain |
| Withholding GB 5% | BC-16305 | 2024-12-08 | IT Infrastructure |
| AT-DI-544 | BC-16320 | 2022-04-20 | Compliance |
| SIG-58-FIB-X69X | BC-16328 | 2024-09-18 | IT Infrastructure |
| SIG-93-MGK-61BG | TC-16330 | 2023-09-09 | Operations |
| SIG-18-WKH-NATG | IC-16352 | 2022-12-09 | Finance |
| PE-PR-98-GR-B-195 | TC-16361 | 2022-04-12 | Supply Chain |
| CO-PA-308 | BC-16392 | 2021-11-05 | Operations |
| SIG-28-STQ-YUPS | TC-16395 | 2023-06-21 | Product Management |
| sodium chloride premium | IC-16396 | 2021-11-14 | Finance |
| SIG-38-WKO-LWQT | BC-16401 | 2021-08-05 | Finance |
| Vertex Logistik | IC-16412 | 2021-10-21 | IT Infrastructure |
| DE-GR-B-244 | BC-16417 | 2023-03-17 | Finance |
| CI-AC-50-PH-GR-863 | BC-16428 | 2022-01-09 | Product Management |
| nexus sourcing | IC-16435 | 2021-08-19 | IT Infrastructure |
| cyclodextrin | TC-16468 | 2024-05-15 | Supply Chain |
| ME-DI-790 Group | IC-16480 | 2023-06-26 | Data Governance |
| VA-ST-G-19-945 | BC-16484 | 2023-06-06 | IT Infrastructure |
| SIG-48-KTU-I0WF | BC-16497 | 2024-05-16 | Finance |
| Sodium Chloride | IC-16512 | 2022-09-05 | Data Governance |
| quantum sourcing | BC-16515 | 2021-07-12 | Compliance |
| dextrin standard | BC-16526 | 2022-04-22 | Data Governance |
| SIG-71-VGV-8K52 | TC-16534 | 2023-07-24 | Product Management |
| SIG-20-FYS-JNIL | BC-16561 | 2022-09-14 | Operations |
| SIG-79-DVU-H9H4 | TC-16567 | 2024-11-06 | Finance |
| SIG-50-ABM-7VSK | IC-16587 | 2023-03-16 | Supply Chain |
| Nexus Chemicals Group | BC-16598 | 2023-04-09 | Product Management |
| Isoglucose | IC-16609 | 2022-11-09 | Supply Chain |
| Atlas Logistics International | IC-16633 | 2021-11-05 | Supply Chain |
| pea protein | IC-16637 | 2022-05-07 | Compliance |
| Ascorbic Acid 70% | IC-16655 | 2023-10-07 | Data Governance |
| SIG-42-FYL-6VKE | TC-16685 | 2021-03-28 | Finance |
| SO-BE-GR-A-760 | IC-16691 | 2024-05-06 | Compliance |
| SIG-94-TOI-OFNK | BC-16700 | 2024-01-01 | IT Infrastructure |
| SIG-48-LUB-IGA7 | IC-16703 | 2022-01-18 | Finance |
| Resistant Starch 99.5% | IC-16705 | 2023-03-10 | Data Governance |
| pacific enterprise | BC-16721 | 2021-10-26 | Supply Chain |
| Catalyst Ingredients International | TC-16734 | 2022-06-28 | Operations |
| Fructose Grade B | BC-16736 | 2023-06-21 | Finance |
| Sonnenblumenöl Qualitätsstufe II | TC-16743 | 2022-01-20 | Data Governance |
| Dextrin Pharmazeutisch rein | TC-16756 | 2021-02-15 | IT Infrastructure |
| Vat Reduced BR 7% | BC-16782 | 2023-09-17 | Compliance |
| Global Rohstoffe AG | TC-16803 | 2021-01-25 | Finance |
| catalyst supply Holdings | BC-16810 | 2021-06-20 | Supply Chain |
| SO-CH-GR-B-273 | IC-16812 | 2021-05-22 | Operations |
| PR-IN-608 BV | TC-16813 | 2023-06-22 | Data Governance |
| SIG-57-YOY-F7N2 | BC-16815 | 2021-12-08 | Data Governance |
| RA-OI-50-PH-GR-538 | TC-16818 | 2024-03-24 | Product Management |
| SIG-92-FQX-S1BC | BC-16820 | 2022-10-17 | Data Governance |
| Withholding IN 10% | TC-16824 | 2021-06-25 | IT Infrastructure |
| vat standard br 0% | IC-16831 | 2024-06-18 | Supply Chain |
| PR-LO-745 | TC-16860 | 2022-03-08 | Supply Chain |
| Vat Standardqualität FR 15% | IC-16884 | 2021-03-02 | IT Infrastructure |
| Pinnacle Werkstoffe | BC-16895 | 2021-07-24 | Supply Chain |
| Rapeseed Oil 99.5% | IC-16901 | 2024-12-02 | Data Governance |
| BA-PA-973 | IC-16903 | 2023-11-05 | Finance |
| Meridian Sourcing | BC-16916 | 2021-05-21 | Compliance |
| NO-MA-994 | TC-16922 | 2024-06-08 | Supply Chain |
| FR-99.5-FO-GR-963 | TC-16924 | 2022-08-13 | Supply Chain |
| Palm Oil 98% | IC-16929 | 2021-07-26 | Supply Chain |
| Nordic Industrien PLC | TC-16936 | 2023-06-11 | Data Governance |
| Central Versorgung GmbH | IC-16942 | 2021-01-24 | Compliance |
| SIG-52-EML-H8JV | BC-16950 | 2022-05-10 | Operations |
| PI-CH-610 Ltd. | BC-16961 | 2021-02-23 | Supply Chain |
| resistant starch premium | IC-16964 | 2023-09-09 | Data Governance |
| atlas logistics | IC-16976 | 2022-12-16 | Supply Chain |
| Vat Standard US 5% | TC-16986 | 2022-11-19 | Finance |
| Customs Duty NL 15% | IC-17003 | 2022-03-13 | IT Infrastructure |
| Elite Chemicals AG | TC-17021 | 2023-08-02 | Data Governance |
| Prime Materials | TC-17029 | 2023-08-17 | Supply Chain |
| wheat gluten 98% | BC-17048 | 2023-04-07 | Product Management |
| SIG-40-OEJ-4XCR | IC-17060 | 2021-04-22 | Product Management |
| SIG-12-BIH-AKGD | IC-17069 | 2021-04-18 | Operations |
| SIG-83-BMJ-HHIG | TC-17110 | 2024-07-10 | Data Governance |
| Fructose Grade A | IC-17139 | 2022-04-28 | IT Infrastructure |
| SIG-62-BTJ-PQV9 | BC-17164 | 2024-04-12 | Compliance |
| Dextrose | IC-17182 | 2023-10-05 | Finance |
| FR-99.5-PH-GR-378 | IC-17192 | 2022-09-22 | Finance |
| SIG-79-GUR-O5DB NV | BC-17208 | 2021-12-28 | Supply Chain |
| SIG-84-DSO-4S47 | BC-17211 | 2022-02-25 | Operations |
| SIG-70-IKQ-7KBN | TC-17218 | 2022-04-28 | Finance |
| SIG-86-VCP-SVOL | IC-17223 | 2023-01-03 | Operations |
| Lactic Acid 98% | TC-17226 | 2021-11-15 | Product Management |
| fructose 99.5% food grade | IC-17244 | 2023-06-28 | Supply Chain |
| AP-SO-576 | BC-17246 | 2023-12-04 | Finance |
| SIG-68-VLD-BDX3 International | IC-17247 | 2021-10-24 | Product Management |
| vertex enterprise Group | TC-17263 | 2024-08-04 | Product Management |
| SIG-99-CEZ-35MR | IC-17267 | 2023-01-22 | Operations |
| calcium carbonate | IC-17282 | 2022-09-25 | Compliance |
| SIG-79-SPO-WT80 | TC-17291 | 2021-02-26 | Product Management |
| Pacific Industrien | TC-17306 | 2022-02-18 | Finance |
| Stratos Sourcing | IC-17320 | 2021-08-21 | IT Infrastructure |
| Stellar Logistik | BC-17332 | 2024-07-17 | Compliance |
| Pea Protein 25% | TC-17356 | 2024-01-02 | Operations |
| Zitronensäure | IC-17357 | 2022-03-13 | Finance |
| Sonnenblumenöl | TC-17394 | 2024-09-19 | Operations |
| Glucose Syrup | TC-17401 | 2023-09-17 | Operations |
| palm oil | IC-17404 | 2022-03-17 | Supply Chain |
| Elite Logistik | IC-17419 | 2021-04-10 | Operations |
| DE-70-GR-A-741 | TC-17433 | 2023-06-16 | IT Infrastructure |
| SIG-47-LPF-7QXJ | TC-17488 | 2023-04-18 | Compliance |
| Calcium Carbonate 50% Grade A | BC-17496 | 2021-05-16 | Supply Chain |
| nexus logistics | BC-17497 | 2024-07-15 | IT Infrastructure |
| Atlantic Ingredients | IC-17499 | 2021-01-07 | Compliance |
| SIG-20-ISN-0EWL | IC-17501 | 2022-11-11 | Data Governance |
| SIG-76-QBY-ERKM | IC-17524 | 2024-05-11 | Compliance |
| SO-BE-PH-GR-831 | BC-17527 | 2023-08-05 | IT Infrastructure |
| Customs Duty CN 25% | TC-17528 | 2021-02-20 | Supply Chain |
| atlantic commodities | IC-17545 | 2022-10-02 | Compliance |
| Weizenklebereiweiß | TC-17547 | 2024-11-06 | Data Governance |
| SIG-51-ZHS-W8WR International | IC-17556 | 2022-11-08 | Compliance |
| SIG-90-YRJ-4LRE | IC-17583 | 2023-06-22 | Data Governance |
| CI-AC-50-PH-GR-863 | IC-17602 | 2023-10-14 | Compliance |
| AS-AC-782 | BC-17606 | 2022-04-16 | Compliance |
| fructose 70% | IC-17617 | 2023-04-22 | IT Infrastructure |
| Global Ingredients BV | IC-17622 | 2023-08-21 | Compliance |
| CI-AC-50-PH-GR-863 | BC-17633 | 2023-03-14 | Supply Chain |
| Traubenzucker 70% | BC-17657 | 2023-01-28 | Data Governance |
| SIG-37-JLF-9KYP | IC-17666 | 2021-01-17 | Data Governance |
| nordic ingredients SARL | BC-17673 | 2023-04-13 | Operations |
| soy isolate 99.5% | BC-17675 | 2024-03-10 | Supply Chain |
| CA-884 | BC-17678 | 2024-06-11 | Compliance |
| Horizon Ingredients BV | IC-17682 | 2024-08-07 | Supply Chain |
| Sodium Benzoate Pharma Grade | TC-17713 | 2021-11-04 | Product Management |
| Horizon Logistics | TC-17720 | 2023-08-06 | IT Infrastructure |
| Meridian Werkstoffe Corp. | BC-17727 | 2022-02-22 | Product Management |
| SIG-47-HPA-L2FX | TC-17742 | 2021-02-01 | IT Infrastructure |
| Pacific Chemicals GmbH | TC-17745 | 2024-06-16 | Operations |
| Fructose 25% | BC-17747 | 2024-12-12 | IT Infrastructure |
| Vat Reduced BR 15% | BC-17749 | 2021-08-18 | Operations |
| Sonnenblumenöl Qualitätsstufe II | IC-17755 | 2021-03-25 | Operations |
| wheat gluten pharma grade | IC-17761 | 2024-07-01 | Finance |
| nexus distribution Corp. | TC-17768 | 2023-04-04 | Supply Chain |
| potassium sorbate 98% | TC-17787 | 2022-06-28 | Operations |
| Vertex Chemicals Holdings | BC-17793 | 2022-03-17 | IT Infrastructure |
| Prism Ingredients | IC-17818 | 2022-12-13 | Compliance |
| VA-DI-105 | TC-17843 | 2024-10-22 | IT Infrastructure |
| soy isolate food grade | IC-17847 | 2024-11-26 | Finance |
| premier logistics Ltd. | IC-17848 | 2023-02-06 | Compliance |
| SIG-25-EZW-5GYT | BC-17866 | 2021-05-07 | Data Governance |
| CO-OI-FO-GR-162 | BC-17867 | 2023-02-11 | IT Infrastructure |
| AS-AC-99.5-619 | BC-17888 | 2023-04-25 | Product Management |
| SIG-83-MZM-HGMN GmbH | IC-17892 | 2021-07-11 | Operations |
| AS-AC-165 | IC-17894 | 2021-10-20 | Compliance |
| sunflower oil 50% pharma grade | BC-17902 | 2022-08-23 | Data Governance |
| SIG-85-FIY-2QW4 | BC-17909 | 2023-02-04 | Compliance |
| withholding de 15% | TC-17911 | 2021-01-20 | IT Infrastructure |
| SO-CH-99.5-618 | IC-17941 | 2023-09-28 | Supply Chain |
| Sorbinsäure 98% | TC-17952 | 2021-01-06 | Supply Chain |
| vat standard us 15% | TC-17955 | 2024-03-03 | Operations |
| Global Trading Ltd. | TC-17962 | 2023-11-28 | IT Infrastructure |
| Apex Solutions International | IC-17984 | 2021-09-11 | Operations |
| Pea Protein 25% Pharmazeutisch rein | IC-17987 | 2024-11-05 | Product Management |
| Continental Partners KG | TC-18028 | 2022-04-21 | IT Infrastructure |
| PO-SO-50-TE-282 | BC-18034 | 2021-03-23 | Finance |
| Dextrose | TC-18047 | 2023-10-09 | Supply Chain |
| palm oil food grade | BC-18076 | 2023-03-18 | Supply Chain |
| Vat Reduced BR 10% | BC-18085 | 2024-05-04 | Finance |
| Natriumbenzoat 50% | TC-18086 | 2022-07-28 | Finance |
| Rapeseed Oil 70% Grade B | BC-18091 | 2024-03-25 | Product Management |
| Sorbic Acid 70% | TC-18095 | 2021-09-05 | IT Infrastructure |
| Rapeseed Oil Grade A | IC-18103 | 2021-10-02 | Finance |
| SIG-30-NQN-ZENP | BC-18143 | 2024-10-03 | Finance |
| Catalyst Rohstoffe NV | TC-18157 | 2023-08-02 | IT Infrastructure |
| Dextrin Qualitätsstufe II | IC-18175 | 2022-04-15 | Data Governance |
| SIG-20-BPG-W8VL | BC-18188 | 2024-01-27 | Operations |
| Citric Acid | TC-18195 | 2023-10-17 | Compliance |
| Pinnacle Handel Inc. | BC-18199 | 2021-12-08 | Data Governance |
| Vat Reduced NL 21% | TC-18232 | 2023-02-04 | Compliance |
| VE-CH-445 Group | TC-18265 | 2023-07-23 | Operations |
| SIG-31-IKO-T2D8 | TC-18268 | 2024-11-27 | Data Governance |
| potassium sorbate | BC-18279 | 2024-03-08 | Operations |
| Dextrose Food Grade | BC-18281 | 2023-04-20 | IT Infrastructure |
| Pea Protein Pharma Grade | IC-18311 | 2022-10-20 | Operations |
| Cyclodextrin Standard | TC-18317 | 2022-05-15 | IT Infrastructure |
| vanguard industries Inc. | TC-18331 | 2022-11-03 | Operations |
| CU-DU-F-20-900 | TC-18335 | 2021-11-05 | Product Management |
| isoglucose | BC-18344 | 2021-09-13 | Supply Chain |
| Kasein | BC-18353 | 2021-09-22 | Product Management |
| SIG-14-MDA-Y0XA | TC-18358 | 2024-08-25 | Compliance |
| SU-OI-765 | IC-18367 | 2021-08-23 | Supply Chain |
| SIG-60-QPM-2TRI | IC-18392 | 2024-06-14 | Data Governance |
| EX-F-25-579 | TC-18399 | 2021-10-23 | Supply Chain |
| EL-LO-372 | IC-18427 | 2023-10-16 | Compliance |
| NO-SU-CO-498 | IC-18429 | 2024-09-22 | IT Infrastructure |
| Natriumbenzoat | IC-18442 | 2021-08-15 | Compliance |
| Premier Rohstoffe Holdings | BC-18453 | 2024-12-26 | Product Management |
| Palmfett | BC-18462 | 2021-10-01 | Operations |
| CI-AC-GR-A-280 | IC-18472 | 2024-01-01 | Product Management |
| withholding fr 5% | TC-18476 | 2021-12-01 | Finance |
| Atlas Ingredients Ltd. | IC-18478 | 2021-06-14 | IT Infrastructure |
| vat standard de 7% | BC-18483 | 2021-05-08 | Data Governance |
| Traubenzucker 98% Qualitätsstufe I | TC-18488 | 2022-11-27 | Compliance |
| SIG-24-CXH-R2TY | IC-18528 | 2022-04-08 | Finance |
| Zitronensäure | IC-18530 | 2024-11-14 | IT Infrastructure |
| core distribution BV | BC-18565 | 2024-11-24 | Finance |
| Sunflower Oil | TC-18572 | 2022-11-06 | Compliance |
| nexus distribution Corp. | IC-18578 | 2024-12-09 | Data Governance |
| Catalyst Logistics SA | IC-18581 | 2024-05-07 | IT Infrastructure |
| ST-SU-CO-731 | TC-18597 | 2023-08-07 | Product Management |
| Prism Sourcing | TC-18602 | 2023-05-25 | Supply Chain |
| SIG-24-CXH-R2TY | TC-18613 | 2021-08-19 | Compliance |
| Calcium Carbonate 98% | BC-18642 | 2023-09-16 | Supply Chain |
| Vat Reduced IN 10% | TC-18650 | 2021-02-18 | Data Governance |
| Stratos Werkstoffe | TC-18666 | 2022-01-03 | Supply Chain |
| vanguard materials | BC-18673 | 2023-01-15 | Operations |
| NO-PA-492 LLC | BC-18689 | 2024-07-06 | Operations |
| Nexus Partners GmbH | BC-18696 | 2023-10-11 | Data Governance |
| Maltodextrin DE10 | TC-18698 | 2021-03-21 | Finance |
| SIG-36-RVG-E4FG | BC-18703 | 2023-06-24 | Data Governance |
| Stellar Supply | BC-18714 | 2022-08-17 | Compliance |
| Sorbic Acid 50% Food Grade | BC-18717 | 2021-12-23 | Product Management |
| apex supply | IC-18721 | 2022-07-27 | Operations |
| potassium sorbate | TC-18759 | 2023-11-19 | Finance |
| MA-DE-738 | TC-18772 | 2024-11-07 | IT Infrastructure |
| Vertex Distribution AG | BC-18775 | 2021-02-16 | Data Governance |
| Weizenklebereiweiß | BC-18781 | 2023-12-07 | Supply Chain |
| Global Sourcing | BC-18792 | 2023-08-15 | Data Governance |
| dextrose food grade | TC-18796 | 2022-05-02 | Operations |
| RE-ST-FO-GR-238 | BC-18808 | 2024-02-08 | Supply Chain |
| Apex Ingredients KG | TC-18833 | 2022-06-03 | Product Management |
| SIG-73-KLZ-PDKU | TC-18844 | 2023-04-06 | Data Governance |
| SIG-99-CTB-8OFG Group | IC-18863 | 2022-09-16 | Product Management |
| Vertex Ingredients Ltd. | IC-18867 | 2023-09-02 | Supply Chain |
| Fructose 99.5% Technical | IC-18870 | 2022-05-18 | Product Management |
| Calcium Carbonate 98% Pharmazeutisch rein | TC-18878 | 2021-08-22 | Product Management |
| vertex industries NV | BC-18896 | 2022-08-03 | Supply Chain |
| Sunflower Oil Pharma Grade | BC-18907 | 2021-01-08 | IT Infrastructure |
| coconut oil standard | IC-18916 | 2022-08-01 | Compliance |
| Palmfett 98% | IC-18920 | 2024-11-25 | Compliance |
| CU-DU-B-15-379 | BC-18935 | 2021-09-08 | Product Management |
| SIG-34-JQN-ROWX | IC-18944 | 2023-03-02 | Operations |
| PE-PR-746 | BC-18947 | 2024-10-03 | IT Infrastructure |
| SU-OI-765 | IC-18949 | 2023-01-09 | Operations |
| glucose syrup food grade | IC-18958 | 2021-06-02 | Data Governance |
| fructose standard | IC-18984 | 2023-02-28 | Finance |
| Coconut Oil 98% Technical | TC-18990 | 2024-08-14 | Product Management |
| SIG-36-BVE-5U7D | BC-18998 | 2024-01-04 | Product Management |
| potassium sorbate premium | IC-19003 | 2022-10-07 | Data Governance |
| PO-SO-50-TE-282 | IC-19004 | 2024-11-02 | Data Governance |
| DE-602 | IC-19032 | 2023-10-19 | IT Infrastructure |
| SIG-78-LTE-H4VL | IC-19055 | 2021-01-28 | Data Governance |
| SIG-10-UIB-YQL1 | BC-19063 | 2021-02-03 | Supply Chain |
| Calcium Carbonate 70% Premiumqualität | TC-19065 | 2021-02-03 | Compliance |
| SIG-51-BUX-VLME Group | BC-19066 | 2024-06-19 | Product Management |
| Quantum Processing Ltd. | IC-19071 | 2023-04-04 | Finance |
| PA-OI-GR-B-326 | IC-19073 | 2023-11-23 | Operations |
| SIG-44-HTV-P84J | IC-19075 | 2022-06-10 | Finance |
| ST-IN-505 SA | BC-19088 | 2021-09-15 | Supply Chain |
| sodium benzoate | IC-19100 | 2022-06-09 | Supply Chain |
| SIG-12-QLD-RUJ3 Inc. | TC-19136 | 2024-03-07 | Data Governance |
| SIG-51-HUK-F1HG | BC-19145 | 2021-09-03 | Operations |
| prism manufacturing Ltd. | TC-19147 | 2024-07-19 | IT Infrastructure |
| Resistente Stärke | BC-19150 | 2022-06-16 | Operations |
| Apex Handel International | BC-19158 | 2022-04-18 | Compliance |
| SIG-68-TVY-N4XJ | TC-19177 | 2021-03-01 | Product Management |
| Soy Isolate 98% | IC-19180 | 2021-01-27 | Finance |
| Ascorbic Acid | TC-19185 | 2022-01-08 | Operations |
| Ascorbic Acid 70% | BC-19192 | 2023-08-21 | Supply Chain |
| VE-LO-902 Group | TC-19196 | 2023-08-10 | Supply Chain |
| Stratos Ingredients SARL | BC-19207 | 2024-11-25 | Product Management |
| Catalyst Werkstoffe | BC-19236 | 2024-06-09 | Product Management |
| Resistant Starch Grade B | BC-19239 | 2024-07-16 | Data Governance |
| SO-BE-667 | BC-19257 | 2022-08-20 | Finance |
| soy isolate 98% | IC-19261 | 2023-06-14 | Compliance |
| Meridian Vertrieb International | TC-19266 | 2022-01-25 | IT Infrastructure |
| lactic acid | BC-19269 | 2022-12-14 | Compliance |
| SIG-73-LLJ-LNGI | TC-19293 | 2023-02-05 | Operations |
| isoglucose 70% | TC-19305 | 2023-01-07 | Supply Chain |
| CA-CA-GR-B-162 | TC-19317 | 2021-01-05 | Finance |
| Sodium Chloride | IC-19321 | 2021-02-11 | IT Infrastructure |
| Dextrin 50% | BC-19329 | 2023-01-09 | Compliance |
| WI-F-5-977 | IC-19334 | 2022-05-13 | Compliance |
| Excise BR 19% | BC-19337 | 2024-02-22 | Supply Chain |
| vertex materials | BC-19344 | 2021-01-09 | Supply Chain |
| SIG-65-ONA-WQOF Corp. | BC-19354 | 2021-07-22 | Finance |
| prism materials | IC-19368 | 2024-03-23 | Operations |
| Wheat Gluten | BC-19376 | 2024-12-28 | Finance |
| SIG-66-JGK-EM8M | IC-19381 | 2022-06-07 | Product Management |
| Isoglucose Grade B | IC-19389 | 2021-04-22 | Compliance |
| Apex Sourcing | BC-19403 | 2023-11-06 | Compliance |
| SIG-69-BWM-8WBG | BC-19425 | 2024-01-26 | IT Infrastructure |
| Resistant Starch Technical | IC-19446 | 2024-08-07 | IT Infrastructure |
| Isoglucose 70% | IC-19490 | 2023-02-26 | Finance |
| SIG-78-NWO-RO6D | BC-19495 | 2021-12-19 | Finance |
| Atlantic Processing | IC-19502 | 2023-08-07 | Product Management |
| Central Logistik Holdings | BC-19507 | 2024-02-08 | Product Management |
| VA-ST-N-5-192 | IC-19520 | 2022-09-14 | Compliance |
| SIG-19-QLH-ILRZ | BC-19528 | 2023-05-08 | Data Governance |
| SIG-43-MIT-DWCJ SA | IC-19553 | 2022-11-07 | Finance |
| ST-PA-504 | IC-19567 | 2023-01-01 | Supply Chain |
| SIG-91-WVE-3ESP | IC-19572 | 2022-08-19 | Data Governance |
| pacific supply | TC-19608 | 2023-12-19 | Product Management |
| cyclodextrin 98% | IC-19613 | 2022-05-01 | IT Infrastructure |
| SIG-74-LEZ-GZA2 AG | IC-19622 | 2023-04-09 | IT Infrastructure |
| ST-LO-378 | BC-19624 | 2023-11-19 | Compliance |
| CY-GR-A-208 | BC-19628 | 2024-08-10 | Product Management |
| SIG-93-YGI-KLQ0 | TC-19648 | 2024-07-19 | IT Infrastructure |
| SIG-55-EGS-MYD1 | IC-19652 | 2022-02-13 | Product Management |
| nexus logistics | BC-19657 | 2022-03-01 | Product Management |
| horizon materials | TC-19663 | 2022-05-17 | Supply Chain |
| Sodium Chloride 70% | BC-19676 | 2022-07-26 | Finance |
| Soy Isolate 25% Standard | TC-19678 | 2024-10-04 | Supply Chain |
| soy isolate standard | TC-19679 | 2022-03-01 | Operations |
| Lactic Acid 98% | IC-19684 | 2021-05-07 | Operations |
| Potassium Sorbate | BC-19701 | 2021-07-19 | Product Management |
| sodium benzoate premium | IC-19718 | 2024-01-04 | IT Infrastructure |
| quantum processing International | TC-19720 | 2024-05-22 | Finance |
| SIG-60-RUC-CU6A | BC-19745 | 2021-12-01 | Data Governance |
| sorbic acid food grade | IC-19804 | 2022-09-08 | Product Management |
| CO-OI-50-147 | BC-19815 | 2022-06-06 | Operations |
| Casein 98% Grade B | IC-19826 | 2023-12-06 | IT Infrastructure |
| SIG-44-HTV-P84J | IC-19834 | 2024-07-24 | IT Infrastructure |
| SIG-23-IEJ-V2T3 | TC-19843 | 2022-02-04 | Operations |
| Stellar Processing Holdings | BC-19860 | 2021-10-27 | Supply Chain |
| Baltic Manufacturing | TC-19862 | 2022-11-22 | IT Infrastructure |
| zenith trading GmbH | BC-19867 | 2021-06-14 | Product Management |
| SIG-47-SRN-QNYY | IC-19874 | 2022-10-13 | Supply Chain |
| ST-TR-590 | BC-19879 | 2024-08-05 | Compliance |
| SIG-60-OHC-5EQB | BC-19900 | 2024-07-16 | Data Governance |
| VA-RE-C-10-444 | TC-19904 | 2023-05-07 | Supply Chain |
| Fructose 99.5% | IC-19914 | 2023-08-11 | Operations |
| Atlas Chemicals SARL | IC-19953 | 2021-02-24 | Product Management |
| withholding fr 25% | TC-19957 | 2024-03-25 | Compliance |
| SIG-83-ZHQ-A0CR | TC-19973 | 2024-10-02 | IT Infrastructure |
| Lactic Acid | IC-19978 | 2024-10-18 | IT Infrastructure |
| Vat Standard NL 19% | IC-19981 | 2022-09-27 | Operations |
| RE-ST-GR-B-598 | TC-19987 | 2022-01-08 | IT Infrastructure |
| SIG-15-YBX-K4SY | IC-19989 | 2022-06-19 | Product Management |
| NO-MA-452 | TC-19998 | 2023-11-26 | Finance |
| Customs Duty IN 25% | BC-20010 | 2023-03-18 | Supply Chain |
| ZE-MA-316 | IC-20058 | 2022-05-25 | Product Management |
| VA-ST-G-19-277 | TC-20105 | 2024-07-23 | Supply Chain |
| SIG-79-DVU-H9H4 | TC-20114 | 2023-01-08 | Operations |
| PO-SO-99.5-897 | TC-20135 | 2024-12-25 | Product Management |
| SIG-19-TPS-MSKY | BC-20149 | 2024-07-09 | Operations |
| SIG-12-JHE-FNCL | BC-20155 | 2022-02-18 | Data Governance |
| SIG-57-YNB-5KMT | IC-20173 | 2023-12-13 | IT Infrastructure |
| SIG-20-XSP-FVHF | BC-20178 | 2021-02-11 | Operations |
| coconut oil | BC-20190 | 2023-09-13 | Data Governance |
| GL-SY-99.5-ST-205 | TC-20198 | 2023-07-05 | Product Management |
| MA-DE-585 | TC-20201 | 2021-03-12 | IT Infrastructure |
| Apex Logistics | TC-20202 | 2023-04-07 | Compliance |
| Cyclodextrin | TC-20218 | 2021-07-15 | Supply Chain |
| cyclodextrin pharma grade | IC-20221 | 2022-07-14 | Operations |
| SIG-56-ZVH-GATJ | IC-20229 | 2024-11-04 | Compliance |
| AT-IN-327 | TC-20234 | 2021-06-02 | Supply Chain |
| citric acid premium | BC-20247 | 2021-06-02 | Compliance |
| glucose syrup 98% | BC-20249 | 2023-02-14 | Product Management |
| stratos supply AG | TC-20288 | 2022-09-14 | Compliance |
| atlas partners | IC-20317 | 2022-04-08 | Product Management |
| quantum enterprise BV | IC-20364 | 2024-11-21 | Compliance |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| Apex Chemicals Corp. | IC-8834 | SUPERSEDED | Historical - verify before use |
| CO-OI-98-890 | IC-7078 | REVIEW REQUIRED | Historical - verify before use |
| SIG-70-MMO-95UC | IC-8787 | REVIEW REQUIRED | Historical - verify before use |
| SO-IS-25-323 | IC-9151 | DEPRECATED | Historical - verify before use |
| rapeseed oil tech grade | IC-7059 | SUPERSEDED | Historical - verify before use |
| Nordic Distribution | IC-7456 | PROVISIONAL | Historical - verify before use |
| Excise IN 25% | IC-7760 | SUPERSEDED | Historical - verify before use |
| PO-SO-50-GR-B-154 | IC-7339 | REVIEW REQUIRED | Historical - verify before use |
| Pinnacle Werkstoffe SARL | IC-7606 | SUPERSEDED | Historical - verify before use |
| citric acid 99.5% | IC-8519 | REVIEW REQUIRED | Historical - verify before use |
| SIG-40-CXK-QT2E Group | IC-5752 | PROVISIONAL | Historical - verify before use |
| PE-PR-PR-564 | IC-9411 | DEPRECATED | Historical - verify before use |
| Zitronensäure Technische Qualität | IC-7213 | REVIEW REQUIRED | Historical - verify before use |
| SIG-26-WVS-AQ3B | IC-7916 | PROVISIONAL | Historical - verify before use |
| citric acid | IC-7590 | REVIEW REQUIRED | Historical - verify before use |
| Vat Standard CN 10% | IC-5667 | SUPERSEDED | Historical - verify before use |
| PO-SO-50-TE-497 | IC-9081 | SUPERSEDED | Historical - verify before use |
| Continental Solutions | IC-8923 | PROVISIONAL | Historical - verify before use |
| Customs Duty FR 19% | IC-5507 | DEPRECATED | Historical - verify before use |
| SIG-67-MFU-QOZ9 Group | IC-9999 | REVIEW REQUIRED | Historical - verify before use |
| Fructose Grade A | IC-8675 | REVIEW REQUIRED | Historical - verify before use |
| SIG-44-FWT-OA3N | IC-6834 | DEPRECATED | Historical - verify before use |
| CA-CA-947 | IC-8244 | REVIEW REQUIRED | Historical - verify before use |
| Elite Handel Corp. | IC-7817 | PROVISIONAL | Historical - verify before use |
| SIG-13-SXA-38WM | IC-9299 | DEPRECATED | Historical - verify before use |
| Nordic Distribution | IC-8472 | SUPERSEDED | Historical - verify before use |
| vat standard us 19% | IC-9867 | REVIEW REQUIRED | Historical - verify before use |
| prism ingredients | IC-6066 | DEPRECATED | Historical - verify before use |
| SIG-25-VPE-TOC1 | IC-6492 | SUPERSEDED | Historical - verify before use |
| CY-577 | IC-6906 | SUPERSEDED | Historical - verify before use |
| Cyclodextrin Premiumqualität | IC-7888 | DEPRECATED | Historical - verify before use |
| Cyclodextrin Qualitätsstufe I | IC-5712 | PROVISIONAL | Historical - verify before use |
| PR-IN-149 Holdings | IC-5890 | PROVISIONAL | Historical - verify before use |
| Pinnacle Rohstoffe NV | IC-8012 | PROVISIONAL | Historical - verify before use |
| SIG-76-GDP-2JN8 | IC-7644 | PROVISIONAL | Historical - verify before use |
| Atlas Versorgung GmbH | IC-9022 | REVIEW REQUIRED | Historical - verify before use |
| CO-SO-101 | IC-9298 | SUPERSEDED | Historical - verify before use |
| Resistente Stärke Pharmazeutisch rein | IC-6738 | PROVISIONAL | Historical - verify before use |
| GL-LO-935 | IC-5105 | SUPERSEDED | Historical - verify before use |
| SIG-40-CXK-QT2E Group | IC-8378 | REVIEW REQUIRED | Historical - verify before use |
| DE-PH-GR-173 | IC-8445 | PROVISIONAL | Historical - verify before use |
| SO-IS-50-GR-B-983 | IC-6827 | REVIEW REQUIRED | Historical - verify before use |
| VA-ST-N-5-192 | IC-5158 | PROVISIONAL | Historical - verify before use |
| Citric Acid 70% Food Grade | IC-6381 | SUPERSEDED | Historical - verify before use |
| SIG-13-ZIB-S8MV International | IC-9140 | SUPERSEDED | Historical - verify before use |
| Isoglucose 70% | IC-7949 | DEPRECATED | Historical - verify before use |
| SIG-56-CMM-ODF7 | IC-7752 | DEPRECATED | Historical - verify before use |
| Vat Reduced GB 21% | IC-6970 | REVIEW REQUIRED | Historical - verify before use |
| atlantic supply | IC-6990 | SUPERSEDED | Historical - verify before use |
| Dextrin 50% | IC-5602 | SUPERSEDED | Historical - verify before use |
| Lactic Acid 50% Premiumqualität | IC-8550 | REVIEW REQUIRED | Historical - verify before use |
| GL-IN-746 LLC | IC-6838 | SUPERSEDED | Historical - verify before use |
| Baltic Versorgung GmbH | IC-9408 | PROVISIONAL | Historical - verify before use |
| PR-IN-409 LLC | IC-9054 | PROVISIONAL | Historical - verify before use |
| atlas logistics | IC-8179 | DEPRECATED | Historical - verify before use |
| SIG-64-VUE-OGQ2 | IC-8795 | SUPERSEDED | Historical - verify before use |
| Kasein 98% | IC-5060 | REVIEW REQUIRED | Historical - verify before use |
| CI-AC-PH-GR-209 | IC-7850 | PROVISIONAL | Historical - verify before use |
| Soja Isolate Premiumqualität | IC-8809 | SUPERSEDED | Historical - verify before use |
| ST-LO-637 | IC-7436 | PROVISIONAL | Historical - verify before use |
| Soja Isolate Lebensmittelrein | IC-9629 | DEPRECATED | Historical - verify before use |
| Apex Chemicals | IC-5268 | REVIEW REQUIRED | Historical - verify before use |
| Prime Enterprise Holdings | IC-6416 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat | IC-9833 | SUPERSEDED | Historical - verify before use |
| Quantum Commodities PLC | IC-8991 | SUPERSEDED | Historical - verify before use |
| Glukosesirup Syrup 99.5% Qualitätsstufe II | IC-7090 | SUPERSEDED | Historical - verify before use |
| Central Partners Corp. | IC-6655 | PROVISIONAL | Historical - verify before use |
| Lactic Acid | IC-5136 | REVIEW REQUIRED | Historical - verify before use |
| SIG-87-SQR-587P | IC-5349 | DEPRECATED | Historical - verify before use |
| Elite Logistics Holdings | IC-9011 | DEPRECATED | Historical - verify before use |
| Coconut Oil 25% | IC-7108 | DEPRECATED | Historical - verify before use |
| SIG-50-CEU-F5QB | IC-6059 | REVIEW REQUIRED | Historical - verify before use |
| LA-AC-70-781 | IC-6066 | SUPERSEDED | Historical - verify before use |
| SIG-79-HKV-T268 | IC-5918 | PROVISIONAL | Historical - verify before use |
| CO-OI-98-876 | IC-6727 | DEPRECATED | Historical - verify before use |
| Pinnacle Supply International | IC-7708 | REVIEW REQUIRED | Historical - verify before use |
| SIG-29-KJI-GJKC | IC-8367 | SUPERSEDED | Historical - verify before use |
| Excise NL 20% | IC-7348 | SUPERSEDED | Historical - verify before use |
| Sorbinsäure 50% Lebensmittelrein | IC-8533 | PROVISIONAL | Historical - verify before use |
| Elite Versorgung SA | IC-6131 | PROVISIONAL | Historical - verify before use |
| Coconut Oil Pharma Grade | IC-5384 | SUPERSEDED | Historical - verify before use |
| maltodextrin de25 | IC-9846 | REVIEW REQUIRED | Historical - verify before use |
| Pinnacle Logistics International | IC-7630 | SUPERSEDED | Historical - verify before use |
| Traubenzucker Qualitätsstufe I | IC-8855 | DEPRECATED | Historical - verify before use |
| wheat gluten food grade | IC-8399 | DEPRECATED | Historical - verify before use |
| DE-99.5-ST-905 | IC-7997 | DEPRECATED | Historical - verify before use |
| nexus enterprise | IC-8613 | PROVISIONAL | Historical - verify before use |
| catalyst enterprise | IC-5503 | PROVISIONAL | Historical - verify before use |
| Catalyst Materials | IC-9839 | SUPERSEDED | Historical - verify before use |
| prime supply | IC-6250 | SUPERSEDED | Historical - verify before use |
| potassium sorbate 50% tech grade | IC-9420 | SUPERSEDED | Historical - verify before use |
| Lactic Acid 98% | IC-9692 | SUPERSEDED | Historical - verify before use |
| SU-OI-98-462 | IC-9406 | DEPRECATED | Historical - verify before use |
| Global Versorgung | IC-7025 | PROVISIONAL | Historical - verify before use |
| SIG-84-DSO-4S47 | IC-8433 | REVIEW REQUIRED | Historical - verify before use |
| SIG-58-SVK-Z948 | IC-5572 | DEPRECATED | Historical - verify before use |
| SIG-96-FYH-4ROJ SARL | IC-8489 | REVIEW REQUIRED | Historical - verify before use |
| SIG-66-ZOH-E8TV | IC-9336 | SUPERSEDED | Historical - verify before use |
| nordic sourcing | IC-5587 | SUPERSEDED | Historical - verify before use |
| Vat Standardqualität DE 25% | IC-8484 | PROVISIONAL | Historical - verify before use |
| Ascorbic Acid 70% | IC-9153 | SUPERSEDED | Historical - verify before use |
| SIG-69-OFZ-JW34 | IC-7215 | PROVISIONAL | Historical - verify before use |
| SIG-20-UMV-LJM6 | IC-8695 | REVIEW REQUIRED | Historical - verify before use |
| PA-OI-25-GR-A-241 | IC-8752 | SUPERSEDED | Historical - verify before use |
| Vanguard Werkstoffe | IC-5478 | PROVISIONAL | Historical - verify before use |
| SIG-68-KHP-8RTJ | IC-9666 | DEPRECATED | Historical - verify before use |
| Zitronensäure Standardqualität | IC-5917 | SUPERSEDED | Historical - verify before use |
| SU-OI-FO-GR-778 | IC-7691 | DEPRECATED | Historical - verify before use |
| ZE-PA-511 PLC | IC-6905 | SUPERSEDED | Historical - verify before use |
| SIG-29-XAN-WDDA | IC-6501 | REVIEW REQUIRED | Historical - verify before use |
| SIG-13-WHV-DDIN | IC-9875 | PROVISIONAL | Historical - verify before use |
| casein | IC-8915 | PROVISIONAL | Historical - verify before use |
| SIG-39-BHZ-K8SS | IC-7356 | DEPRECATED | Historical - verify before use |
| SIG-95-HLU-HD5X GmbH | IC-7519 | DEPRECATED | Historical - verify before use |
| Wheat Gluten | IC-8617 | DEPRECATED | Historical - verify before use |
| SIG-53-MHB-8KZX | IC-6453 | PROVISIONAL | Historical - verify before use |
| SO-IS-PR-242 | IC-5736 | REVIEW REQUIRED | Historical - verify before use |
| Vat Reduced BR 10% | IC-7016 | REVIEW REQUIRED | Historical - verify before use |
| SIG-52-JJF-4GXO International | IC-5905 | REVIEW REQUIRED | Historical - verify before use |
| Dextrose | IC-5711 | PROVISIONAL | Historical - verify before use |
| GL-SY-98-FO-GR-198 | IC-8091 | SUPERSEDED | Historical - verify before use |
| pea protein standard | IC-9515 | REVIEW REQUIRED | Historical - verify before use |
| PA-LO-382 Group | IC-7468 | PROVISIONAL | Historical - verify before use |
| Pacific Vertrieb Group | IC-6009 | PROVISIONAL | Historical - verify before use |
| Casein Grade A | IC-5952 | SUPERSEDED | Historical - verify before use |
| dextrose standard | IC-9972 | DEPRECATED | Historical - verify before use |
| Fructose | IC-6671 | REVIEW REQUIRED | Historical - verify before use |
| EX-I-19-464 | IC-5318 | REVIEW REQUIRED | Historical - verify before use |
| SIG-99-TBJ-83YG KG | IC-6668 | REVIEW REQUIRED | Historical - verify before use |
| Sorbinsäure 98% | IC-6598 | DEPRECATED | Historical - verify before use |
| central sourcing | IC-5424 | REVIEW REQUIRED | Historical - verify before use |
| nexus supply | IC-8312 | REVIEW REQUIRED | Historical - verify before use |
| Weizenklebereiweiß | IC-5414 | SUPERSEDED | Historical - verify before use |
| QU-TR-440 | IC-8296 | PROVISIONAL | Historical - verify before use |
| sunflower oil standard | IC-8806 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-98-GR-B-961 | IC-5707 | REVIEW REQUIRED | Historical - verify before use |
| SIG-92-RHW-233J | IC-6720 | REVIEW REQUIRED | Historical - verify before use |
| Casein | IC-9381 | DEPRECATED | Historical - verify before use |
| ME-LO-731 | IC-7314 | PROVISIONAL | Historical - verify before use |
| SIG-60-RUC-CU6A | IC-9367 | PROVISIONAL | Historical - verify before use |
| pinnacle supply | IC-5260 | REVIEW REQUIRED | Historical - verify before use |
| SIG-69-UAZ-1ODW | IC-6290 | PROVISIONAL | Historical - verify before use |
| SIG-43-GRJ-P3HT | IC-6364 | PROVISIONAL | Historical - verify before use |
| SIG-89-HLJ-NILC | IC-9817 | DEPRECATED | Historical - verify before use |
| lactic acid 70% | IC-7424 | SUPERSEDED | Historical - verify before use |
| Palmfett | IC-9089 | REVIEW REQUIRED | Historical - verify before use |
| Sonnenblumenöl 70% | IC-7279 | SUPERSEDED | Historical - verify before use |
| SIG-35-SZU-VMRU | IC-9825 | PROVISIONAL | Historical - verify before use |
| SIG-83-TNT-G0Q1 AG | IC-9819 | REVIEW REQUIRED | Historical - verify before use |
| SIG-39-BAT-DD7R | IC-7456 | PROVISIONAL | Historical - verify before use |
| Vanguard Logistik | IC-9028 | DEPRECATED | Historical - verify before use |
| maltodextrin de10 | IC-5702 | REVIEW REQUIRED | Historical - verify before use |
| Soy Isolate | IC-5712 | REVIEW REQUIRED | Historical - verify before use |
| LA-AC-471 | IC-7892 | REVIEW REQUIRED | Historical - verify before use |
| Natriumchlorid 98% | IC-5686 | SUPERSEDED | Historical - verify before use |
| SIG-42-BEO-614U | IC-6742 | SUPERSEDED | Historical - verify before use |
| Maltodextrin DE15 | IC-9128 | PROVISIONAL | Historical - verify before use |
| Palmfett | IC-9585 | REVIEW REQUIRED | Historical - verify before use |
| nexus logistics | IC-7706 | SUPERSEDED | Historical - verify before use |
| fructose standard | IC-7114 | PROVISIONAL | Historical - verify before use |
| DE-GR-A-351 | IC-9067 | DEPRECATED | Historical - verify before use |
| Natriumbenzoat 99.5% | IC-5266 | DEPRECATED | Historical - verify before use |
| FR-GR-A-600 | IC-8807 | REVIEW REQUIRED | Historical - verify before use |
| casein 98% standard | IC-5765 | SUPERSEDED | Historical - verify before use |
| lactic acid standard | IC-5739 | PROVISIONAL | Historical - verify before use |
| SIG-47-HDT-7PPC | IC-6339 | PROVISIONAL | Historical - verify before use |
| PA-SO-270 | IC-7547 | DEPRECATED | Historical - verify before use |
| SIG-85-PGT-NQA4 | IC-5112 | DEPRECATED | Historical - verify before use |
| Stellar Werkstoffe | IC-9705 | REVIEW REQUIRED | Historical - verify before use |
| SIG-47-NVU-R3XU | IC-5153 | REVIEW REQUIRED | Historical - verify before use |
| CU-DU-N-15-558 | IC-6667 | DEPRECATED | Historical - verify before use |
| Natriumchlorid Technische Qualität | IC-7837 | PROVISIONAL | Historical - verify before use |
| ST-CO-650 International | IC-7678 | PROVISIONAL | Historical - verify before use |
| PO-SO-50-GR-B-154 | IC-5160 | PROVISIONAL | Historical - verify before use |
| Atlas Industrien International | IC-6503 | PROVISIONAL | Historical - verify before use |
| Premier Logistik KG | IC-5241 | REVIEW REQUIRED | Historical - verify before use |
| Customs Duty FR 25% | IC-6046 | DEPRECATED | Historical - verify before use |
| SIG-82-ZXL-FF30 International | IC-7395 | PROVISIONAL | Historical - verify before use |
| vanguard supply NV | IC-9244 | REVIEW REQUIRED | Historical - verify before use |
| Soy Isolate 99.5% Standard | IC-7279 | DEPRECATED | Historical - verify before use |
| AP-TR-161 International | IC-6397 | DEPRECATED | Historical - verify before use |
| Fructose Qualitätsstufe II | IC-7371 | REVIEW REQUIRED | Historical - verify before use |
| QU-TR-219 International | IC-5235 | SUPERSEDED | Historical - verify before use |
| ascorbic acid | IC-6817 | SUPERSEDED | Historical - verify before use |
| Atlantic Materials | IC-7230 | PROVISIONAL | Historical - verify before use |
| Sodium Chloride | IC-8913 | REVIEW REQUIRED | Historical - verify before use |
| SIG-41-OMW-SN1T | IC-9755 | REVIEW REQUIRED | Historical - verify before use |
| CE-PR-134 | IC-8336 | REVIEW REQUIRED | Historical - verify before use |
| withholding gb 21% | IC-7632 | DEPRECATED | Historical - verify before use |
| sunflower oil 98% | IC-5796 | SUPERSEDED | Historical - verify before use |
| SO-BE-GR-B-936 | IC-8289 | DEPRECATED | Historical - verify before use |
| Vat Standard FR 20% | IC-7772 | SUPERSEDED | Historical - verify before use |
| SIG-35-SZU-VMRU | IC-8698 | PROVISIONAL | Historical - verify before use |
| Isoglucose Technical | IC-8260 | REVIEW REQUIRED | Historical - verify before use |
| SIG-35-BYM-BYQ7 Inc. | IC-8755 | SUPERSEDED | Historical - verify before use |
| Pea Protein Premiumqualität | IC-9505 | REVIEW REQUIRED | Historical - verify before use |
| Customs Duty FR 15% | IC-6570 | REVIEW REQUIRED | Historical - verify before use |
| Cyclodextrin 70% Food Grade | IC-5607 | SUPERSEDED | Historical - verify before use |
| Sodium Benzoate 25% | IC-8787 | PROVISIONAL | Historical - verify before use |
| SIG-73-AXD-XIX9 | IC-9429 | SUPERSEDED | Historical - verify before use |
| SO-CH-GR-B-273 | IC-9827 | SUPERSEDED | Historical - verify before use |
| palm oil 99.5% | IC-9454 | PROVISIONAL | Historical - verify before use |
| Vanguard Sourcing | IC-8156 | PROVISIONAL | Historical - verify before use |
| CO-CH-401 Inc. | IC-9173 | PROVISIONAL | Historical - verify before use |
| Atlantic Industrien International | IC-5615 | PROVISIONAL | Historical - verify before use |
| SIG-44-UKH-MO4F | IC-6276 | SUPERSEDED | Historical - verify before use |
| Fructose Qualitätsstufe II | IC-6955 | PROVISIONAL | Historical - verify before use |
| SIG-75-GGJ-DK9O | IC-8966 | SUPERSEDED | Historical - verify before use |
| SO-IS-50-568 | IC-9879 | SUPERSEDED | Historical - verify before use |
| ST-SU-125 SA | IC-6110 | DEPRECATED | Historical - verify before use |
| Calcium Carbonate 99.5% Food Grade | IC-9857 | DEPRECATED | Historical - verify before use |
| continental manufacturing Inc. | IC-9602 | PROVISIONAL | Historical - verify before use |
| Soja Isolate 98% Premiumqualität | IC-6935 | REVIEW REQUIRED | Historical - verify before use |
| HO-LO-699 | IC-6433 | DEPRECATED | Historical - verify before use |
| WI-G-15-758 | IC-8646 | PROVISIONAL | Historical - verify before use |
| Ascorbic Acid 99.5% | IC-7476 | PROVISIONAL | Historical - verify before use |
| SIG-57-GUP-S7UK | IC-8612 | PROVISIONAL | Historical - verify before use |
| SIG-44-HTV-P84J | IC-9138 | PROVISIONAL | Historical - verify before use |
| Premier Enterprise International | IC-5893 | REVIEW REQUIRED | Historical - verify before use |
| NE-EN-710 NV | IC-8756 | PROVISIONAL | Historical - verify before use |
| ST-SU-950 SAS | IC-5855 | DEPRECATED | Historical - verify before use |
| SIG-89-ISH-EQW6 | IC-8906 | SUPERSEDED | Historical - verify before use |
| calcium carbonate 50% pharma grade | IC-5762 | DEPRECATED | Historical - verify before use |
| VA-ST-D-21-476 | IC-6520 | REVIEW REQUIRED | Historical - verify before use |
| SO-BE-99.5-ST-342 | IC-5372 | PROVISIONAL | Historical - verify before use |
| Vanguard Logistik International | IC-6760 | PROVISIONAL | Historical - verify before use |
| Dextrin Qualitätsstufe II | IC-7557 | PROVISIONAL | Historical - verify before use |
| SIG-78-WDE-NNV9 | IC-9749 | DEPRECATED | Historical - verify before use |
| Customs Duty BR 21% | IC-7807 | PROVISIONAL | Historical - verify before use |
| GL-SY-371 | IC-5782 | SUPERSEDED | Historical - verify before use |
| Traubenzucker 99.5% | IC-9449 | PROVISIONAL | Historical - verify before use |
| sodium benzoate | IC-9736 | DEPRECATED | Historical - verify before use |
| palm oil standard | IC-8019 | DEPRECATED | Historical - verify before use |
| SO-AC-PR-928 | IC-7865 | PROVISIONAL | Historical - verify before use |
| RA-OI-GR-A-980 | IC-7841 | REVIEW REQUIRED | Historical - verify before use |
| central materials BV | IC-6177 | REVIEW REQUIRED | Historical - verify before use |
| Palmfett 70% Technische Qualität | IC-9631 | DEPRECATED | Historical - verify before use |
| Calcium Carbonate 98% | IC-5997 | REVIEW REQUIRED | Historical - verify before use |
| Fructose Premiumqualität | IC-7494 | PROVISIONAL | Historical - verify before use |
| CI-AC-GR-A-813 | IC-5212 | REVIEW REQUIRED | Historical - verify before use |
| Baltic Rohstoffe Ltd. | IC-7977 | PROVISIONAL | Historical - verify before use |
| LA-AC-FO-GR-469 | IC-6890 | PROVISIONAL | Historical - verify before use |
| SIG-65-RQH-9Y5B | IC-7340 | REVIEW REQUIRED | Historical - verify before use |
| EX-B-25-579 | IC-5269 | DEPRECATED | Historical - verify before use |
| Continental Solutions NV | IC-6749 | DEPRECATED | Historical - verify before use |
| SIG-25-WCC-PPMH | IC-8183 | PROVISIONAL | Historical - verify before use |
| SIG-24-PBC-613L | IC-5560 | REVIEW REQUIRED | Historical - verify before use |
| SIG-49-UKY-6H3R | IC-6311 | DEPRECATED | Historical - verify before use |
| lactic acid 98% | IC-6714 | SUPERSEDED | Historical - verify before use |
| Soja Isolate 99.5% | IC-7721 | REVIEW REQUIRED | Historical - verify before use |
| dextrin premium | IC-9302 | SUPERSEDED | Historical - verify before use |
| customs duty fr 15% | IC-6426 | SUPERSEDED | Historical - verify before use |
| QU-PR-732 SA | IC-6689 | SUPERSEDED | Historical - verify before use |
| Sodium Benzoate 98% | IC-6937 | DEPRECATED | Historical - verify before use |
| Maltodextrin DE15 Premium | IC-9144 | SUPERSEDED | Historical - verify before use |
| Customs Duty CN 10% | IC-6231 | SUPERSEDED | Historical - verify before use |
| SIG-99-IZM-CYBY | IC-9934 | PROVISIONAL | Historical - verify before use |
| DE-PH-GR-173 | IC-5768 | SUPERSEDED | Historical - verify before use |
| Wheat Gluten 25% Food Grade | IC-6360 | DEPRECATED | Historical - verify before use |
| citric acid | IC-9982 | PROVISIONAL | Historical - verify before use |
| Premier Trading Group | IC-9748 | SUPERSEDED | Historical - verify before use |
| Weizenklebereiweiß Qualitätsstufe II | IC-7472 | REVIEW REQUIRED | Historical - verify before use |
| Soja Isolate Lebensmittelrein | IC-9688 | REVIEW REQUIRED | Historical - verify before use |
| Sonnenblumenöl 50% Qualitätsstufe I | IC-8790 | DEPRECATED | Historical - verify before use |
| PE-PR-557 | IC-9143 | SUPERSEDED | Historical - verify before use |
| Stratos Materials | IC-7899 | REVIEW REQUIRED | Historical - verify before use |
| SIG-10-BLC-3L38 | IC-9841 | REVIEW REQUIRED | Historical - verify before use |
| Baltic Industrien NV | IC-7852 | PROVISIONAL | Historical - verify before use |
| Glucose Syrup Technical | IC-6742 | DEPRECATED | Historical - verify before use |
| Calcium Carbonate | IC-9634 | PROVISIONAL | Historical - verify before use |
| SIG-45-ZHK-QWIG | IC-6710 | DEPRECATED | Historical - verify before use |
| SIG-15-VIS-079C | IC-6373 | REVIEW REQUIRED | Historical - verify before use |
| SIG-76-GDP-2JN8 | IC-9580 | DEPRECATED | Historical - verify before use |
| SIG-83-TEU-OH8F Group | IC-5143 | REVIEW REQUIRED | Historical - verify before use |
| Fructose Technische Qualität | IC-8748 | DEPRECATED | Historical - verify before use |
| Potassium Sorbate Standard | IC-6841 | REVIEW REQUIRED | Historical - verify before use |
| SIG-19-TLQ-1P5Z | IC-9136 | REVIEW REQUIRED | Historical - verify before use |
| SIG-44-NHM-IY9D | IC-7714 | SUPERSEDED | Historical - verify before use |
| SO-AC-GR-A-997 | IC-9201 | REVIEW REQUIRED | Historical - verify before use |
| Rapeseed Oil Grade A | IC-6751 | SUPERSEDED | Historical - verify before use |
| cyclodextrin 70% food grade | IC-5027 | PROVISIONAL | Historical - verify before use |
| WI-F-10-935 | IC-6989 | PROVISIONAL | Historical - verify before use |
| CI-AC-ST-565 | IC-9936 | PROVISIONAL | Historical - verify before use |
| Pinnacle Materials SA | IC-5893 | REVIEW REQUIRED | Historical - verify before use |
| excise in 7% | IC-6088 | SUPERSEDED | Historical - verify before use |
| Sodium Chloride | IC-9318 | REVIEW REQUIRED | Historical - verify before use |
| SIG-71-OEX-5BRF | IC-9004 | SUPERSEDED | Historical - verify before use |
| SIG-16-YRD-5C3Z | IC-5018 | SUPERSEDED | Historical - verify before use |
| SIG-43-TPO-RSBY | IC-6638 | DEPRECATED | Historical - verify before use |
| SIG-92-CZO-O9ON | IC-5665 | PROVISIONAL | Historical - verify before use |
| Pacific Vertrieb International | IC-8246 | PROVISIONAL | Historical - verify before use |
| SIG-76-PYX-S5PY | IC-8108 | PROVISIONAL | Historical - verify before use |
| Ascorbic Acid Premiumqualität | IC-6432 | DEPRECATED | Historical - verify before use |
| Cyclodextrin | IC-8875 | REVIEW REQUIRED | Historical - verify before use |
| Resistant Starch Pharma Grade | IC-9695 | PROVISIONAL | Historical - verify before use |
| calcium carbonate | IC-5771 | DEPRECATED | Historical - verify before use |
| Global Logistics | IC-6988 | SUPERSEDED | Historical - verify before use |
| SIG-58-JZY-SBU1 | IC-6260 | DEPRECATED | Historical - verify before use |
| Vertex Sourcing | IC-6019 | REVIEW REQUIRED | Historical - verify before use |
| coconut oil 70% | IC-6252 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat | IC-9002 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-GR-B-273 | IC-9569 | PROVISIONAL | Historical - verify before use |
| dextrin standard | IC-5988 | DEPRECATED | Historical - verify before use |
| Sorbinsäure Qualitätsstufe II | IC-8532 | SUPERSEDED | Historical - verify before use |
| SIG-86-VGU-A4FE | IC-9208 | SUPERSEDED | Historical - verify before use |
| Lactic Acid 25% | IC-5285 | PROVISIONAL | Historical - verify before use |
| SIG-46-SVJ-5IZO | IC-5621 | DEPRECATED | Historical - verify before use |
| Wheat Gluten 50% Pharma Grade | IC-9200 | REVIEW REQUIRED | Historical - verify before use |
| SIG-64-ILX-G2AZ PLC | IC-5914 | REVIEW REQUIRED | Historical - verify before use |


#### 4.3.4 Excluded Assignments

Assignments excluded from scope per stakeholder decision:

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-7989-B | Missing required attributes | Business owner notified |
| NOISE-9909-H | Pending validation | Manual review scheduled |
| NOISE-7304-B | Pending validation | Manual review scheduled |
| NOISE-8022-E | Missing required attributes | Business owner notified |
| NOISE-8340-H | Out of scope per business decision | Business owner notified |
| NOISE-5133-D | Pending validation | Manual review scheduled |
| NOISE-8118-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-3701-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7807-B | Pending validation | Manual review scheduled |
| NOISE-1435-D | Missing required attributes | Business owner notified |
| NOISE-2800-A | Out of scope per business decision | Business owner notified |
| NOISE-2418-G | Pending validation | Business owner notified |
| NOISE-8209-F | Data quality insufficient | Escalated to data steward |
| NOISE-2613-G | Duplicate source record | Business owner notified |
| NOISE-4061-B | Data quality insufficient | Escalated to data steward |
| NOISE-7678-F | Missing required attributes | Manual review scheduled |
| NOISE-1920-F | Missing required attributes | Manual review scheduled |
| NOISE-6881-B | Pending validation | Business owner notified |
| NOISE-7531-E | Data quality insufficient | Business owner notified |
| NOISE-8157-F | Duplicate source record | Business owner notified |
| NOISE-6741-H | Pending validation | Business owner notified |
| NOISE-4078-G | Data quality insufficient | Escalated to data steward |
| NOISE-5707-E | Missing required attributes | Escalated to data steward |
| NOISE-5536-H | Duplicate source record | Business owner notified |
| NOISE-7495-A | Pending validation | Escalated to data steward |
| NOISE-6584-F | Missing required attributes | Manual review scheduled |
| NOISE-9343-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-5972-D | Pending validation | Business owner notified |
| NOISE-3549-D | Pending validation | Escalated to data steward |
| NOISE-2573-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-1781-C | Duplicate source record | Business owner notified |
| NOISE-6369-H | Pending validation | Escalated to data steward |
| NOISE-5608-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8043-E | Pending validation | Business owner notified |
| NOISE-4177-G | Duplicate source record | Business owner notified |
| NOISE-7552-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7174-G | Duplicate source record | Escalated to data steward |
| NOISE-2190-H | Pending validation | Manual review scheduled |
| NOISE-3455-G | Out of scope per business decision | Business owner notified |
| NOISE-3388-E | Pending validation | Manual review scheduled |
| NOISE-2318-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-9429-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-5119-G | Missing required attributes | Manual review scheduled |
| NOISE-7051-H | Duplicate source record | Escalated to data steward |
| NOISE-6279-A | Pending validation | Deferred to Phase 2 |
| NOISE-6568-D | Pending validation | Business owner notified |
| NOISE-1559-B | Data quality insufficient | Business owner notified |
| NOISE-8897-H | Missing required attributes | Manual review scheduled |
| NOISE-7087-D | Out of scope per business decision | Manual review scheduled |
| NOISE-3836-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-4485-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3170-G | Out of scope per business decision | Business owner notified |
| NOISE-8960-H | Out of scope per business decision | Escalated to data steward |
| NOISE-7346-B | Data quality insufficient | Escalated to data steward |
| NOISE-5962-B | Pending validation | Business owner notified |
| NOISE-2121-E | Missing required attributes | Manual review scheduled |
| NOISE-5097-F | Data quality insufficient | Escalated to data steward |
| NOISE-8885-G | Duplicate source record | Escalated to data steward |
| NOISE-6164-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-7829-B | Data quality insufficient | Escalated to data steward |
| NOISE-5976-E | Data quality insufficient | Manual review scheduled |
| NOISE-9692-C | Pending validation | Escalated to data steward |
| NOISE-7957-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-7360-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5130-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-5704-F | Missing required attributes | Manual review scheduled |
| NOISE-2008-F | Pending validation | Escalated to data steward |
| NOISE-1480-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-7512-C | Out of scope per business decision | Escalated to data steward |
| NOISE-1819-D | Data quality insufficient | Escalated to data steward |
| NOISE-5394-G | Out of scope per business decision | Escalated to data steward |
| NOISE-1530-D | Missing required attributes | Escalated to data steward |
| NOISE-6211-G | Missing required attributes | Escalated to data steward |
| NOISE-3788-C | Pending validation | Manual review scheduled |
| NOISE-7692-B | Missing required attributes | Escalated to data steward |
| NOISE-8819-G | Duplicate source record | Business owner notified |
| NOISE-9584-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7297-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-8990-F | Out of scope per business decision | Escalated to data steward |
| NOISE-5431-C | Out of scope per business decision | Manual review scheduled |
| NOISE-1995-A | Out of scope per business decision | Business owner notified |
| NOISE-2006-H | Out of scope per business decision | Business owner notified |
| NOISE-4917-A | Out of scope per business decision | Manual review scheduled |
| NOISE-1362-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-9196-E | Out of scope per business decision | Escalated to data steward |
| NOISE-5945-C | Missing required attributes | Business owner notified |
| NOISE-1382-D | Duplicate source record | Manual review scheduled |
| NOISE-2423-C | Out of scope per business decision | Escalated to data steward |
| NOISE-1385-F | Data quality insufficient | Escalated to data steward |
| NOISE-2071-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-4204-G | Missing required attributes | Business owner notified |
| NOISE-6493-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7167-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-5630-E | Duplicate source record | Manual review scheduled |
| NOISE-2190-C | Pending validation | Business owner notified |
| NOISE-1009-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-1170-D | Missing required attributes | Business owner notified |
| NOISE-2036-D | Pending validation | Business owner notified |
| NOISE-8151-F | Pending validation | Escalated to data steward |
| NOISE-3686-F | Out of scope per business decision | Manual review scheduled |
| NOISE-3247-E | Out of scope per business decision | Escalated to data steward |
| NOISE-7015-F | Duplicate source record | Business owner notified |
| NOISE-4082-C | Data quality insufficient | Manual review scheduled |
| NOISE-6652-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-8155-E | Data quality insufficient | Escalated to data steward |
| NOISE-5096-E | Duplicate source record | Escalated to data steward |
| NOISE-4422-C | Data quality insufficient | Manual review scheduled |
| NOISE-7098-C | Duplicate source record | Business owner notified |
| NOISE-3594-D | Missing required attributes | Escalated to data steward |
| NOISE-3159-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-7858-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-1119-H | Missing required attributes | Manual review scheduled |
| NOISE-9704-B | Data quality insufficient | Business owner notified |
| NOISE-3148-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5004-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-4664-F | Pending validation | Manual review scheduled |
| NOISE-9306-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-4407-F | Missing required attributes | Business owner notified |
| NOISE-1975-G | Out of scope per business decision | Business owner notified |
| NOISE-5905-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4531-B | Pending validation | Manual review scheduled |
| NOISE-4899-G | Missing required attributes | Business owner notified |
| NOISE-7804-G | Out of scope per business decision | Business owner notified |
| NOISE-1020-H | Missing required attributes | Manual review scheduled |
| NOISE-3355-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2929-D | Out of scope per business decision | Business owner notified |
| NOISE-2771-E | Duplicate source record | Manual review scheduled |
| NOISE-1283-F | Data quality insufficient | Manual review scheduled |
| NOISE-5395-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4202-F | Pending validation | Business owner notified |
| NOISE-6464-C | Missing required attributes | Business owner notified |
| NOISE-3197-E | Missing required attributes | Escalated to data steward |
| NOISE-9209-C | Data quality insufficient | Business owner notified |
| NOISE-3215-F | Pending validation | Escalated to data steward |
| NOISE-3661-B | Missing required attributes | Business owner notified |
| NOISE-5008-H | Pending validation | Deferred to Phase 2 |
| NOISE-4354-B | Data quality insufficient | Business owner notified |
| NOISE-3664-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-1576-G | Data quality insufficient | Business owner notified |
| NOISE-6666-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7239-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7972-H | Missing required attributes | Business owner notified |
| NOISE-1393-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-9517-D | Out of scope per business decision | Manual review scheduled |
| NOISE-2401-B | Pending validation | Business owner notified |
| NOISE-8006-G | Out of scope per business decision | Escalated to data steward |
| NOISE-1249-G | Data quality insufficient | Escalated to data steward |
| NOISE-6789-F | Out of scope per business decision | Business owner notified |
| NOISE-2527-D | Missing required attributes | Escalated to data steward |
| NOISE-3436-G | Pending validation | Business owner notified |
| NOISE-6722-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-7041-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-1298-D | Data quality insufficient | Business owner notified |
| NOISE-5947-C | Data quality insufficient | Manual review scheduled |
| NOISE-4905-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9815-E | Missing required attributes | Business owner notified |
| NOISE-1614-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3510-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-2750-A | Missing required attributes | Business owner notified |
| NOISE-5592-B | Data quality insufficient | Escalated to data steward |
| NOISE-6835-H | Data quality insufficient | Escalated to data steward |
| NOISE-1074-B | Duplicate source record | Manual review scheduled |
| NOISE-3075-F | Out of scope per business decision | Manual review scheduled |
| NOISE-7755-A | Duplicate source record | Business owner notified |
| NOISE-6841-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9616-D | Missing required attributes | Escalated to data steward |
| NOISE-5196-C | Pending validation | Business owner notified |
| NOISE-3789-C | Pending validation | Escalated to data steward |
| NOISE-6850-B | Out of scope per business decision | Escalated to data steward |
| NOISE-2329-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2130-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-5896-A | Pending validation | Deferred to Phase 2 |
| NOISE-9507-A | Out of scope per business decision | Manual review scheduled |
| NOISE-5182-F | Pending validation | Business owner notified |
| NOISE-6923-E | Out of scope per business decision | Business owner notified |
| NOISE-4221-B | Pending validation | Manual review scheduled |
| NOISE-3101-G | Data quality insufficient | Escalated to data steward |
| NOISE-5924-H | Pending validation | Escalated to data steward |
| NOISE-1081-B | Pending validation | Escalated to data steward |
| NOISE-6580-E | Missing required attributes | Business owner notified |
| NOISE-2326-B | Data quality insufficient | Business owner notified |
| NOISE-3370-F | Missing required attributes | Manual review scheduled |
| NOISE-3502-H | Pending validation | Manual review scheduled |
| NOISE-1349-C | Duplicate source record | Escalated to data steward |
| NOISE-9112-D | Duplicate source record | Escalated to data steward |
| NOISE-2562-C | Out of scope per business decision | Manual review scheduled |
| NOISE-5254-H | Pending validation | Business owner notified |
| NOISE-3087-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3417-A | Pending validation | Deferred to Phase 2 |
| NOISE-5065-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6824-F | Out of scope per business decision | Business owner notified |
| NOISE-4723-G | Pending validation | Business owner notified |
| NOISE-4738-F | Pending validation | Manual review scheduled |
| NOISE-9539-B | Missing required attributes | Business owner notified |
| NOISE-3442-B | Data quality insufficient | Business owner notified |
| NOISE-4841-C | Missing required attributes | Escalated to data steward |
| NOISE-2961-A | Out of scope per business decision | Manual review scheduled |
| NOISE-8025-F | Out of scope per business decision | Business owner notified |
| NOISE-9589-G | Out of scope per business decision | Escalated to data steward |
| NOISE-1166-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-8759-D | Data quality insufficient | Escalated to data steward |
| NOISE-2018-C | Missing required attributes | Escalated to data steward |
| NOISE-1948-D | Data quality insufficient | Escalated to data steward |
| NOISE-4209-H | Data quality insufficient | Manual review scheduled |
| NOISE-9594-F | Out of scope per business decision | Business owner notified |
| NOISE-3715-C | Pending validation | Escalated to data steward |
| NOISE-2301-B | Pending validation | Deferred to Phase 2 |
| NOISE-7805-E | Out of scope per business decision | Escalated to data steward |
| NOISE-9969-B | Pending validation | Manual review scheduled |
| NOISE-5712-E | Pending validation | Business owner notified |
| NOISE-8956-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1892-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-4117-H | Duplicate source record | Escalated to data steward |
| NOISE-6044-E | Data quality insufficient | Business owner notified |
| NOISE-8469-H | Duplicate source record | Business owner notified |
| NOISE-4597-F | Duplicate source record | Manual review scheduled |
| NOISE-7103-G | Out of scope per business decision | Manual review scheduled |
| NOISE-9572-B | Out of scope per business decision | Business owner notified |
| NOISE-6780-F | Missing required attributes | Business owner notified |
| NOISE-9005-D | Out of scope per business decision | Manual review scheduled |
| NOISE-8036-B | Data quality insufficient | Escalated to data steward |
| NOISE-6171-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9579-H | Out of scope per business decision | Escalated to data steward |
| NOISE-6066-A | Missing required attributes | Escalated to data steward |
| NOISE-5354-E | Pending validation | Deferred to Phase 2 |
| NOISE-1115-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-3776-F | Missing required attributes | Escalated to data steward |
| NOISE-4428-C | Out of scope per business decision | Manual review scheduled |
| NOISE-3174-D | Out of scope per business decision | Escalated to data steward |
| NOISE-4122-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2737-E | Missing required attributes | Business owner notified |
| NOISE-5621-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-8907-D | Missing required attributes | Escalated to data steward |
| NOISE-5530-A | Out of scope per business decision | Escalated to data steward |
| NOISE-1157-A | Out of scope per business decision | Escalated to data steward |
| NOISE-6830-D | Pending validation | Escalated to data steward |
| NOISE-8577-C | Pending validation | Manual review scheduled |
| NOISE-3206-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-7908-A | Missing required attributes | Manual review scheduled |
| NOISE-5257-G | Data quality insufficient | Business owner notified |
| NOISE-9596-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8892-B | Pending validation | Manual review scheduled |
| NOISE-6010-B | Out of scope per business decision | Business owner notified |
| NOISE-9277-E | Pending validation | Manual review scheduled |
| NOISE-7790-B | Duplicate source record | Business owner notified |
| NOISE-1435-H | Data quality insufficient | Escalated to data steward |
| NOISE-4098-D | Pending validation | Manual review scheduled |
| NOISE-8560-E | Pending validation | Manual review scheduled |
| NOISE-7879-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-8236-H | Missing required attributes | Escalated to data steward |
| NOISE-6006-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2713-D | Duplicate source record | Escalated to data steward |
| NOISE-6552-D | Data quality insufficient | Business owner notified |
| NOISE-3890-F | Out of scope per business decision | Manual review scheduled |
| NOISE-9685-E | Out of scope per business decision | Manual review scheduled |
| NOISE-4787-A | Duplicate source record | Escalated to data steward |
| NOISE-4099-E | Pending validation | Escalated to data steward |
| NOISE-7562-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9434-F | Missing required attributes | Escalated to data steward |
| NOISE-8220-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8323-C | Data quality insufficient | Escalated to data steward |
| NOISE-7543-G | Pending validation | Manual review scheduled |
| NOISE-9167-B | Data quality insufficient | Manual review scheduled |
| NOISE-2336-H | Out of scope per business decision | Business owner notified |
| NOISE-9612-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-6586-B | Pending validation | Manual review scheduled |
| NOISE-4806-F | Missing required attributes | Escalated to data steward |
| NOISE-5946-B | Duplicate source record | Business owner notified |
| NOISE-3279-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-3108-F | Out of scope per business decision | Manual review scheduled |
| NOISE-8630-A | Pending validation | Business owner notified |
| NOISE-4940-H | Duplicate source record | Manual review scheduled |
| NOISE-7294-A | Pending validation | Manual review scheduled |
| NOISE-5177-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1887-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9437-C | Out of scope per business decision | Manual review scheduled |
| NOISE-9607-E | Duplicate source record | Escalated to data steward |
| NOISE-6333-C | Data quality insufficient | Business owner notified |
| NOISE-8827-D | Pending validation | Manual review scheduled |
| NOISE-3644-G | Missing required attributes | Business owner notified |
| NOISE-2294-H | Pending validation | Escalated to data steward |
| NOISE-9833-F | Data quality insufficient | Business owner notified |
| NOISE-8074-D | Pending validation | Escalated to data steward |
| NOISE-3438-B | Pending validation | Deferred to Phase 2 |
| NOISE-8357-B | Data quality insufficient | Escalated to data steward |
| NOISE-9415-G | Missing required attributes | Manual review scheduled |
| NOISE-9386-A | Duplicate source record | Manual review scheduled |
| NOISE-4275-B | Missing required attributes | Business owner notified |
| NOISE-8830-H | Data quality insufficient | Manual review scheduled |
| NOISE-1616-A | Duplicate source record | Manual review scheduled |
| NOISE-8750-B | Duplicate source record | Manual review scheduled |
| NOISE-2305-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4506-H | Data quality insufficient | Escalated to data steward |
| NOISE-3492-H | Pending validation | Business owner notified |
| NOISE-4444-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-3500-C | Out of scope per business decision | Business owner notified |
| NOISE-5217-E | Out of scope per business decision | Escalated to data steward |
| NOISE-4787-H | Duplicate source record | Deferred to Phase 2 |
| NOISE-1973-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-6136-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7913-D | Duplicate source record | Manual review scheduled |
| NOISE-4068-B | Pending validation | Business owner notified |
| NOISE-7555-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4144-B | Data quality insufficient | Manual review scheduled |
| NOISE-5173-E | Pending validation | Business owner notified |
| NOISE-5317-E | Data quality insufficient | Business owner notified |
| NOISE-7685-G | Out of scope per business decision | Manual review scheduled |
| NOISE-1381-F | Missing required attributes | Business owner notified |
| NOISE-3036-A | Out of scope per business decision | Manual review scheduled |


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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230730_000000`
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
| Project Lead | Lisa Rodriguez (Quality Assurance) | lisa@company.com | +1-555-0101 |
| Technical Lead | Anna Mueller (EU Compliance) | anna@company.com | +1-555-0102 |
| Business Owner | Maria Garcia (Supply Chain) | maria@company.com | +1-555-0103 |
| Data Steward | Michael Weber (Business Operations) | michael@company.com | +1-555-0104 |

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
