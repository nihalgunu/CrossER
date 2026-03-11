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
| Total entities assessed | 1446 | Completed |
| Successfully mapped | 1044 | Verified |
| Excluded from scope | 313 | Documented |
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
| Isoglucose 25% | palm oil tech grade | auto_generated | Historical match confirmed |
| Fructose 99.5% Technische Qualität | SIG-42-AYY-K71K | auto_generated | Confirmed by domain expert |
| SIG-61-XKV-ODPX | Maltodextrin DE20 | unverified | Confirmed by domain expert |
| SIG-45-ZZU-GRXH International | premier manufacturing BV | unverified | Cross-referenced with transactions |
| SIG-77-TUK-IN2B | Ascorbic Acid 98% Pharmazeutisch rein | unverified | Cross-referenced with transactions |
| SIG-76-YLU-7DL9 | Natriumchlorid 25% Premiumqualität | auto_generated | Cross-referenced with transactions |
| sorbic acid | Pea Protein 99.5% Premiumqualität | unverified | Confirmed by domain expert |
| zenith logistics | SIG-36-PCG-IRVO | unverified | Historical match confirmed |
| VA-RE-I-20-892 | Excise GB 19% | unverified | Confirmed by domain expert |
| SIG-29-BZP-SU62 | SO-BE-70-PR-120 | pending_review | Verified via product specs |
| Isoglucose 70% | Dextrin | unverified | Verified via product specs |
| Fructose 25% | SIG-66-AQR-B68Q | auto_generated | Historical match confirmed |
| SIG-79-SPO-WT80 | Sorbinsäure | pending_review | Verified via product specs |
| Calcium Carbonate 98% | isoglucose 70% premium | unverified | Confirmed by domain expert |
| Atlas Materials | SIG-98-HZM-47LK | pending_review | Historical match confirmed |
| nexus supply | Quantum Partners Group | pending_review | Confirmed by domain expert |
| RE-ST-FO-GR-238 | SIG-50-ABM-7VSK | auto_generated | Confirmed by domain expert |
| Sorbinsäure 50% Lebensmittelrein | Dextrose 70% | auto_generated | Verified via product specs |
| Potassium Sorbate 50% Technical | rapeseed oil standard | unverified | Cross-referenced with transactions |
| SIG-69-TRZ-SFLQ | EX-U-15-972 | unverified | Auto-mapped, validated |
| vanguard industries AG | PA-EN-915 | auto_generated | Auto-mapped, validated |
| SIG-42-AJS-6RPK | Soja Isolate | pending_review | Auto-mapped, validated |
| SIG-43-XDN-7VEU | Excise CN 19% | auto_generated | Verified via product specs |
| Fructose | lactic acid | auto_generated | Confirmed by domain expert |
| core chemicals Group | HO-PA-149 International | pending_review | Auto-mapped, validated |
| Zitronensäure Qualitätsstufe I | Palm Oil 70% Pharma Grade | auto_generated | Auto-mapped, validated |
| CO-OI-50-PH-GR-568 | maltodextrin de30 | unverified | Verified via product specs |
| Fructose 25% | SIG-80-WEB-2C7R | pending_review | Cross-referenced with transactions |
| SIG-95-APX-PWFS | rapeseed oil premium | pending_review | Auto-mapped, validated |
| Dextrin Premium | SO-CH-99.5-618 | auto_generated | Confirmed by domain expert |
| SIG-10-DWM-ZA0C | Kasein 25% Pharmazeutisch rein | pending_review | Auto-mapped, validated |
| ME-LO-670 | SIG-13-NXM-NP9H | unverified | Historical match confirmed |
| Pea Protein 98% Grade B | Natriumbenzoat | unverified | Confirmed by domain expert |
| sunflower oil | CI-AC-99.5-469 | unverified | Confirmed by domain expert |
| SIG-38-OTV-E78M | Withholding US 10% | auto_generated | Historical match confirmed |
| Resistant Starch Grade A | Sorbinsäure 98% | auto_generated | Cross-referenced with transactions |
| SIG-30-LJO-TN4Y | PE-PR-25-472 | auto_generated | Auto-mapped, validated |
| Vanguard Materials | AT-SO-226 | auto_generated | Verified via product specs |
| calcium carbonate 50% premium | Ascorbic Acid 99.5% Premium | auto_generated | Auto-mapped, validated |
| CU-DU-F-5-228 | Vat Standardqualität DE 25% | unverified | Verified via product specs |
| Lactic Acid 70% Pharmazeutisch rein | Dextrin 50% | auto_generated | Auto-mapped, validated |
| SIG-19-TLQ-1P5Z | MA-DE-146 | pending_review | Cross-referenced with transactions |
| Sorbinsäure | isoglucose | unverified | Auto-mapped, validated |
| Fructose | FR-PR-346 | pending_review | Cross-referenced with transactions |
| SIG-84-HBF-DDQL | sorbic acid 25% pharma grade | unverified | Historical match confirmed |
| dextrose 25% | Calcium Carbonate 99.5% | auto_generated | Verified via product specs |
| Weizenklebereiweiß Qualitätsstufe I | SIG-36-ABO-ZBYW | auto_generated | Verified via product specs |
| vertex logistics | QU-SO-233 | pending_review | Confirmed by domain expert |
| Sodium Chloride 99.5% Grade A | Soja Isolate 98% | pending_review | Confirmed by domain expert |
| Dextrin Grade B | SIG-16-FQO-8S1S | pending_review | Auto-mapped, validated |
| WH-GL-50-TE-338 | Sodium Benzoate 25% Standard | unverified | Historical match confirmed |
| CE-LO-195 | Continental Processing Group | unverified | Cross-referenced with transactions |
| SU-OI-FO-GR-778 | Soja Isolate 70% | pending_review | Auto-mapped, validated |
| Withholding NL 5% | Vat Reduced NL 25% | unverified | Historical match confirmed |
| VE-SO-401 | atlas materials | unverified | Verified via product specs |
| Sunflower Oil Pharma Grade | SIG-50-JOR-LO4P | auto_generated | Verified via product specs |
| Sorbic Acid 50% Grade A | Ascorbic Acid Premiumqualität | unverified | Auto-mapped, validated |
| atlantic processing Holdings | Central Processing | unverified | Historical match confirmed |
| pacific industries | AP-MA-145 International | pending_review | Historical match confirmed |
| Resistant Starch 98% Pharma Grade | soy isolate 25% | pending_review | Auto-mapped, validated |
| SIG-68-HOK-ETCC | nexus industries | auto_generated | Verified via product specs |
| continental solutions SARL | SIG-54-ZFB-4REP Inc. | auto_generated | Cross-referenced with transactions |
| Ascorbic Acid | Rapsöl 99.5% | unverified | Historical match confirmed |
| premier manufacturing BV | Vertex Solutions BV | pending_review | Historical match confirmed |
| SIG-75-DRM-1CLN | CA-CA-25-PH-GR-684 | pending_review | Historical match confirmed |
| IS-641 | fructose standard | unverified | Cross-referenced with transactions |
| Dextrose Grade B | SIG-31-ZKD-VVIA | pending_review | Auto-mapped, validated |
| VA-RE-G-25-615 | Withholding BR 20% | pending_review | Confirmed by domain expert |
| Quantum Partners | AP-CH-617 LLC | unverified | Auto-mapped, validated |
| Premier Handel Group | PI-SO-581 Inc. | pending_review | Confirmed by domain expert |
| Pacific Materials | SIG-26-NTJ-I6T6 | unverified | Historical match confirmed |
| Withholding US 25% | Vat Standardqualität NL 20% | auto_generated | Cross-referenced with transactions |
| Atlantic Trading | quantum manufacturing GmbH | pending_review | Confirmed by domain expert |
| coconut oil 25% tech grade | Fructose Food Grade | unverified | Cross-referenced with transactions |
| LA-AC-927 | Cyclodextrin | auto_generated | Confirmed by domain expert |
| Kasein 98% | Soy Isolate 25% Technical | unverified | Confirmed by domain expert |
| RA-OI-25-FO-GR-818 | dextrose premium | auto_generated | Confirmed by domain expert |
| cyclodextrin 98% | PE-PR-TE-718 | unverified | Confirmed by domain expert |
| Zitronensäure Qualitätsstufe II | Wheat Gluten 98% Premium | unverified | Auto-mapped, validated |
| DE-70-856 | Fructose 70% | unverified | Cross-referenced with transactions |
| Zitronensäure | SIG-67-MFG-46DE | pending_review | Historical match confirmed |
| AS-AC-573 | SIG-99-IMJ-KFOM | unverified | Cross-referenced with transactions |
| Stratos Distribution Group | SIG-77-WCC-DNFC Holdings | unverified | Cross-referenced with transactions |
| PR-SU-CO-443 | Vertex Versorgung GmbH | pending_review | Cross-referenced with transactions |
| SIG-83-XMM-APXP | Palmfett 98% Qualitätsstufe I | pending_review | Historical match confirmed |
| premier partners SARL | Central Logistik GmbH | auto_generated | Cross-referenced with transactions |
| Rapeseed Oil Technical | SIG-99-IMJ-KFOM | auto_generated | Historical match confirmed |
| SIG-55-DBH-2QS3 | nexus materials | auto_generated | Verified via product specs |
| Prism Sourcing | SIG-86-ILL-9XTM | pending_review | Historical match confirmed |
| lactic acid standard | CI-AC-98-939 | auto_generated | Cross-referenced with transactions |
| Core Chemicals Holdings | SIG-42-UOJ-4ACC Holdings | auto_generated | Auto-mapped, validated |
| soy isolate | Sorbinsäure | auto_generated | Verified via product specs |
| Premier Supply Co. | vanguard sourcing | unverified | Verified via product specs |
| pinnacle distribution Holdings | Atlantic Manufacturing | auto_generated | Verified via product specs |
| Traubenzucker 98% Qualitätsstufe I | AS-AC-279 | auto_generated | Verified via product specs |
| Coconut Oil 25% Grade A | CO-OI-FO-GR-870 | auto_generated | Verified via product specs |
| soy isolate 99.5% premium | MA-DE-161 | auto_generated | Auto-mapped, validated |
| PR-IN-608 BV | Catalyst Industrien International | unverified | Auto-mapped, validated |
| Atlas Enterprise International | SIG-13-RWR-7JHQ SA | auto_generated | Verified via product specs |
| Zitronensäure Premiumqualität | SIG-64-LXA-3LJO | pending_review | Cross-referenced with transactions |
| QU-SU-CO-890 | SIG-24-YWL-8DWF | unverified | Historical match confirmed |
| SIG-86-EKJ-RFVB | Atlas Versorgung GmbH | pending_review | Cross-referenced with transactions |
| Resistant Starch 99.5% | ascorbic acid | auto_generated | Historical match confirmed |
| SIG-18-PCA-V46E | Dextrose | auto_generated | Verified via product specs |
| resistant starch standard | SIG-44-MHK-SRCB | pending_review | Historical match confirmed |
| PI-SO-581 Inc. | SIG-69-CZY-YXFK | pending_review | Cross-referenced with transactions |
| Withholding NL 21% | VA-ST-N-25-114 | unverified | Verified via product specs |
| SIG-33-IWB-UV4J | zenith supply | auto_generated | Historical match confirmed |
| Palmfett 98% Qualitätsstufe I | SIG-82-VDF-0XQT | pending_review | Confirmed by domain expert |
| NO-SU-CO-498 | Premier Versorgung GmbH | pending_review | Confirmed by domain expert |
| ascorbic acid 98% premium | Kaliumsorbat | pending_review | Verified via product specs |
| stratos logistics | SIG-83-SGE-Q8I0 | auto_generated | Cross-referenced with transactions |
| PR-CO-800 Corp. | horizon commodities PLC | unverified | Confirmed by domain expert |
| Casein 98% Technical | Pea Protein Premiumqualität | auto_generated | Confirmed by domain expert |
| SIG-47-MIU-LIH6 | Pacific Versorgung GmbH | unverified | Auto-mapped, validated |
| SIG-99-VAH-2H31 | DE-GR-A-472 | pending_review | Verified via product specs |
| Elite Supply Co. | VE-SO-366 | unverified | Historical match confirmed |
| horizon ingredients LLC | Vertex Distribution Holdings | pending_review | Cross-referenced with transactions |
| Palm Oil Food Grade | SIG-93-GFI-NZRV | unverified | Historical match confirmed |
| SIG-58-NYA-2O4M | rapeseed oil 50% pharma grade | auto_generated | Verified via product specs |
| Vertex Vertrieb Group | SIG-23-WOJ-YTND International | pending_review | Auto-mapped, validated |
| Core Distribution | QU-PA-830 Group | auto_generated | Cross-referenced with transactions |
| nexus logistics | SIG-47-MLZ-TPP5 | unverified | Verified via product specs |
| casein premium | Soy Isolate Grade B | pending_review | Auto-mapped, validated |
| SO-BE-ST-871 | glucose syrup 99.5% food grade | unverified | Historical match confirmed |
| Zitronensäure 98% | SIG-42-BEO-614U | auto_generated | Historical match confirmed |
| premier enterprise Holdings | Baltic Solutions International | pending_review | Verified via product specs |
| Citric Acid 50% Grade A | SIG-82-GZF-51ZF | auto_generated | Confirmed by domain expert |
| apex enterprise International | Global Ingredients BV | unverified | Historical match confirmed |
| SIG-33-FUV-53NO | GL-SY-PR-440 | pending_review | Auto-mapped, validated |
| SO-IS-PH-GR-671 | SIG-90-SJW-O06V | unverified | Verified via product specs |
| Quantum Supply Co. | NO-SO-478 | pending_review | Verified via product specs |
| cyclodextrin 98% pharma grade | Maltodextrin DE5 | pending_review | Verified via product specs |
| SO-CH-GR-B-273 | Pea Protein 70% Premiumqualität | unverified | Confirmed by domain expert |
| Traubenzucker Qualitätsstufe I | SIG-42-LOE-5XD8 | pending_review | Confirmed by domain expert |
| Palm Oil 98% | Ascorbic Acid | unverified | Confirmed by domain expert |
| Meridian Logistics | NE-MA-923 | unverified | Cross-referenced with transactions |
| PI-LO-142 | Pacific Sourcing | unverified | Verified via product specs |
| SIG-82-JMP-PVGN | Casein Grade A | unverified | Confirmed by domain expert |
| SO-BE-GR-A-760 | Kaliumsorbat 50% Technische Qualität | auto_generated | Confirmed by domain expert |
| SIG-92-VAB-1JHU | Dextrin | unverified | Auto-mapped, validated |
| CO-OI-25-TE-157 | Calcium Carbonate 99.5% | unverified | Auto-mapped, validated |
| SIG-34-UJK-TJA6 | Sodium Benzoate 50% Technical | pending_review | Confirmed by domain expert |
| Sorbic Acid 25% Grade B | SIG-93-UJT-52AL | pending_review | Confirmed by domain expert |
| Sorbinsäure 70% | PA-OI-PH-GR-124 | unverified | Cross-referenced with transactions |
| Catalyst Materials | elite sourcing | pending_review | Historical match confirmed |
| Pacific Werkstoffe | Quantum Logistics | unverified | Verified via product specs |
| Soy Isolate 98% Food Grade | sorbic acid 70% | unverified | Verified via product specs |
| fructose 70% | Sorbinsäure | pending_review | Cross-referenced with transactions |
| SIG-79-HKV-T268 | GL-MA-770 | unverified | Cross-referenced with transactions |
| PO-SO-339 | Cyclodextrin | unverified | Verified via product specs |
| Vat Standard NL 19% | VA-ST-D-25-524 | pending_review | Historical match confirmed |
| RA-OI-431 | Lactic Acid 50% Grade A | pending_review | Cross-referenced with transactions |
| AP-SO-576 | SIG-22-SOG-POO8 | auto_generated | Verified via product specs |
| sodium chloride 99.5% premium | CI-AC-215 | pending_review | Auto-mapped, validated |
| Stratos Partners SAS | PR-IN-608 BV | pending_review | Cross-referenced with transactions |
| SIG-38-WKO-LWQT | Prime Materials | unverified | Confirmed by domain expert |
| PA-SO-270 | Pacific Sourcing | unverified | Verified via product specs |
| SIG-77-RVO-CE8D Inc. | horizon logistics PLC | auto_generated | Confirmed by domain expert |
| Ascorbic Acid Pharmazeutisch rein | AS-AC-70-515 | auto_generated | Verified via product specs |
| Prism Sourcing | Core Sourcing | pending_review | Verified via product specs |
| PA-CH-580 KG | horizon processing International | unverified | Historical match confirmed |
| Isoglucose | SIG-15-MKL-LGBK | unverified | Cross-referenced with transactions |
| PO-SO-768 | SIG-63-YJW-AP00 | unverified | Cross-referenced with transactions |
| CA-CA-99.5-291 | Ascorbic Acid 70% | pending_review | Historical match confirmed |
| SIG-14-TOH-IPJ4 | Core Chemicals AG | unverified | Cross-referenced with transactions |
| SIG-27-RTX-YEAW | calcium carbonate 99.5% food grade | pending_review | Auto-mapped, validated |
| SO-IS-GR-A-940 | SIG-65-EFS-5P03 | unverified | Historical match confirmed |
| quantum processing International | Prism Materials Ltd. | auto_generated | Historical match confirmed |
| SIG-27-FHB-EY0E | CA-LO-415 | pending_review | Auto-mapped, validated |
| FR-99.5-TE-579 | SIG-83-BZY-VHAE | auto_generated | Auto-mapped, validated |
| Vanguard Enterprise International | Pacific Rohstoffe International | pending_review | Historical match confirmed |
| ascorbic acid standard | Maltodextrin-Pulver DE10 | pending_review | Confirmed by domain expert |
| Lactic Acid 25% Lebensmittelrein | PA-OI-TE-134 | pending_review | Confirmed by domain expert |
| SIG-81-HMA-4WEQ | Vat Standardqualität CN 19% | auto_generated | Verified via product specs |
| Vat Standardqualität FR 21% | Vat Reduced FR 25% | pending_review | Historical match confirmed |
| Stellar Werkstoffe | nordic supply | auto_generated | Historical match confirmed |
| Fructose | SIG-20-ISN-0EWL | pending_review | Confirmed by domain expert |
| horizon trading Ltd. | NE-PR-315 Holdings | unverified | Cross-referenced with transactions |
| Resistente Stärke | sodium benzoate 99.5% premium | pending_review | Auto-mapped, validated |
| SIG-73-AXD-XIX9 | Vanguard Supply Co. | pending_review | Verified via product specs |
| Prism Manufacturing NV | meridian distribution Group | auto_generated | Confirmed by domain expert |
| Vanguard Industries BV | baltic chemicals | auto_generated | Verified via product specs |
| Nordic Supply Co. | SIG-75-GGJ-DK9O | auto_generated | Confirmed by domain expert |
| Elite Manufacturing | SIG-80-QLX-7SNL SAS | auto_generated | Historical match confirmed |
| SIG-58-BDQ-I1V3 | Pinnacle Supply Co. | auto_generated | Verified via product specs |
| Pea Protein 70% Technische Qualität | SIG-51-ZAY-11PM | unverified | Auto-mapped, validated |
| PA-SO-568 | Pacific Werkstoffe | pending_review | Historical match confirmed |
| Pinnacle Rohstoffe NV | SIG-54-ZOX-KCNY SAS | unverified | Verified via product specs |
| Vanguard Enterprise Group | SIG-50-PBC-BNK3 LLC | unverified | Auto-mapped, validated |
| Fructose | rapeseed oil 98% | pending_review | Cross-referenced with transactions |
| WH-GL-GR-A-583 | Sunflower Oil Grade B | unverified | Cross-referenced with transactions |
| Kasein | SO-BE-GR-B-914 | unverified | Confirmed by domain expert |
| Natriumbenzoat 25% | SIG-30-RXC-HFDI | pending_review | Confirmed by domain expert |
| NE-SO-652 | Central Versorgung GmbH | pending_review | Auto-mapped, validated |
| fructose tech grade | Sodium Benzoate Grade B | pending_review | Cross-referenced with transactions |
| Meridian Logistics | VE-LO-603 | unverified | Confirmed by domain expert |
| PR-SU-CO-349 | Elite Werkstoffe | unverified | Cross-referenced with transactions |
| vanguard supply NV | SIG-54-QHS-YUMN | pending_review | Cross-referenced with transactions |
| maltodextrin de15 | Maltodextrin DE20 | auto_generated | Confirmed by domain expert |
| CA-CA-50-GR-A-195 | Lactic Acid 50% Grade A | auto_generated | Verified via product specs |
| Horizon Partners | prime supply PLC | auto_generated | Verified via product specs |
| Ascorbic Acid 99.5% Technische Qualität | SIG-72-IMA-8RAP | auto_generated | Historical match confirmed |
| VA-PA-407 | atlas solutions | pending_review | Confirmed by domain expert |
| SO-AC-25-ST-106 | SIG-39-BAT-DD7R | auto_generated | Cross-referenced with transactions |
| PI-MA-680 | SIG-16-ICW-E4VV | auto_generated | Historical match confirmed |
| SIG-60-VTH-H7AM | Vertex Sourcing | auto_generated | Auto-mapped, validated |
| VA-RE-N-10-785 | SIG-67-YOR-JCUH | unverified | Verified via product specs |
| Natriumbenzoat | sodium chloride 98% pharma grade | auto_generated | Verified via product specs |
| SIG-92-GIK-H4FF | Excise NL 0% | pending_review | Confirmed by domain expert |
| Global Solutions Group | ST-LO-635 LLC | pending_review | Verified via product specs |
| SIG-15-MKL-LGBK | calcium carbonate 25% pharma grade | auto_generated | Verified via product specs |
| Vanguard Supply Co. | Atlas Versorgung GmbH | pending_review | Verified via product specs |
| PR-IN-195 KG | SIG-42-SPP-A6C6 | unverified | Confirmed by domain expert |
| Customs Duty DE 5% | SIG-20-IMA-GJKF | auto_generated | Confirmed by domain expert |
| continental manufacturing Inc. | Premier Solutions | auto_generated | Historical match confirmed |
| Customs Duty US 20% | Vat Standard IN 19% | auto_generated | Verified via product specs |
| VE-SO-366 | Core Sourcing | unverified | Verified via product specs |
| Soy Isolate | Pea Protein | unverified | Historical match confirmed |
| coconut oil | Sodium Benzoate Food Grade | pending_review | Historical match confirmed |
| AS-AC-PR-778 | sodium benzoate 99.5% tech grade | auto_generated | Confirmed by domain expert |
| Resistente Stärke | SO-CH-98-GR-B-961 | auto_generated | Verified via product specs |
| Catalyst Industries International | SIG-87-OKN-L3O4 | auto_generated | Verified via product specs |
| SIG-70-EXR-LD0M | Stellar Commodities | pending_review | Auto-mapped, validated |
| Potassium Sorbate Technical | AS-AC-50-321 | unverified | Verified via product specs |
| Sodium Benzoate Grade A | rapeseed oil 50% premium | unverified | Cross-referenced with transactions |
| ZE-PA-511 PLC | vanguard industries Inc. | auto_generated | Confirmed by domain expert |
| SIG-97-EIS-DKQB Holdings | AT-IN-847 GmbH | auto_generated | Historical match confirmed |
| Lactic Acid | GL-SY-70-655 | unverified | Auto-mapped, validated |
| SIG-94-MKW-LH8F | vat standard de 7% | auto_generated | Auto-mapped, validated |
| Elite Logistics Holdings | VA-MA-681 PLC | unverified | Verified via product specs |
| casein | SIG-50-XSG-WQVA | pending_review | Cross-referenced with transactions |
| Sorbinsäure 99.5% | dextrin | auto_generated | Cross-referenced with transactions |
| SIG-50-BJQ-W54O Holdings | stratos supply AG | unverified | Auto-mapped, validated |
| HO-MA-854 | Baltic Supply Co. | unverified | Confirmed by domain expert |
| SIG-22-DOP-7UDK | casein premium | unverified | Confirmed by domain expert |
| Kaliumsorbat | Ascorbic Acid 70% | unverified | Auto-mapped, validated |
| Vertex Distribution AG | Central Solutions | pending_review | Historical match confirmed |
| Ascorbic Acid 70% | Traubenzucker Standardqualität | auto_generated | Historical match confirmed |
| SIG-52-CQW-KL19 | PR-EN-809 Holdings | pending_review | Cross-referenced with transactions |
| vanguard enterprise | Core Rohstoffe | pending_review | Cross-referenced with transactions |
| Palm Oil | SO-AC-50-FO-GR-250 | auto_generated | Cross-referenced with transactions |
| Isoglucose | WH-GL-146 | pending_review | Auto-mapped, validated |
| lactic acid | CA-25-TE-580 | pending_review | Auto-mapped, validated |
| PR-CH-808 AG | Premier Enterprise Holdings | auto_generated | Auto-mapped, validated |
| continental enterprise GmbH | Stratos Logistik | pending_review | Confirmed by domain expert |
| vat standard in 5% | SIG-43-KPC-8R3Y | auto_generated | Cross-referenced with transactions |
| Baltic Logistics | Meridian Werkstoffe | pending_review | Confirmed by domain expert |
| IS-641 | SIG-60-GHI-04X0 | unverified | Historical match confirmed |
| Sodium Benzoate 98% Standard | SIG-68-XQK-6G5I | pending_review | Cross-referenced with transactions |
| CO-MA-295 | Zenith Logistics | unverified | Verified via product specs |
| sodium chloride 98% standard | Resistant Starch 99.5% | pending_review | Confirmed by domain expert |
| Palm Oil 70% Pharma Grade | ascorbic acid pharma grade | auto_generated | Cross-referenced with transactions |
| SIG-39-MAR-LMVK | Isoglucose 70% | auto_generated | Confirmed by domain expert |
| SIG-43-NCZ-FT9Z | Lactic Acid | auto_generated | Auto-mapped, validated |
| Cyclodextrin Food Grade | Lactic Acid Qualitätsstufe I | pending_review | Historical match confirmed |
| SIG-20-XIG-T8ME | SO-AC-PH-GR-274 | auto_generated | Verified via product specs |
| SIG-92-FQX-S1BC | Stellar Vertrieb | unverified | Confirmed by domain expert |
| Continental Werkstoffe BV | quantum ingredients Holdings | auto_generated | Auto-mapped, validated |
| SIG-37-SOD-NFZK | Prime Rohstoffe LLC | pending_review | Cross-referenced with transactions |
| SIG-15-VIS-079C | Excise IN 10% | pending_review | Historical match confirmed |
| SIG-84-DSO-4S47 | CO-OI-966 | auto_generated | Historical match confirmed |
| Kasein 50% Premiumqualität | SU-OI-ST-338 | pending_review | Cross-referenced with transactions |
| Central Sourcing | Pinnacle Versorgung GmbH | unverified | Auto-mapped, validated |
| stratos sourcing | PA-LO-674 | pending_review | Historical match confirmed |
| nordic ingredients SARL | Pacific Werkstoffe GmbH | unverified | Verified via product specs |
| RA-OI-98-ST-938 | Calcium Carbonate 70% | auto_generated | Historical match confirmed |
| SIG-74-EPP-R9AG | VA-RE-U-10-922 | auto_generated | Verified via product specs |
| PA-OI-410 | glucose syrup | auto_generated | Auto-mapped, validated |
| resistant starch | Calcium Carbonate 50% | auto_generated | Cross-referenced with transactions |
| global materials | Horizon Sourcing | pending_review | Auto-mapped, validated |
| SIG-37-ZOD-1VME | Sodium Chloride 70% | auto_generated | Verified via product specs |
| casein standard | SIG-14-WZC-EEWK | pending_review | Historical match confirmed |
| CO-OI-50-PH-GR-568 | SIG-31-XRN-45GD | auto_generated | Auto-mapped, validated |
| Pinnacle Vertrieb Ltd. | Catalyst Ingredients International | auto_generated | Historical match confirmed |
| Fructose 70% | Sonnenblumenöl Qualitätsstufe I | unverified | Confirmed by domain expert |
| Cyclodextrin Qualitätsstufe I | AS-AC-70-133 | auto_generated | Auto-mapped, validated |
| Apex Logistik | SIG-81-AMW-NE5V | unverified | Auto-mapped, validated |
| premier sourcing | NO-SO-478 | unverified | Confirmed by domain expert |
| Prime Versorgung GmbH | SIG-36-RVG-E4FG | pending_review | Cross-referenced with transactions |
| GL-SU-CO-783 | SIG-20-RSZ-19RE | auto_generated | Historical match confirmed |
| SIG-57-YOY-F7N2 | Casein | pending_review | Verified via product specs |
| SIG-43-GRJ-P3HT | RE-ST-FO-GR-238 | pending_review | Verified via product specs |
| Customs Duty IN 25% | Customs Duty CN 10% | auto_generated | Cross-referenced with transactions |
| cyclodextrin premium | PO-SO-50-TE-497 | unverified | Verified via product specs |
| Atlas Sourcing | central logistics | pending_review | Verified via product specs |
| Dextrin Technische Qualität | dextrose 99.5% | pending_review | Auto-mapped, validated |
| SIG-98-JEQ-77GG | Sonnenblumenöl Pharmazeutisch rein | unverified | Historical match confirmed |
| Lactic Acid | SIG-42-AJS-6RPK | pending_review | Cross-referenced with transactions |
| Global Werkstoffe | SIG-37-DJF-CB5E | unverified | Confirmed by domain expert |
| CA-GR-B-950 | SIG-42-XLZ-4BOM | unverified | Confirmed by domain expert |
| Vat Standard NL 20% | withholding us 21% | auto_generated | Auto-mapped, validated |
| SIG-29-BZP-SU62 | Dextrin Technische Qualität | auto_generated | Auto-mapped, validated |
| Natriumbenzoat Qualitätsstufe II | Resistant Starch 70% Food Grade | unverified | Historical match confirmed |
| Continental Chemicals Inc. | Core Logistics Holdings | pending_review | Confirmed by domain expert |
| Global Werkstoffe | AT-SU-CO-364 | auto_generated | Auto-mapped, validated |
| Customs Duty GB 0% | SIG-92-GIK-H4FF | pending_review | Confirmed by domain expert |
| Palmfett | Isoglucose 70% | auto_generated | Auto-mapped, validated |
| SIG-66-RQA-05UV | Glucose Syrup 99.5% Grade B | unverified | Auto-mapped, validated |
| Premier Enterprise | stellar distribution | unverified | Historical match confirmed |
| SIG-98-OXJ-W0H6 SAS | Atlas Chemicals SARL | auto_generated | Verified via product specs |
| Palmfett | Sodium Benzoate | auto_generated | Historical match confirmed |
| Maltodextrin DE20 | CO-OI-70-553 | pending_review | Verified via product specs |
| Zitronensäure Pharmazeutisch rein | Sodium Benzoate | pending_review | Cross-referenced with transactions |
| Soy Isolate Standard | SIG-30-ISA-9SS7 | pending_review | Confirmed by domain expert |
| Dextrin 50% | Sodium Chloride | pending_review | Cross-referenced with transactions |
| lactic acid | SIG-39-QZD-93EZ | auto_generated | Verified via product specs |
| vanguard materials | Prime Logistics | unverified | Historical match confirmed |
| soy isolate | Ascorbic Acid 50% | pending_review | Auto-mapped, validated |
| fructose tech grade | SIG-30-ISA-9SS7 | auto_generated | Cross-referenced with transactions |
| SU-OI-TE-705 | Wheat Gluten 98% Premium | pending_review | Cross-referenced with transactions |
| Kaliumsorbat 98% Qualitätsstufe II | casein | unverified | Cross-referenced with transactions |
| calcium carbonate standard | SIG-43-KEL-FPY6 | unverified | Auto-mapped, validated |
| VA-TR-900 LLC | Pinnacle Solutions Corp. | pending_review | Historical match confirmed |
| pea protein | SIG-53-LJE-NZKR | pending_review | Auto-mapped, validated |
| Vat Standard BR 0% | Vat Reduced GB 25% | pending_review | Auto-mapped, validated |
| Dextrose Food Grade | IS-802 | pending_review | Confirmed by domain expert |
| lactic acid tech grade | CO-OI-50-TE-561 | unverified | Cross-referenced with transactions |
| Fructose | SO-CH-70-365 | pending_review | Verified via product specs |
| SIG-51-EJL-Y9QB | stellar logistics | unverified | Historical match confirmed |
| SIG-94-TOI-OFNK | Ascorbic Acid 70% | pending_review | Historical match confirmed |
| SIG-48-YBV-ZD0Y | Premier Solutions Inc. | pending_review | Cross-referenced with transactions |
| Withholding US 5% | EX-G-25-188 | unverified | Confirmed by domain expert |
| Sorbinsäure | CI-AC-98-939 | pending_review | Historical match confirmed |
| soy isolate food grade | Soy Isolate 25% | pending_review | Verified via product specs |
| rapeseed oil 50% premium | PA-OI-ST-879 | auto_generated | Verified via product specs |
| Apex Logistics Inc. | AP-TR-571 Group | auto_generated | Historical match confirmed |
| baltic materials | SIG-24-VMY-QMRL | auto_generated | Confirmed by domain expert |
| SO-IS-275 | Kaliumsorbat Premiumqualität | unverified | Auto-mapped, validated |
| SIG-45-ZZU-GRXH International | Pacific Industries Ltd. | pending_review | Confirmed by domain expert |
| Rapeseed Oil Grade B | Natriumbenzoat Qualitätsstufe I | unverified | Confirmed by domain expert |
| SIG-27-WVB-8FZQ | potassium sorbate | pending_review | Verified via product specs |
| SIG-26-ADB-B4F0 | Sodium Benzoate 50% | pending_review | Historical match confirmed |
| Premier Manufacturing NV | SIG-59-HNQ-A8N5 Ltd. | pending_review | Auto-mapped, validated |
| SIG-74-HUK-JA04 | citric acid food grade | auto_generated | Historical match confirmed |
| RE-ST-FO-GR-727 | SIG-32-RJE-L1OT | pending_review | Verified via product specs |
| Sodium Benzoate Grade B | SIG-51-IYK-630P | auto_generated | Historical match confirmed |
| SIG-40-RSD-JF0U | PR-CH-565 SAS | auto_generated | Cross-referenced with transactions |
| NE-DI-240 Ltd. | Pacific Enterprise International | pending_review | Verified via product specs |
| Apex Logistik | ZE-SU-CO-430 | auto_generated | Auto-mapped, validated |
| rapeseed oil 25% | Kaliumsorbat | pending_review | Verified via product specs |
| Sunflower Oil | Rapsöl 50% Pharmazeutisch rein | auto_generated | Confirmed by domain expert |
| potassium sorbate | SIG-83-PHT-N27M | auto_generated | Confirmed by domain expert |
| SIG-67-MJH-V4Q5 | Horizon Logistics | pending_review | Historical match confirmed |
| Atlas Ingredients Ltd. | GL-LO-196 NV | pending_review | Verified via product specs |
| Sonnenblumenöl Qualitätsstufe I | SIG-18-KSV-TA83 | unverified | Cross-referenced with transactions |
| ST-TR-590 | Apex Verarbeitung | unverified | Verified via product specs |
| Soja Isolate | SIG-88-RKE-8R7A | unverified | Auto-mapped, validated |
| ME-SO-944 Inc. | horizon materials | pending_review | Verified via product specs |
| Nordic Logistik | PR-SO-632 | pending_review | Cross-referenced with transactions |
| Core Supply Co. | VE-SO-701 | pending_review | Confirmed by domain expert |
| SIG-59-HNQ-A8N5 Ltd. | Prime Processing Ltd. | auto_generated | Historical match confirmed |
| SIG-97-PAD-AUZ7 | Horizon Industries | unverified | Verified via product specs |
| SIG-43-FIP-49V7 | vertex materials | pending_review | Historical match confirmed |
| PO-SO-768 | palm oil pharma grade | pending_review | Auto-mapped, validated |
| Dextrin Premium | CA-CA-GR-B-761 | auto_generated | Verified via product specs |
| sorbic acid | SIG-48-GDK-Y8XN | auto_generated | Verified via product specs |
| Lactic Acid Lebensmittelrein | cyclodextrin 70% food grade | pending_review | Historical match confirmed |
| elite solutions Holdings | EL-SO-163 | auto_generated | Cross-referenced with transactions |
| Vat Standard GB 19% | SIG-71-FSV-21LW | auto_generated | Confirmed by domain expert |
| Dextrose 25% Technical | glucose syrup 98% standard | pending_review | Historical match confirmed |
| Weizenklebereiweiß Qualitätsstufe I | citric acid 99.5% | unverified | Cross-referenced with transactions |
| Resistente Stärke | SO-AC-852 | unverified | Verified via product specs |
| Nordic Chemicals BV | prime processing PLC | pending_review | Auto-mapped, validated |
| SIG-47-HDT-7PPC | CO-OI-25-252 | unverified | Historical match confirmed |
| sorbic acid food grade | WH-GL-403 | unverified | Historical match confirmed |
| Casein Technical | rapeseed oil | pending_review | Cross-referenced with transactions |
| SIG-33-VWP-VX5U | central sourcing | pending_review | Historical match confirmed |
| SIG-88-RKE-8R7A | Glukosesirup Syrup Technische Qualität | unverified | Verified via product specs |
| Vertex Commodities | Global Solutions | unverified | Confirmed by domain expert |
| Nordic Logistik | AT-SU-CO-755 | pending_review | Verified via product specs |
| customs duty fr 7% | Excise BR 19% | pending_review | Historical match confirmed |
| Soja Isolate 25% | SO-AC-25-PH-GR-887 | unverified | Confirmed by domain expert |
| Apex Sourcing | central materials | auto_generated | Auto-mapped, validated |
| apex trading | Baltic Ingredients | auto_generated | Historical match confirmed |
| core logistics | SIG-12-DBI-8UY5 | auto_generated | Verified via product specs |
| Coconut Oil 70% Qualitätsstufe I | Sunflower Oil 98% Premium | auto_generated | Verified via product specs |
| Rapeseed Oil 98% Standard | SO-IS-GR-A-940 | pending_review | Historical match confirmed |
| casein 50% premium | SIG-18-NCG-WT1V | pending_review | Verified via product specs |
| PR-TR-294 | Prism Manufacturing PLC | unverified | Confirmed by domain expert |
| Soja Isolate | GL-SY-98-939 | auto_generated | Cross-referenced with transactions |
| citric acid standard | Fructose 70% | unverified | Verified via product specs |
| soy isolate premium | SIG-92-RZH-LRHH | pending_review | Auto-mapped, validated |
| citric acid standard | SIG-39-BAT-DD7R | unverified | Historical match confirmed |
| SIG-67-RMU-WA6Y | VA-RE-C-21-521 | pending_review | Cross-referenced with transactions |
| Resistente Stärke Qualitätsstufe II | PE-PR-25-PH-GR-591 | auto_generated | Verified via product specs |
| SIG-91-FOC-36I6 | Lactic Acid Technische Qualität | pending_review | Cross-referenced with transactions |
| Fructose | SIG-76-YLU-7DL9 | auto_generated | Historical match confirmed |
| Soy Isolate 99.5% Premium | MA-DE-GR-A-871 | auto_generated | Verified via product specs |
| WH-GL-ST-378 | Sonnenblumenöl Qualitätsstufe II | auto_generated | Confirmed by domain expert |
| soy isolate 50% | Palmfett Technische Qualität | auto_generated | Confirmed by domain expert |
| SIG-34-UJK-TJA6 | citric acid 99.5% | pending_review | Auto-mapped, validated |
| IS-PR-125 | SIG-15-PFO-2W85 | auto_generated | Auto-mapped, validated |
| AS-AC-99.5-PR-761 | Palmfett | auto_generated | Confirmed by domain expert |
| coconut oil | Isoglucose | auto_generated | Cross-referenced with transactions |
| Catalyst Ingredients Holdings | stellar commodities Holdings | auto_generated | Cross-referenced with transactions |
| SIG-31-FGA-64VZ | vat standard nl 20% | pending_review | Auto-mapped, validated |
| VE-CH-841 Group | SIG-39-CCW-1KX2 | unverified | Confirmed by domain expert |
| Prime Werkstoffe | nexus logistics | auto_generated | Historical match confirmed |
| Natriumchlorid 25% Premiumqualität | resistant starch 50% | unverified | Verified via product specs |
| nexus sourcing | SIG-36-PCG-IRVO | unverified | Verified via product specs |
| ascorbic acid standard | Coconut Oil Qualitätsstufe I | pending_review | Cross-referenced with transactions |
| Central Manufacturing Holdings | Quantum Ingredients SARL | auto_generated | Verified via product specs |
| IS-FO-GR-555 | casein 25% tech grade | auto_generated | Verified via product specs |
| SIG-66-AQR-B68Q | Natriumbenzoat 25% | auto_generated | Verified via product specs |
| lactic acid standard | Sorbinsäure Standardqualität | pending_review | Cross-referenced with transactions |
| SIG-42-BEO-614U | Soy Isolate 25% | pending_review | Cross-referenced with transactions |
| SIG-20-XSP-FVHF | Sunflower Oil Standard | unverified | Cross-referenced with transactions |
| resistant starch 98% | Wheat Gluten Grade A | auto_generated | Auto-mapped, validated |
| SIG-56-ZQV-YINP SA | Baltic Ingredients SA | unverified | Historical match confirmed |
| Atlas Logistics International | PR-SO-121 Corp. | auto_generated | Cross-referenced with transactions |
| SIG-16-GRX-X3AK | SO-BE-70-PR-120 | auto_generated | Confirmed by domain expert |
| Potassium Sorbate 50% | AS-AC-FO-GR-283 | auto_generated | Verified via product specs |
| Central Logistik | quantum materials | unverified | Confirmed by domain expert |
| Pacific Vertrieb NV | stratos enterprise SARL | unverified | Verified via product specs |
| Excise DE 10% | SIG-44-TSI-A6UF | unverified | Auto-mapped, validated |
| Dextrose Technical | SIG-44-QME-TTIM | auto_generated | Auto-mapped, validated |
| SIG-39-JMB-X1VA | Potassium Sorbate 70% | auto_generated | Historical match confirmed |
| ascorbic acid 99.5% standard | Dextrin Standardqualität | auto_generated | Confirmed by domain expert |
| SIG-94-TUN-H84G | Calcium Carbonate 98% | unverified | Verified via product specs |
| SIG-78-QFN-H3BV | Baltic Enterprise Holdings | pending_review | Verified via product specs |
| ST-DI-183 Inc. | SIG-53-OGW-YU4I Ltd. | auto_generated | Confirmed by domain expert |
| SIG-91-XWQ-EANP | Maltodextrin-Pulver DE20 | pending_review | Verified via product specs |
| Calcium Carbonate Qualitätsstufe II | Sunflower Oil | auto_generated | Verified via product specs |
| SIG-80-QOK-BKBF | Potassium Sorbate 98% | unverified | Cross-referenced with transactions |
| resistant starch standard | Lactic Acid Lebensmittelrein | unverified | Confirmed by domain expert |
| SIG-83-HEH-XF50 | sorbic acid premium | unverified | Historical match confirmed |
| Stellar Manufacturing SA | ME-TR-411 SAS | unverified | Historical match confirmed |
| isoglucose | Traubenzucker Standardqualität | unverified | Confirmed by domain expert |
| Resistant Starch Grade B | Lactic Acid Technische Qualität | pending_review | Verified via product specs |
| Sodium Chloride 25% Premium | resistant starch standard | unverified | Historical match confirmed |
| apex supply | SIG-92-ZAC-Y2PV | pending_review | Confirmed by domain expert |
| Isoglucose | Sorbic Acid 98% | auto_generated | Verified via product specs |
| SU-OI-765 | Fructose Premiumqualität | unverified | Verified via product specs |
| SIG-78-LTE-H4VL | Coconut Oil Grade A | auto_generated | Historical match confirmed |
| global processing | NO-LO-598 Holdings | pending_review | Cross-referenced with transactions |
| Sunflower Oil Grade B | Natriumbenzoat 99.5% | auto_generated | Confirmed by domain expert |
| Vertex Logistik | SIG-77-OCZ-Q3GH | unverified | Confirmed by domain expert |
| Glukosesirup Syrup 70% Lebensmittelrein | Dextrin Pharma Grade | auto_generated | Historical match confirmed |
| VA-RE-N-7-243 | Withholding NL 20% | auto_generated | Cross-referenced with transactions |
| dextrin standard | Fructose Premium | auto_generated | Auto-mapped, validated |
| customs duty nl 15% | Vat Standardqualität CN 19% | unverified | Cross-referenced with transactions |
| SIG-23-NOR-OPI3 | PR-SU-986 Ltd. | auto_generated | Cross-referenced with transactions |
| Natriumchlorid 70% | rapeseed oil 25% | auto_generated | Confirmed by domain expert |
| Zenith Trading | AT-MA-324 International | auto_generated | Historical match confirmed |
| RE-ST-ST-946 | Dextrin Technische Qualität | auto_generated | Auto-mapped, validated |
| SIG-84-VYG-QI55 | Coconut Oil Lebensmittelrein | unverified | Historical match confirmed |
| Ascorbic Acid Standardqualität | CA-580 | pending_review | Cross-referenced with transactions |
| SO-IS-275 | Pea Protein 25% Pharma Grade | pending_review | Verified via product specs |
| sodium benzoate | Calcium Carbonate 50% Qualitätsstufe II | unverified | Cross-referenced with transactions |
| SIG-91-GKA-MSWV | ST-TR-786 International | pending_review | Verified via product specs |
| Resistant Starch Technical | Weizenklebereiweiß 99.5% Technische Qualität | pending_review | Cross-referenced with transactions |
| Resistente Stärke | Dextrin Standard | auto_generated | Cross-referenced with transactions |
| SIG-64-TCV-R5SR | rapeseed oil 70% premium | auto_generated | Verified via product specs |
| Kasein Premiumqualität | SIG-30-UET-0Q2O | auto_generated | Historical match confirmed |
| Calcium Carbonate 99.5% | Kasein | auto_generated | Cross-referenced with transactions |
| EX-I-0-103 | Withholding NL 5% | pending_review | Cross-referenced with transactions |
| Sonnenblumenöl 70% | SIG-63-TFP-OMUW | auto_generated | Auto-mapped, validated |
| SIG-35-HZD-3XBW | SU-OI-GR-B-259 | unverified | Cross-referenced with transactions |
| SIG-41-LTG-3D5I | sodium benzoate 50% | pending_review | Cross-referenced with transactions |
| SIG-97-KNV-Q7J8 | Pacific Logistics | pending_review | Verified via product specs |
| SIG-52-QOU-LC66 | Central Logistics | unverified | Auto-mapped, validated |
| SIG-54-LIP-WKBS | Natriumbenzoat Pharmazeutisch rein | pending_review | Auto-mapped, validated |
| Natriumchlorid 25% Lebensmittelrein | Sodium Chloride | unverified | Confirmed by domain expert |
| Kaliumsorbat Standardqualität | Dextrose Grade A | pending_review | Historical match confirmed |
| SIG-36-FSA-X73Q | Palm Oil 70% | pending_review | Auto-mapped, validated |
| Palm Oil 98% | sunflower oil standard | pending_review | Auto-mapped, validated |
| Zenith Sourcing | SIG-59-ECO-OXB3 | pending_review | Verified via product specs |
| RE-ST-70-901 | Calcium Carbonate 98% | pending_review | Cross-referenced with transactions |
| NE-DI-555 Corp. | Vertex Solutions BV | pending_review | Historical match confirmed |
| continental enterprise International | Prime Rohstoffe PLC | unverified | Confirmed by domain expert |
| ST-CO-650 International | premier supply PLC | pending_review | Cross-referenced with transactions |
| prime logistics | EL-SO-199 | auto_generated | Historical match confirmed |
| Palmfett | SIG-19-BHQ-S1GD | pending_review | Historical match confirmed |
| SIG-85-SQB-MODP BV | Quantum Partners Group | auto_generated | Historical match confirmed |
| Atlas Sourcing | ME-LO-670 | pending_review | Confirmed by domain expert |
| VE-DI-139 KG | SIG-58-GKH-LOY0 Group | pending_review | Auto-mapped, validated |
| Sunflower Oil Grade B | casein 50% premium | unverified | Confirmed by domain expert |
| WH-GL-GR-B-660 | Coconut Oil 98% Food Grade | auto_generated | Auto-mapped, validated |
| Natriumbenzoat 70% Premiumqualität | SIG-22-XCC-QSNV | pending_review | Auto-mapped, validated |
| Fructose 50% Standardqualität | AS-AC-GR-B-855 | pending_review | Auto-mapped, validated |
| SIG-52-JLE-5KJF SAS | Atlantic Supply | auto_generated | Historical match confirmed |
| SIG-12-NAY-4AKW | Soy Isolate | pending_review | Auto-mapped, validated |
| resistant starch 70% food grade | Resistente Stärke Qualitätsstufe II | auto_generated | Verified via product specs |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | SIG-88-AGF-FF5L | auto_generated | Historical match confirmed |
| Potassium Sorbate | DE-25-260 | unverified | Auto-mapped, validated |
| AT-IN-716 Corp. | SIG-78-WKT-9TDY SAS | pending_review | Historical match confirmed |
| BA-LO-814 SAS | vanguard enterprise | pending_review | Verified via product specs |
| Lactic Acid Food Grade | SIG-63-TFP-OMUW | pending_review | Auto-mapped, validated |
| Stratos Logistics | NO-SU-CO-498 | auto_generated | Confirmed by domain expert |
| PA-OI-ST-879 | Lactic Acid 70% | auto_generated | Historical match confirmed |
| SIG-82-DVA-0TXE | CO-OI-ST-153 | pending_review | Historical match confirmed |
| FR-99.5-GR-A-438 | Resistant Starch Grade B | unverified | Cross-referenced with transactions |
| SIG-78-WKT-9TDY SAS | ZE-SU-434 NV | unverified | Confirmed by domain expert |
| AT-IN-716 Corp. | Stratos Versorgung Inc. | pending_review | Confirmed by domain expert |
| Kasein 98% Qualitätsstufe II | Sunflower Oil Grade A | pending_review | Confirmed by domain expert |
| SIG-61-MHS-BQG3 | Ascorbic Acid | pending_review | Auto-mapped, validated |
| premier logistics | Prism Supply Co. | auto_generated | Auto-mapped, validated |
| SIG-30-UET-0Q2O | ascorbic acid food grade | unverified | Cross-referenced with transactions |
| AT-LO-628 | SIG-74-ZJN-KVHO | pending_review | Historical match confirmed |
| SIG-44-LEF-PDJN SARL | core chemicals Group | pending_review | Auto-mapped, validated |
| catalyst sourcing | PR-MA-295 | pending_review | Cross-referenced with transactions |
| Dextrin Pharma Grade | SIG-31-DTE-83EP | auto_generated | Verified via product specs |
| Natriumbenzoat Qualitätsstufe I | WH-GL-98-511 | unverified | Confirmed by domain expert |
| SIG-35-IQA-J92D | Prime Logistik | auto_generated | Verified via product specs |
| Catalyst Logistik | nexus logistics | unverified | Auto-mapped, validated |
| SO-AC-GR-A-997 | maltodextrin de20 | auto_generated | Cross-referenced with transactions |
| nexus sourcing | Catalyst Materials | unverified | Confirmed by domain expert |
| Central Werkstoffe | vertex materials | auto_generated | Verified via product specs |
| SIG-96-DUH-99Q6 | pea protein 99.5% | auto_generated | Auto-mapped, validated |
| vanguard logistics | Quantum Supply Co. | pending_review | Confirmed by domain expert |
| WI-F-15-675 | excise br 21% | unverified | Historical match confirmed |
| AT-LO-568 SA | Baltic Chemicals Group | auto_generated | Confirmed by domain expert |
| vat reduced in 5% | SIG-87-KZL-I3ZY | unverified | Confirmed by domain expert |
| pacific industries | ZE-PR-578 NV | unverified | Verified via product specs |
| lactic acid 70% pharma grade | Traubenzucker 25% Technische Qualität | auto_generated | Verified via product specs |
| DE-25-TE-949 | Fructose Grade B | auto_generated | Confirmed by domain expert |
| Rapsöl 98% | SIG-41-YLB-IZED | auto_generated | Verified via product specs |
| Sodium Benzoate 50% | SIG-88-VVU-EL88 | pending_review | Historical match confirmed |
| Lactic Acid Lebensmittelrein | SIG-41-QPX-D1RL | auto_generated | Auto-mapped, validated |
| elite materials | PR-SO-469 | unverified | Confirmed by domain expert |
| casein 70% tech grade | Calcium Carbonate 50% Food Grade | pending_review | Confirmed by domain expert |
| SIG-79-IWJ-YNSA | vertex logistics KG | unverified | Verified via product specs |
| SIG-80-MXD-T81P | palm oil food grade | pending_review | Cross-referenced with transactions |
| Prism Logistics | SIG-52-QOU-LC66 | unverified | Historical match confirmed |
| Kaliumsorbat Technische Qualität | Potassium Sorbate 70% | unverified | Cross-referenced with transactions |
| Pea Protein 98% Qualitätsstufe II | SIG-56-NOU-ZR98 | auto_generated | Verified via product specs |
| PA-OI-25-GR-A-241 | calcium carbonate 50% pharma grade | auto_generated | Cross-referenced with transactions |
| pea protein | Coconut Oil 98% | pending_review | Auto-mapped, validated |
| Elite Werkstoffe | ME-LO-670 | pending_review | Verified via product specs |
| SIG-51-DNC-4AET | excise in 10% | pending_review | Confirmed by domain expert |
| zenith logistics | Stratos Sourcing | pending_review | Verified via product specs |
| SIG-94-TOI-OFNK | Sodium Chloride Grade A | pending_review | Historical match confirmed |
| Calcium Carbonate | SIG-95-HRL-AO5O | unverified | Cross-referenced with transactions |
| lactic acid tech grade | Maltodextrin-Pulver DE15 | auto_generated | Historical match confirmed |
| SIG-39-DJJ-3SY8 | Calcium Carbonate 50% Grade B | auto_generated | Auto-mapped, validated |
| Wheat Gluten | wheat gluten pharma grade | auto_generated | Historical match confirmed |
| coconut oil 25% standard | SIG-69-INT-Z1YQ | unverified | Historical match confirmed |
| CU-DU-N-25-811 | Vat Reduced CN 5% | auto_generated | Confirmed by domain expert |
| continental commodities | AP-MA-248 International | unverified | Confirmed by domain expert |
| sorbic acid premium | Resistente Stärke Qualitätsstufe I | pending_review | Cross-referenced with transactions |
| Nexus Sourcing | ZE-LO-372 | unverified | Confirmed by domain expert |
| Cyclodextrin Standard | rapeseed oil | auto_generated | Confirmed by domain expert |
| casein standard | Soy Isolate 50% Food Grade | unverified | Cross-referenced with transactions |
| Pacific Werkstoffe | vertex sourcing | auto_generated | Auto-mapped, validated |
| Pacific Vertrieb International | SIG-78-LEG-I3QI Holdings | auto_generated | Auto-mapped, validated |
| Stellar Partners AG | SIG-78-QFN-H3BV | unverified | Cross-referenced with transactions |
| Ascorbic Acid Standardqualität | Casein Grade A | pending_review | Historical match confirmed |
| Isoglucose 70% Food Grade | RA-OI-25-FO-GR-818 | unverified | Historical match confirmed |
| sodium benzoate 25% | Resistente Stärke | unverified | Auto-mapped, validated |
| nordic logistics Group | ZE-PR-578 NV | unverified | Auto-mapped, validated |
| Natriumbenzoat Qualitätsstufe I | SIG-29-ZZE-ZUAD | auto_generated | Verified via product specs |
| Continental Ingredients | SIG-42-HFI-EQFJ Ltd. | pending_review | Verified via product specs |
| CU-DU-D-20-742 | Vat Reduced FR 20% | pending_review | Historical match confirmed |
| SIG-69-OFZ-JW34 | CA-GR-B-950 | pending_review | Historical match confirmed |
| soy isolate 50% premium | Casein Standard | unverified | Auto-mapped, validated |
| Customs Duty BR 21% | Vat Standardqualität NL 25% | unverified | Historical match confirmed |
| Vat Reduced NL 5% | Excise DE 21% | unverified | Historical match confirmed |
| SIG-53-MEZ-6IT1 | Maltodextrin DE10 | unverified | Historical match confirmed |
| SIG-43-OLC-OFCX | dextrose | auto_generated | Cross-referenced with transactions |
| SIG-74-ZNA-1VYW | Customs Duty DE 15% | pending_review | Historical match confirmed |
| QU-MA-886 | Baltic Supply Co. | pending_review | Cross-referenced with transactions |
| Citric Acid Food Grade | PE-PR-98-GR-B-195 | pending_review | Confirmed by domain expert |
| SIG-68-BSO-NW8J Group | Atlantic Chemicals SAS | pending_review | Cross-referenced with transactions |
| PR-IN-608 BV | SIG-41-ZTZ-VNMI Holdings | pending_review | Historical match confirmed |
| SIG-62-KTK-XM5L Holdings | nexus ingredients SA | pending_review | Historical match confirmed |
| SO-BE-113 | Maltodextrin-Pulver DE25 | auto_generated | Cross-referenced with transactions |
| resistant starch standard | Calcium Carbonate 98% Standard | pending_review | Cross-referenced with transactions |
| CU-DU-N-25-811 | SIG-68-WEI-HOKG | auto_generated | Historical match confirmed |
| Pea Protein Premium | Lactic Acid Lebensmittelrein | unverified | Auto-mapped, validated |
| Pea Protein Premiumqualität | Sodium Chloride | auto_generated | Confirmed by domain expert |
| Atlantic Werkstoffe | Central Materials | pending_review | Historical match confirmed |
| Citric Acid | CY-GR-A-208 | unverified | Verified via product specs |
| Core Rohstoffe NV | SIG-79-TAG-A44Y | pending_review | Verified via product specs |
| Natriumbenzoat | SIG-72-JEH-P5K7 | unverified | Auto-mapped, validated |
| SIG-56-NOU-ZR98 | Pea Protein Premiumqualität | unverified | Verified via product specs |
| Excise GB 5% | SIG-65-SMZ-JJEO | pending_review | Confirmed by domain expert |
| coconut oil 25% tech grade | FR-GR-B-311 | pending_review | Confirmed by domain expert |
| Lactic Acid Food Grade | sunflower oil 70% food grade | unverified | Cross-referenced with transactions |
| fructose 99.5% premium | SIG-26-PJJ-DUD8 | auto_generated | Confirmed by domain expert |
| Soy Isolate 50% Grade B | potassium sorbate food grade | unverified | Confirmed by domain expert |
| SIG-80-ZKZ-ANXJ | customs duty fr 7% | pending_review | Confirmed by domain expert |
| Dextrin Technische Qualität | coconut oil 98% tech grade | unverified | Verified via product specs |
| RE-ST-ST-946 | isoglucose food grade | pending_review | Historical match confirmed |
| SIG-92-SMV-JF74 | Withholding FR 15% | auto_generated | Cross-referenced with transactions |
| coconut oil food grade | Zitronensäure Standardqualität | auto_generated | Auto-mapped, validated |
| IS-GR-B-640 | SIG-71-VGV-8K52 | pending_review | Cross-referenced with transactions |
| DE-70-512 | Weizenklebereiweiß 98% | pending_review | Historical match confirmed |
| Soja Isolate Lebensmittelrein | SIG-68-CNV-EOUU | pending_review | Cross-referenced with transactions |
| vat standard br 0% | Withholding IN 20% | auto_generated | Auto-mapped, validated |
| Vertex Logistics | SIG-62-DCP-L2AF | pending_review | Cross-referenced with transactions |
| Rapeseed Oil Pharma Grade | Lactic Acid | unverified | Historical match confirmed |
| Weizenklebereiweiß | Resistant Starch 50% | unverified | Confirmed by domain expert |
| Pinnacle Materials | VE-SU-CO-378 | pending_review | Confirmed by domain expert |
| PA-OI-70-780 | citric acid 99.5% pharma grade | unverified | Confirmed by domain expert |
| FR-ST-953 | ascorbic acid tech grade | unverified | Auto-mapped, validated |
| CU-DU-D-20-742 | Excise US 7% | pending_review | Confirmed by domain expert |
| ST-PA-980 | Nordic Manufacturing Group | unverified | Historical match confirmed |
| SIG-41-YLB-IZED | pea protein 99.5% | pending_review | Confirmed by domain expert |
| SIG-88-RGQ-WZOI | apex manufacturing KG | auto_generated | Verified via product specs |
| AT-IN-931 | Global Processing KG | pending_review | Confirmed by domain expert |
| Catalyst Materials | SIG-73-KSW-UVZU | unverified | Verified via product specs |
| SIG-64-LXA-3LJO | Dextrose Grade A | auto_generated | Cross-referenced with transactions |
| Vertex Versorgung GmbH | SIG-75-GGJ-DK9O | unverified | Cross-referenced with transactions |
| Pea Protein Premiumqualität | Wheat Gluten 99.5% | pending_review | Historical match confirmed |
| SIG-87-QRK-668S | Ascorbic Acid 99.5% | auto_generated | Historical match confirmed |
| SIG-30-JDQ-UNB9 Holdings | QU-PR-732 SA | auto_generated | Confirmed by domain expert |
| PA-OI-GR-B-224 | sodium benzoate premium | pending_review | Confirmed by domain expert |
| DE-GR-B-942 | SIG-83-HEH-XF50 | auto_generated | Verified via product specs |
| PO-SO-202 | soy isolate | auto_generated | Confirmed by domain expert |
| vertex ingredients KG | Stratos Handel Group | pending_review | Cross-referenced with transactions |
| Dextrose | RE-ST-50-232 | unverified | Cross-referenced with transactions |
| SO-AC-25-GR-B-198 | Sorbinsäure | auto_generated | Auto-mapped, validated |
| Vat Standardqualität IN 10% | Withholding GB 15% | pending_review | Cross-referenced with transactions |
| SIG-97-XJT-7TBU | Sodium Chloride Technical | pending_review | Historical match confirmed |
| meridian chemicals Holdings | SIG-49-LWO-P3PY | auto_generated | Verified via product specs |
| SIG-47-TCL-S6FG | Baltic Supply Co. | pending_review | Confirmed by domain expert |
| SIG-86-JBA-HCDI | apex chemicals Inc. | pending_review | Cross-referenced with transactions |
| baltic supply | Global Versorgung GmbH | unverified | Historical match confirmed |
| Core Rohstoffe NV | PR-IN-695 Holdings | unverified | Historical match confirmed |
| PE-PR-746 | SIG-60-WYC-NAXS | auto_generated | Cross-referenced with transactions |
| SIG-24-YWL-8DWF | PA-MA-102 | unverified | Auto-mapped, validated |
| Sorbinsäure | SIG-82-JMP-PVGN | unverified | Auto-mapped, validated |
| Soy Isolate 50% Grade B | LA-AC-GR-A-949 | auto_generated | Cross-referenced with transactions |
| VA-IN-954 PLC | Catalyst Distribution | unverified | Cross-referenced with transactions |
| Cyclodextrin Standard | CI-AC-538 | auto_generated | Verified via product specs |
| glucose syrup | Coconut Oil 50% | unverified | Historical match confirmed |
| excise cn 19% | Withholding NL 7% | unverified | Verified via product specs |
| LA-AC-393 | SIG-24-VEK-YPIS | auto_generated | Historical match confirmed |
| Calcium Carbonate 98% | lactic acid 98% | pending_review | Auto-mapped, validated |
| PO-SO-202 | Weizenklebereiweiß Lebensmittelrein | unverified | Confirmed by domain expert |
| Nordic Logistics | Central Logistik | auto_generated | Auto-mapped, validated |
| Glucose Syrup Technical | resistant starch tech grade | pending_review | Historical match confirmed |
| SO-IS-FO-GR-437 | Soy Isolate | pending_review | Auto-mapped, validated |
| citric acid | Palm Oil 99.5% | pending_review | Confirmed by domain expert |
| SIG-59-EWO-HAXW | CO-LO-520 | auto_generated | Auto-mapped, validated |
| sunflower oil 50% pharma grade | Potassium Sorbate | unverified | Confirmed by domain expert |
| SIG-31-IKO-T2D8 | PO-SO-ST-111 | unverified | Cross-referenced with transactions |
| Sunflower Oil Grade A | GL-SY-TE-601 | auto_generated | Cross-referenced with transactions |
| Glukosesirup Syrup Lebensmittelrein | SO-CH-185 | pending_review | Auto-mapped, validated |
| Pacific Materials KG | SIG-51-HOK-PC9S Holdings | pending_review | Confirmed by domain expert |
| Meridian Materials | apex sourcing | pending_review | Verified via product specs |
| Sonnenblumenöl 70% Lebensmittelrein | SIG-15-QIT-5CZE | unverified | Confirmed by domain expert |
| SIG-51-KQC-QY9M | cyclodextrin standard | unverified | Verified via product specs |
| SIG-61-IQH-EKWH | Rapsöl 99.5% | auto_generated | Verified via product specs |
| Calcium Carbonate 98% Standard | CA-TE-562 | pending_review | Verified via product specs |
| Weizenklebereiweiß 99.5% | ascorbic acid premium | auto_generated | Historical match confirmed |
| sorbic acid 98% | PA-OI-383 | auto_generated | Cross-referenced with transactions |
| Prism Materials Ltd. | SIG-93-ABB-76KE | unverified | Verified via product specs |
| pea protein 98% standard | SIG-66-EQU-IW6V | unverified | Verified via product specs |
| palm oil | SU-OI-TE-705 | pending_review | Confirmed by domain expert |
| vat standard nl 5% | Withholding CN 0% | unverified | Auto-mapped, validated |
| Withholding NL 21% | CU-DU-D-0-383 | auto_generated | Auto-mapped, validated |
| AT-IN-716 Corp. | Atlantic Commodities | auto_generated | Auto-mapped, validated |
| LA-AC-25-PR-377 | Sunflower Oil 50% Grade A | unverified | Historical match confirmed |
| soy isolate pharma grade | Sunflower Oil Pharma Grade | unverified | Historical match confirmed |
| SIG-14-MDA-Y0XA | citric acid premium | auto_generated | Historical match confirmed |
| potassium sorbate | Lactic Acid | pending_review | Auto-mapped, validated |
| FR-99.5-PH-GR-378 | SIG-95-EES-2FE9 | unverified | Confirmed by domain expert |
| PR-MA-686 | Vertex Materials | unverified | Verified via product specs |
| CA-CO-939 | Stratos Partners SAS | pending_review | Confirmed by domain expert |
| NE-PR-315 Holdings | Nexus Verarbeitung Group | auto_generated | Historical match confirmed |
| Quantum Processing Ltd. | Vertex Vertrieb NV | auto_generated | Auto-mapped, validated |
| withholding nl 20% | Vat Reduced IN 5% | auto_generated | Historical match confirmed |
| Catalyst Supply Holdings | Central Logistik NV | unverified | Historical match confirmed |
| BA-MA-943 | Central Versorgung GmbH | auto_generated | Confirmed by domain expert |
| Rapeseed Oil Technical | resistant starch food grade | auto_generated | Auto-mapped, validated |
| SU-OI-98-462 | Calcium Carbonate 50% Qualitätsstufe II | pending_review | Cross-referenced with transactions |
| potassium sorbate food grade | AS-AC-782 | unverified | Confirmed by domain expert |
| meridian supply | AP-SU-CO-755 | pending_review | Confirmed by domain expert |
| citric acid 99.5% pharma grade | Fructose 70% | pending_review | Cross-referenced with transactions |
| SIG-78-OGT-WEKQ | Cyclodextrin | unverified | Cross-referenced with transactions |
| Natriumbenzoat | casein 98% premium | auto_generated | Historical match confirmed |
| Sodium Benzoate 50% Technical | Traubenzucker | auto_generated | Confirmed by domain expert |
| central logistics International | Core Manufacturing | unverified | Auto-mapped, validated |
| Casein 98% Grade B | SIG-60-BLZ-R91Q | pending_review | Verified via product specs |
| SIG-79-HZP-CLBR | CY-763 | unverified | Confirmed by domain expert |
| SIG-62-GUN-FTYL | IS-25-FO-GR-789 | auto_generated | Auto-mapped, validated |
| customs duty fr 25% | Customs Duty FR 7% | auto_generated | Confirmed by domain expert |
| Vat Reduced CN 5% | vat standard de 21% | unverified | Cross-referenced with transactions |
| Vanguard Vertrieb | SIG-86-XWS-MOPG Corp. | pending_review | Verified via product specs |
| Vertex Chemicals Holdings | SIG-98-OXJ-W0H6 SAS | unverified | Historical match confirmed |
| Isoglucose 25% Standard | Dextrin | unverified | Confirmed by domain expert |
| SIG-73-GRJ-1VRU | EX-D-10-430 | unverified | Auto-mapped, validated |
| Calcium Carbonate | SIG-22-SKR-CTIC | auto_generated | Cross-referenced with transactions |
| CA-MA-370 | SIG-20-AKD-OM7O | auto_generated | Historical match confirmed |
| Traubenzucker Qualitätsstufe I | wheat gluten premium | unverified | Cross-referenced with transactions |
| Prime Supply Co. | Nexus Logistik | unverified | Confirmed by domain expert |
| Lactic Acid | casein standard | pending_review | Auto-mapped, validated |
| Sorbic Acid Grade B | rapeseed oil 25% food grade | unverified | Verified via product specs |
| nexus materials | VE-MA-908 | auto_generated | Historical match confirmed |
| PA-OI-25-GR-A-241 | SIG-97-WMO-6B83 | pending_review | Confirmed by domain expert |
| dextrose | Resistente Stärke Qualitätsstufe I | unverified | Verified via product specs |
| SIG-87-YFT-P51V | sorbic acid 98% | pending_review | Confirmed by domain expert |
| sodium benzoate 99.5% premium | CI-AC-70-FO-GR-198 | pending_review | Historical match confirmed |
| Withholding BR 10% | SIG-98-NDY-OCEW | auto_generated | Confirmed by domain expert |
| Natriumbenzoat Qualitätsstufe I | IS-50-TE-886 | auto_generated | Auto-mapped, validated |
| Vertex Versorgung GmbH | VE-LO-603 | unverified | Cross-referenced with transactions |
| SIG-27-NTH-I37Y | SO-IS-98-430 | pending_review | Cross-referenced with transactions |
| Traubenzucker 25% Technische Qualität | SIG-16-FQO-8S1S | auto_generated | Historical match confirmed |
| CU-DU-U-15-275 | withholding nl 20% | pending_review | Confirmed by domain expert |
| rapeseed oil | Lactic Acid 98% Qualitätsstufe I | pending_review | Cross-referenced with transactions |
| SIG-10-BLC-3L38 | resistant starch 70% food grade | auto_generated | Confirmed by domain expert |
| Atlas Trading SA | PI-IN-970 Corp. | pending_review | Verified via product specs |
| Prism Ingredients | Nordic Chemicals | unverified | Verified via product specs |
| SIG-51-HLJ-TN1E | Palm Oil 98% | unverified | Verified via product specs |
| SIG-74-AEB-PMX7 | Sodium Chloride 70% | auto_generated | Confirmed by domain expert |
| SIG-60-WYC-NAXS | citric acid standard | unverified | Confirmed by domain expert |
| withholding nl 19% | Vat Reduced NL 25% | pending_review | Cross-referenced with transactions |
| WI-N-15-362 | SIG-42-QOC-A3JP | pending_review | Cross-referenced with transactions |
| IS-50-FO-GR-562 | Weizenklebereiweiß 70% | pending_review | Auto-mapped, validated |
| glucose syrup 98% food grade | Fructose | auto_generated | Historical match confirmed |
| SIG-86-QTB-N3VO International | Premier Partners | unverified | Confirmed by domain expert |
| stratos logistics | Pinnacle Werkstoffe | pending_review | Confirmed by domain expert |
| cyclodextrin premium | SIG-30-RXC-HFDI | unverified | Historical match confirmed |
| Ascorbic Acid Qualitätsstufe II | SIG-53-LJE-NZKR | pending_review | Auto-mapped, validated |
| CY-TE-117 | Sodium Benzoate Pharma Grade | unverified | Cross-referenced with transactions |
| SIG-20-BPG-W8VL | SO-IS-PR-309 | pending_review | Confirmed by domain expert |
| customs duty de 20% | VA-ST-G-19-154 | pending_review | Confirmed by domain expert |
| Natriumbenzoat | CA-PR-568 | pending_review | Historical match confirmed |
| WH-GL-99.5-557 | SIG-26-ADB-B4F0 | pending_review | Auto-mapped, validated |
| vat reduced cn 21% | Vat Standardqualität US 20% | auto_generated | Auto-mapped, validated |
| SIG-26-EJV-LZ44 | Atlantic Commodities | auto_generated | Verified via product specs |
| SIG-25-VPE-TOC1 | Calcium Carbonate 98% | unverified | Cross-referenced with transactions |
| palm oil 98% | Traubenzucker 25% | auto_generated | Confirmed by domain expert |
| DE-70-769 | Maltodextrin DE18 Pharma Grade | auto_generated | Historical match confirmed |
| AT-MA-363 | Global Versorgung GmbH | pending_review | Cross-referenced with transactions |
| SIG-47-LBV-Y27V | pea protein | pending_review | Auto-mapped, validated |
| SIG-30-MCM-OXZ5 | withholding br 15% | auto_generated | Verified via product specs |
| SIG-36-BVE-5U7D | lactic acid 70% | auto_generated | Historical match confirmed |
| SIG-45-ZTJ-PA16 | Resistente Stärke | unverified | Verified via product specs |
| Atlantic Versorgung LLC | nordic logistics Group | unverified | Cross-referenced with transactions |
| Dextrin | PA-OI-50-PR-573 | unverified | Historical match confirmed |
| Elite Sourcing | Catalyst Materials | pending_review | Cross-referenced with transactions |
| Atlantic Ingredients Holdings | PI-CH-997 SAS | unverified | Confirmed by domain expert |
| pea protein 70% premium | FR-50-ST-938 | pending_review | Auto-mapped, validated |
| SO-CH-185 | SIG-68-VDM-0UT1 | unverified | Verified via product specs |
| Soja Isolate 50% Qualitätsstufe II | sorbic acid 70% | pending_review | Verified via product specs |
| Calcium Carbonate Standardqualität | CA-TE-336 | auto_generated | Historical match confirmed |
| SO-IS-98-880 | SIG-29-CYR-T4UF | auto_generated | Verified via product specs |
| Calcium Carbonate 70% Premium | Sonnenblumenöl 70% Lebensmittelrein | unverified | Confirmed by domain expert |
| Traubenzucker 50% Qualitätsstufe II | SO-BE-667 | pending_review | Cross-referenced with transactions |
| rapeseed oil 99.5% | SIG-94-DKR-CJTR | auto_generated | Cross-referenced with transactions |
| Apex Verarbeitung | Atlantic Logistics SAS | unverified | Cross-referenced with transactions |
| Dextrose 25% Technical | SIG-56-NOU-ZR98 | auto_generated | Cross-referenced with transactions |
| FR-113 | SIG-82-OMQ-EPBO | pending_review | Verified via product specs |
| VA-LO-248 | SIG-55-KQD-CQMQ | pending_review | Cross-referenced with transactions |
| Vat Reduced BR 15% | SIG-68-WEI-HOKG | unverified | Confirmed by domain expert |
| central manufacturing NV | Zenith Industrien LLC | pending_review | Auto-mapped, validated |
| horizon partners Ltd. | AT-LO-826 AG | pending_review | Verified via product specs |
| CE-MA-931 | Core Logistik Holdings | pending_review | Verified via product specs |
| Maltodextrin DE20 | PE-PR-99.5-863 | pending_review | Historical match confirmed |
| Pinnacle Materials SA | CA-IN-566 International | unverified | Auto-mapped, validated |
| lactic acid | SIG-47-SRN-QNYY | unverified | Verified via product specs |
| Catalyst Commodities SAS | Global Solutions | auto_generated | Cross-referenced with transactions |
| Kaliumsorbat | SO-AC-PH-GR-274 | auto_generated | Verified via product specs |
| Nordic Versorgung GmbH | stratos sourcing | auto_generated | Historical match confirmed |
| prime chemicals KG | SIG-93-ABB-76KE | pending_review | Verified via product specs |
| VE-LO-864 | premier logistics | auto_generated | Auto-mapped, validated |
| Coconut Oil 70% | SO-CH-257 | pending_review | Verified via product specs |
| Ascorbic Acid Standardqualität | Sodium Benzoate | auto_generated | Verified via product specs |
| SIG-13-CGO-2Y4L | Traubenzucker 25% | auto_generated | Auto-mapped, validated |
| Coconut Oil 98% Grade A | dextrose | auto_generated | Auto-mapped, validated |
| Lactic Acid | Soja Isolate 99.5% | pending_review | Verified via product specs |
| Wheat Gluten 25% Standard | Calcium Carbonate Premiumqualität | auto_generated | Historical match confirmed |
| LA-AC-25-PR-377 | Ascorbic Acid 99.5% Technische Qualität | unverified | Confirmed by domain expert |
| Casein Grade B | Rapsöl 99.5% | auto_generated | Verified via product specs |
| vertex logistics Holdings | SIG-97-BXB-U2Y7 Ltd. | auto_generated | Verified via product specs |
| VE-SO-576 | Global Versorgung GmbH | pending_review | Cross-referenced with transactions |
| SU-OI-TE-879 | Traubenzucker Standardqualität | pending_review | Historical match confirmed |
| Glukosesirup Syrup | dextrose food grade | pending_review | Cross-referenced with transactions |
| Baltic Commodities Inc. | AT-CH-341 SA | unverified | Confirmed by domain expert |
| SIG-21-UJY-RKOF | WI-B-20-331 | unverified | Historical match confirmed |
| SIG-12-IYC-8W63 Holdings | apex materials Group | pending_review | Auto-mapped, validated |
| Prism Logistik | Atlas Supply Co. | unverified | Auto-mapped, validated |
| Quantum Partners | apex logistics LLC | unverified | Confirmed by domain expert |
| Baltic Industrien PLC | premier industries Holdings | unverified | Verified via product specs |
| Premier Partners SARL | ST-MA-621 International | auto_generated | Verified via product specs |
| AP-SU-CO-755 | global materials | unverified | Cross-referenced with transactions |
| SIG-38-ZZL-D5F0 | vat standard de 25% | pending_review | Verified via product specs |
| Zenith Supply Co. | Apex Versorgung GmbH | unverified | Historical match confirmed |
| Meridian Sourcing | Baltic Materials | unverified | Verified via product specs |
| sodium benzoate | Palmfett 98% Qualitätsstufe I | pending_review | Historical match confirmed |
| SO-BE-708 | SIG-83-XMM-APXP | pending_review | Confirmed by domain expert |
| Sonnenblumenöl 50% Qualitätsstufe I | SIG-41-HMT-W0GK | auto_generated | Confirmed by domain expert |
| atlas materials | Quantum Supply Co. | unverified | Cross-referenced with transactions |
| fructose standard | SIG-62-LDL-CC5R | auto_generated | Historical match confirmed |
| Rapsöl Qualitätsstufe I | SO-CH-881 | pending_review | Verified via product specs |
| SIG-51-EJL-Y9QB | prime supply | auto_generated | Historical match confirmed |
| SIG-76-GDP-2JN8 | Citric Acid 50% | pending_review | Cross-referenced with transactions |
| Potassium Sorbate Standard | Sorbinsäure 50% Standardqualität | pending_review | Historical match confirmed |
| Vat Reduced US 19% | VA-ST-D-25-900 | pending_review | Cross-referenced with transactions |
| Stellar Versorgung GmbH | Pacific Supply Co. | pending_review | Historical match confirmed |
| vat standard cn 19% | Customs Duty IN 25% | unverified | Confirmed by domain expert |
| Rapeseed Oil 70% Technical | CO-OI-98-GR-A-763 | auto_generated | Auto-mapped, validated |
| SIG-36-WFS-RS21 | Sonnenblumenöl Pharmazeutisch rein | auto_generated | Verified via product specs |
| SIG-99-CEZ-35MR | Zenith Manufacturing | pending_review | Confirmed by domain expert |
| ascorbic acid food grade | Rapeseed Oil Technical | auto_generated | Confirmed by domain expert |
| CE-LO-195 | Prime Chemicals KG | pending_review | Cross-referenced with transactions |
| Pea Protein | SIG-53-TLC-AZKT | pending_review | Confirmed by domain expert |
| Palm Oil 70% Pharma Grade | SIG-72-LCQ-PU6W | pending_review | Verified via product specs |
| CU-DU-F-15-864 | Customs Duty IN 25% | auto_generated | Verified via product specs |
| Sunflower Oil Grade B | resistant starch tech grade | auto_generated | Verified via product specs |
| SIG-32-ETO-4DT1 | nexus sourcing | unverified | Cross-referenced with transactions |
| BA-SO-682 International | central logistics Group | auto_generated | Verified via product specs |
| coconut oil standard | SIG-71-WDX-2GRR | auto_generated | Confirmed by domain expert |
| SIG-40-RSD-JF0U | Prime Handel Group | pending_review | Verified via product specs |
| Withholding NL 20% | Vat Reduced US 21% | unverified | Cross-referenced with transactions |
| Premier Solutions LLC | Stellar Handel | unverified | Verified via product specs |
| SIG-47-LPF-7QXJ | citric acid standard | auto_generated | Auto-mapped, validated |
| nordic ingredients SARL | Pinnacle Industrien SAS | pending_review | Confirmed by domain expert |
| SIG-69-MNI-DH5B | CU-DU-G-7-855 | pending_review | Verified via product specs |
| ascorbic acid | RE-ST-676 | unverified | Cross-referenced with transactions |
| Potassium Sorbate 50% Grade B | WH-GL-99.5-GR-A-933 | unverified | Verified via product specs |
| Elite Sourcing | nexus sourcing | pending_review | Verified via product specs |
| Dextrin 70% | SIG-85-CVG-OC50 | unverified | Auto-mapped, validated |
| Dextrose Grade B | SO-CH-TE-286 | pending_review | Verified via product specs |
| SIG-95-APX-PWFS | Lactic Acid | unverified | Confirmed by domain expert |
| calcium carbonate pharma grade | Kaliumsorbat | pending_review | Confirmed by domain expert |
| SIG-86-JBA-HCDI | Premier Industrien Group | unverified | Historical match confirmed |
| Zenith Manufacturing Holdings | Pacific Chemicals AG | auto_generated | Auto-mapped, validated |
| Sorbic Acid 70% | soy isolate premium | auto_generated | Historical match confirmed |
| ascorbic acid | SIG-20-UMV-LJM6 | unverified | Historical match confirmed |
| Sodium Benzoate 99.5% Technical | Natriumchlorid 99.5% | pending_review | Auto-mapped, validated |
| Customs Duty GB 7% | Excise BR 10% | unverified | Historical match confirmed |
| Lactic Acid Standard | SIG-80-EUW-QTKC | unverified | Confirmed by domain expert |
| WI-F-5-977 | SIG-30-HHL-9B4G | auto_generated | Verified via product specs |
| Customs Duty IN 5% | VA-ST-I-20-301 | auto_generated | Auto-mapped, validated |
| Maltodextrin DE10 | SIG-58-LWY-Q8P6 | pending_review | Cross-referenced with transactions |
| Vat Reduced IN 20% | SIG-43-KPC-8R3Y | pending_review | Confirmed by domain expert |
| Pea Protein 99.5% Premiumqualität | SO-CH-70-GR-B-821 | unverified | Verified via product specs |
| Sodium Chloride Premium | Kaliumsorbat 98% Qualitätsstufe II | pending_review | Historical match confirmed |
| horizon partners Ltd. | SIG-40-KNF-W24X PLC | unverified | Cross-referenced with transactions |
| SIG-37-ZOD-1VME | Soy Isolate Standard | auto_generated | Historical match confirmed |
| Rapeseed Oil Technical | Natriumbenzoat 25% | unverified | Cross-referenced with transactions |
| SIG-70-YLY-65JU PLC | Premier Rohstoffe Holdings | unverified | Auto-mapped, validated |
| QU-LO-363 | SIG-90-AUH-5HQ5 | auto_generated | Verified via product specs |
| Citric Acid | sorbic acid premium | auto_generated | Confirmed by domain expert |
| sodium benzoate 50% | SO-IS-25-TE-320 | auto_generated | Historical match confirmed |
| ascorbic acid premium | Sorbinsäure 50% Lebensmittelrein | unverified | Verified via product specs |
| SIG-10-HXN-BKWJ | Prism Supply Co. | auto_generated | Auto-mapped, validated |
| PA-MA-435 | Stellar Materials | pending_review | Verified via product specs |
| Cyclodextrin 98% Pharmazeutisch rein | rapeseed oil | pending_review | Auto-mapped, validated |
| Traubenzucker 99.5% Qualitätsstufe II | Lactic Acid 70% Pharma Grade | unverified | Verified via product specs |
| Casein 98% Technical | SIG-80-WEB-2C7R | pending_review | Cross-referenced with transactions |
| cyclodextrin | Dextrose | unverified | Cross-referenced with transactions |
| Nexus Enterprise BV | prism materials International | pending_review | Verified via product specs |
| Rapeseed Oil | palm oil food grade | auto_generated | Cross-referenced with transactions |
| SIG-80-JPG-N6YV SA | EL-CH-879 | pending_review | Cross-referenced with transactions |
| ST-MA-148 SAS | core partners NV | pending_review | Confirmed by domain expert |
| Glukosesirup Syrup | SIG-16-MLJ-HWA7 | unverified | Historical match confirmed |
| SIG-62-DCP-L2AF | Catalyst Werkstoffe | pending_review | Historical match confirmed |
| coconut oil standard | Cyclodextrin | pending_review | Cross-referenced with transactions |
| rapeseed oil 98% | SO-BE-25-GR-B-233 | pending_review | Historical match confirmed |
| Vat Standard US 15% | excise fr 21% | unverified | Historical match confirmed |
| BA-SO-139 | Global Sourcing | pending_review | Confirmed by domain expert |
| Prime Ingredients NV | pacific industries International | auto_generated | Cross-referenced with transactions |
| Fructose | Lactic Acid 99.5% Qualitätsstufe II | unverified | Historical match confirmed |
| Sodium Benzoate Pharma Grade | coconut oil standard | auto_generated | Cross-referenced with transactions |
| pinnacle industries KG | Apex Solutions International | auto_generated | Auto-mapped, validated |
| Resistant Starch Premium | DE-GR-B-942 | pending_review | Cross-referenced with transactions |
| Calcium Carbonate 70% | SIG-90-SJW-O06V | pending_review | Auto-mapped, validated |
| SIG-42-AYY-K71K | Sorbinsäure | pending_review | Cross-referenced with transactions |
| dextrose 25% tech grade | LA-AC-GR-A-949 | auto_generated | Auto-mapped, validated |
| Potassium Sorbate | Ascorbic Acid | unverified | Historical match confirmed |
| Excise FR 10% | SIG-24-KLH-SHKW | pending_review | Auto-mapped, validated |
| SIG-62-LDL-CC5R | sorbic acid 25% pharma grade | auto_generated | Verified via product specs |
| Vat Standardqualität CN 19% | Vat Reduced FR 10% | auto_generated | Verified via product specs |
| SIG-17-LVE-03G9 | Glukosesirup Syrup | unverified | Historical match confirmed |
| SIG-42-MEI-2SCI | SU-OI-FO-GR-778 | pending_review | Cross-referenced with transactions |
| Customs Duty FR 19% | CU-DU-U-0-415 | auto_generated | Historical match confirmed |
| VA-ST-D-7-855 | Vat Standardqualität BR 0% | pending_review | Auto-mapped, validated |
| isoglucose | Coconut Oil Food Grade | unverified | Confirmed by domain expert |
| SIG-68-TVY-N4XJ | Sodium Benzoate 99.5% Technical | pending_review | Historical match confirmed |
| cyclodextrin | SIG-44-FWT-OA3N | auto_generated | Confirmed by domain expert |
| core partners BV | Prism Industrien LLC | auto_generated | Auto-mapped, validated |
| SIG-85-FAV-D2EE | Traubenzucker Lebensmittelrein | pending_review | Verified via product specs |
| rapeseed oil | Casein Technical | unverified | Confirmed by domain expert |
| DE-25-TE-949 | Lactic Acid 99.5% | unverified | Auto-mapped, validated |
| Coconut Oil 70% Grade A | SIG-51-LVQ-VS8Q | pending_review | Verified via product specs |
| CI-AC-215 | sodium benzoate 50% | auto_generated | Verified via product specs |
| soy isolate 99.5% standard | SIG-34-GNA-EHC2 | pending_review | Historical match confirmed |
| SIG-11-SLQ-KF5B | fructose pharma grade | unverified | Verified via product specs |
| SIG-59-HZI-WDX6 Group | Continental Werkstoffe NV | pending_review | Auto-mapped, validated |
| Natriumchlorid | PA-OI-TE-134 | pending_review | Confirmed by domain expert |
| Vertex Sourcing | Vanguard Versorgung GmbH | auto_generated | Confirmed by domain expert |
| SIG-98-NIJ-5N8C | RE-ST-70-901 | auto_generated | Historical match confirmed |
| RA-OI-GR-A-272 | Potassium Sorbate 50% Technical | pending_review | Cross-referenced with transactions |
| Dextrin Qualitätsstufe II | Lactic Acid 98% Premium | pending_review | Verified via product specs |
| resistant starch 98% pharma grade | SIG-89-TVE-WANI | unverified | Historical match confirmed |
| Vertex Sourcing | SIG-70-ROA-COR7 | unverified | Verified via product specs |
| central materials | Vertex Materials | auto_generated | Auto-mapped, validated |
| Pinnacle Processing | premier solutions Corp. | unverified | Cross-referenced with transactions |
| Horizon Handel KG | AP-PR-849 PLC | unverified | Cross-referenced with transactions |
| ME-TR-366 International | apex manufacturing KG | pending_review | Confirmed by domain expert |
| premier distribution Group | PR-IN-149 Holdings | unverified | Verified via product specs |
| SIG-40-PLP-7A3U | palm oil standard | pending_review | Confirmed by domain expert |
| NO-LO-302 | Horizon Logistics | unverified | Historical match confirmed |
| SIG-51-RJJ-5BIE | Vat Standard US 7% | pending_review | Confirmed by domain expert |
| Customs Duty FR 19% | SIG-74-SAC-3HZG | unverified | Historical match confirmed |
| VE-EN-393 Group | Central Partners Corp. | unverified | Confirmed by domain expert |
| Natriumbenzoat 25% Qualitätsstufe II | PA-OI-25-GR-A-241 | auto_generated | Cross-referenced with transactions |
| SIG-80-WEB-2C7R | MA-DE-569 | pending_review | Verified via product specs |
| Baltic Supply Co. | SIG-96-HGE-2AKA | pending_review | Cross-referenced with transactions |
| Kasein 25% Technische Qualität | RE-ST-676 | auto_generated | Cross-referenced with transactions |
| CU-DU-F-5-228 | Vat Reduced DE 20% | pending_review | Auto-mapped, validated |
| Vat Reduced FR 0% | VA-ST-F-20-240 | auto_generated | Auto-mapped, validated |
| Fructose | Coconut Oil | unverified | Historical match confirmed |
| Global Processing SAS | catalyst supply Holdings | unverified | Auto-mapped, validated |
| continental processing SA | ST-SO-965 | pending_review | Auto-mapped, validated |
| Resistant Starch 50% | SIG-84-HBF-DDQL | unverified | Confirmed by domain expert |
| PI-IN-388 | Nexus Commodities International | pending_review | Verified via product specs |
| AS-AC-70-347 | Sunflower Oil Grade B | unverified | Auto-mapped, validated |
| Pea Protein Qualitätsstufe I | SIG-18-SSS-CTEL | pending_review | Confirmed by domain expert |
| apex sourcing | SIG-46-SZM-WPIS | pending_review | Cross-referenced with transactions |
| SIG-64-LXA-3LJO | Ascorbic Acid | unverified | Cross-referenced with transactions |
| Apex Enterprise Holdings | HO-MA-349 | unverified | Cross-referenced with transactions |
| Meridian Chemicals AG | SIG-36-FMG-DSYM Group | auto_generated | Cross-referenced with transactions |
| Pacific Materials | HO-IN-413 | pending_review | Cross-referenced with transactions |
| AT-IN-956 PLC | Prism Manufacturing NV | pending_review | Confirmed by domain expert |
| Sodium Chloride 99.5% Grade A | wheat gluten 70% | pending_review | Auto-mapped, validated |
| Central Versorgung GmbH | nexus materials | unverified | Historical match confirmed |
| Maltodextrin-Pulver DE25 | Dextrin Technical | auto_generated | Verified via product specs |
| Pea Protein | IS-FO-GR-335 | pending_review | Verified via product specs |
| GL-SY-70-549 | Sodium Benzoate 50% | unverified | Cross-referenced with transactions |
| Ascorbic Acid Standardqualität | ascorbic acid standard | unverified | Confirmed by domain expert |
| Stellar Partners | SIG-17-GFH-X0JO PLC | unverified | Auto-mapped, validated |
| Lactic Acid 98% | Dextrose Standard | unverified | Auto-mapped, validated |
| PR-EN-764 Ltd. | Central Logistics | unverified | Confirmed by domain expert |
| VE-LO-777 | Prime Handel Group | unverified | Confirmed by domain expert |
| SIG-90-BVN-BJY6 | Atlantic Werkstoffe | unverified | Auto-mapped, validated |
| QU-LO-333 | baltic supply | auto_generated | Auto-mapped, validated |
| SIG-79-RTU-R8IQ | soy isolate premium | pending_review | Verified via product specs |
| Central Materials SARL | Atlas Ingredients Ltd. | unverified | Auto-mapped, validated |
| citric acid standard | Sodium Benzoate 70% | pending_review | Confirmed by domain expert |
| CI-AC-488 | Pea Protein 50% | auto_generated | Verified via product specs |
| SIG-64-LXA-3LJO | Kaliumsorbat | unverified | Cross-referenced with transactions |
| Resistant Starch Technical | IS-GR-B-649 | pending_review | Auto-mapped, validated |
| soy isolate standard | Ascorbic Acid 70% | pending_review | Confirmed by domain expert |
| SIG-42-SPP-A6C6 | atlas solutions | auto_generated | Verified via product specs |
| Ascorbic Acid 98% Qualitätsstufe II | SIG-99-JMF-1NOQ | auto_generated | Verified via product specs |
| lactic acid standard | Palmfett | auto_generated | Cross-referenced with transactions |
| SIG-58-EEN-BKJF | Natriumbenzoat 50% | auto_generated | Auto-mapped, validated |
| Zitronensäure Lebensmittelrein | dextrin standard | auto_generated | Cross-referenced with transactions |
| atlas materials | Core Logistik | unverified | Historical match confirmed |
| Atlas Sourcing | atlas supply | auto_generated | Historical match confirmed |
| SO-IS-975 | SIG-42-IEF-RFC9 | pending_review | Verified via product specs |
| SIG-31-LIW-GW9B International | CO-IN-363 AG | unverified | Historical match confirmed |
| Resistant Starch 70% Food Grade | Ascorbic Acid | unverified | Auto-mapped, validated |
| excise nl 21% | Excise CN 20% | auto_generated | Verified via product specs |
| SIG-78-WDE-NNV9 | sunflower oil 70% | auto_generated | Historical match confirmed |
| Vat Standard FR 20% | VA-RE-F-21-230 | unverified | Auto-mapped, validated |
| maltodextrin de18 | SIG-45-ZHK-QWIG | auto_generated | Verified via product specs |
| vanguard industries Inc. | SIG-86-JSN-H9KJ SA | pending_review | Auto-mapped, validated |
| Potassium Sorbate 50% Technical | SO-BE-TE-847 | unverified | Cross-referenced with transactions |
| Stratos Sourcing | CO-MA-245 | unverified | Cross-referenced with transactions |
| Pea Protein 70% Premium | SIG-40-PLP-7A3U | pending_review | Historical match confirmed |
| Vertex Commodities | SIG-36-FMG-DSYM Group | auto_generated | Auto-mapped, validated |
| quantum sourcing | SIG-82-PJM-2KX0 | unverified | Auto-mapped, validated |
| SIG-94-TOI-OFNK | Ascorbic Acid Food Grade | unverified | Historical match confirmed |
| Casein Grade A | CI-AC-488 | auto_generated | Auto-mapped, validated |
| Palm Oil Food Grade | Coconut Oil Lebensmittelrein | unverified | Cross-referenced with transactions |
| SIG-69-OFZ-JW34 | Resistant Starch | auto_generated | Cross-referenced with transactions |
| SIG-86-QXF-N0RG | Palmfett | auto_generated | Auto-mapped, validated |
| CO-OI-50-147 | SIG-36-ABO-ZBYW | pending_review | Historical match confirmed |
| Vertex Sourcing | catalyst supply | pending_review | Auto-mapped, validated |
| Premier Logistics AG | Elite Handel PLC | unverified | Verified via product specs |
| CO-OI-98-890 | SIG-83-KGL-Q4QE | pending_review | Cross-referenced with transactions |
| SO-AC-PH-GR-620 | sunflower oil 50% premium | auto_generated | Cross-referenced with transactions |
| VA-RE-I-25-366 | Customs Duty GB 5% | auto_generated | Cross-referenced with transactions |
| Zenith Logistik | nexus sourcing | unverified | Historical match confirmed |
| Excise NL 0% | SIG-65-LOJ-4KXS | pending_review | Verified via product specs |
| ME-SO-734 | Atlantic Materials | unverified | Confirmed by domain expert |
| pinnacle trading Inc. | SIG-42-UOJ-4ACC Holdings | unverified | Auto-mapped, validated |
| Withholding NL 15% | WI-U-19-722 | unverified | Historical match confirmed |
| soy isolate 99.5% premium | SO-IS-98-PR-717 | auto_generated | Confirmed by domain expert |
| PE-PR-ST-174 | SIG-23-BLM-EZKX | unverified | Historical match confirmed |
| CU-DU-G-5-599 | Withholding US 0% | auto_generated | Cross-referenced with transactions |
| SIG-60-WYC-NAXS | SO-IS-25-323 | auto_generated | Verified via product specs |
| Vat Reduced GB 25% | vat standard gb 21% | auto_generated | Confirmed by domain expert |
| nexus logistics | PR-MA-161 | auto_generated | Auto-mapped, validated |
| HO-LO-534 PLC | SIG-80-GVE-ZK1G | unverified | Auto-mapped, validated |
| SIG-52-EML-H8JV | MA-DE-PR-303 | unverified | Verified via product specs |
| SIG-91-PEG-USI6 | WH-GL-99.5-GR-A-933 | auto_generated | Verified via product specs |
| Resistente Stärke 70% | soy isolate tech grade | unverified | Confirmed by domain expert |
| Ascorbic Acid Premium | Rapsöl 98% Standardqualität | auto_generated | Auto-mapped, validated |
| GL-SY-609 | SIG-16-LZG-DGBK | unverified | Verified via product specs |
| Horizon Sourcing | SIG-23-PGX-VBNK | unverified | Verified via product specs |
| Lactic Acid Lebensmittelrein | wheat gluten standard | pending_review | Auto-mapped, validated |
| Central Solutions | SIG-12-QLD-RUJ3 Inc. | unverified | Verified via product specs |
| Vat Standard NL 19% | SIG-38-OTV-E78M | auto_generated | Cross-referenced with transactions |
| SO-AC-99.5-338 | SIG-18-NCG-WT1V | pending_review | Auto-mapped, validated |
| Traubenzucker 70% | SIG-83-JEP-R0ZJ | auto_generated | Confirmed by domain expert |
| Pea Protein Grade A | PO-SO-50-GR-B-154 | pending_review | Confirmed by domain expert |
| EL-MA-995 | Vertex Handel Holdings | auto_generated | Confirmed by domain expert |
| SO-AC-658 | SIG-12-JLN-YFH3 | pending_review | Verified via product specs |
| ME-MA-989 | continental sourcing | pending_review | Cross-referenced with transactions |
| casein pharma grade | CA-CA-GR-B-761 | unverified | Cross-referenced with transactions |
| Meridian Logistics | SIG-39-CCW-1KX2 | auto_generated | Verified via product specs |
| CI-AC-99.5-674 | Pea Protein Qualitätsstufe I | unverified | Auto-mapped, validated |
| Ascorbic Acid Premiumqualität | AS-AC-PR-308 | auto_generated | Auto-mapped, validated |
| Central Werkstoffe | Elite Sourcing | pending_review | Auto-mapped, validated |
| SIG-29-CYR-T4UF | coconut oil 25% standard | pending_review | Historical match confirmed |
| excise in 20% | Excise CN 25% | auto_generated | Auto-mapped, validated |
| Glucose Syrup 99.5% Food Grade | Weizenklebereiweiß 50% Technische Qualität | pending_review | Verified via product specs |
| Traubenzucker Qualitätsstufe I | SIG-37-MXA-3C7Q | pending_review | Cross-referenced with transactions |
| Calcium Carbonate 98% Standard | FR-50-ST-130 | pending_review | Auto-mapped, validated |
| SIG-58-EEN-BKJF | rapeseed oil 70% premium | auto_generated | Verified via product specs |
| SIG-61-ZIT-092H | Zenith Logistics | auto_generated | Cross-referenced with transactions |
| SO-CH-25-PR-784 | SIG-58-SVK-Z948 | auto_generated | Verified via product specs |
| Weizenklebereiweiß | SIG-40-MRL-94W6 | unverified | Historical match confirmed |
| QU-SO-556 | Stratos Versorgung BV | unverified | Auto-mapped, validated |
| SIG-70-IPH-1O08 | soy isolate | pending_review | Confirmed by domain expert |
| Quantum Versorgung GmbH | SIG-75-GGJ-DK9O | pending_review | Verified via product specs |
| rapeseed oil tech grade | Rapsöl 50% Qualitätsstufe I | pending_review | Auto-mapped, validated |
| SIG-71-VGV-8K52 | Rapsöl Technische Qualität | auto_generated | Auto-mapped, validated |
| CO-LO-919 Holdings | Premier Ingredients Ltd. | pending_review | Confirmed by domain expert |
| SIG-14-WWQ-VPK2 SARL | AT-IN-956 PLC | pending_review | Cross-referenced with transactions |
| PO-SO-560 | citric acid | auto_generated | Historical match confirmed |
| Nexus Sourcing | Nexus Materials | auto_generated | Historical match confirmed |
| SIG-57-YOY-F7N2 | pea protein standard | unverified | Auto-mapped, validated |
| Rapsöl | ascorbic acid 98% premium | auto_generated | Cross-referenced with transactions |
| Glukosesirup Syrup 99.5% Qualitätsstufe II | SIG-32-RJE-L1OT | unverified | Cross-referenced with transactions |
| Citric Acid 25% | coconut oil standard | auto_generated | Historical match confirmed |
| Soja Isolate Premiumqualität | Potassium Sorbate | unverified | Auto-mapped, validated |
| CE-MA-213 | nexus logistics | auto_generated | Historical match confirmed |
| sorbic acid food grade | SIG-30-ISA-9SS7 | pending_review | Confirmed by domain expert |
| CI-AC-25-TE-484 | Resistente Stärke Pharmazeutisch rein | unverified | Auto-mapped, validated |
| SIG-64-VUE-OGQ2 | fructose standard | unverified | Confirmed by domain expert |
| SU-OI-ST-194 | SIG-58-LWY-Q8P6 | unverified | Auto-mapped, validated |
| calcium carbonate standard | Maltodextrin-Pulver DE25 | pending_review | Verified via product specs |
| CU-DU-C-25-616 | customs duty br 5% | unverified | Confirmed by domain expert |
| SIG-55-SMZ-MJ0B | PO-SO-GR-A-715 | unverified | Historical match confirmed |
| SIG-43-SDJ-TRJ6 | Sodium Benzoate 25% Grade B | auto_generated | Cross-referenced with transactions |
| baltic trading | PR-PR-701 Ltd. | unverified | Confirmed by domain expert |
| Palmfett | SIG-70-IKQ-7KBN | auto_generated | Historical match confirmed |
| SIG-23-OPT-7QHV | Soja Isolate Premiumqualität | auto_generated | Historical match confirmed |
| Dextrose 25% Technical | CY-GR-A-428 | unverified | Confirmed by domain expert |
| SO-BE-99.5-TE-953 | glucose syrup 98% | auto_generated | Verified via product specs |
| Sorbinsäure Standardqualität | MA-DE-186 | auto_generated | Verified via product specs |
| Maltodextrin-Pulver DE10 | soy isolate premium | auto_generated | Auto-mapped, validated |
| Ascorbic Acid 25% Grade B | resistant starch food grade | pending_review | Historical match confirmed |
| SIG-44-HTV-P84J | Fructose Pharmazeutisch rein | auto_generated | Historical match confirmed |
| Horizon Sourcing | Atlas Werkstoffe | auto_generated | Verified via product specs |

