# Migration Runbook: System Migration: SYSTEM_UPGRADE_2023

**Document ID**: RB-SYSTEM_UPGRADE_2023-9815
**Version**: 2.0
**Last Updated**: 2023-03-23
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the System Migration: SYSTEM_UPGRADE_2023 project.
The migration involves transitioning master data and transactional records from SOURCE
to TARGET while maintaining data integrity and business continuity.

**Project Timeline**: 2023-01-20 to 2023-06-10
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
| Total entities assessed | 1467 | Completed |
| Codes assigned | 1085 | Staged |
| Excluded from scope | 325 | Documented |
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

| Source Entity (SOURCE) | Internal Code | Assignment Date | Department |
|--------------------------------|---------------|-----------------|------------|
| SIG-65-EFS-5P03 | TC-8277 | 2023-05-05 | Compliance |
| Horizon Industrien GmbH | IC-8281 | 2021-07-12 | Operations |
| SO-CH-752 | BC-8300 | 2021-08-23 | Compliance |
| SIG-37-ZOD-1VME | TC-8311 | 2021-01-13 | Supply Chain |
| DE-GR-A-512 | TC-8313 | 2021-11-16 | Operations |
| Prism Industrien Holdings | IC-8322 | 2021-11-02 | Data Governance |
| SIG-78-WDE-NNV9 | BC-8329 | 2023-11-11 | Operations |
| Pea Protein 99.5% | IC-8349 | 2023-05-19 | Product Management |
| FR-PR-346 | BC-8360 | 2021-06-19 | IT Infrastructure |
| Nexus Materials | TC-8367 | 2021-06-22 | Operations |
| Meridian Versorgung GmbH | IC-8372 | 2024-01-17 | Finance |
| Nexus Sourcing | IC-8382 | 2024-11-23 | Data Governance |
| SIG-68-HOK-ETCC | TC-8385 | 2024-10-12 | Compliance |
| Fructose | BC-8389 | 2023-04-16 | Product Management |
| VE-IN-631 Ltd. | TC-8399 | 2024-06-11 | Operations |
| Rapsöl Qualitätsstufe I | IC-8422 | 2024-12-12 | Data Governance |
| Maltodextrin DE30 Standard | IC-8424 | 2022-01-14 | Product Management |
| Vanguard Logistik SA | BC-8451 | 2023-12-15 | Supply Chain |
| Isoglucose Qualitätsstufe II | IC-8453 | 2023-10-23 | IT Infrastructure |
| core supply | TC-8526 | 2023-05-24 | Product Management |
| VA-IN-429 | BC-8528 | 2024-08-18 | IT Infrastructure |
| CO-OI-50-PH-GR-568 | BC-8543 | 2023-02-11 | Compliance |
| elite logistics | TC-8555 | 2023-03-07 | Product Management |
| ascorbic acid | TC-8568 | 2022-04-23 | Product Management |
| Meridian Enterprise | IC-8580 | 2023-03-08 | Finance |
| pinnacle distribution Ltd. | BC-8581 | 2021-03-16 | IT Infrastructure |
| CU-DU-G-0-770 | TC-8587 | 2022-11-16 | Compliance |
| Zenith Versorgung GmbH | IC-8594 | 2024-07-21 | Supply Chain |
| sodium chloride 98% pharma grade | TC-8630 | 2023-04-22 | Finance |
| Wheat Gluten 50% | TC-8641 | 2021-01-07 | Compliance |
| CY-577 | IC-8646 | 2021-08-18 | IT Infrastructure |
| Ascorbic Acid 98% | BC-8666 | 2024-05-08 | Data Governance |
| pea protein standard | TC-8670 | 2024-08-20 | Operations |
| Dextrin 50% | IC-8674 | 2024-02-26 | IT Infrastructure |
| Central Commodities Ltd. | BC-8688 | 2023-11-12 | Operations |
| SIG-17-OVA-CCDM | BC-8693 | 2021-02-23 | Compliance |
| SIG-39-EWA-Q37M | BC-8704 | 2023-10-13 | Supply Chain |
| palm oil 50% | BC-8706 | 2023-02-19 | Operations |
| sodium benzoate premium | TC-8716 | 2023-06-07 | IT Infrastructure |
| Isoglucose 50% Lebensmittelrein | IC-8730 | 2022-05-21 | Data Governance |
| pacific materials GmbH | IC-8737 | 2022-01-28 | Product Management |
| Dextrin Technical | IC-8745 | 2023-02-26 | Supply Chain |
| Ascorbic Acid | BC-8756 | 2023-03-12 | Product Management |
| Vat Standardqualität GB 15% | BC-8765 | 2024-05-26 | Supply Chain |
| atlantic materials | BC-8770 | 2021-05-18 | Supply Chain |
| Fructose | IC-8775 | 2021-02-25 | Supply Chain |
| SIG-42-HBL-L3KU International | BC-8790 | 2022-04-14 | Product Management |
| sodium chloride 70% | IC-8799 | 2022-09-16 | Compliance |
| Pea Protein | IC-8831 | 2023-08-02 | Finance |
| Atlantic Commodities | BC-8847 | 2022-10-01 | IT Infrastructure |
| CA-PH-GR-524 | IC-8854 | 2022-12-02 | Product Management |
| SIG-71-CWF-DGP5 | BC-8858 | 2023-06-15 | Compliance |
| MA-DE-146 | TC-8872 | 2023-05-17 | Supply Chain |
| resistant starch food grade | IC-8880 | 2022-12-03 | Supply Chain |
| CO-OI-25-ST-613 | IC-8890 | 2022-02-11 | Product Management |
| SIG-51-KQC-QY9M | IC-8892 | 2022-06-17 | Compliance |
| PA-MA-412 GmbH | TC-8907 | 2021-08-12 | Supply Chain |
| Sodium Benzoate Grade A | BC-8908 | 2021-11-03 | IT Infrastructure |
| PR-CO-481 International | TC-8931 | 2022-11-08 | Data Governance |
| prism industries International | BC-8937 | 2024-03-26 | Product Management |
| cyclodextrin premium | TC-8938 | 2022-09-23 | Operations |
| SIG-54-ZFB-4REP Inc. | TC-8978 | 2023-09-16 | IT Infrastructure |
| SIG-83-BZY-VHAE | IC-9020 | 2023-05-14 | Operations |
| Palmfett | TC-9033 | 2022-04-05 | Compliance |
| SIG-65-BMI-KAWJ Holdings | TC-9037 | 2023-09-20 | Product Management |
| SIG-50-QXM-GFI4 | BC-9043 | 2024-06-27 | Supply Chain |
| Prism Versorgung GmbH | IC-9045 | 2024-10-10 | Operations |
| Sorbinsäure | TC-9049 | 2024-11-27 | Finance |
| sodium benzoate 50% | TC-9052 | 2022-03-15 | Operations |
| ST-PA-227 PLC | BC-9054 | 2021-05-19 | Operations |
| AS-AC-GR-B-855 | IC-9059 | 2022-04-04 | Supply Chain |
| SIG-44-HLB-IC48 SARL | BC-9086 | 2023-12-01 | Data Governance |
| Rapeseed Oil | TC-9089 | 2023-08-04 | Data Governance |
| Potassium Sorbate 50% Technical | IC-9095 | 2023-02-18 | Compliance |
| CY-892 | TC-9097 | 2021-12-15 | Compliance |
| SIG-39-WTU-81JC | TC-9111 | 2022-05-20 | Finance |
| Core Logistics | BC-9126 | 2022-11-19 | Supply Chain |
| SIG-26-HEJ-USUB Group | BC-9127 | 2021-02-13 | Data Governance |
| SIG-47-QLD-IL46 | IC-9128 | 2022-06-12 | Operations |
| Maltodextrin-Pulver DE15 | BC-9153 | 2023-08-28 | Operations |
| Pinnacle Sourcing | IC-9157 | 2023-01-07 | Data Governance |
| potassium sorbate | TC-9160 | 2022-11-26 | Product Management |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | BC-9180 | 2021-01-14 | IT Infrastructure |
| Sorbinsäure Premiumqualität | BC-9186 | 2024-07-23 | Product Management |
| Soja Isolate 25% Technische Qualität | BC-9190 | 2021-07-03 | Data Governance |
| glucose syrup 25% | IC-9193 | 2023-10-24 | Compliance |
| Traubenzucker Qualitätsstufe I | BC-9195 | 2021-04-10 | Data Governance |
| WH-GL-GR-B-129 | IC-9201 | 2024-10-23 | Data Governance |
| Soja Isolate 98% Premiumqualität | TC-9206 | 2021-07-08 | Product Management |
| NO-MA-529 | TC-9217 | 2023-08-10 | IT Infrastructure |
| SIG-86-JBA-HCDI | TC-9239 | 2022-06-16 | Supply Chain |
| Horizon Ingredients BV | IC-9245 | 2022-01-14 | Data Governance |
| Atlantic Industrien International | TC-9247 | 2023-01-21 | Compliance |
| BA-IN-585 SARL | IC-9248 | 2022-04-26 | Supply Chain |
| Atlantic Trading BV | IC-9254 | 2021-11-06 | Supply Chain |
| Isoglucose Lebensmittelrein | IC-9255 | 2021-05-18 | Finance |
| PE-PR-163 | BC-9259 | 2022-11-22 | Supply Chain |
| SIG-27-KMU-WPWH GmbH | IC-9263 | 2024-06-06 | Finance |
| sodium benzoate 98% | BC-9264 | 2024-10-11 | Operations |
| Stratos Commodities International | IC-9281 | 2022-06-03 | Finance |
| Rapsöl 70% Premiumqualität | IC-9308 | 2024-12-24 | Data Governance |
| SIG-42-AYY-K71K | BC-9335 | 2021-09-07 | Product Management |
| Premier Logistics | IC-9336 | 2024-01-28 | Finance |
| baltic solutions Group | BC-9359 | 2024-04-08 | Operations |
| SO-CH-99.5-GR-A-206 | IC-9369 | 2022-11-20 | Supply Chain |
| IS-FO-GR-555 | BC-9371 | 2022-04-10 | Operations |
| Casein Standard | TC-9396 | 2022-10-08 | IT Infrastructure |
| SIG-45-GXT-XIBF | IC-9398 | 2021-07-17 | Compliance |
| Atlantic Manufacturing | IC-9401 | 2021-02-15 | Data Governance |
| ascorbic acid | IC-9409 | 2022-04-12 | Operations |
| SIG-47-YTF-UPMT | TC-9424 | 2024-10-02 | Product Management |
| sodium chloride 99.5% premium | BC-9431 | 2021-03-26 | Product Management |
| Rapsöl Lebensmittelrein | IC-9433 | 2022-06-22 | Compliance |
| Dextrose 70% Grade A | IC-9437 | 2024-12-17 | Operations |
| SIG-93-FDC-Q685 | TC-9458 | 2021-06-07 | Operations |
| SIG-86-QTB-N3VO International | TC-9508 | 2024-08-12 | Finance |
| Prism Materials Ltd. | BC-9511 | 2021-03-07 | IT Infrastructure |
| zenith logistics | IC-9514 | 2024-06-12 | Finance |
| RE-ST-PR-679 | BC-9516 | 2023-05-05 | Compliance |
| Vat Standard NL 19% | BC-9530 | 2021-12-10 | Finance |
| Atlantic Chemicals SAS | BC-9542 | 2023-11-12 | Supply Chain |
| SIG-27-GRI-K7JV | TC-9556 | 2021-09-19 | Product Management |
| Ascorbic Acid Premiumqualität | TC-9561 | 2024-08-01 | Data Governance |
| PI-LO-946 | IC-9572 | 2022-07-12 | Operations |
| AT-CH-905 Holdings | BC-9604 | 2021-03-14 | Supply Chain |
| SIG-12-JLN-YFH3 | TC-9609 | 2022-06-21 | Operations |
| CO-MA-993 Corp. | TC-9612 | 2024-03-12 | Compliance |
| RE-ST-463 | TC-9616 | 2022-03-14 | Product Management |
| Isoglucose | BC-9622 | 2023-02-09 | Supply Chain |
| PR-CH-121 KG | IC-9657 | 2022-09-21 | Compliance |
| Central Sourcing | BC-9667 | 2024-09-24 | Finance |
| meridian logistics | IC-9670 | 2022-11-05 | Product Management |
| Citric Acid 25% Technical | TC-9677 | 2022-08-07 | Product Management |
| PA-MA-324 | IC-9686 | 2022-08-14 | Product Management |
| AP-SU-CO-755 | BC-9691 | 2024-12-16 | Data Governance |
| Elite Sourcing | TC-9699 | 2024-04-02 | Compliance |
| Vat Reduced BR 19% | IC-9704 | 2022-03-28 | Data Governance |
| Sunflower Oil 50% Pharma Grade | BC-9715 | 2021-12-18 | Supply Chain |
| atlantic ingredients | TC-9738 | 2022-12-24 | Product Management |
| SIG-57-YOY-F7N2 | IC-9751 | 2024-11-19 | Product Management |
| Sodium Benzoate 99.5% Technical | BC-9754 | 2024-04-14 | Compliance |
| CO-MA-295 | IC-9755 | 2023-11-02 | Product Management |
| Zitronensäure Qualitätsstufe I | IC-9757 | 2022-04-22 | Product Management |
| SIG-23-LAS-L2MX Holdings | BC-9760 | 2023-10-26 | Product Management |
| dextrin | TC-9768 | 2023-11-15 | Product Management |
| EX-U-7-320 | IC-9771 | 2023-09-18 | IT Infrastructure |
| Fructose Technical | TC-9834 | 2022-09-25 | Compliance |
| calcium carbonate | BC-9842 | 2021-06-14 | IT Infrastructure |
| Glucose Syrup Technical | TC-9854 | 2023-02-01 | Finance |
| SIG-23-BLM-EZKX | TC-9856 | 2024-03-15 | IT Infrastructure |
| Dextrin Technical | BC-9859 | 2021-09-16 | Supply Chain |
| sorbic acid 98% | BC-9872 | 2024-05-12 | Operations |
| Premier Logistics | IC-9902 | 2022-08-27 | IT Infrastructure |
| sodium benzoate 98% | IC-9933 | 2021-02-11 | Finance |
| VE-SO-701 | IC-9937 | 2022-09-04 | Compliance |
| SIG-36-ZWC-F2K1 | TC-9968 | 2023-07-27 | Finance |
| SIG-61-IQH-EKWH | TC-9978 | 2023-03-01 | Compliance |
| Zitronensäure | IC-9991 | 2024-09-18 | Supply Chain |
| Maltodextrin-Pulver DE10 | IC-9999 | 2023-07-18 | IT Infrastructure |
| sodium chloride tech grade | BC-10005 | 2023-11-17 | IT Infrastructure |
| Isoglucose | BC-10011 | 2022-12-23 | IT Infrastructure |
| Weizenklebereiweiß Lebensmittelrein | BC-10023 | 2022-08-13 | Compliance |
| wheat gluten pharma grade | IC-10035 | 2023-10-20 | Compliance |
| baltic processing | TC-10055 | 2023-08-14 | Compliance |
| RA-OI-TE-584 | IC-10071 | 2021-06-22 | Supply Chain |
| customs duty fr 7% | TC-10079 | 2021-03-15 | Supply Chain |
| SIG-28-SXX-AKUN | IC-10102 | 2024-12-05 | Supply Chain |
| AT-SU-CO-755 | IC-10113 | 2021-03-07 | Operations |
| Horizon Partners Ltd. | TC-10115 | 2023-04-11 | Product Management |
| Vat Standard GB 19% | IC-10140 | 2021-08-05 | Supply Chain |
| fructose standard | BC-10145 | 2022-04-22 | IT Infrastructure |
| Dextrin | BC-10147 | 2022-06-19 | Finance |
| Nexus Partners GmbH | TC-10173 | 2024-08-12 | Product Management |
| RE-ST-GR-B-598 | IC-10178 | 2024-08-26 | Supply Chain |
| Vertex Vertrieb Holdings | BC-10218 | 2022-09-23 | Data Governance |
| Sodium Chloride 25% Food Grade | BC-10224 | 2024-07-24 | Data Governance |
| LA-AC-TE-651 | IC-10238 | 2024-12-15 | IT Infrastructure |
| Natriumbenzoat 50% Technische Qualität | IC-10242 | 2024-01-06 | Supply Chain |
| PA-CH-580 KG | IC-10266 | 2022-10-26 | Product Management |
| SIG-69-BWM-8WBG | IC-10277 | 2023-05-24 | IT Infrastructure |
| Isoglucose | BC-10280 | 2024-09-25 | Operations |
| fructose standard | TC-10282 | 2022-03-28 | Data Governance |
| NO-SU-CO-376 | TC-10304 | 2024-12-09 | Supply Chain |
| SIG-14-HQE-PUWC | IC-10309 | 2024-07-05 | Finance |
| withholding nl 5% | IC-10321 | 2022-03-19 | Finance |
| Catalyst Versorgung International | BC-10329 | 2023-10-19 | Product Management |
| SIG-51-CZK-SBJH | BC-10338 | 2022-02-02 | Operations |
| AT-CH-341 SA | TC-10359 | 2022-01-01 | Finance |
| Traubenzucker 70% | TC-10368 | 2024-09-26 | Operations |
| Citric Acid 99.5% | TC-10373 | 2023-01-10 | Supply Chain |
| PR-SO-362 | BC-10377 | 2022-03-10 | Compliance |
| SIG-68-KHP-8RTJ | TC-10391 | 2021-10-21 | Operations |
| Ascorbic Acid | BC-10392 | 2021-10-05 | Product Management |
| soy isolate 50% premium | BC-10398 | 2023-06-04 | Compliance |
| Withholding NL 5% | IC-10404 | 2024-06-01 | Compliance |
| CO-OI-98-PR-329 | IC-10410 | 2023-01-13 | Product Management |
| SIG-98-XJT-L879 | IC-10417 | 2023-10-09 | IT Infrastructure |
| Apex Ingredients AG | IC-10418 | 2022-07-04 | Supply Chain |
| IS-25-FO-GR-789 | BC-10423 | 2024-02-24 | IT Infrastructure |
| Withholding FR 5% | TC-10424 | 2022-12-28 | Finance |
| Sodium Chloride Technical | IC-10428 | 2024-11-03 | Compliance |
| Ascorbic Acid 50% Technical | IC-10449 | 2021-12-06 | Product Management |
| Palm Oil 70% Grade B | IC-10469 | 2021-07-27 | IT Infrastructure |
| PE-PR-50-128 | BC-10475 | 2023-03-15 | Operations |
| Glukosesirup Syrup 25% | TC-10487 | 2024-10-23 | IT Infrastructure |
| Dextrose 70% Grade A | BC-10494 | 2022-02-01 | Compliance |
| Catalyst Materials | BC-10515 | 2023-08-01 | Finance |
| lactic acid standard | IC-10519 | 2021-10-14 | Finance |
| Potassium Sorbate | IC-10524 | 2021-04-27 | Data Governance |
| Pea Protein Standard | BC-10562 | 2021-12-02 | Operations |
| Stratos Ingredients SARL | TC-10564 | 2021-10-06 | Compliance |
| Kaliumsorbat Lebensmittelrein | BC-10590 | 2021-03-24 | Data Governance |
| Vat Reduced CN 19% | IC-10591 | 2024-09-05 | Product Management |
| Sodium Benzoate 99.5% Grade A | BC-10599 | 2022-08-26 | Operations |
| Lactic Acid | BC-10617 | 2021-05-23 | IT Infrastructure |
| Horizon Chemicals PLC | BC-10621 | 2021-11-05 | Compliance |
| soy isolate 99.5% | IC-10650 | 2024-02-02 | Data Governance |
| nordic processing SAS | BC-10654 | 2022-01-26 | Supply Chain |
| SIG-86-NGE-LKTW | IC-10661 | 2022-07-12 | Data Governance |
| Palm Oil 25% Grade A | BC-10663 | 2023-10-17 | Compliance |
| SIG-68-DWS-MNR6 | IC-10672 | 2021-06-02 | Data Governance |
| NE-TR-634 International | TC-10717 | 2021-10-11 | IT Infrastructure |
| Vat Reduced GB 19% | IC-10723 | 2024-12-14 | Finance |
| Withholding DE 20% | IC-10734 | 2022-08-17 | Product Management |
| MA-DE-335 | TC-10741 | 2024-05-14 | Compliance |
| Resistente Stärke | BC-10748 | 2024-10-02 | Data Governance |
| coconut oil standard | IC-10794 | 2023-02-12 | Data Governance |
| coconut oil 25% standard | TC-10828 | 2021-01-12 | Data Governance |
| Vat Reduced BR 25% | IC-10857 | 2022-05-03 | Finance |
| Excise US 19% | IC-10874 | 2022-12-25 | Compliance |
| CA-CA-FO-GR-991 | BC-10904 | 2022-08-13 | Product Management |
| Soja Isolate 99.5% | IC-10909 | 2024-09-12 | Data Governance |
| SIG-15-IUN-M051 | BC-10912 | 2021-09-22 | Operations |
| Resistente Stärke | BC-10919 | 2023-01-22 | Finance |
| potassium sorbate 25% pharma grade | BC-10940 | 2023-02-04 | Compliance |
| SO-BE-824 | BC-10952 | 2023-03-28 | Supply Chain |
| SO-BE-99.5-GR-A-930 | IC-10955 | 2021-02-25 | Compliance |
| pea protein premium | BC-10957 | 2024-01-08 | IT Infrastructure |
| SIG-26-PJJ-DUD8 | BC-10961 | 2021-09-28 | IT Infrastructure |
| Pea Protein 98% Qualitätsstufe II | TC-10971 | 2024-11-04 | Supply Chain |
| Vertex Solutions NV | BC-10978 | 2023-09-02 | Operations |
| sorbic acid | BC-10992 | 2023-04-10 | Operations |
| Pea Protein 25% | TC-10996 | 2024-09-13 | Supply Chain |
| PA-LO-674 | TC-10998 | 2024-12-16 | Finance |
| SIG-22-XCC-QSNV | TC-11007 | 2021-04-07 | Supply Chain |
| CO-IN-915 KG | TC-11010 | 2021-12-08 | IT Infrastructure |
| vertex chemicals International | TC-11024 | 2023-05-12 | IT Infrastructure |
| Atlantic Industrien International | TC-11038 | 2024-11-09 | Finance |
| pinnacle distribution Ltd. | IC-11041 | 2022-02-26 | Data Governance |
| SO-AC-PR-928 | BC-11054 | 2022-09-05 | Data Governance |
| Soy Isolate 50% Grade B | BC-11064 | 2022-04-28 | Product Management |
| Citric Acid 50% Grade A | IC-11090 | 2024-07-15 | Operations |
| Rapsöl 70% Qualitätsstufe II | TC-11105 | 2023-06-06 | Supply Chain |
| Pinnacle Materials | BC-11110 | 2024-11-04 | Data Governance |
| SIG-44-QME-TTIM | BC-11111 | 2024-06-18 | Data Governance |
| Calcium Carbonate Food Grade | BC-11132 | 2023-03-06 | Product Management |
| Nordic Chemicals BV | TC-11142 | 2023-07-18 | Compliance |
| NO-IN-797 | TC-11146 | 2023-11-22 | Compliance |
| Soy Isolate 25% Standard | TC-11148 | 2022-03-09 | Finance |
| Maltodextrin DE18 | TC-11150 | 2021-03-22 | IT Infrastructure |
| Meridian Enterprise | IC-11163 | 2022-02-14 | Compliance |
| rapeseed oil | BC-11171 | 2021-06-06 | Product Management |
| NO-LO-114 Ltd. | IC-11189 | 2022-10-13 | Compliance |
| Lactic Acid | TC-11218 | 2023-10-08 | Operations |
| Pinnacle Chemicals SA | TC-11262 | 2021-06-12 | Supply Chain |
| Excise BR 5% | IC-11265 | 2024-01-05 | IT Infrastructure |
| LA-AC-FO-GR-469 | BC-11275 | 2023-12-10 | Supply Chain |
| Natriumbenzoat 99.5% Technische Qualität | TC-11287 | 2022-12-18 | Product Management |
| Coconut Oil Food Grade | BC-11289 | 2024-01-08 | Data Governance |
| excise us 5% | IC-11293 | 2022-12-22 | Data Governance |
| Sodium Benzoate Pharma Grade | TC-11321 | 2023-08-23 | Operations |
| glucose syrup 98% food grade | IC-11343 | 2023-12-03 | IT Infrastructure |
| CO-IN-421 | BC-11368 | 2022-09-13 | Finance |
| Atlantic Handel BV | TC-11402 | 2021-10-02 | Finance |
| Quantum Rohstoffe | TC-11416 | 2024-07-20 | IT Infrastructure |
| SIG-58-NPG-WEEE PLC | TC-11428 | 2024-08-26 | Data Governance |
| Sonnenblumenöl Qualitätsstufe I | IC-11429 | 2023-02-16 | IT Infrastructure |
| SU-OI-TE-705 | TC-11436 | 2022-07-05 | Finance |
| Ascorbic Acid 98% Premium | TC-11439 | 2022-05-16 | Data Governance |
| PA-OI-98-856 | IC-11457 | 2024-02-18 | Supply Chain |
| Atlas Werkstoffe | BC-11459 | 2022-02-27 | IT Infrastructure |
| Pea Protein 25% | TC-11468 | 2022-11-05 | Operations |
| Weizenklebereiweiß 99.5% Technische Qualität | IC-11476 | 2024-04-03 | Product Management |
| SIG-65-TTX-PCJA | BC-11478 | 2023-10-23 | Supply Chain |
| Lactic Acid Technische Qualität | IC-11481 | 2024-04-05 | Operations |
| CE-SU-CO-752 | TC-11483 | 2022-11-05 | Data Governance |
| palm oil 50% | TC-11484 | 2021-10-23 | Data Governance |
| Nordic Logistik PLC | IC-11511 | 2022-07-07 | Data Governance |
| Natriumbenzoat 25% | TC-11518 | 2021-07-19 | Operations |
| SIG-29-ZZE-ZUAD | IC-11529 | 2021-04-20 | Data Governance |
| Fructose 98% Premiumqualität | IC-11539 | 2023-03-15 | IT Infrastructure |
| dextrose standard | IC-11547 | 2023-12-06 | Compliance |
| apex sourcing | TC-11559 | 2024-07-03 | Finance |
| Dextrose 25% | TC-11583 | 2024-08-14 | Supply Chain |
| Vertex Logistics Holdings | BC-11628 | 2021-05-20 | Data Governance |
| CI-AC-70-265 | BC-11636 | 2021-05-09 | IT Infrastructure |
| SIG-19-TLQ-1P5Z | TC-11641 | 2021-11-08 | Supply Chain |
| EX-F-19-312 | BC-11664 | 2024-05-23 | Supply Chain |
| SIG-91-WVE-3ESP | BC-11666 | 2021-05-20 | Finance |
| Premier Logistik | IC-11676 | 2024-09-01 | Supply Chain |
| customs duty nl 21% | IC-11696 | 2021-08-20 | Finance |
| Horizon Rohstoffe PLC | TC-11705 | 2022-05-28 | Compliance |
| Withholding NL 7% | BC-11714 | 2023-07-10 | Finance |
| Stratos Enterprise International | IC-11723 | 2022-02-14 | Finance |
| CA-MA-366 | IC-11734 | 2024-03-14 | Supply Chain |
| vat standard br 7% | TC-11775 | 2023-03-15 | IT Infrastructure |
| elite sourcing | TC-11780 | 2024-12-23 | Supply Chain |
| Global Rohstoffe AG | TC-11788 | 2024-08-03 | Supply Chain |
| Global Versorgung | BC-11800 | 2023-09-02 | Compliance |
| SIG-98-YBY-PFKQ | TC-11811 | 2024-12-04 | Operations |
| SIG-54-MUH-KY6K | IC-11816 | 2024-05-05 | IT Infrastructure |
| pea protein 98% standard | TC-11829 | 2022-02-01 | Supply Chain |
| PE-PR-50-128 | TC-11831 | 2022-04-13 | Data Governance |
| stratos sourcing | IC-11838 | 2022-04-19 | Product Management |
| SIG-86-JSN-H9KJ SA | IC-11843 | 2021-11-24 | IT Infrastructure |
| PA-OI-632 | BC-11849 | 2021-11-02 | Product Management |
| WI-G-21-298 | IC-11856 | 2022-11-20 | Data Governance |
| casein | IC-11860 | 2024-11-19 | Operations |
| Stratos Sourcing | BC-11861 | 2023-06-24 | Supply Chain |
| SIG-29-BKQ-HXCX Group | TC-11870 | 2022-07-05 | Operations |
| Vat Reduced BR 10% | IC-11891 | 2023-04-14 | Compliance |
| Traubenzucker 99.5% | TC-11896 | 2021-09-12 | Compliance |
| EL-SO-472 | IC-11899 | 2024-03-28 | Compliance |
| Nexus Logistik | IC-11907 | 2022-07-16 | Product Management |
| SIG-70-KJX-6V9L | BC-11922 | 2021-04-06 | Data Governance |
| Ascorbic Acid Pharmazeutisch rein | TC-11926 | 2021-05-27 | Operations |
| Sonnenblumenöl Standardqualität | TC-11927 | 2023-01-01 | Operations |
| Global Solutions International | BC-11935 | 2024-07-25 | Finance |
| PA-MA-664 | IC-11940 | 2021-07-17 | Compliance |
| WH-GL-830 | IC-11943 | 2023-12-28 | IT Infrastructure |
| Resistente Stärke 70% | IC-11948 | 2022-04-08 | Supply Chain |
| CY-PH-GR-870 | IC-11964 | 2024-02-06 | IT Infrastructure |
| PA-SU-CO-905 | TC-11979 | 2023-08-03 | IT Infrastructure |
| Citric Acid Pharma Grade | IC-11981 | 2022-06-27 | Product Management |
| Palm Oil 25% Grade A | TC-11982 | 2022-04-08 | Operations |
| Vat Standardqualität BR 15% | BC-11998 | 2023-03-07 | Product Management |
| PA-OI-TE-134 | TC-12005 | 2023-01-24 | Supply Chain |
| vat reduced gb 25% | BC-12025 | 2022-10-11 | Supply Chain |
| SIG-90-XNG-UYZN | BC-12062 | 2022-11-14 | Operations |
| Dextrin 50% | TC-12075 | 2024-03-03 | IT Infrastructure |
| core supply | IC-12080 | 2021-04-06 | Finance |
| sunflower oil food grade | TC-12083 | 2024-05-19 | Compliance |
| soy isolate standard | BC-12089 | 2024-02-05 | Data Governance |
| Prism Supply Co. | IC-12106 | 2022-05-18 | Finance |
| Sunflower Oil 50% Grade A | TC-12108 | 2023-02-05 | Data Governance |
| Vat Reduced NL 15% | IC-12115 | 2023-02-05 | Operations |
| Weizenklebereiweiß Lebensmittelrein | BC-12130 | 2022-09-04 | Operations |
| Sonnenblumenöl Technische Qualität | TC-12138 | 2024-08-22 | IT Infrastructure |
| Glucose Syrup 99.5% Grade B | TC-12170 | 2022-09-28 | Data Governance |
| Cyclodextrin | IC-12190 | 2023-01-16 | Supply Chain |
| core logistics | IC-12202 | 2021-11-07 | Supply Chain |
| SIG-18-LLP-8GUU | TC-12206 | 2021-11-26 | IT Infrastructure |
| Sodium Benzoate Pharma Grade | BC-12210 | 2022-01-01 | Supply Chain |
| BA-SU-CO-430 | BC-12211 | 2022-05-20 | Supply Chain |
| Kaliumsorbat | BC-12216 | 2021-08-12 | Operations |
| SIG-62-BTJ-PQV9 | BC-12232 | 2023-09-02 | Data Governance |
| Sunflower Oil Grade A | BC-12247 | 2023-09-04 | Product Management |
| Zenith Manufacturing | BC-12250 | 2023-03-10 | Product Management |
| Ascorbic Acid 50% Technical | TC-12265 | 2022-03-23 | IT Infrastructure |
| Excise FR 21% | IC-12289 | 2023-04-28 | Operations |
| lactic acid food grade | BC-12297 | 2023-11-22 | Data Governance |
| SO-CH-GR-A-776 | IC-12315 | 2022-10-23 | Operations |
| AP-SU-CO-755 | IC-12318 | 2024-09-18 | Product Management |
| SIG-58-DDZ-4JKE International | IC-12321 | 2023-12-28 | Finance |
| AP-LO-246 | BC-12325 | 2021-06-16 | Supply Chain |
| CU-DU-F-7-469 | BC-12333 | 2024-08-06 | Compliance |
| prism ingredients | BC-12338 | 2022-03-28 | Product Management |
| Sodium Chloride Technical | IC-12348 | 2024-12-02 | Supply Chain |
| sodium chloride premium | TC-12352 | 2023-06-28 | Data Governance |
| Rapsöl Technische Qualität | BC-12375 | 2021-10-26 | Finance |
| FR-99.5-TE-779 | BC-12380 | 2022-09-17 | Finance |
| sodium benzoate | IC-12388 | 2024-07-16 | Compliance |
| VA-EN-308 | IC-12401 | 2024-02-12 | Finance |
| Calcium Carbonate 99.5% Food Grade | BC-12405 | 2024-06-25 | Compliance |
| QU-SO-261 | BC-12410 | 2021-09-21 | Compliance |
| Apex Chemicals Corp. | BC-12414 | 2022-07-21 | Product Management |
| Vat Standardqualität DE 25% | IC-12422 | 2022-08-18 | Finance |
| SIG-30-SYO-74WX | TC-12429 | 2021-11-04 | Compliance |
| PR-IN-135 International | BC-12433 | 2023-01-20 | Finance |
| Excise FR 10% | TC-12457 | 2022-02-06 | Product Management |
| Glukosesirup Syrup | TC-12468 | 2023-10-25 | Supply Chain |
| SIG-57-GUP-S7UK | BC-12469 | 2022-07-05 | Supply Chain |
| Kaliumsorbat | TC-12478 | 2021-02-23 | IT Infrastructure |
| Casein 25% Technical | IC-12482 | 2024-11-24 | Compliance |
| Palm Oil 98% | BC-12501 | 2023-10-25 | Finance |
| PR-LO-745 | IC-12502 | 2024-11-02 | Operations |
| RE-ST-GR-B-598 | IC-12508 | 2021-11-20 | Compliance |
| resistant starch | BC-12520 | 2021-10-25 | Supply Chain |
| CU-DU-N-15-558 | TC-12547 | 2022-02-22 | Supply Chain |
| potassium sorbate 98% | IC-12550 | 2024-01-13 | Product Management |
| CI-AC-99.5-674 | TC-12575 | 2022-12-17 | Data Governance |
| Calcium Carbonate 70% Premiumqualität | IC-12614 | 2023-09-27 | Supply Chain |
| Isoglucose 25% Lebensmittelrein | TC-12652 | 2024-04-06 | Product Management |
| Premier Partners SARL | BC-12654 | 2024-07-01 | Compliance |
| Rapeseed Oil 70% Premium | IC-12666 | 2021-10-07 | IT Infrastructure |
| Vanguard Logistik SA | BC-12668 | 2024-04-08 | Supply Chain |
| PR-LO-704 | BC-12670 | 2021-08-16 | Operations |
| Excise DE 21% | TC-12671 | 2023-07-19 | Compliance |
| Prime Partners | TC-12680 | 2023-07-04 | Finance |
| citric acid 99.5% | TC-12687 | 2022-06-10 | Compliance |
| Prism Versorgung GmbH | IC-12692 | 2023-01-04 | Product Management |
| Natriumbenzoat 50% Technische Qualität | TC-12704 | 2021-11-13 | Finance |
| SIG-58-BDP-AYRN | TC-12723 | 2022-06-11 | Operations |
| SIG-25-ROA-G6G0 | IC-12727 | 2021-11-16 | Data Governance |
| SO-IS-FO-GR-334 | TC-12732 | 2021-07-22 | Operations |
| RE-ST-25-FO-GR-112 | IC-12748 | 2021-05-20 | IT Infrastructure |
| SIG-34-GNA-EHC2 | BC-12751 | 2022-02-16 | Finance |
| Soy Isolate Technical | BC-12775 | 2023-12-27 | IT Infrastructure |
| Prime Logistik | TC-12781 | 2021-02-07 | Compliance |
| CO-OI-966 | BC-12787 | 2023-02-03 | Supply Chain |
| Sorbic Acid Standard | BC-12791 | 2023-12-01 | Supply Chain |
| CO-OI-FO-GR-162 | TC-12799 | 2021-09-22 | Compliance |
| sodium chloride | IC-12805 | 2023-06-12 | Product Management |
| SIG-42-BSJ-L2CG | BC-12808 | 2021-03-13 | IT Infrastructure |
| Kaliumsorbat Premiumqualität | TC-12814 | 2021-02-23 | Finance |
| ascorbic acid 99.5% tech grade | IC-12824 | 2022-08-12 | Operations |
| horizon supply | TC-12826 | 2024-11-09 | Compliance |
| Pacific Industries Holdings | IC-12851 | 2023-01-11 | Supply Chain |
| QU-SO-233 | TC-12855 | 2023-12-26 | Operations |
| Maltodextrin DE5 Food Grade | BC-12877 | 2021-10-12 | Product Management |
| LA-AC-TE-651 | BC-12889 | 2022-12-17 | Product Management |
| quantum trading SARL | BC-12900 | 2021-07-23 | Finance |
| Sonnenblumenöl Premiumqualität | IC-12902 | 2024-09-19 | Operations |
| wheat gluten 98% | BC-12946 | 2022-04-03 | Product Management |
| SIG-85-WWC-01LO | IC-12949 | 2021-03-12 | Finance |
| Core Versorgung GmbH | TC-12953 | 2022-01-26 | Data Governance |
| sodium benzoate 99.5% tech grade | TC-12956 | 2023-11-22 | Product Management |
| Sodium Benzoate Pharma Grade | IC-12960 | 2021-09-20 | Product Management |
| Vertex Logistik | TC-12981 | 2023-04-09 | Compliance |
| Continental Werkstoffe NV | TC-12996 | 2021-12-17 | IT Infrastructure |
| Vertex Ingredients GmbH | IC-13003 | 2024-11-01 | Product Management |
| Dextrose | BC-13021 | 2023-03-06 | Finance |
| Resistente Stärke Technische Qualität | TC-13039 | 2023-04-28 | Supply Chain |
| Rapsöl 70% Premiumqualität | BC-13044 | 2021-12-05 | Data Governance |
| Weizenklebereiweiß 99.5% | IC-13056 | 2021-05-21 | Data Governance |
| catalyst supply | IC-13068 | 2024-12-20 | Product Management |
| VA-ST-I-5-735 | IC-13099 | 2023-12-09 | Compliance |
| calcium carbonate standard | BC-13104 | 2022-05-22 | Data Governance |
| AS-AC-165 | IC-13127 | 2022-05-02 | Finance |
| prism manufacturing NV | BC-13154 | 2021-09-17 | Data Governance |
| Palm Oil 98% | BC-13159 | 2022-01-05 | Operations |
| Sodium Benzoate | BC-13180 | 2022-11-22 | Data Governance |
| SIG-42-UOJ-4ACC Holdings | IC-13183 | 2022-10-28 | Data Governance |
| SIG-82-JMP-PVGN | TC-13188 | 2023-07-01 | Operations |
| sodium chloride 98% pharma grade | TC-13216 | 2023-03-18 | Operations |
| Global Chemicals SAS | TC-13223 | 2022-01-24 | Product Management |
| Natriumchlorid 99.5% Qualitätsstufe I | BC-13270 | 2023-04-06 | Supply Chain |
| prism industries International | TC-13284 | 2021-03-13 | Operations |
| core chemicals Holdings | TC-13294 | 2023-05-18 | Data Governance |
| sodium benzoate 99.5% premium | BC-13312 | 2022-10-20 | Operations |
| SIG-88-KUG-5ITD | IC-13345 | 2023-06-16 | Finance |
| Core Chemicals | IC-13354 | 2023-02-19 | Compliance |
| SIG-15-FOA-70S8 | BC-13388 | 2023-08-26 | Operations |
| CA-CA-25-PH-GR-684 | IC-13391 | 2021-11-05 | Supply Chain |
| SIG-10-TIC-7Q1D | IC-13395 | 2022-07-04 | Finance |
| Central Logistics | BC-13396 | 2022-09-19 | Compliance |
| cyclodextrin | IC-13401 | 2024-02-05 | Supply Chain |
| Sonnenblumenöl 70% | IC-13412 | 2021-06-18 | Operations |
| Horizon Partners Ltd. | IC-13424 | 2022-04-27 | Product Management |
| Withholding BR 20% | TC-13443 | 2022-05-26 | Data Governance |
| Nordic Processing SAS | IC-13458 | 2021-06-28 | Data Governance |
| Baltic Industrien PLC | BC-13470 | 2022-04-21 | Compliance |
| SIG-83-JEP-R0ZJ | IC-13475 | 2024-06-10 | Operations |
| Resistant Starch 98% Pharma Grade | TC-13481 | 2022-09-14 | Operations |
| Sodium Chloride 70% Grade B | BC-13490 | 2022-09-05 | Supply Chain |
| SU-OI-GR-A-704 | BC-13493 | 2022-12-04 | Data Governance |
| pinnacle industries SAS | BC-13503 | 2022-07-14 | Data Governance |
| vanguard sourcing | IC-13554 | 2023-12-13 | Supply Chain |
| AS-AC-PH-GR-192 | TC-13561 | 2022-10-07 | Supply Chain |
| glucose syrup 98% standard | IC-13565 | 2021-04-17 | IT Infrastructure |
| ST-PA-227 PLC | TC-13575 | 2024-08-04 | Supply Chain |
| Sonnenblumenöl Qualitätsstufe I | BC-13590 | 2024-06-02 | Product Management |
| FR-278 | IC-13621 | 2021-12-21 | Compliance |
| Dextrin Grade B | BC-13622 | 2023-07-10 | IT Infrastructure |
| SIG-31-CWE-03UX | BC-13623 | 2021-04-09 | Finance |
| HO-LO-886 | TC-13627 | 2023-06-03 | Product Management |
| Meridian Distribution | TC-13628 | 2022-02-14 | Data Governance |
| AP-SO-704 | IC-13646 | 2023-02-18 | Supply Chain |
| nexus supply | TC-13648 | 2021-03-08 | Data Governance |
| citric acid premium | BC-13658 | 2022-11-10 | Compliance |
| Horizon Sourcing | TC-13677 | 2021-01-19 | IT Infrastructure |
| dextrose | IC-13687 | 2022-02-19 | Compliance |
| Dextrin 50% | IC-13699 | 2022-01-27 | Supply Chain |
| LA-AC-GR-A-486 | BC-13710 | 2023-10-02 | Finance |
| Casein Grade A | TC-13722 | 2022-12-05 | Operations |
| DE-25-260 | IC-13728 | 2023-08-24 | Product Management |
| resistant starch 50% | TC-13737 | 2022-02-24 | IT Infrastructure |
| SIG-68-GHA-D32X | IC-13742 | 2021-01-19 | Supply Chain |
| SIG-20-XIG-T8ME | TC-13747 | 2023-06-03 | Operations |
| Maltodextrin-Pulver DE18 | IC-13755 | 2022-09-11 | Finance |
| Core Partners BV | TC-13773 | 2023-12-04 | Operations |
| Vertex Handel Holdings | TC-13777 | 2024-10-03 | Compliance |
| premier supply | IC-13787 | 2021-04-25 | IT Infrastructure |
| PI-CO-717 | IC-13833 | 2022-08-17 | Data Governance |
| palm oil | TC-13862 | 2023-03-26 | Operations |
| customs duty de 25% | BC-13876 | 2022-02-12 | Product Management |
| Sodium Benzoate 99.5% Grade A | BC-13878 | 2021-02-26 | Data Governance |
| Calcium Carbonate 98% | TC-13894 | 2021-04-02 | Compliance |
| Stratos Supply SAS | IC-13911 | 2024-04-24 | Data Governance |
| Meridian Logistics | IC-13919 | 2023-11-26 | Product Management |
| Vat Reduced BR 10% | BC-13920 | 2021-12-24 | Operations |
| Catalyst Industries International | BC-13923 | 2024-01-25 | Finance |
| FR-50-ST-130 | BC-13935 | 2023-12-18 | Operations |
| Atlantic Sourcing | IC-13936 | 2024-11-20 | Data Governance |
| SIG-48-KTU-I0WF | IC-13981 | 2023-12-08 | Supply Chain |
| SIG-36-TML-VS0J | BC-14014 | 2022-04-16 | Compliance |
| CO-OI-FO-GR-162 | BC-14016 | 2023-01-28 | Supply Chain |
| dextrose | BC-14045 | 2022-07-26 | Data Governance |
| Palm Oil | IC-14048 | 2024-02-15 | Compliance |
| SIG-36-TML-VS0J | TC-14061 | 2021-01-23 | Operations |
| SO-CH-TE-789 | BC-14080 | 2024-05-13 | Operations |
| baltic chemicals AG | BC-14084 | 2023-05-11 | Data Governance |
| EX-C-25-332 | TC-14108 | 2023-07-15 | Data Governance |
| stratos supply | IC-14123 | 2021-11-21 | Supply Chain |
| Natriumchlorid | IC-14131 | 2021-08-27 | Finance |
| WH-GL-123 | TC-14152 | 2023-12-27 | Data Governance |
| SIG-78-LTE-H4VL | BC-14153 | 2024-01-04 | Data Governance |
| SIG-24-LUX-S83X | TC-14198 | 2024-09-12 | Supply Chain |
| withholding gb 21% | IC-14200 | 2024-09-22 | Operations |
| AT-LO-628 | BC-14208 | 2024-09-20 | Compliance |
| Quantum Handel Ltd. | TC-14217 | 2024-09-20 | Operations |
| IS-GR-B-640 | BC-14219 | 2021-12-02 | Data Governance |
| Atlas Industrien International | TC-14228 | 2023-03-01 | Operations |
| SIG-81-SBE-HL1C | IC-14233 | 2021-12-06 | Operations |
| SIG-48-LHY-R0O8 | IC-14238 | 2021-08-08 | Operations |
| Natriumbenzoat 99.5% Qualitätsstufe I | TC-14280 | 2021-02-11 | Data Governance |
| LA-AC-393 | BC-14303 | 2023-03-12 | IT Infrastructure |
| SIG-71-WDX-2GRR | BC-14305 | 2021-06-21 | Supply Chain |
| Natriumbenzoat | IC-14318 | 2023-06-03 | Operations |
| Horizon Sourcing | BC-14319 | 2022-04-22 | IT Infrastructure |
| Apex Manufacturing | BC-14355 | 2022-09-10 | Supply Chain |
| SIG-44-UIE-SASC | BC-14366 | 2024-06-20 | IT Infrastructure |
| Glukosesirup Syrup | IC-14375 | 2022-12-06 | Supply Chain |
| lactic acid 98% | TC-14395 | 2022-07-23 | IT Infrastructure |
| Central Manufacturing Ltd. | IC-14409 | 2022-12-01 | Supply Chain |
| SIG-70-ZNI-VX97 NV | BC-14438 | 2024-02-09 | Operations |
| Citric Acid Premium | BC-14446 | 2023-09-27 | Finance |
| Meridian Logistics | TC-14448 | 2023-01-14 | IT Infrastructure |
| SIG-37-MXA-3C7Q | BC-14467 | 2022-06-04 | Compliance |
| SIG-57-YNB-5KMT | IC-14470 | 2023-10-06 | Data Governance |
| Sonnenblumenöl Qualitätsstufe II | IC-14471 | 2021-09-27 | Supply Chain |
| SIG-19-VTP-JBQ4 | TC-14487 | 2021-06-08 | Operations |
| SIG-20-MSW-TMXG | TC-14507 | 2022-09-18 | Compliance |
| PE-PR-25-185 | BC-14525 | 2021-12-16 | IT Infrastructure |
| Customs Duty IN 5% | BC-14528 | 2023-02-17 | Finance |
| Withholding DE 20% | BC-14547 | 2023-07-03 | Supply Chain |
| rapeseed oil food grade | BC-14548 | 2021-03-13 | Product Management |
| SIG-56-ZVH-GATJ | TC-14550 | 2024-11-16 | Compliance |
| CO-OI-98-FO-GR-748 | TC-14552 | 2022-04-19 | Data Governance |
| Traubenzucker 50% | IC-14553 | 2022-03-12 | Data Governance |
| maltodextrin de5 standard | IC-14559 | 2023-11-24 | IT Infrastructure |
| VA-ST-B-25-316 | IC-14571 | 2022-03-19 | Product Management |
| Dextrin Pharma Grade | BC-14573 | 2023-11-22 | IT Infrastructure |
| SO-BE-FO-GR-835 | TC-14578 | 2023-11-12 | Supply Chain |
| SIG-81-FXX-6VPL | BC-14580 | 2021-07-05 | Data Governance |
| Maltodextrin DE15 | IC-14586 | 2022-11-20 | Supply Chain |
| Dextrin 99.5% | TC-14605 | 2024-02-24 | Finance |
| FR-PH-GR-146 | TC-14624 | 2021-08-18 | Operations |
| Cyclodextrin 98% Pharma Grade | BC-14628 | 2021-10-04 | Finance |
| stellar manufacturing International | IC-14641 | 2023-10-21 | Product Management |
| CI-AC-488 | TC-14649 | 2023-04-22 | Data Governance |
| ascorbic acid 98% premium | IC-14657 | 2024-10-12 | Supply Chain |
| prime logistics NV | IC-14659 | 2022-03-05 | Supply Chain |
| Lactic Acid | TC-14670 | 2024-05-03 | Finance |
| CO-IN-754 International | BC-14675 | 2022-12-23 | Compliance |
| Prime Rohstoffe LLC | TC-14696 | 2021-08-12 | IT Infrastructure |
| Pea Protein 98% Qualitätsstufe II | IC-14717 | 2023-05-21 | Supply Chain |
| Sorbic Acid 25% Grade B | TC-14728 | 2023-07-21 | Compliance |
| PA-OI-TE-134 | BC-14732 | 2023-01-16 | Compliance |
| Horizon Versorgung GmbH | TC-14740 | 2021-01-02 | Finance |
| Customs Duty FR 7% | BC-14772 | 2022-11-23 | Operations |
| Baltic Sourcing | BC-14802 | 2022-09-06 | Finance |
| Pea Protein Grade B | TC-14804 | 2023-09-23 | Operations |
| SO-AC-377 | BC-14809 | 2022-10-20 | IT Infrastructure |
| SIG-19-TPS-MSKY | TC-14812 | 2024-07-12 | Supply Chain |
| CA-CA-GR-B-761 | BC-14819 | 2022-10-09 | Data Governance |
| Sonnenblumenöl Standardqualität | BC-14831 | 2022-03-26 | Supply Chain |
| Zenith Supply Co. | TC-14849 | 2021-08-08 | Compliance |
| Natriumbenzoat 25% | BC-14853 | 2021-08-25 | Operations |
| SIG-30-UET-0Q2O | TC-14868 | 2023-07-08 | Finance |
| VA-RE-C-21-521 | IC-14900 | 2022-08-28 | Product Management |
| Palm Oil Grade B | BC-14906 | 2021-07-07 | Supply Chain |
| DE-70-GR-A-741 | TC-14932 | 2024-03-23 | IT Infrastructure |
| Glukosesirup Syrup Qualitätsstufe I | TC-14938 | 2023-02-24 | Data Governance |
| SIG-31-BWX-FDET | TC-14941 | 2021-08-28 | Product Management |
| Atlantic Versorgung GmbH | IC-14973 | 2024-03-20 | Finance |
| CE-LO-195 | TC-14984 | 2024-10-02 | Operations |
| Horizon Distribution Holdings | TC-14987 | 2023-10-09 | IT Infrastructure |
| SIG-18-NCG-WT1V | IC-14991 | 2021-09-11 | Product Management |
| SIG-45-ZZU-GRXH International | BC-15013 | 2021-04-24 | Operations |
| Baltic Handel NV | BC-15017 | 2021-12-27 | Supply Chain |
| CI-AC-TE-350 | BC-15023 | 2021-02-15 | Supply Chain |
| AT-SU-CO-645 | BC-15024 | 2024-05-01 | Finance |
| Sodium Chloride 70% Grade B | TC-15032 | 2022-09-04 | Product Management |
| meridian supply | TC-15053 | 2023-09-18 | Operations |
| maltodextrin de30 | IC-15055 | 2023-11-22 | Product Management |
| elite materials | BC-15062 | 2021-03-25 | IT Infrastructure |
| Lactic Acid Food Grade | BC-15075 | 2021-10-16 | IT Infrastructure |
| SO-BE-PH-GR-647 | IC-15096 | 2023-02-11 | IT Infrastructure |
| Natriumbenzoat | BC-15118 | 2023-12-28 | Data Governance |
| Sonnenblumenöl | BC-15124 | 2024-09-28 | Operations |
| Stratos Sourcing | IC-15133 | 2021-11-04 | Supply Chain |
| prime sourcing | BC-15154 | 2021-10-04 | Operations |
| Catalyst Industrien International | BC-15161 | 2022-08-15 | IT Infrastructure |
| continental logistics | TC-15170 | 2022-07-04 | Operations |
| SIG-92-AXW-GPAG | TC-15199 | 2023-09-23 | Operations |
| Vat Standardqualität GB 19% | TC-15213 | 2021-06-13 | Supply Chain |
| CI-AC-PR-827 | TC-15220 | 2023-01-21 | Compliance |
| nordic sourcing | IC-15246 | 2021-04-15 | Data Governance |
| pacific supply | BC-15276 | 2023-12-04 | Finance |
| SO-AC-25-PH-GR-887 | IC-15282 | 2021-05-06 | Operations |
| Fructose Food Grade | IC-15292 | 2024-08-24 | Data Governance |
| glucose syrup | TC-15295 | 2023-07-09 | Product Management |
| Excise IN 20% | IC-15298 | 2024-09-02 | IT Infrastructure |
| Excise FR 21% | BC-15316 | 2022-06-11 | IT Infrastructure |
| Palm Oil 70% Pharma Grade | BC-15328 | 2021-06-18 | Product Management |
| SO-BE-708 | TC-15332 | 2022-04-11 | Operations |
| SIG-65-LOJ-4KXS | IC-15337 | 2021-12-13 | Operations |
| ascorbic acid standard | BC-15341 | 2021-10-06 | Finance |
| LA-AC-FO-GR-469 | IC-15349 | 2024-09-20 | Operations |
| SIG-40-XXD-GE9O | IC-15352 | 2022-07-21 | Operations |
| soy isolate premium | IC-15364 | 2021-01-19 | Compliance |
| RE-ST-PR-679 | BC-15372 | 2021-08-27 | Operations |
| DE-ST-385 | BC-15376 | 2022-09-14 | IT Infrastructure |
| Soy Isolate Standard | BC-15377 | 2023-07-27 | Supply Chain |
| Horizon Logistics International | BC-15385 | 2022-07-02 | Data Governance |
| LA-AC-TE-761 | BC-15386 | 2023-01-11 | Product Management |
| GL-SY-PR-440 | TC-15388 | 2021-03-13 | Product Management |
| Sodium Benzoate Grade A | IC-15389 | 2024-07-15 | Finance |
| prism sourcing | TC-15392 | 2021-05-09 | IT Infrastructure |
| IS-802 | TC-15439 | 2022-11-27 | Data Governance |
| ascorbic acid tech grade | IC-15443 | 2021-11-06 | IT Infrastructure |
| Fructose Standardqualität | BC-15462 | 2024-11-05 | IT Infrastructure |
| Isoglucose Technical | TC-15473 | 2024-03-18 | Compliance |
| nexus distribution AG | BC-15496 | 2023-11-20 | Compliance |
| PA-OI-383 | BC-15501 | 2021-02-12 | Operations |
| Premier Partners Group | BC-15528 | 2022-08-13 | IT Infrastructure |
| Ascorbic Acid Premiumqualität | IC-15561 | 2023-10-22 | Data Governance |
| VA-RE-I-5-252 | BC-15564 | 2021-10-08 | IT Infrastructure |
| Citric Acid 25% Technical | TC-15580 | 2023-03-10 | Finance |
| DE-840 | TC-15582 | 2022-11-04 | Compliance |
| dextrose 70% | IC-15587 | 2024-12-24 | Finance |
| SO-CH-99.5-GR-A-634 | BC-15606 | 2024-06-01 | Supply Chain |
| vertex logistics | IC-15618 | 2022-02-26 | Supply Chain |
| Traubenzucker 25% Technische Qualität | TC-15630 | 2023-05-25 | Product Management |
| Resistant Starch | BC-15644 | 2024-12-05 | Data Governance |
| Elite Logistics | BC-15651 | 2022-12-27 | Data Governance |
| SIG-20-IKV-891D | BC-15656 | 2021-07-06 | Product Management |
| pea protein pharma grade | IC-15673 | 2024-08-18 | Data Governance |
| ST-PA-504 | TC-15678 | 2023-03-22 | Product Management |
| Natriumchlorid | TC-15690 | 2024-06-26 | Supply Chain |
| Potassium Sorbate 50% Technical | BC-15702 | 2024-07-20 | Finance |
| SIG-60-GHI-04X0 | IC-15704 | 2021-02-01 | Operations |
| Palm Oil 99.5% Grade A | TC-15708 | 2023-07-21 | Finance |
| Dextrin Standardqualität | IC-15722 | 2023-08-11 | Data Governance |
| sunflower oil premium | BC-15725 | 2021-12-18 | Finance |
| SIG-21-PIO-0RWR | IC-15734 | 2024-01-17 | Product Management |
| Rapsöl Technische Qualität | TC-15749 | 2021-11-22 | Data Governance |
| withholding in 20% | IC-15763 | 2023-09-16 | Finance |
| Horizon Partners Ltd. | BC-15770 | 2024-01-24 | Compliance |
| sodium chloride tech grade | IC-15786 | 2023-01-09 | IT Infrastructure |
| SIG-51-EYN-NILM LLC | TC-15788 | 2024-04-04 | Finance |
| apex supply | IC-15796 | 2022-06-20 | Product Management |
| Sorbinsäure 98% | BC-15798 | 2024-03-28 | Supply Chain |
| Sunflower Oil Pharma Grade | TC-15814 | 2023-01-22 | IT Infrastructure |
| Premier Enterprise International | TC-15835 | 2021-12-28 | Supply Chain |
| Rapsöl | TC-15870 | 2022-03-04 | IT Infrastructure |
| sorbic acid premium | IC-15874 | 2022-05-22 | Data Governance |
| Sonnenblumenöl Standardqualität | BC-15880 | 2021-04-03 | IT Infrastructure |
| Vat Reduced BR 10% | BC-15884 | 2023-08-02 | Supply Chain |
| Central Logistik | TC-15886 | 2021-11-02 | Finance |
| Pea Protein 25% | BC-15907 | 2021-12-20 | Supply Chain |
| SIG-74-AEB-PMX7 | BC-15913 | 2021-08-03 | Finance |
| Apex Werkstoffe International | BC-15922 | 2022-08-10 | Operations |
| Maltodextrin-Pulver DE30 | BC-15927 | 2021-04-18 | Operations |
| Baltic Werkstoffe | IC-15928 | 2024-07-19 | Supply Chain |
| SIG-67-JNR-XNTM | BC-15936 | 2024-04-23 | Compliance |
| SIG-22-VQM-AGKC | BC-15944 | 2022-12-25 | Operations |
| SIG-82-PJM-2KX0 | TC-15987 | 2024-11-02 | Supply Chain |
| Sunflower Oil Technical | BC-15995 | 2024-02-22 | Product Management |
| PI-IN-970 Corp. | TC-16009 | 2024-01-21 | Compliance |
| Atlantic Werkstoffe | TC-16023 | 2021-09-06 | Finance |
| Nordic Versorgung GmbH | IC-16025 | 2021-08-24 | IT Infrastructure |
| citric acid premium | TC-16038 | 2021-06-11 | Operations |
| Sodium Chloride | TC-16043 | 2024-04-21 | Compliance |
| AT-SO-915 | TC-16048 | 2024-11-07 | Data Governance |
| SIG-83-KGL-Q4QE | TC-16062 | 2023-01-20 | IT Infrastructure |
| SIG-77-LSN-T27F | IC-16066 | 2022-10-24 | Finance |
| potassium sorbate 50% standard | BC-16083 | 2022-07-12 | Compliance |
| Catalyst Werkstoffe | TC-16093 | 2024-07-14 | Product Management |
| atlas enterprise | TC-16098 | 2023-07-21 | Compliance |
| LA-AC-927 | BC-16105 | 2024-09-25 | Supply Chain |
| MA-DE-738 | IC-16124 | 2022-05-19 | Operations |
| Stratos Versorgung GmbH | TC-16143 | 2022-05-06 | Product Management |
| apex manufacturing KG | TC-16159 | 2021-09-19 | Product Management |
| SIG-58-MKV-8WKD | BC-16164 | 2023-03-25 | Finance |
| Atlantic Trading | BC-16165 | 2021-11-04 | Supply Chain |
| Vertex Vertrieb Group | IC-16173 | 2024-10-04 | Finance |
| Coconut Oil 70% Grade A | TC-16183 | 2021-11-28 | Operations |
| SIG-68-BSO-NW8J Group | TC-16188 | 2022-07-06 | Supply Chain |
| SIG-88-AJL-T9ZS | TC-16206 | 2022-05-23 | Operations |
| SIG-15-AXQ-9Z8K | IC-16233 | 2021-09-28 | Product Management |
| SIG-42-BSJ-L2CG | BC-16236 | 2021-12-17 | Data Governance |
| LA-AC-690 | BC-16245 | 2022-06-24 | IT Infrastructure |
| dextrin 70% pharma grade | IC-16263 | 2023-04-16 | Supply Chain |
| Sorbinsäure | BC-16265 | 2021-03-13 | Compliance |
| Cyclodextrin Standard | BC-16276 | 2024-03-19 | Supply Chain |
| SIG-57-YOY-F7N2 | BC-16285 | 2021-02-22 | Operations |
| Apex Sourcing | BC-16290 | 2021-03-08 | Compliance |
| Glukosesirup Syrup Premiumqualität | BC-16309 | 2024-11-21 | Supply Chain |
| Central Materials NV | TC-16310 | 2022-11-20 | Compliance |
| cyclodextrin 70% food grade | TC-16337 | 2023-09-04 | Finance |
| stratos logistics | TC-16342 | 2023-05-07 | Data Governance |
| pea protein | BC-16355 | 2023-07-21 | IT Infrastructure |
| Rapsöl 50% Pharmazeutisch rein | TC-16366 | 2022-04-27 | Supply Chain |
| Pinnacle Trading | TC-16387 | 2023-01-06 | Compliance |
| ascorbic acid premium | IC-16406 | 2022-01-02 | Operations |
| Vat Standardqualität US 21% | IC-16415 | 2021-12-27 | IT Infrastructure |
| Core Rohstoffe | IC-16419 | 2021-12-15 | Finance |
| coconut oil 25% | BC-16431 | 2023-04-14 | Product Management |
| SIG-27-VCT-2O4S | BC-16450 | 2023-11-18 | Operations |
| Palm Oil Food Grade | TC-16465 | 2023-06-28 | Compliance |
| Nordic Manufacturing Holdings | BC-16482 | 2023-06-25 | Compliance |
| SIG-79-OZQ-4I2N | TC-16486 | 2023-01-03 | Product Management |
| Coconut Oil 99.5% Pharma Grade | BC-16501 | 2023-12-04 | Finance |
| Nexus Materials | TC-16509 | 2023-05-09 | Finance |
| Kaliumsorbat | IC-16520 | 2024-04-13 | IT Infrastructure |
| Pinnacle Chemicals SAS | IC-16522 | 2022-09-24 | Compliance |
| SIG-67-TPL-WT5F | TC-16532 | 2024-09-13 | IT Infrastructure |
| NE-SO-511 | TC-16546 | 2022-08-16 | Operations |
| sodium chloride | TC-16568 | 2022-04-10 | Supply Chain |
| Meridian Distribution | TC-16611 | 2022-12-16 | Compliance |
| SIG-81-LVQ-2J60 | IC-16627 | 2024-03-21 | IT Infrastructure |
| BA-IN-547 | BC-16629 | 2022-03-19 | Finance |
| Nexus Processing International | TC-16671 | 2021-05-18 | Data Governance |
| CO-LO-944 | BC-16676 | 2022-06-17 | Finance |
| VE-SU-CO-378 | BC-16677 | 2023-08-23 | Data Governance |
| SIG-64-BPY-A8RD | BC-16694 | 2021-06-20 | IT Infrastructure |
| Horizon Sourcing | BC-16732 | 2023-07-21 | Finance |
| CE-LO-198 Holdings | TC-16749 | 2022-02-18 | Operations |
| vat reduced gb 25% | BC-16751 | 2023-10-06 | IT Infrastructure |
| SO-BE-708 | IC-16753 | 2021-03-03 | Product Management |
| Dextrin 50% | IC-16764 | 2022-09-24 | Supply Chain |
| SIG-44-UKH-MO4F | IC-16772 | 2021-12-23 | Operations |
| Ascorbic Acid 98% Qualitätsstufe II | IC-16777 | 2021-04-21 | Product Management |
| Baltic Distribution Group | TC-16795 | 2022-01-24 | IT Infrastructure |
| Coconut Oil 98% Lebensmittelrein | TC-16821 | 2024-06-17 | Supply Chain |
| Excise GB 5% | IC-16833 | 2024-01-28 | Product Management |
| PA-LO-382 Group | BC-16839 | 2024-06-07 | IT Infrastructure |
| Central Vertrieb | BC-16855 | 2023-08-16 | Product Management |
| SIG-41-FFO-RXYJ | BC-16869 | 2022-03-17 | Operations |
| Soja Isolate Pharmazeutisch rein | TC-16909 | 2021-11-05 | Data Governance |
| Nexus Materials | IC-16911 | 2021-05-25 | Compliance |
| Pinnacle Logistics International | TC-16913 | 2024-07-07 | Finance |
| SIG-90-SZM-PZJ4 | TC-16927 | 2023-06-01 | Product Management |
| Rapsöl 50% Qualitätsstufe I | IC-16937 | 2023-09-01 | IT Infrastructure |
| Dextrin Technical | IC-16954 | 2021-05-14 | Compliance |
| AP-PR-849 PLC | TC-16959 | 2024-02-23 | Supply Chain |
| Prism Werkstoffe Ltd. | BC-16971 | 2021-02-10 | Data Governance |
| PO-SO-ST-111 | IC-16973 | 2024-04-17 | IT Infrastructure |
| SIG-98-CGL-FHWJ | BC-16978 | 2023-08-11 | Product Management |
| Excise CN 19% | IC-16981 | 2021-04-21 | IT Infrastructure |
| SIG-94-TUN-H84G | IC-17002 | 2023-04-07 | Finance |
| CO-OI-FO-GR-162 | BC-17010 | 2023-08-01 | Supply Chain |
| SO-AC-GR-A-997 | IC-17013 | 2021-04-05 | Compliance |
| CU-DU-C-25-616 | IC-17016 | 2023-01-20 | Supply Chain |
| PE-PR-251 | TC-17024 | 2022-04-26 | IT Infrastructure |
| dextrose 70% | IC-17032 | 2021-06-11 | Compliance |
| Lactic Acid 25% Premium | IC-17039 | 2023-02-22 | Product Management |
| coconut oil food grade | BC-17047 | 2022-02-19 | Operations |
| sodium chloride 98% standard | IC-17053 | 2022-07-12 | Compliance |
| SIG-88-AGF-FF5L | BC-17067 | 2022-02-24 | Compliance |
| WH-GL-GR-A-924 | TC-17072 | 2021-04-16 | IT Infrastructure |
| SIG-58-WYL-XCXB | IC-17074 | 2023-09-10 | Finance |
| DE-50-891 | IC-17087 | 2021-06-03 | Data Governance |
| Calcium Carbonate | IC-17125 | 2024-08-25 | Product Management |
| Atlantic Manufacturing International | TC-17132 | 2022-04-24 | Supply Chain |
| SO-BE-70-PR-120 | TC-17137 | 2023-10-06 | Finance |
| Soy Isolate | TC-17155 | 2024-08-15 | IT Infrastructure |
| SIG-62-BTJ-PQV9 | TC-17171 | 2023-10-08 | Supply Chain |
| MA-DE-186 | TC-17173 | 2023-12-09 | Finance |
| Elite Logistik | TC-17185 | 2024-01-15 | IT Infrastructure |
| SIG-16-IYP-EOZP | TC-17189 | 2023-11-11 | Data Governance |
| HO-LO-699 | BC-17194 | 2021-07-21 | Supply Chain |
| QU-LO-616 | BC-17199 | 2021-04-18 | Finance |
| VA-MA-537 Holdings | TC-17225 | 2022-02-17 | IT Infrastructure |
| Zitronensäure 70% Lebensmittelrein | BC-17229 | 2024-04-12 | Operations |
| Core Logistik | TC-17236 | 2023-12-10 | IT Infrastructure |
| AP-MA-145 International | IC-17239 | 2024-07-23 | Compliance |
| Atlantic Supply Co. | BC-17259 | 2023-01-08 | Compliance |
| SO-BE-667 | IC-17261 | 2022-02-23 | Compliance |
| Ascorbic Acid 99.5% Technische Qualität | IC-17265 | 2024-06-14 | Product Management |
| Nordic Supply Co. | IC-17287 | 2021-08-20 | Finance |
| Vat Reduced CN 10% | TC-17303 | 2024-06-20 | Finance |
| pacific chemicals AG | BC-17313 | 2022-07-15 | IT Infrastructure |
| Withholding US 10% | IC-17339 | 2022-05-08 | Product Management |
| Continental Sourcing | BC-17344 | 2021-09-26 | Supply Chain |
| Withholding FR 5% | IC-17352 | 2023-11-19 | Finance |
| Vertex Materials | BC-17353 | 2021-02-03 | Compliance |
| Vat Standardqualität IN 0% | BC-17360 | 2024-11-05 | Compliance |
| SO-AC-98-579 | IC-17367 | 2024-04-01 | Compliance |
| Isoglucose 50% Qualitätsstufe I | IC-17376 | 2021-09-04 | Compliance |
| Nordic Industries Ltd. | BC-17382 | 2022-06-23 | Finance |
| Pinnacle Werkstoffe | BC-17386 | 2022-08-13 | Finance |
| SIG-74-ZNA-1VYW | TC-17391 | 2023-11-06 | Operations |
| Zenith Trading | IC-17398 | 2023-12-08 | Product Management |
| Soja Isolate Premiumqualität | IC-17407 | 2023-01-18 | Data Governance |
| SIG-71-KJM-D5G1 Holdings | BC-17425 | 2023-05-03 | Operations |
| Sodium Benzoate Technical | BC-17458 | 2024-06-06 | Product Management |
| Citric Acid 99.5% | IC-17460 | 2022-08-07 | Compliance |
| Coconut Oil 70% | TC-17464 | 2024-08-07 | Data Governance |
| SIG-89-HLJ-NILC | IC-17479 | 2021-11-01 | IT Infrastructure |
| palm oil 50% | IC-17510 | 2023-07-13 | Supply Chain |
| Pea Protein 98% Grade B | BC-17519 | 2023-12-13 | Finance |
| Coconut Oil Pharma Grade | IC-17534 | 2021-12-18 | Compliance |
| global chemicals SARL | TC-17542 | 2024-07-26 | Data Governance |
| Sodium Chloride | TC-17571 | 2022-01-04 | Supply Chain |
| VE-MA-682 | BC-17576 | 2024-10-17 | Finance |
| SIG-56-FFG-XS2P | IC-17577 | 2023-03-02 | Operations |
| Wheat Gluten Grade A | TC-17595 | 2024-06-16 | IT Infrastructure |
| LA-AC-GR-A-486 | TC-17600 | 2022-04-03 | Supply Chain |
| SIG-41-VXU-J3AN | TC-17615 | 2022-05-16 | Operations |
| potassium sorbate | BC-17627 | 2023-12-22 | Product Management |
| Sonnenblumenöl Standardqualität | IC-17642 | 2022-04-28 | IT Infrastructure |
| lactic acid standard | BC-17651 | 2023-08-14 | IT Infrastructure |
| Wheat Gluten | IC-17671 | 2021-02-15 | Compliance |
| Traubenzucker 25% | TC-17680 | 2023-05-16 | Product Management |
| Traubenzucker 25% | BC-17712 | 2024-07-12 | Operations |
| AT-SO-658 | TC-17724 | 2022-03-01 | Data Governance |
| Prism Materials | BC-17726 | 2024-05-14 | IT Infrastructure |
| Vanguard Handel LLC | IC-17750 | 2022-08-25 | Data Governance |
| CO-MA-371 | IC-17765 | 2024-03-21 | Compliance |
| SIG-39-IRP-PQZF | TC-17771 | 2024-01-06 | Compliance |
| SIG-39-BAT-DD7R | TC-17774 | 2021-05-22 | IT Infrastructure |
| CY-577 | BC-17795 | 2021-02-03 | Product Management |
| quantum processing SARL | IC-17806 | 2021-08-04 | Supply Chain |
| pea protein 70% premium | IC-17810 | 2024-07-05 | Product Management |
| Pea Protein Premiumqualität | TC-17828 | 2024-03-05 | IT Infrastructure |
| CI-AC-PR-827 | TC-17835 | 2021-02-06 | Compliance |
| casein | BC-17850 | 2023-12-09 | Supply Chain |
| Maltodextrin DE10 | TC-17856 | 2022-05-23 | IT Infrastructure |
| Kaliumsorbat 98% | IC-17859 | 2023-03-19 | Finance |
| sunflower oil 50% pharma grade | IC-17861 | 2021-12-20 | Product Management |
| Atlas Partners | TC-17864 | 2023-01-13 | Finance |
| Stellar Manufacturing Group | BC-17878 | 2023-10-13 | Supply Chain |
| Zenith Manufacturing Holdings | TC-17896 | 2024-07-10 | Compliance |
| customs duty fr 25% | TC-17908 | 2023-04-28 | Operations |
| potassium sorbate standard | TC-17919 | 2023-09-24 | Compliance |
| Citric Acid Food Grade | BC-17921 | 2023-10-05 | Operations |
| Wheat Gluten Grade B | TC-17950 | 2021-02-05 | Operations |
| Stellar Processing Holdings | IC-17978 | 2022-06-18 | Supply Chain |
| SIG-64-VAK-3T2G AG | TC-17980 | 2022-03-15 | IT Infrastructure |
| Palmfett 70% Technische Qualität | TC-17983 | 2021-11-02 | IT Infrastructure |
| Pinnacle Ingredients KG | BC-17995 | 2024-02-27 | Supply Chain |
| FR-GR-A-600 | IC-18000 | 2024-06-25 | Compliance |
| Sorbinsäure Lebensmittelrein | BC-18006 | 2024-11-26 | Compliance |
| CU-DU-B-21-305 | IC-18008 | 2024-05-11 | Data Governance |
| SIG-39-OZI-N968 | TC-18011 | 2023-11-18 | IT Infrastructure |
| Elite Handel Corp. | IC-18015 | 2022-01-21 | Data Governance |
| Ascorbic Acid Premiumqualität | IC-18018 | 2024-03-03 | Product Management |
| Nexus Processing Holdings | BC-18019 | 2024-09-16 | Product Management |
| Apex Commodities Holdings | TC-18048 | 2021-03-05 | Product Management |
| ZE-MA-316 | IC-18052 | 2021-08-03 | Compliance |
| SIG-39-UPB-Q8DA | IC-18055 | 2024-01-09 | Data Governance |
| SIG-39-JXL-BQ85 SARL | IC-18064 | 2023-01-04 | Data Governance |
| SIG-97-SBT-Y595 | BC-18078 | 2021-11-03 | Data Governance |
| Soy Isolate Grade B | IC-18081 | 2023-09-05 | Compliance |
| SIG-41-ZGH-C0Y2 Holdings | IC-18083 | 2023-07-19 | Product Management |
| potassium sorbate 98% | TC-18107 | 2021-02-23 | IT Infrastructure |
| SIG-61-XKV-ODPX | TC-18118 | 2023-09-17 | Operations |
| Continental Supply Co. | TC-18133 | 2023-10-20 | Supply Chain |
| SIG-92-KFT-DU1S | BC-18136 | 2024-04-18 | Supply Chain |
| citric acid 99.5% | BC-18144 | 2022-01-24 | Compliance |
| SO-IS-432 | TC-18154 | 2021-12-02 | Compliance |
| Glucose Syrup 99.5% Grade B | IC-18176 | 2024-06-16 | IT Infrastructure |
| central materials | BC-18217 | 2023-12-16 | Compliance |
| calcium carbonate standard | BC-18222 | 2022-12-08 | IT Infrastructure |
| Dextrose | IC-18227 | 2021-04-25 | Product Management |
| CA-CO-939 | IC-18228 | 2021-04-04 | Product Management |
| prism materials | TC-18244 | 2022-02-27 | Finance |
| Stratos Versorgung GmbH | BC-18246 | 2021-03-08 | Supply Chain |
| Traubenzucker Technische Qualität | BC-18248 | 2024-09-08 | Product Management |
| EX-B-0-514 | TC-18260 | 2023-12-09 | Compliance |
| Resistente Stärke Technische Qualität | TC-18276 | 2024-07-07 | Product Management |
| CO-PA-491 BV | IC-18283 | 2023-01-24 | IT Infrastructure |
| Fructose Grade B | TC-18287 | 2023-08-14 | Product Management |
| Dextrin 70% Pharma Grade | TC-18290 | 2022-02-06 | Finance |
| Sonnenblumenöl Qualitätsstufe I | TC-18303 | 2022-07-22 | Compliance |
| SIG-60-TMF-XHW0 | BC-18307 | 2023-12-12 | IT Infrastructure |
| Catalyst Supply Holdings | IC-18315 | 2023-03-01 | Product Management |
| PA-OI-98-587 | BC-18320 | 2024-09-21 | Compliance |
| FR-TE-414 | IC-18334 | 2023-01-19 | IT Infrastructure |
| Lactic Acid Technische Qualität | IC-18347 | 2024-06-28 | Supply Chain |
| Stellar Sourcing | BC-18360 | 2024-07-25 | Data Governance |
| prism ingredients AG | IC-18363 | 2024-01-14 | Finance |
| Core Logistik Holdings | IC-18371 | 2024-09-24 | IT Infrastructure |
| RA-OI-70-PR-405 | TC-18377 | 2023-11-07 | IT Infrastructure |
| Dextrose Grade B | IC-18378 | 2022-08-09 | Product Management |
| SIG-38-CEJ-1ISY | IC-18404 | 2024-11-25 | Finance |
| SIG-80-GVE-ZK1G | BC-18411 | 2022-11-08 | Compliance |
| Customs Duty US 19% | TC-18419 | 2021-08-17 | Compliance |
| dextrin premium | IC-18422 | 2023-08-07 | Operations |
| Coconut Oil 25% Food Grade | BC-18430 | 2024-12-21 | Data Governance |
| SIG-82-DVA-0TXE | TC-18432 | 2022-08-01 | Finance |
| Zenith Processing | TC-18448 | 2023-12-19 | Compliance |
| Soy Isolate 25% Pharma Grade | BC-18455 | 2022-02-07 | IT Infrastructure |
| SIG-36-BVE-5U7D | IC-18465 | 2022-11-16 | Finance |
| SIG-84-VYG-QI55 | TC-18469 | 2024-10-17 | Finance |
| LA-AC-554 | BC-18503 | 2021-08-04 | Compliance |
| Vat Reduced GB 20% | TC-18524 | 2024-03-22 | Data Governance |
| Traubenzucker 99.5% Qualitätsstufe II | IC-18535 | 2024-06-25 | Finance |
| Pea Protein 25% Pharma Grade | BC-18542 | 2022-04-21 | Operations |
| SIG-45-CWR-EI9N | BC-18545 | 2023-08-12 | Supply Chain |
| Lactic Acid 98% | TC-18558 | 2024-07-11 | Supply Chain |
| MA-DE-700 | BC-18562 | 2021-11-21 | Product Management |
| vat standard nl 5% | BC-18591 | 2021-09-06 | Operations |
| AS-AC-279 | TC-18593 | 2023-02-06 | Product Management |
| SIG-99-CEZ-35MR | BC-18594 | 2023-02-28 | Data Governance |
| SIG-71-PGT-OFPC | IC-18619 | 2022-11-21 | Operations |
| atlantic manufacturing Group | TC-18628 | 2024-03-20 | Compliance |
| pinnacle logistics International | TC-18638 | 2023-09-28 | Supply Chain |
| SIG-51-LVQ-VS8Q | TC-18657 | 2021-05-16 | Data Governance |
| vat reduced br 21% | TC-18660 | 2022-03-14 | IT Infrastructure |
| Vat Reduced NL 25% | TC-18685 | 2023-05-21 | Data Governance |
| Atlantic Verarbeitung Holdings | IC-18688 | 2021-07-10 | IT Infrastructure |
| Ascorbic Acid Technical | IC-18692 | 2021-02-26 | Data Governance |
| withholding nl 7% | BC-18693 | 2023-12-13 | IT Infrastructure |
| Calcium Carbonate 98% Pharmazeutisch rein | TC-18732 | 2024-11-01 | Product Management |
| CO-MA-245 | TC-18741 | 2022-04-28 | Finance |
| NO-IN-670 International | TC-18745 | 2023-06-20 | Product Management |
| Lactic Acid 50% Grade A | BC-18752 | 2023-05-15 | Product Management |
| horizon partners Ltd. | TC-18785 | 2024-01-11 | Data Governance |
| Potassium Sorbate Grade A | BC-18800 | 2022-07-28 | Supply Chain |
| Natriumbenzoat | BC-18810 | 2023-04-27 | IT Infrastructure |
| Atlas Ingredients Ltd. | TC-18819 | 2023-06-09 | Operations |
| Quantum Versorgung GmbH | TC-18835 | 2021-06-24 | IT Infrastructure |
| potassium sorbate tech grade | TC-18839 | 2023-04-02 | Data Governance |
| SIG-81-SBE-HL1C | IC-18846 | 2022-12-04 | Compliance |
| SIG-93-ZCF-6HM3 | IC-18856 | 2024-03-23 | IT Infrastructure |
| Prime Logistics | TC-18858 | 2022-12-27 | Finance |
| Premier Supply Co. | TC-18859 | 2024-06-28 | Operations |
| SIG-29-BJH-NXI0 | BC-18860 | 2022-11-01 | Data Governance |
| fructose | IC-18862 | 2021-10-19 | IT Infrastructure |
| AT-PA-589 | BC-18880 | 2024-05-11 | Data Governance |
| SIG-43-GRJ-P3HT | TC-18883 | 2022-01-21 | Operations |
| EX-N-15-178 | IC-18884 | 2023-09-12 | Supply Chain |
| Lactic Acid | IC-18888 | 2023-09-04 | IT Infrastructure |
| Vat Standard US 19% | BC-18892 | 2021-09-14 | Compliance |
| SIG-18-CIG-ZUL8 Holdings | TC-18928 | 2022-03-16 | Compliance |
| SIG-76-IIX-V2Y9 | TC-18965 | 2024-04-13 | Product Management |
| palm oil standard | TC-18973 | 2022-10-07 | Finance |
| Prism Versorgung GmbH | IC-18991 | 2021-01-17 | Data Governance |
| zenith trading GmbH | BC-18992 | 2021-10-12 | Supply Chain |
| RE-ST-TE-614 | IC-19000 | 2023-11-18 | Finance |
| calcium carbonate 25% pharma grade | IC-19018 | 2022-12-10 | Data Governance |
| Fructose | IC-19043 | 2022-11-12 | IT Infrastructure |
| Fructose 70% | IC-19044 | 2024-11-21 | Compliance |
| NO-LO-114 Ltd. | TC-19052 | 2021-06-27 | Compliance |
| Isoglucose | TC-19068 | 2022-02-11 | Finance |
| isoglucose 70% | BC-19082 | 2021-10-12 | Supply Chain |
| PI-SO-251 | TC-19084 | 2023-05-03 | Operations |
| SIG-92-ZTO-VZGU | IC-19094 | 2023-06-01 | Data Governance |
| Prism Sourcing | IC-19107 | 2023-01-22 | Supply Chain |
| Natriumchlorid 98% | TC-19120 | 2024-04-17 | Operations |
| Prime Materials | IC-19131 | 2024-06-08 | IT Infrastructure |
| horizon logistics PLC | BC-19138 | 2023-02-23 | Compliance |
| Natriumbenzoat 25% | TC-19160 | 2023-02-20 | IT Infrastructure |
| quantum supply | IC-19169 | 2021-04-12 | Supply Chain |
| potassium sorbate 98% | TC-19175 | 2023-02-25 | Operations |
| glucose syrup | BC-19179 | 2024-10-16 | Supply Chain |
| PA-OI-50-273 | IC-19188 | 2022-09-28 | Product Management |
| GL-SO-534 Holdings | TC-19200 | 2021-01-23 | Compliance |
| Vat Reduced GB 20% | TC-19205 | 2021-08-11 | Data Governance |
| WH-GL-GR-A-924 | IC-19222 | 2023-01-10 | IT Infrastructure |
| Global Logistics | TC-19225 | 2023-08-23 | Data Governance |
| SIG-23-NOR-OPI3 | BC-19230 | 2021-03-06 | Compliance |
| Baltic Sourcing | IC-19233 | 2023-01-18 | Finance |
| CO-PA-308 | IC-19237 | 2022-08-02 | Operations |
| SIG-64-IEU-FRGN | IC-19240 | 2022-06-25 | Product Management |
| SIG-10-NNQ-6CGO | TC-19247 | 2022-09-25 | Product Management |
| Lactic Acid | BC-19273 | 2021-01-19 | Compliance |
| citric acid 99.5% | TC-19274 | 2023-12-02 | Data Governance |
| Fructose 70% | TC-19278 | 2023-06-14 | Data Governance |
| Sonnenblumenöl Pharmazeutisch rein | BC-19299 | 2023-06-20 | Supply Chain |
| Potassium Sorbate 98% Grade B | BC-19310 | 2022-05-14 | IT Infrastructure |
| Pinnacle Enterprise AG | TC-19318 | 2024-05-01 | Finance |
| CE-PR-134 | BC-19323 | 2022-09-16 | Supply Chain |
| Rapsöl 50% Pharmazeutisch rein | BC-19341 | 2024-12-15 | Supply Chain |
| PO-SO-50-GR-B-154 | TC-19357 | 2021-03-28 | Operations |
| vertex materials | IC-19358 | 2022-12-03 | Operations |
| glucose syrup 99.5% food grade | IC-19385 | 2022-01-12 | Compliance |
| AT-CH-905 Holdings | BC-19386 | 2021-03-10 | Finance |
| vat standard de 25% | IC-19408 | 2024-12-10 | Compliance |
| Vanguard Logistik International | BC-19418 | 2022-09-02 | Compliance |
| SIG-77-WZV-TKWL | BC-19435 | 2021-06-01 | Data Governance |
| Wheat Gluten Grade A | TC-19439 | 2023-11-13 | Supply Chain |
| nexus distribution Corp. | IC-19448 | 2022-01-19 | Finance |
| Vat Reduced GB 19% | TC-19488 | 2023-09-06 | Compliance |
| customs duty nl 21% | BC-19491 | 2021-04-27 | Data Governance |
| SIG-97-UWA-JWLN | IC-19540 | 2021-05-21 | Product Management |
| Pinnacle Industries SAS | IC-19544 | 2022-04-19 | Operations |
| Customs Duty IN 20% | TC-19548 | 2023-11-20 | Compliance |
| SIG-60-RUC-CU6A | IC-19554 | 2023-03-10 | Supply Chain |
| Sodium Benzoate 50% | BC-19560 | 2023-06-25 | Supply Chain |
| Atlantic Processing International | TC-19562 | 2021-07-05 | Compliance |
| pea protein standard | TC-19563 | 2024-08-08 | Compliance |
| lactic acid food grade | IC-19571 | 2024-07-14 | IT Infrastructure |
| ME-SO-760 GmbH | IC-19576 | 2021-10-20 | Supply Chain |
| Apex Handel International | TC-19577 | 2024-02-04 | Product Management |
| Coconut Oil 25% Technical | IC-19582 | 2022-05-26 | Operations |
| SIG-44-HTV-P84J | IC-19610 | 2024-08-11 | Operations |
| PE-PR-25-185 | TC-19615 | 2022-04-01 | Product Management |
| rapeseed oil tech grade | IC-19644 | 2024-07-11 | IT Infrastructure |
| Sodium Benzoate 25% Standard | BC-19646 | 2024-07-10 | IT Infrastructure |
| Glucose Syrup 25% | TC-19649 | 2022-10-16 | Compliance |
| Natriumchlorid Technische Qualität | BC-19669 | 2022-05-08 | IT Infrastructure |
| SO-BE-824 | BC-19672 | 2024-09-13 | Product Management |
| Zitronensäure 70% | IC-19674 | 2023-01-18 | Compliance |
| PI-PR-193 | IC-19686 | 2023-11-02 | Product Management |
| Atlantic Partners SARL | TC-19690 | 2023-09-13 | Operations |
| Premier Solutions Inc. | IC-19691 | 2024-07-02 | Operations |
| sorbic acid | IC-19714 | 2023-09-16 | Compliance |
| SIG-63-NTB-209C | IC-19730 | 2024-08-12 | Product Management |
| Potassium Sorbate | BC-19735 | 2021-07-13 | Supply Chain |
| prime solutions | IC-19749 | 2024-04-24 | Compliance |
| PE-PR-929 | IC-19755 | 2023-06-03 | Finance |
| Resistant Starch Technical | BC-19761 | 2022-01-09 | Data Governance |
| Stellar Logistics | BC-19774 | 2023-06-23 | Data Governance |
| PR-IN-409 LLC | TC-19787 | 2024-05-08 | Operations |
| CO-PA-491 BV | BC-19788 | 2024-05-04 | Finance |
| Calcium Carbonate 50% Food Grade | TC-19812 | 2022-05-02 | Operations |
| SIG-20-IMA-GJKF | TC-19818 | 2021-02-01 | Operations |
| SIG-25-ABB-2SBA | IC-19825 | 2024-01-06 | Supply Chain |
| SIG-86-ZYB-L8NP BV | BC-19828 | 2022-08-13 | Compliance |
| Kaliumsorbat 50% Technische Qualität | IC-19845 | 2022-09-01 | Operations |
| Dextrose 25% | IC-19861 | 2022-12-20 | IT Infrastructure |
| pea protein standard | BC-19865 | 2024-07-16 | Finance |
| casein 50% premium | BC-19883 | 2024-07-22 | Finance |
| LA-AC-25-819 | TC-19886 | 2022-09-15 | Operations |
| Vanguard Ingredients | BC-19890 | 2024-05-18 | IT Infrastructure |
| calcium carbonate | IC-19912 | 2023-01-06 | Compliance |
| Withholding NL 10% | TC-19920 | 2022-10-10 | Finance |
| Sodium Benzoate 99.5% Technical | IC-19924 | 2023-05-18 | Product Management |
| AT-MA-510 | IC-19928 | 2023-04-12 | Compliance |
| SIG-82-VDF-0XQT | BC-19933 | 2021-09-19 | Product Management |
| Baltic Sourcing | IC-19944 | 2021-08-08 | Compliance |
| Glukosesirup Syrup | IC-19947 | 2021-02-07 | Operations |
| Sorbinsäure | BC-19951 | 2021-03-08 | Compliance |
| LA-AC-471 | TC-19958 | 2023-07-09 | Data Governance |
| apex logistics | IC-19967 | 2024-01-17 | IT Infrastructure |
| NE-LO-300 | IC-19972 | 2024-04-18 | Finance |
| ascorbic acid | TC-19995 | 2021-02-11 | IT Infrastructure |
| Vertex Chemicals Holdings | TC-20024 | 2024-03-23 | IT Infrastructure |
| SIG-51-MVX-XKUB | TC-20037 | 2021-11-23 | IT Infrastructure |
| Calcium Carbonate 98% Standardqualität | IC-20067 | 2023-06-06 | Operations |
| GL-LO-494 | IC-20070 | 2021-01-02 | Compliance |
| dextrose 99.5% standard | TC-20107 | 2022-12-20 | Supply Chain |
| Glucose Syrup 98% Standard | IC-20124 | 2023-02-28 | Compliance |
| SO-IS-975 | TC-20130 | 2022-07-25 | Supply Chain |
| Glucose Syrup 98% | TC-20132 | 2022-04-05 | Product Management |
| apex materials Group | IC-20137 | 2024-09-08 | Product Management |
| SIG-68-LYO-7YQ5 | BC-20138 | 2021-10-01 | Product Management |
| SIG-58-HNG-1XJ7 | IC-20141 | 2021-08-06 | Compliance |
| SIG-54-BLS-33OX | IC-20143 | 2023-01-06 | Product Management |
| VA-RE-N-20-326 | IC-20146 | 2024-03-02 | Data Governance |
| SIG-43-XDN-7VEU | IC-20163 | 2022-11-09 | Finance |
| EX-F-25-579 | TC-20180 | 2024-05-16 | Finance |
| PR-LO-420 | BC-20212 | 2024-07-15 | Data Governance |
| SIG-48-GDK-Y8XN | IC-20236 | 2021-06-11 | Operations |
| Stratos Chemicals | BC-20238 | 2021-02-23 | Supply Chain |
| SIG-57-QDA-RQ8R | TC-20256 | 2021-11-13 | Product Management |
| CY-TE-117 | IC-20257 | 2024-12-18 | IT Infrastructure |
| SIG-60-OBI-GVJP | TC-20265 | 2021-02-01 | Operations |
| Quantum Supply Co. | IC-20271 | 2023-07-25 | Supply Chain |
| Vat Reduced BR 10% | TC-20297 | 2021-03-04 | Supply Chain |
| VA-LO-948 | IC-20301 | 2022-05-21 | IT Infrastructure |
| SIG-45-ZHK-QWIG | BC-20311 | 2024-06-23 | IT Infrastructure |
| CA-ST-375 | IC-20322 | 2021-09-06 | IT Infrastructure |
| Wheat Gluten 25% Standard | BC-20324 | 2021-06-28 | IT Infrastructure |
| Cyclodextrin | BC-20327 | 2021-10-11 | Supply Chain |
| Stratos Chemicals | IC-20332 | 2024-07-05 | Finance |
| wheat gluten standard | BC-20344 | 2023-05-10 | Supply Chain |
| fructose premium | BC-20346 | 2024-05-25 | Product Management |
| VA-SU-CO-459 | IC-20355 | 2024-07-25 | Supply Chain |
| palm oil 50% | BC-20392 | 2022-10-14 | Product Management |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| SIG-65-EFS-5P03 | IC-7677 | SUPERSEDED | Historical - verify before use |
| Horizon Industrien GmbH | IC-9256 | DEPRECATED | Historical - verify before use |
| SO-CH-752 | IC-5910 | REVIEW REQUIRED | Historical - verify before use |
| SIG-37-ZOD-1VME | IC-5697 | REVIEW REQUIRED | Historical - verify before use |
| DE-GR-A-512 | IC-7484 | PROVISIONAL | Historical - verify before use |
| Prism Industrien Holdings | IC-5454 | REVIEW REQUIRED | Historical - verify before use |
| SIG-78-WDE-NNV9 | IC-6030 | PROVISIONAL | Historical - verify before use |
| Pea Protein 99.5% | IC-8617 | SUPERSEDED | Historical - verify before use |
| FR-PR-346 | IC-5722 | SUPERSEDED | Historical - verify before use |
| Nexus Materials | IC-6584 | DEPRECATED | Historical - verify before use |
| Meridian Versorgung GmbH | IC-9941 | PROVISIONAL | Historical - verify before use |
| Nexus Sourcing | IC-9408 | DEPRECATED | Historical - verify before use |
| SIG-68-HOK-ETCC | IC-9553 | REVIEW REQUIRED | Historical - verify before use |
| Fructose | IC-7702 | REVIEW REQUIRED | Historical - verify before use |
| VE-IN-631 Ltd. | IC-8052 | PROVISIONAL | Historical - verify before use |
| Rapsöl Qualitätsstufe I | IC-9190 | PROVISIONAL | Historical - verify before use |
| Maltodextrin DE30 Standard | IC-5378 | REVIEW REQUIRED | Historical - verify before use |
| Vanguard Logistik SA | IC-5052 | SUPERSEDED | Historical - verify before use |
| Isoglucose Qualitätsstufe II | IC-6219 | DEPRECATED | Historical - verify before use |
| core supply | IC-8545 | REVIEW REQUIRED | Historical - verify before use |
| VA-IN-429 | IC-5301 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-50-PH-GR-568 | IC-9105 | REVIEW REQUIRED | Historical - verify before use |
| elite logistics | IC-9737 | DEPRECATED | Historical - verify before use |
| ascorbic acid | IC-5720 | DEPRECATED | Historical - verify before use |
| Meridian Enterprise | IC-7228 | DEPRECATED | Historical - verify before use |
| pinnacle distribution Ltd. | IC-5719 | PROVISIONAL | Historical - verify before use |
| CU-DU-G-0-770 | IC-5223 | REVIEW REQUIRED | Historical - verify before use |
| Zenith Versorgung GmbH | IC-6162 | SUPERSEDED | Historical - verify before use |
| sodium chloride 98% pharma grade | IC-7774 | REVIEW REQUIRED | Historical - verify before use |
| Wheat Gluten 50% | IC-9494 | SUPERSEDED | Historical - verify before use |
| CY-577 | IC-5405 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid 98% | IC-5312 | DEPRECATED | Historical - verify before use |
| pea protein standard | IC-6234 | SUPERSEDED | Historical - verify before use |
| Dextrin 50% | IC-9243 | PROVISIONAL | Historical - verify before use |
| Central Commodities Ltd. | IC-8980 | DEPRECATED | Historical - verify before use |
| SIG-17-OVA-CCDM | IC-8572 | PROVISIONAL | Historical - verify before use |
| SIG-39-EWA-Q37M | IC-7783 | REVIEW REQUIRED | Historical - verify before use |
| palm oil 50% | IC-8031 | PROVISIONAL | Historical - verify before use |
| sodium benzoate premium | IC-7539 | PROVISIONAL | Historical - verify before use |
| Isoglucose 50% Lebensmittelrein | IC-6054 | PROVISIONAL | Historical - verify before use |
| pacific materials GmbH | IC-6356 | PROVISIONAL | Historical - verify before use |
| Dextrin Technical | IC-6314 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid | IC-5079 | DEPRECATED | Historical - verify before use |
| Vat Standardqualität GB 15% | IC-9186 | PROVISIONAL | Historical - verify before use |
| atlantic materials | IC-8954 | REVIEW REQUIRED | Historical - verify before use |
| Fructose | IC-5619 | REVIEW REQUIRED | Historical - verify before use |
| SIG-42-HBL-L3KU International | IC-6106 | PROVISIONAL | Historical - verify before use |
| sodium chloride 70% | IC-6571 | REVIEW REQUIRED | Historical - verify before use |
| Pea Protein | IC-6396 | PROVISIONAL | Historical - verify before use |
| Atlantic Commodities | IC-8617 | REVIEW REQUIRED | Historical - verify before use |
| CA-PH-GR-524 | IC-6502 | SUPERSEDED | Historical - verify before use |
| SIG-71-CWF-DGP5 | IC-9374 | SUPERSEDED | Historical - verify before use |
| MA-DE-146 | IC-6197 | PROVISIONAL | Historical - verify before use |
| resistant starch food grade | IC-9869 | SUPERSEDED | Historical - verify before use |
| CO-OI-25-ST-613 | IC-5391 | PROVISIONAL | Historical - verify before use |
| SIG-51-KQC-QY9M | IC-5643 | REVIEW REQUIRED | Historical - verify before use |
| PA-MA-412 GmbH | IC-7001 | PROVISIONAL | Historical - verify before use |
| Sodium Benzoate Grade A | IC-7213 | SUPERSEDED | Historical - verify before use |
| PR-CO-481 International | IC-6688 | DEPRECATED | Historical - verify before use |
| prism industries International | IC-7124 | DEPRECATED | Historical - verify before use |
| cyclodextrin premium | IC-5551 | REVIEW REQUIRED | Historical - verify before use |
| SIG-54-ZFB-4REP Inc. | IC-5796 | DEPRECATED | Historical - verify before use |
| SIG-83-BZY-VHAE | IC-8195 | SUPERSEDED | Historical - verify before use |
| Palmfett | IC-7183 | PROVISIONAL | Historical - verify before use |
| SIG-65-BMI-KAWJ Holdings | IC-6042 | DEPRECATED | Historical - verify before use |
| SIG-50-QXM-GFI4 | IC-8166 | SUPERSEDED | Historical - verify before use |
| Prism Versorgung GmbH | IC-9140 | REVIEW REQUIRED | Historical - verify before use |
| Sorbinsäure | IC-9945 | PROVISIONAL | Historical - verify before use |
| sodium benzoate 50% | IC-6864 | DEPRECATED | Historical - verify before use |
| ST-PA-227 PLC | IC-6715 | REVIEW REQUIRED | Historical - verify before use |
| AS-AC-GR-B-855 | IC-7158 | PROVISIONAL | Historical - verify before use |
| SIG-44-HLB-IC48 SARL | IC-9206 | PROVISIONAL | Historical - verify before use |
| Rapeseed Oil | IC-7988 | REVIEW REQUIRED | Historical - verify before use |
| Potassium Sorbate 50% Technical | IC-9312 | DEPRECATED | Historical - verify before use |
| CY-892 | IC-5174 | DEPRECATED | Historical - verify before use |
| SIG-39-WTU-81JC | IC-8683 | REVIEW REQUIRED | Historical - verify before use |
| Core Logistics | IC-8189 | REVIEW REQUIRED | Historical - verify before use |
| SIG-26-HEJ-USUB Group | IC-5476 | SUPERSEDED | Historical - verify before use |
| SIG-47-QLD-IL46 | IC-9181 | PROVISIONAL | Historical - verify before use |
| Maltodextrin-Pulver DE15 | IC-5317 | REVIEW REQUIRED | Historical - verify before use |
| Pinnacle Sourcing | IC-5811 | DEPRECATED | Historical - verify before use |
| potassium sorbate | IC-5482 | PROVISIONAL | Historical - verify before use |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | IC-8228 | PROVISIONAL | Historical - verify before use |
| Sorbinsäure Premiumqualität | IC-9380 | SUPERSEDED | Historical - verify before use |
| Soja Isolate 25% Technische Qualität | IC-5835 | PROVISIONAL | Historical - verify before use |
| glucose syrup 25% | IC-6718 | DEPRECATED | Historical - verify before use |
| Traubenzucker Qualitätsstufe I | IC-9133 | PROVISIONAL | Historical - verify before use |
| WH-GL-GR-B-129 | IC-8961 | REVIEW REQUIRED | Historical - verify before use |
| Soja Isolate 98% Premiumqualität | IC-9769 | SUPERSEDED | Historical - verify before use |
| NO-MA-529 | IC-8714 | REVIEW REQUIRED | Historical - verify before use |
| SIG-86-JBA-HCDI | IC-5762 | SUPERSEDED | Historical - verify before use |
| Horizon Ingredients BV | IC-6180 | DEPRECATED | Historical - verify before use |
| Atlantic Industrien International | IC-6368 | REVIEW REQUIRED | Historical - verify before use |
| BA-IN-585 SARL | IC-6207 | REVIEW REQUIRED | Historical - verify before use |
| Atlantic Trading BV | IC-7953 | PROVISIONAL | Historical - verify before use |
| Isoglucose Lebensmittelrein | IC-7367 | DEPRECATED | Historical - verify before use |
| PE-PR-163 | IC-8456 | REVIEW REQUIRED | Historical - verify before use |
| SIG-27-KMU-WPWH GmbH | IC-8229 | REVIEW REQUIRED | Historical - verify before use |
| sodium benzoate 98% | IC-9939 | REVIEW REQUIRED | Historical - verify before use |
| Stratos Commodities International | IC-8909 | DEPRECATED | Historical - verify before use |
| Rapsöl 70% Premiumqualität | IC-5807 | SUPERSEDED | Historical - verify before use |
| SIG-42-AYY-K71K | IC-9191 | PROVISIONAL | Historical - verify before use |
| Premier Logistics | IC-7446 | DEPRECATED | Historical - verify before use |
| baltic solutions Group | IC-8298 | SUPERSEDED | Historical - verify before use |
| SO-CH-99.5-GR-A-206 | IC-6484 | REVIEW REQUIRED | Historical - verify before use |
| IS-FO-GR-555 | IC-9987 | PROVISIONAL | Historical - verify before use |
| Casein Standard | IC-9484 | SUPERSEDED | Historical - verify before use |
| SIG-45-GXT-XIBF | IC-9965 | DEPRECATED | Historical - verify before use |
| Atlantic Manufacturing | IC-8999 | DEPRECATED | Historical - verify before use |
| ascorbic acid | IC-7331 | REVIEW REQUIRED | Historical - verify before use |
| SIG-47-YTF-UPMT | IC-6567 | SUPERSEDED | Historical - verify before use |
| sodium chloride 99.5% premium | IC-8498 | REVIEW REQUIRED | Historical - verify before use |
| Rapsöl Lebensmittelrein | IC-7945 | REVIEW REQUIRED | Historical - verify before use |
| Dextrose 70% Grade A | IC-8980 | PROVISIONAL | Historical - verify before use |
| SIG-93-FDC-Q685 | IC-7538 | REVIEW REQUIRED | Historical - verify before use |
| SIG-86-QTB-N3VO International | IC-6958 | REVIEW REQUIRED | Historical - verify before use |
| Prism Materials Ltd. | IC-8469 | SUPERSEDED | Historical - verify before use |
| zenith logistics | IC-7605 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-PR-679 | IC-6163 | DEPRECATED | Historical - verify before use |
| Vat Standard NL 19% | IC-9857 | DEPRECATED | Historical - verify before use |
| Atlantic Chemicals SAS | IC-6148 | SUPERSEDED | Historical - verify before use |
| SIG-27-GRI-K7JV | IC-6711 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid Premiumqualität | IC-5299 | REVIEW REQUIRED | Historical - verify before use |
| PI-LO-946 | IC-7371 | PROVISIONAL | Historical - verify before use |
| AT-CH-905 Holdings | IC-7183 | REVIEW REQUIRED | Historical - verify before use |
| SIG-12-JLN-YFH3 | IC-6506 | SUPERSEDED | Historical - verify before use |
| CO-MA-993 Corp. | IC-6393 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-463 | IC-5963 | PROVISIONAL | Historical - verify before use |
| Isoglucose | IC-5459 | SUPERSEDED | Historical - verify before use |
| PR-CH-121 KG | IC-7705 | DEPRECATED | Historical - verify before use |
| Central Sourcing | IC-9504 | PROVISIONAL | Historical - verify before use |
| meridian logistics | IC-6274 | PROVISIONAL | Historical - verify before use |
| Citric Acid 25% Technical | IC-8305 | PROVISIONAL | Historical - verify before use |
| PA-MA-324 | IC-7326 | REVIEW REQUIRED | Historical - verify before use |
| AP-SU-CO-755 | IC-8848 | PROVISIONAL | Historical - verify before use |
| Elite Sourcing | IC-5924 | SUPERSEDED | Historical - verify before use |
| Vat Reduced BR 19% | IC-5243 | DEPRECATED | Historical - verify before use |
| Sunflower Oil 50% Pharma Grade | IC-5130 | SUPERSEDED | Historical - verify before use |
| atlantic ingredients | IC-7848 | REVIEW REQUIRED | Historical - verify before use |
| SIG-57-YOY-F7N2 | IC-7539 | SUPERSEDED | Historical - verify before use |
| Sodium Benzoate 99.5% Technical | IC-5915 | SUPERSEDED | Historical - verify before use |
| CO-MA-295 | IC-9373 | PROVISIONAL | Historical - verify before use |
| Zitronensäure Qualitätsstufe I | IC-7666 | SUPERSEDED | Historical - verify before use |
| SIG-23-LAS-L2MX Holdings | IC-8820 | REVIEW REQUIRED | Historical - verify before use |
| dextrin | IC-7403 | DEPRECATED | Historical - verify before use |
| EX-U-7-320 | IC-9183 | REVIEW REQUIRED | Historical - verify before use |
| Fructose Technical | IC-6168 | DEPRECATED | Historical - verify before use |
| calcium carbonate | IC-8005 | REVIEW REQUIRED | Historical - verify before use |
| Glucose Syrup Technical | IC-6566 | DEPRECATED | Historical - verify before use |
| SIG-23-BLM-EZKX | IC-8710 | SUPERSEDED | Historical - verify before use |
| Dextrin Technical | IC-8847 | REVIEW REQUIRED | Historical - verify before use |
| sorbic acid 98% | IC-7945 | DEPRECATED | Historical - verify before use |
| Premier Logistics | IC-7196 | PROVISIONAL | Historical - verify before use |
| sodium benzoate 98% | IC-7029 | DEPRECATED | Historical - verify before use |
| VE-SO-701 | IC-7139 | DEPRECATED | Historical - verify before use |
| SIG-36-ZWC-F2K1 | IC-9153 | REVIEW REQUIRED | Historical - verify before use |
| SIG-61-IQH-EKWH | IC-9037 | PROVISIONAL | Historical - verify before use |
| Zitronensäure | IC-5546 | PROVISIONAL | Historical - verify before use |
| Maltodextrin-Pulver DE10 | IC-8350 | DEPRECATED | Historical - verify before use |
| sodium chloride tech grade | IC-7774 | SUPERSEDED | Historical - verify before use |
| Isoglucose | IC-6161 | PROVISIONAL | Historical - verify before use |
| Weizenklebereiweiß Lebensmittelrein | IC-8836 | REVIEW REQUIRED | Historical - verify before use |
| wheat gluten pharma grade | IC-5556 | REVIEW REQUIRED | Historical - verify before use |
| baltic processing | IC-7034 | REVIEW REQUIRED | Historical - verify before use |
| RA-OI-TE-584 | IC-7808 | PROVISIONAL | Historical - verify before use |
| customs duty fr 7% | IC-7858 | PROVISIONAL | Historical - verify before use |
| SIG-28-SXX-AKUN | IC-6566 | PROVISIONAL | Historical - verify before use |
| AT-SU-CO-755 | IC-7884 | PROVISIONAL | Historical - verify before use |
| Horizon Partners Ltd. | IC-5693 | SUPERSEDED | Historical - verify before use |
| Vat Standard GB 19% | IC-9663 | DEPRECATED | Historical - verify before use |
| fructose standard | IC-5235 | PROVISIONAL | Historical - verify before use |
| Dextrin | IC-7541 | PROVISIONAL | Historical - verify before use |
| Nexus Partners GmbH | IC-7361 | DEPRECATED | Historical - verify before use |
| RE-ST-GR-B-598 | IC-7335 | PROVISIONAL | Historical - verify before use |
| Vertex Vertrieb Holdings | IC-8757 | DEPRECATED | Historical - verify before use |
| Sodium Chloride 25% Food Grade | IC-5105 | REVIEW REQUIRED | Historical - verify before use |
| LA-AC-TE-651 | IC-8306 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat 50% Technische Qualität | IC-6908 | REVIEW REQUIRED | Historical - verify before use |
| PA-CH-580 KG | IC-8213 | PROVISIONAL | Historical - verify before use |
| SIG-69-BWM-8WBG | IC-6610 | PROVISIONAL | Historical - verify before use |
| Isoglucose | IC-8581 | PROVISIONAL | Historical - verify before use |
| fructose standard | IC-8882 | PROVISIONAL | Historical - verify before use |
| NO-SU-CO-376 | IC-5786 | DEPRECATED | Historical - verify before use |
| SIG-14-HQE-PUWC | IC-9115 | REVIEW REQUIRED | Historical - verify before use |
| withholding nl 5% | IC-5511 | DEPRECATED | Historical - verify before use |
| Catalyst Versorgung International | IC-5268 | DEPRECATED | Historical - verify before use |
| SIG-51-CZK-SBJH | IC-9713 | DEPRECATED | Historical - verify before use |
| AT-CH-341 SA | IC-8114 | PROVISIONAL | Historical - verify before use |
| Traubenzucker 70% | IC-5442 | PROVISIONAL | Historical - verify before use |
| Citric Acid 99.5% | IC-7151 | PROVISIONAL | Historical - verify before use |
| PR-SO-362 | IC-9160 | SUPERSEDED | Historical - verify before use |
| SIG-68-KHP-8RTJ | IC-5362 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid | IC-8059 | REVIEW REQUIRED | Historical - verify before use |
| soy isolate 50% premium | IC-6732 | SUPERSEDED | Historical - verify before use |
| Withholding NL 5% | IC-9864 | DEPRECATED | Historical - verify before use |
| CO-OI-98-PR-329 | IC-5527 | PROVISIONAL | Historical - verify before use |
| SIG-98-XJT-L879 | IC-9889 | SUPERSEDED | Historical - verify before use |
| Apex Ingredients AG | IC-9691 | PROVISIONAL | Historical - verify before use |
| IS-25-FO-GR-789 | IC-7694 | REVIEW REQUIRED | Historical - verify before use |
| Withholding FR 5% | IC-7659 | REVIEW REQUIRED | Historical - verify before use |
| Sodium Chloride Technical | IC-7242 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid 50% Technical | IC-5199 | SUPERSEDED | Historical - verify before use |
| Palm Oil 70% Grade B | IC-5147 | SUPERSEDED | Historical - verify before use |
| PE-PR-50-128 | IC-8224 | SUPERSEDED | Historical - verify before use |
| Glukosesirup Syrup 25% | IC-5405 | REVIEW REQUIRED | Historical - verify before use |
| Dextrose 70% Grade A | IC-6655 | REVIEW REQUIRED | Historical - verify before use |
| Catalyst Materials | IC-6509 | REVIEW REQUIRED | Historical - verify before use |
| lactic acid standard | IC-6200 | REVIEW REQUIRED | Historical - verify before use |
| Potassium Sorbate | IC-6154 | SUPERSEDED | Historical - verify before use |
| Pea Protein Standard | IC-5048 | PROVISIONAL | Historical - verify before use |
| Stratos Ingredients SARL | IC-9947 | DEPRECATED | Historical - verify before use |
| Kaliumsorbat Lebensmittelrein | IC-5714 | PROVISIONAL | Historical - verify before use |
| Vat Reduced CN 19% | IC-7514 | DEPRECATED | Historical - verify before use |
| Sodium Benzoate 99.5% Grade A | IC-5155 | PROVISIONAL | Historical - verify before use |
| Lactic Acid | IC-6458 | SUPERSEDED | Historical - verify before use |
| Horizon Chemicals PLC | IC-6942 | REVIEW REQUIRED | Historical - verify before use |
| soy isolate 99.5% | IC-7529 | DEPRECATED | Historical - verify before use |
| nordic processing SAS | IC-6717 | SUPERSEDED | Historical - verify before use |
| SIG-86-NGE-LKTW | IC-8930 | SUPERSEDED | Historical - verify before use |
| Palm Oil 25% Grade A | IC-9205 | SUPERSEDED | Historical - verify before use |
| SIG-68-DWS-MNR6 | IC-9184 | PROVISIONAL | Historical - verify before use |
| NE-TR-634 International | IC-7261 | SUPERSEDED | Historical - verify before use |
| Vat Reduced GB 19% | IC-7767 | PROVISIONAL | Historical - verify before use |
| Withholding DE 20% | IC-6357 | PROVISIONAL | Historical - verify before use |
| MA-DE-335 | IC-5598 | DEPRECATED | Historical - verify before use |
| Resistente Stärke | IC-8382 | REVIEW REQUIRED | Historical - verify before use |
| coconut oil standard | IC-7145 | PROVISIONAL | Historical - verify before use |
| coconut oil 25% standard | IC-8287 | SUPERSEDED | Historical - verify before use |
| Vat Reduced BR 25% | IC-5011 | PROVISIONAL | Historical - verify before use |
| Excise US 19% | IC-9328 | DEPRECATED | Historical - verify before use |
| CA-CA-FO-GR-991 | IC-8495 | SUPERSEDED | Historical - verify before use |
| Soja Isolate 99.5% | IC-9704 | PROVISIONAL | Historical - verify before use |
| SIG-15-IUN-M051 | IC-6600 | DEPRECATED | Historical - verify before use |
| Resistente Stärke | IC-8946 | SUPERSEDED | Historical - verify before use |
| potassium sorbate 25% pharma grade | IC-8960 | DEPRECATED | Historical - verify before use |
| SO-BE-824 | IC-6346 | DEPRECATED | Historical - verify before use |
| SO-BE-99.5-GR-A-930 | IC-5070 | DEPRECATED | Historical - verify before use |
| pea protein premium | IC-9350 | SUPERSEDED | Historical - verify before use |
| SIG-26-PJJ-DUD8 | IC-5483 | SUPERSEDED | Historical - verify before use |
| Pea Protein 98% Qualitätsstufe II | IC-6686 | DEPRECATED | Historical - verify before use |
| Vertex Solutions NV | IC-7328 | DEPRECATED | Historical - verify before use |
| sorbic acid | IC-8825 | REVIEW REQUIRED | Historical - verify before use |
| Pea Protein 25% | IC-5509 | REVIEW REQUIRED | Historical - verify before use |
| PA-LO-674 | IC-7475 | DEPRECATED | Historical - verify before use |
| SIG-22-XCC-QSNV | IC-8195 | REVIEW REQUIRED | Historical - verify before use |
| CO-IN-915 KG | IC-5961 | PROVISIONAL | Historical - verify before use |
| vertex chemicals International | IC-8707 | REVIEW REQUIRED | Historical - verify before use |
| Atlantic Industrien International | IC-6862 | PROVISIONAL | Historical - verify before use |
| pinnacle distribution Ltd. | IC-7622 | DEPRECATED | Historical - verify before use |
| SO-AC-PR-928 | IC-9841 | PROVISIONAL | Historical - verify before use |
| Soy Isolate 50% Grade B | IC-7032 | DEPRECATED | Historical - verify before use |
| Citric Acid 50% Grade A | IC-6770 | PROVISIONAL | Historical - verify before use |
| Rapsöl 70% Qualitätsstufe II | IC-6007 | DEPRECATED | Historical - verify before use |
| Pinnacle Materials | IC-9203 | SUPERSEDED | Historical - verify before use |
| SIG-44-QME-TTIM | IC-6319 | PROVISIONAL | Historical - verify before use |
| Calcium Carbonate Food Grade | IC-5519 | DEPRECATED | Historical - verify before use |
| Nordic Chemicals BV | IC-7492 | DEPRECATED | Historical - verify before use |
| NO-IN-797 | IC-6197 | DEPRECATED | Historical - verify before use |
| Soy Isolate 25% Standard | IC-8364 | PROVISIONAL | Historical - verify before use |
| Maltodextrin DE18 | IC-5524 | REVIEW REQUIRED | Historical - verify before use |
| Meridian Enterprise | IC-5555 | DEPRECATED | Historical - verify before use |
| rapeseed oil | IC-6111 | REVIEW REQUIRED | Historical - verify before use |
| NO-LO-114 Ltd. | IC-6288 | PROVISIONAL | Historical - verify before use |
| Lactic Acid | IC-7501 | REVIEW REQUIRED | Historical - verify before use |
| Pinnacle Chemicals SA | IC-6187 | PROVISIONAL | Historical - verify before use |
| Excise BR 5% | IC-9036 | REVIEW REQUIRED | Historical - verify before use |
| LA-AC-FO-GR-469 | IC-6684 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat 99.5% Technische Qualität | IC-7674 | DEPRECATED | Historical - verify before use |
| Coconut Oil Food Grade | IC-7621 | REVIEW REQUIRED | Historical - verify before use |
| excise us 5% | IC-9797 | REVIEW REQUIRED | Historical - verify before use |
| Sodium Benzoate Pharma Grade | IC-7237 | PROVISIONAL | Historical - verify before use |
| glucose syrup 98% food grade | IC-7131 | SUPERSEDED | Historical - verify before use |
| CO-IN-421 | IC-5011 | PROVISIONAL | Historical - verify before use |
| Atlantic Handel BV | IC-7727 | REVIEW REQUIRED | Historical - verify before use |
| Quantum Rohstoffe | IC-7856 | DEPRECATED | Historical - verify before use |
| SIG-58-NPG-WEEE PLC | IC-6532 | REVIEW REQUIRED | Historical - verify before use |
| Sonnenblumenöl Qualitätsstufe I | IC-9938 | DEPRECATED | Historical - verify before use |
| SU-OI-TE-705 | IC-9485 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid 98% Premium | IC-8454 | PROVISIONAL | Historical - verify before use |
| PA-OI-98-856 | IC-7126 | SUPERSEDED | Historical - verify before use |
| Atlas Werkstoffe | IC-6617 | PROVISIONAL | Historical - verify before use |
| Pea Protein 25% | IC-5231 | SUPERSEDED | Historical - verify before use |
| Weizenklebereiweiß 99.5% Technische Qualität | IC-9161 | PROVISIONAL | Historical - verify before use |
| SIG-65-TTX-PCJA | IC-8613 | DEPRECATED | Historical - verify before use |
| Lactic Acid Technische Qualität | IC-8052 | REVIEW REQUIRED | Historical - verify before use |
| CE-SU-CO-752 | IC-8810 | REVIEW REQUIRED | Historical - verify before use |
| palm oil 50% | IC-6419 | REVIEW REQUIRED | Historical - verify before use |
| Nordic Logistik PLC | IC-9842 | REVIEW REQUIRED | Historical - verify before use |
| Natriumbenzoat 25% | IC-8342 | REVIEW REQUIRED | Historical - verify before use |
| SIG-29-ZZE-ZUAD | IC-5542 | DEPRECATED | Historical - verify before use |
| Fructose 98% Premiumqualität | IC-8525 | PROVISIONAL | Historical - verify before use |
| dextrose standard | IC-6655 | REVIEW REQUIRED | Historical - verify before use |
| apex sourcing | IC-7341 | DEPRECATED | Historical - verify before use |
| Dextrose 25% | IC-7639 | SUPERSEDED | Historical - verify before use |
| Vertex Logistics Holdings | IC-8287 | DEPRECATED | Historical - verify before use |
| CI-AC-70-265 | IC-9655 | SUPERSEDED | Historical - verify before use |
| SIG-19-TLQ-1P5Z | IC-5618 | DEPRECATED | Historical - verify before use |
| EX-F-19-312 | IC-7142 | DEPRECATED | Historical - verify before use |
| SIG-91-WVE-3ESP | IC-8270 | REVIEW REQUIRED | Historical - verify before use |
| Premier Logistik | IC-6702 | REVIEW REQUIRED | Historical - verify before use |
| customs duty nl 21% | IC-7325 | REVIEW REQUIRED | Historical - verify before use |
| Horizon Rohstoffe PLC | IC-6856 | PROVISIONAL | Historical - verify before use |
| Withholding NL 7% | IC-9684 | PROVISIONAL | Historical - verify before use |
| Stratos Enterprise International | IC-5639 | DEPRECATED | Historical - verify before use |
| CA-MA-366 | IC-7322 | SUPERSEDED | Historical - verify before use |
| vat standard br 7% | IC-5225 | REVIEW REQUIRED | Historical - verify before use |
| elite sourcing | IC-6382 | REVIEW REQUIRED | Historical - verify before use |
| Global Rohstoffe AG | IC-9259 | DEPRECATED | Historical - verify before use |
| Global Versorgung | IC-8440 | PROVISIONAL | Historical - verify before use |
| SIG-98-YBY-PFKQ | IC-7873 | DEPRECATED | Historical - verify before use |
| SIG-54-MUH-KY6K | IC-9111 | SUPERSEDED | Historical - verify before use |
| pea protein 98% standard | IC-5341 | DEPRECATED | Historical - verify before use |
| PE-PR-50-128 | IC-8686 | PROVISIONAL | Historical - verify before use |
| stratos sourcing | IC-5561 | DEPRECATED | Historical - verify before use |
| SIG-86-JSN-H9KJ SA | IC-7738 | SUPERSEDED | Historical - verify before use |
| PA-OI-632 | IC-7460 | DEPRECATED | Historical - verify before use |
| WI-G-21-298 | IC-7230 | PROVISIONAL | Historical - verify before use |
| casein | IC-9380 | DEPRECATED | Historical - verify before use |
| Stratos Sourcing | IC-9983 | PROVISIONAL | Historical - verify before use |
| SIG-29-BKQ-HXCX Group | IC-8697 | DEPRECATED | Historical - verify before use |
| Vat Reduced BR 10% | IC-6306 | DEPRECATED | Historical - verify before use |
| Traubenzucker 99.5% | IC-8317 | SUPERSEDED | Historical - verify before use |
| EL-SO-472 | IC-5701 | PROVISIONAL | Historical - verify before use |
| Nexus Logistik | IC-6893 | DEPRECATED | Historical - verify before use |
| SIG-70-KJX-6V9L | IC-5350 | PROVISIONAL | Historical - verify before use |


