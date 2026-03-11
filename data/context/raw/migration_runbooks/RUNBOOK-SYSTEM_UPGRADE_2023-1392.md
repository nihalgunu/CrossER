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
| Total entities assessed | 1467 | Completed |
| Successfully mapped | 1085 | Verified |
| Excluded from scope | 325 | Documented |
| Manual review required | 3 | In Progress |

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
| SIG-65-EFS-5P03 | Dextrin Qualitätsstufe II | unverified | Auto-mapped, validated |
| Horizon Industrien GmbH | CE-LO-195 | auto_generated | Verified via product specs |
| SO-CH-752 | Sodium Benzoate Grade B | pending_review | Verified via product specs |
| SIG-37-ZOD-1VME | Rapeseed Oil 98% Standard | pending_review | Confirmed by domain expert |
| DE-GR-A-512 | Maltodextrin-Pulver DE10 | pending_review | Cross-referenced with transactions |
| Prism Industrien Holdings | PR-SO-362 | unverified | Auto-mapped, validated |
| SIG-78-WDE-NNV9 | Casein 25% Technical | unverified | Cross-referenced with transactions |
| Pea Protein 99.5% | isoglucose | auto_generated | Auto-mapped, validated |
| FR-PR-346 | Maltodextrin-Pulver DE18 Pharmazeutisch rein | auto_generated | Verified via product specs |
| Nexus Materials | Elite Logistik | auto_generated | Historical match confirmed |
| Meridian Versorgung GmbH | Quantum Materials | auto_generated | Historical match confirmed |
| Nexus Sourcing | SIG-83-CDB-3QOI | auto_generated | Auto-mapped, validated |
| SIG-68-HOK-ETCC | stellar distribution Corp. | pending_review | Confirmed by domain expert |
| Fructose | CA-98-PR-260 | pending_review | Historical match confirmed |
| VE-IN-631 Ltd. | Meridian Werkstoffe Corp. | auto_generated | Historical match confirmed |
| Rapsöl Qualitätsstufe I | DE-GR-B-244 | auto_generated | Verified via product specs |
| Maltodextrin DE30 Standard | cyclodextrin premium | pending_review | Historical match confirmed |
| Vanguard Logistik SA | SIG-44-DMA-GL51 International | unverified | Cross-referenced with transactions |
| Isoglucose Qualitätsstufe II | WH-GL-923 | unverified | Cross-referenced with transactions |
| core supply | SIG-60-NXS-8BAO | pending_review | Verified via product specs |
| VA-IN-429 | meridian industries | pending_review | Historical match confirmed |
| CO-OI-50-PH-GR-568 | Calcium Carbonate 25% | pending_review | Confirmed by domain expert |
| elite logistics | NE-SO-394 | pending_review | Auto-mapped, validated |
| ascorbic acid | SIG-21-PIO-0RWR | pending_review | Cross-referenced with transactions |
| Meridian Enterprise | Central Manufacturing PLC | unverified | Historical match confirmed |
| pinnacle distribution Ltd. | PR-CH-121 KG | pending_review | Auto-mapped, validated |
| CU-DU-G-0-770 | Customs Duty DE 20% | auto_generated | Confirmed by domain expert |
| Zenith Versorgung GmbH | central sourcing | unverified | Verified via product specs |
| sodium chloride 98% pharma grade | FR-PR-346 | auto_generated | Cross-referenced with transactions |
| Wheat Gluten 50% | SIG-58-EEN-BKJF | unverified | Auto-mapped, validated |
| CY-577 | SIG-24-SWK-GROA | auto_generated | Verified via product specs |
| Ascorbic Acid 98% | Ascorbic Acid 98% Premiumqualität | unverified | Cross-referenced with transactions |
| pea protein standard | SO-CH-GR-B-273 | auto_generated | Auto-mapped, validated |
| Dextrin 50% | PA-OI-98-GR-A-940 | auto_generated | Historical match confirmed |
| Central Commodities Ltd. | CE-SU-700 Group | auto_generated | Historical match confirmed |
| SIG-17-OVA-CCDM | Maltodextrin-Pulver DE10 Premiumqualität | pending_review | Confirmed by domain expert |
| SIG-39-EWA-Q37M | Nexus Sourcing | pending_review | Historical match confirmed |
| palm oil 50% | SO-BE-25-GR-B-233 | unverified | Auto-mapped, validated |
| sodium benzoate premium | MA-DE-437 | auto_generated | Auto-mapped, validated |
| Isoglucose 50% Lebensmittelrein | SIG-13-TIV-U5CX | pending_review | Confirmed by domain expert |
| pacific materials GmbH | SIG-50-HWB-Y27E Ltd. | unverified | Verified via product specs |
| Dextrin Technical | CY-515 | unverified | Cross-referenced with transactions |
| Ascorbic Acid | glucose syrup premium | unverified | Confirmed by domain expert |
| Vat Standardqualität GB 15% | SIG-37-NGX-7Z2S | unverified | Cross-referenced with transactions |
| atlantic materials | Prism Sourcing | pending_review | Auto-mapped, validated |
| Fructose | DE-25-PR-846 | unverified | Verified via product specs |
| SIG-42-HBL-L3KU International | Stellar Distribution SA | unverified | Auto-mapped, validated |
| sodium chloride 70% | Fructose Technische Qualität | pending_review | Verified via product specs |
| Pea Protein | SIG-27-SJP-0JO4 | unverified | Auto-mapped, validated |
| Atlantic Commodities | SIG-59-CKH-O7IN Group | pending_review | Cross-referenced with transactions |
| CA-PH-GR-524 | soy isolate 25% tech grade | pending_review | Confirmed by domain expert |
| SIG-71-CWF-DGP5 | lactic acid 70% pharma grade | pending_review | Auto-mapped, validated |
| MA-DE-146 | fructose 99.5% food grade | pending_review | Cross-referenced with transactions |
| resistant starch food grade | IS-802 | auto_generated | Cross-referenced with transactions |
| CO-OI-25-ST-613 | SIG-18-NCG-WT1V | auto_generated | Cross-referenced with transactions |
| SIG-51-KQC-QY9M | Soy Isolate 70% | pending_review | Confirmed by domain expert |
| PA-MA-412 GmbH | SIG-50-BJQ-W54O Holdings | auto_generated | Cross-referenced with transactions |
| Sodium Benzoate Grade A | DE-25-TE-737 | auto_generated | Confirmed by domain expert |
| PR-CO-481 International | SIG-36-PWY-HJFC International | auto_generated | Verified via product specs |
| prism industries International | ST-DI-782 SA | pending_review | Historical match confirmed |
| cyclodextrin premium | Potassium Sorbate 50% | unverified | Verified via product specs |
| SIG-54-ZFB-4REP Inc. | Nexus Processing Holdings | unverified | Auto-mapped, validated |
| SIG-83-BZY-VHAE | Calcium Carbonate 70% Premiumqualität | unverified | Confirmed by domain expert |
| Palmfett | wheat gluten 50% tech grade | auto_generated | Cross-referenced with transactions |
| SIG-65-BMI-KAWJ Holdings | BA-SO-835 Corp. | auto_generated | Verified via product specs |
| SIG-50-QXM-GFI4 | elite sourcing | pending_review | Confirmed by domain expert |
| Prism Versorgung GmbH | premier supply | auto_generated | Auto-mapped, validated |
| Sorbinsäure | SO-IS-PH-GR-671 | unverified | Historical match confirmed |
| sodium benzoate 50% | SIG-57-EMA-EI5R | auto_generated | Cross-referenced with transactions |
| ST-PA-227 PLC | Premier Partners | pending_review | Verified via product specs |
| AS-AC-GR-B-855 | cyclodextrin 98% pharma grade | auto_generated | Cross-referenced with transactions |
| SIG-44-HLB-IC48 SARL | Baltic Ingredients | auto_generated | Verified via product specs |
| Rapeseed Oil | Fructose 70% Pharmazeutisch rein | auto_generated | Confirmed by domain expert |
| Potassium Sorbate 50% Technical | sorbic acid food grade | auto_generated | Confirmed by domain expert |
| CY-892 | Sorbinsäure Premiumqualität | unverified | Auto-mapped, validated |
| SIG-39-WTU-81JC | Baltic Chemicals AG | pending_review | Verified via product specs |
| Core Logistics | Pacific Werkstoffe | pending_review | Verified via product specs |
| SIG-26-HEJ-USUB Group | Global Ingredients GmbH | pending_review | Historical match confirmed |
| SIG-47-QLD-IL46 | Coconut Oil | unverified | Historical match confirmed |
| Maltodextrin-Pulver DE15 | SIG-76-IIX-V2Y9 | unverified | Confirmed by domain expert |
| Pinnacle Sourcing | CO-SO-442 | pending_review | Confirmed by domain expert |
| potassium sorbate | Pea Protein 70% Pharma Grade | auto_generated | Historical match confirmed |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | Maltodextrin DE18 Pharma Grade | auto_generated | Cross-referenced with transactions |
| Sorbinsäure Premiumqualität | SIG-48-LHY-R0O8 | pending_review | Auto-mapped, validated |
| Soja Isolate 25% Technische Qualität | SIG-48-ASO-8G0Y | unverified | Historical match confirmed |
| glucose syrup 25% | Pea Protein Grade A | unverified | Historical match confirmed |
| Traubenzucker Qualitätsstufe I | palm oil 50% | auto_generated | Confirmed by domain expert |
| WH-GL-GR-B-129 | SIG-88-AGF-FF5L | unverified | Historical match confirmed |
| Soja Isolate 98% Premiumqualität | SIG-67-MFG-46DE | unverified | Auto-mapped, validated |
| NO-MA-529 | vertex commodities AG | unverified | Historical match confirmed |
| SIG-86-JBA-HCDI | Stratos Processing | unverified | Confirmed by domain expert |
| Horizon Ingredients BV | Nordic Processing SAS | unverified | Historical match confirmed |
| Atlantic Industrien International | SIG-31-YNJ-FQMJ Holdings | auto_generated | Verified via product specs |
| BA-IN-585 SARL | Nexus Distribution PLC | unverified | Verified via product specs |
| Atlantic Trading BV | SIG-37-AVX-CY7Q SAS | pending_review | Verified via product specs |
| Isoglucose Lebensmittelrein | sodium benzoate premium | pending_review | Confirmed by domain expert |
| PE-PR-163 | SIG-99-GVJ-VPM6 | unverified | Verified via product specs |
| SIG-27-KMU-WPWH GmbH | BA-TR-619 | pending_review | Historical match confirmed |
| sodium benzoate 98% | Resistant Starch Standard | auto_generated | Auto-mapped, validated |
| Stratos Commodities International | SIG-63-KQC-K1S7 | unverified | Auto-mapped, validated |
| Rapsöl 70% Premiumqualität | Palm Oil Standard | auto_generated | Cross-referenced with transactions |
| SIG-42-AYY-K71K | LA-AC-927 | auto_generated | Cross-referenced with transactions |
| Premier Logistics | PI-MA-112 | unverified | Auto-mapped, validated |
| baltic solutions Group | Central Solutions | unverified | Verified via product specs |
| SO-CH-99.5-GR-A-206 | Pea Protein | unverified | Historical match confirmed |
| IS-FO-GR-555 | sunflower oil 70% | pending_review | Confirmed by domain expert |
| Casein Standard | pea protein 99.5% | auto_generated | Auto-mapped, validated |
| SIG-45-GXT-XIBF | SO-AC-340 | unverified | Historical match confirmed |
| Atlantic Manufacturing | SIG-86-ZYB-L8NP BV | unverified | Historical match confirmed |
| ascorbic acid | Sorbinsäure 25% Standardqualität | pending_review | Auto-mapped, validated |
| SIG-47-YTF-UPMT | sodium benzoate | auto_generated | Auto-mapped, validated |
| sodium chloride 99.5% premium | Coconut Oil 98% | auto_generated | Cross-referenced with transactions |
| Rapsöl Lebensmittelrein | AS-AC-279 | pending_review | Verified via product specs |
| Dextrose 70% Grade A | SIG-38-YTD-7BST | unverified | Confirmed by domain expert |
| SIG-93-FDC-Q685 | Dextrose | unverified | Verified via product specs |
| SIG-86-QTB-N3VO International | Global Verarbeitung Group | pending_review | Cross-referenced with transactions |
| Prism Materials Ltd. | VE-LO-902 Group | pending_review | Auto-mapped, validated |
| zenith logistics | Meridian Versorgung GmbH | unverified | Historical match confirmed |
| RE-ST-PR-679 | lactic acid 98% premium | unverified | Auto-mapped, validated |
| Vat Standard NL 19% | Excise IN 7% | auto_generated | Verified via product specs |
| Atlantic Chemicals SAS | EL-SO-163 | unverified | Cross-referenced with transactions |
| SIG-27-GRI-K7JV | CU-DU-B-7-760 | auto_generated | Cross-referenced with transactions |
| Ascorbic Acid Premiumqualität | FR-GR-B-231 | pending_review | Historical match confirmed |
| PI-LO-946 | central materials BV | unverified | Verified via product specs |
| AT-CH-905 Holdings | Stratos Versorgung BV | auto_generated | Auto-mapped, validated |
| SIG-12-JLN-YFH3 | Isoglucose | unverified | Auto-mapped, validated |
| CO-MA-993 Corp. | atlas partners | pending_review | Historical match confirmed |
| RE-ST-463 | Coconut Oil 98% | unverified | Cross-referenced with transactions |
| Isoglucose | Weizenklebereiweiß Qualitätsstufe I | auto_generated | Verified via product specs |
| PR-CH-121 KG | Pinnacle Rohstoffe NV | pending_review | Verified via product specs |
| Central Sourcing | BA-MA-998 | auto_generated | Confirmed by domain expert |
| meridian logistics | PI-SO-952 | pending_review | Cross-referenced with transactions |
| Citric Acid 25% Technical | dextrin tech grade | pending_review | Cross-referenced with transactions |
| PA-MA-324 | Global Materials | unverified | Confirmed by domain expert |
| AP-SU-CO-755 | Atlantic Materials | unverified | Verified via product specs |
| Elite Sourcing | SIG-17-TYG-MKJ1 | auto_generated | Auto-mapped, validated |
| Vat Reduced BR 19% | Excise BR 19% | auto_generated | Auto-mapped, validated |
| Sunflower Oil 50% Pharma Grade | casein 70% tech grade | pending_review | Confirmed by domain expert |
| atlantic ingredients | Baltic Solutions International | auto_generated | Verified via product specs |
| SIG-57-YOY-F7N2 | Lactic Acid Lebensmittelrein | pending_review | Verified via product specs |
| Sodium Benzoate 99.5% Technical | SIG-38-YGZ-FBOJ | auto_generated | Cross-referenced with transactions |
| CO-MA-295 | SIG-43-TPO-RSBY | pending_review | Historical match confirmed |
| Zitronensäure Qualitätsstufe I | SIG-25-VPE-TOC1 | pending_review | Verified via product specs |
| SIG-23-LAS-L2MX Holdings | Meridian Versorgung | auto_generated | Cross-referenced with transactions |
| dextrin | AS-AC-165 | auto_generated | Confirmed by domain expert |
| EX-U-7-320 | Excise BR 19% | pending_review | Cross-referenced with transactions |
| Fructose Technical | Resistente Stärke Qualitätsstufe II | auto_generated | Verified via product specs |
| calcium carbonate | Rapeseed Oil 50% Food Grade | unverified | Cross-referenced with transactions |
| Glucose Syrup Technical | casein 70% tech grade | auto_generated | Auto-mapped, validated |
| SIG-23-BLM-EZKX | Lactic Acid Technical | pending_review | Verified via product specs |
| Dextrin Technical | isoglucose | auto_generated | Historical match confirmed |
| sorbic acid 98% | Calcium Carbonate 25% Pharma Grade | unverified | Confirmed by domain expert |
| Premier Logistics | Pacific Versorgung GmbH | unverified | Confirmed by domain expert |
| sodium benzoate 98% | Ascorbic Acid 50% Standardqualität | auto_generated | Verified via product specs |
| VE-SO-701 | Vanguard Supply Co. | unverified | Auto-mapped, validated |
| SIG-36-ZWC-F2K1 | rapeseed oil 70% tech grade | pending_review | Cross-referenced with transactions |
| SIG-61-IQH-EKWH | Ascorbic Acid Premiumqualität | auto_generated | Confirmed by domain expert |
| Zitronensäure | SIG-89-TVE-WANI | auto_generated | Historical match confirmed |
| Maltodextrin-Pulver DE10 | SIG-50-JOR-LO4P | unverified | Auto-mapped, validated |
| sodium chloride tech grade | SIG-36-FSA-X73Q | pending_review | Historical match confirmed |
| Isoglucose | Rapeseed Oil Grade A | auto_generated | Confirmed by domain expert |
| Weizenklebereiweiß Lebensmittelrein | Calcium Carbonate 50% | pending_review | Auto-mapped, validated |
| wheat gluten pharma grade | Sunflower Oil Standard | auto_generated | Verified via product specs |
| baltic processing | Meridian Werkstoffe Corp. | auto_generated | Confirmed by domain expert |
| RA-OI-TE-584 | Maltodextrin DE25 | pending_review | Auto-mapped, validated |
| customs duty fr 7% | CU-DU-F-20-900 | unverified | Confirmed by domain expert |
| SIG-28-SXX-AKUN | ST-SU-CO-396 | pending_review | Auto-mapped, validated |
| AT-SU-CO-755 | Pacific Werkstoffe | auto_generated | Auto-mapped, validated |
| Horizon Partners Ltd. | SIG-63-OTU-T27J Corp. | auto_generated | Auto-mapped, validated |
| Vat Standard GB 19% | VA-RE-F-10-219 | auto_generated | Auto-mapped, validated |
| fructose standard | FR-PR-267 | auto_generated | Cross-referenced with transactions |
| Dextrin | SIG-20-UMV-LJM6 | auto_generated | Cross-referenced with transactions |
| Nexus Partners GmbH | SIG-60-XUT-HTI7 | unverified | Verified via product specs |
| RE-ST-GR-B-598 | Lactic Acid Technische Qualität | auto_generated | Historical match confirmed |
| Vertex Vertrieb Holdings | prism solutions Ltd. | pending_review | Cross-referenced with transactions |
| Sodium Chloride 25% Food Grade | dextrin premium | auto_generated | Historical match confirmed |
| LA-AC-TE-651 | coconut oil 25% food grade | pending_review | Cross-referenced with transactions |
| Natriumbenzoat 50% Technische Qualität | SIG-65-XHR-R1SP | auto_generated | Auto-mapped, validated |
| PA-CH-580 KG | SIG-49-LWO-P3PY | pending_review | Cross-referenced with transactions |
| SIG-69-BWM-8WBG | Apex Handel | auto_generated | Confirmed by domain expert |
| Isoglucose | dextrose 25% | pending_review | Cross-referenced with transactions |
| fructose standard | Maltodextrin-Pulver DE15 | auto_generated | Historical match confirmed |
| NO-SU-CO-376 | pinnacle materials | auto_generated | Historical match confirmed |
| SIG-14-HQE-PUWC | atlantic industries International | auto_generated | Historical match confirmed |
| withholding nl 5% | Withholding BR 10% | pending_review | Cross-referenced with transactions |
| Catalyst Versorgung International | Nexus Partners GmbH | unverified | Historical match confirmed |
| SIG-51-CZK-SBJH | EX-C-21-179 | auto_generated | Confirmed by domain expert |
| AT-CH-341 SA | Nordic Vertrieb | unverified | Cross-referenced with transactions |
| Traubenzucker 70% | lactic acid | unverified | Verified via product specs |
| Citric Acid 99.5% | coconut oil 25% standard | unverified | Confirmed by domain expert |
| PR-SO-362 | premier enterprise | auto_generated | Historical match confirmed |
| SIG-68-KHP-8RTJ | Lactic Acid | unverified | Confirmed by domain expert |
| Ascorbic Acid | sodium benzoate 50% | auto_generated | Confirmed by domain expert |
| soy isolate 50% premium | SIG-45-ADT-8MFS | unverified | Verified via product specs |
| Withholding NL 5% | excise gb 0% | unverified | Historical match confirmed |
| CO-OI-98-PR-329 | Dextrin Food Grade | auto_generated | Verified via product specs |
| SIG-98-XJT-L879 | GL-SY-GR-B-331 | pending_review | Auto-mapped, validated |
| Apex Ingredients AG | SIG-59-CKH-O7IN Group | unverified | Cross-referenced with transactions |
| IS-25-FO-GR-789 | Zitronensäure 25% Technische Qualität | auto_generated | Verified via product specs |
| Withholding FR 5% | CU-DU-C-25-424 | pending_review | Confirmed by domain expert |
| Sodium Chloride Technical | soy isolate 99.5% premium | pending_review | Cross-referenced with transactions |
| Ascorbic Acid 50% Technical | Maltodextrin-Pulver DE5 Qualitätsstufe I | unverified | Auto-mapped, validated |
| Palm Oil 70% Grade B | Isoglucose | pending_review | Verified via product specs |
| PE-PR-50-128 | Natriumbenzoat 50% | auto_generated | Cross-referenced with transactions |
| Glukosesirup Syrup 25% | Soy Isolate 98% Food Grade | auto_generated | Verified via product specs |
| Dextrose 70% Grade A | SO-IS-PH-GR-671 | pending_review | Confirmed by domain expert |
| Catalyst Materials | SIG-66-HXC-DMKU | auto_generated | Cross-referenced with transactions |
| lactic acid standard | Cyclodextrin | unverified | Confirmed by domain expert |
| Potassium Sorbate | cyclodextrin premium | unverified | Auto-mapped, validated |
| Pea Protein Standard | Lactic Acid 98% Premiumqualität | auto_generated | Auto-mapped, validated |
| Stratos Ingredients SARL | Prism Ingredients | unverified | Historical match confirmed |
| Kaliumsorbat Lebensmittelrein | SO-BE-ST-871 | auto_generated | Auto-mapped, validated |
| Vat Reduced CN 19% | VA-ST-F-20-240 | pending_review | Cross-referenced with transactions |
| Sodium Benzoate 99.5% Grade A | Ascorbic Acid 70% | unverified | Historical match confirmed |
| Lactic Acid | RE-ST-TE-614 | auto_generated | Historical match confirmed |
| Horizon Chemicals PLC | NE-CH-574 Group | auto_generated | Confirmed by domain expert |
| soy isolate 99.5% | Ascorbic Acid 99.5% | pending_review | Confirmed by domain expert |
| nordic processing SAS | Stellar Rohstoffe | auto_generated | Auto-mapped, validated |
| SIG-86-NGE-LKTW | PA-MA-102 | auto_generated | Auto-mapped, validated |
| Palm Oil 25% Grade A | PE-PR-25-185 | auto_generated | Historical match confirmed |
| SIG-68-DWS-MNR6 | Potassium Sorbate | pending_review | Auto-mapped, validated |
| NE-TR-634 International | SIG-23-NOR-OPI3 | unverified | Auto-mapped, validated |
| Vat Reduced GB 19% | VA-RE-I-5-252 | unverified | Auto-mapped, validated |
| Withholding DE 20% | VA-RE-B-21-369 | auto_generated | Confirmed by domain expert |
| MA-DE-335 | resistant starch standard | unverified | Confirmed by domain expert |
| Resistente Stärke | SIG-52-ITT-ELH9 | unverified | Auto-mapped, validated |
| coconut oil standard | Ascorbic Acid 50% Standardqualität | auto_generated | Verified via product specs |
| coconut oil 25% standard | SIG-46-YHU-BU2J | unverified | Confirmed by domain expert |
| Vat Reduced BR 25% | Withholding DE 25% | auto_generated | Historical match confirmed |
| Excise US 19% | Customs Duty BR 7% | unverified | Verified via product specs |
| CA-CA-FO-GR-991 | Lactic Acid | pending_review | Confirmed by domain expert |
| Soja Isolate 99.5% | SIG-82-ZPY-WR2F | pending_review | Auto-mapped, validated |
| SIG-15-IUN-M051 | Withholding FR 5% | auto_generated | Verified via product specs |
| Resistente Stärke | SIG-66-RQA-05UV | auto_generated | Confirmed by domain expert |
| potassium sorbate 25% pharma grade | SIG-53-MEZ-6IT1 | pending_review | Auto-mapped, validated |
| SO-BE-824 | Lactic Acid 98% Premiumqualität | unverified | Verified via product specs |
| SO-BE-99.5-GR-A-930 | resistant starch 50% | unverified | Cross-referenced with transactions |
| pea protein premium | Palm Oil Grade B | pending_review | Historical match confirmed |
| SIG-26-PJJ-DUD8 | Calcium Carbonate 25% | auto_generated | Confirmed by domain expert |
| Pea Protein 98% Qualitätsstufe II | SIG-94-TUN-H84G | pending_review | Verified via product specs |
| Vertex Solutions NV | PR-LO-109 Group | pending_review | Confirmed by domain expert |
| sorbic acid | SIG-65-RQH-9Y5B | unverified | Confirmed by domain expert |
| Pea Protein 25% | SIG-53-AHT-MGFX | auto_generated | Confirmed by domain expert |
| PA-LO-674 | SIG-89-HLJ-NILC | unverified | Confirmed by domain expert |
| SIG-22-XCC-QSNV | Fructose Technische Qualität | pending_review | Confirmed by domain expert |
| CO-IN-915 KG | Premier Enterprise International | auto_generated | Auto-mapped, validated |
| vertex chemicals International | SIG-75-XPL-QWB7 GmbH | auto_generated | Verified via product specs |
| Atlantic Industrien International | SIG-58-FND-MEQW Ltd. | unverified | Verified via product specs |
| pinnacle distribution Ltd. | SIG-58-DDZ-4JKE International | unverified | Confirmed by domain expert |
| SO-AC-PR-928 | Glukosesirup Syrup 98% Qualitätsstufe I | unverified | Auto-mapped, validated |
| Soy Isolate 50% Grade B | Kasein 98% Qualitätsstufe II | pending_review | Historical match confirmed |
| Citric Acid 50% Grade A | soy isolate tech grade | pending_review | Auto-mapped, validated |
| Rapsöl 70% Qualitätsstufe II | Dextrin Pharma Grade | auto_generated | Confirmed by domain expert |
| Pinnacle Materials | SIG-10-PGH-BTUF | pending_review | Cross-referenced with transactions |
| SIG-44-QME-TTIM | Kasein Technische Qualität | auto_generated | Historical match confirmed |
| Calcium Carbonate Food Grade | SO-AC-PH-GR-620 | auto_generated | Cross-referenced with transactions |
| Nordic Chemicals BV | SIG-43-MIT-DWCJ SA | auto_generated | Auto-mapped, validated |
| NO-IN-797 | Stratos Rohstoffe Inc. | auto_generated | Historical match confirmed |
| Soy Isolate 25% Standard | Palmfett 70% Technische Qualität | auto_generated | Cross-referenced with transactions |
| Maltodextrin DE18 | Soja Isolate 50% Premiumqualität | unverified | Auto-mapped, validated |
| Meridian Enterprise | Nexus Solutions SAS | auto_generated | Auto-mapped, validated |
| rapeseed oil | DE-99.5-ST-905 | pending_review | Verified via product specs |
| NO-LO-114 Ltd. | Zenith Verarbeitung | unverified | Auto-mapped, validated |
| Lactic Acid | maltodextrin de18 pharma grade | unverified | Auto-mapped, validated |
| Pinnacle Chemicals SA | PR-PA-794 PLC | auto_generated | Verified via product specs |
| Excise BR 5% | VA-ST-F-5-251 | unverified | Confirmed by domain expert |
| LA-AC-FO-GR-469 | Isoglucose | unverified | Historical match confirmed |
| Natriumbenzoat 99.5% Technische Qualität | sodium benzoate | auto_generated | Confirmed by domain expert |
| Coconut Oil Food Grade | Kasein | unverified | Verified via product specs |
| excise us 5% | SIG-53-IAB-UGH9 | auto_generated | Verified via product specs |
| Sodium Benzoate Pharma Grade | calcium carbonate 25% pharma grade | auto_generated | Confirmed by domain expert |
| glucose syrup 98% food grade | Citric Acid 50% Grade A | unverified | Confirmed by domain expert |
| CO-IN-421 | premier solutions Corp. | unverified | Verified via product specs |
| Atlantic Handel BV | premier enterprise Holdings | pending_review | Auto-mapped, validated |
| Quantum Rohstoffe | SIG-41-LVX-8RWD SAS | pending_review | Auto-mapped, validated |
| SIG-58-NPG-WEEE PLC | Prism Manufacturing LLC | auto_generated | Historical match confirmed |
| Sonnenblumenöl Qualitätsstufe I | SO-AC-50-FO-GR-250 | auto_generated | Auto-mapped, validated |
| SU-OI-TE-705 | maltodextrin de25 | pending_review | Auto-mapped, validated |
| Ascorbic Acid 98% Premium | dextrose standard | pending_review | Verified via product specs |
| PA-OI-98-856 | Glucose Syrup 98% | pending_review | Verified via product specs |
| Atlas Werkstoffe | CA-MA-271 | unverified | Confirmed by domain expert |
| Pea Protein 25% | CA-CA-98-928 | unverified | Auto-mapped, validated |
| Weizenklebereiweiß 99.5% Technische Qualität | WH-GL-138 | auto_generated | Auto-mapped, validated |
| SIG-65-TTX-PCJA | Elite Materials | pending_review | Historical match confirmed |
| Lactic Acid Technische Qualität | DE-PH-GR-173 | unverified | Verified via product specs |
| CE-SU-CO-752 | SIG-97-JHL-5AAT | pending_review | Verified via product specs |
| palm oil 50% | Sodium Chloride 99.5% Grade A | unverified | Historical match confirmed |
| Nordic Logistik PLC | Meridian Distribution | pending_review | Cross-referenced with transactions |
| Natriumbenzoat 25% | RE-ST-98-445 | unverified | Confirmed by domain expert |
| SIG-29-ZZE-ZUAD | Pea Protein 99.5% Premium | pending_review | Auto-mapped, validated |
| Fructose 98% Premiumqualität | Calcium Carbonate | auto_generated | Cross-referenced with transactions |
| dextrose standard | Ascorbic Acid 70% | pending_review | Historical match confirmed |
| apex sourcing | PR-SO-469 | auto_generated | Historical match confirmed |
| Dextrose 25% | Kaliumsorbat | pending_review | Cross-referenced with transactions |
| Vertex Logistics Holdings | SIG-59-HNQ-A8N5 Ltd. | pending_review | Cross-referenced with transactions |
| CI-AC-70-265 | casein 70% tech grade | unverified | Historical match confirmed |
| SIG-19-TLQ-1P5Z | potassium sorbate | auto_generated | Auto-mapped, validated |
| EX-F-19-312 | Vat Standardqualität FR 0% | unverified | Historical match confirmed |
| SIG-91-WVE-3ESP | Dextrin 99.5% | pending_review | Cross-referenced with transactions |
| Premier Logistik | VE-SO-366 | unverified | Auto-mapped, validated |
| customs duty nl 21% | Vat Reduced GB 15% | auto_generated | Auto-mapped, validated |
| Horizon Rohstoffe PLC | EL-PA-851 | unverified | Verified via product specs |
| Withholding NL 7% | SIG-76-SFN-GRTJ | unverified | Historical match confirmed |
| Stratos Enterprise International | ST-TR-400 NV | auto_generated | Auto-mapped, validated |
| CA-MA-366 | SIG-45-ZQV-Q4GS | pending_review | Verified via product specs |
| vat standard br 7% | Customs Duty NL 25% | auto_generated | Verified via product specs |
| elite sourcing | Core Werkstoffe | pending_review | Confirmed by domain expert |
| Global Rohstoffe AG | Atlas Commodities SAS | unverified | Auto-mapped, validated |
| Global Versorgung | AT-PR-442 | unverified | Verified via product specs |
| SIG-98-YBY-PFKQ | Pinnacle Sourcing | pending_review | Confirmed by domain expert |
| SIG-54-MUH-KY6K | Vat Standardqualität DE 21% | pending_review | Auto-mapped, validated |
| pea protein 98% standard | Citric Acid Premium | unverified | Auto-mapped, validated |
| PE-PR-50-128 | maltodextrin de10 | pending_review | Verified via product specs |
| stratos sourcing | Core Sourcing | auto_generated | Cross-referenced with transactions |
| SIG-86-JSN-H9KJ SA | BA-SU-479 | auto_generated | Verified via product specs |
| PA-OI-632 | Dextrose Grade A | auto_generated | Auto-mapped, validated |
| WI-G-21-298 | Excise DE 10% | unverified | Historical match confirmed |
| casein | Isoglucose Premiumqualität | unverified | Confirmed by domain expert |
| Stratos Sourcing | Premier Werkstoffe | pending_review | Cross-referenced with transactions |
| SIG-29-BKQ-HXCX Group | nexus enterprise NV | pending_review | Verified via product specs |
| Vat Reduced BR 10% | VA-ST-N-20-984 | pending_review | Auto-mapped, validated |
| Traubenzucker 99.5% | dextrose | pending_review | Auto-mapped, validated |
| EL-SO-472 | meridian materials | unverified | Auto-mapped, validated |
| Nexus Logistik | Pinnacle Materials | pending_review | Cross-referenced with transactions |
| SIG-70-KJX-6V9L | Zenith Logistics | unverified | Confirmed by domain expert |
| Ascorbic Acid Pharmazeutisch rein | SO-CH-892 | unverified | Historical match confirmed |
| Sonnenblumenöl Standardqualität | SIG-84-HFZ-NPNZ | unverified | Auto-mapped, validated |
| Global Solutions International | Baltic Chemicals AG | unverified | Historical match confirmed |
| PA-MA-664 | Catalyst Werkstoffe | unverified | Confirmed by domain expert |
| WH-GL-830 | calcium carbonate 98% pharma grade | unverified | Cross-referenced with transactions |
| Resistente Stärke 70% | SIG-21-PIO-0RWR | pending_review | Cross-referenced with transactions |
| CY-PH-GR-870 | Isoglucose | unverified | Auto-mapped, validated |
| PA-SU-CO-905 | SIG-44-DLM-CU63 | auto_generated | Cross-referenced with transactions |
| Citric Acid Pharma Grade | Soja Isolate 50% | pending_review | Cross-referenced with transactions |
| Palm Oil 25% Grade A | Isoglucose | pending_review | Confirmed by domain expert |
| Vat Standardqualität BR 15% | Vat Standard FR 20% | pending_review | Confirmed by domain expert |
| PA-OI-TE-134 | Maltodextrin-Pulver DE15 | auto_generated | Verified via product specs |
| vat reduced gb 25% | VA-RE-C-10-444 | pending_review | Auto-mapped, validated |
| SIG-90-XNG-UYZN | atlas materials | unverified | Auto-mapped, validated |
| Dextrin 50% | SIG-44-QME-TTIM | unverified | Cross-referenced with transactions |
| core supply | Core Logistics | auto_generated | Confirmed by domain expert |
| sunflower oil food grade | MA-DE-161 | auto_generated | Auto-mapped, validated |
| soy isolate standard | Sonnenblumenöl Technische Qualität | unverified | Historical match confirmed |
| Prism Supply Co. | PI-MA-112 | auto_generated | Cross-referenced with transactions |
| Sunflower Oil 50% Grade A | Maltodextrin-Pulver DE25 | auto_generated | Confirmed by domain expert |
| Vat Reduced NL 15% | WI-B-25-986 | pending_review | Confirmed by domain expert |
| Weizenklebereiweiß Lebensmittelrein | Sodium Benzoate Pharma Grade | auto_generated | Auto-mapped, validated |
| Sonnenblumenöl Technische Qualität | SU-OI-TE-879 | unverified | Confirmed by domain expert |
| Glucose Syrup 99.5% Grade B | isoglucose tech grade | unverified | Auto-mapped, validated |
| Cyclodextrin | calcium carbonate 99.5% | unverified | Auto-mapped, validated |
| core logistics | SIG-39-BHZ-K8SS | pending_review | Cross-referenced with transactions |
| SIG-18-LLP-8GUU | Weizenklebereiweiß Qualitätsstufe I | unverified | Cross-referenced with transactions |
| Sodium Benzoate Pharma Grade | calcium carbonate | auto_generated | Historical match confirmed |
| BA-SU-CO-430 | Vertex Logistics | pending_review | Cross-referenced with transactions |
| Kaliumsorbat | potassium sorbate premium | auto_generated | Historical match confirmed |
| SIG-62-BTJ-PQV9 | fructose 25% | unverified | Confirmed by domain expert |
| Sunflower Oil Grade A | WH-GL-99.5-TE-628 | auto_generated | Cross-referenced with transactions |
| Zenith Manufacturing | prime processing AG | unverified | Cross-referenced with transactions |
| Ascorbic Acid 50% Technical | SIG-77-CMG-ORNE | pending_review | Confirmed by domain expert |
| Excise FR 21% | Customs Duty NL 15% | auto_generated | Confirmed by domain expert |
| lactic acid food grade | Calcium Carbonate Qualitätsstufe II | pending_review | Cross-referenced with transactions |
| SO-CH-GR-A-776 | soy isolate 25% | pending_review | Verified via product specs |
| AP-SU-CO-755 | SIG-85-TWH-HQKB | unverified | Historical match confirmed |
| SIG-58-DDZ-4JKE International | Apex Materials Group | auto_generated | Historical match confirmed |
| AP-LO-246 | Core Logistics | unverified | Cross-referenced with transactions |
| CU-DU-F-7-469 | excise in 10% | pending_review | Auto-mapped, validated |
| prism ingredients | SIG-35-VQC-JQ0H AG | pending_review | Historical match confirmed |
| Sodium Chloride Technical | SIG-91-PEG-USI6 | unverified | Cross-referenced with transactions |
| sodium chloride premium | Palmfett 99.5% Qualitätsstufe I | unverified | Auto-mapped, validated |
| Rapsöl Technische Qualität | Casein 50% Premium | unverified | Verified via product specs |
| FR-99.5-TE-779 | isoglucose 70% food grade | unverified | Auto-mapped, validated |
| sodium benzoate | Sorbinsäure 70% | pending_review | Cross-referenced with transactions |
| VA-EN-308 | pacific distribution | auto_generated | Historical match confirmed |
| Calcium Carbonate 99.5% Food Grade | cyclodextrin premium | pending_review | Verified via product specs |
| QU-SO-261 | SIG-98-HZM-47LK | pending_review | Cross-referenced with transactions |
| Apex Chemicals Corp. | SIG-41-LKO-OD4P Ltd. | unverified | Historical match confirmed |
| Vat Standardqualität DE 25% | SIG-19-JRR-02SD | unverified | Auto-mapped, validated |
| SIG-30-SYO-74WX | sodium benzoate 25% | auto_generated | Cross-referenced with transactions |
| PR-IN-135 International | Meridian Solutions LLC | unverified | Historical match confirmed |
| Excise FR 10% | Excise GB 19% | unverified | Verified via product specs |
| Glukosesirup Syrup | Fructose 99.5% Technical | auto_generated | Cross-referenced with transactions |
| SIG-57-GUP-S7UK | GL-SO-841 | unverified | Historical match confirmed |
| Kaliumsorbat | SIG-43-KEL-FPY6 | unverified | Historical match confirmed |
| Casein 25% Technical | Kaliumsorbat | unverified | Verified via product specs |
| Palm Oil 98% | PE-PR-746 | unverified | Cross-referenced with transactions |
| PR-LO-745 | SIG-16-CZD-P41B | auto_generated | Confirmed by domain expert |
| RE-ST-GR-B-598 | citric acid food grade | unverified | Confirmed by domain expert |
| resistant starch | Isoglucose | auto_generated | Historical match confirmed |
| CU-DU-N-15-558 | SIG-70-QEI-4QFG | unverified | Historical match confirmed |
| potassium sorbate 98% | CA-98-TE-238 | auto_generated | Cross-referenced with transactions |
| CI-AC-99.5-674 | SIG-76-IIX-V2Y9 | unverified | Cross-referenced with transactions |
| Calcium Carbonate 70% Premiumqualität | dextrin | auto_generated | Historical match confirmed |
| Isoglucose 25% Lebensmittelrein | SIG-48-ASO-8G0Y | pending_review | Verified via product specs |
| Premier Partners SARL | apex chemicals Inc. | unverified | Confirmed by domain expert |
| Rapeseed Oil 70% Premium | Maltodextrin-Pulver DE15 | unverified | Cross-referenced with transactions |
| Vanguard Logistik SA | Stellar Distribution | pending_review | Historical match confirmed |
| PR-LO-704 | quantum supply | unverified | Confirmed by domain expert |
| Excise DE 21% | VA-ST-F-5-251 | auto_generated | Confirmed by domain expert |
| Prime Partners | Nexus Enterprise | pending_review | Confirmed by domain expert |
| citric acid 99.5% | CO-OI-70-553 | auto_generated | Cross-referenced with transactions |
| Prism Versorgung GmbH | PR-MA-609 | unverified | Auto-mapped, validated |
| Natriumbenzoat 50% Technische Qualität | resistant starch food grade | unverified | Confirmed by domain expert |
| SIG-58-BDP-AYRN | Pinnacle Logistics BV | pending_review | Historical match confirmed |
| SIG-25-ROA-G6G0 | Palm Oil Food Grade | unverified | Confirmed by domain expert |
| SO-IS-FO-GR-334 | isoglucose 70% | auto_generated | Auto-mapped, validated |
| RE-ST-25-FO-GR-112 | Soy Isolate 50% Grade B | unverified | Confirmed by domain expert |
| SIG-34-GNA-EHC2 | Fructose | unverified | Historical match confirmed |
| Soy Isolate Technical | SIG-10-TIC-7Q1D | auto_generated | Verified via product specs |
| Prime Logistik | Stratos Materials | unverified | Cross-referenced with transactions |
| CO-OI-966 | SIG-80-QOK-BKBF | auto_generated | Cross-referenced with transactions |
| Sorbic Acid Standard | soy isolate standard | pending_review | Historical match confirmed |
| CO-OI-FO-GR-162 | Calcium Carbonate Grade B | unverified | Auto-mapped, validated |
| sodium chloride | SIG-91-FOC-36I6 | auto_generated | Historical match confirmed |
| SIG-42-BSJ-L2CG | Stellar Werkstoffe | auto_generated | Confirmed by domain expert |
| Kaliumsorbat Premiumqualität | MA-DE-700 | pending_review | Cross-referenced with transactions |
| ascorbic acid 99.5% tech grade | SIG-96-DUH-99Q6 | pending_review | Historical match confirmed |
| horizon supply | Apex Sourcing | pending_review | Auto-mapped, validated |
| Pacific Industries Holdings | NE-PR-315 Holdings | auto_generated | Confirmed by domain expert |
| QU-SO-233 | SIG-63-NTB-209C | pending_review | Auto-mapped, validated |
| Maltodextrin DE5 Food Grade | Coconut Oil | auto_generated | Auto-mapped, validated |
| LA-AC-TE-651 | SIG-83-XMM-APXP | pending_review | Verified via product specs |
| quantum trading SARL | SIG-78-QFN-H3BV | unverified | Confirmed by domain expert |
| Sonnenblumenöl Premiumqualität | ascorbic acid standard | unverified | Auto-mapped, validated |
| wheat gluten 98% | Resistant Starch 99.5% | auto_generated | Cross-referenced with transactions |
| SIG-85-WWC-01LO | IS-641 | pending_review | Confirmed by domain expert |
| Core Versorgung GmbH | SIG-23-TWA-K947 | auto_generated | Confirmed by domain expert |
| sodium benzoate 99.5% tech grade | Rapeseed Oil | pending_review | Confirmed by domain expert |
| Sodium Benzoate Pharma Grade | Natriumbenzoat Standardqualität | auto_generated | Historical match confirmed |
| Vertex Logistik | Pinnacle Materials | pending_review | Historical match confirmed |
| Continental Werkstoffe NV | SIG-49-AVR-NL0H International | pending_review | Confirmed by domain expert |
| Vertex Ingredients GmbH | nordic distribution AG | auto_generated | Historical match confirmed |
| Dextrose | coconut oil 98% | unverified | Verified via product specs |
| Resistente Stärke Technische Qualität | LA-AC-893 | unverified | Cross-referenced with transactions |
| Rapsöl 70% Premiumqualität | maltodextrin de20 | pending_review | Historical match confirmed |
| Weizenklebereiweiß 99.5% | SIG-50-NZZ-E4UN | auto_generated | Auto-mapped, validated |
| catalyst supply | PR-SU-CO-333 | unverified | Verified via product specs |
| VA-ST-I-5-735 | Excise US 20% | auto_generated | Historical match confirmed |
| calcium carbonate standard | CI-AC-99.5-674 | unverified | Auto-mapped, validated |
| AS-AC-165 | SIG-30-UET-0Q2O | pending_review | Verified via product specs |
| prism manufacturing NV | Elite Partners GmbH | unverified | Auto-mapped, validated |
| Palm Oil 98% | Fructose 99.5% | pending_review | Confirmed by domain expert |
| Sodium Benzoate | Ascorbic Acid Premiumqualität | auto_generated | Verified via product specs |
| SIG-42-UOJ-4ACC Holdings | Stratos Trading Holdings | unverified | Confirmed by domain expert |
| SIG-82-JMP-PVGN | CY-PR-796 | unverified | Confirmed by domain expert |
| sodium chloride 98% pharma grade | Maltodextrin DE18 | auto_generated | Historical match confirmed |
| Global Chemicals SAS | VA-EN-308 | pending_review | Historical match confirmed |
| Natriumchlorid 99.5% Qualitätsstufe I | resistant starch standard | pending_review | Cross-referenced with transactions |
| prism industries International | Stellar Verarbeitung | auto_generated | Verified via product specs |
| core chemicals Holdings | SIG-60-GCS-MZ2C Ltd. | pending_review | Confirmed by domain expert |
| sodium benzoate 99.5% premium | PO-SO-PR-101 | unverified | Historical match confirmed |
| SIG-88-KUG-5ITD | CY-763 | pending_review | Historical match confirmed |
| Core Chemicals | Baltic Industrien PLC | pending_review | Auto-mapped, validated |
| SIG-15-FOA-70S8 | Natriumbenzoat 70% Premiumqualität | unverified | Verified via product specs |
| CA-CA-25-PH-GR-684 | Palm Oil Grade B | pending_review | Auto-mapped, validated |
| SIG-10-TIC-7Q1D | SO-AC-658 | auto_generated | Historical match confirmed |
| Central Logistics | atlas logistics | unverified | Confirmed by domain expert |
| cyclodextrin | SIG-95-APX-PWFS | pending_review | Confirmed by domain expert |
| Sonnenblumenöl 70% | casein premium | unverified | Verified via product specs |
| Horizon Partners Ltd. | continental enterprise International | pending_review | Historical match confirmed |
| Withholding BR 20% | VA-RE-F-21-230 | unverified | Verified via product specs |
| Nordic Processing SAS | Elite Logistik | unverified | Historical match confirmed |
| Baltic Industrien PLC | SIG-88-RGQ-WZOI | pending_review | Verified via product specs |
| SIG-83-JEP-R0ZJ | Pea Protein Pharma Grade | pending_review | Auto-mapped, validated |
| Resistant Starch 98% Pharma Grade | SIG-64-BPY-A8RD | auto_generated | Auto-mapped, validated |
| Sodium Chloride 70% Grade B | casein 98% standard | auto_generated | Verified via product specs |
| SU-OI-GR-A-704 | SIG-56-SME-QSOD | pending_review | Cross-referenced with transactions |
| pinnacle industries SAS | SIG-17-DGK-V0ZS International | unverified | Auto-mapped, validated |
| vanguard sourcing | Catalyst Materials | pending_review | Auto-mapped, validated |
| AS-AC-PH-GR-192 | soy isolate 50% premium | pending_review | Auto-mapped, validated |
| glucose syrup 98% standard | Dextrin 98% | auto_generated | Cross-referenced with transactions |
| ST-PA-227 PLC | vanguard supply NV | auto_generated | Auto-mapped, validated |
| Sonnenblumenöl Qualitätsstufe I | wheat gluten | auto_generated | Historical match confirmed |
| FR-278 | Sodium Chloride Standard | unverified | Verified via product specs |
| Dextrin Grade B | PA-OI-TE-134 | pending_review | Confirmed by domain expert |
| SIG-31-CWE-03UX | Natriumbenzoat | pending_review | Historical match confirmed |
| HO-LO-886 | Apex Versorgung GmbH | pending_review | Historical match confirmed |
| Meridian Distribution | Atlas Ingredients Ltd. | auto_generated | Confirmed by domain expert |
| AP-SO-704 | Apex Solutions International | unverified | Confirmed by domain expert |
| nexus supply | SIG-86-JSN-H9KJ SA | auto_generated | Historical match confirmed |
| citric acid premium | Soy Isolate | auto_generated | Cross-referenced with transactions |
| Horizon Sourcing | Apex Sourcing | unverified | Confirmed by domain expert |
| dextrose | Dextrin 50% | unverified | Historical match confirmed |
| Dextrin 50% | SO-CH-GR-A-776 | auto_generated | Cross-referenced with transactions |
| LA-AC-GR-A-486 | Potassium Sorbate 50% Food Grade | auto_generated | Cross-referenced with transactions |
| Casein Grade A | ascorbic acid | unverified | Historical match confirmed |
| DE-25-260 | Sodium Benzoate 99.5% Standard | auto_generated | Auto-mapped, validated |
| resistant starch 50% | SIG-91-GMY-Q91Y | auto_generated | Cross-referenced with transactions |
| SIG-68-GHA-D32X | Nexus Logistik | pending_review | Verified via product specs |
| SIG-20-XIG-T8ME | Palmfett 98% | pending_review | Verified via product specs |
| Maltodextrin-Pulver DE18 | SIG-12-BIH-AKGD | unverified | Cross-referenced with transactions |
| Core Partners BV | SIG-89-WUP-8NG0 | unverified | Auto-mapped, validated |
| Vertex Handel Holdings | Atlantic Industries AG | pending_review | Confirmed by domain expert |
| premier supply | SIG-33-LXL-8AJM | auto_generated | Confirmed by domain expert |
| PI-CO-717 | Prism Manufacturing PLC | pending_review | Auto-mapped, validated |
| palm oil | Pea Protein 70% Lebensmittelrein | auto_generated | Verified via product specs |
| customs duty de 25% | Vat Reduced CN 21% | auto_generated | Verified via product specs |
| Sodium Benzoate 99.5% Grade A | Palmfett Technische Qualität | auto_generated | Cross-referenced with transactions |
| Calcium Carbonate 98% | SU-OI-251 | auto_generated | Verified via product specs |
| Stratos Supply SAS | pacific materials | auto_generated | Confirmed by domain expert |
| Meridian Logistics | CO-LO-199 | auto_generated | Verified via product specs |
| Vat Reduced BR 10% | Excise BR 10% | pending_review | Cross-referenced with transactions |
| Catalyst Industries International | Elite Werkstoffe | auto_generated | Verified via product specs |
| FR-50-ST-130 | Isoglucose Qualitätsstufe II | unverified | Historical match confirmed |
| Atlantic Sourcing | Baltic Versorgung GmbH | unverified | Cross-referenced with transactions |
| SIG-48-KTU-I0WF | Customs Duty FR 7% | unverified | Verified via product specs |
| SIG-36-TML-VS0J | Cyclodextrin Standard | unverified | Cross-referenced with transactions |
| CO-OI-FO-GR-162 | SIG-66-LJV-5E3H | unverified | Historical match confirmed |
| dextrose | FR-99.5-TE-579 | unverified | Cross-referenced with transactions |
| Palm Oil | Isoglucose | pending_review | Historical match confirmed |
| SIG-36-TML-VS0J | dextrin standard | pending_review | Cross-referenced with transactions |
| SO-CH-TE-789 | ascorbic acid tech grade | unverified | Confirmed by domain expert |
| baltic chemicals AG | AT-CH-905 Holdings | unverified | Verified via product specs |
| EX-C-25-332 | excise gb 19% | unverified | Cross-referenced with transactions |
| stratos supply | SIG-38-FPC-A25N | auto_generated | Auto-mapped, validated |
| Natriumchlorid | rapeseed oil tech grade | unverified | Confirmed by domain expert |
| WH-GL-123 | Lactic Acid Qualitätsstufe II | unverified | Historical match confirmed |
| SIG-78-LTE-H4VL | sodium benzoate premium | auto_generated | Confirmed by domain expert |
| SIG-24-LUX-S83X | Excise FR 10% | unverified | Verified via product specs |
| withholding gb 21% | Vat Reduced DE 20% | pending_review | Verified via product specs |
| AT-LO-628 | SIG-63-NTB-209C | auto_generated | Historical match confirmed |
| Quantum Handel Ltd. | SIG-53-NHM-OFA2 | unverified | Verified via product specs |
| IS-GR-B-640 | Sonnenblumenöl | unverified | Confirmed by domain expert |
| Atlas Industrien International | pacific industries International | auto_generated | Verified via product specs |
| SIG-81-SBE-HL1C | Lactic Acid Grade B | auto_generated | Verified via product specs |
| SIG-48-LHY-R0O8 | Palmfett Lebensmittelrein | auto_generated | Verified via product specs |
| Natriumbenzoat 99.5% Qualitätsstufe I | WH-GL-99.5-TE-628 | auto_generated | Cross-referenced with transactions |
| LA-AC-393 | Palmfett 50% | pending_review | Historical match confirmed |
| SIG-71-WDX-2GRR | Zitronensäure Qualitätsstufe II | auto_generated | Cross-referenced with transactions |
| Natriumbenzoat | RE-ST-GR-B-677 | unverified | Historical match confirmed |
| Horizon Sourcing | ST-LO-745 | unverified | Confirmed by domain expert |
| Apex Manufacturing | SIG-53-HTQ-XVWB Group | pending_review | Auto-mapped, validated |
| SIG-44-UIE-SASC | Ascorbic Acid Lebensmittelrein | pending_review | Verified via product specs |
| Glukosesirup Syrup | resistant starch 50% | pending_review | Auto-mapped, validated |
| lactic acid 98% | SIG-75-XMY-5X1F | auto_generated | Confirmed by domain expert |
| Central Manufacturing Ltd. | Meridian Logistics | pending_review | Verified via product specs |
| SIG-70-ZNI-VX97 NV | atlantic supply | unverified | Confirmed by domain expert |
| Citric Acid Premium | SIG-82-TQD-ODWH | unverified | Historical match confirmed |
| Meridian Logistics | SIG-98-HZM-47LK | auto_generated | Confirmed by domain expert |
| SIG-37-MXA-3C7Q | Zitronensäure 50% Pharmazeutisch rein | auto_generated | Verified via product specs |
| SIG-57-YNB-5KMT | SO-IS-50-GR-B-983 | pending_review | Verified via product specs |
| Sonnenblumenöl Qualitätsstufe II | SO-CH-70-317 | unverified | Auto-mapped, validated |
| SIG-19-VTP-JBQ4 | Kaliumsorbat 98% | auto_generated | Verified via product specs |
| SIG-20-MSW-TMXG | Baltic Rohstoffe Ltd. | pending_review | Auto-mapped, validated |
| PE-PR-25-185 | Zitronensäure Qualitätsstufe I | unverified | Confirmed by domain expert |
| Customs Duty IN 5% | SIG-92-NWY-1FV5 | pending_review | Historical match confirmed |
| Withholding DE 20% | vat reduced cn 21% | unverified | Cross-referenced with transactions |
| rapeseed oil food grade | Palm Oil 50% | unverified | Confirmed by domain expert |
| SIG-56-ZVH-GATJ | Palm Oil 98% | auto_generated | Historical match confirmed |
| CO-OI-98-FO-GR-748 | Zitronensäure Lebensmittelrein | unverified | Cross-referenced with transactions |
| Traubenzucker 50% | Soy Isolate 98% Premium | auto_generated | Auto-mapped, validated |
| maltodextrin de5 standard | SIG-48-ASO-8G0Y | pending_review | Confirmed by domain expert |
| VA-ST-B-25-316 | Vat Reduced NL 21% | auto_generated | Auto-mapped, validated |
| Dextrin Pharma Grade | FR-FO-GR-823 | auto_generated | Historical match confirmed |
| SO-BE-FO-GR-835 | SIG-63-MOD-EKOJ | auto_generated | Confirmed by domain expert |
| SIG-81-FXX-6VPL | Rapeseed Oil 99.5% Technical | pending_review | Historical match confirmed |
| Maltodextrin DE15 | SIG-72-IMA-8RAP | unverified | Auto-mapped, validated |
| Dextrin 99.5% | CI-AC-857 | unverified | Cross-referenced with transactions |
| FR-PH-GR-146 | SIG-26-KHF-99OH | pending_review | Historical match confirmed |
| Cyclodextrin 98% Pharma Grade | lactic acid | auto_generated | Historical match confirmed |
| stellar manufacturing International | SIG-34-TUW-UWNZ Group | pending_review | Auto-mapped, validated |
| CI-AC-488 | Kaliumsorbat | unverified | Confirmed by domain expert |
| ascorbic acid 98% premium | DE-TE-380 | auto_generated | Historical match confirmed |
| prime logistics NV | SIG-14-BST-M9NP GmbH | unverified | Auto-mapped, validated |
| Lactic Acid | rapeseed oil | pending_review | Confirmed by domain expert |
| CO-IN-754 International | meridian distribution Holdings | pending_review | Verified via product specs |
| Prime Rohstoffe LLC | SIG-25-KUC-FYE7 Ltd. | pending_review | Cross-referenced with transactions |
| Pea Protein 98% Qualitätsstufe II | Isoglucose Grade B | pending_review | Historical match confirmed |
| Sorbic Acid 25% Grade B | SIG-57-HAE-WNSM | unverified | Confirmed by domain expert |
| PA-OI-TE-134 | Soy Isolate | pending_review | Confirmed by domain expert |
| Horizon Versorgung GmbH | SIG-65-MYR-QISO | unverified | Verified via product specs |
| Customs Duty FR 7% | Vat Standard IN 0% | pending_review | Historical match confirmed |
| Baltic Sourcing | Prism Versorgung GmbH | auto_generated | Auto-mapped, validated |
| Pea Protein Grade B | casein | pending_review | Confirmed by domain expert |
| SO-AC-377 | coconut oil 98% | pending_review | Cross-referenced with transactions |
| SIG-19-TPS-MSKY | potassium sorbate | unverified | Verified via product specs |
| CA-CA-GR-B-761 | SIG-73-KLZ-PDKU | unverified | Auto-mapped, validated |
| Sonnenblumenöl Standardqualität | sodium chloride tech grade | unverified | Historical match confirmed |
| Zenith Supply Co. | HO-LO-597 | pending_review | Auto-mapped, validated |
| Natriumbenzoat 25% | Soy Isolate | unverified | Cross-referenced with transactions |
| SIG-30-UET-0Q2O | Calcium Carbonate | unverified | Confirmed by domain expert |
| VA-RE-C-21-521 | Customs Duty BR 15% | unverified | Verified via product specs |
| Palm Oil Grade B | sodium benzoate food grade | auto_generated | Confirmed by domain expert |
| DE-70-GR-A-741 | lactic acid | pending_review | Verified via product specs |
| Glukosesirup Syrup Qualitätsstufe I | pea protein 50% | unverified | Confirmed by domain expert |
| SIG-31-BWX-FDET | EX-D-7-904 | auto_generated | Verified via product specs |
| Atlantic Versorgung GmbH | VE-LO-693 | unverified | Historical match confirmed |
| CE-LO-195 | SIG-99-AYV-D18J International | unverified | Auto-mapped, validated |
| Horizon Distribution Holdings | SIG-32-DNR-U0SL | unverified | Auto-mapped, validated |
| SIG-18-NCG-WT1V | CA-CA-50-260 | auto_generated | Verified via product specs |
| SIG-45-ZZU-GRXH International | nordic distribution AG | auto_generated | Confirmed by domain expert |
| Baltic Handel NV | ME-DI-790 Group | pending_review | Confirmed by domain expert |
| CI-AC-TE-350 | Calcium Carbonate Premiumqualität | auto_generated | Auto-mapped, validated |
| AT-SU-CO-645 | apex supply | auto_generated | Verified via product specs |
| Sodium Chloride 70% Grade B | Kaliumsorbat 50% Lebensmittelrein | auto_generated | Historical match confirmed |
| meridian supply | SIG-46-DGC-R6Z2 | unverified | Verified via product specs |
| maltodextrin de30 | Dextrin 50% | auto_generated | Auto-mapped, validated |
| elite materials | Stellar Versorgung GmbH | pending_review | Verified via product specs |
| Lactic Acid Food Grade | resistant starch tech grade | auto_generated | Historical match confirmed |
| SO-BE-PH-GR-647 | Casein 25% Grade A | pending_review | Cross-referenced with transactions |
| Natriumbenzoat | SIG-39-KIX-VA2J | auto_generated | Auto-mapped, validated |
| Sonnenblumenöl | Sodium Chloride Technical | pending_review | Auto-mapped, validated |
| Stratos Sourcing | Pacific Versorgung GmbH | pending_review | Cross-referenced with transactions |
| prime sourcing | Core Logistik | unverified | Auto-mapped, validated |
| Catalyst Industrien International | pacific ingredients NV | auto_generated | Verified via product specs |
| continental logistics | Stellar Versorgung GmbH | auto_generated | Confirmed by domain expert |
| SIG-92-AXW-GPAG | Quantum Verarbeitung PLC | auto_generated | Confirmed by domain expert |
| Vat Standardqualität GB 19% | excise us 20% | pending_review | Auto-mapped, validated |
| CI-AC-PR-827 | Lactic Acid Food Grade | auto_generated | Historical match confirmed |
| nordic sourcing | SIG-59-EWO-HAXW | unverified | Auto-mapped, validated |
| pacific supply | Central Materials | pending_review | Verified via product specs |
| SO-AC-25-PH-GR-887 | cyclodextrin standard | unverified | Cross-referenced with transactions |
| Fructose Food Grade | PA-OI-399 | pending_review | Historical match confirmed |
| glucose syrup | Natriumbenzoat Standardqualität | pending_review | Auto-mapped, validated |
| Excise IN 20% | SIG-92-NWY-1FV5 | pending_review | Verified via product specs |
| Excise FR 21% | Customs Duty GB 5% | auto_generated | Historical match confirmed |
| Palm Oil 70% Pharma Grade | Ascorbic Acid | unverified | Historical match confirmed |
| SO-BE-708 | coconut oil 98% | pending_review | Confirmed by domain expert |
| SIG-65-LOJ-4KXS | Vat Standard DE 7% | auto_generated | Auto-mapped, validated |
| ascorbic acid standard | CY-PR-796 | unverified | Historical match confirmed |
| LA-AC-FO-GR-469 | Sodium Chloride 99.5% | pending_review | Confirmed by domain expert |
| SIG-40-XXD-GE9O | prime sourcing | unverified | Historical match confirmed |
| soy isolate premium | SU-OI-TE-705 | auto_generated | Auto-mapped, validated |
| RE-ST-PR-679 | SIG-76-GDP-2JN8 | pending_review | Historical match confirmed |
| DE-ST-385 | SIG-49-QVY-JMMU | unverified | Confirmed by domain expert |
| Soy Isolate Standard | Resistente Stärke 70% | pending_review | Cross-referenced with transactions |
| Horizon Logistics International | SIG-31-MAP-SEFM | auto_generated | Confirmed by domain expert |
| LA-AC-TE-761 | glucose syrup 25% | unverified | Auto-mapped, validated |
| GL-SY-PR-440 | Lactic Acid | auto_generated | Historical match confirmed |
| Sodium Benzoate Grade A | SIG-53-TLC-AZKT | auto_generated | Verified via product specs |
| prism sourcing | SIG-56-QPM-7YY5 | pending_review | Verified via product specs |
| IS-802 | Sodium Benzoate 99.5% Technical | pending_review | Cross-referenced with transactions |
| ascorbic acid tech grade | SO-IS-99.5-PR-187 | unverified | Historical match confirmed |
| Fructose Standardqualität | SIG-56-NOU-ZR98 | pending_review | Auto-mapped, validated |
| Isoglucose Technical | RE-ST-50-232 | unverified | Verified via product specs |
| nexus distribution AG | SIG-68-BSB-VSIA | auto_generated | Cross-referenced with transactions |
| PA-OI-383 | SIG-49-OHU-U248 | unverified | Historical match confirmed |
| Premier Partners Group | SIG-58-MRH-P47P | pending_review | Verified via product specs |
| Ascorbic Acid Premiumqualität | SIG-20-UGT-P0LW | unverified | Cross-referenced with transactions |
| VA-RE-I-5-252 | Excise US 7% | auto_generated | Confirmed by domain expert |
| Citric Acid 25% Technical | Weizenklebereiweiß 99.5% Technische Qualität | auto_generated | Confirmed by domain expert |
| DE-840 | Natriumbenzoat | pending_review | Cross-referenced with transactions |
| dextrose 70% | SIG-16-JKI-B4JG | pending_review | Auto-mapped, validated |
| SO-CH-99.5-GR-A-634 | ascorbic acid 99.5% standard | unverified | Historical match confirmed |
| vertex logistics | GL-SO-841 | auto_generated | Auto-mapped, validated |
| Traubenzucker 25% Technische Qualität | SIG-79-IKL-24HE | unverified | Confirmed by domain expert |
| Resistant Starch | SU-OI-GR-A-224 | unverified | Cross-referenced with transactions |
| Elite Logistics | AT-MA-363 | pending_review | Cross-referenced with transactions |
| SIG-20-IKV-891D | Vat Reduced BR 10% | unverified | Cross-referenced with transactions |
| pea protein pharma grade | SIG-27-FHX-VO6Y | unverified | Cross-referenced with transactions |
| ST-PA-504 | SIG-19-KAW-QNPA | pending_review | Auto-mapped, validated |
| Natriumchlorid | SIG-42-LOE-5XD8 | unverified | Confirmed by domain expert |
| Potassium Sorbate 50% Technical | Kaliumsorbat | pending_review | Auto-mapped, validated |
| SIG-60-GHI-04X0 | wheat gluten 50% tech grade | unverified | Confirmed by domain expert |
| Palm Oil 99.5% Grade A | palm oil food grade | unverified | Cross-referenced with transactions |
| Dextrin Standardqualität | sodium benzoate 99.5% | unverified | Auto-mapped, validated |
| sunflower oil premium | AS-AC-GR-B-855 | unverified | Auto-mapped, validated |
| SIG-21-PIO-0RWR | Zitronensäure 50% Qualitätsstufe I | unverified | Confirmed by domain expert |
| Rapsöl Technische Qualität | SIG-36-ZKX-4SE4 | auto_generated | Auto-mapped, validated |
| withholding in 20% | Customs Duty DE 20% | unverified | Cross-referenced with transactions |
| Horizon Partners Ltd. | SIG-95-QUH-2TS2 | pending_review | Historical match confirmed |
| sodium chloride tech grade | Sodium Benzoate Pharma Grade | pending_review | Confirmed by domain expert |
| SIG-51-EYN-NILM LLC | PI-DI-543 Ltd. | unverified | Auto-mapped, validated |
| apex supply | ST-MA-730 | auto_generated | Confirmed by domain expert |
| Sorbinsäure 98% | sodium benzoate 50% | unverified | Confirmed by domain expert |
| Sunflower Oil Pharma Grade | Traubenzucker Qualitätsstufe II | pending_review | Auto-mapped, validated |
| Premier Enterprise International | prime processing AG | unverified | Verified via product specs |
| Rapsöl | CI-AC-ST-565 | unverified | Historical match confirmed |
| sorbic acid premium | SIG-36-MYP-7NC2 | pending_review | Cross-referenced with transactions |
| Sonnenblumenöl Standardqualität | SIG-68-DWS-MNR6 | unverified | Confirmed by domain expert |
| Vat Reduced BR 10% | SIG-73-GRJ-1VRU | unverified | Auto-mapped, validated |
| Central Logistik | BA-SU-CO-480 | auto_generated | Cross-referenced with transactions |
| Pea Protein 25% | Soja Isolate Standardqualität | unverified | Verified via product specs |
| SIG-74-AEB-PMX7 | Pea Protein | pending_review | Confirmed by domain expert |
| Apex Werkstoffe International | PI-IN-244 | auto_generated | Confirmed by domain expert |
| Maltodextrin-Pulver DE30 | resistant starch 70% food grade | auto_generated | Cross-referenced with transactions |
| Baltic Werkstoffe | catalyst supply | pending_review | Confirmed by domain expert |
| SIG-67-JNR-XNTM | atlas materials | pending_review | Historical match confirmed |
| SIG-22-VQM-AGKC | Dextrose Grade A | auto_generated | Auto-mapped, validated |
| SIG-82-PJM-2KX0 | Pinnacle Supply Co. | pending_review | Verified via product specs |
| Sunflower Oil Technical | resistant starch pharma grade | unverified | Auto-mapped, validated |
| PI-IN-970 Corp. | central solutions | auto_generated | Cross-referenced with transactions |
| Atlantic Werkstoffe | Baltic Supply Co. | pending_review | Auto-mapped, validated |
| Nordic Versorgung GmbH | ST-SO-491 | pending_review | Confirmed by domain expert |
| citric acid premium | SIG-99-VAH-2H31 | pending_review | Historical match confirmed |
| Sodium Chloride | SIG-25-WDK-CWCD | auto_generated | Verified via product specs |
| AT-SO-915 | SIG-86-ILL-9XTM | unverified | Historical match confirmed |
| SIG-83-KGL-Q4QE | dextrose 25% tech grade | unverified | Verified via product specs |
| SIG-77-LSN-T27F | Citric Acid 25% | pending_review | Confirmed by domain expert |
| potassium sorbate 50% standard | Ascorbic Acid Standard | unverified | Auto-mapped, validated |
| Catalyst Werkstoffe | SIG-77-MDI-MBKO | auto_generated | Verified via product specs |
| atlas enterprise | SIG-32-WFB-DVCF International | unverified | Verified via product specs |
| LA-AC-927 | Coconut Oil 98% Technical | unverified | Auto-mapped, validated |
| MA-DE-738 | wheat gluten | unverified | Confirmed by domain expert |
| Stratos Versorgung GmbH | Premier Supply Co. | pending_review | Auto-mapped, validated |
| apex manufacturing KG | Stellar Distribution SA | pending_review | Historical match confirmed |
| SIG-58-MKV-8WKD | CA-LO-415 | pending_review | Cross-referenced with transactions |
| Atlantic Trading | catalyst processing Holdings | pending_review | Confirmed by domain expert |
| Vertex Vertrieb Group | VE-DI-578 International | pending_review | Confirmed by domain expert |
| Coconut Oil 70% Grade A | potassium sorbate standard | pending_review | Historical match confirmed |
| SIG-68-BSO-NW8J Group | BA-PR-950 | pending_review | Confirmed by domain expert |
| SIG-88-AJL-T9ZS | RE-ST-PR-679 | auto_generated | Confirmed by domain expert |
| SIG-15-AXQ-9Z8K | Customs Duty DE 7% | auto_generated | Auto-mapped, validated |
| SIG-42-BSJ-L2CG | prism materials | pending_review | Verified via product specs |
| LA-AC-690 | SIG-77-LFQ-EKT4 | pending_review | Historical match confirmed |
| dextrin 70% pharma grade | SIG-19-QLH-ILRZ | unverified | Confirmed by domain expert |
| Sorbinsäure | SIG-79-RKA-P64T | auto_generated | Auto-mapped, validated |
| Cyclodextrin Standard | SIG-79-SPO-WT80 | auto_generated | Historical match confirmed |
| SIG-57-YOY-F7N2 | Palm Oil Grade B | pending_review | Cross-referenced with transactions |
| Apex Sourcing | SIG-24-YWL-8DWF | unverified | Confirmed by domain expert |
| Glukosesirup Syrup Premiumqualität | rapeseed oil 50% pharma grade | pending_review | Cross-referenced with transactions |
| Central Materials NV | Central Manufacturing Ltd. | pending_review | Verified via product specs |
| cyclodextrin 70% food grade | DE-GR-A-250 | unverified | Auto-mapped, validated |
| stratos logistics | Pinnacle Materials | auto_generated | Confirmed by domain expert |
| pea protein | SIG-60-IRZ-OTKZ | auto_generated | Verified via product specs |
| Rapsöl 50% Pharmazeutisch rein | Soy Isolate Technical | auto_generated | Historical match confirmed |
| Pinnacle Trading | Meridian Ingredients | pending_review | Historical match confirmed |
| ascorbic acid premium | Fructose 50% Standardqualität | unverified | Confirmed by domain expert |
| Vat Standardqualität US 21% | SIG-72-IQP-IKAX | pending_review | Confirmed by domain expert |
| Core Rohstoffe | SIG-68-SJS-K3N3 | unverified | Historical match confirmed |
| coconut oil 25% | Dextrin Standardqualität | unverified | Cross-referenced with transactions |
| SIG-27-VCT-2O4S | central materials | unverified | Confirmed by domain expert |
| Palm Oil Food Grade | CI-AC-99.5-440 | auto_generated | Auto-mapped, validated |
| Nordic Manufacturing Holdings | Global Verarbeitung Group | unverified | Confirmed by domain expert |
| SIG-79-OZQ-4I2N | Traubenzucker 70% Qualitätsstufe I | unverified | Cross-referenced with transactions |
| Coconut Oil 99.5% Pharma Grade | Ascorbic Acid Technische Qualität | unverified | Verified via product specs |
| Nexus Materials | SIG-28-SOZ-K6XK | pending_review | Verified via product specs |
| Kaliumsorbat | SO-BE-99.5-GR-A-143 | unverified | Historical match confirmed |
| Pinnacle Chemicals SAS | Stratos Ingredients Group | auto_generated | Verified via product specs |
| SIG-67-TPL-WT5F | Isoglucose | pending_review | Confirmed by domain expert |
| NE-SO-511 | SIG-54-ZFB-4REP Inc. | unverified | Confirmed by domain expert |
| sodium chloride | SIG-21-HVD-EZVS | pending_review | Historical match confirmed |
| Meridian Distribution | CE-MA-847 | auto_generated | Historical match confirmed |
| SIG-81-LVQ-2J60 | prism manufacturing Ltd. | pending_review | Auto-mapped, validated |
| BA-IN-547 | atlas solutions | pending_review | Auto-mapped, validated |
| Nexus Processing International | SIG-72-FHF-DYSG | pending_review | Auto-mapped, validated |
| CO-LO-944 | prime logistics | unverified | Historical match confirmed |
| VE-SU-CO-378 | Prime Logistik | auto_generated | Confirmed by domain expert |
| SIG-64-BPY-A8RD | WH-GL-99.5-TE-628 | pending_review | Verified via product specs |
| Horizon Sourcing | SIG-73-KSW-UVZU | auto_generated | Confirmed by domain expert |
| CE-LO-198 Holdings | Central Logistik Holdings | auto_generated | Verified via product specs |
| vat reduced gb 25% | VA-ST-I-19-287 | pending_review | Verified via product specs |
| SO-BE-708 | SIG-44-FWT-OA3N | unverified | Cross-referenced with transactions |
| Dextrin 50% | SIG-64-TCV-R5SR | auto_generated | Confirmed by domain expert |
| SIG-44-UKH-MO4F | Vat Reduced FR 25% | pending_review | Historical match confirmed |
| Ascorbic Acid 98% Qualitätsstufe II | SO-CH-ST-522 | auto_generated | Confirmed by domain expert |
| Baltic Distribution Group | ST-SU-959 KG | unverified | Auto-mapped, validated |
| Coconut Oil 98% Lebensmittelrein | Cyclodextrin 70% Food Grade | auto_generated | Confirmed by domain expert |
| Excise GB 5% | SIG-90-NAM-FDV1 | unverified | Verified via product specs |
| PA-LO-382 Group | global processing | pending_review | Auto-mapped, validated |
| Central Vertrieb | NO-LO-598 Holdings | auto_generated | Cross-referenced with transactions |
| SIG-41-FFO-RXYJ | Weizenklebereiweiß | auto_generated | Cross-referenced with transactions |
| Soja Isolate Pharmazeutisch rein | RA-OI-98-679 | auto_generated | Historical match confirmed |
| Nexus Materials | central logistics | unverified | Auto-mapped, validated |
| Pinnacle Logistics International | Atlas Partners | unverified | Verified via product specs |
| SIG-90-SZM-PZJ4 | Kasein 25% Pharmazeutisch rein | auto_generated | Verified via product specs |
| Rapsöl 50% Qualitätsstufe I | SIG-56-LHF-WMFP | pending_review | Confirmed by domain expert |
| Dextrin Technical | SIG-94-KAU-6F8H | auto_generated | Verified via product specs |
| AP-PR-849 PLC | prime processing AG | pending_review | Verified via product specs |
| Prism Werkstoffe Ltd. | Nordic Manufacturing NV | auto_generated | Confirmed by domain expert |
| PO-SO-ST-111 | Sodium Chloride 70% | unverified | Verified via product specs |
| SIG-98-CGL-FHWJ | Kasein Premiumqualität | auto_generated | Historical match confirmed |
| Excise CN 19% | SIG-47-TWK-RYLY | pending_review | Auto-mapped, validated |
| SIG-94-TUN-H84G | Coconut Oil 25% | auto_generated | Verified via product specs |
| CO-OI-FO-GR-162 | SIG-84-VYG-QI55 | unverified | Historical match confirmed |
| SO-AC-GR-A-997 | SIG-23-OPT-7QHV | pending_review | Verified via product specs |
| CU-DU-C-25-616 | Withholding BR 20% | pending_review | Auto-mapped, validated |
| PE-PR-251 | SIG-66-JGK-EM8M | auto_generated | Cross-referenced with transactions |
| dextrose 70% | SIG-39-UPB-Q8DA | auto_generated | Auto-mapped, validated |
| Lactic Acid 25% Premium | citric acid 99.5% | auto_generated | Verified via product specs |
| coconut oil food grade | Ascorbic Acid Premiumqualität | unverified | Auto-mapped, validated |
| sodium chloride 98% standard | Coconut Oil 25% | unverified | Cross-referenced with transactions |
| SIG-88-AGF-FF5L | ascorbic acid tech grade | auto_generated | Verified via product specs |
| WH-GL-GR-A-924 | Lactic Acid | auto_generated | Confirmed by domain expert |
| SIG-58-WYL-XCXB | Stellar Manufacturing Holdings | pending_review | Cross-referenced with transactions |
| DE-50-891 | Citric Acid 70% | unverified | Auto-mapped, validated |
| Calcium Carbonate | Traubenzucker 25% Technische Qualität | pending_review | Cross-referenced with transactions |
| Atlantic Manufacturing International | Elite Solutions | auto_generated | Cross-referenced with transactions |
| SO-BE-70-PR-120 | coconut oil food grade | auto_generated | Historical match confirmed |
| Soy Isolate | SIG-24-MFK-ZAUG | unverified | Historical match confirmed |
| SIG-62-BTJ-PQV9 | AS-AC-FO-GR-283 | auto_generated | Historical match confirmed |
| MA-DE-186 | Lactic Acid 50% Grade A | auto_generated | Historical match confirmed |
| Elite Logistik | SIG-88-RGQ-WZOI | auto_generated | Historical match confirmed |
| SIG-16-IYP-EOZP | Coconut Oil 98% Technical | pending_review | Confirmed by domain expert |
| HO-LO-699 | SIG-13-PHC-GSY7 | pending_review | Auto-mapped, validated |
| QU-LO-616 | SIG-10-PGH-BTUF | auto_generated | Historical match confirmed |
| VA-MA-537 Holdings | SIG-56-EAF-SHQE Group | auto_generated | Verified via product specs |
| Zitronensäure 70% Lebensmittelrein | Dextrose Technical | auto_generated | Verified via product specs |
| Core Logistik | Meridian Materials | pending_review | Historical match confirmed |
| AP-MA-145 International | Stratos Processing | pending_review | Historical match confirmed |
| Atlantic Supply Co. | horizon materials | pending_review | Verified via product specs |
| SO-BE-667 | SIG-37-PEJ-WFOY | auto_generated | Historical match confirmed |
| Ascorbic Acid 99.5% Technische Qualität | SIG-56-BPD-M0A6 | pending_review | Historical match confirmed |
| Nordic Supply Co. | Meridian Versorgung GmbH | auto_generated | Historical match confirmed |
| Vat Reduced CN 10% | SIG-46-DQX-JN7N | auto_generated | Historical match confirmed |
| pacific chemicals AG | SIG-39-JXL-BQ85 SARL | unverified | Historical match confirmed |
| Withholding US 10% | withholding in 20% | auto_generated | Cross-referenced with transactions |
| Continental Sourcing | Catalyst Werkstoffe | auto_generated | Cross-referenced with transactions |
| Withholding FR 5% | customs duty fr 7% | auto_generated | Historical match confirmed |
| Vertex Materials | SIG-76-ESC-PNV7 | auto_generated | Historical match confirmed |
| Vat Standardqualität IN 0% | vat reduced gb 20% | pending_review | Historical match confirmed |
| SO-AC-98-579 | SIG-79-GLV-IEST | pending_review | Cross-referenced with transactions |
| Isoglucose 50% Qualitätsstufe I | Wheat Gluten Grade A | auto_generated | Historical match confirmed |
| Nordic Industries Ltd. | meridian chemicals Holdings | pending_review | Auto-mapped, validated |
| Pinnacle Werkstoffe | central sourcing | pending_review | Cross-referenced with transactions |
| SIG-74-ZNA-1VYW | VA-ST-B-25-316 | auto_generated | Auto-mapped, validated |
| Zenith Trading | atlantic commodities | unverified | Auto-mapped, validated |
| Soja Isolate Premiumqualität | FR-PR-614 | pending_review | Historical match confirmed |
| SIG-71-KJM-D5G1 Holdings | Elite Materials NV | unverified | Verified via product specs |
| Sodium Benzoate Technical | maltodextrin de20 | pending_review | Verified via product specs |
| Citric Acid 99.5% | SO-CH-115 | auto_generated | Cross-referenced with transactions |
| Coconut Oil 70% | CO-OI-25-FO-GR-778 | auto_generated | Auto-mapped, validated |
| SIG-89-HLJ-NILC | Vanguard Logistik | pending_review | Historical match confirmed |
| palm oil 50% | SIG-18-KSV-TA83 | auto_generated | Historical match confirmed |
| Pea Protein 98% Grade B | CO-OI-50-147 | pending_review | Confirmed by domain expert |
| Coconut Oil Pharma Grade | PO-SO-70-899 | pending_review | Historical match confirmed |
| global chemicals SARL | Stellar Manufacturing Holdings | pending_review | Confirmed by domain expert |
| Sodium Chloride | ascorbic acid pharma grade | auto_generated | Verified via product specs |
| VE-MA-682 | SIG-48-TZQ-5ZZ0 | unverified | Verified via product specs |
| SIG-56-FFG-XS2P | PA-MA-742 KG | pending_review | Historical match confirmed |
| Wheat Gluten Grade A | Cyclodextrin Standardqualität | pending_review | Confirmed by domain expert |
| LA-AC-GR-A-486 | Sunflower Oil 70% | pending_review | Confirmed by domain expert |
| SIG-41-VXU-J3AN | VE-DI-578 International | unverified | Confirmed by domain expert |
| potassium sorbate | SIG-61-KUY-VFFK | pending_review | Historical match confirmed |
| Sonnenblumenöl Standardqualität | PO-SO-768 | auto_generated | Confirmed by domain expert |
| lactic acid standard | SO-BE-PH-GR-831 | auto_generated | Historical match confirmed |
| Wheat Gluten | WH-GL-50-865 | auto_generated | Confirmed by domain expert |
| Traubenzucker 25% | SIG-37-MXA-3C7Q | auto_generated | Auto-mapped, validated |
| Traubenzucker 25% | fructose | auto_generated | Verified via product specs |
| AT-SO-658 | Vertex Sourcing | pending_review | Historical match confirmed |
| Prism Materials | AP-LO-246 | auto_generated | Confirmed by domain expert |
| Vanguard Handel LLC | NE-EN-710 NV | pending_review | Verified via product specs |
| CO-MA-371 | nordic ingredients | auto_generated | Auto-mapped, validated |
| SIG-39-IRP-PQZF | RE-ST-575 | auto_generated | Auto-mapped, validated |
| SIG-39-BAT-DD7R | Fructose 99.5% | unverified | Confirmed by domain expert |
| CY-577 | Traubenzucker 25% Technische Qualität | auto_generated | Cross-referenced with transactions |
| quantum processing SARL | SIG-79-TAG-A44Y | unverified | Historical match confirmed |
| pea protein 70% premium | LA-AC-891 | auto_generated | Historical match confirmed |
| Pea Protein Premiumqualität | Sorbic Acid 50% Grade A | pending_review | Verified via product specs |
| CI-AC-PR-827 | Sodium Benzoate 99.5% Technical | unverified | Cross-referenced with transactions |
| casein | Sodium Chloride | pending_review | Historical match confirmed |
| Maltodextrin DE10 | SO-IS-354 | unverified | Historical match confirmed |
| Kaliumsorbat 98% | Soy Isolate 70% | pending_review | Confirmed by domain expert |
| sunflower oil 50% pharma grade | Palmfett | unverified | Confirmed by domain expert |
| Atlas Partners | Vertex Ingredients | unverified | Verified via product specs |
| Stellar Manufacturing Group | PI-IN-388 | auto_generated | Confirmed by domain expert |
| Zenith Manufacturing Holdings | Central Commodities Ltd. | auto_generated | Cross-referenced with transactions |
| customs duty fr 25% | EX-C-21-179 | auto_generated | Cross-referenced with transactions |
| potassium sorbate standard | Soja Isolate Premiumqualität | unverified | Confirmed by domain expert |
| Citric Acid Food Grade | sodium benzoate food grade | unverified | Auto-mapped, validated |
| Wheat Gluten Grade B | SIG-16-YRD-5C3Z | pending_review | Confirmed by domain expert |
| Stellar Processing Holdings | NO-IN-797 | pending_review | Verified via product specs |
| SIG-64-VAK-3T2G AG | Vertex Logistik Group | pending_review | Auto-mapped, validated |
| Palmfett 70% Technische Qualität | soy isolate 99.5% standard | unverified | Confirmed by domain expert |
| Pinnacle Ingredients KG | NO-DI-180 Ltd. | unverified | Verified via product specs |
| FR-GR-A-600 | SIG-66-FRL-CVIT | unverified | Confirmed by domain expert |
| Sorbinsäure Lebensmittelrein | glucose syrup | auto_generated | Verified via product specs |
| CU-DU-B-21-305 | Vat Reduced CN 10% | pending_review | Auto-mapped, validated |
| SIG-39-OZI-N968 | resistant starch food grade | pending_review | Historical match confirmed |
| Elite Handel Corp. | pacific industries Ltd. | auto_generated | Historical match confirmed |
| Ascorbic Acid Premiumqualität | DE-25-PR-846 | pending_review | Auto-mapped, validated |
| Nexus Processing Holdings | SIG-76-RWX-Q314 International | auto_generated | Confirmed by domain expert |
| Apex Commodities Holdings | Stratos Versorgung | pending_review | Confirmed by domain expert |
| ZE-MA-316 | SIG-41-LVX-8RWD SAS | auto_generated | Cross-referenced with transactions |
| SIG-39-UPB-Q8DA | Kasein 98% Premiumqualität | auto_generated | Historical match confirmed |
| SIG-39-JXL-BQ85 SARL | Stratos Partners SAS | pending_review | Auto-mapped, validated |
| SIG-97-SBT-Y595 | lactic acid | auto_generated | Verified via product specs |
| Soy Isolate Grade B | dextrose tech grade | unverified | Cross-referenced with transactions |
| SIG-41-ZGH-C0Y2 Holdings | Atlas Ingredients PLC | pending_review | Confirmed by domain expert |
| potassium sorbate 98% | Fructose Qualitätsstufe II | auto_generated | Auto-mapped, validated |
| SIG-61-XKV-ODPX | Palm Oil | unverified | Auto-mapped, validated |
| Continental Supply Co. | SIG-35-HUP-NW3M | auto_generated | Cross-referenced with transactions |
| SIG-92-KFT-DU1S | VA-RE-F-25-555 | auto_generated | Verified via product specs |
| citric acid 99.5% | FR-25-GR-B-641 | unverified | Verified via product specs |
| SO-IS-432 | wheat gluten 99.5% premium | pending_review | Auto-mapped, validated |
| Glucose Syrup 99.5% Grade B | dextrose standard | auto_generated | Cross-referenced with transactions |
| central materials | SIG-52-HZA-742D | auto_generated | Cross-referenced with transactions |
| calcium carbonate standard | Kaliumsorbat Technische Qualität | auto_generated | Cross-referenced with transactions |
| Dextrose | cyclodextrin | auto_generated | Cross-referenced with transactions |
| CA-CO-939 | continental processing SA | unverified | Historical match confirmed |
| prism materials | SIG-31-LIW-GW9B International | auto_generated | Historical match confirmed |
| Stratos Versorgung GmbH | SIG-20-AKD-OM7O | auto_generated | Verified via product specs |
| Traubenzucker Technische Qualität | PE-PR-746 | unverified | Historical match confirmed |
| EX-B-0-514 | SIG-65-QKW-Y1YW | auto_generated | Confirmed by domain expert |
| Resistente Stärke Technische Qualität | Dextrose Food Grade | unverified | Historical match confirmed |
| CO-PA-491 BV | Pacific Commodities SAS | pending_review | Cross-referenced with transactions |
| Fructose Grade B | Ascorbic Acid | pending_review | Confirmed by domain expert |
| Dextrin 70% Pharma Grade | Ascorbic Acid 98% Qualitätsstufe II | pending_review | Confirmed by domain expert |
| Sonnenblumenöl Qualitätsstufe I | SO-AC-99.5-338 | unverified | Cross-referenced with transactions |
| SIG-60-TMF-XHW0 | CI-AC-25-GR-A-669 | unverified | Cross-referenced with transactions |
| Catalyst Supply Holdings | AT-IN-716 Corp. | unverified | Auto-mapped, validated |
| PA-OI-98-587 | SIG-84-PAS-5S3O | pending_review | Confirmed by domain expert |
| FR-TE-414 | Casein | pending_review | Confirmed by domain expert |
| Lactic Acid Technische Qualität | wheat gluten standard | pending_review | Auto-mapped, validated |
| Stellar Sourcing | Pinnacle Supply Co. | auto_generated | Verified via product specs |
| prism ingredients AG | Stellar Versorgung SA | pending_review | Historical match confirmed |
| Core Logistik Holdings | AT-MA-324 International | auto_generated | Historical match confirmed |
| RA-OI-70-PR-405 | SIG-84-EIB-2MOT | pending_review | Cross-referenced with transactions |
| Dextrose Grade B | cyclodextrin | pending_review | Historical match confirmed |
| SIG-38-CEJ-1ISY | Sodium Benzoate 99.5% | unverified | Auto-mapped, validated |
| SIG-80-GVE-ZK1G | Prism Manufacturing PLC | pending_review | Auto-mapped, validated |
| Customs Duty US 19% | Vat Standardqualität FR 10% | auto_generated | Confirmed by domain expert |
| dextrin premium | Natriumchlorid 70% | pending_review | Cross-referenced with transactions |
| Coconut Oil 25% Food Grade | DE-TE-414 | auto_generated | Historical match confirmed |
| SIG-82-DVA-0TXE | rapeseed oil tech grade | unverified | Confirmed by domain expert |
| Zenith Processing | SIG-18-CIG-ZUL8 Holdings | auto_generated | Cross-referenced with transactions |
| Soy Isolate 25% Pharma Grade | SIG-19-QLH-ILRZ | pending_review | Verified via product specs |
| SIG-36-BVE-5U7D | SO-CH-25-PR-784 | pending_review | Verified via product specs |
| SIG-84-VYG-QI55 | RA-OI-258 | auto_generated | Cross-referenced with transactions |
| LA-AC-554 | SIG-22-VQM-AGKC | auto_generated | Cross-referenced with transactions |
| Vat Reduced GB 20% | vat standard nl 20% | pending_review | Historical match confirmed |
| Traubenzucker 99.5% Qualitätsstufe II | Rapeseed Oil 50% Food Grade | pending_review | Historical match confirmed |
| Pea Protein 25% Pharma Grade | Rapsöl 99.5% | auto_generated | Auto-mapped, validated |
| SIG-45-CWR-EI9N | Soy Isolate Grade A | pending_review | Confirmed by domain expert |
| Lactic Acid 98% | sunflower oil food grade | unverified | Confirmed by domain expert |
| MA-DE-700 | SIG-77-LFQ-EKT4 | unverified | Verified via product specs |
| vat standard nl 5% | VA-ST-U-10-638 | unverified | Verified via product specs |
| AS-AC-279 | casein standard | auto_generated | Confirmed by domain expert |
| SIG-99-CEZ-35MR | Stellar Partners Ltd. | unverified | Verified via product specs |
| SIG-71-PGT-OFPC | DE-840 | pending_review | Confirmed by domain expert |
| atlantic manufacturing Group | ME-TR-366 International | unverified | Cross-referenced with transactions |
| pinnacle logistics International | Vertex Ingredients | auto_generated | Cross-referenced with transactions |
| SIG-51-LVQ-VS8Q | rapeseed oil | pending_review | Confirmed by domain expert |
| vat reduced br 21% | Customs Duty IN 5% | pending_review | Auto-mapped, validated |
| Vat Reduced NL 25% | VA-ST-F-15-255 | pending_review | Verified via product specs |
| Atlantic Verarbeitung Holdings | BA-PA-973 | pending_review | Confirmed by domain expert |
| Ascorbic Acid Technical | PA-OI-ST-879 | auto_generated | Auto-mapped, validated |
| withholding nl 7% | EX-I-0-103 | pending_review | Auto-mapped, validated |
| Calcium Carbonate 98% Pharmazeutisch rein | SIG-82-IYU-XY3P | auto_generated | Cross-referenced with transactions |
| CO-MA-245 | Meridian Logistik | unverified | Confirmed by domain expert |
| NO-IN-670 International | Central Manufacturing Holdings | pending_review | Confirmed by domain expert |
| Lactic Acid 50% Grade A | Pea Protein 70% Technische Qualität | auto_generated | Auto-mapped, validated |
| horizon partners Ltd. | Premier Logistik KG | auto_generated | Cross-referenced with transactions |
| Potassium Sorbate Grade A | pea protein | unverified | Cross-referenced with transactions |
| Natriumbenzoat | Calcium Carbonate 98% | auto_generated | Auto-mapped, validated |
| Atlas Ingredients Ltd. | Core Chemicals | unverified | Confirmed by domain expert |
| Quantum Versorgung GmbH | pacific sourcing | unverified | Auto-mapped, validated |
| potassium sorbate tech grade | Maltodextrin DE5 | pending_review | Cross-referenced with transactions |
| SIG-81-SBE-HL1C | sunflower oil 70% | pending_review | Historical match confirmed |
| SIG-93-ZCF-6HM3 | Zitronensäure Qualitätsstufe I | auto_generated | Verified via product specs |
| Prime Logistics | quantum logistics | auto_generated | Historical match confirmed |
| Premier Supply Co. | Core Logistik | unverified | Historical match confirmed |
| SIG-29-BJH-NXI0 | Ascorbic Acid | auto_generated | Historical match confirmed |
| fructose | Palm Oil Pharma Grade | auto_generated | Confirmed by domain expert |
| AT-PA-589 | Stratos Trading Holdings | auto_generated | Historical match confirmed |
| SIG-43-GRJ-P3HT | SO-IS-99.5-338 | pending_review | Verified via product specs |
| EX-N-15-178 | Vat Standardqualität FR 25% | pending_review | Verified via product specs |
| Lactic Acid | RE-ST-FO-GR-727 | auto_generated | Confirmed by domain expert |
| Vat Standard US 19% | SIG-47-MRM-FIIH | auto_generated | Confirmed by domain expert |
| SIG-18-CIG-ZUL8 Holdings | Pinnacle Rohstoffe NV | pending_review | Cross-referenced with transactions |
| SIG-76-IIX-V2Y9 | Sonnenblumenöl 70% | unverified | Verified via product specs |
| palm oil standard | SO-BE-PH-GR-831 | auto_generated | Verified via product specs |
| Prism Versorgung GmbH | prism logistics | unverified | Historical match confirmed |
| zenith trading GmbH | Baltic Trading BV | auto_generated | Auto-mapped, validated |
| RE-ST-TE-614 | Coconut Oil | unverified | Confirmed by domain expert |
| calcium carbonate 25% pharma grade | Calcium Carbonate 98% | auto_generated | Historical match confirmed |
| Fructose | PO-SO-GR-A-715 | auto_generated | Historical match confirmed |
| Fructose 70% | dextrin standard | unverified | Confirmed by domain expert |
| NO-LO-114 Ltd. | Prism Ingredients NV | pending_review | Auto-mapped, validated |
| Isoglucose | FR-50-ST-938 | auto_generated | Historical match confirmed |
| isoglucose 70% | Lactic Acid Lebensmittelrein | pending_review | Historical match confirmed |
| PI-SO-251 | Stellar Sourcing | pending_review | Cross-referenced with transactions |
| SIG-92-ZTO-VZGU | Palm Oil 70% Premium | pending_review | Cross-referenced with transactions |
| Prism Sourcing | SIG-33-YPL-RQCS | auto_generated | Historical match confirmed |
| Natriumchlorid 98% | palm oil 99.5% | pending_review | Auto-mapped, validated |
| Prime Materials | Prism Versorgung GmbH | unverified | Confirmed by domain expert |
| horizon logistics PLC | Global Verarbeitung SAS | pending_review | Confirmed by domain expert |
| Natriumbenzoat 25% | soy isolate food grade | pending_review | Auto-mapped, validated |
| quantum supply | SIG-94-DAC-86F9 | pending_review | Auto-mapped, validated |
| potassium sorbate 98% | Wheat Gluten Grade B | auto_generated | Confirmed by domain expert |
| glucose syrup | SIG-74-HUK-JA04 | unverified | Auto-mapped, validated |
| PA-OI-50-273 | Palm Oil Food Grade | unverified | Confirmed by domain expert |
| GL-SO-534 Holdings | Continental Commodities GmbH | pending_review | Cross-referenced with transactions |
| Vat Reduced GB 20% | excise in 7% | pending_review | Verified via product specs |
| WH-GL-GR-A-924 | SIG-20-UMV-LJM6 | unverified | Confirmed by domain expert |
| Global Logistics | stellar supply | auto_generated | Confirmed by domain expert |
| SIG-23-NOR-OPI3 | AP-CH-166 International | auto_generated | Auto-mapped, validated |
| Baltic Sourcing | SIG-56-YYA-I8SV | unverified | Cross-referenced with transactions |
| CO-PA-308 | Stellar Handel | auto_generated | Verified via product specs |
| SIG-64-IEU-FRGN | resistant starch tech grade | unverified | Historical match confirmed |
| SIG-10-NNQ-6CGO | Excise FR 19% | unverified | Historical match confirmed |
| Lactic Acid | Ascorbic Acid Standardqualität | auto_generated | Confirmed by domain expert |
| citric acid 99.5% | Lactic Acid 99.5% | pending_review | Verified via product specs |
| Fructose 70% | Resistente Stärke Lebensmittelrein | auto_generated | Confirmed by domain expert |
| Sonnenblumenöl Pharmazeutisch rein | PA-OI-399 | auto_generated | Historical match confirmed |
| Potassium Sorbate 98% Grade B | SIG-36-JLA-CSEN | unverified | Auto-mapped, validated |
| Pinnacle Enterprise AG | atlantic supply | auto_generated | Verified via product specs |
| CE-PR-134 | premier partners | auto_generated | Verified via product specs |
| Rapsöl 50% Pharmazeutisch rein | Isoglucose 98% | pending_review | Auto-mapped, validated |
| PO-SO-50-GR-B-154 | Lactic Acid | auto_generated | Confirmed by domain expert |
| vertex materials | AT-SU-CO-364 | unverified | Verified via product specs |
| glucose syrup 99.5% food grade | SIG-48-ZZX-UQIO | unverified | Auto-mapped, validated |
| AT-CH-905 Holdings | Atlas Logistik International | unverified | Confirmed by domain expert |
| vat standard de 25% | VA-ST-B-25-250 | unverified | Auto-mapped, validated |
| Vanguard Logistik International | AP-SO-704 | auto_generated | Auto-mapped, validated |
| SIG-77-WZV-TKWL | Premier Logistics | unverified | Confirmed by domain expert |
| Wheat Gluten Grade A | RA-OI-745 | unverified | Cross-referenced with transactions |
| nexus distribution Corp. | Premier Rohstoffe Group | auto_generated | Auto-mapped, validated |
| Vat Reduced GB 19% | vat reduced us 5% | pending_review | Verified via product specs |
| customs duty nl 21% | CU-DU-F-19-568 | unverified | Auto-mapped, validated |
| SIG-97-UWA-JWLN | Apex Versorgung GmbH | pending_review | Historical match confirmed |
| Pinnacle Industries SAS | ST-CO-827 Holdings | unverified | Cross-referenced with transactions |
| Customs Duty IN 20% | WI-F-10-935 | auto_generated | Cross-referenced with transactions |
| SIG-60-RUC-CU6A | Elite Chemicals AG | pending_review | Historical match confirmed |
| Sodium Benzoate 50% | Kasein 70% Technische Qualität | pending_review | Auto-mapped, validated |
| Atlantic Processing International | Global Industrien | pending_review | Historical match confirmed |
| pea protein standard | SIG-47-GAT-ET7B | unverified | Historical match confirmed |
| lactic acid food grade | Calcium Carbonate Grade B | unverified | Confirmed by domain expert |
| ME-SO-760 GmbH | Apex Rohstoffe Holdings | pending_review | Auto-mapped, validated |
| Apex Handel International | PI-IN-244 | pending_review | Historical match confirmed |
| Coconut Oil 25% Technical | Natriumbenzoat Qualitätsstufe I | auto_generated | Historical match confirmed |
| SIG-44-HTV-P84J | Palm Oil Food Grade | auto_generated | Historical match confirmed |
| PE-PR-25-185 | SIG-20-OVW-HRUP | pending_review | Historical match confirmed |
| rapeseed oil tech grade | CY-GR-A-208 | unverified | Verified via product specs |
| Sodium Benzoate 25% Standard | Sorbinsäure Premiumqualität | auto_generated | Historical match confirmed |
| Glucose Syrup 25% | CA-580 | auto_generated | Verified via product specs |
| Natriumchlorid Technische Qualität | Soy Isolate | pending_review | Auto-mapped, validated |
| SO-BE-824 | wheat gluten | auto_generated | Auto-mapped, validated |
| Zitronensäure 70% | Coconut Oil 25% Standard | unverified | Auto-mapped, validated |
| PI-PR-193 | Catalyst Enterprise International | unverified | Auto-mapped, validated |
| Atlantic Partners SARL | Catalyst Enterprise International | unverified | Auto-mapped, validated |
| Premier Solutions Inc. | SIG-35-FKH-6ZOM KG | pending_review | Confirmed by domain expert |
| sorbic acid | Potassium Sorbate 98% | auto_generated | Confirmed by domain expert |
| SIG-63-NTB-209C | Nexus Logistik | pending_review | Historical match confirmed |
| Potassium Sorbate | SO-AC-ST-392 | unverified | Historical match confirmed |
| prime solutions | SIG-40-DEO-UM9B International | unverified | Auto-mapped, validated |
| PE-PR-929 | soy isolate 50% | auto_generated | Verified via product specs |
| Resistant Starch Technical | SIG-55-CTS-U5X0 | auto_generated | Cross-referenced with transactions |
| Stellar Logistics | Nexus Sourcing | pending_review | Confirmed by domain expert |
| PR-IN-409 LLC | Core Werkstoffe | auto_generated | Confirmed by domain expert |
| CO-PA-491 BV | SIG-37-AVX-CY7Q SAS | auto_generated | Confirmed by domain expert |
| Calcium Carbonate 50% Food Grade | FR-99.5-GR-A-438 | pending_review | Confirmed by domain expert |
| SIG-20-IMA-GJKF | Customs Duty NL 5% | auto_generated | Cross-referenced with transactions |
| SIG-25-ABB-2SBA | Lactic Acid | auto_generated | Historical match confirmed |
| SIG-86-ZYB-L8NP BV | premier industries Holdings | auto_generated | Verified via product specs |
| Kaliumsorbat 50% Technische Qualität | Lactic Acid Technical | pending_review | Verified via product specs |
| Dextrose 25% | Resistente Stärke Standardqualität | unverified | Historical match confirmed |
| pea protein standard | Pea Protein | pending_review | Confirmed by domain expert |
| casein 50% premium | Kasein | pending_review | Auto-mapped, validated |
| LA-AC-25-819 | Citric Acid | auto_generated | Historical match confirmed |
| Vanguard Ingredients | SIG-78-QFN-H3BV | pending_review | Auto-mapped, validated |
| calcium carbonate | Weizenklebereiweiß | unverified | Historical match confirmed |
| Withholding NL 10% | EX-N-15-468 | auto_generated | Verified via product specs |
| Sodium Benzoate 99.5% Technical | LA-AC-FO-GR-687 | auto_generated | Confirmed by domain expert |
| AT-MA-510 | Prime Logistik | unverified | Confirmed by domain expert |
| SIG-82-VDF-0XQT | Isoglucose | pending_review | Cross-referenced with transactions |
| Baltic Sourcing | EL-MA-832 | pending_review | Verified via product specs |
| Glukosesirup Syrup | SIG-67-VXU-FPWB | pending_review | Verified via product specs |
| Sorbinsäure | casein 98% standard | unverified | Historical match confirmed |
| LA-AC-471 | Sonnenblumenöl Standardqualität | unverified | Auto-mapped, validated |
| apex logistics | SIG-76-ESC-PNV7 | unverified | Cross-referenced with transactions |
| NE-LO-300 | horizon logistics | unverified | Cross-referenced with transactions |
| ascorbic acid | Kasein | auto_generated | Verified via product specs |
| Vertex Chemicals Holdings | pacific industries Ltd. | unverified | Cross-referenced with transactions |
| SIG-51-MVX-XKUB | Customs Duty DE 5% | unverified | Verified via product specs |
| Calcium Carbonate 98% Standardqualität | AS-AC-98-PR-217 | auto_generated | Cross-referenced with transactions |
| GL-LO-494 | SIG-23-PGX-VBNK | unverified | Auto-mapped, validated |
| dextrose 99.5% standard | Resistente Stärke Pharmazeutisch rein | auto_generated | Confirmed by domain expert |
| Glucose Syrup 98% Standard | Isoglucose Premiumqualität | pending_review | Cross-referenced with transactions |
| SO-IS-975 | Wheat Gluten 25% Standard | unverified | Auto-mapped, validated |
| Glucose Syrup 98% | SIG-12-BIH-AKGD | pending_review | Confirmed by domain expert |
| apex materials Group | GL-CO-894 | unverified | Cross-referenced with transactions |
| SIG-68-LYO-7YQ5 | Catalyst Logistik | unverified | Confirmed by domain expert |
| SIG-58-HNG-1XJ7 | GL-SY-70-549 | pending_review | Auto-mapped, validated |
| SIG-54-BLS-33OX | Baltic Werkstoffe | pending_review | Auto-mapped, validated |
| VA-RE-N-20-326 | Vat Standard US 5% | unverified | Cross-referenced with transactions |
| SIG-43-XDN-7VEU | EX-B-21-936 | auto_generated | Historical match confirmed |
| EX-F-25-579 | Withholding NL 20% | pending_review | Confirmed by domain expert |
| PR-LO-420 | SIG-36-PCG-IRVO | unverified | Confirmed by domain expert |
| SIG-48-GDK-Y8XN | CI-AC-ST-836 | unverified | Historical match confirmed |
| Stratos Chemicals | Vanguard Distribution | pending_review | Confirmed by domain expert |
| SIG-57-QDA-RQ8R | Ascorbic Acid | pending_review | Auto-mapped, validated |
| CY-TE-117 | lactic acid food grade | auto_generated | Verified via product specs |
| SIG-60-OBI-GVJP | Pacific Supply Co. | auto_generated | Confirmed by domain expert |
| Quantum Supply Co. | QU-SU-CO-774 | auto_generated | Cross-referenced with transactions |
| Vat Reduced BR 10% | vat standard de 7% | auto_generated | Confirmed by domain expert |
| VA-LO-948 | vertex commodities KG | auto_generated | Confirmed by domain expert |
| SIG-45-ZHK-QWIG | Natriumchlorid Lebensmittelrein | unverified | Confirmed by domain expert |
| CA-ST-375 | SIG-71-VGV-8K52 | unverified | Cross-referenced with transactions |
| Wheat Gluten 25% Standard | sorbic acid premium | pending_review | Historical match confirmed |
| Cyclodextrin | rapeseed oil 25% food grade | pending_review | Historical match confirmed |
| Stratos Chemicals | SIG-77-RVO-CE8D Inc. | auto_generated | Historical match confirmed |
| wheat gluten standard | Isoglucose Qualitätsstufe II | unverified | Cross-referenced with transactions |
| fructose premium | FR-TE-414 | pending_review | Confirmed by domain expert |
| VA-SU-CO-459 | Premier Logistik | auto_generated | Confirmed by domain expert |
| palm oil 50% | Soy Isolate | pending_review | Confirmed by domain expert |

