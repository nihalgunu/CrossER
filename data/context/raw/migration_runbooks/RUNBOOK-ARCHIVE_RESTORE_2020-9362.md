# Migration Runbook: System Migration: ARCHIVE_RESTORE_2020

**Document ID**: RB-ARCHIVE_RESTORE_2020-1813
**Version**: 2.5
**Last Updated**: 2023-04-14
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the System Migration: ARCHIVE_RESTORE_2020 project.
The migration involves transitioning master data and transactional records from SOURCE
to TARGET while maintaining data integrity and business continuity.

**Project Timeline**: 2023-01-18 to 2023-06-01
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
| Total entities assessed | 1488 | Completed |
| Codes assigned | 1098 | Staged |
| Excluded from scope | 329 | Documented |
| Pending review | 6 | In Progress |

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
| Vertex Rohstoffe | BC-8286 | 2021-06-14 | Product Management |
| Vat Standardqualität NL 25% | BC-8291 | 2023-08-24 | Operations |
| SIG-61-MHS-BQG3 | IC-8292 | 2021-09-14 | IT Infrastructure |
| Coconut Oil 98% | TC-8298 | 2023-07-15 | Compliance |
| Horizon Ingredients International | TC-8302 | 2022-05-28 | Product Management |
| soy isolate | BC-8305 | 2024-09-08 | IT Infrastructure |
| withholding gb 5% | TC-8317 | 2023-07-03 | Product Management |
| elite partners | TC-8320 | 2024-02-15 | Compliance |
| Coconut Oil 70% | BC-8331 | 2021-12-22 | Data Governance |
| Elite Solutions | BC-8340 | 2023-06-09 | Finance |
| SIG-10-KDB-LGYT | BC-8356 | 2022-01-08 | Operations |
| ascorbic acid premium | IC-8394 | 2022-10-13 | Finance |
| Vat Standardqualität FR 0% | TC-8401 | 2021-01-26 | Finance |
| sodium benzoate 99.5% premium | TC-8427 | 2021-07-10 | Data Governance |
| SIG-77-AEN-CA8D | TC-8428 | 2022-12-14 | IT Infrastructure |
| Vat Standardqualität US 10% | TC-8439 | 2021-10-08 | Supply Chain |
| SIG-10-TIC-7Q1D | IC-8441 | 2023-05-18 | Data Governance |
| Ascorbic Acid 70% | BC-8446 | 2021-01-15 | Product Management |
| Ascorbic Acid 98% Pharmazeutisch rein | IC-8448 | 2022-08-07 | Product Management |
| GL-SY-PR-440 | IC-8460 | 2024-03-27 | Finance |
| apex sourcing | IC-8470 | 2021-11-22 | Supply Chain |
| SIG-88-AGF-FF5L | TC-8476 | 2021-08-27 | Operations |
| SIG-80-ZKZ-ANXJ | IC-8484 | 2022-10-15 | Compliance |
| Resistente Stärke | TC-8486 | 2024-05-12 | Compliance |
| rapeseed oil 50% pharma grade | TC-8487 | 2022-06-05 | Data Governance |
| atlantic supply | IC-8496 | 2024-08-09 | Supply Chain |
| Baltic Industries BV | TC-8524 | 2024-10-18 | IT Infrastructure |
| SO-CH-98-657 | TC-8527 | 2022-04-07 | Product Management |
| potassium sorbate food grade | TC-8541 | 2022-12-03 | Compliance |
| Ascorbic Acid Food Grade | TC-8562 | 2021-03-19 | Operations |
| Cyclodextrin | BC-8586 | 2024-01-25 | Supply Chain |
| ME-LO-670 | TC-8602 | 2021-11-23 | Operations |
| sorbic acid 70% | IC-8608 | 2022-07-14 | Supply Chain |
| SIG-57-HAE-WNSM | BC-8610 | 2022-09-22 | Finance |
| Kaliumsorbat Qualitätsstufe II | BC-8644 | 2021-07-06 | IT Infrastructure |
| SIG-91-FOC-36I6 | BC-8649 | 2023-02-09 | Supply Chain |
| Lactic Acid 99.5% Grade B | TC-8655 | 2023-02-02 | Supply Chain |
| GL-SY-98-FO-GR-198 | TC-8656 | 2021-10-10 | Compliance |
| Pacific Materials | BC-8660 | 2024-03-20 | Finance |
| SIG-61-FGJ-AO1L NV | TC-8662 | 2022-10-26 | Finance |
| lactic acid standard | TC-8684 | 2023-08-18 | Supply Chain |
| Excise DE 10% | TC-8687 | 2022-02-01 | Operations |
| Vat Standard GB 19% | BC-8695 | 2021-02-22 | Data Governance |
| Citric Acid 99.5% | IC-8697 | 2022-03-08 | Operations |
| Atlantic Rohstoffe GmbH | IC-8725 | 2024-09-02 | Finance |
| Dextrin 25% Premiumqualität | BC-8727 | 2022-05-28 | Finance |
| SIG-69-BWM-8WBG | IC-8728 | 2024-12-27 | Operations |
| ascorbic acid pharma grade | BC-8742 | 2021-09-08 | Supply Chain |
| Meridian Versorgung | IC-8747 | 2023-01-25 | Data Governance |
| AS-AC-130 | TC-8758 | 2021-06-27 | Product Management |
| SIG-27-MIG-RYBN | IC-8760 | 2022-02-20 | Supply Chain |
| Calcium Carbonate 50% Pharma Grade | BC-8772 | 2023-10-19 | Product Management |
| apex logistics | BC-8779 | 2021-04-28 | Product Management |
| vat standard gb 21% | IC-8785 | 2023-08-01 | Compliance |
| Coconut Oil 25% Technical | BC-8787 | 2023-02-16 | Compliance |
| global enterprise NV | BC-8795 | 2021-10-25 | Finance |
| SIG-37-MXA-3C7Q | BC-8802 | 2021-09-22 | IT Infrastructure |
| SIG-97-OGU-PBXC | IC-8819 | 2021-01-28 | Data Governance |
| SIG-99-GVJ-VPM6 | BC-8827 | 2023-09-06 | Operations |
| SO-IS-99.5-PR-187 | TC-8832 | 2022-06-12 | Finance |
| ZE-PA-718 LLC | TC-8837 | 2022-09-08 | Finance |
| SIG-78-AVK-U9PX | TC-8841 | 2022-04-09 | IT Infrastructure |
| citric acid | IC-8857 | 2024-04-19 | Operations |
| SIG-69-OFZ-JW34 | TC-8875 | 2024-05-27 | Finance |
| Natriumbenzoat | TC-8876 | 2021-10-10 | IT Infrastructure |
| SIG-79-OZQ-4I2N | BC-8883 | 2021-02-23 | Compliance |
| excise in 25% | IC-8900 | 2023-01-09 | Data Governance |
| SIG-75-GGJ-DK9O | BC-8901 | 2022-06-01 | Data Governance |
| SIG-16-MNF-F4AF | BC-8909 | 2021-09-01 | IT Infrastructure |
| PI-LO-946 | IC-8929 | 2023-01-06 | Compliance |
| sorbic acid 50% food grade | BC-8930 | 2023-02-13 | Operations |
| Nexus Werkstoffe | BC-8959 | 2022-08-25 | Data Governance |
| Wheat Gluten | TC-8969 | 2021-05-16 | IT Infrastructure |
| Wheat Gluten Grade B | BC-8983 | 2022-10-27 | Finance |
| SIG-45-QQC-Z4N0 | TC-8988 | 2022-08-23 | Supply Chain |
| RA-OI-FO-GR-269 | IC-8992 | 2023-04-11 | Compliance |
| SIG-88-KUG-5ITD | TC-8998 | 2023-11-09 | Operations |
| DE-635 | BC-9008 | 2024-04-10 | Finance |
| Ascorbic Acid 99.5% Premiumqualität | BC-9014 | 2022-06-08 | Data Governance |
| PA-MA-166 SARL | BC-9029 | 2024-03-06 | Supply Chain |
| SIG-87-LPT-3ADB | BC-9047 | 2023-02-20 | IT Infrastructure |
| dextrose premium | BC-9063 | 2022-09-22 | IT Infrastructure |
| PR-CH-334 GmbH | IC-9068 | 2022-09-03 | Finance |
| Sodium Chloride | TC-9074 | 2022-03-15 | Product Management |
| Maltodextrin DE18 Pharma Grade | IC-9076 | 2022-07-18 | Compliance |
| Coconut Oil 70% Grade A | TC-9079 | 2024-04-04 | Operations |
| stellar logistics | TC-9081 | 2021-01-06 | Operations |
| Calcium Carbonate Qualitätsstufe II | BC-9087 | 2021-05-21 | Product Management |
| Catalyst Commodities SAS | TC-9092 | 2023-11-28 | Finance |
| GL-SY-98-939 | IC-9117 | 2024-09-26 | Product Management |
| sodium benzoate 98% | TC-9122 | 2024-02-07 | Finance |
| prism ingredients | IC-8625 | 2021-07-06 | Finance |
| FR-50-ST-938 | IC-9142 | 2021-02-27 | Compliance |
| casein premium | IC-9145 | 2021-04-07 | Product Management |
| Palm Oil 70% Premium | TC-9150 | 2022-03-21 | IT Infrastructure |
| Vat Reduced BR 25% | IC-9162 | 2021-07-25 | Product Management |
| sorbic acid 98% | IC-9168 | 2021-01-02 | Supply Chain |
| Casein Standard | BC-9191 | 2022-12-21 | Data Governance |
| Prism Industrien Holdings | BC-9222 | 2021-09-14 | Product Management |
| Ascorbic Acid Premiumqualität | BC-9251 | 2021-11-25 | Compliance |
| Rapsöl 70% Qualitätsstufe II | BC-9252 | 2023-10-27 | Product Management |
| SIG-10-PGH-BTUF | IC-9262 | 2021-07-11 | Compliance |
| Baltic Ingredients | IC-9272 | 2023-09-22 | Data Governance |
| Sorbic Acid Food Grade | TC-9277 | 2022-03-02 | Data Governance |
| Continental Enterprise KG | TC-9293 | 2021-12-10 | Data Governance |
| Dextrin | BC-9296 | 2021-10-07 | Supply Chain |
| Ascorbic Acid 99.5% Premiumqualität | IC-9301 | 2024-09-05 | Operations |
| SIG-20-OAV-1IKJ | BC-9304 | 2021-11-13 | Finance |
| Central Logistik | IC-9329 | 2024-11-03 | IT Infrastructure |
| SO-BE-PR-691 | BC-9331 | 2024-12-09 | Product Management |
| Excise NL 20% | TC-9390 | 2024-11-15 | Data Governance |
| premier logistics | IC-9410 | 2024-12-09 | Compliance |
| Isoglucose 70% Lebensmittelrein | IC-9419 | 2023-01-13 | Compliance |
| Withholding US 25% | TC-9421 | 2022-10-22 | Supply Chain |
| PA-MA-412 GmbH | BC-9429 | 2021-01-03 | Product Management |
| Vat Standard CN 0% | TC-9442 | 2024-04-09 | Product Management |
| Natriumbenzoat Pharmazeutisch rein | IC-9463 | 2024-09-20 | IT Infrastructure |
| Nordic Manufacturing NV | IC-9477 | 2023-03-28 | Compliance |
| casein 98% standard | TC-9482 | 2023-12-03 | IT Infrastructure |
| RA-OI-98-117 | BC-9492 | 2021-04-26 | Operations |
| SIG-58-NYA-2O4M | BC-9494 | 2022-12-18 | Data Governance |
| SO-BE-964 | BC-9506 | 2022-10-27 | Operations |
| SU-OI-70-FO-GR-432 | TC-9523 | 2021-09-04 | Supply Chain |
| SIG-84-MGK-H2ME | TC-9539 | 2021-11-28 | IT Infrastructure |
| SIG-11-AEJ-CHNJ | TC-9546 | 2024-03-13 | Product Management |
| dextrose tech grade | IC-9553 | 2021-06-10 | Product Management |
| Casein 25% Grade B | BC-9566 | 2021-05-28 | IT Infrastructure |
| Ascorbic Acid 50% Technische Qualität | IC-9569 | 2023-01-20 | Compliance |
| Rapsöl Qualitätsstufe I | TC-9577 | 2021-02-23 | Data Governance |
| Pea Protein 70% Premiumqualität | BC-9579 | 2023-04-05 | IT Infrastructure |
| customs duty fr 19% | BC-9614 | 2022-11-17 | Finance |
| citric acid | TC-9621 | 2024-03-26 | Product Management |
| AP-MA-498 | IC-9634 | 2021-02-04 | Data Governance |
| SIG-14-GCI-G4Q9 | BC-9636 | 2024-01-25 | Data Governance |
| sodium benzoate 98% pharma grade | BC-9641 | 2023-11-21 | Operations |
| Sunflower Oil Grade A | TC-9663 | 2024-09-02 | Data Governance |
| Vanguard Chemicals SAS | BC-9669 | 2021-12-03 | Compliance |
| CE-MA-720 | TC-9671 | 2024-03-09 | Finance |
| Palmfett Lebensmittelrein | BC-9679 | 2024-03-17 | IT Infrastructure |
| Cyclodextrin Food Grade | IC-9690 | 2021-07-05 | Finance |
| SIG-56-FFG-XS2P | TC-9724 | 2023-06-26 | Supply Chain |
| Ascorbic Acid | BC-9728 | 2022-01-17 | Data Governance |
| Prism Supply Co. | IC-9741 | 2022-05-17 | Data Governance |
| prime solutions | BC-9761 | 2023-10-22 | IT Infrastructure |
| AT-CO-808 GmbH | BC-9766 | 2022-11-03 | Product Management |
| customs duty us 15% | IC-9783 | 2022-07-26 | Supply Chain |
| SIG-16-MLJ-HWA7 | BC-9785 | 2023-02-07 | Product Management |
| Stratos Sourcing | TC-9787 | 2022-10-10 | Supply Chain |
| coconut oil | TC-9792 | 2023-03-16 | Data Governance |
| Withholding NL 21% | BC-9806 | 2021-04-27 | Data Governance |
| SIG-12-ANK-TJ9A | BC-9814 | 2024-01-21 | Compliance |
| central logistics International | IC-9833 | 2024-04-01 | Supply Chain |
| VA-DI-229 | BC-9836 | 2023-05-03 | Compliance |
| Lactic Acid 25% Lebensmittelrein | TC-9861 | 2022-05-06 | Data Governance |
| Natriumbenzoat Technische Qualität | BC-9877 | 2022-07-20 | IT Infrastructure |
| pea protein | TC-9879 | 2023-04-01 | Operations |
| citric acid | IC-9880 | 2021-12-14 | IT Infrastructure |
| DE-98-512 | BC-9886 | 2022-05-09 | Operations |
| Dextrin 98% | TC-9890 | 2024-04-10 | Supply Chain |
| SIG-78-TUT-T3NS | BC-9904 | 2021-06-15 | Data Governance |
| Zitronensäure Qualitätsstufe II | IC-9907 | 2023-01-22 | Finance |
| maltodextrin de30 | IC-9924 | 2022-09-28 | Supply Chain |
| Atlantic Rohstoffe International | TC-9942 | 2022-05-26 | Product Management |
| SIG-80-QLX-7SNL SAS | IC-9960 | 2021-01-23 | Operations |
| rapeseed oil | BC-9962 | 2021-12-01 | Product Management |
| dextrose | TC-9986 | 2022-01-14 | Compliance |
| Coconut Oil | TC-9993 | 2021-09-17 | Product Management |
| vat standard br 7% | IC-10010 | 2022-09-12 | IT Infrastructure |
| vat standard fr 0% | TC-10016 | 2024-04-03 | Supply Chain |
| resistant starch 70% standard | TC-10018 | 2022-05-28 | Operations |
| Excise NL 19% | IC-10026 | 2022-01-24 | Operations |
| CU-DU-B-15-686 | IC-10032 | 2022-12-26 | IT Infrastructure |
| Customs Duty BR 21% | TC-10037 | 2023-04-01 | Product Management |
| CA-GR-A-380 | BC-10051 | 2024-08-11 | Supply Chain |
| SO-AC-99.5-338 | IC-10059 | 2021-07-27 | Supply Chain |
| SIG-29-XAN-WDDA | BC-10062 | 2023-01-15 | Supply Chain |
| LA-AC-TE-651 | BC-10075 | 2024-09-23 | Finance |
| Sorbinsäure 50% | BC-10121 | 2023-05-19 | Product Management |
| SU-OI-98-PR-692 | TC-10123 | 2022-02-14 | IT Infrastructure |
| Coconut Oil Pharma Grade | BC-10143 | 2021-08-20 | Finance |
| Withholding GB 21% | IC-10154 | 2023-07-23 | Supply Chain |
| SIG-88-RKE-8R7A | IC-10163 | 2022-09-17 | Supply Chain |
| Baltic Solutions | TC-10169 | 2023-01-03 | Finance |
| VE-CH-841 Group | TC-10214 | 2023-06-16 | Operations |
| Natriumbenzoat 99.5% Technische Qualität | BC-10220 | 2024-03-24 | Supply Chain |
| CI-AC-70-FO-GR-198 | TC-10221 | 2023-03-05 | Finance |
| excise br 25% | BC-10233 | 2023-06-23 | Supply Chain |
| RA-OI-25-FO-GR-966 | TC-10241 | 2024-07-08 | Compliance |
| pea protein 25% pharma grade | TC-10258 | 2024-12-20 | Supply Chain |
| SIG-86-VCP-SVOL | IC-10273 | 2021-12-11 | Compliance |
| excise de 21% | IC-10285 | 2024-02-20 | Compliance |
| coconut oil 98% premium | IC-10293 | 2022-04-05 | Product Management |
| RA-OI-FO-GR-269 | TC-10298 | 2023-04-13 | Operations |
| SIG-71-CWF-DGP5 | BC-10299 | 2022-01-08 | IT Infrastructure |
| atlas supply | BC-10314 | 2022-06-16 | Finance |
| NO-CO-357 International | BC-10350 | 2021-08-23 | Finance |
| Maltodextrin DE25 | BC-10361 | 2021-08-26 | Compliance |
| SO-CH-PR-862 | BC-10381 | 2022-09-08 | Supply Chain |
| Wheat Gluten Grade B | TC-10399 | 2023-04-14 | Operations |
| Maltodextrin DE10 | BC-10427 | 2024-02-18 | Data Governance |
| Resistant Starch Technical | TC-10435 | 2022-04-24 | Product Management |
| Stratos Chemicals | BC-10464 | 2023-10-19 | Supply Chain |
| Apex Sourcing | IC-10472 | 2023-02-06 | Product Management |
| SIG-98-XJT-L879 | TC-10496 | 2023-06-07 | Compliance |
| SIG-36-XEW-9SSB | TC-10498 | 2023-10-19 | IT Infrastructure |
| SIG-21-VZE-Q2WM | IC-10521 | 2022-03-18 | Data Governance |
| Resistente Stärke Standardqualität | BC-10574 | 2021-03-09 | Operations |
| Ascorbic Acid 98% Qualitätsstufe II | TC-10595 | 2021-08-25 | IT Infrastructure |
| Glukosesirup Syrup Lebensmittelrein | IC-10605 | 2022-12-09 | Operations |
| Baltic Trading Holdings | TC-10622 | 2022-06-25 | Operations |
| SIG-60-WEX-2G05 | TC-10635 | 2021-03-11 | Compliance |
| SIG-32-UBB-EMYO | TC-10639 | 2024-09-19 | Supply Chain |
| withholding br 10% | BC-10652 | 2024-11-17 | Operations |
| SIG-38-YTD-7BST | IC-10659 | 2022-06-23 | Compliance |
| CA-CO-128 SAS | TC-10665 | 2021-12-25 | Data Governance |
| SIG-87-OKN-L3O4 | BC-10686 | 2022-09-20 | Supply Chain |
| Quantum Versorgung GmbH | IC-10697 | 2021-03-06 | Data Governance |
| sodium chloride 99.5% premium | IC-10710 | 2023-09-11 | Product Management |
| Meridian Werkstoffe Corp. | IC-10713 | 2022-12-19 | Finance |
| SIG-95-LOJ-S1L2 | BC-10731 | 2022-07-06 | Operations |
| coconut oil standard | TC-10733 | 2022-01-26 | Operations |
| Potassium Sorbate 25% Pharma Grade | BC-10736 | 2024-09-03 | Supply Chain |
| meridian distribution Holdings | TC-10740 | 2022-12-17 | Data Governance |
| ZE-PA-511 PLC | IC-10757 | 2021-04-04 | Compliance |
| fructose 99.5% food grade | BC-10808 | 2022-04-12 | Operations |
| SIG-13-FTX-P5F3 | IC-10813 | 2024-07-20 | Data Governance |
| Cyclodextrin | TC-10820 | 2023-08-15 | IT Infrastructure |
| Calcium Carbonate 70% Premiumqualität | IC-10829 | 2024-03-03 | Finance |
| Atlantic Materials | BC-10859 | 2022-11-18 | Product Management |
| Pinnacle Sourcing | BC-10861 | 2024-08-03 | Product Management |
| Meridian Sourcing | BC-10878 | 2022-10-19 | IT Infrastructure |
| Vanguard Chemicals SAS | TC-10885 | 2023-07-20 | Data Governance |
| Core Logistik | IC-10887 | 2024-10-13 | Data Governance |
| Coconut Oil 25% | BC-10892 | 2023-08-01 | Supply Chain |
| Ascorbic Acid Technical | IC-10898 | 2022-08-27 | Data Governance |
| SIG-15-NIP-N1UH | TC-10915 | 2023-04-10 | Data Governance |
| fructose standard | BC-10930 | 2021-05-25 | Operations |
| AS-AC-413 | TC-10936 | 2023-06-08 | Compliance |
| Withholding GB 5% | TC-10942 | 2024-05-03 | Product Management |
| SIG-42-XLZ-4BOM | BC-10946 | 2022-09-19 | Finance |
| AP-MA-145 International | TC-10951 | 2024-07-21 | Product Management |
| Prism Chemicals KG | TC-10954 | 2024-02-06 | Finance |
| NE-LO-125 | BC-10958 | 2021-02-17 | Compliance |
| Natriumchlorid | IC-10964 | 2023-04-24 | Operations |
| citric acid premium | IC-10966 | 2024-07-14 | IT Infrastructure |
| continental processing SA | TC-10979 | 2021-09-19 | Operations |
| Dextrose 25% Technical | TC-10984 | 2024-01-05 | Compliance |
| Resistente Stärke | BC-11016 | 2022-05-13 | Operations |
| cyclodextrin 70% food grade | TC-11021 | 2024-01-20 | Data Governance |
| SIG-97-SBT-Y595 | TC-11022 | 2022-08-16 | Data Governance |
| SIG-87-KZL-I3ZY | BC-11033 | 2021-04-28 | Supply Chain |
| SO-IS-99.5-PR-187 | BC-11043 | 2021-02-05 | IT Infrastructure |
| Palm Oil Food Grade | IC-11044 | 2024-04-15 | Supply Chain |
| AS-AC-782 | TC-11079 | 2023-11-06 | Supply Chain |
| Isoglucose 25% Lebensmittelrein | BC-11082 | 2021-10-15 | Product Management |
| Coconut Oil 70% Qualitätsstufe I | TC-11133 | 2024-11-03 | Supply Chain |
| Sorbic Acid 70% | IC-11135 | 2023-01-15 | Data Governance |
| Traubenzucker 70% | TC-11144 | 2021-10-28 | Compliance |
| Lactic Acid | BC-11152 | 2021-07-08 | Finance |
| SIG-82-ZXL-FF30 International | IC-11174 | 2023-03-02 | Data Governance |
| Excise NL 21% | IC-11180 | 2023-10-13 | Compliance |
| SO-AC-852 | BC-11188 | 2023-01-28 | Compliance |
| SIG-56-YYA-I8SV | BC-11198 | 2021-04-01 | Product Management |
| PR-EN-875 Group | BC-11207 | 2021-01-12 | IT Infrastructure |
| CO-OI-FO-GR-870 | TC-11214 | 2021-12-03 | Operations |
| Catalyst Enterprise International | IC-11219 | 2021-07-22 | Finance |
| Isoglucose | TC-11227 | 2024-02-02 | Finance |
| FR-25-GR-B-641 | IC-11242 | 2023-10-23 | Finance |
| Prism Versorgung GmbH | IC-11253 | 2022-09-20 | Compliance |
| Sodium Benzoate Pharma Grade | TC-11267 | 2021-07-13 | Supply Chain |
| VA-RE-G-25-207 | IC-11269 | 2024-08-04 | Data Governance |
| Traubenzucker 70% Qualitätsstufe I | IC-11285 | 2024-08-07 | Operations |
| Prism Materials | BC-11294 | 2022-12-22 | Supply Chain |
| nordic supply | BC-11297 | 2023-02-17 | Operations |
| Resistente Stärke | TC-11316 | 2024-11-20 | Product Management |
| Sonnenblumenöl Qualitätsstufe II | IC-11319 | 2023-04-10 | Operations |
| NO-LO-598 Holdings | TC-11327 | 2023-06-11 | Supply Chain |
| vat standard nl 20% | BC-11335 | 2022-08-26 | IT Infrastructure |
| atlantic trading | TC-11349 | 2021-05-22 | Supply Chain |
| SIG-47-YTF-UPMT | BC-11351 | 2024-06-28 | IT Infrastructure |
| Vertex Ingredients Ltd. | BC-11354 | 2023-04-19 | Product Management |
| dextrin | IC-11366 | 2021-06-22 | Data Governance |
| casein | BC-11371 | 2024-05-03 | Finance |
| Vanguard Versorgung BV | BC-11372 | 2023-11-15 | Finance |
| SO-AC-98-579 | TC-11374 | 2024-07-27 | Supply Chain |
| PA-OI-70-GR-B-781 | IC-11381 | 2021-11-02 | Supply Chain |
| SIG-64-BPY-A8RD | IC-11387 | 2023-02-01 | Data Governance |
| Horizon Logistics | TC-11395 | 2023-06-09 | Operations |
| Sodium Benzoate | BC-11403 | 2022-10-13 | Supply Chain |
| SIG-24-NPE-GDMB | IC-11412 | 2023-05-22 | Compliance |
| SIG-73-UUF-1F99 | TC-11438 | 2023-03-12 | Supply Chain |
| Lactic Acid Grade A | TC-11443 | 2021-09-25 | Compliance |
| meridian trading Group | TC-11451 | 2022-06-28 | Product Management |
| Prism Chemicals PLC | TC-11453 | 2022-07-14 | Operations |
| Citric Acid 70% | BC-11455 | 2023-06-16 | Finance |
| Core Chemicals AG | BC-11474 | 2022-08-20 | Supply Chain |
| Lactic Acid | IC-11488 | 2024-01-15 | Finance |
| VA-RE-N-7-243 | IC-11495 | 2024-12-06 | Compliance |
| fructose | IC-11506 | 2023-10-17 | Supply Chain |
| SIG-42-HBL-L3KU International | TC-11525 | 2022-10-27 | Finance |
| atlantic materials | BC-11532 | 2021-05-18 | Product Management |
| SIG-36-UIL-7X71 | BC-11540 | 2024-10-25 | Supply Chain |
| Rapsöl 99.5% Technische Qualität | TC-11545 | 2024-01-04 | Supply Chain |
| CY-577 | IC-11563 | 2021-12-04 | Product Management |
| SIG-53-LJE-NZKR | IC-11566 | 2024-11-25 | Data Governance |
| VE-SO-366 | IC-11570 | 2024-07-16 | IT Infrastructure |
| SO-IS-FO-GR-334 | BC-11592 | 2021-06-04 | Data Governance |
| Kaliumsorbat | IC-11596 | 2023-07-14 | IT Infrastructure |
| pinnacle supply | TC-11620 | 2022-07-03 | IT Infrastructure |
| isoglucose | TC-11638 | 2023-11-17 | Data Governance |
| EX-N-21-216 | BC-11643 | 2023-09-09 | Operations |
| SIG-32-UBB-EMYO | IC-11659 | 2021-08-05 | Operations |
| Meridian Werkstoffe | TC-11668 | 2022-10-06 | Operations |
| excise br 5% | BC-11673 | 2023-10-17 | Data Governance |
| Pinnacle Rohstoffe NV | IC-11681 | 2021-03-20 | Finance |
| ST-LO-136 | BC-11686 | 2023-09-14 | Data Governance |
| Traubenzucker Lebensmittelrein | TC-11708 | 2024-08-03 | Supply Chain |
| dextrin premium | TC-11716 | 2021-02-02 | IT Infrastructure |
| baltic enterprise KG | BC-11729 | 2023-06-16 | IT Infrastructure |
| SIG-44-FWT-OA3N | TC-11730 | 2022-07-19 | Supply Chain |
| CA-CA-947 | TC-11744 | 2021-05-19 | Product Management |
| Stellar Logistics | TC-11748 | 2023-07-06 | Finance |
| Atlas Logistik International | BC-11770 | 2023-09-03 | Supply Chain |
| withholding nl 15% | IC-11778 | 2021-09-03 | Finance |
| soy isolate | IC-11781 | 2023-06-24 | Supply Chain |
| pacific supply | IC-11784 | 2023-08-20 | Operations |
| resistant starch food grade | IC-11798 | 2023-10-16 | Operations |
| QU-SU-CO-959 | IC-11799 | 2022-03-24 | Operations |
| SIG-27-FHX-VO6Y | IC-11867 | 2022-02-14 | Finance |
| Cyclodextrin Qualitätsstufe I | IC-11901 | 2023-08-01 | IT Infrastructure |
| SIG-27-QBW-ROGA | IC-11904 | 2022-11-14 | Finance |
| SIG-62-AQF-O1V3 | TC-11905 | 2023-02-05 | IT Infrastructure |
| Rapeseed Oil 98% Standard | TC-11908 | 2023-05-07 | Data Governance |
| Pinnacle Rohstoffe NV | TC-11937 | 2023-04-16 | Data Governance |
| SIG-59-JAB-QS66 | TC-11957 | 2022-06-01 | Supply Chain |
| Prism Materials International | IC-11959 | 2021-01-11 | Operations |
| nordic logistics Group | BC-11975 | 2024-12-05 | Supply Chain |
| Zitronensäure 50% Qualitätsstufe I | BC-11986 | 2023-06-11 | Finance |
| Kasein 98% Premiumqualität | IC-11991 | 2023-05-28 | Product Management |
| potassium sorbate | BC-11994 | 2021-10-07 | Finance |
| quantum sourcing | TC-12010 | 2022-07-24 | Product Management |
| nordic ingredients | TC-12012 | 2023-07-05 | Operations |
| vat standard nl 19% | TC-12017 | 2024-05-18 | Compliance |
| SIG-78-WDE-NNV9 | IC-12038 | 2021-01-06 | Data Governance |
| Nexus Verarbeitung AG | BC-12041 | 2021-06-24 | Data Governance |
| SIG-17-UCW-S6NB | BC-12044 | 2021-12-01 | Finance |
| SIG-57-LIL-I8Z3 Inc. | IC-12068 | 2021-05-09 | Compliance |
| SIG-76-GST-OWGM | BC-12070 | 2022-02-21 | Finance |
| Zitronensäure 70% | TC-12086 | 2024-04-11 | Product Management |
| AS-AC-70-133 | IC-12095 | 2021-02-04 | IT Infrastructure |
| PE-PR-746 | TC-12105 | 2022-02-27 | Product Management |
| Soy Isolate 99.5% Premium | BC-12110 | 2024-09-10 | Operations |
| FR-98-PR-250 | BC-12117 | 2024-06-27 | Data Governance |
| Nexus Ingredients SARL | IC-12159 | 2021-06-18 | Product Management |
| Palm Oil 25% Grade A | IC-12200 | 2021-10-07 | Operations |
| SIG-36-JLA-CSEN | BC-12222 | 2022-03-07 | IT Infrastructure |
| Ascorbic Acid 99.5% Technische Qualität | IC-12224 | 2024-02-28 | Operations |
| WH-GL-99.5-GR-A-933 | TC-12230 | 2023-01-06 | Product Management |
| Weizenklebereiweiß Qualitätsstufe II | IC-12234 | 2022-10-02 | IT Infrastructure |
| Dextrose Food Grade | TC-12246 | 2021-06-21 | Finance |
| PR-CO-443 Group | TC-12248 | 2022-02-12 | Product Management |
| maltodextrin de10 | BC-12266 | 2024-04-06 | Supply Chain |
| Glucose Syrup | BC-12268 | 2023-07-23 | Finance |
| Soja Isolate | TC-12270 | 2021-05-28 | Finance |
| SIG-79-IKL-24HE | BC-12291 | 2022-07-13 | Operations |
| SIG-24-VMY-QMRL | BC-12304 | 2022-12-27 | Operations |
| Atlas Commodities SAS | BC-12307 | 2024-12-12 | Supply Chain |
| palm oil 50% premium | BC-12313 | 2022-04-08 | Finance |
| SIG-83-JEP-R0ZJ | IC-12341 | 2021-11-25 | IT Infrastructure |
| Atlas Werkstoffe | BC-12344 | 2022-01-25 | Finance |
| Baltic Sourcing | TC-12355 | 2023-09-27 | Operations |
| SIG-72-JEH-P5K7 | BC-12367 | 2024-09-25 | Product Management |
| CE-MA-720 | TC-12381 | 2022-05-14 | Product Management |
| casein standard | TC-12397 | 2022-02-28 | Compliance |
| CE-PR-134 | TC-12411 | 2021-02-19 | Product Management |
| RE-ST-GR-B-805 | BC-12413 | 2022-12-07 | Supply Chain |
| continental processing SA | TC-12435 | 2023-07-07 | IT Infrastructure |
| SIG-56-FFG-XS2P | TC-12437 | 2022-06-16 | Product Management |
| SIG-72-KAT-NI1G | BC-12440 | 2021-09-19 | Supply Chain |
| RE-ST-GR-B-598 | TC-12446 | 2022-05-21 | Operations |
| Vat Reduced IN 25% | BC-12452 | 2021-01-06 | Finance |
| Nexus Werkstoffe | IC-12454 | 2023-07-21 | IT Infrastructure |
| SIG-39-BAT-DD7R | IC-12460 | 2021-11-25 | Operations |
| Premier Logistik | IC-12466 | 2024-08-02 | Operations |
| SIG-51-EJL-Y9QB | BC-12484 | 2024-11-19 | Finance |
| maltodextrin de25 | IC-12487 | 2021-10-22 | Operations |
| MA-DE-ST-267 | BC-12499 | 2023-01-06 | Operations |
| SIG-75-WDP-0BHF | BC-12516 | 2023-12-01 | Operations |
| palm oil | IC-12518 | 2024-01-10 | Product Management |
| sodium benzoate premium | TC-12534 | 2024-10-25 | Finance |
| Potassium Sorbate 50% Grade B | TC-12552 | 2022-10-10 | Compliance |
| Nexus Enterprise | BC-12564 | 2024-10-25 | IT Infrastructure |
| Coconut Oil 25% Technical | TC-12588 | 2022-03-09 | Operations |
| Elite Logistics Holdings | BC-12592 | 2022-06-13 | IT Infrastructure |
| Kasein 98% Technische Qualität | TC-12602 | 2023-01-12 | Operations |
| SIG-69-UAZ-1ODW | BC-12612 | 2022-11-06 | Product Management |
| SIG-65-SMZ-JJEO | IC-12626 | 2024-06-17 | Product Management |
| Sunflower Oil Grade A | IC-12631 | 2023-03-07 | Operations |
| dextrose 99.5% standard | IC-12648 | 2023-03-08 | Operations |
| Vat Standard GB 21% | IC-12653 | 2023-06-10 | Finance |
| Zenith Manufacturing Holdings | IC-12676 | 2021-10-13 | Product Management |
| SIG-40-YZP-9CC3 | TC-12709 | 2021-04-28 | Supply Chain |
| Sonnenblumenöl | BC-12714 | 2021-02-18 | Supply Chain |
| CU-DU-D-0-955 | TC-12730 | 2022-08-24 | Supply Chain |
| Vat Standard NL 5% | BC-12741 | 2022-04-06 | IT Infrastructure |
| Customs Duty CN 7% | BC-12759 | 2023-01-16 | Operations |
| Vat Standard NL 19% | TC-12773 | 2021-09-08 | Finance |
| Elite Trading | IC-12793 | 2023-03-12 | Data Governance |
| RA-OI-98-679 | TC-12810 | 2021-05-01 | Product Management |
| SIG-95-LOJ-S1L2 | BC-12817 | 2024-12-08 | Data Governance |
| Zitronensäure 70% Lebensmittelrein | IC-12839 | 2024-07-26 | Finance |
| Fructose Food Grade | IC-12858 | 2022-06-11 | Finance |
| Wheat Gluten 50% | IC-12860 | 2024-10-25 | Supply Chain |
| dextrose 25% tech grade | BC-12865 | 2022-06-05 | Product Management |
| SIG-73-UUF-1F99 | TC-12868 | 2022-04-25 | IT Infrastructure |
| SO-IS-PR-242 | TC-12874 | 2021-08-08 | Operations |
| SIG-13-JUR-FV2B | TC-12911 | 2022-07-22 | Product Management |
| Dextrose Food Grade | BC-12913 | 2022-04-05 | Supply Chain |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | TC-12931 | 2022-08-04 | Supply Chain |
| glucose syrup 25% | IC-12933 | 2021-10-25 | Supply Chain |
| SIG-72-YVG-ZCUK | IC-12951 | 2023-07-18 | Compliance |
| SIG-24-KLH-SHKW | BC-12954 | 2023-04-25 | Supply Chain |
| calcium carbonate food grade | TC-12966 | 2022-07-15 | Operations |
| RE-ST-223 | IC-12975 | 2022-02-23 | Data Governance |
| rapeseed oil 70% standard | IC-12992 | 2022-02-01 | Data Governance |
| Atlantic Distribution Group | BC-13010 | 2023-07-27 | Supply Chain |
| prism industries Inc. | BC-13029 | 2024-12-01 | Product Management |
| Pacific Werkstoffe GmbH | TC-13052 | 2023-05-23 | Finance |
| SIG-52-QOU-LC66 | TC-13062 | 2024-10-12 | Data Governance |
| Apex Logistics | IC-13063 | 2021-03-05 | IT Infrastructure |
| Vat Standardqualität US 5% | IC-13073 | 2021-07-19 | Product Management |
| SIG-96-FYH-4ROJ SARL | IC-13078 | 2022-08-08 | Supply Chain |
| SIG-46-SVJ-5IZO | TC-13090 | 2023-06-19 | Data Governance |
| sorbic acid 98% | BC-13101 | 2022-07-13 | Finance |
| sorbic acid 98% | TC-13106 | 2024-11-24 | IT Infrastructure |
| wheat gluten 50% pharma grade | IC-13116 | 2022-07-15 | Supply Chain |
| AP-SU-CO-755 | IC-13129 | 2022-08-26 | IT Infrastructure |
| Core Logistik | BC-13141 | 2024-05-14 | Finance |
| SIG-97-WMO-6B83 | IC-13144 | 2024-03-18 | Operations |
| Core Materials | BC-13145 | 2022-12-13 | Compliance |
| VA-LO-948 | TC-13147 | 2021-03-12 | IT Infrastructure |
| Vat Reduced BR 10% | BC-13167 | 2022-08-19 | Data Governance |
| Casein | BC-13200 | 2024-10-01 | Operations |
| VA-RE-C-19-810 | IC-13219 | 2023-10-13 | Supply Chain |
| Quantum Rohstoffe PLC | IC-13221 | 2021-06-14 | Finance |
| Horizon Logistics | BC-13239 | 2024-10-21 | Operations |
| Weizenklebereiweiß Qualitätsstufe II | IC-13243 | 2021-11-01 | Data Governance |
| SIG-63-KXZ-46Q1 | BC-13252 | 2022-08-19 | IT Infrastructure |
| resistant starch food grade | BC-13258 | 2022-10-16 | Data Governance |
| withholding nl 20% | BC-13275 | 2021-06-07 | Supply Chain |
| Soja Isolate 50% Qualitätsstufe II | IC-13279 | 2023-03-26 | Compliance |
| SIG-27-QBW-ROGA | BC-13286 | 2023-11-21 | Product Management |
| EL-SO-688 | TC-13379 | 2024-09-04 | Compliance |
| Calcium Carbonate 98% Pharmazeutisch rein | BC-13380 | 2021-08-15 | Data Governance |
| VA-RE-F-10-219 | BC-13389 | 2023-07-09 | Operations |
| Dextrin | TC-13398 | 2021-12-08 | Finance |
| Pea Protein 25% | BC-13406 | 2024-04-26 | IT Infrastructure |
| Stratos Materials Group | BC-13417 | 2024-05-17 | Finance |
| Pacific Distribution International | TC-13449 | 2024-07-18 | Product Management |
| citric acid 70% | IC-13457 | 2021-04-18 | Operations |
| SIG-68-DWS-MNR6 | BC-13465 | 2022-10-10 | IT Infrastructure |
| Traubenzucker 50% Qualitätsstufe II | IC-13469 | 2023-05-10 | Data Governance |
| Core Partners PLC | TC-13473 | 2021-03-13 | Operations |
| Traubenzucker 99.5% | TC-13508 | 2024-01-16 | Operations |
| Maltodextrin-Pulver DE20 | TC-13521 | 2024-05-28 | Finance |
| RE-ST-25-TE-177 | IC-13523 | 2023-08-09 | Operations |
| nordic partners | BC-13528 | 2024-10-04 | Compliance |
| Natriumchlorid 70% | TC-13532 | 2022-05-19 | Data Governance |
| CY-515 | IC-13539 | 2022-04-17 | Finance |
| Pinnacle Verarbeitung | TC-13544 | 2024-07-23 | Operations |
| SIG-48-OWU-RTGZ | TC-13548 | 2023-09-13 | Product Management |
| dextrin | IC-13573 | 2024-03-16 | Data Governance |
| AT-LO-583 | IC-13577 | 2023-04-25 | Finance |
| Glucose Syrup 25% | TC-13598 | 2022-05-04 | Data Governance |
| Maltodextrin-Pulver DE15 | TC-13600 | 2023-02-25 | Finance |
| vat standard gb 21% | TC-13614 | 2021-09-23 | Supply Chain |
| vat standard gb 21% | BC-13638 | 2021-09-05 | IT Infrastructure |
| Potassium Sorbate 50% | IC-13649 | 2021-09-02 | IT Infrastructure |
| SIG-30-LJO-TN4Y | IC-13656 | 2022-04-27 | Data Governance |
| SIG-39-SXC-H14U | TC-13679 | 2021-01-19 | Supply Chain |
| PR-IN-135 International | BC-13711 | 2021-06-19 | Operations |
| SIG-16-XLB-CB69 | BC-13721 | 2022-12-16 | Data Governance |
| calcium carbonate | IC-13727 | 2023-03-23 | Operations |
| Pinnacle Trading | TC-13734 | 2021-11-09 | Product Management |
| Pinnacle Processing | IC-13736 | 2021-11-08 | Data Governance |
| SIG-28-STQ-YUPS | TC-13764 | 2022-09-22 | Finance |
| SIG-68-KHP-8RTJ | IC-13771 | 2022-04-24 | Operations |
| SIG-60-PEY-H3GM | BC-13779 | 2021-06-11 | Supply Chain |
| Glucose Syrup Food Grade | TC-13799 | 2024-01-27 | Compliance |
| Resistant Starch 98% | IC-13803 | 2024-01-20 | Supply Chain |
| Rapsöl 50% Qualitätsstufe I | TC-13834 | 2024-03-21 | Supply Chain |
| Resistant Starch 99.5% | IC-13840 | 2024-03-19 | Data Governance |
| SIG-96-UYO-0BNC | IC-13848 | 2023-04-26 | Data Governance |
| resistant starch | TC-13864 | 2023-06-22 | Product Management |
| SIG-72-LCQ-PU6W | TC-13869 | 2022-05-27 | Finance |
| Natriumbenzoat 25% Qualitätsstufe II | BC-13881 | 2022-07-05 | Compliance |
| BA-DI-254 | BC-13889 | 2023-01-01 | Finance |
| Rapeseed Oil | IC-13907 | 2021-02-09 | IT Infrastructure |
| sodium benzoate 50% | TC-13947 | 2022-03-22 | Compliance |
| SIG-47-GAT-ET7B | IC-13953 | 2024-12-07 | Compliance |
| Catalyst Enterprise International | IC-13978 | 2024-01-26 | Data Governance |
| Pinnacle Trading Group | IC-13985 | 2022-06-10 | Finance |
| SIG-18-PCA-V46E | TC-13989 | 2022-02-18 | Supply Chain |
| Zitronensäure Premiumqualität | IC-13992 | 2021-11-04 | Operations |
| Quantum Partners Group | TC-13995 | 2024-07-22 | Finance |
| Palmfett Lebensmittelrein | TC-13997 | 2022-01-13 | IT Infrastructure |
| prime commodities | TC-14011 | 2022-02-25 | Finance |
| SIG-93-NSF-DUXM Corp. | IC-14024 | 2024-06-27 | Product Management |
| SIG-76-CCF-UYHN | IC-14027 | 2021-06-09 | IT Infrastructure |
| Stratos Ingredients SARL | BC-14036 | 2023-07-05 | Supply Chain |
| SIG-44-NHM-IY9D | BC-14042 | 2024-11-22 | Product Management |
| PI-LO-710 NV | BC-14072 | 2021-11-11 | Operations |
| PO-SO-50-TE-282 | IC-14090 | 2021-11-16 | IT Infrastructure |
| Withholding NL 5% | IC-14097 | 2021-09-07 | Supply Chain |
| LA-AC-554 | BC-14099 | 2023-07-14 | IT Infrastructure |
| rapeseed oil 70% tech grade | IC-14111 | 2023-12-18 | Operations |
| SIG-94-QXV-F18G | TC-14129 | 2022-10-28 | IT Infrastructure |
| dextrin standard | TC-14140 | 2024-05-28 | Supply Chain |
| Cyclodextrin | BC-14154 | 2022-12-18 | Data Governance |
| IS-230 | TC-14164 | 2024-04-06 | Operations |
| SU-OI-TE-705 | TC-14178 | 2023-06-14 | Finance |
| VE-SO-914 Ltd. | TC-14179 | 2023-02-18 | Product Management |
| Fructose | IC-14189 | 2022-10-04 | Product Management |
| Isoglucose 70% | TC-14199 | 2021-06-16 | Operations |
| Central Logistics | BC-14204 | 2022-02-14 | Data Governance |
| Baltic Sourcing | TC-14209 | 2024-03-06 | Finance |
| Vertex Werkstoffe | BC-14211 | 2021-01-04 | Data Governance |
| SIG-69-UAZ-1ODW | BC-14214 | 2022-11-15 | Operations |
| NE-IN-874 SA | IC-14216 | 2024-03-11 | Finance |
| Nordic Manufacturing NV | TC-14225 | 2023-04-25 | Finance |
| SIG-24-MFK-ZAUG | TC-14231 | 2023-04-23 | IT Infrastructure |
| VA-RE-B-7-231 | IC-14256 | 2021-11-27 | Supply Chain |
| PI-LO-710 NV | TC-14263 | 2024-07-08 | Product Management |
| customs duty de 7% | IC-14269 | 2023-01-05 | Finance |
| SIG-96-FYH-4ROJ SARL | IC-14274 | 2023-01-08 | Supply Chain |
| Soja Isolate 98% Premiumqualität | BC-14277 | 2024-07-04 | IT Infrastructure |
| Atlas Manufacturing Corp. | BC-14283 | 2021-12-23 | Data Governance |
| palm oil food grade | IC-14313 | 2024-10-27 | Data Governance |
| coconut oil 25% standard | IC-14327 | 2024-08-14 | Product Management |
| stellar supply | TC-14343 | 2022-09-20 | Supply Chain |
| AP-SU-CO-787 | TC-14349 | 2023-06-15 | Supply Chain |
| Central Supply Co. | IC-14368 | 2022-07-15 | Supply Chain |
| SIG-30-LJO-TN4Y | TC-14370 | 2023-11-18 | Product Management |
| PA-CH-795 | BC-14374 | 2021-03-28 | Product Management |
| Lactic Acid 99.5% Grade B | BC-14381 | 2022-05-28 | Data Governance |
| SIG-68-TVY-N4XJ | IC-14390 | 2024-06-09 | Supply Chain |
| SIG-98-NDY-OCEW | IC-14405 | 2022-12-22 | Data Governance |
| AT-MA-796 LLC | TC-14435 | 2021-03-20 | Operations |
| SIG-39-MGB-86C4 | IC-14452 | 2024-05-10 | Compliance |
| Prism Vertrieb NV | TC-14455 | 2023-03-24 | Data Governance |
| Elite Sourcing | IC-14461 | 2024-08-09 | Operations |
| SIG-53-MEZ-6IT1 | BC-14473 | 2022-07-15 | IT Infrastructure |
| WI-D-25-711 | IC-14475 | 2023-06-12 | Product Management |
| AT-LO-568 SA | BC-14477 | 2024-03-27 | Data Governance |
| prism industries International | TC-14480 | 2023-09-15 | Supply Chain |
| CO-OI-98-GR-A-763 | BC-14490 | 2024-07-24 | Compliance |
| soy isolate | TC-14494 | 2024-01-17 | Finance |
| CO-OI-98-PR-329 | BC-14498 | 2023-04-26 | Data Governance |
| Fructose Technische Qualität | IC-14522 | 2023-05-21 | Product Management |
| CI-AC-99.5-440 | BC-14531 | 2021-02-14 | IT Infrastructure |
| Calcium Carbonate 70% Premium | BC-14533 | 2024-05-01 | IT Infrastructure |
| AS-AC-279 | BC-14536 | 2022-05-07 | Operations |
| Premier Rohstoffe Holdings | BC-14545 | 2023-04-17 | Supply Chain |
| excise gb 19% | TC-14557 | 2021-08-21 | Supply Chain |
| Lactic Acid | IC-14561 | 2023-07-22 | Data Governance |
| Stratos Materials Group | IC-14568 | 2024-04-11 | Data Governance |
| lactic acid tech grade | BC-14576 | 2022-02-25 | Data Governance |
| SIG-78-WKT-9TDY SAS | BC-14591 | 2024-12-18 | Finance |
| withholding nl 5% | TC-14600 | 2024-01-21 | Operations |
| MA-DE-944 | IC-14608 | 2021-01-20 | IT Infrastructure |
| Calcium Carbonate 70% Premium | IC-14617 | 2021-11-17 | Finance |
| Rapeseed Oil | IC-14636 | 2022-02-07 | Finance |
| RE-ST-676 | BC-14664 | 2022-07-11 | IT Infrastructure |
| Fructose | TC-14666 | 2024-10-08 | Data Governance |
| VA-EN-308 | IC-14671 | 2024-02-22 | Operations |
| AS-AC-50-321 | IC-14673 | 2022-07-23 | Product Management |
| Cyclodextrin | BC-14682 | 2022-03-25 | Product Management |
| SIG-59-LNO-OJGF | IC-14687 | 2023-07-05 | IT Infrastructure |
| Traubenzucker Qualitätsstufe I | BC-14692 | 2023-04-24 | Product Management |
| CO-OI-98-PR-329 | TC-14697 | 2024-07-27 | Supply Chain |
| Resistente Stärke Lebensmittelrein | BC-14700 | 2023-06-11 | IT Infrastructure |
| Vat Reduced GB 0% | BC-14742 | 2021-10-27 | Compliance |
| SIG-18-NCG-WT1V | BC-14743 | 2023-09-03 | Finance |
| Core Logistik | IC-14745 | 2022-06-04 | Operations |
| SIG-28-FYV-P1ZR Group | BC-14751 | 2021-03-10 | Finance |
| DE-98-512 | BC-14753 | 2023-09-20 | IT Infrastructure |
| soy isolate 99.5% | BC-14759 | 2022-06-03 | Supply Chain |
| Glukosesirup Syrup | IC-14764 | 2024-09-08 | Supply Chain |
| PR-LO-801 AG | BC-14777 | 2023-01-16 | Supply Chain |
| nexus enterprise | BC-14783 | 2024-04-14 | Product Management |
| Casein Grade A | IC-14808 | 2022-06-01 | Finance |
| Vat Reduced FR 25% | TC-14828 | 2021-10-08 | Product Management |
| SIG-73-LLJ-LNGI | IC-14836 | 2022-04-21 | Compliance |
| Kasein Technische Qualität | TC-14844 | 2021-11-16 | Supply Chain |
| Glucose Syrup Food Grade | BC-14862 | 2022-05-13 | Supply Chain |
| Lactic Acid Technical | IC-14880 | 2022-05-23 | Operations |
| SIG-98-PIN-G89V | TC-14885 | 2021-07-11 | Data Governance |
| SIG-86-QXF-N0RG | TC-14888 | 2023-06-19 | Product Management |
| SIG-63-KXZ-46Q1 | BC-14898 | 2021-06-13 | Compliance |
| SIG-50-ABM-7VSK | TC-14918 | 2021-04-04 | Operations |
| Central Logistics | TC-14954 | 2021-11-04 | Supply Chain |
| Vat Reduced FR 20% | IC-14957 | 2024-01-15 | Finance |
| Kasein 50% Qualitätsstufe II | IC-14961 | 2024-11-21 | Supply Chain |
| HO-IN-526 Corp. | IC-14966 | 2024-10-27 | IT Infrastructure |
| atlas supply | TC-14989 | 2022-10-27 | Operations |
| zenith trading AG | BC-15010 | 2023-10-03 | Supply Chain |
| SO-AC-25-ST-106 | BC-15020 | 2022-09-17 | Supply Chain |
| SIG-89-TVE-WANI | BC-15039 | 2021-12-13 | Operations |
| Coconut Oil 98% | BC-15042 | 2021-10-03 | Compliance |
| DE-70-769 | IC-15048 | 2023-09-16 | IT Infrastructure |
| Soy Isolate 99.5% | TC-15060 | 2024-01-11 | Compliance |
| VA-PA-407 | IC-15080 | 2023-10-05 | Operations |
| Sonnenblumenöl Premiumqualität | TC-15087 | 2024-12-15 | Supply Chain |
| stellar logistics | TC-15097 | 2022-09-24 | Compliance |
| vanguard sourcing | BC-15111 | 2023-03-04 | Product Management |
| SO-AC-25-GR-B-198 | IC-15141 | 2023-07-24 | Supply Chain |
| SIG-85-SIL-CNEA | BC-15146 | 2021-11-28 | Product Management |
| PE-PR-PR-775 | TC-15156 | 2023-06-04 | Supply Chain |
| sodium benzoate 98% standard | BC-15159 | 2023-01-01 | IT Infrastructure |
| SIG-58-LWY-Q8P6 | TC-15183 | 2024-09-23 | IT Infrastructure |
| atlas materials | IC-15189 | 2024-12-28 | Finance |
| isoglucose | IC-15192 | 2024-04-06 | Supply Chain |
| soy isolate | IC-15194 | 2024-12-13 | Operations |
| SIG-38-AAT-YMEN | TC-15196 | 2021-04-17 | Finance |
| Dextrin 70% Pharma Grade | BC-15207 | 2022-09-23 | Data Governance |
| atlantic logistics SARL | IC-15215 | 2023-12-25 | Compliance |
| CE-MA-720 | IC-15227 | 2021-11-09 | IT Infrastructure |
| SIG-14-HQE-PUWC | IC-15259 | 2021-02-17 | Operations |
| Palmfett | TC-15267 | 2022-08-26 | Compliance |
| Pinnacle Sourcing | IC-15269 | 2023-01-18 | Data Governance |
| SU-OI-ST-194 | TC-15283 | 2022-05-22 | Compliance |
| AT-IN-100 Group | IC-15285 | 2021-03-14 | Compliance |
| Prism Werkstoffe International | IC-15289 | 2024-02-26 | Data Governance |
| SIG-57-QDA-RQ8R | BC-15296 | 2023-05-20 | Supply Chain |
| SIG-76-GDP-2JN8 | IC-15308 | 2021-10-03 | Product Management |
| Atlas Sourcing | IC-15325 | 2021-08-01 | Data Governance |
| SIG-48-UJX-49KW | IC-15357 | 2022-09-17 | Supply Chain |
| CU-DU-F-25-387 | IC-15361 | 2023-07-10 | IT Infrastructure |
| Catalyst Enterprise International | TC-15363 | 2021-10-05 | Supply Chain |
| SIG-24-MFK-ZAUG | IC-15375 | 2022-09-04 | Product Management |
| SIG-60-WEX-2G05 | IC-15394 | 2024-10-17 | Supply Chain |
| RE-ST-GR-B-805 | BC-15395 | 2021-11-25 | Product Management |
| Sunflower Oil Grade A | IC-15396 | 2022-02-03 | IT Infrastructure |
| Zitronensäure | BC-15398 | 2023-06-13 | Product Management |
| Natriumchlorid 25% Lebensmittelrein | IC-15402 | 2022-07-01 | Compliance |
| SIG-36-UIL-7X71 | BC-15409 | 2022-07-18 | Product Management |
| Ascorbic Acid Food Grade | BC-15436 | 2024-04-11 | Supply Chain |
| SIG-42-XLZ-4BOM | BC-15441 | 2023-02-17 | Compliance |
| AS-AC-99.5-TE-765 | IC-15444 | 2023-10-28 | IT Infrastructure |
| SIG-99-OQS-ADHF | IC-15475 | 2024-12-18 | Operations |
| SO-AC-70-542 | IC-15477 | 2022-08-15 | IT Infrastructure |
| LA-AC-ST-663 | BC-15479 | 2021-05-01 | Data Governance |
| Prime Sourcing | BC-15488 | 2021-03-12 | Compliance |
| SO-BE-99.5-TE-213 | IC-15516 | 2023-11-02 | Product Management |
| cyclodextrin | IC-15519 | 2021-02-25 | Data Governance |
| central materials BV | BC-15550 | 2022-08-02 | Supply Chain |
| Calcium Carbonate Lebensmittelrein | BC-15566 | 2021-10-09 | Operations |
| resistant starch 98% | BC-15570 | 2023-10-01 | IT Infrastructure |
| Baltic Enterprise Holdings | TC-15583 | 2022-01-24 | Compliance |
| CO-OI-25-252 | IC-15597 | 2021-07-19 | Supply Chain |
| SO-CH-70-365 | TC-15608 | 2024-06-22 | Operations |
| PI-IN-970 Corp. | BC-15616 | 2023-08-10 | Data Governance |
| Lactic Acid Lebensmittelrein | BC-15626 | 2023-05-22 | Compliance |
| Stratos Sourcing | IC-15632 | 2023-03-01 | IT Infrastructure |
| resistant starch | TC-15634 | 2024-05-06 | IT Infrastructure |
| SIG-78-LTE-H4VL | IC-15637 | 2023-02-26 | Operations |
| Zitronensäure 70% Lebensmittelrein | IC-15643 | 2023-07-27 | Compliance |
| nordic partners | IC-15650 | 2022-02-24 | Data Governance |
| SIG-50-GYK-UH5P | IC-15658 | 2022-11-14 | Data Governance |
| Natriumchlorid 98% | TC-15661 | 2024-12-20 | IT Infrastructure |
| CU-DU-I-21-633 | TC-15671 | 2022-05-14 | Data Governance |
| EL-SU-CO-921 | BC-15676 | 2024-09-09 | Finance |
| SIG-26-PJJ-DUD8 | IC-15677 | 2024-11-20 | Product Management |
| NO-DI-180 Ltd. | IC-15689 | 2023-07-19 | IT Infrastructure |
| sunflower oil | TC-15695 | 2023-09-21 | Supply Chain |
| CA-TE-562 | TC-15697 | 2024-10-08 | Product Management |
| EX-I-15-456 | IC-15699 | 2024-11-27 | Compliance |
| SO-CH-GR-A-776 | BC-15712 | 2021-10-15 | Compliance |
| Lactic Acid Grade B | BC-15720 | 2022-09-02 | Finance |
| Isoglucose 70% Food Grade | IC-15730 | 2023-04-09 | Product Management |
| SIG-72-OSZ-6T19 | IC-15736 | 2024-10-05 | Compliance |
| Sorbinsäure 98% | BC-15819 | 2021-06-02 | Product Management |
| Soy Isolate | BC-15846 | 2021-06-01 | Compliance |
| Prime Handel Group | BC-15847 | 2021-08-02 | Operations |
| CI-AC-GR-A-280 | IC-15872 | 2021-10-09 | Product Management |
| Lactic Acid 50% Premium | TC-15890 | 2021-11-11 | Compliance |
| fructose premium | BC-15894 | 2023-07-05 | Operations |
| Lactic Acid Technical | TC-15911 | 2023-03-14 | Data Governance |
| DE-TE-406 | TC-15915 | 2021-09-14 | Compliance |
| SIG-20-UGT-P0LW | IC-15934 | 2021-08-10 | Compliance |
| SIG-53-MEZ-6IT1 | BC-15938 | 2023-03-23 | Finance |
| Prism Sourcing | TC-15941 | 2022-02-16 | Data Governance |
| SIG-69-OFZ-JW34 | IC-15943 | 2024-08-05 | Supply Chain |
| EX-B-5-383 | BC-15947 | 2024-03-21 | Data Governance |
| CI-AC-GR-A-280 | BC-15948 | 2022-09-20 | Finance |
| Core Chemicals | IC-15957 | 2022-08-18 | Product Management |
| SIG-79-GKV-W8GA | TC-15974 | 2023-09-17 | Product Management |
| SIG-43-NCZ-FT9Z | TC-15981 | 2023-06-16 | Finance |
| Traubenzucker Lebensmittelrein | TC-16011 | 2023-01-13 | Data Governance |
| Resistente Stärke | TC-16017 | 2024-07-13 | Finance |
| calcium carbonate | BC-16019 | 2024-05-10 | Operations |
| Atlantic Vertrieb Holdings | TC-16030 | 2022-08-28 | Operations |
| AS-AC-50-321 | IC-16058 | 2023-01-10 | Compliance |
| Horizon Materials PLC | TC-16067 | 2021-07-01 | Compliance |
| Nexus Processing Holdings | IC-16071 | 2024-06-16 | Finance |
| Stellar Rohstoffe | BC-16075 | 2023-01-06 | Data Governance |
| Coconut Oil 50% Technische Qualität | TC-16086 | 2024-08-22 | Operations |
| ascorbic acid food grade | BC-16108 | 2022-05-09 | Finance |
| wheat gluten | TC-16110 | 2023-08-27 | Operations |
| baltic trading NV | BC-16114 | 2023-03-23 | Data Governance |
| LA-AC-GR-A-949 | BC-16118 | 2024-10-10 | IT Infrastructure |
| Casein 25% Grade A | BC-16127 | 2021-04-27 | Finance |
| CO-OI-98-PR-329 | IC-16132 | 2021-08-01 | Data Governance |
| AS-AC-439 | IC-16134 | 2023-10-12 | Compliance |
| Meridian Ingredients | BC-16149 | 2022-06-15 | Data Governance |
| glucose syrup tech grade | TC-16150 | 2022-02-06 | Operations |
| VA-ST-N-5-804 | BC-16181 | 2024-12-17 | Product Management |
| lactic acid 98% premium | IC-16190 | 2024-08-01 | Operations |
| SIG-60-WEX-2G05 | BC-16191 | 2022-09-08 | Operations |
| sodium chloride tech grade | BC-16199 | 2023-09-04 | Compliance |
| CO-OI-25-TE-157 | TC-16204 | 2021-11-19 | Operations |
| CO-OI-25-252 | TC-16209 | 2024-10-26 | IT Infrastructure |
| SIG-39-ARU-8X3V | IC-16212 | 2021-02-13 | Supply Chain |
| SIG-89-PFV-OOFP | IC-16235 | 2021-08-22 | Product Management |
| Meridian Trading | TC-16239 | 2021-09-22 | IT Infrastructure |
| SIG-67-MFG-46DE | IC-16244 | 2021-06-05 | Data Governance |
| SIG-43-GRJ-P3HT | BC-16259 | 2021-05-15 | IT Infrastructure |
| PA-MA-166 SARL | IC-16268 | 2021-08-28 | Finance |
| Citric Acid | TC-16278 | 2022-10-22 | Supply Chain |
| SO-CH-TE-286 | BC-16302 | 2023-11-17 | IT Infrastructure |
| dextrose 50% | BC-16316 | 2023-03-04 | Data Governance |
| Ascorbic Acid 50% Standardqualität | BC-16335 | 2022-07-04 | IT Infrastructure |
| Prime Logistik | IC-16339 | 2021-02-07 | Operations |
| core materials | BC-16359 | 2024-06-23 | Operations |
| Maltodextrin DE10 | BC-16365 | 2022-12-06 | Finance |
| Pinnacle Processing | BC-16370 | 2023-11-18 | Operations |
| Cyclodextrin Pharma Grade | BC-16372 | 2023-07-02 | Compliance |
| LA-AC-FO-GR-687 | IC-16397 | 2021-04-02 | Finance |
| Dextrose | IC-16405 | 2024-01-26 | Compliance |
| SU-OI-TE-879 | BC-16409 | 2022-08-21 | Operations |
| Ascorbic Acid Standardqualität | IC-16442 | 2023-12-25 | Compliance |
| SIG-53-TLC-AZKT | BC-16447 | 2023-05-04 | Compliance |
| SIG-50-PNF-Z2E8 | IC-16449 | 2021-04-09 | Product Management |
| VA-ST-F-15-255 | BC-16453 | 2022-09-06 | Operations |
| meridian industries | IC-16470 | 2023-11-12 | IT Infrastructure |
| SIG-16-FVU-3EBQ | IC-16474 | 2023-12-22 | Product Management |
| Central Logistik GmbH | TC-16488 | 2021-02-24 | Finance |
| Glukosesirup Syrup 99.5% Standardqualität | BC-16499 | 2024-08-03 | IT Infrastructure |
| Premier Solutions LLC | BC-16511 | 2021-05-02 | Finance |
| Dextrin | TC-16513 | 2023-07-09 | Finance |
| Meridian Versorgung GmbH | IC-16521 | 2021-09-21 | Product Management |
| SIG-84-DSO-4S47 | TC-16528 | 2021-12-01 | Operations |
| LA-AC-TE-651 | BC-16540 | 2022-09-15 | Operations |
| MA-DE-ST-267 | IC-16555 | 2021-03-17 | Operations |
| sunflower oil food grade | TC-16579 | 2023-06-04 | Compliance |
| Rapeseed Oil | IC-16583 | 2023-12-16 | Operations |
| SIG-30-RXC-HFDI | TC-16589 | 2024-02-28 | Finance |
| vertex materials | IC-16591 | 2022-07-15 | Finance |
| SIG-50-PNF-Z2E8 | BC-16594 | 2022-08-06 | Product Management |
| Ascorbic Acid 98% Pharmazeutisch rein | TC-16599 | 2021-05-04 | Data Governance |
| SIG-43-FST-BKJ7 | IC-16601 | 2021-01-22 | IT Infrastructure |
| MA-DE-933 | IC-16606 | 2021-01-15 | Operations |
| Apex Chemicals | IC-16613 | 2024-03-14 | Product Management |
| SIG-21-PIO-0RWR | BC-16615 | 2023-10-08 | Compliance |
| IS-802 | IC-16621 | 2023-03-23 | Operations |
| Elite Partners International | TC-16648 | 2021-07-08 | Finance |
| Fructose Food Grade | IC-16649 | 2022-04-06 | IT Infrastructure |
| Glukosesirup Syrup Qualitätsstufe II | IC-16657 | 2021-02-06 | Finance |
| Catalyst Logistik | IC-16659 | 2022-02-18 | Operations |
| Continental Processing | TC-16661 | 2024-09-03 | Product Management |
| Baltic Handel | IC-16670 | 2021-08-21 | Finance |
| Isoglucose | IC-16683 | 2021-04-15 | Finance |
| Pinnacle Logistik BV | TC-16687 | 2023-01-07 | Supply Chain |
| SIG-65-ZJD-9K32 Group | TC-16727 | 2022-06-15 | Data Governance |
| NE-CO-575 Holdings | BC-16762 | 2021-07-01 | Supply Chain |
| Maltodextrin DE30 Standard | TC-16768 | 2021-06-08 | Operations |
| Soja Isolate Premiumqualität | BC-16769 | 2023-05-19 | Product Management |
| sodium chloride | TC-16779 | 2021-11-20 | Supply Chain |
| Nordic Verarbeitung | BC-16784 | 2024-08-23 | Finance |
| Wheat Gluten Food Grade | TC-16798 | 2023-06-03 | Supply Chain |
| Vertex Distribution AG | TC-16808 | 2024-08-08 | Operations |
| Prism Partners | IC-16817 | 2021-03-28 | Supply Chain |
| Customs Duty CN 7% | BC-16822 | 2022-12-26 | Finance |
| Zitronensäure | IC-16826 | 2023-05-21 | Compliance |
| SIG-88-AGF-FF5L | BC-16828 | 2022-06-19 | Compliance |
| SIG-21-PIO-0RWR | TC-16851 | 2023-11-17 | Product Management |
| Global Materials NV | BC-16864 | 2021-03-08 | Product Management |
| CU-DU-U-15-275 | TC-16899 | 2024-10-05 | Operations |
| Dextrin Standardqualität | BC-16904 | 2024-05-20 | Finance |
| SIG-28-MAP-2EOP Holdings | IC-16945 | 2023-05-02 | Compliance |
| Ascorbic Acid Premiumqualität | BC-16958 | 2024-08-12 | IT Infrastructure |
| Apex Werkstoffe | TC-16975 | 2024-02-21 | Finance |
| Prism Industrien Holdings | TC-16979 | 2022-05-17 | Data Governance |
| SIG-30-PVA-ZMF8 | TC-16994 | 2023-10-24 | Finance |
| isoglucose tech grade | TC-17006 | 2023-04-20 | Supply Chain |
| coconut oil | TC-17018 | 2023-01-06 | Operations |
| Traubenzucker Standardqualität | TC-17040 | 2024-01-26 | Product Management |
| IS-FO-GR-335 | BC-17055 | 2023-09-01 | Operations |
| pacific materials | BC-17057 | 2024-03-10 | Compliance |
| SIG-90-SJW-O06V | TC-17062 | 2021-12-08 | Data Governance |
| Vat Reduced GB 25% | IC-17063 | 2022-01-07 | Data Governance |
| Kaliumsorbat 50% Technische Qualität | BC-17068 | 2021-02-13 | Compliance |
| SIG-37-CWM-V4K0 | BC-17134 | 2024-10-25 | Product Management |
| citric acid 25% tech grade | IC-17154 | 2023-07-10 | IT Infrastructure |
| SIG-88-LSM-PKYH Holdings | BC-17177 | 2022-06-15 | IT Infrastructure |
| Lactic Acid | IC-17201 | 2024-04-18 | Compliance |
| SIG-60-KAS-IVMD | IC-17202 | 2021-10-21 | Product Management |
| AS-AC-FO-GR-283 | IC-17215 | 2021-03-26 | IT Infrastructure |
| Natriumchlorid 98% Pharmazeutisch rein | TC-17221 | 2021-06-21 | Product Management |
| Customs Duty US 20% | TC-17252 | 2022-10-23 | Operations |
| Pinnacle Logistics International | IC-17269 | 2024-03-10 | Compliance |
| customs duty de 5% | TC-17270 | 2021-01-24 | Product Management |
| VA-ST-D-19-529 | TC-17273 | 2024-10-13 | Finance |
| Maltodextrin DE5 Grade A | IC-17275 | 2022-01-09 | Data Governance |
| dextrose | TC-17277 | 2024-02-02 | IT Infrastructure |
| fructose 99.5% premium | TC-17285 | 2023-10-04 | Finance |
| resistant starch | TC-17318 | 2021-01-14 | Compliance |
| casein | IC-17325 | 2024-04-01 | Operations |
| SIG-83-BZY-VHAE | BC-17331 | 2023-10-01 | Supply Chain |
| Lactic Acid Lebensmittelrein | BC-17335 | 2024-01-16 | Supply Chain |
| SIG-98-OXJ-W0H6 SAS | IC-17349 | 2024-06-10 | Operations |
| SO-IS-GR-A-940 | TC-17378 | 2023-09-03 | Compliance |
| Sunflower Oil 98% Premium | TC-17396 | 2023-07-21 | Compliance |
| VA-ST-N-10-130 | TC-17399 | 2023-10-11 | Product Management |
| potassium sorbate | TC-17405 | 2023-11-25 | Product Management |
| Ascorbic Acid 50% Standardqualität | TC-17409 | 2023-05-18 | Compliance |
| Nordic Ingredients SARL | IC-17410 | 2024-05-06 | Supply Chain |
| citric acid premium | TC-17413 | 2024-05-18 | Operations |
| SIG-93-VLZ-VI4P | TC-17415 | 2021-11-16 | Operations |
| VE-LO-902 Group | TC-17436 | 2021-12-26 | Data Governance |
| Zenith Handel | TC-17443 | 2024-05-17 | IT Infrastructure |
| Resistente Stärke Qualitätsstufe II | IC-17447 | 2022-04-14 | Supply Chain |
| SIG-85-TWH-HQKB | BC-17450 | 2021-02-26 | Product Management |
| quantum commodities Holdings | IC-17456 | 2022-07-07 | Operations |
| sodium benzoate 98% | IC-17466 | 2023-12-19 | IT Infrastructure |
| SIG-24-VMY-QMRL | BC-17482 | 2022-06-24 | Compliance |
| SIG-79-OZQ-4I2N | TC-17503 | 2022-06-08 | Operations |
| SIG-66-AQR-B68Q | IC-17512 | 2023-07-22 | Finance |
| sodium benzoate 25% standard | IC-17514 | 2022-09-23 | Operations |
| Wheat Gluten Grade B | TC-17525 | 2021-03-23 | Product Management |
| DE-70-769 | TC-17530 | 2022-05-18 | Operations |
| stratos materials Group | TC-17543 | 2024-12-22 | Operations |
| Citric Acid 70% | BC-17544 | 2021-06-07 | Compliance |
| SIG-91-UWU-GPZB | IC-17551 | 2021-11-07 | Data Governance |
| SIG-10-NNQ-6CGO | BC-17552 | 2022-10-02 | Compliance |
| Pinnacle Ingredients KG | TC-17564 | 2021-12-24 | Supply Chain |
| citric acid 25% | TC-17573 | 2024-10-03 | Supply Chain |
| resistant starch 50% | BC-17575 | 2023-11-13 | Operations |
| Nexus Solutions SAS | TC-17580 | 2021-06-05 | Data Governance |
| casein 98% standard | TC-17582 | 2021-02-21 | Data Governance |
| Palm Oil | TC-17587 | 2022-06-14 | Data Governance |
| nordic manufacturing International | IC-17588 | 2021-07-18 | Finance |
| Zenith Processing | TC-17589 | 2021-07-05 | Product Management |
| SIG-77-MDI-MBKO | BC-17597 | 2021-12-05 | Supply Chain |
| atlantic distribution Holdings | TC-17609 | 2022-12-25 | Operations |
| SIG-47-UOO-GQED | TC-17611 | 2022-03-03 | Product Management |
| Wheat Gluten 25% Food Grade | TC-17637 | 2022-11-08 | Finance |
| Meridian Sourcing | TC-17640 | 2022-01-23 | Supply Chain |
| Lactic Acid 99.5% | BC-17645 | 2024-02-08 | Product Management |
| LA-AC-98-GR-A-841 | TC-17668 | 2021-10-16 | Operations |
| vanguard industries BV | BC-17688 | 2022-02-02 | IT Infrastructure |
| SIG-56-BPD-M0A6 | TC-17693 | 2024-10-26 | IT Infrastructure |
| Vat Standardqualität GB 20% | TC-17707 | 2022-09-04 | Finance |
| Pinnacle Sourcing | TC-17711 | 2022-05-13 | IT Infrastructure |
| Lactic Acid Qualitätsstufe II | BC-17715 | 2024-11-06 | Compliance |
| Isoglucose Premium | TC-17735 | 2021-12-15 | Operations |
| SIG-68-PIZ-R6Q5 | TC-17740 | 2021-08-25 | Finance |
| casein premium | TC-17751 | 2022-05-25 | Compliance |
| SIG-89-TVE-WANI | BC-17759 | 2023-07-13 | Data Governance |
| central logistics | BC-17762 | 2022-05-16 | Supply Chain |
| CA-TE-336 | TC-17777 | 2023-12-21 | IT Infrastructure |
| Nordic Manufacturing Group | TC-17781 | 2024-07-13 | Finance |
| Casein Grade A | BC-17791 | 2024-07-24 | Supply Chain |
| ascorbic acid 50% standard | TC-17797 | 2024-10-11 | Finance |
| stratos logistics | IC-17803 | 2021-03-06 | IT Infrastructure |
| Horizon Logistics International | TC-17813 | 2021-06-19 | Operations |
| vertex supply | TC-17816 | 2024-09-12 | Supply Chain |
| SIG-19-QLH-ILRZ | IC-17831 | 2023-01-20 | Finance |
| Global Distribution LLC | BC-17833 | 2022-12-08 | Data Governance |
| SIG-47-MIU-LIH6 | TC-17854 | 2024-07-18 | Operations |
| Continental Sourcing | TC-17868 | 2024-05-26 | Product Management |
| Lactic Acid 98% | BC-17880 | 2023-01-24 | Finance |
| Soja Isolate 98% | IC-17882 | 2021-11-27 | Supply Chain |
| Soja Isolate Qualitätsstufe I | IC-17915 | 2024-03-01 | Supply Chain |
| Dextrin | TC-17927 | 2022-05-19 | Operations |
| meridian ingredients GmbH | IC-17930 | 2023-07-03 | IT Infrastructure |
| Coconut Oil Lebensmittelrein | BC-17937 | 2023-05-24 | IT Infrastructure |
| cyclodextrin | TC-17954 | 2022-01-26 | Compliance |
| SIG-35-VQC-JQ0H AG | BC-17968 | 2023-09-22 | Compliance |
| horizon ingredients LLC | IC-17972 | 2024-12-02 | Operations |
| Ascorbic Acid 70% | IC-17981 | 2023-10-21 | Compliance |
| Natriumchlorid 25% Lebensmittelrein | BC-17997 | 2024-10-18 | IT Infrastructure |
| Soy Isolate Technical | TC-18025 | 2021-12-18 | IT Infrastructure |
| Prism Partners | IC-18031 | 2022-07-11 | Operations |
| Potassium Sorbate 25% Pharma Grade | TC-18044 | 2022-07-02 | Product Management |
| Lactic Acid 99.5% Qualitätsstufe II | TC-18072 | 2024-03-07 | Operations |
| Rapsöl 25% Lebensmittelrein | BC-18074 | 2021-09-27 | Product Management |
| Soy Isolate 25% | TC-18087 | 2021-11-05 | Compliance |
| CY-98-PH-GR-614 | IC-18100 | 2024-09-19 | Supply Chain |
| Calcium Carbonate Premiumqualität | TC-18102 | 2024-08-19 | Supply Chain |
| Maltodextrin DE15 | BC-18115 | 2022-11-15 | Product Management |
| Quantum Supply Co. | BC-18121 | 2023-09-03 | IT Infrastructure |
| SIG-50-NOW-F1TK GmbH | BC-18123 | 2022-12-09 | Supply Chain |
| EX-G-25-188 | BC-18135 | 2021-11-10 | Compliance |
| SIG-12-QLD-RUJ3 Inc. | TC-18147 | 2021-09-20 | Data Governance |
| Apex Commodities Holdings | IC-18159 | 2021-09-07 | Product Management |
| AS-AC-ST-243 | IC-18184 | 2022-08-01 | Compliance |
| Prism Industrien LLC | BC-18193 | 2021-09-08 | Data Governance |
| SIG-60-IRZ-OTKZ | BC-18196 | 2021-04-18 | Data Governance |
| Baltic Supply Co. | IC-18205 | 2022-10-16 | IT Infrastructure |
| Dextrose | BC-18209 | 2022-03-10 | Compliance |
| BA-EN-363 KG | IC-18216 | 2023-03-09 | Product Management |
| Wheat Gluten | TC-18235 | 2021-08-16 | Operations |
| pea protein standard | TC-18238 | 2021-02-03 | Operations |
| Traubenzucker 50% Qualitätsstufe II | BC-18242 | 2021-01-04 | Compliance |
| SIG-72-JEH-P5K7 | IC-18255 | 2024-01-10 | Operations |
| Isoglucose | IC-18258 | 2021-01-10 | IT Infrastructure |
| Premier Handel AG | TC-18270 | 2023-09-15 | Product Management |
| AT-MA-324 International | IC-18278 | 2024-06-26 | Product Management |
| soy isolate 70% | TC-18280 | 2023-03-25 | IT Infrastructure |
| customs duty gb 7% | IC-18296 | 2022-06-08 | Supply Chain |
| elite materials | BC-18301 | 2021-06-06 | Supply Chain |
| EL-LO-188 | IC-18305 | 2023-02-14 | Data Governance |
| Soy Isolate 25% | BC-18308 | 2021-04-15 | Supply Chain |
| Stellar Vertrieb | TC-18313 | 2024-04-15 | Data Governance |
| GL-SU-CO-128 | TC-18343 | 2024-09-15 | Finance |
| resistant starch | TC-18356 | 2021-01-09 | Data Governance |
| Premier Partners SARL | IC-18373 | 2022-04-16 | IT Infrastructure |
| Coconut Oil 70% Grade A | TC-18379 | 2023-01-28 | Supply Chain |
| vat reduced cn 21% | TC-18384 | 2022-08-02 | Operations |
| SIG-20-IMA-GJKF | IC-18385 | 2024-01-20 | Supply Chain |
| Soy Isolate 50% Grade B | IC-18390 | 2022-11-04 | Data Governance |
| CI-AC-PH-GR-209 | IC-18398 | 2021-01-27 | Supply Chain |
| FR-99.5-PH-GR-378 | BC-18406 | 2021-11-18 | Finance |
| SIG-65-BMI-KAWJ Holdings | TC-18408 | 2024-12-26 | Product Management |
| Wheat Gluten | IC-18434 | 2021-01-24 | Data Governance |
| SO-CH-99.5-GR-A-634 | IC-18437 | 2021-05-01 | IT Infrastructure |
| Sodium Benzoate | BC-18449 | 2022-02-13 | Data Governance |
| Zitronensäure Technische Qualität | TC-18458 | 2023-12-06 | IT Infrastructure |
| Nexus Partners | TC-18487 | 2023-01-17 | Finance |
| CU-DU-U-19-893 | IC-18501 | 2022-04-20 | Compliance |
| Customs Duty FR 19% | TC-18511 | 2023-03-09 | Compliance |
| rapeseed oil 50% standard | TC-18517 | 2024-11-01 | Supply Chain |
| pea protein | IC-18519 | 2021-04-06 | Supply Chain |
| Natriumbenzoat | IC-18525 | 2023-10-26 | Compliance |
| Prism Materials Ltd. | IC-18532 | 2024-03-24 | Data Governance |
| resistant starch food grade | BC-18547 | 2023-10-06 | Compliance |
| WH-GL-ST-378 | TC-18554 | 2021-06-02 | Compliance |
| SIG-46-DQX-JN7N | IC-18561 | 2022-09-03 | Operations |
| meridian chemicals Holdings | IC-18575 | 2021-09-05 | Product Management |
| sodium benzoate premium | TC-18610 | 2022-10-02 | Product Management |
| dextrose tech grade | BC-18622 | 2024-10-18 | Supply Chain |
| AT-IN-899 Group | BC-18630 | 2023-06-04 | Supply Chain |
| SIG-17-LVE-03G9 | IC-18636 | 2021-06-13 | Finance |
| AS-AC-573 | BC-18663 | 2022-11-05 | Supply Chain |
| SO-IS-99.5-141 | TC-18667 | 2022-11-19 | IT Infrastructure |
| glucose syrup 25% | BC-18676 | 2022-04-16 | Product Management |
| Coconut Oil 70% | BC-18706 | 2024-02-09 | Supply Chain |
| glucose syrup | BC-18734 | 2021-08-12 | Finance |
| SIG-44-MHK-SRCB | IC-18738 | 2024-04-22 | Operations |
| Resistente Stärke Qualitätsstufe II | BC-18744 | 2021-08-22 | Product Management |
| SIG-90-SJW-O06V | BC-18756 | 2022-12-09 | Product Management |
| SIG-59-LNO-OJGF | IC-18769 | 2021-04-26 | IT Infrastructure |
| SO-CH-354 | BC-18790 | 2023-05-24 | Product Management |
| SIG-23-CJO-TSA9 | BC-18794 | 2022-10-14 | Product Management |
| wheat gluten food grade | IC-18802 | 2023-08-25 | Product Management |
| SIG-97-EIS-DKQB Holdings | BC-18804 | 2023-05-24 | Data Governance |
| elite solutions Holdings | BC-18813 | 2023-11-08 | IT Infrastructure |
| SIG-60-PEY-H3GM | TC-18814 | 2024-06-11 | Operations |
| RA-OI-GR-B-834 | BC-18821 | 2022-11-20 | Data Governance |
| vertex supply | IC-18823 | 2021-07-19 | Supply Chain |
| Citric Acid 70% Food Grade | BC-18841 | 2024-07-08 | Finance |
| premier partners | BC-18854 | 2024-05-05 | Compliance |
| calcium carbonate | IC-18897 | 2023-07-14 | Compliance |
| stratos supply | TC-18899 | 2023-05-15 | Operations |
| RE-ST-GR-A-614 | TC-18909 | 2024-09-11 | IT Infrastructure |
| SIG-61-CIV-LFWA | TC-18926 | 2024-12-28 | Supply Chain |
| Coconut Oil 98% Technische Qualität | IC-18942 | 2021-02-16 | Supply Chain |
| LA-AC-FO-GR-469 | TC-18956 | 2024-07-08 | Operations |
| pinnacle supply | BC-18961 | 2021-03-25 | IT Infrastructure |
| SIG-50-QXM-GFI4 | TC-18993 | 2024-02-23 | Product Management |
| Vat Reduced BR 10% | BC-18996 | 2023-10-24 | Data Governance |
| Atlas Logistics | BC-19012 | 2022-03-01 | Supply Chain |
| SIG-15-PFO-2W85 | BC-19021 | 2022-02-20 | Product Management |
| Customs Duty GB 7% | IC-19023 | 2021-03-17 | Supply Chain |
| Apex Chemicals Corp. | BC-19058 | 2024-02-18 | Compliance |
| PI-DI-618 NV | IC-19096 | 2023-12-02 | Finance |
| Customs Duty FR 5% | TC-19104 | 2024-10-18 | Supply Chain |
| AS-AC-GR-B-395 | IC-19111 | 2021-06-17 | Data Governance |
| LA-AC-TE-761 | TC-19122 | 2022-07-27 | Product Management |
| Stratos Trading Holdings | TC-19167 | 2024-09-03 | Finance |
| Pinnacle Logistik BV | TC-19174 | 2022-01-11 | Product Management |
| fructose pharma grade | TC-19182 | 2021-04-07 | Product Management |
| Citric Acid 25% Grade A | BC-19189 | 2022-04-07 | Product Management |
| Global Distribution LLC | TC-19190 | 2021-04-08 | IT Infrastructure |
| EX-F-21-522 | BC-19212 | 2024-03-07 | Finance |
| Weizenklebereiweiß 50% Technische Qualität | IC-19218 | 2024-04-01 | IT Infrastructure |
| casein | IC-17116 | 2024-10-12 | Data Governance |
| potassium sorbate 50% tech grade | BC-19280 | 2022-08-14 | Finance |
| Cyclodextrin 70% Food Grade | IC-19290 | 2023-04-28 | Finance |
| SIG-46-YOE-MYAX SA | BC-19301 | 2021-07-02 | IT Infrastructure |
| Sodium Chloride 98% Standard | TC-19312 | 2021-07-08 | Finance |
| CA-CA-648 | TC-19315 | 2023-05-20 | IT Infrastructure |
| lactic acid food grade | TC-19325 | 2024-12-27 | Product Management |
| SIG-93-TEG-8CN0 SARL | IC-19327 | 2022-07-11 | Supply Chain |
| SIG-64-TCV-R5SR | IC-19340 | 2022-07-26 | Finance |
| Lactic Acid Grade B | BC-19346 | 2022-08-22 | Product Management |
| Glucose Syrup 70% | IC-19351 | 2022-01-10 | Data Governance |
| palm oil 70% tech grade | BC-19365 | 2022-04-13 | Product Management |
| Palmfett Standardqualität | TC-19366 | 2023-06-02 | Supply Chain |
| SIG-70-ROA-COR7 | IC-19373 | 2021-11-02 | Product Management |
| Isoglucose | IC-19375 | 2024-04-11 | Supply Chain |
| Coconut Oil 25% | IC-19388 | 2021-04-24 | Supply Chain |
| quantum trading SARL | BC-19391 | 2022-05-17 | Finance |
| Catalyst Rohstoffe SA | BC-19392 | 2021-10-21 | IT Infrastructure |
| QU-MA-886 | BC-19395 | 2021-02-21 | Product Management |
| SIG-52-EML-H8JV | BC-19412 | 2024-02-01 | Operations |
| atlas enterprise | TC-19417 | 2021-04-17 | Product Management |
| ascorbic acid food grade | TC-19450 | 2021-04-13 | Finance |
| glucose syrup 99.5% food grade | IC-19453 | 2024-05-01 | Product Management |
| Sunflower Oil Pharma Grade | IC-19455 | 2022-01-05 | Compliance |
| SIG-88-RUZ-O3Q0 | IC-19501 | 2021-08-07 | Supply Chain |
| Pinnacle Ingredients KG | TC-19512 | 2022-02-03 | Supply Chain |
| Isoglucose Grade B | BC-19514 | 2024-01-09 | Operations |
| Resistant Starch 50% Standard | IC-19538 | 2022-09-17 | Compliance |
| SIG-47-TWK-RYLY | TC-19565 | 2023-03-06 | Supply Chain |
| Elite Logistics | IC-19568 | 2021-07-05 | Finance |
| CI-AC-GR-A-280 | IC-19580 | 2021-01-15 | Finance |
| Atlas Logistics International | BC-19586 | 2021-07-10 | IT Infrastructure |
| Central Werkstoffe | TC-19588 | 2024-05-20 | IT Infrastructure |
| RE-ST-575 | TC-19591 | 2024-09-16 | Compliance |
| vertex logistics KG | IC-19612 | 2023-10-22 | Data Governance |
| glucose syrup 98% food grade | BC-19616 | 2024-01-13 | Finance |
| casein standard | IC-19632 | 2021-06-13 | Product Management |
| IS-230 | TC-19636 | 2023-11-13 | Finance |
| Pinnacle Commodities BV | TC-19693 | 2021-02-09 | Finance |
| soy isolate 99.5% | BC-19725 | 2023-03-24 | IT Infrastructure |
| SIG-16-CAW-LD7M | IC-19728 | 2023-10-09 | Data Governance |
| Atlas Industrien International | BC-19733 | 2024-06-11 | Compliance |
| Sodium Benzoate 99.5% Standard | IC-19736 | 2021-09-21 | Supply Chain |
| Rapsöl | TC-19744 | 2022-04-26 | Finance |
| Ascorbic Acid | BC-19746 | 2021-06-22 | Operations |
| Potassium Sorbate 50% Grade B | IC-19747 | 2023-09-09 | IT Infrastructure |
| vat standard nl 20% | IC-19751 | 2022-01-27 | Operations |
| pea protein 70% tech grade | BC-19754 | 2021-04-19 | Operations |
| SIG-63-TFP-OMUW | IC-19758 | 2024-01-16 | Product Management |
| Pacific Werkstoffe | BC-19768 | 2024-03-11 | Data Governance |
| CO-SU-411 | BC-19771 | 2024-03-02 | Compliance |
| cyclodextrin 70% food grade | BC-19779 | 2022-04-24 | Compliance |
| VE-CH-445 Group | TC-19791 | 2022-09-07 | Supply Chain |
| SIG-39-JXL-BQ85 SARL | BC-19800 | 2021-02-27 | Product Management |
| ascorbic acid | TC-19809 | 2023-01-11 | IT Infrastructure |
| horizon partners Ltd. | IC-19848 | 2022-05-21 | Operations |
| SIG-86-LPN-HCNV | TC-19863 | 2022-01-02 | Finance |
| global materials | TC-19875 | 2021-12-01 | Finance |
| prism partners Holdings | TC-19892 | 2023-09-26 | IT Infrastructure |
| IS-25-FO-GR-789 | IC-19894 | 2022-09-02 | Compliance |
| Sonnenblumenöl Standardqualität | IC-19902 | 2022-07-27 | Product Management |
| PR-EN-361 International | IC-19905 | 2022-10-13 | Supply Chain |
| Customs Duty IN 5% | BC-19907 | 2024-06-15 | IT Infrastructure |
| Meridian Werkstoffe | BC-19915 | 2024-05-01 | Data Governance |
| GL-SY-70-549 | IC-19926 | 2024-03-06 | Compliance |
| zenith trading GmbH | BC-19936 | 2021-07-15 | Data Governance |
| dextrin pharma grade | TC-19940 | 2021-05-15 | Supply Chain |
| SIG-64-LXA-3LJO | BC-19963 | 2023-07-27 | IT Infrastructure |
| SIG-83-CDB-3QOI | BC-19979 | 2022-04-09 | Supply Chain |
| SIG-92-NWY-1FV5 | BC-19999 | 2021-03-07 | Supply Chain |
| Natriumbenzoat | TC-20002 | 2022-10-05 | Data Governance |
| Isoglucose 70% | TC-20005 | 2021-02-25 | Product Management |
| Customs Duty CN 0% | IC-20008 | 2021-01-05 | Supply Chain |
| SIG-73-LLJ-LNGI | BC-20017 | 2024-01-19 | Operations |
| nexus logistics | TC-20019 | 2023-03-19 | Compliance |
| potassium sorbate | TC-20022 | 2024-06-23 | Compliance |
| SIG-34-IKF-VQJA | TC-20034 | 2021-05-05 | Data Governance |
| SO-IS-99.5-141 | BC-20045 | 2024-02-04 | Finance |
| core partners NV | TC-20056 | 2022-11-23 | Finance |
| Sorbic Acid Food Grade | BC-20063 | 2023-07-01 | Operations |
| ascorbic acid standard | TC-20073 | 2022-04-21 | Product Management |
| Pea Protein 50% | TC-20081 | 2022-05-20 | Product Management |
| Resistente Stärke | TC-20086 | 2024-01-11 | IT Infrastructure |
| DE-70-PH-GR-978 | TC-20091 | 2022-12-04 | IT Infrastructure |
| SIG-53-DUL-C550 Group | IC-20101 | 2024-01-12 | IT Infrastructure |
| Maltodextrin DE25 | IC-20111 | 2022-06-05 | Finance |
| pacific industries Ltd. | BC-20117 | 2023-08-03 | Compliance |
| SO-CH-TE-223 | BC-20120 | 2021-10-16 | Supply Chain |
| Soja Isolate 25% Technische Qualität | IC-20134 | 2021-03-21 | Finance |
| SIG-61-QOJ-MGS9 BV | IC-20147 | 2023-08-20 | Finance |
| sodium benzoate 50% | IC-20159 | 2023-01-04 | Finance |
| Wheat Gluten 99.5% | BC-20171 | 2023-08-25 | Compliance |
| nexus ingredients SA | TC-20203 | 2024-03-12 | Operations |
| resistant starch 25% food grade | IC-20232 | 2024-03-23 | Compliance |
| Kasein | TC-20262 | 2024-12-12 | IT Infrastructure |
| Resistente Stärke 98% | TC-20298 | 2021-06-05 | IT Infrastructure |
| Continental Commodities GmbH | BC-20303 | 2022-06-09 | Data Governance |
| Ascorbic Acid Premium | TC-20306 | 2024-06-19 | Compliance |
| SIG-47-YTF-UPMT | IC-20343 | 2023-04-17 | Finance |
| Sodium Benzoate Pharma Grade | IC-20396 | 2022-04-26 | Finance |
| Quantum Handel Group | BC-20405 | 2024-03-08 | Finance |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| Vertex Rohstoffe | IC-9625 | PROVISIONAL | Historical - verify before use |
| Vat Standardqualität NL 25% | IC-9435 | DEPRECATED | Historical - verify before use |
| SIG-61-MHS-BQG3 | IC-8036 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil 98% | IC-6775 | REVIEW REQUIRED | Historical - verify before use |
| Horizon Ingredients International | IC-5773 | SUPERSEDED | Historical - verify before use |
| soy isolate | IC-8570 | DEPRECATED | Historical - verify before use |
| withholding gb 5% | IC-9023 | PROVISIONAL | Historical - verify before use |
| elite partners | IC-7183 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil 70% | IC-7674 | REVIEW REQUIRED | Historical - verify before use |
| Elite Solutions | IC-6139 | SUPERSEDED | Historical - verify before use |
| SIG-10-KDB-LGYT | IC-8413 | DEPRECATED | Historical - verify before use |
| ascorbic acid premium | IC-7157 | REVIEW REQUIRED | Historical - verify before use |
| Vat Standardqualität FR 0% | IC-5353 | REVIEW REQUIRED | Historical - verify before use |
| sodium benzoate 99.5% premium | IC-6890 | PROVISIONAL | Historical - verify before use |
| SIG-77-AEN-CA8D | IC-9641 | REVIEW REQUIRED | Historical - verify before use |
| Vat Standardqualität US 10% | IC-8956 | PROVISIONAL | Historical - verify before use |
| SIG-10-TIC-7Q1D | IC-9178 | PROVISIONAL | Historical - verify before use |
| Ascorbic Acid 70% | IC-6545 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid 98% Pharmazeutisch rein | IC-7555 | SUPERSEDED | Historical - verify before use |
| GL-SY-PR-440 | IC-5973 | DEPRECATED | Historical - verify before use |
| apex sourcing | IC-7220 | DEPRECATED | Historical - verify before use |
| SIG-88-AGF-FF5L | IC-5419 | REVIEW REQUIRED | Historical - verify before use |
| SIG-80-ZKZ-ANXJ | IC-8695 | SUPERSEDED | Historical - verify before use |
| Resistente Stärke | IC-6317 | SUPERSEDED | Historical - verify before use |
| rapeseed oil 50% pharma grade | IC-9473 | REVIEW REQUIRED | Historical - verify before use |
| atlantic supply | IC-7846 | PROVISIONAL | Historical - verify before use |
| Baltic Industries BV | IC-6856 | PROVISIONAL | Historical - verify before use |
| SO-CH-98-657 | IC-9448 | PROVISIONAL | Historical - verify before use |
| potassium sorbate food grade | IC-5222 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid Food Grade | IC-6516 | REVIEW REQUIRED | Historical - verify before use |
| Cyclodextrin | IC-8260 | SUPERSEDED | Historical - verify before use |
| ME-LO-670 | IC-9605 | PROVISIONAL | Historical - verify before use |
| sorbic acid 70% | IC-5394 | SUPERSEDED | Historical - verify before use |
| SIG-57-HAE-WNSM | IC-5550 | SUPERSEDED | Historical - verify before use |
| Kaliumsorbat Qualitätsstufe II | IC-6368 | DEPRECATED | Historical - verify before use |
| SIG-91-FOC-36I6 | IC-5815 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid 99.5% Grade B | IC-9326 | SUPERSEDED | Historical - verify before use |
| GL-SY-98-FO-GR-198 | IC-5421 | REVIEW REQUIRED | Historical - verify before use |
| Pacific Materials | IC-8328 | SUPERSEDED | Historical - verify before use |
| SIG-61-FGJ-AO1L NV | IC-6012 | DEPRECATED | Historical - verify before use |
| lactic acid standard | IC-8401 | REVIEW REQUIRED | Historical - verify before use |
| Excise DE 10% | IC-9671 | PROVISIONAL | Historical - verify before use |
| Vat Standard GB 19% | IC-9476 | REVIEW REQUIRED | Historical - verify before use |
| Citric Acid 99.5% | IC-7783 | DEPRECATED | Historical - verify before use |
| Atlantic Rohstoffe GmbH | IC-5247 | SUPERSEDED | Historical - verify before use |
| Dextrin 25% Premiumqualität | IC-8298 | PROVISIONAL | Historical - verify before use |
| SIG-69-BWM-8WBG | IC-9846 | DEPRECATED | Historical - verify before use |
| ascorbic acid pharma grade | IC-6073 | SUPERSEDED | Historical - verify before use |
| Meridian Versorgung | IC-6946 | SUPERSEDED | Historical - verify before use |
| AS-AC-130 | IC-6624 | REVIEW REQUIRED | Historical - verify before use |
| SIG-27-MIG-RYBN | IC-9781 | DEPRECATED | Historical - verify before use |
| Calcium Carbonate 50% Pharma Grade | IC-7575 | DEPRECATED | Historical - verify before use |
| apex logistics | IC-8341 | REVIEW REQUIRED | Historical - verify before use |
| vat standard gb 21% | IC-7454 | PROVISIONAL | Historical - verify before use |
| Coconut Oil 25% Technical | IC-7983 | REVIEW REQUIRED | Historical - verify before use |
| global enterprise NV | IC-6862 | SUPERSEDED | Historical - verify before use |
| SIG-37-MXA-3C7Q | IC-9714 | REVIEW REQUIRED | Historical - verify before use |
| SIG-97-OGU-PBXC | IC-8160 | PROVISIONAL | Historical - verify before use |
| SIG-99-GVJ-VPM6 | IC-7382 | SUPERSEDED | Historical - verify before use |
| SO-IS-99.5-PR-187 | IC-8571 | DEPRECATED | Historical - verify before use |
| ZE-PA-718 LLC | IC-7449 | PROVISIONAL | Historical - verify before use |
| SIG-78-AVK-U9PX | IC-9070 | REVIEW REQUIRED | Historical - verify before use |
| citric acid | IC-9935 | DEPRECATED | Historical - verify before use |
| SIG-69-OFZ-JW34 | IC-8986 | DEPRECATED | Historical - verify before use |
| Natriumbenzoat | IC-5388 | REVIEW REQUIRED | Historical - verify before use |
| SIG-79-OZQ-4I2N | IC-6755 | DEPRECATED | Historical - verify before use |
| excise in 25% | IC-9450 | SUPERSEDED | Historical - verify before use |
| SIG-75-GGJ-DK9O | IC-6731 | SUPERSEDED | Historical - verify before use |
| SIG-16-MNF-F4AF | IC-7735 | SUPERSEDED | Historical - verify before use |
| PI-LO-946 | IC-9915 | PROVISIONAL | Historical - verify before use |
| sorbic acid 50% food grade | IC-6920 | REVIEW REQUIRED | Historical - verify before use |
| Nexus Werkstoffe | IC-5942 | DEPRECATED | Historical - verify before use |
| Wheat Gluten | IC-5288 | PROVISIONAL | Historical - verify before use |
| Wheat Gluten Grade B | IC-7693 | REVIEW REQUIRED | Historical - verify before use |
| SIG-45-QQC-Z4N0 | IC-6943 | REVIEW REQUIRED | Historical - verify before use |
| RA-OI-FO-GR-269 | IC-8224 | DEPRECATED | Historical - verify before use |
| SIG-88-KUG-5ITD | IC-9486 | DEPRECATED | Historical - verify before use |
| DE-635 | IC-6808 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid 99.5% Premiumqualität | IC-8693 | REVIEW REQUIRED | Historical - verify before use |
| PA-MA-166 SARL | IC-5030 | PROVISIONAL | Historical - verify before use |
| SIG-87-LPT-3ADB | IC-8486 | SUPERSEDED | Historical - verify before use |
| dextrose premium | IC-5145 | REVIEW REQUIRED | Historical - verify before use |
| PR-CH-334 GmbH | IC-6666 | REVIEW REQUIRED | Historical - verify before use |
| Sodium Chloride | IC-7533 | DEPRECATED | Historical - verify before use |
| Maltodextrin DE18 Pharma Grade | IC-6661 | SUPERSEDED | Historical - verify before use |
| Coconut Oil 70% Grade A | IC-8537 | SUPERSEDED | Historical - verify before use |
| stellar logistics | IC-5108 | SUPERSEDED | Historical - verify before use |
| Calcium Carbonate Qualitätsstufe II | IC-8199 | SUPERSEDED | Historical - verify before use |
| Catalyst Commodities SAS | IC-8619 | DEPRECATED | Historical - verify before use |
| GL-SY-98-939 | IC-7756 | PROVISIONAL | Historical - verify before use |
| sodium benzoate 98% | IC-7020 | REVIEW REQUIRED | Historical - verify before use |
| prism ingredients | IC-5059 | DEPRECATED | Historical - verify before use |
| FR-50-ST-938 | IC-5886 | SUPERSEDED | Historical - verify before use |
| casein premium | IC-8121 | PROVISIONAL | Historical - verify before use |
| Palm Oil 70% Premium | IC-7469 | PROVISIONAL | Historical - verify before use |
| Vat Reduced BR 25% | IC-8746 | SUPERSEDED | Historical - verify before use |
| sorbic acid 98% | IC-7931 | DEPRECATED | Historical - verify before use |
| Casein Standard | IC-8035 | DEPRECATED | Historical - verify before use |
| Prism Industrien Holdings | IC-9405 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid Premiumqualität | IC-6302 | SUPERSEDED | Historical - verify before use |
| Rapsöl 70% Qualitätsstufe II | IC-5814 | DEPRECATED | Historical - verify before use |
| SIG-10-PGH-BTUF | IC-7870 | SUPERSEDED | Historical - verify before use |
| Baltic Ingredients | IC-9895 | DEPRECATED | Historical - verify before use |
| Sorbic Acid Food Grade | IC-5039 | REVIEW REQUIRED | Historical - verify before use |
| Continental Enterprise KG | IC-5241 | SUPERSEDED | Historical - verify before use |
| Dextrin | IC-7116 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid 99.5% Premiumqualität | IC-5330 | SUPERSEDED | Historical - verify before use |
| SIG-20-OAV-1IKJ | IC-7266 | DEPRECATED | Historical - verify before use |
| Central Logistik | IC-7400 | REVIEW REQUIRED | Historical - verify before use |
| SO-BE-PR-691 | IC-9306 | DEPRECATED | Historical - verify before use |
| Excise NL 20% | IC-9847 | SUPERSEDED | Historical - verify before use |
| premier logistics | IC-9851 | DEPRECATED | Historical - verify before use |
| Isoglucose 70% Lebensmittelrein | IC-7045 | PROVISIONAL | Historical - verify before use |
| Withholding US 25% | IC-6686 | SUPERSEDED | Historical - verify before use |
| PA-MA-412 GmbH | IC-7385 | SUPERSEDED | Historical - verify before use |
| Vat Standard CN 0% | IC-7739 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat Pharmazeutisch rein | IC-7042 | SUPERSEDED | Historical - verify before use |
| Nordic Manufacturing NV | IC-5713 | DEPRECATED | Historical - verify before use |
| casein 98% standard | IC-9847 | SUPERSEDED | Historical - verify before use |
| RA-OI-98-117 | IC-7462 | SUPERSEDED | Historical - verify before use |
| SIG-58-NYA-2O4M | IC-8968 | SUPERSEDED | Historical - verify before use |
| SO-BE-964 | IC-6298 | REVIEW REQUIRED | Historical - verify before use |
| SU-OI-70-FO-GR-432 | IC-6178 | SUPERSEDED | Historical - verify before use |
| SIG-84-MGK-H2ME | IC-8927 | PROVISIONAL | Historical - verify before use |
| SIG-11-AEJ-CHNJ | IC-6568 | PROVISIONAL | Historical - verify before use |
| dextrose tech grade | IC-8644 | REVIEW REQUIRED | Historical - verify before use |
| Casein 25% Grade B | IC-6625 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid 50% Technische Qualität | IC-9006 | PROVISIONAL | Historical - verify before use |
| Rapsöl Qualitätsstufe I | IC-6377 | PROVISIONAL | Historical - verify before use |
| Pea Protein 70% Premiumqualität | IC-9012 | PROVISIONAL | Historical - verify before use |
| customs duty fr 19% | IC-6378 | REVIEW REQUIRED | Historical - verify before use |
| citric acid | IC-9502 | REVIEW REQUIRED | Historical - verify before use |
| AP-MA-498 | IC-8636 | DEPRECATED | Historical - verify before use |
| SIG-14-GCI-G4Q9 | IC-7326 | REVIEW REQUIRED | Historical - verify before use |
| sodium benzoate 98% pharma grade | IC-5083 | REVIEW REQUIRED | Historical - verify before use |
| Sunflower Oil Grade A | IC-7582 | PROVISIONAL | Historical - verify before use |
| Vanguard Chemicals SAS | IC-7350 | DEPRECATED | Historical - verify before use |
| CE-MA-720 | IC-8614 | SUPERSEDED | Historical - verify before use |
| Palmfett Lebensmittelrein | IC-7792 | REVIEW REQUIRED | Historical - verify before use |
| Cyclodextrin Food Grade | IC-8043 | SUPERSEDED | Historical - verify before use |
| SIG-56-FFG-XS2P | IC-6230 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid | IC-7547 | PROVISIONAL | Historical - verify before use |
| Prism Supply Co. | IC-7765 | DEPRECATED | Historical - verify before use |
| prime solutions | IC-8624 | REVIEW REQUIRED | Historical - verify before use |
| AT-CO-808 GmbH | IC-6304 | PROVISIONAL | Historical - verify before use |
| customs duty us 15% | IC-5995 | DEPRECATED | Historical - verify before use |
| SIG-16-MLJ-HWA7 | IC-9343 | DEPRECATED | Historical - verify before use |
| Stratos Sourcing | IC-6040 | DEPRECATED | Historical - verify before use |
| coconut oil | IC-5430 | DEPRECATED | Historical - verify before use |
| Withholding NL 21% | IC-7773 | DEPRECATED | Historical - verify before use |
| SIG-12-ANK-TJ9A | IC-8756 | DEPRECATED | Historical - verify before use |
| central logistics International | IC-9691 | SUPERSEDED | Historical - verify before use |
| VA-DI-229 | IC-8801 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid 25% Lebensmittelrein | IC-6115 | SUPERSEDED | Historical - verify before use |
| Natriumbenzoat Technische Qualität | IC-7608 | DEPRECATED | Historical - verify before use |
| pea protein | IC-5300 | REVIEW REQUIRED | Historical - verify before use |
| citric acid | IC-7722 | REVIEW REQUIRED | Historical - verify before use |
| DE-98-512 | IC-9243 | REVIEW REQUIRED | Historical - verify before use |
| Dextrin 98% | IC-5288 | REVIEW REQUIRED | Historical - verify before use |
| SIG-78-TUT-T3NS | IC-6442 | REVIEW REQUIRED | Historical - verify before use |
| Zitronensäure Qualitätsstufe II | IC-7590 | PROVISIONAL | Historical - verify before use |
| maltodextrin de30 | IC-5729 | PROVISIONAL | Historical - verify before use |
| Atlantic Rohstoffe International | IC-5862 | REVIEW REQUIRED | Historical - verify before use |
| SIG-80-QLX-7SNL SAS | IC-6717 | REVIEW REQUIRED | Historical - verify before use |
| rapeseed oil | IC-7118 | PROVISIONAL | Historical - verify before use |
| dextrose | IC-7137 | SUPERSEDED | Historical - verify before use |
| Coconut Oil | IC-5903 | PROVISIONAL | Historical - verify before use |
| vat standard br 7% | IC-5617 | REVIEW REQUIRED | Historical - verify before use |
| vat standard fr 0% | IC-7321 | PROVISIONAL | Historical - verify before use |
| resistant starch 70% standard | IC-8510 | SUPERSEDED | Historical - verify before use |
| Excise NL 19% | IC-9712 | SUPERSEDED | Historical - verify before use |
| CU-DU-B-15-686 | IC-8096 | REVIEW REQUIRED | Historical - verify before use |
| Customs Duty BR 21% | IC-9592 | SUPERSEDED | Historical - verify before use |
| CA-GR-A-380 | IC-9503 | DEPRECATED | Historical - verify before use |
| SO-AC-99.5-338 | IC-9066 | PROVISIONAL | Historical - verify before use |
| SIG-29-XAN-WDDA | IC-7877 | SUPERSEDED | Historical - verify before use |
| LA-AC-TE-651 | IC-6195 | PROVISIONAL | Historical - verify before use |
| Sorbinsäure 50% | IC-9651 | SUPERSEDED | Historical - verify before use |
| SU-OI-98-PR-692 | IC-6176 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil Pharma Grade | IC-6191 | PROVISIONAL | Historical - verify before use |
| Withholding GB 21% | IC-5122 | REVIEW REQUIRED | Historical - verify before use |
| SIG-88-RKE-8R7A | IC-9451 | REVIEW REQUIRED | Historical - verify before use |
| Baltic Solutions | IC-6822 | REVIEW REQUIRED | Historical - verify before use |
| VE-CH-841 Group | IC-5460 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat 99.5% Technische Qualität | IC-8335 | PROVISIONAL | Historical - verify before use |
| CI-AC-70-FO-GR-198 | IC-9068 | DEPRECATED | Historical - verify before use |
| excise br 25% | IC-9963 | PROVISIONAL | Historical - verify before use |
| RA-OI-25-FO-GR-966 | IC-7477 | DEPRECATED | Historical - verify before use |
| pea protein 25% pharma grade | IC-8390 | REVIEW REQUIRED | Historical - verify before use |
| SIG-86-VCP-SVOL | IC-8369 | SUPERSEDED | Historical - verify before use |
| excise de 21% | IC-9915 | DEPRECATED | Historical - verify before use |
| coconut oil 98% premium | IC-6288 | PROVISIONAL | Historical - verify before use |
| RA-OI-FO-GR-269 | IC-8177 | SUPERSEDED | Historical - verify before use |
| SIG-71-CWF-DGP5 | IC-7419 | SUPERSEDED | Historical - verify before use |
| atlas supply | IC-8716 | REVIEW REQUIRED | Historical - verify before use |
| NO-CO-357 International | IC-7480 | DEPRECATED | Historical - verify before use |
| Maltodextrin DE25 | IC-5114 | REVIEW REQUIRED | Historical - verify before use |
| SO-CH-PR-862 | IC-9595 | DEPRECATED | Historical - verify before use |
| Wheat Gluten Grade B | IC-5552 | REVIEW REQUIRED | Historical - verify before use |
| Maltodextrin DE10 | IC-7360 | PROVISIONAL | Historical - verify before use |
| Resistant Starch Technical | IC-6815 | PROVISIONAL | Historical - verify before use |
| Stratos Chemicals | IC-6568 | SUPERSEDED | Historical - verify before use |
| Apex Sourcing | IC-7715 | DEPRECATED | Historical - verify before use |
| SIG-98-XJT-L879 | IC-5154 | SUPERSEDED | Historical - verify before use |
| SIG-36-XEW-9SSB | IC-6544 | DEPRECATED | Historical - verify before use |
| SIG-21-VZE-Q2WM | IC-7343 | REVIEW REQUIRED | Historical - verify before use |
| Resistente Stärke Standardqualität | IC-8716 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid 98% Qualitätsstufe II | IC-8207 | SUPERSEDED | Historical - verify before use |
| Glukosesirup Syrup Lebensmittelrein | IC-8567 | DEPRECATED | Historical - verify before use |
| Baltic Trading Holdings | IC-5459 | DEPRECATED | Historical - verify before use |
| SIG-60-WEX-2G05 | IC-5289 | REVIEW REQUIRED | Historical - verify before use |
| SIG-32-UBB-EMYO | IC-9384 | SUPERSEDED | Historical - verify before use |
| withholding br 10% | IC-8931 | PROVISIONAL | Historical - verify before use |
| SIG-38-YTD-7BST | IC-5951 | REVIEW REQUIRED | Historical - verify before use |
| CA-CO-128 SAS | IC-6507 | DEPRECATED | Historical - verify before use |
| SIG-87-OKN-L3O4 | IC-9738 | PROVISIONAL | Historical - verify before use |
| Quantum Versorgung GmbH | IC-5417 | SUPERSEDED | Historical - verify before use |
| sodium chloride 99.5% premium | IC-7502 | DEPRECATED | Historical - verify before use |
| Meridian Werkstoffe Corp. | IC-8253 | DEPRECATED | Historical - verify before use |
| SIG-95-LOJ-S1L2 | IC-6559 | PROVISIONAL | Historical - verify before use |
| coconut oil standard | IC-6123 | REVIEW REQUIRED | Historical - verify before use |
| Potassium Sorbate 25% Pharma Grade | IC-6781 | SUPERSEDED | Historical - verify before use |
| meridian distribution Holdings | IC-5188 | DEPRECATED | Historical - verify before use |
| ZE-PA-511 PLC | IC-6850 | PROVISIONAL | Historical - verify before use |
| fructose 99.5% food grade | IC-8423 | PROVISIONAL | Historical - verify before use |
| SIG-13-FTX-P5F3 | IC-5589 | DEPRECATED | Historical - verify before use |
| Cyclodextrin | IC-6270 | SUPERSEDED | Historical - verify before use |
| Calcium Carbonate 70% Premiumqualität | IC-9660 | SUPERSEDED | Historical - verify before use |
| Atlantic Materials | IC-5241 | SUPERSEDED | Historical - verify before use |
| Pinnacle Sourcing | IC-6912 | DEPRECATED | Historical - verify before use |
| Meridian Sourcing | IC-7314 | PROVISIONAL | Historical - verify before use |
| Vanguard Chemicals SAS | IC-6977 | DEPRECATED | Historical - verify before use |
| Core Logistik | IC-7002 | DEPRECATED | Historical - verify before use |
| Coconut Oil 25% | IC-7136 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid Technical | IC-5763 | REVIEW REQUIRED | Historical - verify before use |
| SIG-15-NIP-N1UH | IC-9366 | SUPERSEDED | Historical - verify before use |
| fructose standard | IC-7815 | DEPRECATED | Historical - verify before use |
| AS-AC-413 | IC-5563 | SUPERSEDED | Historical - verify before use |
| Withholding GB 5% | IC-8808 | SUPERSEDED | Historical - verify before use |
| SIG-42-XLZ-4BOM | IC-6921 | SUPERSEDED | Historical - verify before use |
| AP-MA-145 International | IC-7109 | PROVISIONAL | Historical - verify before use |
| Prism Chemicals KG | IC-7448 | DEPRECATED | Historical - verify before use |
| NE-LO-125 | IC-6158 | PROVISIONAL | Historical - verify before use |
| Natriumchlorid | IC-6634 | DEPRECATED | Historical - verify before use |
| citric acid premium | IC-9129 | REVIEW REQUIRED | Historical - verify before use |
| continental processing SA | IC-9807 | DEPRECATED | Historical - verify before use |
| Dextrose 25% Technical | IC-9802 | DEPRECATED | Historical - verify before use |
| Resistente Stärke | IC-7181 | PROVISIONAL | Historical - verify before use |
| cyclodextrin 70% food grade | IC-6100 | SUPERSEDED | Historical - verify before use |
| SIG-97-SBT-Y595 | IC-7952 | PROVISIONAL | Historical - verify before use |
| SIG-87-KZL-I3ZY | IC-6599 | DEPRECATED | Historical - verify before use |
| SO-IS-99.5-PR-187 | IC-8357 | SUPERSEDED | Historical - verify before use |
| Palm Oil Food Grade | IC-5125 | PROVISIONAL | Historical - verify before use |
| AS-AC-782 | IC-7942 | PROVISIONAL | Historical - verify before use |
| Isoglucose 25% Lebensmittelrein | IC-8654 | PROVISIONAL | Historical - verify before use |
| Coconut Oil 70% Qualitätsstufe I | IC-5375 | DEPRECATED | Historical - verify before use |
| Sorbic Acid 70% | IC-9416 | DEPRECATED | Historical - verify before use |
| Traubenzucker 70% | IC-7636 | PROVISIONAL | Historical - verify before use |
| Lactic Acid | IC-5660 | DEPRECATED | Historical - verify before use |
| SIG-82-ZXL-FF30 International | IC-6736 | PROVISIONAL | Historical - verify before use |
| Excise NL 21% | IC-5494 | DEPRECATED | Historical - verify before use |
| SO-AC-852 | IC-8109 | PROVISIONAL | Historical - verify before use |
| SIG-56-YYA-I8SV | IC-8793 | DEPRECATED | Historical - verify before use |
| PR-EN-875 Group | IC-6091 | PROVISIONAL | Historical - verify before use |
| CO-OI-FO-GR-870 | IC-7013 | SUPERSEDED | Historical - verify before use |
| Catalyst Enterprise International | IC-8803 | REVIEW REQUIRED | Historical - verify before use |
| Isoglucose | IC-7996 | PROVISIONAL | Historical - verify before use |
| FR-25-GR-B-641 | IC-8019 | PROVISIONAL | Historical - verify before use |
| Prism Versorgung GmbH | IC-8540 | REVIEW REQUIRED | Historical - verify before use |
| Sodium Benzoate Pharma Grade | IC-9374 | REVIEW REQUIRED | Historical - verify before use |
| VA-RE-G-25-207 | IC-9515 | PROVISIONAL | Historical - verify before use |
| Traubenzucker 70% Qualitätsstufe I | IC-5984 | DEPRECATED | Historical - verify before use |
| Prism Materials | IC-5222 | SUPERSEDED | Historical - verify before use |
| nordic supply | IC-6394 | REVIEW REQUIRED | Historical - verify before use |
| Resistente Stärke | IC-9805 | PROVISIONAL | Historical - verify before use |
| Sonnenblumenöl Qualitätsstufe II | IC-8416 | DEPRECATED | Historical - verify before use |
| NO-LO-598 Holdings | IC-6871 | DEPRECATED | Historical - verify before use |
| vat standard nl 20% | IC-5992 | PROVISIONAL | Historical - verify before use |
| atlantic trading | IC-9651 | PROVISIONAL | Historical - verify before use |
| SIG-47-YTF-UPMT | IC-8103 | SUPERSEDED | Historical - verify before use |
| Vertex Ingredients Ltd. | IC-6050 | SUPERSEDED | Historical - verify before use |
| dextrin | IC-8582 | DEPRECATED | Historical - verify before use |
| casein | IC-9004 | PROVISIONAL | Historical - verify before use |
| Vanguard Versorgung BV | IC-6960 | PROVISIONAL | Historical - verify before use |
| SO-AC-98-579 | IC-6085 | PROVISIONAL | Historical - verify before use |
| PA-OI-70-GR-B-781 | IC-9085 | REVIEW REQUIRED | Historical - verify before use |
| SIG-64-BPY-A8RD | IC-8178 | DEPRECATED | Historical - verify before use |
| Horizon Logistics | IC-8636 | PROVISIONAL | Historical - verify before use |
| Sodium Benzoate | IC-6727 | SUPERSEDED | Historical - verify before use |
| SIG-24-NPE-GDMB | IC-8606 | DEPRECATED | Historical - verify before use |
| SIG-73-UUF-1F99 | IC-9858 | SUPERSEDED | Historical - verify before use |
| Lactic Acid Grade A | IC-5469 | DEPRECATED | Historical - verify before use |
| meridian trading Group | IC-9708 | DEPRECATED | Historical - verify before use |
| Prism Chemicals PLC | IC-5713 | REVIEW REQUIRED | Historical - verify before use |
| Citric Acid 70% | IC-7295 | REVIEW REQUIRED | Historical - verify before use |
| Core Chemicals AG | IC-6052 | DEPRECATED | Historical - verify before use |
| Lactic Acid | IC-8655 | DEPRECATED | Historical - verify before use |
| VA-RE-N-7-243 | IC-8705 | SUPERSEDED | Historical - verify before use |
| fructose | IC-5165 | REVIEW REQUIRED | Historical - verify before use |
| SIG-42-HBL-L3KU International | IC-9513 | SUPERSEDED | Historical - verify before use |
| atlantic materials | IC-6626 | SUPERSEDED | Historical - verify before use |
| SIG-36-UIL-7X71 | IC-5097 | DEPRECATED | Historical - verify before use |
| Rapsöl 99.5% Technische Qualität | IC-5020 | REVIEW REQUIRED | Historical - verify before use |
| CY-577 | IC-7569 | PROVISIONAL | Historical - verify before use |
| SIG-53-LJE-NZKR | IC-8330 | DEPRECATED | Historical - verify before use |
| VE-SO-366 | IC-6990 | PROVISIONAL | Historical - verify before use |
| SO-IS-FO-GR-334 | IC-6259 | REVIEW REQUIRED | Historical - verify before use |
| Kaliumsorbat | IC-8605 | PROVISIONAL | Historical - verify before use |
| pinnacle supply | IC-6616 | PROVISIONAL | Historical - verify before use |
| isoglucose | IC-7402 | DEPRECATED | Historical - verify before use |
| EX-N-21-216 | IC-7409 | PROVISIONAL | Historical - verify before use |
| SIG-32-UBB-EMYO | IC-6466 | PROVISIONAL | Historical - verify before use |
| Meridian Werkstoffe | IC-5622 | PROVISIONAL | Historical - verify before use |
| excise br 5% | IC-9891 | DEPRECATED | Historical - verify before use |
| Pinnacle Rohstoffe NV | IC-5734 | SUPERSEDED | Historical - verify before use |
| ST-LO-136 | IC-5040 | DEPRECATED | Historical - verify before use |
| Traubenzucker Lebensmittelrein | IC-7156 | DEPRECATED | Historical - verify before use |
| dextrin premium | IC-5836 | DEPRECATED | Historical - verify before use |
| baltic enterprise KG | IC-5011 | DEPRECATED | Historical - verify before use |
| SIG-44-FWT-OA3N | IC-7984 | REVIEW REQUIRED | Historical - verify before use |
| CA-CA-947 | IC-9954 | REVIEW REQUIRED | Historical - verify before use |
| Stellar Logistics | IC-6896 | REVIEW REQUIRED | Historical - verify before use |
| Atlas Logistik International | IC-5893 | PROVISIONAL | Historical - verify before use |
| withholding nl 15% | IC-9745 | PROVISIONAL | Historical - verify before use |
| soy isolate | IC-6291 | SUPERSEDED | Historical - verify before use |
| pacific supply | IC-8774 | DEPRECATED | Historical - verify before use |
| resistant starch food grade | IC-6773 | SUPERSEDED | Historical - verify before use |
| QU-SU-CO-959 | IC-5229 | PROVISIONAL | Historical - verify before use |
| SIG-27-FHX-VO6Y | IC-5843 | DEPRECATED | Historical - verify before use |


