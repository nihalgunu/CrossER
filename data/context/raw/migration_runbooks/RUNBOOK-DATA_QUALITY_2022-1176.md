# Migration Runbook: System Migration: DATA_QUALITY_2022

**Document ID**: RB-DATA_QUALITY_2022-5191
**Version**: 2.3
**Last Updated**: 2023-06-07
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the System Migration: DATA_QUALITY_2022 project.
The migration involves transitioning master data and transactional records from SOURCE
to TARGET while maintaining data integrity and business continuity.

**Project Timeline**: 2023-03-04 to 2023-08-05
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
| Total entities assessed | 1590 | Completed |
| Successfully mapped | 1077 | Verified |
| Excluded from scope | 323 | Documented |
| Manual review required | 9 | In Progress |

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
| PR-SU-935 Ltd. | pacific distribution | unverified | Cross-referenced with transactions |
| Kaliumsorbat | sodium benzoate standard | pending_review | Cross-referenced with transactions |
| Ascorbic Acid 50% Standardqualität | Wheat Gluten 98% | unverified | Auto-mapped, validated |
| Stellar Partners | quantum processing International | auto_generated | Cross-referenced with transactions |
| Stratos Chemicals | premier enterprise Holdings | auto_generated | Auto-mapped, validated |
| Global Solutions Group | SIG-14-WWQ-VPK2 SARL | auto_generated | Historical match confirmed |
| pinnacle ingredients GmbH | CO-PR-215 Group | unverified | Auto-mapped, validated |
| Atlantic Rohstoffe International | SIG-12-QLD-RUJ3 Inc. | pending_review | Historical match confirmed |
| SIG-35-RSV-01YT | VA-ST-D-19-529 | auto_generated | Verified via product specs |
| Vanguard Logistik | CO-PR-215 Group | auto_generated | Verified via product specs |
| Atlas Logistics | SIG-33-IHK-2GVW | pending_review | Verified via product specs |
| Premier Rohstoffe Holdings | SIG-59-HZI-WDX6 Group | pending_review | Cross-referenced with transactions |
| Vat Standard CN 10% | EX-N-21-216 | pending_review | Auto-mapped, validated |
| customs duty fr 19% | Withholding NL 21% | pending_review | Verified via product specs |
| ST-MA-670 Group | Central Materials SARL | auto_generated | Historical match confirmed |
| SIG-37-NAI-M1G9 | sunflower oil premium | pending_review | Confirmed by domain expert |
| SIG-22-ADK-3T78 | Excise DE 21% | pending_review | Auto-mapped, validated |
| SIG-70-HGQ-WORL | BA-SO-633 | auto_generated | Cross-referenced with transactions |
| AS-AC-GR-B-395 | Calcium Carbonate 98% | unverified | Auto-mapped, validated |
| vertex enterprise Group | Meridian Trading | unverified | Auto-mapped, validated |
| Baltic Enterprise KG | SIG-39-SXC-H14U | auto_generated | Historical match confirmed |
| sodium benzoate 99.5% tech grade | Cyclodextrin Standard | auto_generated | Confirmed by domain expert |
| DE-GR-A-472 | SIG-27-RTX-YEAW | unverified | Verified via product specs |
| PR-PA-643 | baltic enterprise International | pending_review | Historical match confirmed |
| Sorbinsäure 50% Standardqualität | Dextrose 25% | auto_generated | Confirmed by domain expert |
| SIG-89-RGS-FIRM Holdings | Catalyst Industries | auto_generated | Historical match confirmed |
| SIG-98-DBG-MTO5 | Atlas Logistics | pending_review | Verified via product specs |
| RE-ST-GR-B-805 | Calcium Carbonate 25% Pharma Grade | auto_generated | Verified via product specs |
| SIG-26-WVS-AQ3B | Vat Reduced FR 0% | pending_review | Verified via product specs |
| vat reduced cn 19% | SIG-62-JTP-RUMX | auto_generated | Cross-referenced with transactions |
| SIG-55-KQD-CQMQ | Atlantic Materials | auto_generated | Verified via product specs |
| Zitronensäure 70% | Palm Oil 50% | pending_review | Confirmed by domain expert |
| PR-SO-388 | Nexus Sourcing | auto_generated | Cross-referenced with transactions |
| CU-DU-N-5-217 | Excise DE 10% | unverified | Historical match confirmed |
| CA-GR-A-380 | rapeseed oil food grade | auto_generated | Verified via product specs |
| Traubenzucker Standardqualität | LA-AC-ST-823 | auto_generated | Historical match confirmed |
| Pea Protein Grade A | FR-130 | auto_generated | Historical match confirmed |
| SIG-75-DRM-1CLN | AS-AC-70-347 | pending_review | Confirmed by domain expert |
| NO-DI-582 AG | Continental Werkstoffe NV | unverified | Auto-mapped, validated |
| Zitronensäure Qualitätsstufe I | LA-AC-25-PR-377 | pending_review | Verified via product specs |
| ST-LO-136 | Premier Logistik | unverified | Historical match confirmed |
| SIG-81-FXX-6VPL | Sodium Benzoate 50% Technical | unverified | Cross-referenced with transactions |
| Sorbinsäure 98% | CO-OI-98-890 | auto_generated | Confirmed by domain expert |
| palm oil 99.5% | SIG-63-KMB-9J7M | unverified | Cross-referenced with transactions |
| Vat Reduced BR 25% | Customs Duty US 15% | auto_generated | Auto-mapped, validated |
| SIG-35-HUP-NW3M | Vertex Materials | unverified | Historical match confirmed |
| PO-SO-PR-101 | Sorbic Acid | unverified | Historical match confirmed |
| Rapsöl 99.5% Technische Qualität | Sunflower Oil 50% Grade A | auto_generated | Verified via product specs |
| global materials | SIG-45-ZQV-Q4GS | unverified | Cross-referenced with transactions |
| Nexus Commodities International | SIG-56-JML-GDXB | auto_generated | Historical match confirmed |
| Excise GB 25% | Customs Duty CN 10% | auto_generated | Verified via product specs |
| Natriumchlorid 70% | SIG-51-IYK-630P | pending_review | Historical match confirmed |
| PR-MA-669 Ltd. | Nordic Materials Holdings | pending_review | Cross-referenced with transactions |
| calcium carbonate 99.5% | CA-CA-50-GR-A-195 | auto_generated | Verified via product specs |
| MA-DE-933 | SIG-50-XSG-WQVA | auto_generated | Historical match confirmed |
| Stellar Versorgung GmbH | AT-LO-914 | pending_review | Cross-referenced with transactions |
| SIG-27-FHX-VO6Y | citric acid | auto_generated | Cross-referenced with transactions |
| Baltic Sourcing | Baltic Logistics | auto_generated | Verified via product specs |
| Potassium Sorbate 70% | sunflower oil premium | pending_review | Cross-referenced with transactions |
| Coconut Oil 98% | SO-BE-50-924 | pending_review | Auto-mapped, validated |
| SO-CH-70-GR-B-821 | Natriumbenzoat Pharmazeutisch rein | auto_generated | Cross-referenced with transactions |
| Elite Materials | PI-SU-CO-734 | auto_generated | Historical match confirmed |
| vat standard nl 5% | VA-RE-B-7-231 | unverified | Verified via product specs |
| Central Logistik Holdings | Vertex Enterprise Holdings | pending_review | Auto-mapped, validated |
| Ascorbic Acid | dextrose standard | pending_review | Historical match confirmed |
| SIG-91-XWQ-EANP | sodium chloride 99.5% premium | pending_review | Cross-referenced with transactions |
| Excise IN 19% | excise fr 0% | pending_review | Verified via product specs |
| sorbic acid | Kasein | unverified | Cross-referenced with transactions |
| Vat Standardqualität IN 0% | Vat Standard NL 19% | pending_review | Cross-referenced with transactions |
| Zitronensäure Qualitätsstufe I | IS-GR-B-640 | unverified | Historical match confirmed |
| Excise IN 25% | Excise FR 21% | pending_review | Cross-referenced with transactions |
| Natriumchlorid Technische Qualität | CY-892 | auto_generated | Auto-mapped, validated |
| SIG-30-PPI-DU4D | Vat Standardqualität BR 0% | pending_review | Confirmed by domain expert |
| AP-SU-CO-814 | SIG-75-QOJ-Q4NY | unverified | Historical match confirmed |
| Withholding BR 5% | SIG-50-TGM-XVD2 | unverified | Cross-referenced with transactions |
| apex chemicals Inc. | Premier Manufacturing NV | pending_review | Historical match confirmed |
| meridian materials | Vertex Logistics | unverified | Confirmed by domain expert |
| wheat gluten 70% | GL-SY-99.5-GR-B-358 | auto_generated | Cross-referenced with transactions |
| Dextrin 50% | Maltodextrin DE15 | auto_generated | Verified via product specs |
| SIG-29-RWA-CHL8 | Coconut Oil 98% Grade A | pending_review | Auto-mapped, validated |
| Atlas Logistics | CE-SU-CO-752 | pending_review | Historical match confirmed |
| Isoglucose 98% | RE-ST-575 | unverified | Auto-mapped, validated |
| Vat Reduced IN 20% | SIG-97-QNX-7TWO | auto_generated | Cross-referenced with transactions |
| Baltic Versorgung | NO-CO-357 International | auto_generated | Cross-referenced with transactions |
| nexus sourcing | Quantum Versorgung GmbH | unverified | Historical match confirmed |
| Sorbinsäure | potassium sorbate | unverified | Confirmed by domain expert |
| RA-OI-FO-GR-269 | Dextrin | pending_review | Cross-referenced with transactions |
| Nordic Logistik | SIG-13-SXA-38WM | unverified | Auto-mapped, validated |
| apex processing Ltd. | Atlas Ingredients PLC | unverified | Auto-mapped, validated |
| Vat Reduced BR 19% | EX-U-15-972 | unverified | Auto-mapped, validated |
| Ascorbic Acid 70% | CI-AC-98-939 | pending_review | Historical match confirmed |
| Pea Protein | MA-DE-GR-B-565 | auto_generated | Confirmed by domain expert |
| AS-AC-165 | Traubenzucker Standardqualität | pending_review | Cross-referenced with transactions |
| elite materials | Meridian Werkstoffe | pending_review | Historical match confirmed |
| Ascorbic Acid 50% | sodium chloride premium | unverified | Confirmed by domain expert |
| SIG-99-IZM-CYBY | Traubenzucker Qualitätsstufe II | pending_review | Verified via product specs |
| Dextrin 98% | SIG-80-QNF-AHPO | pending_review | Auto-mapped, validated |
| Apex Trading Holdings | atlantic industries International | auto_generated | Historical match confirmed |
| lactic acid 98% premium | SO-IS-99.5-PR-187 | auto_generated | Verified via product specs |
| SIG-90-NFZ-XRLG | Stratos Sourcing | unverified | Confirmed by domain expert |
| SIG-39-OZI-N968 | Dextrin Grade A | pending_review | Historical match confirmed |
| Fructose Premiumqualität | SIG-61-XKV-ODPX | pending_review | Verified via product specs |
| citric acid standard | SIG-99-OQS-ADHF | auto_generated | Cross-referenced with transactions |
| Soja Isolate Premiumqualität | dextrose 99.5% | pending_review | Cross-referenced with transactions |
| SIG-61-CIV-LFWA | Resistant Starch 70% | pending_review | Cross-referenced with transactions |
| Isoglucose Lebensmittelrein | SIG-78-AVK-U9PX | auto_generated | Auto-mapped, validated |
| Fructose Standardqualität | SIG-57-YNB-5KMT | auto_generated | Cross-referenced with transactions |
| Prime Werkstoffe | SIG-55-DBH-2QS3 | pending_review | Cross-referenced with transactions |
| SIG-58-SVK-Z948 | Zitronensäure 99.5% | pending_review | Historical match confirmed |
| SO-AC-70-785 | SIG-62-GDA-2IVD | auto_generated | Historical match confirmed |
| Stratos Supply SAS | Horizon Vertrieb International | pending_review | Historical match confirmed |
| Atlantic Verarbeitung Group | baltic processing | unverified | Historical match confirmed |
| Atlantic Logistics SAS | Nordic Ingredients SARL | pending_review | Verified via product specs |
| Customs Duty BR 21% | SIG-58-SWU-PQGW | pending_review | Auto-mapped, validated |
| SIG-93-ZCF-6HM3 | Sorbinsäure 70% | unverified | Confirmed by domain expert |
| PR-SU-CO-591 | Premier Logistics | auto_generated | Historical match confirmed |
| Vat Reduced CN 21% | customs duty nl 15% | unverified | Historical match confirmed |
| CO-OI-ST-153 | Pea Protein 70% Pharma Grade | pending_review | Historical match confirmed |
| ST-SO-673 | stellar materials | auto_generated | Auto-mapped, validated |
| Glucose Syrup 70% | Fructose Standardqualität | auto_generated | Auto-mapped, validated |
| Elite Sourcing | SIG-19-GAY-Z6O1 | auto_generated | Historical match confirmed |
| dextrose | SIG-48-IWQ-OJ98 | unverified | Cross-referenced with transactions |
| CE-PA-586 SARL | Core Chemicals | auto_generated | Auto-mapped, validated |
| CA-CA-648 | SIG-19-QLH-ILRZ | pending_review | Cross-referenced with transactions |
| PR-MA-161 | SIG-40-XXD-GE9O | auto_generated | Historical match confirmed |
| pinnacle industries SAS | Atlantic Verarbeitung Group | pending_review | Historical match confirmed |
| PR-SO-469 | Continental Logistik | unverified | Cross-referenced with transactions |
| Isoglucose | CA-98-TE-238 | pending_review | Cross-referenced with transactions |
| SIG-93-ZCF-6HM3 | ascorbic acid food grade | unverified | Auto-mapped, validated |
| SIG-27-FHX-VO6Y | palm oil 70% premium | pending_review | Historical match confirmed |
| SIG-88-XZP-H10B | Ascorbic Acid | unverified | Cross-referenced with transactions |
| Casein 50% Premium | MA-DE-738 | auto_generated | Verified via product specs |
| SIG-43-OLC-OFCX | Lactic Acid | auto_generated | Verified via product specs |
| PA-OI-70-GR-B-781 | dextrose 25% | unverified | Confirmed by domain expert |
| Rapsöl 98% Standardqualität | SIG-12-ANK-TJ9A | pending_review | Historical match confirmed |
| Natriumbenzoat | SIG-92-RZH-LRHH | pending_review | Confirmed by domain expert |
| SIG-52-EML-H8JV | Calcium Carbonate Grade B | auto_generated | Historical match confirmed |
| Nordic Manufacturing Holdings | CE-SU-700 Group | unverified | Auto-mapped, validated |
| PA-OI-TE-134 | SIG-18-SSS-CTEL | unverified | Verified via product specs |
| Global Werkstoffe | SIG-66-UEK-CKJ1 | auto_generated | Historical match confirmed |
| Vertex Chemicals Holdings | stratos ingredients | pending_review | Cross-referenced with transactions |
| IS-FO-GR-555 | pea protein 99.5% | unverified | Auto-mapped, validated |
| PR-PA-269 AG | meridian distribution Group | unverified | Verified via product specs |
| SU-OI-FO-GR-778 | SIG-25-EZW-5GYT | pending_review | Cross-referenced with transactions |
| SIG-92-ZTO-VZGU | Resistant Starch Grade B | pending_review | Auto-mapped, validated |
| Stellar Sourcing | VE-LO-437 | unverified | Verified via product specs |
| fructose 99.5% tech grade | Ascorbic Acid Premiumqualität | unverified | Auto-mapped, validated |
| sorbic acid 25% pharma grade | SIG-13-TIV-U5CX | auto_generated | Verified via product specs |
| CU-DU-G-0-770 | Withholding NL 15% | pending_review | Auto-mapped, validated |
| quantum supply | Horizon Sourcing | pending_review | Historical match confirmed |
| Calcium Carbonate 50% Food Grade | Weizenklebereiweiß Qualitätsstufe I | pending_review | Verified via product specs |
| sorbic acid premium | Potassium Sorbate | auto_generated | Cross-referenced with transactions |
| SIG-92-RZH-LRHH | resistant starch | auto_generated | Historical match confirmed |
| vat standard fr 5% | Withholding DE 20% | auto_generated | Cross-referenced with transactions |
| Sonnenblumenöl 70% Lebensmittelrein | SIG-24-GPL-7S00 | unverified | Cross-referenced with transactions |
| stratos commodities Holdings | Apex Processing | unverified | Confirmed by domain expert |
| Pea Protein | CA-TE-562 | unverified | Auto-mapped, validated |
| Sonnenblumenöl 70% Lebensmittelrein | DE-FO-GR-588 | auto_generated | Auto-mapped, validated |
| SIG-56-JML-GDXB | Continental Rohstoffe GmbH | auto_generated | Verified via product specs |
| Lactic Acid 99.5% Grade B | Natriumbenzoat 99.5% | pending_review | Historical match confirmed |
| Dextrose 25% | Sonnenblumenöl Pharmazeutisch rein | unverified | Cross-referenced with transactions |
| SIG-50-JOR-LO4P | Dextrin | unverified | Cross-referenced with transactions |
| Coconut Oil 70% Qualitätsstufe I | sodium benzoate | auto_generated | Verified via product specs |
| SIG-13-CGO-2Y4L | calcium carbonate standard | pending_review | Confirmed by domain expert |
| baltic supply | Stellar Materials | auto_generated | Historical match confirmed |
| Traubenzucker Lebensmittelrein | RE-ST-223 | auto_generated | Confirmed by domain expert |
| Isoglucose 25% Lebensmittelrein | SIG-74-HUK-JA04 | auto_generated | Verified via product specs |
| Continental Werkstoffe NV | continental commodities | auto_generated | Cross-referenced with transactions |
| SIG-56-BPD-M0A6 | Citric Acid 99.5% | pending_review | Verified via product specs |
| SIG-98-CGL-FHWJ | CA-CA-99.5-FO-GR-839 | pending_review | Cross-referenced with transactions |
| SIG-65-XHR-R1SP | Natriumbenzoat | unverified | Cross-referenced with transactions |
| SIG-70-QGS-CCAF | VA-ST-N-19-883 | unverified | Cross-referenced with transactions |
| Pea Protein 70% Pharma Grade | Ascorbic Acid 70% | auto_generated | Confirmed by domain expert |
| quantum logistics | SIG-92-ZAC-Y2PV | unverified | Cross-referenced with transactions |
| CA-CA-648 | SIG-89-JZC-1682 | auto_generated | Historical match confirmed |
| Premier Versorgung GmbH | SIG-61-ZIT-092H | unverified | Confirmed by domain expert |
| apex logistics LLC | PI-MA-367 SA | auto_generated | Confirmed by domain expert |
| Lactic Acid | Calcium Carbonate 50% Pharmazeutisch rein | pending_review | Cross-referenced with transactions |
| Isoglucose 70% | sodium benzoate 25% | auto_generated | Cross-referenced with transactions |
| Fructose 99.5% Pharma Grade | citric acid pharma grade | unverified | Historical match confirmed |
| Excise US 19% | VA-RE-B-7-231 | pending_review | Historical match confirmed |
| Isoglucose Food Grade | Lactic Acid 50% Premiumqualität | auto_generated | Confirmed by domain expert |
| quantum ingredients Holdings | Central Solutions | auto_generated | Historical match confirmed |
| Zitronensäure 98% | wheat gluten | pending_review | Verified via product specs |
| LA-AC-ST-663 | Sorbic Acid 50% Food Grade | unverified | Historical match confirmed |
| CA-580 | potassium sorbate | pending_review | Historical match confirmed |
| SO-BE-824 | SIG-68-SYL-8192 | unverified | Historical match confirmed |
| Lactic Acid Technical | SIG-79-SPO-WT80 | auto_generated | Verified via product specs |
| CE-MA-338 | Horizon Logistics | pending_review | Cross-referenced with transactions |
| Wheat Gluten 25% Standard | WH-GL-99.5-557 | pending_review | Verified via product specs |
| CO-OI-98-876 | SIG-73-WMX-7XJJ | pending_review | Verified via product specs |
| SO-IS-PH-GR-671 | SIG-21-PIO-0RWR | unverified | Auto-mapped, validated |
| dextrose 50% standard | SIG-34-JQN-ROWX | auto_generated | Cross-referenced with transactions |
| PO-SO-339 | Dextrose | auto_generated | Verified via product specs |
| pea protein 70% premium | Sodium Chloride | unverified | Cross-referenced with transactions |
| Global Chemicals | SIG-83-MZM-HGMN GmbH | pending_review | Confirmed by domain expert |
| SIG-56-ZQV-YINP SA | pinnacle supply | unverified | Confirmed by domain expert |
| SIG-98-HZM-47LK | PR-SO-469 | auto_generated | Verified via product specs |
| SIG-22-XCC-QSNV | potassium sorbate | auto_generated | Cross-referenced with transactions |
| SIG-42-HBL-L3KU International | Stratos Ingredients | pending_review | Cross-referenced with transactions |
| lactic acid standard | IS-614 | auto_generated | Confirmed by domain expert |
| Pea Protein 98% | Sorbic Acid | pending_review | Historical match confirmed |
| VE-IN-631 Ltd. | global trading PLC | unverified | Auto-mapped, validated |
| SIG-94-MKW-LH8F | Vat Reduced BR 7% | auto_generated | Confirmed by domain expert |
| SIG-81-AXG-9CBI AG | PA-DI-201 NV | auto_generated | Historical match confirmed |
| Isoglucose Grade B | casein 70% tech grade | pending_review | Confirmed by domain expert |
| SIG-51-ZAY-11PM | Calcium Carbonate 50% | auto_generated | Verified via product specs |
| Catalyst Manufacturing GmbH | AT-PR-985 International | auto_generated | Verified via product specs |
| maltodextrin de18 | SIG-76-GST-OWGM | pending_review | Historical match confirmed |
| Sonnenblumenöl Standardqualität | Sunflower Oil Grade A | unverified | Cross-referenced with transactions |
| Meridian Solutions KG | pinnacle processing | unverified | Confirmed by domain expert |
| vanguard enterprise | Elite Partners GmbH | auto_generated | Confirmed by domain expert |
| Quantum Werkstoffe | Stratos Materials | unverified | Historical match confirmed |
| Stellar Handel | ZE-IN-456 LLC | unverified | Confirmed by domain expert |
| Customs Duty FR 25% | CU-DU-U-15-275 | auto_generated | Cross-referenced with transactions |
| Natriumchlorid Lebensmittelrein | AS-AC-GR-B-395 | unverified | Confirmed by domain expert |
| SIG-76-AAU-3VM8 | Pea Protein Premium | auto_generated | Verified via product specs |
| Fructose | SIG-24-NPE-GDMB | pending_review | Confirmed by domain expert |
| Nordic Rohstoffe | Prime Materials Inc. | auto_generated | Cross-referenced with transactions |
| Coconut Oil 25% Technische Qualität | CY-TE-117 | unverified | Verified via product specs |
| Traubenzucker Standardqualität | DE-840 | unverified | Historical match confirmed |
| Soja Isolate Premiumqualität | isoglucose 70% | unverified | Historical match confirmed |
| Baltic Processing PLC | SIG-69-BWM-8WBG | pending_review | Cross-referenced with transactions |
| Prism Logistik | Continental Logistics | pending_review | Verified via product specs |
| SIG-97-SMQ-9SG6 | Vat Reduced NL 0% | unverified | Verified via product specs |
| Casein Standard | lactic acid | auto_generated | Confirmed by domain expert |
| Coconut Oil 70% Qualitätsstufe I | Cyclodextrin Food Grade | unverified | Verified via product specs |
| Palm Oil 99.5% | Weizenklebereiweiß Pharmazeutisch rein | unverified | Auto-mapped, validated |
| LA-AC-ST-663 | SIG-24-PBC-613L | unverified | Auto-mapped, validated |
| PI-DI-618 NV | vertex enterprise Holdings | auto_generated | Auto-mapped, validated |
| SIG-50-FUX-7S9T | wheat gluten standard | pending_review | Verified via product specs |
| Atlas Logistik | PI-LO-142 | unverified | Confirmed by domain expert |
| Ascorbic Acid | WH-GL-99.5-GR-A-933 | unverified | Cross-referenced with transactions |
| CA-CA-436 | SIG-13-FYG-4NN9 | pending_review | Auto-mapped, validated |
| Sodium Benzoate | DE-ST-553 | pending_review | Verified via product specs |
| Pea Protein 99.5% | Sorbinsäure | pending_review | Confirmed by domain expert |
| Core Sourcing | Quantum Sourcing | unverified | Verified via product specs |
| Potassium Sorbate | Rapsöl Pharmazeutisch rein | pending_review | Confirmed by domain expert |
| Lactic Acid Food Grade | Zitronensäure 50% Pharmazeutisch rein | auto_generated | Verified via product specs |
| sorbic acid 98% | SIG-46-YHU-BU2J | auto_generated | Historical match confirmed |
| SIG-99-CTB-8OFG Group | Central Trading Group | unverified | Auto-mapped, validated |
| WH-GL-923 | Sodium Chloride 70% | unverified | Verified via product specs |
| Nexus Versorgung GmbH | ST-MA-703 | unverified | Verified via product specs |
| PO-SO-339 | SIG-58-HNG-1XJ7 | pending_review | Cross-referenced with transactions |
| sodium benzoate premium | Ascorbic Acid 50% | pending_review | Historical match confirmed |
| Resistente Stärke Lebensmittelrein | rapeseed oil 70% premium | auto_generated | Auto-mapped, validated |
| SIG-71-FSV-21LW | EX-B-10-648 | pending_review | Verified via product specs |
| Resistente Stärke | coconut oil 98% premium | unverified | Cross-referenced with transactions |
| customs duty us 15% | Vat Standard NL 5% | unverified | Historical match confirmed |
| Stellar Manufacturing Holdings | pinnacle solutions Group | auto_generated | Auto-mapped, validated |
| NE-MA-648 | global materials | auto_generated | Cross-referenced with transactions |
| excise br 21% | WI-B-20-331 | auto_generated | Verified via product specs |
| Sunflower Oil Standard | calcium carbonate | unverified | Historical match confirmed |
| casein standard | Sodium Benzoate Grade A | auto_generated | Confirmed by domain expert |
| SIG-75-GUI-J643 | Calcium Carbonate Lebensmittelrein | unverified | Verified via product specs |
| sunflower oil | Calcium Carbonate 99.5% | unverified | Verified via product specs |
| Ascorbic Acid | Sodium Benzoate 99.5% Technical | auto_generated | Auto-mapped, validated |
| SIG-97-UWA-JWLN | prism sourcing | pending_review | Historical match confirmed |
| NE-PA-358 | Nordic Manufacturing Holdings | auto_generated | Auto-mapped, validated |
| Coconut Oil Grade A | Palmfett | auto_generated | Verified via product specs |
| ST-IN-592 SA | Apex Handel International | unverified | Cross-referenced with transactions |
| SIG-55-DBH-2QS3 | Global Materials | unverified | Verified via product specs |
| sodium benzoate premium | SIG-13-EJJ-5506 | pending_review | Historical match confirmed |
| quantum supply | Prism Sourcing | pending_review | Auto-mapped, validated |
| atlas partners | Pinnacle Enterprise AG | auto_generated | Confirmed by domain expert |
| vat standard de 0% | WI-U-0-465 | unverified | Auto-mapped, validated |
| BA-IN-547 | SIG-92-FQX-S1BC | pending_review | Historical match confirmed |
| DE-70-769 | Glukosesirup Syrup | auto_generated | Verified via product specs |
| AT-SU-CO-864 | SIG-96-EVO-10JM | unverified | Cross-referenced with transactions |
| SIG-79-GKV-W8GA | Maltodextrin-Pulver DE18 | pending_review | Historical match confirmed |
| Dextrose 70% Grade A | Natriumchlorid Technische Qualität | pending_review | Historical match confirmed |
| Dextrin 98% | SO-IS-432 | pending_review | Verified via product specs |
| dextrose standard | Wheat Gluten Grade A | unverified | Auto-mapped, validated |
| prime processing PLC | NE-PR-428 GmbH | pending_review | Verified via product specs |
| Pea Protein | sodium chloride 70% | unverified | Confirmed by domain expert |
| SO-AC-852 | Lactic Acid 99.5% | auto_generated | Verified via product specs |
| SIG-50-DEU-V25U | ME-MA-156 Corp. | pending_review | Historical match confirmed |
| meridian chemicals Holdings | SIG-65-ONA-WQOF Corp. | pending_review | Historical match confirmed |
| stratos partners SA | SIG-85-SQB-MODP BV | unverified | Cross-referenced with transactions |
| SIG-62-DCP-L2AF | Nexus Materials | unverified | Confirmed by domain expert |
| PI-SU-CO-734 | SIG-13-ZRN-WZGO | auto_generated | Confirmed by domain expert |
| Casein Premium | Weizenklebereiweiß Qualitätsstufe I | pending_review | Historical match confirmed |
| PE-PR-70-PR-387 | rapeseed oil 50% premium | unverified | Historical match confirmed |
| SIG-83-CDB-3QOI | quantum materials | pending_review | Verified via product specs |
| MA-DE-146 | Soy Isolate | unverified | Historical match confirmed |
| Stellar Materials | ST-LO-181 | unverified | Auto-mapped, validated |
| SIG-44-MHK-SRCB | SO-CH-99.5-618 | unverified | Cross-referenced with transactions |
| SIG-66-LJV-5E3H | Coconut Oil | pending_review | Cross-referenced with transactions |
| sodium benzoate | SIG-71-COB-BL7A | unverified | Verified via product specs |
| Vat Standardqualität BR 15% | customs duty in 21% | auto_generated | Verified via product specs |
| Zitronensäure 50% Qualitätsstufe I | SIG-12-RDG-0JI1 | unverified | Confirmed by domain expert |
| Stellar Sourcing | Meridian Versorgung GmbH | unverified | Historical match confirmed |
| SIG-18-LLP-8GUU | Natriumbenzoat Qualitätsstufe I | auto_generated | Auto-mapped, validated |
| Natriumbenzoat 99.5% Qualitätsstufe I | Calcium Carbonate | unverified | Historical match confirmed |
| lactic acid tech grade | RE-ST-FO-GR-238 | auto_generated | Confirmed by domain expert |
| Coconut Oil 98% | RE-ST-PR-679 | pending_review | Auto-mapped, validated |
| SIG-53-AHT-MGFX | Glucose Syrup 25% | auto_generated | Auto-mapped, validated |
| SIG-26-WVS-AQ3B | withholding de 15% | pending_review | Cross-referenced with transactions |
| RE-ST-25-TE-177 | Coconut Oil Standard | unverified | Historical match confirmed |
| Sodium Benzoate 50% | Resistente Stärke Lebensmittelrein | auto_generated | Verified via product specs |
| Atlantic Trading BV | vertex logistics PLC | pending_review | Verified via product specs |
| Sodium Benzoate 99.5% | Rapsöl Qualitätsstufe I | auto_generated | Confirmed by domain expert |
| SIG-86-DMG-XSKY | potassium sorbate | auto_generated | Verified via product specs |
| SO-CH-TE-304 | SIG-30-LJO-TN4Y | unverified | Historical match confirmed |
| vertex solutions | SIG-67-LHQ-GQOH BV | unverified | Confirmed by domain expert |
| Lactic Acid Lebensmittelrein | CO-OI-ST-153 | unverified | Verified via product specs |
| SIG-49-QVY-JMMU | CA-PR-568 | pending_review | Auto-mapped, validated |
| Maltodextrin DE10 | SO-CH-257 | unverified | Confirmed by domain expert |
| SIG-84-HFZ-NPNZ | CI-AC-99.5-638 | auto_generated | Confirmed by domain expert |
| SIG-46-YOE-MYAX SA | VA-DI-105 | auto_generated | Auto-mapped, validated |
| Sonnenblumenöl Qualitätsstufe I | PO-SO-560 | auto_generated | Auto-mapped, validated |
| ascorbic acid | CI-AC-PR-827 | pending_review | Confirmed by domain expert |
| SO-IS-FO-GR-334 | Zitronensäure | unverified | Confirmed by domain expert |
| SO-BE-FO-GR-650 | potassium sorbate 25% pharma grade | auto_generated | Historical match confirmed |
| LA-AC-ST-823 | Ascorbic Acid 99.5% | unverified | Verified via product specs |
| SIG-16-GDL-YC2T LLC | nordic logistics Group | pending_review | Historical match confirmed |
| SIG-22-SKR-CTIC | sunflower oil standard | pending_review | Auto-mapped, validated |
| SO-IS-PR-242 | SIG-93-ZCF-6HM3 | auto_generated | Auto-mapped, validated |
| Sorbinsäure | CO-OI-ST-153 | auto_generated | Verified via product specs |
| SIG-69-CZY-YXFK | VE-IN-631 Ltd. | pending_review | Auto-mapped, validated |
| palm oil pharma grade | Traubenzucker 99.5% | pending_review | Confirmed by domain expert |
| Prime Materials Inc. | Vertex Vertrieb NV | unverified | Verified via product specs |
| Sodium Benzoate 99.5% Grade A | SIG-39-FND-AALU | unverified | Confirmed by domain expert |
| Coconut Oil 70% | SIG-71-COB-BL7A | unverified | Auto-mapped, validated |
| SIG-73-OCH-3A8Y | Lactic Acid Grade A | unverified | Confirmed by domain expert |
| SIG-48-BCW-76F8 | Apex Sourcing | unverified | Auto-mapped, validated |
| Maltodextrin DE5 Food Grade | SO-CH-752 | pending_review | Verified via product specs |
| Ascorbic Acid Lebensmittelrein | SIG-91-FOC-36I6 | pending_review | Cross-referenced with transactions |
| Stellar Partners Ltd. | PR-LO-245 Ltd. | auto_generated | Verified via product specs |
| IS-802 | Sodium Chloride Grade B | pending_review | Cross-referenced with transactions |
| ST-TR-590 | Apex Verarbeitung | auto_generated | Historical match confirmed |
| Rapsöl | citric acid pharma grade | auto_generated | Auto-mapped, validated |
| lactic acid standard | Kaliumsorbat | pending_review | Verified via product specs |
| Sorbinsäure | Lactic Acid Grade B | pending_review | Historical match confirmed |
| SIG-68-TVY-N4XJ | Zitronensäure Premiumqualität | unverified | Confirmed by domain expert |
| DE-70-GR-A-741 | sunflower oil standard | auto_generated | Cross-referenced with transactions |
| Dextrin | sunflower oil 70% | unverified | Confirmed by domain expert |
| SO-IS-PR-242 | SIG-44-UIE-SASC | unverified | Verified via product specs |
| SIG-35-FKH-6ZOM KG | Elite Solutions Group | auto_generated | Confirmed by domain expert |
| PA-OI-50-PR-573 | SIG-94-DKR-CJTR | unverified | Auto-mapped, validated |
| fructose standard | Isoglucose Grade B | auto_generated | Historical match confirmed |
| Maltodextrin DE5 Grade A | WH-GL-923 | unverified | Historical match confirmed |
| SO-IS-PR-167 | lactic acid tech grade | pending_review | Confirmed by domain expert |
| Dextrose 50% | rapeseed oil premium | pending_review | Auto-mapped, validated |
| CA-580 | Ascorbic Acid Lebensmittelrein | auto_generated | Confirmed by domain expert |
| sodium chloride 98% | SIG-65-RQH-9Y5B | pending_review | Verified via product specs |
| Isoglucose | coconut oil standard | pending_review | Historical match confirmed |
| Glukosesirup Syrup | fructose 99.5% pharma grade | unverified | Cross-referenced with transactions |
| SIG-80-QOK-BKBF | isoglucose | unverified | Verified via product specs |
| Dextrin 50% | Kasein 98% | pending_review | Verified via product specs |
| Weizenklebereiweiß 99.5% Qualitätsstufe I | Coconut Oil Grade A | pending_review | Auto-mapped, validated |
| Lactic Acid Grade A | resistant starch | auto_generated | Auto-mapped, validated |
| AT-SO-658 | elite logistics | unverified | Auto-mapped, validated |
| Elite Sourcing | SIG-97-UWA-JWLN | unverified | Auto-mapped, validated |
| Resistant Starch | CI-AC-GR-A-280 | auto_generated | Verified via product specs |
| Sodium Chloride 25% Food Grade | SIG-26-ADB-B4F0 | auto_generated | Cross-referenced with transactions |
| SIG-51-LVQ-VS8Q | Lactic Acid Standard | unverified | Confirmed by domain expert |
| Casein | IS-GR-B-640 | auto_generated | Auto-mapped, validated |
| SO-BE-25-774 | Fructose 99.5% Grade A | pending_review | Auto-mapped, validated |
| MA-DE-933 | Lactic Acid Grade A | unverified | Auto-mapped, validated |
| Central Materials SARL | zenith partners Inc. | pending_review | Auto-mapped, validated |
| potassium sorbate | Cyclodextrin 98% | unverified | Historical match confirmed |
| Fructose Qualitätsstufe II | MA-DE-744 | pending_review | Historical match confirmed |
| Sorbic Acid 50% Grade A | Kasein 98% Premiumqualität | auto_generated | Verified via product specs |
| Catalyst Enterprise International | Atlas Partners Corp. | auto_generated | Auto-mapped, validated |
| CO-CO-290 BV | global partners BV | auto_generated | Cross-referenced with transactions |
| SIG-89-PTG-ZQNK | Sorbinsäure Qualitätsstufe I | auto_generated | Historical match confirmed |
| SIG-87-QRK-668S | Resistant Starch Food Grade | auto_generated | Confirmed by domain expert |
| maltodextrin de20 | SIG-68-KHP-8RTJ | unverified | Confirmed by domain expert |
| EL-SO-163 | nexus partners SARL | auto_generated | Cross-referenced with transactions |
| Calcium Carbonate 98% | PA-OI-50-497 | pending_review | Historical match confirmed |
| Weizenklebereiweiß | WH-GL-99.5-557 | auto_generated | Confirmed by domain expert |
| Ascorbic Acid Technische Qualität | Pea Protein 25% | pending_review | Auto-mapped, validated |
| resistant starch 50% | Resistant Starch Grade B | pending_review | Confirmed by domain expert |
| Lactic Acid | SIG-95-APX-PWFS | pending_review | Confirmed by domain expert |
| SIG-79-GLS-4ZZ9 | PR-PR-701 Ltd. | pending_review | Verified via product specs |
| Ascorbic Acid 98% Qualitätsstufe II | Sunflower Oil Grade A | auto_generated | Cross-referenced with transactions |
| Vanguard Supply Co. | nexus supply | unverified | Auto-mapped, validated |
| Potassium Sorbate 98% | SIG-83-OTU-QZB6 | auto_generated | Cross-referenced with transactions |
| SIG-70-YBK-DUQ6 | Ascorbic Acid | pending_review | Confirmed by domain expert |
| Ascorbic Acid Qualitätsstufe II | Sodium Chloride | auto_generated | Historical match confirmed |
| CO-OI-966 | Rapsöl | unverified | Auto-mapped, validated |
| palm oil 70% tech grade | Lactic Acid 25% Lebensmittelrein | auto_generated | Historical match confirmed |
| resistant starch 25% tech grade | CO-OI-98-FO-GR-748 | pending_review | Verified via product specs |
| horizon materials | NO-IN-155 SA | auto_generated | Verified via product specs |
| SIG-23-PGX-VBNK | PR-SU-CO-176 | unverified | Verified via product specs |
| Lactic Acid | SO-CH-99.5-GR-A-206 | auto_generated | Verified via product specs |
| SIG-35-HUP-NW3M | vertex logistics | auto_generated | Cross-referenced with transactions |
| Palm Oil Food Grade | SO-IS-PR-309 | auto_generated | Historical match confirmed |
| Stratos Processing | pinnacle chemicals Ltd. | pending_review | Auto-mapped, validated |
| RA-OI-745 | Resistente Stärke | unverified | Auto-mapped, validated |
| isoglucose 25% | SIG-42-MEI-2SCI | unverified | Auto-mapped, validated |
| EX-N-19-830 | Excise IN 7% | pending_review | Historical match confirmed |
| VE-DI-556 SA | vertex distribution International | unverified | Auto-mapped, validated |
| NE-DI-555 Corp. | SIG-58-DDZ-4JKE International | unverified | Confirmed by domain expert |
| apex chemicals Inc. | CE-MA-338 | unverified | Confirmed by domain expert |
| SIG-70-KJX-6V9L | Meridian Versorgung GmbH | auto_generated | Verified via product specs |
| EX-D-7-904 | Excise IN 20% | pending_review | Historical match confirmed |
| sunflower oil standard | Maltodextrin DE15 Premium | pending_review | Historical match confirmed |
| Zenith Supply Co. | prime logistics | unverified | Auto-mapped, validated |
| AS-AC-99.5-619 | ascorbic acid standard | auto_generated | Auto-mapped, validated |
| Quantum Chemicals | PR-IN-608 BV | unverified | Auto-mapped, validated |
| Fructose Grade B | Maltodextrin-Pulver DE18 Pharmazeutisch rein | auto_generated | Confirmed by domain expert |
| core processing Group | Elite Chemicals KG | pending_review | Confirmed by domain expert |
| Maltodextrin-Pulver DE5 Qualitätsstufe I | fructose 99.5% pharma grade | pending_review | Auto-mapped, validated |
| SIG-16-GRX-X3AK | Soja Isolate 50% Qualitätsstufe II | pending_review | Cross-referenced with transactions |
| atlantic industries International | SIG-94-MUO-QFTQ | auto_generated | Verified via product specs |
| Dextrin | SIG-89-ISH-EQW6 | unverified | Cross-referenced with transactions |
| SIG-85-WWC-01LO | sodium benzoate | auto_generated | Confirmed by domain expert |
| Isoglucose 50% Technical | dextrose 70% premium | pending_review | Confirmed by domain expert |
| Premier Vertrieb | SIG-97-TPD-0NJR LLC | pending_review | Verified via product specs |
| glucose syrup 98% food grade | AS-AC-TE-342 | unverified | Verified via product specs |
| RE-ST-FO-GR-998 | Traubenzucker 25% Technische Qualität | unverified | Cross-referenced with transactions |
| Zenith Trading | SIG-89-PGD-QMHH GmbH | unverified | Auto-mapped, validated |
| nexus industries | NE-PA-358 | auto_generated | Auto-mapped, validated |
| Calcium Carbonate | Isoglucose Qualitätsstufe II | auto_generated | Auto-mapped, validated |
| SIG-41-HXT-0U1R | Calcium Carbonate 50% Grade A | auto_generated | Historical match confirmed |
| Catalyst Supply Co. | pacific sourcing | pending_review | Verified via product specs |
| PO-SO-GR-A-715 | Glukosesirup Syrup | auto_generated | Auto-mapped, validated |
| Kasein | fructose 99.5% food grade | unverified | Confirmed by domain expert |
| SIG-98-LSP-BA0T | Atlas Materials | pending_review | Confirmed by domain expert |
| SO-CH-70-317 | Pea Protein 98% Qualitätsstufe II | pending_review | Cross-referenced with transactions |
| sodium chloride | SO-BE-99.5-TE-213 | pending_review | Auto-mapped, validated |
| continental supply | Prime Logistik | auto_generated | Cross-referenced with transactions |
| Ascorbic Acid 50% Technische Qualität | SIG-60-WEX-2G05 | auto_generated | Verified via product specs |
| Global Verarbeitung GmbH | SIG-71-XRY-PI0Y SAS | unverified | Cross-referenced with transactions |
| Atlas Materials BV | atlas ingredients | auto_generated | Confirmed by domain expert |
| SIG-89-FBG-6HKF | Quantum Versorgung GmbH | auto_generated | Cross-referenced with transactions |
| vat reduced cn 10% | Vat Standardqualität NL 20% | auto_generated | Historical match confirmed |
| SO-IS-PH-GR-671 | SIG-85-VFA-F0TJ | unverified | Historical match confirmed |
| Soja Isolate Pharmazeutisch rein | CI-AC-215 | auto_generated | Auto-mapped, validated |
| sodium benzoate 99.5% tech grade | SO-CH-99.5-GR-A-634 | unverified | Confirmed by domain expert |
| RE-ST-50-692 | Potassium Sorbate | unverified | Cross-referenced with transactions |
| continental manufacturing Inc. | Baltic Partners International | pending_review | Auto-mapped, validated |
| palm oil tech grade | Resistente Stärke | auto_generated | Historical match confirmed |
| nexus logistics | EL-SO-358 | unverified | Confirmed by domain expert |
| SIG-51-EYN-NILM LLC | stratos supply NV | unverified | Auto-mapped, validated |
| calcium carbonate 50% | Glukosesirup Syrup Premiumqualität | unverified | Confirmed by domain expert |
| vat standard br 7% | Vat Reduced FR 10% | auto_generated | Auto-mapped, validated |
| Sorbinsäure 50% | SIG-58-HNG-1XJ7 | pending_review | Confirmed by domain expert |
| SIG-16-FVU-3EBQ | Kaliumsorbat Pharmazeutisch rein | auto_generated | Confirmed by domain expert |
| SO-AC-98-579 | palm oil food grade | unverified | Historical match confirmed |
| ST-LO-927 | Atlantic Materials | auto_generated | Auto-mapped, validated |
| SIG-73-YMY-EMYO | stratos sourcing | pending_review | Cross-referenced with transactions |
| QU-SO-556 | Stratos Trading Holdings | pending_review | Verified via product specs |
| Withholding IN 20% | EX-B-10-648 | unverified | Cross-referenced with transactions |
| Fructose 70% | resistant starch standard | unverified | Verified via product specs |
| Dextrin Standardqualität | LA-AC-927 | unverified | Auto-mapped, validated |
| Traubenzucker 99.5% Standardqualität | SIG-76-GST-OWGM | unverified | Cross-referenced with transactions |
| pinnacle supply | ZE-MA-924 | pending_review | Cross-referenced with transactions |
| RE-ST-50-232 | Rapsöl 25% Lebensmittelrein | auto_generated | Confirmed by domain expert |
| SIG-54-LIP-WKBS | SO-IS-99.5-GR-A-499 | pending_review | Historical match confirmed |
| Natriumchlorid Standardqualität | sunflower oil food grade | auto_generated | Cross-referenced with transactions |
| SIG-51-IYK-630P | RA-OI-TE-584 | unverified | Historical match confirmed |
| prism industries Group | SIG-45-JPK-8INR | pending_review | Confirmed by domain expert |
| SIG-20-XSP-FVHF | SO-CH-892 | unverified | Cross-referenced with transactions |
| quantum supply | Vertex Logistics | unverified | Auto-mapped, validated |
| SIG-42-MEI-2SCI | Maltodextrin DE10 | pending_review | Verified via product specs |
| SIG-13-CZK-ACKX | dextrose standard | auto_generated | Cross-referenced with transactions |
| catalyst logistics SA | Stellar Manufacturing Group | unverified | Verified via product specs |
| nexus logistics | SIG-28-STQ-YUPS | auto_generated | Cross-referenced with transactions |
| Stratos Ingredients | Global Solutions International | auto_generated | Auto-mapped, validated |
| prime supply | Meridian Werkstoffe | pending_review | Auto-mapped, validated |
| Isoglucose Food Grade | maltodextrin de20 | auto_generated | Confirmed by domain expert |
| dextrose food grade | Soy Isolate | pending_review | Historical match confirmed |
| Cyclodextrin | Maltodextrin DE15 Premium | unverified | Historical match confirmed |
| Vanguard Versorgung BV | QU-TR-440 | auto_generated | Confirmed by domain expert |
| SIG-59-ECO-OXB3 | NO-SU-CO-376 | pending_review | Confirmed by domain expert |
| Sodium Chloride Grade B | Kasein Standardqualität | auto_generated | Confirmed by domain expert |
| maltodextrin de5 standard | Resistente Stärke 98% | auto_generated | Cross-referenced with transactions |
| SIG-59-CFT-59LL Holdings | Quantum Enterprise NV | unverified | Auto-mapped, validated |
| palm oil 50% | Maltodextrin-Pulver DE5 Qualitätsstufe II | pending_review | Verified via product specs |
| Premier Supply PLC | AT-SU-661 Corp. | auto_generated | Cross-referenced with transactions |
| VA-RE-I-5-890 | Excise NL 0% | unverified | Historical match confirmed |
| Citric Acid Grade B | GL-SY-FO-GR-600 | unverified | Confirmed by domain expert |
| LA-AC-50-PR-288 | soy isolate 99.5% standard | auto_generated | Auto-mapped, validated |
| Core Werkstoffe | Zenith Industries LLC | unverified | Auto-mapped, validated |
| Zenith Versorgung GmbH | SIG-49-QCL-LPWL | unverified | Verified via product specs |
| Sunflower Oil Grade B | SIG-55-DCV-7OXN | pending_review | Auto-mapped, validated |
| Atlantic Processing | SIG-14-TOH-IPJ4 | auto_generated | Historical match confirmed |
| Traubenzucker Qualitätsstufe I | SIG-68-PIZ-R6Q5 | auto_generated | Auto-mapped, validated |
| CO-SU-CO-318 | baltic supply | unverified | Verified via product specs |
| casein | LA-AC-98-GR-A-841 | auto_generated | Verified via product specs |
| Lactic Acid 70% Pharma Grade | Calcium Carbonate Lebensmittelrein | unverified | Cross-referenced with transactions |
| WH-GL-99.5-557 | Calcium Carbonate 50% Qualitätsstufe II | auto_generated | Cross-referenced with transactions |
| PO-SO-98-216 | Isoglucose 50% Lebensmittelrein | unverified | Confirmed by domain expert |
| Sodium Benzoate 70% | SIG-83-BMJ-HHIG | auto_generated | Historical match confirmed |
| Nordic Versorgung GmbH | SIG-53-PHC-GR8D | auto_generated | Historical match confirmed |
| Casein | ascorbic acid 99.5% standard | unverified | Confirmed by domain expert |
| Nexus Partners GmbH | Global Werkstoffe BV | auto_generated | Verified via product specs |
| Ascorbic Acid 99.5% Technische Qualität | Ascorbic Acid Standard | unverified | Cross-referenced with transactions |
| AS-AC-99.5-619 | Pea Protein Premium | unverified | Historical match confirmed |
| SIG-70-HGQ-WORL | PR-SO-469 | pending_review | Verified via product specs |
| Wheat Gluten | Weizenklebereiweiß 98% Premiumqualität | pending_review | Confirmed by domain expert |
| Atlantic Manufacturing | EL-PR-129 Ltd. | pending_review | Cross-referenced with transactions |
| AS-AC-439 | Traubenzucker Qualitätsstufe I | pending_review | Verified via product specs |
| Core Partners Ltd. | PI-IN-444 | unverified | Historical match confirmed |
| glucose syrup | Lactic Acid | pending_review | Auto-mapped, validated |
| sunflower oil 70% | SIG-45-ZHK-QWIG | auto_generated | Confirmed by domain expert |
| SIG-39-CJT-QHM3 | AT-SO-260 | auto_generated | Auto-mapped, validated |
| vertex materials | Core Versorgung GmbH | auto_generated | Verified via product specs |
| elite trading Ltd. | Prism Ingredients NV | pending_review | Cross-referenced with transactions |
| Stellar Distribution | SIG-73-XKX-JG0D SAS | unverified | Auto-mapped, validated |
| Weizenklebereiweiß Qualitätsstufe II | Coconut Oil 70% | unverified | Historical match confirmed |
| PO-SO-50-GR-B-154 | SIG-44-UIE-SASC | pending_review | Historical match confirmed |
| PO-SO-339 | SIG-30-MPO-SJEV | unverified | Cross-referenced with transactions |
| Calcium Carbonate 50% Pharmazeutisch rein | CI-AC-PR-827 | auto_generated | Verified via product specs |
| Elite Logistik Group | SIG-23-LAS-L2MX Holdings | pending_review | Confirmed by domain expert |
| ZE-PA-511 PLC | SIG-16-ZDY-GYTX Holdings | auto_generated | Cross-referenced with transactions |
| quantum logistics | Prism Sourcing | unverified | Cross-referenced with transactions |
| PR-EN-764 Ltd. | Quantum Partners | auto_generated | Confirmed by domain expert |
| Fructose | AS-AC-PH-GR-192 | unverified | Confirmed by domain expert |
| Rapsöl 50% Qualitätsstufe I | DE-99.5-720 | auto_generated | Cross-referenced with transactions |
| Natriumbenzoat 25% Standardqualität | RA-OI-431 | unverified | Historical match confirmed |
| VA-MA-537 Holdings | baltic enterprise KG | auto_generated | Historical match confirmed |
| SIG-89-JZC-1682 | Sunflower Oil Grade A | pending_review | Cross-referenced with transactions |
| SIG-45-CWR-EI9N | Potassium Sorbate 50% | pending_review | Confirmed by domain expert |
| Quantum Ingredients SARL | PR-PA-794 PLC | unverified | Historical match confirmed |
| Nordic Manufacturing NV | central solutions | pending_review | Historical match confirmed |
| Horizon Sourcing | nexus sourcing | pending_review | Verified via product specs |
| excise us 15% | Vat Standardqualität IN 0% | unverified | Confirmed by domain expert |
| SIG-92-FQX-S1BC | PA-IN-447 | unverified | Cross-referenced with transactions |
| CO-OI-ST-153 | SIG-20-CGL-C8HS | unverified | Confirmed by domain expert |
| Traubenzucker Qualitätsstufe I | SIG-41-QPX-D1RL | unverified | Confirmed by domain expert |
| SIG-29-LEJ-26GF Group | AP-TR-161 International | unverified | Auto-mapped, validated |
| SIG-52-LQX-X1DO | Rapeseed Oil Grade A | pending_review | Cross-referenced with transactions |
| dextrose premium | Pea Protein 70% Lebensmittelrein | auto_generated | Cross-referenced with transactions |
| Stratos Handel | SIG-56-END-D8WH | unverified | Historical match confirmed |
| Stratos Materials | SIG-13-NXM-NP9H | pending_review | Confirmed by domain expert |
| Soy Isolate 25% Technical | SIG-93-MGK-61BG | pending_review | Auto-mapped, validated |
| SO-IS-25-ST-345 | cyclodextrin | unverified | Auto-mapped, validated |
| sunflower oil 98% | Glukosesirup Syrup 99.5% Standardqualität | auto_generated | Verified via product specs |
| SIG-59-HZI-WDX6 Group | Quantum Vertrieb Holdings | unverified | Cross-referenced with transactions |
| maltodextrin de5 standard | Isoglucose 25% Standard | auto_generated | Auto-mapped, validated |
| SIG-57-YNC-H4UX | Customs Duty GB 5% | pending_review | Cross-referenced with transactions |
| Glukosesirup Syrup | SIG-24-GPL-7S00 | unverified | Verified via product specs |
| lactic acid standard | SIG-39-DJJ-3SY8 | unverified | Verified via product specs |
| Sunflower Oil Standard | Traubenzucker Qualitätsstufe I | auto_generated | Verified via product specs |
| Resistant Starch Standard | SIG-42-XLZ-4BOM | pending_review | Verified via product specs |
| Resistente Stärke Technische Qualität | Citric Acid 99.5% | unverified | Historical match confirmed |
| SIG-73-AXY-5E8O | LA-AC-99.5-GR-B-756 | auto_generated | Verified via product specs |
| zenith logistics | SIG-42-FYL-6VKE | unverified | Auto-mapped, validated |
| prime commodities | CO-MA-726 NV | pending_review | Verified via product specs |
| Global Versorgung GmbH | AT-MA-363 | pending_review | Verified via product specs |
| SIG-19-JRR-02SD | Customs Duty FR 7% | auto_generated | Cross-referenced with transactions |
| soy isolate pharma grade | Potassium Sorbate | auto_generated | Cross-referenced with transactions |
| Ascorbic Acid 99.5% | PE-PR-PR-564 | unverified | Verified via product specs |
| Excise US 7% | Customs Duty BR 21% | unverified | Auto-mapped, validated |
| EL-SO-199 | Prism Logistik | auto_generated | Auto-mapped, validated |
| SIG-57-NGZ-ILDZ | Kasein Pharmazeutisch rein | auto_generated | Verified via product specs |
| Lactic Acid 50% Premium | palm oil 50% | unverified | Historical match confirmed |
| CA-CA-GR-B-162 | Resistant Starch 70% | pending_review | Auto-mapped, validated |
| casein pharma grade | SO-CH-257 | auto_generated | Historical match confirmed |
| sunflower oil standard | Sunflower Oil 50% Grade A | unverified | Verified via product specs |
| casein 98% premium | GL-SY-98-ST-578 | pending_review | Cross-referenced with transactions |
| Ascorbic Acid 98% Premium | SO-BE-25-774 | auto_generated | Verified via product specs |
| AS-AC-GR-B-395 | Sunflower Oil Grade A | unverified | Historical match confirmed |
| fructose premium | Maltodextrin-Pulver DE5 Lebensmittelrein | unverified | Historical match confirmed |
| Sonnenblumenöl 98% Premiumqualität | SIG-98-NIJ-5N8C | unverified | Confirmed by domain expert |
| SIG-92-SMV-JF74 | vat standard cn 0% | unverified | Auto-mapped, validated |
| customs duty br 7% | CU-DU-D-5-294 | unverified | Historical match confirmed |
| vanguard supply NV | Horizon Partners International | unverified | Verified via product specs |
| citric acid standard | AS-AC-ST-243 | auto_generated | Auto-mapped, validated |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | sodium chloride premium | pending_review | Verified via product specs |
| ascorbic acid standard | Cyclodextrin | auto_generated | Auto-mapped, validated |
| Kaliumsorbat Technische Qualität | SIG-22-VQM-AGKC | unverified | Verified via product specs |
| Pacific Materials | atlantic logistics | pending_review | Historical match confirmed |
| SIG-70-MMO-95UC | meridian chemicals Holdings | auto_generated | Cross-referenced with transactions |
| SIG-51-MVX-XKUB | withholding fr 19% | unverified | Cross-referenced with transactions |
| Calcium Carbonate 70% Premium | SIG-33-FUV-53NO | pending_review | Cross-referenced with transactions |
| Core Logistics | pacific supply | auto_generated | Cross-referenced with transactions |
| SIG-32-DNR-U0SL | Pacific Werkstoffe GmbH | auto_generated | Confirmed by domain expert |
| Sorbinsäure Qualitätsstufe II | SO-BE-GR-B-936 | unverified | Confirmed by domain expert |
| PA-OI-70-780 | Maltodextrin DE15 | pending_review | Verified via product specs |
| BA-SU-CO-430 | vertex supply | auto_generated | Confirmed by domain expert |
| Glukosesirup Syrup 70% Lebensmittelrein | citric acid pharma grade | pending_review | Verified via product specs |
| Lactic Acid Qualitätsstufe II | PA-OI-417 | auto_generated | Verified via product specs |
| SU-OI-251 | SIG-53-LJE-NZKR | pending_review | Historical match confirmed |
| SIG-48-GDK-Y8XN | casein 25% tech grade | auto_generated | Auto-mapped, validated |
| SIG-40-YZP-9CC3 | quantum sourcing | auto_generated | Historical match confirmed |
| AT-LO-132 | stratos trading SARL | unverified | Auto-mapped, validated |
| Palmfett | SIG-95-APX-PWFS | pending_review | Auto-mapped, validated |
| Atlas Sourcing | PR-SU-CO-968 | unverified | Confirmed by domain expert |
| SIG-93-DAB-6LKS | Natriumchlorid | auto_generated | Historical match confirmed |
| meridian materials | Meridian Logistik | pending_review | Historical match confirmed |
| Glukosesirup Syrup Technische Qualität | DE-ST-553 | auto_generated | Auto-mapped, validated |
| Resistente Stärke 70% | SIG-61-KUY-VFFK | pending_review | Historical match confirmed |
| DE-TE-340 | lactic acid | pending_review | Confirmed by domain expert |
| premier solutions Corp. | Premier Partners | unverified | Verified via product specs |
| Natriumbenzoat 50% Technische Qualität | SIG-18-NCG-WT1V | unverified | Auto-mapped, validated |
| AS-AC-99.5-TE-765 | SIG-12-HNK-0H4F | unverified | Cross-referenced with transactions |
| pinnacle sourcing | Prime Logistik | pending_review | Auto-mapped, validated |
| Central Werkstoffe | Premier Materials | pending_review | Historical match confirmed |
| Pinnacle Chemicals PLC | SIG-37-AVX-CY7Q SAS | auto_generated | Auto-mapped, validated |
| VA-RE-I-20-892 | SIG-47-TWK-RYLY | unverified | Verified via product specs |
| MA-DE-951 | Calcium Carbonate Grade B | auto_generated | Historical match confirmed |
| SIG-43-GRJ-P3HT | WH-GL-50-865 | auto_generated | Historical match confirmed |
| Nordic Ingredients | SIG-70-SAQ-KIAC | unverified | Verified via product specs |
| Sorbic Acid Standard | glucose syrup 98% | pending_review | Cross-referenced with transactions |
| SIG-95-HRL-AO5O | wheat gluten standard | pending_review | Verified via product specs |
| Premier Partners Group | Prism Solutions | unverified | Auto-mapped, validated |
| NO-IN-155 SA | Continental Ingredients | auto_generated | Cross-referenced with transactions |
| Fructose 99.5% Technical | PA-OI-632 | pending_review | Historical match confirmed |
| Sonnenblumenöl Standardqualität | Cyclodextrin 98% Pharma Grade | unverified | Verified via product specs |
| Stratos Materials Group | ST-SU-125 SA | pending_review | Historical match confirmed |
| Citric Acid | isoglucose | unverified | Historical match confirmed |
| Rapsöl 50% Pharmazeutisch rein | ascorbic acid standard | unverified | Verified via product specs |
| CA-CA-99.5-FO-GR-839 | resistant starch | pending_review | Verified via product specs |
| Fructose 98% Premiumqualität | SIG-52-NBD-2SF6 | unverified | Confirmed by domain expert |
| CA-LO-415 | SIG-48-LUB-IGA7 | unverified | Cross-referenced with transactions |
| SIG-24-OUE-RXOK | Natriumbenzoat 25% | pending_review | Auto-mapped, validated |
| sodium benzoate 98% pharma grade | CI-AC-634 | auto_generated | Historical match confirmed |
| AT-SU-CO-945 | Central Logistik | pending_review | Confirmed by domain expert |
| Ascorbic Acid Standard | SO-CH-99.5-GR-A-634 | unverified | Auto-mapped, validated |
| vertex commodities KG | Nordic Verarbeitung | pending_review | Verified via product specs |
| Apex Werkstoffe | Vanguard Distribution | unverified | Cross-referenced with transactions |
| Quantum Materials | SIG-52-NEO-FFB3 | unverified | Auto-mapped, validated |
| SIG-13-DJH-ML2N | VA-RE-F-0-158 | unverified | Cross-referenced with transactions |
| SIG-75-PHG-NW65 | Soy Isolate 99.5% Premium | pending_review | Historical match confirmed |
| Withholding NL 7% | Customs Duty BR 21% | auto_generated | Confirmed by domain expert |
| wheat gluten standard | SIG-68-SYL-8192 | unverified | Confirmed by domain expert |
| SIG-60-GZP-BB7N NV | Horizon Partners Ltd. | unverified | Cross-referenced with transactions |
| central partners Inc. | Zenith Versorgung BV | auto_generated | Confirmed by domain expert |
| Apex Logistik | CE-MA-720 | auto_generated | Verified via product specs |
| Palm Oil 50% | SIG-86-QXF-N0RG | auto_generated | Auto-mapped, validated |
| pacific materials | Elite Sourcing | auto_generated | Auto-mapped, validated |
| SIG-56-JML-GDXB | ME-TR-587 | pending_review | Historical match confirmed |
| sorbic acid 25% standard | Citric Acid 25% Technical | auto_generated | Auto-mapped, validated |
| SIG-56-LHF-WMFP | PE-PR-25-185 | pending_review | Verified via product specs |
| Sodium Benzoate | SIG-51-HLJ-TN1E | unverified | Auto-mapped, validated |
| CI-AC-70-265 | Zitronensäure 70% Lebensmittelrein | pending_review | Auto-mapped, validated |
| Vat Reduced NL 25% | VA-ST-I-20-301 | auto_generated | Historical match confirmed |
| glucose syrup | Lactic Acid | unverified | Verified via product specs |
| Withholding FR 5% | SIG-41-EOV-7THY | auto_generated | Confirmed by domain expert |
| SIG-90-NFZ-XRLG | Core Logistics | auto_generated | Historical match confirmed |
| SO-CH-354 | Ascorbic Acid Technische Qualität | unverified | Auto-mapped, validated |
| Customs Duty DE 5% | WI-B-25-986 | pending_review | Confirmed by domain expert |
| quantum trading Holdings | Central Enterprise | unverified | Cross-referenced with transactions |
| IS-50-GR-A-791 | sodium benzoate 99.5% standard | pending_review | Historical match confirmed |
| Coconut Oil 99.5% Pharmazeutisch rein | SIG-70-YBK-DUQ6 | unverified | Auto-mapped, validated |
| Vat Standard IN 0% | Vat Standardqualität IN 19% | pending_review | Cross-referenced with transactions |
| SIG-80-QOK-BKBF | Fructose Premiumqualität | pending_review | Verified via product specs |
| SO-AC-FO-GR-175 | Palmfett 50% | unverified | Cross-referenced with transactions |
| resistant starch standard | MA-DE-585 | auto_generated | Confirmed by domain expert |
| pea protein pharma grade | Coconut Oil 50% Pharmazeutisch rein | auto_generated | Verified via product specs |
| PR-PR-135 KG | Catalyst Supply Holdings | unverified | Confirmed by domain expert |
| AT-LO-927 Holdings | Atlantic Trading | unverified | Auto-mapped, validated |
| vat reduced nl 20% | EX-B-25-579 | pending_review | Verified via product specs |
| vertex materials | Global Werkstoffe | auto_generated | Historical match confirmed |
| Central Versorgung GmbH | pacific materials | pending_review | Confirmed by domain expert |
| wheat gluten standard | SIG-61-XKV-ODPX | unverified | Confirmed by domain expert |
| Core Partners Ltd. | nexus processing AG | pending_review | Confirmed by domain expert |
| SIG-84-HBF-DDQL | Sodium Chloride 99.5% | pending_review | Auto-mapped, validated |
| citric acid | PA-OI-98-GR-A-940 | unverified | Confirmed by domain expert |
| CA-CA-GR-B-761 | Soja Isolate | auto_generated | Confirmed by domain expert |
| Withholding GB 5% | SIG-28-HHW-S34S | unverified | Verified via product specs |
| dextrin 70% pharma grade | Isoglucose Qualitätsstufe II | pending_review | Confirmed by domain expert |
| SIG-86-PYU-PCGN | meridian materials | auto_generated | Cross-referenced with transactions |
| Sorbic Acid 25% Pharma Grade | MA-DE-700 | auto_generated | Auto-mapped, validated |
| sorbic acid premium | SIG-42-XLZ-4BOM | auto_generated | Cross-referenced with transactions |
| ascorbic acid food grade | CA-CA-648 | unverified | Auto-mapped, validated |
| SIG-52-CHY-4N5P | dextrin | auto_generated | Historical match confirmed |
| AT-CH-900 AG | Elite Solutions | pending_review | Verified via product specs |
| Resistant Starch 50% Standard | citric acid 70% | pending_review | Confirmed by domain expert |
| SU-OI-GR-B-259 | SIG-53-LJE-NZKR | auto_generated | Auto-mapped, validated |
| SIG-69-FIT-Y3OC International | Central Logistik GmbH | auto_generated | Historical match confirmed |
| SIG-50-NZZ-E4UN | Dextrose | unverified | Cross-referenced with transactions |
| Calcium Carbonate 98% Standard | CY-ST-539 | unverified | Verified via product specs |
| continental ingredients | HO-PR-719 Holdings | auto_generated | Auto-mapped, validated |
| elite trading Group | Atlantic Trading | pending_review | Auto-mapped, validated |
| Glukosesirup Syrup | SO-CH-TE-223 | pending_review | Verified via product specs |
| SIG-66-FRL-CVIT | resistant starch | auto_generated | Cross-referenced with transactions |
| Meridian Versorgung GmbH | prism supply | pending_review | Verified via product specs |
| sunflower oil premium | SIG-88-RKE-8R7A | auto_generated | Cross-referenced with transactions |
| SIG-71-FNO-CX9K | LA-AC-70-PH-GR-221 | pending_review | Historical match confirmed |
| Calcium Carbonate Standardqualität | dextrin tech grade | unverified | Cross-referenced with transactions |
| Central Enterprise | SIG-36-PWY-HJFC International | pending_review | Cross-referenced with transactions |
| MA-DE-859 | Fructose 50% Standard | auto_generated | Cross-referenced with transactions |
| SIG-61-CIV-LFWA | Dextrose 99.5% | auto_generated | Historical match confirmed |
| SIG-51-HOK-PC9S Holdings | PR-MA-826 Corp. | unverified | Verified via product specs |
| stellar logistics | Central Logistics | auto_generated | Verified via product specs |
| Traubenzucker Qualitätsstufe I | SIG-27-RTX-YEAW | pending_review | Historical match confirmed |
| SIG-64-BPY-A8RD | DE-ST-385 | auto_generated | Cross-referenced with transactions |
| Kaliumsorbat | CA-CA-99.5-FO-GR-839 | pending_review | Historical match confirmed |
| Atlas Logistik International | Horizon Trading Ltd. | auto_generated | Historical match confirmed |
| SO-CH-115 | dextrose premium | pending_review | Confirmed by domain expert |
| Sodium Chloride 25% Food Grade | SO-IS-GR-A-940 | auto_generated | Confirmed by domain expert |
| FR-124 | SIG-66-LJV-5E3H | unverified | Verified via product specs |
| SIG-81-AMW-NE5V | catalyst sourcing | unverified | Historical match confirmed |
| SIG-62-BTJ-PQV9 | lactic acid | auto_generated | Cross-referenced with transactions |
| maltodextrin de20 | SIG-10-KDB-LGYT | pending_review | Cross-referenced with transactions |
| SIG-78-WKT-9TDY SAS | Global Logistics | unverified | Historical match confirmed |
| Palm Oil 50% | SO-IS-432 | pending_review | Verified via product specs |
| ST-DI-183 Inc. | Catalyst Werkstoffe NV | auto_generated | Verified via product specs |
| Core Werkstoffe | SIG-68-BSB-VSIA | auto_generated | Historical match confirmed |
| Withholding NL 7% | SIG-43-SSK-5L22 | pending_review | Auto-mapped, validated |
| RE-ST-50-526 | Pea Protein 70% Pharma Grade | auto_generated | Verified via product specs |
| Dextrin Food Grade | Sonnenblumenöl | auto_generated | Confirmed by domain expert |
| SIG-66-ZOH-E8TV | casein | unverified | Verified via product specs |
| Nexus Partners Group | Nexus Chemicals Group | pending_review | Confirmed by domain expert |
| SIG-48-DTM-5XF3 Corp. | Apex Materials Group | auto_generated | Auto-mapped, validated |
| SIG-12-OAV-ALF4 | CO-OI-25-252 | pending_review | Historical match confirmed |
| ascorbic acid pharma grade | Resistente Stärke Pharmazeutisch rein | pending_review | Verified via product specs |
| EX-N-21-216 | Withholding GB 21% | unverified | Verified via product specs |
| Ascorbic Acid 50% | sorbic acid standard | unverified | Verified via product specs |
| elite trading | Zenith Manufacturing Holdings | unverified | Confirmed by domain expert |
| lactic acid standard | SO-BE-99.5-GR-A-930 | pending_review | Confirmed by domain expert |
| CO-OI-GR-A-370 | Weizenklebereiweiß | unverified | Historical match confirmed |
| IS-FO-GR-335 | Resistente Stärke Pharmazeutisch rein | auto_generated | Cross-referenced with transactions |
| SIG-70-MMO-95UC | pinnacle logistics | pending_review | Cross-referenced with transactions |
| Pinnacle Materials | vertex sourcing | unverified | Verified via product specs |
| Pea Protein Premiumqualität | Soy Isolate 25% Pharma Grade | pending_review | Historical match confirmed |
| Lactic Acid Food Grade | wheat gluten 98% | auto_generated | Cross-referenced with transactions |
| GL-SY-70-549 | Lactic Acid Food Grade | unverified | Verified via product specs |
| potassium sorbate standard | SIG-42-LOE-5XD8 | auto_generated | Verified via product specs |
| soy isolate | Weizenklebereiweiß Lebensmittelrein | auto_generated | Confirmed by domain expert |
| Continental Chemicals Inc. | SIG-67-LHQ-GQOH BV | unverified | Cross-referenced with transactions |
| PR-CH-565 SAS | Stratos Handel Group | unverified | Confirmed by domain expert |
| Potassium Sorbate Food Grade | dextrose | auto_generated | Historical match confirmed |
| Lactic Acid Food Grade | SIG-51-KQC-QY9M | unverified | Cross-referenced with transactions |
| SIG-72-FHF-DYSG | Vertex Chemicals | auto_generated | Cross-referenced with transactions |
| Soy Isolate 25% Technical | GL-SY-PR-440 | auto_generated | Historical match confirmed |
| core partners BV | SIG-50-GYK-UH5P | unverified | Confirmed by domain expert |
| Sorbinsäure 50% Standardqualität | SIG-47-NVU-R3XU | unverified | Confirmed by domain expert |
| SIG-79-RTU-R8IQ | Soy Isolate 99.5% | auto_generated | Historical match confirmed |
| Natriumbenzoat 99.5% Qualitätsstufe I | SIG-16-GRX-X3AK | unverified | Verified via product specs |
| Cyclodextrin Lebensmittelrein | AS-AC-50-321 | unverified | Cross-referenced with transactions |
| AS-AC-GR-B-855 | Fructose Food Grade | unverified | Auto-mapped, validated |
| SO-BE-99.5-TE-213 | Weizenklebereiweiß Qualitätsstufe I | unverified | Historical match confirmed |
| SIG-68-DWS-MNR6 | DE-98-512 | auto_generated | Auto-mapped, validated |
| Dextrin Technical | AS-AC-99.5-PR-761 | pending_review | Verified via product specs |
| SIG-60-OHC-5EQB | Prism Versorgung GmbH | auto_generated | Verified via product specs |
| excise in 20% | SIG-51-DNC-4AET | pending_review | Auto-mapped, validated |
| SIG-67-MJH-V4Q5 | Catalyst Werkstoffe | unverified | Cross-referenced with transactions |
| Kasein Premiumqualität | Fructose Premium | auto_generated | Auto-mapped, validated |
| Ascorbic Acid Lebensmittelrein | glucose syrup 25% | unverified | Verified via product specs |
| SIG-63-MSP-S6JE | prime sourcing | auto_generated | Cross-referenced with transactions |
| Nexus Werkstoffe | CE-SO-153 | auto_generated | Historical match confirmed |
| Dextrose 25% | Dextrin Technische Qualität | pending_review | Historical match confirmed |
| global distribution | Central Supply Holdings | auto_generated | Cross-referenced with transactions |
| SIG-93-MGK-61BG | soy isolate 99.5% premium | pending_review | Auto-mapped, validated |
| CO-OI-25-TE-157 | Isoglucose 70% | unverified | Verified via product specs |
| Vertex Logistics | Premier Logistik | auto_generated | Cross-referenced with transactions |
| VA-RE-C-10-444 | SIG-98-NDY-OCEW | unverified | Verified via product specs |
| SIG-92-AXW-GPAG | Vertex Chemicals | unverified | Cross-referenced with transactions |
| SIG-66-MYF-XDYQ | Natriumchlorid | pending_review | Cross-referenced with transactions |
| Zenith Logistics | stellar logistics | pending_review | Cross-referenced with transactions |
| SIG-86-XWS-MOPG Corp. | Stellar Materials Group | auto_generated | Confirmed by domain expert |
| Lactic Acid | SIG-72-YEU-SCIQ | pending_review | Auto-mapped, validated |
| Palmfett 50% | pea protein | pending_review | Auto-mapped, validated |
| Vat Standardqualität US 21% | Vat Reduced GB 21% | auto_generated | Verified via product specs |
| SIG-68-BSB-VSIA | Global Solutions International | auto_generated | Historical match confirmed |
| Rapsöl 70% Premiumqualität | fructose | pending_review | Cross-referenced with transactions |
| Vanguard Handel LLC | PR-CH-188 | auto_generated | Confirmed by domain expert |
| SIG-62-NKL-SM8R | continental processing Group | pending_review | Auto-mapped, validated |
| Pinnacle Chemicals Ltd. | Baltic Processing PLC | auto_generated | Historical match confirmed |
| dextrin | DE-50-891 | unverified | Auto-mapped, validated |
| Vat Reduced BR 21% | SIG-20-GIF-RAEQ | pending_review | Historical match confirmed |
| SIG-64-IEU-FRGN | resistant starch 70% | unverified | Cross-referenced with transactions |
| Sorbic Acid Food Grade | SIG-24-LEE-BXW7 | auto_generated | Auto-mapped, validated |
| Sodium Benzoate 99.5% Technical | SIG-52-ITT-ELH9 | pending_review | Cross-referenced with transactions |
| Isoglucose Qualitätsstufe II | potassium sorbate | auto_generated | Confirmed by domain expert |
| nexus sourcing | Premier Supply Co. | pending_review | Auto-mapped, validated |
| Ascorbic Acid 70% | Rapsöl 50% Pharmazeutisch rein | unverified | Cross-referenced with transactions |
| Isoglucose Qualitätsstufe II | SIG-38-CEJ-1ISY | unverified | Cross-referenced with transactions |
| Pinnacle Industries SAS | Vanguard Ingredients | auto_generated | Confirmed by domain expert |
| Kaliumsorbat Qualitätsstufe II | AS-AC-PR-778 | unverified | Confirmed by domain expert |
| SIG-17-LVE-03G9 | Resistente Stärke 70% | unverified | Historical match confirmed |
| Natriumchlorid 98% Pharmazeutisch rein | pea protein 70% tech grade | unverified | Auto-mapped, validated |
| Ascorbic Acid | Glucose Syrup 25% | pending_review | Historical match confirmed |
| SIG-86-VCP-SVOL | Rapeseed Oil 98% | unverified | Historical match confirmed |
| Maltodextrin-Pulver DE15 Standardqualität | Sodium Benzoate Grade A | unverified | Verified via product specs |
| RA-OI-FO-GR-269 | Resistant Starch | auto_generated | Cross-referenced with transactions |
| SIG-99-AYV-D18J International | Meridian Vertrieb International | pending_review | Cross-referenced with transactions |
| SIG-88-RGQ-WZOI | apex ingredients KG | pending_review | Confirmed by domain expert |
| pacific logistics Holdings | Baltic Enterprise Holdings | pending_review | Auto-mapped, validated |
| SIG-73-AXD-XIX9 | Vanguard Versorgung GmbH | unverified | Verified via product specs |
| Glucose Syrup 98% | SU-OI-ST-194 | pending_review | Verified via product specs |
| Sodium Benzoate | SO-IS-PR-309 | unverified | Verified via product specs |
| Resistant Starch | SIG-16-QDM-JLQM | unverified | Confirmed by domain expert |
| Continental Manufacturing Inc. | SIG-58-WYL-XCXB | unverified | Confirmed by domain expert |
| Citric Acid | SIG-23-IEJ-V2T3 | auto_generated | Historical match confirmed |
| Weizenklebereiweiß Qualitätsstufe I | sodium benzoate food grade | unverified | Historical match confirmed |
| Ascorbic Acid 50% Technische Qualität | AS-AC-165 | auto_generated | Verified via product specs |
| Fructose 99.5% Technical | potassium sorbate | pending_review | Confirmed by domain expert |
| Vertex Logistik | ZE-SO-131 | pending_review | Cross-referenced with transactions |
| Rapeseed Oil | SO-BE-50-427 | unverified | Confirmed by domain expert |
| Stellar Versorgung GmbH | SIG-89-HLJ-NILC | auto_generated | Auto-mapped, validated |
| palm oil food grade | RE-ST-70-901 | auto_generated | Verified via product specs |
| CY-PR-796 | SIG-47-UCC-EFEL | auto_generated | Confirmed by domain expert |
| SIG-79-OZQ-4I2N | Dextrin 25% Premiumqualität | pending_review | Cross-referenced with transactions |
| Maltodextrin-Pulver DE10 Premiumqualität | Isoglucose Technical | unverified | Auto-mapped, validated |
| Vat Reduced NL 25% | WI-D-15-830 | pending_review | Auto-mapped, validated |
| SIG-33-IHK-2GVW | Core Logistik | pending_review | Historical match confirmed |
| SIG-44-UIE-SASC | WH-GL-GR-B-926 | auto_generated | Auto-mapped, validated |
| Palm Oil | AS-AC-98-PR-217 | auto_generated | Auto-mapped, validated |
| SIG-38-CEJ-1ISY | PO-SO-25-PH-GR-260 | auto_generated | Confirmed by domain expert |
| SIG-18-WKH-NATG | RA-OI-98-679 | unverified | Cross-referenced with transactions |
| pinnacle logistics | Horizon Rohstoffe PLC | pending_review | Verified via product specs |
| Maltodextrin-Pulver DE10 | SO-BE-TE-847 | pending_review | Historical match confirmed |
| CA-MA-129 | elite supply | pending_review | Auto-mapped, validated |
| PA-SU-CO-173 | Atlas Versorgung GmbH | unverified | Verified via product specs |
| ST-SO-965 | stellar partners Ltd. | unverified | Verified via product specs |
| Calcium Carbonate 98% Pharmazeutisch rein | Isoglucose Grade B | pending_review | Historical match confirmed |
| central materials | ST-SO-491 | unverified | Confirmed by domain expert |
| PR-CH-314 Group | Atlas Industrien KG | pending_review | Cross-referenced with transactions |
| zenith industries | Catalyst Distribution | pending_review | Historical match confirmed |
| SU-OI-TE-705 | Traubenzucker Pharmazeutisch rein | pending_review | Auto-mapped, validated |
| Vat Standard GB 19% | vat standard de 7% | auto_generated | Historical match confirmed |
| vanguard partners Ltd. | SIG-98-CTS-XPY5 | auto_generated | Confirmed by domain expert |
| VA-RE-F-25-707 | vat reduced de 5% | pending_review | Verified via product specs |
| citric acid premium | SIG-83-PHT-N27M | pending_review | Confirmed by domain expert |
| SIG-48-ASO-8G0Y | isoglucose 70% | pending_review | Verified via product specs |
| Lactic Acid 70% Pharmazeutisch rein | soy isolate premium | unverified | Confirmed by domain expert |
| Fructose | CO-OI-70-553 | unverified | Auto-mapped, validated |
| SO-AC-FO-GR-175 | SIG-35-SZU-VMRU | auto_generated | Cross-referenced with transactions |
| Pacific Sourcing | stellar logistics | pending_review | Auto-mapped, validated |
| SIG-27-DQT-IQ97 | Stratos Supply Group | unverified | Confirmed by domain expert |
| rapeseed oil 98% | Soja Isolate | auto_generated | Confirmed by domain expert |
| SO-AC-50-ST-563 | Sonnenblumenöl Technische Qualität | auto_generated | Confirmed by domain expert |
| fructose | Casein Standard | unverified | Verified via product specs |
| Resistente Stärke 70% Lebensmittelrein | Resistant Starch Technical | auto_generated | Historical match confirmed |
| CE-MA-338 | Atlas Industrien International | auto_generated | Verified via product specs |
| Prime Partners | Apex Materials Group | pending_review | Cross-referenced with transactions |
| nexus partners Group | SIG-98-SID-2107 GmbH | pending_review | Verified via product specs |
| Withholding NL 21% | WI-G-21-298 | pending_review | Historical match confirmed |
| Atlas Trading SA | Pacific Ingredients BV | pending_review | Verified via product specs |
| Rapeseed Oil Technical | SIG-25-ABB-2SBA | pending_review | Auto-mapped, validated |
| Horizon Supply Co. | SIG-75-QOJ-Q4NY | pending_review | Verified via product specs |
| PE-PR-TE-718 | ascorbic acid tech grade | auto_generated | Auto-mapped, validated |
| Calcium Carbonate 99.5% | SO-AC-25-PH-GR-887 | pending_review | Cross-referenced with transactions |
| SIG-91-UWU-GPZB | Lactic Acid 50% Grade A | pending_review | Historical match confirmed |
| Soy Isolate Grade A | SU-OI-765 | unverified | Confirmed by domain expert |
| SIG-47-SRN-QNYY | CI-AC-ST-565 | pending_review | Historical match confirmed |
| Fructose | sunflower oil standard | auto_generated | Auto-mapped, validated |
| Quantum Supply Co. | SIG-65-TTX-PCJA | pending_review | Historical match confirmed |
| Resistente Stärke 50% | dextrose | auto_generated | Historical match confirmed |
| Dextrin Lebensmittelrein | SIG-91-GMY-Q91Y | unverified | Cross-referenced with transactions |
| SIG-81-EUR-UFA2 | stellar logistics | auto_generated | Auto-mapped, validated |
| FR-ST-953 | SIG-83-BMJ-HHIG | unverified | Cross-referenced with transactions |
| NO-LO-302 | Prism Logistik | unverified | Cross-referenced with transactions |
| Glukosesirup Syrup | glucose syrup | auto_generated | Confirmed by domain expert |
| Customs Duty DE 0% | SIG-27-VXG-OFKE | unverified | Cross-referenced with transactions |
| Coconut Oil 98% | rapeseed oil | unverified | Auto-mapped, validated |
| pinnacle ingredients GmbH | SIG-69-CZY-YXFK | pending_review | Cross-referenced with transactions |
| SIG-75-WDP-0BHF | Sorbic Acid 98% | unverified | Auto-mapped, validated |
| Quantum Handel Ltd. | Zenith Manufacturing | unverified | Historical match confirmed |
| Central Logistics | SIG-68-BSB-VSIA | pending_review | Historical match confirmed |
| sorbic acid 98% | Isoglucose 25% | unverified | Auto-mapped, validated |
| AP-SO-576 | Catalyst Materials | auto_generated | Historical match confirmed |
| SIG-46-SVJ-5IZO | ascorbic acid | auto_generated | Confirmed by domain expert |
| Soja Isolate 99.5% | SIG-82-GZF-51ZF | unverified | Historical match confirmed |
| Dextrose | Soja Isolate 99.5% Premiumqualität | pending_review | Auto-mapped, validated |
| SIG-43-XDN-7VEU | Excise NL 10% | pending_review | Confirmed by domain expert |
| Vanguard Supply Co. | QU-LO-616 | pending_review | Verified via product specs |
| sodium benzoate 99.5% tech grade | SIG-20-OAV-1IKJ | auto_generated | Auto-mapped, validated |
| GL-SU-CO-128 | Vertex Werkstoffe | auto_generated | Verified via product specs |
| Pinnacle Chemicals SA | prism partners Holdings | unverified | Historical match confirmed |
| SIG-18-PCA-V46E | Fructose 99.5% Technische Qualität | pending_review | Cross-referenced with transactions |
| Sorbinsäure | SIG-84-DSO-4S47 | unverified | Confirmed by domain expert |
| central logistics Group | SIG-82-ZXL-FF30 International | auto_generated | Auto-mapped, validated |
| ST-DI-183 Inc. | Atlas Enterprise International | unverified | Historical match confirmed |
| Natriumchlorid Technische Qualität | PA-OI-98-587 | auto_generated | Historical match confirmed |
| Nexus Logistik | Nordic Logistics | unverified | Confirmed by domain expert |
| Coconut Oil 98% Technische Qualität | SIG-20-UMV-LJM6 | pending_review | Verified via product specs |
| Fructose Pharmazeutisch rein | ascorbic acid pharma grade | pending_review | Cross-referenced with transactions |
| SIG-81-EKU-R7CX Group | Prime Solutions Holdings | auto_generated | Historical match confirmed |
| Pacific Enterprise International | SIG-94-AWA-77SY Holdings | auto_generated | Confirmed by domain expert |
| SO-BE-98-PH-GR-434 | sodium chloride | pending_review | Historical match confirmed |
| isoglucose 70% | Coconut Oil 98% | unverified | Cross-referenced with transactions |
| pea protein 99.5% | WH-GL-GR-B-129 | auto_generated | Confirmed by domain expert |
| FR-GR-B-231 | SIG-17-OVA-CCDM | unverified | Auto-mapped, validated |
| Traubenzucker 25% | SU-OI-TE-705 | auto_generated | Verified via product specs |
| Apex Handel | pinnacle distribution Ltd. | pending_review | Cross-referenced with transactions |
| Apex Chemicals | GL-PR-599 | unverified | Auto-mapped, validated |
| SIG-98-ZFI-37SU | Sorbinsäure 50% Standardqualität | auto_generated | Auto-mapped, validated |
| Resistente Stärke Pharmazeutisch rein | Sodium Benzoate 98% | unverified | Confirmed by domain expert |
| Casein 98% Technical | SO-BE-25-982 | auto_generated | Historical match confirmed |
| resistant starch standard | Calcium Carbonate 99.5% Food Grade | pending_review | Verified via product specs |
| sorbic acid | CO-OI-50-TE-561 | pending_review | Auto-mapped, validated |
| EX-U-15-972 | Vat Reduced FR 20% | auto_generated | Historical match confirmed |
| Vanguard Chemicals SAS | SIG-69-VKL-Z1GW KG | unverified | Historical match confirmed |
| SIG-74-LEZ-GZA2 AG | Elite Materials NV | auto_generated | Verified via product specs |
| SIG-26-KHF-99OH | Lactic Acid 50% Premium | auto_generated | Historical match confirmed |
| Traubenzucker 25% | LA-AC-GR-A-949 | pending_review | Auto-mapped, validated |
| SIG-32-NVJ-H1RC | excise cn 21% | auto_generated | Historical match confirmed |
| Traubenzucker Standardqualität | SO-AC-50-FO-GR-250 | auto_generated | Auto-mapped, validated |
| Prism Manufacturing LLC | global supply | unverified | Cross-referenced with transactions |
| SIG-59-HVI-BACX Group | atlantic trading BV | pending_review | Confirmed by domain expert |
| Elite Handel PLC | SIG-51-ZHS-W8WR International | unverified | Cross-referenced with transactions |
| SIG-47-LPF-7QXJ | SO-CH-354 | pending_review | Auto-mapped, validated |
| pinnacle logistics | Nexus Materials | pending_review | Verified via product specs |
| VA-RE-C-21-484 | Vat Reduced NL 25% | unverified | Confirmed by domain expert |
| Weizenklebereiweiß 98% Premiumqualität | PO-SO-FO-GR-989 | pending_review | Verified via product specs |
| Withholding NL 10% | SIG-19-JRR-02SD | unverified | Confirmed by domain expert |
| Apex Werkstoffe | ST-DI-517 Holdings | unverified | Confirmed by domain expert |
| SIG-49-OHU-U248 | fructose 70% | unverified | Historical match confirmed |
| Fructose 99.5% Technical | Sonnenblumenöl Pharmazeutisch rein | pending_review | Historical match confirmed |
| Vertex Distribution AG | pinnacle distribution Holdings | auto_generated | Cross-referenced with transactions |
| LA-AC-690 | wheat gluten | unverified | Cross-referenced with transactions |
| Glukosesirup Syrup | soy isolate 98% | auto_generated | Historical match confirmed |
| CO-OI-98-TE-864 | SIG-44-FWT-OA3N | auto_generated | Confirmed by domain expert |
| Dextrin | SIG-26-ADB-B4F0 | unverified | Verified via product specs |
| RE-ST-575 | Soy Isolate 99.5% | pending_review | Confirmed by domain expert |
| Sodium Chloride | MA-DE-186 | pending_review | Confirmed by domain expert |
| sorbic acid | Rapsöl | pending_review | Auto-mapped, validated |
| Coconut Oil 98% Grade A | CI-AC-488 | pending_review | Verified via product specs |
| SO-CH-98-GR-B-961 | Calcium Carbonate 98% | auto_generated | Cross-referenced with transactions |
| SIG-23-NOR-OPI3 | Prime Rohstoffe LLC | pending_review | Cross-referenced with transactions |
| Kaliumsorbat | Pea Protein | unverified | Historical match confirmed |
| Rapeseed Oil Technical | Calcium Carbonate 25% | pending_review | Historical match confirmed |
| Vertex Industrien NV | SIG-63-DWD-X8UB | pending_review | Auto-mapped, validated |
| SIG-94-OAX-GACW Ltd. | Prime Chemicals SAS | pending_review | Verified via product specs |
| Horizon Sourcing | SIG-43-FST-BKJ7 | unverified | Historical match confirmed |
| SIG-42-IEF-RFC9 | wheat gluten standard | auto_generated | Verified via product specs |
| SIG-14-GCI-G4Q9 | Pinnacle Supply Co. | auto_generated | Historical match confirmed |
| Glucose Syrup | SO-BE-TE-847 | pending_review | Auto-mapped, validated |
| Customs Duty US 20% | excise cn 19% | unverified | Auto-mapped, validated |
| Prism Industrien International | Prime Chemicals | auto_generated | Verified via product specs |
| Resistente Stärke Technische Qualität | DE-GR-B-157 | unverified | Historical match confirmed |
| WI-U-19-722 | Customs Duty FR 19% | auto_generated | Auto-mapped, validated |
| dextrin 70% pharma grade | CO-OI-817 | auto_generated | Verified via product specs |
| Horizon Logistik | BA-SU-CO-569 | auto_generated | Verified via product specs |
| Casein Grade B | SIG-29-GNG-K4K6 | unverified | Verified via product specs |
| SIG-50-TGM-XVD2 | Vat Standardqualität NL 19% | unverified | Historical match confirmed |
| WI-I-21-324 | Vat Reduced GB 15% | auto_generated | Auto-mapped, validated |
| SIG-22-XCC-QSNV | MA-DE-933 | unverified | Confirmed by domain expert |
| meridian materials | Prism Sourcing | auto_generated | Verified via product specs |
| Dextrin 70% Pharma Grade | CI-AC-215 | unverified | Verified via product specs |
| Cyclodextrin 98% Premiumqualität | Dextrin | unverified | Cross-referenced with transactions |
| SO-IS-GR-A-940 | SIG-61-HXH-PFBC | pending_review | Verified via product specs |
| Weizenklebereiweiß Pharmazeutisch rein | FR-FO-GR-823 | auto_generated | Auto-mapped, validated |
| Catalyst Commodities GmbH | Atlas Chemicals | pending_review | Historical match confirmed |
| RA-OI-25-FO-GR-818 | SIG-89-ISH-EQW6 | auto_generated | Verified via product specs |
| Fructose | fructose 25% | auto_generated | Historical match confirmed |
| PR-SO-362 | Prime Partners | pending_review | Verified via product specs |
| Sorbic Acid Grade B | Kaliumsorbat | unverified | Cross-referenced with transactions |
| ME-LO-731 | SIG-33-YPL-RQCS | auto_generated | Auto-mapped, validated |
| AS-AC-TE-342 | Lactic Acid 50% Premiumqualität | pending_review | Cross-referenced with transactions |
| Stratos Ingredients | atlas materials | unverified | Confirmed by domain expert |
| Withholding CN 0% | Vat Reduced NL 20% | unverified | Historical match confirmed |
| PI-SU-CO-364 | Horizon Versorgung GmbH | unverified | Historical match confirmed |
| Soy Isolate 50% Grade B | LA-AC-554 | unverified | Cross-referenced with transactions |
| AS-AC-130 | SIG-58-NYA-2O4M | unverified | Historical match confirmed |
| Dextrin | SIG-51-YTN-F537 | pending_review | Verified via product specs |
| Vertex Werkstoffe | horizon logistics | pending_review | Cross-referenced with transactions |
| fructose 99.5% pharma grade | SIG-53-AHT-MGFX | auto_generated | Verified via product specs |
| SIG-37-ZOD-1VME | WH-GL-GR-A-924 | auto_generated | Verified via product specs |
| Pea Protein 99.5% Premium | dextrose 70% | pending_review | Historical match confirmed |
| MA-DE-161 | Isoglucose 70% | pending_review | Auto-mapped, validated |
| Potassium Sorbate | Maltodextrin-Pulver DE10 Premiumqualität | pending_review | Cross-referenced with transactions |
| SIG-12-HNK-0H4F | Weizenklebereiweiß Qualitätsstufe I | pending_review | Auto-mapped, validated |
| Dextrose Grade A | Lactic Acid Technische Qualität | auto_generated | Confirmed by domain expert |
| Coconut Oil Pharma Grade | DE-GR-A-351 | unverified | Confirmed by domain expert |
| RA-OI-745 | Dextrose | pending_review | Verified via product specs |
| glucose syrup 25% | PA-OI-417 | pending_review | Cross-referenced with transactions |
| Catalyst Ingredients Holdings | Premier Trading KG | pending_review | Confirmed by domain expert |
| Sodium Benzoate 99.5% Grade A | Fructose 99.5% Technische Qualität | unverified | Auto-mapped, validated |
| palm oil tech grade | Resistant Starch | unverified | Verified via product specs |
| Excise IN 15% | customs duty br 20% | auto_generated | Auto-mapped, validated |
| PR-PA-779 PLC | SIG-81-ZWF-2I7Z Corp. | unverified | Auto-mapped, validated |
| Vertex Logistics | Vanguard Versorgung GmbH | pending_review | Auto-mapped, validated |
| Potassium Sorbate Standard | fructose 99.5% premium | unverified | Confirmed by domain expert |
| VE-SO-701 | pacific supply | pending_review | Historical match confirmed |
| Pea Protein | casein standard | auto_generated | Verified via product specs |
| SO-AC-25-GR-B-198 | SIG-32-TTU-44MW | unverified | Verified via product specs |
| vat reduced br 21% | SIG-45-QQC-Z4N0 | unverified | Historical match confirmed |
| GL-MA-770 | Baltic Sourcing | unverified | Confirmed by domain expert |
| SIG-20-LIK-8TZV Ltd. | ME-EN-379 Group | pending_review | Auto-mapped, validated |
| Atlantic Sourcing | AP-SO-576 | auto_generated | Cross-referenced with transactions |
| sodium benzoate 99.5% standard | SIG-68-SYL-8192 | pending_review | Auto-mapped, validated |
| SIG-22-HSE-KSCU | central logistics | pending_review | Historical match confirmed |
| nexus partners SARL | Core Partners | auto_generated | Cross-referenced with transactions |
| prism materials | Vertex Materials | auto_generated | Historical match confirmed |
| sodium benzoate | Cyclodextrin Standardqualität | auto_generated | Auto-mapped, validated |
| Global Distribution LLC | CA-SU-512 Holdings | auto_generated | Historical match confirmed |
| CI-AC-FO-GR-293 | dextrin standard | unverified | Cross-referenced with transactions |
| SIG-99-CEZ-35MR | Vanguard Industrien | auto_generated | Verified via product specs |
| AT-CO-808 GmbH | premier industries Holdings | unverified | Confirmed by domain expert |
| CY-763 | glucose syrup tech grade | unverified | Auto-mapped, validated |
| Sorbinsäure 99.5% | Palm Oil 50% | pending_review | Auto-mapped, validated |
| Cyclodextrin Pharma Grade | CY-926 | auto_generated | Confirmed by domain expert |
| ascorbic acid 70% | PE-PR-557 | unverified | Auto-mapped, validated |
| dextrose tech grade | Soy Isolate 50% Grade B | unverified | Auto-mapped, validated |
| SIG-44-DLM-CU63 | Pacific Materials | unverified | Auto-mapped, validated |
| Soy Isolate 99.5% Grade A | SIG-32-TTU-44MW | unverified | Confirmed by domain expert |
| Vanguard Logistics | SIG-82-DAB-YHKJ | unverified | Historical match confirmed |
| Soy Isolate 99.5% Grade A | IS-802 | pending_review | Historical match confirmed |
| SIG-27-QTK-7Y6C | Pinnacle Ingredients KG | pending_review | Verified via product specs |
| SO-IS-PR-309 | Citric Acid Food Grade | pending_review | Historical match confirmed |
| SO-CH-ST-522 | Traubenzucker 25% | pending_review | Confirmed by domain expert |
| Sodium Benzoate 98% | calcium carbonate 50% | pending_review | Historical match confirmed |
| maltodextrin de5 premium | Sodium Chloride | pending_review | Verified via product specs |
| Resistente Stärke 70% | CO-OI-50-147 | pending_review | Historical match confirmed |
| Weizenklebereiweiß Qualitätsstufe II | SU-OI-ST-194 | unverified | Historical match confirmed |
| Soja Isolate 98% Premiumqualität | Dextrose 25% | pending_review | Confirmed by domain expert |
| SIG-86-VCP-SVOL | pea protein standard | auto_generated | Cross-referenced with transactions |
| Zitronensäure | SIG-45-CWR-EI9N | unverified | Cross-referenced with transactions |
| Atlas Logistik | SIG-69-XDV-YH2E | auto_generated | Cross-referenced with transactions |
| premier industries Holdings | Prism Manufacturing LLC | auto_generated | Auto-mapped, validated |
| SO-AC-340 | SIG-25-ABB-2SBA | unverified | Historical match confirmed |
| Lactic Acid 99.5% | Glucose Syrup 98% Grade A | unverified | Auto-mapped, validated |
| SIG-16-QDW-AN2Z | Prism Sourcing | auto_generated | Confirmed by domain expert |
| Soja Isolate 98% | citric acid 99.5% | unverified | Confirmed by domain expert |
| SIG-15-MKL-LGBK | Coconut Oil Lebensmittelrein | unverified | Confirmed by domain expert |
| SO-AC-852 | Wheat Gluten Grade A | pending_review | Verified via product specs |
| SIG-93-DAB-6LKS | Ascorbic Acid Technical | auto_generated | Confirmed by domain expert |
| SIG-38-FPC-A25N | PR-MA-897 | auto_generated | Historical match confirmed |
| Nexus Materials | ST-SO-771 | auto_generated | Historical match confirmed |
| Pea Protein 25% | calcium carbonate food grade | unverified | Cross-referenced with transactions |
| SIG-80-ZKZ-ANXJ | Excise FR 0% | auto_generated | Auto-mapped, validated |
| Coconut Oil 70% | cyclodextrin | pending_review | Auto-mapped, validated |
| CA-CA-FO-GR-685 | wheat gluten 98% | unverified | Historical match confirmed |
| Wheat Gluten Grade B | PO-SO-560 | unverified | Cross-referenced with transactions |
| meridian supply | Atlantic Versorgung GmbH | auto_generated | Verified via product specs |
| dextrin premium | LA-AC-GR-A-949 | unverified | Auto-mapped, validated |
| SIG-88-EEY-HOGD | SO-BE-50-427 | auto_generated | Confirmed by domain expert |
| PA-OI-98-856 | Natriumbenzoat Qualitätsstufe II | pending_review | Cross-referenced with transactions |
| CO-SU-CO-635 | quantum materials | auto_generated | Verified via product specs |
| Stratos Ingredients Group | ME-MA-156 Corp. | unverified | Historical match confirmed |
| HO-PA-149 International | Stellar Manufacturing Group | pending_review | Confirmed by domain expert |
| VA-MA-502 | SIG-13-PHC-GSY7 | unverified | Auto-mapped, validated |
| Isoglucose | rapeseed oil 99.5% | auto_generated | Cross-referenced with transactions |
| Stellar Versorgung NV | prime commodities | pending_review | Verified via product specs |
| SIG-41-SWO-23GD | glucose syrup tech grade | auto_generated | Confirmed by domain expert |
| glucose syrup | SIG-66-FRL-CVIT | unverified | Auto-mapped, validated |
| nexus supply | ST-LO-637 | auto_generated | Cross-referenced with transactions |
| PR-LO-351 | SIG-74-ZJN-KVHO | unverified | Verified via product specs |
| Premier Versorgung GmbH | SIG-28-STQ-YUPS | unverified | Verified via product specs |
| Citric Acid 50% | SIG-50-SVK-9TOS | pending_review | Cross-referenced with transactions |
| SIG-42-SPP-A6C6 | horizon commodities PLC | unverified | Historical match confirmed |
| maltodextrin de20 | SIG-93-FDC-Q685 | auto_generated | Verified via product specs |
| Weizenklebereiweiß 99.5% Qualitätsstufe I | SIG-34-UJK-TJA6 | auto_generated | Auto-mapped, validated |
| sodium benzoate | Rapsöl 99.5% | pending_review | Verified via product specs |
| Withholding FR 15% | EX-D-7-182 | pending_review | Cross-referenced with transactions |
| CE-MA-604 | SIG-77-WCC-DNFC Holdings | unverified | Historical match confirmed |
| SIG-60-VTH-H7AM | prism materials | auto_generated | Confirmed by domain expert |
| soy isolate premium | SIG-61-XKV-ODPX | unverified | Confirmed by domain expert |
| Rapsöl Technische Qualität | Wheat Gluten 99.5% Grade A | pending_review | Verified via product specs |
| vertex commodities KG | Stratos Trading Holdings | unverified | Verified via product specs |
| Ascorbic Acid | Sodium Benzoate 25% | pending_review | Historical match confirmed |
| ZE-TR-467 AG | SIG-53-OGW-YU4I Ltd. | unverified | Confirmed by domain expert |
| Isoglucose 25% Lebensmittelrein | PE-PR-25-185 | auto_generated | Verified via product specs |
| Vanguard Partners PLC | Apex Chemicals International | unverified | Historical match confirmed |
| PE-PR-163 | fructose tech grade | unverified | Auto-mapped, validated |
| citric acid 70% | SIG-68-TVY-N4XJ | unverified | Cross-referenced with transactions |
| RE-ST-98-445 | Dextrose | pending_review | Historical match confirmed |
| Resistant Starch | PA-OI-399 | pending_review | Historical match confirmed |
| SO-BE-50-TE-276 | SIG-26-ADB-B4F0 | pending_review | Verified via product specs |
| DE-99.5-720 | SIG-31-XRN-45GD | pending_review | Historical match confirmed |
| PR-LO-104 KG | Global Solutions International | pending_review | Auto-mapped, validated |
| atlantic commodities | Zenith Partners LLC | unverified | Auto-mapped, validated |
| Coconut Oil 25% Food Grade | Lactic Acid Standardqualität | pending_review | Verified via product specs |
| Rapsöl Qualitätsstufe I | DE-25-260 | unverified | Cross-referenced with transactions |
| SIG-47-HPA-L2FX | Rapsöl Qualitätsstufe I | auto_generated | Verified via product specs |
| Ascorbic Acid Premiumqualität | CA-CA-50-260 | pending_review | Auto-mapped, validated |
| SIG-72-OHB-75ML SAS | Apex Chemicals | auto_generated | Historical match confirmed |
| SIG-58-LVK-OFDU KG | CO-CH-610 | pending_review | Confirmed by domain expert |
| Resistant Starch Technical | Maltodextrin-Pulver DE25 | pending_review | Confirmed by domain expert |
| Ascorbic Acid 50% | SIG-20-XSP-FVHF | auto_generated | Cross-referenced with transactions |
| EL-SO-199 | SIG-86-EKJ-RFVB | pending_review | Confirmed by domain expert |
| Ascorbic Acid | SIG-42-BEO-614U | unverified | Cross-referenced with transactions |
| CI-AC-GR-B-103 | Maltodextrin-Pulver DE10 | unverified | Auto-mapped, validated |
| Maltodextrin DE20 | SIG-73-KLZ-PDKU | pending_review | Verified via product specs |
| SIG-83-CDB-3QOI | Stellar Sourcing | pending_review | Auto-mapped, validated |
| Vanguard Logistics SARL | SIG-13-QNH-MZKO SAS | unverified | Cross-referenced with transactions |
| elite trading Ltd. | Nexus Enterprise Group | auto_generated | Historical match confirmed |
| SIG-92-KFT-DU1S | Vat Standard BR 0% | pending_review | Cross-referenced with transactions |
| SIG-11-SLQ-KF5B | Natriumchlorid 25% Premiumqualität | unverified | Cross-referenced with transactions |
| Continental Enterprise GmbH | Apex Processing | pending_review | Verified via product specs |
| PA-OI-GR-B-326 | SIG-47-AWI-4RQV | pending_review | Auto-mapped, validated |
| CO-SU-CO-635 | Global Werkstoffe | pending_review | Cross-referenced with transactions |
| rapeseed oil | LA-AC-FO-GR-469 | unverified | Cross-referenced with transactions |
| VA-RE-B-10-482 | Withholding NL 7% | auto_generated | Confirmed by domain expert |
| Prism Materials International | meridian distribution Group | auto_generated | Confirmed by domain expert |
| sodium benzoate | SIG-23-BLM-EZKX | pending_review | Historical match confirmed |
| FR-278 | Fructose 50% Standard | pending_review | Confirmed by domain expert |