#### 4.3.3 Excluded Mappings

Provisional mappings pending business validation:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-3964-G | Invalid Entry 198 | Pending validation |
| NOISE-8889-A | Invalid Entry 225 | Duplicate detected |
| NOISE-3144-C | Invalid Entry 385 | Duplicate detected |
| NOISE-1842-G | Invalid Entry 262 | Out of scope per business decision |
| NOISE-1478-B | Invalid Entry 349 | Superseded by newer mapping |
| NOISE-9328-B | Invalid Entry 896 | Pending validation |
| NOISE-6844-E | Invalid Entry 292 | Out of scope per business decision |
| NOISE-1729-C | Invalid Entry 160 | Pending validation |
| NOISE-6042-G | Invalid Entry 834 | Data quality insufficient |
| NOISE-7022-E | Invalid Entry 752 | Pending validation |
| NOISE-3679-D | Invalid Entry 734 | Superseded by newer mapping |
| NOISE-8629-D | Invalid Entry 907 | Superseded by newer mapping |
| NOISE-8867-A | Invalid Entry 872 | Data quality insufficient |
| NOISE-7668-B | Invalid Entry 177 | Duplicate detected |
| NOISE-4419-E | Invalid Entry 450 | Duplicate detected |
| NOISE-3490-H | Invalid Entry 487 | Superseded by newer mapping |
| NOISE-4313-E | Invalid Entry 380 | Superseded by newer mapping |
| NOISE-8900-C | Invalid Entry 688 | Out of scope per business decision |
| NOISE-4248-A | Invalid Entry 431 | Data quality insufficient |
| NOISE-2104-B | Invalid Entry 380 | Pending validation |
| NOISE-8228-C | Invalid Entry 734 | Pending validation |
| NOISE-1135-F | Invalid Entry 390 | Duplicate detected |
| NOISE-5338-F | Invalid Entry 932 | Superseded by newer mapping |
| NOISE-3589-B | Invalid Entry 866 | Data quality insufficient |
| NOISE-8905-H | Invalid Entry 783 | Out of scope per business decision |
| NOISE-7342-C | Invalid Entry 402 | Duplicate detected |
| NOISE-7933-E | Invalid Entry 355 | Out of scope per business decision |
| NOISE-3569-A | Invalid Entry 883 | Out of scope per business decision |
| NOISE-7872-H | Invalid Entry 353 | Out of scope per business decision |
| NOISE-5463-D | Invalid Entry 627 | Pending validation |
| NOISE-5488-C | Invalid Entry 526 | Superseded by newer mapping |
| NOISE-4740-C | Invalid Entry 813 | Pending validation |
| NOISE-2823-G | Invalid Entry 431 | Duplicate detected |
| NOISE-9198-E | Invalid Entry 837 | Out of scope per business decision |
| NOISE-1140-E | Invalid Entry 989 | Superseded by newer mapping |
| NOISE-7712-F | Invalid Entry 438 | Superseded by newer mapping |
| NOISE-4505-F | Invalid Entry 513 | Superseded by newer mapping |
| NOISE-4467-C | Invalid Entry 880 | Superseded by newer mapping |
| NOISE-1474-H | Invalid Entry 251 | Data quality insufficient |
| NOISE-7482-B | Invalid Entry 188 | Pending validation |
| NOISE-7875-C | Invalid Entry 785 | Out of scope per business decision |
| NOISE-8422-B | Invalid Entry 318 | Duplicate detected |
| NOISE-7272-D | Invalid Entry 609 | Superseded by newer mapping |
| NOISE-9135-D | Invalid Entry 157 | Pending validation |
| NOISE-4188-G | Invalid Entry 112 | Superseded by newer mapping |
| NOISE-7439-F | Invalid Entry 337 | Pending validation |
| NOISE-4269-G | Invalid Entry 363 | Superseded by newer mapping |
| NOISE-7492-G | Invalid Entry 595 | Duplicate detected |
| NOISE-3542-D | Invalid Entry 463 | Duplicate detected |
| NOISE-9720-F | Invalid Entry 979 | Data quality insufficient |
| NOISE-1772-A | Invalid Entry 230 | Superseded by newer mapping |
| NOISE-1826-A | Invalid Entry 816 | Data quality insufficient |
| NOISE-1381-C | Invalid Entry 131 | Duplicate detected |
| NOISE-5144-E | Invalid Entry 524 | Duplicate detected |
| NOISE-8269-C | Invalid Entry 779 | Pending validation |
| NOISE-7986-A | Invalid Entry 231 | Pending validation |
| NOISE-3075-G | Invalid Entry 479 | Pending validation |
| NOISE-8517-D | Invalid Entry 409 | Superseded by newer mapping |
| NOISE-9460-E | Invalid Entry 772 | Duplicate detected |
| NOISE-4013-F | Invalid Entry 203 | Out of scope per business decision |
| NOISE-4650-D | Invalid Entry 730 | Superseded by newer mapping |
| NOISE-4066-D | Invalid Entry 911 | Pending validation |
| NOISE-2568-G | Invalid Entry 149 | Out of scope per business decision |
| NOISE-2005-H | Invalid Entry 139 | Superseded by newer mapping |
| NOISE-6593-D | Invalid Entry 476 | Data quality insufficient |
| NOISE-4632-D | Invalid Entry 300 | Out of scope per business decision |
| NOISE-4844-G | Invalid Entry 995 | Superseded by newer mapping |
| NOISE-2900-C | Invalid Entry 914 | Duplicate detected |
| NOISE-7867-F | Invalid Entry 472 | Out of scope per business decision |
| NOISE-8562-H | Invalid Entry 707 | Superseded by newer mapping |
| NOISE-7832-H | Invalid Entry 430 | Pending validation |
| NOISE-3792-D | Invalid Entry 608 | Out of scope per business decision |
| NOISE-1760-F | Invalid Entry 987 | Out of scope per business decision |
| NOISE-5032-H | Invalid Entry 350 | Data quality insufficient |
| NOISE-9169-G | Invalid Entry 694 | Duplicate detected |
| NOISE-1386-F | Invalid Entry 354 | Duplicate detected |
| NOISE-9473-D | Invalid Entry 117 | Out of scope per business decision |
| NOISE-1665-F | Invalid Entry 668 | Data quality insufficient |
| NOISE-6661-H | Invalid Entry 909 | Pending validation |
| NOISE-4025-B | Invalid Entry 311 | Duplicate detected |
| NOISE-5360-G | Invalid Entry 700 | Pending validation |
| NOISE-9537-F | Invalid Entry 839 | Duplicate detected |
| NOISE-6788-E | Invalid Entry 808 | Duplicate detected |
| NOISE-9960-C | Invalid Entry 726 | Pending validation |
| NOISE-3495-E | Invalid Entry 389 | Superseded by newer mapping |
| NOISE-8128-F | Invalid Entry 658 | Duplicate detected |
| NOISE-8209-A | Invalid Entry 365 | Duplicate detected |
| NOISE-5169-G | Invalid Entry 262 | Duplicate detected |
| NOISE-7716-H | Invalid Entry 158 | Duplicate detected |
| NOISE-2579-E | Invalid Entry 828 | Out of scope per business decision |
| NOISE-5027-B | Invalid Entry 691 | Superseded by newer mapping |
| NOISE-3106-E | Invalid Entry 998 | Duplicate detected |
| NOISE-2462-D | Invalid Entry 735 | Pending validation |
| NOISE-4301-F | Invalid Entry 203 | Data quality insufficient |
| NOISE-8910-C | Invalid Entry 171 | Pending validation |
| NOISE-4317-B | Invalid Entry 470 | Data quality insufficient |
| NOISE-2098-B | Invalid Entry 592 | Pending validation |
| NOISE-2069-C | Invalid Entry 168 | Data quality insufficient |
| NOISE-4016-D | Invalid Entry 504 | Data quality insufficient |
| NOISE-7603-A | Invalid Entry 916 | Duplicate detected |
| NOISE-4199-A | Invalid Entry 786 | Out of scope per business decision |
| NOISE-5433-H | Invalid Entry 925 | Out of scope per business decision |
| NOISE-4688-H | Invalid Entry 313 | Out of scope per business decision |
| NOISE-9373-C | Invalid Entry 774 | Data quality insufficient |
| NOISE-3843-C | Invalid Entry 415 | Duplicate detected |
| NOISE-9829-D | Invalid Entry 302 | Out of scope per business decision |
| NOISE-8149-D | Invalid Entry 667 | Superseded by newer mapping |
| NOISE-3507-D | Invalid Entry 824 | Superseded by newer mapping |
| NOISE-2453-A | Invalid Entry 931 | Superseded by newer mapping |
| NOISE-3750-G | Invalid Entry 394 | Pending validation |
| NOISE-7553-H | Invalid Entry 190 | Data quality insufficient |
| NOISE-6065-H | Invalid Entry 713 | Superseded by newer mapping |
| NOISE-6240-F | Invalid Entry 451 | Superseded by newer mapping |
| NOISE-1663-A | Invalid Entry 125 | Superseded by newer mapping |
| NOISE-8603-E | Invalid Entry 536 | Superseded by newer mapping |
| NOISE-3131-B | Invalid Entry 797 | Out of scope per business decision |
| NOISE-4478-E | Invalid Entry 959 | Superseded by newer mapping |
| NOISE-5720-F | Invalid Entry 837 | Pending validation |
| NOISE-4080-D | Invalid Entry 978 | Out of scope per business decision |
| NOISE-4411-H | Invalid Entry 480 | Out of scope per business decision |
| NOISE-3580-G | Invalid Entry 783 | Duplicate detected |
| NOISE-7275-B | Invalid Entry 935 | Duplicate detected |
| NOISE-1115-A | Invalid Entry 304 | Data quality insufficient |
| NOISE-8913-B | Invalid Entry 139 | Duplicate detected |
| NOISE-1331-D | Invalid Entry 179 | Data quality insufficient |
| NOISE-4256-D | Invalid Entry 693 | Superseded by newer mapping |
| NOISE-8362-B | Invalid Entry 263 | Duplicate detected |
| NOISE-8087-G | Invalid Entry 395 | Superseded by newer mapping |
| NOISE-3367-D | Invalid Entry 462 | Superseded by newer mapping |
| NOISE-5187-B | Invalid Entry 242 | Pending validation |
| NOISE-2338-D | Invalid Entry 716 | Data quality insufficient |
| NOISE-8509-C | Invalid Entry 761 | Superseded by newer mapping |
| NOISE-8148-B | Invalid Entry 264 | Duplicate detected |
| NOISE-3397-H | Invalid Entry 904 | Pending validation |
| NOISE-7677-H | Invalid Entry 618 | Data quality insufficient |
| NOISE-9557-G | Invalid Entry 613 | Duplicate detected |
| NOISE-5415-C | Invalid Entry 536 | Duplicate detected |
| NOISE-2926-F | Invalid Entry 485 | Out of scope per business decision |
| NOISE-7530-A | Invalid Entry 252 | Superseded by newer mapping |
| NOISE-3950-F | Invalid Entry 975 | Pending validation |
| NOISE-8053-E | Invalid Entry 978 | Data quality insufficient |
| NOISE-8423-G | Invalid Entry 995 | Out of scope per business decision |
| NOISE-1596-A | Invalid Entry 815 | Pending validation |
| NOISE-2932-A | Invalid Entry 206 | Out of scope per business decision |
| NOISE-9790-D | Invalid Entry 114 | Out of scope per business decision |
| NOISE-5942-H | Invalid Entry 102 | Data quality insufficient |
| NOISE-9920-E | Invalid Entry 978 | Pending validation |
| NOISE-4528-D | Invalid Entry 926 | Data quality insufficient |
| NOISE-2386-H | Invalid Entry 213 | Superseded by newer mapping |
| NOISE-8288-A | Invalid Entry 143 | Data quality insufficient |
| NOISE-4391-B | Invalid Entry 693 | Superseded by newer mapping |
| NOISE-7954-F | Invalid Entry 916 | Data quality insufficient |
| NOISE-7786-H | Invalid Entry 682 | Duplicate detected |
| NOISE-8450-F | Invalid Entry 927 | Data quality insufficient |
| NOISE-6116-G | Invalid Entry 727 | Pending validation |
| NOISE-1050-C | Invalid Entry 849 | Out of scope per business decision |
| NOISE-6872-D | Invalid Entry 975 | Out of scope per business decision |
| NOISE-2322-H | Invalid Entry 434 | Duplicate detected |
| NOISE-1056-G | Invalid Entry 305 | Out of scope per business decision |
| NOISE-9846-D | Invalid Entry 242 | Pending validation |
| NOISE-6046-C | Invalid Entry 723 | Out of scope per business decision |
| NOISE-5910-B | Invalid Entry 608 | Pending validation |
| NOISE-7861-B | Invalid Entry 472 | Pending validation |
| NOISE-4024-E | Invalid Entry 898 | Superseded by newer mapping |
| NOISE-5704-D | Invalid Entry 133 | Duplicate detected |
| NOISE-1396-H | Invalid Entry 683 | Duplicate detected |
| NOISE-5533-G | Invalid Entry 717 | Pending validation |
| NOISE-2817-A | Invalid Entry 495 | Out of scope per business decision |
| NOISE-7119-B | Invalid Entry 669 | Duplicate detected |
| NOISE-8214-C | Invalid Entry 348 | Duplicate detected |
| NOISE-9937-H | Invalid Entry 754 | Pending validation |
| NOISE-7912-E | Invalid Entry 504 | Pending validation |
| NOISE-4372-H | Invalid Entry 465 | Pending validation |
| NOISE-5196-G | Invalid Entry 965 | Data quality insufficient |
| NOISE-5316-C | Invalid Entry 504 | Out of scope per business decision |
| NOISE-1727-G | Invalid Entry 651 | Superseded by newer mapping |
| NOISE-1592-E | Invalid Entry 833 | Data quality insufficient |
| NOISE-4706-G | Invalid Entry 331 | Superseded by newer mapping |
| NOISE-3045-E | Invalid Entry 226 | Out of scope per business decision |
| NOISE-2882-G | Invalid Entry 741 | Pending validation |
| NOISE-7051-G | Invalid Entry 472 | Out of scope per business decision |
| NOISE-8003-C | Invalid Entry 768 | Pending validation |
| NOISE-7849-A | Invalid Entry 358 | Out of scope per business decision |
| NOISE-1961-H | Invalid Entry 340 | Duplicate detected |
| NOISE-6110-B | Invalid Entry 538 | Pending validation |
| NOISE-9645-G | Invalid Entry 461 | Duplicate detected |
| NOISE-8552-D | Invalid Entry 489 | Data quality insufficient |
| NOISE-5057-G | Invalid Entry 386 | Duplicate detected |
| NOISE-7499-G | Invalid Entry 201 | Data quality insufficient |
| NOISE-1122-D | Invalid Entry 381 | Duplicate detected |
| NOISE-8342-F | Invalid Entry 575 | Superseded by newer mapping |
| NOISE-1124-E | Invalid Entry 554 | Out of scope per business decision |
| NOISE-3572-F | Invalid Entry 429 | Pending validation |
| NOISE-4839-F | Invalid Entry 846 | Out of scope per business decision |
| NOISE-1524-D | Invalid Entry 393 | Superseded by newer mapping |
| NOISE-3820-G | Invalid Entry 182 | Duplicate detected |
| NOISE-2800-A | Invalid Entry 153 | Out of scope per business decision |
| NOISE-3806-H | Invalid Entry 634 | Data quality insufficient |
| NOISE-2384-D | Invalid Entry 607 | Duplicate detected |
| NOISE-9702-D | Invalid Entry 331 | Data quality insufficient |
| NOISE-2938-C | Invalid Entry 596 | Pending validation |
| NOISE-9452-G | Invalid Entry 594 | Superseded by newer mapping |
| NOISE-4461-E | Invalid Entry 358 | Duplicate detected |
| NOISE-7199-E | Invalid Entry 919 | Out of scope per business decision |
| NOISE-3793-A | Invalid Entry 523 | Duplicate detected |
| NOISE-3948-E | Invalid Entry 527 | Data quality insufficient |
| NOISE-3105-H | Invalid Entry 294 | Out of scope per business decision |
| NOISE-7309-G | Invalid Entry 963 | Duplicate detected |
| NOISE-5630-E | Invalid Entry 766 | Out of scope per business decision |
| NOISE-2002-A | Invalid Entry 943 | Superseded by newer mapping |
| NOISE-8146-A | Invalid Entry 206 | Out of scope per business decision |
| NOISE-3784-H | Invalid Entry 396 | Superseded by newer mapping |
| NOISE-6213-G | Invalid Entry 920 | Pending validation |
| NOISE-2852-H | Invalid Entry 998 | Pending validation |
| NOISE-5279-A | Invalid Entry 872 | Data quality insufficient |
| NOISE-7556-A | Invalid Entry 762 | Pending validation |
| NOISE-9224-B | Invalid Entry 879 | Out of scope per business decision |
| NOISE-1595-H | Invalid Entry 351 | Out of scope per business decision |
| NOISE-6978-H | Invalid Entry 481 | Pending validation |
| NOISE-7813-H | Invalid Entry 654 | Superseded by newer mapping |
| NOISE-6366-A | Invalid Entry 603 | Data quality insufficient |
| NOISE-9702-F | Invalid Entry 662 | Duplicate detected |
| NOISE-4076-H | Invalid Entry 960 | Duplicate detected |
| NOISE-4277-E | Invalid Entry 280 | Duplicate detected |
| NOISE-8253-D | Invalid Entry 967 | Pending validation |
| NOISE-5465-C | Invalid Entry 935 | Data quality insufficient |
| NOISE-4734-A | Invalid Entry 628 | Out of scope per business decision |
| NOISE-4004-H | Invalid Entry 959 | Pending validation |
| NOISE-5762-C | Invalid Entry 762 | Pending validation |
| NOISE-8321-F | Invalid Entry 608 | Data quality insufficient |
| NOISE-2496-D | Invalid Entry 524 | Data quality insufficient |
| NOISE-4965-F | Invalid Entry 773 | Out of scope per business decision |
| NOISE-9587-F | Invalid Entry 202 | Out of scope per business decision |
| NOISE-1777-H | Invalid Entry 444 | Duplicate detected |
| NOISE-7040-C | Invalid Entry 957 | Out of scope per business decision |
| NOISE-3228-A | Invalid Entry 176 | Pending validation |
| NOISE-3136-C | Invalid Entry 346 | Superseded by newer mapping |
| NOISE-6311-G | Invalid Entry 521 | Out of scope per business decision |
| NOISE-7596-D | Invalid Entry 349 | Superseded by newer mapping |
| NOISE-5296-C | Invalid Entry 521 | Duplicate detected |
| NOISE-8977-D | Invalid Entry 916 | Superseded by newer mapping |
| NOISE-1400-C | Invalid Entry 828 | Superseded by newer mapping |
| NOISE-1849-D | Invalid Entry 420 | Pending validation |
| NOISE-7541-F | Invalid Entry 927 | Out of scope per business decision |
| NOISE-8020-F | Invalid Entry 262 | Data quality insufficient |
| NOISE-7236-B | Invalid Entry 944 | Data quality insufficient |
| NOISE-4215-B | Invalid Entry 865 | Out of scope per business decision |
| NOISE-5470-C | Invalid Entry 732 | Pending validation |
| NOISE-5877-E | Invalid Entry 805 | Data quality insufficient |
| NOISE-5548-A | Invalid Entry 718 | Superseded by newer mapping |
| NOISE-3397-E | Invalid Entry 947 | Out of scope per business decision |
| NOISE-7942-H | Invalid Entry 594 | Out of scope per business decision |
| NOISE-3080-F | Invalid Entry 203 | Superseded by newer mapping |
| NOISE-6589-E | Invalid Entry 501 | Duplicate detected |
| NOISE-2966-A | Invalid Entry 712 | Duplicate detected |
| NOISE-8832-F | Invalid Entry 658 | Data quality insufficient |
| NOISE-7409-F | Invalid Entry 289 | Superseded by newer mapping |
| NOISE-4352-D | Invalid Entry 102 | Superseded by newer mapping |
| NOISE-2458-F | Invalid Entry 167 | Out of scope per business decision |
| NOISE-2157-D | Invalid Entry 621 | Duplicate detected |
| NOISE-7199-C | Invalid Entry 723 | Superseded by newer mapping |
| NOISE-5999-A | Invalid Entry 633 | Duplicate detected |
| NOISE-8839-C | Invalid Entry 871 | Data quality insufficient |
| NOISE-2875-E | Invalid Entry 903 | Data quality insufficient |
| NOISE-9641-B | Invalid Entry 153 | Out of scope per business decision |
| NOISE-2232-B | Invalid Entry 154 | Out of scope per business decision |
| NOISE-9841-B | Invalid Entry 417 | Data quality insufficient |
| NOISE-8840-F | Invalid Entry 315 | Out of scope per business decision |
| NOISE-4918-C | Invalid Entry 453 | Pending validation |
| NOISE-3572-A | Invalid Entry 181 | Superseded by newer mapping |
| NOISE-8608-D | Invalid Entry 592 | Pending validation |
| NOISE-8140-C | Invalid Entry 392 | Pending validation |
| NOISE-8054-E | Invalid Entry 930 | Superseded by newer mapping |
| NOISE-8635-F | Invalid Entry 991 | Superseded by newer mapping |
| NOISE-1878-F | Invalid Entry 763 | Out of scope per business decision |
| NOISE-1938-A | Invalid Entry 106 | Data quality insufficient |
| NOISE-5993-E | Invalid Entry 790 | Superseded by newer mapping |
| NOISE-1343-D | Invalid Entry 641 | Pending validation |
| NOISE-4861-D | Invalid Entry 495 | Pending validation |
| NOISE-6857-F | Invalid Entry 640 | Data quality insufficient |
| NOISE-5162-E | Invalid Entry 359 | Pending validation |
| NOISE-3914-E | Invalid Entry 337 | Data quality insufficient |
| NOISE-9484-A | Invalid Entry 832 | Pending validation |
| NOISE-9972-F | Invalid Entry 901 | Superseded by newer mapping |
| NOISE-2362-A | Invalid Entry 676 | Pending validation |
| NOISE-4952-D | Invalid Entry 338 | Out of scope per business decision |
| NOISE-2394-F | Invalid Entry 283 | Out of scope per business decision |
| NOISE-5496-C | Invalid Entry 373 | Data quality insufficient |
| NOISE-7458-G | Invalid Entry 866 | Superseded by newer mapping |
| NOISE-2237-A | Invalid Entry 304 | Out of scope per business decision |
| NOISE-3957-H | Invalid Entry 467 | Out of scope per business decision |
| NOISE-6308-G | Invalid Entry 101 | Pending validation |
| NOISE-6560-A | Invalid Entry 141 | Out of scope per business decision |
| NOISE-5965-H | Invalid Entry 518 | Data quality insufficient |
| NOISE-5171-E | Invalid Entry 935 | Pending validation |
| NOISE-5821-D | Invalid Entry 346 | Out of scope per business decision |
| NOISE-6932-H | Invalid Entry 573 | Pending validation |
| NOISE-6243-D | Invalid Entry 428 | Duplicate detected |
| NOISE-1746-E | Invalid Entry 944 | Out of scope per business decision |
| NOISE-7310-H | Invalid Entry 586 | Pending validation |
| NOISE-5179-G | Invalid Entry 560 | Duplicate detected |
| NOISE-2201-F | Invalid Entry 508 | Data quality insufficient |
| NOISE-9924-H | Invalid Entry 238 | Duplicate detected |
| NOISE-3547-F | Invalid Entry 151 | Data quality insufficient |
| NOISE-9058-C | Invalid Entry 876 | Duplicate detected |
| NOISE-8702-A | Invalid Entry 348 | Pending validation |
| NOISE-7431-E | Invalid Entry 377 | Pending validation |
| NOISE-1846-E | Invalid Entry 955 | Data quality insufficient |
| NOISE-3616-A | Invalid Entry 451 | Pending validation |
| NOISE-4356-H | Invalid Entry 140 | Duplicate detected |
| NOISE-1343-E | Invalid Entry 335 | Superseded by newer mapping |
| NOISE-3582-H | Invalid Entry 639 | Duplicate detected |
| NOISE-5895-F | Invalid Entry 721 | Data quality insufficient |

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