#### 4.3.3 Excluded Mappings

Provisional mappings pending business validation:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-7345-E | Invalid Entry 918 | Duplicate detected |
| NOISE-1237-D | Invalid Entry 140 | Data quality insufficient |
| NOISE-3057-G | Invalid Entry 170 | Pending validation |
| NOISE-9956-F | Invalid Entry 377 | Out of scope per business decision |
| NOISE-8485-F | Invalid Entry 359 | Data quality insufficient |
| NOISE-9619-F | Invalid Entry 344 | Superseded by newer mapping |
| NOISE-9469-G | Invalid Entry 211 | Data quality insufficient |
| NOISE-4581-C | Invalid Entry 972 | Data quality insufficient |
| NOISE-1829-D | Invalid Entry 419 | Data quality insufficient |
| NOISE-6084-F | Invalid Entry 156 | Data quality insufficient |
| NOISE-1287-F | Invalid Entry 886 | Data quality insufficient |
| NOISE-9224-D | Invalid Entry 809 | Data quality insufficient |
| NOISE-6491-A | Invalid Entry 269 | Superseded by newer mapping |
| NOISE-6355-B | Invalid Entry 187 | Superseded by newer mapping |
| NOISE-3061-H | Invalid Entry 991 | Pending validation |
| NOISE-9817-F | Invalid Entry 481 | Data quality insufficient |
| NOISE-1757-A | Invalid Entry 252 | Pending validation |
| NOISE-9210-B | Invalid Entry 987 | Out of scope per business decision |
| NOISE-2438-A | Invalid Entry 245 | Out of scope per business decision |
| NOISE-1810-A | Invalid Entry 254 | Out of scope per business decision |
| NOISE-8144-F | Invalid Entry 478 | Pending validation |
| NOISE-3712-C | Invalid Entry 109 | Superseded by newer mapping |
| NOISE-2238-C | Invalid Entry 296 | Duplicate detected |
| NOISE-4004-C | Invalid Entry 708 | Duplicate detected |
| NOISE-5002-E | Invalid Entry 311 | Data quality insufficient |
| NOISE-2592-G | Invalid Entry 762 | Pending validation |
| NOISE-7332-D | Invalid Entry 314 | Superseded by newer mapping |
| NOISE-6977-A | Invalid Entry 560 | Superseded by newer mapping |
| NOISE-9362-A | Invalid Entry 201 | Out of scope per business decision |
| NOISE-9761-B | Invalid Entry 942 | Out of scope per business decision |
| NOISE-8923-H | Invalid Entry 195 | Pending validation |
| NOISE-3415-F | Invalid Entry 395 | Data quality insufficient |
| NOISE-8819-B | Invalid Entry 623 | Superseded by newer mapping |
| NOISE-3968-H | Invalid Entry 883 | Superseded by newer mapping |
| NOISE-7997-F | Invalid Entry 597 | Out of scope per business decision |
| NOISE-7939-F | Invalid Entry 808 | Pending validation |
| NOISE-3296-D | Invalid Entry 137 | Out of scope per business decision |
| NOISE-4012-C | Invalid Entry 756 | Out of scope per business decision |
| NOISE-6410-C | Invalid Entry 513 | Superseded by newer mapping |
| NOISE-2849-A | Invalid Entry 116 | Superseded by newer mapping |
| NOISE-2831-F | Invalid Entry 577 | Out of scope per business decision |
| NOISE-3336-F | Invalid Entry 295 | Superseded by newer mapping |
| NOISE-6890-E | Invalid Entry 353 | Out of scope per business decision |
| NOISE-9307-H | Invalid Entry 168 | Duplicate detected |
| NOISE-3323-H | Invalid Entry 169 | Superseded by newer mapping |
| NOISE-6616-F | Invalid Entry 295 | Pending validation |
| NOISE-1471-E | Invalid Entry 844 | Out of scope per business decision |
| NOISE-8515-A | Invalid Entry 513 | Duplicate detected |
| NOISE-4221-G | Invalid Entry 585 | Data quality insufficient |
| NOISE-9230-A | Invalid Entry 133 | Duplicate detected |
| NOISE-1884-E | Invalid Entry 620 | Superseded by newer mapping |
| NOISE-7119-D | Invalid Entry 819 | Data quality insufficient |
| NOISE-6388-F | Invalid Entry 380 | Pending validation |
| NOISE-7448-A | Invalid Entry 306 | Out of scope per business decision |
| NOISE-3400-C | Invalid Entry 106 | Pending validation |
| NOISE-6028-A | Invalid Entry 775 | Data quality insufficient |
| NOISE-6059-D | Invalid Entry 591 | Duplicate detected |
| NOISE-5522-F | Invalid Entry 902 | Data quality insufficient |
| NOISE-2197-G | Invalid Entry 845 | Out of scope per business decision |
| NOISE-1022-G | Invalid Entry 688 | Duplicate detected |
| NOISE-8921-C | Invalid Entry 108 | Duplicate detected |
| NOISE-4373-E | Invalid Entry 578 | Duplicate detected |
| NOISE-7391-B | Invalid Entry 563 | Out of scope per business decision |
| NOISE-5065-D | Invalid Entry 766 | Duplicate detected |
| NOISE-3639-B | Invalid Entry 787 | Superseded by newer mapping |
| NOISE-7728-B | Invalid Entry 169 | Superseded by newer mapping |
| NOISE-6003-C | Invalid Entry 604 | Pending validation |
| NOISE-6243-E | Invalid Entry 366 | Out of scope per business decision |
| NOISE-6713-C | Invalid Entry 906 | Pending validation |
| NOISE-7908-E | Invalid Entry 302 | Superseded by newer mapping |
| NOISE-8227-F | Invalid Entry 576 | Pending validation |
| NOISE-7685-B | Invalid Entry 540 | Superseded by newer mapping |
| NOISE-6278-G | Invalid Entry 681 | Superseded by newer mapping |
| NOISE-7540-D | Invalid Entry 390 | Superseded by newer mapping |
| NOISE-2279-E | Invalid Entry 128 | Duplicate detected |
| NOISE-9518-G | Invalid Entry 459 | Data quality insufficient |
| NOISE-8373-B | Invalid Entry 442 | Data quality insufficient |
| NOISE-9760-H | Invalid Entry 263 | Pending validation |
| NOISE-4787-A | Invalid Entry 749 | Superseded by newer mapping |
| NOISE-3869-D | Invalid Entry 162 | Duplicate detected |
| NOISE-7117-C | Invalid Entry 692 | Out of scope per business decision |
| NOISE-7348-E | Invalid Entry 306 | Superseded by newer mapping |
| NOISE-2206-A | Invalid Entry 507 | Pending validation |
| NOISE-6365-H | Invalid Entry 520 | Out of scope per business decision |
| NOISE-4321-H | Invalid Entry 929 | Superseded by newer mapping |
| NOISE-9733-G | Invalid Entry 654 | Out of scope per business decision |
| NOISE-4147-C | Invalid Entry 728 | Data quality insufficient |
| NOISE-6069-E | Invalid Entry 297 | Superseded by newer mapping |
| NOISE-4940-C | Invalid Entry 709 | Superseded by newer mapping |
| NOISE-8888-H | Invalid Entry 991 | Duplicate detected |
| NOISE-5557-D | Invalid Entry 996 | Duplicate detected |
| NOISE-1045-C | Invalid Entry 571 | Superseded by newer mapping |
| NOISE-4653-C | Invalid Entry 420 | Out of scope per business decision |
| NOISE-5350-E | Invalid Entry 685 | Superseded by newer mapping |
| NOISE-5484-G | Invalid Entry 816 | Duplicate detected |
| NOISE-2053-H | Invalid Entry 188 | Duplicate detected |
| NOISE-1580-F | Invalid Entry 513 | Superseded by newer mapping |
| NOISE-5154-A | Invalid Entry 323 | Pending validation |
| NOISE-8076-E | Invalid Entry 346 | Duplicate detected |
| NOISE-2760-B | Invalid Entry 208 | Superseded by newer mapping |
| NOISE-3594-F | Invalid Entry 563 | Out of scope per business decision |
| NOISE-4464-B | Invalid Entry 858 | Data quality insufficient |
| NOISE-5222-E | Invalid Entry 916 | Superseded by newer mapping |
| NOISE-6989-D | Invalid Entry 233 | Duplicate detected |
| NOISE-8403-H | Invalid Entry 740 | Duplicate detected |
| NOISE-4371-A | Invalid Entry 939 | Pending validation |
| NOISE-1385-E | Invalid Entry 737 | Duplicate detected |
| NOISE-3537-A | Invalid Entry 754 | Out of scope per business decision |
| NOISE-5588-B | Invalid Entry 806 | Superseded by newer mapping |
| NOISE-8933-G | Invalid Entry 440 | Superseded by newer mapping |
| NOISE-1420-A | Invalid Entry 850 | Out of scope per business decision |
| NOISE-9271-E | Invalid Entry 789 | Pending validation |
| NOISE-1863-E | Invalid Entry 152 | Superseded by newer mapping |
| NOISE-5755-B | Invalid Entry 943 | Out of scope per business decision |
| NOISE-7047-D | Invalid Entry 397 | Out of scope per business decision |
| NOISE-4372-F | Invalid Entry 460 | Pending validation |
| NOISE-5557-E | Invalid Entry 633 | Superseded by newer mapping |
| NOISE-4646-F | Invalid Entry 870 | Superseded by newer mapping |
| NOISE-1018-C | Invalid Entry 957 | Superseded by newer mapping |
| NOISE-4758-F | Invalid Entry 944 | Superseded by newer mapping |
| NOISE-6433-A | Invalid Entry 749 | Duplicate detected |
| NOISE-7120-D | Invalid Entry 376 | Out of scope per business decision |
| NOISE-2684-B | Invalid Entry 464 | Pending validation |
| NOISE-8574-E | Invalid Entry 108 | Out of scope per business decision |
| NOISE-3027-G | Invalid Entry 228 | Data quality insufficient |
| NOISE-7770-G | Invalid Entry 949 | Superseded by newer mapping |
| NOISE-6942-G | Invalid Entry 141 | Duplicate detected |
| NOISE-1769-D | Invalid Entry 899 | Data quality insufficient |
| NOISE-9203-B | Invalid Entry 113 | Data quality insufficient |
| NOISE-7927-F | Invalid Entry 768 | Superseded by newer mapping |
| NOISE-9710-C | Invalid Entry 230 | Data quality insufficient |
| NOISE-5096-D | Invalid Entry 565 | Pending validation |
| NOISE-8738-D | Invalid Entry 780 | Pending validation |
| NOISE-3411-B | Invalid Entry 819 | Out of scope per business decision |
| NOISE-3049-C | Invalid Entry 323 | Data quality insufficient |
| NOISE-6478-B | Invalid Entry 746 | Pending validation |
| NOISE-9452-E | Invalid Entry 257 | Out of scope per business decision |
| NOISE-1304-D | Invalid Entry 314 | Duplicate detected |
| NOISE-4397-E | Invalid Entry 421 | Superseded by newer mapping |
| NOISE-5510-E | Invalid Entry 862 | Out of scope per business decision |
| NOISE-4725-B | Invalid Entry 267 | Data quality insufficient |
| NOISE-7109-E | Invalid Entry 342 | Out of scope per business decision |
| NOISE-5479-G | Invalid Entry 304 | Superseded by newer mapping |
| NOISE-8829-E | Invalid Entry 510 | Superseded by newer mapping |
| NOISE-5144-C | Invalid Entry 913 | Superseded by newer mapping |
| NOISE-5324-B | Invalid Entry 244 | Data quality insufficient |
| NOISE-1550-F | Invalid Entry 274 | Pending validation |
| NOISE-4482-A | Invalid Entry 287 | Duplicate detected |
| NOISE-2270-C | Invalid Entry 601 | Out of scope per business decision |
| NOISE-2156-E | Invalid Entry 957 | Data quality insufficient |
| NOISE-1177-C | Invalid Entry 576 | Duplicate detected |
| NOISE-3883-H | Invalid Entry 243 | Pending validation |
| NOISE-1482-H | Invalid Entry 270 | Superseded by newer mapping |
| NOISE-6468-C | Invalid Entry 570 | Duplicate detected |
| NOISE-3202-F | Invalid Entry 835 | Pending validation |
| NOISE-6234-F | Invalid Entry 407 | Duplicate detected |
| NOISE-2903-D | Invalid Entry 480 | Data quality insufficient |
| NOISE-2119-A | Invalid Entry 297 | Duplicate detected |
| NOISE-7269-H | Invalid Entry 406 | Superseded by newer mapping |
| NOISE-3034-F | Invalid Entry 726 | Pending validation |
| NOISE-2699-G | Invalid Entry 441 | Out of scope per business decision |
| NOISE-1176-B | Invalid Entry 987 | Duplicate detected |
| NOISE-3133-E | Invalid Entry 380 | Pending validation |
| NOISE-9412-D | Invalid Entry 578 | Out of scope per business decision |
| NOISE-7248-D | Invalid Entry 544 | Data quality insufficient |
| NOISE-2077-H | Invalid Entry 939 | Pending validation |
| NOISE-1052-A | Invalid Entry 514 | Duplicate detected |
| NOISE-3369-F | Invalid Entry 605 | Pending validation |
| NOISE-9141-F | Invalid Entry 589 | Data quality insufficient |
| NOISE-1107-F | Invalid Entry 634 | Out of scope per business decision |
| NOISE-4332-C | Invalid Entry 415 | Pending validation |
| NOISE-3408-G | Invalid Entry 744 | Data quality insufficient |
| NOISE-3684-D | Invalid Entry 370 | Superseded by newer mapping |
| NOISE-3009-C | Invalid Entry 162 | Superseded by newer mapping |
| NOISE-4144-C | Invalid Entry 845 | Pending validation |
| NOISE-7499-E | Invalid Entry 667 | Data quality insufficient |
| NOISE-3153-D | Invalid Entry 966 | Out of scope per business decision |
| NOISE-3483-G | Invalid Entry 263 | Duplicate detected |
| NOISE-5473-B | Invalid Entry 918 | Superseded by newer mapping |
| NOISE-5284-D | Invalid Entry 236 | Superseded by newer mapping |
| NOISE-2481-F | Invalid Entry 325 | Duplicate detected |
| NOISE-1127-D | Invalid Entry 400 | Duplicate detected |
| NOISE-2899-D | Invalid Entry 754 | Superseded by newer mapping |
| NOISE-6839-C | Invalid Entry 739 | Duplicate detected |
| NOISE-5031-C | Invalid Entry 303 | Data quality insufficient |
| NOISE-8353-E | Invalid Entry 888 | Data quality insufficient |
| NOISE-8982-A | Invalid Entry 600 | Data quality insufficient |
| NOISE-6101-E | Invalid Entry 271 | Data quality insufficient |
| NOISE-5792-G | Invalid Entry 610 | Superseded by newer mapping |
| NOISE-1138-D | Invalid Entry 674 | Duplicate detected |
| NOISE-7395-H | Invalid Entry 603 | Duplicate detected |
| NOISE-2689-A | Invalid Entry 830 | Superseded by newer mapping |
| NOISE-7019-D | Invalid Entry 793 | Pending validation |
| NOISE-8206-D | Invalid Entry 947 | Duplicate detected |
| NOISE-8602-B | Invalid Entry 285 | Superseded by newer mapping |
| NOISE-2933-G | Invalid Entry 339 | Data quality insufficient |
| NOISE-4392-F | Invalid Entry 332 | Duplicate detected |
| NOISE-8768-B | Invalid Entry 576 | Pending validation |
| NOISE-2707-H | Invalid Entry 221 | Data quality insufficient |
| NOISE-1400-A | Invalid Entry 638 | Duplicate detected |
| NOISE-4032-A | Invalid Entry 674 | Superseded by newer mapping |
| NOISE-5531-A | Invalid Entry 954 | Pending validation |
| NOISE-8353-F | Invalid Entry 497 | Duplicate detected |
| NOISE-2733-A | Invalid Entry 210 | Pending validation |
| NOISE-4986-B | Invalid Entry 825 | Pending validation |
| NOISE-1594-G | Invalid Entry 550 | Superseded by newer mapping |
| NOISE-2237-D | Invalid Entry 706 | Out of scope per business decision |
| NOISE-2063-D | Invalid Entry 953 | Pending validation |
| NOISE-3896-B | Invalid Entry 164 | Data quality insufficient |
| NOISE-6485-D | Invalid Entry 851 | Duplicate detected |
| NOISE-3222-C | Invalid Entry 106 | Duplicate detected |
| NOISE-3768-F | Invalid Entry 670 | Out of scope per business decision |
| NOISE-5049-B | Invalid Entry 576 | Out of scope per business decision |
| NOISE-8867-G | Invalid Entry 942 | Data quality insufficient |
| NOISE-7817-G | Invalid Entry 165 | Pending validation |
| NOISE-3763-H | Invalid Entry 436 | Pending validation |
| NOISE-3573-G | Invalid Entry 696 | Duplicate detected |
| NOISE-5319-B | Invalid Entry 427 | Out of scope per business decision |
| NOISE-8033-G | Invalid Entry 745 | Duplicate detected |
| NOISE-3695-D | Invalid Entry 807 | Duplicate detected |
| NOISE-8028-E | Invalid Entry 676 | Data quality insufficient |
| NOISE-9151-G | Invalid Entry 539 | Out of scope per business decision |
| NOISE-9219-H | Invalid Entry 952 | Pending validation |
| NOISE-9389-G | Invalid Entry 124 | Duplicate detected |
| NOISE-8313-F | Invalid Entry 405 | Duplicate detected |
| NOISE-2629-B | Invalid Entry 735 | Data quality insufficient |
| NOISE-5171-E | Invalid Entry 699 | Data quality insufficient |
| NOISE-8548-G | Invalid Entry 815 | Out of scope per business decision |
| NOISE-9482-D | Invalid Entry 744 | Superseded by newer mapping |
| NOISE-8834-D | Invalid Entry 259 | Superseded by newer mapping |
| NOISE-3619-C | Invalid Entry 478 | Superseded by newer mapping |
| NOISE-9877-G | Invalid Entry 165 | Out of scope per business decision |
| NOISE-6389-D | Invalid Entry 142 | Superseded by newer mapping |
| NOISE-9514-A | Invalid Entry 438 | Duplicate detected |
| NOISE-3577-E | Invalid Entry 560 | Duplicate detected |
| NOISE-9752-G | Invalid Entry 440 | Duplicate detected |
| NOISE-6454-E | Invalid Entry 518 | Data quality insufficient |
| NOISE-8087-F | Invalid Entry 705 | Data quality insufficient |
| NOISE-6340-G | Invalid Entry 717 | Pending validation |
| NOISE-1111-B | Invalid Entry 636 | Superseded by newer mapping |
| NOISE-3028-A | Invalid Entry 984 | Duplicate detected |
| NOISE-2661-F | Invalid Entry 656 | Data quality insufficient |
| NOISE-4619-B | Invalid Entry 339 | Out of scope per business decision |
| NOISE-1629-E | Invalid Entry 225 | Out of scope per business decision |
| NOISE-1726-C | Invalid Entry 156 | Out of scope per business decision |
| NOISE-7758-D | Invalid Entry 464 | Pending validation |
| NOISE-4804-G | Invalid Entry 599 | Superseded by newer mapping |
| NOISE-9780-C | Invalid Entry 518 | Superseded by newer mapping |
| NOISE-7573-A | Invalid Entry 444 | Out of scope per business decision |
| NOISE-2831-G | Invalid Entry 622 | Out of scope per business decision |
| NOISE-7402-C | Invalid Entry 998 | Duplicate detected |
| NOISE-4644-F | Invalid Entry 259 | Duplicate detected |
| NOISE-3452-F | Invalid Entry 121 | Out of scope per business decision |
| NOISE-1427-G | Invalid Entry 386 | Data quality insufficient |
| NOISE-9814-E | Invalid Entry 773 | Pending validation |
| NOISE-8808-C | Invalid Entry 523 | Data quality insufficient |
| NOISE-5743-E | Invalid Entry 520 | Data quality insufficient |
| NOISE-8045-G | Invalid Entry 794 | Superseded by newer mapping |
| NOISE-1628-B | Invalid Entry 705 | Superseded by newer mapping |
| NOISE-5173-A | Invalid Entry 571 | Pending validation |
| NOISE-4801-B | Invalid Entry 925 | Superseded by newer mapping |
| NOISE-3208-D | Invalid Entry 649 | Pending validation |
| NOISE-2962-G | Invalid Entry 155 | Pending validation |
| NOISE-9019-C | Invalid Entry 569 | Duplicate detected |
| NOISE-3012-H | Invalid Entry 468 | Superseded by newer mapping |
| NOISE-7115-H | Invalid Entry 696 | Superseded by newer mapping |
| NOISE-6191-B | Invalid Entry 567 | Out of scope per business decision |
| NOISE-6093-G | Invalid Entry 843 | Pending validation |
| NOISE-4913-D | Invalid Entry 659 | Data quality insufficient |
| NOISE-9183-D | Invalid Entry 660 | Duplicate detected |
| NOISE-7139-H | Invalid Entry 954 | Superseded by newer mapping |
| NOISE-9061-F | Invalid Entry 315 | Pending validation |
| NOISE-6665-B | Invalid Entry 717 | Pending validation |
| NOISE-2078-H | Invalid Entry 958 | Data quality insufficient |
| NOISE-4537-H | Invalid Entry 320 | Superseded by newer mapping |
| NOISE-8859-A | Invalid Entry 785 | Pending validation |
| NOISE-7324-A | Invalid Entry 262 | Pending validation |
| NOISE-5214-B | Invalid Entry 242 | Pending validation |
| NOISE-8205-A | Invalid Entry 465 | Data quality insufficient |
| NOISE-6160-F | Invalid Entry 839 | Duplicate detected |
| NOISE-1592-E | Invalid Entry 678 | Data quality insufficient |
| NOISE-3891-B | Invalid Entry 117 | Superseded by newer mapping |
| NOISE-6842-C | Invalid Entry 821 | Out of scope per business decision |
| NOISE-2608-C | Invalid Entry 725 | Out of scope per business decision |
| NOISE-4884-E | Invalid Entry 622 | Superseded by newer mapping |
| NOISE-3225-D | Invalid Entry 238 | Pending validation |
| NOISE-9140-D | Invalid Entry 288 | Data quality insufficient |
| NOISE-5666-F | Invalid Entry 497 | Data quality insufficient |
| NOISE-3979-B | Invalid Entry 746 | Superseded by newer mapping |
| NOISE-6339-E | Invalid Entry 770 | Superseded by newer mapping |
| NOISE-5740-B | Invalid Entry 338 | Duplicate detected |
| NOISE-2717-E | Invalid Entry 225 | Pending validation |
| NOISE-3321-E | Invalid Entry 831 | Out of scope per business decision |
| NOISE-5368-D | Invalid Entry 366 | Out of scope per business decision |
| NOISE-1743-G | Invalid Entry 815 | Out of scope per business decision |
| NOISE-5064-B | Invalid Entry 774 | Superseded by newer mapping |
| NOISE-7542-C | Invalid Entry 559 | Out of scope per business decision |
| NOISE-6311-F | Invalid Entry 109 | Data quality insufficient |
| NOISE-3954-D | Invalid Entry 170 | Data quality insufficient |
| NOISE-5369-A | Invalid Entry 992 | Out of scope per business decision |
| NOISE-2032-D | Invalid Entry 885 | Duplicate detected |
| NOISE-2837-E | Invalid Entry 504 | Data quality insufficient |
| NOISE-3506-E | Invalid Entry 186 | Pending validation |
| NOISE-9885-H | Invalid Entry 141 | Out of scope per business decision |
| NOISE-7809-F | Invalid Entry 859 | Out of scope per business decision |
| NOISE-8805-A | Invalid Entry 732 | Data quality insufficient |
| NOISE-7390-B | Invalid Entry 856 | Superseded by newer mapping |
| NOISE-1431-A | Invalid Entry 832 | Pending validation |
| NOISE-2278-E | Invalid Entry 921 | Superseded by newer mapping |
| NOISE-5894-D | Invalid Entry 740 | Data quality insufficient |
| NOISE-3280-G | Invalid Entry 440 | Superseded by newer mapping |
| NOISE-5294-A | Invalid Entry 185 | Out of scope per business decision |
| NOISE-1541-H | Invalid Entry 309 | Duplicate detected |
| NOISE-5316-D | Invalid Entry 224 | Superseded by newer mapping |
| NOISE-5751-B | Invalid Entry 480 | Out of scope per business decision |
| NOISE-2026-E | Invalid Entry 299 | Pending validation |
| NOISE-9994-E | Invalid Entry 498 | Superseded by newer mapping |
| NOISE-3615-A | Invalid Entry 111 | Out of scope per business decision |
| NOISE-5506-A | Invalid Entry 122 | Duplicate detected |
| NOISE-2455-F | Invalid Entry 797 | Out of scope per business decision |
| NOISE-2444-C | Invalid Entry 631 | Data quality insufficient |
| NOISE-1912-D | Invalid Entry 284 | Data quality insufficient |
| NOISE-5044-D | Invalid Entry 676 | Data quality insufficient |
| NOISE-7228-B | Invalid Entry 575 | Pending validation |
| NOISE-8249-A | Invalid Entry 824 | Data quality insufficient |

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
