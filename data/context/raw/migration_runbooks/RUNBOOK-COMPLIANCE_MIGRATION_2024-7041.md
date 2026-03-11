# Migration Runbook: System Migration: COMPLIANCE_MIGRATION_2024

**Document ID**: RB-COMPLIANCE_MIGRATION_2024-8141
**Version**: 2.1
**Last Updated**: 2023-07-28
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the System Migration: COMPLIANCE_MIGRATION_2024 project.
The migration involves transitioning master data and transactional records from SOURCE
to TARGET while maintaining data integrity and business continuity.

**Project Timeline**: 2023-05-21 to 2023-09-28
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
| Total entities assessed | 1446 | Completed |
| Codes assigned | 1044 | Staged |
| Excluded from scope | 313 | Documented |
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
| Isoglucose 25% | TC-8279 | 2023-07-07 | Operations |
| Fructose 99.5% Technische Qualität | IC-8282 | 2021-11-10 | Finance |
| SIG-61-XKV-ODPX | BC-8284 | 2024-02-09 | Finance |
| SIG-45-ZZU-GRXH International | BC-8295 | 2023-07-01 | Supply Chain |
| SIG-77-TUK-IN2B | IC-8325 | 2021-11-18 | IT Infrastructure |
| SIG-76-YLU-7DL9 | TC-8335 | 2023-11-03 | IT Infrastructure |
| sorbic acid | BC-8342 | 2024-12-17 | Finance |
| zenith logistics | TC-8353 | 2024-11-23 | Product Management |
| VA-RE-I-20-892 | TC-8371 | 2022-02-28 | IT Infrastructure |
| SIG-29-BZP-SU62 | IC-8380 | 2024-02-27 | Compliance |
| Isoglucose 70% | TC-8393 | 2024-04-01 | Data Governance |
| Fructose 25% | BC-8412 | 2024-01-11 | Data Governance |
| SIG-79-SPO-WT80 | TC-8419 | 2021-05-07 | Finance |
| Calcium Carbonate 98% | TC-8421 | 2024-08-04 | Compliance |
| Atlas Materials | IC-8430 | 2021-12-08 | Data Governance |
| nexus supply | IC-8435 | 2021-02-11 | Data Governance |
| RE-ST-FO-GR-238 | BC-8457 | 2024-10-28 | Product Management |
| Sorbinsäure 50% Lebensmittelrein | TC-8461 | 2024-08-21 | Operations |
| Potassium Sorbate 50% Technical | IC-8463 | 2024-03-07 | Finance |
| SIG-69-TRZ-SFLQ | IC-8478 | 2021-09-06 | Compliance |
| vanguard industries AG | IC-8479 | 2023-05-07 | Finance |
| SIG-42-AJS-6RPK | BC-8481 | 2022-08-19 | Product Management |
| SIG-43-XDN-7VEU | IC-8489 | 2023-11-23 | Compliance |
| Fructose | BC-8504 | 2022-10-19 | Product Management |
| core chemicals Group | BC-8510 | 2021-04-10 | Supply Chain |
| Zitronensäure Qualitätsstufe I | IC-8514 | 2022-10-04 | Data Governance |
| CO-OI-50-PH-GR-568 | BC-8516 | 2022-04-06 | Operations |
| Fructose 25% | IC-8522 | 2023-05-04 | Supply Chain |
| SIG-95-APX-PWFS | TC-8533 | 2023-01-23 | Data Governance |
| Dextrin Premium | BC-8549 | 2023-09-27 | Product Management |
| SIG-10-DWM-ZA0C | TC-8551 | 2022-02-05 | Supply Chain |
| ME-LO-670 | BC-8560 | 2022-03-05 | Finance |
| Pea Protein 98% Grade B | IC-8561 | 2024-10-04 | Compliance |
| sunflower oil | TC-8566 | 2024-11-21 | Supply Chain |
| SIG-38-OTV-E78M | TC-8571 | 2024-12-19 | Compliance |
| Resistant Starch Grade A | BC-8575 | 2024-06-28 | IT Infrastructure |
| SIG-30-LJO-TN4Y | BC-8583 | 2023-03-21 | Data Governance |
| Vanguard Materials | TC-8591 | 2024-01-15 | Operations |
| calcium carbonate 50% premium | IC-8596 | 2024-01-08 | Finance |
| CU-DU-F-5-228 | TC-8604 | 2022-05-18 | Product Management |
| Lactic Acid 70% Pharmazeutisch rein | IC-8613 | 2024-10-03 | Data Governance |
| SIG-19-TLQ-1P5Z | IC-8618 | 2023-04-03 | Compliance |
| Sorbinsäure | TC-8619 | 2024-05-28 | IT Infrastructure |
| Fructose | IC-8622 | 2024-04-03 | Data Governance |
| SIG-84-HBF-DDQL | BC-8636 | 2024-10-02 | IT Infrastructure |
| dextrose 25% | BC-8647 | 2023-05-25 | Supply Chain |
| Weizenklebereiweiß Qualitätsstufe I | TC-8652 | 2022-03-12 | IT Infrastructure |
| vertex logistics | TC-8668 | 2021-07-01 | Operations |
| Sodium Chloride 99.5% Grade A | BC-8676 | 2024-07-06 | Compliance |
| Dextrin Grade B | TC-8682 | 2021-01-14 | Compliance |
| WH-GL-50-TE-338 | TC-8701 | 2021-12-11 | Data Governance |
| CE-LO-195 | BC-8702 | 2021-09-13 | Operations |
| SU-OI-FO-GR-778 | BC-8720 | 2023-12-05 | Supply Chain |
| Withholding NL 5% | BC-8733 | 2024-05-14 | Product Management |
| VE-SO-401 | TC-8739 | 2021-08-21 | IT Infrastructure |
| Sunflower Oil Pharma Grade | TC-8752 | 2022-12-20 | Finance |
| Sorbic Acid 50% Grade A | IC-8757 | 2021-02-25 | IT Infrastructure |
| atlantic processing Holdings | IC-8763 | 2023-12-28 | Product Management |
| pacific industries | IC-8767 | 2022-03-10 | IT Infrastructure |
| Resistant Starch 98% Pharma Grade | BC-8788 | 2022-01-12 | Product Management |
| SIG-68-HOK-ETCC | BC-8793 | 2022-11-08 | Supply Chain |
| continental solutions SARL | TC-8811 | 2021-04-15 | Operations |
| Ascorbic Acid | BC-8813 | 2022-11-01 | Data Governance |
| premier manufacturing BV | BC-8817 | 2024-12-06 | Product Management |
| SIG-75-DRM-1CLN | TC-8830 | 2022-08-15 | Compliance |
| IS-641 | IC-8835 | 2021-12-04 | Supply Chain |
| Dextrose Grade B | BC-8842 | 2022-01-04 | Product Management |
| VA-RE-G-25-615 | TC-8845 | 2024-04-20 | Finance |
| Quantum Partners | BC-8860 | 2021-12-09 | Operations |
| Premier Handel Group | TC-8866 | 2023-04-25 | Finance |
| Pacific Materials | TC-8870 | 2022-04-07 | Operations |
| Withholding US 25% | IC-8879 | 2024-01-26 | Data Governance |
| Atlantic Trading | IC-8898 | 2021-11-28 | Operations |
| coconut oil 25% tech grade | TC-8925 | 2024-03-17 | Operations |
| LA-AC-927 | TC-8927 | 2024-10-03 | Supply Chain |
| Kasein 98% | BC-8935 | 2021-05-16 | IT Infrastructure |
| RA-OI-25-FO-GR-818 | TC-8943 | 2024-02-20 | Finance |
| cyclodextrin 98% | BC-8948 | 2024-09-03 | Compliance |
| Zitronensäure Qualitätsstufe II | TC-8950 | 2024-11-08 | Data Governance |
| DE-70-856 | IC-8952 | 2024-06-27 | Operations |
| Zitronensäure | IC-8954 | 2024-05-22 | Product Management |
| AS-AC-573 | BC-8965 | 2024-04-21 | Product Management |
| Stratos Distribution Group | IC-8967 | 2024-01-20 | Supply Chain |
| PR-SU-CO-443 | TC-8975 | 2021-10-11 | Finance |
| SIG-83-XMM-APXP | IC-8976 | 2023-03-23 | Product Management |
| premier partners SARL | BC-8982 | 2022-05-04 | Compliance |
| Rapeseed Oil Technical | TC-8995 | 2021-03-17 | Operations |
| SIG-55-DBH-2QS3 | TC-9001 | 2021-02-08 | IT Infrastructure |
| Prism Sourcing | TC-9024 | 2021-04-04 | IT Infrastructure |
| lactic acid standard | BC-9056 | 2021-12-28 | Data Governance |
| Core Chemicals Holdings | BC-9062 | 2024-11-27 | Finance |
| soy isolate | BC-9101 | 2022-07-03 | Supply Chain |
| Premier Supply Co. | TC-9108 | 2021-04-25 | Compliance |
| pinnacle distribution Holdings | BC-9120 | 2022-08-04 | Data Governance |
| Traubenzucker 98% Qualitätsstufe I | IC-9129 | 2024-11-01 | Operations |
| Coconut Oil 25% Grade A | TC-9139 | 2021-11-10 | Finance |
| soy isolate 99.5% premium | IC-9147 | 2021-04-26 | Operations |
| PR-IN-608 BV | BC-9155 | 2023-12-06 | IT Infrastructure |
| Atlas Enterprise International | TC-9173 | 2024-11-23 | Operations |
| Zitronensäure Premiumqualität | IC-9174 | 2024-06-14 | Product Management |
| QU-SU-CO-890 | IC-9179 | 2024-03-21 | Operations |
| SIG-86-EKJ-RFVB | TC-9183 | 2022-10-14 | Compliance |
| Resistant Starch 99.5% | TC-9184 | 2021-12-06 | Data Governance |
| SIG-18-PCA-V46E | TC-9199 | 2021-10-27 | IT Infrastructure |
| resistant starch standard | TC-9209 | 2021-02-26 | Product Management |
| PI-SO-581 Inc. | TC-9220 | 2021-04-18 | Product Management |
| Withholding NL 21% | IC-9227 | 2022-09-21 | Supply Chain |
| SIG-33-IWB-UV4J | IC-9229 | 2023-11-03 | Product Management |
| Palmfett 98% Qualitätsstufe I | TC-9241 | 2022-10-19 | Finance |
| NO-SU-CO-498 | TC-9274 | 2021-11-24 | Finance |
| ascorbic acid 98% premium | TC-9287 | 2024-07-03 | Compliance |
| stratos logistics | BC-9291 | 2021-07-11 | Compliance |
| PR-CO-800 Corp. | IC-9299 | 2021-10-07 | Product Management |
| Casein 98% Technical | IC-9302 | 2021-01-26 | Compliance |
| SIG-47-MIU-LIH6 | BC-9309 | 2023-05-07 | Finance |
| SIG-99-VAH-2H31 | BC-9311 | 2023-11-09 | IT Infrastructure |
| Elite Supply Co. | TC-9318 | 2024-03-06 | IT Infrastructure |
| horizon ingredients LLC | TC-9319 | 2022-10-16 | Supply Chain |
| Palm Oil Food Grade | IC-9322 | 2024-02-16 | Product Management |
| SIG-58-NYA-2O4M | TC-9325 | 2023-11-20 | Compliance |
| Vertex Vertrieb Group | BC-9327 | 2021-12-16 | Supply Chain |
| Core Distribution | BC-9341 | 2021-02-03 | Finance |
| nexus logistics | IC-9357 | 2021-09-06 | Finance |
| casein premium | BC-9361 | 2021-04-07 | Operations |
| SO-BE-ST-871 | IC-9362 | 2024-02-09 | Product Management |
| Zitronensäure 98% | BC-9363 | 2021-05-23 | Data Governance |
| premier enterprise Holdings | IC-9364 | 2024-02-06 | Compliance |
| Citric Acid 50% Grade A | BC-9412 | 2022-01-08 | Operations |
| apex enterprise International | BC-9418 | 2023-07-07 | Finance |
| SIG-33-FUV-53NO | TC-9447 | 2023-10-15 | Data Governance |
| SO-IS-PH-GR-671 | BC-9457 | 2021-11-01 | Compliance |
| Quantum Supply Co. | IC-9479 | 2022-11-25 | Data Governance |
| cyclodextrin 98% pharma grade | IC-9481 | 2021-07-26 | IT Infrastructure |
| SO-CH-GR-B-273 | IC-9485 | 2023-08-15 | Finance |
| Traubenzucker Qualitätsstufe I | BC-9496 | 2021-11-01 | Data Governance |
| Palm Oil 98% | TC-9498 | 2021-01-21 | Supply Chain |
| Meridian Logistics | TC-9500 | 2022-08-14 | Compliance |
| PI-LO-142 | IC-9502 | 2021-07-17 | Product Management |
| SIG-82-JMP-PVGN | TC-9505 | 2022-07-15 | Compliance |
| SO-BE-GR-A-760 | IC-9532 | 2022-02-09 | Product Management |
| SIG-92-VAB-1JHU | BC-9585 | 2024-08-18 | Product Management |
| CO-OI-25-TE-157 | TC-9586 | 2023-04-26 | IT Infrastructure |
| SIG-34-UJK-TJA6 | IC-9607 | 2024-02-26 | Data Governance |
| Sorbic Acid 25% Grade B | TC-9631 | 2024-06-24 | Compliance |
| Sorbinsäure 70% | BC-9645 | 2024-05-03 | Data Governance |
| Catalyst Materials | BC-9653 | 2022-04-15 | Compliance |
| Pacific Werkstoffe | TC-9681 | 2023-01-07 | Data Governance |
| Soy Isolate 98% Food Grade | IC-9694 | 2023-10-09 | Supply Chain |
| fructose 70% | IC-9705 | 2021-07-27 | Compliance |
| SIG-79-HKV-T268 | IC-9713 | 2023-04-09 | Compliance |
| PO-SO-339 | BC-9736 | 2024-05-03 | Finance |
| Vat Standard NL 19% | IC-9748 | 2022-12-28 | Operations |
| RA-OI-431 | IC-9753 | 2021-02-15 | IT Infrastructure |
| AP-SO-576 | IC-9772 | 2022-05-03 | IT Infrastructure |
| sodium chloride 99.5% premium | IC-9774 | 2022-01-24 | IT Infrastructure |
| Stratos Partners SAS | IC-9804 | 2023-01-06 | Data Governance |
| SIG-38-WKO-LWQT | IC-9818 | 2021-02-07 | Operations |
| PA-SO-270 | TC-9820 | 2024-02-19 | Supply Chain |
| SIG-77-RVO-CE8D Inc. | IC-9831 | 2023-05-06 | Data Governance |
| Ascorbic Acid Pharmazeutisch rein | BC-9863 | 2023-11-01 | Compliance |
| Prism Sourcing | TC-9865 | 2024-01-13 | Data Governance |
| PA-CH-580 KG | IC-9868 | 2023-05-23 | Operations |
| Isoglucose | IC-9875 | 2021-10-06 | Operations |
| PO-SO-768 | BC-9896 | 2023-02-11 | Supply Chain |
| CA-CA-99.5-291 | BC-9911 | 2022-10-12 | IT Infrastructure |
| SIG-14-TOH-IPJ4 | IC-9930 | 2023-08-25 | Finance |
| SIG-27-RTX-YEAW | BC-9969 | 2023-11-11 | Product Management |
| SO-IS-GR-A-940 | BC-9973 | 2021-08-18 | Supply Chain |
| quantum processing International | BC-10004 | 2023-12-26 | Data Governance |
| SIG-27-FHB-EY0E | BC-10008 | 2024-02-08 | IT Infrastructure |
| FR-99.5-TE-579 | BC-10013 | 2021-07-10 | Finance |
| Vanguard Enterprise International | BC-10044 | 2023-08-02 | Finance |
| ascorbic acid standard | IC-10046 | 2022-02-24 | Finance |
| Lactic Acid 25% Lebensmittelrein | BC-10048 | 2024-06-15 | Operations |
| SIG-81-HMA-4WEQ | IC-10067 | 2022-02-04 | Product Management |
| Vat Standardqualität FR 21% | TC-10086 | 2022-12-03 | IT Infrastructure |
| Stellar Werkstoffe | TC-10149 | 2021-10-09 | Data Governance |
| Fructose | TC-10150 | 2021-08-03 | Compliance |
| horizon trading Ltd. | BC-10180 | 2024-04-05 | Data Governance |
| Resistente Stärke | BC-10188 | 2021-04-02 | Operations |
| SIG-73-AXD-XIX9 | IC-10232 | 2024-09-20 | Data Governance |
| Prism Manufacturing NV | BC-10235 | 2023-01-16 | Data Governance |
| Vanguard Industries BV | IC-10243 | 2024-05-21 | Finance |
| Nordic Supply Co. | BC-10246 | 2021-02-16 | IT Infrastructure |
| Elite Manufacturing | TC-10248 | 2023-05-15 | Compliance |
| SIG-58-BDQ-I1V3 | TC-10250 | 2022-04-17 | Product Management |
| Pea Protein 70% Technische Qualität | IC-10256 | 2021-02-25 | Finance |
| PA-SO-568 | TC-10289 | 2023-05-09 | Operations |
| Pinnacle Rohstoffe NV | IC-10303 | 2024-03-19 | Data Governance |
| Vanguard Enterprise Group | BC-10307 | 2024-08-03 | Finance |
| Fructose | TC-10319 | 2023-10-01 | Finance |
| WH-GL-GR-A-583 | TC-10327 | 2023-09-22 | IT Infrastructure |
| Kasein | TC-10342 | 2022-03-10 | Product Management |
| Natriumbenzoat 25% | BC-10345 | 2022-02-12 | Product Management |
| NE-SO-652 | TC-10347 | 2023-05-21 | Supply Chain |
| fructose tech grade | BC-10353 | 2024-02-15 | Operations |
| Meridian Logistics | IC-10362 | 2021-05-15 | Data Governance |
| PR-SU-CO-349 | TC-10364 | 2022-03-11 | Data Governance |
| vanguard supply NV | IC-10366 | 2023-03-19 | Product Management |
| maltodextrin de15 | TC-10375 | 2024-05-13 | Operations |
| CA-CA-50-GR-A-195 | TC-10401 | 2023-03-23 | Finance |
| Horizon Partners | TC-10414 | 2023-04-07 | Finance |
| Ascorbic Acid 99.5% Technische Qualität | BC-10415 | 2024-11-14 | Data Governance |
| VA-PA-407 | BC-10421 | 2022-11-16 | Compliance |
| SO-AC-25-ST-106 | TC-10433 | 2024-07-22 | Compliance |
| PI-MA-680 | BC-10441 | 2022-10-19 | Data Governance |
| SIG-60-VTH-H7AM | BC-10456 | 2023-09-16 | Product Management |
| VA-RE-N-10-785 | TC-10492 | 2024-05-07 | Operations |
| Natriumbenzoat | TC-10500 | 2024-08-25 | Product Management |
| SIG-92-GIK-H4FF | IC-10517 | 2023-09-13 | Compliance |
| Global Solutions Group | TC-10523 | 2023-11-23 | Finance |
| SIG-15-MKL-LGBK | IC-10532 | 2022-09-17 | Data Governance |
| Vanguard Supply Co. | TC-10538 | 2022-06-24 | Finance |
| PR-IN-195 KG | TC-10541 | 2023-01-03 | Operations |
| Customs Duty DE 5% | IC-10549 | 2024-10-21 | Operations |
| continental manufacturing Inc. | IC-10559 | 2024-05-19 | IT Infrastructure |
| Customs Duty US 20% | TC-10584 | 2022-02-09 | Operations |
| VE-SO-366 | IC-10586 | 2023-03-28 | Data Governance |
| Soy Isolate | TC-10598 | 2023-01-09 | Compliance |
| coconut oil | TC-10626 | 2021-09-10 | Supply Chain |
| AS-AC-PR-778 | IC-10627 | 2022-03-01 | Data Governance |
| Resistente Stärke | TC-10628 | 2023-03-24 | Product Management |
| Catalyst Industries International | IC-10633 | 2022-09-10 | Data Governance |
| SIG-70-EXR-LD0M | IC-10634 | 2024-02-14 | Compliance |
| Potassium Sorbate Technical | BC-10670 | 2021-09-05 | IT Infrastructure |
| Sodium Benzoate Grade A | IC-10694 | 2023-03-22 | Data Governance |
| ZE-PA-511 PLC | BC-10696 | 2024-11-24 | Supply Chain |
| SIG-97-EIS-DKQB Holdings | TC-10698 | 2022-01-25 | IT Infrastructure |
| Lactic Acid | BC-10702 | 2023-12-20 | Compliance |
| SIG-94-MKW-LH8F | BC-10720 | 2023-10-23 | Data Governance |
| Elite Logistics Holdings | IC-10721 | 2023-01-14 | Data Governance |
| casein | TC-10725 | 2021-09-06 | Compliance |
| Sorbinsäure 99.5% | IC-10738 | 2022-10-22 | Supply Chain |
| SIG-50-BJQ-W54O Holdings | BC-10750 | 2021-12-19 | Supply Chain |
| HO-MA-854 | BC-10755 | 2021-06-14 | Product Management |
| SIG-22-DOP-7UDK | IC-10781 | 2024-07-07 | IT Infrastructure |
| Kaliumsorbat | TC-10785 | 2024-12-04 | IT Infrastructure |
| Vertex Distribution AG | TC-10790 | 2024-02-17 | IT Infrastructure |
| Ascorbic Acid 70% | IC-10793 | 2023-02-27 | Finance |
| SIG-52-CQW-KL19 | TC-10800 | 2024-01-20 | IT Infrastructure |
| vanguard enterprise | BC-10806 | 2023-09-10 | IT Infrastructure |
| Palm Oil | TC-10811 | 2021-07-10 | Product Management |
| Isoglucose | TC-10816 | 2024-12-03 | Finance |
| lactic acid | TC-10846 | 2022-08-22 | Supply Chain |
| PR-CH-808 AG | BC-10863 | 2021-10-06 | Product Management |
| continental enterprise GmbH | IC-10865 | 2022-02-05 | Compliance |
| vat standard in 5% | BC-10883 | 2022-02-27 | Supply Chain |
| Baltic Logistics | BC-10906 | 2024-02-17 | Product Management |
| IS-641 | BC-10924 | 2024-11-12 | Data Governance |
| Sodium Benzoate 98% Standard | BC-10944 | 2023-05-05 | Product Management |
| CO-MA-295 | BC-10948 | 2021-07-16 | Compliance |
| sodium chloride 98% standard | BC-11001 | 2022-02-22 | Supply Chain |
| Palm Oil 70% Pharma Grade | TC-11014 | 2023-06-21 | Supply Chain |
| SIG-39-MAR-LMVK | IC-11018 | 2021-03-23 | Compliance |
| SIG-43-NCZ-FT9Z | BC-11028 | 2022-12-04 | Data Governance |
| Cyclodextrin Food Grade | IC-11057 | 2021-10-07 | IT Infrastructure |
| SIG-20-XIG-T8ME | BC-11069 | 2024-04-02 | Product Management |
| SIG-92-FQX-S1BC | IC-11075 | 2023-05-19 | Operations |
| Continental Werkstoffe BV | IC-11092 | 2023-02-08 | Supply Chain |
| SIG-37-SOD-NFZK | IC-11107 | 2024-09-25 | Compliance |
| SIG-15-VIS-079C | IC-11113 | 2024-04-08 | Product Management |
| SIG-84-DSO-4S47 | TC-11139 | 2021-11-16 | Data Governance |
| Kasein 50% Premiumqualität | TC-11159 | 2024-11-05 | Product Management |
| Central Sourcing | IC-11166 | 2021-10-16 | Compliance |
| stratos sourcing | IC-11167 | 2023-10-13 | Compliance |
| nordic ingredients SARL | BC-11202 | 2021-06-15 | Supply Chain |
| RA-OI-98-ST-938 | TC-11205 | 2023-10-16 | Data Governance |
| SIG-74-EPP-R9AG | BC-11246 | 2024-12-23 | Compliance |
| PA-OI-410 | IC-11252 | 2021-01-23 | Supply Chain |
| resistant starch | BC-11255 | 2023-08-09 | Data Governance |
| global materials | IC-11272 | 2021-09-28 | Operations |
| SIG-37-ZOD-1VME | BC-11278 | 2023-12-10 | Supply Chain |
| casein standard | BC-11300 | 2021-07-16 | Compliance |
| CO-OI-50-PH-GR-568 | BC-11317 | 2024-01-25 | Finance |
| Pinnacle Vertrieb Ltd. | TC-11323 | 2022-01-18 | Operations |
| Fructose 70% | IC-11341 | 2023-06-18 | Operations |
| Cyclodextrin Qualitätsstufe I | IC-11347 | 2021-02-14 | Compliance |
| Apex Logistik | BC-11357 | 2023-02-11 | Supply Chain |
| premier sourcing | IC-11375 | 2022-12-02 | Operations |
| Prime Versorgung GmbH | TC-11377 | 2024-04-19 | Finance |
| GL-SU-CO-783 | TC-11379 | 2024-02-06 | Compliance |
| SIG-57-YOY-F7N2 | IC-11384 | 2022-05-24 | Finance |
| SIG-43-GRJ-P3HT | TC-11398 | 2021-02-15 | Operations |
| Customs Duty IN 25% | BC-11414 | 2024-05-10 | Operations |
| cyclodextrin premium | BC-11417 | 2024-04-11 | Data Governance |
| Atlas Sourcing | IC-11422 | 2024-01-15 | Finance |
| Dextrin Technische Qualität | IC-11444 | 2021-04-16 | Finance |
| SIG-98-JEQ-77GG | BC-11461 | 2024-11-19 | Finance |
| Lactic Acid | IC-11463 | 2024-01-16 | Data Governance |
| Global Werkstoffe | TC-11465 | 2021-08-07 | Supply Chain |
| CA-GR-B-950 | IC-11472 | 2023-09-25 | IT Infrastructure |
| Vat Standard NL 20% | IC-11485 | 2021-10-03 | IT Infrastructure |
| SIG-29-BZP-SU62 | BC-11503 | 2022-04-22 | IT Infrastructure |
| Natriumbenzoat Qualitätsstufe II | TC-11513 | 2022-07-17 | Supply Chain |
| Continental Chemicals Inc. | IC-11523 | 2023-12-08 | Operations |
| Global Werkstoffe | BC-11527 | 2021-06-05 | Data Governance |
| Customs Duty GB 0% | BC-11554 | 2023-06-20 | Supply Chain |
| Palmfett | TC-11555 | 2024-02-05 | IT Infrastructure |
| SIG-66-RQA-05UV | TC-11568 | 2023-02-27 | Data Governance |
| Premier Enterprise | IC-11573 | 2021-11-07 | Finance |
| SIG-98-OXJ-W0H6 SAS | IC-11576 | 2021-05-25 | Product Management |
| Palmfett | IC-11588 | 2024-02-24 | Operations |
| Maltodextrin DE20 | TC-11589 | 2022-05-18 | IT Infrastructure |
| Zitronensäure Pharmazeutisch rein | TC-11599 | 2024-02-10 | Product Management |
| Soy Isolate Standard | TC-11610 | 2024-05-02 | Operations |
| Dextrin 50% | IC-11616 | 2021-10-17 | Finance |
| lactic acid | TC-11650 | 2022-07-08 | Data Governance |
| vanguard materials | IC-11658 | 2022-11-12 | Finance |
| soy isolate | TC-11661 | 2022-07-12 | Finance |
| fructose tech grade | IC-11671 | 2022-08-09 | Compliance |
| SU-OI-TE-705 | BC-11709 | 2023-07-05 | Operations |
| Kaliumsorbat 98% Qualitätsstufe II | TC-11712 | 2024-02-22 | IT Infrastructure |
| calcium carbonate standard | BC-11717 | 2022-02-13 | Product Management |
| VA-TR-900 LLC | IC-11757 | 2021-09-08 | Data Governance |
| pea protein | IC-11774 | 2024-09-25 | Data Governance |
| Vat Standard BR 0% | IC-11794 | 2024-10-18 | Operations |
| Dextrose Food Grade | TC-11797 | 2024-10-16 | Supply Chain |
| lactic acid tech grade | BC-11802 | 2023-03-14 | Data Governance |
| Fructose | TC-11822 | 2024-03-19 | Compliance |
| SIG-51-EJL-Y9QB | IC-11826 | 2021-06-13 | Supply Chain |
| SIG-94-TOI-OFNK | TC-11836 | 2022-04-23 | Operations |
| SIG-48-YBV-ZD0Y | IC-11852 | 2022-04-23 | Product Management |
| Withholding US 5% | TC-11858 | 2021-04-12 | Data Governance |
| Sorbinsäure | IC-11873 | 2024-12-08 | Compliance |
| soy isolate food grade | TC-11880 | 2023-04-15 | Supply Chain |
| rapeseed oil 50% premium | BC-11887 | 2023-09-18 | Operations |
| Apex Logistics Inc. | IC-11889 | 2022-02-24 | Data Governance |
| baltic materials | BC-11915 | 2023-04-08 | Supply Chain |
| SO-IS-275 | BC-11920 | 2022-04-21 | Finance |
| SIG-45-ZZU-GRXH International | BC-11931 | 2024-08-11 | Compliance |
| Rapeseed Oil Grade B | IC-11945 | 2023-09-14 | Product Management |
| SIG-27-WVB-8FZQ | TC-11952 | 2022-02-17 | Compliance |
| SIG-26-ADB-B4F0 | TC-11955 | 2022-05-01 | Compliance |
| Premier Manufacturing NV | TC-11968 | 2022-01-01 | Supply Chain |
| SIG-74-HUK-JA04 | TC-11971 | 2024-05-08 | Operations |
| RE-ST-FO-GR-727 | TC-11973 | 2021-05-14 | Finance |
| Sodium Benzoate Grade B | IC-11984 | 2022-01-23 | Product Management |
| SIG-40-RSD-JF0U | TC-11988 | 2022-12-09 | Data Governance |
| NE-DI-240 Ltd. | BC-12002 | 2023-05-12 | Data Governance |
| Apex Logistik | TC-12007 | 2024-11-27 | Supply Chain |
| rapeseed oil 25% | BC-12030 | 2021-05-21 | Product Management |
| Sunflower Oil | BC-12034 | 2023-01-12 | Product Management |
| potassium sorbate | IC-12036 | 2022-12-08 | Operations |
| SIG-67-MJH-V4Q5 | TC-12043 | 2021-05-07 | Product Management |
| Atlas Ingredients Ltd. | TC-12063 | 2024-07-09 | IT Infrastructure |
| Sonnenblumenöl Qualitätsstufe I | TC-12098 | 2024-12-23 | Product Management |
| ST-TR-590 | TC-12099 | 2023-12-23 | Compliance |
| Soja Isolate | TC-12120 | 2024-04-11 | Operations |
| ME-SO-944 Inc. | IC-12167 | 2021-03-09 | Operations |
| Nordic Logistik | IC-12169 | 2021-02-02 | Product Management |
| Core Supply Co. | BC-12179 | 2024-02-04 | Data Governance |
| SIG-59-HNQ-A8N5 Ltd. | TC-12198 | 2021-02-07 | IT Infrastructure |
| SIG-97-PAD-AUZ7 | BC-12220 | 2023-07-10 | Product Management |
| SIG-43-FIP-49V7 | BC-12226 | 2021-08-06 | Compliance |
| PO-SO-768 | TC-12245 | 2021-07-18 | Product Management |
| Dextrin Premium | BC-12262 | 2023-07-17 | Data Governance |
| sorbic acid | IC-12281 | 2024-10-08 | Product Management |
| Lactic Acid Lebensmittelrein | BC-12284 | 2022-01-13 | Finance |
| elite solutions Holdings | TC-12311 | 2021-01-07 | IT Infrastructure |
| Vat Standard GB 19% | IC-12320 | 2023-09-20 | Compliance |
| Dextrose 25% Technical | TC-12327 | 2024-02-27 | Operations |
| Weizenklebereiweiß Qualitätsstufe I | TC-12361 | 2024-12-05 | Operations |
| Resistente Stärke | TC-12369 | 2021-11-19 | Supply Chain |
| Nordic Chemicals BV | BC-12390 | 2022-08-18 | Operations |
| SIG-47-HDT-7PPC | IC-12394 | 2021-11-22 | Finance |
| sorbic acid food grade | BC-12403 | 2024-03-20 | Finance |
| Casein Technical | TC-12419 | 2024-04-23 | Product Management |
| SIG-33-VWP-VX5U | IC-12424 | 2022-05-02 | Operations |
| SIG-88-RKE-8R7A | BC-12432 | 2024-05-07 | Compliance |
| Vertex Commodities | TC-12441 | 2024-08-09 | IT Infrastructure |
| Nordic Logistik | TC-12455 | 2023-07-24 | Compliance |
| customs duty fr 7% | TC-12472 | 2022-12-22 | Operations |
| Soja Isolate 25% | IC-12474 | 2024-02-03 | Product Management |
| Apex Sourcing | BC-12476 | 2022-03-22 | Supply Chain |
| apex trading | IC-12513 | 2021-10-24 | IT Infrastructure |
| core logistics | BC-12527 | 2021-05-17 | Operations |
| Coconut Oil 70% Qualitätsstufe I | TC-12529 | 2021-09-26 | Product Management |
| Rapeseed Oil 98% Standard | IC-12541 | 2021-12-06 | Supply Chain |
| casein 50% premium | IC-12542 | 2021-07-15 | Finance |
| PR-TR-294 | BC-12546 | 2022-05-18 | Finance |
| Soja Isolate | TC-12566 | 2023-06-09 | Data Governance |
| citric acid standard | IC-12570 | 2023-08-08 | Data Governance |
| soy isolate premium | TC-12579 | 2023-10-03 | Operations |
| citric acid standard | IC-12581 | 2021-07-06 | Data Governance |
| SIG-67-RMU-WA6Y | TC-12583 | 2023-04-14 | Data Governance |
| Resistente Stärke Qualitätsstufe II | TC-12589 | 2024-12-04 | Data Governance |
| SIG-91-FOC-36I6 | BC-12593 | 2024-03-25 | Data Governance |
| Fructose | IC-12598 | 2023-08-15 | IT Infrastructure |
| Soy Isolate 99.5% Premium | BC-12608 | 2023-03-18 | Compliance |
| WH-GL-ST-378 | TC-12610 | 2023-02-28 | Data Governance |
| soy isolate 50% | BC-12616 | 2022-10-01 | IT Infrastructure |
| SIG-34-UJK-TJA6 | BC-12628 | 2024-10-07 | Product Management |
| IS-PR-125 | BC-12655 | 2022-04-17 | Compliance |
| AS-AC-99.5-PR-761 | IC-12662 | 2022-11-21 | Operations |
| coconut oil | IC-12690 | 2024-10-03 | IT Infrastructure |
| Catalyst Ingredients Holdings | IC-12696 | 2022-07-16 | Operations |
| SIG-31-FGA-64VZ | IC-12699 | 2024-06-22 | Finance |
| VE-CH-841 Group | BC-12710 | 2023-06-26 | Data Governance |
| Prime Werkstoffe | TC-12717 | 2022-02-28 | Data Governance |
| Natriumchlorid 25% Premiumqualität | TC-12725 | 2021-03-17 | Data Governance |
| nexus sourcing | BC-12739 | 2022-05-20 | Operations |
| ascorbic acid standard | TC-12778 | 2021-01-21 | Operations |
| Central Manufacturing Holdings | TC-12782 | 2022-02-28 | Product Management |
| IS-FO-GR-555 | TC-12785 | 2024-02-21 | Product Management |
| SIG-66-AQR-B68Q | IC-12789 | 2021-01-16 | Supply Chain |
| lactic acid standard | BC-12828 | 2022-07-18 | Compliance |
| SIG-42-BEO-614U | TC-12830 | 2024-02-13 | IT Infrastructure |
| SIG-20-XSP-FVHF | IC-12835 | 2021-05-07 | Compliance |
| resistant starch 98% | BC-12841 | 2022-01-14 | Compliance |
| SIG-56-ZQV-YINP SA | IC-12847 | 2022-07-19 | Finance |
| Atlas Logistics International | BC-12871 | 2021-10-09 | Supply Chain |
| SIG-16-GRX-X3AK | BC-12881 | 2023-02-04 | Operations |
| Potassium Sorbate 50% | BC-12892 | 2023-07-01 | Operations |
| Central Logistik | BC-12897 | 2021-10-21 | Product Management |
| Pacific Vertrieb NV | TC-12907 | 2021-09-24 | Compliance |
| Excise DE 10% | IC-12919 | 2022-12-10 | Supply Chain |
| Dextrose Technical | BC-12923 | 2022-09-09 | Compliance |
| SIG-39-JMB-X1VA | IC-12925 | 2024-02-12 | Data Governance |
| ascorbic acid 99.5% standard | TC-12936 | 2024-09-03 | Compliance |
| SIG-94-TUN-H84G | IC-12942 | 2023-10-18 | Finance |
| SIG-78-QFN-H3BV | IC-12978 | 2024-01-03 | Operations |
| ST-DI-183 Inc. | IC-12979 | 2024-11-27 | Operations |
| SIG-91-XWQ-EANP | BC-12984 | 2023-11-28 | Product Management |
| Calcium Carbonate Qualitätsstufe II | BC-12985 | 2024-08-10 | Finance |
| SIG-80-QOK-BKBF | BC-12995 | 2022-08-09 | Supply Chain |
| resistant starch standard | IC-12999 | 2023-03-08 | Finance |
| SIG-83-HEH-XF50 | BC-13000 | 2024-10-20 | IT Infrastructure |
| Stellar Manufacturing SA | IC-13005 | 2021-06-03 | IT Infrastructure |
| isoglucose | IC-13008 | 2022-11-25 | IT Infrastructure |
| Resistant Starch Grade B | IC-13011 | 2021-01-09 | Product Management |
| Sodium Chloride 25% Premium | TC-13017 | 2023-08-16 | Supply Chain |
| apex supply | IC-13034 | 2023-12-08 | IT Infrastructure |
| Isoglucose | TC-13043 | 2021-11-16 | Finance |
| SU-OI-765 | IC-13058 | 2021-01-24 | IT Infrastructure |
| SIG-78-LTE-H4VL | TC-13082 | 2023-12-20 | Finance |
| global processing | TC-13118 | 2024-11-17 | Compliance |
| Sunflower Oil Grade B | TC-13120 | 2021-07-26 | Compliance |
| Vertex Logistik | TC-13149 | 2021-02-04 | IT Infrastructure |
| Glukosesirup Syrup 70% Lebensmittelrein | BC-13164 | 2023-05-08 | Compliance |
| VA-RE-N-7-243 | BC-13165 | 2022-03-05 | Product Management |
| dextrin standard | BC-13173 | 2023-05-18 | IT Infrastructure |
| customs duty nl 15% | IC-13186 | 2023-06-20 | Operations |
| SIG-23-NOR-OPI3 | TC-13202 | 2024-02-27 | Operations |
| Natriumchlorid 70% | IC-13206 | 2021-04-21 | Finance |
| Zenith Trading | TC-13208 | 2023-08-18 | IT Infrastructure |
| RE-ST-ST-946 | TC-13224 | 2024-11-09 | IT Infrastructure |
| SIG-84-VYG-QI55 | IC-13230 | 2023-12-06 | Data Governance |
| Ascorbic Acid Standardqualität | BC-13253 | 2024-12-10 | IT Infrastructure |
| SO-IS-275 | BC-13256 | 2024-05-25 | Finance |
| sodium benzoate | IC-13263 | 2023-08-10 | IT Infrastructure |
| SIG-91-GKA-MSWV | BC-13283 | 2022-03-24 | Product Management |
| Resistant Starch Technical | BC-13287 | 2022-09-19 | Compliance |
| Resistente Stärke | IC-13301 | 2022-02-10 | Finance |
| SIG-64-TCV-R5SR | IC-13303 | 2022-09-01 | Data Governance |
| Kasein Premiumqualität | TC-13327 | 2022-03-12 | Data Governance |
| Calcium Carbonate 99.5% | TC-13331 | 2023-08-19 | Data Governance |
| EX-I-0-103 | IC-13366 | 2021-04-26 | Finance |
| Sonnenblumenöl 70% | BC-13373 | 2024-09-20 | Compliance |
| SIG-35-HZD-3XBW | IC-13386 | 2022-08-14 | Operations |
| SIG-41-LTG-3D5I | IC-13393 | 2023-08-15 | Supply Chain |
| SIG-97-KNV-Q7J8 | BC-13422 | 2022-01-09 | Compliance |
| SIG-52-QOU-LC66 | IC-13435 | 2023-10-28 | Supply Chain |
| SIG-54-LIP-WKBS | IC-13439 | 2024-07-28 | Product Management |
| Natriumchlorid 25% Lebensmittelrein | TC-13460 | 2023-05-26 | Data Governance |
| Kaliumsorbat Standardqualität | IC-13479 | 2023-02-15 | Data Governance |
| SIG-36-FSA-X73Q | IC-13505 | 2021-10-21 | Product Management |
| Palm Oil 98% | BC-13519 | 2024-01-09 | Product Management |
| Zenith Sourcing | BC-13526 | 2021-07-17 | Finance |
| RE-ST-70-901 | BC-13542 | 2024-11-12 | Supply Chain |
| NE-DI-555 Corp. | IC-13552 | 2023-10-16 | Product Management |
| continental enterprise International | IC-13558 | 2024-02-09 | Data Governance |
| ST-CO-650 International | IC-13569 | 2022-08-25 | Compliance |
| prime logistics | IC-13585 | 2024-08-03 | Operations |
| Palmfett | BC-13588 | 2023-10-26 | Operations |
| SIG-85-SQB-MODP BV | TC-13595 | 2024-09-28 | Operations |
| Atlas Sourcing | TC-13605 | 2024-05-06 | Finance |
| VE-DI-139 KG | BC-13608 | 2022-04-27 | IT Infrastructure |
| Sunflower Oil Grade B | BC-13611 | 2021-11-22 | Data Governance |
| WH-GL-GR-B-660 | BC-13616 | 2023-10-28 | IT Infrastructure |
| Natriumbenzoat 70% Premiumqualität | IC-13617 | 2021-04-10 | Operations |
| Fructose 50% Standardqualität | BC-13640 | 2021-01-13 | Compliance |
| SIG-52-JLE-5KJF SAS | BC-13655 | 2021-04-02 | Product Management |
| SIG-12-NAY-4AKW | IC-13702 | 2021-03-19 | Product Management |
| resistant starch 70% food grade | TC-13712 | 2021-09-02 | Data Governance |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | BC-13715 | 2023-05-20 | Finance |
| Potassium Sorbate | TC-13718 | 2022-06-07 | IT Infrastructure |
| AT-IN-716 Corp. | BC-13725 | 2024-05-13 | Operations |
| BA-LO-814 SAS | BC-13730 | 2022-01-27 | Supply Chain |
| Lactic Acid Food Grade | BC-13745 | 2024-08-06 | Data Governance |
| Stratos Logistics | TC-13770 | 2021-05-22 | Product Management |
| PA-OI-ST-879 | IC-13784 | 2023-08-05 | IT Infrastructure |
| SIG-82-DVA-0TXE | TC-13790 | 2021-07-01 | Operations |
| FR-99.5-GR-A-438 | BC-13794 | 2023-11-09 | Supply Chain |
| SIG-78-WKT-9TDY SAS | TC-13822 | 2022-01-24 | Product Management |
| AT-IN-716 Corp. | BC-13836 | 2022-01-11 | Supply Chain |
| Kasein 98% Qualitätsstufe II | IC-13851 | 2024-11-28 | Supply Chain |
| SIG-61-MHS-BQG3 | TC-13853 | 2021-01-05 | Product Management |
| premier logistics | IC-13860 | 2024-11-07 | Finance |
| SIG-30-UET-0Q2O | IC-13866 | 2024-11-08 | Finance |
| AT-LO-628 | IC-13871 | 2023-06-25 | Compliance |
| SIG-44-LEF-PDJN SARL | IC-13899 | 2021-07-20 | Supply Chain |
| catalyst sourcing | TC-13909 | 2024-08-12 | Data Governance |
| Dextrin Pharma Grade | BC-13917 | 2022-06-27 | Compliance |
| Natriumbenzoat Qualitätsstufe I | IC-13950 | 2022-10-11 | Operations |
| SIG-35-IQA-J92D | TC-13958 | 2023-12-15 | Finance |
| Catalyst Logistik | IC-13961 | 2022-05-20 | Data Governance |
| SO-AC-GR-A-997 | TC-13964 | 2024-09-12 | IT Infrastructure |
| nexus sourcing | BC-13975 | 2023-07-24 | Data Governance |
| Central Werkstoffe | BC-13999 | 2021-07-08 | Operations |
| SIG-96-DUH-99Q6 | BC-14018 | 2022-04-04 | Operations |
| vanguard logistics | TC-14022 | 2023-02-17 | Supply Chain |
| WI-F-15-675 | IC-14030 | 2022-07-13 | Supply Chain |
| AT-LO-568 SA | BC-14058 | 2022-06-10 | Data Governance |
| vat reduced in 5% | IC-14063 | 2024-06-02 | Operations |
| pacific industries | IC-14087 | 2024-02-28 | Supply Chain |
| lactic acid 70% pharma grade | BC-14092 | 2022-05-09 | Operations |
| DE-25-TE-949 | IC-14104 | 2023-05-04 | Product Management |
| Rapsöl 98% | TC-14107 | 2022-11-27 | Operations |
| Sodium Benzoate 50% | IC-14113 | 2022-04-03 | Product Management |
| Lactic Acid Lebensmittelrein | IC-14120 | 2024-09-15 | Operations |
| elite materials | BC-14167 | 2024-07-22 | Finance |
| casein 70% tech grade | TC-14172 | 2021-06-05 | IT Infrastructure |
| SIG-79-IWJ-YNSA | TC-14181 | 2023-10-23 | IT Infrastructure |
| SIG-80-MXD-T81P | BC-14182 | 2023-04-26 | Product Management |
| Prism Logistics | IC-14187 | 2022-03-15 | Operations |
| Kaliumsorbat Technische Qualität | TC-14202 | 2023-02-18 | Product Management |
| Pea Protein 98% Qualitätsstufe II | BC-14235 | 2024-05-06 | Supply Chain |
| PA-OI-25-GR-A-241 | TC-14248 | 2024-03-15 | Finance |
| pea protein | TC-14254 | 2023-04-09 | IT Infrastructure |
| Elite Werkstoffe | IC-14264 | 2023-06-07 | Finance |
| SIG-51-DNC-4AET | IC-14288 | 2022-10-01 | Supply Chain |
| zenith logistics | BC-14296 | 2021-04-16 | IT Infrastructure |
| SIG-94-TOI-OFNK | IC-14298 | 2024-05-16 | Supply Chain |
| Calcium Carbonate | IC-14300 | 2023-11-22 | Product Management |
| lactic acid tech grade | BC-14316 | 2023-07-19 | Data Governance |
| SIG-39-DJJ-3SY8 | IC-14324 | 2023-02-13 | Supply Chain |
| Wheat Gluten | TC-14331 | 2023-07-19 | Finance |
| coconut oil 25% standard | TC-14335 | 2023-06-25 | Product Management |
| CU-DU-N-25-811 | BC-14338 | 2021-09-09 | Finance |
| continental commodities | IC-14344 | 2023-06-24 | Supply Chain |
| sorbic acid premium | BC-14347 | 2023-06-08 | Compliance |
| Nexus Sourcing | BC-14360 | 2024-05-17 | Finance |
| Cyclodextrin Standard | TC-14361 | 2023-01-03 | Finance |
| casein standard | TC-14388 | 2024-08-28 | Operations |
| Pacific Werkstoffe | BC-14400 | 2022-10-26 | Compliance |
| Pacific Vertrieb International | BC-14424 | 2024-05-22 | Supply Chain |
| Stellar Partners AG | TC-14433 | 2024-05-21 | IT Infrastructure |
| Ascorbic Acid Standardqualität | TC-14445 | 2024-03-21 | IT Infrastructure |
| Isoglucose 70% Food Grade | BC-14496 | 2021-01-01 | Compliance |
| sodium benzoate 25% | TC-14501 | 2022-12-16 | Product Management |
| nordic logistics Group | TC-14505 | 2024-02-01 | Supply Chain |
| Natriumbenzoat Qualitätsstufe I | TC-14513 | 2022-03-18 | Compliance |
| Continental Ingredients | IC-14520 | 2021-01-22 | Operations |
| CU-DU-D-20-742 | TC-14541 | 2024-09-15 | IT Infrastructure |
| SIG-69-OFZ-JW34 | IC-14572 | 2024-01-03 | Supply Chain |
| soy isolate 50% premium | TC-14582 | 2024-03-05 | Supply Chain |
| Customs Duty BR 21% | TC-14589 | 2023-12-11 | Operations |
| Vat Reduced NL 5% | TC-14593 | 2024-08-03 | Operations |
| SIG-53-MEZ-6IT1 | IC-14603 | 2024-01-07 | Product Management |
| SIG-43-OLC-OFCX | BC-14611 | 2024-07-28 | Operations |
| SIG-74-ZNA-1VYW | TC-14615 | 2022-02-18 | Data Governance |
| QU-MA-886 | TC-14623 | 2023-09-06 | Supply Chain |
| Citric Acid Food Grade | BC-14626 | 2023-10-27 | Data Governance |
| SIG-68-BSO-NW8J Group | TC-14633 | 2021-11-19 | Supply Chain |
| PR-IN-608 BV | IC-14640 | 2024-11-28 | Product Management |
| SIG-62-KTK-XM5L Holdings | TC-14668 | 2023-01-12 | Product Management |
| SO-BE-113 | BC-14684 | 2023-02-10 | Product Management |
| resistant starch standard | BC-14685 | 2024-12-16 | Operations |
| CU-DU-N-25-811 | IC-14702 | 2022-03-23 | Compliance |
| Pea Protein Premium | IC-14709 | 2024-05-26 | Product Management |
| Pea Protein Premiumqualität | BC-14711 | 2023-03-21 | Operations |
| Atlantic Werkstoffe | IC-14726 | 2024-12-22 | IT Infrastructure |
| Citric Acid | IC-14748 | 2024-03-20 | Finance |
| Core Rohstoffe NV | BC-14761 | 2022-01-25 | Data Governance |
| Natriumbenzoat | BC-14766 | 2023-10-10 | Supply Chain |
| SIG-56-NOU-ZR98 | IC-14773 | 2023-03-04 | Operations |
| Excise GB 5% | TC-14775 | 2022-02-14 | Finance |
| coconut oil 25% tech grade | BC-14786 | 2021-02-16 | Data Governance |
| Lactic Acid Food Grade | TC-14791 | 2022-11-16 | Operations |
| fructose 99.5% premium | TC-14814 | 2023-09-16 | IT Infrastructure |
| Soy Isolate 50% Grade B | BC-14820 | 2022-08-15 | Compliance |
| SIG-80-ZKZ-ANXJ | BC-14822 | 2022-10-12 | Finance |
| Dextrin Technische Qualität | TC-14823 | 2024-09-19 | Operations |
| RE-ST-ST-946 | TC-14825 | 2024-01-23 | IT Infrastructure |
| SIG-92-SMV-JF74 | IC-14857 | 2021-08-06 | Supply Chain |
| coconut oil food grade | TC-14864 | 2021-12-11 | IT Infrastructure |
| IS-GR-B-640 | IC-14866 | 2024-05-05 | Supply Chain |
| DE-70-512 | IC-14871 | 2023-05-28 | Operations |
| Soja Isolate Lebensmittelrein | IC-14875 | 2022-08-17 | Finance |
| vat standard br 0% | IC-14948 | 2024-04-17 | Product Management |
| Vertex Logistics | TC-14953 | 2024-06-11 | Data Governance |
| Rapeseed Oil Pharma Grade | IC-14964 | 2023-09-28 | Compliance |
| Weizenklebereiweiß | TC-14969 | 2023-03-04 | Compliance |
| Pinnacle Materials | IC-14970 | 2024-03-10 | Data Governance |
| PA-OI-70-780 | BC-14985 | 2024-08-17 | Supply Chain |
| FR-ST-953 | TC-14996 | 2022-07-18 | Supply Chain |
| CU-DU-D-20-742 | BC-14999 | 2023-11-01 | Operations |
| ST-PA-980 | TC-15015 | 2022-02-08 | IT Infrastructure |
| SIG-41-YLB-IZED | BC-15028 | 2023-12-21 | Product Management |
| SIG-88-RGQ-WZOI | IC-15037 | 2021-09-26 | Product Management |
| AT-IN-931 | IC-15040 | 2021-06-21 | IT Infrastructure |
| Catalyst Materials | TC-15066 | 2021-09-06 | Data Governance |
| SIG-64-LXA-3LJO | BC-15067 | 2022-06-24 | Compliance |
| Vertex Versorgung GmbH | IC-15077 | 2023-12-09 | Supply Chain |
| Pea Protein Premiumqualität | BC-15089 | 2021-08-28 | Data Governance |
| SIG-87-QRK-668S | IC-15098 | 2022-12-08 | Compliance |
| SIG-30-JDQ-UNB9 Holdings | BC-15102 | 2021-03-16 | Supply Chain |
| PA-OI-GR-B-224 | TC-15114 | 2022-04-04 | Supply Chain |
| DE-GR-B-942 | BC-15127 | 2021-07-17 | Compliance |
| PO-SO-202 | IC-15139 | 2022-02-06 | Finance |
| vertex ingredients KG | BC-15150 | 2023-03-02 | Operations |
| Dextrose | BC-15165 | 2023-01-05 | Supply Chain |
| SO-AC-25-GR-B-198 | TC-15172 | 2022-07-03 | Supply Chain |
| Vat Standardqualität IN 10% | TC-15174 | 2024-05-12 | Operations |
| SIG-97-XJT-7TBU | BC-15178 | 2022-02-02 | Product Management |
| meridian chemicals Holdings | IC-15191 | 2022-03-24 | IT Infrastructure |
| SIG-47-TCL-S6FG | IC-15201 | 2023-09-22 | IT Infrastructure |
| SIG-86-JBA-HCDI | IC-15203 | 2022-02-09 | Supply Chain |
| baltic supply | IC-15205 | 2024-06-22 | Compliance |
| Core Rohstoffe NV | IC-15209 | 2021-05-05 | Compliance |
| PE-PR-746 | IC-15243 | 2022-04-20 | Compliance |
| SIG-24-YWL-8DWF | IC-15258 | 2021-10-04 | IT Infrastructure |
| Sorbinsäure | TC-15287 | 2021-06-14 | IT Infrastructure |
| Soy Isolate 50% Grade B | IC-15317 | 2024-01-02 | Finance |
| VA-IN-954 PLC | BC-15367 | 2024-03-14 | Supply Chain |
| Cyclodextrin Standard | TC-15380 | 2022-05-12 | Data Governance |
| glucose syrup | TC-15405 | 2023-08-18 | Product Management |
| excise cn 19% | IC-15415 | 2021-01-06 | Operations |
| LA-AC-393 | IC-15452 | 2023-01-15 | Finance |
| Calcium Carbonate 98% | TC-15454 | 2022-02-20 | Compliance |
| PO-SO-202 | TC-15459 | 2024-09-20 | Product Management |
| Nordic Logistics | IC-15465 | 2024-02-23 | Data Governance |
| Glucose Syrup Technical | IC-15467 | 2023-06-13 | IT Infrastructure |
| SO-IS-FO-GR-437 | IC-15484 | 2024-12-05 | Finance |
| citric acid | BC-15486 | 2022-06-04 | Data Governance |
| SIG-59-EWO-HAXW | IC-15492 | 2022-09-25 | IT Infrastructure |
| sunflower oil 50% pharma grade | BC-15494 | 2021-04-05 | Supply Chain |
| SIG-31-IKO-T2D8 | TC-15514 | 2022-03-14 | Operations |
| Sunflower Oil Grade A | IC-15521 | 2022-01-18 | Product Management |
| Glukosesirup Syrup Lebensmittelrein | BC-15542 | 2023-01-26 | Compliance |
| Pacific Materials KG | IC-15552 | 2023-12-25 | Supply Chain |
| Meridian Materials | IC-15577 | 2022-01-12 | Supply Chain |
| Sonnenblumenöl 70% Lebensmittelrein | BC-15584 | 2022-10-25 | IT Infrastructure |
| SIG-51-KQC-QY9M | BC-15593 | 2024-02-20 | IT Infrastructure |
| SIG-61-IQH-EKWH | IC-15614 | 2021-01-01 | Supply Chain |
| Calcium Carbonate 98% Standard | IC-15628 | 2021-03-12 | Operations |
| Weizenklebereiweiß 99.5% | IC-15645 | 2024-01-04 | Supply Chain |
| sorbic acid 98% | BC-15648 | 2024-10-16 | Product Management |
| Prism Materials Ltd. | TC-15672 | 2021-06-26 | Supply Chain |
| pea protein 98% standard | IC-15685 | 2024-11-16 | Supply Chain |
| palm oil | BC-15700 | 2024-07-23 | Data Governance |
| vat standard nl 5% | BC-15745 | 2024-04-06 | Finance |
| Withholding NL 21% | IC-15755 | 2021-02-03 | IT Infrastructure |
| AT-IN-716 Corp. | BC-15765 | 2021-11-01 | Operations |
| LA-AC-25-PR-377 | IC-15767 | 2023-08-14 | Operations |
| soy isolate pharma grade | TC-15775 | 2024-06-06 | Compliance |
| SIG-14-MDA-Y0XA | IC-15779 | 2021-09-06 | Product Management |
| potassium sorbate | TC-15780 | 2022-10-12 | Product Management |
| FR-99.5-PH-GR-378 | IC-15801 | 2024-12-27 | Product Management |
| PR-MA-686 | TC-15808 | 2021-12-15 | Finance |
| CA-CO-939 | IC-15810 | 2024-06-27 | Operations |
| NE-PR-315 Holdings | BC-15817 | 2021-01-25 | IT Infrastructure |
| Quantum Processing Ltd. | BC-15822 | 2024-07-01 | Operations |
| withholding nl 20% | BC-15837 | 2024-08-06 | IT Infrastructure |
| Catalyst Supply Holdings | BC-15853 | 2023-03-16 | Data Governance |
| BA-MA-943 | TC-15857 | 2023-06-18 | Supply Chain |
| Rapeseed Oil Technical | BC-15863 | 2023-04-08 | Data Governance |
| SU-OI-98-462 | BC-15877 | 2021-11-03 | IT Infrastructure |
| potassium sorbate food grade | TC-15891 | 2021-05-02 | Supply Chain |
| meridian supply | TC-15898 | 2023-10-26 | Compliance |
| citric acid 99.5% pharma grade | IC-15905 | 2021-02-18 | Data Governance |
| SIG-78-OGT-WEKQ | BC-15916 | 2022-07-05 | Operations |
| Natriumbenzoat | IC-15949 | 2024-11-16 | Compliance |
| Sodium Benzoate 50% Technical | TC-15962 | 2021-06-23 | IT Infrastructure |
| central logistics International | IC-15978 | 2022-09-09 | Supply Chain |
| Casein 98% Grade B | IC-15997 | 2024-10-06 | Operations |
| SIG-79-HZP-CLBR | TC-16057 | 2021-08-26 | Data Governance |
| SIG-62-GUN-FTYL | IC-16073 | 2023-03-09 | Operations |
| customs duty fr 25% | BC-16080 | 2023-11-03 | IT Infrastructure |
| Vat Reduced CN 5% | BC-16091 | 2024-08-23 | Compliance |
| Vanguard Vertrieb | TC-16095 | 2023-12-16 | Product Management |
| Vertex Chemicals Holdings | IC-16102 | 2022-02-28 | Supply Chain |
| Isoglucose 25% Standard | IC-16120 | 2024-07-20 | Supply Chain |
| SIG-73-GRJ-1VRU | BC-16126 | 2022-04-07 | Data Governance |
| Calcium Carbonate | BC-16136 | 2023-09-19 | Data Governance |
| CA-MA-370 | BC-16138 | 2023-09-09 | IT Infrastructure |
| Traubenzucker Qualitätsstufe I | TC-16166 | 2022-11-14 | Operations |
| Prime Supply Co. | TC-16171 | 2023-05-16 | Operations |
| Lactic Acid | TC-16176 | 2022-04-02 | Compliance |
| Sorbic Acid Grade B | TC-16179 | 2022-02-15 | Supply Chain |
| nexus materials | IC-16182 | 2022-03-12 | Supply Chain |
| PA-OI-25-GR-A-241 | TC-16207 | 2023-06-10 | IT Infrastructure |
| dextrose | BC-16237 | 2023-05-19 | Compliance |
| SIG-87-YFT-P51V | BC-16247 | 2023-12-23 | Data Governance |
| sodium benzoate 99.5% premium | TC-16256 | 2024-08-08 | Data Governance |
| Withholding BR 10% | TC-16267 | 2022-01-04 | Data Governance |
| Natriumbenzoat Qualitätsstufe I | IC-16271 | 2021-08-03 | Data Governance |
| Vertex Versorgung GmbH | BC-16314 | 2023-11-25 | Compliance |
| SIG-27-NTH-I37Y | BC-16325 | 2021-05-11 | Operations |
| Traubenzucker 25% Technische Qualität | TC-16326 | 2023-12-22 | Product Management |
| CU-DU-U-15-275 | BC-16346 | 2023-10-03 | Data Governance |
| rapeseed oil | TC-16381 | 2023-06-26 | Operations |
| SIG-10-BLC-3L38 | TC-16383 | 2022-11-22 | Supply Chain |
| Atlas Trading SA | BC-16385 | 2022-04-06 | Product Management |
| Prism Ingredients | IC-16413 | 2021-12-24 | Supply Chain |
| SIG-51-HLJ-TN1E | TC-16424 | 2021-09-08 | Product Management |
| SIG-74-AEB-PMX7 | IC-16433 | 2024-05-17 | IT Infrastructure |
| SIG-60-WYC-NAXS | BC-16440 | 2024-05-19 | Operations |
| withholding nl 19% | BC-16443 | 2024-08-06 | Supply Chain |
| WI-N-15-362 | IC-16462 | 2024-08-03 | Product Management |
| IS-50-FO-GR-562 | TC-16464 | 2022-03-12 | IT Infrastructure |
| glucose syrup 98% food grade | BC-16467 | 2023-06-22 | Compliance |
| SIG-86-QTB-N3VO International | TC-16494 | 2024-01-05 | IT Infrastructure |
| stratos logistics | IC-16535 | 2022-02-06 | Product Management |
| cyclodextrin premium | TC-16548 | 2021-04-14 | IT Infrastructure |
| Ascorbic Acid Qualitätsstufe II | TC-16550 | 2022-02-02 | Data Governance |
| CY-TE-117 | IC-16577 | 2024-03-21 | Product Management |
| SIG-20-BPG-W8VL | IC-16617 | 2024-12-17 | Compliance |
| customs duty de 20% | TC-16623 | 2023-11-26 | IT Infrastructure |
| Natriumbenzoat | IC-16631 | 2021-04-09 | Data Governance |
| WH-GL-99.5-557 | IC-16640 | 2024-03-04 | Supply Chain |
| vat reduced cn 21% | TC-16644 | 2024-09-03 | Supply Chain |
| SIG-26-EJV-LZ44 | BC-16646 | 2022-09-27 | IT Infrastructure |
| SIG-25-VPE-TOC1 | TC-16652 | 2024-03-12 | Product Management |
| palm oil 98% | BC-16656 | 2024-08-19 | Operations |
| DE-70-769 | TC-16673 | 2023-12-10 | Operations |
| AT-MA-363 | IC-16717 | 2021-02-07 | IT Infrastructure |
| SIG-47-LBV-Y27V | BC-16719 | 2022-11-07 | Supply Chain |
| SIG-30-MCM-OXZ5 | BC-16730 | 2023-07-07 | Finance |
| SIG-36-BVE-5U7D | BC-16789 | 2021-07-07 | Supply Chain |
| SIG-45-ZTJ-PA16 | IC-16797 | 2023-01-02 | Supply Chain |
| Atlantic Versorgung LLC | BC-16805 | 2024-05-07 | IT Infrastructure |
| Dextrin | IC-16829 | 2021-07-05 | Finance |
| Elite Sourcing | TC-16835 | 2024-11-25 | Operations |
| Atlantic Ingredients Holdings | TC-16848 | 2024-02-09 | Operations |
| pea protein 70% premium | TC-16850 | 2021-08-07 | Finance |
| SO-CH-185 | BC-16863 | 2024-03-09 | Finance |
| Soja Isolate 50% Qualitätsstufe II | TC-16871 | 2024-07-25 | Finance |
| Calcium Carbonate Standardqualität | BC-16879 | 2023-03-06 | IT Infrastructure |
| SO-IS-98-880 | TC-16886 | 2021-03-20 | Finance |
| Calcium Carbonate 70% Premium | BC-16891 | 2024-09-22 | Supply Chain |
| Traubenzucker 50% Qualitätsstufe II | TC-16908 | 2021-12-15 | Data Governance |
| rapeseed oil 99.5% | BC-16930 | 2022-01-16 | Compliance |
| Apex Verarbeitung | BC-16931 | 2024-06-26 | Product Management |
| Dextrose 25% Technical | IC-16953 | 2023-08-08 | Supply Chain |
| FR-113 | TC-16969 | 2024-09-19 | Product Management |
| VA-LO-248 | TC-17004 | 2023-11-09 | Data Governance |
| Vat Reduced BR 15% | IC-17043 | 2023-05-12 | Compliance |
| central manufacturing NV | TC-17044 | 2023-10-15 | Operations |
| horizon partners Ltd. | TC-17049 | 2022-07-01 | IT Infrastructure |
| CE-MA-931 | TC-17050 | 2023-02-20 | Finance |
| Maltodextrin DE20 | TC-17079 | 2021-07-13 | Supply Chain |
| Pinnacle Materials SA | IC-17083 | 2023-08-17 | Compliance |
| lactic acid | BC-17088 | 2021-02-14 | Data Governance |
| Catalyst Commodities SAS | TC-17089 | 2022-04-21 | IT Infrastructure |
| Kaliumsorbat | IC-17094 | 2023-11-23 | Operations |
| Nordic Versorgung GmbH | TC-17102 | 2023-12-18 | Data Governance |
| prime chemicals KG | TC-17105 | 2023-05-02 | Compliance |
| VE-LO-864 | BC-17106 | 2024-05-24 | Product Management |
| Coconut Oil 70% | TC-17115 | 2023-12-24 | Operations |
| Ascorbic Acid Standardqualität | BC-17117 | 2024-01-04 | Data Governance |
| SIG-13-CGO-2Y4L | TC-17119 | 2022-12-10 | Data Governance |
| Coconut Oil 98% Grade A | TC-17120 | 2022-05-09 | Compliance |
| Lactic Acid | IC-17124 | 2024-09-17 | Supply Chain |
| Wheat Gluten 25% Standard | TC-17127 | 2024-03-24 | Data Governance |
| LA-AC-25-PR-377 | IC-17150 | 2023-09-04 | Finance |
| Casein Grade B | BC-17151 | 2024-02-17 | Product Management |
| vertex logistics Holdings | TC-17152 | 2021-07-03 | Compliance |
| VE-SO-576 | IC-17156 | 2022-03-17 | Finance |
| SU-OI-TE-879 | TC-17159 | 2023-02-07 | Finance |
| Glukosesirup Syrup | BC-17165 | 2021-08-01 | IT Infrastructure |
| Baltic Commodities Inc. | BC-17167 | 2024-09-19 | IT Infrastructure |
| SIG-21-UJY-RKOF | BC-17175 | 2021-11-18 | Product Management |
| SIG-12-IYC-8W63 Holdings | TC-17180 | 2022-02-22 | Compliance |
| Prism Logistik | BC-17196 | 2023-01-04 | Product Management |
| Quantum Partners | BC-17209 | 2022-03-24 | Operations |
| Baltic Industrien PLC | IC-17234 | 2022-08-10 | Compliance |
| Premier Partners SARL | IC-17250 | 2021-04-19 | Data Governance |
| AP-SU-CO-755 | IC-17280 | 2021-09-17 | Finance |
| SIG-38-ZZL-D5F0 | IC-17294 | 2023-01-09 | Compliance |
| Zenith Supply Co. | BC-17311 | 2023-12-13 | Operations |
| Meridian Sourcing | BC-17315 | 2021-06-16 | Finance |
| sodium benzoate | BC-17322 | 2024-08-14 | Operations |
| SO-BE-708 | BC-17326 | 2022-10-12 | IT Infrastructure |
| Sonnenblumenöl 50% Qualitätsstufe I | IC-17337 | 2022-07-14 | Data Governance |
| atlas materials | TC-17342 | 2022-06-15 | Data Governance |
| fructose standard | BC-17359 | 2023-10-20 | IT Infrastructure |
| Rapsöl Qualitätsstufe I | TC-17363 | 2024-06-20 | Product Management |
| SIG-51-EJL-Y9QB | BC-17370 | 2023-12-07 | Compliance |
| SIG-76-GDP-2JN8 | BC-17388 | 2022-07-11 | Supply Chain |
| Potassium Sorbate Standard | BC-17392 | 2021-07-25 | Compliance |
| Vat Reduced US 19% | TC-17402 | 2021-09-20 | Supply Chain |
| Stellar Versorgung GmbH | IC-17414 | 2023-02-16 | Finance |
| vat standard cn 19% | BC-17417 | 2021-08-01 | IT Infrastructure |
| Rapeseed Oil 70% Technical | IC-17440 | 2021-01-10 | Supply Chain |
| SIG-36-WFS-RS21 | IC-17452 | 2022-02-10 | Supply Chain |
| SIG-99-CEZ-35MR | IC-17469 | 2022-11-23 | Compliance |
| ascorbic acid food grade | BC-17485 | 2023-06-15 | IT Infrastructure |
| CE-LO-195 | IC-17493 | 2023-09-05 | Data Governance |
| Pea Protein | IC-17511 | 2022-04-14 | Operations |
| Palm Oil 70% Pharma Grade | TC-17517 | 2024-10-17 | Data Governance |
| CU-DU-F-15-864 | TC-17559 | 2022-04-24 | Compliance |
| Sunflower Oil Grade B | IC-17584 | 2022-07-13 | Data Governance |
| SIG-32-ETO-4DT1 | BC-17612 | 2022-09-09 | Compliance |
| BA-SO-682 International | IC-17620 | 2023-12-18 | Finance |
| coconut oil standard | BC-17630 | 2024-08-23 | Product Management |
| SIG-40-RSD-JF0U | IC-17647 | 2023-02-20 | Operations |
| Withholding NL 20% | BC-17648 | 2021-06-23 | Operations |
| Premier Solutions LLC | IC-17661 | 2021-08-23 | Product Management |
| SIG-47-LPF-7QXJ | BC-17662 | 2024-09-14 | Data Governance |
| nordic ingredients SARL | BC-17663 | 2022-10-08 | IT Infrastructure |
| SIG-69-MNI-DH5B | BC-17664 | 2023-05-12 | IT Infrastructure |
| ascorbic acid | TC-17676 | 2023-01-13 | Compliance |
| Potassium Sorbate 50% Grade B | TC-17677 | 2021-03-25 | Supply Chain |
| Elite Sourcing | TC-17685 | 2024-03-26 | Finance |
| Dextrin 70% | IC-17689 | 2023-01-08 | Compliance |
| Dextrose Grade B | TC-17704 | 2022-05-14 | Finance |
| SIG-95-APX-PWFS | BC-17737 | 2021-05-07 | Finance |
| calcium carbonate pharma grade | IC-17741 | 2021-06-04 | Operations |
| SIG-86-JBA-HCDI | BC-17756 | 2021-03-10 | Data Governance |
| Zenith Manufacturing Holdings | TC-17763 | 2023-03-05 | Data Governance |
| Sorbic Acid 70% | IC-17804 | 2021-08-08 | Product Management |
| ascorbic acid | BC-17808 | 2023-07-26 | Data Governance |
| Sodium Benzoate 99.5% Technical | IC-17832 | 2021-09-20 | IT Infrastructure |
| Customs Duty GB 7% | BC-17841 | 2023-03-18 | Operations |
| Lactic Acid Standard | IC-17874 | 2024-06-25 | Supply Chain |
| WI-F-5-977 | IC-17876 | 2024-11-27 | Data Governance |
| Customs Duty IN 5% | IC-17885 | 2022-08-18 | Data Governance |
| Maltodextrin DE10 | IC-17907 | 2021-01-12 | Data Governance |
| Vat Reduced IN 20% | BC-17916 | 2022-02-22 | Product Management |
| Pea Protein 99.5% Premiumqualität | TC-17924 | 2021-09-16 | IT Infrastructure |
| Sodium Chloride Premium | BC-17933 | 2022-02-08 | Product Management |
| horizon partners Ltd. | BC-17940 | 2021-08-15 | Data Governance |
| SIG-37-ZOD-1VME | BC-17989 | 2023-10-23 | IT Infrastructure |
| Rapeseed Oil Technical | TC-17999 | 2022-01-03 | Supply Chain |
| SIG-70-YLY-65JU PLC | BC-18023 | 2022-11-16 | Operations |
| QU-LO-363 | BC-18030 | 2024-09-03 | Operations |
| Citric Acid | IC-18039 | 2021-12-02 | Compliance |
| sodium benzoate 50% | TC-18045 | 2021-05-03 | IT Infrastructure |
| ascorbic acid premium | IC-18050 | 2022-09-17 | Operations |
| SIG-10-HXN-BKWJ | IC-18059 | 2023-05-03 | Product Management |
| PA-MA-435 | IC-18069 | 2022-03-08 | Finance |
| Cyclodextrin 98% Pharmazeutisch rein | BC-18112 | 2024-05-05 | Supply Chain |
| Traubenzucker 99.5% Qualitätsstufe II | BC-18128 | 2024-06-01 | Operations |
| Casein 98% Technical | BC-18130 | 2023-10-09 | Supply Chain |
| cyclodextrin | BC-18137 | 2022-01-25 | Supply Chain |
| Nexus Enterprise BV | BC-18139 | 2021-12-11 | Operations |
| Rapeseed Oil | BC-18141 | 2021-02-20 | Finance |
| SIG-80-JPG-N6YV SA | IC-18145 | 2022-12-13 | Product Management |
| ST-MA-148 SAS | TC-18162 | 2022-02-12 | Product Management |
| Glukosesirup Syrup | TC-18174 | 2022-08-19 | Product Management |
| SIG-62-DCP-L2AF | BC-18179 | 2024-05-25 | Data Governance |
| coconut oil standard | BC-18191 | 2024-11-06 | Product Management |
| rapeseed oil 98% | TC-18202 | 2023-01-17 | Data Governance |
| Vat Standard US 15% | IC-18211 | 2023-07-01 | Compliance |
| BA-SO-139 | TC-18230 | 2021-09-15 | Finance |
| Prime Ingredients NV | IC-18234 | 2024-07-21 | IT Infrastructure |
| Fructose | IC-18250 | 2021-04-25 | Supply Chain |
| Sodium Benzoate Pharma Grade | TC-18292 | 2023-05-27 | Data Governance |
| pinnacle industries KG | BC-18328 | 2022-03-28 | Product Management |
| Resistant Starch Premium | IC-18336 | 2024-09-04 | Compliance |
| Calcium Carbonate 70% | IC-18340 | 2024-08-28 | Supply Chain |
| SIG-42-AYY-K71K | IC-18349 | 2023-11-26 | Product Management |
| dextrose 25% tech grade | TC-18365 | 2021-04-21 | Operations |
| Potassium Sorbate | TC-18369 | 2023-02-24 | Supply Chain |
| Excise FR 10% | TC-18370 | 2024-11-23 | Finance |
| SIG-62-LDL-CC5R | IC-18375 | 2021-07-13 | Product Management |
| Vat Standardqualität CN 19% | IC-18387 | 2023-01-13 | Supply Chain |
| SIG-17-LVE-03G9 | BC-18414 | 2023-02-07 | Data Governance |
| SIG-42-MEI-2SCI | IC-18417 | 2022-06-28 | IT Infrastructure |
| Customs Duty FR 19% | TC-18425 | 2022-04-18 | IT Infrastructure |
| VA-ST-D-7-855 | IC-18460 | 2021-08-09 | Product Management |
| isoglucose | TC-18493 | 2021-12-25 | IT Infrastructure |
| SIG-68-TVY-N4XJ | BC-18496 | 2022-07-16 | Compliance |
| cyclodextrin | BC-18498 | 2022-12-25 | Operations |
| core partners BV | BC-18507 | 2024-05-08 | Operations |
| SIG-85-FAV-D2EE | IC-18508 | 2023-02-17 | Compliance |
| rapeseed oil | IC-18510 | 2022-05-17 | IT Infrastructure |
| DE-25-TE-949 | BC-18515 | 2024-04-03 | Supply Chain |
| Coconut Oil 70% Grade A | BC-18537 | 2021-10-19 | Product Management |
| CI-AC-215 | IC-18564 | 2021-10-16 | Operations |
| soy isolate 99.5% standard | IC-18567 | 2022-10-17 | Product Management |
| SIG-11-SLQ-KF5B | TC-18569 | 2022-10-16 | Supply Chain |
| SIG-59-HZI-WDX6 Group | BC-18580 | 2021-09-07 | Operations |
| Natriumchlorid | TC-18585 | 2021-06-11 | IT Infrastructure |
| Vertex Sourcing | BC-18588 | 2024-10-14 | Finance |
| SIG-98-NIJ-5N8C | BC-18589 | 2021-11-14 | Product Management |
| RA-OI-GR-A-272 | BC-18599 | 2021-09-26 | Data Governance |
| Dextrin Qualitätsstufe II | TC-18605 | 2022-04-05 | Compliance |
| resistant starch 98% pharma grade | BC-18615 | 2023-08-07 | Finance |
| Vertex Sourcing | IC-18618 | 2021-06-05 | Compliance |
| central materials | BC-18620 | 2023-06-26 | Supply Chain |
| Pinnacle Processing | TC-18624 | 2022-11-27 | IT Infrastructure |
| Horizon Handel KG | BC-18632 | 2023-05-06 | IT Infrastructure |
| ME-TR-366 International | IC-18639 | 2024-03-04 | Operations |
| premier distribution Group | TC-18653 | 2022-07-11 | Supply Chain |
| SIG-40-PLP-7A3U | TC-18654 | 2021-01-25 | Data Governance |
| NO-LO-302 | BC-18670 | 2021-06-05 | IT Infrastructure |
| SIG-51-RJJ-5BIE | BC-18679 | 2024-03-27 | Supply Chain |
| Customs Duty FR 19% | BC-18684 | 2024-10-02 | Product Management |
| VE-EN-393 Group | BC-18701 | 2024-03-22 | Finance |
| Natriumbenzoat 25% Qualitätsstufe II | TC-18711 | 2024-02-22 | Data Governance |
| SIG-80-WEB-2C7R | BC-18724 | 2021-07-06 | Data Governance |
| Baltic Supply Co. | BC-18728 | 2024-04-07 | Product Management |
| Kasein 25% Technische Qualität | TC-18736 | 2023-08-17 | Compliance |
| CU-DU-F-5-228 | BC-18749 | 2023-09-18 | Data Governance |
| Vat Reduced FR 0% | TC-18762 | 2022-12-14 | Finance |
| Fructose | TC-18773 | 2021-08-13 | IT Infrastructure |
| Global Processing SAS | BC-18779 | 2024-05-06 | Data Governance |
| continental processing SA | IC-18798 | 2022-03-04 | Product Management |
| Resistant Starch 50% | BC-18807 | 2021-02-19 | Product Management |
| PI-IN-388 | BC-18831 | 2021-11-23 | Finance |
| AS-AC-70-347 | IC-18848 | 2023-05-19 | Supply Chain |
| Pea Protein Qualitätsstufe I | BC-18872 | 2022-03-17 | Supply Chain |
| apex sourcing | BC-18885 | 2023-04-25 | Supply Chain |
| SIG-64-LXA-3LJO | BC-18894 | 2024-02-18 | Finance |
| Apex Enterprise Holdings | BC-18903 | 2023-12-16 | Operations |
| Meridian Chemicals AG | TC-18912 | 2022-04-25 | Compliance |
| Pacific Materials | IC-18919 | 2023-02-26 | Data Governance |
| AT-IN-956 PLC | BC-18921 | 2022-06-11 | Finance |
| Sodium Chloride 99.5% Grade A | TC-18937 | 2023-08-11 | Product Management |
| Central Versorgung GmbH | IC-18938 | 2022-09-23 | Product Management |
| Maltodextrin-Pulver DE25 | BC-18939 | 2021-07-18 | Finance |
| Pea Protein | IC-18940 | 2022-06-02 | Finance |
| GL-SY-70-549 | TC-18948 | 2022-12-18 | Data Governance |
| Ascorbic Acid Standardqualität | BC-18951 | 2021-11-01 | Supply Chain |
| Stellar Partners | IC-18967 | 2023-12-19 | Finance |
| Lactic Acid 98% | BC-18970 | 2024-10-05 | Supply Chain |
| PR-EN-764 Ltd. | TC-18972 | 2022-07-17 | Operations |
| VE-LO-777 | BC-18995 | 2024-11-11 | Finance |
| SIG-90-BVN-BJY6 | BC-19009 | 2021-10-13 | Data Governance |
| QU-LO-333 | IC-19014 | 2022-09-26 | IT Infrastructure |
| SIG-79-RTU-R8IQ | TC-19025 | 2024-11-09 | Finance |
| Central Materials SARL | BC-19037 | 2024-05-22 | Operations |
| citric acid standard | BC-19051 | 2024-08-05 | Compliance |
| CI-AC-488 | TC-19076 | 2022-11-26 | Finance |
| SIG-64-LXA-3LJO | BC-19124 | 2021-09-23 | IT Infrastructure |
| Resistant Starch Technical | BC-19125 | 2023-09-17 | Finance |
| soy isolate standard | TC-19134 | 2024-01-14 | IT Infrastructure |
| SIG-42-SPP-A6C6 | IC-19141 | 2021-03-11 | Operations |
| Ascorbic Acid 98% Qualitätsstufe II | BC-19149 | 2021-09-03 | Product Management |
| lactic acid standard | IC-19156 | 2021-07-23 | Supply Chain |
| SIG-58-EEN-BKJF | IC-19162 | 2023-07-05 | Finance |
| Zitronensäure Lebensmittelrein | BC-19164 | 2022-10-01 | Supply Chain |
| atlas materials | IC-19197 | 2023-05-14 | Operations |
| Atlas Sourcing | IC-19221 | 2024-07-11 | Data Governance |
| SO-IS-975 | TC-19272 | 2023-10-22 | Compliance |
| SIG-31-LIW-GW9B International | BC-19279 | 2022-06-02 | Operations |
| Resistant Starch 70% Food Grade | IC-19284 | 2024-12-26 | Finance |
| excise nl 21% | BC-19306 | 2023-11-27 | Product Management |
| SIG-78-WDE-NNV9 | IC-19308 | 2021-04-23 | Data Governance |
| Vat Standard FR 20% | TC-19314 | 2023-06-13 | Finance |
| maltodextrin de18 | IC-19360 | 2023-08-04 | Supply Chain |
| vanguard industries Inc. | BC-19363 | 2023-09-28 | IT Infrastructure |
| Potassium Sorbate 50% Technical | IC-19371 | 2021-12-24 | Finance |
| Stratos Sourcing | BC-19394 | 2023-05-05 | Operations |
| Pea Protein 70% Premium | BC-19401 | 2024-01-24 | Supply Chain |
| Vertex Commodities | BC-19404 | 2022-03-22 | Supply Chain |
| quantum sourcing | IC-19407 | 2022-05-15 | Product Management |
| SIG-94-TOI-OFNK | TC-19416 | 2023-04-14 | Product Management |
| Casein Grade A | BC-19427 | 2024-01-01 | Finance |
| Palm Oil Food Grade | BC-19432 | 2023-10-22 | Data Governance |
| SIG-69-OFZ-JW34 | TC-19433 | 2021-06-27 | Finance |
| SIG-86-QXF-N0RG | BC-19442 | 2024-09-19 | Operations |
| CO-OI-50-147 | TC-19459 | 2022-06-04 | Product Management |
| Vertex Sourcing | TC-19462 | 2023-09-13 | Operations |
| Premier Logistics AG | TC-19465 | 2021-02-18 | Finance |
| CO-OI-98-890 | BC-19472 | 2021-10-02 | Compliance |
| SO-AC-PH-GR-620 | TC-19480 | 2021-01-18 | Product Management |
| VA-RE-I-25-366 | TC-19487 | 2023-09-02 | Finance |
| Zenith Logistik | TC-19496 | 2022-04-16 | Supply Chain |
| Excise NL 0% | IC-19500 | 2024-09-02 | Data Governance |
| ME-SO-734 | IC-19523 | 2022-04-02 | Compliance |
| pinnacle trading Inc. | TC-19532 | 2021-08-27 | Finance |
| Withholding NL 15% | IC-19542 | 2024-04-07 | Supply Chain |
| soy isolate 99.5% premium | IC-19552 | 2021-08-04 | Compliance |
| PE-PR-ST-174 | IC-19564 | 2023-07-07 | Data Governance |
| CU-DU-G-5-599 | BC-19590 | 2022-01-23 | Supply Chain |
| SIG-60-WYC-NAXS | TC-19604 | 2024-01-28 | Finance |
| Vat Reduced GB 25% | BC-19606 | 2023-02-19 | Compliance |
| nexus logistics | TC-19620 | 2024-07-06 | Operations |
| HO-LO-534 PLC | TC-19627 | 2024-11-10 | Supply Chain |
| SIG-52-EML-H8JV | TC-19639 | 2023-06-14 | IT Infrastructure |
| SIG-91-PEG-USI6 | BC-19641 | 2023-04-20 | Finance |
| Resistente Stärke 70% | TC-19673 | 2023-03-12 | Compliance |
| Ascorbic Acid Premium | IC-19682 | 2022-11-25 | Product Management |
| GL-SY-609 | BC-19698 | 2023-04-10 | Compliance |
| Horizon Sourcing | BC-19703 | 2023-09-03 | IT Infrastructure |
| Lactic Acid Lebensmittelrein | IC-19707 | 2021-02-06 | Finance |
| Central Solutions | BC-19766 | 2024-04-07 | Finance |
| Vat Standard NL 19% | TC-19777 | 2024-02-26 | Finance |
| SO-AC-99.5-338 | BC-19797 | 2024-08-09 | Data Governance |
| Traubenzucker 70% | TC-19799 | 2023-05-09 | Operations |
| Pea Protein Grade A | IC-19806 | 2023-04-28 | Supply Chain |
| EL-MA-995 | TC-19830 | 2024-04-13 | Operations |
| SO-AC-658 | IC-19832 | 2023-11-10 | Data Governance |
| ME-MA-989 | TC-19835 | 2024-02-02 | Finance |
| casein pharma grade | IC-19850 | 2024-03-16 | Supply Chain |
| Meridian Logistics | TC-19852 | 2023-01-15 | Operations |
| CI-AC-99.5-674 | IC-19877 | 2021-06-17 | Product Management |
| Ascorbic Acid Premiumqualität | IC-19881 | 2024-08-09 | Operations |
| Central Werkstoffe | BC-19885 | 2024-07-02 | Supply Chain |
| SIG-29-CYR-T4UF | BC-19921 | 2024-06-01 | Supply Chain |
| excise in 20% | IC-19960 | 2021-12-28 | Product Management |
| Glucose Syrup 99.5% Food Grade | TC-19962 | 2022-01-02 | Finance |
| Traubenzucker Qualitätsstufe I | BC-19965 | 2022-07-18 | Supply Chain |
| Calcium Carbonate 98% Standard | IC-19991 | 2021-11-11 | Supply Chain |
| SIG-58-EEN-BKJF | TC-20004 | 2021-10-02 | Product Management |
| SIG-61-ZIT-092H | TC-20011 | 2024-10-28 | Product Management |
| SO-CH-25-PR-784 | BC-20014 | 2023-06-24 | Compliance |
| Weizenklebereiweiß | BC-20026 | 2022-03-11 | Operations |
| QU-SO-556 | IC-20035 | 2022-02-26 | Product Management |
| SIG-70-IPH-1O08 | BC-20041 | 2024-03-21 | Compliance |
| Quantum Versorgung GmbH | IC-20043 | 2021-04-24 | Finance |
| rapeseed oil tech grade | BC-20076 | 2024-11-19 | Data Governance |
| SIG-71-VGV-8K52 | BC-20080 | 2024-05-05 | Compliance |
| CO-LO-919 Holdings | BC-20082 | 2023-05-27 | Operations |
| SIG-14-WWQ-VPK2 SARL | BC-20084 | 2021-06-07 | Product Management |
| PO-SO-560 | TC-20092 | 2024-04-13 | Data Governance |
| Nexus Sourcing | IC-20126 | 2021-07-06 | IT Infrastructure |
| SIG-57-YOY-F7N2 | IC-20145 | 2023-04-03 | Product Management |
| Rapsöl | BC-20151 | 2021-10-24 | Product Management |
| Glukosesirup Syrup 99.5% Qualitätsstufe II | IC-20153 | 2022-12-15 | IT Infrastructure |
| Citric Acid 25% | TC-20157 | 2022-10-12 | Compliance |
| Soja Isolate Premiumqualität | TC-20161 | 2023-04-28 | Operations |
| CE-MA-213 | IC-20193 | 2023-10-01 | Data Governance |
| sorbic acid food grade | BC-20195 | 2023-01-02 | Finance |
| CI-AC-25-TE-484 | BC-20205 | 2024-06-11 | Compliance |
| SIG-64-VUE-OGQ2 | IC-20207 | 2024-03-06 | Operations |
| SU-OI-ST-194 | BC-20241 | 2021-08-11 | Product Management |
| calcium carbonate standard | TC-20269 | 2021-03-07 | Product Management |
| CU-DU-C-25-616 | BC-20278 | 2022-06-15 | Operations |
| SIG-55-SMZ-MJ0B | BC-20285 | 2022-05-02 | Compliance |
| SIG-43-SDJ-TRJ6 | IC-20293 | 2023-07-23 | Compliance |
| baltic trading | BC-20305 | 2021-10-21 | Compliance |
| Palmfett | TC-20307 | 2022-04-11 | Supply Chain |
| SIG-23-OPT-7QHV | BC-20326 | 2023-12-06 | Finance |
| Dextrose 25% Technical | BC-20339 | 2022-12-07 | Finance |
| SO-BE-99.5-TE-953 | IC-20341 | 2023-03-03 | Data Governance |
| Sorbinsäure Standardqualität | TC-20350 | 2024-12-14 | Compliance |
| Maltodextrin-Pulver DE10 | IC-20359 | 2023-09-22 | Operations |
| Ascorbic Acid 25% Grade B | TC-20377 | 2021-01-04 | Product Management |
| SIG-44-HTV-P84J | IC-20394 | 2021-09-02 | Finance |
| Horizon Sourcing | TC-20402 | 2023-09-18 | Compliance |


