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
| Total entities assessed | 1473 | Completed |
| Successfully mapped | 1033 | Verified |
| Excluded from scope | 309 | Documented |
| Manual review required | 5 | In Progress |

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
| Apex Chemicals Corp. | Nexus Processing International | auto_generated | Cross-referenced with transactions |
| CO-OI-98-890 | Calcium Carbonate Standardqualität | pending_review | Verified via product specs |
| SIG-70-MMO-95UC | horizon logistics International | auto_generated | Confirmed by domain expert |
| SO-IS-25-323 | sorbic acid 50% standard | pending_review | Auto-mapped, validated |
| rapeseed oil tech grade | Weizenklebereiweiß | unverified | Verified via product specs |
| Nordic Distribution | QU-PA-830 Group | unverified | Auto-mapped, validated |
| Excise IN 25% | CU-DU-B-15-379 | pending_review | Auto-mapped, validated |
| PO-SO-50-GR-B-154 | Potassium Sorbate Standard | unverified | Confirmed by domain expert |
| Pinnacle Werkstoffe SARL | VE-CH-841 Group | unverified | Confirmed by domain expert |
| citric acid 99.5% | SIG-85-ACE-0XNG | unverified | Verified via product specs |
| SIG-40-CXK-QT2E Group | QU-DI-467 Holdings | pending_review | Auto-mapped, validated |
| PE-PR-PR-564 | Ascorbic Acid Premiumqualität | pending_review | Cross-referenced with transactions |
| Zitronensäure Technische Qualität | DE-TE-380 | auto_generated | Cross-referenced with transactions |
| SIG-26-WVS-AQ3B | withholding us 10% | pending_review | Historical match confirmed |
| citric acid | Lactic Acid | pending_review | Verified via product specs |
| Vat Standard CN 10% | SIG-51-MVX-XKUB | unverified | Verified via product specs |
| PO-SO-50-TE-497 | citric acid 25% premium | unverified | Cross-referenced with transactions |
| Continental Solutions | SIG-56-END-D8WH | pending_review | Auto-mapped, validated |
| Customs Duty FR 19% | Vat Standard DE 19% | unverified | Historical match confirmed |
| SIG-67-MFU-QOZ9 Group | VE-DI-578 International | auto_generated | Verified via product specs |
| Fructose Grade A | Isoglucose | pending_review | Confirmed by domain expert |
| SIG-44-FWT-OA3N | Wheat Gluten 25% Standard | pending_review | Auto-mapped, validated |
| CA-CA-947 | Traubenzucker 99.5% | pending_review | Auto-mapped, validated |
| Elite Handel Corp. | SIG-53-HTQ-XVWB Group | auto_generated | Historical match confirmed |
| SIG-13-SXA-38WM | Nexus Sourcing | unverified | Verified via product specs |
| Nordic Distribution | Vertex Ingredients Ltd. | unverified | Confirmed by domain expert |
| vat standard us 19% | Customs Duty BR 15% | pending_review | Historical match confirmed |
| prism ingredients | AT-SU-435 KG | unverified | Auto-mapped, validated |
| SIG-25-VPE-TOC1 | Maltodextrin-Pulver DE10 | unverified | Cross-referenced with transactions |
| CY-577 | Weizenklebereiweiß | pending_review | Historical match confirmed |
| Cyclodextrin Premiumqualität | SIG-87-IEF-VKAD | unverified | Confirmed by domain expert |
| Cyclodextrin Qualitätsstufe I | PE-PR-302 | unverified | Auto-mapped, validated |
| PR-IN-149 Holdings | nordic distribution AG | unverified | Cross-referenced with transactions |
| Pinnacle Rohstoffe NV | SIG-48-MQG-OVJU SAS | unverified | Confirmed by domain expert |
| SIG-76-GDP-2JN8 | SO-CH-ST-522 | pending_review | Cross-referenced with transactions |
| Atlas Versorgung GmbH | Nexus Materials | pending_review | Cross-referenced with transactions |
| CO-SO-101 | SIG-62-DCP-L2AF | auto_generated | Verified via product specs |
| Resistente Stärke Pharmazeutisch rein | PO-SO-763 | auto_generated | Historical match confirmed |
| GL-LO-935 | SIG-39-EWA-Q37M | pending_review | Cross-referenced with transactions |
| SIG-40-CXK-QT2E Group | CA-CO-939 | pending_review | Verified via product specs |
| DE-PH-GR-173 | sunflower oil standard | pending_review | Cross-referenced with transactions |
| SO-IS-50-GR-B-983 | SIG-22-TOX-02GV | auto_generated | Historical match confirmed |
| VA-ST-N-5-192 | Withholding BR 5% | auto_generated | Historical match confirmed |
| Citric Acid 70% Food Grade | SIG-30-ISA-9SS7 | pending_review | Cross-referenced with transactions |
| SIG-13-ZIB-S8MV International | ST-CO-827 Holdings | pending_review | Cross-referenced with transactions |
| Isoglucose 70% | SIG-58-SVK-Z948 | auto_generated | Confirmed by domain expert |
| SIG-56-CMM-ODF7 | casein 50% premium | pending_review | Historical match confirmed |
| Vat Reduced GB 21% | SIG-48-BCI-7SYR | unverified | Cross-referenced with transactions |
| atlantic supply | Premier Solutions LLC | auto_generated | Cross-referenced with transactions |
| Dextrin 50% | lactic acid | auto_generated | Auto-mapped, validated |
| Lactic Acid 50% Premiumqualität | citric acid 25% | pending_review | Verified via product specs |
| GL-IN-746 LLC | SIG-92-FQX-S1BC | unverified | Auto-mapped, validated |
| Baltic Versorgung GmbH | Vertex Supply Co. | unverified | Cross-referenced with transactions |
| PR-IN-409 LLC | Atlantic Trading | auto_generated | Confirmed by domain expert |
| atlas logistics | CO-MA-295 | pending_review | Verified via product specs |
| SIG-64-VUE-OGQ2 | Ascorbic Acid | auto_generated | Auto-mapped, validated |
| Kasein 98% | SIG-41-YLB-IZED | unverified | Verified via product specs |
| CI-AC-PH-GR-209 | Cyclodextrin | auto_generated | Cross-referenced with transactions |
| Soja Isolate Premiumqualität | RA-OI-GR-A-272 | auto_generated | Historical match confirmed |
| ST-LO-637 | Vertex Logistics | auto_generated | Historical match confirmed |
| Soja Isolate Lebensmittelrein | SIG-41-SWO-23GD | auto_generated | Cross-referenced with transactions |
| Apex Chemicals | apex chemicals Inc. | auto_generated | Confirmed by domain expert |
| Prime Enterprise Holdings | Stratos Ingredients | unverified | Confirmed by domain expert |
| Kaliumsorbat | Fructose | pending_review | Cross-referenced with transactions |
| Quantum Commodities PLC | QU-DI-467 Holdings | auto_generated | Verified via product specs |
| Glukosesirup Syrup 99.5% Qualitätsstufe II | SIG-47-HPA-L2FX | unverified | Confirmed by domain expert |
| Central Partners Corp. | SIG-67-MFU-QOZ9 Group | auto_generated | Auto-mapped, validated |
| Lactic Acid | CO-OI-FO-GR-870 | pending_review | Historical match confirmed |
| SIG-87-SQR-587P | excise us 20% | unverified | Confirmed by domain expert |
| Elite Logistics Holdings | SIG-31-LDA-I5LG Ltd. | auto_generated | Auto-mapped, validated |
| Coconut Oil 25% | SIG-50-NZZ-E4UN | unverified | Verified via product specs |
| SIG-50-CEU-F5QB | PR-LO-393 | unverified | Cross-referenced with transactions |
| LA-AC-70-781 | Glukosesirup Syrup 99.5% Qualitätsstufe II | pending_review | Verified via product specs |
| SIG-79-HKV-T268 | Quantum Materials | pending_review | Verified via product specs |
| CO-OI-98-876 | soy isolate premium | pending_review | Confirmed by domain expert |
| Pinnacle Supply International | quantum trading Holdings | unverified | Auto-mapped, validated |
| SIG-29-KJI-GJKC | Palm Oil 25% Grade A | unverified | Cross-referenced with transactions |
| Excise NL 20% | VA-RE-G-10-585 | pending_review | Historical match confirmed |
| Sorbinsäure 50% Lebensmittelrein | CA-CA-98-928 | unverified | Historical match confirmed |
| Elite Versorgung SA | Central Commodities Ltd. | unverified | Cross-referenced with transactions |
| Coconut Oil Pharma Grade | SO-BE-ST-871 | auto_generated | Historical match confirmed |
| maltodextrin de25 | Calcium Carbonate | auto_generated | Historical match confirmed |
| Pinnacle Logistics International | Global Solutions | pending_review | Historical match confirmed |
| Traubenzucker Qualitätsstufe I | SO-BE-25-774 | pending_review | Verified via product specs |
| wheat gluten food grade | Soy Isolate Standard | auto_generated | Historical match confirmed |
| DE-99.5-ST-905 | Isoglucose | pending_review | Verified via product specs |
| nexus enterprise | PA-MA-672 | pending_review | Auto-mapped, validated |
| catalyst enterprise | SIG-75-XPL-QWB7 GmbH | unverified | Verified via product specs |
| Catalyst Materials | pacific materials | pending_review | Verified via product specs |
| prime supply | Core Logistik | auto_generated | Verified via product specs |
| potassium sorbate 50% tech grade | Casein 25% Grade A | auto_generated | Historical match confirmed |
| Lactic Acid 98% | SO-AC-98-579 | unverified | Cross-referenced with transactions |
| SU-OI-98-462 | Sodium Benzoate 70% | auto_generated | Verified via product specs |
| Global Versorgung | quantum commodities Holdings | pending_review | Auto-mapped, validated |
| SIG-84-DSO-4S47 | Cyclodextrin Lebensmittelrein | unverified | Auto-mapped, validated |
| SIG-58-SVK-Z948 | Rapeseed Oil | unverified | Auto-mapped, validated |
| SIG-96-FYH-4ROJ SARL | Atlantic Versorgung LLC | pending_review | Cross-referenced with transactions |
| SIG-66-ZOH-E8TV | SO-BE-667 | auto_generated | Cross-referenced with transactions |
| nordic sourcing | Global Sourcing | unverified | Historical match confirmed |
| Vat Standardqualität DE 25% | vat standard fr 25% | pending_review | Verified via product specs |
| Ascorbic Acid 70% | Rapsöl 98% | pending_review | Auto-mapped, validated |
| SIG-69-OFZ-JW34 | RA-OI-745 | auto_generated | Confirmed by domain expert |
| SIG-20-UMV-LJM6 | Resistant Starch 50% | pending_review | Historical match confirmed |
| PA-OI-25-GR-A-241 | coconut oil premium | pending_review | Confirmed by domain expert |
| Vanguard Werkstoffe | vanguard supply | unverified | Verified via product specs |
| SIG-68-KHP-8RTJ | FR-25-GR-B-641 | pending_review | Verified via product specs |
| Zitronensäure Standardqualität | PO-SO-339 | pending_review | Verified via product specs |
| SU-OI-FO-GR-778 | Dextrose | auto_generated | Confirmed by domain expert |
| ZE-PA-511 PLC | Vertex Vertrieb NV | auto_generated | Confirmed by domain expert |
| SIG-29-XAN-WDDA | Nexus Materials | auto_generated | Verified via product specs |
| SIG-13-WHV-DDIN | SO-BE-98-PH-GR-434 | auto_generated | Confirmed by domain expert |
| casein | Traubenzucker Standardqualität | unverified | Verified via product specs |
| SIG-39-BHZ-K8SS | Prism Sourcing | unverified | Auto-mapped, validated |
| SIG-95-HLU-HD5X GmbH | premier materials | unverified | Auto-mapped, validated |
| Wheat Gluten | SIG-88-VVU-EL88 | pending_review | Verified via product specs |
| SIG-53-MHB-8KZX | Prism Materials | pending_review | Confirmed by domain expert |
| SO-IS-PR-242 | Natriumchlorid Technische Qualität | pending_review | Cross-referenced with transactions |
| Vat Reduced BR 10% | customs duty de 0% | auto_generated | Verified via product specs |
| SIG-52-JJF-4GXO International | Meridian Ingredients | pending_review | Confirmed by domain expert |
| Dextrose | SIG-90-SJW-O06V | pending_review | Cross-referenced with transactions |
| GL-SY-98-FO-GR-198 | Calcium Carbonate Grade B | auto_generated | Auto-mapped, validated |
| pea protein standard | SIG-85-SIL-CNEA | auto_generated | Cross-referenced with transactions |
| PA-LO-382 Group | Catalyst Verarbeitung | unverified | Verified via product specs |
| Pacific Vertrieb Group | prism chemicals | auto_generated | Confirmed by domain expert |
| Casein Grade A | Fructose Standardqualität | auto_generated | Historical match confirmed |
| dextrose standard | Maltodextrin-Pulver DE10 Premiumqualität | pending_review | Historical match confirmed |
| Fructose | MA-DE-859 | auto_generated | Historical match confirmed |
| EX-I-19-464 | excise in 0% | pending_review | Auto-mapped, validated |
| SIG-99-TBJ-83YG KG | Central Manufacturing Holdings | pending_review | Cross-referenced with transactions |
| Sorbinsäure 98% | Coconut Oil Standard | unverified | Confirmed by domain expert |
| central sourcing | PI-SO-251 | pending_review | Confirmed by domain expert |
| nexus supply | PI-DI-618 NV | unverified | Verified via product specs |
| Weizenklebereiweiß | Calcium Carbonate 98% | auto_generated | Cross-referenced with transactions |
| QU-TR-440 | Quantum Verarbeitung PLC | auto_generated | Cross-referenced with transactions |
| sunflower oil standard | DE-706 | unverified | Auto-mapped, validated |
| SO-CH-98-GR-B-961 | potassium sorbate | unverified | Auto-mapped, validated |
| SIG-92-RHW-233J | excise br 5% | pending_review | Historical match confirmed |
| Casein | AS-AC-TE-342 | unverified | Auto-mapped, validated |
| ME-LO-731 | zenith sourcing | unverified | Verified via product specs |
| SIG-60-RUC-CU6A | zenith trading AG | pending_review | Confirmed by domain expert |
| pinnacle supply | Nordic Rohstoffe | auto_generated | Cross-referenced with transactions |
| SIG-69-UAZ-1ODW | Zenith Versorgung GmbH | pending_review | Historical match confirmed |
| SIG-43-GRJ-P3HT | Potassium Sorbate | pending_review | Auto-mapped, validated |
| SIG-89-HLJ-NILC | CO-SU-CO-635 | unverified | Confirmed by domain expert |
| lactic acid 70% | Pea Protein 98% | auto_generated | Verified via product specs |
| Palmfett | rapeseed oil tech grade | pending_review | Auto-mapped, validated |
| Sonnenblumenöl 70% | DE-FO-GR-588 | unverified | Historical match confirmed |
| SIG-35-SZU-VMRU | Palmfett | auto_generated | Auto-mapped, validated |
| SIG-83-TNT-G0Q1 AG | vertex commodities AG | auto_generated | Cross-referenced with transactions |
| SIG-39-BAT-DD7R | AS-AC-GR-B-855 | pending_review | Cross-referenced with transactions |
| Vanguard Logistik | SIG-97-BAE-XNL8 | unverified | Verified via product specs |
| maltodextrin de10 | Zitronensäure 70% | pending_review | Verified via product specs |
| Soy Isolate | sodium benzoate 98% pharma grade | unverified | Cross-referenced with transactions |
| LA-AC-471 | Wheat Gluten | unverified | Verified via product specs |
| Natriumchlorid 98% | sodium chloride | auto_generated | Verified via product specs |
| SIG-42-BEO-614U | SU-OI-251 | pending_review | Verified via product specs |
| Maltodextrin DE15 | rapeseed oil tech grade | auto_generated | Auto-mapped, validated |
| Palmfett | sodium benzoate premium | auto_generated | Historical match confirmed |
| nexus logistics | PI-SU-CO-364 | auto_generated | Historical match confirmed |
| fructose standard | Traubenzucker Standardqualität | pending_review | Auto-mapped, validated |
| DE-GR-A-351 | SIG-58-EEN-BKJF | pending_review | Auto-mapped, validated |
| Natriumbenzoat 99.5% | Lactic Acid Food Grade | auto_generated | Cross-referenced with transactions |
| FR-GR-A-600 | SIG-66-EQU-IW6V | pending_review | Confirmed by domain expert |
| casein 98% standard | Citric Acid | pending_review | Auto-mapped, validated |
| lactic acid standard | Calcium Carbonate Qualitätsstufe II | unverified | Confirmed by domain expert |
| SIG-47-HDT-7PPC | Sorbic Acid 70% | auto_generated | Cross-referenced with transactions |
| PA-SO-270 | SIG-44-DLM-CU63 | unverified | Confirmed by domain expert |
| SIG-85-PGT-NQA4 | SO-BE-99.5-195 | unverified | Confirmed by domain expert |
| Stellar Werkstoffe | ME-LO-670 | unverified | Auto-mapped, validated |
| SIG-47-NVU-R3XU | SU-OI-FO-GR-778 | auto_generated | Confirmed by domain expert |
| CU-DU-N-15-558 | SIG-51-MVX-XKUB | pending_review | Verified via product specs |
| Natriumchlorid Technische Qualität | palm oil food grade | unverified | Cross-referenced with transactions |
| ST-CO-650 International | elite trading Ltd. | auto_generated | Historical match confirmed |
| PO-SO-50-GR-B-154 | SIG-70-IKQ-7KBN | pending_review | Confirmed by domain expert |
| Atlas Industrien International | vanguard partners Ltd. | unverified | Confirmed by domain expert |
| Premier Logistik KG | Stratos Processing | auto_generated | Verified via product specs |
| Customs Duty FR 25% | CU-DU-I-5-731 | auto_generated | Auto-mapped, validated |
| SIG-82-ZXL-FF30 International | Stellar Partners | pending_review | Historical match confirmed |
| vanguard supply NV | Nordic Chemicals | unverified | Verified via product specs |
| Soy Isolate 99.5% Standard | SIG-61-IQH-EKWH | pending_review | Auto-mapped, validated |
| AP-TR-161 International | Stratos Ingredients SARL | pending_review | Cross-referenced with transactions |
| Fructose Qualitätsstufe II | wheat gluten 98% | auto_generated | Verified via product specs |
| QU-TR-219 International | premier trading GmbH | pending_review | Confirmed by domain expert |
| ascorbic acid | Soja Isolate Qualitätsstufe I | pending_review | Historical match confirmed |
| Atlantic Materials | pacific supply | pending_review | Confirmed by domain expert |
| Sodium Chloride | sodium benzoate 99.5% tech grade | auto_generated | Historical match confirmed |
| SIG-41-OMW-SN1T | AS-AC-70-515 | auto_generated | Historical match confirmed |
| CE-PR-134 | prism industries Inc. | unverified | Cross-referenced with transactions |
| withholding gb 21% | Vat Reduced CN 21% | auto_generated | Verified via product specs |
| sunflower oil 98% | SIG-11-RGJ-D3IR | unverified | Cross-referenced with transactions |
| SO-BE-GR-B-936 | wheat gluten standard | unverified | Auto-mapped, validated |
| Vat Standard FR 20% | VA-ST-D-19-529 | auto_generated | Historical match confirmed |
| SIG-35-SZU-VMRU | Pea Protein 70% Lebensmittelrein | auto_generated | Verified via product specs |
| Isoglucose Technical | PA-OI-410 | unverified | Confirmed by domain expert |
| SIG-35-BYM-BYQ7 Inc. | QU-PR-732 SA | unverified | Confirmed by domain expert |
| Pea Protein Premiumqualität | SO-BE-GR-A-760 | unverified | Auto-mapped, validated |
| Customs Duty FR 15% | SIG-30-HHL-9B4G | pending_review | Cross-referenced with transactions |
| Cyclodextrin 70% Food Grade | Dextrin Lebensmittelrein | pending_review | Confirmed by domain expert |
| Sodium Benzoate 25% | Sonnenblumenöl Premiumqualität | unverified | Verified via product specs |
| SIG-73-AXD-XIX9 | zenith supply | auto_generated | Confirmed by domain expert |
| SO-CH-GR-B-273 | SIG-11-SLQ-KF5B | pending_review | Confirmed by domain expert |
| palm oil 99.5% | Resistente Stärke Lebensmittelrein | auto_generated | Historical match confirmed |
| Vanguard Sourcing | VA-SU-CO-459 | pending_review | Auto-mapped, validated |
| CO-CH-401 Inc. | Atlantic Partners | auto_generated | Historical match confirmed |
| Atlantic Industrien International | Stellar Processing Holdings | pending_review | Cross-referenced with transactions |
| SIG-44-UKH-MO4F | withholding fr 5% | unverified | Cross-referenced with transactions |
| Fructose Qualitätsstufe II | MA-DE-437 | auto_generated | Verified via product specs |
| SIG-75-GGJ-DK9O | AT-SO-260 | pending_review | Confirmed by domain expert |
| SO-IS-50-568 | SIG-41-HMT-W0GK | unverified | Verified via product specs |
| ST-SU-125 SA | baltic chemicals AG | unverified | Auto-mapped, validated |
| Calcium Carbonate 99.5% Food Grade | Traubenzucker 25% | pending_review | Verified via product specs |
| continental manufacturing Inc. | VA-LO-190 International | unverified | Confirmed by domain expert |
| Soja Isolate 98% Premiumqualität | SIG-51-ZAY-11PM | auto_generated | Verified via product specs |
| HO-LO-699 | stellar supply | unverified | Confirmed by domain expert |
| WI-G-15-758 | Customs Duty BR 15% | auto_generated | Confirmed by domain expert |
| Ascorbic Acid 99.5% | SIG-58-NYA-2O4M | pending_review | Verified via product specs |
| SIG-57-GUP-S7UK | apex sourcing | unverified | Historical match confirmed |
| SIG-44-HTV-P84J | Dextrose Standard | auto_generated | Verified via product specs |
| Premier Enterprise International | PR-EN-764 Ltd. | pending_review | Auto-mapped, validated |
| NE-EN-710 NV | premier enterprise Holdings | unverified | Historical match confirmed |
| ST-SU-950 SAS | vertex distribution NV | pending_review | Confirmed by domain expert |
| SIG-89-ISH-EQW6 | RE-ST-98-PH-GR-372 | auto_generated | Confirmed by domain expert |
| calcium carbonate 50% pharma grade | Soja Isolate 50% Premiumqualität | unverified | Auto-mapped, validated |
| VA-ST-D-21-476 | excise nl 15% | unverified | Historical match confirmed |
| SO-BE-99.5-ST-342 | Maltodextrin-Pulver DE15 Standardqualität | pending_review | Cross-referenced with transactions |
| Vanguard Logistik International | prime solutions | auto_generated | Verified via product specs |
| Dextrin Qualitätsstufe II | DE-GR-A-472 | unverified | Verified via product specs |
| SIG-78-WDE-NNV9 | Calcium Carbonate 50% Pharma Grade | pending_review | Verified via product specs |
| Customs Duty BR 21% | VA-ST-D-25-900 | auto_generated | Auto-mapped, validated |
| GL-SY-371 | SIG-60-TMF-XHW0 | auto_generated | Historical match confirmed |
| Traubenzucker 99.5% | SIG-56-ZVH-GATJ | auto_generated | Cross-referenced with transactions |
| sodium benzoate | CY-GR-A-208 | pending_review | Verified via product specs |
| palm oil standard | SIG-37-PYQ-815V | pending_review | Verified via product specs |
| SO-AC-PR-928 | Kaliumsorbat | auto_generated | Historical match confirmed |
| RA-OI-GR-A-980 | Sunflower Oil Grade A | unverified | Historical match confirmed |
| central materials BV | Prime Verarbeitung AG | unverified | Cross-referenced with transactions |
| Palmfett 70% Technische Qualität | sorbic acid | auto_generated | Auto-mapped, validated |
| Calcium Carbonate 98% | Kasein 25% Pharmazeutisch rein | pending_review | Historical match confirmed |
| Fructose Premiumqualität | CY-892 | pending_review | Verified via product specs |
| CI-AC-GR-A-813 | SIG-76-RKG-E8RT | auto_generated | Cross-referenced with transactions |
| Baltic Rohstoffe Ltd. | continental enterprise International | auto_generated | Historical match confirmed |
| LA-AC-FO-GR-469 | Palmfett Lebensmittelrein | unverified | Historical match confirmed |
| SIG-65-RQH-9Y5B | SO-AC-99.5-338 | auto_generated | Confirmed by domain expert |
| EX-B-25-579 | Vat Standard IN 0% | auto_generated | Historical match confirmed |
| Continental Solutions NV | Stratos Processing | auto_generated | Cross-referenced with transactions |
| SIG-25-WCC-PPMH | vat standard fr 19% | pending_review | Cross-referenced with transactions |
| SIG-24-PBC-613L | Soja Isolate Standardqualität | auto_generated | Verified via product specs |
| SIG-49-UKY-6H3R | GL-SY-99.5-FO-GR-825 | pending_review | Verified via product specs |
| lactic acid 98% | SIG-24-CXH-R2TY | pending_review | Confirmed by domain expert |
| Soja Isolate 99.5% | CA-50-PR-226 | auto_generated | Confirmed by domain expert |
| dextrin premium | SO-CH-GR-B-273 | pending_review | Cross-referenced with transactions |
| customs duty fr 15% | Vat Standardqualität US 20% | auto_generated | Verified via product specs |
| QU-PR-732 SA | Pinnacle Industrien SAS | unverified | Historical match confirmed |
| Sodium Benzoate 98% | SU-OI-50-GR-A-521 | pending_review | Auto-mapped, validated |
| Maltodextrin DE15 Premium | sodium benzoate 25% | auto_generated | Auto-mapped, validated |
| Customs Duty CN 10% | Vat Reduced BR 21% | pending_review | Cross-referenced with transactions |
| SIG-99-IZM-CYBY | Sorbinsäure 98% | unverified | Cross-referenced with transactions |
| DE-PH-GR-173 | Calcium Carbonate 98% Pharmazeutisch rein | unverified | Historical match confirmed |
| Wheat Gluten 25% Food Grade | wheat gluten 98% premium | unverified | Cross-referenced with transactions |
| citric acid | Sodium Chloride Technical | pending_review | Cross-referenced with transactions |
| Premier Trading Group | atlas enterprise | pending_review | Historical match confirmed |
| Weizenklebereiweiß Qualitätsstufe II | SIG-51-YTN-F537 | pending_review | Cross-referenced with transactions |
| Soja Isolate Lebensmittelrein | SIG-60-WYC-NAXS | auto_generated | Confirmed by domain expert |
| Sonnenblumenöl 50% Qualitätsstufe I | SIG-16-MLJ-HWA7 | unverified | Cross-referenced with transactions |
| PE-PR-557 | Dextrin Standardqualität | pending_review | Confirmed by domain expert |
| Stratos Materials | Stellar Logistik | auto_generated | Verified via product specs |
| SIG-10-BLC-3L38 | Dextrin Grade A | unverified | Cross-referenced with transactions |
| Baltic Industrien NV | elite partners GmbH | pending_review | Confirmed by domain expert |
| Glucose Syrup Technical | SIG-30-EKM-GB1A | auto_generated | Historical match confirmed |
| Calcium Carbonate | CO-OI-FO-GR-162 | unverified | Historical match confirmed |
| SIG-45-ZHK-QWIG | coconut oil 98% food grade | pending_review | Auto-mapped, validated |
| SIG-15-VIS-079C | VA-RE-F-21-230 | unverified | Auto-mapped, validated |
| SIG-76-GDP-2JN8 | Palm Oil 50% Premium | unverified | Auto-mapped, validated |
| SIG-83-TEU-OH8F Group | zenith trading AG | auto_generated | Auto-mapped, validated |
| Fructose Technische Qualität | SO-BE-GR-B-914 | auto_generated | Auto-mapped, validated |
| Potassium Sorbate Standard | LA-AC-98-GR-A-841 | auto_generated | Auto-mapped, validated |
| SIG-19-TLQ-1P5Z | soy isolate 25% | unverified | Auto-mapped, validated |
| SIG-44-NHM-IY9D | EX-I-19-464 | unverified | Historical match confirmed |
| SO-AC-GR-A-997 | Palm Oil Food Grade | pending_review | Confirmed by domain expert |
| Rapeseed Oil Grade A | coconut oil 70% | unverified | Verified via product specs |
| cyclodextrin 70% food grade | SIG-89-MUE-HZH1 | pending_review | Verified via product specs |
| WI-F-10-935 | SIG-34-HFN-4G56 | unverified | Cross-referenced with transactions |
| CI-AC-ST-565 | Sonnenblumenöl Technische Qualität | pending_review | Cross-referenced with transactions |
| Pinnacle Materials SA | ST-PA-227 PLC | unverified | Auto-mapped, validated |
| excise in 7% | VA-ST-D-21-476 | pending_review | Cross-referenced with transactions |
| Sodium Chloride | SIG-42-MEI-2SCI | auto_generated | Historical match confirmed |
| SIG-71-OEX-5BRF | Glucose Syrup | auto_generated | Historical match confirmed |
| SIG-16-YRD-5C3Z | ascorbic acid standard | auto_generated | Historical match confirmed |
| SIG-43-TPO-RSBY | horizon materials | unverified | Cross-referenced with transactions |
| SIG-92-CZO-O9ON | CA-CA-50-GR-B-200 | auto_generated | Verified via product specs |
| Pacific Vertrieb International | NE-IN-874 SA | pending_review | Historical match confirmed |
| SIG-76-PYX-S5PY | SO-IS-25-PH-GR-832 | auto_generated | Confirmed by domain expert |
| Ascorbic Acid Premiumqualität | Lactic Acid Grade B | pending_review | Confirmed by domain expert |
| Cyclodextrin | rapeseed oil 50% premium | auto_generated | Cross-referenced with transactions |
| Resistant Starch Pharma Grade | PO-SO-ST-914 | auto_generated | Auto-mapped, validated |
| calcium carbonate | Isoglucose Qualitätsstufe II | auto_generated | Historical match confirmed |
| Global Logistics | Vertex Solutions NV | unverified | Auto-mapped, validated |
| SIG-58-JZY-SBU1 | Customs Duty CN 0% | pending_review | Verified via product specs |
| Vertex Sourcing | stratos logistics | pending_review | Auto-mapped, validated |
| coconut oil 70% | Resistente Stärke | auto_generated | Confirmed by domain expert |
| Kaliumsorbat | dextrin | pending_review | Confirmed by domain expert |
| SO-CH-GR-B-273 | sodium chloride 98% standard | unverified | Confirmed by domain expert |
| dextrin standard | Natriumbenzoat 99.5% | pending_review | Cross-referenced with transactions |
| Sorbinsäure Qualitätsstufe II | dextrose 99.5% | pending_review | Auto-mapped, validated |
| SIG-86-VGU-A4FE | Palm Oil Food Grade | auto_generated | Verified via product specs |
| Lactic Acid 25% | Kaliumsorbat | pending_review | Auto-mapped, validated |
| SIG-46-SVJ-5IZO | Fructose Technical | auto_generated | Confirmed by domain expert |
| Wheat Gluten 50% Pharma Grade | Sorbinsäure 50% | pending_review | Verified via product specs |
| SIG-64-ILX-G2AZ PLC | Baltic Industrien NV | auto_generated | Cross-referenced with transactions |
| Nordic Chemicals BV | NE-SU-335 | auto_generated | Historical match confirmed |
| Sodium Chloride 25% Food Grade | sunflower oil food grade | unverified | Historical match confirmed |
| SIG-32-UBB-EMYO | withholding fr 15% | auto_generated | Auto-mapped, validated |
| CA-98-TE-238 | resistant starch 70% | auto_generated | Cross-referenced with transactions |
| SIG-79-DVU-H9H4 | Sunflower Oil Standard | pending_review | Cross-referenced with transactions |
| wheat gluten 70% | CA-CA-FO-GR-991 | auto_generated | Auto-mapped, validated |
| ST-LO-635 LLC | SIG-20-ZUA-APIG Ltd. | auto_generated | Historical match confirmed |
| CY-763 | SIG-35-HZD-3XBW | auto_generated | Auto-mapped, validated |
| SIG-39-OZI-N968 | Rapsöl 70% Qualitätsstufe II | pending_review | Historical match confirmed |
| Lactic Acid Lebensmittelrein | Palm Oil 70% Technical | pending_review | Confirmed by domain expert |
| Maltodextrin-Pulver DE30 | Maltodextrin DE15 Premium | unverified | Confirmed by domain expert |
| WH-GL-FO-GR-876 | Kaliumsorbat | unverified | Cross-referenced with transactions |
| Lactic Acid 98% Grade A | lactic acid | pending_review | Historical match confirmed |
| SIG-35-TKX-8TRE | Sonnenblumenöl Standardqualität | auto_generated | Historical match confirmed |
| catalyst supply Holdings | QU-SO-556 | pending_review | Historical match confirmed |
| SIG-78-QOY-5RIX | Vanguard Sourcing | pending_review | Auto-mapped, validated |
| SIG-30-NQN-ZENP | NE-PR-428 GmbH | pending_review | Auto-mapped, validated |
| Rapeseed Oil | Palmfett | unverified | Auto-mapped, validated |
| Natriumchlorid Technische Qualität | SIG-50-ABM-7VSK | auto_generated | Cross-referenced with transactions |
| SIG-99-TBJ-83YG KG | global distribution Corp. | unverified | Historical match confirmed |
| Weizenklebereiweiß Qualitätsstufe II | SIG-42-IEF-RFC9 | pending_review | Verified via product specs |
| Vertex Materials | GL-MA-770 | pending_review | Historical match confirmed |
| SIG-27-UKP-V2ME | Kaliumsorbat Standardqualität | auto_generated | Auto-mapped, validated |
| CA-CA-98-PH-GR-242 | SIG-89-JZC-1682 | auto_generated | Confirmed by domain expert |
| Withholding BR 20% | Vat Standardqualität FR 0% | auto_generated | Verified via product specs |
| resistant starch 70% food grade | Sorbic Acid 25% Grade B | unverified | Verified via product specs |
| Ascorbic Acid | Sonnenblumenöl Standardqualität | auto_generated | Cross-referenced with transactions |
| Isoglucose Grade B | SIG-91-PEG-USI6 | auto_generated | Auto-mapped, validated |
| AS-AC-ST-686 | Glucose Syrup 99.5% Grade B | pending_review | Cross-referenced with transactions |
| sorbic acid premium | Pea Protein | pending_review | Historical match confirmed |
| CO-MA-127 Group | prism solutions Ltd. | pending_review | Verified via product specs |
| Palm Oil Grade B | SIG-41-YLB-IZED | unverified | Auto-mapped, validated |
| glucose syrup food grade | PA-OI-50-273 | pending_review | Cross-referenced with transactions |
| Global Enterprise NV | SIG-69-VKL-Z1GW KG | unverified | Historical match confirmed |
| RA-OI-GR-B-834 | SIG-76-GST-OWGM | unverified | Confirmed by domain expert |
| Sorbinsäure 50% Standardqualität | SIG-13-FYG-4NN9 | unverified | Auto-mapped, validated |
| Horizon Rohstoffe PLC | SIG-14-BST-M9NP GmbH | unverified | Historical match confirmed |
| cyclodextrin | Dextrose | auto_generated | Historical match confirmed |
| SIG-71-PGT-OFPC | Weizenklebereiweiß 50% Technische Qualität | unverified | Auto-mapped, validated |
| prism ingredients NV | SIG-97-BXB-U2Y7 Ltd. | pending_review | Confirmed by domain expert |
| Catalyst Enterprise International | continental partners | pending_review | Verified via product specs |
| Nexus Materials | Elite Logistik | auto_generated | Auto-mapped, validated |
| Core Werkstoffe | VA-LO-948 | unverified | Cross-referenced with transactions |
| Vat Reduced CN 19% | VA-RE-C-10-738 | pending_review | Cross-referenced with transactions |
| Vertex Sourcing | nexus sourcing | unverified | Verified via product specs |
| SIG-29-KJI-GJKC | SU-OI-TE-705 | pending_review | Auto-mapped, validated |
| Horizon Materials | Zenith Logistik | unverified | Verified via product specs |
| Baltic Verarbeitung Group | SIG-99-AYV-D18J International | unverified | Auto-mapped, validated |
| Soy Isolate | SO-CH-99.5-618 | auto_generated | Auto-mapped, validated |
| Prime Versorgung | Baltic Distribution Group | auto_generated | Verified via product specs |
| coconut oil 25% tech grade | SU-OI-98-462 | auto_generated | Auto-mapped, validated |
| SIG-17-LVE-03G9 | Isoglucose 25% | auto_generated | Verified via product specs |
| LA-AC-554 | sodium benzoate 50% | pending_review | Verified via product specs |
| Global Chemicals Ltd. | Nexus Partners SAS | unverified | Historical match confirmed |
| vertex ingredients PLC | Apex Verarbeitung | auto_generated | Verified via product specs |
| Central Sourcing | atlas supply | auto_generated | Cross-referenced with transactions |
| SO-AC-25-GR-B-198 | Weizenklebereiweiß Standardqualität | auto_generated | Auto-mapped, validated |
| SIG-76-GST-OWGM | Palm Oil Food Grade | pending_review | Historical match confirmed |
| Natriumbenzoat 50% | SU-OI-ST-338 | pending_review | Verified via product specs |
| Isoglucose | CA-CA-98-928 | unverified | Confirmed by domain expert |
| Natriumbenzoat | sodium benzoate 25% | unverified | Historical match confirmed |
| ME-MA-989 | SIG-52-QOU-LC66 | unverified | Historical match confirmed |
| SIG-23-OPT-7QHV | Rapeseed Oil Technical | pending_review | Confirmed by domain expert |
| Pea Protein | SIG-52-FHA-5PI2 | unverified | Cross-referenced with transactions |
| SIG-36-BVE-5U7D | Zitronensäure 50% Qualitätsstufe I | pending_review | Cross-referenced with transactions |
| PR-SO-102 | SIG-85-SQB-MODP BV | pending_review | Confirmed by domain expert |
| Pacific Supply Co. | Nordic Versorgung GmbH | pending_review | Confirmed by domain expert |
| Core Partners | Vertex Distribution | pending_review | Auto-mapped, validated |
| SO-CH-70-GR-B-821 | dextrin pharma grade | auto_generated | Verified via product specs |
| nexus chemicals Group | EL-CH-346 GmbH | pending_review | Verified via product specs |
| Vanguard Handel LLC | catalyst enterprise | auto_generated | Auto-mapped, validated |
| resistant starch 50% | Weizenklebereiweiß 99.5% Technische Qualität | auto_generated | Historical match confirmed |
| SIG-58-NYA-2O4M | Resistant Starch 70% | auto_generated | Historical match confirmed |
| SO-AC-25-GR-B-198 | sodium benzoate 99.5% standard | pending_review | Cross-referenced with transactions |
| sorbic acid pharma grade | SIG-17-IQV-FES7 | pending_review | Historical match confirmed |
| SIG-98-CGL-FHWJ | Traubenzucker Standardqualität | unverified | Cross-referenced with transactions |
| Baltic Versorgung GmbH | PI-MA-112 | auto_generated | Confirmed by domain expert |
| PR-SO-632 | Vertex Supply Co. | auto_generated | Verified via product specs |
| Central Versorgung GmbH | SIG-90-ALF-TQ8F | pending_review | Confirmed by domain expert |
| dextrose 99.5% | SIG-79-RTU-R8IQ | auto_generated | Confirmed by domain expert |
| SIG-55-OPY-GVTN | VA-ST-G-20-932 | pending_review | Auto-mapped, validated |
| Sodium Benzoate 50% Technical | PO-SO-604 | auto_generated | Auto-mapped, validated |
| SIG-62-GUN-FTYL | PA-OI-GR-B-326 | pending_review | Auto-mapped, validated |
| EX-B-21-936 | Withholding GB 5% | unverified | Auto-mapped, validated |
| DE-99.5-720 | Cyclodextrin | auto_generated | Confirmed by domain expert |
| SIG-94-TOI-OFNK | Lactic Acid Pharmazeutisch rein | auto_generated | Cross-referenced with transactions |
| CA-CA-70-883 | Natriumbenzoat Qualitätsstufe II | pending_review | Historical match confirmed |
| casein standard | Ascorbic Acid 50% Standardqualität | auto_generated | Cross-referenced with transactions |
| SU-OI-ST-338 | SIG-60-ZEV-V2NY | auto_generated | Historical match confirmed |
| SIG-56-ZVH-GATJ | fructose 98% premium | auto_generated | Historical match confirmed |
| FR-99.5-FO-GR-963 | SIG-19-ZOZ-1S2O | unverified | Confirmed by domain expert |
| baltic trading NV | Quantum Ingredients | pending_review | Cross-referenced with transactions |
| Stratos Werkstoffe | atlantic materials | unverified | Historical match confirmed |
| SIG-75-QRF-XA0H | PR-SU-CO-832 | unverified | Auto-mapped, validated |
| Glukosesirup Syrup Premiumqualität | SIG-41-HMT-W0GK | pending_review | Historical match confirmed |
| Zenith Versorgung GmbH | SIG-92-EXW-KC66 | pending_review | Cross-referenced with transactions |
| DE-TE-406 | Maltodextrin-Pulver DE5 Qualitätsstufe I | auto_generated | Cross-referenced with transactions |
| Dextrin Technische Qualität | Glucose Syrup 98% Food Grade | unverified | Auto-mapped, validated |
| SIG-55-DCV-7OXN | Sodium Benzoate 98% | pending_review | Confirmed by domain expert |
| SIG-61-HXH-PFBC | MA-DE-161 | auto_generated | Confirmed by domain expert |
| SIG-12-IYC-8W63 Holdings | Vertex Trading Group | unverified | Cross-referenced with transactions |
| Citric Acid Grade B | GL-SY-98-939 | unverified | Historical match confirmed |
| SIG-74-EPP-R9AG | CU-DU-D-0-383 | auto_generated | Cross-referenced with transactions |
| Palmfett Standardqualität | DE-GR-B-942 | unverified | Cross-referenced with transactions |
| Catalyst Supply Holdings | NE-SO-511 | auto_generated | Auto-mapped, validated |
| sorbic acid 50% | SO-BE-70-PR-120 | unverified | Cross-referenced with transactions |
| Horizon Partners Ltd. | Catalyst Rohstoffe NV | pending_review | Cross-referenced with transactions |
| Elite Logistics Holdings | CO-LO-919 Holdings | unverified | Confirmed by domain expert |
| Potassium Sorbate 50% | Ascorbic Acid Qualitätsstufe II | unverified | Verified via product specs |
| SIG-23-BLM-EZKX | SO-BE-PH-GR-831 | auto_generated | Confirmed by domain expert |
| BA-SU-CO-430 | Meridian Werkstoffe | pending_review | Cross-referenced with transactions |
| Sodium Benzoate 98% | SU-OI-ST-338 | auto_generated | Auto-mapped, validated |
| Premier Supply Co. | Core Sourcing | pending_review | Cross-referenced with transactions |
| SIG-78-WDE-NNV9 | glucose syrup | unverified | Verified via product specs |
| RA-OI-FO-GR-269 | Casein Grade B | unverified | Auto-mapped, validated |
| Traubenzucker Qualitätsstufe I | SIG-98-JEQ-77GG | auto_generated | Verified via product specs |
| Baltic Verarbeitung Group | SIG-40-RSD-JF0U | auto_generated | Historical match confirmed |
| fructose | CA-CA-50-GR-B-200 | unverified | Cross-referenced with transactions |
| Pea Protein 99.5% | SIG-15-QIT-5CZE | auto_generated | Historical match confirmed |
| SIG-37-JCQ-RB0M | Excise BR 19% | pending_review | Confirmed by domain expert |
| SIG-92-FQW-WCF5 SARL | Atlantic Distribution | auto_generated | Auto-mapped, validated |
| Pea Protein Technical | LA-AC-70-781 | pending_review | Verified via product specs |
| Casein 98% Technical | coconut oil 98% | pending_review | Auto-mapped, validated |
| Prism Manufacturing | AT-IN-899 Group | pending_review | Verified via product specs |
| SIG-38-BKW-2ZX1 | Stratos Materials | unverified | Auto-mapped, validated |
| maltodextrin de25 | Dextrin 70% | pending_review | Historical match confirmed |
| Baltic Versorgung GmbH | premier materials | pending_review | Confirmed by domain expert |
| Resistente Stärke Pharmazeutisch rein | SIG-12-RDG-0JI1 | auto_generated | Confirmed by domain expert |
| Dextrin | SIG-52-EML-H8JV | auto_generated | Verified via product specs |
| Customs Duty DE 0% | vat reduced us 19% | pending_review | Verified via product specs |
| Fructose 50% Standard | Fructose | unverified | Confirmed by domain expert |
| Meridian Materials | Catalyst Werkstoffe | unverified | Verified via product specs |
| calcium carbonate | Resistente Stärke 98% | auto_generated | Verified via product specs |
| NE-DI-555 | SIG-48-MQG-OVJU SAS | auto_generated | Cross-referenced with transactions |
| CU-DU-N-21-524 | excise fr 0% | unverified | Historical match confirmed |
| Vat Standardqualität CN 0% | Vat Reduced FR 21% | pending_review | Auto-mapped, validated |
| Natriumchlorid 25% Premiumqualität | SO-IS-99.5-PR-187 | auto_generated | Cross-referenced with transactions |
| SO-IS-99.5-PR-187 | fructose 70% | auto_generated | Auto-mapped, validated |
| SIG-16-JKI-B4JG | Rapsöl | pending_review | Confirmed by domain expert |
| Glukosesirup Syrup 98% | Casein 50% Premium | auto_generated | Verified via product specs |
| SIG-16-YRD-5C3Z | palm oil 98% | auto_generated | Cross-referenced with transactions |
| ascorbic acid tech grade | SIG-58-LWY-Q8P6 | pending_review | Auto-mapped, validated |
| SIG-49-QVY-JMMU | SO-BE-GR-A-760 | auto_generated | Cross-referenced with transactions |
| Zitronensäure Standardqualität | sodium benzoate 99.5% premium | auto_generated | Auto-mapped, validated |
| Central Werkstoffe | vertex supply | unverified | Cross-referenced with transactions |
| PA-OI-383 | pea protein | pending_review | Verified via product specs |
| Fructose Qualitätsstufe I | PO-SO-TE-239 | unverified | Cross-referenced with transactions |
| Palmfett | Isoglucose Grade B | auto_generated | Historical match confirmed |
| SIG-19-TPS-MSKY | SO-BE-PR-691 | pending_review | Historical match confirmed |
| PO-SO-632 | Traubenzucker | pending_review | Cross-referenced with transactions |
| Pacific Versorgung GmbH | prism materials | unverified | Verified via product specs |
| Rapsöl 98% Standardqualität | CA-CA-99.5-FO-GR-839 | unverified | Cross-referenced with transactions |
| Prism Distribution BV | SIG-78-LEG-I3QI Holdings | pending_review | Verified via product specs |
| fructose 99.5% tech grade | AS-AC-PR-308 | auto_generated | Auto-mapped, validated |
| Palmfett | Palm Oil 70% Grade B | pending_review | Cross-referenced with transactions |
| SIG-84-PAS-5S3O | Maltodextrin-Pulver DE18 Pharmazeutisch rein | pending_review | Historical match confirmed |
| PI-LO-710 NV | Stratos Distribution Group | auto_generated | Historical match confirmed |
| Cyclodextrin Standard | Pea Protein Premiumqualität | pending_review | Historical match confirmed |
| Weizenklebereiweiß 25% Premiumqualität | SIG-79-GLV-IEST | auto_generated | Confirmed by domain expert |
| Atlantic Materials | Continental Versorgung GmbH | pending_review | Historical match confirmed |
| SIG-13-ZRN-WZGO | Vertex Logistics | pending_review | Verified via product specs |
| Dextrose 99.5% | ascorbic acid 50% standard | pending_review | Historical match confirmed |
| SIG-16-FQO-8S1S | Lactic Acid Food Grade | pending_review | Auto-mapped, validated |
| SIG-48-UJX-49KW | pea protein pharma grade | pending_review | Verified via product specs |
| ST-MA-342 | Vertex Sourcing | pending_review | Auto-mapped, validated |
| AP-SU-CO-314 | SIG-38-FPC-A25N | pending_review | Historical match confirmed |
| Premier Rohstoffe Holdings | Meridian Solutions Ltd. | auto_generated | Auto-mapped, validated |
| Calcium Carbonate Qualitätsstufe II | SIG-56-NOU-ZR98 | auto_generated | Cross-referenced with transactions |
| Global Chemicals SAS | elite materials NV | unverified | Cross-referenced with transactions |
| Sorbic Acid Standard | citric acid 99.5% | pending_review | Verified via product specs |
| Central Logistik | SIG-90-ALF-TQ8F | auto_generated | Historical match confirmed |
| Resistant Starch Technical | Lactic Acid | pending_review | Verified via product specs |
| Stellar Supply Co. | AT-SU-CO-755 | auto_generated | Confirmed by domain expert |
| Apex Verarbeitung | SIG-94-CCX-H0AN International | auto_generated | Confirmed by domain expert |
| Atlas Supply Co. | SIG-66-DRZ-QEHY | auto_generated | Historical match confirmed |
| dextrose | Rapeseed Oil 50% Food Grade | auto_generated | Confirmed by domain expert |
| Global Trading Ltd. | SIG-80-QLX-7SNL SAS | unverified | Cross-referenced with transactions |
| Vanguard Logistics | vanguard supply | pending_review | Historical match confirmed |
| potassium sorbate 50% tech grade | FR-PR-614 | unverified | Verified via product specs |
| sorbic acid | SIG-22-SKR-CTIC | unverified | Cross-referenced with transactions |
| casein 25% tech grade | Zitronensäure 70% | pending_review | Auto-mapped, validated |
| core chemicals Group | Vertex Distribution | auto_generated | Confirmed by domain expert |
| Atlantic Vertrieb Holdings | nexus partners Group | pending_review | Cross-referenced with transactions |
| vanguard enterprise | Prism Materials Ltd. | pending_review | Confirmed by domain expert |
| SIG-97-XJT-7TBU | isoglucose 25% | unverified | Verified via product specs |
| Traubenzucker 99.5% | sodium chloride 98% | pending_review | Cross-referenced with transactions |
| ST-PR-265 Corp. | Pacific Werkstoffe GmbH | unverified | Historical match confirmed |
| CU-DU-D-20-742 | Vat Standardqualität DE 0% | pending_review | Auto-mapped, validated |
| Maltodextrin DE15 | casein | unverified | Historical match confirmed |
| GL-SY-GR-B-331 | potassium sorbate tech grade | auto_generated | Auto-mapped, validated |
| Maltodextrin-Pulver DE15 Standardqualität | SIG-18-PCA-V46E | auto_generated | Historical match confirmed |
| Pea Protein 25% Pharmazeutisch rein | cyclodextrin pharma grade | unverified | Cross-referenced with transactions |
| Horizon Materials | elite logistics | pending_review | Historical match confirmed |
| sorbic acid 50% standard | SIG-37-CWM-V4K0 | pending_review | Cross-referenced with transactions |
| LA-AC-70-PH-GR-221 | SIG-32-BYW-WPR9 | pending_review | Historical match confirmed |
| prime processing AG | SIG-94-MUO-QFTQ | auto_generated | Historical match confirmed |
| Ascorbic Acid Premiumqualität | MA-DE-186 | unverified | Auto-mapped, validated |
| Catalyst Ingredients Holdings | CO-DI-629 BV | unverified | Confirmed by domain expert |
| CA-CA-GR-B-162 | Lactic Acid 98% Premium | pending_review | Historical match confirmed |
| SIG-56-ZVH-GATJ | Fructose Technical | unverified | Cross-referenced with transactions |
| CO-OI-70-701 | Palm Oil Pharma Grade | pending_review | Confirmed by domain expert |
| apex trading BV | Atlas Chemicals | auto_generated | Auto-mapped, validated |
| dextrose premium | SO-BE-964 | pending_review | Verified via product specs |
| BA-IN-547 | Quantum Processing SA | unverified | Verified via product specs |
| Global Chemicals Ltd. | SIG-99-PXI-1L7K | pending_review | Confirmed by domain expert |
| Sodium Chloride | Glukosesirup Syrup 99.5% Qualitätsstufe II | pending_review | Verified via product specs |
| SIG-61-PIG-0DBF | glucose syrup 70% food grade | auto_generated | Auto-mapped, validated |
| Premier Logistics | QU-LO-363 | auto_generated | Verified via product specs |
| Pacific Werkstoffe | SIG-51-MQP-ZO0K | unverified | Historical match confirmed |
| Quantum Vertrieb Holdings | QU-PA-832 NV | pending_review | Confirmed by domain expert |
| baltic sourcing | SIG-50-BLC-3NYL | pending_review | Historical match confirmed |
| dextrose 50% | SU-OI-GR-A-224 | unverified | Cross-referenced with transactions |
| Glucose Syrup Food Grade | AS-AC-ST-686 | unverified | Historical match confirmed |
| WH-GL-GR-A-924 | Kaliumsorbat | unverified | Cross-referenced with transactions |
| Dextrose | GL-SY-25-722 | unverified | Confirmed by domain expert |
| Rapsöl | soy isolate standard | unverified | Cross-referenced with transactions |
| Natriumbenzoat 99.5% Qualitätsstufe I | MA-DE-GR-A-871 | pending_review | Cross-referenced with transactions |
| Zitronensäure 70% | SIG-48-LHY-R0O8 | unverified | Historical match confirmed |
| continental processing Group | Global Rohstoffe AG | auto_generated | Historical match confirmed |
| Casein | Isoglucose | auto_generated | Verified via product specs |
| SO-IS-324 | SIG-59-EGO-78TM | unverified | Verified via product specs |
| Customs Duty GB 5% | customs duty in 20% | unverified | Historical match confirmed |
| prism chemicals | Baltic Industrien PLC | unverified | Cross-referenced with transactions |
| Glucose Syrup 99.5% Grade B | sodium benzoate 50% | auto_generated | Cross-referenced with transactions |
| nexus distribution Corp. | PR-PA-643 | pending_review | Confirmed by domain expert |
| sodium benzoate | Traubenzucker 99.5% | pending_review | Verified via product specs |
| DE-ST-712 | Soy Isolate 50% Grade B | unverified | Confirmed by domain expert |
| vat reduced nl 25% | Excise NL 15% | unverified | Historical match confirmed |
| SU-OI-GR-A-704 | Lactic Acid Technical | pending_review | Historical match confirmed |
| Vanguard Distribution | VE-EN-845 Group | auto_generated | Cross-referenced with transactions |
| GL-SY-533 | Calcium Carbonate Standard | pending_review | Auto-mapped, validated |
| SO-IS-PR-309 | SIG-43-GRJ-P3HT | unverified | Auto-mapped, validated |
| FR-PH-GR-146 | SIG-20-XSP-FVHF | pending_review | Auto-mapped, validated |
| Soy Isolate 50% Food Grade | Soja Isolate Premiumqualität | auto_generated | Cross-referenced with transactions |
| premier partners Group | PR-CO-156 PLC | unverified | Confirmed by domain expert |
| Soy Isolate 50% Grade B | SIG-36-ZWC-F2K1 | unverified | Auto-mapped, validated |
| Global Enterprise NV | Elite Werkstoffe | unverified | Cross-referenced with transactions |
| Soja Isolate Premiumqualität | Calcium Carbonate 70% Premium | auto_generated | Auto-mapped, validated |
| Global Ingredients NV | pacific industries Ltd. | unverified | Historical match confirmed |
| Atlas Materials | HO-LO-948 | pending_review | Historical match confirmed |
| palm oil | SIG-13-IPI-71PJ | unverified | Verified via product specs |
| PR-SU-CO-333 | zenith supply | auto_generated | Auto-mapped, validated |
| Meridian Versorgung | zenith industries | unverified | Historical match confirmed |
| Ascorbic Acid 98% Qualitätsstufe II | Sorbic Acid 98% | unverified | Historical match confirmed |
| Isoglucose 50% Qualitätsstufe I | soy isolate 99.5% | unverified | Cross-referenced with transactions |
| DE-FO-GR-588 | Soy Isolate | pending_review | Historical match confirmed |
| Fructose | SO-BE-ST-871 | auto_generated | Verified via product specs |
| Coconut Oil 70% | Wheat Gluten | unverified | Auto-mapped, validated |
| Lactic Acid Technical | Ascorbic Acid Standardqualität | unverified | Historical match confirmed |
| Fructose Technical | SIG-53-AHT-MGFX | auto_generated | Cross-referenced with transactions |
| SIG-92-VAB-1JHU | AS-AC-782 | auto_generated | Confirmed by domain expert |
| Weizenklebereiweiß | Dextrose 25% Technical | unverified | Auto-mapped, validated |
| premier solutions Corp. | Quantum Enterprise NV | unverified | Confirmed by domain expert |
| SIG-41-OMW-SN1T | Ascorbic Acid Lebensmittelrein | auto_generated | Cross-referenced with transactions |
| VA-RE-C-10-242 | vat reduced gb 19% | unverified | Historical match confirmed |
| Dextrose | lactic acid tech grade | unverified | Confirmed by domain expert |
| PO-SO-70-GR-A-581 | dextrose premium | auto_generated | Auto-mapped, validated |
| palm oil | Zitronensäure 70% | auto_generated | Cross-referenced with transactions |
| SIG-40-PLP-7A3U | SO-BE-50-TE-276 | unverified | Cross-referenced with transactions |
| SIG-86-VCP-SVOL | CA-CA-50-260 | auto_generated | Cross-referenced with transactions |
| Meridian Logistik | Pinnacle Sourcing | pending_review | Confirmed by domain expert |
| Soy Isolate | Pea Protein 70% Lebensmittelrein | auto_generated | Historical match confirmed |
| SIG-71-VGV-8K52 | sorbic acid premium | auto_generated | Verified via product specs |
| sorbic acid premium | SIG-60-PEY-H3GM | pending_review | Auto-mapped, validated |
| atlas supply | Meridian Ingredients GmbH | unverified | Auto-mapped, validated |
| ST-SU-323 Group | Core Rohstoffe | unverified | Confirmed by domain expert |
| Coconut Oil 99.5% Pharma Grade | CI-AC-99.5-674 | auto_generated | Verified via product specs |
| Prime Logistik | SIG-46-VTQ-P108 | pending_review | Historical match confirmed |
| Potassium Sorbate 50% Food Grade | dextrin | pending_review | Verified via product specs |
| SIG-37-HHT-38YO | Traubenzucker 99.5% | unverified | Cross-referenced with transactions |
| GL-SY-99.5-GR-B-358 | wheat gluten | pending_review | Verified via product specs |
| Rapsöl 25% Lebensmittelrein | SIG-15-PFO-2W85 | unverified | Historical match confirmed |
| SIG-86-AKS-BEQE | AS-AC-FO-GR-835 | unverified | Confirmed by domain expert |
| SIG-88-KUG-5ITD | maltodextrin de20 | pending_review | Cross-referenced with transactions |
| Calcium Carbonate 50% | SIG-24-NPE-GDMB | pending_review | Verified via product specs |
| SIG-39-BAT-DD7R | Zitronensäure 70% | auto_generated | Cross-referenced with transactions |
| Isoglucose | CI-AC-488 | pending_review | Cross-referenced with transactions |
| AT-SO-915 | nordic supply | unverified | Verified via product specs |
| PI-DI-543 Ltd. | Elite Handel PLC | unverified | Historical match confirmed |
| Sodium Chloride 25% Premium | SIG-30-LJO-TN4Y | auto_generated | Historical match confirmed |
| SIG-24-NPE-GDMB | isoglucose 25% | pending_review | Cross-referenced with transactions |
| SIG-58-DDZ-4JKE International | Core Chemicals Holdings | pending_review | Auto-mapped, validated |
| Fructose | PE-PR-251 | auto_generated | Verified via product specs |
| citric acid 99.5% | MA-DE-799 | auto_generated | Cross-referenced with transactions |
| SIG-66-UEK-CKJ1 | Quantum Logistik | pending_review | Historical match confirmed |
| SIG-65-MYR-QISO | Atlas Sourcing | auto_generated | Confirmed by domain expert |
| SIG-12-RDG-0JI1 | Fructose | pending_review | Cross-referenced with transactions |
| SIG-35-IQA-J92D | GL-SU-CO-255 | unverified | Confirmed by domain expert |
| Apex Logistik | vanguard logistics | pending_review | Historical match confirmed |
| Horizon Sourcing | Catalyst Logistik | pending_review | Cross-referenced with transactions |
| Stratos Sourcing | Baltic Supply Co. | unverified | Cross-referenced with transactions |
| SIG-87-SQR-587P | Withholding NL 10% | pending_review | Verified via product specs |
| sunflower oil premium | SIG-39-JMB-X1VA | auto_generated | Cross-referenced with transactions |
| PR-IN-695 Holdings | Pinnacle Ingredients AG | pending_review | Auto-mapped, validated |
| Catalyst Versorgung International | pinnacle industries SAS | unverified | Verified via product specs |
| VA-ST-I-20-301 | Vat Reduced CN 21% | auto_generated | Auto-mapped, validated |
| Quantum Ingredients | Nexus Supply Group | auto_generated | Cross-referenced with transactions |
| palm oil 98% | SIG-46-SVJ-5IZO | unverified | Confirmed by domain expert |
| AS-AC-PH-GR-192 | dextrose 70% premium | pending_review | Verified via product specs |
| Dextrin Pharma Grade | SIG-86-VGU-A4FE | pending_review | Verified via product specs |
| ST-PR-265 Corp. | SIG-97-TPD-0NJR LLC | unverified | Verified via product specs |
| Atlantic Partners | nexus distribution AG | auto_generated | Auto-mapped, validated |
| Baltic Versorgung | SIG-99-CEZ-35MR | pending_review | Confirmed by domain expert |
| SIG-81-SBE-HL1C | casein | pending_review | Auto-mapped, validated |
| GL-SY-70-655 | Zitronensäure 70% | auto_generated | Auto-mapped, validated |
| Pea Protein Premiumqualität | RA-OI-98-117 | unverified | Historical match confirmed |
| Natriumbenzoat | SIG-63-YJW-AP00 | unverified | Auto-mapped, validated |
| PR-SU-CO-920 | Core Sourcing | auto_generated | Confirmed by domain expert |
| Maltodextrin DE30 Standard | RE-ST-GR-B-805 | unverified | Confirmed by domain expert |
| withholding fr 5% | SIG-68-WEI-HOKG | unverified | Cross-referenced with transactions |
| PA-SU-CO-454 | meridian materials | auto_generated | Historical match confirmed |
| Maltodextrin-Pulver DE10 | PE-PR-GR-B-793 | unverified | Cross-referenced with transactions |
| SIG-56-ZQV-YINP SA | Pinnacle Supply International | pending_review | Cross-referenced with transactions |
| ascorbic acid food grade | Ascorbic Acid | unverified | Cross-referenced with transactions |
| Vanguard Vertrieb | SIG-98-WXH-VOMX | unverified | Confirmed by domain expert |
| stellar distribution Corp. | Meridian Versorgung | unverified | Cross-referenced with transactions |
| palm oil 50% premium | Lactic Acid 98% | auto_generated | Auto-mapped, validated |
| Stellar Logistik | SIG-43-TPO-RSBY | pending_review | Cross-referenced with transactions |
| Sodium Chloride 98% | Coconut Oil 25% Lebensmittelrein | unverified | Cross-referenced with transactions |
| SIG-58-FIB-X69X | SO-BE-GR-B-914 | auto_generated | Confirmed by domain expert |
| Sorbinsäure Qualitätsstufe I | SIG-45-PNR-H9Q3 | pending_review | Confirmed by domain expert |
| PR-SU-CO-805 | Quantum Sourcing | pending_review | Auto-mapped, validated |
| Resistant Starch Premium | Sorbinsäure 50% Standardqualität | unverified | Verified via product specs |
| Fructose 99.5% Technical | Rapsöl Qualitätsstufe I | auto_generated | Confirmed by domain expert |
| Pacific Materials | Premier Werkstoffe | pending_review | Verified via product specs |
| Vanguard Logistik | SIG-66-UEK-CKJ1 | auto_generated | Auto-mapped, validated |
| SIG-64-IEU-FRGN | Coconut Oil 50% Pharmazeutisch rein | auto_generated | Auto-mapped, validated |
| Calcium Carbonate 50% Grade B | PO-SO-50-TE-282 | unverified | Cross-referenced with transactions |
| prism chemicals GmbH | Atlantic Manufacturing International | auto_generated | Auto-mapped, validated |
| BA-SO-835 Corp. | Baltic Verarbeitung Group | auto_generated | Confirmed by domain expert |
| Calcium Carbonate 99.5% | wheat gluten 98% premium | pending_review | Verified via product specs |
| SIG-69-TRZ-SFLQ | Customs Duty BR 20% | unverified | Historical match confirmed |
| SO-BE-98-410 | Natriumbenzoat 99.5% | pending_review | Cross-referenced with transactions |
| SIG-82-ZPY-WR2F | IS-50-GR-A-791 | unverified | Auto-mapped, validated |
| Vat Reduced IN 20% | EX-U-20-144 | auto_generated | Confirmed by domain expert |
| SIG-30-RXC-HFDI | Sodium Chloride | unverified | Cross-referenced with transactions |
| Coconut Oil | Isoglucose | pending_review | Cross-referenced with transactions |
| Excise CN 20% | VA-RE-B-21-369 | auto_generated | Verified via product specs |
| global materials | Meridian Supply Co. | auto_generated | Confirmed by domain expert |
| RE-ST-50-232 | Coconut Oil 25% Food Grade | auto_generated | Historical match confirmed |
| SIG-17-IQV-FES7 | Soja Isolate 50% Premiumqualität | auto_generated | Cross-referenced with transactions |
| meridian solutions GmbH | PR-SO-284 Group | unverified | Historical match confirmed |
| SIG-29-CYR-T4UF | ascorbic acid standard | unverified | Confirmed by domain expert |
| sodium chloride 70% standard | SIG-16-JKI-B4JG | pending_review | Historical match confirmed |
| PA-OI-98-587 | ascorbic acid | unverified | Verified via product specs |
| SIG-20-RSZ-19RE | prism logistics | auto_generated | Cross-referenced with transactions |
| PR-CO-481 International | SIG-59-FNZ-ZVBE Ltd. | auto_generated | Auto-mapped, validated |
| Fructose Standardqualität | Palm Oil 70% Technical | pending_review | Verified via product specs |
| global logistics | Core Ingredients | unverified | Cross-referenced with transactions |
| Ascorbic Acid Technische Qualität | Fructose | auto_generated | Verified via product specs |
| Potassium Sorbate 50% Technical | RE-ST-GR-B-598 | pending_review | Historical match confirmed |
| SIG-72-JEH-P5K7 | Traubenzucker 25% | auto_generated | Auto-mapped, validated |
| vat standard nl 5% | VA-RE-B-10-727 | unverified | Cross-referenced with transactions |
| Citric Acid 70% Grade B | Sorbinsäure 50% | unverified | Verified via product specs |
| DE-70-769 | Natriumchlorid 98% | pending_review | Verified via product specs |
| prime commodities | Horizon Ingredients BV | auto_generated | Verified via product specs |
| SO-CH-TE-223 | Isoglucose 70% Lebensmittelrein | pending_review | Verified via product specs |
| AT-LO-592 | Baltic Sourcing | unverified | Cross-referenced with transactions |
| Premier Materials | Pacific Versorgung GmbH | pending_review | Confirmed by domain expert |
| Rapsöl 98% Standardqualität | SIG-37-WYK-X3LH | pending_review | Confirmed by domain expert |
| Nexus Sourcing | VA-MA-951 | pending_review | Cross-referenced with transactions |
| pea protein 99.5% | Maltodextrin DE20 | unverified | Historical match confirmed |
| Sorbinsäure Qualitätsstufe II | SIG-35-TKX-8TRE | unverified | Verified via product specs |
| Elite Chemicals AG | atlas materials | pending_review | Historical match confirmed |
| PE-PR-70-PR-387 | Palm Oil 98% | auto_generated | Confirmed by domain expert |
| nexus distribution AG | SIG-48-YBV-ZD0Y | pending_review | Cross-referenced with transactions |
| SIG-82-VDF-0XQT | Calcium Carbonate Grade B | pending_review | Historical match confirmed |
| Customs Duty US 20% | WI-F-10-935 | auto_generated | Confirmed by domain expert |
| Global Werkstoffe | atlantic materials | unverified | Confirmed by domain expert |
| CO-IN-915 KG | SIG-42-SPP-A6C6 | auto_generated | Confirmed by domain expert |
| Nordic Manufacturing Holdings | SIG-68-SJS-K3N3 | auto_generated | Cross-referenced with transactions |
| Citric Acid Pharma Grade | Palmfett 50% | pending_review | Auto-mapped, validated |
| vanguard logistics | HO-MA-349 | pending_review | Confirmed by domain expert |
| Withholding GB 5% | excise in 21% | auto_generated | Cross-referenced with transactions |
| AT-DI-544 | SIG-77-TQY-IC8H Holdings | auto_generated | Historical match confirmed |
| SIG-58-FIB-X69X | PA-OI-50-497 | pending_review | Historical match confirmed |
| SIG-93-MGK-61BG | resistant starch 70% food grade | pending_review | Cross-referenced with transactions |
| SIG-18-WKH-NATG | Kaliumsorbat | unverified | Confirmed by domain expert |
| PE-PR-98-GR-B-195 | Pea Protein 70% Lebensmittelrein | pending_review | Verified via product specs |
| CO-PA-308 | atlantic ingredients | unverified | Verified via product specs |
| SIG-28-STQ-YUPS | EL-LO-372 | auto_generated | Cross-referenced with transactions |
| sodium chloride premium | Cyclodextrin Pharma Grade | unverified | Cross-referenced with transactions |
| SIG-38-WKO-LWQT | continental supply | unverified | Confirmed by domain expert |
| Vertex Logistik | Prism Sourcing | pending_review | Historical match confirmed |
| DE-GR-B-244 | Sodium Chloride | pending_review | Auto-mapped, validated |
| CI-AC-50-PH-GR-863 | Fructose 25% | auto_generated | Cross-referenced with transactions |
| nexus sourcing | CA-MA-370 | pending_review | Cross-referenced with transactions |
| cyclodextrin | SIG-11-RGJ-D3IR | unverified | Auto-mapped, validated |
| ME-DI-790 Group | Premier Partners | unverified | Cross-referenced with transactions |
| VA-ST-G-19-945 | Vat Standardqualität DE 21% | pending_review | Auto-mapped, validated |
| SIG-48-KTU-I0WF | VA-RE-G-19-672 | auto_generated | Verified via product specs |
| Sodium Chloride | Maltodextrin-Pulver DE5 Qualitätsstufe I | unverified | Historical match confirmed |
| quantum sourcing | SIG-70-ROA-COR7 | pending_review | Historical match confirmed |
| dextrin standard | RA-OI-98-679 | unverified | Confirmed by domain expert |
| SIG-71-VGV-8K52 | Palmfett | unverified | Cross-referenced with transactions |
| SIG-20-FYS-JNIL | Meridian Sourcing | unverified | Verified via product specs |
| SIG-79-DVU-H9H4 | Palm Oil Pharma Grade | unverified | Confirmed by domain expert |
| SIG-50-ABM-7VSK | CI-AC-215 | unverified | Cross-referenced with transactions |
| Nexus Chemicals Group | PR-MA-448 | pending_review | Verified via product specs |
| Isoglucose | sunflower oil 98% | unverified | Historical match confirmed |
| Atlas Logistics International | Continental Manufacturing | pending_review | Historical match confirmed |
| pea protein | SO-AC-PH-GR-620 | unverified | Confirmed by domain expert |
| Ascorbic Acid 70% | palm oil 50% premium | unverified | Confirmed by domain expert |
| SIG-42-FYL-6VKE | Vanguard Versorgung GmbH | auto_generated | Auto-mapped, validated |
| SO-BE-GR-A-760 | SIG-13-CZK-ACKX | pending_review | Auto-mapped, validated |
| SIG-94-TOI-OFNK | Casein Standard | pending_review | Verified via product specs |
| SIG-48-LUB-IGA7 | Baltic Supply Co. | pending_review | Auto-mapped, validated |
| Resistant Starch 99.5% | Coconut Oil 70% | unverified | Cross-referenced with transactions |
| pacific enterprise | SIG-68-BSB-VSIA | unverified | Cross-referenced with transactions |
| Catalyst Ingredients International | GL-CH-617 SARL | unverified | Historical match confirmed |
| Fructose Grade B | Palmfett Lebensmittelrein | pending_review | Cross-referenced with transactions |
| Sonnenblumenöl Qualitätsstufe II | SIG-52-CHY-4N5P | pending_review | Historical match confirmed |
| Dextrin Pharmazeutisch rein | Potassium Sorbate Technical | auto_generated | Historical match confirmed |
| Vat Reduced BR 7% | EX-I-15-456 | unverified | Cross-referenced with transactions |
| Global Rohstoffe AG | CO-MA-371 | unverified | Auto-mapped, validated |
| catalyst supply Holdings | NE-EN-400 Group | unverified | Historical match confirmed |
| SO-CH-GR-B-273 | Sodium Benzoate | unverified | Auto-mapped, validated |
| PR-IN-608 BV | prism materials | unverified | Cross-referenced with transactions |
| SIG-57-YOY-F7N2 | Cyclodextrin Qualitätsstufe I | unverified | Historical match confirmed |
| RA-OI-50-PH-GR-538 | Traubenzucker 50% Qualitätsstufe II | pending_review | Auto-mapped, validated |
| SIG-92-FQX-S1BC | pinnacle ingredients GmbH | unverified | Historical match confirmed |
| Withholding IN 10% | excise nl 20% | auto_generated | Historical match confirmed |
| vat standard br 0% | SIG-31-BWX-FDET | auto_generated | Auto-mapped, validated |
| PR-LO-745 | Baltic Sourcing | auto_generated | Confirmed by domain expert |
| Vat Standardqualität FR 15% | VA-ST-F-25-272 | pending_review | Confirmed by domain expert |
| Pinnacle Werkstoffe | SIG-27-LAH-JE6F | unverified | Verified via product specs |
| Rapeseed Oil 99.5% | Resistente Stärke Qualitätsstufe II | auto_generated | Confirmed by domain expert |
| BA-PA-973 | Pinnacle Chemicals Ltd. | auto_generated | Historical match confirmed |
| Meridian Sourcing | catalyst supply | auto_generated | Auto-mapped, validated |
| NO-MA-994 | Catalyst Rohstoffe NV | auto_generated | Cross-referenced with transactions |
| FR-99.5-FO-GR-963 | rapeseed oil standard | auto_generated | Historical match confirmed |
| Palm Oil 98% | SIG-84-VYG-QI55 | pending_review | Auto-mapped, validated |
| Nordic Industrien PLC | SIG-94-MUO-QFTQ | auto_generated | Historical match confirmed |
| Central Versorgung GmbH | Catalyst Materials | pending_review | Historical match confirmed |
| SIG-52-EML-H8JV | Dextrin Qualitätsstufe II | unverified | Cross-referenced with transactions |
| PI-CH-610 Ltd. | Elite Solutions | auto_generated | Historical match confirmed |
| resistant starch premium | SO-CH-70-GR-B-821 | unverified | Verified via product specs |
| atlas logistics | SIG-90-BVN-BJY6 | unverified | Verified via product specs |
| Vat Standard US 5% | Vat Reduced CN 10% | unverified | Confirmed by domain expert |
| Customs Duty NL 15% | Vat Standardqualität FR 25% | auto_generated | Historical match confirmed |
| Elite Chemicals AG | Pinnacle Chemicals SAS | pending_review | Verified via product specs |
| Prime Materials | vanguard supply | unverified | Verified via product specs |
| wheat gluten 98% | Pea Protein 70% Technische Qualität | auto_generated | Cross-referenced with transactions |
| SIG-40-OEJ-4XCR | WH-GL-GR-B-926 | pending_review | Auto-mapped, validated |
| SIG-12-BIH-AKGD | glucose syrup | unverified | Cross-referenced with transactions |
| SIG-83-BMJ-HHIG | Soja Isolate 50% Qualitätsstufe II | pending_review | Auto-mapped, validated |
| Fructose Grade A | palm oil 99.5% | auto_generated | Historical match confirmed |
| SIG-62-BTJ-PQV9 | CI-AC-98-939 | pending_review | Historical match confirmed |
| Dextrose | Weizenklebereiweiß | auto_generated | Verified via product specs |
| FR-99.5-PH-GR-378 | Casein 25% Pharma Grade | pending_review | Cross-referenced with transactions |
| SIG-79-GUR-O5DB NV | prism chemicals | unverified | Historical match confirmed |
| SIG-84-DSO-4S47 | Sorbinsäure Qualitätsstufe II | auto_generated | Confirmed by domain expert |
| SIG-70-IKQ-7KBN | Coconut Oil | pending_review | Cross-referenced with transactions |
| SIG-86-VCP-SVOL | sodium benzoate | pending_review | Cross-referenced with transactions |
| Lactic Acid 98% | Wheat Gluten Grade A | auto_generated | Historical match confirmed |
| fructose 99.5% food grade | Dextrin Food Grade | pending_review | Historical match confirmed |
| AP-SO-576 | Pacific Sourcing | pending_review | Historical match confirmed |
| SIG-68-VLD-BDX3 International | catalyst ingredients | unverified | Verified via product specs |
| vertex enterprise Group | SIG-98-CTS-XPY5 | pending_review | Verified via product specs |
| SIG-99-CEZ-35MR | Baltic Ingredients SA | auto_generated | Cross-referenced with transactions |
| calcium carbonate | SIG-97-OGU-PBXC | unverified | Verified via product specs |
| SIG-79-SPO-WT80 | Dextrin Qualitätsstufe II | pending_review | Confirmed by domain expert |
| Pacific Industrien | zenith industries | pending_review | Historical match confirmed |
| Stratos Sourcing | global supply | unverified | Historical match confirmed |
| Stellar Logistik | EL-MA-832 | unverified | Verified via product specs |
| Pea Protein 25% | sunflower oil 98% | pending_review | Cross-referenced with transactions |
| Zitronensäure | casein | unverified | Auto-mapped, validated |
| Sonnenblumenöl | SIG-60-IRZ-OTKZ | pending_review | Confirmed by domain expert |
| Glucose Syrup | Traubenzucker 50% Qualitätsstufe II | unverified | Confirmed by domain expert |
| palm oil | Sonnenblumenöl 70% | auto_generated | Historical match confirmed |
| Elite Logistik | premier supply PLC | pending_review | Historical match confirmed |
| DE-70-GR-A-741 | dextrin 50% | auto_generated | Historical match confirmed |
| SIG-47-LPF-7QXJ | cyclodextrin food grade | auto_generated | Verified via product specs |
| Calcium Carbonate 50% Grade A | citric acid 25% tech grade | unverified | Cross-referenced with transactions |
| nexus logistics | Horizon Sourcing | auto_generated | Confirmed by domain expert |
| Atlantic Ingredients | Elite Vertrieb International | unverified | Confirmed by domain expert |
| SIG-20-ISN-0EWL | sorbic acid premium | auto_generated | Historical match confirmed |
| SIG-76-QBY-ERKM | pea protein | auto_generated | Historical match confirmed |
| SO-BE-PH-GR-831 | resistant starch | unverified | Verified via product specs |
| Customs Duty CN 25% | SIG-65-QDW-KJG8 | pending_review | Auto-mapped, validated |
| atlantic commodities | Apex Verarbeitung | auto_generated | Confirmed by domain expert |
| Weizenklebereiweiß | DE-GR-B-157 | auto_generated | Historical match confirmed |
| SIG-51-ZHS-W8WR International | Nordic Ingredients | pending_review | Historical match confirmed |
| SIG-90-YRJ-4LRE | Elite Sourcing | pending_review | Confirmed by domain expert |
| CI-AC-50-PH-GR-863 | SIG-98-XJT-L879 | unverified | Historical match confirmed |
| AS-AC-782 | Ascorbic Acid 99.5% Premiumqualität | auto_generated | Auto-mapped, validated |
| fructose 70% | RA-OI-98-679 | pending_review | Cross-referenced with transactions |
| Global Ingredients BV | SIG-71-RDD-KOLF SAS | pending_review | Confirmed by domain expert |
| CI-AC-50-PH-GR-863 | lactic acid tech grade | pending_review | Confirmed by domain expert |
| Traubenzucker 70% | SIG-40-OEJ-4XCR | unverified | Verified via product specs |
| SIG-37-JLF-9KYP | DE-ST-712 | unverified | Historical match confirmed |
| nordic ingredients SARL | Global Verarbeitung Group | unverified | Auto-mapped, validated |
| soy isolate 99.5% | SIG-61-IQH-EKWH | pending_review | Auto-mapped, validated |
| CA-884 | sodium benzoate 98% standard | unverified | Historical match confirmed |
| Horizon Ingredients BV | quantum commodities Holdings | pending_review | Historical match confirmed |
| Sodium Benzoate Pharma Grade | SIG-88-KUG-5ITD | auto_generated | Auto-mapped, validated |
| Horizon Logistics | Stellar Versorgung GmbH | pending_review | Cross-referenced with transactions |
| Meridian Werkstoffe Corp. | zenith trading AG | auto_generated | Confirmed by domain expert |
| SIG-47-HPA-L2FX | sodium benzoate | unverified | Cross-referenced with transactions |
| Pacific Chemicals GmbH | Nexus Chemicals Group | pending_review | Confirmed by domain expert |
| Fructose 25% | sorbic acid premium | pending_review | Cross-referenced with transactions |
| Vat Reduced BR 15% | withholding nl 21% | auto_generated | Cross-referenced with transactions |
| Sonnenblumenöl Qualitätsstufe II | palm oil | auto_generated | Auto-mapped, validated |
| wheat gluten pharma grade | SIG-46-SVJ-5IZO | pending_review | Confirmed by domain expert |
| nexus distribution Corp. | ZE-TR-467 AG | unverified | Verified via product specs |
| potassium sorbate 98% | SIG-92-ZTO-VZGU | pending_review | Historical match confirmed |
| Vertex Chemicals Holdings | central enterprise PLC | pending_review | Confirmed by domain expert |
| Prism Ingredients | SIG-83-BZN-2A0N KG | auto_generated | Historical match confirmed |
| VA-DI-105 | SIG-61-YSE-8JLK SARL | auto_generated | Historical match confirmed |
| soy isolate food grade | SO-BE-113 | pending_review | Verified via product specs |
| premier logistics Ltd. | Horizon Industries | pending_review | Historical match confirmed |
| SIG-25-EZW-5GYT | maltodextrin de20 | auto_generated | Cross-referenced with transactions |
| CO-OI-FO-GR-162 | SIG-47-AWI-4RQV | unverified | Auto-mapped, validated |
| AS-AC-99.5-619 | Cyclodextrin | unverified | Auto-mapped, validated |
| SIG-83-MZM-HGMN GmbH | AT-IN-956 PLC | auto_generated | Auto-mapped, validated |
| AS-AC-165 | palm oil 70% premium | unverified | Cross-referenced with transactions |
| sunflower oil 50% pharma grade | Resistant Starch Grade B | pending_review | Confirmed by domain expert |
| SIG-85-FIY-2QW4 | sunflower oil 98% premium | auto_generated | Verified via product specs |
| withholding de 15% | SIG-74-SAC-3HZG | pending_review | Confirmed by domain expert |
| SO-CH-99.5-618 | SIG-31-ZKD-VVIA | pending_review | Auto-mapped, validated |
| Sorbinsäure 98% | CA-CA-99.5-291 | unverified | Cross-referenced with transactions |
| vat standard us 15% | SIG-95-LOJ-S1L2 | auto_generated | Historical match confirmed |
| Global Trading Ltd. | Nordic Vertrieb | auto_generated | Auto-mapped, validated |
| Apex Solutions International | SIG-30-SZZ-Z75G GmbH | unverified | Cross-referenced with transactions |
| Pea Protein 25% Pharmazeutisch rein | AS-AC-130 | auto_generated | Verified via product specs |
| Continental Partners KG | PA-DI-201 NV | auto_generated | Verified via product specs |
| PO-SO-50-TE-282 | Zitronensäure | pending_review | Verified via product specs |
| Dextrose | Weizenklebereiweiß 99.5% Technische Qualität | auto_generated | Historical match confirmed |
| palm oil food grade | SIG-82-VDF-0XQT | pending_review | Historical match confirmed |
| Vat Reduced BR 10% | SIG-72-CRV-0OZ3 | auto_generated | Cross-referenced with transactions |
| Natriumbenzoat 50% | SIG-30-MPO-SJEV | pending_review | Auto-mapped, validated |
| Rapeseed Oil 70% Grade B | CO-OI-50-PH-GR-568 | auto_generated | Verified via product specs |
| Sorbic Acid 70% | SIG-98-JEQ-77GG | auto_generated | Verified via product specs |
| Rapeseed Oil Grade A | soy isolate 99.5% | auto_generated | Confirmed by domain expert |
| SIG-30-NQN-ZENP | Prism Chemicals PLC | pending_review | Verified via product specs |
| Catalyst Rohstoffe NV | QU-PR-732 SA | auto_generated | Cross-referenced with transactions |
| Dextrin Qualitätsstufe II | SIG-13-FTX-P5F3 | pending_review | Confirmed by domain expert |
| SIG-20-BPG-W8VL | Sorbic Acid 50% Standard | unverified | Verified via product specs |
| Citric Acid | RE-ST-ST-711 | unverified | Cross-referenced with transactions |
| Pinnacle Handel Inc. | continental materials Holdings | auto_generated | Cross-referenced with transactions |
| Vat Reduced NL 21% | Customs Duty BR 20% | auto_generated | Verified via product specs |
| VE-CH-445 Group | Vertex Ingredients | auto_generated | Verified via product specs |
| SIG-31-IKO-T2D8 | Isoglucose 25% Lebensmittelrein | pending_review | Auto-mapped, validated |
| potassium sorbate | SIG-57-YOY-F7N2 | pending_review | Historical match confirmed |
| Dextrose Food Grade | sorbic acid | auto_generated | Cross-referenced with transactions |
| Pea Protein Pharma Grade | RE-ST-25-TE-177 | auto_generated | Verified via product specs |
| Cyclodextrin Standard | LA-AC-50-PR-288 | auto_generated | Confirmed by domain expert |
| vanguard industries Inc. | Quantum Manufacturing KG | pending_review | Confirmed by domain expert |
| CU-DU-F-20-900 | vat reduced gb 15% | pending_review | Auto-mapped, validated |
| isoglucose | SIG-16-GRX-X3AK | auto_generated | Confirmed by domain expert |
| Kasein | dextrin 50% | unverified | Confirmed by domain expert |
| SIG-14-MDA-Y0XA | Coconut Oil 99.5% Pharma Grade | unverified | Cross-referenced with transactions |
| SU-OI-765 | citric acid premium | pending_review | Confirmed by domain expert |
| SIG-60-QPM-2TRI | Sunflower Oil 70% | unverified | Cross-referenced with transactions |
| EX-F-25-579 | SIG-89-EJE-7I11 | unverified | Cross-referenced with transactions |
| EL-LO-372 | Apex Sourcing | pending_review | Cross-referenced with transactions |
| NO-SU-CO-498 | pacific materials | pending_review | Auto-mapped, validated |
| Natriumbenzoat | potassium sorbate | unverified | Historical match confirmed |
| Premier Rohstoffe Holdings | AT-MA-295 GmbH | unverified | Verified via product specs |
| Palmfett | FR-124 | pending_review | Cross-referenced with transactions |
| CI-AC-GR-A-280 | fructose pharma grade | auto_generated | Confirmed by domain expert |
| withholding fr 5% | VA-ST-U-20-479 | unverified | Auto-mapped, validated |
| Atlas Ingredients Ltd. | Nordic Ingredients SA | pending_review | Cross-referenced with transactions |
| vat standard de 7% | Customs Duty GB 0% | auto_generated | Verified via product specs |
| Traubenzucker 98% Qualitätsstufe I | SIG-99-VAH-2H31 | unverified | Verified via product specs |
| SIG-24-CXH-R2TY | SO-BE-99.5-TE-213 | unverified | Verified via product specs |
| Zitronensäure | Dextrin 70% Pharma Grade | pending_review | Auto-mapped, validated |
| core distribution BV | Atlantic Industries AG | pending_review | Cross-referenced with transactions |
| Sunflower Oil | glucose syrup 98% standard | auto_generated | Cross-referenced with transactions |
| nexus distribution Corp. | Central Rohstoffe PLC | unverified | Verified via product specs |
| Catalyst Logistics SA | CO-IN-363 AG | unverified | Cross-referenced with transactions |
| ST-SU-CO-731 | SIG-74-ZGY-ZA9S | auto_generated | Verified via product specs |
| Prism Sourcing | Elite Materials | auto_generated | Cross-referenced with transactions |
| SIG-24-CXH-R2TY | Ascorbic Acid 99.5% Premium | auto_generated | Verified via product specs |
| Calcium Carbonate 98% | potassium sorbate standard | unverified | Historical match confirmed |
| Vat Reduced IN 10% | SIG-98-NDY-OCEW | unverified | Cross-referenced with transactions |
| Stratos Werkstoffe | AP-SU-CO-787 | pending_review | Auto-mapped, validated |
| vanguard materials | Horizon Versorgung GmbH | unverified | Cross-referenced with transactions |
| NO-PA-492 LLC | SIG-46-YOE-MYAX SA | auto_generated | Verified via product specs |
| Nexus Partners GmbH | Pacific Vertrieb Group | unverified | Confirmed by domain expert |
| Maltodextrin DE10 | GL-SY-98-749 | auto_generated | Historical match confirmed |
| SIG-36-RVG-E4FG | Baltic Sourcing | unverified | Auto-mapped, validated |
| Stellar Supply | stratos partners SA | unverified | Confirmed by domain expert |
| Sorbic Acid 50% Food Grade | SO-AC-99.5-338 | unverified | Confirmed by domain expert |
| apex supply | GL-SU-CO-255 | auto_generated | Confirmed by domain expert |
| potassium sorbate | SIG-69-INT-Z1YQ | unverified | Auto-mapped, validated |
| MA-DE-738 | Natriumchlorid 25% Premiumqualität | auto_generated | Verified via product specs |
| Vertex Distribution AG | Stratos Handel | auto_generated | Auto-mapped, validated |
| Weizenklebereiweiß | SU-OI-ST-194 | unverified | Auto-mapped, validated |
| Global Sourcing | core materials | pending_review | Auto-mapped, validated |
| dextrose food grade | Palmfett | auto_generated | Historical match confirmed |
| RE-ST-FO-GR-238 | SIG-85-STS-67D6 | unverified | Auto-mapped, validated |
| Apex Ingredients KG | SIG-39-CCW-1KX2 | unverified | Cross-referenced with transactions |
| SIG-73-KLZ-PDKU | Wheat Gluten 50% | auto_generated | Historical match confirmed |
| SIG-99-CTB-8OFG Group | Continental Ingredients | pending_review | Auto-mapped, validated |
| Vertex Ingredients Ltd. | Quantum Ingredients | auto_generated | Auto-mapped, validated |
| Fructose 99.5% Technical | resistant starch tech grade | auto_generated | Cross-referenced with transactions |
| Calcium Carbonate 98% Pharmazeutisch rein | SIG-61-KUY-VFFK | unverified | Cross-referenced with transactions |
| vertex industries NV | Meridian Enterprise | auto_generated | Confirmed by domain expert |
| Sunflower Oil Pharma Grade | potassium sorbate premium | pending_review | Auto-mapped, validated |
| coconut oil standard | Ascorbic Acid | pending_review | Cross-referenced with transactions |
| Palmfett 98% | isoglucose | unverified | Verified via product specs |
| CU-DU-B-15-379 | vat standard nl 19% | pending_review | Cross-referenced with transactions |
| SIG-34-JQN-ROWX | Pea Protein Grade A | unverified | Historical match confirmed |
| PE-PR-746 | resistant starch | auto_generated | Confirmed by domain expert |
| SU-OI-765 | SIG-18-LLP-8GUU | unverified | Auto-mapped, validated |
| glucose syrup food grade | SIG-72-IMA-8RAP | unverified | Auto-mapped, validated |
| fructose standard | Pea Protein Premiumqualität | pending_review | Verified via product specs |
| Coconut Oil 98% Technical | calcium carbonate 50% | unverified | Verified via product specs |
| SIG-36-BVE-5U7D | Citric Acid | pending_review | Verified via product specs |
| potassium sorbate premium | SO-BE-ST-871 | auto_generated | Cross-referenced with transactions |
| PO-SO-50-TE-282 | SIG-26-DML-NZS4 | pending_review | Confirmed by domain expert |
| DE-602 | Coconut Oil 25% Technical | auto_generated | Cross-referenced with transactions |
| SIG-78-LTE-H4VL | RE-ST-70-901 | auto_generated | Historical match confirmed |
| SIG-10-UIB-YQL1 | glucose syrup premium | pending_review | Auto-mapped, validated |
| Calcium Carbonate 70% Premiumqualität | SIG-55-CTS-U5X0 | auto_generated | Confirmed by domain expert |
| SIG-51-BUX-VLME Group | Nordic Manufacturing NV | unverified | Confirmed by domain expert |
| Quantum Processing Ltd. | NO-MA-529 | unverified | Confirmed by domain expert |
| PA-OI-GR-B-326 | Fructose Standardqualität | auto_generated | Confirmed by domain expert |
| SIG-44-HTV-P84J | Zitronensäure 70% | auto_generated | Auto-mapped, validated |
| ST-IN-505 SA | SIG-69-FIT-Y3OC International | pending_review | Historical match confirmed |
| sodium benzoate | SIG-61-XKV-ODPX | unverified | Historical match confirmed |
| SIG-12-QLD-RUJ3 Inc. | prism logistics BV | pending_review | Confirmed by domain expert |
| SIG-51-HUK-F1HG | VA-RE-F-21-230 | pending_review | Confirmed by domain expert |
| prism manufacturing Ltd. | Meridian Ingredients | pending_review | Cross-referenced with transactions |
| Resistente Stärke | casein | unverified | Historical match confirmed |
| Apex Handel International | PR-EN-764 Ltd. | unverified | Historical match confirmed |
| SIG-68-TVY-N4XJ | WH-GL-99.5-557 | unverified | Historical match confirmed |
| Soy Isolate 98% | PA-OI-25-GR-A-241 | pending_review | Historical match confirmed |
| Ascorbic Acid | wheat gluten 99.5% premium | unverified | Verified via product specs |
| Ascorbic Acid 70% | SIG-29-DTY-HFJL | auto_generated | Auto-mapped, validated |
| VE-LO-902 Group | SIG-58-DDZ-4JKE International | pending_review | Cross-referenced with transactions |
| Stratos Ingredients SARL | PR-CO-800 Corp. | unverified | Cross-referenced with transactions |
| Catalyst Werkstoffe | Premier Supply Co. | unverified | Cross-referenced with transactions |
| Resistant Starch Grade B | LA-AC-99.5-GR-B-756 | auto_generated | Auto-mapped, validated |
| SO-BE-667 | Citric Acid Food Grade | auto_generated | Auto-mapped, validated |
| soy isolate 98% | SIG-99-OQS-ADHF | unverified | Verified via product specs |
| Meridian Vertrieb International | Stellar Manufacturing Holdings | pending_review | Confirmed by domain expert |
| lactic acid | RE-ST-98-PH-GR-372 | pending_review | Historical match confirmed |
| SIG-73-LLJ-LNGI | Isoglucose 50% Lebensmittelrein | unverified | Verified via product specs |
| isoglucose 70% | PA-OI-50-497 | pending_review | Auto-mapped, validated |
| CA-CA-GR-B-162 | Ascorbic Acid 98% | unverified | Confirmed by domain expert |
| Sodium Chloride | CI-AC-ST-836 | pending_review | Confirmed by domain expert |
| Dextrin 50% | sorbic acid 70% | pending_review | Verified via product specs |
| WI-F-5-977 | SIG-89-HHQ-75TJ | pending_review | Verified via product specs |
| Excise BR 19% | vat reduced cn 15% | pending_review | Confirmed by domain expert |
| vertex materials | Vertex Werkstoffe | auto_generated | Cross-referenced with transactions |
| SIG-65-ONA-WQOF Corp. | Continental Manufacturing | auto_generated | Cross-referenced with transactions |
| prism materials | Premier Logistik | auto_generated | Verified via product specs |
| Wheat Gluten | Pea Protein 70% Technische Qualität | auto_generated | Verified via product specs |
| SIG-66-JGK-EM8M | Coconut Oil | unverified | Cross-referenced with transactions |
| Isoglucose Grade B | GL-SY-371 | unverified | Auto-mapped, validated |
| Apex Sourcing | Continental Logistics | unverified | Confirmed by domain expert |
| SIG-69-BWM-8WBG | Premier Chemicals | pending_review | Historical match confirmed |
| Resistant Starch Technical | Glukosesirup Syrup | unverified | Cross-referenced with transactions |
| Isoglucose 70% | Ascorbic Acid Lebensmittelrein | auto_generated | Verified via product specs |
| SIG-78-NWO-RO6D | DE-70-769 | pending_review | Cross-referenced with transactions |
| Atlantic Processing | prime partners Group | auto_generated | Confirmed by domain expert |
| Central Logistik Holdings | Stellar Supply | auto_generated | Cross-referenced with transactions |
| VA-ST-N-5-192 | Customs Duty CN 19% | auto_generated | Confirmed by domain expert |
| SIG-19-QLH-ILRZ | sodium benzoate 50% | unverified | Cross-referenced with transactions |
| SIG-43-MIT-DWCJ SA | AT-PR-985 International | unverified | Auto-mapped, validated |
| ST-PA-504 | SIG-93-ABB-76KE | pending_review | Verified via product specs |
| SIG-91-WVE-3ESP | Sorbinsäure 98% | pending_review | Historical match confirmed |
| pacific supply | Prism Materials | auto_generated | Verified via product specs |
| cyclodextrin 98% | SIG-54-LIP-WKBS | pending_review | Cross-referenced with transactions |
| SIG-74-LEZ-GZA2 AG | Core Manufacturing | auto_generated | Confirmed by domain expert |
| ST-LO-378 | SIG-94-ASN-E5J2 | unverified | Cross-referenced with transactions |
| CY-GR-A-208 | SIG-58-FIB-X69X | pending_review | Confirmed by domain expert |
| SIG-93-YGI-KLQ0 | CE-LO-198 Holdings | auto_generated | Historical match confirmed |
| SIG-55-EGS-MYD1 | Vat Standard DE 7% | unverified | Cross-referenced with transactions |
| nexus logistics | VE-SO-576 | unverified | Auto-mapped, validated |
| horizon materials | SIG-46-AAW-27BR | auto_generated | Confirmed by domain expert |
| Sodium Chloride 70% | Soja Isolate Premiumqualität | pending_review | Confirmed by domain expert |
| Soy Isolate 25% Standard | Isoglucose Qualitätsstufe II | auto_generated | Cross-referenced with transactions |
| soy isolate standard | Rapeseed Oil Technical | pending_review | Historical match confirmed |
| Lactic Acid 98% | wheat gluten 70% | pending_review | Auto-mapped, validated |
| Potassium Sorbate | SIG-41-LTG-3D5I | pending_review | Historical match confirmed |
| sodium benzoate premium | Cyclodextrin Standard | unverified | Verified via product specs |
| quantum processing International | Pinnacle Chemicals SAS | auto_generated | Confirmed by domain expert |
| SIG-60-RUC-CU6A | Global Rohstoffe AG | pending_review | Historical match confirmed |
| sorbic acid food grade | Sorbic Acid | pending_review | Auto-mapped, validated |
| CO-OI-50-147 | Potassium Sorbate Food Grade | unverified | Cross-referenced with transactions |
| Casein 98% Grade B | dextrin | unverified | Historical match confirmed |
| SIG-44-HTV-P84J | RE-ST-50-824 | auto_generated | Auto-mapped, validated |
| SIG-23-IEJ-V2T3 | sorbic acid 98% | pending_review | Historical match confirmed |
| Stellar Processing Holdings | PR-EN-764 Ltd. | pending_review | Cross-referenced with transactions |
| Baltic Manufacturing | ST-SU-125 SA | unverified | Auto-mapped, validated |
| zenith trading GmbH | Nexus Commodities International | auto_generated | Verified via product specs |
| SIG-47-SRN-QNYY | PA-OI-GR-B-326 | pending_review | Confirmed by domain expert |
| ST-TR-590 | central materials BV | auto_generated | Auto-mapped, validated |
| SIG-60-OHC-5EQB | Vertex Logistik | auto_generated | Historical match confirmed |
| VA-RE-C-10-444 | Customs Duty DE 20% | pending_review | Confirmed by domain expert |
| Fructose 99.5% | SIG-64-VUE-OGQ2 | pending_review | Auto-mapped, validated |
| Atlas Chemicals SARL | Catalyst Industries | pending_review | Verified via product specs |
| withholding fr 25% | Excise NL 0% | auto_generated | Auto-mapped, validated |
| SIG-83-ZHQ-A0CR | Customs Duty NL 15% | pending_review | Auto-mapped, validated |
| Lactic Acid | SIG-27-QBW-ROGA | pending_review | Confirmed by domain expert |
| Vat Standard NL 19% | SIG-41-SEX-2DFF | auto_generated | Historical match confirmed |
| RE-ST-GR-B-598 | Weizenklebereiweiß Qualitätsstufe II | pending_review | Historical match confirmed |
| SIG-15-YBX-K4SY | GL-MA-581 | pending_review | Cross-referenced with transactions |
| NO-MA-452 | prime ingredients NV | unverified | Historical match confirmed |
| Customs Duty IN 25% | customs duty nl 15% | unverified | Cross-referenced with transactions |
| ZE-MA-316 | stratos enterprise SARL | auto_generated | Verified via product specs |
| VA-ST-G-19-277 | Vat Reduced FR 0% | auto_generated | Verified via product specs |
| SIG-79-DVU-H9H4 | AS-AC-ST-243 | auto_generated | Cross-referenced with transactions |
| PO-SO-99.5-897 | Kasein 25% Pharmazeutisch rein | auto_generated | Historical match confirmed |
| SIG-19-TPS-MSKY | sodium benzoate standard | auto_generated | Historical match confirmed |
| SIG-12-JHE-FNCL | Stellar Werkstoffe | unverified | Verified via product specs |
| SIG-57-YNB-5KMT | sodium chloride 99.5% premium | auto_generated | Cross-referenced with transactions |
| SIG-20-XSP-FVHF | SO-IS-50-568 | auto_generated | Historical match confirmed |
| coconut oil | SIG-91-PEG-USI6 | unverified | Historical match confirmed |
| GL-SY-99.5-ST-205 | Palmfett | unverified | Confirmed by domain expert |
| MA-DE-585 | Casein Grade A | auto_generated | Verified via product specs |
| Apex Logistics | ME-LO-731 | auto_generated | Historical match confirmed |
| Cyclodextrin | SIG-22-XCC-QSNV | pending_review | Confirmed by domain expert |
| cyclodextrin pharma grade | Casein Standard | unverified | Confirmed by domain expert |
| SIG-56-ZVH-GATJ | Kaliumsorbat | auto_generated | Verified via product specs |
| AT-IN-327 | meridian enterprise Group | pending_review | Historical match confirmed |
| citric acid premium | Dextrin Technical | unverified | Verified via product specs |
| glucose syrup 98% | SIG-51-ZAY-11PM | auto_generated | Confirmed by domain expert |
| stratos supply AG | Core Processing Holdings | auto_generated | Verified via product specs |
| atlas partners | Horizon Materials PLC | pending_review | Confirmed by domain expert |
| quantum enterprise BV | CA-SU-681 Group | auto_generated | Cross-referenced with transactions |

