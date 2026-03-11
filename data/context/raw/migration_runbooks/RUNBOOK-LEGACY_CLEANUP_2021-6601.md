# Migration Runbook: System Migration: LEGACY_CLEANUP_2021

**Document ID**: RB-LEGACY_CLEANUP_2021-9395
**Version**: 2.3
**Last Updated**: 2023-06-27
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the System Migration: LEGACY_CLEANUP_2021 project.
The migration involves transitioning master data and transactional records from SOURCE
to TARGET while maintaining data integrity and business continuity.

**Project Timeline**: 2023-04-01 to 2023-07-08
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
| Total entities assessed | 1541 | Completed |
| Codes assigned | 1070 | Staged |
| Excluded from scope | 321 | Documented |
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

| Source Entity (SOURCE) | Internal Code | Assignment Date | Department |
|--------------------------------|---------------|-----------------|------------|
| Premier Partners Group | BC-8278 | 2023-10-26 | Operations |
| SIG-25-WDK-CWCD | TC-8310 | 2021-01-26 | Data Governance |
| lactic acid standard | BC-8327 | 2023-02-22 | Operations |
| Zitronensäure | IC-8333 | 2021-10-02 | Operations |
| Vat Standardqualität BR 25% | TC-8337 | 2023-07-16 | IT Infrastructure |
| Baltic Processing PLC | TC-8350 | 2022-11-17 | Data Governance |
| Pinnacle Materials | TC-8358 | 2023-12-23 | Finance |
| Citric Acid 70% | BC-8365 | 2022-09-25 | Operations |
| SIG-69-XLH-L6HZ | TC-8368 | 2023-09-26 | Supply Chain |
| Dextrose Grade A | BC-8369 | 2023-09-16 | Product Management |
| central distribution | IC-8375 | 2024-03-01 | Finance |
| Quantum Commodities PLC | TC-8396 | 2022-06-22 | Data Governance |
| WH-GL-ST-378 | BC-8407 | 2021-11-21 | Data Governance |
| VA-RE-F-21-230 | IC-8414 | 2023-10-01 | Product Management |
| WH-GL-146 | BC-8420 | 2021-10-15 | Compliance |
| sorbic acid | TC-8431 | 2021-03-08 | Finance |
| quantum logistics | TC-8449 | 2021-10-27 | Product Management |
| Lactic Acid | TC-8473 | 2023-11-07 | Data Governance |
| Resistente Stärke Lebensmittelrein | IC-8491 | 2022-10-18 | Supply Chain |
| Resistant Starch Pharma Grade | IC-8503 | 2024-05-05 | Operations |
| Maltodextrin-Pulver DE15 | BC-8508 | 2022-08-08 | Product Management |
| ME-IN-934 NV | IC-8521 | 2024-01-20 | Operations |
| SIG-13-CAZ-HXXP | BC-8537 | 2024-10-24 | Finance |
| SIG-66-DRZ-QEHY | BC-8540 | 2023-03-20 | Operations |
| Soy Isolate 98% | TC-8545 | 2024-07-19 | Supply Chain |
| Lactic Acid | IC-8588 | 2022-05-21 | Product Management |
| Lactic Acid | IC-8624 | 2024-07-21 | IT Infrastructure |
| resistant starch | IC-8639 | 2021-02-23 | Finance |
| SIG-67-TPL-WT5F | IC-8658 | 2021-10-23 | Compliance |
| coconut oil food grade | BC-8664 | 2022-09-28 | Data Governance |
| Coconut Oil | BC-8689 | 2022-07-25 | Operations |
| SIG-24-VMY-QMRL | BC-8699 | 2022-01-13 | Finance |
| vertex materials | IC-8707 | 2022-11-11 | Finance |
| Sorbinsäure Premiumqualität | BC-8708 | 2022-04-28 | Operations |
| Apex Versorgung GmbH | TC-8710 | 2021-10-08 | Product Management |
| GL-SY-70-549 | TC-8714 | 2022-12-23 | IT Infrastructure |
| PO-SO-GR-A-715 | IC-8718 | 2021-09-18 | Compliance |
| nordic manufacturing International | TC-8729 | 2023-02-07 | Data Governance |
| HO-DI-531 Group | IC-8754 | 2024-04-11 | IT Infrastructure |
| nexus ingredients SAS | IC-8762 | 2023-04-17 | Product Management |
| Cyclodextrin Standardqualität | TC-8784 | 2022-03-07 | IT Infrastructure |
| Sorbinsäure 98% | IC-8807 | 2021-09-23 | Product Management |
| meridian sourcing | BC-8808 | 2021-07-11 | Finance |
| Coconut Oil Standard | BC-8814 | 2021-10-22 | Compliance |
| central distribution | TC-8843 | 2021-02-22 | IT Infrastructure |
| SIG-22-TOX-02GV | TC-8849 | 2023-11-05 | Operations |
| LA-AC-891 | IC-8864 | 2021-09-26 | Operations |
| PA-OI-70-GR-B-781 | TC-8881 | 2023-10-01 | Data Governance |
| dextrose 25% tech grade | BC-8884 | 2023-06-23 | Finance |
| Coconut Oil 50% | TC-8896 | 2023-02-11 | Finance |
| Glucose Syrup 70% | TC-8913 | 2023-10-25 | IT Infrastructure |
| prism supply | TC-8914 | 2024-09-10 | Supply Chain |
| Resistente Stärke 50% Standardqualität | IC-8923 | 2024-08-22 | IT Infrastructure |
| wheat gluten premium | BC-8932 | 2023-02-14 | Operations |
| Sodium Benzoate Grade A | TC-8945 | 2024-01-15 | Supply Chain |
| Withholding NL 7% | TC-8955 | 2022-09-08 | Operations |
| Atlantic Materials | IC-8961 | 2021-01-12 | Supply Chain |
| Core Trading | IC-8971 | 2021-01-17 | IT Infrastructure |
| baltic solutions Group | IC-8986 | 2021-12-21 | Data Governance |
| Zitronensäure Premiumqualität | IC-8989 | 2021-04-04 | Compliance |
| SIG-39-KYF-P35A | BC-8999 | 2022-09-22 | Data Governance |
| Prism Werkstoffe | TC-9034 | 2021-07-27 | IT Infrastructure |
| resistant starch 98% pharma grade | BC-9035 | 2024-02-14 | Data Governance |
| nexus logistics | BC-9040 | 2022-05-12 | Finance |
| SIG-13-ZIB-S8MV International | TC-9066 | 2023-06-07 | Operations |
| Palm Oil | BC-9070 | 2023-04-13 | Finance |
| Isoglucose Premium | IC-9094 | 2023-07-12 | Supply Chain |
| fructose premium | BC-9099 | 2024-09-03 | Operations |
| VA-ST-D-10-295 | BC-9110 | 2023-08-27 | Compliance |
| CA-50-GR-B-203 | IC-9115 | 2024-05-07 | Product Management |
| Prime Versorgung GmbH | BC-9123 | 2023-04-26 | Supply Chain |
| Isoglucose Technical | IC-9140 | 2022-04-13 | IT Infrastructure |
| SIG-59-ZZK-AYAJ PLC | TC-9167 | 2023-11-08 | Finance |
| Fructose | BC-9177 | 2022-01-14 | Operations |
| Natriumbenzoat Standardqualität | BC-9188 | 2022-12-17 | IT Infrastructure |
| Cyclodextrin Premiumqualität | TC-9194 | 2021-03-03 | Compliance |
| SIG-39-QZD-93EZ | TC-9198 | 2022-03-15 | Product Management |
| Dextrin 70% Pharmazeutisch rein | IC-9204 | 2023-02-12 | Compliance |
| Maltodextrin DE10 | IC-9224 | 2021-05-20 | Product Management |
| WI-U-10-721 | IC-9225 | 2023-10-07 | Product Management |
| atlas sourcing | BC-9236 | 2021-06-23 | IT Infrastructure |
| NO-SU-CO-376 | TC-9242 | 2023-12-24 | IT Infrastructure |
| SIG-88-AGF-FF5L | TC-9257 | 2024-06-28 | Data Governance |
| Natriumbenzoat 25% | BC-9283 | 2023-03-03 | Product Management |
| excise in 10% | TC-9306 | 2021-10-27 | Operations |
| withholding fr 10% | BC-9313 | 2023-08-10 | Supply Chain |
| Continental Enterprise Holdings | IC-9345 | 2024-09-01 | Compliance |
| Vanguard Logistics | TC-9347 | 2022-07-02 | Operations |
| Glukosesirup Syrup Technische Qualität | TC-9348 | 2021-06-11 | Product Management |
| Premier Logistics | BC-9351 | 2024-08-14 | Compliance |
| EL-SO-688 | TC-9373 | 2024-08-12 | Finance |
| Maltodextrin DE5 Grade B | IC-9377 | 2022-07-21 | Finance |
| vat standard gb 19% | TC-9382 | 2021-04-06 | Data Governance |
| Catalyst Industries International | TC-9393 | 2024-08-03 | Data Governance |
| Palmfett Qualitätsstufe II | IC-9406 | 2021-07-24 | Finance |
| Isoglucose | IC-9408 | 2021-04-27 | Finance |
| SIG-65-IJJ-DXAJ SA | IC-9439 | 2023-08-23 | Product Management |
| sodium benzoate 99.5% tech grade | IC-9445 | 2024-09-21 | Data Governance |
| Casein 25% Pharma Grade | IC-9449 | 2024-01-15 | Operations |
| SIG-52-HZA-742D | IC-9454 | 2023-10-13 | Operations |
| Vat Standardqualität IN 0% | BC-9459 | 2022-01-23 | Supply Chain |
| Vanguard Partners PLC | BC-9467 | 2021-11-18 | Product Management |
| Resistant Starch 70% Food Grade | TC-9471 | 2024-04-16 | Product Management |
| Casein Technical | BC-9473 | 2024-08-24 | Operations |
| vanguard industries PLC | IC-9475 | 2023-11-11 | Product Management |
| AS-AC-130 | BC-9488 | 2023-04-24 | Supply Chain |
| Pea Protein Premiumqualität | IC-9503 | 2022-03-19 | Product Management |
| SIG-40-NOO-BAK8 | IC-9509 | 2021-02-07 | Product Management |
| Customs Duty FR 7% | BC-9513 | 2024-01-23 | Product Management |
| fructose standard | TC-9519 | 2024-01-18 | Supply Chain |
| Potassium Sorbate Food Grade | TC-9522 | 2024-05-03 | Compliance |
| PO-SO-TE-239 | IC-9525 | 2022-01-01 | Supply Chain |
| SIG-60-KAS-IVMD | IC-9528 | 2024-06-05 | Compliance |
| Vat Reduced GB 25% | BC-9562 | 2022-05-22 | IT Infrastructure |
| DE-70-PH-GR-978 | TC-9564 | 2022-12-22 | Product Management |
| SIG-60-KAS-IVMD | BC-9583 | 2022-11-07 | Supply Chain |
| Dextrin 50% | IC-9591 | 2023-02-06 | Compliance |
| Resistant Starch Grade B | TC-9596 | 2024-07-18 | Operations |
| EX-F-21-883 | TC-9599 | 2023-12-14 | Data Governance |
| Zitronensäure | TC-9618 | 2024-09-02 | Operations |
| SIG-75-XPL-QWB7 GmbH | TC-9647 | 2022-12-04 | IT Infrastructure |
| PA-OI-70-GR-B-781 | TC-9649 | 2023-08-01 | Product Management |
| CA-CA-50-GR-A-195 | BC-9652 | 2021-07-03 | Supply Chain |
| DE-GR-B-157 | IC-9675 | 2021-11-05 | Product Management |
| Maltodextrin-Pulver DE10 | IC-9710 | 2022-06-01 | Data Governance |
| RA-OI-99.5-602 | BC-9719 | 2022-05-16 | IT Infrastructure |
| Palmfett 98% Qualitätsstufe I | BC-9722 | 2023-06-01 | IT Infrastructure |
| NE-LO-735 | TC-9725 | 2022-04-15 | Data Governance |
| Zitronensäure | BC-9735 | 2024-08-18 | IT Infrastructure |
| Kasein 98% Technische Qualität | IC-9744 | 2021-11-27 | IT Infrastructure |
| SO-BE-50-427 | IC-9764 | 2024-10-08 | Data Governance |
| HO-LO-534 PLC | BC-9770 | 2022-02-15 | Data Governance |
| SO-CH-70-365 | TC-9789 | 2021-07-24 | Operations |
| GL-SY-TE-803 | BC-9790 | 2024-11-26 | Data Governance |
| GL-LO-935 | IC-9794 | 2022-02-04 | IT Infrastructure |
| SIG-95-APX-PWFS | BC-9801 | 2024-01-10 | Supply Chain |
| potassium sorbate premium | TC-9816 | 2021-10-21 | Supply Chain |
| catalyst supply | IC-9823 | 2021-08-10 | Supply Chain |
| wheat gluten premium | IC-9849 | 2023-08-05 | Operations |
| Maltodextrin DE25 | TC-9850 | 2023-02-10 | Operations |
| Ascorbic Acid Pharmazeutisch rein | IC-9870 | 2024-11-06 | Supply Chain |
| SIG-18-LLP-8GUU | IC-9897 | 2022-02-20 | Supply Chain |
| CI-AC-25-GR-A-669 | BC-9913 | 2022-04-08 | Product Management |
| WI-B-10-442 | TC-9917 | 2023-10-15 | Data Governance |
| Sorbic Acid | IC-9919 | 2021-01-05 | Operations |
| Vat Reduced US 19% | IC-9922 | 2022-09-11 | Compliance |
| SIG-64-QID-BCT3 | BC-9939 | 2021-06-05 | Finance |
| Quantum Supply Co. | TC-9953 | 2021-07-15 | Operations |
| RE-ST-FO-GR-998 | IC-9958 | 2023-02-14 | Supply Chain |
| pacific distribution | TC-9963 | 2023-10-11 | Supply Chain |
| RA-OI-TE-584 | IC-9964 | 2021-02-13 | Product Management |
| CA-884 | IC-9965 | 2024-01-15 | IT Infrastructure |
| Sorbinsäure | IC-9976 | 2021-06-16 | Finance |
| PO-SO-480 | TC-9977 | 2024-10-01 | Product Management |
| Sorbic Acid 98% | BC-9984 | 2022-09-11 | Operations |
| ST-TR-786 International | TC-10001 | 2023-07-28 | IT Infrastructure |
| Rapsöl Lebensmittelrein | IC-10002 | 2023-02-02 | Finance |
| SIG-13-PHC-GSY7 | BC-10028 | 2023-07-15 | Supply Chain |
| Pacific Industrien | TC-10031 | 2021-05-12 | Product Management |
| DE-70-512 | BC-10047 | 2023-01-27 | Data Governance |
| Lactic Acid | IC-10057 | 2021-10-09 | Compliance |
| Coconut Oil 70% | BC-10066 | 2024-05-20 | Operations |
| Lactic Acid 70% Pharmazeutisch rein | BC-10074 | 2024-03-14 | Finance |
| Natriumchlorid 98% Standardqualität | TC-10088 | 2021-08-22 | Data Governance |
| SIG-50-PNF-Z2E8 | TC-10092 | 2021-06-07 | Operations |
| SIG-13-BSD-DJSO International | TC-10096 | 2023-08-13 | Operations |
| nexus enterprise | TC-10111 | 2024-03-13 | Compliance |
| PI-PR-193 | BC-10126 | 2021-05-13 | Data Governance |
| Dextrin 50% | BC-10131 | 2024-05-05 | IT Infrastructure |
| sodium chloride 70% | IC-10133 | 2023-12-11 | Compliance |
| Maltodextrin DE25 | BC-10141 | 2022-08-26 | Operations |
| customs duty de 0% | BC-10161 | 2024-09-07 | Finance |
| Citric Acid 99.5% | TC-10164 | 2024-11-06 | Finance |
| Prism Logistik | IC-10176 | 2023-07-22 | Operations |
| Rapsöl Pharmazeutisch rein | TC-10185 | 2023-09-24 | Supply Chain |
| Soy Isolate 50% Grade B | IC-10197 | 2023-08-01 | Product Management |
| stratos trading | TC-10204 | 2022-02-26 | Operations |
| SU-OI-GR-A-224 | BC-10213 | 2021-02-27 | Product Management |
| LA-AC-393 | TC-10223 | 2024-05-20 | IT Infrastructure |
| SIG-55-ICI-Z2GP GmbH | IC-10228 | 2023-02-18 | Finance |
| Pea Protein Premium | TC-10253 | 2021-12-02 | Supply Chain |
| pinnacle commodities BV | IC-10260 | 2021-12-27 | Operations |
| Potassium Sorbate 50% Food Grade | BC-10263 | 2021-12-09 | Product Management |
| CO-OI-GR-A-370 | TC-10265 | 2021-06-23 | Supply Chain |
| Natriumbenzoat Lebensmittelrein | IC-10272 | 2022-01-17 | Operations |
| ascorbic acid standard | IC-10275 | 2023-07-13 | Compliance |
| SIG-68-QRN-LSY2 | TC-10316 | 2021-10-23 | Data Governance |
| Natriumchlorid 99.5% | IC-10323 | 2022-10-28 | Operations |
| SIG-74-ZJN-KVHO | BC-10325 | 2021-01-08 | Data Governance |
| Ascorbic Acid 99.5% Technische Qualität | TC-10331 | 2024-07-10 | IT Infrastructure |
| Dextrin Pharma Grade | IC-10333 | 2022-08-24 | Finance |
| SIG-92-AXW-GPAG | TC-10335 | 2024-10-02 | Product Management |
| premier partners Group | BC-10340 | 2023-02-13 | Product Management |
| Vertex Rohstoffe | TC-10372 | 2021-11-01 | Product Management |
| Core Versorgung GmbH | BC-10388 | 2021-11-01 | Operations |
| Sonnenblumenöl 98% | BC-10395 | 2023-03-22 | Data Governance |
| Zitronensäure Standardqualität | BC-10412 | 2024-03-18 | Operations |
| Stellar Rohstoffe | IC-10430 | 2022-07-23 | IT Infrastructure |
| sodium benzoate | TC-10438 | 2024-01-04 | Finance |
| meridian sourcing | IC-10447 | 2023-07-15 | IT Infrastructure |
| LA-AC-TE-651 | TC-10460 | 2024-07-21 | Operations |
| lactic acid standard | TC-10467 | 2022-06-02 | Compliance |
| lactic acid 98% premium | IC-10480 | 2024-08-16 | IT Infrastructure |
| Vertex Distribution | BC-10504 | 2024-08-17 | Data Governance |
| Ascorbic Acid 50% | IC-10508 | 2024-02-09 | Finance |
| Sorbic Acid 25% Grade B | BC-10514 | 2024-10-13 | Supply Chain |
| Palm Oil | TC-10542 | 2024-11-03 | Compliance |
| sodium benzoate 99.5% standard | BC-10548 | 2024-03-17 | Product Management |
| Quantum Trading | IC-10567 | 2024-05-23 | Supply Chain |
| CA-98-TE-238 | IC-10572 | 2024-08-01 | IT Infrastructure |
| Continental Logistik | TC-10594 | 2024-06-02 | Supply Chain |
| VA-ST-D-7-855 | BC-10613 | 2024-11-11 | Data Governance |
| DE-635 | TC-10619 | 2023-08-16 | Data Governance |
| SIG-63-YJW-AP00 | BC-10624 | 2021-08-21 | Compliance |
| SIG-36-ZKX-4SE4 | IC-10645 | 2022-08-08 | Supply Chain |
| SIG-52-LXJ-ZU4J | TC-10653 | 2022-06-07 | Compliance |
| Vat Reduced DE 20% | IC-10666 | 2023-04-26 | Finance |
| Catalyst Logistics | BC-10668 | 2021-09-15 | Product Management |
| quantum logistics | TC-10678 | 2024-02-20 | Compliance |
| Horizon Materials SAS | TC-10681 | 2022-09-12 | Operations |
| Rapsöl 25% Lebensmittelrein | TC-10684 | 2023-12-11 | IT Infrastructure |
| Isoglucose 98% | BC-10689 | 2021-06-17 | Finance |
| SIG-80-WKN-N0SS | IC-10708 | 2021-05-24 | Operations |
| Isoglucose | TC-10711 | 2022-11-07 | IT Infrastructure |
| isoglucose 70% | BC-10719 | 2022-09-12 | IT Infrastructure |
| ascorbic acid pharma grade | BC-10727 | 2024-11-10 | Finance |
| SIG-51-MQP-ZO0K | TC-10743 | 2023-06-06 | Finance |
| Dextrose 25% | TC-10746 | 2023-03-25 | Compliance |
| FR-108 | TC-10774 | 2022-05-22 | Supply Chain |
| Maltodextrin DE20 | TC-10775 | 2024-05-07 | Product Management |
| Cyclodextrin 98% Pharmazeutisch rein | BC-10782 | 2023-09-02 | Product Management |
| DE-25-PR-846 | IC-10797 | 2022-12-20 | Product Management |
| Isoglucose 70% | TC-10803 | 2021-05-13 | Operations |
| sorbic acid 50% | IC-10804 | 2024-05-13 | Compliance |
| continental ingredients AG | TC-10822 | 2024-01-12 | Data Governance |
| Global Materials | BC-10840 | 2024-02-10 | IT Infrastructure |
| ST-LO-927 | IC-10849 | 2021-08-25 | Compliance |
| SIG-67-YAJ-18K0 | BC-10853 | 2021-10-23 | Data Governance |
| Prism Ingredients | BC-10893 | 2023-05-13 | Supply Chain |
| VA-RE-C-19-810 | BC-10895 | 2024-10-20 | Finance |
| Continental Werkstoffe NV | TC-10903 | 2021-09-19 | IT Infrastructure |
| CO-MA-245 | TC-10905 | 2021-09-26 | Compliance |
| Cyclodextrin | TC-10916 | 2022-09-02 | Data Governance |
| Nexus Ingredients SARL | TC-10925 | 2022-06-19 | Product Management |
| Isoglucose 70% | BC-10928 | 2022-11-24 | Product Management |
| SIG-89-RGS-FIRM Holdings | BC-10937 | 2022-09-27 | Compliance |
| Sodium Benzoate 25% Grade B | IC-10969 | 2024-05-26 | Data Governance |
| Soy Isolate 99.5% | TC-11000 | 2024-05-13 | IT Infrastructure |
| AS-AC-FO-GR-835 | IC-11004 | 2024-09-18 | Supply Chain |
| withholding fr 10% | TC-11006 | 2024-10-12 | Supply Chain |
| SIG-84-EIB-2MOT | IC-11031 | 2023-11-20 | Operations |
| Central Manufacturing Holdings | IC-11035 | 2023-11-09 | Supply Chain |
| global distribution Corp. | IC-11063 | 2021-05-26 | Operations |
| CO-OI-98-876 | BC-11070 | 2024-02-26 | Data Governance |
| SIG-83-MZM-HGMN GmbH | BC-11088 | 2024-06-10 | Compliance |
| SO-AC-98-579 | BC-11098 | 2022-08-02 | Supply Chain |
| Soy Isolate 99.5% | BC-11101 | 2021-06-07 | Compliance |
| SIG-25-VPE-TOC1 | IC-11103 | 2021-08-03 | IT Infrastructure |
| SIG-41-WHZ-QDKE | TC-11122 | 2024-05-14 | Product Management |
| SIG-15-PFO-2W85 | TC-11126 | 2024-03-22 | Compliance |
| Apex Chemicals | IC-11140 | 2021-02-05 | Compliance |
| Weizenklebereiweiß Qualitätsstufe I | BC-11175 | 2022-01-11 | IT Infrastructure |
| vat reduced nl 0% | BC-11186 | 2021-10-14 | Supply Chain |
| Natriumchlorid 98% | TC-11209 | 2022-05-22 | Finance |
| central supply | IC-11210 | 2023-10-23 | Finance |
| SIG-79-GKV-W8GA | IC-11213 | 2024-12-05 | Supply Chain |
| CE-PR-134 | TC-11224 | 2022-10-20 | Supply Chain |
| fructose tech grade | TC-11238 | 2022-07-28 | IT Infrastructure |
| SIG-69-INT-Z1YQ | TC-11250 | 2021-06-25 | Operations |
| AT-LO-132 | TC-11270 | 2022-10-06 | Finance |
| Wheat Gluten | BC-11307 | 2021-02-25 | IT Infrastructure |
| SIG-53-HTQ-XVWB Group | TC-11311 | 2021-07-26 | Finance |
| SIG-87-YFT-P51V | BC-11325 | 2024-03-20 | Product Management |
| FR-99.5-PH-GR-378 | TC-11333 | 2022-04-28 | Operations |
| pinnacle industries Corp. | IC-11352 | 2023-01-11 | Data Governance |
| fructose 25% | TC-11356 | 2023-12-01 | Compliance |
| Withholding BR 15% | BC-11361 | 2024-07-14 | Operations |
| SU-OI-TE-879 | BC-11397 | 2022-05-18 | Data Governance |
| Sodium Chloride 70% Grade B | TC-11405 | 2023-05-02 | IT Infrastructure |
| Zitronensäure 70% Lebensmittelrein | TC-11419 | 2021-01-07 | Finance |
| Global Materials | IC-11424 | 2022-02-13 | Finance |
| Resistente Stärke | TC-11430 | 2022-12-12 | Compliance |
| PO-SO-339 | BC-11432 | 2022-03-02 | Supply Chain |
| AS-AC-TE-342 | TC-11435 | 2023-02-27 | Finance |
| SIG-87-YFT-P51V | IC-11466 | 2024-06-01 | Data Governance |
| VA-ST-G-20-932 | TC-11470 | 2021-03-28 | Supply Chain |
| Pea Protein 99.5% | TC-11490 | 2023-12-28 | Product Management |
| SIG-68-ELC-6AVE | TC-11514 | 2024-08-22 | Finance |
| PI-SU-CO-216 | BC-11535 | 2022-05-28 | Product Management |
| SIG-29-BKQ-HXCX Group | TC-11536 | 2021-11-14 | Compliance |
| Meridian Sourcing | IC-11549 | 2021-05-13 | Finance |
| Customs Duty DE 5% | BC-11553 | 2024-04-14 | Data Governance |
| SIG-62-JTP-RUMX | IC-11586 | 2024-01-10 | Compliance |
| Prism Manufacturing LLC | BC-11618 | 2024-03-01 | Finance |
| ascorbic acid food grade | BC-11621 | 2021-09-08 | Compliance |
| SO-AC-98-741 | IC-11623 | 2022-03-13 | IT Infrastructure |
| SIG-10-PGH-BTUF | TC-11634 | 2021-01-07 | IT Infrastructure |
| SIG-20-LIK-8TZV Ltd. | IC-11655 | 2021-02-07 | Operations |
| SIG-64-ILX-G2AZ PLC | TC-11665 | 2023-06-14 | Data Governance |
| Ascorbic Acid Pharmazeutisch rein | IC-11678 | 2022-12-12 | Product Management |
| Kaliumsorbat | TC-11689 | 2021-03-19 | Data Governance |
| WH-GL-99.5-TE-628 | TC-11694 | 2021-08-26 | Operations |
| QU-SU-CO-774 | BC-11699 | 2021-08-22 | IT Infrastructure |
| DE-TE-414 | TC-11752 | 2024-08-26 | Data Governance |
| SIG-25-ROA-G6G0 | BC-11755 | 2024-03-14 | Data Governance |
| SIG-86-LPN-HCNV | TC-11776 | 2021-11-23 | Operations |
| Atlas Ingredients Ltd. | BC-11804 | 2021-08-04 | Product Management |
| Horizon Partners Ltd. | TC-11820 | 2021-02-25 | Supply Chain |
| SIG-83-GEN-QNXZ | IC-11834 | 2021-06-13 | Supply Chain |
| Soja Isolate Standardqualität | IC-11842 | 2024-09-18 | Operations |
| pacific sourcing | IC-11846 | 2021-03-01 | Finance |
| Calcium Carbonate 50% Grade A | BC-11864 | 2022-05-02 | Compliance |
| Natriumbenzoat 25% Qualitätsstufe II | IC-11868 | 2021-12-23 | Compliance |
| VA-ST-N-20-275 | TC-11883 | 2023-03-14 | IT Infrastructure |
| Citric Acid 99.5% Pharma Grade | IC-11884 | 2021-11-25 | Product Management |
| Natriumchlorid | TC-11893 | 2021-07-27 | Finance |
| Sonnenblumenöl 98% | TC-11897 | 2024-06-15 | Compliance |
| SIG-95-EES-2FE9 | TC-11924 | 2023-07-05 | Finance |
| Sodium Benzoate | BC-11928 | 2022-04-06 | IT Infrastructure |
| quantum enterprise BV | IC-11947 | 2022-06-07 | Compliance |
| Zitronensäure Qualitätsstufe I | IC-11950 | 2022-08-26 | IT Infrastructure |
| Catalyst Materials | BC-11962 | 2023-06-26 | Product Management |
| vat standard de 7% | TC-12000 | 2021-07-10 | Supply Chain |
| Zenith Supply Co. | TC-12001 | 2021-04-07 | Supply Chain |
| Vanguard Supply Co. | TC-12011 | 2023-12-16 | Compliance |
| dextrose 25% | IC-12027 | 2022-01-16 | Product Management |
| sodium benzoate 98% pharma grade | TC-12039 | 2022-09-14 | Compliance |
| Lactic Acid Technical | IC-12050 | 2021-11-15 | Product Management |
| Maltodextrin-Pulver DE30 | BC-12053 | 2023-04-23 | Finance |
| CO-OI-70-701 | BC-12071 | 2021-07-04 | Product Management |
| SIG-92-RZH-LRHH | BC-12073 | 2022-02-10 | Product Management |
| Vanguard Supply Co. | IC-12082 | 2022-01-05 | Finance |
| SIG-83-OBQ-GEIL GmbH | BC-12087 | 2021-05-10 | Product Management |
| Glucose Syrup 99.5% Grade B | IC-12096 | 2024-11-05 | Finance |
| IS-FO-GR-335 | IC-12113 | 2021-03-03 | Operations |
| Rapsöl 70% Qualitätsstufe II | TC-12147 | 2023-01-15 | Compliance |
| SIG-86-VCP-SVOL | IC-12157 | 2021-03-23 | Data Governance |
| CY-515 | IC-12165 | 2022-10-04 | Compliance |
| SIG-72-JEH-P5K7 | TC-12174 | 2023-03-09 | Supply Chain |
| Prime Partners | BC-12177 | 2024-02-10 | Product Management |
| Sonnenblumenöl 98% | IC-12194 | 2021-01-24 | Product Management |
| Lactic Acid | IC-12196 | 2021-05-02 | Supply Chain |
| SIG-69-UAZ-1ODW | TC-12207 | 2024-06-03 | Supply Chain |
| SIG-14-WZC-EEWK | TC-12213 | 2022-04-28 | Operations |
| lactic acid 98% | BC-12218 | 2023-10-02 | IT Infrastructure |
| prism materials | IC-12221 | 2021-01-22 | Finance |
| Pinnacle Chemicals SA | TC-12241 | 2022-01-07 | Data Governance |
| SIG-69-TRZ-SFLQ | IC-12254 | 2024-02-25 | Compliance |
| Resistente Stärke 25% Technische Qualität | TC-12257 | 2024-08-15 | Finance |
| Natriumchlorid 99.5% Qualitätsstufe I | BC-12259 | 2022-12-17 | IT Infrastructure |
| Elite Supply Co. | IC-12263 | 2024-04-17 | Compliance |
| coconut oil 25% food grade | IC-12272 | 2022-08-28 | IT Infrastructure |
| FR-98-PR-250 | TC-12299 | 2023-09-12 | Supply Chain |
| citric acid 98% | IC-12301 | 2024-04-26 | IT Infrastructure |
| Vat Reduced NL 25% | TC-12303 | 2023-01-01 | Operations |
| CA-PR-568 | BC-12305 | 2022-11-12 | Product Management |
| Elite Processing SA | BC-12308 | 2022-03-12 | Product Management |
| SIG-18-LLP-8GUU | IC-12336 | 2022-07-05 | Compliance |
| nexus partners Group | BC-12376 | 2022-11-14 | Data Governance |
| Ascorbic Acid | TC-12378 | 2021-12-04 | Compliance |
| SIG-72-HBS-JIQY | TC-12384 | 2024-04-24 | Compliance |
| SIG-86-XNZ-5Q7H | TC-12400 | 2021-10-14 | Data Governance |
| SIG-44-FWT-OA3N | TC-12417 | 2024-12-22 | Product Management |
| Isoglucose 50% Technical | TC-12425 | 2021-02-17 | IT Infrastructure |
| Vat Reduced NL 25% | IC-12462 | 2023-07-16 | Supply Chain |
| Nexus Distribution PLC | TC-12480 | 2023-08-13 | Supply Chain |
| SIG-39-MAR-LMVK | TC-12510 | 2021-12-20 | IT Infrastructure |
| SIG-52-FHA-5PI2 | IC-12522 | 2023-12-19 | Product Management |
| soy isolate 98% | IC-12536 | 2022-11-11 | Compliance |
| Calcium Carbonate 50% Grade B | BC-12585 | 2024-01-01 | IT Infrastructure |
| SIG-20-RSZ-19RE | TC-12586 | 2023-08-18 | Compliance |
| FR-124 | TC-12620 | 2021-07-03 | IT Infrastructure |
| Natriumbenzoat 50% | BC-12625 | 2021-03-11 | IT Infrastructure |
| nexus processing AG | BC-12633 | 2024-01-08 | Supply Chain |
| Horizon Materials PLC | IC-12635 | 2022-11-22 | Finance |
| citric acid 99.5% pharma grade | IC-12641 | 2022-03-05 | Data Governance |
| Potassium Sorbate 98% | IC-12643 | 2021-09-21 | Operations |
| SIG-89-HLJ-NILC | BC-12646 | 2024-11-05 | Compliance |
| Baltic Distribution Group | IC-12651 | 2024-02-08 | Compliance |
| stellar supply | IC-12657 | 2021-12-26 | Compliance |
| Withholding NL 7% | TC-12674 | 2021-06-12 | Supply Chain |
| Maltodextrin-Pulver DE25 | BC-12682 | 2022-05-20 | Operations |
| SIG-15-FOA-70S8 | IC-12698 | 2024-09-06 | Product Management |
| SIG-82-DEO-X80R | TC-12716 | 2021-10-08 | IT Infrastructure |
| DE-98-FO-GR-211 | IC-12731 | 2022-11-27 | Data Governance |
| Global Processing Holdings | TC-12738 | 2024-06-14 | Operations |
| maltodextrin de25 | BC-12740 | 2021-05-26 | Data Governance |
| Natriumbenzoat 25% | BC-12743 | 2023-07-06 | Product Management |
| Fructose Standardqualität | TC-12746 | 2023-04-18 | Compliance |
| Natriumchlorid Technische Qualität | TC-12753 | 2022-01-19 | Finance |
| Vat Standard DE 10% | IC-12754 | 2022-03-26 | Finance |
| CI-AC-ST-836 | BC-12756 | 2023-03-03 | Data Governance |
| lactic acid tech grade | IC-12761 | 2022-10-20 | IT Infrastructure |
| Vat Standardqualität FR 10% | TC-12765 | 2024-12-08 | IT Infrastructure |
| ascorbic acid food grade | BC-12820 | 2024-07-06 | Supply Chain |
| DE-50-727 | TC-12821 | 2023-03-24 | Data Governance |
| Soja Isolate 25% | TC-12837 | 2022-03-08 | Data Governance |
| VE-IN-644 Ltd. | TC-12863 | 2023-12-06 | Data Governance |
| ascorbic acid 50% tech grade | BC-12869 | 2021-12-08 | Compliance |
| Vat Standardqualität DE 19% | TC-12875 | 2021-03-24 | Compliance |
| Prime Rohstoffe LLC | TC-12887 | 2021-06-25 | Finance |
| Ascorbic Acid 98% Pharma Grade | BC-12899 | 2024-08-12 | Product Management |
| IS-230 | IC-12904 | 2023-09-18 | Product Management |
| Rapsöl 99.5% | IC-12916 | 2024-04-07 | Compliance |
| Baltic Enterprise Holdings | TC-12927 | 2023-05-26 | IT Infrastructure |
| Excise DE 10% | TC-12934 | 2023-02-26 | IT Infrastructure |
| Vat Standardqualität GB 21% | BC-12963 | 2023-01-03 | Data Governance |
| Lactic Acid 99.5% Qualitätsstufe II | TC-13025 | 2024-11-08 | Supply Chain |
| Quantum Verarbeitung PLC | TC-13031 | 2022-11-17 | IT Infrastructure |
| Apex Trading Holdings | BC-13036 | 2021-06-08 | Finance |
| Central Logistics | BC-13041 | 2024-02-28 | Product Management |
| Rapeseed Oil | TC-13048 | 2021-02-18 | Data Governance |
| fructose 25% | TC-13076 | 2022-10-09 | Product Management |
| FR-GR-B-311 | IC-13080 | 2023-11-11 | Product Management |
| DE-GR-A-250 | BC-13088 | 2021-09-27 | Product Management |
| SIG-53-NHM-OFA2 | IC-13112 | 2022-02-18 | IT Infrastructure |
| vanguard industries AG | BC-13122 | 2022-10-01 | Compliance |
| premier supply PLC | BC-13139 | 2021-05-01 | IT Infrastructure |
| Dextrin | IC-13143 | 2021-11-18 | Data Governance |
| SIG-40-MRL-94W6 | BC-13148 | 2023-05-27 | Data Governance |
| Nexus Werkstoffe | BC-13171 | 2024-10-18 | Product Management |
| Baltic Chemicals AG | TC-13179 | 2021-07-25 | Compliance |
| Atlantic Versorgung GmbH | IC-13189 | 2024-06-06 | Compliance |
| Traubenzucker 99.5% Standardqualität | BC-13195 | 2022-07-04 | Product Management |
| isoglucose 70% | IC-13198 | 2022-11-15 | IT Infrastructure |
| LA-AC-165 | TC-13204 | 2023-05-25 | Operations |
| Sodium Benzoate 50% Technical | BC-13205 | 2024-08-04 | Product Management |
| Catalyst Commodities | IC-13211 | 2023-04-18 | Operations |
| sorbic acid food grade | BC-13220 | 2021-06-17 | Product Management |
| maltodextrin de10 | IC-13235 | 2022-10-18 | IT Infrastructure |
| Atlas Logistik | BC-13241 | 2022-07-15 | IT Infrastructure |
| Meridian Chemicals International | BC-13246 | 2024-03-28 | Data Governance |
| Nexus Materials | BC-13281 | 2024-10-12 | Finance |
| RE-ST-PR-679 | BC-13292 | 2023-05-21 | Product Management |
| prism partners Holdings | BC-13296 | 2021-03-20 | Product Management |
| SIG-76-RKG-E8RT | TC-13298 | 2022-03-09 | Supply Chain |
| DE-GR-B-244 | TC-13316 | 2024-07-05 | Product Management |
| Sorbinsäure 70% | IC-13323 | 2021-07-02 | Operations |
| potassium sorbate | IC-13343 | 2023-12-14 | Product Management |
| SIG-50-BJQ-W54O Holdings | BC-13347 | 2021-04-06 | Product Management |
| atlas supply | BC-13350 | 2024-06-18 | Data Governance |
| SIG-41-ZTZ-VNMI Holdings | IC-13351 | 2022-10-02 | Operations |
| Quantum Sourcing | IC-13355 | 2022-12-03 | Finance |
| SIG-99-JMF-1NOQ | IC-13360 | 2024-12-07 | IT Infrastructure |
| SO-AC-PH-GR-620 | BC-13362 | 2022-01-19 | Compliance |
| SIG-93-VLZ-VI4P | TC-13371 | 2023-10-10 | Supply Chain |
| Vertex Sourcing | BC-13403 | 2022-09-11 | Data Governance |
| CU-DU-D-0-955 | BC-13427 | 2024-08-19 | Finance |
| SIG-71-KJM-D5G1 Holdings | BC-13437 | 2021-11-01 | IT Infrastructure |
| SIG-38-VFI-SR88 Corp. | IC-13444 | 2021-03-09 | IT Infrastructure |
| sodium benzoate | BC-13447 | 2024-02-03 | Finance |
| Soja Isolate 25% | TC-13463 | 2022-05-10 | Supply Chain |
| NE-LO-125 | IC-13474 | 2022-12-03 | Data Governance |
| Zenith Handel AG | BC-13477 | 2024-05-14 | IT Infrastructure |
| AS-AC-70-347 | TC-13485 | 2023-02-07 | Product Management |
| Central Sourcing | BC-13486 | 2024-10-08 | Product Management |
| Zenith Verarbeitung | IC-13488 | 2023-08-04 | Operations |
| sodium benzoate | IC-13506 | 2024-08-04 | Product Management |
| resistant starch | BC-13514 | 2023-05-14 | IT Infrastructure |
| SIG-36-JLA-CSEN | BC-13531 | 2024-03-08 | Operations |
| Elite Chemicals AG | IC-13537 | 2024-04-03 | Finance |
| vanguard industries Inc. | BC-13550 | 2024-09-08 | Data Governance |
| CA-98-PR-260 | TC-13571 | 2024-10-24 | Finance |
| SIG-32-TTU-44MW | TC-13582 | 2021-01-21 | Finance |
| SIG-53-XQL-BVVB | BC-13594 | 2022-03-06 | Finance |
| SIG-56-END-D8WH | TC-13602 | 2024-10-11 | Product Management |
| Natriumbenzoat | BC-13613 | 2024-03-10 | Supply Chain |
| Customs Duty NL 15% | TC-13618 | 2023-04-03 | Compliance |
| SO-IS-99.5-141 | TC-13620 | 2024-12-16 | Operations |
| NO-DI-180 Ltd. | BC-13625 | 2023-04-23 | Product Management |
| Fructose Standardqualität | IC-13652 | 2022-03-07 | IT Infrastructure |
| SIG-52-LQX-X1DO | IC-13654 | 2022-04-19 | Product Management |
| Vanguard Partners PLC | IC-13663 | 2022-02-23 | Data Governance |
| Isoglucose | BC-13671 | 2021-06-18 | Supply Chain |
| Zitronensäure Standardqualität | BC-13673 | 2024-03-05 | Operations |
| resistant starch | BC-13684 | 2023-06-21 | Compliance |
| Global Trading Ltd. | TC-13695 | 2021-12-02 | Supply Chain |
| SIG-70-IET-75TA | BC-13714 | 2023-06-02 | Supply Chain |
| SIG-32-RJE-L1OT | TC-13750 | 2021-07-10 | Supply Chain |
| SIG-98-PIN-G89V | BC-13769 | 2022-12-19 | Finance |
| SIG-13-ZRN-WZGO | TC-13775 | 2021-06-25 | Data Governance |
| Premier Versorgung GmbH | BC-13793 | 2021-09-25 | Product Management |
| stratos logistics | BC-13798 | 2022-03-01 | IT Infrastructure |
| sodium benzoate | IC-13800 | 2023-05-12 | Operations |
| CE-MA-997 KG | TC-13806 | 2021-12-22 | Finance |
| atlas supply | IC-13810 | 2022-01-25 | IT Infrastructure |
| SIG-41-YLB-IZED | TC-13813 | 2023-11-08 | Finance |
| Sodium Benzoate 99.5% Technical | BC-13816 | 2021-12-01 | Compliance |
| Lactic Acid Standardqualität | IC-13828 | 2023-07-12 | Data Governance |
| EX-B-21-936 | BC-13830 | 2024-05-13 | Supply Chain |
| Rapeseed Oil Grade A | IC-13845 | 2021-04-15 | Operations |
| SIG-84-MUG-BUXR | TC-13882 | 2022-02-24 | IT Infrastructure |
| quantum processing International | TC-13902 | 2023-05-24 | Operations |
| Zitronensäure Technische Qualität | IC-13910 | 2021-07-15 | Compliance |
| Stratos Sourcing | BC-13924 | 2021-11-15 | Product Management |
| SIG-18-IQS-O98Z SA | TC-13927 | 2021-02-24 | Product Management |
| LA-AC-891 | IC-13932 | 2023-03-12 | Product Management |
| SIG-42-BEO-614U | BC-13939 | 2023-10-23 | Supply Chain |
| SIG-81-LVQ-2J60 | TC-13942 | 2024-05-02 | Compliance |
| Weizenklebereiweiß 70% | IC-13945 | 2022-07-19 | Data Governance |
| Resistant Starch 70% Food Grade | BC-13955 | 2024-08-26 | Operations |
| Nordic Logistik PLC | BC-13966 | 2022-05-02 | Data Governance |
| SIG-16-YRD-5C3Z | BC-13973 | 2024-12-19 | Operations |
| Fructose | BC-13980 | 2021-02-25 | Operations |
| Calcium Carbonate | IC-13994 | 2021-04-10 | Operations |
| SIG-42-IEF-RFC9 | TC-14004 | 2021-08-14 | Compliance |
| Sodium Benzoate Grade A | IC-14025 | 2022-04-18 | Data Governance |
| LA-AC-GR-A-949 | BC-14034 | 2024-07-15 | Data Governance |
| stratos partners SA | BC-14051 | 2023-07-22 | Finance |
| isoglucose | TC-14056 | 2023-12-07 | Operations |
| Lactic Acid | BC-14066 | 2021-05-03 | IT Infrastructure |
| Continental Logistics | TC-14068 | 2023-08-21 | Data Governance |
| Nordic Versorgung GmbH | BC-14069 | 2022-08-08 | Product Management |
| Vat Standardqualität IN 20% | BC-14074 | 2023-06-12 | IT Infrastructure |
| SIG-32-RJE-L1OT | IC-14093 | 2024-01-11 | IT Infrastructure |
| SIG-83-OTU-QZB6 | IC-14095 | 2024-03-18 | Product Management |
| casein | IC-14100 | 2022-10-05 | Data Governance |
| Maltodextrin DE5 Grade A | IC-14105 | 2022-06-19 | IT Infrastructure |
| SIG-16-ZDY-GYTX Holdings | BC-14124 | 2022-09-08 | Operations |
| Catalyst Commodities SAS | BC-14137 | 2023-08-27 | Data Governance |
| Natriumbenzoat 70% Premiumqualität | IC-14146 | 2021-10-03 | Finance |
| CO-OI-977 | IC-14149 | 2023-01-11 | Product Management |
| PR-LO-862 | IC-14150 | 2022-12-19 | Data Governance |
| Dextrin Technische Qualität | BC-14161 | 2021-09-09 | Compliance |
| wheat gluten pharma grade | BC-14184 | 2022-02-28 | Compliance |
| GL-SO-534 Holdings | IC-14193 | 2021-04-11 | Compliance |
| SO-AC-340 | BC-14197 | 2023-06-27 | Finance |
| Central Logistics | IC-14221 | 2024-02-27 | Product Management |
| CO-SU-411 | BC-14224 | 2023-12-18 | Finance |
| Soy Isolate Food Grade | IC-14227 | 2021-10-21 | Operations |
| Wheat Gluten 50% Pharma Grade | TC-14237 | 2024-02-07 | Compliance |
| Quantum Chemicals | IC-14239 | 2021-12-09 | Compliance |
| Sodium Benzoate 25% | BC-14242 | 2024-07-17 | Supply Chain |
| WI-I-10-242 | IC-14252 | 2021-05-08 | Finance |
| vertex enterprise Holdings | BC-14266 | 2021-10-15 | Finance |
| Continental Sourcing | IC-14310 | 2024-04-15 | Finance |
| glucose syrup | BC-14312 | 2021-11-17 | Finance |
| catalyst materials | BC-14330 | 2021-11-02 | Finance |
| atlas sourcing | BC-14345 | 2021-05-26 | Compliance |
| CA-CA-25-PH-GR-684 | IC-14393 | 2022-05-05 | Supply Chain |
| SO-IS-99.5-GR-A-499 | BC-14396 | 2022-11-22 | Data Governance |
| SIG-19-TLQ-1P5Z | TC-14402 | 2021-12-02 | Data Governance |
| SIG-45-NEB-M5RE | BC-14414 | 2023-06-08 | IT Infrastructure |
| SIG-48-BCI-7SYR | BC-14417 | 2024-12-10 | Data Governance |
| potassium sorbate 50% tech grade | IC-14429 | 2021-01-21 | Data Governance |
| RE-ST-223 | TC-14432 | 2021-11-17 | Finance |
| SIG-93-CZZ-ZGWF | BC-14444 | 2021-09-18 | Data Governance |
| SU-OI-ST-338 | BC-14454 | 2021-11-17 | Product Management |
| Traubenzucker Technische Qualität | TC-14486 | 2021-11-27 | Product Management |
| central logistics Group | IC-14500 | 2022-06-24 | Operations |
| Fructose | BC-14503 | 2022-09-12 | Operations |
| withholding nl 20% | BC-14510 | 2022-08-09 | IT Infrastructure |
| AP-LO-246 | IC-14517 | 2022-05-04 | IT Infrastructure |
| ascorbic acid 50% tech grade | TC-14527 | 2024-01-23 | Product Management |
| stratos materials Group | TC-14543 | 2024-03-23 | Product Management |
| SIG-75-XMY-5X1F | IC-14544 | 2024-12-03 | Operations |
| lactic acid food grade | IC-14584 | 2021-08-15 | IT Infrastructure |
| ME-SU-CO-314 | BC-14595 | 2021-04-21 | Data Governance |
| Stratos Sourcing | IC-14596 | 2024-02-12 | IT Infrastructure |
| customs duty br 20% | BC-14619 | 2022-07-01 | Supply Chain |
| Soy Isolate 25% | IC-14621 | 2023-03-26 | IT Infrastructure |
| MA-DE-PR-303 | BC-14638 | 2024-05-08 | Supply Chain |
| Soy Isolate Premium | IC-14646 | 2024-04-25 | Data Governance |
| sodium benzoate 99.5% | BC-14651 | 2024-06-15 | Data Governance |
| Casein Grade A | BC-14652 | 2022-03-19 | Operations |
| HO-IN-142 AG | TC-14653 | 2024-01-28 | Compliance |
| Pea Protein Grade A | TC-14662 | 2023-10-14 | Finance |
| Atlantic Manufacturing | BC-14663 | 2021-04-13 | Supply Chain |
| ascorbic acid standard | TC-14678 | 2022-11-20 | Compliance |
| Soja Isolate 99.5% | IC-14689 | 2023-09-06 | Finance |
| SIG-15-NIP-N1UH | IC-14693 | 2022-09-28 | Product Management |
| Zenith Manufacturing PLC | TC-14713 | 2024-06-09 | Product Management |
| Nordic Ingredients | IC-14715 | 2022-06-10 | Compliance |
| Pinnacle Solutions | IC-14724 | 2021-12-02 | Supply Chain |
| SIG-58-LWY-Q8P6 | TC-14762 | 2021-09-14 | Finance |
| ME-LO-731 | IC-14770 | 2021-07-28 | Operations |
| SIG-24-CXH-R2TY | BC-14817 | 2023-10-06 | Finance |
| VA-RE-I-20-892 | IC-14839 | 2024-10-05 | Data Governance |
| SIG-86-XNZ-5Q7H | TC-12400 | 2021-10-14 | Data Governance |
| MA-DE-ST-267 | TC-14870 | 2021-08-25 | Product Management |
| Continental Sourcing | IC-14873 | 2022-04-04 | Data Governance |
| SIG-58-FIB-X69X | IC-14877 | 2021-02-20 | Finance |
| RE-ST-GR-B-805 | BC-14883 | 2024-06-08 | Supply Chain |
| SIG-82-AKA-U48G | BC-14894 | 2021-08-13 | IT Infrastructure |
| SIG-56-BPD-M0A6 | TC-14909 | 2021-05-06 | Finance |
| HO-DI-531 Group | IC-14914 | 2023-07-03 | Product Management |
| prism industries Corp. | BC-14925 | 2021-05-24 | Product Management |
| Sodium Chloride | TC-14943 | 2022-01-07 | Data Governance |
| QU-DI-467 Holdings | BC-14963 | 2023-08-09 | IT Infrastructure |
| wheat gluten | BC-14983 | 2023-01-09 | IT Infrastructure |
| Rapsöl 25% Lebensmittelrein | BC-15011 | 2023-02-26 | Operations |
| SO-CH-99.5-GR-A-634 | IC-15026 | 2023-09-26 | Compliance |
| VA-RE-C-21-521 | IC-15043 | 2022-05-02 | Product Management |
| SIG-40-KVV-E07S | TC-15058 | 2022-01-15 | IT Infrastructure |
| WI-N-21-724 | TC-15059 | 2022-06-08 | Finance |
| Stratos Supply | IC-15070 | 2022-12-01 | Compliance |
| Sodium Chloride 25% Premium | IC-15072 | 2022-09-04 | Compliance |
| SIG-52-LXJ-ZU4J | IC-15074 | 2021-02-14 | Supply Chain |
| Nordic Logistics | TC-15091 | 2022-11-15 | Compliance |
| SIG-41-HMT-W0GK | TC-15094 | 2023-06-01 | Finance |
| apex logistics | BC-15099 | 2024-10-11 | Supply Chain |
| Palmfett 99.5% Qualitätsstufe I | TC-15104 | 2024-01-28 | Operations |
| continental ingredients AG | IC-15120 | 2024-11-02 | Supply Chain |
| Core Sourcing | TC-15122 | 2021-07-13 | Finance |
| Coconut Oil 70% Qualitätsstufe I | TC-15128 | 2023-09-12 | IT Infrastructure |
| DE-98-512 | BC-15164 | 2022-04-23 | Compliance |
| customs duty cn 7% | IC-15204 | 2022-11-17 | Finance |
| SIG-89-PTG-ZQNK | IC-15217 | 2023-12-10 | Operations |
| meridian industries | IC-15226 | 2023-04-15 | IT Infrastructure |
| sorbic acid food grade | BC-15230 | 2024-01-26 | Finance |
| nordic processing SAS | BC-15232 | 2021-08-23 | Product Management |
| vat reduced us 10% | BC-15234 | 2021-07-12 | Product Management |
| WI-G-5-718 | BC-15237 | 2023-05-27 | Data Governance |
| Weizenklebereiweiß Qualitätsstufe I | IC-15238 | 2024-01-25 | Data Governance |
| Kaliumsorbat Technische Qualität | IC-15240 | 2023-07-01 | Finance |
| Pinnacle Trading | IC-15250 | 2022-08-28 | Product Management |
| Lactic Acid Food Grade | IC-15252 | 2024-06-03 | Product Management |
| SO-BE-700 | IC-15262 | 2022-01-12 | Data Governance |
| SIG-72-YEU-SCIQ | IC-15311 | 2023-02-10 | Data Governance |
| SIG-68-SJS-K3N3 | IC-15320 | 2022-03-08 | Finance |
| Sodium Chloride Standard | IC-15343 | 2024-09-06 | Finance |
| Pacific Logistics | BC-15347 | 2021-01-03 | Operations |
| SU-OI-50-GR-A-521 | BC-15358 | 2021-03-10 | Operations |
| CO-OI-70-GR-A-633 | BC-15369 | 2021-12-03 | Operations |
| Casein 50% Premium | IC-15407 | 2024-12-25 | Finance |
| SIG-11-SLQ-KF5B | TC-15418 | 2022-10-26 | Finance |
| SIG-91-GKA-MSWV | BC-15422 | 2021-11-21 | IT Infrastructure |
| Continental Versorgung GmbH | TC-15434 | 2022-05-23 | Finance |
| SIG-69-MPP-WUGO | BC-15446 | 2021-08-22 | IT Infrastructure |
| Vat Reduced BR 7% | TC-15469 | 2024-02-26 | Finance |
| Dextrin Premium | IC-15474 | 2022-12-02 | IT Infrastructure |
| Potassium Sorbate | TC-15482 | 2022-01-24 | Data Governance |
| Pea Protein Standardqualität | TC-15503 | 2021-07-26 | Finance |
| Continental Sourcing | TC-15505 | 2023-04-14 | Product Management |
| Zitronensäure 98% | IC-15507 | 2022-08-22 | Product Management |
| SIG-12-OAV-ALF4 | BC-15510 | 2022-07-09 | IT Infrastructure |
| Sodium Benzoate Pharma Grade | TC-15515 | 2023-05-11 | Data Governance |
| Potassium Sorbate | IC-15533 | 2024-06-20 | IT Infrastructure |
| customs duty nl 15% | IC-15537 | 2023-04-21 | Supply Chain |
| WH-GL-830 | IC-15547 | 2021-04-12 | Product Management |
| PE-PR-163 | BC-15559 | 2023-07-03 | Product Management |
| SIG-76-GST-OWGM | IC-15565 | 2024-07-22 | Product Management |
| cyclodextrin food grade | BC-15568 | 2021-05-07 | Compliance |
| nordic sourcing | BC-15575 | 2021-05-15 | Operations |
| Pea Protein | TC-15578 | 2023-07-10 | Product Management |
| SIG-77-WZV-TKWL | IC-15589 | 2023-07-09 | Operations |
| Central Partners | IC-15591 | 2021-07-07 | IT Infrastructure |
| Calcium Carbonate 50% Qualitätsstufe II | TC-15600 | 2021-12-08 | Operations |
| Atlas Supply Co. | BC-15611 | 2023-02-04 | Data Governance |
| SO-IS-99.5-GR-A-499 | BC-15620 | 2021-11-13 | Data Governance |
| premier supply | BC-15641 | 2021-09-03 | Data Governance |
| ST-TR-590 | BC-15647 | 2021-06-20 | Product Management |
| VA-EN-308 | BC-15662 | 2023-10-03 | Product Management |
| Kasein 50% Premiumqualität | IC-15664 | 2022-04-22 | Supply Chain |
| VA-ST-N-20-162 | BC-15669 | 2022-08-05 | Supply Chain |
| Fructose 99.5% Food Grade | TC-15674 | 2023-06-01 | Data Governance |
| SIG-30-UET-0Q2O | BC-15682 | 2023-01-07 | Operations |
| Elite Sourcing | IC-15687 | 2024-01-16 | Operations |
| LA-AC-25-PR-377 | IC-15694 | 2021-01-14 | Data Governance |
| PA-OI-983 | BC-15701 | 2023-05-10 | Finance |
| Vat Reduced GB 25% | IC-15707 | 2024-10-15 | Finance |
| continental ingredients AG | BC-15710 | 2023-02-27 | Data Governance |
| Lactic Acid 98% Premium | TC-15717 | 2022-03-19 | IT Infrastructure |
| Sodium Benzoate 50% | IC-15742 | 2024-09-03 | Operations |
| SO-BE-70-PR-120 | BC-15750 | 2024-07-08 | Compliance |
| calcium carbonate 98% pharma grade | TC-15752 | 2022-04-06 | Supply Chain |
| Natriumbenzoat Premiumqualität | BC-15759 | 2022-06-24 | Data Governance |
| LA-AC-893 | IC-15773 | 2021-05-07 | Operations |
| Casein 50% Premium | TC-15782 | 2024-04-18 | IT Infrastructure |
| Core Logistics Holdings | BC-15804 | 2021-12-01 | Finance |
| Cyclodextrin | IC-15811 | 2023-07-18 | IT Infrastructure |
| sorbic acid premium | IC-15818 | 2023-08-07 | Operations |
| Sunflower Oil Standard | IC-15820 | 2021-02-23 | Operations |
| Pacific Vertrieb Group | BC-15826 | 2022-10-28 | Supply Chain |
| pea protein tech grade | TC-15829 | 2024-06-19 | Supply Chain |
| Elite Chemicals AG | BC-15831 | 2023-09-27 | Supply Chain |
| Vanguard Ingredients | IC-15839 | 2022-02-17 | Finance |
| Resistant Starch 50% | TC-15843 | 2023-04-03 | Supply Chain |
| dextrose | TC-15849 | 2023-06-01 | Operations |
| premier chemicals KG | BC-15851 | 2023-07-16 | Data Governance |
| SIG-40-CXK-QT2E Group | TC-15855 | 2024-06-02 | Compliance |
| SIG-94-MGT-4WYA | TC-15861 | 2023-03-07 | Operations |
| SIG-83-OTU-QZB6 | IC-15864 | 2021-08-25 | Product Management |
| Natriumchlorid 98% | TC-15867 | 2023-08-16 | Product Management |
| stratos sourcing | IC-15875 | 2022-09-04 | Product Management |
| PO-SO-196 | TC-15882 | 2021-02-26 | Operations |
| ST-MA-730 | IC-15887 | 2022-10-28 | IT Infrastructure |
| SIG-30-NQN-ZENP | IC-15903 | 2021-03-15 | Supply Chain |
| Nexus Distribution PLC | TC-15904 | 2021-12-27 | Data Governance |
| soy isolate | BC-15910 | 2022-01-25 | Supply Chain |
| resistant starch 50% | IC-15925 | 2022-10-28 | Data Governance |
| Maltodextrin DE15 | BC-15953 | 2022-10-24 | Finance |
| Stellar Logistik | BC-15960 | 2023-07-12 | Operations |
| Stratos Rohstoffe Inc. | TC-16003 | 2023-04-22 | Compliance |
| calcium carbonate | BC-16015 | 2021-11-26 | Compliance |
| Meridian Materials | BC-16018 | 2024-03-11 | Product Management |
| GL-DI-754 | BC-16020 | 2022-12-15 | Data Governance |
| SIG-13-CGO-2Y4L | IC-16026 | 2023-08-26 | Supply Chain |
| dextrose 25% tech grade | TC-16041 | 2023-11-25 | Data Governance |
| Resistente Stärke 50% Standardqualität | IC-16049 | 2024-09-18 | Data Governance |
| Cyclodextrin 70% Food Grade | TC-16064 | 2023-01-08 | Operations |
| Excise NL 19% | IC-16076 | 2022-11-15 | Compliance |
| SIG-71-FNO-CX9K | BC-16077 | 2022-01-18 | Product Management |
| Kaliumsorbat Standardqualität | TC-16085 | 2024-01-11 | Product Management |
| NO-IN-797 | BC-16121 | 2023-11-19 | Data Governance |
| sodium benzoate | IC-16129 | 2023-01-22 | Operations |
| soy isolate 99.5% | TC-16140 | 2024-12-26 | Compliance |
| zenith supply | TC-16144 | 2022-12-26 | Operations |
| SO-IS-98-880 | BC-16145 | 2021-01-18 | Supply Chain |
| VE-LO-902 Group | BC-16146 | 2022-02-28 | Product Management |
| Vat Reduced GB 0% | IC-16152 | 2021-01-12 | Product Management |
| Ascorbic Acid | IC-16177 | 2022-11-16 | Finance |
| PA-SO-568 | TC-16201 | 2021-11-07 | Data Governance |
| withholding nl 15% | BC-16221 | 2021-01-02 | IT Infrastructure |
| Lactic Acid 99.5% | TC-16226 | 2022-03-02 | Product Management |
| NE-SU-335 | IC-16229 | 2022-03-20 | Finance |
| Fructose Food Grade | BC-16249 | 2023-07-17 | Operations |
| nordic distribution AG | IC-16253 | 2022-06-01 | Operations |
| CO-CO-290 BV | TC-16274 | 2023-10-25 | Compliance |
| SIG-47-AWI-4RQV | BC-16279 | 2022-07-25 | IT Infrastructure |
| Weizenklebereiweiß Qualitätsstufe I | IC-16304 | 2022-05-04 | Product Management |
| SIG-17-IQV-FES7 | IC-16307 | 2021-05-22 | Compliance |
| vertex logistics | BC-16331 | 2023-10-05 | Data Governance |
| Zenith Sourcing | IC-16351 | 2021-11-27 | Product Management |
| QU-SU-CO-890 | IC-16376 | 2022-01-14 | Supply Chain |
| HO-LO-699 | IC-16389 | 2024-02-07 | IT Infrastructure |
| maltodextrin de5 standard | IC-16391 | 2022-01-11 | Data Governance |
| Rapsöl 98% | TC-16426 | 2022-12-03 | IT Infrastructure |
| CO-SO-101 | IC-16455 | 2022-08-21 | Compliance |
| Quantum Trading | IC-16457 | 2024-05-12 | Finance |
| Atlas Logistics | BC-16459 | 2023-04-02 | Supply Chain |
| PE-PR-929 | BC-16460 | 2023-11-18 | Supply Chain |
| customs duty br 7% | BC-16471 | 2021-10-23 | Supply Chain |
| SIG-89-PGD-QMHH GmbH | BC-16477 | 2024-04-12 | Product Management |
| zenith materials | BC-16478 | 2024-04-23 | Operations |
| Natriumchlorid | BC-16489 | 2021-12-24 | Product Management |
| Fructose | BC-16492 | 2024-04-18 | Finance |
| Maltodextrin DE20 | IC-16505 | 2021-03-04 | IT Infrastructure |
| CU-DU-N-7-394 | IC-16517 | 2022-01-18 | Operations |
| SIG-61-CIV-LFWA | TC-16529 | 2023-12-03 | Product Management |
| PR-SO-441 | BC-16538 | 2022-12-18 | Product Management |
| Palmfett 70% Technische Qualität | TC-16543 | 2021-08-22 | Supply Chain |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | BC-16559 | 2022-09-25 | Compliance |
| CA-50-GR-B-203 | BC-16565 | 2022-09-08 | Supply Chain |
| Meridian Logistik SAS | IC-16571 | 2023-11-23 | Data Governance |
| CY-PH-GR-870 | IC-16576 | 2024-03-26 | Finance |
| SIG-90-SZM-PZJ4 | IC-16596 | 2022-01-26 | Operations |
| Nexus Sourcing | IC-16604 | 2024-11-23 | Data Governance |
| resistant starch | IC-16608 | 2022-09-16 | Finance |
| CA-CA-GR-B-565 | TC-16619 | 2023-11-26 | Data Governance |
| Customs Duty US 20% | TC-16634 | 2024-01-08 | Finance |
| Core Sourcing | BC-16639 | 2021-04-02 | Data Governance |
| Traubenzucker Standardqualität | TC-16667 | 2024-03-10 | Compliance |
| SIG-33-YPL-RQCS | IC-16696 | 2023-03-13 | Compliance |
| Pinnacle Verarbeitung | TC-16698 | 2021-03-28 | Supply Chain |
| baltic materials | TC-16714 | 2022-08-01 | Product Management |
| Pea Protein 70% Lebensmittelrein | BC-16715 | 2022-01-12 | IT Infrastructure |
| Pinnacle Distribution | IC-16724 | 2022-04-04 | Compliance |
| VE-SU-CO-566 | IC-16747 | 2021-11-09 | Supply Chain |
| FR-GR-A-600 | TC-16758 | 2022-10-24 | Compliance |
| SIG-95-EES-2FE9 | IC-16766 | 2023-04-22 | Product Management |
| Soja Isolate | BC-16785 | 2021-09-18 | Product Management |
| SIG-44-HRR-WZP6 | BC-16786 | 2021-08-25 | Operations |
| Elite Materials | BC-16788 | 2021-03-07 | Finance |
| VE-CO-558 | BC-16792 | 2023-02-15 | Data Governance |
| Vertex Ingredients GmbH | IC-16834 | 2023-05-04 | Compliance |
| Zitronensäure Standardqualität | BC-16838 | 2023-01-20 | Compliance |
| Weizenklebereiweiß 99.5% Qualitätsstufe I | IC-16841 | 2021-12-18 | IT Infrastructure |
| SIG-39-EWA-Q37M | IC-16842 | 2024-11-12 | Product Management |
| VA-LO-948 | IC-16858 | 2021-04-08 | Operations |
| Soy Isolate | BC-16875 | 2022-01-08 | IT Infrastructure |
| Stratos Commodities International | IC-16877 | 2022-05-12 | Compliance |
| SIG-79-OZQ-4I2N | IC-16878 | 2022-11-20 | Operations |
| SO-CH-99.5-618 | BC-16882 | 2022-11-15 | Supply Chain |
| casein pharma grade | TC-16887 | 2023-04-11 | Data Governance |
| ME-SO-760 GmbH | IC-16889 | 2021-01-28 | IT Infrastructure |
| Cyclodextrin 98% Pharmazeutisch rein | IC-16893 | 2023-04-03 | Data Governance |
| CO-MA-863 | BC-16957 | 2024-01-26 | Operations |
| Soja Isolate 98% Premiumqualität | BC-16962 | 2024-01-06 | IT Infrastructure |
| Vat Standard NL 25% | IC-16966 | 2022-02-10 | Operations |
| RE-ST-GR-B-805 | IC-16995 | 2024-06-11 | IT Infrastructure |
| CY-98-PH-GR-614 | BC-16996 | 2022-07-22 | Compliance |
| Fructose Qualitätsstufe I | TC-17026 | 2021-06-11 | Finance |
| CI-AC-25-GR-A-669 | IC-17034 | 2024-07-28 | Compliance |
| ZE-LO-524 | TC-17035 | 2021-12-07 | Compliance |
| Vat Standardqualität NL 19% | BC-17046 | 2022-09-27 | Compliance |
| cyclodextrin premium | IC-17075 | 2021-08-28 | Finance |
| Nexus Materials | IC-17077 | 2024-06-26 | Finance |
| Citric Acid 99.5% | BC-17080 | 2023-01-25 | Finance |
| fructose tech grade | TC-17093 | 2024-11-26 | Compliance |
| HO-PA-149 International | IC-17099 | 2023-02-15 | Product Management |
| Continental Enterprise GmbH | BC-17100 | 2021-11-15 | Compliance |
| vanguard sourcing | IC-17109 | 2024-11-02 | Data Governance |
| SIG-69-OFZ-JW34 | TC-17112 | 2022-03-25 | Finance |
| casein | IC-17116 | 2024-10-12 | Data Governance |
| Palm Oil 98% | BC-17129 | 2024-04-18 | Supply Chain |
| Catalyst Materials | TC-17145 | 2021-01-22 | Operations |
| CY-PH-GR-870 | IC-17148 | 2024-04-27 | Compliance |
| Dextrose Grade A | IC-17158 | 2024-10-04 | Finance |
| sorbic acid food grade | IC-17161 | 2022-10-05 | IT Infrastructure |
| Premier Supply Co. | TC-17169 | 2023-01-10 | Operations |
| RE-ST-FO-GR-998 | TC-17197 | 2022-01-02 | Data Governance |
| SO-BE-70-PR-120 | TC-17205 | 2021-11-10 | Operations |
| Quantum Versorgung GmbH | BC-17212 | 2023-06-25 | Data Governance |
| Palmfett | IC-17220 | 2022-04-02 | Finance |
| ascorbic acid standard | TC-17241 | 2021-09-03 | Product Management |
| CO-MA-245 | TC-17253 | 2021-07-26 | Product Management |
| AT-PA-546 Corp. | TC-17256 | 2023-05-09 | Compliance |
| Soy Isolate 50% Food Grade | BC-17279 | 2024-08-05 | Product Management |
| Traubenzucker Qualitätsstufe I | IC-17289 | 2024-04-02 | IT Infrastructure |
| dextrin standard | TC-17300 | 2022-01-25 | IT Infrastructure |
| vat reduced cn 15% | IC-17323 | 2023-06-01 | Data Governance |
| Excise NL 15% | BC-17328 | 2023-08-18 | Data Governance |
| Vanguard Partners PLC | TC-17333 | 2023-12-20 | Compliance |
| VE-CO-290 AG | BC-17421 | 2024-08-03 | Supply Chain |
| DE-PH-GR-173 | IC-17422 | 2022-04-01 | Product Management |
| SIG-88-RKE-8R7A | TC-17431 | 2021-08-15 | Data Governance |
| lactic acid | TC-17445 | 2021-03-07 | Finance |
| SIG-27-VCT-2O4S | TC-17462 | 2024-02-19 | Data Governance |
| Citric Acid 25% Technical | TC-17473 | 2021-07-22 | Operations |
| SIG-19-TLQ-1P5Z | TC-17480 | 2024-08-12 | Product Management |
| SIG-89-JZC-1682 | BC-17484 | 2022-12-14 | Data Governance |
| Excise IN 5% | TC-17508 | 2021-09-12 | IT Infrastructure |
| SIG-12-USU-9HWB GmbH | TC-17523 | 2022-09-08 | Finance |
| Natriumbenzoat 50% | BC-17531 | 2022-07-03 | Operations |
| Quantum Supply Co. | TC-17533 | 2022-11-10 | Operations |
| Atlas Ingredients PLC | IC-17538 | 2023-09-07 | Operations |
| SIG-50-GYK-UH5P | BC-17546 | 2021-08-07 | Finance |
| Vat Reduced GB 25% | BC-17554 | 2024-07-24 | Supply Chain |
| SIG-60-OHC-5EQB | BC-17562 | 2021-11-19 | Finance |
| Kaliumsorbat | IC-17567 | 2024-12-10 | Compliance |
| Resistant Starch Standard | BC-17569 | 2024-02-12 | Supply Chain |
| Zitronensäure Lebensmittelrein | IC-17578 | 2024-09-25 | IT Infrastructure |
| Elite Supply Co. | IC-17592 | 2021-05-10 | Operations |
| Global Logistics | TC-17603 | 2021-03-08 | Product Management |
| Dextrin 98% Food Grade | BC-17608 | 2023-11-20 | Product Management |
| soy isolate premium | BC-17629 | 2021-02-18 | Product Management |
| LA-AC-393 | BC-17635 | 2022-09-24 | IT Infrastructure |
| Lactic Acid 99.5% | TC-17643 | 2024-12-14 | Finance |
| Rapsöl | BC-17652 | 2024-03-14 | Product Management |
| Cyclodextrin Lebensmittelrein | BC-17687 | 2023-07-03 | Product Management |
| PR-SU-CO-650 | BC-17700 | 2023-08-26 | Operations |
| sorbic acid | BC-17709 | 2022-09-05 | Finance |
| Natriumbenzoat 50% Technische Qualität | BC-17722 | 2023-06-13 | IT Infrastructure |
| Vat Reduced FR 20% | TC-17730 | 2021-03-12 | Compliance |
| SIG-80-WKN-N0SS | IC-17732 | 2024-01-09 | Finance |
| Atlas Sourcing | IC-17734 | 2024-08-25 | Data Governance |
| VA-ST-G-20-932 | IC-17738 | 2022-11-07 | Data Governance |
| Citric Acid Pharma Grade | IC-17758 | 2023-08-26 | IT Infrastructure |
| pea protein 25% pharma grade | IC-17769 | 2022-02-22 | Compliance |
| sodium benzoate 99.5% premium | IC-17772 | 2022-01-15 | Finance |
| Pacific Supply Co. | BC-17776 | 2021-07-25 | Product Management |
| Zitronensäure 98% | TC-17779 | 2021-09-26 | Data Governance |
| nexus ingredients SAS | TC-17784 | 2023-06-15 | Supply Chain |
| SIG-69-OFZ-JW34 | IC-17800 | 2023-05-03 | Supply Chain |
| CY-763 | IC-17821 | 2021-07-16 | Operations |
| Nordic Manufacturing Group | IC-17829 | 2023-08-16 | Compliance |
| Vat Reduced IN 5% | TC-17840 | 2021-10-23 | Operations |
| SIG-13-ZRN-WZGO | IC-17846 | 2024-08-23 | Product Management |
| Meridian Versorgung GmbH | IC-17852 | 2023-01-07 | IT Infrastructure |
| Kaliumsorbat | TC-17899 | 2024-10-08 | Supply Chain |
| EX-B-10-648 | BC-17904 | 2021-02-15 | Supply Chain |
| Atlantic Logistics SAS | IC-17906 | 2022-02-09 | Compliance |
| GL-MA-581 | TC-17913 | 2022-11-20 | IT Infrastructure |
| Ascorbic Acid 99.5% Premiumqualität | IC-17944 | 2024-03-20 | IT Infrastructure |
| SIG-97-QNX-7TWO | TC-17958 | 2024-04-18 | Product Management |
| Palmfett 98% | IC-17960 | 2023-11-03 | Supply Chain |
| CA-CA-50-260 | TC-17988 | 2022-09-16 | Product Management |
| Kasein Qualitätsstufe I | TC-18003 | 2021-02-27 | IT Infrastructure |
| global partners BV | BC-18037 | 2022-11-18 | Supply Chain |
| SIG-39-OZI-N968 | TC-18042 | 2021-12-14 | Compliance |
| Soy Isolate Grade B | IC-18051 | 2024-09-07 | Product Management |
| calcium carbonate | IC-18056 | 2022-03-15 | Operations |
| calcium carbonate | TC-18061 | 2022-08-02 | IT Infrastructure |
| PR-SU-CO-920 | IC-18067 | 2021-04-08 | Supply Chain |
| SIG-17-YLM-LBLW | TC-18080 | 2022-11-14 | Operations |
| Pea Protein | TC-18092 | 2024-06-06 | Supply Chain |
| SIG-11-EIQ-WD14 | BC-18125 | 2024-07-02 | Compliance |
| SIG-83-SCO-PIKN | BC-18127 | 2023-02-03 | Supply Chain |
| ZE-SU-434 NV | TC-18148 | 2023-01-13 | Supply Chain |
| VA-ST-D-0-573 | TC-18150 | 2021-11-02 | Supply Chain |
| SIG-85-ACE-0XNG | TC-18172 | 2024-09-01 | Finance |
| SIG-30-SYO-74WX | BC-18208 | 2022-02-15 | Finance |
| Dextrose Technical | BC-18214 | 2022-02-25 | Data Governance |
| Palm Oil | TC-18220 | 2022-02-13 | Finance |
| Sodium Benzoate 50% | IC-18239 | 2022-12-28 | Operations |
| pea protein | IC-18243 | 2024-08-09 | Operations |
| EL-SO-688 | BC-18272 | 2023-11-15 | Data Governance |
| MA-DE-516 | IC-18273 | 2022-11-11 | IT Infrastructure |
| sodium chloride 70% | IC-18284 | 2021-09-13 | Operations |
| Meridian Solutions International | TC-18294 | 2021-11-03 | IT Infrastructure |
| pea protein 70% premium | IC-18299 | 2024-06-21 | Finance |
| SIG-14-HQE-PUWC | IC-18319 | 2023-06-13 | Finance |
| citric acid food grade | TC-18324 | 2022-09-16 | Product Management |
| Resistant Starch Technical | BC-18342 | 2022-04-06 | Operations |
| Lactic Acid Food Grade | TC-18423 | 2021-03-18 | Compliance |
| Vat Reduced BR 7% | IC-18445 | 2023-03-18 | Compliance |
| SIG-60-NXS-8BAO | IC-18451 | 2023-05-25 | Operations |
| SIG-58-LWY-Q8P6 | TC-18468 | 2022-04-05 | Product Management |
| Palmfett 25% | TC-18474 | 2023-05-08 | IT Infrastructure |
| Kasein | BC-18480 | 2024-01-12 | Operations |
| SIG-79-DVU-H9H4 | BC-18482 | 2024-07-19 | Operations |
| SIG-47-GAT-ET7B | TC-18509 | 2021-08-18 | Data Governance |
| Apex Sourcing | BC-18522 | 2021-09-27 | Compliance |
| QU-TR-219 International | TC-18526 | 2023-05-10 | Operations |
| excise in 21% | BC-18553 | 2024-10-08 | Supply Chain |
| BA-TR-377 NV | TC-18583 | 2021-11-11 | Data Governance |
| VA-RE-I-5-252 | BC-18596 | 2022-07-10 | Compliance |
| prism ingredients AG | TC-18600 | 2021-03-20 | Data Governance |
| CI-AC-538 | IC-18608 | 2022-08-15 | IT Infrastructure |
| WH-GL-123 | BC-18625 | 2024-08-03 | Operations |
| SIG-40-WLB-9IFD | IC-18633 | 2021-09-08 | Operations |
| IS-70-838 | TC-18647 | 2024-05-02 | Supply Chain |
| SIG-56-NOU-ZR98 | BC-18649 | 2022-10-21 | Compliance |
| SIG-42-UMA-WZ7F | TC-18682 | 2024-04-15 | IT Infrastructure |
| CI-AC-99.5-674 | BC-18694 | 2021-08-22 | Supply Chain |
| pea protein | IC-18709 | 2021-02-27 | IT Infrastructure |
| SIG-60-TMF-XHW0 | BC-18715 | 2024-12-28 | IT Infrastructure |
| ME-SO-760 GmbH | BC-18716 | 2021-10-02 | Supply Chain |
| DE-840 | IC-18720 | 2021-03-21 | Compliance |
| Atlantic Logistik SAS | TC-18730 | 2023-06-28 | Data Governance |
| sorbic acid standard | IC-18731 | 2024-11-04 | IT Infrastructure |
| apex logistics | IC-18747 | 2023-10-02 | Operations |
| SIG-99-GVJ-VPM6 | BC-18760 | 2021-04-18 | Data Governance |
| SIG-47-YTF-UPMT | BC-18766 | 2022-10-04 | Data Governance |
| Withholding BR 0% | BC-18767 | 2022-10-06 | IT Infrastructure |
| SO-BE-GR-B-914 | IC-18774 | 2021-07-19 | Data Governance |
| VE-DI-556 SA | IC-18777 | 2022-11-19 | Finance |
| SIG-36-TML-VS0J | BC-18783 | 2023-02-24 | Supply Chain |
| CE-SU-700 Group | IC-18788 | 2022-11-18 | Data Governance |
| potassium sorbate 50% tech grade | BC-18825 | 2023-02-11 | Compliance |
| SO-CH-98-657 | BC-18828 | 2022-11-10 | Supply Chain |
| Pacific Distribution NV | IC-18836 | 2021-08-16 | IT Infrastructure |
| SIG-83-DGX-TY87 | TC-18837 | 2021-07-13 | Data Governance |
| SO-CH-257 | BC-18843 | 2024-08-14 | Supply Chain |
| Calcium Carbonate 98% | TC-18850 | 2021-10-20 | Compliance |
| PI-SO-581 Inc. | BC-18852 | 2021-08-23 | Data Governance |
| Citric Acid 25% | BC-18865 | 2024-11-26 | Supply Chain |
| Nexus Distribution | IC-18879 | 2021-12-05 | Operations |
| VA-DI-105 | BC-18890 | 2024-09-10 | Compliance |
| Fructose Pharmazeutisch rein | IC-18901 | 2023-09-06 | Product Management |
| Stratos Logistik | TC-18931 | 2023-08-12 | Finance |
| isoglucose 70% | BC-18963 | 2022-05-19 | IT Infrastructure |
| Excise NL 21% | IC-18975 | 2021-02-09 | Finance |
| Fructose | BC-18986 | 2024-01-15 | Data Governance |
| Prism Industrien Holdings | IC-18987 | 2021-02-27 | Compliance |
| Excise US 5% | IC-19001 | 2022-03-23 | Product Management |
| PI-PR-193 | BC-19006 | 2021-09-23 | IT Infrastructure |
| Rapsöl 50% Pharmazeutisch rein | BC-19015 | 2022-07-09 | IT Infrastructure |
| SIG-23-IEJ-V2T3 | BC-19027 | 2024-04-10 | Operations |
| Vat Reduced GB 19% | BC-19029 | 2023-09-16 | Data Governance |
| RA-OI-25-PH-GR-210 | BC-19035 | 2021-08-15 | Product Management |
| Stratos Supply Co. | BC-19040 | 2023-06-09 | Data Governance |
| Casein Technical | IC-19045 | 2022-11-08 | Compliance |
| dextrose | TC-19060 | 2024-04-10 | Supply Chain |
| FR-FO-GR-823 | IC-19078 | 2021-12-20 | IT Infrastructure |
| sodium benzoate 99.5% tech grade | IC-19080 | 2022-01-05 | Operations |
| SIG-83-PHT-N27M | IC-19097 | 2023-01-05 | Compliance |
| Isoglucose 70% | TC-19102 | 2023-08-10 | Operations |
| Apex Commodities Holdings | TC-19115 | 2021-12-03 | Compliance |
| zenith sourcing | TC-19116 | 2022-03-26 | Compliance |
| Palmfett | IC-19127 | 2023-07-22 | Product Management |
| Sorbinsäure | BC-19154 | 2022-01-08 | Supply Chain |
| Natriumchlorid 98% Pharmazeutisch rein | TC-19159 | 2021-10-12 | Data Governance |
| SIG-45-ZTJ-PA16 | IC-19171 | 2022-01-12 | Finance |
| Dextrin Standardqualität | IC-19186 | 2023-05-12 | IT Infrastructure |
| ME-MA-977 | BC-19215 | 2022-08-13 | IT Infrastructure |
| Resistente Stärke Pharmazeutisch rein | IC-19227 | 2023-08-25 | Product Management |
| Citric Acid | BC-19231 | 2022-11-28 | Product Management |
| Nexus Partners GmbH | IC-19250 | 2022-07-24 | IT Infrastructure |
| SIG-13-CGO-2Y4L | IC-19258 | 2024-01-14 | Finance |
| Coconut Oil 50% Technische Qualität | BC-19276 | 2022-11-21 | IT Infrastructure |
| DE-602 | TC-19283 | 2024-10-03 | Finance |
| SIG-60-PEY-H3GM | BC-19286 | 2023-05-12 | Operations |
| prism industries International | IC-19297 | 2022-09-04 | Product Management |
| SIG-17-YLM-LBLW | IC-19298 | 2022-05-10 | Operations |
| SIG-88-VVU-EL88 | IC-19303 | 2021-05-21 | Compliance |
| SO-BE-113 | IC-19332 | 2022-07-20 | IT Infrastructure |
| SIG-60-WEX-2G05 | BC-19353 | 2021-08-15 | IT Infrastructure |
| potassium sorbate | TC-19374 | 2021-04-03 | IT Infrastructure |
| Global Logistics | TC-19379 | 2024-02-05 | Supply Chain |
| rapeseed oil 98% standard | BC-19415 | 2022-02-03 | Product Management |
| Rapeseed Oil Technical | IC-19423 | 2021-01-21 | Product Management |
| Catalyst Industrien PLC | TC-19430 | 2023-03-18 | Product Management |
| vertex ingredients KG | TC-19437 | 2022-12-15 | IT Infrastructure |
| wheat gluten premium | IC-19440 | 2021-08-20 | Data Governance |
| citric acid food grade | IC-19443 | 2021-07-07 | Supply Chain |
| NO-LO-524 | TC-19467 | 2024-09-26 | Operations |
| AT-IN-847 GmbH | BC-19469 | 2022-02-03 | Data Governance |
| SIG-45-ZZU-GRXH International | BC-19474 | 2022-04-19 | Data Governance |
| SIG-60-ZEV-V2NY | IC-19482 | 2024-06-11 | Product Management |
| SIG-16-IYP-EOZP | BC-19483 | 2021-09-17 | Finance |
| Quantum Sourcing | BC-19494 | 2024-03-09 | Supply Chain |
| SIG-27-IRG-QSO9 International | BC-19498 | 2022-02-01 | IT Infrastructure |
| WH-GL-123 | TC-19509 | 2024-07-24 | Operations |
| Coconut Oil 50% | IC-19515 | 2022-03-24 | Product Management |
| Ascorbic Acid 50% Standardqualität | IC-19518 | 2023-03-25 | Operations |
| rapeseed oil | IC-19524 | 2021-12-03 | Compliance |
| Stratos Logistik | TC-19527 | 2023-04-17 | Operations |
| VE-LO-777 | BC-19537 | 2021-12-19 | Compliance |
| SO-IS-99.5-PR-187 | IC-19546 | 2024-01-11 | Compliance |
| resistant starch | BC-19557 | 2023-09-19 | Supply Chain |
| calcium carbonate 98% pharma grade | TC-19579 | 2023-05-14 | Supply Chain |
| AT-MA-796 LLC | BC-19584 | 2023-01-21 | Compliance |
| CA-CA-50-GR-A-195 | TC-19596 | 2024-12-20 | Product Management |
| Apex Solutions International | IC-19598 | 2021-11-18 | Supply Chain |
| Vertex Distribution Holdings | TC-19600 | 2023-06-08 | Compliance |
| Palm Oil 70% | BC-19611 | 2023-03-14 | Compliance |
| SIG-39-LKH-DFJY | IC-19647 | 2021-10-07 | Operations |
| Nordic Logistik PLC | IC-19688 | 2021-09-23 | Compliance |
| Calcium Carbonate Standardqualität | TC-19705 | 2021-07-21 | Supply Chain |
| Lactic Acid Standardqualität | TC-19740 | 2022-04-17 | IT Infrastructure |
| Sorbinsäure 98% | TC-19741 | 2024-06-16 | Supply Chain |
| sorbic acid 70% | IC-19756 | 2021-04-13 | Supply Chain |
| Continental Processing | TC-19783 | 2021-02-13 | Data Governance |
| Dextrose | TC-19785 | 2024-04-27 | Finance |
| PR-CO-443 Group | TC-19810 | 2024-08-25 | Finance |
| prime chemicals SA | TC-19821 | 2021-06-14 | Compliance |
| resistant starch | BC-19837 | 2021-02-24 | Compliance |
| NE-PA-358 | IC-19840 | 2021-01-07 | Operations |
| SIG-32-RJE-L1OT | IC-19855 | 2022-11-03 | Supply Chain |
| stratos partners SA | BC-19870 | 2021-09-07 | Finance |
| Rapsöl 99.5% Technische Qualität | TC-19871 | 2021-10-05 | Operations |
| PR-SO-769 LLC | IC-19887 | 2021-08-19 | IT Infrastructure |
| palm oil 70% premium | TC-19897 | 2022-12-25 | Data Governance |
| pacific materials | BC-19931 | 2023-07-16 | Supply Chain |
| CA-CA-70-883 | BC-19939 | 2023-02-08 | Data Governance |
| Atlantic Commodities | TC-19942 | 2021-03-07 | Finance |
| Vat Standardqualität DE 25% | BC-19945 | 2024-02-02 | Operations |
| Core Chemicals | BC-19950 | 2024-01-15 | Finance |
| sodium benzoate | IC-19983 | 2023-02-12 | IT Infrastructure |
| PE-PR-746 | TC-19992 | 2021-04-06 | IT Infrastructure |
| Dextrose 50% | TC-20003 | 2024-01-17 | Operations |
| Palmfett | IC-20028 | 2024-10-13 | Operations |
| CO-DI-629 BV | IC-20039 | 2023-10-21 | Supply Chain |
| stratos trading | IC-20048 | 2022-12-03 | Finance |
| Potassium Sorbate | IC-20051 | 2021-11-24 | Supply Chain |
| MA-DE-744 | IC-20053 | 2023-12-17 | IT Infrastructure |
| nexus logistics | TC-20088 | 2024-04-12 | IT Infrastructure |
| global logistics | TC-20094 | 2022-01-11 | Compliance |
| Continental Sourcing | IC-20097 | 2021-12-09 | Product Management |
| Fructose 70% | TC-20102 | 2021-10-22 | Supply Chain |
| IS-50-GR-A-791 | IC-20109 | 2024-05-18 | Compliance |
| Palmfett | TC-20123 | 2021-11-26 | Finance |
| PE-PR-302 | IC-20154 | 2021-03-04 | Supply Chain |
| SIG-17-ZBZ-BJS4 SARL | TC-20166 | 2021-05-02 | Supply Chain |
| Dextrin Premium | IC-20168 | 2023-11-16 | Product Management |
| DE-98-512 | BC-20188 | 2022-03-03 | Data Governance |
| coconut oil 25% tech grade | BC-20191 | 2022-05-14 | Data Governance |
| AS-AC-FO-GR-835 | BC-20210 | 2023-03-22 | Finance |
| SIG-70-EXR-LD0M | TC-20215 | 2023-11-24 | Supply Chain |
| SIG-50-FUX-7S9T | IC-20223 | 2021-02-25 | Compliance |
| SIG-34-TKJ-QFOY | IC-20225 | 2023-08-04 | Data Governance |
| Excise CN 21% | TC-20243 | 2022-06-26 | Compliance |
| Lactic Acid | TC-20246 | 2022-01-08 | Finance |
| Natriumchlorid | IC-20248 | 2023-05-02 | Compliance |
| SIG-77-OCZ-Q3GH | BC-20250 | 2022-06-23 | Operations |
| Apex Sourcing | BC-20253 | 2022-05-08 | IT Infrastructure |
| Sonnenblumenöl 70% Lebensmittelrein | IC-20260 | 2023-03-14 | Supply Chain |
| Core Logistik | IC-20268 | 2023-09-23 | Finance |
| Resistant Starch 98% Grade B | TC-20295 | 2024-04-12 | Product Management |
| HO-SU-CO-454 | IC-20308 | 2023-06-24 | IT Infrastructure |
| MA-DE-799 | TC-20314 | 2024-06-01 | Operations |
| vat reduced br 5% | IC-20330 | 2021-09-25 | Data Governance |
| SIG-62-BTJ-PQV9 | IC-20352 | 2024-10-12 | Supply Chain |
| Isoglucose 50% Lebensmittelrein | IC-20354 | 2021-10-18 | Supply Chain |
| SIG-85-FIY-2QW4 | IC-20362 | 2023-03-24 | Compliance |
| Resistant Starch 70% | BC-20370 | 2021-09-03 | Supply Chain |
| Dextrin 70% | TC-20403 | 2024-05-10 | Product Management |
| SO-AC-377 | IC-20407 | 2024-12-06 | Data Governance |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| Premier Partners Group | IC-8145 | SUPERSEDED | Historical - verify before use |
| SIG-25-WDK-CWCD | IC-8414 | SUPERSEDED | Historical - verify before use |
| lactic acid standard | IC-7769 | PROVISIONAL | Historical - verify before use |
| Zitronensäure | IC-5156 | SUPERSEDED | Historical - verify before use |
| Vat Standardqualität BR 25% | IC-9457 | PROVISIONAL | Historical - verify before use |
| Baltic Processing PLC | IC-9584 | DEPRECATED | Historical - verify before use |
| Pinnacle Materials | IC-6637 | REVIEW REQUIRED | Historical - verify before use |
| Citric Acid 70% | IC-9825 | DEPRECATED | Historical - verify before use |
| SIG-69-XLH-L6HZ | IC-7800 | REVIEW REQUIRED | Historical - verify before use |
| Dextrose Grade A | IC-5377 | REVIEW REQUIRED | Historical - verify before use |
| central distribution | IC-7016 | DEPRECATED | Historical - verify before use |
| Quantum Commodities PLC | IC-5217 | SUPERSEDED | Historical - verify before use |
| WH-GL-ST-378 | IC-5542 | REVIEW REQUIRED | Historical - verify before use |
| VA-RE-F-21-230 | IC-7335 | REVIEW REQUIRED | Historical - verify before use |
| WH-GL-146 | IC-7002 | PROVISIONAL | Historical - verify before use |
| sorbic acid | IC-8376 | REVIEW REQUIRED | Historical - verify before use |
| quantum logistics | IC-7819 | DEPRECATED | Historical - verify before use |
| Lactic Acid | IC-8726 | DEPRECATED | Historical - verify before use |
| Resistente Stärke Lebensmittelrein | IC-6336 | SUPERSEDED | Historical - verify before use |
| Resistant Starch Pharma Grade | IC-9597 | REVIEW REQUIRED | Historical - verify before use |
| Maltodextrin-Pulver DE15 | IC-8018 | DEPRECATED | Historical - verify before use |
| ME-IN-934 NV | IC-9479 | REVIEW REQUIRED | Historical - verify before use |
| SIG-13-CAZ-HXXP | IC-7532 | SUPERSEDED | Historical - verify before use |
| SIG-66-DRZ-QEHY | IC-6217 | REVIEW REQUIRED | Historical - verify before use |
| Soy Isolate 98% | IC-7497 | PROVISIONAL | Historical - verify before use |
| Lactic Acid | IC-8260 | DEPRECATED | Historical - verify before use |
| Lactic Acid | IC-7113 | SUPERSEDED | Historical - verify before use |
| resistant starch | IC-8858 | PROVISIONAL | Historical - verify before use |
| SIG-67-TPL-WT5F | IC-8592 | REVIEW REQUIRED | Historical - verify before use |
| coconut oil food grade | IC-9403 | DEPRECATED | Historical - verify before use |
| Coconut Oil | IC-7636 | SUPERSEDED | Historical - verify before use |
| SIG-24-VMY-QMRL | IC-7393 | SUPERSEDED | Historical - verify before use |
| vertex materials | IC-7241 | REVIEW REQUIRED | Historical - verify before use |
| Sorbinsäure Premiumqualität | IC-9995 | PROVISIONAL | Historical - verify before use |
| Apex Versorgung GmbH | IC-5171 | REVIEW REQUIRED | Historical - verify before use |
| GL-SY-70-549 | IC-5716 | REVIEW REQUIRED | Historical - verify before use |
| PO-SO-GR-A-715 | IC-8685 | PROVISIONAL | Historical - verify before use |
| nordic manufacturing International | IC-8388 | SUPERSEDED | Historical - verify before use |
| HO-DI-531 Group | IC-9297 | DEPRECATED | Historical - verify before use |
| nexus ingredients SAS | IC-9129 | REVIEW REQUIRED | Historical - verify before use |
| Cyclodextrin Standardqualität | IC-8278 | DEPRECATED | Historical - verify before use |
| Sorbinsäure 98% | IC-6986 | PROVISIONAL | Historical - verify before use |
| meridian sourcing | IC-9551 | DEPRECATED | Historical - verify before use |
| Coconut Oil Standard | IC-6707 | DEPRECATED | Historical - verify before use |
| central distribution | IC-6879 | REVIEW REQUIRED | Historical - verify before use |
| SIG-22-TOX-02GV | IC-6071 | PROVISIONAL | Historical - verify before use |
| LA-AC-891 | IC-6165 | REVIEW REQUIRED | Historical - verify before use |
| PA-OI-70-GR-B-781 | IC-6982 | SUPERSEDED | Historical - verify before use |
| dextrose 25% tech grade | IC-7304 | PROVISIONAL | Historical - verify before use |
| Coconut Oil 50% | IC-5943 | REVIEW REQUIRED | Historical - verify before use |
| Glucose Syrup 70% | IC-6108 | REVIEW REQUIRED | Historical - verify before use |
| prism supply | IC-5499 | DEPRECATED | Historical - verify before use |
| Resistente Stärke 50% Standardqualität | IC-6873 | PROVISIONAL | Historical - verify before use |
| wheat gluten premium | IC-5593 | PROVISIONAL | Historical - verify before use |
| Sodium Benzoate Grade A | IC-5839 | PROVISIONAL | Historical - verify before use |
| Withholding NL 7% | IC-9757 | SUPERSEDED | Historical - verify before use |
| Atlantic Materials | IC-7733 | DEPRECATED | Historical - verify before use |
| Core Trading | IC-9854 | REVIEW REQUIRED | Historical - verify before use |
| baltic solutions Group | IC-9492 | DEPRECATED | Historical - verify before use |
| Zitronensäure Premiumqualität | IC-8236 | PROVISIONAL | Historical - verify before use |
| SIG-39-KYF-P35A | IC-5496 | SUPERSEDED | Historical - verify before use |
| Prism Werkstoffe | IC-7629 | REVIEW REQUIRED | Historical - verify before use |
| resistant starch 98% pharma grade | IC-8922 | REVIEW REQUIRED | Historical - verify before use |
| nexus logistics | IC-6222 | DEPRECATED | Historical - verify before use |
| SIG-13-ZIB-S8MV International | IC-9522 | REVIEW REQUIRED | Historical - verify before use |
| Palm Oil | IC-9118 | SUPERSEDED | Historical - verify before use |
| Isoglucose Premium | IC-6579 | PROVISIONAL | Historical - verify before use |
| fructose premium | IC-5455 | SUPERSEDED | Historical - verify before use |
| VA-ST-D-10-295 | IC-7357 | PROVISIONAL | Historical - verify before use |
| CA-50-GR-B-203 | IC-9952 | REVIEW REQUIRED | Historical - verify before use |
| Prime Versorgung GmbH | IC-8169 | PROVISIONAL | Historical - verify before use |
| Isoglucose Technical | IC-9230 | DEPRECATED | Historical - verify before use |
| SIG-59-ZZK-AYAJ PLC | IC-6022 | SUPERSEDED | Historical - verify before use |
| Fructose | IC-5366 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat Standardqualität | IC-7058 | PROVISIONAL | Historical - verify before use |
| Cyclodextrin Premiumqualität | IC-9439 | SUPERSEDED | Historical - verify before use |
| SIG-39-QZD-93EZ | IC-8947 | PROVISIONAL | Historical - verify before use |
| Dextrin 70% Pharmazeutisch rein | IC-6482 | SUPERSEDED | Historical - verify before use |
| Maltodextrin DE10 | IC-6654 | REVIEW REQUIRED | Historical - verify before use |
| WI-U-10-721 | IC-9908 | DEPRECATED | Historical - verify before use |
| atlas sourcing | IC-5221 | SUPERSEDED | Historical - verify before use |
| NO-SU-CO-376 | IC-7104 | SUPERSEDED | Historical - verify before use |
| SIG-88-AGF-FF5L | IC-9871 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat 25% | IC-6013 | SUPERSEDED | Historical - verify before use |
| excise in 10% | IC-5197 | DEPRECATED | Historical - verify before use |
| withholding fr 10% | IC-6128 | SUPERSEDED | Historical - verify before use |
| Continental Enterprise Holdings | IC-5273 | PROVISIONAL | Historical - verify before use |
| Vanguard Logistics | IC-7836 | SUPERSEDED | Historical - verify before use |
| Glukosesirup Syrup Technische Qualität | IC-8807 | PROVISIONAL | Historical - verify before use |
| Premier Logistics | IC-7191 | REVIEW REQUIRED | Historical - verify before use |
| EL-SO-688 | IC-8139 | REVIEW REQUIRED | Historical - verify before use |
| Maltodextrin DE5 Grade B | IC-6321 | DEPRECATED | Historical - verify before use |
| vat standard gb 19% | IC-5079 | SUPERSEDED | Historical - verify before use |
| Catalyst Industries International | IC-6202 | REVIEW REQUIRED | Historical - verify before use |
| Palmfett Qualitätsstufe II | IC-5191 | REVIEW REQUIRED | Historical - verify before use |
| Isoglucose | IC-9006 | REVIEW REQUIRED | Historical - verify before use |
| SIG-65-IJJ-DXAJ SA | IC-7124 | SUPERSEDED | Historical - verify before use |
| sodium benzoate 99.5% tech grade | IC-9866 | REVIEW REQUIRED | Historical - verify before use |
| Casein 25% Pharma Grade | IC-8877 | REVIEW REQUIRED | Historical - verify before use |
| SIG-52-HZA-742D | IC-5617 | SUPERSEDED | Historical - verify before use |
| Vat Standardqualität IN 0% | IC-6902 | REVIEW REQUIRED | Historical - verify before use |
| Vanguard Partners PLC | IC-8773 | DEPRECATED | Historical - verify before use |
| Resistant Starch 70% Food Grade | IC-9574 | DEPRECATED | Historical - verify before use |
| Casein Technical | IC-7155 | REVIEW REQUIRED | Historical - verify before use |
| vanguard industries PLC | IC-5936 | PROVISIONAL | Historical - verify before use |
| AS-AC-130 | IC-7355 | SUPERSEDED | Historical - verify before use |
| Pea Protein Premiumqualität | IC-5881 | PROVISIONAL | Historical - verify before use |
| SIG-40-NOO-BAK8 | IC-7262 | SUPERSEDED | Historical - verify before use |
| Customs Duty FR 7% | IC-6863 | PROVISIONAL | Historical - verify before use |
| fructose standard | IC-5512 | PROVISIONAL | Historical - verify before use |
| Potassium Sorbate Food Grade | IC-6833 | REVIEW REQUIRED | Historical - verify before use |
| PO-SO-TE-239 | IC-9967 | REVIEW REQUIRED | Historical - verify before use |
| SIG-60-KAS-IVMD | IC-9081 | DEPRECATED | Historical - verify before use |
| Vat Reduced GB 25% | IC-6007 | REVIEW REQUIRED | Historical - verify before use |
| DE-70-PH-GR-978 | IC-7471 | PROVISIONAL | Historical - verify before use |
| SIG-60-KAS-IVMD | IC-9415 | REVIEW REQUIRED | Historical - verify before use |
| Dextrin 50% | IC-7022 | SUPERSEDED | Historical - verify before use |
| Resistant Starch Grade B | IC-9645 | PROVISIONAL | Historical - verify before use |
| EX-F-21-883 | IC-7741 | PROVISIONAL | Historical - verify before use |
| Zitronensäure | IC-8108 | DEPRECATED | Historical - verify before use |
| SIG-75-XPL-QWB7 GmbH | IC-7260 | SUPERSEDED | Historical - verify before use |
| PA-OI-70-GR-B-781 | IC-9885 | DEPRECATED | Historical - verify before use |
| CA-CA-50-GR-A-195 | IC-7858 | PROVISIONAL | Historical - verify before use |
| DE-GR-B-157 | IC-7007 | SUPERSEDED | Historical - verify before use |
| Maltodextrin-Pulver DE10 | IC-8017 | PROVISIONAL | Historical - verify before use |
| RA-OI-99.5-602 | IC-8102 | PROVISIONAL | Historical - verify before use |
| Palmfett 98% Qualitätsstufe I | IC-9874 | DEPRECATED | Historical - verify before use |
| NE-LO-735 | IC-6895 | PROVISIONAL | Historical - verify before use |
| Zitronensäure | IC-9043 | PROVISIONAL | Historical - verify before use |
| Kasein 98% Technische Qualität | IC-7322 | PROVISIONAL | Historical - verify before use |
| SO-BE-50-427 | IC-9317 | SUPERSEDED | Historical - verify before use |
| HO-LO-534 PLC | IC-6290 | PROVISIONAL | Historical - verify before use |
| SO-CH-70-365 | IC-6240 | SUPERSEDED | Historical - verify before use |
| GL-SY-TE-803 | IC-8936 | PROVISIONAL | Historical - verify before use |
| GL-LO-935 | IC-9314 | SUPERSEDED | Historical - verify before use |
| SIG-95-APX-PWFS | IC-5550 | PROVISIONAL | Historical - verify before use |
| potassium sorbate premium | IC-6236 | PROVISIONAL | Historical - verify before use |
| catalyst supply | IC-7694 | SUPERSEDED | Historical - verify before use |
| wheat gluten premium | IC-5611 | REVIEW REQUIRED | Historical - verify before use |
| Maltodextrin DE25 | IC-6688 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid Pharmazeutisch rein | IC-6688 | PROVISIONAL | Historical - verify before use |
| SIG-18-LLP-8GUU | IC-8438 | DEPRECATED | Historical - verify before use |
| CI-AC-25-GR-A-669 | IC-7826 | REVIEW REQUIRED | Historical - verify before use |
| WI-B-10-442 | IC-7501 | REVIEW REQUIRED | Historical - verify before use |
| Sorbic Acid | IC-6577 | SUPERSEDED | Historical - verify before use |
| Vat Reduced US 19% | IC-9984 | SUPERSEDED | Historical - verify before use |
| SIG-64-QID-BCT3 | IC-5419 | SUPERSEDED | Historical - verify before use |
| Quantum Supply Co. | IC-7994 | DEPRECATED | Historical - verify before use |
| RE-ST-FO-GR-998 | IC-8121 | DEPRECATED | Historical - verify before use |
| pacific distribution | IC-5258 | REVIEW REQUIRED | Historical - verify before use |
| RA-OI-TE-584 | IC-7623 | SUPERSEDED | Historical - verify before use |
| CA-884 | IC-6281 | SUPERSEDED | Historical - verify before use |
| Sorbinsäure | IC-6722 | DEPRECATED | Historical - verify before use |
| PO-SO-480 | IC-9298 | DEPRECATED | Historical - verify before use |
| Sorbic Acid 98% | IC-6253 | PROVISIONAL | Historical - verify before use |
| ST-TR-786 International | IC-8428 | PROVISIONAL | Historical - verify before use |
| Rapsöl Lebensmittelrein | IC-9278 | DEPRECATED | Historical - verify before use |
| SIG-13-PHC-GSY7 | IC-5791 | REVIEW REQUIRED | Historical - verify before use |
| Pacific Industrien | IC-5734 | REVIEW REQUIRED | Historical - verify before use |
| DE-70-512 | IC-9580 | DEPRECATED | Historical - verify before use |
| Lactic Acid | IC-5423 | SUPERSEDED | Historical - verify before use |
| Coconut Oil 70% | IC-7699 | DEPRECATED | Historical - verify before use |
| Lactic Acid 70% Pharmazeutisch rein | IC-8300 | DEPRECATED | Historical - verify before use |
| Natriumchlorid 98% Standardqualität | IC-7932 | DEPRECATED | Historical - verify before use |
| SIG-50-PNF-Z2E8 | IC-5148 | SUPERSEDED | Historical - verify before use |
| SIG-13-BSD-DJSO International | IC-7891 | DEPRECATED | Historical - verify before use |
| nexus enterprise | IC-8800 | PROVISIONAL | Historical - verify before use |
| PI-PR-193 | IC-5781 | SUPERSEDED | Historical - verify before use |
| Dextrin 50% | IC-6920 | REVIEW REQUIRED | Historical - verify before use |
| sodium chloride 70% | IC-7755 | DEPRECATED | Historical - verify before use |
| Maltodextrin DE25 | IC-7834 | SUPERSEDED | Historical - verify before use |
| customs duty de 0% | IC-7669 | SUPERSEDED | Historical - verify before use |
| Citric Acid 99.5% | IC-5392 | DEPRECATED | Historical - verify before use |
| Prism Logistik | IC-6305 | DEPRECATED | Historical - verify before use |
| Rapsöl Pharmazeutisch rein | IC-8534 | SUPERSEDED | Historical - verify before use |
| Soy Isolate 50% Grade B | IC-9287 | PROVISIONAL | Historical - verify before use |
| stratos trading | IC-7468 | REVIEW REQUIRED | Historical - verify before use |
| SU-OI-GR-A-224 | IC-9895 | PROVISIONAL | Historical - verify before use |
| LA-AC-393 | IC-6390 | PROVISIONAL | Historical - verify before use |
| SIG-55-ICI-Z2GP GmbH | IC-5480 | PROVISIONAL | Historical - verify before use |
| Pea Protein Premium | IC-5552 | DEPRECATED | Historical - verify before use |
| pinnacle commodities BV | IC-9779 | SUPERSEDED | Historical - verify before use |
| Potassium Sorbate 50% Food Grade | IC-9763 | PROVISIONAL | Historical - verify before use |
| CO-OI-GR-A-370 | IC-7305 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat Lebensmittelrein | IC-7185 | SUPERSEDED | Historical - verify before use |
| ascorbic acid standard | IC-6831 | REVIEW REQUIRED | Historical - verify before use |
| SIG-68-QRN-LSY2 | IC-6639 | SUPERSEDED | Historical - verify before use |
| Natriumchlorid 99.5% | IC-5216 | DEPRECATED | Historical - verify before use |
| SIG-74-ZJN-KVHO | IC-6181 | PROVISIONAL | Historical - verify before use |
| Ascorbic Acid 99.5% Technische Qualität | IC-8450 | PROVISIONAL | Historical - verify before use |
| Dextrin Pharma Grade | IC-5061 | SUPERSEDED | Historical - verify before use |
| SIG-92-AXW-GPAG | IC-9203 | DEPRECATED | Historical - verify before use |
| premier partners Group | IC-5880 | PROVISIONAL | Historical - verify before use |
| Vertex Rohstoffe | IC-5647 | DEPRECATED | Historical - verify before use |
| Core Versorgung GmbH | IC-8867 | REVIEW REQUIRED | Historical - verify before use |
| Sonnenblumenöl 98% | IC-8761 | SUPERSEDED | Historical - verify before use |
| Zitronensäure Standardqualität | IC-5972 | REVIEW REQUIRED | Historical - verify before use |
| Stellar Rohstoffe | IC-5388 | SUPERSEDED | Historical - verify before use |
| sodium benzoate | IC-8254 | REVIEW REQUIRED | Historical - verify before use |
| meridian sourcing | IC-9039 | DEPRECATED | Historical - verify before use |
| LA-AC-TE-651 | IC-6457 | REVIEW REQUIRED | Historical - verify before use |
| lactic acid standard | IC-7013 | DEPRECATED | Historical - verify before use |
| lactic acid 98% premium | IC-7020 | SUPERSEDED | Historical - verify before use |
| Vertex Distribution | IC-8482 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid 50% | IC-6137 | SUPERSEDED | Historical - verify before use |
| Sorbic Acid 25% Grade B | IC-9154 | PROVISIONAL | Historical - verify before use |
| Palm Oil | IC-7937 | PROVISIONAL | Historical - verify before use |
| sodium benzoate 99.5% standard | IC-9491 | SUPERSEDED | Historical - verify before use |
| Quantum Trading | IC-5369 | PROVISIONAL | Historical - verify before use |
| CA-98-TE-238 | IC-8821 | REVIEW REQUIRED | Historical - verify before use |
| Continental Logistik | IC-5979 | SUPERSEDED | Historical - verify before use |
| VA-ST-D-7-855 | IC-8007 | PROVISIONAL | Historical - verify before use |
| DE-635 | IC-7827 | PROVISIONAL | Historical - verify before use |
| SIG-63-YJW-AP00 | IC-5106 | SUPERSEDED | Historical - verify before use |
| SIG-36-ZKX-4SE4 | IC-9806 | REVIEW REQUIRED | Historical - verify before use |
| SIG-52-LXJ-ZU4J | IC-6204 | SUPERSEDED | Historical - verify before use |
| Vat Reduced DE 20% | IC-8474 | PROVISIONAL | Historical - verify before use |
| Catalyst Logistics | IC-7547 | SUPERSEDED | Historical - verify before use |
| quantum logistics | IC-8987 | DEPRECATED | Historical - verify before use |
| Horizon Materials SAS | IC-8038 | PROVISIONAL | Historical - verify before use |
| Rapsöl 25% Lebensmittelrein | IC-9589 | DEPRECATED | Historical - verify before use |
| Isoglucose 98% | IC-8738 | SUPERSEDED | Historical - verify before use |
| SIG-80-WKN-N0SS | IC-6147 | SUPERSEDED | Historical - verify before use |
| Isoglucose | IC-6017 | DEPRECATED | Historical - verify before use |
| isoglucose 70% | IC-6497 | REVIEW REQUIRED | Historical - verify before use |
| ascorbic acid pharma grade | IC-7544 | DEPRECATED | Historical - verify before use |
| SIG-51-MQP-ZO0K | IC-9299 | PROVISIONAL | Historical - verify before use |
| Dextrose 25% | IC-7536 | PROVISIONAL | Historical - verify before use |
| FR-108 | IC-5059 | REVIEW REQUIRED | Historical - verify before use |
| Maltodextrin DE20 | IC-5100 | SUPERSEDED | Historical - verify before use |
| Cyclodextrin 98% Pharmazeutisch rein | IC-6556 | REVIEW REQUIRED | Historical - verify before use |
| DE-25-PR-846 | IC-6268 | DEPRECATED | Historical - verify before use |
| Isoglucose 70% | IC-8499 | SUPERSEDED | Historical - verify before use |
| sorbic acid 50% | IC-9446 | SUPERSEDED | Historical - verify before use |
| continental ingredients AG | IC-6900 | PROVISIONAL | Historical - verify before use |
| Global Materials | IC-6933 | SUPERSEDED | Historical - verify before use |
| ST-LO-927 | IC-6817 | PROVISIONAL | Historical - verify before use |
| SIG-67-YAJ-18K0 | IC-8714 | REVIEW REQUIRED | Historical - verify before use |
| Prism Ingredients | IC-9288 | SUPERSEDED | Historical - verify before use |
| VA-RE-C-19-810 | IC-7682 | REVIEW REQUIRED | Historical - verify before use |
| Continental Werkstoffe NV | IC-7023 | PROVISIONAL | Historical - verify before use |
| CO-MA-245 | IC-6333 | PROVISIONAL | Historical - verify before use |
| Cyclodextrin | IC-8325 | SUPERSEDED | Historical - verify before use |
| Nexus Ingredients SARL | IC-8290 | PROVISIONAL | Historical - verify before use |
| Isoglucose 70% | IC-5509 | SUPERSEDED | Historical - verify before use |
| SIG-89-RGS-FIRM Holdings | IC-6903 | PROVISIONAL | Historical - verify before use |
| Sodium Benzoate 25% Grade B | IC-8821 | REVIEW REQUIRED | Historical - verify before use |
| Soy Isolate 99.5% | IC-5681 | SUPERSEDED | Historical - verify before use |
| AS-AC-FO-GR-835 | IC-5833 | DEPRECATED | Historical - verify before use |
| withholding fr 10% | IC-6796 | DEPRECATED | Historical - verify before use |
| SIG-84-EIB-2MOT | IC-6244 | SUPERSEDED | Historical - verify before use |
| Central Manufacturing Holdings | IC-5009 | PROVISIONAL | Historical - verify before use |
| global distribution Corp. | IC-9010 | PROVISIONAL | Historical - verify before use |
| CO-OI-98-876 | IC-5425 | DEPRECATED | Historical - verify before use |
| SIG-83-MZM-HGMN GmbH | IC-9083 | PROVISIONAL | Historical - verify before use |
| SO-AC-98-579 | IC-6322 | PROVISIONAL | Historical - verify before use |
| Soy Isolate 99.5% | IC-5091 | DEPRECATED | Historical - verify before use |
| SIG-25-VPE-TOC1 | IC-5927 | SUPERSEDED | Historical - verify before use |
| SIG-41-WHZ-QDKE | IC-6510 | DEPRECATED | Historical - verify before use |
| SIG-15-PFO-2W85 | IC-5929 | DEPRECATED | Historical - verify before use |
| Apex Chemicals | IC-7499 | SUPERSEDED | Historical - verify before use |
| Weizenklebereiweiß Qualitätsstufe I | IC-7729 | SUPERSEDED | Historical - verify before use |
| vat reduced nl 0% | IC-5995 | DEPRECATED | Historical - verify before use |
| Natriumchlorid 98% | IC-9178 | PROVISIONAL | Historical - verify before use |
| central supply | IC-7140 | PROVISIONAL | Historical - verify before use |
| SIG-79-GKV-W8GA | IC-6818 | SUPERSEDED | Historical - verify before use |
| CE-PR-134 | IC-5057 | DEPRECATED | Historical - verify before use |
| fructose tech grade | IC-5792 | SUPERSEDED | Historical - verify before use |
| SIG-69-INT-Z1YQ | IC-5953 | REVIEW REQUIRED | Historical - verify before use |
| AT-LO-132 | IC-7516 | PROVISIONAL | Historical - verify before use |
| Wheat Gluten | IC-7677 | REVIEW REQUIRED | Historical - verify before use |
| SIG-53-HTQ-XVWB Group | IC-5547 | PROVISIONAL | Historical - verify before use |
| SIG-87-YFT-P51V | IC-5189 | DEPRECATED | Historical - verify before use |
| FR-99.5-PH-GR-378 | IC-5818 | PROVISIONAL | Historical - verify before use |
| pinnacle industries Corp. | IC-5718 | PROVISIONAL | Historical - verify before use |
| fructose 25% | IC-9939 | REVIEW REQUIRED | Historical - verify before use |
| Withholding BR 15% | IC-8217 | REVIEW REQUIRED | Historical - verify before use |
| SU-OI-TE-879 | IC-7573 | PROVISIONAL | Historical - verify before use |
| Sodium Chloride 70% Grade B | IC-5616 | SUPERSEDED | Historical - verify before use |
| Zitronensäure 70% Lebensmittelrein | IC-7410 | REVIEW REQUIRED | Historical - verify before use |
| Global Materials | IC-8114 | PROVISIONAL | Historical - verify before use |
| Resistente Stärke | IC-6673 | SUPERSEDED | Historical - verify before use |
| PO-SO-339 | IC-7640 | SUPERSEDED | Historical - verify before use |
| AS-AC-TE-342 | IC-5411 | REVIEW REQUIRED | Historical - verify before use |
| SIG-87-YFT-P51V | IC-5218 | DEPRECATED | Historical - verify before use |
| VA-ST-G-20-932 | IC-8145 | REVIEW REQUIRED | Historical - verify before use |
| Pea Protein 99.5% | IC-7524 | DEPRECATED | Historical - verify before use |
| SIG-68-ELC-6AVE | IC-5745 | PROVISIONAL | Historical - verify before use |
| PI-SU-CO-216 | IC-5023 | REVIEW REQUIRED | Historical - verify before use |
| SIG-29-BKQ-HXCX Group | IC-9821 | REVIEW REQUIRED | Historical - verify before use |
| Meridian Sourcing | IC-7915 | REVIEW REQUIRED | Historical - verify before use |
| Customs Duty DE 5% | IC-7265 | SUPERSEDED | Historical - verify before use |
| SIG-62-JTP-RUMX | IC-9556 | DEPRECATED | Historical - verify before use |
| Prism Manufacturing LLC | IC-9300 | REVIEW REQUIRED | Historical - verify before use |
| ascorbic acid food grade | IC-6127 | PROVISIONAL | Historical - verify before use |
| SO-AC-98-741 | IC-5558 | REVIEW REQUIRED | Historical - verify before use |
| SIG-10-PGH-BTUF | IC-9853 | REVIEW REQUIRED | Historical - verify before use |
| SIG-20-LIK-8TZV Ltd. | IC-7887 | DEPRECATED | Historical - verify before use |
| SIG-64-ILX-G2AZ PLC | IC-7278 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid Pharmazeutisch rein | IC-7585 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat | IC-9706 | DEPRECATED | Historical - verify before use |
| WH-GL-99.5-TE-628 | IC-5567 | SUPERSEDED | Historical - verify before use |
| QU-SU-CO-774 | IC-8371 | PROVISIONAL | Historical - verify before use |
| DE-TE-414 | IC-7070 | PROVISIONAL | Historical - verify before use |
| SIG-25-ROA-G6G0 | IC-7546 | DEPRECATED | Historical - verify before use |
| SIG-86-LPN-HCNV | IC-7708 | PROVISIONAL | Historical - verify before use |
| Atlas Ingredients Ltd. | IC-7381 | PROVISIONAL | Historical - verify before use |
| Horizon Partners Ltd. | IC-5150 | SUPERSEDED | Historical - verify before use |
| SIG-83-GEN-QNXZ | IC-7835 | SUPERSEDED | Historical - verify before use |
| Soja Isolate Standardqualität | IC-7902 | DEPRECATED | Historical - verify before use |
| pacific sourcing | IC-5366 | PROVISIONAL | Historical - verify before use |
| Calcium Carbonate 50% Grade A | IC-5947 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat 25% Qualitätsstufe II | IC-7624 | REVIEW REQUIRED | Historical - verify before use |
| VA-ST-N-20-275 | IC-9427 | PROVISIONAL | Historical - verify before use |
| Citric Acid 99.5% Pharma Grade | IC-9434 | DEPRECATED | Historical - verify before use |
| Natriumchlorid | IC-9515 | REVIEW REQUIRED | Historical - verify before use |
| Sonnenblumenöl 98% | IC-6173 | REVIEW REQUIRED | Historical - verify before use |
| SIG-95-EES-2FE9 | IC-9331 | SUPERSEDED | Historical - verify before use |
| Sodium Benzoate | IC-6085 | REVIEW REQUIRED | Historical - verify before use |
| quantum enterprise BV | IC-5279 | REVIEW REQUIRED | Historical - verify before use |
| Zitronensäure Qualitätsstufe I | IC-8617 | DEPRECATED | Historical - verify before use |


