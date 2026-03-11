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
| Total entities assessed | 1541 | Completed |
| Successfully mapped | 1070 | Verified |
| Excluded from scope | 321 | Documented |
| Manual review required | 2 | In Progress |

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
| Premier Partners Group | core partners NV | pending_review | Historical match confirmed |
| SIG-25-WDK-CWCD | dextrin tech grade | pending_review | Verified via product specs |
| lactic acid standard | Coconut Oil 98% Lebensmittelrein | auto_generated | Verified via product specs |
| Zitronensäure | fructose standard | auto_generated | Verified via product specs |
| Vat Standardqualität BR 25% | SIG-67-YOR-JCUH | pending_review | Auto-mapped, validated |
| Baltic Processing PLC | SIG-61-SLO-3QQX PLC | unverified | Historical match confirmed |
| Pinnacle Materials | central logistics | pending_review | Cross-referenced with transactions |
| Citric Acid 70% | Traubenzucker Qualitätsstufe I | auto_generated | Verified via product specs |
| SIG-69-XLH-L6HZ | elite logistics | pending_review | Auto-mapped, validated |
| Dextrose Grade A | SIG-73-UUF-1F99 | unverified | Cross-referenced with transactions |
| central distribution | SIG-48-MQG-OVJU SAS | unverified | Historical match confirmed |
| Quantum Commodities PLC | Atlantic Logistik SAS | unverified | Confirmed by domain expert |
| WH-GL-ST-378 | Casein | auto_generated | Confirmed by domain expert |
| VA-RE-F-21-230 | SIG-70-QGS-CCAF | auto_generated | Cross-referenced with transactions |
| WH-GL-146 | Lactic Acid 25% Lebensmittelrein | pending_review | Cross-referenced with transactions |
| sorbic acid | Dextrose 25% | pending_review | Auto-mapped, validated |
| quantum logistics | Nexus Logistics | auto_generated | Historical match confirmed |
| Lactic Acid | Resistente Stärke Qualitätsstufe II | auto_generated | Confirmed by domain expert |
| Resistente Stärke Lebensmittelrein | SIG-37-MXA-3C7Q | auto_generated | Verified via product specs |
| Resistant Starch Pharma Grade | SIG-39-UPB-Q8DA | auto_generated | Cross-referenced with transactions |
| Maltodextrin-Pulver DE15 | resistant starch | unverified | Auto-mapped, validated |
| ME-IN-934 NV | Stratos Ingredients Group | unverified | Auto-mapped, validated |
| SIG-13-CAZ-HXXP | Lactic Acid | unverified | Cross-referenced with transactions |
| SIG-66-DRZ-QEHY | Pacific Versorgung GmbH | unverified | Auto-mapped, validated |
| Soy Isolate 98% | Weizenklebereiweiß 50% Technische Qualität | unverified | Cross-referenced with transactions |
| Lactic Acid | Natriumbenzoat Pharmazeutisch rein | auto_generated | Cross-referenced with transactions |
| Lactic Acid | ascorbic acid 99.5% | unverified | Confirmed by domain expert |
| resistant starch | Sunflower Oil Grade B | auto_generated | Confirmed by domain expert |
| SIG-67-TPL-WT5F | CO-OI-977 | pending_review | Verified via product specs |
| coconut oil food grade | SIG-51-KQC-QY9M | auto_generated | Confirmed by domain expert |
| Coconut Oil | fructose 98% premium | pending_review | Auto-mapped, validated |
| SIG-24-VMY-QMRL | Vanguard Supply Co. | auto_generated | Verified via product specs |
| vertex materials | PI-SU-CO-216 | pending_review | Auto-mapped, validated |
| Sorbinsäure Premiumqualität | PE-PR-25-185 | unverified | Cross-referenced with transactions |
| Apex Versorgung GmbH | Premier Supply Co. | auto_generated | Historical match confirmed |
| GL-SY-70-549 | Coconut Oil 70% Grade A | pending_review | Cross-referenced with transactions |
| PO-SO-GR-A-715 | Sorbinsäure 98% | pending_review | Cross-referenced with transactions |
| nordic manufacturing International | Pinnacle Industries | auto_generated | Auto-mapped, validated |
| HO-DI-531 Group | SIG-41-BJL-NXWK Holdings | auto_generated | Verified via product specs |
| nexus ingredients SAS | Pacific Ingredients BV | pending_review | Confirmed by domain expert |
| Cyclodextrin Standardqualität | cyclodextrin standard | auto_generated | Auto-mapped, validated |
| Sorbinsäure 98% | SIG-61-IQH-EKWH | unverified | Confirmed by domain expert |
| meridian sourcing | Meridian Logistics | unverified | Historical match confirmed |
| Coconut Oil Standard | WH-GL-99.5-557 | pending_review | Verified via product specs |
| central distribution | NE-PR-315 Holdings | unverified | Historical match confirmed |
| SIG-22-TOX-02GV | Rapeseed Oil 98% | pending_review | Cross-referenced with transactions |
| LA-AC-891 | citric acid premium | auto_generated | Auto-mapped, validated |
| PA-OI-70-GR-B-781 | Palmfett | auto_generated | Auto-mapped, validated |
| dextrose 25% tech grade | Ascorbic Acid Pharma Grade | unverified | Confirmed by domain expert |
| Coconut Oil 50% | Palm Oil | auto_generated | Cross-referenced with transactions |
| Glucose Syrup 70% | FR-TE-414 | unverified | Auto-mapped, validated |
| prism supply | Nexus Werkstoffe | pending_review | Auto-mapped, validated |
| Resistente Stärke 50% Standardqualität | IS-25-FO-GR-789 | unverified | Cross-referenced with transactions |
| wheat gluten premium | DE-GR-A-472 | unverified | Cross-referenced with transactions |
| Sodium Benzoate Grade A | SIG-55-CTS-U5X0 | pending_review | Verified via product specs |
| Withholding NL 7% | Withholding NL 21% | pending_review | Historical match confirmed |
| Atlantic Materials | Central Werkstoffe | unverified | Auto-mapped, validated |
| Core Trading | Prism Chemicals AG | auto_generated | Cross-referenced with transactions |
| baltic solutions Group | SIG-94-CCX-H0AN International | auto_generated | Historical match confirmed |
| Zitronensäure Premiumqualität | SIG-37-HHT-38YO | pending_review | Auto-mapped, validated |
| SIG-39-KYF-P35A | global logistics | pending_review | Cross-referenced with transactions |
| Prism Werkstoffe | nexus sourcing | auto_generated | Confirmed by domain expert |
| resistant starch 98% pharma grade | SIG-80-MXD-T81P | unverified | Cross-referenced with transactions |
| nexus logistics | SIG-76-ESC-PNV7 | pending_review | Verified via product specs |
| SIG-13-ZIB-S8MV International | Stratos Supply | pending_review | Confirmed by domain expert |
| Palm Oil | Natriumbenzoat | unverified | Historical match confirmed |
| Isoglucose Premium | Ascorbic Acid 50% | auto_generated | Historical match confirmed |
| fructose premium | Natriumchlorid 98% Standardqualität | pending_review | Auto-mapped, validated |
| VA-ST-D-10-295 | Vat Standard US 5% | auto_generated | Cross-referenced with transactions |
| CA-50-GR-B-203 | soy isolate 99.5% | pending_review | Cross-referenced with transactions |
| Prime Versorgung GmbH | Elite Supply Co. | pending_review | Confirmed by domain expert |
| Isoglucose Technical | CY-892 | auto_generated | Historical match confirmed |
| SIG-59-ZZK-AYAJ PLC | AT-CH-905 Holdings | pending_review | Verified via product specs |
| Fructose | SIG-47-NVU-R3XU | auto_generated | Confirmed by domain expert |
| Natriumbenzoat Standardqualität | glucose syrup tech grade | auto_generated | Cross-referenced with transactions |
| Cyclodextrin Premiumqualität | sodium benzoate premium | pending_review | Verified via product specs |
| SIG-39-QZD-93EZ | maltodextrin de18 | auto_generated | Verified via product specs |
| Dextrin 70% Pharmazeutisch rein | Sorbic Acid 25% Pharma Grade | unverified | Auto-mapped, validated |
| Maltodextrin DE10 | SO-BE-824 | auto_generated | Cross-referenced with transactions |
| WI-U-10-721 | Vat Standard DE 21% | pending_review | Cross-referenced with transactions |
| atlas sourcing | AP-LO-445 | unverified | Cross-referenced with transactions |
| NO-SU-CO-376 | horizon logistics | pending_review | Historical match confirmed |
| SIG-88-AGF-FF5L | Zitronensäure Qualitätsstufe I | auto_generated | Historical match confirmed |
| Natriumbenzoat 25% | resistant starch food grade | unverified | Auto-mapped, validated |
| excise in 10% | Withholding IN 10% | auto_generated | Verified via product specs |
| withholding fr 10% | WI-N-21-724 | pending_review | Cross-referenced with transactions |
| Continental Enterprise Holdings | SIG-76-YAI-8VE6 SAS | pending_review | Auto-mapped, validated |
| Vanguard Logistics | PR-CO-443 Group | auto_generated | Cross-referenced with transactions |
| Glukosesirup Syrup Technische Qualität | CA-GR-A-380 | auto_generated | Cross-referenced with transactions |
| Premier Logistics | QU-LO-616 | pending_review | Historical match confirmed |
| EL-SO-688 | catalyst materials | auto_generated | Auto-mapped, validated |
| Maltodextrin DE5 Grade B | SU-OI-50-GR-A-521 | pending_review | Verified via product specs |
| vat standard gb 19% | SIG-37-QAD-9FMK | unverified | Cross-referenced with transactions |
| Catalyst Industries International | pinnacle industries Corp. | unverified | Confirmed by domain expert |
| Palmfett Qualitätsstufe II | SIG-51-IYK-630P | auto_generated | Confirmed by domain expert |
| Isoglucose | Traubenzucker 99.5% Qualitätsstufe II | auto_generated | Auto-mapped, validated |
| SIG-65-IJJ-DXAJ SA | stratos processing LLC | pending_review | Historical match confirmed |
| sodium benzoate 99.5% tech grade | Natriumbenzoat Qualitätsstufe II | pending_review | Confirmed by domain expert |
| Casein 25% Pharma Grade | Cyclodextrin Lebensmittelrein | auto_generated | Confirmed by domain expert |
| SIG-52-HZA-742D | quantum materials | unverified | Historical match confirmed |
| Vat Standardqualität IN 0% | VA-RE-F-0-158 | pending_review | Confirmed by domain expert |
| Vanguard Partners PLC | CO-DI-629 BV | unverified | Confirmed by domain expert |
| Resistant Starch 70% Food Grade | CY-98-PH-GR-614 | unverified | Verified via product specs |
| Casein Technical | PO-SO-TE-239 | unverified | Confirmed by domain expert |
| vanguard industries PLC | AT-DI-544 | auto_generated | Cross-referenced with transactions |
| AS-AC-130 | Dextrose 25% Technical | unverified | Auto-mapped, validated |
| Pea Protein Premiumqualität | SO-BE-PR-691 | auto_generated | Cross-referenced with transactions |
| SIG-40-NOO-BAK8 | Nordic Logistics | auto_generated | Historical match confirmed |
| Customs Duty FR 7% | withholding us 0% | pending_review | Verified via product specs |
| fructose standard | Traubenzucker Standardqualität | pending_review | Auto-mapped, validated |
| Potassium Sorbate Food Grade | LA-AC-927 | pending_review | Historical match confirmed |
| PO-SO-TE-239 | fructose standard | unverified | Verified via product specs |
| SIG-60-KAS-IVMD | SO-IS-50-GR-B-346 | auto_generated | Verified via product specs |
| Vat Reduced GB 25% | CU-DU-C-25-424 | pending_review | Historical match confirmed |
| DE-70-PH-GR-978 | Pea Protein 99.5% Premium | auto_generated | Verified via product specs |
| SIG-60-KAS-IVMD | sorbic acid 50% standard | unverified | Auto-mapped, validated |
| Dextrin 50% | dextrose 70% | unverified | Verified via product specs |
| Resistant Starch Grade B | SIG-91-FOC-36I6 | unverified | Auto-mapped, validated |
| EX-F-21-883 | SIG-93-VLZ-VI4P | auto_generated | Verified via product specs |
| Zitronensäure | DE-70-856 | unverified | Confirmed by domain expert |
| SIG-75-XPL-QWB7 GmbH | Atlas Partners | pending_review | Confirmed by domain expert |
| PA-OI-70-GR-B-781 | Kasein 98% | auto_generated | Cross-referenced with transactions |
| CA-CA-50-GR-A-195 | Maltodextrin DE5 | unverified | Historical match confirmed |
| DE-GR-B-157 | potassium sorbate 98% | auto_generated | Confirmed by domain expert |
| Maltodextrin-Pulver DE10 | resistant starch 70% food grade | pending_review | Historical match confirmed |
| RA-OI-99.5-602 | pea protein | auto_generated | Cross-referenced with transactions |
| Palmfett 98% Qualitätsstufe I | Wheat Gluten | unverified | Historical match confirmed |
| NE-LO-735 | SIG-19-GAY-Z6O1 | pending_review | Cross-referenced with transactions |
| Zitronensäure | SIG-73-LLJ-LNGI | unverified | Cross-referenced with transactions |
| Kasein 98% Technische Qualität | Soy Isolate | pending_review | Verified via product specs |
| SO-BE-50-427 | Maltodextrin-Pulver DE18 | pending_review | Verified via product specs |
| HO-LO-534 PLC | Nexus Supply Group | unverified | Confirmed by domain expert |
| SO-CH-70-365 | Coconut Oil Lebensmittelrein | auto_generated | Confirmed by domain expert |
| GL-SY-TE-803 | SIG-16-CAW-LD7M | auto_generated | Cross-referenced with transactions |
| GL-LO-935 | Core Werkstoffe | auto_generated | Auto-mapped, validated |
| SIG-95-APX-PWFS | PE-PR-ST-174 | pending_review | Verified via product specs |
| potassium sorbate premium | Coconut Oil 99.5% Pharma Grade | auto_generated | Cross-referenced with transactions |
| catalyst supply | Stratos Supply Co. | auto_generated | Confirmed by domain expert |
| wheat gluten premium | SIG-30-EKM-GB1A | pending_review | Verified via product specs |
| Maltodextrin DE25 | ascorbic acid tech grade | pending_review | Historical match confirmed |
| Ascorbic Acid Pharmazeutisch rein | rapeseed oil premium | pending_review | Verified via product specs |
| SIG-18-LLP-8GUU | Traubenzucker Standardqualität | unverified | Verified via product specs |
| CI-AC-25-GR-A-669 | Calcium Carbonate Qualitätsstufe II | unverified | Verified via product specs |
| WI-B-10-442 | Vat Standardqualität US 21% | auto_generated | Auto-mapped, validated |
| Sorbic Acid | SO-AC-FO-GR-286 | auto_generated | Verified via product specs |
| Vat Reduced US 19% | vat reduced cn 21% | unverified | Cross-referenced with transactions |
| SIG-64-QID-BCT3 | GL-SY-99.5-GR-B-358 | pending_review | Auto-mapped, validated |
| Quantum Supply Co. | SIG-28-SXX-AKUN | pending_review | Confirmed by domain expert |
| RE-ST-FO-GR-998 | Coconut Oil 98% | auto_generated | Cross-referenced with transactions |
| pacific distribution | Prime Materials Inc. | auto_generated | Cross-referenced with transactions |
| RA-OI-TE-584 | Fructose Pharmazeutisch rein | unverified | Confirmed by domain expert |
| CA-884 | Dextrin Technical | auto_generated | Cross-referenced with transactions |
| Sorbinsäure | SIG-42-BEO-614U | pending_review | Cross-referenced with transactions |
| PO-SO-480 | SIG-83-JEP-R0ZJ | auto_generated | Auto-mapped, validated |
| Sorbic Acid 98% | SIG-58-LWY-Q8P6 | auto_generated | Cross-referenced with transactions |
| ST-TR-786 International | Stratos Versorgung | auto_generated | Cross-referenced with transactions |
| Rapsöl Lebensmittelrein | GL-SY-533 | unverified | Verified via product specs |
| SIG-13-PHC-GSY7 | premier supply | unverified | Cross-referenced with transactions |
| Pacific Industrien | pacific industries | pending_review | Historical match confirmed |
| DE-70-512 | Calcium Carbonate 98% | unverified | Auto-mapped, validated |
| Lactic Acid | RA-OI-25-PH-GR-210 | auto_generated | Cross-referenced with transactions |
| Coconut Oil 70% | SIG-79-BBY-UB7L | pending_review | Verified via product specs |
| Lactic Acid 70% Pharmazeutisch rein | pea protein | unverified | Verified via product specs |
| Natriumchlorid 98% Standardqualität | Ascorbic Acid | pending_review | Historical match confirmed |
| SIG-50-PNF-Z2E8 | Nexus Logistik | unverified | Historical match confirmed |
| SIG-13-BSD-DJSO International | Vertex Distribution SA | auto_generated | Auto-mapped, validated |
| nexus enterprise | SIG-56-ZQV-YINP SA | auto_generated | Auto-mapped, validated |
| PI-PR-193 | continental enterprise International | auto_generated | Cross-referenced with transactions |
| Dextrin 50% | resistant starch standard | auto_generated | Historical match confirmed |
| sodium chloride 70% | Ascorbic Acid | auto_generated | Cross-referenced with transactions |
| Maltodextrin DE25 | IS-GR-B-640 | pending_review | Confirmed by domain expert |
| customs duty de 0% | Excise GB 25% | unverified | Verified via product specs |
| Citric Acid 99.5% | SU-OI-98-462 | unverified | Cross-referenced with transactions |
| Prism Logistik | SIG-65-KWQ-0U4R | auto_generated | Verified via product specs |
| Rapsöl Pharmazeutisch rein | rapeseed oil tech grade | unverified | Historical match confirmed |
| Soy Isolate 50% Grade B | Maltodextrin-Pulver DE5 Qualitätsstufe I | unverified | Historical match confirmed |
| stratos trading | CA-IN-146 SA | pending_review | Verified via product specs |
| SU-OI-GR-A-224 | Resistant Starch Premium | unverified | Historical match confirmed |
| LA-AC-393 | Glucose Syrup 25% | unverified | Cross-referenced with transactions |
| SIG-55-ICI-Z2GP GmbH | Central Manufacturing Holdings | auto_generated | Cross-referenced with transactions |
| Pea Protein Premium | DE-GR-A-472 | unverified | Verified via product specs |
| pinnacle commodities BV | Prime Chemicals | auto_generated | Auto-mapped, validated |
| Potassium Sorbate 50% Food Grade | Palmfett Standardqualität | unverified | Historical match confirmed |
| CO-OI-GR-A-370 | Zitronensäure | pending_review | Cross-referenced with transactions |
| Natriumbenzoat Lebensmittelrein | CA-CA-70-883 | unverified | Verified via product specs |
| ascorbic acid standard | Fructose 25% | auto_generated | Confirmed by domain expert |
| SIG-68-QRN-LSY2 | SO-IS-PH-GR-671 | auto_generated | Auto-mapped, validated |
| Natriumchlorid 99.5% | Dextrin 70% | auto_generated | Auto-mapped, validated |
| SIG-74-ZJN-KVHO | ME-MA-977 | unverified | Confirmed by domain expert |
| Ascorbic Acid 99.5% Technische Qualität | citric acid 99.5% | pending_review | Historical match confirmed |
| Dextrin Pharma Grade | SIG-91-GMY-Q91Y | pending_review | Verified via product specs |
| SIG-92-AXW-GPAG | VE-CH-841 Group | auto_generated | Cross-referenced with transactions |
| premier partners Group | Prime Rohstoffe PLC | auto_generated | Verified via product specs |
| Vertex Rohstoffe | PI-CH-610 Ltd. | pending_review | Historical match confirmed |
| Core Versorgung GmbH | AT-SO-165 | unverified | Historical match confirmed |
| Sonnenblumenöl 98% | PO-SO-632 | pending_review | Auto-mapped, validated |
| Zitronensäure Standardqualität | SIG-30-MPO-SJEV | auto_generated | Cross-referenced with transactions |
| Stellar Rohstoffe | PR-SU-312 KG | pending_review | Verified via product specs |
| sodium benzoate | SIG-42-STL-CX7L | auto_generated | Cross-referenced with transactions |
| meridian sourcing | Meridian Sourcing | unverified | Confirmed by domain expert |
| LA-AC-TE-651 | glucose syrup 25% | pending_review | Auto-mapped, validated |
| lactic acid standard | Soy Isolate 25% Standard | unverified | Verified via product specs |
| lactic acid 98% premium | CA-GR-A-380 | unverified | Auto-mapped, validated |
| Vertex Distribution | nordic partners | auto_generated | Cross-referenced with transactions |
| Ascorbic Acid 50% | pea protein pharma grade | unverified | Historical match confirmed |
| Sorbic Acid 25% Grade B | FR-99.5-FO-GR-963 | auto_generated | Historical match confirmed |
| Palm Oil | SIG-82-JMP-PVGN | unverified | Verified via product specs |
| sodium benzoate 99.5% standard | SO-CH-TE-223 | auto_generated | Verified via product specs |
| Quantum Trading | PR-SO-121 Corp. | auto_generated | Cross-referenced with transactions |
| CA-98-TE-238 | Coconut Oil Lebensmittelrein | pending_review | Cross-referenced with transactions |
| Continental Logistik | Pinnacle Materials | pending_review | Cross-referenced with transactions |
| VA-ST-D-7-855 | Customs Duty US 10% | unverified | Historical match confirmed |
| DE-635 | Natriumbenzoat 99.5% Technische Qualität | pending_review | Cross-referenced with transactions |
| SIG-63-YJW-AP00 | Sorbinsäure 50% Lebensmittelrein | pending_review | Auto-mapped, validated |
| SIG-36-ZKX-4SE4 | Glucose Syrup 98% Grade A | auto_generated | Cross-referenced with transactions |
| SIG-52-LXJ-ZU4J | Atlas Versorgung GmbH | pending_review | Auto-mapped, validated |
| Vat Reduced DE 20% | VA-RE-C-21-484 | unverified | Historical match confirmed |
| Catalyst Logistics | SIG-14-GCI-G4Q9 | pending_review | Confirmed by domain expert |
| quantum logistics | SIG-21-DOL-82H3 | auto_generated | Verified via product specs |
| Horizon Materials SAS | continental solutions | unverified | Verified via product specs |
| Rapsöl 25% Lebensmittelrein | SIG-49-UKY-6H3R | auto_generated | Cross-referenced with transactions |
| Isoglucose 98% | resistant starch 25% food grade | pending_review | Auto-mapped, validated |
| SIG-80-WKN-N0SS | Isoglucose 50% Qualitätsstufe I | pending_review | Historical match confirmed |
| Isoglucose | rapeseed oil 50% pharma grade | auto_generated | Auto-mapped, validated |
| isoglucose 70% | DE-ST-553 | unverified | Cross-referenced with transactions |
| ascorbic acid pharma grade | SIG-99-OQS-ADHF | unverified | Auto-mapped, validated |
| SIG-51-MQP-ZO0K | AT-SU-CO-707 | auto_generated | Verified via product specs |
| Dextrose 25% | DE-GR-A-351 | unverified | Verified via product specs |
| FR-108 | Citric Acid | unverified | Cross-referenced with transactions |
| Maltodextrin DE20 | pea protein 50% | unverified | Historical match confirmed |
| Cyclodextrin 98% Pharmazeutisch rein | SIG-71-OEX-5BRF | pending_review | Auto-mapped, validated |
| DE-25-PR-846 | SIG-61-PIG-0DBF | pending_review | Verified via product specs |
| Isoglucose 70% | Citric Acid 50% | pending_review | Auto-mapped, validated |
| sorbic acid 50% | Pea Protein | pending_review | Cross-referenced with transactions |
| continental ingredients AG | Continental Chemicals Inc. | auto_generated | Verified via product specs |
| Global Materials | PR-MA-161 | auto_generated | Historical match confirmed |
| ST-LO-927 | Vertex Versorgung GmbH | pending_review | Auto-mapped, validated |
| SIG-67-YAJ-18K0 | Sorbic Acid 50% Grade A | unverified | Auto-mapped, validated |
| Prism Ingredients | Continental Enterprise Group | auto_generated | Confirmed by domain expert |
| VA-RE-C-19-810 | Excise IN 15% | auto_generated | Auto-mapped, validated |
| Continental Werkstoffe NV | Horizon Trading Ltd. | auto_generated | Confirmed by domain expert |
| CO-MA-245 | nordic supply | unverified | Historical match confirmed |
| Cyclodextrin | LA-AC-393 | pending_review | Auto-mapped, validated |
| Nexus Ingredients SARL | Core Manufacturing Holdings | unverified | Historical match confirmed |
| Isoglucose 70% | SO-BE-PR-691 | auto_generated | Historical match confirmed |
| SIG-89-RGS-FIRM Holdings | Zenith Trading LLC | auto_generated | Auto-mapped, validated |
| Sodium Benzoate 25% Grade B | potassium sorbate food grade | unverified | Verified via product specs |
| Soy Isolate 99.5% | RE-ST-GR-B-677 | auto_generated | Confirmed by domain expert |
| AS-AC-FO-GR-835 | Palm Oil 70% Premium | pending_review | Cross-referenced with transactions |
| withholding fr 10% | Vat Reduced GB 25% | unverified | Historical match confirmed |
| SIG-84-EIB-2MOT | Dextrose 99.5% Grade B | pending_review | Verified via product specs |
| Central Manufacturing Holdings | SIG-49-AVR-NL0H International | pending_review | Verified via product specs |
| global distribution Corp. | GL-PA-520 BV | unverified | Historical match confirmed |
| CO-OI-98-876 | SIG-52-EML-H8JV | pending_review | Historical match confirmed |
| SIG-83-MZM-HGMN GmbH | Zenith Manufacturing Ltd. | pending_review | Cross-referenced with transactions |
| SO-AC-98-579 | SIG-13-CAZ-HXXP | unverified | Historical match confirmed |
| Soy Isolate 99.5% | Fructose | auto_generated | Cross-referenced with transactions |
| SIG-25-VPE-TOC1 | palm oil 98% | auto_generated | Auto-mapped, validated |
| SIG-41-WHZ-QDKE | Meridian Sourcing | unverified | Auto-mapped, validated |
| SIG-15-PFO-2W85 | Weizenklebereiweiß 50% Technische Qualität | pending_review | Verified via product specs |
| Apex Chemicals | nexus processing AG | unverified | Auto-mapped, validated |
| Weizenklebereiweiß Qualitätsstufe I | SIG-80-QOK-BKBF | auto_generated | Verified via product specs |
| vat reduced nl 0% | Vat Standardqualität NL 10% | pending_review | Confirmed by domain expert |
| Natriumchlorid 98% | SIG-52-ITT-ELH9 | unverified | Historical match confirmed |
| central supply | Atlantic Materials | unverified | Auto-mapped, validated |
| SIG-79-GKV-W8GA | Dextrose 25% Technical | pending_review | Historical match confirmed |
| CE-PR-134 | Premier Ingredients Ltd. | unverified | Historical match confirmed |
| fructose tech grade | FR-194 | auto_generated | Confirmed by domain expert |
| SIG-69-INT-Z1YQ | IS-25-FO-GR-789 | pending_review | Cross-referenced with transactions |
| AT-LO-132 | Vertex Solutions NV | auto_generated | Cross-referenced with transactions |
| Wheat Gluten | SU-OI-ST-338 | pending_review | Cross-referenced with transactions |
| SIG-53-HTQ-XVWB Group | NO-MA-484 BV | auto_generated | Auto-mapped, validated |
| SIG-87-YFT-P51V | Fructose | pending_review | Auto-mapped, validated |
| FR-99.5-PH-GR-378 | Sorbic Acid Food Grade | unverified | Cross-referenced with transactions |
| pinnacle industries Corp. | SIG-62-KTK-XM5L Holdings | auto_generated | Verified via product specs |
| fructose 25% | Cyclodextrin | pending_review | Cross-referenced with transactions |
| Withholding BR 15% | SIG-15-EUV-5BD1 | unverified | Historical match confirmed |
| SU-OI-TE-879 | Weizenklebereiweiß 99.5% | pending_review | Cross-referenced with transactions |
| Sodium Chloride 70% Grade B | SIG-60-GHI-04X0 | unverified | Cross-referenced with transactions |
| Zitronensäure 70% Lebensmittelrein | SIG-34-JQN-ROWX | pending_review | Cross-referenced with transactions |
| Global Materials | pinnacle supply | unverified | Cross-referenced with transactions |
| Resistente Stärke | dextrin premium | unverified | Historical match confirmed |
| PO-SO-339 | Ascorbic Acid | pending_review | Cross-referenced with transactions |
| AS-AC-TE-342 | Palm Oil 98% | pending_review | Cross-referenced with transactions |
| SIG-87-YFT-P51V | Calcium Carbonate 25% Pharma Grade | unverified | Confirmed by domain expert |
| VA-ST-G-20-932 | Withholding FR 5% | pending_review | Historical match confirmed |
| Pea Protein 99.5% | coconut oil food grade | unverified | Verified via product specs |
| SIG-68-ELC-6AVE | MA-DE-ST-267 | auto_generated | Confirmed by domain expert |
| PI-SU-CO-216 | SIG-69-UAZ-1ODW | auto_generated | Cross-referenced with transactions |
| SIG-29-BKQ-HXCX Group | Quantum Manufacturing | unverified | Confirmed by domain expert |
| Meridian Sourcing | Quantum Supply Co. | pending_review | Cross-referenced with transactions |
| Customs Duty DE 5% | Excise BR 5% | pending_review | Verified via product specs |
| SIG-62-JTP-RUMX | CU-DU-G-0-770 | pending_review | Historical match confirmed |
| Prism Manufacturing LLC | Vanguard Industrien | auto_generated | Historical match confirmed |
| ascorbic acid food grade | SIG-13-CGO-2Y4L | auto_generated | Verified via product specs |
| SO-AC-98-741 | sorbic acid 98% | auto_generated | Confirmed by domain expert |
| SIG-10-PGH-BTUF | nexus supply | pending_review | Historical match confirmed |
| SIG-20-LIK-8TZV Ltd. | CE-MA-997 KG | pending_review | Confirmed by domain expert |
| SIG-64-ILX-G2AZ PLC | apex chemicals International | unverified | Cross-referenced with transactions |
| Ascorbic Acid Pharmazeutisch rein | wheat gluten 99.5% premium | auto_generated | Historical match confirmed |
| Kaliumsorbat | Palm Oil | pending_review | Verified via product specs |
| WH-GL-99.5-TE-628 | SIG-39-FND-AALU | pending_review | Cross-referenced with transactions |
| QU-SU-CO-774 | Pacific Materials | unverified | Confirmed by domain expert |
| DE-TE-414 | SIG-57-YOY-F7N2 | pending_review | Verified via product specs |
| SIG-25-ROA-G6G0 | resistant starch food grade | unverified | Cross-referenced with transactions |
| SIG-86-LPN-HCNV | Citric Acid | auto_generated | Historical match confirmed |
| Atlas Ingredients Ltd. | ST-SU-959 KG | unverified | Verified via product specs |
| Horizon Partners Ltd. | SIG-13-ZIB-S8MV International | unverified | Historical match confirmed |
| SIG-83-GEN-QNXZ | Apex Sourcing | auto_generated | Historical match confirmed |
| Soja Isolate Standardqualität | SO-CH-185 | unverified | Historical match confirmed |
| pacific sourcing | Prism Sourcing | auto_generated | Auto-mapped, validated |
| Calcium Carbonate 50% Grade A | Coconut Oil 98% | auto_generated | Verified via product specs |
| Natriumbenzoat 25% Qualitätsstufe II | calcium carbonate standard | pending_review | Cross-referenced with transactions |
| VA-ST-N-20-275 | Excise DE 7% | auto_generated | Historical match confirmed |
| Citric Acid 99.5% Pharma Grade | Traubenzucker Qualitätsstufe II | unverified | Verified via product specs |
| Natriumchlorid | rapeseed oil tech grade | auto_generated | Verified via product specs |
| Sonnenblumenöl 98% | Palm Oil Grade B | unverified | Historical match confirmed |
| SIG-95-EES-2FE9 | sunflower oil 70% food grade | auto_generated | Historical match confirmed |
| Sodium Benzoate | SIG-52-LQX-X1DO | unverified | Cross-referenced with transactions |
| quantum enterprise BV | ZE-TR-467 AG | auto_generated | Verified via product specs |
| Zitronensäure Qualitätsstufe I | pea protein | auto_generated | Cross-referenced with transactions |
| Catalyst Materials | NE-MA-923 | pending_review | Confirmed by domain expert |
| vat standard de 7% | SIG-89-EJE-7I11 | pending_review | Historical match confirmed |
| Zenith Supply Co. | stratos sourcing | pending_review | Historical match confirmed |
| Vanguard Supply Co. | PI-SO-922 | pending_review | Historical match confirmed |
| dextrose 25% | SO-IS-PH-GR-671 | auto_generated | Cross-referenced with transactions |
| sodium benzoate 98% pharma grade | AS-AC-FO-GR-283 | pending_review | Verified via product specs |
| Lactic Acid Technical | PO-SO-GR-A-715 | pending_review | Historical match confirmed |
| Maltodextrin-Pulver DE30 | coconut oil 25% tech grade | pending_review | Cross-referenced with transactions |
| CO-OI-70-701 | Palm Oil | auto_generated | Cross-referenced with transactions |
| SIG-92-RZH-LRHH | sodium chloride | auto_generated | Auto-mapped, validated |
| Vanguard Supply Co. | BA-SO-978 | unverified | Historical match confirmed |
| SIG-83-OBQ-GEIL GmbH | PR-SU-986 Ltd. | pending_review | Confirmed by domain expert |
| Glucose Syrup 99.5% Grade B | wheat gluten standard | pending_review | Auto-mapped, validated |
| IS-FO-GR-335 | sodium benzoate 70% | auto_generated | Historical match confirmed |
| Rapsöl 70% Qualitätsstufe II | Lactic Acid 98% Grade A | auto_generated | Verified via product specs |
| SIG-86-VCP-SVOL | Traubenzucker Qualitätsstufe I | pending_review | Confirmed by domain expert |
| CY-515 | Calcium Carbonate | auto_generated | Historical match confirmed |
| SIG-72-JEH-P5K7 | Natriumbenzoat Technische Qualität | pending_review | Auto-mapped, validated |
| Prime Partners | premier enterprise Holdings | pending_review | Verified via product specs |
| Sonnenblumenöl 98% | Coconut Oil 70% Grade A | auto_generated | Auto-mapped, validated |
| Lactic Acid | SIG-20-UMV-LJM6 | auto_generated | Historical match confirmed |
| SIG-69-UAZ-1ODW | Prime Materials | pending_review | Verified via product specs |
| SIG-14-WZC-EEWK | Sonnenblumenöl 70% Lebensmittelrein | pending_review | Auto-mapped, validated |
| lactic acid 98% | Dextrin Grade B | unverified | Verified via product specs |
| prism materials | PR-CH-808 AG | auto_generated | Historical match confirmed |
| Pinnacle Chemicals SA | Nexus Partners Group | unverified | Cross-referenced with transactions |
| SIG-69-TRZ-SFLQ | WI-B-10-442 | unverified | Verified via product specs |
| Resistente Stärke 25% Technische Qualität | SIG-52-CHY-4N5P | unverified | Cross-referenced with transactions |
| Natriumchlorid 99.5% Qualitätsstufe I | Wheat Gluten Grade A | unverified | Confirmed by domain expert |
| Elite Supply Co. | ME-SO-734 | unverified | Cross-referenced with transactions |
| coconut oil 25% food grade | Soy Isolate 50% Grade B | unverified | Confirmed by domain expert |
| FR-98-PR-250 | SIG-64-LXA-3LJO | pending_review | Cross-referenced with transactions |
| citric acid 98% | Palm Oil Grade B | auto_generated | Auto-mapped, validated |
| Vat Reduced NL 25% | Vat Reduced CN 15% | auto_generated | Auto-mapped, validated |
| CA-PR-568 | potassium sorbate | auto_generated | Cross-referenced with transactions |
| Elite Processing SA | ST-SU-950 SAS | pending_review | Cross-referenced with transactions |
| SIG-18-LLP-8GUU | Sorbinsäure | auto_generated | Verified via product specs |
| nexus partners Group | Quantum Enterprise NV | auto_generated | Cross-referenced with transactions |
| Ascorbic Acid | Ascorbic Acid Lebensmittelrein | auto_generated | Verified via product specs |
| SIG-72-HBS-JIQY | Customs Duty GB 7% | auto_generated | Auto-mapped, validated |
| SIG-86-XNZ-5Q7H | zenith partners | pending_review | Confirmed by domain expert |
| SIG-44-FWT-OA3N | glucose syrup tech grade | pending_review | Historical match confirmed |
| Isoglucose 50% Technical | citric acid 99.5% pharma grade | unverified | Confirmed by domain expert |
| Vat Reduced NL 25% | vat reduced nl 21% | pending_review | Historical match confirmed |
| Nexus Distribution PLC | prism chemicals GmbH | pending_review | Cross-referenced with transactions |
| SIG-39-MAR-LMVK | calcium carbonate food grade | pending_review | Historical match confirmed |
| SIG-52-FHA-5PI2 | Sodium Benzoate 98% | auto_generated | Verified via product specs |
| soy isolate 98% | Sodium Benzoate Grade B | pending_review | Cross-referenced with transactions |
| Calcium Carbonate 50% Grade B | SIG-91-GMY-Q91Y | unverified | Historical match confirmed |
| SIG-20-RSZ-19RE | Stellar Logistics | pending_review | Cross-referenced with transactions |
| FR-124 | SIG-91-WVE-3ESP | auto_generated | Confirmed by domain expert |
| Natriumbenzoat 50% | Dextrose Standard | pending_review | Cross-referenced with transactions |
| nexus processing AG | QU-IN-923 International | unverified | Auto-mapped, validated |
| Horizon Materials PLC | Elite Partners GmbH | auto_generated | Verified via product specs |
| citric acid 99.5% pharma grade | Potassium Sorbate | unverified | Auto-mapped, validated |
| Potassium Sorbate 98% | sodium benzoate 50% | auto_generated | Verified via product specs |
| SIG-89-HLJ-NILC | Catalyst Sourcing | auto_generated | Confirmed by domain expert |
| Baltic Distribution Group | SIG-85-CBK-XO7I | pending_review | Cross-referenced with transactions |
| stellar supply | Atlantic Logistik | auto_generated | Verified via product specs |
| Withholding NL 7% | SIG-88-YRN-7S19 | unverified | Confirmed by domain expert |
| Maltodextrin-Pulver DE25 | RE-ST-70-901 | auto_generated | Confirmed by domain expert |
| SIG-15-FOA-70S8 | potassium sorbate | auto_generated | Verified via product specs |
| SIG-82-DEO-X80R | calcium carbonate pharma grade | unverified | Confirmed by domain expert |
| DE-98-FO-GR-211 | SIG-80-MXD-T81P | unverified | Cross-referenced with transactions |
| Global Processing Holdings | SIG-16-ZDY-GYTX Holdings | pending_review | Confirmed by domain expert |
| maltodextrin de25 | Maltodextrin-Pulver DE25 | auto_generated | Confirmed by domain expert |
| Natriumbenzoat 25% | SIG-85-STS-67D6 | pending_review | Verified via product specs |
| Fructose Standardqualität | MA-DE-161 | unverified | Verified via product specs |
| Natriumchlorid Technische Qualität | SIG-17-LVE-03G9 | unverified | Confirmed by domain expert |
| Vat Standard DE 10% | Vat Reduced NL 19% | auto_generated | Cross-referenced with transactions |
| CI-AC-ST-836 | SIG-22-SKR-CTIC | unverified | Historical match confirmed |
| lactic acid tech grade | Soja Isolate Premiumqualität | auto_generated | Auto-mapped, validated |
| Vat Standardqualität FR 10% | SIG-90-NAM-FDV1 | pending_review | Verified via product specs |
| ascorbic acid food grade | SIG-88-AGF-FF5L | auto_generated | Historical match confirmed |
| DE-50-727 | Weizenklebereiweiß Lebensmittelrein | unverified | Auto-mapped, validated |
| Soja Isolate 25% | SIG-39-QZD-93EZ | pending_review | Cross-referenced with transactions |
| VE-IN-644 Ltd. | Premier Manufacturing NV | unverified | Confirmed by domain expert |
| ascorbic acid 50% tech grade | Soy Isolate 99.5% Premium | unverified | Auto-mapped, validated |
| Vat Standardqualität DE 19% | Vat Reduced NL 20% | auto_generated | Verified via product specs |
| Prime Rohstoffe LLC | PA-SU-946 Group | auto_generated | Auto-mapped, validated |
| Ascorbic Acid 98% Pharma Grade | Kasein 98% Qualitätsstufe II | pending_review | Verified via product specs |
| IS-230 | SIG-78-WDE-NNV9 | pending_review | Verified via product specs |
| Rapsöl 99.5% | AS-AC-70-133 | pending_review | Confirmed by domain expert |
| Baltic Enterprise Holdings | SIG-98-OXJ-W0H6 SAS | pending_review | Cross-referenced with transactions |
| Excise DE 10% | VA-RE-N-7-243 | auto_generated | Confirmed by domain expert |
| Vat Standardqualität GB 21% | Vat Standard NL 20% | pending_review | Auto-mapped, validated |
| Lactic Acid 99.5% Qualitätsstufe II | Pea Protein | pending_review | Verified via product specs |
| Quantum Verarbeitung PLC | Stellar Manufacturing Holdings | unverified | Auto-mapped, validated |
| Apex Trading Holdings | nordic logistics Group | pending_review | Historical match confirmed |
| Central Logistics | Zenith Versorgung GmbH | auto_generated | Cross-referenced with transactions |
| Rapeseed Oil | LA-AC-FO-GR-553 | unverified | Cross-referenced with transactions |
| fructose 25% | MA-DE-859 | unverified | Cross-referenced with transactions |
| FR-GR-B-311 | calcium carbonate 99.5% | auto_generated | Auto-mapped, validated |
| DE-GR-A-250 | Natriumbenzoat | auto_generated | Cross-referenced with transactions |
| SIG-53-NHM-OFA2 | ST-DI-782 SA | auto_generated | Cross-referenced with transactions |
| vanguard industries AG | Baltic Versorgung | auto_generated | Historical match confirmed |
| premier supply PLC | ST-PA-504 | auto_generated | Historical match confirmed |
| Dextrin | citric acid 99.5% | auto_generated | Historical match confirmed |
| SIG-40-MRL-94W6 | Palmfett Qualitätsstufe II | auto_generated | Historical match confirmed |
| Nexus Werkstoffe | Pinnacle Sourcing | pending_review | Historical match confirmed |
| Baltic Chemicals AG | baltic chemicals AG | auto_generated | Verified via product specs |
| Atlantic Versorgung GmbH | core supply | auto_generated | Confirmed by domain expert |
| Traubenzucker 99.5% Standardqualität | CO-OI-98-GR-A-763 | auto_generated | Auto-mapped, validated |
| isoglucose 70% | RA-OI-TE-584 | pending_review | Verified via product specs |
| LA-AC-165 | glucose syrup | auto_generated | Cross-referenced with transactions |
| Sodium Benzoate 50% Technical | Glukosesirup Syrup Qualitätsstufe I | pending_review | Historical match confirmed |
| Catalyst Commodities | vertex logistics Holdings | unverified | Verified via product specs |
| sorbic acid food grade | Sodium Chloride | unverified | Historical match confirmed |
| maltodextrin de10 | Traubenzucker 25% | unverified | Cross-referenced with transactions |
| Atlas Logistik | SIG-48-BCW-76F8 | auto_generated | Verified via product specs |
| Meridian Chemicals International | Core Chemicals AG | unverified | Verified via product specs |
| Nexus Materials | premier supply | unverified | Auto-mapped, validated |
| RE-ST-PR-679 | Potassium Sorbate | pending_review | Historical match confirmed |
| prism partners Holdings | Atlas Handel SARL | unverified | Verified via product specs |
| SIG-76-RKG-E8RT | Kasein | unverified | Auto-mapped, validated |
| DE-GR-B-244 | SIG-32-TTU-44MW | pending_review | Confirmed by domain expert |
| Sorbinsäure 70% | SIG-31-IKO-T2D8 | auto_generated | Historical match confirmed |
| potassium sorbate | SIG-29-BJH-NXI0 | pending_review | Historical match confirmed |
| SIG-50-BJQ-W54O Holdings | Catalyst Industries | pending_review | Cross-referenced with transactions |
| atlas supply | AT-SU-CO-707 | auto_generated | Historical match confirmed |
| SIG-41-ZTZ-VNMI Holdings | meridian industries | unverified | Cross-referenced with transactions |
| Quantum Sourcing | Nexus Werkstoffe | auto_generated | Verified via product specs |
| SIG-99-JMF-1NOQ | rapeseed oil tech grade | pending_review | Confirmed by domain expert |
| SO-AC-PH-GR-620 | Sodium Chloride Technical | pending_review | Confirmed by domain expert |
| SIG-93-VLZ-VI4P | customs duty gb 7% | unverified | Verified via product specs |
| Vertex Sourcing | SIG-50-QSV-L15R | pending_review | Cross-referenced with transactions |
| CU-DU-D-0-955 | vat reduced gb 15% | auto_generated | Historical match confirmed |
| SIG-71-KJM-D5G1 Holdings | Apex Ingredients KG | pending_review | Auto-mapped, validated |
| SIG-38-VFI-SR88 Corp. | CE-TR-144 International | pending_review | Confirmed by domain expert |
| sodium benzoate | PO-SO-GR-A-715 | unverified | Confirmed by domain expert |
| Soja Isolate 25% | SIG-60-IRZ-OTKZ | unverified | Auto-mapped, validated |
| NE-LO-125 | Elite Werkstoffe | pending_review | Verified via product specs |
| Zenith Handel AG | Central Manufacturing Holdings | unverified | Verified via product specs |
| AS-AC-70-347 | Resistente Stärke | pending_review | Cross-referenced with transactions |
| Central Sourcing | SIG-22-HSE-KSCU | auto_generated | Auto-mapped, validated |
| Zenith Verarbeitung | pacific industries International | auto_generated | Verified via product specs |
| sodium benzoate | CO-OI-FO-GR-162 | auto_generated | Cross-referenced with transactions |
| resistant starch | SO-AC-FO-GR-175 | unverified | Verified via product specs |
| SIG-36-JLA-CSEN | Citric Acid | unverified | Auto-mapped, validated |
| Elite Chemicals AG | SIG-14-WWQ-VPK2 SARL | pending_review | Auto-mapped, validated |
| vanguard industries Inc. | VE-SO-914 Ltd. | auto_generated | Confirmed by domain expert |
| CA-98-PR-260 | SIG-76-YLU-7DL9 | auto_generated | Cross-referenced with transactions |
| SIG-32-TTU-44MW | Natriumbenzoat Technische Qualität | unverified | Confirmed by domain expert |
| SIG-53-XQL-BVVB | soy isolate premium | auto_generated | Auto-mapped, validated |
| SIG-56-END-D8WH | VE-CO-558 | auto_generated | Auto-mapped, validated |
| Natriumbenzoat | SIG-85-FIY-2QW4 | unverified | Confirmed by domain expert |
| Customs Duty NL 15% | Excise DE 10% | auto_generated | Confirmed by domain expert |
| SO-IS-99.5-141 | pea protein 99.5% | unverified | Historical match confirmed |
| NO-DI-180 Ltd. | core processing Group | auto_generated | Cross-referenced with transactions |
| Fructose Standardqualität | RE-ST-99.5-242 | unverified | Verified via product specs |
| SIG-52-LQX-X1DO | Palm Oil Pharma Grade | unverified | Auto-mapped, validated |
| Vanguard Partners PLC | SIG-11-LPV-TM1Q International | unverified | Cross-referenced with transactions |
| Isoglucose | ascorbic acid food grade | pending_review | Auto-mapped, validated |
| Zitronensäure Standardqualität | Potassium Sorbate Standard | pending_review | Historical match confirmed |
| resistant starch | SIG-81-SBE-HL1C | unverified | Verified via product specs |
| Global Trading Ltd. | Global Handel Ltd. | pending_review | Historical match confirmed |
| SIG-70-IET-75TA | Vat Reduced US 21% | unverified | Historical match confirmed |
| SIG-32-RJE-L1OT | Calcium Carbonate 50% Pharma Grade | auto_generated | Auto-mapped, validated |
| SIG-98-PIN-G89V | Horizon Chemicals PLC | auto_generated | Historical match confirmed |
| SIG-13-ZRN-WZGO | PR-MA-686 | pending_review | Auto-mapped, validated |
| Premier Versorgung GmbH | Continental Sourcing | auto_generated | Verified via product specs |
| stratos logistics | Pacific Sourcing | auto_generated | Cross-referenced with transactions |
| sodium benzoate | Potassium Sorbate | unverified | Historical match confirmed |
| CE-MA-997 KG | pacific distribution | pending_review | Confirmed by domain expert |
| atlas supply | Quantum Versorgung GmbH | pending_review | Auto-mapped, validated |
| SIG-41-YLB-IZED | Resistente Stärke | unverified | Historical match confirmed |
| Sodium Benzoate 99.5% Technical | SO-CH-758 | auto_generated | Verified via product specs |
| Lactic Acid Standardqualität | CO-OI-966 | unverified | Verified via product specs |
| EX-B-21-936 | Customs Duty US 15% | auto_generated | Historical match confirmed |
| Rapeseed Oil Grade A | SIG-23-IEJ-V2T3 | pending_review | Confirmed by domain expert |
| SIG-84-MUG-BUXR | Elite Logistics | auto_generated | Historical match confirmed |
| quantum processing International | SIG-99-CTB-8OFG Group | unverified | Auto-mapped, validated |
| Zitronensäure Technische Qualität | Dextrose 25% Technical | unverified | Cross-referenced with transactions |
| Stratos Sourcing | PR-MA-295 | auto_generated | Verified via product specs |
| SIG-18-IQS-O98Z SA | Global Materials NV | pending_review | Auto-mapped, validated |
| LA-AC-891 | Dextrin 70% | unverified | Cross-referenced with transactions |
| SIG-42-BEO-614U | Weizenklebereiweiß Standardqualität | pending_review | Auto-mapped, validated |
| SIG-81-LVQ-2J60 | Quantum Ingredients | pending_review | Historical match confirmed |
| Weizenklebereiweiß 70% | Palm Oil 70% | pending_review | Verified via product specs |
| Resistant Starch 70% Food Grade | Cyclodextrin | auto_generated | Verified via product specs |
| Nordic Logistik PLC | SIG-95-HLU-HD5X GmbH | pending_review | Historical match confirmed |
| SIG-16-YRD-5C3Z | soy isolate 25% tech grade | auto_generated | Auto-mapped, validated |
| Fructose | dextrose | unverified | Verified via product specs |
| Calcium Carbonate | SIG-40-OEJ-4XCR | unverified | Confirmed by domain expert |
| SIG-42-IEF-RFC9 | Sorbinsäure Qualitätsstufe II | auto_generated | Confirmed by domain expert |
| Sodium Benzoate Grade A | CI-AC-PH-GR-209 | pending_review | Confirmed by domain expert |
| LA-AC-GR-A-949 | Glukosesirup Syrup Lebensmittelrein | pending_review | Historical match confirmed |
| stratos partners SA | Pinnacle Industrien LLC | pending_review | Historical match confirmed |
| isoglucose | Citric Acid 99.5% Pharma Grade | pending_review | Confirmed by domain expert |
| Lactic Acid | Ascorbic Acid | pending_review | Auto-mapped, validated |
| Continental Logistics | HO-SU-CO-454 | pending_review | Verified via product specs |
| Nordic Versorgung GmbH | AT-MA-127 | unverified | Verified via product specs |
| Vat Standardqualität IN 20% | WI-G-21-298 | auto_generated | Cross-referenced with transactions |
| SIG-32-RJE-L1OT | Isoglucose 70% | pending_review | Cross-referenced with transactions |
| SIG-83-OTU-QZB6 | Kasein 50% Premiumqualität | pending_review | Verified via product specs |
| casein | SIG-25-ABB-2SBA | auto_generated | Auto-mapped, validated |
| Maltodextrin DE5 Grade A | pea protein standard | unverified | Cross-referenced with transactions |
| SIG-16-ZDY-GYTX Holdings | ST-DI-183 Inc. | auto_generated | Confirmed by domain expert |
| Catalyst Commodities SAS | Atlantic Rohstoffe GmbH | auto_generated | Cross-referenced with transactions |
| Natriumbenzoat 70% Premiumqualität | SO-IS-25-ST-345 | unverified | Auto-mapped, validated |
| CO-OI-977 | Maltodextrin-Pulver DE10 | unverified | Historical match confirmed |
| PR-LO-862 | Stellar Logistics | auto_generated | Confirmed by domain expert |
| Dextrin Technische Qualität | Glucose Syrup 99.5% Food Grade | auto_generated | Auto-mapped, validated |
| wheat gluten pharma grade | SO-IS-99.5-141 | auto_generated | Historical match confirmed |
| GL-SO-534 Holdings | Premier Materials SAS | pending_review | Verified via product specs |
| SO-AC-340 | ascorbic acid pharma grade | pending_review | Cross-referenced with transactions |
| Central Logistics | Zenith Sourcing | unverified | Historical match confirmed |
| CO-SU-411 | apex chemicals International | unverified | Auto-mapped, validated |
| Soy Isolate Food Grade | SIG-16-LZG-DGBK | auto_generated | Cross-referenced with transactions |
| Wheat Gluten 50% Pharma Grade | SIG-13-WHV-DDIN | auto_generated | Auto-mapped, validated |
| Quantum Chemicals | CO-PA-491 BV | pending_review | Verified via product specs |
| Sodium Benzoate 25% | dextrin 70% pharma grade | auto_generated | Verified via product specs |
| WI-I-10-242 | Vat Standardqualität NL 20% | unverified | Verified via product specs |
| vertex enterprise Holdings | SIG-59-HNQ-A8N5 Ltd. | unverified | Auto-mapped, validated |
| Continental Sourcing | SIG-79-UGU-7OFC | pending_review | Verified via product specs |
| glucose syrup | Natriumchlorid Technische Qualität | auto_generated | Cross-referenced with transactions |
| catalyst materials | Stellar Logistik | unverified | Confirmed by domain expert |
| atlas sourcing | PR-LO-704 | unverified | Cross-referenced with transactions |
| CA-CA-25-PH-GR-684 | SIG-86-VGU-A4FE | auto_generated | Cross-referenced with transactions |
| SO-IS-99.5-GR-A-499 | Glucose Syrup Food Grade | pending_review | Verified via product specs |
| SIG-19-TLQ-1P5Z | coconut oil 98% tech grade | auto_generated | Verified via product specs |
| SIG-45-NEB-M5RE | excise in 7% | unverified | Cross-referenced with transactions |
| SIG-48-BCI-7SYR | VA-RE-N-10-232 | pending_review | Cross-referenced with transactions |
| potassium sorbate 50% tech grade | SIG-45-ZTJ-PA16 | unverified | Verified via product specs |
| RE-ST-223 | Kasein 98% Qualitätsstufe II | unverified | Historical match confirmed |
| SIG-93-CZZ-ZGWF | Prism Materials | auto_generated | Historical match confirmed |
| SU-OI-ST-338 | SIG-88-EEY-HOGD | pending_review | Confirmed by domain expert |
| Traubenzucker Technische Qualität | coconut oil | pending_review | Verified via product specs |
| central logistics Group | PA-MA-672 | unverified | Auto-mapped, validated |
| Fructose | SIG-11-RGJ-D3IR | auto_generated | Historical match confirmed |
| withholding nl 20% | Excise US 20% | auto_generated | Cross-referenced with transactions |
| AP-LO-246 | Prism Sourcing | unverified | Auto-mapped, validated |
| ascorbic acid 50% tech grade | Kaliumsorbat | unverified | Verified via product specs |
| stratos materials Group | SIG-17-GFH-X0JO PLC | unverified | Verified via product specs |
| SIG-75-XMY-5X1F | resistant starch | auto_generated | Auto-mapped, validated |
| lactic acid food grade | RE-ST-676 | unverified | Cross-referenced with transactions |
| ME-SU-CO-314 | core supply | pending_review | Auto-mapped, validated |
| Stratos Sourcing | SIG-52-ERT-6O1N | auto_generated | Verified via product specs |
| customs duty br 20% | Excise NL 20% | unverified | Cross-referenced with transactions |
| Soy Isolate 25% | sunflower oil | auto_generated | Historical match confirmed |
| MA-DE-PR-303 | Lactic Acid | unverified | Historical match confirmed |
| Soy Isolate Premium | SIG-36-XEW-9SSB | unverified | Historical match confirmed |
| sodium benzoate 99.5% | Sorbic Acid Pharma Grade | auto_generated | Auto-mapped, validated |
| Casein Grade A | Resistente Stärke Technische Qualität | pending_review | Verified via product specs |
| HO-IN-142 AG | Stratos Processing | unverified | Auto-mapped, validated |
| Pea Protein Grade A | maltodextrin de25 | auto_generated | Historical match confirmed |
| Atlantic Manufacturing | SIG-63-OTU-T27J Corp. | auto_generated | Auto-mapped, validated |
| ascorbic acid standard | IS-50-GR-A-791 | pending_review | Verified via product specs |
| Soja Isolate 99.5% | SIG-60-KAS-IVMD | pending_review | Historical match confirmed |
| SIG-15-NIP-N1UH | Citric Acid Standard | pending_review | Historical match confirmed |
| Zenith Manufacturing PLC | Vertex Vertrieb Group | pending_review | Confirmed by domain expert |
| Nordic Ingredients | NE-DI-555 | pending_review | Auto-mapped, validated |
| Pinnacle Solutions | SIG-72-JWR-R2ZI BV | pending_review | Verified via product specs |
| SIG-58-LWY-Q8P6 | Kasein | unverified | Verified via product specs |
| ME-LO-731 | Quantum Versorgung GmbH | pending_review | Cross-referenced with transactions |
| SIG-24-CXH-R2TY | AS-AC-439 | pending_review | Cross-referenced with transactions |
| VA-RE-I-20-892 | vat reduced nl 0% | pending_review | Confirmed by domain expert |
| SIG-86-XNZ-5Q7H | zenith partners | unverified | Confirmed by domain expert |
| MA-DE-ST-267 | SIG-85-FIY-2QW4 | unverified | Cross-referenced with transactions |
| Continental Sourcing | AT-SO-790 | pending_review | Confirmed by domain expert |
| SIG-58-FIB-X69X | Dextrose | auto_generated | Verified via product specs |
| RE-ST-GR-B-805 | Weizenklebereiweiß 25% Premiumqualität | unverified | Verified via product specs |
| SIG-82-AKA-U48G | Calcium Carbonate 50% Qualitätsstufe II | auto_generated | Historical match confirmed |
| SIG-56-BPD-M0A6 | coconut oil pharma grade | pending_review | Historical match confirmed |
| HO-DI-531 Group | Stratos Chemicals | auto_generated | Historical match confirmed |
| prism industries Corp. | SIG-77-WCC-DNFC Holdings | unverified | Historical match confirmed |
| Sodium Chloride | SIG-24-MFK-ZAUG | auto_generated | Cross-referenced with transactions |
| QU-DI-467 Holdings | SIG-57-LIL-I8Z3 Inc. | auto_generated | Confirmed by domain expert |
| wheat gluten | FR-99.5-TE-779 | unverified | Confirmed by domain expert |
| Rapsöl 25% Lebensmittelrein | Sodium Chloride 98% | unverified | Historical match confirmed |
| SO-CH-99.5-GR-A-634 | Traubenzucker 70% | unverified | Cross-referenced with transactions |
| VA-RE-C-21-521 | SIG-22-ADK-3T78 | unverified | Historical match confirmed |
| SIG-40-KVV-E07S | citric acid standard | pending_review | Auto-mapped, validated |
| WI-N-21-724 | excise gb 5% | pending_review | Confirmed by domain expert |
| Stratos Supply | vertex enterprise Group | pending_review | Verified via product specs |
| Sodium Chloride 25% Premium | SIG-86-VGU-A4FE | unverified | Verified via product specs |
| SIG-52-LXJ-ZU4J | Baltic Logistics | auto_generated | Cross-referenced with transactions |
| Nordic Logistics | EL-PR-129 Ltd. | auto_generated | Confirmed by domain expert |
| SIG-41-HMT-W0GK | Dextrin | pending_review | Cross-referenced with transactions |
| apex logistics | SIG-78-QOY-5RIX | auto_generated | Confirmed by domain expert |
| Palmfett 99.5% Qualitätsstufe I | citric acid | auto_generated | Verified via product specs |
| continental ingredients AG | Prism Partners | unverified | Verified via product specs |
| Core Sourcing | SIG-65-QBD-QZJW | unverified | Confirmed by domain expert |
| Coconut Oil 70% Qualitätsstufe I | SIG-76-YLU-7DL9 | pending_review | Verified via product specs |
| DE-98-512 | Casein Standard | auto_generated | Cross-referenced with transactions |
| customs duty cn 7% | Customs Duty DE 20% | pending_review | Confirmed by domain expert |
| SIG-89-PTG-ZQNK | LA-AC-FO-GR-469 | auto_generated | Cross-referenced with transactions |
| meridian industries | SIG-32-VLW-1KKT NV | unverified | Auto-mapped, validated |
| sorbic acid food grade | Kasein Qualitätsstufe I | pending_review | Cross-referenced with transactions |
| nordic processing SAS | NE-TR-634 International | auto_generated | Cross-referenced with transactions |
| vat reduced us 10% | Withholding NL 5% | unverified | Historical match confirmed |
| WI-G-5-718 | Excise GB 19% | auto_generated | Cross-referenced with transactions |
| Weizenklebereiweiß Qualitätsstufe I | Sodium Benzoate 50% | unverified | Historical match confirmed |
| Kaliumsorbat Technische Qualität | SIG-40-KVV-E07S | auto_generated | Cross-referenced with transactions |
| Pinnacle Trading | Nexus Rohstoffe Group | auto_generated | Cross-referenced with transactions |
| Lactic Acid Food Grade | lactic acid | pending_review | Verified via product specs |
| SO-BE-700 | Sorbinsäure | auto_generated | Confirmed by domain expert |
| SIG-72-YEU-SCIQ | Isoglucose 70% Food Grade | unverified | Cross-referenced with transactions |
| SIG-68-SJS-K3N3 | atlantic trading BV | pending_review | Cross-referenced with transactions |
| Sodium Chloride Standard | Sorbinsäure 50% | auto_generated | Cross-referenced with transactions |
| Pacific Logistics | SIG-49-MMU-1GJR | auto_generated | Confirmed by domain expert |
| SU-OI-50-GR-A-521 | calcium carbonate standard | pending_review | Confirmed by domain expert |
| CO-OI-70-GR-A-633 | Soy Isolate 25% Pharma Grade | pending_review | Verified via product specs |
| Casein 50% Premium | sodium benzoate | auto_generated | Confirmed by domain expert |
| SIG-11-SLQ-KF5B | Sorbinsäure 98% | auto_generated | Auto-mapped, validated |
| SIG-91-GKA-MSWV | Vanguard Logistik | pending_review | Cross-referenced with transactions |
| Continental Versorgung GmbH | SIG-68-BPW-3DSD | pending_review | Historical match confirmed |
| SIG-69-MPP-WUGO | ME-TR-587 | unverified | Historical match confirmed |
| Vat Reduced BR 7% | Vat Reduced CN 5% | unverified | Historical match confirmed |
| Dextrin Premium | Calcium Carbonate 98% | auto_generated | Cross-referenced with transactions |
| Potassium Sorbate | MA-DE-335 | pending_review | Auto-mapped, validated |
| Pea Protein Standardqualität | Maltodextrin DE15 | unverified | Historical match confirmed |
| Continental Sourcing | SIG-47-MLZ-TPP5 | auto_generated | Historical match confirmed |
| Zitronensäure 98% | SIG-47-GAT-ET7B | pending_review | Cross-referenced with transactions |
| SIG-12-OAV-ALF4 | CI-AC-PR-827 | auto_generated | Confirmed by domain expert |
| Sodium Benzoate Pharma Grade | GL-SY-98-FO-GR-198 | auto_generated | Verified via product specs |
| Potassium Sorbate | SIG-53-LJE-NZKR | unverified | Historical match confirmed |
| customs duty nl 15% | VA-RE-G-0-937 | unverified | Historical match confirmed |
| WH-GL-830 | Ascorbic Acid 98% Qualitätsstufe II | pending_review | Historical match confirmed |
| PE-PR-163 | Coconut Oil Lebensmittelrein | auto_generated | Historical match confirmed |
| SIG-76-GST-OWGM | Citric Acid 25% Grade A | auto_generated | Auto-mapped, validated |
| cyclodextrin food grade | SIG-98-ZFI-37SU | pending_review | Auto-mapped, validated |
| nordic sourcing | Nexus Logistik | unverified | Cross-referenced with transactions |
| Pea Protein | sodium benzoate 99.5% standard | unverified | Auto-mapped, validated |
| SIG-77-WZV-TKWL | pinnacle sourcing | unverified | Auto-mapped, validated |
| Central Partners | continental distribution International | unverified | Historical match confirmed |
| Calcium Carbonate 50% Qualitätsstufe II | sodium benzoate 99.5% premium | pending_review | Historical match confirmed |
| Atlas Supply Co. | SIG-92-WPI-MU2K | pending_review | Verified via product specs |
| SO-IS-99.5-GR-A-499 | Kasein | unverified | Cross-referenced with transactions |
| premier supply | ST-LO-378 | auto_generated | Cross-referenced with transactions |
| ST-TR-590 | Premier Trading SA | unverified | Auto-mapped, validated |
| VA-EN-308 | SIG-12-JYK-S9KT Group | pending_review | Confirmed by domain expert |
| Kasein 50% Premiumqualität | DE-ST-999 | pending_review | Historical match confirmed |
| VA-ST-N-20-162 | SIG-74-EPP-R9AG | auto_generated | Historical match confirmed |
| Fructose 99.5% Food Grade | SIG-83-OTU-QZB6 | pending_review | Verified via product specs |
| SIG-30-UET-0Q2O | resistant starch standard | pending_review | Verified via product specs |
| Elite Sourcing | stratos logistics | pending_review | Cross-referenced with transactions |
| LA-AC-25-PR-377 | SIG-45-CWR-EI9N | pending_review | Verified via product specs |
| PA-OI-983 | SIG-51-IYK-630P | auto_generated | Auto-mapped, validated |
| Vat Reduced GB 25% | Customs Duty DE 0% | unverified | Auto-mapped, validated |
| continental ingredients AG | SIG-28-FYV-P1ZR Group | unverified | Cross-referenced with transactions |
| Lactic Acid 98% Premium | coconut oil 25% food grade | unverified | Confirmed by domain expert |
| Sodium Benzoate 50% | SIG-47-GAT-ET7B | unverified | Verified via product specs |
| SO-BE-70-PR-120 | wheat gluten standard | pending_review | Auto-mapped, validated |
| calcium carbonate 98% pharma grade | Traubenzucker Pharmazeutisch rein | unverified | Auto-mapped, validated |
| Natriumbenzoat Premiumqualität | SIG-29-RWA-CHL8 | unverified | Confirmed by domain expert |
| LA-AC-893 | Kaliumsorbat 98% Qualitätsstufe II | unverified | Cross-referenced with transactions |
| Casein 50% Premium | SIG-85-SIL-CNEA | pending_review | Verified via product specs |
| Core Logistics Holdings | Vanguard Enterprise | pending_review | Historical match confirmed |
| Cyclodextrin | LA-AC-70-PH-GR-221 | auto_generated | Historical match confirmed |
| sorbic acid premium | Sodium Benzoate 50% | unverified | Auto-mapped, validated |
| Sunflower Oil Standard | Weizenklebereiweiß | unverified | Confirmed by domain expert |
| Pacific Vertrieb Group | Continental Enterprise KG | auto_generated | Auto-mapped, validated |
| pea protein tech grade | CA-CA-GR-B-565 | unverified | Auto-mapped, validated |
| Elite Chemicals AG | SIG-77-TQY-IC8H Holdings | unverified | Auto-mapped, validated |
| Vanguard Ingredients | Quantum Ingredients | pending_review | Historical match confirmed |
| Resistant Starch 50% | SIG-38-YTD-7BST | pending_review | Verified via product specs |
| dextrose | Traubenzucker 50% Qualitätsstufe II | pending_review | Confirmed by domain expert |
| premier chemicals KG | Nordic Ingredients | auto_generated | Confirmed by domain expert |
| SIG-40-CXK-QT2E Group | continental solutions | pending_review | Cross-referenced with transactions |
| SIG-94-MGT-4WYA | Citric Acid 70% | unverified | Confirmed by domain expert |
| SIG-83-OTU-QZB6 | Glucose Syrup 98% | unverified | Auto-mapped, validated |
| Natriumchlorid 98% | Resistant Starch | unverified | Confirmed by domain expert |
| stratos sourcing | SIG-87-LPT-3ADB | unverified | Historical match confirmed |
| PO-SO-196 | sodium benzoate 99.5% | unverified | Cross-referenced with transactions |
| ST-MA-730 | SIG-60-VTH-H7AM | auto_generated | Auto-mapped, validated |
| SIG-30-NQN-ZENP | Catalyst Logistics SA | pending_review | Confirmed by domain expert |
| Nexus Distribution PLC | PR-CH-808 AG | pending_review | Cross-referenced with transactions |
| soy isolate | Soja Isolate Standardqualität | auto_generated | Auto-mapped, validated |
| resistant starch 50% | CA-CA-GR-B-565 | auto_generated | Verified via product specs |
| Maltodextrin DE15 | sodium benzoate 50% | pending_review | Confirmed by domain expert |
| Stellar Logistik | SIG-31-JNR-6FQ9 | auto_generated | Confirmed by domain expert |
| Stratos Rohstoffe Inc. | pinnacle processing | auto_generated | Cross-referenced with transactions |
| calcium carbonate | Fructose Grade A | pending_review | Confirmed by domain expert |
| Meridian Materials | Nexus Werkstoffe | pending_review | Cross-referenced with transactions |
| GL-DI-754 | Pacific Industries Holdings | pending_review | Cross-referenced with transactions |
| SIG-13-CGO-2Y4L | Resistant Starch 50% | auto_generated | Cross-referenced with transactions |
| dextrose 25% tech grade | SIG-78-OGT-WEKQ | unverified | Auto-mapped, validated |
| Resistente Stärke 50% Standardqualität | SO-BE-ST-871 | pending_review | Cross-referenced with transactions |
| Cyclodextrin 70% Food Grade | PO-SO-98-216 | unverified | Confirmed by domain expert |
| Excise NL 19% | customs duty de 5% | pending_review | Confirmed by domain expert |
| SIG-71-FNO-CX9K | Soja Isolate Pharmazeutisch rein | pending_review | Verified via product specs |
| Kaliumsorbat Standardqualität | CO-OI-977 | auto_generated | Auto-mapped, validated |
| NO-IN-797 | nexus ingredients Ltd. | auto_generated | Historical match confirmed |
| sodium benzoate | SO-BE-FO-GR-835 | auto_generated | Confirmed by domain expert |
| soy isolate 99.5% | Fructose | pending_review | Historical match confirmed |
| zenith supply | Baltic Supply Co. | auto_generated | Cross-referenced with transactions |
| SO-IS-98-880 | palm oil 98% | auto_generated | Confirmed by domain expert |
| VE-LO-902 Group | SIG-14-HVI-T0Z6 SARL | auto_generated | Confirmed by domain expert |
| Vat Reduced GB 0% | vat reduced us 21% | auto_generated | Historical match confirmed |
| Ascorbic Acid | isoglucose 70% food grade | unverified | Verified via product specs |
| PA-SO-568 | SIG-49-MMU-1GJR | auto_generated | Historical match confirmed |
| withholding nl 15% | CU-DU-N-5-217 | pending_review | Auto-mapped, validated |
| Lactic Acid 99.5% | lactic acid standard | pending_review | Cross-referenced with transactions |
| NE-SU-335 | SIG-70-SAQ-KIAC | pending_review | Cross-referenced with transactions |
| Fructose Food Grade | CI-AC-538 | unverified | Verified via product specs |
| nordic distribution AG | SIG-53-NHM-OFA2 | unverified | Auto-mapped, validated |
| CO-CO-290 BV | continental solutions SARL | pending_review | Verified via product specs |
| SIG-47-AWI-4RQV | Dextrose | unverified | Confirmed by domain expert |
| Weizenklebereiweiß Qualitätsstufe I | SO-IS-FO-GR-437 | unverified | Cross-referenced with transactions |
| SIG-17-IQV-FES7 | Casein Standard | unverified | Cross-referenced with transactions |
| vertex logistics | Elite Werkstoffe | pending_review | Confirmed by domain expert |
| Zenith Sourcing | Atlantic Supply Co. | unverified | Auto-mapped, validated |
| QU-SU-CO-890 | apex supply | pending_review | Cross-referenced with transactions |
| HO-LO-699 | SIG-98-OYH-5RPI | auto_generated | Historical match confirmed |
| maltodextrin de5 standard | Calcium Carbonate 70% Premiumqualität | unverified | Verified via product specs |
| Rapsöl 98% | SIG-61-MHS-BQG3 | pending_review | Auto-mapped, validated |
| CO-SO-101 | Stratos Logistik | unverified | Cross-referenced with transactions |
| Quantum Trading | Vertex Ingredients | pending_review | Auto-mapped, validated |
| Atlas Logistics | atlas materials | unverified | Verified via product specs |
| PE-PR-929 | Dextrose 25% | unverified | Historical match confirmed |
| customs duty br 7% | Vat Reduced BR 7% | auto_generated | Auto-mapped, validated |
| SIG-89-PGD-QMHH GmbH | Pacific Logistik | pending_review | Cross-referenced with transactions |
| zenith materials | Continental Manufacturing | auto_generated | Confirmed by domain expert |
| Natriumchlorid | rapeseed oil 70% premium | pending_review | Auto-mapped, validated |
| Fructose | Soy Isolate Technical | pending_review | Auto-mapped, validated |
| Maltodextrin DE20 | SO-BE-25-ST-520 | auto_generated | Cross-referenced with transactions |
| CU-DU-N-7-394 | vat reduced gb 19% | pending_review | Auto-mapped, validated |
| SIG-61-CIV-LFWA | CA-CA-99.5-FO-GR-839 | auto_generated | Cross-referenced with transactions |
| PR-SO-441 | SIG-89-YWW-NUVL | unverified | Verified via product specs |
| Palmfett 70% Technische Qualität | Sodium Chloride 70% | pending_review | Cross-referenced with transactions |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | Wheat Gluten | unverified | Confirmed by domain expert |
| CA-50-GR-B-203 | SIG-68-XQK-6G5I | unverified | Auto-mapped, validated |
| Meridian Logistik SAS | premier supply | unverified | Historical match confirmed |
| CY-PH-GR-870 | coconut oil 25% standard | pending_review | Auto-mapped, validated |
| SIG-90-SZM-PZJ4 | Dextrin | auto_generated | Verified via product specs |
| Nexus Sourcing | atlantic materials | pending_review | Confirmed by domain expert |
| resistant starch | SIG-10-DWM-ZA0C | auto_generated | Cross-referenced with transactions |
| CA-CA-GR-B-565 | SIG-89-TVE-WANI | auto_generated | Confirmed by domain expert |
| Customs Duty US 20% | WI-I-10-242 | pending_review | Auto-mapped, validated |
| Core Sourcing | Stratos Werkstoffe | pending_review | Auto-mapped, validated |
| Traubenzucker Standardqualität | sodium benzoate 99.5% tech grade | auto_generated | Auto-mapped, validated |
| SIG-33-YPL-RQCS | Vertex Materials | pending_review | Verified via product specs |
| Pinnacle Verarbeitung | VE-IN-811 | auto_generated | Auto-mapped, validated |
| baltic materials | Nordic Supply Co. | unverified | Confirmed by domain expert |
| Pea Protein 70% Lebensmittelrein | Casein | auto_generated | Verified via product specs |
| Pinnacle Distribution | Catalyst Industrien SARL | auto_generated | Auto-mapped, validated |
| VE-SU-CO-566 | Vertex Logistics | pending_review | Cross-referenced with transactions |
| FR-GR-A-600 | casein | unverified | Confirmed by domain expert |
| SIG-95-EES-2FE9 | Fructose Standardqualität | pending_review | Confirmed by domain expert |
| Soja Isolate | pea protein standard | auto_generated | Historical match confirmed |
| SIG-44-HRR-WZP6 | Glucose Syrup 70% | unverified | Historical match confirmed |
| Elite Materials | Atlas Versorgung GmbH | auto_generated | Verified via product specs |
| VE-CO-558 | premier commodities Holdings | unverified | Historical match confirmed |
| Vertex Ingredients GmbH | Vanguard Logistics | pending_review | Verified via product specs |
| Zitronensäure Standardqualität | SIG-89-ISH-EQW6 | unverified | Cross-referenced with transactions |
| Weizenklebereiweiß 99.5% Qualitätsstufe I | SIG-39-FND-AALU | auto_generated | Confirmed by domain expert |
| SIG-39-EWA-Q37M | Quantum Supply Co. | auto_generated | Verified via product specs |
| VA-LO-948 | Baltic Manufacturing | auto_generated | Historical match confirmed |
| Soy Isolate | citric acid standard | auto_generated | Auto-mapped, validated |
| Stratos Commodities International | Quantum Handel Group | pending_review | Confirmed by domain expert |
| SIG-79-OZQ-4I2N | IS-614 | pending_review | Historical match confirmed |
| SO-CH-99.5-618 | Soja Isolate 98% | auto_generated | Confirmed by domain expert |
| casein pharma grade | SO-CH-FO-GR-642 | unverified | Verified via product specs |
| ME-SO-760 GmbH | Continental Processing Group | pending_review | Confirmed by domain expert |
| Cyclodextrin 98% Pharmazeutisch rein | AS-AC-ST-686 | unverified | Confirmed by domain expert |
| CO-MA-863 | catalyst industries SAS | unverified | Cross-referenced with transactions |
| Soja Isolate 98% Premiumqualität | SIG-41-YLB-IZED | pending_review | Verified via product specs |
| Vat Standard NL 25% | SIG-74-ZNA-1VYW | pending_review | Cross-referenced with transactions |
| RE-ST-GR-B-805 | Wheat Gluten Food Grade | pending_review | Historical match confirmed |
| CY-98-PH-GR-614 | SIG-91-UWU-GPZB | unverified | Auto-mapped, validated |
| Fructose Qualitätsstufe I | citric acid pharma grade | unverified | Auto-mapped, validated |
| CI-AC-25-GR-A-669 | lactic acid 98% premium | auto_generated | Auto-mapped, validated |
| ZE-LO-524 | meridian materials | auto_generated | Verified via product specs |
| Vat Standardqualität NL 19% | Vat Reduced CN 10% | auto_generated | Verified via product specs |
| cyclodextrin premium | SIG-58-NYA-2O4M | pending_review | Auto-mapped, validated |
| Nexus Materials | Baltic Sourcing | auto_generated | Historical match confirmed |
| Citric Acid 99.5% | RA-OI-98-679 | auto_generated | Confirmed by domain expert |
| fructose tech grade | SO-CH-892 | auto_generated | Verified via product specs |
| HO-PA-149 International | zenith industries | pending_review | Verified via product specs |
| Continental Enterprise GmbH | atlas partners | auto_generated | Cross-referenced with transactions |
| vanguard sourcing | ST-SU-CO-731 | auto_generated | Auto-mapped, validated |
| SIG-69-OFZ-JW34 | resistant starch tech grade | auto_generated | Cross-referenced with transactions |
| casein | SIG-29-BZP-SU62 | pending_review | Historical match confirmed |
| Palm Oil 98% | SO-BE-25-982 | auto_generated | Confirmed by domain expert |
| Catalyst Materials | SIG-49-MMU-1GJR | pending_review | Verified via product specs |
| CY-PH-GR-870 | Maltodextrin DE5 Food Grade | unverified | Auto-mapped, validated |
| Dextrose Grade A | WH-GL-ST-378 | unverified | Auto-mapped, validated |
| sorbic acid food grade | Potassium Sorbate Technical | pending_review | Historical match confirmed |
| Premier Supply Co. | Atlas Sourcing | pending_review | Auto-mapped, validated |
| RE-ST-FO-GR-998 | Traubenzucker | unverified | Cross-referenced with transactions |
| SO-BE-70-PR-120 | Cyclodextrin Standardqualität | auto_generated | Verified via product specs |
| Quantum Versorgung GmbH | Core Logistics | unverified | Verified via product specs |
| Palmfett | SIG-36-ZKX-4SE4 | pending_review | Auto-mapped, validated |
| ascorbic acid standard | SO-CH-GR-B-273 | pending_review | Historical match confirmed |
| CO-MA-245 | Apex Sourcing | auto_generated | Cross-referenced with transactions |
| AT-PA-546 Corp. | Atlas Industries LLC | pending_review | Confirmed by domain expert |
| Soy Isolate 50% Food Grade | SIG-27-UKP-V2ME | unverified | Cross-referenced with transactions |
| Traubenzucker Qualitätsstufe I | Pea Protein | auto_generated | Cross-referenced with transactions |
| dextrin standard | Zitronensäure Qualitätsstufe I | unverified | Historical match confirmed |
| vat reduced cn 15% | EX-D-7-593 | unverified | Auto-mapped, validated |
| Excise NL 15% | vat standard nl 20% | auto_generated | Auto-mapped, validated |
| Vanguard Partners PLC | ST-PA-504 | pending_review | Historical match confirmed |
| VE-CO-290 AG | Core Distribution | auto_generated | Cross-referenced with transactions |
| DE-PH-GR-173 | Soy Isolate 98% | auto_generated | Confirmed by domain expert |
| SIG-88-RKE-8R7A | Ascorbic Acid 99.5% Premiumqualität | unverified | Cross-referenced with transactions |
| lactic acid | PO-SO-50-TE-497 | pending_review | Auto-mapped, validated |
| SIG-27-VCT-2O4S | Apex Versorgung GmbH | pending_review | Cross-referenced with transactions |
| Citric Acid 25% Technical | Zitronensäure | auto_generated | Confirmed by domain expert |
| SIG-19-TLQ-1P5Z | CO-OI-70-701 | auto_generated | Cross-referenced with transactions |
| SIG-89-JZC-1682 | Dextrose | pending_review | Confirmed by domain expert |
| Excise IN 5% | Excise GB 19% | unverified | Confirmed by domain expert |
| SIG-12-USU-9HWB GmbH | vanguard industries PLC | unverified | Confirmed by domain expert |
| Natriumbenzoat 50% | Sorbic Acid 98% | pending_review | Verified via product specs |
| Quantum Supply Co. | PR-LO-351 | pending_review | Verified via product specs |
| Atlas Ingredients PLC | Elite Versorgung SA | unverified | Cross-referenced with transactions |
| SIG-50-GYK-UH5P | CA-IN-566 International | auto_generated | Cross-referenced with transactions |
| Vat Reduced GB 25% | EX-B-10-648 | unverified | Cross-referenced with transactions |
| SIG-60-OHC-5EQB | CE-SO-153 | auto_generated | Auto-mapped, validated |
| Kaliumsorbat | resistant starch 50% | auto_generated | Cross-referenced with transactions |
| Resistant Starch Standard | Fructose Standardqualität | pending_review | Auto-mapped, validated |
| Zitronensäure Lebensmittelrein | sunflower oil 98% | unverified | Confirmed by domain expert |
| Elite Supply Co. | atlas sourcing | pending_review | Auto-mapped, validated |
| Global Logistics | atlas supply | pending_review | Cross-referenced with transactions |
| Dextrin 98% Food Grade | DE-TE-406 | auto_generated | Cross-referenced with transactions |
| soy isolate premium | SIG-50-MPG-UDLW | pending_review | Cross-referenced with transactions |
| LA-AC-393 | Rapeseed Oil 70% Premium | auto_generated | Auto-mapped, validated |
| Lactic Acid 99.5% | pea protein 98% | auto_generated | Cross-referenced with transactions |
| Rapsöl | SIG-78-WDE-NNV9 | auto_generated | Confirmed by domain expert |
| Cyclodextrin Lebensmittelrein | SIG-12-OAV-ALF4 | unverified | Auto-mapped, validated |
| PR-SU-CO-650 | Baltic Werkstoffe | auto_generated | Auto-mapped, validated |
| sorbic acid | Lactic Acid 99.5% Grade B | pending_review | Confirmed by domain expert |
| Natriumbenzoat 50% Technische Qualität | soy isolate standard | pending_review | Confirmed by domain expert |
| Vat Reduced FR 20% | VA-RE-C-19-228 | auto_generated | Historical match confirmed |
| SIG-80-WKN-N0SS | Cyclodextrin Standard | pending_review | Verified via product specs |
| Atlas Sourcing | QU-MA-886 | pending_review | Verified via product specs |
| VA-ST-G-20-932 | Customs Duty CN 0% | pending_review | Historical match confirmed |
| Citric Acid Pharma Grade | SIG-89-ISH-EQW6 | pending_review | Historical match confirmed |
| pea protein 25% pharma grade | SIG-13-FYG-4NN9 | pending_review | Historical match confirmed |
| sodium benzoate 99.5% premium | Ascorbic Acid | pending_review | Auto-mapped, validated |
| Pacific Supply Co. | CE-LO-713 | pending_review | Cross-referenced with transactions |
| Zitronensäure 98% | ascorbic acid | unverified | Verified via product specs |
| nexus ingredients SAS | Vertex Vertrieb Group | pending_review | Historical match confirmed |
| SIG-69-OFZ-JW34 | DE-840 | unverified | Auto-mapped, validated |
| CY-763 | sodium benzoate premium | unverified | Auto-mapped, validated |
| Nordic Manufacturing Group | Baltic Supply Holdings | pending_review | Auto-mapped, validated |
| Vat Reduced IN 5% | Vat Reduced CN 19% | unverified | Confirmed by domain expert |
| SIG-13-ZRN-WZGO | PR-MA-428 | unverified | Historical match confirmed |
| Meridian Versorgung GmbH | SIG-13-SXA-38WM | unverified | Verified via product specs |
| Kaliumsorbat | palm oil | pending_review | Auto-mapped, validated |
| EX-B-10-648 | vat standard fr 5% | auto_generated | Cross-referenced with transactions |
| Atlantic Logistics SAS | SIG-81-EKU-R7CX Group | unverified | Historical match confirmed |
| GL-MA-581 | Nordic Versorgung GmbH | unverified | Auto-mapped, validated |
| Ascorbic Acid 99.5% Premiumqualität | rapeseed oil 99.5% | auto_generated | Historical match confirmed |
| SIG-97-QNX-7TWO | withholding nl 20% | pending_review | Auto-mapped, validated |
| Palmfett 98% | maltodextrin de25 | pending_review | Confirmed by domain expert |
| CA-CA-50-260 | Natriumbenzoat Qualitätsstufe I | unverified | Confirmed by domain expert |
| Kasein Qualitätsstufe I | Casein 98% Grade B | pending_review | Confirmed by domain expert |
| global partners BV | SIG-17-UCE-6H7J Corp. | auto_generated | Auto-mapped, validated |
| SIG-39-OZI-N968 | Pea Protein 70% Pharma Grade | auto_generated | Confirmed by domain expert |
| Soy Isolate Grade B | SIG-24-LEE-BXW7 | pending_review | Auto-mapped, validated |
| calcium carbonate | LA-AC-690 | auto_generated | Verified via product specs |
| calcium carbonate | SIG-83-BMJ-HHIG | pending_review | Confirmed by domain expert |
| PR-SU-CO-920 | core sourcing | unverified | Cross-referenced with transactions |
| SIG-17-YLM-LBLW | CO-OI-70-553 | unverified | Historical match confirmed |
| Pea Protein | SIG-11-QDU-30PE | unverified | Verified via product specs |
| SIG-11-EIQ-WD14 | zenith supply | auto_generated | Auto-mapped, validated |
| SIG-83-SCO-PIKN | Excise GB 19% | unverified | Verified via product specs |
| ZE-SU-434 NV | SIG-40-KNF-W24X PLC | pending_review | Auto-mapped, validated |
| VA-ST-D-0-573 | Vat Reduced IN 5% | auto_generated | Auto-mapped, validated |
| SIG-85-ACE-0XNG | SO-CH-25-FO-GR-400 | pending_review | Cross-referenced with transactions |
| SIG-30-SYO-74WX | Weizenklebereiweiß Lebensmittelrein | unverified | Historical match confirmed |
| Dextrose Technical | SIG-19-ZOZ-1S2O | pending_review | Cross-referenced with transactions |
| Palm Oil | glucose syrup 98% standard | pending_review | Confirmed by domain expert |
| Sodium Benzoate 50% | CO-OI-99.5-PH-GR-944 | unverified | Historical match confirmed |
| pea protein | Resistente Stärke Lebensmittelrein | pending_review | Historical match confirmed |
| EL-SO-688 | SIG-20-RSZ-19RE | pending_review | Verified via product specs |
| MA-DE-516 | Resistant Starch 98% Pharma Grade | unverified | Verified via product specs |
| sodium chloride 70% | Glucose Syrup 99.5% Grade B | pending_review | Confirmed by domain expert |
| Meridian Solutions International | stellar manufacturing International | unverified | Historical match confirmed |
| pea protein 70% premium | DE-602 | pending_review | Historical match confirmed |
| SIG-14-HQE-PUWC | Prism Partners | unverified | Confirmed by domain expert |
| citric acid food grade | SIG-58-NYA-2O4M | pending_review | Confirmed by domain expert |
| Resistant Starch Technical | resistant starch | unverified | Verified via product specs |
| Lactic Acid Food Grade | Glukosesirup Syrup 98% | pending_review | Historical match confirmed |
| Vat Reduced BR 7% | Excise FR 21% | pending_review | Historical match confirmed |
| SIG-60-NXS-8BAO | Atlantic Sourcing | unverified | Cross-referenced with transactions |
| SIG-58-LWY-Q8P6 | LA-AC-471 | unverified | Cross-referenced with transactions |
| Palmfett 25% | Soy Isolate 25% | unverified | Verified via product specs |
| Kasein | SIG-47-AWI-4RQV | pending_review | Cross-referenced with transactions |
| SIG-79-DVU-H9H4 | CI-AC-ST-565 | unverified | Verified via product specs |
| SIG-47-GAT-ET7B | Palm Oil | auto_generated | Cross-referenced with transactions |
| Apex Sourcing | AT-MA-739 | pending_review | Historical match confirmed |
| QU-TR-219 International | Catalyst Verarbeitung | pending_review | Cross-referenced with transactions |
| excise in 21% | WI-G-20-674 | unverified | Historical match confirmed |
| BA-TR-377 NV | continental processing SA | unverified | Cross-referenced with transactions |
| VA-RE-I-5-252 | SIG-12-PRR-STQE | auto_generated | Confirmed by domain expert |
| prism ingredients AG | SIG-76-COR-DQEF GmbH | pending_review | Confirmed by domain expert |
| CI-AC-538 | SIG-61-MHS-BQG3 | unverified | Confirmed by domain expert |
| WH-GL-123 | Weizenklebereiweiß 98% | pending_review | Auto-mapped, validated |
| SIG-40-WLB-9IFD | Quantum Sourcing | unverified | Auto-mapped, validated |
| IS-70-838 | Traubenzucker Qualitätsstufe II | pending_review | Confirmed by domain expert |
| SIG-56-NOU-ZR98 | Cyclodextrin 98% | pending_review | Cross-referenced with transactions |
| SIG-42-UMA-WZ7F | Vat Reduced BR 0% | auto_generated | Historical match confirmed |
| CI-AC-99.5-674 | Natriumbenzoat 99.5% Technische Qualität | auto_generated | Cross-referenced with transactions |
| pea protein | SIG-72-YEU-SCIQ | unverified | Auto-mapped, validated |
| SIG-60-TMF-XHW0 | Kasein 70% Technische Qualität | pending_review | Historical match confirmed |
| ME-SO-760 GmbH | SIG-26-PVD-6QGC AG | unverified | Auto-mapped, validated |
| DE-840 | Maltodextrin DE20 | auto_generated | Auto-mapped, validated |
| Atlantic Logistik SAS | Vertex Commodities | unverified | Cross-referenced with transactions |
| sorbic acid standard | Wheat Gluten 50% | unverified | Verified via product specs |
| apex logistics | AT-LO-628 | unverified | Confirmed by domain expert |
| SIG-99-GVJ-VPM6 | sodium chloride tech grade | pending_review | Auto-mapped, validated |
| SIG-47-YTF-UPMT | Sunflower Oil Technical | auto_generated | Confirmed by domain expert |
| Withholding BR 0% | SIG-65-LOJ-4KXS | unverified | Verified via product specs |
| SO-BE-GR-B-914 | SIG-86-VCP-SVOL | auto_generated | Confirmed by domain expert |
| VE-DI-556 SA | baltic ingredients | unverified | Confirmed by domain expert |
| SIG-36-TML-VS0J | FR-FO-GR-823 | pending_review | Historical match confirmed |
| CE-SU-700 Group | stellar processing | pending_review | Verified via product specs |
| potassium sorbate 50% tech grade | SIG-37-JLF-9KYP | unverified | Auto-mapped, validated |
| SO-CH-98-657 | SIG-37-MXA-3C7Q | unverified | Cross-referenced with transactions |
| Pacific Distribution NV | SIG-89-WUP-8NG0 | pending_review | Confirmed by domain expert |
| SIG-83-DGX-TY87 | Excise US 5% | auto_generated | Auto-mapped, validated |
| SO-CH-257 | rapeseed oil 25% | auto_generated | Verified via product specs |
| Calcium Carbonate 98% | Ascorbic Acid | pending_review | Auto-mapped, validated |
| PI-SO-581 Inc. | Pinnacle Industries SAS | auto_generated | Cross-referenced with transactions |
| Citric Acid 25% | SIG-37-NAI-M1G9 | auto_generated | Confirmed by domain expert |
| Nexus Distribution | SIG-55-TGR-SSTC Holdings | pending_review | Auto-mapped, validated |
| VA-DI-105 | core trading KG | pending_review | Auto-mapped, validated |
| Fructose Pharmazeutisch rein | SIG-29-YUO-5FO9 | auto_generated | Confirmed by domain expert |
| Stratos Logistik | Vanguard Supply Co. | pending_review | Confirmed by domain expert |
| isoglucose 70% | Traubenzucker 50% | pending_review | Verified via product specs |
| Excise NL 21% | WI-F-5-102 | pending_review | Confirmed by domain expert |
| Fructose | Lactic Acid | auto_generated | Verified via product specs |
| Prism Industrien Holdings | baltic supply | unverified | Cross-referenced with transactions |
| Excise US 5% | SIG-47-MRM-FIIH | pending_review | Confirmed by domain expert |
| PI-PR-193 | Catalyst Manufacturing GmbH | pending_review | Cross-referenced with transactions |
| Rapsöl 50% Pharmazeutisch rein | Citric Acid 25% Technical | unverified | Cross-referenced with transactions |
| SIG-23-IEJ-V2T3 | Kasein 98% | unverified | Cross-referenced with transactions |
| Vat Reduced GB 19% | WI-G-15-758 | pending_review | Cross-referenced with transactions |
| RA-OI-25-PH-GR-210 | Lactic Acid Technical | auto_generated | Verified via product specs |
| Stratos Supply Co. | premier sourcing | unverified | Auto-mapped, validated |
| Casein Technical | Sorbinsäure | auto_generated | Verified via product specs |
| dextrose | SO-CH-70-365 | pending_review | Auto-mapped, validated |
| FR-FO-GR-823 | Casein Premium | unverified | Confirmed by domain expert |
| sodium benzoate 99.5% tech grade | Kaliumsorbat | unverified | Verified via product specs |
| SIG-83-PHT-N27M | Pea Protein Grade A | unverified | Historical match confirmed |
| Isoglucose 70% | SO-CH-758 | unverified | Auto-mapped, validated |
| Apex Commodities Holdings | Quantum Handel Ltd. | pending_review | Verified via product specs |
| zenith sourcing | SIG-15-GJL-MVIC | unverified | Auto-mapped, validated |
| Palmfett | SIG-32-RJE-L1OT | pending_review | Confirmed by domain expert |
| Sorbinsäure | Pea Protein 25% Pharma Grade | unverified | Cross-referenced with transactions |
| Natriumchlorid 98% Pharmazeutisch rein | SIG-81-FXX-6VPL | pending_review | Historical match confirmed |
| SIG-45-ZTJ-PA16 | Citric Acid Food Grade | auto_generated | Cross-referenced with transactions |
| Dextrin Standardqualität | SIG-60-WYC-NAXS | auto_generated | Confirmed by domain expert |
| ME-MA-977 | Core Supply Co. | auto_generated | Confirmed by domain expert |
| Resistente Stärke Pharmazeutisch rein | rapeseed oil premium | auto_generated | Confirmed by domain expert |
| Citric Acid | citric acid 98% | unverified | Cross-referenced with transactions |
| Nexus Partners GmbH | NO-CO-357 International | unverified | Confirmed by domain expert |
| SIG-13-CGO-2Y4L | Glucose Syrup 99.5% Food Grade | pending_review | Cross-referenced with transactions |
| Coconut Oil 50% Technische Qualität | AS-AC-GR-B-395 | unverified | Auto-mapped, validated |
| DE-602 | Kaliumsorbat | auto_generated | Auto-mapped, validated |
| SIG-60-PEY-H3GM | Rapeseed Oil 50% Food Grade | unverified | Historical match confirmed |
| prism industries International | Pacific Vertrieb NV | auto_generated | Verified via product specs |
| SIG-17-YLM-LBLW | Ascorbic Acid Standard | unverified | Auto-mapped, validated |
| SIG-88-VVU-EL88 | Resistant Starch 70% | pending_review | Confirmed by domain expert |
| SO-BE-113 | Weizenklebereiweiß 25% Premiumqualität | pending_review | Verified via product specs |
| SIG-60-WEX-2G05 | Isoglucose Qualitätsstufe II | pending_review | Historical match confirmed |
| potassium sorbate | Soja Isolate 99.5% | auto_generated | Confirmed by domain expert |
| Global Logistics | SIG-53-HTQ-XVWB Group | auto_generated | Auto-mapped, validated |
| rapeseed oil 98% standard | Kasein Standardqualität | pending_review | Historical match confirmed |
| Rapeseed Oil Technical | SIG-93-FDC-Q685 | pending_review | Confirmed by domain expert |
| Catalyst Industrien PLC | SIG-37-AVX-CY7Q SAS | pending_review | Historical match confirmed |
| vertex ingredients KG | BA-TR-773 BV | unverified | Verified via product specs |
| wheat gluten premium | GL-SY-70-655 | auto_generated | Auto-mapped, validated |
| citric acid food grade | SIG-24-NPE-GDMB | unverified | Confirmed by domain expert |
| NO-LO-524 | prism logistics | unverified | Historical match confirmed |
| AT-IN-847 GmbH | Pacific Vertrieb International | auto_generated | Cross-referenced with transactions |
| SIG-45-ZZU-GRXH International | stratos materials Group | auto_generated | Confirmed by domain expert |
| SIG-60-ZEV-V2NY | pea protein | auto_generated | Confirmed by domain expert |
| SIG-16-IYP-EOZP | Coconut Oil | pending_review | Confirmed by domain expert |
| Quantum Sourcing | SIG-80-OEM-5LVP | pending_review | Cross-referenced with transactions |
| SIG-27-IRG-QSO9 International | Nordic Chemicals | unverified | Verified via product specs |
| WH-GL-123 | SIG-94-DKR-CJTR | unverified | Confirmed by domain expert |
| Coconut Oil 50% | Natriumbenzoat Qualitätsstufe I | unverified | Auto-mapped, validated |
| Ascorbic Acid 50% Standardqualität | PE-PR-70-PR-387 | auto_generated | Cross-referenced with transactions |
| rapeseed oil | PO-SO-339 | unverified | Historical match confirmed |
| Stratos Logistik | SIG-97-KNV-Q7J8 | pending_review | Auto-mapped, validated |
| VE-LO-777 | SIG-79-DZB-60U2 International | unverified | Auto-mapped, validated |
| SO-IS-99.5-PR-187 | sorbic acid | pending_review | Verified via product specs |
| resistant starch | LA-AC-98-226 | auto_generated | Auto-mapped, validated |
| calcium carbonate 98% pharma grade | FR-ST-953 | auto_generated | Confirmed by domain expert |
| AT-MA-796 LLC | stratos supply BV | pending_review | Verified via product specs |
| CA-CA-50-GR-A-195 | Dextrin Qualitätsstufe II | pending_review | Cross-referenced with transactions |
| Apex Solutions International | CO-DI-629 BV | unverified | Historical match confirmed |
| Vertex Distribution Holdings | SIG-68-BSO-NW8J Group | pending_review | Auto-mapped, validated |
| Palm Oil 70% | FR-TE-414 | unverified | Confirmed by domain expert |
| SIG-39-LKH-DFJY | Pacific Materials | pending_review | Auto-mapped, validated |
| Nordic Logistik PLC | PR-CO-443 Group | pending_review | Historical match confirmed |
| Calcium Carbonate Standardqualität | SIG-29-BZP-SU62 | unverified | Confirmed by domain expert |
| Lactic Acid Standardqualität | SIG-27-NTH-I37Y | unverified | Confirmed by domain expert |
| Sorbinsäure 98% | Coconut Oil 98% Food Grade | pending_review | Cross-referenced with transactions |
| sorbic acid 70% | Pea Protein 25% Pharmazeutisch rein | pending_review | Auto-mapped, validated |
| Continental Processing | ST-MA-621 International | pending_review | Historical match confirmed |
| Dextrose | SO-CH-185 | auto_generated | Auto-mapped, validated |
| PR-CO-443 Group | Pinnacle Commodities BV | unverified | Auto-mapped, validated |
| prime chemicals SA | Pinnacle Logistik BV | pending_review | Cross-referenced with transactions |
| resistant starch | Dextrose Grade B | unverified | Verified via product specs |
| NE-PA-358 | Premier Enterprise International | pending_review | Auto-mapped, validated |
| SIG-32-RJE-L1OT | RA-OI-GR-B-834 | auto_generated | Verified via product specs |
| stratos partners SA | Prism Solutions | pending_review | Verified via product specs |
| Rapsöl 99.5% Technische Qualität | IS-GR-B-649 | pending_review | Cross-referenced with transactions |
| PR-SO-769 LLC | Pinnacle Ingredients AG | pending_review | Cross-referenced with transactions |
| palm oil 70% premium | Kaliumsorbat | unverified | Historical match confirmed |
| pacific materials | Continental Versorgung GmbH | pending_review | Cross-referenced with transactions |
| CA-CA-70-883 | Kasein 25% Pharmazeutisch rein | pending_review | Cross-referenced with transactions |
| Atlantic Commodities | premier industries Holdings | pending_review | Historical match confirmed |
| Vat Standardqualität DE 25% | SIG-89-KYU-M9RA | pending_review | Confirmed by domain expert |
| Core Chemicals | SIG-37-YMX-1ATI SARL | auto_generated | Historical match confirmed |
| sodium benzoate | Soja Isolate 50% Qualitätsstufe II | unverified | Historical match confirmed |
| PE-PR-746 | Soy Isolate 99.5% | auto_generated | Cross-referenced with transactions |
| Dextrose 50% | Isoglucose 70% | auto_generated | Confirmed by domain expert |
| Palmfett | sunflower oil 70% | pending_review | Cross-referenced with transactions |
| CO-DI-629 BV | Vertex Distribution AG | pending_review | Cross-referenced with transactions |
| stratos trading | SIG-27-DQT-IQ97 | unverified | Historical match confirmed |
| Potassium Sorbate | SIG-47-YTF-UPMT | auto_generated | Historical match confirmed |
| MA-DE-744 | SIG-63-TFP-OMUW | auto_generated | Cross-referenced with transactions |
| nexus logistics | PA-MA-435 | auto_generated | Confirmed by domain expert |
| global logistics | AT-MA-893 | auto_generated | Auto-mapped, validated |
| Continental Sourcing | AT-MA-127 | pending_review | Historical match confirmed |
| Fructose 70% | rapeseed oil | unverified | Auto-mapped, validated |
| IS-50-GR-A-791 | rapeseed oil 98% standard | pending_review | Auto-mapped, validated |
| Palmfett | WH-GL-GR-A-583 | pending_review | Verified via product specs |
| PE-PR-302 | SIG-45-ADT-8MFS | unverified | Historical match confirmed |
| SIG-17-ZBZ-BJS4 SARL | Meridian Trading Holdings | unverified | Historical match confirmed |
| Dextrin Premium | PA-OI-383 | auto_generated | Confirmed by domain expert |
| DE-98-512 | Glucose Syrup 98% Standard | auto_generated | Verified via product specs |
| coconut oil 25% tech grade | Sodium Chloride 70% Premium | pending_review | Historical match confirmed |
| AS-AC-FO-GR-835 | Cyclodextrin | auto_generated | Confirmed by domain expert |
| SIG-70-EXR-LD0M | prism enterprise Ltd. | pending_review | Confirmed by domain expert |
| SIG-50-FUX-7S9T | calcium carbonate food grade | pending_review | Verified via product specs |
| SIG-34-TKJ-QFOY | VA-ST-N-5-804 | pending_review | Auto-mapped, validated |
| Excise CN 21% | withholding fr 5% | auto_generated | Cross-referenced with transactions |
| Lactic Acid | SIG-99-IZM-CYBY | unverified | Verified via product specs |
| Natriumchlorid | SO-BE-GR-B-936 | unverified | Auto-mapped, validated |
| SIG-77-OCZ-Q3GH | pinnacle supply | auto_generated | Historical match confirmed |
| Apex Sourcing | Pinnacle Sourcing | auto_generated | Cross-referenced with transactions |
| Sonnenblumenöl 70% Lebensmittelrein | CI-AC-215 | unverified | Auto-mapped, validated |
| Core Logistik | atlas materials | auto_generated | Confirmed by domain expert |
| Resistant Starch 98% Grade B | Maltodextrin-Pulver DE5 Lebensmittelrein | pending_review | Auto-mapped, validated |
| HO-SU-CO-454 | SIG-46-AAW-27BR | pending_review | Verified via product specs |
| MA-DE-799 | Ascorbic Acid 70% | auto_generated | Verified via product specs |
| vat reduced br 5% | SIG-27-VXG-OFKE | unverified | Confirmed by domain expert |
| SIG-62-BTJ-PQV9 | SO-BE-25-ST-520 | auto_generated | Confirmed by domain expert |
| Isoglucose 50% Lebensmittelrein | lactic acid 98% | pending_review | Cross-referenced with transactions |
| SIG-85-FIY-2QW4 | Zitronensäure | unverified | Auto-mapped, validated |
| Resistant Starch 70% | GL-SY-PR-440 | unverified | Auto-mapped, validated |
| Dextrin 70% | Lactic Acid Standard | auto_generated | Verified via product specs |
| SO-AC-377 | Rapeseed Oil 99.5% | unverified | Historical match confirmed |