#### 4.3.4 Excluded Assignments

Deprecated code assignments (superseded by newer records):

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-7872-D | Duplicate source record | Escalated to data steward |
| NOISE-7511-G | Duplicate source record | Manual review scheduled |
| NOISE-4075-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-1235-H | Out of scope per business decision | Escalated to data steward |
| NOISE-6950-E | Pending validation | Escalated to data steward |
| NOISE-9528-F | Duplicate source record | Business owner notified |
| NOISE-7567-B | Duplicate source record | Escalated to data steward |
| NOISE-6322-H | Duplicate source record | Deferred to Phase 2 |
| NOISE-1320-F | Missing required attributes | Business owner notified |
| NOISE-2699-E | Missing required attributes | Business owner notified |
| NOISE-8171-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7291-H | Data quality insufficient | Escalated to data steward |
| NOISE-9765-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5531-A | Out of scope per business decision | Business owner notified |
| NOISE-1864-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-2134-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3350-H | Pending validation | Escalated to data steward |
| NOISE-8723-F | Pending validation | Deferred to Phase 2 |
| NOISE-9455-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-6506-F | Pending validation | Business owner notified |
| NOISE-3427-F | Pending validation | Manual review scheduled |
| NOISE-7841-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-4681-A | Pending validation | Business owner notified |
| NOISE-2198-H | Out of scope per business decision | Business owner notified |
| NOISE-1547-H | Out of scope per business decision | Escalated to data steward |
| NOISE-4176-E | Missing required attributes | Business owner notified |
| NOISE-1715-G | Data quality insufficient | Business owner notified |
| NOISE-2405-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-4819-H | Duplicate source record | Manual review scheduled |
| NOISE-5392-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-2817-B | Data quality insufficient | Business owner notified |
| NOISE-6630-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3065-G | Pending validation | Manual review scheduled |
| NOISE-4778-C | Duplicate source record | Business owner notified |
| NOISE-9277-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8411-A | Out of scope per business decision | Escalated to data steward |
| NOISE-7341-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2444-E | Pending validation | Business owner notified |
| NOISE-6973-E | Pending validation | Deferred to Phase 2 |
| NOISE-3399-B | Missing required attributes | Manual review scheduled |
| NOISE-2612-C | Pending validation | Manual review scheduled |
| NOISE-9359-H | Data quality insufficient | Manual review scheduled |
| NOISE-3439-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9592-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-6833-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-1470-A | Data quality insufficient | Manual review scheduled |
| NOISE-9053-G | Duplicate source record | Business owner notified |
| NOISE-3063-H | Pending validation | Deferred to Phase 2 |
| NOISE-6878-A | Pending validation | Manual review scheduled |
| NOISE-3406-G | Duplicate source record | Escalated to data steward |
| NOISE-1858-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-4914-F | Pending validation | Business owner notified |
| NOISE-9324-C | Pending validation | Escalated to data steward |
| NOISE-3002-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-8263-G | Pending validation | Manual review scheduled |
| NOISE-9071-E | Duplicate source record | Escalated to data steward |
| NOISE-1302-C | Pending validation | Manual review scheduled |
| NOISE-3341-A | Out of scope per business decision | Business owner notified |
| NOISE-9402-E | Pending validation | Escalated to data steward |
| NOISE-3273-H | Out of scope per business decision | Business owner notified |
| NOISE-4275-D | Out of scope per business decision | Business owner notified |
| NOISE-8593-H | Missing required attributes | Manual review scheduled |
| NOISE-3445-A | Missing required attributes | Manual review scheduled |
| NOISE-1949-A | Pending validation | Deferred to Phase 2 |
| NOISE-2181-D | Duplicate source record | Manual review scheduled |
| NOISE-7810-C | Missing required attributes | Escalated to data steward |
| NOISE-5545-E | Data quality insufficient | Escalated to data steward |
| NOISE-4323-G | Pending validation | Escalated to data steward |
| NOISE-5935-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-9576-B | Missing required attributes | Escalated to data steward |
| NOISE-3455-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9483-H | Duplicate source record | Manual review scheduled |
| NOISE-4308-E | Missing required attributes | Escalated to data steward |
| NOISE-5524-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2765-C | Out of scope per business decision | Business owner notified |
| NOISE-6408-H | Data quality insufficient | Escalated to data steward |
| NOISE-5973-A | Pending validation | Business owner notified |
| NOISE-5506-H | Out of scope per business decision | Escalated to data steward |
| NOISE-6153-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-6597-H | Missing required attributes | Escalated to data steward |
| NOISE-3033-C | Pending validation | Manual review scheduled |
| NOISE-9316-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9662-D | Duplicate source record | Business owner notified |
| NOISE-9401-C | Duplicate source record | Business owner notified |
| NOISE-5185-A | Data quality insufficient | Business owner notified |
| NOISE-3397-E | Data quality insufficient | Escalated to data steward |
| NOISE-9740-C | Pending validation | Escalated to data steward |
| NOISE-3654-C | Data quality insufficient | Manual review scheduled |
| NOISE-7371-G | Out of scope per business decision | Business owner notified |
| NOISE-2165-G | Out of scope per business decision | Manual review scheduled |
| NOISE-1867-H | Out of scope per business decision | Escalated to data steward |
| NOISE-7334-C | Out of scope per business decision | Manual review scheduled |
| NOISE-9718-E | Duplicate source record | Escalated to data steward |
| NOISE-3748-B | Out of scope per business decision | Escalated to data steward |
| NOISE-9951-B | Pending validation | Escalated to data steward |
| NOISE-4169-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1357-E | Pending validation | Escalated to data steward |
| NOISE-3387-F | Missing required attributes | Manual review scheduled |
| NOISE-1642-D | Missing required attributes | Business owner notified |
| NOISE-1805-B | Missing required attributes | Manual review scheduled |
| NOISE-3350-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-9872-A | Data quality insufficient | Business owner notified |
| NOISE-4520-D | Pending validation | Escalated to data steward |
| NOISE-9829-C | Pending validation | Escalated to data steward |
| NOISE-1878-F | Missing required attributes | Manual review scheduled |
| NOISE-6802-C | Out of scope per business decision | Business owner notified |
| NOISE-6784-D | Data quality insufficient | Escalated to data steward |
| NOISE-4678-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-5111-A | Pending validation | Escalated to data steward |
| NOISE-1488-B | Out of scope per business decision | Business owner notified |
| NOISE-7627-D | Out of scope per business decision | Business owner notified |
| NOISE-1600-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-9877-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3956-F | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2737-D | Out of scope per business decision | Business owner notified |
| NOISE-8391-H | Duplicate source record | Business owner notified |
| NOISE-2255-D | Data quality insufficient | Business owner notified |
| NOISE-6013-F | Pending validation | Manual review scheduled |
| NOISE-2372-G | Out of scope per business decision | Manual review scheduled |
| NOISE-5294-G | Out of scope per business decision | Manual review scheduled |
| NOISE-5621-C | Out of scope per business decision | Manual review scheduled |
| NOISE-5385-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-1818-E | Duplicate source record | Manual review scheduled |
| NOISE-2775-H | Data quality insufficient | Escalated to data steward |
| NOISE-4668-D | Duplicate source record | Manual review scheduled |
| NOISE-8434-F | Data quality insufficient | Escalated to data steward |
| NOISE-5240-G | Duplicate source record | Escalated to data steward |
| NOISE-8040-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9370-D | Duplicate source record | Manual review scheduled |
| NOISE-7418-D | Data quality insufficient | Business owner notified |
| NOISE-8365-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3214-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4124-F | Pending validation | Manual review scheduled |
| NOISE-2166-E | Missing required attributes | Escalated to data steward |
| NOISE-8788-E | Missing required attributes | Manual review scheduled |
| NOISE-1178-B | Pending validation | Deferred to Phase 2 |
| NOISE-8182-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-5914-E | Out of scope per business decision | Manual review scheduled |
| NOISE-5874-F | Pending validation | Business owner notified |
| NOISE-8358-F | Data quality insufficient | Escalated to data steward |
| NOISE-1017-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8270-G | Pending validation | Deferred to Phase 2 |
| NOISE-2065-D | Missing required attributes | Manual review scheduled |
| NOISE-1955-A | Duplicate source record | Manual review scheduled |
| NOISE-2387-B | Out of scope per business decision | Escalated to data steward |
| NOISE-8333-B | Out of scope per business decision | Business owner notified |
| NOISE-6355-B | Out of scope per business decision | Escalated to data steward |
| NOISE-5655-E | Pending validation | Escalated to data steward |
| NOISE-9752-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8779-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5858-E | Data quality insufficient | Manual review scheduled |
| NOISE-3108-C | Pending validation | Manual review scheduled |
| NOISE-4237-B | Data quality insufficient | Business owner notified |
| NOISE-6657-D | Data quality insufficient | Manual review scheduled |
| NOISE-2521-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8364-B | Data quality insufficient | Escalated to data steward |
| NOISE-9165-D | Data quality insufficient | Escalated to data steward |
| NOISE-8225-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-4432-D | Missing required attributes | Manual review scheduled |
| NOISE-2109-E | Pending validation | Deferred to Phase 2 |
| NOISE-5131-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7810-E | Pending validation | Business owner notified |
| NOISE-9943-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-1579-E | Out of scope per business decision | Escalated to data steward |
| NOISE-8550-C | Data quality insufficient | Escalated to data steward |
| NOISE-2754-A | Out of scope per business decision | Business owner notified |
| NOISE-3937-C | Pending validation | Business owner notified |
| NOISE-4248-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1490-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8466-F | Duplicate source record | Escalated to data steward |
| NOISE-4206-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-2523-C | Out of scope per business decision | Manual review scheduled |
| NOISE-5287-F | Data quality insufficient | Escalated to data steward |
| NOISE-2454-H | Out of scope per business decision | Manual review scheduled |
| NOISE-4400-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6441-F | Missing required attributes | Escalated to data steward |
| NOISE-4739-H | Pending validation | Escalated to data steward |
| NOISE-7177-G | Pending validation | Business owner notified |
| NOISE-3344-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-3443-E | Pending validation | Manual review scheduled |
| NOISE-6087-A | Duplicate source record | Escalated to data steward |
| NOISE-4985-F | Data quality insufficient | Manual review scheduled |
| NOISE-3664-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2850-B | Pending validation | Manual review scheduled |
| NOISE-7954-E | Data quality insufficient | Business owner notified |
| NOISE-4761-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-1391-A | Duplicate source record | Manual review scheduled |
| NOISE-4296-F | Out of scope per business decision | Business owner notified |
| NOISE-9023-H | Pending validation | Business owner notified |
| NOISE-6824-H | Duplicate source record | Deferred to Phase 2 |
| NOISE-9867-A | Missing required attributes | Manual review scheduled |
| NOISE-1595-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-7476-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8721-B | Data quality insufficient | Manual review scheduled |
| NOISE-9638-A | Out of scope per business decision | Escalated to data steward |
| NOISE-9426-D | Data quality insufficient | Business owner notified |
| NOISE-1026-G | Data quality insufficient | Business owner notified |
| NOISE-1818-B | Duplicate source record | Manual review scheduled |
| NOISE-4799-D | Missing required attributes | Business owner notified |
| NOISE-3398-F | Out of scope per business decision | Manual review scheduled |
| NOISE-6429-H | Data quality insufficient | Business owner notified |
| NOISE-1337-F | Pending validation | Business owner notified |
| NOISE-9480-G | Data quality insufficient | Manual review scheduled |
| NOISE-5252-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-3797-H | Data quality insufficient | Escalated to data steward |
| NOISE-6327-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8879-B | Missing required attributes | Manual review scheduled |
| NOISE-7615-H | Missing required attributes | Escalated to data steward |
| NOISE-5805-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-5996-D | Missing required attributes | Manual review scheduled |
| NOISE-8299-D | Duplicate source record | Business owner notified |
| NOISE-7697-D | Pending validation | Business owner notified |
| NOISE-1191-E | Duplicate source record | Escalated to data steward |
| NOISE-9578-B | Out of scope per business decision | Business owner notified |
| NOISE-3690-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2792-A | Pending validation | Manual review scheduled |
| NOISE-6156-F | Data quality insufficient | Manual review scheduled |
| NOISE-8042-D | Data quality insufficient | Manual review scheduled |
| NOISE-3110-A | Data quality insufficient | Business owner notified |
| NOISE-9889-G | Data quality insufficient | Manual review scheduled |
| NOISE-6256-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3232-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-7435-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5572-D | Pending validation | Business owner notified |
| NOISE-8064-F | Duplicate source record | Manual review scheduled |
| NOISE-1335-A | Pending validation | Escalated to data steward |
| NOISE-5667-C | Pending validation | Deferred to Phase 2 |
| NOISE-2483-H | Duplicate source record | Manual review scheduled |
| NOISE-3900-C | Pending validation | Business owner notified |
| NOISE-7074-B | Data quality insufficient | Business owner notified |
| NOISE-4552-H | Pending validation | Manual review scheduled |
| NOISE-7107-A | Duplicate source record | Escalated to data steward |
| NOISE-6003-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-7368-D | Duplicate source record | Manual review scheduled |
| NOISE-6390-F | Data quality insufficient | Business owner notified |
| NOISE-4652-C | Data quality insufficient | Escalated to data steward |
| NOISE-4697-H | Pending validation | Deferred to Phase 2 |
| NOISE-7892-E | Out of scope per business decision | Escalated to data steward |
| NOISE-2078-B | Data quality insufficient | Business owner notified |
| NOISE-5154-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-7649-E | Out of scope per business decision | Business owner notified |
| NOISE-7563-H | Duplicate source record | Manual review scheduled |
| NOISE-2615-E | Pending validation | Business owner notified |
| NOISE-3153-E | Duplicate source record | Business owner notified |
| NOISE-9394-C | Duplicate source record | Escalated to data steward |
| NOISE-5650-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-2993-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-5924-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-6876-D | Data quality insufficient | Manual review scheduled |
| NOISE-7728-F | Data quality insufficient | Manual review scheduled |
| NOISE-3417-E | Pending validation | Deferred to Phase 2 |
| NOISE-1081-B | Pending validation | Manual review scheduled |
| NOISE-9431-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-1822-H | Out of scope per business decision | Business owner notified |
| NOISE-8763-A | Pending validation | Business owner notified |
| NOISE-2071-C | Pending validation | Manual review scheduled |
| NOISE-6303-F | Duplicate source record | Business owner notified |
| NOISE-7067-G | Data quality insufficient | Manual review scheduled |
| NOISE-7521-G | Duplicate source record | Manual review scheduled |
| NOISE-6026-F | Data quality insufficient | Manual review scheduled |
| NOISE-3543-G | Out of scope per business decision | Escalated to data steward |
| NOISE-3567-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-1724-H | Data quality insufficient | Escalated to data steward |
| NOISE-2393-D | Duplicate source record | Escalated to data steward |
| NOISE-7314-H | Duplicate source record | Escalated to data steward |
| NOISE-5973-G | Duplicate source record | Business owner notified |
| NOISE-6721-H | Missing required attributes | Business owner notified |
| NOISE-8372-E | Pending validation | Escalated to data steward |
| NOISE-7269-C | Duplicate source record | Business owner notified |
| NOISE-8530-G | Out of scope per business decision | Escalated to data steward |
| NOISE-1936-E | Missing required attributes | Deferred to Phase 2 |
| NOISE-4569-E | Out of scope per business decision | Manual review scheduled |
| NOISE-7650-G | Data quality insufficient | Business owner notified |
| NOISE-2000-H | Pending validation | Deferred to Phase 2 |
| NOISE-3865-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-6678-D | Duplicate source record | Manual review scheduled |
| NOISE-1712-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-9222-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-7387-H | Missing required attributes | Manual review scheduled |
| NOISE-7735-A | Pending validation | Manual review scheduled |
| NOISE-8555-G | Out of scope per business decision | Business owner notified |
| NOISE-6495-A | Missing required attributes | Business owner notified |
| NOISE-9938-B | Pending validation | Manual review scheduled |
| NOISE-8260-B | Out of scope per business decision | Escalated to data steward |
| NOISE-6014-F | Data quality insufficient | Business owner notified |
| NOISE-1058-B | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1393-F | Missing required attributes | Escalated to data steward |
| NOISE-7550-D | Duplicate source record | Manual review scheduled |
| NOISE-3132-E | Duplicate source record | Manual review scheduled |
| NOISE-1865-E | Pending validation | Business owner notified |
| NOISE-7816-B | Data quality insufficient | Business owner notified |
| NOISE-7469-D | Duplicate source record | Business owner notified |
| NOISE-7447-G | Duplicate source record | Business owner notified |
| NOISE-5344-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9501-D | Data quality insufficient | Business owner notified |
| NOISE-4829-F | Missing required attributes | Deferred to Phase 2 |
| NOISE-9642-C | Data quality insufficient | Escalated to data steward |
| NOISE-2493-E | Missing required attributes | Business owner notified |
| NOISE-4794-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8789-A | Duplicate source record | Escalated to data steward |
| NOISE-4380-E | Missing required attributes | Business owner notified |
| NOISE-4184-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-6362-D | Pending validation | Escalated to data steward |
| NOISE-7056-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-6697-G | Out of scope per business decision | Manual review scheduled |
| NOISE-4530-A | Missing required attributes | Manual review scheduled |
| NOISE-8473-H | Duplicate source record | Business owner notified |
| NOISE-7718-H | Data quality insufficient | Manual review scheduled |
| NOISE-4513-G | Missing required attributes | Escalated to data steward |
| NOISE-7507-H | Pending validation | Manual review scheduled |
| NOISE-2866-E | Data quality insufficient | Business owner notified |
| NOISE-5543-B | Pending validation | Manual review scheduled |
| NOISE-2303-F | Pending validation | Business owner notified |
| NOISE-7943-G | Data quality insufficient | Business owner notified |
| NOISE-1394-F | Out of scope per business decision | Business owner notified |
| NOISE-8917-H | Pending validation | Business owner notified |
| NOISE-5997-A | Out of scope per business decision | Escalated to data steward |
| NOISE-1955-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-4965-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4170-G | Out of scope per business decision | Escalated to data steward |
| NOISE-8640-H | Pending validation | Manual review scheduled |
| NOISE-7568-B | Data quality insufficient | Deferred to Phase 2 |
| NOISE-9334-D | Duplicate source record | Manual review scheduled |
| NOISE-7137-C | Data quality insufficient | Manual review scheduled |
| NOISE-5032-F | Duplicate source record | Escalated to data steward |
| NOISE-8327-A | Data quality insufficient | Business owner notified |
| NOISE-5854-C | Out of scope per business decision | Business owner notified |
| NOISE-7756-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5514-D | Data quality insufficient | Business owner notified |


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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230414_000000`
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
| Technical Lead | Michael Weber (Business Operations) | michael@company.com | +1-555-0102 |
| Business Owner | David Kim (Project Management) | david@company.com | +1-555-0103 |
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