#### 4.3.3 Excluded Mappings

Mappings excluded from scope per stakeholder decision:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-9526-D | Invalid Entry 907 | Superseded by newer mapping |
| NOISE-9266-F | Invalid Entry 241 | Superseded by newer mapping |
| NOISE-7199-B | Invalid Entry 868 | Out of scope per business decision |
| NOISE-9977-B | Invalid Entry 564 | Out of scope per business decision |
| NOISE-1268-H | Invalid Entry 605 | Pending validation |
| NOISE-8916-A | Invalid Entry 851 | Pending validation |
| NOISE-5746-H | Invalid Entry 593 | Out of scope per business decision |
| NOISE-2144-D | Invalid Entry 815 | Data quality insufficient |
| NOISE-6732-C | Invalid Entry 416 | Data quality insufficient |
| NOISE-8937-E | Invalid Entry 744 | Data quality insufficient |
| NOISE-4985-E | Invalid Entry 994 | Out of scope per business decision |
| NOISE-3788-A | Invalid Entry 910 | Pending validation |
| NOISE-6732-H | Invalid Entry 179 | Duplicate detected |
| NOISE-2184-G | Invalid Entry 663 | Duplicate detected |
| NOISE-9362-H | Invalid Entry 359 | Data quality insufficient |
| NOISE-5118-E | Invalid Entry 445 | Pending validation |
| NOISE-8039-B | Invalid Entry 939 | Duplicate detected |
| NOISE-6833-F | Invalid Entry 183 | Pending validation |
| NOISE-2015-H | Invalid Entry 329 | Superseded by newer mapping |
| NOISE-9599-G | Invalid Entry 790 | Duplicate detected |
| NOISE-3984-D | Invalid Entry 461 | Superseded by newer mapping |
| NOISE-2781-F | Invalid Entry 430 | Duplicate detected |
| NOISE-4476-A | Invalid Entry 522 | Duplicate detected |
| NOISE-1317-C | Invalid Entry 617 | Superseded by newer mapping |
| NOISE-4940-D | Invalid Entry 789 | Data quality insufficient |
| NOISE-4677-H | Invalid Entry 497 | Duplicate detected |
| NOISE-6701-H | Invalid Entry 404 | Pending validation |
| NOISE-3832-H | Invalid Entry 361 | Data quality insufficient |
| NOISE-1698-H | Invalid Entry 363 | Duplicate detected |
| NOISE-2836-D | Invalid Entry 438 | Out of scope per business decision |
| NOISE-8067-C | Invalid Entry 148 | Out of scope per business decision |
| NOISE-8711-G | Invalid Entry 741 | Superseded by newer mapping |
| NOISE-8226-A | Invalid Entry 704 | Duplicate detected |
| NOISE-9813-D | Invalid Entry 963 | Pending validation |
| NOISE-2145-G | Invalid Entry 642 | Data quality insufficient |
| NOISE-2175-G | Invalid Entry 774 | Duplicate detected |
| NOISE-5430-H | Invalid Entry 842 | Superseded by newer mapping |
| NOISE-1956-B | Invalid Entry 436 | Duplicate detected |
| NOISE-8831-E | Invalid Entry 414 | Duplicate detected |
| NOISE-2473-D | Invalid Entry 884 | Superseded by newer mapping |
| NOISE-7182-E | Invalid Entry 226 | Duplicate detected |
| NOISE-4342-A | Invalid Entry 308 | Pending validation |
| NOISE-7624-A | Invalid Entry 512 | Data quality insufficient |
| NOISE-4441-E | Invalid Entry 935 | Data quality insufficient |
| NOISE-3580-C | Invalid Entry 702 | Data quality insufficient |
| NOISE-5559-E | Invalid Entry 603 | Data quality insufficient |
| NOISE-6785-B | Invalid Entry 832 | Superseded by newer mapping |
| NOISE-6413-E | Invalid Entry 608 | Out of scope per business decision |
| NOISE-2531-B | Invalid Entry 267 | Out of scope per business decision |
| NOISE-6095-A | Invalid Entry 688 | Out of scope per business decision |
| NOISE-6674-F | Invalid Entry 120 | Superseded by newer mapping |
| NOISE-3093-E | Invalid Entry 630 | Pending validation |
| NOISE-3795-E | Invalid Entry 129 | Out of scope per business decision |
| NOISE-8827-G | Invalid Entry 429 | Superseded by newer mapping |
| NOISE-6545-H | Invalid Entry 507 | Duplicate detected |
| NOISE-4141-B | Invalid Entry 745 | Data quality insufficient |
| NOISE-9908-G | Invalid Entry 854 | Pending validation |
| NOISE-2230-C | Invalid Entry 344 | Pending validation |
| NOISE-3220-D | Invalid Entry 809 | Pending validation |
| NOISE-8293-E | Invalid Entry 782 | Data quality insufficient |
| NOISE-9277-B | Invalid Entry 569 | Out of scope per business decision |
| NOISE-8813-B | Invalid Entry 290 | Data quality insufficient |
| NOISE-6114-F | Invalid Entry 803 | Out of scope per business decision |
| NOISE-9899-F | Invalid Entry 458 | Superseded by newer mapping |
| NOISE-2994-E | Invalid Entry 785 | Duplicate detected |
| NOISE-4780-E | Invalid Entry 133 | Duplicate detected |
| NOISE-2121-C | Invalid Entry 314 | Superseded by newer mapping |
| NOISE-3852-D | Invalid Entry 342 | Pending validation |
| NOISE-3463-B | Invalid Entry 270 | Duplicate detected |
| NOISE-5945-H | Invalid Entry 617 | Superseded by newer mapping |
| NOISE-6705-D | Invalid Entry 967 | Out of scope per business decision |
| NOISE-3746-A | Invalid Entry 568 | Out of scope per business decision |
| NOISE-9273-F | Invalid Entry 625 | Pending validation |
| NOISE-4979-B | Invalid Entry 955 | Pending validation |
| NOISE-9637-H | Invalid Entry 102 | Out of scope per business decision |
| NOISE-7493-G | Invalid Entry 279 | Duplicate detected |
| NOISE-2542-D | Invalid Entry 257 | Pending validation |
| NOISE-9005-B | Invalid Entry 541 | Pending validation |
| NOISE-2243-B | Invalid Entry 536 | Out of scope per business decision |
| NOISE-3788-B | Invalid Entry 668 | Data quality insufficient |
| NOISE-2555-A | Invalid Entry 348 | Data quality insufficient |
| NOISE-6749-H | Invalid Entry 538 | Pending validation |
| NOISE-1918-G | Invalid Entry 558 | Duplicate detected |
| NOISE-5133-D | Invalid Entry 842 | Duplicate detected |
| NOISE-8118-B | Invalid Entry 435 | Data quality insufficient |
| NOISE-3701-H | Invalid Entry 168 | Pending validation |
| NOISE-7807-B | Invalid Entry 301 | Data quality insufficient |
| NOISE-1435-D | Invalid Entry 829 | Duplicate detected |
| NOISE-2800-A | Invalid Entry 540 | Pending validation |
| NOISE-2418-G | Invalid Entry 559 | Data quality insufficient |
| NOISE-8209-F | Invalid Entry 528 | Pending validation |
| NOISE-2613-G | Invalid Entry 605 | Duplicate detected |
| NOISE-4061-B | Invalid Entry 175 | Duplicate detected |
| NOISE-7678-F | Invalid Entry 523 | Out of scope per business decision |
| NOISE-1920-F | Invalid Entry 201 | Pending validation |
| NOISE-6881-B | Invalid Entry 159 | Out of scope per business decision |
| NOISE-7531-E | Invalid Entry 135 | Superseded by newer mapping |
| NOISE-8157-F | Invalid Entry 167 | Data quality insufficient |
| NOISE-6741-H | Invalid Entry 770 | Superseded by newer mapping |
| NOISE-4078-G | Invalid Entry 769 | Data quality insufficient |
| NOISE-5707-E | Invalid Entry 820 | Out of scope per business decision |
| NOISE-5536-H | Invalid Entry 213 | Out of scope per business decision |
| NOISE-7495-A | Invalid Entry 518 | Pending validation |
| NOISE-6584-F | Invalid Entry 645 | Pending validation |
| NOISE-9343-C | Invalid Entry 210 | Data quality insufficient |
| NOISE-5972-D | Invalid Entry 193 | Superseded by newer mapping |
| NOISE-3549-D | Invalid Entry 262 | Pending validation |
| NOISE-2573-E | Invalid Entry 803 | Superseded by newer mapping |
| NOISE-1781-C | Invalid Entry 928 | Data quality insufficient |
| NOISE-6369-H | Invalid Entry 985 | Superseded by newer mapping |
| NOISE-5608-C | Invalid Entry 817 | Out of scope per business decision |
| NOISE-8043-E | Invalid Entry 498 | Pending validation |
| NOISE-4177-G | Invalid Entry 671 | Pending validation |
| NOISE-7552-B | Invalid Entry 621 | Duplicate detected |
| NOISE-7174-G | Invalid Entry 363 | Pending validation |
| NOISE-2190-H | Invalid Entry 394 | Pending validation |
| NOISE-3455-G | Invalid Entry 705 | Out of scope per business decision |
| NOISE-3388-E | Invalid Entry 523 | Duplicate detected |
| NOISE-2318-G | Invalid Entry 212 | Duplicate detected |
| NOISE-9429-E | Invalid Entry 108 | Pending validation |
| NOISE-5119-G | Invalid Entry 298 | Data quality insufficient |
| NOISE-7051-H | Invalid Entry 489 | Pending validation |
| NOISE-6279-A | Invalid Entry 495 | Duplicate detected |
| NOISE-6568-D | Invalid Entry 656 | Data quality insufficient |
| NOISE-1559-B | Invalid Entry 417 | Out of scope per business decision |
| NOISE-8897-H | Invalid Entry 627 | Out of scope per business decision |
| NOISE-7087-D | Invalid Entry 240 | Out of scope per business decision |
| NOISE-3836-H | Invalid Entry 644 | Pending validation |
| NOISE-4485-D | Invalid Entry 387 | Out of scope per business decision |
| NOISE-3170-G | Invalid Entry 154 | Data quality insufficient |
| NOISE-8960-H | Invalid Entry 370 | Duplicate detected |
| NOISE-7346-B | Invalid Entry 658 | Superseded by newer mapping |
| NOISE-5962-B | Invalid Entry 289 | Data quality insufficient |
| NOISE-2121-E | Invalid Entry 397 | Data quality insufficient |
| NOISE-5097-F | Invalid Entry 858 | Duplicate detected |
| NOISE-8885-G | Invalid Entry 680 | Data quality insufficient |
| NOISE-6164-F | Invalid Entry 402 | Data quality insufficient |
| NOISE-7829-B | Invalid Entry 296 | Data quality insufficient |
| NOISE-5976-E | Invalid Entry 894 | Data quality insufficient |
| NOISE-9692-C | Invalid Entry 604 | Out of scope per business decision |
| NOISE-7957-B | Invalid Entry 442 | Out of scope per business decision |
| NOISE-7360-F | Invalid Entry 736 | Pending validation |
| NOISE-5130-B | Invalid Entry 687 | Pending validation |
| NOISE-5704-F | Invalid Entry 124 | Data quality insufficient |
| NOISE-2008-F | Invalid Entry 165 | Pending validation |
| NOISE-1480-B | Invalid Entry 338 | Duplicate detected |
| NOISE-7512-C | Invalid Entry 312 | Superseded by newer mapping |
| NOISE-1819-D | Invalid Entry 556 | Out of scope per business decision |
| NOISE-5394-G | Invalid Entry 844 | Duplicate detected |
| NOISE-1530-D | Invalid Entry 728 | Data quality insufficient |
| NOISE-6211-G | Invalid Entry 403 | Pending validation |
| NOISE-3788-C | Invalid Entry 603 | Duplicate detected |
| NOISE-7692-B | Invalid Entry 240 | Out of scope per business decision |
| NOISE-8819-G | Invalid Entry 406 | Pending validation |
| NOISE-9584-A | Invalid Entry 844 | Pending validation |
| NOISE-7297-E | Invalid Entry 736 | Out of scope per business decision |
| NOISE-8990-F | Invalid Entry 403 | Superseded by newer mapping |
| NOISE-5431-C | Invalid Entry 347 | Superseded by newer mapping |
| NOISE-1995-A | Invalid Entry 925 | Superseded by newer mapping |
| NOISE-2006-H | Invalid Entry 751 | Superseded by newer mapping |
| NOISE-4917-A | Invalid Entry 378 | Data quality insufficient |
| NOISE-1362-G | Invalid Entry 233 | Data quality insufficient |
| NOISE-9196-E | Invalid Entry 830 | Pending validation |
| NOISE-5945-C | Invalid Entry 162 | Superseded by newer mapping |
| NOISE-1382-D | Invalid Entry 615 | Duplicate detected |
| NOISE-2423-C | Invalid Entry 262 | Duplicate detected |
| NOISE-1385-F | Invalid Entry 448 | Pending validation |
| NOISE-2071-G | Invalid Entry 928 | Superseded by newer mapping |
| NOISE-4204-G | Invalid Entry 818 | Out of scope per business decision |
| NOISE-6493-H | Invalid Entry 211 | Out of scope per business decision |
| NOISE-7167-B | Invalid Entry 408 | Out of scope per business decision |
| NOISE-5630-E | Invalid Entry 718 | Out of scope per business decision |
| NOISE-2190-C | Invalid Entry 297 | Pending validation |
| NOISE-1009-A | Invalid Entry 288 | Duplicate detected |
| NOISE-1170-D | Invalid Entry 423 | Pending validation |
| NOISE-2036-D | Invalid Entry 698 | Out of scope per business decision |
| NOISE-8151-F | Invalid Entry 665 | Out of scope per business decision |
| NOISE-3686-F | Invalid Entry 597 | Data quality insufficient |
| NOISE-3247-E | Invalid Entry 154 | Duplicate detected |
| NOISE-7015-F | Invalid Entry 866 | Data quality insufficient |
| NOISE-4082-C | Invalid Entry 576 | Out of scope per business decision |
| NOISE-6652-D | Invalid Entry 846 | Superseded by newer mapping |
| NOISE-8155-E | Invalid Entry 893 | Out of scope per business decision |
| NOISE-5096-E | Invalid Entry 640 | Data quality insufficient |
| NOISE-4422-C | Invalid Entry 181 | Duplicate detected |
| NOISE-7098-C | Invalid Entry 733 | Data quality insufficient |
| NOISE-3594-D | Invalid Entry 477 | Pending validation |
| NOISE-3159-B | Invalid Entry 958 | Duplicate detected |
| NOISE-7858-H | Invalid Entry 713 | Superseded by newer mapping |
| NOISE-1119-H | Invalid Entry 428 | Duplicate detected |
| NOISE-9704-B | Invalid Entry 479 | Duplicate detected |
| NOISE-3148-E | Invalid Entry 415 | Superseded by newer mapping |
| NOISE-5004-B | Invalid Entry 286 | Duplicate detected |
| NOISE-4664-F | Invalid Entry 704 | Data quality insufficient |
| NOISE-9306-D | Invalid Entry 610 | Out of scope per business decision |
| NOISE-4407-F | Invalid Entry 697 | Out of scope per business decision |
| NOISE-1975-G | Invalid Entry 592 | Out of scope per business decision |
| NOISE-5905-H | Invalid Entry 890 | Data quality insufficient |
| NOISE-4531-B | Invalid Entry 783 | Out of scope per business decision |
| NOISE-4899-G | Invalid Entry 100 | Duplicate detected |
| NOISE-7804-G | Invalid Entry 984 | Superseded by newer mapping |
| NOISE-1020-H | Invalid Entry 520 | Duplicate detected |
| NOISE-3355-A | Invalid Entry 789 | Pending validation |
| NOISE-2929-D | Invalid Entry 408 | Superseded by newer mapping |
| NOISE-2771-E | Invalid Entry 249 | Superseded by newer mapping |
| NOISE-1283-F | Invalid Entry 278 | Duplicate detected |
| NOISE-5395-H | Invalid Entry 986 | Data quality insufficient |
| NOISE-4202-F | Invalid Entry 377 | Out of scope per business decision |
| NOISE-6464-C | Invalid Entry 476 | Data quality insufficient |
| NOISE-3197-E | Invalid Entry 633 | Out of scope per business decision |
| NOISE-9209-C | Invalid Entry 987 | Data quality insufficient |
| NOISE-3215-F | Invalid Entry 425 | Pending validation |
| NOISE-3661-B | Invalid Entry 472 | Data quality insufficient |
| NOISE-5008-H | Invalid Entry 200 | Pending validation |
| NOISE-4354-B | Invalid Entry 832 | Duplicate detected |
| NOISE-3664-D | Invalid Entry 675 | Out of scope per business decision |
| NOISE-1576-G | Invalid Entry 582 | Duplicate detected |
| NOISE-6666-C | Invalid Entry 748 | Superseded by newer mapping |
| NOISE-7239-C | Invalid Entry 956 | Duplicate detected |
| NOISE-7972-H | Invalid Entry 112 | Duplicate detected |
| NOISE-1393-F | Invalid Entry 280 | Duplicate detected |
| NOISE-9517-D | Invalid Entry 261 | Out of scope per business decision |
| NOISE-2401-B | Invalid Entry 422 | Data quality insufficient |
| NOISE-8006-G | Invalid Entry 525 | Duplicate detected |
| NOISE-1249-G | Invalid Entry 863 | Pending validation |
| NOISE-6789-F | Invalid Entry 122 | Out of scope per business decision |
| NOISE-2527-D | Invalid Entry 218 | Superseded by newer mapping |
| NOISE-3436-G | Invalid Entry 594 | Pending validation |
| NOISE-6722-G | Invalid Entry 949 | Duplicate detected |
| NOISE-7041-C | Invalid Entry 346 | Out of scope per business decision |
| NOISE-1298-D | Invalid Entry 401 | Out of scope per business decision |
| NOISE-5947-C | Invalid Entry 603 | Pending validation |
| NOISE-4905-H | Invalid Entry 782 | Pending validation |
| NOISE-9815-E | Invalid Entry 379 | Out of scope per business decision |
| NOISE-1614-A | Invalid Entry 734 | Superseded by newer mapping |
| NOISE-3510-B | Invalid Entry 259 | Pending validation |
| NOISE-2750-A | Invalid Entry 397 | Data quality insufficient |
| NOISE-5592-B | Invalid Entry 399 | Data quality insufficient |
| NOISE-6835-H | Invalid Entry 265 | Pending validation |
| NOISE-1074-B | Invalid Entry 811 | Out of scope per business decision |
| NOISE-3075-F | Invalid Entry 326 | Pending validation |
| NOISE-7755-A | Invalid Entry 474 | Out of scope per business decision |
| NOISE-6841-C | Invalid Entry 137 | Superseded by newer mapping |
| NOISE-9616-D | Invalid Entry 111 | Superseded by newer mapping |
| NOISE-5196-C | Invalid Entry 164 | Duplicate detected |
| NOISE-3789-C | Invalid Entry 511 | Data quality insufficient |
| NOISE-6850-B | Invalid Entry 973 | Data quality insufficient |
| NOISE-2329-B | Invalid Entry 959 | Superseded by newer mapping |
| NOISE-2130-C | Invalid Entry 428 | Superseded by newer mapping |
| NOISE-5896-A | Invalid Entry 341 | Data quality insufficient |
| NOISE-9507-A | Invalid Entry 505 | Data quality insufficient |
| NOISE-5182-F | Invalid Entry 867 | Pending validation |
| NOISE-6923-E | Invalid Entry 237 | Out of scope per business decision |
| NOISE-4221-B | Invalid Entry 410 | Out of scope per business decision |
| NOISE-3101-G | Invalid Entry 315 | Out of scope per business decision |
| NOISE-5924-H | Invalid Entry 799 | Out of scope per business decision |
| NOISE-1081-B | Invalid Entry 280 | Superseded by newer mapping |
| NOISE-6580-E | Invalid Entry 866 | Data quality insufficient |
| NOISE-2326-B | Invalid Entry 282 | Pending validation |
| NOISE-3370-F | Invalid Entry 482 | Data quality insufficient |
| NOISE-3502-H | Invalid Entry 886 | Data quality insufficient |
| NOISE-1349-C | Invalid Entry 704 | Superseded by newer mapping |
| NOISE-9112-D | Invalid Entry 101 | Duplicate detected |
| NOISE-2562-C | Invalid Entry 700 | Duplicate detected |
| NOISE-5254-H | Invalid Entry 691 | Data quality insufficient |
| NOISE-3087-E | Invalid Entry 234 | Data quality insufficient |
| NOISE-3417-A | Invalid Entry 213 | Superseded by newer mapping |
| NOISE-5065-G | Invalid Entry 992 | Data quality insufficient |
| NOISE-6824-F | Invalid Entry 438 | Data quality insufficient |
| NOISE-4723-G | Invalid Entry 444 | Pending validation |
| NOISE-4738-F | Invalid Entry 441 | Out of scope per business decision |
| NOISE-9539-B | Invalid Entry 985 | Data quality insufficient |
| NOISE-3442-B | Invalid Entry 137 | Duplicate detected |
| NOISE-4841-C | Invalid Entry 700 | Duplicate detected |
| NOISE-2961-A | Invalid Entry 971 | Out of scope per business decision |
| NOISE-8025-F | Invalid Entry 857 | Out of scope per business decision |
| NOISE-9589-G | Invalid Entry 549 | Duplicate detected |
| NOISE-1166-G | Invalid Entry 942 | Pending validation |
| NOISE-8759-D | Invalid Entry 914 | Duplicate detected |
| NOISE-2018-C | Invalid Entry 461 | Duplicate detected |
| NOISE-1948-D | Invalid Entry 865 | Superseded by newer mapping |
| NOISE-4209-H | Invalid Entry 280 | Pending validation |
| NOISE-9594-F | Invalid Entry 915 | Out of scope per business decision |
| NOISE-3715-C | Invalid Entry 495 | Duplicate detected |
| NOISE-2301-B | Invalid Entry 263 | Data quality insufficient |
| NOISE-7805-E | Invalid Entry 865 | Superseded by newer mapping |
| NOISE-9969-B | Invalid Entry 808 | Duplicate detected |
| NOISE-5712-E | Invalid Entry 576 | Duplicate detected |
| NOISE-8956-C | Invalid Entry 499 | Pending validation |
| NOISE-1892-E | Invalid Entry 759 | Superseded by newer mapping |
| NOISE-4117-H | Invalid Entry 946 | Superseded by newer mapping |
| NOISE-6044-E | Invalid Entry 771 | Out of scope per business decision |
| NOISE-8469-H | Invalid Entry 781 | Out of scope per business decision |
| NOISE-4597-F | Invalid Entry 822 | Pending validation |
| NOISE-7103-G | Invalid Entry 299 | Pending validation |
| NOISE-9572-B | Invalid Entry 421 | Superseded by newer mapping |
| NOISE-6780-F | Invalid Entry 355 | Out of scope per business decision |
| NOISE-9005-D | Invalid Entry 549 | Pending validation |
| NOISE-8036-B | Invalid Entry 976 | Duplicate detected |
| NOISE-6171-G | Invalid Entry 687 | Out of scope per business decision |
| NOISE-9579-H | Invalid Entry 660 | Out of scope per business decision |
| NOISE-6066-A | Invalid Entry 412 | Superseded by newer mapping |
| NOISE-5354-E | Invalid Entry 415 | Out of scope per business decision |
| NOISE-1115-D | Invalid Entry 728 | Superseded by newer mapping |
| NOISE-3776-F | Invalid Entry 549 | Out of scope per business decision |
| NOISE-4428-C | Invalid Entry 347 | Out of scope per business decision |
| NOISE-3174-D | Invalid Entry 752 | Superseded by newer mapping |
| NOISE-4122-B | Invalid Entry 217 | Data quality insufficient |
| NOISE-2737-E | Invalid Entry 592 | Data quality insufficient |

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