#### 4.3.3 Excluded Mappings

The following mappings were identified but NOT migrated due to data quality issues:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-7935-E | Invalid Entry 702 | Data quality insufficient |
| NOISE-1709-A | Invalid Entry 963 | Duplicate detected |
| NOISE-8651-A | Invalid Entry 484 | Pending validation |
| NOISE-2899-E | Invalid Entry 965 | Out of scope per business decision |
| NOISE-9021-B | Invalid Entry 426 | Duplicate detected |
| NOISE-5126-C | Invalid Entry 371 | Data quality insufficient |
| NOISE-1304-A | Invalid Entry 549 | Data quality insufficient |
| NOISE-3091-E | Invalid Entry 604 | Superseded by newer mapping |
| NOISE-4225-D | Invalid Entry 963 | Out of scope per business decision |
| NOISE-2011-C | Invalid Entry 981 | Pending validation |
| NOISE-5213-G | Invalid Entry 565 | Out of scope per business decision |
| NOISE-2079-E | Invalid Entry 868 | Data quality insufficient |
| NOISE-2036-H | Invalid Entry 424 | Pending validation |
| NOISE-7122-H | Invalid Entry 383 | Duplicate detected |
| NOISE-3345-G | Invalid Entry 884 | Duplicate detected |
| NOISE-8276-E | Invalid Entry 376 | Pending validation |
| NOISE-9607-G | Invalid Entry 656 | Pending validation |
| NOISE-1029-G | Invalid Entry 189 | Out of scope per business decision |
| NOISE-1305-C | Invalid Entry 244 | Data quality insufficient |
| NOISE-3874-F | Invalid Entry 416 | Out of scope per business decision |
| NOISE-6608-E | Invalid Entry 672 | Superseded by newer mapping |
| NOISE-9948-H | Invalid Entry 657 | Data quality insufficient |
| NOISE-7549-A | Invalid Entry 888 | Duplicate detected |
| NOISE-3212-B | Invalid Entry 906 | Pending validation |
| NOISE-9123-G | Invalid Entry 593 | Out of scope per business decision |
| NOISE-4246-A | Invalid Entry 263 | Out of scope per business decision |
| NOISE-8742-C | Invalid Entry 557 | Pending validation |
| NOISE-6566-B | Invalid Entry 504 | Out of scope per business decision |
| NOISE-5551-D | Invalid Entry 914 | Duplicate detected |
| NOISE-8437-C | Invalid Entry 587 | Out of scope per business decision |
| NOISE-2152-H | Invalid Entry 296 | Pending validation |
| NOISE-6832-F | Invalid Entry 615 | Out of scope per business decision |
| NOISE-5800-F | Invalid Entry 542 | Superseded by newer mapping |
| NOISE-2316-F | Invalid Entry 732 | Pending validation |
| NOISE-4216-C | Invalid Entry 911 | Superseded by newer mapping |
| NOISE-6008-G | Invalid Entry 337 | Out of scope per business decision |
| NOISE-8352-C | Invalid Entry 398 | Out of scope per business decision |
| NOISE-6988-C | Invalid Entry 114 | Out of scope per business decision |
| NOISE-4268-D | Invalid Entry 528 | Data quality insufficient |
| NOISE-1543-F | Invalid Entry 305 | Duplicate detected |
| NOISE-8761-E | Invalid Entry 870 | Data quality insufficient |
| NOISE-6328-F | Invalid Entry 849 | Superseded by newer mapping |
| NOISE-5182-B | Invalid Entry 157 | Duplicate detected |
| NOISE-3968-B | Invalid Entry 715 | Duplicate detected |
| NOISE-4099-B | Invalid Entry 183 | Superseded by newer mapping |
| NOISE-2485-D | Invalid Entry 179 | Data quality insufficient |
| NOISE-1581-H | Invalid Entry 382 | Pending validation |
| NOISE-5656-E | Invalid Entry 220 | Superseded by newer mapping |
| NOISE-5834-G | Invalid Entry 463 | Duplicate detected |
| NOISE-6905-D | Invalid Entry 726 | Duplicate detected |
| NOISE-5550-B | Invalid Entry 861 | Out of scope per business decision |
| NOISE-8867-C | Invalid Entry 632 | Pending validation |
| NOISE-5552-H | Invalid Entry 536 | Pending validation |
| NOISE-9659-E | Invalid Entry 342 | Out of scope per business decision |
| NOISE-7601-G | Invalid Entry 371 | Pending validation |
| NOISE-4628-H | Invalid Entry 622 | Superseded by newer mapping |
| NOISE-5215-B | Invalid Entry 297 | Duplicate detected |
| NOISE-3610-H | Invalid Entry 545 | Superseded by newer mapping |
| NOISE-7046-D | Invalid Entry 416 | Pending validation |
| NOISE-8998-H | Invalid Entry 492 | Out of scope per business decision |
| NOISE-5118-B | Invalid Entry 495 | Out of scope per business decision |
| NOISE-8443-D | Invalid Entry 470 | Duplicate detected |
| NOISE-6959-G | Invalid Entry 501 | Pending validation |
| NOISE-1701-B | Invalid Entry 906 | Superseded by newer mapping |
| NOISE-6716-H | Invalid Entry 888 | Data quality insufficient |
| NOISE-6155-B | Invalid Entry 643 | Out of scope per business decision |
| NOISE-9668-A | Invalid Entry 952 | Out of scope per business decision |
| NOISE-4154-G | Invalid Entry 398 | Pending validation |
| NOISE-8268-E | Invalid Entry 764 | Superseded by newer mapping |
| NOISE-1378-E | Invalid Entry 122 | Out of scope per business decision |
| NOISE-2472-F | Invalid Entry 654 | Superseded by newer mapping |
| NOISE-6916-H | Invalid Entry 773 | Data quality insufficient |
| NOISE-6521-H | Invalid Entry 320 | Out of scope per business decision |
| NOISE-5533-E | Invalid Entry 144 | Pending validation |
| NOISE-6765-C | Invalid Entry 677 | Superseded by newer mapping |
| NOISE-6084-D | Invalid Entry 272 | Duplicate detected |
| NOISE-2320-D | Invalid Entry 940 | Duplicate detected |
| NOISE-1262-D | Invalid Entry 521 | Superseded by newer mapping |
| NOISE-6178-A | Invalid Entry 950 | Superseded by newer mapping |
| NOISE-1741-B | Invalid Entry 414 | Data quality insufficient |
| NOISE-4867-F | Invalid Entry 930 | Superseded by newer mapping |
| NOISE-3355-A | Invalid Entry 852 | Data quality insufficient |
| NOISE-3530-C | Invalid Entry 972 | Duplicate detected |
| NOISE-5247-B | Invalid Entry 905 | Data quality insufficient |
| NOISE-7734-H | Invalid Entry 340 | Superseded by newer mapping |
| NOISE-8543-C | Invalid Entry 976 | Superseded by newer mapping |
| NOISE-7991-A | Invalid Entry 865 | Data quality insufficient |
| NOISE-7292-G | Invalid Entry 842 | Duplicate detected |
| NOISE-8725-C | Invalid Entry 222 | Superseded by newer mapping |
| NOISE-6805-B | Invalid Entry 873 | Duplicate detected |
| NOISE-7109-A | Invalid Entry 426 | Pending validation |
| NOISE-4203-C | Invalid Entry 891 | Pending validation |
| NOISE-8918-B | Invalid Entry 493 | Duplicate detected |
| NOISE-7362-F | Invalid Entry 408 | Superseded by newer mapping |
| NOISE-8445-B | Invalid Entry 150 | Out of scope per business decision |
| NOISE-1166-B | Invalid Entry 931 | Pending validation |
| NOISE-7616-D | Invalid Entry 638 | Data quality insufficient |
| NOISE-2479-C | Invalid Entry 237 | Out of scope per business decision |
| NOISE-9449-H | Invalid Entry 851 | Duplicate detected |
| NOISE-6546-F | Invalid Entry 688 | Duplicate detected |
| NOISE-5968-H | Invalid Entry 283 | Pending validation |
| NOISE-8759-B | Invalid Entry 281 | Pending validation |
| NOISE-4916-D | Invalid Entry 517 | Data quality insufficient |
| NOISE-1669-G | Invalid Entry 782 | Duplicate detected |
| NOISE-7613-C | Invalid Entry 254 | Data quality insufficient |
| NOISE-4645-H | Invalid Entry 328 | Pending validation |
| NOISE-2488-B | Invalid Entry 458 | Out of scope per business decision |
| NOISE-5547-D | Invalid Entry 600 | Out of scope per business decision |
| NOISE-4976-A | Invalid Entry 627 | Superseded by newer mapping |
| NOISE-5668-C | Invalid Entry 986 | Pending validation |
| NOISE-2223-G | Invalid Entry 347 | Superseded by newer mapping |
| NOISE-8212-F | Invalid Entry 393 | Out of scope per business decision |
| NOISE-9390-F | Invalid Entry 407 | Pending validation |
| NOISE-3380-B | Invalid Entry 275 | Data quality insufficient |
| NOISE-2029-E | Invalid Entry 902 | Data quality insufficient |
| NOISE-8424-B | Invalid Entry 732 | Data quality insufficient |
| NOISE-6608-E | Invalid Entry 945 | Pending validation |
| NOISE-4711-G | Invalid Entry 196 | Duplicate detected |
| NOISE-4854-G | Invalid Entry 638 | Duplicate detected |
| NOISE-3958-A | Invalid Entry 167 | Duplicate detected |
| NOISE-4757-G | Invalid Entry 401 | Pending validation |
| NOISE-4210-A | Invalid Entry 802 | Data quality insufficient |
| NOISE-8848-A | Invalid Entry 426 | Data quality insufficient |
| NOISE-4129-B | Invalid Entry 298 | Pending validation |
| NOISE-8799-B | Invalid Entry 407 | Superseded by newer mapping |
| NOISE-8848-A | Invalid Entry 365 | Out of scope per business decision |
| NOISE-5690-C | Invalid Entry 564 | Out of scope per business decision |
| NOISE-9150-E | Invalid Entry 528 | Superseded by newer mapping |
| NOISE-8133-D | Invalid Entry 698 | Data quality insufficient |
| NOISE-9864-H | Invalid Entry 561 | Duplicate detected |
| NOISE-5782-H | Invalid Entry 463 | Data quality insufficient |
| NOISE-7821-D | Invalid Entry 364 | Pending validation |
| NOISE-8101-D | Invalid Entry 546 | Superseded by newer mapping |
| NOISE-5195-D | Invalid Entry 892 | Pending validation |
| NOISE-6968-A | Invalid Entry 547 | Duplicate detected |
| NOISE-5980-H | Invalid Entry 983 | Out of scope per business decision |
| NOISE-1335-F | Invalid Entry 884 | Duplicate detected |
| NOISE-7193-H | Invalid Entry 802 | Pending validation |
| NOISE-8280-F | Invalid Entry 848 | Superseded by newer mapping |
| NOISE-8809-C | Invalid Entry 928 | Out of scope per business decision |
| NOISE-2037-C | Invalid Entry 304 | Out of scope per business decision |
| NOISE-9818-E | Invalid Entry 394 | Out of scope per business decision |
| NOISE-8691-D | Invalid Entry 207 | Out of scope per business decision |
| NOISE-4734-F | Invalid Entry 744 | Out of scope per business decision |
| NOISE-8743-H | Invalid Entry 155 | Out of scope per business decision |
| NOISE-2541-F | Invalid Entry 739 | Pending validation |
| NOISE-9613-A | Invalid Entry 711 | Out of scope per business decision |
| NOISE-1066-E | Invalid Entry 431 | Data quality insufficient |
| NOISE-7011-E | Invalid Entry 793 | Out of scope per business decision |
| NOISE-9686-B | Invalid Entry 644 | Data quality insufficient |
| NOISE-7196-G | Invalid Entry 104 | Data quality insufficient |
| NOISE-6577-D | Invalid Entry 603 | Pending validation |
| NOISE-7433-F | Invalid Entry 189 | Out of scope per business decision |
| NOISE-5746-F | Invalid Entry 428 | Data quality insufficient |
| NOISE-5785-D | Invalid Entry 878 | Superseded by newer mapping |
| NOISE-8914-H | Invalid Entry 572 | Pending validation |
| NOISE-5716-B | Invalid Entry 827 | Superseded by newer mapping |
| NOISE-1651-E | Invalid Entry 107 | Duplicate detected |
| NOISE-5470-E | Invalid Entry 659 | Duplicate detected |
| NOISE-5017-F | Invalid Entry 314 | Duplicate detected |
| NOISE-1631-G | Invalid Entry 189 | Superseded by newer mapping |
| NOISE-5354-C | Invalid Entry 421 | Pending validation |
| NOISE-2183-C | Invalid Entry 272 | Out of scope per business decision |
| NOISE-8801-B | Invalid Entry 275 | Superseded by newer mapping |
| NOISE-7388-E | Invalid Entry 834 | Data quality insufficient |
| NOISE-6826-G | Invalid Entry 871 | Duplicate detected |
| NOISE-5552-H | Invalid Entry 354 | Superseded by newer mapping |
| NOISE-6689-C | Invalid Entry 398 | Data quality insufficient |
| NOISE-3375-B | Invalid Entry 383 | Data quality insufficient |
| NOISE-2031-A | Invalid Entry 203 | Pending validation |
| NOISE-4080-E | Invalid Entry 996 | Out of scope per business decision |
| NOISE-5667-E | Invalid Entry 383 | Duplicate detected |
| NOISE-4944-B | Invalid Entry 137 | Data quality insufficient |
| NOISE-4423-A | Invalid Entry 335 | Out of scope per business decision |
| NOISE-9133-C | Invalid Entry 141 | Duplicate detected |
| NOISE-3469-D | Invalid Entry 718 | Superseded by newer mapping |
| NOISE-5578-E | Invalid Entry 284 | Data quality insufficient |
| NOISE-6466-A | Invalid Entry 437 | Data quality insufficient |
| NOISE-4052-C | Invalid Entry 531 | Duplicate detected |
| NOISE-1736-F | Invalid Entry 872 | Out of scope per business decision |
| NOISE-8439-D | Invalid Entry 368 | Out of scope per business decision |
| NOISE-8538-D | Invalid Entry 885 | Out of scope per business decision |
| NOISE-7147-F | Invalid Entry 350 | Superseded by newer mapping |
| NOISE-4376-C | Invalid Entry 342 | Data quality insufficient |
| NOISE-3661-C | Invalid Entry 981 | Data quality insufficient |
| NOISE-8895-A | Invalid Entry 716 | Pending validation |
| NOISE-2502-D | Invalid Entry 129 | Superseded by newer mapping |
| NOISE-4778-B | Invalid Entry 558 | Data quality insufficient |
| NOISE-7143-E | Invalid Entry 381 | Out of scope per business decision |
| NOISE-4369-H | Invalid Entry 913 | Out of scope per business decision |
| NOISE-6978-F | Invalid Entry 928 | Duplicate detected |
| NOISE-2103-G | Invalid Entry 292 | Superseded by newer mapping |
| NOISE-3138-B | Invalid Entry 902 | Data quality insufficient |
| NOISE-7609-E | Invalid Entry 243 | Data quality insufficient |
| NOISE-5408-C | Invalid Entry 231 | Duplicate detected |
| NOISE-8899-B | Invalid Entry 748 | Data quality insufficient |
| NOISE-3368-D | Invalid Entry 350 | Data quality insufficient |
| NOISE-6824-F | Invalid Entry 698 | Duplicate detected |
| NOISE-9425-B | Invalid Entry 367 | Duplicate detected |
| NOISE-9843-F | Invalid Entry 460 | Data quality insufficient |
| NOISE-3507-H | Invalid Entry 329 | Pending validation |
| NOISE-7831-A | Invalid Entry 795 | Superseded by newer mapping |
| NOISE-1956-E | Invalid Entry 857 | Pending validation |
| NOISE-7031-B | Invalid Entry 432 | Out of scope per business decision |
| NOISE-9581-C | Invalid Entry 882 | Superseded by newer mapping |
| NOISE-6005-A | Invalid Entry 455 | Duplicate detected |
| NOISE-7831-D | Invalid Entry 959 | Superseded by newer mapping |
| NOISE-5750-C | Invalid Entry 110 | Duplicate detected |
| NOISE-4305-A | Invalid Entry 811 | Superseded by newer mapping |
| NOISE-1550-B | Invalid Entry 190 | Out of scope per business decision |
| NOISE-7605-A | Invalid Entry 248 | Superseded by newer mapping |
| NOISE-5520-E | Invalid Entry 526 | Pending validation |
| NOISE-5710-G | Invalid Entry 739 | Out of scope per business decision |
| NOISE-7787-A | Invalid Entry 412 | Pending validation |
| NOISE-9449-B | Invalid Entry 580 | Pending validation |
| NOISE-9698-F | Invalid Entry 636 | Data quality insufficient |
| NOISE-2583-F | Invalid Entry 275 | Pending validation |
| NOISE-9870-H | Invalid Entry 226 | Superseded by newer mapping |
| NOISE-7777-G | Invalid Entry 157 | Duplicate detected |
| NOISE-9119-G | Invalid Entry 929 | Duplicate detected |
| NOISE-9057-G | Invalid Entry 764 | Duplicate detected |
| NOISE-7371-D | Invalid Entry 150 | Duplicate detected |
| NOISE-9224-A | Invalid Entry 896 | Superseded by newer mapping |
| NOISE-2451-C | Invalid Entry 445 | Data quality insufficient |
| NOISE-9534-G | Invalid Entry 166 | Superseded by newer mapping |
| NOISE-3423-D | Invalid Entry 799 | Superseded by newer mapping |
| NOISE-6300-B | Invalid Entry 272 | Duplicate detected |
| NOISE-1434-D | Invalid Entry 586 | Data quality insufficient |
| NOISE-5493-B | Invalid Entry 116 | Pending validation |
| NOISE-3944-D | Invalid Entry 480 | Data quality insufficient |
| NOISE-3768-G | Invalid Entry 611 | Duplicate detected |
| NOISE-1560-F | Invalid Entry 513 | Superseded by newer mapping |
| NOISE-7179-E | Invalid Entry 566 | Superseded by newer mapping |
| NOISE-8802-E | Invalid Entry 661 | Data quality insufficient |
| NOISE-4241-B | Invalid Entry 710 | Duplicate detected |
| NOISE-1726-A | Invalid Entry 959 | Out of scope per business decision |
| NOISE-1621-C | Invalid Entry 882 | Duplicate detected |
| NOISE-4197-H | Invalid Entry 652 | Data quality insufficient |
| NOISE-7864-B | Invalid Entry 158 | Superseded by newer mapping |
| NOISE-3103-E | Invalid Entry 855 | Out of scope per business decision |
| NOISE-3693-E | Invalid Entry 939 | Pending validation |
| NOISE-2899-B | Invalid Entry 130 | Out of scope per business decision |
| NOISE-3218-E | Invalid Entry 529 | Data quality insufficient |
| NOISE-6908-G | Invalid Entry 327 | Superseded by newer mapping |
| NOISE-9321-A | Invalid Entry 862 | Duplicate detected |
| NOISE-1555-F | Invalid Entry 706 | Superseded by newer mapping |
| NOISE-2236-H | Invalid Entry 751 | Data quality insufficient |
| NOISE-4826-F | Invalid Entry 800 | Duplicate detected |
| NOISE-1368-G | Invalid Entry 642 | Duplicate detected |
| NOISE-9511-A | Invalid Entry 794 | Out of scope per business decision |
| NOISE-2404-H | Invalid Entry 849 | Pending validation |
| NOISE-9291-H | Invalid Entry 628 | Duplicate detected |
| NOISE-1405-D | Invalid Entry 133 | Pending validation |
| NOISE-9354-C | Invalid Entry 336 | Pending validation |
| NOISE-9242-B | Invalid Entry 823 | Data quality insufficient |
| NOISE-2319-A | Invalid Entry 270 | Pending validation |
| NOISE-1993-C | Invalid Entry 538 | Superseded by newer mapping |
| NOISE-3722-H | Invalid Entry 525 | Out of scope per business decision |
| NOISE-7975-E | Invalid Entry 376 | Superseded by newer mapping |
| NOISE-1388-D | Invalid Entry 297 | Duplicate detected |
| NOISE-4795-H | Invalid Entry 378 | Duplicate detected |
| NOISE-9313-G | Invalid Entry 829 | Pending validation |
| NOISE-7091-F | Invalid Entry 991 | Pending validation |
| NOISE-1024-H | Invalid Entry 502 | Duplicate detected |
| NOISE-3580-C | Invalid Entry 555 | Superseded by newer mapping |
| NOISE-6154-H | Invalid Entry 234 | Out of scope per business decision |
| NOISE-1124-C | Invalid Entry 744 | Pending validation |
| NOISE-3089-C | Invalid Entry 239 | Pending validation |
| NOISE-1163-H | Invalid Entry 289 | Out of scope per business decision |
| NOISE-1851-B | Invalid Entry 780 | Superseded by newer mapping |
| NOISE-4003-H | Invalid Entry 654 | Out of scope per business decision |
| NOISE-6946-E | Invalid Entry 596 | Pending validation |
| NOISE-1731-E | Invalid Entry 863 | Out of scope per business decision |
| NOISE-9927-E | Invalid Entry 954 | Data quality insufficient |
| NOISE-7177-G | Invalid Entry 803 | Duplicate detected |
| NOISE-1574-F | Invalid Entry 399 | Pending validation |
| NOISE-1864-H | Invalid Entry 177 | Duplicate detected |
| NOISE-3684-B | Invalid Entry 252 | Data quality insufficient |
| NOISE-7758-B | Invalid Entry 398 | Data quality insufficient |
| NOISE-4372-C | Invalid Entry 244 | Superseded by newer mapping |
| NOISE-8120-H | Invalid Entry 105 | Data quality insufficient |
| NOISE-7438-A | Invalid Entry 554 | Out of scope per business decision |
| NOISE-5206-A | Invalid Entry 457 | Out of scope per business decision |
| NOISE-4685-C | Invalid Entry 562 | Superseded by newer mapping |
| NOISE-3872-H | Invalid Entry 846 | Duplicate detected |
| NOISE-7234-D | Invalid Entry 928 | Duplicate detected |
| NOISE-5262-H | Invalid Entry 742 | Duplicate detected |
| NOISE-8556-F | Invalid Entry 110 | Pending validation |
| NOISE-8420-C | Invalid Entry 236 | Out of scope per business decision |
| NOISE-4296-D | Invalid Entry 846 | Out of scope per business decision |
| NOISE-7446-F | Invalid Entry 212 | Duplicate detected |
| NOISE-1863-F | Invalid Entry 766 | Duplicate detected |
| NOISE-3377-A | Invalid Entry 555 | Pending validation |
| NOISE-3672-E | Invalid Entry 421 | Duplicate detected |
| NOISE-4262-H | Invalid Entry 992 | Data quality insufficient |
| NOISE-1346-D | Invalid Entry 779 | Data quality insufficient |
| NOISE-3811-E | Invalid Entry 203 | Pending validation |
| NOISE-6628-H | Invalid Entry 844 | Pending validation |
| NOISE-2553-B | Invalid Entry 321 | Superseded by newer mapping |
| NOISE-8425-F | Invalid Entry 617 | Out of scope per business decision |
| NOISE-6800-F | Invalid Entry 635 | Superseded by newer mapping |
| NOISE-6622-C | Invalid Entry 782 | Out of scope per business decision |
| NOISE-6484-E | Invalid Entry 636 | Pending validation |
| NOISE-8595-F | Invalid Entry 217 | Superseded by newer mapping |
| NOISE-3979-F | Invalid Entry 458 | Pending validation |
| NOISE-8033-D | Invalid Entry 244 | Duplicate detected |
| NOISE-5705-C | Invalid Entry 721 | Duplicate detected |
| NOISE-5828-F | Invalid Entry 882 | Pending validation |
| NOISE-3536-A | Invalid Entry 645 | Duplicate detected |
| NOISE-6591-C | Invalid Entry 128 | Duplicate detected |
| NOISE-6916-C | Invalid Entry 672 | Out of scope per business decision |
| NOISE-8276-H | Invalid Entry 712 | Data quality insufficient |
| NOISE-7684-G | Invalid Entry 731 | Out of scope per business decision |
| NOISE-7645-C | Invalid Entry 211 | Out of scope per business decision |
| NOISE-1593-H | Invalid Entry 593 | Superseded by newer mapping |
| NOISE-5810-B | Invalid Entry 583 | Out of scope per business decision |
| NOISE-5892-B | Invalid Entry 416 | Out of scope per business decision |
| NOISE-6283-G | Invalid Entry 285 | Pending validation |
| NOISE-2448-G | Invalid Entry 418 | Pending validation |
| NOISE-5097-D | Invalid Entry 649 | Duplicate detected |
| NOISE-8333-C | Invalid Entry 514 | Out of scope per business decision |
| NOISE-9008-D | Invalid Entry 745 | Data quality insufficient |
| NOISE-6925-F | Invalid Entry 259 | Out of scope per business decision |

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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230607_000000`
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
| Project Lead | Michael Weber (Business Operations) | michael@company.com | +1-555-0101 |
| Technical Lead | Sarah Chen (Data Governance) | sarah@company.com | +1-555-0102 |
| Business Owner | James Wilson (Finance) | james@company.com | +1-555-0103 |
| Data Steward | David Kim (Project Management) | david@company.com | +1-555-0104 |

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