#### 4.3.3 Historical Assignments (Reference Only)

**WARNING**: The following are historical records preserved for audit purposes.
Some may have been superseded or corrected. Always verify against current MDM Registry.

| Source Entity | Historical Code | Status | Notes |
|---------------|-----------------|--------|-------|
| Isoglucose 25% | IC-6709 | DEPRECATED | Historical - verify before use |
| Fructose 99.5% Technische Qualität | IC-7127 | DEPRECATED | Historical - verify before use |
| SIG-61-XKV-ODPX | IC-7801 | DEPRECATED | Historical - verify before use |
| SIG-45-ZZU-GRXH International | IC-5988 | SUPERSEDED | Historical - verify before use |
| SIG-77-TUK-IN2B | IC-6245 | SUPERSEDED | Historical - verify before use |
| SIG-76-YLU-7DL9 | IC-9879 | PROVISIONAL | Historical - verify before use |
| sorbic acid | IC-8691 | DEPRECATED | Historical - verify before use |
| zenith logistics | IC-8101 | REVIEW REQUIRED | Historical - verify before use |
| VA-RE-I-20-892 | IC-9762 | REVIEW REQUIRED | Historical - verify before use |
| SIG-29-BZP-SU62 | IC-7752 | DEPRECATED | Historical - verify before use |
| Isoglucose 70% | IC-6656 | REVIEW REQUIRED | Historical - verify before use |
| Fructose 25% | IC-7111 | REVIEW REQUIRED | Historical - verify before use |
| SIG-79-SPO-WT80 | IC-7247 | REVIEW REQUIRED | Historical - verify before use |
| Calcium Carbonate 98% | IC-8748 | DEPRECATED | Historical - verify before use |
| Atlas Materials | IC-7047 | PROVISIONAL | Historical - verify before use |
| nexus supply | IC-8950 | REVIEW REQUIRED | Historical - verify before use |
| RE-ST-FO-GR-238 | IC-6453 | REVIEW REQUIRED | Historical - verify before use |
| Sorbinsäure 50% Lebensmittelrein | IC-9704 | REVIEW REQUIRED | Historical - verify before use |
| Potassium Sorbate 50% Technical | IC-8352 | REVIEW REQUIRED | Historical - verify before use |
| SIG-69-TRZ-SFLQ | IC-8182 | PROVISIONAL | Historical - verify before use |
| vanguard industries AG | IC-6624 | SUPERSEDED | Historical - verify before use |
| SIG-42-AJS-6RPK | IC-5288 | DEPRECATED | Historical - verify before use |
| SIG-43-XDN-7VEU | IC-7650 | PROVISIONAL | Historical - verify before use |
| Fructose | IC-5364 | REVIEW REQUIRED | Historical - verify before use |
| core chemicals Group | IC-6927 | SUPERSEDED | Historical - verify before use |
| Zitronensäure Qualitätsstufe I | IC-5552 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-50-PH-GR-568 | IC-5954 | PROVISIONAL | Historical - verify before use |
| Fructose 25% | IC-7242 | SUPERSEDED | Historical - verify before use |
| SIG-95-APX-PWFS | IC-6961 | PROVISIONAL | Historical - verify before use |
| Dextrin Premium | IC-8949 | PROVISIONAL | Historical - verify before use |
| SIG-10-DWM-ZA0C | IC-8614 | REVIEW REQUIRED | Historical - verify before use |
| ME-LO-670 | IC-6145 | REVIEW REQUIRED | Historical - verify before use |
| Pea Protein 98% Grade B | IC-5786 | PROVISIONAL | Historical - verify before use |
| sunflower oil | IC-5067 | DEPRECATED | Historical - verify before use |
| SIG-38-OTV-E78M | IC-9805 | DEPRECATED | Historical - verify before use |
| Resistant Starch Grade A | IC-7728 | DEPRECATED | Historical - verify before use |
| SIG-30-LJO-TN4Y | IC-7323 | REVIEW REQUIRED | Historical - verify before use |
| Vanguard Materials | IC-9671 | PROVISIONAL | Historical - verify before use |
| calcium carbonate 50% premium | IC-5328 | PROVISIONAL | Historical - verify before use |
| CU-DU-F-5-228 | IC-7169 | PROVISIONAL | Historical - verify before use |
| Lactic Acid 70% Pharmazeutisch rein | IC-8066 | PROVISIONAL | Historical - verify before use |
| SIG-19-TLQ-1P5Z | IC-8052 | REVIEW REQUIRED | Historical - verify before use |
| Sorbinsäure | IC-7990 | SUPERSEDED | Historical - verify before use |
| Fructose | IC-6294 | SUPERSEDED | Historical - verify before use |
| SIG-84-HBF-DDQL | IC-5720 | REVIEW REQUIRED | Historical - verify before use |
| dextrose 25% | IC-7105 | SUPERSEDED | Historical - verify before use |
| Weizenklebereiweiß Qualitätsstufe I | IC-5735 | PROVISIONAL | Historical - verify before use |
| vertex logistics | IC-8952 | PROVISIONAL | Historical - verify before use |
| Sodium Chloride 99.5% Grade A | IC-9392 | PROVISIONAL | Historical - verify before use |
| Dextrin Grade B | IC-9145 | SUPERSEDED | Historical - verify before use |
| WH-GL-50-TE-338 | IC-8824 | DEPRECATED | Historical - verify before use |
| CE-LO-195 | IC-7791 | SUPERSEDED | Historical - verify before use |
| SU-OI-FO-GR-778 | IC-9959 | DEPRECATED | Historical - verify before use |
| Withholding NL 5% | IC-8171 | REVIEW REQUIRED | Historical - verify before use |
| VE-SO-401 | IC-6334 | PROVISIONAL | Historical - verify before use |
| Sunflower Oil Pharma Grade | IC-7416 | PROVISIONAL | Historical - verify before use |
| Sorbic Acid 50% Grade A | IC-5988 | REVIEW REQUIRED | Historical - verify before use |
| atlantic processing Holdings | IC-8648 | REVIEW REQUIRED | Historical - verify before use |
| pacific industries | IC-8466 | PROVISIONAL | Historical - verify before use |
| Resistant Starch 98% Pharma Grade | IC-9787 | DEPRECATED | Historical - verify before use |
| SIG-68-HOK-ETCC | IC-7170 | REVIEW REQUIRED | Historical - verify before use |
| continental solutions SARL | IC-7041 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid | IC-6974 | DEPRECATED | Historical - verify before use |
| premier manufacturing BV | IC-5377 | DEPRECATED | Historical - verify before use |
| SIG-75-DRM-1CLN | IC-6284 | SUPERSEDED | Historical - verify before use |
| IS-641 | IC-5272 | DEPRECATED | Historical - verify before use |
| Dextrose Grade B | IC-7498 | REVIEW REQUIRED | Historical - verify before use |
| VA-RE-G-25-615 | IC-8436 | DEPRECATED | Historical - verify before use |
| Quantum Partners | IC-9052 | PROVISIONAL | Historical - verify before use |
| Premier Handel Group | IC-7027 | SUPERSEDED | Historical - verify before use |
| Pacific Materials | IC-6736 | SUPERSEDED | Historical - verify before use |
| Withholding US 25% | IC-5462 | SUPERSEDED | Historical - verify before use |
| Atlantic Trading | IC-7231 | DEPRECATED | Historical - verify before use |
| coconut oil 25% tech grade | IC-9750 | DEPRECATED | Historical - verify before use |
| LA-AC-927 | IC-9764 | SUPERSEDED | Historical - verify before use |
| Kasein 98% | IC-6742 | PROVISIONAL | Historical - verify before use |
| RA-OI-25-FO-GR-818 | IC-9221 | REVIEW REQUIRED | Historical - verify before use |
| cyclodextrin 98% | IC-5314 | PROVISIONAL | Historical - verify before use |
| Zitronensäure Qualitätsstufe II | IC-7634 | REVIEW REQUIRED | Historical - verify before use |
| DE-70-856 | IC-7244 | DEPRECATED | Historical - verify before use |
| Zitronensäure | IC-6091 | SUPERSEDED | Historical - verify before use |
| AS-AC-573 | IC-8409 | PROVISIONAL | Historical - verify before use |
| Stratos Distribution Group | IC-5981 | REVIEW REQUIRED | Historical - verify before use |
| PR-SU-CO-443 | IC-5946 | DEPRECATED | Historical - verify before use |
| SIG-83-XMM-APXP | IC-6870 | DEPRECATED | Historical - verify before use |
| premier partners SARL | IC-9344 | SUPERSEDED | Historical - verify before use |
| Rapeseed Oil Technical | IC-6468 | PROVISIONAL | Historical - verify before use |
| SIG-55-DBH-2QS3 | IC-6486 | REVIEW REQUIRED | Historical - verify before use |
| Prism Sourcing | IC-9938 | DEPRECATED | Historical - verify before use |
| lactic acid standard | IC-5911 | REVIEW REQUIRED | Historical - verify before use |
| Core Chemicals Holdings | IC-8206 | DEPRECATED | Historical - verify before use |
| soy isolate | IC-7652 | DEPRECATED | Historical - verify before use |
| Premier Supply Co. | IC-7197 | SUPERSEDED | Historical - verify before use |
| pinnacle distribution Holdings | IC-5057 | DEPRECATED | Historical - verify before use |
| Traubenzucker 98% Qualitätsstufe I | IC-9099 | REVIEW REQUIRED | Historical - verify before use |
| Coconut Oil 25% Grade A | IC-9382 | SUPERSEDED | Historical - verify before use |
| soy isolate 99.5% premium | IC-7236 | SUPERSEDED | Historical - verify before use |
| PR-IN-608 BV | IC-6448 | SUPERSEDED | Historical - verify before use |
| Atlas Enterprise International | IC-9179 | DEPRECATED | Historical - verify before use |
| Zitronensäure Premiumqualität | IC-5070 | SUPERSEDED | Historical - verify before use |
| QU-SU-CO-890 | IC-9220 | PROVISIONAL | Historical - verify before use |
| SIG-86-EKJ-RFVB | IC-9819 | DEPRECATED | Historical - verify before use |
| Resistant Starch 99.5% | IC-7517 | SUPERSEDED | Historical - verify before use |
| SIG-18-PCA-V46E | IC-9701 | SUPERSEDED | Historical - verify before use |
| resistant starch standard | IC-7437 | DEPRECATED | Historical - verify before use |
| PI-SO-581 Inc. | IC-8356 | REVIEW REQUIRED | Historical - verify before use |
| Withholding NL 21% | IC-9717 | SUPERSEDED | Historical - verify before use |
| SIG-33-IWB-UV4J | IC-9782 | REVIEW REQUIRED | Historical - verify before use |
| Palmfett 98% Qualitätsstufe I | IC-8068 | DEPRECATED | Historical - verify before use |
| NO-SU-CO-498 | IC-7708 | PROVISIONAL | Historical - verify before use |
| ascorbic acid 98% premium | IC-7001 | REVIEW REQUIRED | Historical - verify before use |
| stratos logistics | IC-7307 | REVIEW REQUIRED | Historical - verify before use |
| PR-CO-800 Corp. | IC-6752 | DEPRECATED | Historical - verify before use |
| Casein 98% Technical | IC-7759 | SUPERSEDED | Historical - verify before use |
| SIG-47-MIU-LIH6 | IC-8304 | DEPRECATED | Historical - verify before use |
| SIG-99-VAH-2H31 | IC-8046 | PROVISIONAL | Historical - verify before use |
| Elite Supply Co. | IC-6733 | DEPRECATED | Historical - verify before use |
| horizon ingredients LLC | IC-6120 | PROVISIONAL | Historical - verify before use |
| Palm Oil Food Grade | IC-7907 | REVIEW REQUIRED | Historical - verify before use |
| SIG-58-NYA-2O4M | IC-9209 | SUPERSEDED | Historical - verify before use |
| Vertex Vertrieb Group | IC-5237 | SUPERSEDED | Historical - verify before use |
| Core Distribution | IC-8803 | REVIEW REQUIRED | Historical - verify before use |
| nexus logistics | IC-6213 | PROVISIONAL | Historical - verify before use |
| casein premium | IC-9472 | PROVISIONAL | Historical - verify before use |
| SO-BE-ST-871 | IC-7882 | REVIEW REQUIRED | Historical - verify before use |
| Zitronensäure 98% | IC-8241 | DEPRECATED | Historical - verify before use |
| premier enterprise Holdings | IC-5732 | PROVISIONAL | Historical - verify before use |
| Citric Acid 50% Grade A | IC-5704 | SUPERSEDED | Historical - verify before use |
| apex enterprise International | IC-5603 | SUPERSEDED | Historical - verify before use |
| SIG-33-FUV-53NO | IC-9547 | REVIEW REQUIRED | Historical - verify before use |
| SO-IS-PH-GR-671 | IC-8437 | DEPRECATED | Historical - verify before use |
| Quantum Supply Co. | IC-9131 | REVIEW REQUIRED | Historical - verify before use |
| cyclodextrin 98% pharma grade | IC-6262 | PROVISIONAL | Historical - verify before use |
| SO-CH-GR-B-273 | IC-6517 | REVIEW REQUIRED | Historical - verify before use |
| Traubenzucker Qualitätsstufe I | IC-6379 | REVIEW REQUIRED | Historical - verify before use |
| Palm Oil 98% | IC-8711 | PROVISIONAL | Historical - verify before use |
| Meridian Logistics | IC-5567 | PROVISIONAL | Historical - verify before use |
| PI-LO-142 | IC-6749 | DEPRECATED | Historical - verify before use |
| SIG-82-JMP-PVGN | IC-8001 | SUPERSEDED | Historical - verify before use |
| SO-BE-GR-A-760 | IC-8136 | REVIEW REQUIRED | Historical - verify before use |
| SIG-92-VAB-1JHU | IC-6577 | REVIEW REQUIRED | Historical - verify before use |
| CO-OI-25-TE-157 | IC-9076 | REVIEW REQUIRED | Historical - verify before use |
| SIG-34-UJK-TJA6 | IC-5577 | DEPRECATED | Historical - verify before use |
| Sorbic Acid 25% Grade B | IC-9567 | SUPERSEDED | Historical - verify before use |
| Sorbinsäure 70% | IC-9067 | PROVISIONAL | Historical - verify before use |
| Catalyst Materials | IC-6626 | DEPRECATED | Historical - verify before use |
| Pacific Werkstoffe | IC-5460 | SUPERSEDED | Historical - verify before use |
| Soy Isolate 98% Food Grade | IC-5164 | PROVISIONAL | Historical - verify before use |
| fructose 70% | IC-7647 | REVIEW REQUIRED | Historical - verify before use |
| SIG-79-HKV-T268 | IC-9605 | DEPRECATED | Historical - verify before use |
| PO-SO-339 | IC-6594 | PROVISIONAL | Historical - verify before use |
| Vat Standard NL 19% | IC-8117 | PROVISIONAL | Historical - verify before use |
| RA-OI-431 | IC-5103 | PROVISIONAL | Historical - verify before use |
| AP-SO-576 | IC-6135 | SUPERSEDED | Historical - verify before use |
| sodium chloride 99.5% premium | IC-9555 | SUPERSEDED | Historical - verify before use |
| Stratos Partners SAS | IC-8219 | DEPRECATED | Historical - verify before use |
| SIG-38-WKO-LWQT | IC-8012 | SUPERSEDED | Historical - verify before use |
| PA-SO-270 | IC-6899 | SUPERSEDED | Historical - verify before use |
| SIG-77-RVO-CE8D Inc. | IC-5891 | SUPERSEDED | Historical - verify before use |
| Ascorbic Acid Pharmazeutisch rein | IC-7046 | DEPRECATED | Historical - verify before use |
| Prism Sourcing | IC-6634 | SUPERSEDED | Historical - verify before use |
| PA-CH-580 KG | IC-8167 | REVIEW REQUIRED | Historical - verify before use |
| Isoglucose | IC-7110 | SUPERSEDED | Historical - verify before use |
| PO-SO-768 | IC-9825 | DEPRECATED | Historical - verify before use |
| CA-CA-99.5-291 | IC-8776 | SUPERSEDED | Historical - verify before use |
| SIG-14-TOH-IPJ4 | IC-8246 | PROVISIONAL | Historical - verify before use |
| SIG-27-RTX-YEAW | IC-8448 | PROVISIONAL | Historical - verify before use |
| SO-IS-GR-A-940 | IC-8962 | DEPRECATED | Historical - verify before use |
| quantum processing International | IC-5282 | PROVISIONAL | Historical - verify before use |
| SIG-27-FHB-EY0E | IC-6358 | REVIEW REQUIRED | Historical - verify before use |
| FR-99.5-TE-579 | IC-6271 | SUPERSEDED | Historical - verify before use |
| Vanguard Enterprise International | IC-6587 | PROVISIONAL | Historical - verify before use |
| ascorbic acid standard | IC-7911 | DEPRECATED | Historical - verify before use |
| Lactic Acid 25% Lebensmittelrein | IC-9880 | SUPERSEDED | Historical - verify before use |
| SIG-81-HMA-4WEQ | IC-9360 | PROVISIONAL | Historical - verify before use |
| Vat Standardqualität FR 21% | IC-7874 | SUPERSEDED | Historical - verify before use |
| Stellar Werkstoffe | IC-6208 | PROVISIONAL | Historical - verify before use |
| Fructose | IC-5386 | DEPRECATED | Historical - verify before use |
| horizon trading Ltd. | IC-5298 | REVIEW REQUIRED | Historical - verify before use |
| Resistente Stärke | IC-6043 | DEPRECATED | Historical - verify before use |
| SIG-73-AXD-XIX9 | IC-6506 | REVIEW REQUIRED | Historical - verify before use |
| Prism Manufacturing NV | IC-6471 | PROVISIONAL | Historical - verify before use |
| Vanguard Industries BV | IC-5413 | SUPERSEDED | Historical - verify before use |
| Nordic Supply Co. | IC-5097 | SUPERSEDED | Historical - verify before use |
| Elite Manufacturing | IC-7926 | REVIEW REQUIRED | Historical - verify before use |
| SIG-58-BDQ-I1V3 | IC-6727 | DEPRECATED | Historical - verify before use |
| Pea Protein 70% Technische Qualität | IC-5190 | DEPRECATED | Historical - verify before use |
| PA-SO-568 | IC-9147 | REVIEW REQUIRED | Historical - verify before use |
| Pinnacle Rohstoffe NV | IC-6091 | PROVISIONAL | Historical - verify before use |
| Vanguard Enterprise Group | IC-5249 | SUPERSEDED | Historical - verify before use |
| Fructose | IC-7813 | DEPRECATED | Historical - verify before use |
| WH-GL-GR-A-583 | IC-7072 | SUPERSEDED | Historical - verify before use |
| Kasein | IC-7473 | DEPRECATED | Historical - verify before use |
| Natriumbenzoat 25% | IC-8394 | PROVISIONAL | Historical - verify before use |
| NE-SO-652 | IC-6173 | SUPERSEDED | Historical - verify before use |
| fructose tech grade | IC-8667 | DEPRECATED | Historical - verify before use |
| Meridian Logistics | IC-8634 | SUPERSEDED | Historical - verify before use |
| PR-SU-CO-349 | IC-6320 | DEPRECATED | Historical - verify before use |
| vanguard supply NV | IC-6309 | PROVISIONAL | Historical - verify before use |
| maltodextrin de15 | IC-9345 | REVIEW REQUIRED | Historical - verify before use |
| CA-CA-50-GR-A-195 | IC-8493 | DEPRECATED | Historical - verify before use |
| Horizon Partners | IC-5107 | REVIEW REQUIRED | Historical - verify before use |
| Ascorbic Acid 99.5% Technische Qualität | IC-6052 | SUPERSEDED | Historical - verify before use |
| VA-PA-407 | IC-6487 | SUPERSEDED | Historical - verify before use |
| SO-AC-25-ST-106 | IC-9031 | REVIEW REQUIRED | Historical - verify before use |
| PI-MA-680 | IC-6037 | SUPERSEDED | Historical - verify before use |
| SIG-60-VTH-H7AM | IC-8416 | REVIEW REQUIRED | Historical - verify before use |
| VA-RE-N-10-785 | IC-8032 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat | IC-5205 | REVIEW REQUIRED | Historical - verify before use |
| SIG-92-GIK-H4FF | IC-5070 | PROVISIONAL | Historical - verify before use |
| Global Solutions Group | IC-9767 | PROVISIONAL | Historical - verify before use |
| SIG-15-MKL-LGBK | IC-8758 | PROVISIONAL | Historical - verify before use |
| Vanguard Supply Co. | IC-6669 | REVIEW REQUIRED | Historical - verify before use |
| PR-IN-195 KG | IC-7479 | REVIEW REQUIRED | Historical - verify before use |
| Customs Duty DE 5% | IC-6374 | REVIEW REQUIRED | Historical - verify before use |
| continental manufacturing Inc. | IC-7286 | REVIEW REQUIRED | Historical - verify before use |
| Customs Duty US 20% | IC-9230 | PROVISIONAL | Historical - verify before use |
| VE-SO-366 | IC-7506 | PROVISIONAL | Historical - verify before use |
| Soy Isolate | IC-8402 | REVIEW REQUIRED | Historical - verify before use |
| coconut oil | IC-6506 | PROVISIONAL | Historical - verify before use |
| AS-AC-PR-778 | IC-7631 | DEPRECATED | Historical - verify before use |
| Resistente Stärke | IC-5828 | DEPRECATED | Historical - verify before use |
| Catalyst Industries International | IC-9793 | REVIEW REQUIRED | Historical - verify before use |
| SIG-70-EXR-LD0M | IC-8015 | PROVISIONAL | Historical - verify before use |
| Potassium Sorbate Technical | IC-9534 | SUPERSEDED | Historical - verify before use |
| Sodium Benzoate Grade A | IC-6825 | SUPERSEDED | Historical - verify before use |
| ZE-PA-511 PLC | IC-6725 | DEPRECATED | Historical - verify before use |
| SIG-97-EIS-DKQB Holdings | IC-8747 | REVIEW REQUIRED | Historical - verify before use |
| Lactic Acid | IC-8636 | PROVISIONAL | Historical - verify before use |
| SIG-94-MKW-LH8F | IC-6533 | DEPRECATED | Historical - verify before use |
| Elite Logistics Holdings | IC-6848 | SUPERSEDED | Historical - verify before use |
| casein | IC-7252 | SUPERSEDED | Historical - verify before use |
| Sorbinsäure 99.5% | IC-5196 | REVIEW REQUIRED | Historical - verify before use |
| SIG-50-BJQ-W54O Holdings | IC-5784 | DEPRECATED | Historical - verify before use |
| HO-MA-854 | IC-8236 | PROVISIONAL | Historical - verify before use |
| SIG-22-DOP-7UDK | IC-5392 | SUPERSEDED | Historical - verify before use |
| Kaliumsorbat | IC-7984 | REVIEW REQUIRED | Historical - verify before use |
| Vertex Distribution AG | IC-9652 | DEPRECATED | Historical - verify before use |
| Ascorbic Acid 70% | IC-5502 | PROVISIONAL | Historical - verify before use |
| SIG-52-CQW-KL19 | IC-8587 | PROVISIONAL | Historical - verify before use |
| vanguard enterprise | IC-5319 | PROVISIONAL | Historical - verify before use |
| Palm Oil | IC-5870 | DEPRECATED | Historical - verify before use |
| Isoglucose | IC-7095 | DEPRECATED | Historical - verify before use |
| lactic acid | IC-7796 | REVIEW REQUIRED | Historical - verify before use |
| PR-CH-808 AG | IC-6728 | PROVISIONAL | Historical - verify before use |
| continental enterprise GmbH | IC-8010 | REVIEW REQUIRED | Historical - verify before use |
| vat standard in 5% | IC-5082 | SUPERSEDED | Historical - verify before use |
| Baltic Logistics | IC-7837 | PROVISIONAL | Historical - verify before use |
| IS-641 | IC-6816 | REVIEW REQUIRED | Historical - verify before use |
| Sodium Benzoate 98% Standard | IC-6730 | PROVISIONAL | Historical - verify before use |
| CO-MA-295 | IC-6604 | PROVISIONAL | Historical - verify before use |
| sodium chloride 98% standard | IC-6518 | DEPRECATED | Historical - verify before use |
| Palm Oil 70% Pharma Grade | IC-7765 | PROVISIONAL | Historical - verify before use |
| SIG-39-MAR-LMVK | IC-6922 | PROVISIONAL | Historical - verify before use |
| SIG-43-NCZ-FT9Z | IC-8179 | DEPRECATED | Historical - verify before use |
| Cyclodextrin Food Grade | IC-5490 | SUPERSEDED | Historical - verify before use |
| SIG-20-XIG-T8ME | IC-5950 | REVIEW REQUIRED | Historical - verify before use |
| SIG-92-FQX-S1BC | IC-6058 | DEPRECATED | Historical - verify before use |
| Continental Werkstoffe BV | IC-9997 | DEPRECATED | Historical - verify before use |
| SIG-37-SOD-NFZK | IC-9163 | DEPRECATED | Historical - verify before use |
| SIG-15-VIS-079C | IC-8433 | PROVISIONAL | Historical - verify before use |
| SIG-84-DSO-4S47 | IC-7673 | REVIEW REQUIRED | Historical - verify before use |
| Kasein 50% Premiumqualität | IC-7978 | PROVISIONAL | Historical - verify before use |
| Central Sourcing | IC-8675 | REVIEW REQUIRED | Historical - verify before use |
| stratos sourcing | IC-8981 | PROVISIONAL | Historical - verify before use |
| nordic ingredients SARL | IC-8781 | DEPRECATED | Historical - verify before use |
| RA-OI-98-ST-938 | IC-9063 | REVIEW REQUIRED | Historical - verify before use |
| SIG-74-EPP-R9AG | IC-9856 | PROVISIONAL | Historical - verify before use |
| PA-OI-410 | IC-6385 | SUPERSEDED | Historical - verify before use |
| resistant starch | IC-5297 | SUPERSEDED | Historical - verify before use |
| global materials | IC-8416 | PROVISIONAL | Historical - verify before use |
| SIG-37-ZOD-1VME | IC-9856 | DEPRECATED | Historical - verify before use |
| casein standard | IC-9158 | SUPERSEDED | Historical - verify before use |
| CO-OI-50-PH-GR-568 | IC-9471 | REVIEW REQUIRED | Historical - verify before use |
| Pinnacle Vertrieb Ltd. | IC-8806 | PROVISIONAL | Historical - verify before use |
| Fructose 70% | IC-7642 | DEPRECATED | Historical - verify before use |
| Cyclodextrin Qualitätsstufe I | IC-8035 | PROVISIONAL | Historical - verify before use |
| Apex Logistik | IC-8548 | REVIEW REQUIRED | Historical - verify before use |
| premier sourcing | IC-6396 | SUPERSEDED | Historical - verify before use |
| Prime Versorgung GmbH | IC-9258 | SUPERSEDED | Historical - verify before use |
| GL-SU-CO-783 | IC-9537 | REVIEW REQUIRED | Historical - verify before use |
| SIG-57-YOY-F7N2 | IC-9379 | REVIEW REQUIRED | Historical - verify before use |
| SIG-43-GRJ-P3HT | IC-6878 | REVIEW REQUIRED | Historical - verify before use |
| Customs Duty IN 25% | IC-9067 | REVIEW REQUIRED | Historical - verify before use |
| cyclodextrin premium | IC-8369 | REVIEW REQUIRED | Historical - verify before use |
| Atlas Sourcing | IC-5380 | SUPERSEDED | Historical - verify before use |
| Dextrin Technische Qualität | IC-7879 | SUPERSEDED | Historical - verify before use |
| SIG-98-JEQ-77GG | IC-7492 | SUPERSEDED | Historical - verify before use |
| Lactic Acid | IC-7016 | SUPERSEDED | Historical - verify before use |
| Global Werkstoffe | IC-8844 | DEPRECATED | Historical - verify before use |
| CA-GR-B-950 | IC-7003 | REVIEW REQUIRED | Historical - verify before use |
| Vat Standard NL 20% | IC-6671 | PROVISIONAL | Historical - verify before use |
| SIG-29-BZP-SU62 | IC-5752 | PROVISIONAL | Historical - verify before use |
| Natriumbenzoat Qualitätsstufe II | IC-9084 | DEPRECATED | Historical - verify before use |
| Continental Chemicals Inc. | IC-8089 | DEPRECATED | Historical - verify before use |
| Global Werkstoffe | IC-9756 | REVIEW REQUIRED | Historical - verify before use |
| Customs Duty GB 0% | IC-6778 | PROVISIONAL | Historical - verify before use |
| Palmfett | IC-9078 | REVIEW REQUIRED | Historical - verify before use |
| SIG-66-RQA-05UV | IC-5193 | DEPRECATED | Historical - verify before use |
| Premier Enterprise | IC-7626 | PROVISIONAL | Historical - verify before use |
| SIG-98-OXJ-W0H6 SAS | IC-7036 | REVIEW REQUIRED | Historical - verify before use |
| Palmfett | IC-6586 | DEPRECATED | Historical - verify before use |
| Maltodextrin DE20 | IC-7707 | DEPRECATED | Historical - verify before use |
| Zitronensäure Pharmazeutisch rein | IC-9804 | SUPERSEDED | Historical - verify before use |
| Soy Isolate Standard | IC-9236 | DEPRECATED | Historical - verify before use |
| Dextrin 50% | IC-6835 | PROVISIONAL | Historical - verify before use |
| lactic acid | IC-5142 | DEPRECATED | Historical - verify before use |
| vanguard materials | IC-8234 | SUPERSEDED | Historical - verify before use |
| soy isolate | IC-5332 | DEPRECATED | Historical - verify before use |
| fructose tech grade | IC-9179 | DEPRECATED | Historical - verify before use |
| SU-OI-TE-705 | IC-9774 | DEPRECATED | Historical - verify before use |
| Kaliumsorbat 98% Qualitätsstufe II | IC-7738 | PROVISIONAL | Historical - verify before use |
| calcium carbonate standard | IC-9549 | DEPRECATED | Historical - verify before use |