#### 4.3.4 Excluded Assignments

Deprecated code assignments (superseded by newer records):

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-6178-F | Out of scope per business decision | Manual review scheduled |
| NOISE-5215-E | Out of scope per business decision | Escalated to data steward |
| NOISE-3429-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3929-C | Data quality insufficient | Manual review scheduled |
| NOISE-9510-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-5963-B | Duplicate source record | Business owner notified |
| NOISE-5455-E | Pending validation | Escalated to data steward |
| NOISE-2163-H | Pending validation | Escalated to data steward |
| NOISE-1749-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-1334-C | Data quality insufficient | Business owner notified |
| NOISE-9846-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6267-H | Pending validation | Deferred to Phase 2 |
| NOISE-8801-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2528-B | Duplicate source record | Escalated to data steward |
| NOISE-5634-H | Missing required attributes | Business owner notified |
| NOISE-5214-A | Out of scope per business decision | Manual review scheduled |
| NOISE-1947-D | Out of scope per business decision | Escalated to data steward |
| NOISE-7646-F | Data quality insufficient | Manual review scheduled |
| NOISE-6923-D | Pending validation | Deferred to Phase 2 |
| NOISE-7847-F | Data quality insufficient | Escalated to data steward |
| NOISE-5178-D | Missing required attributes | Manual review scheduled |
| NOISE-2834-A | Missing required attributes | Business owner notified |
| NOISE-9336-E | Duplicate source record | Escalated to data steward |
| NOISE-9444-C | Out of scope per business decision | Manual review scheduled |
| NOISE-7490-F | Pending validation | Manual review scheduled |
| NOISE-9362-A | Missing required attributes | Escalated to data steward |
| NOISE-7773-C | Data quality insufficient | Manual review scheduled |
| NOISE-2252-E | Pending validation | Deferred to Phase 2 |
| NOISE-7430-B | Missing required attributes | Business owner notified |
| NOISE-5681-G | Out of scope per business decision | Manual review scheduled |
| NOISE-8367-C | Pending validation | Deferred to Phase 2 |
| NOISE-3038-D | Missing required attributes | Manual review scheduled |
| NOISE-7009-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-1925-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-2486-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-4402-A | Data quality insufficient | Escalated to data steward |
| NOISE-2436-A | Missing required attributes | Manual review scheduled |
| NOISE-6442-H | Missing required attributes | Manual review scheduled |
| NOISE-3613-F | Duplicate source record | Manual review scheduled |
| NOISE-5688-C | Missing required attributes | Manual review scheduled |
| NOISE-8515-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-1703-C | Out of scope per business decision | Manual review scheduled |
| NOISE-5861-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-3486-E | Pending validation | Escalated to data steward |
| NOISE-2753-H | Data quality insufficient | Business owner notified |
| NOISE-6333-B | Pending validation | Business owner notified |
| NOISE-9934-G | Out of scope per business decision | Escalated to data steward |
| NOISE-2693-D | Pending validation | Manual review scheduled |
| NOISE-3577-H | Out of scope per business decision | Manual review scheduled |
| NOISE-7018-D | Duplicate source record | Business owner notified |
| NOISE-8022-H | Data quality insufficient | Manual review scheduled |
| NOISE-4053-A | Missing required attributes | Business owner notified |
| NOISE-7553-G | Out of scope per business decision | Business owner notified |
| NOISE-8643-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1516-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-5348-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6639-A | Out of scope per business decision | Escalated to data steward |
| NOISE-1450-F | Duplicate source record | Business owner notified |
| NOISE-6472-A | Data quality insufficient | Manual review scheduled |
| NOISE-5564-C | Data quality insufficient | Manual review scheduled |
| NOISE-3576-H | Out of scope per business decision | Business owner notified |
| NOISE-7334-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-5138-A | Pending validation | Business owner notified |
| NOISE-8888-A | Data quality insufficient | Escalated to data steward |
| NOISE-6076-D | Duplicate source record | Business owner notified |
| NOISE-7521-E | Pending validation | Deferred to Phase 2 |
| NOISE-1285-B | Duplicate source record | Escalated to data steward |
| NOISE-2617-G | Pending validation | Business owner notified |
| NOISE-3681-B | Missing required attributes | Escalated to data steward |
| NOISE-4809-B | Missing required attributes | Escalated to data steward |
| NOISE-2380-H | Missing required attributes | Business owner notified |
| NOISE-5463-E | Missing required attributes | Business owner notified |
| NOISE-8832-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-7622-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-3230-D | Out of scope per business decision | Manual review scheduled |
| NOISE-5342-E | Duplicate source record | Business owner notified |
| NOISE-7356-H | Missing required attributes | Manual review scheduled |
| NOISE-6189-A | Pending validation | Manual review scheduled |
| NOISE-6820-G | Out of scope per business decision | Escalated to data steward |
| NOISE-5437-D | Duplicate source record | Manual review scheduled |
| NOISE-7093-A | Duplicate source record | Escalated to data steward |
| NOISE-2540-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-9858-A | Pending validation | Escalated to data steward |
| NOISE-4896-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7831-A | Out of scope per business decision | Escalated to data steward |
| NOISE-8465-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9407-A | Out of scope per business decision | Manual review scheduled |
| NOISE-2511-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-3623-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4011-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3899-G | Missing required attributes | Escalated to data steward |
| NOISE-9932-D | Out of scope per business decision | Escalated to data steward |
| NOISE-7605-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6603-G | Data quality insufficient | Business owner notified |
| NOISE-2195-F | Out of scope per business decision | Escalated to data steward |
| NOISE-2900-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3426-C | Missing required attributes | Business owner notified |
| NOISE-2133-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-9011-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-1397-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-9334-B | Missing required attributes | Manual review scheduled |
| NOISE-8278-F | Out of scope per business decision | Business owner notified |
| NOISE-7212-A | Data quality insufficient | Manual review scheduled |
| NOISE-4958-B | Duplicate source record | Escalated to data steward |
| NOISE-3512-H | Pending validation | Deferred to Phase 2 |
| NOISE-6423-C | Out of scope per business decision | Business owner notified |
| NOISE-1541-B | Duplicate source record | Business owner notified |
| NOISE-1867-A | Data quality insufficient | Manual review scheduled |
| NOISE-4667-C | Duplicate source record | Business owner notified |
| NOISE-4532-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-1961-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-6094-B | Missing required attributes | Escalated to data steward |
| NOISE-1845-A | Duplicate source record | Manual review scheduled |
| NOISE-4079-A | Missing required attributes | Business owner notified |
| NOISE-4430-H | Out of scope per business decision | Manual review scheduled |
| NOISE-4898-C | Data quality insufficient | Manual review scheduled |
| NOISE-3401-E | Duplicate source record | Escalated to data steward |
| NOISE-3442-H | Missing required attributes | Business owner notified |
| NOISE-5073-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1997-B | Out of scope per business decision | Business owner notified |
| NOISE-4624-H | Duplicate source record | Deferred to Phase 2 |
| NOISE-5005-G | Missing required attributes | Manual review scheduled |
| NOISE-8235-F | Pending validation | Manual review scheduled |
| NOISE-9675-G | Out of scope per business decision | Escalated to data steward |
| NOISE-7531-D | Out of scope per business decision | Escalated to data steward |
| NOISE-5154-F | Data quality insufficient | Business owner notified |
| NOISE-4534-B | Missing required attributes | Business owner notified |
| NOISE-4649-D | Duplicate source record | Business owner notified |
| NOISE-9978-A | Pending validation | Deferred to Phase 2 |
| NOISE-8444-E | Missing required attributes | Business owner notified |
| NOISE-9453-G | Pending validation | Deferred to Phase 2 |
| NOISE-5739-E | Out of scope per business decision | Business owner notified |
| NOISE-5140-B | Out of scope per business decision | Manual review scheduled |
| NOISE-3306-E | Data quality insufficient | Business owner notified |
| NOISE-2155-F | Pending validation | Deferred to Phase 2 |
| NOISE-3248-B | Data quality insufficient | Business owner notified |
| NOISE-2389-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-5776-C | Data quality insufficient | Manual review scheduled |
| NOISE-1739-G | Missing required attributes | Escalated to data steward |
| NOISE-3949-E | Out of scope per business decision | Business owner notified |
| NOISE-2934-D | Missing required attributes | Manual review scheduled |
| NOISE-5252-E | Duplicate source record | Manual review scheduled |
| NOISE-8555-E | Data quality insufficient | Escalated to data steward |
| NOISE-8393-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-4202-F | Missing required attributes | Manual review scheduled |
| NOISE-1174-B | Out of scope per business decision | Escalated to data steward |
| NOISE-9213-G | Pending validation | Manual review scheduled |
| NOISE-5023-F | Out of scope per business decision | Manual review scheduled |
| NOISE-4572-H | Duplicate source record | Escalated to data steward |
| NOISE-2809-G | Out of scope per business decision | Business owner notified |
| NOISE-5246-E | Duplicate source record | Escalated to data steward |
| NOISE-5420-F | Missing required attributes | Manual review scheduled |
| NOISE-5646-C | Duplicate source record | Business owner notified |
| NOISE-9218-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5907-B | Missing required attributes | Manual review scheduled |
| NOISE-5138-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-5527-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9761-E | Out of scope per business decision | Business owner notified |
| NOISE-2645-B | Data quality insufficient | Manual review scheduled |
| NOISE-8151-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4483-E | Pending validation | Deferred to Phase 2 |
| NOISE-9291-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-6365-G | Data quality insufficient | Manual review scheduled |
| NOISE-3443-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-6462-H | Pending validation | Manual review scheduled |
| NOISE-6063-D | Data quality insufficient | Escalated to data steward |
| NOISE-2389-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-4871-A | Duplicate source record | Escalated to data steward |
| NOISE-5144-F | Duplicate source record | Business owner notified |
| NOISE-1187-D | Pending validation | Manual review scheduled |
| NOISE-5187-E | Out of scope per business decision | Escalated to data steward |
| NOISE-2743-F | Out of scope per business decision | Manual review scheduled |
| NOISE-7374-A | Pending validation | Escalated to data steward |
| NOISE-2259-A | Data quality insufficient | Manual review scheduled |
| NOISE-6645-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6349-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-6782-E | Duplicate source record | Business owner notified |
| NOISE-9582-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-5890-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2814-E | Data quality insufficient | Manual review scheduled |
| NOISE-4633-G | Duplicate source record | Manual review scheduled |
| NOISE-6066-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-4449-A | Pending validation | Manual review scheduled |
| NOISE-6545-H | Duplicate source record | Business owner notified |
| NOISE-2471-A | Duplicate source record | Business owner notified |
| NOISE-2068-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-6147-G | Data quality insufficient | Business owner notified |
| NOISE-8666-H | Pending validation | Deferred to Phase 2 |
| NOISE-3696-G | Pending validation | Escalated to data steward |
| NOISE-1366-C | Pending validation | Escalated to data steward |
| NOISE-1619-C | Pending validation | Deferred to Phase 2 |
| NOISE-9387-B | Pending validation | Deferred to Phase 2 |
| NOISE-8794-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8506-G | Pending validation | Escalated to data steward |
| NOISE-7979-F | Missing required attributes | Manual review scheduled |
| NOISE-9263-E | Pending validation | Manual review scheduled |
| NOISE-8186-G | Out of scope per business decision | Business owner notified |
| NOISE-7116-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-8718-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2115-G | Duplicate source record | Business owner notified |
| NOISE-1268-F | Missing required attributes | Business owner notified |
| NOISE-9585-G | Pending validation | Business owner notified |
| NOISE-8949-F | Missing required attributes | Business owner notified |
| NOISE-4458-F | Duplicate source record | Business owner notified |
| NOISE-7252-D | Out of scope per business decision | Escalated to data steward |
| NOISE-6044-B | Missing required attributes | Manual review scheduled |
| NOISE-3730-D | Missing required attributes | Escalated to data steward |
| NOISE-3742-E | Missing required attributes | Manual review scheduled |
| NOISE-5729-H | Missing required attributes | Business owner notified |
| NOISE-5496-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5049-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2390-D | Data quality insufficient | Manual review scheduled |
| NOISE-6651-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7403-C | Out of scope per business decision | Manual review scheduled |
| NOISE-8873-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-6712-D | Duplicate source record | Escalated to data steward |
| NOISE-1150-B | Duplicate source record | Manual review scheduled |
| NOISE-6702-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6117-H | Duplicate source record | Business owner notified |
| NOISE-9199-B | Out of scope per business decision | Escalated to data steward |
| NOISE-3042-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-3396-H | Duplicate source record | Manual review scheduled |
| NOISE-4377-H | Pending validation | Manual review scheduled |
| NOISE-2289-F | Data quality insufficient | Manual review scheduled |
| NOISE-7393-C | Out of scope per business decision | Escalated to data steward |
| NOISE-1564-D | Missing required attributes | Manual review scheduled |
| NOISE-9666-C | Missing required attributes | Manual review scheduled |
| NOISE-2205-D | Pending validation | Business owner notified |
| NOISE-8117-F | Duplicate source record | Manual review scheduled |
| NOISE-1073-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-3425-B | Data quality insufficient | Escalated to data steward |
| NOISE-4906-B | Data quality insufficient | Business owner notified |
| NOISE-5126-B | Pending validation | Deferred to Phase 2 |
| NOISE-4360-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-6518-E | Out of scope per business decision | Escalated to data steward |
| NOISE-3676-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-9792-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-7908-D | Pending validation | Business owner notified |
| NOISE-1177-E | Pending validation | Escalated to data steward |
| NOISE-6589-A | Pending validation | Deferred to Phase 2 |
| NOISE-1951-F | Missing required attributes | Manual review scheduled |
| NOISE-3854-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-3688-A | Pending validation | Business owner notified |
| NOISE-1513-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-4953-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-8947-E | Out of scope per business decision | Escalated to data steward |
| NOISE-8283-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-2076-B | Missing required attributes | Business owner notified |
| NOISE-6272-H | Duplicate source record | Manual review scheduled |
| NOISE-7326-H | Missing required attributes | Business owner notified |
| NOISE-9760-C | Pending validation | Business owner notified |
| NOISE-2466-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6701-H | Missing required attributes | Business owner notified |
| NOISE-5054-H | Pending validation | Escalated to data steward |
| NOISE-2981-E | Missing required attributes | Escalated to data steward |
| NOISE-2218-C | Data quality insufficient | Escalated to data steward |
| NOISE-4620-H | Duplicate source record | Business owner notified |
| NOISE-4118-D | Duplicate source record | Escalated to data steward |
| NOISE-4630-F | Missing required attributes | Escalated to data steward |
| NOISE-4560-C | Data quality insufficient | Manual review scheduled |
| NOISE-3096-D | Out of scope per business decision | Business owner notified |
| NOISE-3438-D | Out of scope per business decision | Escalated to data steward |
| NOISE-7144-F | Data quality insufficient | Manual review scheduled |
| NOISE-4467-B | Pending validation | Escalated to data steward |
| NOISE-7160-G | Out of scope per business decision | Business owner notified |
| NOISE-8685-C | Pending validation | Deferred to Phase 2 |
| NOISE-9288-F | Data quality insufficient | Manual review scheduled |
| NOISE-7202-H | Out of scope per business decision | Business owner notified |
| NOISE-2172-F | Data quality insufficient | Business owner notified |
| NOISE-5989-B | Data quality insufficient | Business owner notified |
| NOISE-7081-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-4218-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5191-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-6433-C | Duplicate source record | Business owner notified |
| NOISE-8568-G | Missing required attributes | Escalated to data steward |
| NOISE-2467-C | Out of scope per business decision | Escalated to data steward |
| NOISE-1989-D | Pending validation | Deferred to Phase 2 |
| NOISE-2162-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2818-C | Missing required attributes | Manual review scheduled |
| NOISE-5406-G | Duplicate source record | Manual review scheduled |
| NOISE-2215-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8044-H | Out of scope per business decision | Manual review scheduled |
| NOISE-9922-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-4808-E | Pending validation | Business owner notified |
| NOISE-2959-A | Missing required attributes | Manual review scheduled |
| NOISE-9290-F | Duplicate source record | Business owner notified |
| NOISE-1714-E | Data quality insufficient | Escalated to data steward |
| NOISE-5778-G | Pending validation | Deferred to Phase 2 |
| NOISE-8158-H | Data quality insufficient | Escalated to data steward |
| NOISE-7926-H | Duplicate source record | Escalated to data steward |
| NOISE-9433-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1251-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1994-A | Pending validation | Escalated to data steward |
| NOISE-1409-C | Data quality insufficient | Business owner notified |
| NOISE-4190-A | Data quality insufficient | Escalated to data steward |
| NOISE-9133-H | Duplicate source record | Manual review scheduled |
| NOISE-5801-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-2420-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9258-C | Duplicate source record | Escalated to data steward |
| NOISE-8889-E | Pending validation | Deferred to Phase 2 |
| NOISE-3959-G | Pending validation | Escalated to data steward |
| NOISE-8288-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7665-H | Missing required attributes | Business owner notified |
| NOISE-2696-B | Missing required attributes | Escalated to data steward |
| NOISE-5863-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7633-C | Out of scope per business decision | Manual review scheduled |
| NOISE-2977-D | Duplicate source record | Escalated to data steward |
| NOISE-1501-G | Out of scope per business decision | Escalated to data steward |
| NOISE-4812-F | Duplicate source record | Escalated to data steward |
| NOISE-7956-H | Missing required attributes | Manual review scheduled |
| NOISE-6414-E | Out of scope per business decision | Business owner notified |
| NOISE-5012-E | Out of scope per business decision | Escalated to data steward |
| NOISE-2098-B | Out of scope per business decision | Manual review scheduled |
| NOISE-4298-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-2150-C | Duplicate source record | Escalated to data steward |
| NOISE-8967-D | Missing required attributes | Business owner notified |
| NOISE-1818-G | Duplicate source record | Manual review scheduled |
| NOISE-7563-C | Pending validation | Business owner notified |
| NOISE-8731-H | Data quality insufficient | Escalated to data steward |
| NOISE-7775-B | Out of scope per business decision | Business owner notified |
| NOISE-5755-H | Data quality insufficient | Escalated to data steward |


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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230627_000000`
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
| Project Lead | Maria Garcia (Supply Chain) | maria@company.com | +1-555-0101 |
| Technical Lead | David Kim (Project Management) | david@company.com | +1-555-0102 |
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