#### 4.3.3 Excluded Mappings

Provisional mappings pending business validation:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-2654-B | Invalid Entry 584 | Out of scope per business decision |
| NOISE-1829-H | Invalid Entry 315 | Duplicate detected |
| NOISE-1241-F | Invalid Entry 905 | Out of scope per business decision |
| NOISE-8984-C | Invalid Entry 337 | Superseded by newer mapping |
| NOISE-3265-B | Invalid Entry 157 | Data quality insufficient |
| NOISE-3670-G | Invalid Entry 120 | Out of scope per business decision |
| NOISE-5121-D | Invalid Entry 181 | Pending validation |
| NOISE-8935-E | Invalid Entry 649 | Superseded by newer mapping |
| NOISE-9612-D | Invalid Entry 911 | Data quality insufficient |
| NOISE-7828-F | Invalid Entry 119 | Duplicate detected |
| NOISE-4274-F | Invalid Entry 147 | Out of scope per business decision |
| NOISE-2084-E | Invalid Entry 350 | Superseded by newer mapping |
| NOISE-6638-H | Invalid Entry 267 | Pending validation |
| NOISE-9958-E | Invalid Entry 252 | Out of scope per business decision |
| NOISE-5227-H | Invalid Entry 549 | Duplicate detected |
| NOISE-5787-E | Invalid Entry 724 | Superseded by newer mapping |
| NOISE-2432-H | Invalid Entry 523 | Duplicate detected |
| NOISE-7556-D | Invalid Entry 668 | Out of scope per business decision |
| NOISE-3143-C | Invalid Entry 897 | Superseded by newer mapping |
| NOISE-2887-C | Invalid Entry 162 | Superseded by newer mapping |
| NOISE-2678-F | Invalid Entry 904 | Out of scope per business decision |
| NOISE-7472-A | Invalid Entry 428 | Superseded by newer mapping |
| NOISE-9236-D | Invalid Entry 156 | Out of scope per business decision |
| NOISE-7338-B | Invalid Entry 145 | Pending validation |
| NOISE-9879-H | Invalid Entry 842 | Data quality insufficient |
| NOISE-1442-E | Invalid Entry 708 | Out of scope per business decision |
| NOISE-3257-A | Invalid Entry 454 | Out of scope per business decision |
| NOISE-5383-G | Invalid Entry 265 | Superseded by newer mapping |
| NOISE-1383-H | Invalid Entry 365 | Pending validation |
| NOISE-8755-B | Invalid Entry 784 | Superseded by newer mapping |
| NOISE-5311-B | Invalid Entry 394 | Superseded by newer mapping |
| NOISE-5524-D | Invalid Entry 908 | Superseded by newer mapping |
| NOISE-9163-B | Invalid Entry 408 | Data quality insufficient |
| NOISE-6482-G | Invalid Entry 819 | Out of scope per business decision |
| NOISE-6716-D | Invalid Entry 477 | Duplicate detected |
| NOISE-4790-H | Invalid Entry 390 | Superseded by newer mapping |
| NOISE-3480-H | Invalid Entry 639 | Pending validation |
| NOISE-3473-F | Invalid Entry 176 | Out of scope per business decision |
| NOISE-7877-F | Invalid Entry 951 | Data quality insufficient |
| NOISE-4154-A | Invalid Entry 908 | Data quality insufficient |
| NOISE-1517-F | Invalid Entry 260 | Duplicate detected |
| NOISE-3506-G | Invalid Entry 634 | Superseded by newer mapping |
| NOISE-1846-F | Invalid Entry 512 | Superseded by newer mapping |
| NOISE-6782-H | Invalid Entry 907 | Data quality insufficient |
| NOISE-6510-F | Invalid Entry 433 | Superseded by newer mapping |
| NOISE-3611-G | Invalid Entry 904 | Pending validation |
| NOISE-3781-A | Invalid Entry 169 | Pending validation |
| NOISE-5611-E | Invalid Entry 328 | Out of scope per business decision |
| NOISE-1433-C | Invalid Entry 531 | Out of scope per business decision |
| NOISE-2761-B | Invalid Entry 833 | Data quality insufficient |
| NOISE-2944-A | Invalid Entry 506 | Out of scope per business decision |
| NOISE-3914-D | Invalid Entry 352 | Out of scope per business decision |
| NOISE-9309-F | Invalid Entry 661 | Pending validation |
| NOISE-2958-F | Invalid Entry 453 | Data quality insufficient |
| NOISE-3409-G | Invalid Entry 418 | Data quality insufficient |
| NOISE-8476-C | Invalid Entry 227 | Out of scope per business decision |
| NOISE-9598-E | Invalid Entry 107 | Out of scope per business decision |
| NOISE-3536-G | Invalid Entry 655 | Duplicate detected |
| NOISE-4635-H | Invalid Entry 636 | Superseded by newer mapping |
| NOISE-3666-G | Invalid Entry 908 | Duplicate detected |
| NOISE-4806-H | Invalid Entry 185 | Superseded by newer mapping |
| NOISE-3488-A | Invalid Entry 766 | Superseded by newer mapping |
| NOISE-9166-C | Invalid Entry 740 | Pending validation |
| NOISE-4020-B | Invalid Entry 412 | Duplicate detected |
| NOISE-9357-E | Invalid Entry 327 | Superseded by newer mapping |
| NOISE-2906-E | Invalid Entry 434 | Data quality insufficient |
| NOISE-2636-B | Invalid Entry 717 | Superseded by newer mapping |
| NOISE-6146-B | Invalid Entry 996 | Data quality insufficient |
| NOISE-4346-F | Invalid Entry 151 | Duplicate detected |
| NOISE-6049-B | Invalid Entry 102 | Out of scope per business decision |
| NOISE-5530-C | Invalid Entry 169 | Superseded by newer mapping |
| NOISE-6775-E | Invalid Entry 976 | Out of scope per business decision |
| NOISE-2135-G | Invalid Entry 856 | Superseded by newer mapping |
| NOISE-6417-E | Invalid Entry 904 | Superseded by newer mapping |
| NOISE-6670-F | Invalid Entry 145 | Pending validation |
| NOISE-9855-C | Invalid Entry 869 | Out of scope per business decision |
| NOISE-1558-H | Invalid Entry 823 | Superseded by newer mapping |
| NOISE-3102-E | Invalid Entry 356 | Pending validation |
| NOISE-3429-D | Invalid Entry 710 | Superseded by newer mapping |
| NOISE-3929-C | Invalid Entry 171 | Pending validation |
| NOISE-9510-F | Invalid Entry 528 | Duplicate detected |
| NOISE-5963-B | Invalid Entry 989 | Duplicate detected |
| NOISE-5455-E | Invalid Entry 126 | Superseded by newer mapping |
| NOISE-2163-H | Invalid Entry 136 | Data quality insufficient |
| NOISE-1749-E | Invalid Entry 507 | Pending validation |
| NOISE-1334-C | Invalid Entry 583 | Pending validation |
| NOISE-9846-C | Invalid Entry 571 | Superseded by newer mapping |
| NOISE-6267-H | Invalid Entry 545 | Pending validation |
| NOISE-8801-D | Invalid Entry 868 | Data quality insufficient |
| NOISE-2528-B | Invalid Entry 633 | Pending validation |
| NOISE-5634-H | Invalid Entry 353 | Duplicate detected |
| NOISE-5214-A | Invalid Entry 518 | Duplicate detected |
| NOISE-1947-D | Invalid Entry 506 | Data quality insufficient |
| NOISE-7646-F | Invalid Entry 534 | Pending validation |
| NOISE-6923-D | Invalid Entry 528 | Superseded by newer mapping |
| NOISE-7847-F | Invalid Entry 883 | Pending validation |
| NOISE-5178-D | Invalid Entry 113 | Superseded by newer mapping |
| NOISE-2834-A | Invalid Entry 216 | Data quality insufficient |
| NOISE-9336-E | Invalid Entry 263 | Superseded by newer mapping |
| NOISE-9444-C | Invalid Entry 508 | Pending validation |
| NOISE-7490-F | Invalid Entry 420 | Duplicate detected |
| NOISE-9362-A | Invalid Entry 282 | Data quality insufficient |
| NOISE-7773-C | Invalid Entry 473 | Duplicate detected |
| NOISE-2252-E | Invalid Entry 822 | Out of scope per business decision |
| NOISE-7430-B | Invalid Entry 444 | Pending validation |
| NOISE-5681-G | Invalid Entry 222 | Out of scope per business decision |
| NOISE-8367-C | Invalid Entry 826 | Out of scope per business decision |
| NOISE-3038-D | Invalid Entry 528 | Duplicate detected |
| NOISE-7009-A | Invalid Entry 128 | Duplicate detected |
| NOISE-1925-A | Invalid Entry 869 | Duplicate detected |
| NOISE-2486-E | Invalid Entry 142 | Pending validation |
| NOISE-4402-A | Invalid Entry 627 | Duplicate detected |
| NOISE-2436-A | Invalid Entry 321 | Superseded by newer mapping |
| NOISE-6442-H | Invalid Entry 782 | Data quality insufficient |
| NOISE-3613-F | Invalid Entry 227 | Superseded by newer mapping |
| NOISE-5688-C | Invalid Entry 322 | Superseded by newer mapping |
| NOISE-8515-F | Invalid Entry 970 | Pending validation |
| NOISE-1703-C | Invalid Entry 175 | Duplicate detected |
| NOISE-5861-C | Invalid Entry 620 | Pending validation |
| NOISE-3486-E | Invalid Entry 349 | Pending validation |
| NOISE-2753-H | Invalid Entry 421 | Pending validation |
| NOISE-6333-B | Invalid Entry 645 | Duplicate detected |
| NOISE-9934-G | Invalid Entry 989 | Pending validation |
| NOISE-2693-D | Invalid Entry 127 | Superseded by newer mapping |
| NOISE-3577-H | Invalid Entry 253 | Pending validation |
| NOISE-7018-D | Invalid Entry 297 | Out of scope per business decision |
| NOISE-8022-H | Invalid Entry 933 | Data quality insufficient |
| NOISE-4053-A | Invalid Entry 822 | Duplicate detected |
| NOISE-7553-G | Invalid Entry 285 | Out of scope per business decision |
| NOISE-8643-H | Invalid Entry 190 | Duplicate detected |
| NOISE-1516-D | Invalid Entry 248 | Data quality insufficient |
| NOISE-5348-D | Invalid Entry 484 | Duplicate detected |
| NOISE-6639-A | Invalid Entry 216 | Out of scope per business decision |
| NOISE-1450-F | Invalid Entry 765 | Duplicate detected |
| NOISE-6472-A | Invalid Entry 269 | Pending validation |
| NOISE-5564-C | Invalid Entry 890 | Out of scope per business decision |
| NOISE-3576-H | Invalid Entry 394 | Superseded by newer mapping |
| NOISE-7334-D | Invalid Entry 921 | Data quality insufficient |
| NOISE-5138-A | Invalid Entry 148 | Superseded by newer mapping |
| NOISE-8888-A | Invalid Entry 540 | Data quality insufficient |
| NOISE-6076-D | Invalid Entry 525 | Duplicate detected |
| NOISE-7521-E | Invalid Entry 885 | Out of scope per business decision |
| NOISE-1285-B | Invalid Entry 542 | Out of scope per business decision |
| NOISE-2617-G | Invalid Entry 540 | Superseded by newer mapping |
| NOISE-3681-B | Invalid Entry 824 | Out of scope per business decision |
| NOISE-4809-B | Invalid Entry 532 | Duplicate detected |
| NOISE-2380-H | Invalid Entry 982 | Out of scope per business decision |
| NOISE-5463-E | Invalid Entry 635 | Superseded by newer mapping |
| NOISE-8832-E | Invalid Entry 121 | Duplicate detected |
| NOISE-7622-A | Invalid Entry 893 | Duplicate detected |
| NOISE-3230-D | Invalid Entry 857 | Duplicate detected |
| NOISE-5342-E | Invalid Entry 180 | Superseded by newer mapping |
| NOISE-7356-H | Invalid Entry 964 | Superseded by newer mapping |
| NOISE-6189-A | Invalid Entry 642 | Data quality insufficient |
| NOISE-6820-G | Invalid Entry 389 | Superseded by newer mapping |
| NOISE-5437-D | Invalid Entry 776 | Out of scope per business decision |
| NOISE-7093-A | Invalid Entry 682 | Data quality insufficient |
| NOISE-2540-E | Invalid Entry 679 | Superseded by newer mapping |
| NOISE-9858-A | Invalid Entry 284 | Superseded by newer mapping |
| NOISE-4896-C | Invalid Entry 956 | Pending validation |
| NOISE-7831-A | Invalid Entry 528 | Out of scope per business decision |
| NOISE-8465-C | Invalid Entry 699 | Duplicate detected |
| NOISE-9407-A | Invalid Entry 114 | Data quality insufficient |
| NOISE-2511-E | Invalid Entry 647 | Duplicate detected |
| NOISE-3623-B | Invalid Entry 880 | Duplicate detected |
| NOISE-4011-A | Invalid Entry 640 | Superseded by newer mapping |
| NOISE-3899-G | Invalid Entry 860 | Superseded by newer mapping |
| NOISE-9932-D | Invalid Entry 953 | Out of scope per business decision |
| NOISE-7605-E | Invalid Entry 432 | Pending validation |
| NOISE-6603-G | Invalid Entry 495 | Duplicate detected |
| NOISE-2195-F | Invalid Entry 591 | Out of scope per business decision |
| NOISE-2900-E | Invalid Entry 903 | Data quality insufficient |
| NOISE-3426-C | Invalid Entry 633 | Out of scope per business decision |
| NOISE-2133-G | Invalid Entry 793 | Out of scope per business decision |
| NOISE-9011-B | Invalid Entry 849 | Data quality insufficient |
| NOISE-1397-G | Invalid Entry 101 | Duplicate detected |
| NOISE-9334-B | Invalid Entry 513 | Out of scope per business decision |
| NOISE-8278-F | Invalid Entry 890 | Duplicate detected |
| NOISE-7212-A | Invalid Entry 723 | Out of scope per business decision |
| NOISE-4958-B | Invalid Entry 248 | Pending validation |
| NOISE-3512-H | Invalid Entry 589 | Duplicate detected |
| NOISE-6423-C | Invalid Entry 882 | Duplicate detected |
| NOISE-1541-B | Invalid Entry 703 | Pending validation |
| NOISE-1867-A | Invalid Entry 363 | Superseded by newer mapping |
| NOISE-4667-C | Invalid Entry 129 | Out of scope per business decision |
| NOISE-4532-D | Invalid Entry 693 | Superseded by newer mapping |
| NOISE-1961-F | Invalid Entry 360 | Superseded by newer mapping |
| NOISE-6094-B | Invalid Entry 127 | Data quality insufficient |
| NOISE-1845-A | Invalid Entry 326 | Data quality insufficient |
| NOISE-4079-A | Invalid Entry 363 | Data quality insufficient |
| NOISE-4430-H | Invalid Entry 172 | Pending validation |
| NOISE-4898-C | Invalid Entry 225 | Pending validation |
| NOISE-3401-E | Invalid Entry 612 | Superseded by newer mapping |
| NOISE-3442-H | Invalid Entry 679 | Duplicate detected |
| NOISE-5073-G | Invalid Entry 666 | Duplicate detected |
| NOISE-1997-B | Invalid Entry 450 | Superseded by newer mapping |
| NOISE-4624-H | Invalid Entry 446 | Out of scope per business decision |
| NOISE-5005-G | Invalid Entry 663 | Data quality insufficient |
| NOISE-8235-F | Invalid Entry 487 | Duplicate detected |
| NOISE-9675-G | Invalid Entry 196 | Superseded by newer mapping |
| NOISE-7531-D | Invalid Entry 676 | Duplicate detected |
| NOISE-5154-F | Invalid Entry 692 | Superseded by newer mapping |
| NOISE-4534-B | Invalid Entry 459 | Pending validation |
| NOISE-4649-D | Invalid Entry 678 | Pending validation |
| NOISE-9978-A | Invalid Entry 949 | Pending validation |
| NOISE-8444-E | Invalid Entry 818 | Data quality insufficient |
| NOISE-9453-G | Invalid Entry 655 | Pending validation |
| NOISE-5739-E | Invalid Entry 687 | Superseded by newer mapping |
| NOISE-5140-B | Invalid Entry 646 | Duplicate detected |
| NOISE-3306-E | Invalid Entry 419 | Duplicate detected |
| NOISE-2155-F | Invalid Entry 655 | Out of scope per business decision |
| NOISE-3248-B | Invalid Entry 440 | Duplicate detected |
| NOISE-2389-A | Invalid Entry 688 | Superseded by newer mapping |
| NOISE-5776-C | Invalid Entry 176 | Pending validation |
| NOISE-1739-G | Invalid Entry 128 | Pending validation |
| NOISE-3949-E | Invalid Entry 804 | Superseded by newer mapping |
| NOISE-2934-D | Invalid Entry 667 | Superseded by newer mapping |
| NOISE-5252-E | Invalid Entry 168 | Superseded by newer mapping |
| NOISE-8555-E | Invalid Entry 789 | Superseded by newer mapping |
| NOISE-8393-D | Invalid Entry 907 | Out of scope per business decision |
| NOISE-4202-F | Invalid Entry 585 | Data quality insufficient |
| NOISE-1174-B | Invalid Entry 961 | Duplicate detected |
| NOISE-9213-G | Invalid Entry 370 | Duplicate detected |
| NOISE-5023-F | Invalid Entry 245 | Superseded by newer mapping |
| NOISE-4572-H | Invalid Entry 676 | Duplicate detected |
| NOISE-2809-G | Invalid Entry 791 | Pending validation |
| NOISE-5246-E | Invalid Entry 419 | Superseded by newer mapping |
| NOISE-5420-F | Invalid Entry 732 | Out of scope per business decision |
| NOISE-5646-C | Invalid Entry 292 | Duplicate detected |
| NOISE-9218-G | Invalid Entry 785 | Pending validation |
| NOISE-5907-B | Invalid Entry 425 | Pending validation |
| NOISE-5138-D | Invalid Entry 981 | Duplicate detected |
| NOISE-5527-F | Invalid Entry 890 | Pending validation |
| NOISE-9761-E | Invalid Entry 149 | Data quality insufficient |
| NOISE-2645-B | Invalid Entry 326 | Superseded by newer mapping |
| NOISE-8151-A | Invalid Entry 860 | Duplicate detected |
| NOISE-4483-E | Invalid Entry 352 | Pending validation |
| NOISE-9291-A | Invalid Entry 307 | Pending validation |
| NOISE-6365-G | Invalid Entry 223 | Data quality insufficient |
| NOISE-3443-B | Invalid Entry 384 | Duplicate detected |
| NOISE-6462-H | Invalid Entry 220 | Data quality insufficient |
| NOISE-6063-D | Invalid Entry 324 | Data quality insufficient |
| NOISE-2389-B | Invalid Entry 723 | Duplicate detected |
| NOISE-4871-A | Invalid Entry 738 | Data quality insufficient |
| NOISE-5144-F | Invalid Entry 776 | Superseded by newer mapping |
| NOISE-1187-D | Invalid Entry 214 | Pending validation |
| NOISE-5187-E | Invalid Entry 822 | Superseded by newer mapping |
| NOISE-2743-F | Invalid Entry 715 | Duplicate detected |
| NOISE-7374-A | Invalid Entry 116 | Data quality insufficient |
| NOISE-2259-A | Invalid Entry 621 | Duplicate detected |
| NOISE-6645-H | Invalid Entry 525 | Data quality insufficient |
| NOISE-6349-D | Invalid Entry 951 | Data quality insufficient |
| NOISE-6782-E | Invalid Entry 244 | Out of scope per business decision |
| NOISE-9582-B | Invalid Entry 130 | Out of scope per business decision |
| NOISE-5890-B | Invalid Entry 905 | Pending validation |
| NOISE-2814-E | Invalid Entry 105 | Out of scope per business decision |
| NOISE-4633-G | Invalid Entry 236 | Data quality insufficient |
| NOISE-6066-C | Invalid Entry 422 | Data quality insufficient |
| NOISE-4449-A | Invalid Entry 705 | Out of scope per business decision |
| NOISE-6545-H | Invalid Entry 161 | Pending validation |
| NOISE-2471-A | Invalid Entry 798 | Data quality insufficient |
| NOISE-2068-H | Invalid Entry 191 | Out of scope per business decision |
| NOISE-6147-G | Invalid Entry 604 | Duplicate detected |
| NOISE-8666-H | Invalid Entry 530 | Pending validation |
| NOISE-3696-G | Invalid Entry 169 | Pending validation |
| NOISE-1366-C | Invalid Entry 165 | Superseded by newer mapping |
| NOISE-1619-C | Invalid Entry 315 | Data quality insufficient |
| NOISE-9387-B | Invalid Entry 368 | Out of scope per business decision |
| NOISE-8794-G | Invalid Entry 353 | Out of scope per business decision |
| NOISE-8506-G | Invalid Entry 692 | Pending validation |
| NOISE-7979-F | Invalid Entry 218 | Data quality insufficient |
| NOISE-9263-E | Invalid Entry 360 | Pending validation |
| NOISE-8186-G | Invalid Entry 990 | Data quality insufficient |
| NOISE-7116-A | Invalid Entry 547 | Pending validation |
| NOISE-8718-E | Invalid Entry 120 | Data quality insufficient |
| NOISE-2115-G | Invalid Entry 190 | Superseded by newer mapping |
| NOISE-1268-F | Invalid Entry 276 | Out of scope per business decision |
| NOISE-9585-G | Invalid Entry 262 | Superseded by newer mapping |
| NOISE-8949-F | Invalid Entry 642 | Superseded by newer mapping |
| NOISE-4458-F | Invalid Entry 920 | Duplicate detected |
| NOISE-7252-D | Invalid Entry 897 | Superseded by newer mapping |
| NOISE-6044-B | Invalid Entry 145 | Superseded by newer mapping |
| NOISE-3730-D | Invalid Entry 697 | Pending validation |
| NOISE-3742-E | Invalid Entry 229 | Duplicate detected |
| NOISE-5729-H | Invalid Entry 157 | Data quality insufficient |
| NOISE-5496-G | Invalid Entry 857 | Out of scope per business decision |
| NOISE-5049-B | Invalid Entry 902 | Duplicate detected |
| NOISE-2390-D | Invalid Entry 713 | Duplicate detected |
| NOISE-6651-H | Invalid Entry 857 | Data quality insufficient |
| NOISE-7403-C | Invalid Entry 272 | Pending validation |
| NOISE-8873-C | Invalid Entry 878 | Superseded by newer mapping |
| NOISE-6712-D | Invalid Entry 892 | Data quality insufficient |
| NOISE-1150-B | Invalid Entry 953 | Superseded by newer mapping |
| NOISE-6702-G | Invalid Entry 706 | Duplicate detected |
| NOISE-6117-H | Invalid Entry 153 | Out of scope per business decision |
| NOISE-9199-B | Invalid Entry 508 | Superseded by newer mapping |
| NOISE-3042-G | Invalid Entry 485 | Out of scope per business decision |
| NOISE-3396-H | Invalid Entry 852 | Out of scope per business decision |
| NOISE-4377-H | Invalid Entry 468 | Superseded by newer mapping |
| NOISE-2289-F | Invalid Entry 393 | Out of scope per business decision |
| NOISE-7393-C | Invalid Entry 955 | Duplicate detected |
| NOISE-1564-D | Invalid Entry 239 | Out of scope per business decision |
| NOISE-9666-C | Invalid Entry 174 | Superseded by newer mapping |
| NOISE-2205-D | Invalid Entry 897 | Superseded by newer mapping |
| NOISE-8117-F | Invalid Entry 755 | Pending validation |
| NOISE-1073-A | Invalid Entry 850 | Pending validation |
| NOISE-3425-B | Invalid Entry 365 | Duplicate detected |
| NOISE-4906-B | Invalid Entry 989 | Out of scope per business decision |
| NOISE-5126-B | Invalid Entry 597 | Superseded by newer mapping |
| NOISE-4360-H | Invalid Entry 652 | Duplicate detected |
| NOISE-6518-E | Invalid Entry 765 | Pending validation |
| NOISE-3676-D | Invalid Entry 385 | Data quality insufficient |
| NOISE-9792-C | Invalid Entry 506 | Data quality insufficient |
| NOISE-7908-D | Invalid Entry 275 | Pending validation |
| NOISE-1177-E | Invalid Entry 313 | Superseded by newer mapping |
| NOISE-6589-A | Invalid Entry 862 | Data quality insufficient |
| NOISE-1951-F | Invalid Entry 257 | Data quality insufficient |
| NOISE-3854-E | Invalid Entry 461 | Superseded by newer mapping |
| NOISE-3688-A | Invalid Entry 916 | Data quality insufficient |
| NOISE-1513-B | Invalid Entry 923 | Data quality insufficient |
| NOISE-4953-D | Invalid Entry 105 | Superseded by newer mapping |

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