#### 4.3.4 Excluded Assignments

The following assignments were identified but NOT completed due to data quality issues:

| Source Entity | Reason for Exclusion | Notes |
|---------------|---------------------|-------|
| NOISE-9887-F | Data quality insufficient | Escalated to data steward |
| NOISE-1572-C | Duplicate source record | Deferred to Phase 2 |
| NOISE-2035-E | Missing required attributes | Manual review scheduled |
| NOISE-1456-B | Pending validation | Deferred to Phase 2 |
| NOISE-6956-G | Duplicate source record | Business owner notified |
| NOISE-3394-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3086-C | Duplicate source record | Business owner notified |
| NOISE-8128-F | Out of scope per business decision | Manual review scheduled |
| NOISE-8209-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5169-G | Pending validation | Manual review scheduled |
| NOISE-7716-H | Data quality insufficient | Business owner notified |
| NOISE-2579-E | Data quality insufficient | Business owner notified |
| NOISE-5027-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-3106-E | Out of scope per business decision | Escalated to data steward |
| NOISE-2462-D | Data quality insufficient | Business owner notified |
| NOISE-4301-F | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8910-C | Missing required attributes | Escalated to data steward |
| NOISE-4317-B | Missing required attributes | Deferred to Phase 2 |
| NOISE-2098-B | Out of scope per business decision | Escalated to data steward |
| NOISE-2069-C | Data quality insufficient | Business owner notified |
| NOISE-4016-D | Out of scope per business decision | Escalated to data steward |
| NOISE-7603-A | Missing required attributes | Escalated to data steward |
| NOISE-4199-A | Pending validation | Escalated to data steward |
| NOISE-5433-H | Out of scope per business decision | Escalated to data steward |
| NOISE-4688-H | Data quality insufficient | Manual review scheduled |
| NOISE-9373-C | Out of scope per business decision | Escalated to data steward |
| NOISE-3843-C | Pending validation | Deferred to Phase 2 |
| NOISE-9829-D | Data quality insufficient | Escalated to data steward |
| NOISE-8149-D | Missing required attributes | Business owner notified |
| NOISE-3507-D | Missing required attributes | Deferred to Phase 2 |
| NOISE-2453-A | Pending validation | Manual review scheduled |
| NOISE-3750-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7553-H | Data quality insufficient | Escalated to data steward |
| NOISE-6065-H | Missing required attributes | Escalated to data steward |
| NOISE-6240-F | Pending validation | Escalated to data steward |
| NOISE-1663-A | Pending validation | Deferred to Phase 2 |
| NOISE-8603-E | Duplicate source record | Business owner notified |
| NOISE-3131-B | Data quality insufficient | Business owner notified |
| NOISE-4478-E | Missing required attributes | Business owner notified |
| NOISE-5720-F | Missing required attributes | Business owner notified |
| NOISE-4080-D | Duplicate source record | Manual review scheduled |
| NOISE-4411-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3580-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-7275-B | Data quality insufficient | Escalated to data steward |
| NOISE-1115-A | Data quality insufficient | Escalated to data steward |
| NOISE-8913-B | Duplicate source record | Escalated to data steward |
| NOISE-1331-D | Missing required attributes | Escalated to data steward |
| NOISE-4256-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8362-B | Data quality insufficient | Escalated to data steward |
| NOISE-8087-G | Data quality insufficient | Manual review scheduled |
| NOISE-3367-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5187-B | Duplicate source record | Business owner notified |
| NOISE-2338-D | Out of scope per business decision | Business owner notified |
| NOISE-8509-C | Pending validation | Manual review scheduled |
| NOISE-8148-B | Pending validation | Deferred to Phase 2 |
| NOISE-3397-H | Data quality insufficient | Manual review scheduled |
| NOISE-7677-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-9557-G | Data quality insufficient | Business owner notified |
| NOISE-5415-C | Missing required attributes | Business owner notified |
| NOISE-2926-F | Missing required attributes | Manual review scheduled |
| NOISE-7530-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3950-F | Pending validation | Escalated to data steward |
| NOISE-8053-E | Out of scope per business decision | Escalated to data steward |
| NOISE-8423-G | Out of scope per business decision | Escalated to data steward |
| NOISE-1596-A | Missing required attributes | Escalated to data steward |
| NOISE-2932-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-9790-D | Pending validation | Business owner notified |
| NOISE-5942-H | Missing required attributes | Business owner notified |
| NOISE-9920-E | Pending validation | Deferred to Phase 2 |
| NOISE-4528-D | Missing required attributes | Business owner notified |
| NOISE-2386-H | Missing required attributes | Manual review scheduled |
| NOISE-8288-A | Missing required attributes | Manual review scheduled |
| NOISE-4391-B | Missing required attributes | Manual review scheduled |
| NOISE-7954-F | Pending validation | Manual review scheduled |
| NOISE-7786-H | Data quality insufficient | Escalated to data steward |
| NOISE-8450-F | Pending validation | Business owner notified |
| NOISE-6116-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1050-C | Pending validation | Deferred to Phase 2 |
| NOISE-6872-D | Out of scope per business decision | Escalated to data steward |
| NOISE-2322-H | Duplicate source record | Manual review scheduled |
| NOISE-1056-G | Data quality insufficient | Escalated to data steward |
| NOISE-9846-D | Pending validation | Escalated to data steward |
| NOISE-6046-C | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5910-B | Duplicate source record | Business owner notified |
| NOISE-7861-B | Missing required attributes | Escalated to data steward |
| NOISE-4024-E | Pending validation | Escalated to data steward |
| NOISE-5704-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-1396-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5533-G | Pending validation | Deferred to Phase 2 |
| NOISE-2817-A | Pending validation | Deferred to Phase 2 |
| NOISE-7119-B | Missing required attributes | Escalated to data steward |
| NOISE-8214-C | Missing required attributes | Manual review scheduled |
| NOISE-9937-H | Out of scope per business decision | Business owner notified |
| NOISE-7912-E | Out of scope per business decision | Manual review scheduled |
| NOISE-4372-H | Duplicate source record | Escalated to data steward |
| NOISE-5196-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5316-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-1727-G | Out of scope per business decision | Business owner notified |
| NOISE-1592-E | Data quality insufficient | Escalated to data steward |
| NOISE-4706-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-3045-E | Out of scope per business decision | Manual review scheduled |
| NOISE-2882-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-7051-G | Out of scope per business decision | Manual review scheduled |
| NOISE-8003-C | Data quality insufficient | Manual review scheduled |
| NOISE-7849-A | Duplicate source record | Escalated to data steward |
| NOISE-1961-H | Missing required attributes | Manual review scheduled |
| NOISE-6110-B | Duplicate source record | Escalated to data steward |
| NOISE-9645-G | Data quality insufficient | Manual review scheduled |
| NOISE-8552-D | Missing required attributes | Business owner notified |
| NOISE-5057-G | Pending validation | Escalated to data steward |
| NOISE-7499-G | Pending validation | Manual review scheduled |
| NOISE-1122-D | Data quality insufficient | Business owner notified |
| NOISE-8342-F | Out of scope per business decision | Escalated to data steward |
| NOISE-1124-E | Out of scope per business decision | Business owner notified |
| NOISE-3572-F | Out of scope per business decision | Manual review scheduled |
| NOISE-4839-F | Pending validation | Manual review scheduled |
| NOISE-1524-D | Missing required attributes | Manual review scheduled |
| NOISE-3820-G | Pending validation | Manual review scheduled |
| NOISE-2800-A | Data quality insufficient | Business owner notified |
| NOISE-3806-H | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2384-D | Out of scope per business decision | Business owner notified |
| NOISE-9702-D | Duplicate source record | Business owner notified |
| NOISE-2938-C | Missing required attributes | Escalated to data steward |
| NOISE-9452-G | Duplicate source record | Manual review scheduled |
| NOISE-4461-E | Out of scope per business decision | Escalated to data steward |
| NOISE-7199-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-3793-A | Out of scope per business decision | Escalated to data steward |
| NOISE-3948-E | Data quality insufficient | Manual review scheduled |
| NOISE-3105-H | Data quality insufficient | Manual review scheduled |
| NOISE-7309-G | Duplicate source record | Deferred to Phase 2 |
| NOISE-5630-E | Duplicate source record | Escalated to data steward |
| NOISE-2002-A | Missing required attributes | Escalated to data steward |
| NOISE-8146-A | Out of scope per business decision | Manual review scheduled |
| NOISE-3784-H | Out of scope per business decision | Business owner notified |
| NOISE-6213-G | Out of scope per business decision | Escalated to data steward |
| NOISE-2852-H | Missing required attributes | Manual review scheduled |
| NOISE-5279-A | Data quality insufficient | Escalated to data steward |
| NOISE-7556-A | Pending validation | Manual review scheduled |
| NOISE-9224-B | Duplicate source record | Escalated to data steward |
| NOISE-1595-H | Out of scope per business decision | Manual review scheduled |
| NOISE-6978-H | Duplicate source record | Business owner notified |
| NOISE-7813-H | Pending validation | Manual review scheduled |
| NOISE-6366-A | Missing required attributes | Business owner notified |
| NOISE-9702-F | Out of scope per business decision | Business owner notified |
| NOISE-4076-H | Duplicate source record | Manual review scheduled |
| NOISE-4277-E | Duplicate source record | Manual review scheduled |
| NOISE-8253-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-5465-C | Pending validation | Deferred to Phase 2 |
| NOISE-4734-A | Pending validation | Business owner notified |
| NOISE-4004-H | Duplicate source record | Escalated to data steward |
| NOISE-5762-C | Data quality insufficient | Manual review scheduled |
| NOISE-8321-F | Pending validation | Business owner notified |
| NOISE-2496-D | Data quality insufficient | Manual review scheduled |
| NOISE-4965-F | Pending validation | Manual review scheduled |
| NOISE-9587-F | Duplicate source record | Business owner notified |
| NOISE-1777-H | Out of scope per business decision | Business owner notified |
| NOISE-7040-C | Data quality insufficient | Business owner notified |
| NOISE-3228-A | Duplicate source record | Deferred to Phase 2 |
| NOISE-3136-C | Data quality insufficient | Deferred to Phase 2 |
| NOISE-6311-G | Duplicate source record | Manual review scheduled |
| NOISE-7596-D | Data quality insufficient | Business owner notified |
| NOISE-5296-C | Pending validation | Deferred to Phase 2 |
| NOISE-8977-D | Data quality insufficient | Manual review scheduled |
| NOISE-1400-C | Missing required attributes | Manual review scheduled |
| NOISE-1849-D | Out of scope per business decision | Manual review scheduled |
| NOISE-7541-F | Pending validation | Deferred to Phase 2 |
| NOISE-8020-F | Pending validation | Manual review scheduled |
| NOISE-7236-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-4215-B | Duplicate source record | Deferred to Phase 2 |
| NOISE-5470-C | Data quality insufficient | Business owner notified |
| NOISE-5877-E | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-5548-A | Pending validation | Deferred to Phase 2 |
| NOISE-3397-E | Pending validation | Deferred to Phase 2 |
| NOISE-7942-H | Missing required attributes | Escalated to data steward |
| NOISE-3080-F | Duplicate source record | Escalated to data steward |
| NOISE-6589-E | Missing required attributes | Business owner notified |
| NOISE-2966-A | Pending validation | Business owner notified |
| NOISE-8832-F | Duplicate source record | Manual review scheduled |
| NOISE-7409-F | Duplicate source record | Business owner notified |
| NOISE-4352-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-2458-F | Data quality insufficient | Manual review scheduled |
| NOISE-2157-D | Duplicate source record | Manual review scheduled |
| NOISE-7199-C | Duplicate source record | Business owner notified |
| NOISE-5999-A | Out of scope per business decision | Manual review scheduled |
| NOISE-8839-C | Data quality insufficient | Manual review scheduled |
| NOISE-2875-E | Data quality insufficient | Business owner notified |
| NOISE-9641-B | Missing required attributes | Business owner notified |
| NOISE-2232-B | Missing required attributes | Business owner notified |
| NOISE-9841-B | Duplicate source record | Manual review scheduled |
| NOISE-8840-F | Duplicate source record | Business owner notified |
| NOISE-4918-C | Data quality insufficient | Business owner notified |
| NOISE-3572-A | Data quality insufficient | Business owner notified |
| NOISE-8608-D | Data quality insufficient | Escalated to data steward |
| NOISE-8140-C | Missing required attributes | Manual review scheduled |
| NOISE-8054-E | Out of scope per business decision | Manual review scheduled |
| NOISE-8635-F | Data quality insufficient | Manual review scheduled |
| NOISE-1878-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-1938-A | Duplicate source record | Business owner notified |
| NOISE-5993-E | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1343-D | Duplicate source record | Deferred to Phase 2 |
| NOISE-4861-D | Duplicate source record | Manual review scheduled |
| NOISE-6857-F | Duplicate source record | Business owner notified |
| NOISE-5162-E | Out of scope per business decision | Manual review scheduled |
| NOISE-3914-E | Missing required attributes | Escalated to data steward |
| NOISE-9484-A | Missing required attributes | Escalated to data steward |
| NOISE-9972-F | Duplicate source record | Deferred to Phase 2 |
| NOISE-2362-A | Duplicate source record | Business owner notified |
| NOISE-4952-D | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2394-F | Missing required attributes | Business owner notified |
| NOISE-5496-C | Data quality insufficient | Manual review scheduled |
| NOISE-7458-G | Duplicate source record | Business owner notified |
| NOISE-2237-A | Data quality insufficient | Manual review scheduled |
| NOISE-3957-H | Pending validation | Manual review scheduled |
| NOISE-6308-G | Out of scope per business decision | Escalated to data steward |
| NOISE-6560-A | Pending validation | Escalated to data steward |
| NOISE-5965-H | Duplicate source record | Escalated to data steward |
| NOISE-5171-E | Duplicate source record | Escalated to data steward |
| NOISE-5821-D | Missing required attributes | Escalated to data steward |
| NOISE-6932-H | Pending validation | Manual review scheduled |
| NOISE-6243-D | Out of scope per business decision | Manual review scheduled |
| NOISE-1746-E | Pending validation | Manual review scheduled |
| NOISE-7310-H | Pending validation | Business owner notified |
| NOISE-5179-G | Duplicate source record | Business owner notified |
| NOISE-2201-F | Out of scope per business decision | Business owner notified |
| NOISE-9924-H | Pending validation | Business owner notified |
| NOISE-3547-F | Data quality insufficient | Manual review scheduled |
| NOISE-9058-C | Duplicate source record | Escalated to data steward |
| NOISE-8702-A | Duplicate source record | Manual review scheduled |
| NOISE-7431-E | Pending validation | Manual review scheduled |
| NOISE-1846-E | Pending validation | Manual review scheduled |
| NOISE-3616-A | Missing required attributes | Business owner notified |
| NOISE-4356-H | Missing required attributes | Escalated to data steward |
| NOISE-1343-E | Missing required attributes | Escalated to data steward |
| NOISE-3582-H | Missing required attributes | Deferred to Phase 2 |
| NOISE-5895-F | Out of scope per business decision | Business owner notified |
| NOISE-1731-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8296-C | Missing required attributes | Manual review scheduled |
| NOISE-9293-F | Data quality insufficient | Escalated to data steward |
| NOISE-3004-D | Pending validation | Deferred to Phase 2 |
| NOISE-7574-C | Missing required attributes | Manual review scheduled |
| NOISE-8957-D | Missing required attributes | Escalated to data steward |
| NOISE-6189-B | Out of scope per business decision | Manual review scheduled |
| NOISE-5338-E | Duplicate source record | Manual review scheduled |
| NOISE-6252-C | Duplicate source record | Business owner notified |
| NOISE-3059-C | Pending validation | Escalated to data steward |
| NOISE-9592-A | Pending validation | Manual review scheduled |
| NOISE-3120-B | Out of scope per business decision | Business owner notified |
| NOISE-1880-F | Duplicate source record | Escalated to data steward |
| NOISE-5806-A | Missing required attributes | Business owner notified |
| NOISE-4931-F | Data quality insufficient | Manual review scheduled |
| NOISE-2991-B | Pending validation | Business owner notified |
| NOISE-3884-E | Data quality insufficient | Escalated to data steward |
| NOISE-9937-F | Out of scope per business decision | Manual review scheduled |
| NOISE-5044-H | Missing required attributes | Manual review scheduled |
| NOISE-6254-E | Pending validation | Deferred to Phase 2 |
| NOISE-6281-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-3004-G | Missing required attributes | Deferred to Phase 2 |
| NOISE-2354-B | Duplicate source record | Business owner notified |
| NOISE-8204-F | Out of scope per business decision | Escalated to data steward |
| NOISE-5601-C | Data quality insufficient | Manual review scheduled |
| NOISE-2116-D | Pending validation | Escalated to data steward |
| NOISE-6585-E | Duplicate source record | Manual review scheduled |
| NOISE-2763-H | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-8951-G | Missing required attributes | Escalated to data steward |
| NOISE-7860-E | Duplicate source record | Deferred to Phase 2 |
| NOISE-5106-A | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-9616-E | Missing required attributes | Escalated to data steward |
| NOISE-3990-C | Data quality insufficient | Manual review scheduled |
| NOISE-1791-F | Out of scope per business decision | Escalated to data steward |
| NOISE-2881-G | Out of scope per business decision | Business owner notified |
| NOISE-6234-B | Duplicate source record | Business owner notified |
| NOISE-2467-F | Pending validation | Deferred to Phase 2 |
| NOISE-8274-A | Duplicate source record | Manual review scheduled |
| NOISE-9014-G | Data quality insufficient | Deferred to Phase 2 |
| NOISE-8139-A | Pending validation | Business owner notified |
| NOISE-4484-A | Data quality insufficient | Business owner notified |
| NOISE-5849-E | Data quality insufficient | Business owner notified |
| NOISE-2194-E | Duplicate source record | Business owner notified |
| NOISE-1993-H | Out of scope per business decision | Manual review scheduled |
| NOISE-7861-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-2904-C | Out of scope per business decision | Manual review scheduled |
| NOISE-6552-A | Pending validation | Manual review scheduled |
| NOISE-8690-C | Data quality insufficient | Business owner notified |
| NOISE-1886-A | Out of scope per business decision | Business owner notified |
| NOISE-3601-D | Missing required attributes | Manual review scheduled |
| NOISE-3371-G | Pending validation | Escalated to data steward |
| NOISE-9835-C | Missing required attributes | Escalated to data steward |
| NOISE-3170-C | Missing required attributes | Business owner notified |
| NOISE-8320-A | Pending validation | Escalated to data steward |
| NOISE-1878-B | Pending validation | Deferred to Phase 2 |
| NOISE-8278-D | Missing required attributes | Escalated to data steward |
| NOISE-9300-C | Pending validation | Manual review scheduled |
| NOISE-2987-F | Pending validation | Business owner notified |
| NOISE-2245-A | Missing required attributes | Deferred to Phase 2 |
| NOISE-1393-C | Missing required attributes | Escalated to data steward |
| NOISE-8382-F | Pending validation | Manual review scheduled |
| NOISE-5522-D | Missing required attributes | Manual review scheduled |
| NOISE-1310-C | Missing required attributes | Deferred to Phase 2 |
| NOISE-9450-G | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-4151-A | Data quality insufficient | Business owner notified |
| NOISE-2480-A | Data quality insufficient | Deferred to Phase 2 |
| NOISE-1828-B | Pending validation | Deferred to Phase 2 |
| NOISE-7683-D | Out of scope per business decision | Deferred to Phase 2 |
| NOISE-7924-B | Pending validation | Escalated to data steward |
| NOISE-6910-H | Missing required attributes | Business owner notified |
| NOISE-4336-C | Pending validation | Manual review scheduled |
| NOISE-7884-G | Pending validation | Deferred to Phase 2 |
| NOISE-3493-A | Duplicate source record | Manual review scheduled |
| NOISE-9501-E | Pending validation | Deferred to Phase 2 |
| NOISE-5392-B | Data quality insufficient | Escalated to data steward |
| NOISE-5744-F | Missing required attributes | Manual review scheduled |
| NOISE-4447-A | Pending validation | Manual review scheduled |
| NOISE-3337-E | Out of scope per business decision | Business owner notified |


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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230728_000000`
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
| Technical Lead | James Wilson (Finance) | james@company.com | +1-555-0102 |
| Business Owner | Maria Garcia (Supply Chain) | maria@company.com | +1-555-0103 |
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
