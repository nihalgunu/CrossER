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
- [x] Mapping rules approved by business owners
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
|   SOURCE       |     |   ETL Layer      |     |   TARGET       |
|   (Source)       | --> |   (Integration)  | --> |   (Target)       |
+------------------+     +------------------+     +------------------+
        |                        |                        |
        v                        v                        v
+------------------+     +------------------+     +------------------+
|   Source DB      |     |   Staging DB     |     |   Target DB      |
+------------------+     +------------------+     +------------------+
```

### Integration Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| Extract | Custom Python | Pull data from source APIs |
| Transform | Apache Spark | Data cleansing and mapping |
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
- Individual mapping rule validation
- Data type conversion verification
- Null handling tests

#### Phase 2: Integration Testing
- End-to-end data flow validation
- Cross-system reference integrity
- API compatibility tests

#### Phase 3: User Acceptance Testing
- Business scenario validation
- Report reconciliation
- Workflow continuity

### Test Data Summary

| Entity Type | Source Count | Migrated | Validated | Status |
|-------------|--------------|----------|-----------|--------|
| Products | 2,450 | 2,450 | 2,448 | 99.9% |
| Suppliers | 1,200 | 1,198 | 1,198 | 99.8% |
| Legal Entities | 350 | 350 | 350 | 100% |
| Tax Codes | 180 | 180 | 180 | 100% |

### Known Issues

1. Two product records require manual review due to duplicate detection
2. Supplier payment terms converted using default values where missing
3. Historical transaction links preserved via cross-reference table

## Section 4: Data Migration Details

### 4.1 Scope Overview

This section documents the entity mappings established during the migration from
SOURCE to TARGET. All mappings have been validated by the
data stewardship team unless otherwise noted.

### 4.2 Migration Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1488 | Completed |
| Successfully mapped | 1098 | Verified |
| Excluded from scope | 329 | Documented |
| Manual review required | 6 | In Progress |

### 4.3 Entity Mapping Reference

#### 4.3.1 Mapping Methodology

Entities were mapped using the following prioritized matching criteria:
1. Exact internal code match (highest confidence)
2. Product specification match (concentration, grade, category)
3. Historical transaction correlation
4. Manual expert review (lowest volume, highest accuracy)

#### 4.3.2 Validated Entity Mappings

The following mappings have been verified by the data governance team and are
considered authoritative for system-of-record purposes. Each mapping includes
the source entity identifier, target entity identifier, and verification notes.

| Source Code (SOURCE) | Target Code (TARGET) | Verification | Notes |
|------------------------------|------------------------------|--------------|-------|
| Vertex Rohstoffe | CE-PR-134 | unverified | Confirmed by domain expert |
| Vat Standardqualität NL 25% | EX-N-21-396 | unverified | Historical match confirmed |
| SIG-61-MHS-BQG3 | Sorbinsäure 25% Standardqualität | pending_review | Verified via product specs |
| Coconut Oil 98% | SIG-36-TML-VS0J | unverified | Cross-referenced with transactions |
| Horizon Ingredients International | SIG-39-CCW-1KX2 | unverified | Cross-referenced with transactions |
| soy isolate | SIG-56-BPD-M0A6 | pending_review | Confirmed by domain expert |
| withholding gb 5% | WI-F-5-421 | unverified | Cross-referenced with transactions |
| elite partners | VE-IN-631 Ltd. | unverified | Auto-mapped, validated |
| Coconut Oil 70% | Lactic Acid 50% Premium | auto_generated | Cross-referenced with transactions |
| Elite Solutions | Nordic Partners | unverified | Auto-mapped, validated |
| SIG-10-KDB-LGYT | Isoglucose 70% | auto_generated | Historical match confirmed |
| ascorbic acid premium | Pea Protein Premium | pending_review | Verified via product specs |
| Vat Standardqualität FR 0% | customs duty de 0% | pending_review | Confirmed by domain expert |
| sodium benzoate 99.5% premium | Kaliumsorbat Standardqualität | auto_generated | Confirmed by domain expert |
| SIG-77-AEN-CA8D | Vat Standardqualität FR 10% | auto_generated | Verified via product specs |
| Vat Standardqualität US 10% | Vat Reduced CN 0% | auto_generated | Historical match confirmed |
| SIG-10-TIC-7Q1D | Palmfett | pending_review | Historical match confirmed |
| Ascorbic Acid 70% | sodium benzoate standard | pending_review | Auto-mapped, validated |
| Ascorbic Acid 98% Pharmazeutisch rein | LA-AC-471 | unverified | Auto-mapped, validated |
| GL-SY-PR-440 | Calcium Carbonate 98% Standard | unverified | Auto-mapped, validated |
| apex sourcing | PR-LO-745 | unverified | Historical match confirmed |
| SIG-88-AGF-FF5L | sunflower oil | auto_generated | Cross-referenced with transactions |
| SIG-80-ZKZ-ANXJ | vat reduced gb 25% | pending_review | Cross-referenced with transactions |
| Resistente Stärke | palm oil tech grade | auto_generated | Verified via product specs |
| rapeseed oil 50% pharma grade | SIG-75-WDP-0BHF | unverified | Historical match confirmed |
| atlantic supply | Prism Logistics | auto_generated | Cross-referenced with transactions |
| Baltic Industries BV | Nexus Partners | auto_generated | Cross-referenced with transactions |
| SO-CH-98-657 | Sonnenblumenöl Technische Qualität | auto_generated | Confirmed by domain expert |
| potassium sorbate food grade | SO-IS-25-323 | auto_generated | Verified via product specs |
| Ascorbic Acid Food Grade | Sorbinsäure 50% Lebensmittelrein | unverified | Cross-referenced with transactions |
| Cyclodextrin | Citric Acid Premium | auto_generated | Auto-mapped, validated |
| ME-LO-670 | Vanguard Werkstoffe | pending_review | Cross-referenced with transactions |
| sorbic acid 70% | Lactic Acid Food Grade | auto_generated | Cross-referenced with transactions |
| SIG-57-HAE-WNSM | Citric Acid 99.5% | auto_generated | Cross-referenced with transactions |
| Kaliumsorbat Qualitätsstufe II | SIG-72-YEU-SCIQ | unverified | Auto-mapped, validated |
| SIG-91-FOC-36I6 | AS-AC-99.5-TE-765 | auto_generated | Confirmed by domain expert |
| Lactic Acid 99.5% Grade B | Lactic Acid 98% | auto_generated | Historical match confirmed |
| GL-SY-98-FO-GR-198 | ascorbic acid 70% | auto_generated | Confirmed by domain expert |
| Pacific Materials | AT-MA-739 | pending_review | Auto-mapped, validated |
| SIG-61-FGJ-AO1L NV | Pacific Supply | auto_generated | Auto-mapped, validated |
| lactic acid standard | SIG-82-VDF-0XQT | pending_review | Cross-referenced with transactions |
| Excise DE 10% | SIG-39-MGB-86C4 | auto_generated | Historical match confirmed |
| Vat Standard GB 19% | excise cn 19% | pending_review | Cross-referenced with transactions |
| Citric Acid 99.5% | SIG-16-MLJ-HWA7 | auto_generated | Historical match confirmed |
| Atlantic Rohstoffe GmbH | Horizon Distribution Holdings | auto_generated | Historical match confirmed |
| Dextrin 25% Premiumqualität | Lactic Acid Grade B | unverified | Historical match confirmed |
| SIG-69-BWM-8WBG | atlas materials | unverified | Auto-mapped, validated |
| ascorbic acid pharma grade | SIG-63-JJG-1TCH | unverified | Cross-referenced with transactions |
| Meridian Versorgung | meridian trading Group | unverified | Verified via product specs |
| AS-AC-130 | Weizenklebereiweiß 99.5% | pending_review | Cross-referenced with transactions |
| SIG-27-MIG-RYBN | Premier Versorgung GmbH | auto_generated | Confirmed by domain expert |
| Calcium Carbonate 50% Pharma Grade | SIG-47-NVU-R3XU | pending_review | Verified via product specs |
| apex logistics | Nexus Sourcing | unverified | Confirmed by domain expert |
| vat standard gb 21% | Vat Reduced BR 7% | auto_generated | Verified via product specs |
| Coconut Oil 25% Technical | ascorbic acid | unverified | Auto-mapped, validated |
| global enterprise NV | GL-LO-196 NV | auto_generated | Verified via product specs |
| SIG-37-MXA-3C7Q | Lactic Acid 98% Qualitätsstufe I | unverified | Verified via product specs |
| SIG-97-OGU-PBXC | Weizenklebereiweiß 25% Premiumqualität | pending_review | Auto-mapped, validated |
| SIG-99-GVJ-VPM6 | fructose standard | auto_generated | Verified via product specs |
| SO-IS-99.5-PR-187 | SIG-56-BPD-M0A6 | pending_review | Historical match confirmed |
| ZE-PA-718 LLC | Atlantic Chemicals SAS | auto_generated | Auto-mapped, validated |
| SIG-78-AVK-U9PX | Sodium Chloride Technical | auto_generated | Verified via product specs |
| citric acid | SIG-60-IRZ-OTKZ | unverified | Historical match confirmed |
| SIG-69-OFZ-JW34 | ascorbic acid | auto_generated | Confirmed by domain expert |
| Natriumbenzoat | SIG-29-BJH-NXI0 | auto_generated | Historical match confirmed |
| SIG-79-OZQ-4I2N | MA-DE-585 | auto_generated | Auto-mapped, validated |
| excise in 25% | SIG-51-VAV-WAKJ | auto_generated | Historical match confirmed |
| SIG-75-GGJ-DK9O | Meridian Sourcing | auto_generated | Confirmed by domain expert |
| SIG-16-MNF-F4AF | LA-AC-50-PR-288 | auto_generated | Auto-mapped, validated |
| PI-LO-946 | Horizon Partners International | auto_generated | Historical match confirmed |
| sorbic acid 50% food grade | SIG-93-FDC-Q685 | unverified | Auto-mapped, validated |
| Nexus Werkstoffe | CA-MA-271 | auto_generated | Verified via product specs |
| Wheat Gluten | SIG-41-FFO-RXYJ | pending_review | Verified via product specs |
| Wheat Gluten Grade B | PO-SO-604 | unverified | Historical match confirmed |
| SIG-45-QQC-Z4N0 | excise nl 20% | unverified | Historical match confirmed |
| RA-OI-FO-GR-269 | Calcium Carbonate 99.5% | auto_generated | Historical match confirmed |
| SIG-88-KUG-5ITD | Fructose | auto_generated | Verified via product specs |
| DE-635 | SIG-57-NGZ-ILDZ | pending_review | Cross-referenced with transactions |
| Ascorbic Acid 99.5% Premiumqualität | SO-CH-TE-304 | pending_review | Verified via product specs |
| PA-MA-166 SARL | Elite Versorgung SA | pending_review | Confirmed by domain expert |
| SIG-87-LPT-3ADB | Core Sourcing | unverified | Confirmed by domain expert |
| dextrose premium | Dextrin Technical | auto_generated | Historical match confirmed |
| PR-CH-334 GmbH | SIG-98-SID-2107 GmbH | auto_generated | Auto-mapped, validated |
| Sodium Chloride | Weizenklebereiweiß | auto_generated | Cross-referenced with transactions |
| Maltodextrin DE18 Pharma Grade | SIG-80-QNF-AHPO | unverified | Cross-referenced with transactions |
| Coconut Oil 70% Grade A | fructose 99.5% pharma grade | auto_generated | Verified via product specs |
| stellar logistics | ST-SO-771 | auto_generated | Confirmed by domain expert |
| Calcium Carbonate Qualitätsstufe II | Ascorbic Acid Technical | auto_generated | Auto-mapped, validated |
| Catalyst Commodities SAS | QU-PA-832 NV | pending_review | Auto-mapped, validated |
| GL-SY-98-939 | Potassium Sorbate | unverified | Verified via product specs |
| sodium benzoate 98% | Resistant Starch 98% | pending_review | Cross-referenced with transactions |
| prism ingredients | AT-SU-435 KG | auto_generated | Verified via product specs |
| FR-50-ST-938 | Kaliumsorbat Premiumqualität | unverified | Confirmed by domain expert |
| casein premium | Kasein Pharmazeutisch rein | auto_generated | Cross-referenced with transactions |
| Palm Oil 70% Premium | Kaliumsorbat | unverified | Auto-mapped, validated |
| Vat Reduced BR 25% | EX-C-25-332 | pending_review | Cross-referenced with transactions |
| sorbic acid 98% | Lactic Acid 25% Premium | auto_generated | Historical match confirmed |
| Casein Standard | soy isolate premium | unverified | Verified via product specs |
| Prism Industrien Holdings | Atlas Logistics International | unverified | Auto-mapped, validated |
| Ascorbic Acid Premiumqualität | resistant starch 25% tech grade | unverified | Auto-mapped, validated |
| Rapsöl 70% Qualitätsstufe II | AS-AC-ST-686 | unverified | Cross-referenced with transactions |
| SIG-10-PGH-BTUF | AT-SO-339 | auto_generated | Confirmed by domain expert |
| Baltic Ingredients | ST-TR-590 | pending_review | Historical match confirmed |
| Sorbic Acid Food Grade | dextrose | auto_generated | Verified via product specs |
| Continental Enterprise KG | Premier Solutions | unverified | Cross-referenced with transactions |
| Dextrin | SIG-40-NOU-7O0G | pending_review | Historical match confirmed |
| Ascorbic Acid 99.5% Premiumqualität | SIG-66-RQA-05UV | unverified | Cross-referenced with transactions |
| SIG-20-OAV-1IKJ | Calcium Carbonate 99.5% | unverified | Confirmed by domain expert |
| Central Logistik | NE-SO-652 | auto_generated | Historical match confirmed |
| SO-BE-PR-691 | resistant starch standard | pending_review | Cross-referenced with transactions |
| Excise NL 20% | Vat Standardqualität GB 19% | unverified | Verified via product specs |
| premier logistics | SIG-96-POT-WDYM | auto_generated | Auto-mapped, validated |
| Isoglucose 70% Lebensmittelrein | PO-SO-FO-GR-989 | auto_generated | Cross-referenced with transactions |
| Withholding US 25% | Customs Duty DE 15% | unverified | Verified via product specs |
| PA-MA-412 GmbH | Atlas Logistics International | unverified | Auto-mapped, validated |
| Vat Standard CN 0% | Excise BR 5% | pending_review | Cross-referenced with transactions |
| Natriumbenzoat Pharmazeutisch rein | Citric Acid Premium | auto_generated | Cross-referenced with transactions |
| Nordic Manufacturing NV | central manufacturing NV | auto_generated | Auto-mapped, validated |
| casein 98% standard | Coconut Oil 70% Qualitätsstufe I | auto_generated | Historical match confirmed |
| RA-OI-98-117 | SIG-29-KJI-GJKC | pending_review | Cross-referenced with transactions |
| SIG-58-NYA-2O4M | sorbic acid 25% pharma grade | auto_generated | Cross-referenced with transactions |
| SO-BE-964 | dextrose 70% | pending_review | Cross-referenced with transactions |
| SU-OI-70-FO-GR-432 | SIG-25-ABB-2SBA | unverified | Confirmed by domain expert |
| SIG-84-MGK-H2ME | Sodium Chloride | pending_review | Verified via product specs |
| SIG-11-AEJ-CHNJ | Traubenzucker 25% | pending_review | Confirmed by domain expert |
| dextrose tech grade | SO-BE-964 | unverified | Verified via product specs |
| Casein 25% Grade B | SO-AC-490 | pending_review | Auto-mapped, validated |
| Ascorbic Acid 50% Technische Qualität | DE-70-769 | unverified | Verified via product specs |
| Rapsöl Qualitätsstufe I | Soy Isolate Grade A | pending_review | Historical match confirmed |
| Pea Protein 70% Premiumqualität | Rapeseed Oil Technical | auto_generated | Historical match confirmed |
| customs duty fr 19% | Vat Standard US 21% | pending_review | Auto-mapped, validated |
| citric acid | Sodium Benzoate 99.5% Grade A | unverified | Cross-referenced with transactions |
| AP-MA-498 | Stratos Sourcing | auto_generated | Verified via product specs |
| SIG-14-GCI-G4Q9 | Continental Sourcing | unverified | Historical match confirmed |
| sodium benzoate 98% pharma grade | Traubenzucker Qualitätsstufe I | pending_review | Cross-referenced with transactions |
| Sunflower Oil Grade A | sunflower oil 70% | auto_generated | Auto-mapped, validated |
| Vanguard Chemicals SAS | SIG-23-WOJ-YTND International | pending_review | Verified via product specs |
| CE-MA-720 | Nexus Logistik | pending_review | Historical match confirmed |
| Palmfett Lebensmittelrein | casein | pending_review | Confirmed by domain expert |
| Cyclodextrin Food Grade | potassium sorbate | pending_review | Verified via product specs |
| SIG-56-FFG-XS2P | Global Logistics | auto_generated | Historical match confirmed |
| Ascorbic Acid | resistant starch tech grade | pending_review | Cross-referenced with transactions |
| Prism Supply Co. | PR-MA-367 | auto_generated | Confirmed by domain expert |
| prime solutions | Vertex Ingredients | auto_generated | Auto-mapped, validated |
| AT-CO-808 GmbH | Global Processing Holdings | auto_generated | Historical match confirmed |
| customs duty us 15% | Vat Reduced CN 0% | unverified | Confirmed by domain expert |
| SIG-16-MLJ-HWA7 | dextrose | auto_generated | Auto-mapped, validated |
| Stratos Sourcing | SIG-14-XJN-JI7U | pending_review | Cross-referenced with transactions |
| coconut oil | SIG-37-PEJ-WFOY | auto_generated | Confirmed by domain expert |
| Withholding NL 21% | Customs Duty FR 7% | auto_generated | Confirmed by domain expert |
| SIG-12-ANK-TJ9A | Ascorbic Acid 50% | unverified | Confirmed by domain expert |
| central logistics International | Atlas Chemicals SARL | unverified | Cross-referenced with transactions |
| VA-DI-229 | Catalyst Versorgung International | pending_review | Auto-mapped, validated |
| Lactic Acid 25% Lebensmittelrein | Dextrose Standard | unverified | Auto-mapped, validated |
| Natriumbenzoat Technische Qualität | Coconut Oil 50% | pending_review | Confirmed by domain expert |
| pea protein | Lactic Acid 70% | auto_generated | Verified via product specs |
| citric acid | SIG-82-UKB-5LXO | auto_generated | Verified via product specs |
| DE-98-512 | SIG-44-QME-TTIM | pending_review | Historical match confirmed |
| Dextrin 98% | Traubenzucker | unverified | Verified via product specs |
| SIG-78-TUT-T3NS | Nordic Vertrieb | unverified | Verified via product specs |
| Zitronensäure Qualitätsstufe II | Glucose Syrup 98% Standard | unverified | Verified via product specs |
| maltodextrin de30 | SO-IS-PH-GR-671 | pending_review | Verified via product specs |
| Atlantic Rohstoffe International | CE-LO-567 AG | auto_generated | Cross-referenced with transactions |
| SIG-80-QLX-7SNL SAS | nexus distribution Ltd. | auto_generated | Historical match confirmed |
| rapeseed oil | IS-50-TE-886 | unverified | Confirmed by domain expert |
| dextrose | SIG-89-JZC-1682 | unverified | Cross-referenced with transactions |
| Coconut Oil | PO-SO-99.5-897 | unverified | Auto-mapped, validated |
| vat standard br 7% | VA-RE-G-15-665 | pending_review | Auto-mapped, validated |
| vat standard fr 0% | Excise BR 5% | pending_review | Confirmed by domain expert |
| resistant starch 70% standard | SIG-11-QDU-30PE | pending_review | Historical match confirmed |
| Excise NL 19% | excise gb 0% | auto_generated | Historical match confirmed |
| CU-DU-B-15-686 | customs duty de 0% | auto_generated | Auto-mapped, validated |
| Customs Duty BR 21% | WI-U-10-721 | unverified | Auto-mapped, validated |
| CA-GR-A-380 | Kaliumsorbat Pharmazeutisch rein | unverified | Verified via product specs |
| SO-AC-99.5-338 | SIG-20-BPG-W8VL | auto_generated | Auto-mapped, validated |
| SIG-29-XAN-WDDA | Global Sourcing | unverified | Confirmed by domain expert |
| LA-AC-TE-651 | Coconut Oil 50% Technische Qualität | unverified | Confirmed by domain expert |
| Sorbinsäure 50% | SIG-38-YTD-7BST | pending_review | Auto-mapped, validated |
| SU-OI-98-PR-692 | SIG-68-SYL-8192 | auto_generated | Confirmed by domain expert |
| Coconut Oil Pharma Grade | SIG-21-EAX-PC8Q | pending_review | Verified via product specs |
| Withholding GB 21% | Vat Standardqualität GB 15% | pending_review | Verified via product specs |
| SIG-88-RKE-8R7A | Maltodextrin DE5 Grade A | unverified | Verified via product specs |
| Baltic Solutions | Nexus Enterprise Group | pending_review | Auto-mapped, validated |
| VE-CH-841 Group | prism industries Corp. | auto_generated | Verified via product specs |
| Natriumbenzoat 99.5% Technische Qualität | Pea Protein 50% | pending_review | Cross-referenced with transactions |
| CI-AC-70-FO-GR-198 | SIG-60-WEX-2G05 | unverified | Historical match confirmed |
| excise br 25% | Customs Duty GB 5% | unverified | Confirmed by domain expert |
| RA-OI-25-FO-GR-966 | Citric Acid Food Grade | auto_generated | Verified via product specs |
| pea protein 25% pharma grade | Maltodextrin DE20 | pending_review | Confirmed by domain expert |
| SIG-86-VCP-SVOL | resistant starch | unverified | Auto-mapped, validated |
| excise de 21% | Vat Standardqualität NL 5% | pending_review | Cross-referenced with transactions |
| coconut oil 98% premium | AS-AC-PR-308 | auto_generated | Auto-mapped, validated |
| RA-OI-FO-GR-269 | Zitronensäure Qualitätsstufe I | unverified | Verified via product specs |
| SIG-71-CWF-DGP5 | cyclodextrin 98% pharma grade | unverified | Confirmed by domain expert |
| atlas supply | SIG-24-YWL-8DWF | auto_generated | Auto-mapped, validated |
| NO-CO-357 International | Stratos Supply | pending_review | Cross-referenced with transactions |
| Maltodextrin DE25 | palm oil pharma grade | auto_generated | Verified via product specs |
| SO-CH-PR-862 | SIG-91-WVE-3ESP | unverified | Confirmed by domain expert |
| Wheat Gluten Grade B | dextrose | pending_review | Verified via product specs |
| Maltodextrin DE10 | Sorbinsäure Lebensmittelrein | unverified | Verified via product specs |
| Resistant Starch Technical | Maltodextrin-Pulver DE20 | pending_review | Verified via product specs |
| Stratos Chemicals | SIG-34-TUW-UWNZ Group | auto_generated | Historical match confirmed |
| Apex Sourcing | Catalyst Logistics | pending_review | Verified via product specs |
| SIG-98-XJT-L879 | Dextrin 50% | auto_generated | Confirmed by domain expert |
| SIG-36-XEW-9SSB | Ascorbic Acid Standard | pending_review | Confirmed by domain expert |
| SIG-21-VZE-Q2WM | vat standard nl 20% | auto_generated | Auto-mapped, validated |
| Resistente Stärke Standardqualität | Potassium Sorbate Technical | auto_generated | Historical match confirmed |
| Ascorbic Acid 98% Qualitätsstufe II | dextrin standard | auto_generated | Historical match confirmed |
| Glukosesirup Syrup Lebensmittelrein | SIG-57-YNB-5KMT | pending_review | Auto-mapped, validated |
| Baltic Trading Holdings | nordic partners | auto_generated | Auto-mapped, validated |
| SIG-60-WEX-2G05 | Ascorbic Acid Premiumqualität | auto_generated | Confirmed by domain expert |
| SIG-32-UBB-EMYO | WI-F-5-102 | auto_generated | Auto-mapped, validated |
| withholding br 10% | Customs Duty GB 0% | auto_generated | Cross-referenced with transactions |
| SIG-38-YTD-7BST | RA-OI-GR-B-834 | auto_generated | Verified via product specs |
| CA-CO-128 SAS | Horizon Rohstoffe PLC | pending_review | Confirmed by domain expert |
| SIG-87-OKN-L3O4 | Elite Trading | auto_generated | Historical match confirmed |
| Quantum Versorgung GmbH | SIG-43-FST-BKJ7 | auto_generated | Auto-mapped, validated |
| sodium chloride 99.5% premium | SIG-79-RKA-P64T | pending_review | Historical match confirmed |
| Meridian Werkstoffe Corp. | Pinnacle Materials SA | pending_review | Verified via product specs |
| SIG-95-LOJ-S1L2 | EX-U-20-144 | pending_review | Verified via product specs |
| coconut oil standard | Maltodextrin-Pulver DE5 Lebensmittelrein | unverified | Historical match confirmed |
| Potassium Sorbate 25% Pharma Grade | RA-OI-98-117 | pending_review | Confirmed by domain expert |
| meridian distribution Holdings | BA-MA-518 Group | auto_generated | Historical match confirmed |
| ZE-PA-511 PLC | Premier Versorgung PLC | auto_generated | Confirmed by domain expert |
| fructose 99.5% food grade | Natriumbenzoat 99.5% Technische Qualität | unverified | Verified via product specs |
| SIG-13-FTX-P5F3 | Sorbinsäure Premiumqualität | pending_review | Verified via product specs |
| Cyclodextrin | SIG-39-QZD-93EZ | auto_generated | Cross-referenced with transactions |
| Calcium Carbonate 70% Premiumqualität | SIG-92-CZO-O9ON | unverified | Verified via product specs |
| Atlantic Materials | meridian supply | unverified | Auto-mapped, validated |
| Pinnacle Sourcing | Continental Sourcing | unverified | Confirmed by domain expert |
| Meridian Sourcing | Elite Supply Co. | auto_generated | Historical match confirmed |
| Vanguard Chemicals SAS | SIG-79-GUR-O5DB NV | pending_review | Verified via product specs |
| Core Logistik | SIG-73-YMY-EMYO | auto_generated | Cross-referenced with transactions |
| Coconut Oil 25% | SIG-67-VXU-FPWB | auto_generated | Confirmed by domain expert |
| Ascorbic Acid Technical | RA-OI-258 | pending_review | Confirmed by domain expert |
| SIG-15-NIP-N1UH | Resistant Starch 99.5% | auto_generated | Auto-mapped, validated |
| fructose standard | Casein 25% Grade A | unverified | Confirmed by domain expert |
| AS-AC-413 | resistant starch food grade | auto_generated | Verified via product specs |
| Withholding GB 5% | SIG-74-EPP-R9AG | pending_review | Auto-mapped, validated |
| SIG-42-XLZ-4BOM | sodium benzoate | unverified | Auto-mapped, validated |
| AP-MA-145 International | vertex logistics PLC | unverified | Historical match confirmed |
| Prism Chemicals KG | SIG-54-QHS-YUMN | pending_review | Verified via product specs |
| NE-LO-125 | Pinnacle Sourcing | pending_review | Auto-mapped, validated |
| Natriumchlorid | calcium carbonate | pending_review | Confirmed by domain expert |
| citric acid premium | Sorbinsäure Lebensmittelrein | unverified | Cross-referenced with transactions |
| continental processing SA | EL-LO-712 SA | auto_generated | Historical match confirmed |
| Dextrose 25% Technical | Kaliumsorbat | auto_generated | Auto-mapped, validated |
| Resistente Stärke | sodium chloride | unverified | Verified via product specs |
| cyclodextrin 70% food grade | SIG-41-FFO-RXYJ | unverified | Confirmed by domain expert |
| SIG-97-SBT-Y595 | Rapsöl 99.5% | pending_review | Cross-referenced with transactions |
| SIG-87-KZL-I3ZY | vat standard nl 20% | unverified | Historical match confirmed |
| SO-IS-99.5-PR-187 | Sodium Benzoate 98% | auto_generated | Cross-referenced with transactions |
| Palm Oil Food Grade | resistant starch standard | unverified | Verified via product specs |
| AS-AC-782 | maltodextrin de15 | unverified | Historical match confirmed |
| Isoglucose 25% Lebensmittelrein | lactic acid 98% premium | unverified | Confirmed by domain expert |
| Coconut Oil 70% Qualitätsstufe I | DE-GR-A-250 | auto_generated | Auto-mapped, validated |
| Sorbic Acid 70% | SIG-42-MEI-2SCI | auto_generated | Historical match confirmed |
| Traubenzucker 70% | Coconut Oil 98% Technical | unverified | Historical match confirmed |
| Lactic Acid | SIG-73-LLJ-LNGI | auto_generated | Verified via product specs |
| SIG-82-ZXL-FF30 International | AT-TR-553 | pending_review | Historical match confirmed |
| Excise NL 21% | VA-ST-F-19-413 | auto_generated | Cross-referenced with transactions |
| SO-AC-852 | Dextrose 70% | auto_generated | Verified via product specs |
| SIG-56-YYA-I8SV | Atlantic Logistics | pending_review | Confirmed by domain expert |
| PR-EN-875 Group | atlas ingredients | pending_review | Historical match confirmed |
| CO-OI-FO-GR-870 | Maltodextrin-Pulver DE25 | unverified | Historical match confirmed |
| Catalyst Enterprise International | SIG-40-JOQ-S1CO KG | unverified | Verified via product specs |
| Isoglucose | DE-GR-A-351 | pending_review | Verified via product specs |
| FR-25-GR-B-641 | SIG-23-UKD-B8UO | auto_generated | Cross-referenced with transactions |
| Prism Versorgung GmbH | SIG-47-MIU-LIH6 | pending_review | Confirmed by domain expert |
| Sodium Benzoate Pharma Grade | Calcium Carbonate 99.5% | pending_review | Confirmed by domain expert |
| VA-RE-G-25-207 | Vat Reduced BR 0% | pending_review | Verified via product specs |
| Traubenzucker 70% Qualitätsstufe I | MA-DE-799 | unverified | Cross-referenced with transactions |
| Prism Materials | Meridian Sourcing | unverified | Verified via product specs |
| nordic supply | Stratos Sourcing | unverified | Confirmed by domain expert |
| Resistente Stärke | Wheat Gluten | auto_generated | Verified via product specs |
| Sonnenblumenöl Qualitätsstufe II | Soy Isolate Grade A | pending_review | Auto-mapped, validated |
| NO-LO-598 Holdings | Nordic Werkstoffe | auto_generated | Auto-mapped, validated |
| vat standard nl 20% | VA-ST-I-20-335 | pending_review | Cross-referenced with transactions |
| atlantic trading | Premier Versorgung PLC | unverified | Verified via product specs |
| SIG-47-YTF-UPMT | ascorbic acid | pending_review | Confirmed by domain expert |
| Vertex Ingredients Ltd. | CO-CH-401 Inc. | auto_generated | Cross-referenced with transactions |
| dextrin | Natriumbenzoat 25% Standardqualität | auto_generated | Cross-referenced with transactions |
| casein | Rapsöl Qualitätsstufe I | pending_review | Historical match confirmed |
| Vanguard Versorgung BV | global enterprise NV | unverified | Verified via product specs |
| SO-AC-98-579 | Calcium Carbonate 98% | pending_review | Historical match confirmed |
| PA-OI-70-GR-B-781 | Glucose Syrup Technical | auto_generated | Verified via product specs |
| SIG-64-BPY-A8RD | Rapeseed Oil Pharma Grade | pending_review | Auto-mapped, validated |
| Horizon Logistics | Vanguard Logistik | auto_generated | Cross-referenced with transactions |
| Sodium Benzoate | MA-DE-GR-A-871 | unverified | Confirmed by domain expert |
| SIG-24-NPE-GDMB | Pea Protein 98% Grade B | unverified | Historical match confirmed |
| SIG-73-UUF-1F99 | DE-70-GR-A-741 | auto_generated | Historical match confirmed |
| Lactic Acid Grade A | CO-OI-25-252 | auto_generated | Verified via product specs |
| meridian trading Group | NE-IN-968 SA | auto_generated | Historical match confirmed |
| Prism Chemicals PLC | premier solutions Corp. | pending_review | Historical match confirmed |
| Citric Acid 70% | SIG-64-BPY-A8RD | unverified | Historical match confirmed |
| Core Chemicals AG | pinnacle trading Inc. | unverified | Cross-referenced with transactions |
| Lactic Acid | Resistant Starch 70% | unverified | Cross-referenced with transactions |
| VA-RE-N-7-243 | SIG-51-ZQJ-AURD | pending_review | Auto-mapped, validated |
| fructose | Weizenklebereiweiß Qualitätsstufe I | auto_generated | Auto-mapped, validated |
| SIG-42-HBL-L3KU International | Stratos Ingredients SARL | auto_generated | Auto-mapped, validated |
| atlantic materials | Pinnacle Materials | pending_review | Confirmed by domain expert |
| SIG-36-UIL-7X71 | potassium sorbate | pending_review | Cross-referenced with transactions |
| Rapsöl 99.5% Technische Qualität | resistant starch 50% | auto_generated | Confirmed by domain expert |
| CY-577 | sunflower oil | auto_generated | Confirmed by domain expert |
| SIG-53-LJE-NZKR | sodium benzoate | unverified | Auto-mapped, validated |
| VE-SO-366 | Apex Werkstoffe | auto_generated | Verified via product specs |
| SO-IS-FO-GR-334 | Dextrose | pending_review | Auto-mapped, validated |
| Kaliumsorbat | WH-GL-FO-GR-876 | auto_generated | Cross-referenced with transactions |
| pinnacle supply | PR-SO-388 | auto_generated | Historical match confirmed |
| isoglucose | Sunflower Oil Grade A | pending_review | Cross-referenced with transactions |
| EX-N-21-216 | excise nl 0% | unverified | Confirmed by domain expert |
| SIG-32-UBB-EMYO | Vat Standard NL 5% | pending_review | Verified via product specs |
| Meridian Werkstoffe | Zenith Supply Co. | unverified | Cross-referenced with transactions |
| excise br 5% | Vat Reduced BR 15% | auto_generated | Cross-referenced with transactions |
| Pinnacle Rohstoffe NV | Continental Chemicals Inc. | auto_generated | Verified via product specs |
| ST-LO-136 | SIG-67-NQK-GXJE | auto_generated | Cross-referenced with transactions |
| Traubenzucker Lebensmittelrein | Isoglucose 70% Food Grade | unverified | Auto-mapped, validated |
| dextrin premium | SIG-41-MCG-8Z79 | auto_generated | Confirmed by domain expert |
| baltic enterprise KG | Catalyst Manufacturing GmbH | auto_generated | Verified via product specs |
| SIG-44-FWT-OA3N | Glukosesirup Syrup | auto_generated | Confirmed by domain expert |
| CA-CA-947 | glucose syrup 98% standard | auto_generated | Verified via product specs |
| Stellar Logistics | CE-LO-713 | pending_review | Auto-mapped, validated |
| Atlas Logistik International | Stratos Enterprise International | unverified | Historical match confirmed |
| withholding nl 15% | Vat Standard BR 0% | unverified | Auto-mapped, validated |
| soy isolate | Calcium Carbonate | pending_review | Confirmed by domain expert |
| pacific supply | EL-SO-199 | pending_review | Verified via product specs |
| resistant starch food grade | SIG-25-ROA-G6G0 | unverified | Auto-mapped, validated |
| QU-SU-CO-959 | Catalyst Sourcing | auto_generated | Historical match confirmed |
| SIG-27-FHX-VO6Y | SO-AC-99.5-338 | auto_generated | Cross-referenced with transactions |
| Cyclodextrin Qualitätsstufe I | Palm Oil 98% Grade A | pending_review | Historical match confirmed |
| SIG-27-QBW-ROGA | glucose syrup 70% food grade | auto_generated | Historical match confirmed |
| SIG-62-AQF-O1V3 | NO-LO-524 | pending_review | Confirmed by domain expert |
| Rapeseed Oil 98% Standard | Rapsöl Technische Qualität | auto_generated | Cross-referenced with transactions |
| Pinnacle Rohstoffe NV | Prism Materials International | unverified | Confirmed by domain expert |
| SIG-59-JAB-QS66 | customs duty de 5% | pending_review | Cross-referenced with transactions |
| Prism Materials International | NE-SO-511 | auto_generated | Confirmed by domain expert |
| nordic logistics Group | Continental Materials | pending_review | Auto-mapped, validated |
| Zitronensäure 50% Qualitätsstufe I | SIG-43-GRJ-P3HT | auto_generated | Confirmed by domain expert |
| Kasein 98% Premiumqualität | WH-GL-944 | unverified | Confirmed by domain expert |
| potassium sorbate | WH-GL-99.5-557 | pending_review | Confirmed by domain expert |
| quantum sourcing | Stratos Supply Co. | pending_review | Cross-referenced with transactions |
| nordic ingredients | Nordic Manufacturing NV | pending_review | Cross-referenced with transactions |
| vat standard nl 19% | SIG-70-QGS-CCAF | pending_review | Confirmed by domain expert |
| SIG-78-WDE-NNV9 | citric acid | auto_generated | Cross-referenced with transactions |
| Nexus Verarbeitung AG | SIG-65-ONA-WQOF Corp. | pending_review | Verified via product specs |
| SIG-17-UCW-S6NB | DE-ST-213 | unverified | Cross-referenced with transactions |
| SIG-57-LIL-I8Z3 Inc. | QU-PR-593 International | auto_generated | Auto-mapped, validated |
| SIG-76-GST-OWGM | Palm Oil 70% Grade B | pending_review | Auto-mapped, validated |
| Zitronensäure 70% | soy isolate 25% | unverified | Verified via product specs |
| AS-AC-70-133 | Coconut Oil Grade A | unverified | Auto-mapped, validated |
| PE-PR-746 | SIG-62-NSC-WV2E | unverified | Cross-referenced with transactions |
| Soy Isolate 99.5% Premium | AS-AC-PH-GR-192 | auto_generated | Confirmed by domain expert |
| FR-98-PR-250 | pea protein 25% | auto_generated | Auto-mapped, validated |
| Nexus Ingredients SARL | CA-SU-512 Holdings | auto_generated | Auto-mapped, validated |
| Palm Oil 25% Grade A | casein pharma grade | unverified | Confirmed by domain expert |
| SIG-36-JLA-CSEN | Natriumchlorid 99.5% | unverified | Auto-mapped, validated |
| Ascorbic Acid 99.5% Technische Qualität | SIG-36-ZKX-4SE4 | pending_review | Cross-referenced with transactions |
| WH-GL-99.5-GR-A-933 | Lactic Acid 98% | auto_generated | Auto-mapped, validated |
| Weizenklebereiweiß Qualitätsstufe II | SIG-52-FHA-5PI2 | unverified | Verified via product specs |
| Dextrose Food Grade | SO-BE-25-982 | unverified | Auto-mapped, validated |
| PR-CO-443 Group | Global Verarbeitung GmbH | pending_review | Historical match confirmed |
| maltodextrin de10 | Isoglucose | auto_generated | Cross-referenced with transactions |
| Glucose Syrup | Maltodextrin-Pulver DE15 Standardqualität | auto_generated | Auto-mapped, validated |
| Soja Isolate | SIG-87-DSD-DF5J | auto_generated | Confirmed by domain expert |
| SIG-79-IKL-24HE | Dextrin 50% | pending_review | Historical match confirmed |
| SIG-24-VMY-QMRL | Vertex Versorgung GmbH | auto_generated | Historical match confirmed |
| Atlas Commodities SAS | NE-IN-874 SA | unverified | Historical match confirmed |
| palm oil 50% premium | Weizenklebereiweiß 98% | pending_review | Confirmed by domain expert |
| SIG-83-JEP-R0ZJ | Ascorbic Acid Food Grade | pending_review | Cross-referenced with transactions |
| Atlas Werkstoffe | NE-SO-810 | unverified | Auto-mapped, validated |
| Baltic Sourcing | EL-SU-CO-921 | auto_generated | Confirmed by domain expert |
| SIG-72-JEH-P5K7 | Palm Oil 50% Premium | pending_review | Auto-mapped, validated |
| CE-MA-720 | Atlas Versorgung GmbH | unverified | Auto-mapped, validated |
| casein standard | SIG-39-DJJ-3SY8 | unverified | Historical match confirmed |
| CE-PR-134 | Horizon Trading | auto_generated | Cross-referenced with transactions |
| RE-ST-GR-B-805 | casein premium | pending_review | Verified via product specs |
| continental processing SA | BA-IN-547 | pending_review | Cross-referenced with transactions |
| SIG-56-FFG-XS2P | Pinnacle Materials SA | pending_review | Cross-referenced with transactions |
| SIG-72-KAT-NI1G | Pacific Werkstoffe | pending_review | Cross-referenced with transactions |
| RE-ST-GR-B-598 | SIG-16-YRD-5C3Z | pending_review | Historical match confirmed |
| Vat Reduced IN 25% | Withholding NL 5% | unverified | Auto-mapped, validated |
| Nexus Werkstoffe | Pinnacle Materials | auto_generated | Cross-referenced with transactions |
| SIG-39-BAT-DD7R | Natriumbenzoat 70% Premiumqualität | pending_review | Auto-mapped, validated |
| Premier Logistik | Vanguard Chemicals SAS | auto_generated | Confirmed by domain expert |
| SIG-51-EJL-Y9QB | PR-MA-605 | pending_review | Historical match confirmed |
| maltodextrin de25 | DE-ST-553 | pending_review | Auto-mapped, validated |
| MA-DE-ST-267 | Maltodextrin-Pulver DE5 Qualitätsstufe II | auto_generated | Verified via product specs |
| SIG-75-WDP-0BHF | PA-OI-50-273 | unverified | Historical match confirmed |
| palm oil | Pea Protein | unverified | Verified via product specs |
| sodium benzoate premium | PO-SO-763 | pending_review | Auto-mapped, validated |
| Potassium Sorbate 50% Grade B | palm oil tech grade | auto_generated | Auto-mapped, validated |
| Nexus Enterprise | Global Solutions Group | pending_review | Historical match confirmed |
| Coconut Oil 25% Technical | Lactic Acid 99.5% Qualitätsstufe II | auto_generated | Verified via product specs |
| Elite Logistics Holdings | ZE-DI-241 | unverified | Cross-referenced with transactions |
| Kasein 98% Technische Qualität | dextrose food grade | unverified | Confirmed by domain expert |
| SIG-69-UAZ-1ODW | Global Versorgung GmbH | pending_review | Historical match confirmed |
| SIG-65-SMZ-JJEO | customs duty cn 0% | pending_review | Historical match confirmed |
| Sunflower Oil Grade A | FR-130 | pending_review | Verified via product specs |
| dextrose 99.5% standard | Lactic Acid 99.5% Qualitätsstufe II | auto_generated | Verified via product specs |
| Vat Standard GB 21% | CU-DU-G-5-181 | auto_generated | Historical match confirmed |
| Zenith Manufacturing Holdings | SIG-82-POX-I1CU | unverified | Historical match confirmed |
| SIG-40-YZP-9CC3 | CE-MA-981 | pending_review | Auto-mapped, validated |
| Sonnenblumenöl | Ascorbic Acid | pending_review | Verified via product specs |
| CU-DU-D-0-955 | Vat Reduced FR 25% | auto_generated | Auto-mapped, validated |
| Vat Standard NL 5% | Vat Standardqualität NL 20% | unverified | Auto-mapped, validated |
| Customs Duty CN 7% | SIG-65-QKW-Y1YW | pending_review | Historical match confirmed |
| Vat Standard NL 19% | SIG-92-KVS-DDEE | pending_review | Historical match confirmed |
| Elite Trading | Global Partners NV | unverified | Verified via product specs |
| RA-OI-98-679 | Coconut Oil 98% Lebensmittelrein | unverified | Cross-referenced with transactions |
| SIG-95-LOJ-S1L2 | vat standard de 7% | unverified | Cross-referenced with transactions |
| Zitronensäure 70% Lebensmittelrein | dextrose 25% tech grade | auto_generated | Cross-referenced with transactions |
| Fructose Food Grade | SIG-15-PFO-2W85 | unverified | Auto-mapped, validated |
| Wheat Gluten 50% | GL-SY-GR-B-331 | unverified | Auto-mapped, validated |
| dextrose 25% tech grade | Ascorbic Acid 50% Technical | unverified | Auto-mapped, validated |
| SIG-73-UUF-1F99 | Kasein Technische Qualität | auto_generated | Verified via product specs |
| SO-IS-PR-242 | SIG-63-MOD-EKOJ | unverified | Cross-referenced with transactions |
| SIG-13-JUR-FV2B | Kasein 70% Technische Qualität | pending_review | Auto-mapped, validated |
| Dextrose Food Grade | SIG-16-FVU-3EBQ | pending_review | Cross-referenced with transactions |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | resistant starch 50% | pending_review | Historical match confirmed |
| glucose syrup 25% | Kaliumsorbat Lebensmittelrein | unverified | Confirmed by domain expert |
| SIG-72-YVG-ZCUK | horizon materials | pending_review | Historical match confirmed |
| SIG-24-KLH-SHKW | vat reduced in 25% | auto_generated | Historical match confirmed |
| calcium carbonate food grade | CA-CA-GR-B-761 | auto_generated | Confirmed by domain expert |
| RE-ST-223 | Sunflower Oil Technical | pending_review | Historical match confirmed |
| rapeseed oil 70% standard | PA-OI-98-856 | pending_review | Historical match confirmed |
| Atlantic Distribution Group | PR-TR-517 International | unverified | Auto-mapped, validated |
| prism industries Inc. | Core Rohstoffe NV | auto_generated | Confirmed by domain expert |
| Pacific Werkstoffe GmbH | Nordic Ingredients SA | pending_review | Confirmed by domain expert |
| SIG-52-QOU-LC66 | stratos materials | unverified | Auto-mapped, validated |
| Apex Logistics | ST-LO-136 | pending_review | Verified via product specs |
| Vat Standardqualität US 5% | customs duty cn 10% | unverified | Verified via product specs |
| SIG-96-FYH-4ROJ SARL | Continental Manufacturing | pending_review | Confirmed by domain expert |
| SIG-46-SVJ-5IZO | Palmfett Standardqualität | auto_generated | Confirmed by domain expert |
| sorbic acid 98% | Maltodextrin-Pulver DE25 | auto_generated | Auto-mapped, validated |
| sorbic acid 98% | SIG-72-IMA-8RAP | auto_generated | Historical match confirmed |
| wheat gluten 50% pharma grade | Isoglucose Food Grade | pending_review | Historical match confirmed |
| AP-SU-CO-755 | vanguard logistics | auto_generated | Verified via product specs |
| Core Logistik | prime materials | auto_generated | Verified via product specs |
| SIG-97-WMO-6B83 | soy isolate 25% tech grade | pending_review | Cross-referenced with transactions |
| Core Materials | Meridian Industrien International | unverified | Verified via product specs |
| VA-LO-948 | core manufacturing SA | auto_generated | Cross-referenced with transactions |
| Vat Reduced BR 10% | EX-N-20-817 | auto_generated | Cross-referenced with transactions |
| Casein | RE-ST-50-232 | pending_review | Auto-mapped, validated |
| VA-RE-C-19-810 | Withholding BR 20% | auto_generated | Cross-referenced with transactions |
| Quantum Rohstoffe PLC | apex processing Ltd. | auto_generated | Confirmed by domain expert |
| Horizon Logistics | Continental Versorgung GmbH | unverified | Auto-mapped, validated |
| Weizenklebereiweiß Qualitätsstufe II | DE-840 | unverified | Auto-mapped, validated |
| SIG-63-KXZ-46Q1 | Ascorbic Acid 99.5% Premiumqualität | unverified | Historical match confirmed |
| resistant starch food grade | Casein Grade A | auto_generated | Confirmed by domain expert |
| withholding nl 20% | Vat Reduced GB 10% | unverified | Confirmed by domain expert |
| Soja Isolate 50% Qualitätsstufe II | SIG-40-NOU-7O0G | auto_generated | Auto-mapped, validated |
| SIG-27-QBW-ROGA | calcium carbonate 50% premium | auto_generated | Historical match confirmed |
| EL-SO-688 | Vertex Logistics | pending_review | Historical match confirmed |
| Calcium Carbonate 98% Pharmazeutisch rein | SO-IS-GR-A-940 | pending_review | Confirmed by domain expert |
| VA-RE-F-10-219 | customs duty cn 10% | unverified | Historical match confirmed |
| Dextrin | MA-DE-GR-B-565 | auto_generated | Verified via product specs |
| Pea Protein 25% | Coconut Oil | unverified | Verified via product specs |
| Stratos Materials Group | prime processing AG | pending_review | Cross-referenced with transactions |
| Pacific Distribution International | Nordic Verarbeitung | auto_generated | Cross-referenced with transactions |
| citric acid 70% | Cyclodextrin | auto_generated | Confirmed by domain expert |
| SIG-68-DWS-MNR6 | Rapeseed Oil 99.5% | auto_generated | Cross-referenced with transactions |
| Traubenzucker 50% Qualitätsstufe II | SIG-70-YBK-DUQ6 | auto_generated | Cross-referenced with transactions |
| Core Partners PLC | pacific ingredients NV | unverified | Verified via product specs |
| Traubenzucker 99.5% | Pea Protein 70% Premium | unverified | Confirmed by domain expert |
| Maltodextrin-Pulver DE20 | sodium chloride 99.5% premium | unverified | Confirmed by domain expert |
| RE-ST-25-TE-177 | Palmfett 70% Technische Qualität | unverified | Cross-referenced with transactions |
| nordic partners | Zenith Versorgung BV | unverified | Auto-mapped, validated |
| Natriumchlorid 70% | SIG-77-LSN-T27F | pending_review | Auto-mapped, validated |
| CY-515 | Maltodextrin-Pulver DE15 Standardqualität | pending_review | Confirmed by domain expert |
| Pinnacle Verarbeitung | Atlantic Processing | auto_generated | Confirmed by domain expert |
| SIG-48-OWU-RTGZ | Vat Reduced GB 19% | pending_review | Historical match confirmed |
| dextrin | SIG-44-MHK-SRCB | unverified | Verified via product specs |
| AT-LO-583 | Atlas Supply Co. | unverified | Verified via product specs |
| Glucose Syrup 25% | CO-OI-25-252 | auto_generated | Cross-referenced with transactions |
| Maltodextrin-Pulver DE15 | Coconut Oil 25% Grade B | unverified | Confirmed by domain expert |
| vat standard gb 21% | SIG-75-WHI-YNH2 | auto_generated | Cross-referenced with transactions |
| vat standard gb 21% | SIG-93-SVU-7SQ1 | pending_review | Confirmed by domain expert |
| Potassium Sorbate 50% | Fructose | auto_generated | Verified via product specs |
| SIG-30-LJO-TN4Y | Pea Protein Grade A | auto_generated | Auto-mapped, validated |
| SIG-39-SXC-H14U | CE-MA-604 | pending_review | Auto-mapped, validated |
| PR-IN-135 International | SIG-14-FNK-JNLM NV | auto_generated | Cross-referenced with transactions |
| SIG-16-XLB-CB69 | Nordic Versorgung GmbH | auto_generated | Verified via product specs |
| calcium carbonate | Kasein 98% Technische Qualität | pending_review | Verified via product specs |
| Pinnacle Trading | SIG-94-AWA-77SY Holdings | unverified | Cross-referenced with transactions |
| Pinnacle Processing | SIG-93-TEG-8CN0 SARL | auto_generated | Historical match confirmed |
| SIG-28-STQ-YUPS | Continental Logistik | unverified | Cross-referenced with transactions |
| SIG-68-KHP-8RTJ | Maltodextrin-Pulver DE18 Pharmazeutisch rein | pending_review | Auto-mapped, validated |
| SIG-60-PEY-H3GM | Pea Protein 99.5% Premium | pending_review | Confirmed by domain expert |
| Glucose Syrup Food Grade | rapeseed oil tech grade | auto_generated | Confirmed by domain expert |
| Resistant Starch 98% | dextrose 25% | unverified | Confirmed by domain expert |
| Rapsöl 50% Qualitätsstufe I | LA-AC-471 | unverified | Historical match confirmed |
| Resistant Starch 99.5% | SIG-61-KUY-VFFK | auto_generated | Verified via product specs |
| SIG-96-UYO-0BNC | stellar supply | auto_generated | Verified via product specs |
| resistant starch | Citric Acid | pending_review | Cross-referenced with transactions |
| SIG-72-LCQ-PU6W | RE-ST-99.5-242 | pending_review | Cross-referenced with transactions |
| Natriumbenzoat 25% Qualitätsstufe II | SIG-85-PGT-NQA4 | pending_review | Confirmed by domain expert |
| BA-DI-254 | Prism Solutions | auto_generated | Confirmed by domain expert |
| Rapeseed Oil | DE-98-512 | auto_generated | Confirmed by domain expert |
| sodium benzoate 50% | RE-ST-676 | pending_review | Verified via product specs |
| SIG-47-GAT-ET7B | Soy Isolate 98% | unverified | Cross-referenced with transactions |
| Catalyst Enterprise International | stratos ingredients | pending_review | Historical match confirmed |
| Pinnacle Trading Group | SIG-70-MMO-95UC | auto_generated | Auto-mapped, validated |
| SIG-18-PCA-V46E | Maltodextrin-Pulver DE25 | unverified | Cross-referenced with transactions |
| Zitronensäure Premiumqualität | FR-GR-B-311 | auto_generated | Auto-mapped, validated |
| Quantum Partners Group | premier supply PLC | auto_generated | Auto-mapped, validated |
| Palmfett Lebensmittelrein | resistant starch pharma grade | unverified | Verified via product specs |
| prime commodities | ZE-TR-467 AG | unverified | Cross-referenced with transactions |
| SIG-93-NSF-DUXM Corp. | apex processing Ltd. | unverified | Confirmed by domain expert |
| SIG-76-CCF-UYHN | AS-AC-439 | auto_generated | Auto-mapped, validated |
| Stratos Ingredients SARL | Global Solutions Group | unverified | Historical match confirmed |
| SIG-44-NHM-IY9D | CU-DU-B-7-411 | unverified | Cross-referenced with transactions |
| PI-LO-710 NV | SIG-17-UCE-6H7J Corp. | unverified | Historical match confirmed |
| PO-SO-50-TE-282 | sorbic acid standard | pending_review | Historical match confirmed |
| Withholding NL 5% | Vat Standardqualität FR 0% | auto_generated | Cross-referenced with transactions |
| LA-AC-554 | SIG-95-EES-2FE9 | auto_generated | Confirmed by domain expert |
| rapeseed oil 70% tech grade | SIG-20-OVW-HRUP | pending_review | Historical match confirmed |
| SIG-94-QXV-F18G | GL-CH-617 SARL | pending_review | Cross-referenced with transactions |
| dextrin standard | Potassium Sorbate | auto_generated | Verified via product specs |
| Cyclodextrin | PE-PR-TE-718 | auto_generated | Historical match confirmed |
| IS-230 | Natriumchlorid | unverified | Cross-referenced with transactions |
| SU-OI-TE-705 | SIG-35-FSI-YVRZ | unverified | Verified via product specs |
| VE-SO-914 Ltd. | Quantum Rohstoffe | unverified | Auto-mapped, validated |
| Fructose | CI-AC-215 | unverified | Cross-referenced with transactions |
| Isoglucose 70% | Lactic Acid Lebensmittelrein | auto_generated | Verified via product specs |
| Central Logistics | core materials | pending_review | Historical match confirmed |
| Baltic Sourcing | SIG-51-MQP-ZO0K | unverified | Confirmed by domain expert |
| Vertex Werkstoffe | stratos sourcing | unverified | Verified via product specs |
| SIG-69-UAZ-1ODW | Core Logistik | auto_generated | Historical match confirmed |
| NE-IN-874 SA | SIG-93-NSF-DUXM Corp. | auto_generated | Verified via product specs |
| Nordic Manufacturing NV | Atlantic Trading | pending_review | Confirmed by domain expert |
| SIG-24-MFK-ZAUG | Sunflower Oil | pending_review | Verified via product specs |
| VA-RE-B-7-231 | SIG-77-DIL-HGBK | unverified | Confirmed by domain expert |
| PI-LO-710 NV | Atlas Supply Corp. | auto_generated | Auto-mapped, validated |
| customs duty de 7% | Vat Standard NL 19% | pending_review | Cross-referenced with transactions |
| SIG-96-FYH-4ROJ SARL | CE-SU-700 Group | auto_generated | Verified via product specs |
| Soja Isolate 98% Premiumqualität | isoglucose 70% food grade | auto_generated | Verified via product specs |
| Atlas Manufacturing Corp. | VE-CO-290 AG | pending_review | Auto-mapped, validated |
| palm oil food grade | Sorbinsäure Qualitätsstufe I | unverified | Auto-mapped, validated |
| coconut oil 25% standard | Ascorbic Acid 50% | auto_generated | Cross-referenced with transactions |
| stellar supply | SIG-98-YBY-PFKQ | unverified | Verified via product specs |
| AP-SU-CO-787 | SIG-98-HZM-47LK | auto_generated | Verified via product specs |
| Central Supply Co. | Atlantic Werkstoffe | auto_generated | Confirmed by domain expert |
| SIG-30-LJO-TN4Y | PE-PR-70-PR-387 | auto_generated | Confirmed by domain expert |
| PA-CH-795 | Atlas Handel SARL | pending_review | Verified via product specs |
| Lactic Acid 99.5% Grade B | palm oil 98% | pending_review | Verified via product specs |
| SIG-68-TVY-N4XJ | Zitronensäure Lebensmittelrein | unverified | Verified via product specs |
| SIG-98-NDY-OCEW | WI-F-15-675 | pending_review | Verified via product specs |
| AT-MA-796 LLC | Apex Chemicals | unverified | Verified via product specs |
| SIG-39-MGB-86C4 | Excise BR 19% | pending_review | Verified via product specs |
| Prism Vertrieb NV | SIG-78-LEG-I3QI Holdings | pending_review | Historical match confirmed |
| Elite Sourcing | Vanguard Sourcing | unverified | Auto-mapped, validated |
| SIG-53-MEZ-6IT1 | AS-AC-573 | auto_generated | Cross-referenced with transactions |
| WI-D-25-711 | vat reduced nl 21% | unverified | Confirmed by domain expert |
| AT-LO-568 SA | SIG-28-KHD-E4FM NV | unverified | Historical match confirmed |
| prism industries International | AT-IN-327 | pending_review | Historical match confirmed |
| CO-OI-98-GR-A-763 | Pea Protein Grade A | auto_generated | Auto-mapped, validated |
| soy isolate | FR-50-ST-938 | pending_review | Confirmed by domain expert |
| CO-OI-98-PR-329 | SIG-68-OVP-YJX2 | unverified | Auto-mapped, validated |
| Fructose Technische Qualität | PE-PR-99.5-863 | unverified | Auto-mapped, validated |
| CI-AC-99.5-440 | isoglucose | unverified | Confirmed by domain expert |
| Calcium Carbonate 70% Premium | Coconut Oil 98% | unverified | Cross-referenced with transactions |
| AS-AC-279 | Zitronensäure 98% | auto_generated | Confirmed by domain expert |
| Premier Rohstoffe Holdings | quantum trading SARL | auto_generated | Auto-mapped, validated |
| excise gb 19% | Excise CN 25% | auto_generated | Cross-referenced with transactions |
| Lactic Acid | SIG-84-MGK-H2ME | auto_generated | Confirmed by domain expert |
| Stratos Materials Group | NO-PR-828 SA | pending_review | Historical match confirmed |
| lactic acid tech grade | Fructose 50% Standard | auto_generated | Historical match confirmed |
| SIG-78-WKT-9TDY SAS | premier logistics Ltd. | pending_review | Confirmed by domain expert |
| withholding nl 5% | EX-G-5-484 | unverified | Cross-referenced with transactions |
| MA-DE-944 | Fructose Standardqualität | pending_review | Cross-referenced with transactions |
| Calcium Carbonate 70% Premium | SIG-62-GUN-FTYL | unverified | Verified via product specs |
| Rapeseed Oil | rapeseed oil 25% | pending_review | Confirmed by domain expert |
| RE-ST-676 | SIG-82-OMQ-EPBO | auto_generated | Cross-referenced with transactions |
| Fructose | calcium carbonate standard | auto_generated | Historical match confirmed |
| VA-EN-308 | Pacific Rohstoffe International | unverified | Historical match confirmed |
| AS-AC-50-321 | Sorbinsäure Qualitätsstufe II | unverified | Confirmed by domain expert |
| Cyclodextrin | Maltodextrin-Pulver DE10 Premiumqualität | pending_review | Confirmed by domain expert |
| SIG-59-LNO-OJGF | dextrose food grade | pending_review | Verified via product specs |
| Traubenzucker Qualitätsstufe I | SIG-90-SZM-PZJ4 | pending_review | Confirmed by domain expert |
| CO-OI-98-PR-329 | Rapsöl Qualitätsstufe I | pending_review | Historical match confirmed |
| Resistente Stärke Lebensmittelrein | SIG-43-NCZ-FT9Z | pending_review | Auto-mapped, validated |
| Vat Reduced GB 0% | EX-C-21-240 | unverified | Cross-referenced with transactions |
| SIG-18-NCG-WT1V | cyclodextrin standard | pending_review | Historical match confirmed |
| Core Logistik | SIG-90-AUH-5HQ5 | pending_review | Cross-referenced with transactions |
| SIG-28-FYV-P1ZR Group | GL-EN-914 NV | auto_generated | Historical match confirmed |
| DE-98-512 | Weizenklebereiweiß | pending_review | Auto-mapped, validated |
| soy isolate 99.5% | Coconut Oil Standard | auto_generated | Cross-referenced with transactions |
| Glukosesirup Syrup | CA-GR-B-950 | auto_generated | Confirmed by domain expert |
| PR-LO-801 AG | Prime Ingredients NV | pending_review | Auto-mapped, validated |
| nexus enterprise | AT-SU-435 KG | pending_review | Confirmed by domain expert |
| Casein Grade A | Rapsöl 70% Premiumqualität | auto_generated | Auto-mapped, validated |
| Vat Reduced FR 25% | SIG-34-GED-84J3 | auto_generated | Historical match confirmed |
| SIG-73-LLJ-LNGI | Calcium Carbonate 99.5% Food Grade | unverified | Verified via product specs |
| Kasein Technische Qualität | SO-BE-GR-B-914 | auto_generated | Confirmed by domain expert |
| Glucose Syrup Food Grade | CY-763 | auto_generated | Verified via product specs |
| Lactic Acid Technical | Pea Protein | unverified | Historical match confirmed |
| SIG-98-PIN-G89V | premier partners Group | pending_review | Confirmed by domain expert |
| SIG-86-QXF-N0RG | Maltodextrin-Pulver DE30 Standardqualität | unverified | Confirmed by domain expert |
| SIG-63-KXZ-46Q1 | Maltodextrin-Pulver DE15 Standardqualität | auto_generated | Confirmed by domain expert |
| SIG-50-ABM-7VSK | Fructose Premium | auto_generated | Historical match confirmed |
| Central Logistics | SIG-33-LOJ-LA02 | auto_generated | Historical match confirmed |
| Vat Reduced FR 20% | VA-RE-B-25-739 | pending_review | Confirmed by domain expert |
| Kasein 50% Qualitätsstufe II | soy isolate | unverified | Verified via product specs |
| HO-IN-526 Corp. | SIG-43-AAR-M0YW | auto_generated | Cross-referenced with transactions |
| atlas supply | Pinnacle Ingredients | pending_review | Cross-referenced with transactions |
| zenith trading AG | NO-SU-658 AG | pending_review | Historical match confirmed |
| SO-AC-25-ST-106 | SIG-48-LHY-R0O8 | unverified | Cross-referenced with transactions |
| SIG-89-TVE-WANI | PE-PR-25-PH-GR-591 | pending_review | Cross-referenced with transactions |
| Coconut Oil 98% | DE-ST-385 | pending_review | Verified via product specs |
| DE-70-769 | Potassium Sorbate | unverified | Confirmed by domain expert |
| Soy Isolate 99.5% | SIG-78-AVK-U9PX | auto_generated | Auto-mapped, validated |
| VA-PA-407 | SIG-54-ESI-QCBZ Corp. | auto_generated | Confirmed by domain expert |
| Sonnenblumenöl Premiumqualität | dextrin | unverified | Historical match confirmed |
| stellar logistics | Stellar Logistik | unverified | Historical match confirmed |
| vanguard sourcing | SIG-39-LKH-DFJY | unverified | Historical match confirmed |
| SO-AC-25-GR-B-198 | Coconut Oil Standard | auto_generated | Auto-mapped, validated |
| SIG-85-SIL-CNEA | Fructose Grade B | unverified | Auto-mapped, validated |
| PE-PR-PR-775 | Natriumbenzoat 25% Qualitätsstufe II | unverified | Cross-referenced with transactions |
| sodium benzoate 98% standard | Dextrin | unverified | Auto-mapped, validated |
| SIG-58-LWY-Q8P6 | Zitronensäure 70% | auto_generated | Verified via product specs |
| atlas materials | PR-SU-CO-232 | auto_generated | Historical match confirmed |
| isoglucose | Soja Isolate 99.5% | auto_generated | Auto-mapped, validated |
| soy isolate | Resistente Stärke 50% Standardqualität | unverified | Confirmed by domain expert |
| SIG-38-AAT-YMEN | Maltodextrin-Pulver DE25 | auto_generated | Cross-referenced with transactions |
| Dextrin 70% Pharma Grade | CA-50-GR-B-203 | pending_review | Verified via product specs |
| atlantic logistics SARL | Global Processing SAS | auto_generated | Cross-referenced with transactions |
| CE-MA-720 | catalyst supply | unverified | Cross-referenced with transactions |
| SIG-14-HQE-PUWC | AT-IN-327 | unverified | Auto-mapped, validated |
| Palmfett | PO-SO-PR-101 | auto_generated | Verified via product specs |
| Pinnacle Sourcing | SIG-33-LXL-8AJM | unverified | Cross-referenced with transactions |
| SU-OI-ST-194 | lactic acid standard | pending_review | Historical match confirmed |
| AT-IN-100 Group | SIG-32-VLW-1KKT NV | unverified | Auto-mapped, validated |
| Prism Werkstoffe International | meridian enterprise Group | unverified | Confirmed by domain expert |
| SIG-57-QDA-RQ8R | casein | unverified | Cross-referenced with transactions |
| SIG-76-GDP-2JN8 | Dextrose Food Grade | auto_generated | Confirmed by domain expert |
| Atlas Sourcing | SIG-38-TDY-99S2 | unverified | Verified via product specs |
| SIG-48-UJX-49KW | Resistant Starch Technical | unverified | Historical match confirmed |
| CU-DU-F-25-387 | SIG-70-QEI-4QFG | unverified | Auto-mapped, validated |
| Catalyst Enterprise International | SIG-14-WWQ-VPK2 SARL | pending_review | Historical match confirmed |
| SIG-24-MFK-ZAUG | Wheat Gluten | pending_review | Verified via product specs |
| SIG-60-WEX-2G05 | Resistente Stärke Standardqualität | unverified | Verified via product specs |
| RE-ST-GR-B-805 | Casein Standard | auto_generated | Verified via product specs |
| Sunflower Oil Grade A | Maltodextrin-Pulver DE10 Premiumqualität | auto_generated | Verified via product specs |
| Zitronensäure | WH-GL-GR-B-926 | pending_review | Verified via product specs |
| Natriumchlorid 25% Lebensmittelrein | casein 70% tech grade | pending_review | Cross-referenced with transactions |
| SIG-36-UIL-7X71 | CO-OI-25-252 | auto_generated | Confirmed by domain expert |
| Ascorbic Acid Food Grade | cyclodextrin | unverified | Auto-mapped, validated |
| SIG-42-XLZ-4BOM | Traubenzucker 25% | pending_review | Cross-referenced with transactions |
| AS-AC-99.5-TE-765 | Rapeseed Oil Grade A | unverified | Historical match confirmed |
| SIG-99-OQS-ADHF | SO-CH-98-657 | auto_generated | Confirmed by domain expert |
| SO-AC-70-542 | Ascorbic Acid 99.5% | unverified | Historical match confirmed |
| LA-AC-ST-663 | Sonnenblumenöl Lebensmittelrein | pending_review | Confirmed by domain expert |
| Prime Sourcing | AT-LO-583 | pending_review | Cross-referenced with transactions |
| SO-BE-99.5-TE-213 | Resistant Starch Technical | unverified | Historical match confirmed |
| cyclodextrin | Sodium Benzoate 50% Technical | auto_generated | Auto-mapped, validated |
| central materials BV | VA-MA-681 PLC | auto_generated | Auto-mapped, validated |
| Calcium Carbonate Lebensmittelrein | Palm Oil 50% | auto_generated | Verified via product specs |
| resistant starch 98% | SIG-88-EEY-HOGD | auto_generated | Confirmed by domain expert |
| Baltic Enterprise Holdings | Atlas Solutions BV | pending_review | Cross-referenced with transactions |
| CO-OI-25-252 | Resistant Starch | pending_review | Historical match confirmed |
| SO-CH-70-365 | SIG-60-WYC-NAXS | unverified | Cross-referenced with transactions |
| PI-IN-970 Corp. | SIG-59-HNQ-A8N5 Ltd. | auto_generated | Verified via product specs |
| Lactic Acid Lebensmittelrein | SIG-83-PIY-NKQE | unverified | Verified via product specs |
| Stratos Sourcing | SIG-78-NPP-9017 | auto_generated | Confirmed by domain expert |
| resistant starch | SO-AC-98-741 | pending_review | Auto-mapped, validated |
| SIG-78-LTE-H4VL | Resistente Stärke Lebensmittelrein | pending_review | Cross-referenced with transactions |
| Zitronensäure 70% Lebensmittelrein | Isoglucose | unverified | Verified via product specs |
| nordic partners | SIG-32-VLW-1KKT NV | unverified | Cross-referenced with transactions |
| SIG-50-GYK-UH5P | stratos commodities Holdings | unverified | Confirmed by domain expert |
| Natriumchlorid 98% | GL-SY-TE-601 | unverified | Verified via product specs |
| CU-DU-I-21-633 | SIG-42-EYO-WK0H | auto_generated | Confirmed by domain expert |
| EL-SU-CO-921 | SIG-65-KWQ-0U4R | pending_review | Historical match confirmed |
| SIG-26-PJJ-DUD8 | Maltodextrin-Pulver DE20 | auto_generated | Auto-mapped, validated |
| NO-DI-180 Ltd. | Prism Chemicals AG | auto_generated | Confirmed by domain expert |
| sunflower oil | Isoglucose 25% Lebensmittelrein | auto_generated | Auto-mapped, validated |
| CA-TE-562 | Traubenzucker 25% | auto_generated | Verified via product specs |
| EX-I-15-456 | withholding fr 5% | auto_generated | Cross-referenced with transactions |
| SO-CH-GR-A-776 | SIG-65-XHR-R1SP | pending_review | Confirmed by domain expert |
| Lactic Acid Grade B | Natriumbenzoat Pharmazeutisch rein | pending_review | Cross-referenced with transactions |
| Isoglucose 70% Food Grade | Lactic Acid | auto_generated | Confirmed by domain expert |
| SIG-72-OSZ-6T19 | CI-AC-538 | auto_generated | Cross-referenced with transactions |
| Sorbinsäure 98% | sunflower oil premium | pending_review | Verified via product specs |
| Soy Isolate | SIG-74-AEB-PMX7 | unverified | Auto-mapped, validated |
| Prime Handel Group | core processing Group | pending_review | Cross-referenced with transactions |
| CI-AC-GR-A-280 | soy isolate 50% premium | pending_review | Auto-mapped, validated |
| Lactic Acid 50% Premium | Calcium Carbonate | unverified | Confirmed by domain expert |
| fructose premium | CO-OI-98-GR-A-763 | unverified | Verified via product specs |
| Lactic Acid Technical | SIG-38-YGZ-FBOJ | unverified | Historical match confirmed |
| DE-TE-406 | Casein | pending_review | Cross-referenced with transactions |
| SIG-20-UGT-P0LW | sodium chloride 98% pharma grade | auto_generated | Verified via product specs |
| SIG-53-MEZ-6IT1 | Citric Acid Food Grade | pending_review | Cross-referenced with transactions |
| Prism Sourcing | zenith supply | pending_review | Confirmed by domain expert |
| SIG-69-OFZ-JW34 | wheat gluten 70% | pending_review | Historical match confirmed |
| EX-B-5-383 | customs duty gb 5% | unverified | Auto-mapped, validated |
| CI-AC-GR-A-280 | Lactic Acid 50% Grade A | unverified | Verified via product specs |
| Core Chemicals | Quantum Versorgung Corp. | auto_generated | Historical match confirmed |
| SIG-79-GKV-W8GA | PA-OI-983 | auto_generated | Verified via product specs |
| SIG-43-NCZ-FT9Z | Rapeseed Oil Technical | auto_generated | Cross-referenced with transactions |
| Traubenzucker Lebensmittelrein | SO-BE-25-GR-B-233 | unverified | Confirmed by domain expert |
| Resistente Stärke | SO-AC-25-PH-GR-887 | unverified | Verified via product specs |
| calcium carbonate | Potassium Sorbate | unverified | Cross-referenced with transactions |
| Atlantic Vertrieb Holdings | AT-SU-132 | unverified | Cross-referenced with transactions |
| AS-AC-50-321 | Zitronensäure Lebensmittelrein | auto_generated | Historical match confirmed |
| Horizon Materials PLC | SIG-63-OTU-T27J Corp. | auto_generated | Cross-referenced with transactions |
| Nexus Processing Holdings | SIG-62-YMZ-RQQI LLC | unverified | Verified via product specs |
| Stellar Rohstoffe | prism materials | unverified | Auto-mapped, validated |
| Coconut Oil 50% Technische Qualität | SIG-15-QIT-5CZE | auto_generated | Verified via product specs |
| ascorbic acid food grade | SO-IS-PR-242 | auto_generated | Historical match confirmed |
| wheat gluten | SIG-19-TLQ-1P5Z | pending_review | Historical match confirmed |
| baltic trading NV | Elite Handel Holdings | auto_generated | Historical match confirmed |
| LA-AC-GR-A-949 | rapeseed oil 70% tech grade | pending_review | Confirmed by domain expert |
| Casein 25% Grade A | Rapsöl 98% Standardqualität | unverified | Confirmed by domain expert |
| CO-OI-98-PR-329 | Resistente Stärke | pending_review | Cross-referenced with transactions |
| AS-AC-439 | Sonnenblumenöl Technische Qualität | auto_generated | Historical match confirmed |
| Meridian Ingredients | prism materials | pending_review | Historical match confirmed |
| glucose syrup tech grade | Kaliumsorbat Technische Qualität | unverified | Historical match confirmed |
| VA-ST-N-5-804 | SIG-44-NHM-IY9D | unverified | Auto-mapped, validated |
| lactic acid 98% premium | CI-AC-25-TE-200 | auto_generated | Historical match confirmed |
| SIG-60-WEX-2G05 | Glucose Syrup 25% | pending_review | Cross-referenced with transactions |
| sodium chloride tech grade | Glucose Syrup Food Grade | unverified | Confirmed by domain expert |
| CO-OI-25-TE-157 | Wheat Gluten | unverified | Auto-mapped, validated |
| CO-OI-25-252 | Sodium Benzoate 99.5% Technical | auto_generated | Verified via product specs |
| SIG-39-ARU-8X3V | prime materials | unverified | Auto-mapped, validated |
| SIG-89-PFV-OOFP | atlas materials | auto_generated | Confirmed by domain expert |
| Meridian Trading | VE-LO-777 | pending_review | Verified via product specs |
| SIG-67-MFG-46DE | Wheat Gluten Grade B | pending_review | Confirmed by domain expert |
| SIG-43-GRJ-P3HT | Sorbic Acid | pending_review | Auto-mapped, validated |
| PA-MA-166 SARL | quantum ingredients Holdings | unverified | Cross-referenced with transactions |
| Citric Acid | sodium benzoate 99.5% premium | auto_generated | Cross-referenced with transactions |
| SO-CH-TE-286 | Lactic Acid Grade A | unverified | Confirmed by domain expert |
| dextrose 50% | WH-GL-50-865 | pending_review | Verified via product specs |
| Ascorbic Acid 50% Standardqualität | Wheat Gluten 99.5% | pending_review | Cross-referenced with transactions |
| Prime Logistik | SIG-17-TYG-MKJ1 | unverified | Cross-referenced with transactions |
| core materials | Pacific Sourcing | pending_review | Confirmed by domain expert |
| Maltodextrin DE10 | AS-AC-130 | pending_review | Verified via product specs |
| Pinnacle Processing | SIG-39-ZIX-L5KV International | pending_review | Auto-mapped, validated |
| Cyclodextrin Pharma Grade | SIG-31-DTE-83EP | unverified | Cross-referenced with transactions |
| LA-AC-FO-GR-687 | soy isolate premium | pending_review | Auto-mapped, validated |
| Dextrose | PE-PR-25-PH-GR-591 | auto_generated | Confirmed by domain expert |
| SU-OI-TE-879 | Fructose | auto_generated | Auto-mapped, validated |
| Ascorbic Acid Standardqualität | SIG-95-LLS-0RNG | auto_generated | Historical match confirmed |
| SIG-53-TLC-AZKT | dextrin | pending_review | Cross-referenced with transactions |
| SIG-50-PNF-Z2E8 | Central Logistics | pending_review | Historical match confirmed |
| VA-ST-F-15-255 | Excise BR 19% | unverified | Historical match confirmed |
| meridian industries | Zenith Verarbeitung | pending_review | Historical match confirmed |
| SIG-16-FVU-3EBQ | CI-AC-596 | unverified | Historical match confirmed |
| Central Logistik GmbH | PR-PA-998 Holdings | pending_review | Verified via product specs |
| Glukosesirup Syrup 99.5% Standardqualität | SIG-44-SRN-1MKF | pending_review | Auto-mapped, validated |
| Premier Solutions LLC | atlas materials | pending_review | Cross-referenced with transactions |
| Dextrin | GL-SY-98-939 | auto_generated | Cross-referenced with transactions |
| Meridian Versorgung GmbH | zenith supply | auto_generated | Confirmed by domain expert |
| SIG-84-DSO-4S47 | CY-763 | unverified | Cross-referenced with transactions |
| LA-AC-TE-651 | SIG-64-TCV-R5SR | auto_generated | Verified via product specs |
| MA-DE-ST-267 | dextrose | auto_generated | Auto-mapped, validated |
| sunflower oil food grade | Traubenzucker Standardqualität | auto_generated | Historical match confirmed |
| Rapeseed Oil | Sorbinsäure 50% | pending_review | Historical match confirmed |
| SIG-30-RXC-HFDI | citric acid 99.5% pharma grade | unverified | Cross-referenced with transactions |
| vertex materials | Atlantic Sourcing | unverified | Cross-referenced with transactions |
| SIG-50-PNF-Z2E8 | Stratos Logistik | auto_generated | Cross-referenced with transactions |
| Ascorbic Acid 98% Pharmazeutisch rein | CI-AC-99.5-674 | pending_review | Confirmed by domain expert |
| SIG-43-FST-BKJ7 | Vertex Logistics | auto_generated | Confirmed by domain expert |
| MA-DE-933 | SIG-99-JMF-1NOQ | auto_generated | Confirmed by domain expert |
| Apex Chemicals | BA-SO-682 International | auto_generated | Verified via product specs |
| SIG-21-PIO-0RWR | PE-PR-25-185 | pending_review | Confirmed by domain expert |
| IS-802 | Coconut Oil | pending_review | Auto-mapped, validated |
| Elite Partners International | SIG-26-EJV-LZ44 | pending_review | Confirmed by domain expert |
| Fructose Food Grade | SIG-90-SZM-PZJ4 | pending_review | Confirmed by domain expert |
| Glukosesirup Syrup Qualitätsstufe II | SIG-20-OAV-1IKJ | auto_generated | Auto-mapped, validated |
| Catalyst Logistik | SIG-26-NTJ-I6T6 | pending_review | Cross-referenced with transactions |
| Continental Processing | Horizon Partners International | pending_review | Verified via product specs |
| Baltic Handel | Pinnacle Materials SA | unverified | Historical match confirmed |
| Isoglucose | LA-AC-98-GR-A-841 | auto_generated | Verified via product specs |
| Pinnacle Logistik BV | Horizon Distribution Holdings | pending_review | Confirmed by domain expert |
| SIG-65-ZJD-9K32 Group | prime processing AG | pending_review | Historical match confirmed |
| NE-CO-575 Holdings | Atlantic Processing | auto_generated | Confirmed by domain expert |
| Maltodextrin DE30 Standard | SIG-30-EKM-GB1A | auto_generated | Verified via product specs |
| Soja Isolate Premiumqualität | SIG-47-GAT-ET7B | pending_review | Confirmed by domain expert |
| sodium chloride | Calcium Carbonate 98% | unverified | Confirmed by domain expert |
| Nordic Verarbeitung | AT-IN-956 PLC | unverified | Cross-referenced with transactions |
| Wheat Gluten Food Grade | fructose premium | pending_review | Historical match confirmed |
| Vertex Distribution AG | Core Logistik Holdings | pending_review | Cross-referenced with transactions |
| Prism Partners | meridian trading Group | pending_review | Historical match confirmed |
| Customs Duty CN 7% | Vat Standardqualität IN 19% | auto_generated | Auto-mapped, validated |
| Zitronensäure | Wheat Gluten Grade A | pending_review | Confirmed by domain expert |
| SIG-88-AGF-FF5L | coconut oil | auto_generated | Verified via product specs |
| SIG-21-PIO-0RWR | PE-PR-302 | unverified | Verified via product specs |
| Global Materials NV | vanguard chemicals | auto_generated | Verified via product specs |
| CU-DU-U-15-275 | SIG-92-HGP-O3TO | auto_generated | Cross-referenced with transactions |
| Dextrin Standardqualität | WH-GL-98-511 | auto_generated | Confirmed by domain expert |
| SIG-28-MAP-2EOP Holdings | Core Manufacturing Holdings | pending_review | Auto-mapped, validated |
| Ascorbic Acid Premiumqualität | FR-99.5-TE-579 | unverified | Historical match confirmed |
| Apex Werkstoffe | Atlantic Processing | auto_generated | Confirmed by domain expert |
| Prism Industrien Holdings | SIG-88-LSM-PKYH Holdings | unverified | Cross-referenced with transactions |
| SIG-30-PVA-ZMF8 | Fructose Qualitätsstufe I | unverified | Confirmed by domain expert |
| isoglucose tech grade | SIG-86-DMG-XSKY | unverified | Auto-mapped, validated |
| coconut oil | Maltodextrin DE20 | unverified | Confirmed by domain expert |
| Traubenzucker Standardqualität | WH-GL-FO-GR-876 | unverified | Historical match confirmed |
| IS-FO-GR-335 | Resistant Starch 70% Technical | auto_generated | Verified via product specs |
| pacific materials | QU-IN-923 International | auto_generated | Historical match confirmed |
| SIG-90-SJW-O06V | pea protein | auto_generated | Cross-referenced with transactions |
| Vat Reduced GB 25% | excise in 15% | pending_review | Confirmed by domain expert |
| Kaliumsorbat 50% Technische Qualität | SIG-35-FSI-YVRZ | auto_generated | Confirmed by domain expert |
| SIG-37-CWM-V4K0 | Sonnenblumenöl Pharmazeutisch rein | unverified | Confirmed by domain expert |
| citric acid 25% tech grade | CO-OI-25-TE-157 | pending_review | Historical match confirmed |
| SIG-88-LSM-PKYH Holdings | prism manufacturing NV | auto_generated | Historical match confirmed |
| Lactic Acid | SO-CH-881 | pending_review | Historical match confirmed |
| SIG-60-KAS-IVMD | PE-PR-PR-564 | unverified | Auto-mapped, validated |
| AS-AC-FO-GR-283 | Calcium Carbonate 98% | pending_review | Cross-referenced with transactions |
| Natriumchlorid 98% Pharmazeutisch rein | SO-CH-TE-789 | pending_review | Confirmed by domain expert |
| Customs Duty US 20% | vat reduced us 19% | pending_review | Historical match confirmed |
| Pinnacle Logistics International | SIG-52-CQW-KL19 | pending_review | Historical match confirmed |
| customs duty de 5% | VA-RE-N-19-835 | unverified | Auto-mapped, validated |
| VA-ST-D-19-529 | Vat Standardqualität NL 19% | auto_generated | Historical match confirmed |
| Maltodextrin DE5 Grade A | WH-GL-403 | unverified | Auto-mapped, validated |
| dextrose | Dextrin Pharmazeutisch rein | auto_generated | Verified via product specs |
| fructose 99.5% premium | SIG-17-YLM-LBLW | pending_review | Cross-referenced with transactions |
| resistant starch | DE-GR-A-472 | auto_generated | Historical match confirmed |
| casein | Dextrin Grade B | pending_review | Verified via product specs |
| SIG-83-BZY-VHAE | Maltodextrin-Pulver DE20 | pending_review | Historical match confirmed |
| Lactic Acid Lebensmittelrein | pea protein | unverified | Cross-referenced with transactions |
| SIG-98-OXJ-W0H6 SAS | Premier Partners | auto_generated | Confirmed by domain expert |
| SO-IS-GR-A-940 | SIG-99-IMJ-KFOM | pending_review | Confirmed by domain expert |
| Sunflower Oil 98% Premium | SIG-66-AQR-B68Q | pending_review | Auto-mapped, validated |
| VA-ST-N-10-130 | Vat Reduced NL 19% | unverified | Confirmed by domain expert |
| potassium sorbate | SIG-37-MXA-3C7Q | unverified | Confirmed by domain expert |
| Ascorbic Acid 50% Standardqualität | SIG-60-GHI-04X0 | unverified | Verified via product specs |
| Nordic Ingredients SARL | NO-CO-357 International | pending_review | Historical match confirmed |
| citric acid premium | Dextrose | auto_generated | Auto-mapped, validated |
| SIG-93-VLZ-VI4P | Vat Reduced BR 7% | auto_generated | Confirmed by domain expert |
| VE-LO-902 Group | Horizon Ingredients BV | auto_generated | Historical match confirmed |
| Zenith Handel | VA-IN-429 | auto_generated | Auto-mapped, validated |
| Resistente Stärke Qualitätsstufe II | Dextrin Standard | auto_generated | Confirmed by domain expert |
| SIG-85-TWH-HQKB | Atlantic Versorgung GmbH | pending_review | Historical match confirmed |
| quantum commodities Holdings | Premier Logistics AG | unverified | Verified via product specs |
| sodium benzoate 98% | Potassium Sorbate | pending_review | Confirmed by domain expert |
| SIG-24-VMY-QMRL | pacific materials | pending_review | Auto-mapped, validated |
| SIG-79-OZQ-4I2N | Casein Grade B | unverified | Verified via product specs |
| SIG-66-AQR-B68Q | AS-AC-279 | auto_generated | Auto-mapped, validated |
| sodium benzoate 25% standard | Soy Isolate 99.5% | pending_review | Confirmed by domain expert |
| Wheat Gluten Grade B | potassium sorbate 50% standard | auto_generated | Historical match confirmed |
| DE-70-769 | Soja Isolate 50% Qualitätsstufe II | auto_generated | Cross-referenced with transactions |
| stratos materials Group | GL-IN-746 LLC | auto_generated | Historical match confirmed |
| Citric Acid 70% | SIG-36-BVE-5U7D | pending_review | Historical match confirmed |
| SIG-91-UWU-GPZB | Maltodextrin-Pulver DE30 Standardqualität | unverified | Confirmed by domain expert |
| SIG-10-NNQ-6CGO | VA-RE-C-19-648 | unverified | Cross-referenced with transactions |
| Pinnacle Ingredients KG | nexus processing AG | auto_generated | Auto-mapped, validated |
| citric acid 25% | Resistente Stärke Qualitätsstufe I | unverified | Historical match confirmed |
| resistant starch 50% | SIG-57-YOY-F7N2 | unverified | Cross-referenced with transactions |
| Nexus Solutions SAS | SIG-86-VFH-L4DY Holdings | unverified | Auto-mapped, validated |
| casein 98% standard | Resistente Stärke 50% | auto_generated | Verified via product specs |
| Palm Oil | SIG-12-OAV-ALF4 | pending_review | Auto-mapped, validated |
| nordic manufacturing International | Central Solutions | pending_review | Verified via product specs |
| Zenith Processing | AT-IN-100 Group | unverified | Confirmed by domain expert |
| SIG-77-MDI-MBKO | Atlantic Werkstoffe | pending_review | Confirmed by domain expert |
| atlantic distribution Holdings | Quantum Handel Group | unverified | Confirmed by domain expert |
| SIG-47-UOO-GQED | CU-DU-F-15-864 | auto_generated | Cross-referenced with transactions |
| Wheat Gluten 25% Food Grade | lactic acid 25% premium | unverified | Cross-referenced with transactions |
| Meridian Sourcing | prism materials | pending_review | Cross-referenced with transactions |
| Lactic Acid 99.5% | SIG-17-OVA-CCDM | auto_generated | Confirmed by domain expert |
| LA-AC-98-GR-A-841 | potassium sorbate | pending_review | Verified via product specs |
| vanguard industries BV | Global Distribution LLC | auto_generated | Auto-mapped, validated |
| SIG-56-BPD-M0A6 | Lactic Acid 98% | unverified | Confirmed by domain expert |
| Vat Standardqualität GB 20% | customs duty fr 19% | auto_generated | Historical match confirmed |
| Pinnacle Sourcing | SIG-36-RVG-E4FG | pending_review | Historical match confirmed |
| Lactic Acid Qualitätsstufe II | Ascorbic Acid | unverified | Confirmed by domain expert |
| Isoglucose Premium | Dextrin Qualitätsstufe II | pending_review | Historical match confirmed |
| SIG-68-PIZ-R6Q5 | Sunflower Oil | unverified | Auto-mapped, validated |
| casein premium | Dextrin Premiumqualität | auto_generated | Confirmed by domain expert |
| SIG-89-TVE-WANI | DE-ST-553 | pending_review | Cross-referenced with transactions |
| central logistics | Atlas Versorgung GmbH | auto_generated | Verified via product specs |
| CA-TE-336 | SIG-21-HVD-EZVS | unverified | Confirmed by domain expert |
| Nordic Manufacturing Group | SIG-70-MMO-95UC | auto_generated | Cross-referenced with transactions |
| Casein Grade A | SIG-79-DVU-H9H4 | pending_review | Confirmed by domain expert |
| ascorbic acid 50% standard | SIG-56-CMM-ODF7 | pending_review | Historical match confirmed |
| stratos logistics | SIG-26-NTJ-I6T6 | unverified | Historical match confirmed |
| Horizon Logistics International | NO-PR-828 SA | auto_generated | Historical match confirmed |
| vertex supply | Continental Sourcing | unverified | Verified via product specs |
| SIG-19-QLH-ILRZ | CA-50-GR-B-203 | auto_generated | Confirmed by domain expert |
| Global Distribution LLC | SIG-68-BSO-NW8J Group | unverified | Confirmed by domain expert |
| SIG-47-MIU-LIH6 | global materials | unverified | Historical match confirmed |
| Continental Sourcing | quantum materials | pending_review | Auto-mapped, validated |
| Lactic Acid 98% | SIG-42-STL-CX7L | unverified | Confirmed by domain expert |
| Soja Isolate 98% | sorbic acid food grade | pending_review | Verified via product specs |
| Soja Isolate Qualitätsstufe I | rapeseed oil 70% premium | auto_generated | Historical match confirmed |
| Dextrin | Ascorbic Acid 99.5% Premiumqualität | pending_review | Auto-mapped, validated |
| meridian ingredients GmbH | Atlas Materials Holdings | pending_review | Auto-mapped, validated |
| Coconut Oil Lebensmittelrein | dextrose 70% | unverified | Historical match confirmed |
| cyclodextrin | Resistant Starch 98% Pharma Grade | auto_generated | Historical match confirmed |
| SIG-35-VQC-JQ0H AG | CA-CO-176 | pending_review | Verified via product specs |
| horizon ingredients LLC | QU-EN-736 NV | unverified | Auto-mapped, validated |
| Ascorbic Acid 70% | Pea Protein | pending_review | Historical match confirmed |
| Natriumchlorid 25% Lebensmittelrein | DE-TE-956 | auto_generated | Auto-mapped, validated |
| Soy Isolate Technical | Weizenklebereiweiß 99.5% Technische Qualität | unverified | Historical match confirmed |
| Prism Partners | Quantum Ingredients | unverified | Cross-referenced with transactions |
| Potassium Sorbate 25% Pharma Grade | MA-DE-PR-303 | pending_review | Cross-referenced with transactions |
| Lactic Acid 99.5% Qualitätsstufe II | SIG-50-MPG-UDLW | pending_review | Auto-mapped, validated |
| Rapsöl 25% Lebensmittelrein | dextrin 50% | pending_review | Cross-referenced with transactions |
| Soy Isolate 25% | DE-GR-B-157 | unverified | Auto-mapped, validated |
| CY-98-PH-GR-614 | SIG-11-AEJ-CHNJ | auto_generated | Historical match confirmed |
| Calcium Carbonate Premiumqualität | Dextrose Grade A | auto_generated | Confirmed by domain expert |
| Maltodextrin DE15 | Ascorbic Acid Premiumqualität | auto_generated | Confirmed by domain expert |
| Quantum Supply Co. | catalyst sourcing | auto_generated | Auto-mapped, validated |
| SIG-50-NOW-F1TK GmbH | Nordic Industries | auto_generated | Cross-referenced with transactions |
| EX-G-25-188 | customs duty gb 5% | auto_generated | Verified via product specs |
| SIG-12-QLD-RUJ3 Inc. | Apex Commodities Holdings | pending_review | Verified via product specs |
| Apex Commodities Holdings | PR-PA-643 | auto_generated | Cross-referenced with transactions |
| AS-AC-ST-243 | sorbic acid 70% | unverified | Verified via product specs |
| Prism Industrien LLC | SIG-63-KQC-K1S7 | unverified | Historical match confirmed |
| SIG-60-IRZ-OTKZ | IS-FO-GR-335 | pending_review | Verified via product specs |
| Baltic Supply Co. | ME-LO-583 | unverified | Confirmed by domain expert |
| Dextrose | CO-OI-817 | pending_review | Confirmed by domain expert |
| BA-EN-363 KG | continental distribution International | pending_review | Cross-referenced with transactions |
| Wheat Gluten | AS-AC-TE-342 | auto_generated | Verified via product specs |
| pea protein standard | SIG-38-AAT-YMEN | pending_review | Verified via product specs |
| Traubenzucker 50% Qualitätsstufe II | ascorbic acid 50% tech grade | auto_generated | Confirmed by domain expert |
| SIG-72-JEH-P5K7 | resistant starch 98% | pending_review | Confirmed by domain expert |
| Isoglucose | PE-PR-PR-564 | unverified | Auto-mapped, validated |
| Premier Handel AG | Pacific Supply | unverified | Cross-referenced with transactions |
| AT-MA-324 International | Core Vertrieb | unverified | Verified via product specs |
| soy isolate 70% | SIG-17-UCW-S6NB | unverified | Auto-mapped, validated |
| customs duty gb 7% | SIG-92-PYF-X5ZO | unverified | Confirmed by domain expert |
| elite materials | Catalyst Logistik | pending_review | Auto-mapped, validated |
| EL-LO-188 | Atlas Supply Co. | pending_review | Cross-referenced with transactions |
| Soy Isolate 25% | SU-OI-ST-194 | pending_review | Historical match confirmed |
| Stellar Vertrieb | SIG-60-XUT-HTI7 | unverified | Verified via product specs |
| GL-SU-CO-128 | Stellar Versorgung GmbH | auto_generated | Cross-referenced with transactions |
| resistant starch | SIG-58-NYA-2O4M | pending_review | Verified via product specs |
| Premier Partners SARL | PR-PR-701 Ltd. | auto_generated | Historical match confirmed |
| Coconut Oil 70% Grade A | SIG-45-ZHK-QWIG | unverified | Cross-referenced with transactions |
| vat reduced cn 21% | Vat Reduced CN 19% | unverified | Cross-referenced with transactions |
| SIG-20-IMA-GJKF | EX-D-10-430 | unverified | Cross-referenced with transactions |
| Soy Isolate 50% Grade B | Zitronensäure Premiumqualität | pending_review | Historical match confirmed |
| CI-AC-PH-GR-209 | SIG-70-YBK-DUQ6 | unverified | Auto-mapped, validated |
| FR-99.5-PH-GR-378 | SIG-12-RDG-0JI1 | pending_review | Verified via product specs |
| SIG-65-BMI-KAWJ Holdings | VA-DI-105 | unverified | Cross-referenced with transactions |
| Wheat Gluten | SIG-72-LCQ-PU6W | auto_generated | Confirmed by domain expert |
| SO-CH-99.5-GR-A-634 | ascorbic acid premium | auto_generated | Cross-referenced with transactions |
| Sodium Benzoate | Lactic Acid Technische Qualität | pending_review | Verified via product specs |
| Zitronensäure Technische Qualität | Lactic Acid Grade A | auto_generated | Historical match confirmed |
| Nexus Partners | nexus ingredients SA | pending_review | Auto-mapped, validated |
| CU-DU-U-19-893 | SIG-64-PME-V0B9 | auto_generated | Auto-mapped, validated |
| Customs Duty FR 19% | CU-DU-G-0-297 | pending_review | Cross-referenced with transactions |
| rapeseed oil 50% standard | Dextrose | pending_review | Cross-referenced with transactions |
| pea protein | Sorbinsäure 98% | pending_review | Confirmed by domain expert |
| Natriumbenzoat | Ascorbic Acid 70% | unverified | Confirmed by domain expert |
| Prism Materials Ltd. | Catalyst Industrien International | auto_generated | Historical match confirmed |
| resistant starch food grade | Sunflower Oil 70% | unverified | Confirmed by domain expert |
| WH-GL-ST-378 | sodium benzoate 99.5% premium | unverified | Historical match confirmed |
| SIG-46-DQX-JN7N | Vat Standardqualität IN 5% | pending_review | Verified via product specs |
| meridian chemicals Holdings | ME-TR-587 | pending_review | Historical match confirmed |
| sodium benzoate premium | GL-SY-533 | auto_generated | Verified via product specs |
| dextrose tech grade | SIG-56-SME-QSOD | pending_review | Verified via product specs |
| AT-IN-899 Group | Central Enterprise | unverified | Historical match confirmed |
| SIG-17-LVE-03G9 | Ascorbic Acid Pharmazeutisch rein | auto_generated | Verified via product specs |
| AS-AC-573 | sodium chloride | pending_review | Verified via product specs |
| SO-IS-99.5-141 | Dextrose 25% | auto_generated | Auto-mapped, validated |
| glucose syrup 25% | Calcium Carbonate 25% Pharma Grade | pending_review | Auto-mapped, validated |
| Coconut Oil 70% | SIG-86-QXF-N0RG | pending_review | Historical match confirmed |
| glucose syrup | SU-OI-423 | auto_generated | Auto-mapped, validated |
| SIG-44-MHK-SRCB | rapeseed oil | unverified | Cross-referenced with transactions |
| Resistente Stärke Qualitätsstufe II | citric acid premium | pending_review | Cross-referenced with transactions |
| SIG-90-SJW-O06V | Ascorbic Acid 99.5% Premiumqualität | pending_review | Auto-mapped, validated |
| SIG-59-LNO-OJGF | Palm Oil 70% | auto_generated | Auto-mapped, validated |
| SO-CH-354 | Coconut Oil 25% Grade B | pending_review | Verified via product specs |
| SIG-23-CJO-TSA9 | AT-SO-226 | auto_generated | Auto-mapped, validated |
| wheat gluten food grade | SIG-80-MLG-VDQ0 | pending_review | Auto-mapped, validated |
| SIG-97-EIS-DKQB Holdings | Zenith Industries Corp. | pending_review | Confirmed by domain expert |
| elite solutions Holdings | CO-LO-919 Holdings | auto_generated | Cross-referenced with transactions |
| SIG-60-PEY-H3GM | Dextrin 70% Pharma Grade | unverified | Verified via product specs |
| RA-OI-GR-B-834 | Rapeseed Oil Technical | pending_review | Auto-mapped, validated |
| vertex supply | Vertex Supply Co. | unverified | Verified via product specs |
| Citric Acid 70% Food Grade | SIG-13-CAZ-HXXP | unverified | Historical match confirmed |
| premier partners | Nordic Industries | unverified | Verified via product specs |
| calcium carbonate | Weizenklebereiweiß 99.5% | auto_generated | Auto-mapped, validated |
| stratos supply | SIG-39-EWA-Q37M | auto_generated | Confirmed by domain expert |
| RE-ST-GR-A-614 | Ascorbic Acid | unverified | Historical match confirmed |
| SIG-61-CIV-LFWA | PE-PR-PR-564 | pending_review | Verified via product specs |
| Coconut Oil 98% Technische Qualität | SIG-16-IYP-EOZP | pending_review | Cross-referenced with transactions |
| LA-AC-FO-GR-469 | Coconut Oil Grade A | pending_review | Auto-mapped, validated |
| pinnacle supply | Meridian Logistik | pending_review | Cross-referenced with transactions |
| SIG-50-QXM-GFI4 | Stratos Logistik | pending_review | Historical match confirmed |
| Vat Reduced BR 10% | VA-ST-N-20-162 | pending_review | Cross-referenced with transactions |
| Atlas Logistics | Continental Sourcing | pending_review | Auto-mapped, validated |
| SIG-15-PFO-2W85 | Traubenzucker Qualitätsstufe I | unverified | Confirmed by domain expert |
| Customs Duty GB 7% | Excise IN 19% | unverified | Confirmed by domain expert |
| Apex Chemicals Corp. | PR-LO-801 AG | unverified | Verified via product specs |
| PI-DI-618 NV | SIG-55-TGR-SSTC Holdings | pending_review | Historical match confirmed |
| Customs Duty FR 5% | WI-G-5-718 | pending_review | Historical match confirmed |
| AS-AC-GR-B-395 | SIG-44-QME-TTIM | unverified | Verified via product specs |
| LA-AC-TE-761 | Maltodextrin-Pulver DE10 | pending_review | Historical match confirmed |
| Stratos Trading Holdings | PR-CH-334 GmbH | pending_review | Verified via product specs |
| Pinnacle Logistik BV | SIG-58-FND-MEQW Ltd. | unverified | Cross-referenced with transactions |
| fructose pharma grade | SIG-93-GFI-NZRV | unverified | Auto-mapped, validated |
| Citric Acid 25% Grade A | SIG-45-IJY-KUT6 | unverified | Auto-mapped, validated |
| Global Distribution LLC | NE-EN-710 NV | unverified | Historical match confirmed |
| EX-F-21-522 | Withholding CN 15% | unverified | Verified via product specs |
| Weizenklebereiweiß 50% Technische Qualität | SIG-91-GMY-Q91Y | unverified | Verified via product specs |
| casein | SIG-29-BZP-SU62 | auto_generated | Cross-referenced with transactions |
| potassium sorbate 50% tech grade | SIG-43-KEL-FPY6 | pending_review | Confirmed by domain expert |
| Cyclodextrin 70% Food Grade | DE-70-769 | auto_generated | Historical match confirmed |
| SIG-46-YOE-MYAX SA | Premier Versorgung PLC | pending_review | Verified via product specs |
| Sodium Chloride 98% Standard | maltodextrin de5 premium | auto_generated | Auto-mapped, validated |
| CA-CA-648 | SIG-68-VDM-0UT1 | auto_generated | Historical match confirmed |
| lactic acid food grade | Dextrin 50% | auto_generated | Auto-mapped, validated |
| SIG-93-TEG-8CN0 SARL | ST-PA-227 PLC | auto_generated | Historical match confirmed |
| SIG-64-TCV-R5SR | Sorbinsäure | unverified | Confirmed by domain expert |
| Lactic Acid Grade B | Weizenklebereiweiß 99.5% | unverified | Confirmed by domain expert |
| Glucose Syrup 70% | Zitronensäure 98% | pending_review | Auto-mapped, validated |
| palm oil 70% tech grade | Maltodextrin-Pulver DE5 Qualitätsstufe I | auto_generated | Confirmed by domain expert |
| Palmfett Standardqualität | isoglucose tech grade | auto_generated | Auto-mapped, validated |
| SIG-70-ROA-COR7 | atlas materials | unverified | Confirmed by domain expert |
| Isoglucose | SIG-15-NIP-N1UH | unverified | Auto-mapped, validated |
| Coconut Oil 25% | Dextrose | pending_review | Historical match confirmed |
| quantum trading SARL | Global Verarbeitung SAS | pending_review | Confirmed by domain expert |
| Catalyst Rohstoffe SA | central ingredients International | unverified | Historical match confirmed |
| QU-MA-886 | elite logistics | unverified | Verified via product specs |
| SIG-52-EML-H8JV | pea protein 98% | unverified | Cross-referenced with transactions |
| atlas enterprise | HO-LO-534 PLC | unverified | Historical match confirmed |
| ascorbic acid food grade | SIG-42-LOE-5XD8 | pending_review | Historical match confirmed |
| glucose syrup 99.5% food grade | Traubenzucker 70% | auto_generated | Auto-mapped, validated |
| Sunflower Oil Pharma Grade | Weizenklebereiweiß 98% | unverified | Auto-mapped, validated |
| SIG-88-RUZ-O3Q0 | Premier Enterprise Holdings | auto_generated | Auto-mapped, validated |
| Pinnacle Ingredients KG | PI-SO-581 Inc. | pending_review | Auto-mapped, validated |
| Isoglucose Grade B | Coconut Oil 70% | auto_generated | Auto-mapped, validated |
| Resistant Starch 50% Standard | Isoglucose Lebensmittelrein | auto_generated | Auto-mapped, validated |
| SIG-47-TWK-RYLY | Excise NL 7% | unverified | Auto-mapped, validated |
| Elite Logistics | SIG-39-CJT-QHM3 | unverified | Confirmed by domain expert |
| CI-AC-GR-A-280 | SIG-83-OTU-QZB6 | pending_review | Confirmed by domain expert |
| Atlas Logistics International | SIG-78-LEG-I3QI Holdings | unverified | Confirmed by domain expert |
| Central Werkstoffe | SIG-81-AMW-NE5V | unverified | Auto-mapped, validated |
| RE-ST-575 | Sorbinsäure 25% Standardqualität | auto_generated | Verified via product specs |
| vertex logistics KG | AP-MA-546 AG | unverified | Verified via product specs |
| glucose syrup 98% food grade | SIG-20-BPG-W8VL | pending_review | Confirmed by domain expert |
| casein standard | Traubenzucker 70% | unverified | Auto-mapped, validated |
| IS-230 | cyclodextrin | pending_review | Verified via product specs |
| Pinnacle Commodities BV | CO-CH-401 Inc. | pending_review | Cross-referenced with transactions |
| soy isolate 99.5% | Citric Acid 25% | pending_review | Verified via product specs |
| SIG-16-CAW-LD7M | Dextrin Pharma Grade | auto_generated | Confirmed by domain expert |
| Atlas Industrien International | Baltic Chemicals AG | unverified | Verified via product specs |
| Sodium Benzoate 99.5% Standard | Resistente Stärke Qualitätsstufe II | unverified | Verified via product specs |
| Rapsöl | SO-CH-257 | pending_review | Cross-referenced with transactions |
| Ascorbic Acid | Sorbinsäure 50% | auto_generated | Confirmed by domain expert |
| Potassium Sorbate 50% Grade B | Sorbinsäure Technische Qualität | unverified | Confirmed by domain expert |
| vat standard nl 20% | SIG-41-SEX-2DFF | unverified | Cross-referenced with transactions |
| pea protein 70% tech grade | PE-PR-70-PR-387 | auto_generated | Auto-mapped, validated |
| SIG-63-TFP-OMUW | Kaliumsorbat Premiumqualität | pending_review | Verified via product specs |
| Pacific Werkstoffe | meridian logistics | pending_review | Cross-referenced with transactions |
| CO-SU-411 | Prism Manufacturing PLC | pending_review | Historical match confirmed |
| cyclodextrin 70% food grade | Kaliumsorbat | pending_review | Auto-mapped, validated |
| VE-CH-445 Group | premier enterprise Holdings | pending_review | Cross-referenced with transactions |
| SIG-39-JXL-BQ85 SARL | AP-IN-643 LLC | pending_review | Confirmed by domain expert |
| ascorbic acid | Citric Acid | unverified | Auto-mapped, validated |
| horizon partners Ltd. | Premier Chemicals | auto_generated | Confirmed by domain expert |
| SIG-86-LPN-HCNV | coconut oil standard | unverified | Historical match confirmed |
| global materials | VA-MA-951 | unverified | Cross-referenced with transactions |
| prism partners Holdings | PR-CH-121 KG | pending_review | Auto-mapped, validated |
| IS-25-FO-GR-789 | Natriumchlorid | pending_review | Cross-referenced with transactions |
| Sonnenblumenöl Standardqualität | sunflower oil standard | auto_generated | Verified via product specs |
| PR-EN-361 International | nordic partners | pending_review | Cross-referenced with transactions |
| Customs Duty IN 5% | EX-U-15-972 | unverified | Auto-mapped, validated |
| Meridian Werkstoffe | Quantum Supply Co. | auto_generated | Historical match confirmed |
| GL-SY-70-549 | sunflower oil | auto_generated | Cross-referenced with transactions |
| zenith trading GmbH | Quantum Processing SA | pending_review | Confirmed by domain expert |
| dextrin pharma grade | Coconut Oil 25% | auto_generated | Confirmed by domain expert |
| SIG-64-LXA-3LJO | Traubenzucker Standardqualität | auto_generated | Confirmed by domain expert |
| SIG-83-CDB-3QOI | global supply | pending_review | Auto-mapped, validated |
| SIG-92-NWY-1FV5 | Vat Reduced GB 25% | pending_review | Auto-mapped, validated |
| Natriumbenzoat | cyclodextrin | unverified | Historical match confirmed |
| Isoglucose 70% | Kaliumsorbat | pending_review | Historical match confirmed |
| Customs Duty CN 0% | SIG-74-VWV-7YSU | auto_generated | Verified via product specs |
| SIG-73-LLJ-LNGI | casein | auto_generated | Cross-referenced with transactions |
| nexus logistics | SIG-42-HLS-D63Y | auto_generated | Verified via product specs |
| potassium sorbate | Palmfett | pending_review | Auto-mapped, validated |
| SIG-34-IKF-VQJA | Wheat Gluten 50% Pharma Grade | unverified | Confirmed by domain expert |
| SO-IS-99.5-141 | SIG-68-XQK-6G5I | unverified | Historical match confirmed |
| core partners NV | SIG-78-WKT-9TDY SAS | unverified | Confirmed by domain expert |
| Sorbic Acid Food Grade | dextrose 70% premium | unverified | Cross-referenced with transactions |
| ascorbic acid standard | Pea Protein | pending_review | Auto-mapped, validated |
| Pea Protein 50% | sunflower oil premium | pending_review | Confirmed by domain expert |
| Resistente Stärke | SO-CH-758 | auto_generated | Auto-mapped, validated |
| DE-70-PH-GR-978 | Kasein 98% Technische Qualität | pending_review | Auto-mapped, validated |
| SIG-53-DUL-C550 Group | Premier Industries SAS | unverified | Cross-referenced with transactions |
| Maltodextrin DE25 | SIG-10-TIC-7Q1D | pending_review | Verified via product specs |
| pacific industries Ltd. | SIG-68-HOK-ETCC | unverified | Auto-mapped, validated |
| SO-CH-TE-223 | SIG-80-WEB-2C7R | auto_generated | Historical match confirmed |
| Soja Isolate 25% Technische Qualität | Soy Isolate | auto_generated | Auto-mapped, validated |
| SIG-61-QOJ-MGS9 BV | VE-IN-631 Ltd. | pending_review | Verified via product specs |
| sodium benzoate 50% | Sorbinsäure Premiumqualität | pending_review | Historical match confirmed |
| Wheat Gluten 99.5% | Zitronensäure 50% Pharmazeutisch rein | unverified | Verified via product specs |
| nexus ingredients SA | Pinnacle Ingredients Ltd. | pending_review | Verified via product specs |
| resistant starch 25% food grade | SO-AC-70-785 | auto_generated | Confirmed by domain expert |
| Kasein | sunflower oil 50% premium | unverified | Verified via product specs |
| Resistente Stärke 98% | wheat gluten standard | unverified | Confirmed by domain expert |
| Continental Commodities GmbH | apex materials Group | pending_review | Verified via product specs |
| Ascorbic Acid Premium | wheat gluten standard | pending_review | Auto-mapped, validated |
| SIG-47-YTF-UPMT | Weizenklebereiweiß | auto_generated | Historical match confirmed |
| Sodium Benzoate Pharma Grade | CA-CA-25-PH-GR-684 | auto_generated | Auto-mapped, validated |
| Quantum Handel Group | ME-TR-587 | auto_generated | Verified via product specs |

#### 4.3.3 Excluded Mappings

Mappings excluded from scope per stakeholder decision:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-6056-H | Invalid Entry 895 | Data quality insufficient |
| NOISE-3524-B | Invalid Entry 591 | Out of scope per business decision |
| NOISE-6162-D | Invalid Entry 357 | Out of scope per business decision |
| NOISE-2472-G | Invalid Entry 974 | Duplicate detected |
| NOISE-8676-D | Invalid Entry 902 | Superseded by newer mapping |
| NOISE-8785-A | Invalid Entry 624 | Data quality insufficient |
| NOISE-7835-E | Invalid Entry 785 | Data quality insufficient |
| NOISE-3130-C | Invalid Entry 405 | Data quality insufficient |
| NOISE-9725-D | Invalid Entry 108 | Data quality insufficient |
| NOISE-6486-G | Invalid Entry 788 | Duplicate detected |
| NOISE-8534-F | Invalid Entry 678 | Superseded by newer mapping |
| NOISE-4550-B | Invalid Entry 546 | Duplicate detected |
| NOISE-5366-F | Invalid Entry 964 | Out of scope per business decision |
| NOISE-5315-A | Invalid Entry 336 | Pending validation |
| NOISE-8913-D | Invalid Entry 419 | Superseded by newer mapping |
| NOISE-5440-A | Invalid Entry 891 | Out of scope per business decision |
| NOISE-3635-F | Invalid Entry 332 | Superseded by newer mapping |
| NOISE-4032-G | Invalid Entry 811 | Pending validation |
| NOISE-2100-C | Invalid Entry 201 | Pending validation |
| NOISE-7657-B | Invalid Entry 525 | Superseded by newer mapping |
| NOISE-9953-F | Invalid Entry 130 | Superseded by newer mapping |
| NOISE-3147-D | Invalid Entry 950 | Out of scope per business decision |
| NOISE-6150-G | Invalid Entry 957 | Duplicate detected |
| NOISE-6966-D | Invalid Entry 689 | Data quality insufficient |
| NOISE-5765-G | Invalid Entry 406 | Data quality insufficient |
| NOISE-8973-A | Invalid Entry 909 | Data quality insufficient |
| NOISE-9901-D | Invalid Entry 441 | Out of scope per business decision |
| NOISE-2884-A | Invalid Entry 804 | Pending validation |
| NOISE-4886-G | Invalid Entry 660 | Pending validation |
| NOISE-1061-G | Invalid Entry 118 | Pending validation |
| NOISE-6067-D | Invalid Entry 542 | Out of scope per business decision |
| NOISE-7399-H | Invalid Entry 984 | Duplicate detected |
| NOISE-5041-A | Invalid Entry 814 | Superseded by newer mapping |
| NOISE-5938-H | Invalid Entry 965 | Data quality insufficient |
| NOISE-9810-C | Invalid Entry 201 | Superseded by newer mapping |
| NOISE-1079-A | Invalid Entry 761 | Superseded by newer mapping |
| NOISE-5532-E | Invalid Entry 726 | Data quality insufficient |
| NOISE-5090-D | Invalid Entry 398 | Duplicate detected |
| NOISE-2426-E | Invalid Entry 596 | Superseded by newer mapping |
| NOISE-8854-D | Invalid Entry 555 | Out of scope per business decision |
| NOISE-3754-H | Invalid Entry 777 | Out of scope per business decision |
| NOISE-8273-E | Invalid Entry 942 | Data quality insufficient |
| NOISE-5701-H | Invalid Entry 449 | Data quality insufficient |
| NOISE-6094-F | Invalid Entry 553 | Out of scope per business decision |
| NOISE-9686-C | Invalid Entry 153 | Out of scope per business decision |
| NOISE-8602-C | Invalid Entry 426 | Data quality insufficient |
| NOISE-9486-A | Invalid Entry 280 | Superseded by newer mapping |
| NOISE-2724-D | Invalid Entry 364 | Duplicate detected |
| NOISE-2234-E | Invalid Entry 538 | Data quality insufficient |
| NOISE-7193-H | Invalid Entry 459 | Pending validation |
| NOISE-3353-C | Invalid Entry 115 | Duplicate detected |
| NOISE-1920-G | Invalid Entry 608 | Data quality insufficient |
| NOISE-7781-G | Invalid Entry 802 | Pending validation |
| NOISE-7355-E | Invalid Entry 754 | Duplicate detected |
| NOISE-1229-B | Invalid Entry 395 | Duplicate detected |
| NOISE-6430-A | Invalid Entry 725 | Pending validation |
| NOISE-8432-G | Invalid Entry 545 | Superseded by newer mapping |
| NOISE-1578-H | Invalid Entry 934 | Duplicate detected |
| NOISE-1834-E | Invalid Entry 506 | Superseded by newer mapping |
| NOISE-3247-D | Invalid Entry 123 | Pending validation |
| NOISE-2179-C | Invalid Entry 682 | Out of scope per business decision |
| NOISE-4824-E | Invalid Entry 347 | Superseded by newer mapping |
| NOISE-5273-B | Invalid Entry 645 | Data quality insufficient |
| NOISE-8617-D | Invalid Entry 363 | Data quality insufficient |
| NOISE-4269-E | Invalid Entry 237 | Out of scope per business decision |
| NOISE-7714-A | Invalid Entry 467 | Data quality insufficient |
| NOISE-9832-F | Invalid Entry 926 | Superseded by newer mapping |
| NOISE-1989-G | Invalid Entry 966 | Pending validation |
| NOISE-5026-H | Invalid Entry 474 | Duplicate detected |
| NOISE-9749-B | Invalid Entry 976 | Out of scope per business decision |
| NOISE-7832-D | Invalid Entry 224 | Data quality insufficient |
| NOISE-7206-C | Invalid Entry 547 | Pending validation |
| NOISE-3171-H | Invalid Entry 993 | Duplicate detected |
| NOISE-4455-H | Invalid Entry 981 | Superseded by newer mapping |
| NOISE-2427-E | Invalid Entry 231 | Superseded by newer mapping |
| NOISE-1330-D | Invalid Entry 112 | Out of scope per business decision |
| NOISE-6138-G | Invalid Entry 348 | Out of scope per business decision |
| NOISE-8210-D | Invalid Entry 400 | Pending validation |
| NOISE-2245-B | Invalid Entry 966 | Pending validation |
| NOISE-2673-A | Invalid Entry 946 | Pending validation |
| NOISE-4793-B | Invalid Entry 693 | Superseded by newer mapping |
| NOISE-4547-A | Invalid Entry 205 | Superseded by newer mapping |
| NOISE-7035-D | Invalid Entry 774 | Duplicate detected |
| NOISE-7485-D | Invalid Entry 756 | Out of scope per business decision |
| NOISE-4075-G | Invalid Entry 293 | Data quality insufficient |
| NOISE-1235-H | Invalid Entry 874 | Superseded by newer mapping |
| NOISE-6950-E | Invalid Entry 588 | Data quality insufficient |
| NOISE-9528-F | Invalid Entry 472 | Duplicate detected |
| NOISE-7567-B | Invalid Entry 758 | Superseded by newer mapping |
| NOISE-6322-H | Invalid Entry 308 | Data quality insufficient |
| NOISE-1320-F | Invalid Entry 739 | Out of scope per business decision |
| NOISE-2699-E | Invalid Entry 895 | Out of scope per business decision |
| NOISE-8171-D | Invalid Entry 186 | Data quality insufficient |
| NOISE-7291-H | Invalid Entry 235 | Data quality insufficient |
| NOISE-9765-C | Invalid Entry 432 | Pending validation |
| NOISE-5531-A | Invalid Entry 276 | Data quality insufficient |
| NOISE-1864-D | Invalid Entry 401 | Pending validation |
| NOISE-2134-F | Invalid Entry 869 | Superseded by newer mapping |
| NOISE-3350-H | Invalid Entry 764 | Out of scope per business decision |
| NOISE-8723-F | Invalid Entry 102 | Duplicate detected |
| NOISE-9455-E | Invalid Entry 633 | Duplicate detected |
| NOISE-6506-F | Invalid Entry 955 | Pending validation |
| NOISE-3427-F | Invalid Entry 175 | Out of scope per business decision |
| NOISE-7841-C | Invalid Entry 873 | Out of scope per business decision |
| NOISE-4681-A | Invalid Entry 926 | Data quality insufficient |
| NOISE-2198-H | Invalid Entry 701 | Pending validation |
| NOISE-1547-H | Invalid Entry 776 | Pending validation |
| NOISE-4176-E | Invalid Entry 460 | Duplicate detected |
| NOISE-1715-G | Invalid Entry 818 | Pending validation |
| NOISE-2405-B | Invalid Entry 662 | Data quality insufficient |
| NOISE-4819-H | Invalid Entry 911 | Out of scope per business decision |
| NOISE-5392-C | Invalid Entry 823 | Superseded by newer mapping |
| NOISE-2817-B | Invalid Entry 876 | Duplicate detected |
| NOISE-6630-C | Invalid Entry 105 | Superseded by newer mapping |
| NOISE-3065-G | Invalid Entry 631 | Data quality insufficient |
| NOISE-4778-C | Invalid Entry 740 | Data quality insufficient |
| NOISE-9277-G | Invalid Entry 755 | Data quality insufficient |
| NOISE-8411-A | Invalid Entry 944 | Superseded by newer mapping |
| NOISE-7341-G | Invalid Entry 564 | Duplicate detected |
| NOISE-2444-E | Invalid Entry 956 | Out of scope per business decision |
| NOISE-6973-E | Invalid Entry 397 | Duplicate detected |
| NOISE-3399-B | Invalid Entry 863 | Data quality insufficient |
| NOISE-2612-C | Invalid Entry 606 | Duplicate detected |
| NOISE-9359-H | Invalid Entry 464 | Superseded by newer mapping |
| NOISE-3439-C | Invalid Entry 912 | Duplicate detected |
| NOISE-9592-G | Invalid Entry 722 | Out of scope per business decision |
| NOISE-6833-C | Invalid Entry 113 | Superseded by newer mapping |
| NOISE-1470-A | Invalid Entry 897 | Pending validation |
| NOISE-9053-G | Invalid Entry 460 | Pending validation |
| NOISE-3063-H | Invalid Entry 206 | Pending validation |
| NOISE-6878-A | Invalid Entry 243 | Superseded by newer mapping |
| NOISE-3406-G | Invalid Entry 713 | Data quality insufficient |
| NOISE-1858-G | Invalid Entry 126 | Out of scope per business decision |
| NOISE-4914-F | Invalid Entry 795 | Pending validation |
| NOISE-9324-C | Invalid Entry 978 | Data quality insufficient |
| NOISE-3002-C | Invalid Entry 619 | Superseded by newer mapping |
| NOISE-8263-G | Invalid Entry 846 | Pending validation |
| NOISE-9071-E | Invalid Entry 816 | Duplicate detected |
| NOISE-1302-C | Invalid Entry 892 | Out of scope per business decision |
| NOISE-3341-A | Invalid Entry 324 | Data quality insufficient |
| NOISE-9402-E | Invalid Entry 983 | Out of scope per business decision |
| NOISE-3273-H | Invalid Entry 100 | Data quality insufficient |
| NOISE-4275-D | Invalid Entry 513 | Out of scope per business decision |
| NOISE-8593-H | Invalid Entry 978 | Data quality insufficient |
| NOISE-3445-A | Invalid Entry 608 | Duplicate detected |
| NOISE-1949-A | Invalid Entry 717 | Pending validation |
| NOISE-2181-D | Invalid Entry 633 | Data quality insufficient |
| NOISE-7810-C | Invalid Entry 428 | Out of scope per business decision |
| NOISE-5545-E | Invalid Entry 771 | Out of scope per business decision |
| NOISE-4323-G | Invalid Entry 883 | Superseded by newer mapping |
| NOISE-5935-D | Invalid Entry 609 | Duplicate detected |
| NOISE-9576-B | Invalid Entry 240 | Superseded by newer mapping |
| NOISE-3455-E | Invalid Entry 453 | Data quality insufficient |
| NOISE-9483-H | Invalid Entry 692 | Superseded by newer mapping |
| NOISE-4308-E | Invalid Entry 346 | Pending validation |
| NOISE-5524-G | Invalid Entry 571 | Duplicate detected |
| NOISE-2765-C | Invalid Entry 989 | Pending validation |
| NOISE-6408-H | Invalid Entry 642 | Superseded by newer mapping |
| NOISE-5973-A | Invalid Entry 830 | Out of scope per business decision |
| NOISE-5506-H | Invalid Entry 542 | Pending validation |
| NOISE-6153-C | Invalid Entry 196 | Duplicate detected |
| NOISE-6597-H | Invalid Entry 943 | Data quality insufficient |
| NOISE-3033-C | Invalid Entry 807 | Pending validation |
| NOISE-9316-B | Invalid Entry 782 | Superseded by newer mapping |
| NOISE-9662-D | Invalid Entry 424 | Superseded by newer mapping |
| NOISE-9401-C | Invalid Entry 784 | Out of scope per business decision |
| NOISE-5185-A | Invalid Entry 575 | Pending validation |
| NOISE-3397-E | Invalid Entry 732 | Duplicate detected |
| NOISE-9740-C | Invalid Entry 583 | Pending validation |
| NOISE-3654-C | Invalid Entry 907 | Data quality insufficient |
| NOISE-7371-G | Invalid Entry 274 | Pending validation |
| NOISE-2165-G | Invalid Entry 486 | Pending validation |
| NOISE-1867-H | Invalid Entry 966 | Out of scope per business decision |
| NOISE-7334-C | Invalid Entry 482 | Superseded by newer mapping |
| NOISE-9718-E | Invalid Entry 308 | Data quality insufficient |
| NOISE-3748-B | Invalid Entry 942 | Superseded by newer mapping |
| NOISE-9951-B | Invalid Entry 301 | Superseded by newer mapping |
| NOISE-4169-E | Invalid Entry 384 | Superseded by newer mapping |
| NOISE-1357-E | Invalid Entry 833 | Out of scope per business decision |
| NOISE-3387-F | Invalid Entry 407 | Data quality insufficient |
| NOISE-1642-D | Invalid Entry 943 | Duplicate detected |
| NOISE-1805-B | Invalid Entry 531 | Pending validation |
| NOISE-3350-G | Invalid Entry 360 | Data quality insufficient |
| NOISE-9872-A | Invalid Entry 607 | Data quality insufficient |
| NOISE-4520-D | Invalid Entry 639 | Pending validation |
| NOISE-9829-C | Invalid Entry 513 | Superseded by newer mapping |
| NOISE-1878-F | Invalid Entry 912 | Out of scope per business decision |
| NOISE-6802-C | Invalid Entry 927 | Data quality insufficient |
| NOISE-6784-D | Invalid Entry 765 | Data quality insufficient |
| NOISE-4678-E | Invalid Entry 938 | Pending validation |
| NOISE-5111-A | Invalid Entry 418 | Superseded by newer mapping |
| NOISE-1488-B | Invalid Entry 847 | Superseded by newer mapping |
| NOISE-7627-D | Invalid Entry 927 | Out of scope per business decision |
| NOISE-1600-F | Invalid Entry 707 | Pending validation |
| NOISE-9877-E | Invalid Entry 487 | Superseded by newer mapping |
| NOISE-3956-F | Invalid Entry 183 | Out of scope per business decision |
| NOISE-2737-D | Invalid Entry 942 | Pending validation |
| NOISE-8391-H | Invalid Entry 197 | Pending validation |
| NOISE-2255-D | Invalid Entry 494 | Superseded by newer mapping |
| NOISE-6013-F | Invalid Entry 787 | Pending validation |
| NOISE-2372-G | Invalid Entry 895 | Superseded by newer mapping |
| NOISE-5294-G | Invalid Entry 881 | Data quality insufficient |
| NOISE-5621-C | Invalid Entry 976 | Duplicate detected |
| NOISE-5385-D | Invalid Entry 691 | Superseded by newer mapping |
| NOISE-1818-E | Invalid Entry 516 | Superseded by newer mapping |
| NOISE-2775-H | Invalid Entry 894 | Superseded by newer mapping |
| NOISE-4668-D | Invalid Entry 758 | Duplicate detected |
| NOISE-8434-F | Invalid Entry 153 | Superseded by newer mapping |
| NOISE-5240-G | Invalid Entry 352 | Data quality insufficient |
| NOISE-8040-B | Invalid Entry 848 | Out of scope per business decision |
| NOISE-9370-D | Invalid Entry 646 | Data quality insufficient |
| NOISE-7418-D | Invalid Entry 715 | Out of scope per business decision |
| NOISE-8365-C | Invalid Entry 353 | Pending validation |
| NOISE-3214-B | Invalid Entry 727 | Superseded by newer mapping |
| NOISE-4124-F | Invalid Entry 691 | Pending validation |
| NOISE-2166-E | Invalid Entry 534 | Out of scope per business decision |
| NOISE-8788-E | Invalid Entry 595 | Superseded by newer mapping |
| NOISE-1178-B | Invalid Entry 190 | Superseded by newer mapping |
| NOISE-8182-C | Invalid Entry 350 | Out of scope per business decision |
| NOISE-5914-E | Invalid Entry 139 | Pending validation |
| NOISE-5874-F | Invalid Entry 576 | Pending validation |
| NOISE-8358-F | Invalid Entry 919 | Pending validation |
| NOISE-1017-C | Invalid Entry 401 | Pending validation |
| NOISE-8270-G | Invalid Entry 375 | Out of scope per business decision |
| NOISE-2065-D | Invalid Entry 746 | Superseded by newer mapping |
| NOISE-1955-A | Invalid Entry 749 | Pending validation |
| NOISE-2387-B | Invalid Entry 641 | Data quality insufficient |
| NOISE-8333-B | Invalid Entry 708 | Out of scope per business decision |
| NOISE-6355-B | Invalid Entry 831 | Superseded by newer mapping |
| NOISE-5655-E | Invalid Entry 933 | Out of scope per business decision |
| NOISE-9752-G | Invalid Entry 404 | Data quality insufficient |
| NOISE-8779-E | Invalid Entry 633 | Out of scope per business decision |
| NOISE-5858-E | Invalid Entry 100 | Out of scope per business decision |
| NOISE-3108-C | Invalid Entry 425 | Data quality insufficient |
| NOISE-4237-B | Invalid Entry 368 | Superseded by newer mapping |
| NOISE-6657-D | Invalid Entry 930 | Duplicate detected |
| NOISE-2521-B | Invalid Entry 877 | Superseded by newer mapping |
| NOISE-8364-B | Invalid Entry 247 | Data quality insufficient |
| NOISE-9165-D | Invalid Entry 126 | Data quality insufficient |
| NOISE-8225-D | Invalid Entry 346 | Superseded by newer mapping |
| NOISE-4432-D | Invalid Entry 201 | Data quality insufficient |
| NOISE-2109-E | Invalid Entry 692 | Superseded by newer mapping |
| NOISE-5131-E | Invalid Entry 866 | Data quality insufficient |
| NOISE-7810-E | Invalid Entry 496 | Superseded by newer mapping |
| NOISE-9943-A | Invalid Entry 238 | Pending validation |
| NOISE-1579-E | Invalid Entry 747 | Duplicate detected |
| NOISE-8550-C | Invalid Entry 816 | Pending validation |
| NOISE-2754-A | Invalid Entry 868 | Pending validation |
| NOISE-3937-C | Invalid Entry 216 | Duplicate detected |
| NOISE-4248-E | Invalid Entry 276 | Data quality insufficient |
| NOISE-1490-G | Invalid Entry 754 | Superseded by newer mapping |
| NOISE-8466-F | Invalid Entry 313 | Pending validation |
| NOISE-4206-A | Invalid Entry 583 | Out of scope per business decision |
| NOISE-2523-C | Invalid Entry 485 | Data quality insufficient |
| NOISE-5287-F | Invalid Entry 933 | Duplicate detected |
| NOISE-2454-H | Invalid Entry 477 | Superseded by newer mapping |
| NOISE-4400-B | Invalid Entry 755 | Out of scope per business decision |
| NOISE-6441-F | Invalid Entry 851 | Out of scope per business decision |
| NOISE-4739-H | Invalid Entry 566 | Data quality insufficient |
| NOISE-7177-G | Invalid Entry 512 | Pending validation |
| NOISE-3344-C | Invalid Entry 507 | Pending validation |
| NOISE-3443-E | Invalid Entry 443 | Superseded by newer mapping |
| NOISE-6087-A | Invalid Entry 668 | Duplicate detected |
| NOISE-4985-F | Invalid Entry 645 | Superseded by newer mapping |
| NOISE-3664-E | Invalid Entry 982 | Superseded by newer mapping |
| NOISE-2850-B | Invalid Entry 327 | Out of scope per business decision |
| NOISE-7954-E | Invalid Entry 589 | Superseded by newer mapping |
| NOISE-4761-H | Invalid Entry 294 | Superseded by newer mapping |
| NOISE-1391-A | Invalid Entry 438 | Duplicate detected |
| NOISE-4296-F | Invalid Entry 863 | Duplicate detected |
| NOISE-9023-H | Invalid Entry 856 | Superseded by newer mapping |
| NOISE-6824-H | Invalid Entry 278 | Duplicate detected |
| NOISE-9867-A | Invalid Entry 519 | Out of scope per business decision |
| NOISE-1595-D | Invalid Entry 595 | Pending validation |
| NOISE-7476-F | Invalid Entry 608 | Duplicate detected |
| NOISE-8721-B | Invalid Entry 614 | Out of scope per business decision |
| NOISE-9638-A | Invalid Entry 826 | Out of scope per business decision |
| NOISE-9426-D | Invalid Entry 635 | Pending validation |
| NOISE-1026-G | Invalid Entry 152 | Duplicate detected |
| NOISE-1818-B | Invalid Entry 426 | Pending validation |
| NOISE-4799-D | Invalid Entry 601 | Pending validation |
| NOISE-3398-F | Invalid Entry 189 | Duplicate detected |
| NOISE-6429-H | Invalid Entry 815 | Out of scope per business decision |
| NOISE-1337-F | Invalid Entry 356 | Out of scope per business decision |
| NOISE-9480-G | Invalid Entry 645 | Data quality insufficient |
| NOISE-5252-G | Invalid Entry 617 | Data quality insufficient |
| NOISE-3797-H | Invalid Entry 407 | Duplicate detected |
| NOISE-6327-B | Invalid Entry 119 | Pending validation |
| NOISE-8879-B | Invalid Entry 428 | Out of scope per business decision |
| NOISE-7615-H | Invalid Entry 324 | Superseded by newer mapping |
| NOISE-5805-A | Invalid Entry 996 | Duplicate detected |
| NOISE-5996-D | Invalid Entry 477 | Data quality insufficient |
| NOISE-8299-D | Invalid Entry 157 | Superseded by newer mapping |
| NOISE-7697-D | Invalid Entry 222 | Out of scope per business decision |
| NOISE-1191-E | Invalid Entry 120 | Superseded by newer mapping |
| NOISE-9578-B | Invalid Entry 805 | Out of scope per business decision |
| NOISE-3690-F | Invalid Entry 488 | Pending validation |
| NOISE-2792-A | Invalid Entry 689 | Duplicate detected |
| NOISE-6156-F | Invalid Entry 369 | Duplicate detected |
| NOISE-8042-D | Invalid Entry 331 | Pending validation |
| NOISE-3110-A | Invalid Entry 425 | Data quality insufficient |
| NOISE-9889-G | Invalid Entry 970 | Pending validation |
| NOISE-6256-A | Invalid Entry 761 | Superseded by newer mapping |
| NOISE-3232-A | Invalid Entry 147 | Duplicate detected |
| NOISE-7435-C | Invalid Entry 253 | Pending validation |
| NOISE-5572-D | Invalid Entry 557 | Superseded by newer mapping |
| NOISE-8064-F | Invalid Entry 658 | Duplicate detected |
| NOISE-1335-A | Invalid Entry 615 | Pending validation |
| NOISE-5667-C | Invalid Entry 354 | Data quality insufficient |
| NOISE-2483-H | Invalid Entry 455 | Superseded by newer mapping |
| NOISE-3900-C | Invalid Entry 437 | Data quality insufficient |
| NOISE-7074-B | Invalid Entry 302 | Pending validation |
| NOISE-4552-H | Invalid Entry 971 | Duplicate detected |
| NOISE-7107-A | Invalid Entry 508 | Duplicate detected |
| NOISE-6003-G | Invalid Entry 408 | Superseded by newer mapping |
| NOISE-7368-D | Invalid Entry 233 | Data quality insufficient |
| NOISE-6390-F | Invalid Entry 244 | Data quality insufficient |
| NOISE-4652-C | Invalid Entry 453 | Duplicate detected |
| NOISE-4697-H | Invalid Entry 264 | Pending validation |
| NOISE-7892-E | Invalid Entry 344 | Data quality insufficient |
| NOISE-2078-B | Invalid Entry 867 | Superseded by newer mapping |
| NOISE-5154-F | Invalid Entry 216 | Superseded by newer mapping |
| NOISE-7649-E | Invalid Entry 731 | Data quality insufficient |
| NOISE-7563-H | Invalid Entry 222 | Duplicate detected |
| NOISE-2615-E | Invalid Entry 284 | Pending validation |
| NOISE-3153-E | Invalid Entry 433 | Superseded by newer mapping |
| NOISE-9394-C | Invalid Entry 495 | Superseded by newer mapping |
| NOISE-5650-C | Invalid Entry 684 | Pending validation |
| NOISE-2993-F | Invalid Entry 244 | Data quality insufficient |

#### 4.3.4 Special Handling Notes

Some entities required special handling due to:
- Regional naming variations (German/English translations)
- Legacy code formats incompatible with new system
- Historical product splits or mergers
- Regulatory classification changes

Refer to the entity-specific notes in the mapping table above for details.


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
| 1.1 | 2023-02-01 | S. Chen | Added rollback procedures |
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