#### 4.3.4 Excluded Assignments

Assignments excluded from scope per stakeholder decision:

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-3206-C | Out of scope per business decision | Manual review scheduled |
| NOISE-3929-F | Out of scope per business decision | Business owner notified |
| NOISE-3303-G | Duplicate source record | Escalated to data steward |
| NOISE-2419-B | Duplicate source record | Escalated to data steward |
| NOISE-5039-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5567-H | Pending validation | Deferred to Phase 2 |
| NOISE-9934-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4147-C | Data quality insufficient | Manual review scheduled |
| NOISE-6069-E | Missing required attributes | Business owner notified |
| NOISE-4940-C | Out of scope per business decision | Escalated to data steward |
| NOISE-8888-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5557-D | Data quality insufficient | Escalated to data steward |
| NOISE-1045-C | Duplicate source record | Escalated to data steward |
| NOISE-4653-C | Pending validation | Manual review scheduled |
| NOISE-5350-E | Data quality insufficient | Business owner notified |
| NOISE-5484-G | Data quality insufficient | Manual review scheduled |
| NOISE-2053-H | Missing required attributes | Manual review scheduled |
| NOISE-1580-F | Data quality insufficient | Manual review scheduled |
| NOISE-5154-A | Missing required attributes | Escalated to data steward |
| NOISE-8076-E | Duplicate source record | Manual review scheduled |
| NOISE-2760-B | Missing required attributes | Business owner notified |
| NOISE-3594-F | Pending validation | Business owner notified |
| NOISE-4464-B | Pending validation | Business owner notified |
| NOISE-5222-E | Duplicate source record | Manual review scheduled |
| NOISE-6989-D | Pending validation | Escalated to data steward |
| NOISE-8403-H | Data quality insufficient | Business owner notified |
| NOISE-4371-A | Pending validation | Escalated to data steward |
| NOISE-1385-E | Pending validation | Business owner notified |
| NOISE-3537-A | Pending validation | Business owner notified |
| NOISE-5588-B | Pending validation | Business owner notified |
| NOISE-8933-G | Pending validation | Business owner notified |
| NOISE-1420-A | Missing required attributes | Business owner notified |
| NOISE-9271-E | Out of scope per business decision | Manual review scheduled |
| NOISE-1863-E | Out of scope per business decision | Business owner notified |
| NOISE-5755-B | Data quality insufficient | Escalated to data steward |
| NOISE-7047-D | Missing required attributes | Manual review scheduled |
| NOISE-4372-F | Pending validation | Business owner notified |
| NOISE-5557-E | Duplicate source record | Business owner notified |
| NOISE-4646-F | Duplicate source record | Escalated to data steward |
| NOISE-1018-C | Data quality insufficient | Business owner notified |
| NOISE-4758-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-6433-A | Duplicate source record | Business owner notified |
| NOISE-7120-D | Duplicate source record | Business owner notified |
| NOISE-2684-B | Duplicate source record | Manual review scheduled |
| NOISE-8574-E | Data quality insufficient | Business owner notified |
| NOISE-3027-G | Duplicate source record | Escalated to data steward |
| NOISE-7770-G | Out of scope per business decision | Manual review scheduled |
| NOISE-6942-G | Duplicate source record | Business owner notified |
| NOISE-1769-D | Pending validation | Escalated to data steward |
| NOISE-9203-B | Missing required attributes | Business owner notified |
| NOISE-7927-F | Pending validation | Deferred to Phase 2 |
| NOISE-9710-C | Duplicate source record | Escalated to data steward |
| NOISE-5096-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-8738-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3411-B | Data quality insufficient | Manual review scheduled |
| NOISE-3049-C | Duplicate source record | Escalated to data steward |
| NOISE-6478-B | Duplicate source record | Escalated to data steward |
| NOISE-9452-E | Out of scope per business decision | Business owner notified |
| NOISE-1304-D | Pending validation | Manual review scheduled |
| NOISE-4397-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-5510-E | Missing required attributes | Business owner notified |
| NOISE-4725-B | Out of scope per business decision | Escalated to data steward |
| NOISE-7109-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-5479-G | Out of scope per business decision | Manual review scheduled |
| NOISE-8829-E | Missing required attributes | Escalated to data steward |
| NOISE-5144-C | Data quality insufficient | Manual review scheduled |
| NOISE-5324-B | Missing required attributes | Business owner notified |
| NOISE-1550-F | Pending validation | Escalated to data steward |
| NOISE-4482-A | Pending validation | Deferred to Phase 2 |
| NOISE-2270-C | Pending validation | Deferred to Phase 2 |
| NOISE-2156-E | Duplicate source record | Manual review scheduled |
| NOISE-1177-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-3883-H | Out of scope per business decision | Escalated to data steward |
| NOISE-1482-H | Pending validation | Business owner notified |
| NOISE-6468-C | Missing required attributes | Business owner notified |
| NOISE-3202-F | Out of scope per business decision | Manual review scheduled |
| NOISE-6234-F | Duplicate source record | Business owner notified |
| NOISE-2903-D | Duplicate source record | Escalated to data steward |
| NOISE-2119-A | Data quality insufficient | Business owner notified |
| NOISE-7269-H | Pending validation | Manual review scheduled |
| NOISE-3034-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-2699-G | Data quality insufficient | Escalated to data steward |
| NOISE-1176-B | Duplicate source record | Escalated to data steward |
| NOISE-3133-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-9412-D | Out of scope per business decision | Escalated to data steward |
| NOISE-7248-D | Duplicate source record | Manual review scheduled |
| NOISE-2077-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1052-A | Duplicate source record | Manual review scheduled |
| NOISE-3369-F | Missing required attributes | Manual review scheduled |
| NOISE-9141-F | Duplicate source record | Manual review scheduled |
| NOISE-1107-F | Missing required attributes | Business owner notified |
| NOISE-4332-C | Data quality insufficient | Business owner notified |
| NOISE-3408-G | Pending validation | Business owner notified |
| NOISE-3684-D | Duplicate source record | Business owner notified |
| NOISE-3009-C | Data quality insufficient | Escalated to data steward |
| NOISE-4144-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-7499-E | Missing required attributes | Escalated to data steward |
| NOISE-3153-D | Data quality insufficient | Business owner notified |
| NOISE-3483-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5473-B | Pending validation | Business owner notified |
| NOISE-5284-D | Duplicate source record | Manual review scheduled |
| NOISE-2481-F | Pending validation | Business owner notified |
| NOISE-1127-D | Missing required attributes | Business owner notified |
| NOISE-2899-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6839-C | Duplicate source record | Manual review scheduled |
| NOISE-5031-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8353-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8982-A | Missing required attributes | Escalated to data steward |
| NOISE-6101-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-5792-G | Out of scope per business decision | Escalated to data steward |
| NOISE-1138-D | Pending validation | Business owner notified |
| NOISE-7395-H | Duplicate source record | Escalated to data steward |
| NOISE-2689-A | Duplicate source record | Business owner notified |
| NOISE-7019-D | Out of scope per business decision | Escalated to data steward |
| NOISE-8206-D | Data quality insufficient | Manual review scheduled |
| NOISE-8602-B | Duplicate source record | Escalated to data steward |
| NOISE-2933-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4392-F | Out of scope per business decision | Manual review scheduled |
| NOISE-8768-B | Duplicate source record | Manual review scheduled |
| NOISE-2707-H | Data quality insufficient | Manual review scheduled |
| NOISE-1400-A | Pending validation | Business owner notified |
| NOISE-4032-A | Out of scope per business decision | Business owner notified |
| NOISE-5531-A | Pending validation | Deferred to Phase 2 |
| NOISE-8353-F | Out of scope per business decision | Business owner notified |
| NOISE-2733-A | Pending validation | Business owner notified |
| NOISE-4986-B | Pending validation | Escalated to data steward |
| NOISE-1594-G | Pending validation | Escalated to data steward |
| NOISE-2237-D | Out of scope per business decision | Manual review scheduled |
| NOISE-2063-D | Out of scope per business decision | Manual review scheduled |
| NOISE-3896-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-6485-D | Duplicate source record | Business owner notified |
| NOISE-3222-C | Pending validation | Manual review scheduled |
| NOISE-3768-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5049-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-8867-G | Duplicate source record | Business owner notified |
| NOISE-7817-G | Data quality insufficient | Escalated to data steward |
| NOISE-3763-H | Pending validation | Deferred to Phase 2 |
| NOISE-3573-G | Out of scope per business decision | Business owner notified |
| NOISE-5319-B | Out of scope per business decision | Business owner notified |
| NOISE-8033-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3695-D | Duplicate source record | Escalated to data steward |
| NOISE-8028-E | Data quality insufficient | Business owner notified |
| NOISE-9151-G | Out of scope per business decision | Escalated to data steward |
| NOISE-9219-H | Missing required attributes | Escalated to data steward |
| NOISE-9389-G | Missing required attributes | Manual review scheduled |
| NOISE-8313-F | Duplicate source record | Manual review scheduled |
| NOISE-2629-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-5171-E | Out of scope per business decision | Manual review scheduled |
| NOISE-8548-G | Missing required attributes | Business owner notified |
| NOISE-9482-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-8834-D | Pending validation | Deferred to Phase 2 |
| NOISE-3619-C | Out of scope per business decision | Escalated to data steward |
| NOISE-9877-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-6389-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-9514-A | Missing required attributes | Business owner notified |
| NOISE-3577-E | Pending validation | Business owner notified |
| NOISE-9752-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-6454-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-8087-F | Missing required attributes | Manual review scheduled |
| NOISE-6340-G | Missing required attributes | Escalated to data steward |
| NOISE-1111-B | Pending validation | Manual review scheduled |
| NOISE-3028-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2661-F | Data quality insufficient | Escalated to data steward |
| NOISE-4619-B | Data quality insufficient | Escalated to data steward |
| NOISE-1629-E | Data quality insufficient | Escalated to data steward |
| NOISE-1726-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-7758-D | Pending validation | Escalated to data steward |
| NOISE-4804-G | Pending validation | Manual review scheduled |
| NOISE-9780-C | Out of scope per business decision | Manual review scheduled |
| NOISE-7573-A | Pending validation | Deferred to Phase 2 |
| NOISE-2831-G | Missing required attributes | Escalated to data steward |
| NOISE-7402-C | Pending validation | Deferred to Phase 2 |
| NOISE-4644-F | Duplicate source record | Manual review scheduled |
| NOISE-3452-F | Out of scope per business decision | Business owner notified |
| NOISE-1427-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9814-E | Duplicate source record | Manual review scheduled |
| NOISE-8808-C | Pending validation | Manual review scheduled |
| NOISE-5743-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8045-G | Duplicate source record | Manual review scheduled |
| NOISE-1628-B | Duplicate source record | Manual review scheduled |
| NOISE-5173-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-4801-B | Pending validation | Manual review scheduled |
| NOISE-3208-D | Missing required attributes | Escalated to data steward |
| NOISE-2962-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-9019-C | Data quality insufficient | Business owner notified |
| NOISE-3012-H | Out of scope per business decision | Business owner notified |
| NOISE-7115-H | Data quality insufficient | Escalated to data steward |
| NOISE-6191-B | Out of scope per business decision | Manual review scheduled |
| NOISE-6093-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-4913-D | Duplicate source record | Business owner notified |
| NOISE-9183-D | Out of scope per business decision | Business owner notified |
| NOISE-7139-H | Duplicate source record | Business owner notified |
| NOISE-9061-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-6665-B | Duplicate source record | Escalated to data steward |
| NOISE-2078-H | Data quality insufficient | Business owner notified |
| NOISE-4537-H | Duplicate source record | Manual review scheduled |
| NOISE-8859-A | Duplicate source record | Business owner notified |
| NOISE-7324-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5214-B | Out of scope per business decision | Escalated to data steward |
| NOISE-8205-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-6160-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-1592-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3891-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-6842-C | Pending validation | Deferred to Phase 2 |
| NOISE-2608-C | Out of scope per business decision | Escalated to data steward |
| NOISE-4884-E | Duplicate source record | Business owner notified |
| NOISE-3225-D | Missing required attributes | Manual review scheduled |
| NOISE-9140-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-5666-F | Out of scope per business decision | Business owner notified |
| NOISE-3979-B | Duplicate source record | Manual review scheduled |
| NOISE-6339-E | Out of scope per business decision | Business owner notified |
| NOISE-5740-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-2717-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-3321-E | Missing required attributes | Manual review scheduled |
| NOISE-5368-D | Pending validation | Manual review scheduled |
| NOISE-1743-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5064-B | Missing required attributes | Escalated to data steward |
| NOISE-7542-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6311-F | Data quality insufficient | Business owner notified |
| NOISE-3954-D | Pending validation | Manual review scheduled |
| NOISE-5369-A | Data quality insufficient | Business owner notified |
| NOISE-2032-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2837-E | Out of scope per business decision | Escalated to data steward |
| NOISE-3506-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9885-H | Duplicate source record | Deferred to Phase 2 |
| NOISE-7809-F | Data quality insufficient | Business owner notified |
| NOISE-8805-A | Missing required attributes | Manual review scheduled |
| NOISE-7390-B | Data quality insufficient | Business owner notified |
| NOISE-1431-A | Duplicate source record | Business owner notified |
| NOISE-2278-E | Missing required attributes | Escalated to data steward |
| NOISE-5894-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-3280-G | Pending validation | Manual review scheduled |
| NOISE-5294-A | Missing required attributes | Business owner notified |
| NOISE-1541-H | Out of scope per business decision | Escalated to data steward |
| NOISE-5316-D | Pending validation | Business owner notified |
| NOISE-5751-B | Data quality insufficient | Manual review scheduled |
| NOISE-2026-E | Pending validation | Escalated to data steward |
| NOISE-9994-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-3615-A | Pending validation | Escalated to data steward |
| NOISE-5506-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2455-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-2444-C | Missing required attributes | Escalated to data steward |
| NOISE-1912-D | Data quality insufficient | Escalated to data steward |
| NOISE-5044-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7228-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-8249-A | Pending validation | Deferred to Phase 2 |
| NOISE-8801-E | Data quality insufficient | Business owner notified |
| NOISE-6226-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8716-H | Pending validation | Business owner notified |
| NOISE-4010-G | Pending validation | Deferred to Phase 2 |
| NOISE-1188-C | Out of scope per business decision | Business owner notified |
| NOISE-5927-D | Data quality insufficient | Manual review scheduled |
| NOISE-1881-E | Out of scope per business decision | Escalated to data steward |
| NOISE-9248-D | Pending validation | Business owner notified |
| NOISE-2100-G | Missing required attributes | Manual review scheduled |
| NOISE-2812-C | Missing required attributes | Escalated to data steward |
| NOISE-8631-D | Out of scope per business decision | Business owner notified |
| NOISE-2902-B | Missing required attributes | Escalated to data steward |
| NOISE-6439-F | Data quality insufficient | Manual review scheduled |
| NOISE-8525-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-9881-B | Duplicate source record | Manual review scheduled |
| NOISE-1889-G | Duplicate source record | Escalated to data steward |
| NOISE-4441-B | Data quality insufficient | Business owner notified |
| NOISE-6591-F | Duplicate source record | Escalated to data steward |
| NOISE-5595-A | Out of scope per business decision | Manual review scheduled |
| NOISE-4794-D | Out of scope per business decision | Business owner notified |
| NOISE-5253-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-9631-D | Out of scope per business decision | Manual review scheduled |
| NOISE-2167-G | Missing required attributes | Manual review scheduled |
| NOISE-8948-D | Data quality insufficient | Business owner notified |
| NOISE-7557-B | Data quality insufficient | Escalated to data steward |
| NOISE-3692-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-3014-F | Pending validation | Deferred to Phase 2 |
| NOISE-3685-F | Pending validation | Business owner notified |
| NOISE-4994-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-4218-D | Duplicate source record | Manual review scheduled |
| NOISE-8783-G | Pending validation | Escalated to data steward |
| NOISE-8563-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-9201-B | Pending validation | Business owner notified |
| NOISE-2294-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9349-E | Pending validation | Business owner notified |
| NOISE-4856-G | Pending validation | Escalated to data steward |
| NOISE-5250-D | Missing required attributes | Escalated to data steward |
| NOISE-3537-G | Duplicate source record | Manual review scheduled |
| NOISE-6720-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4487-E | Pending validation | Escalated to data steward |
| NOISE-5776-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5829-F | Duplicate source record | Business owner notified |
| NOISE-8695-H | Out of scope per business decision | Manual review scheduled |
| NOISE-3362-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4465-F | Out of scope per business decision | Escalated to data steward |
| NOISE-8026-E | Data quality insufficient | Manual review scheduled |
| NOISE-3559-G | Missing required attributes | Escalated to data steward |
| NOISE-9344-G | Pending validation | Manual review scheduled |
| NOISE-2150-B | Out of scope per business decision | Escalated to data steward |
| NOISE-4607-B | Duplicate source record | Business owner notified |
| NOISE-5486-C | Duplicate source record | Escalated to data steward |
| NOISE-5315-F | Duplicate source record | Manual review scheduled |
| NOISE-9442-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-4323-F | Out of scope per business decision | Business owner notified |
| NOISE-8505-B | Duplicate source record | Manual review scheduled |
| NOISE-8449-G | Missing required attributes | Manual review scheduled |
| NOISE-6925-C | Data quality insufficient | Escalated to data steward |
| NOISE-3290-F | Data quality insufficient | Business owner notified |
| NOISE-2933-B | Data quality insufficient | Escalated to data steward |
| NOISE-5832-D | Data quality insufficient | Escalated to data steward |
| NOISE-8487-C | Pending validation | Business owner notified |
| NOISE-2865-C | Out of scope per business decision | Escalated to data steward |
| NOISE-1213-F | Missing required attributes | Business owner notified |
| NOISE-9599-A | Duplicate source record | Escalated to data steward |
| NOISE-3594-G | Duplicate source record | Escalated to data steward |
| NOISE-9762-G | Out of scope per business decision | Business owner notified |
| NOISE-2533-C | Pending validation | Deferred to Phase 2 |
| NOISE-3325-E | Duplicate source record | Manual review scheduled |
| NOISE-8876-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7579-B | Data quality insufficient | Escalated to data steward |
| NOISE-3187-E | Data quality insufficient | Business owner notified |
| NOISE-5187-E | Duplicate source record | Business owner notified |
| NOISE-1774-F | Data quality insufficient | Manual review scheduled |
| NOISE-5763-F | Pending validation | Manual review scheduled |
| NOISE-6708-C | Duplicate source record | Escalated to data steward |
| NOISE-4396-A | Duplicate source record | Business owner notified |
| NOISE-9803-F | Pending validation | Manual review scheduled |
| NOISE-5602-H | Missing required attributes | Escalated to data steward |
| NOISE-2228-H | Missing required attributes | Deferred to Phase 2 |


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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230323_000000`
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
| Business Owner | David Kim (Project Management) | david@company.com | +1-555-0103 |
| Data Steward | Sarah Chen (Data Governance) | sarah@company.com | +1-555-0104 |

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
