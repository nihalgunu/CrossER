# Migration Runbook: Legacy SIGMA System Decommission

**Document ID**: RB-SIGMA_DECOMMISSION_2023-2679
**Version**: 2.5
**Last Updated**: 2023-08-13
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the Legacy SIGMA System Decommission project.
The migration involves transitioning master data and transactional records from LEGACY_SIGMA
to ERP_ALPHA while maintaining data integrity and business continuity.

**Project Timeline**: 2023-06-13 to 2023-09-25
**Business Sponsor**: Global Data Governance
**Technical Owner**: IT Infrastructure

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
|   LEGACY_SIGMA       |     |   ETL Layer      |     |   ERP_ALPHA       |
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
LEGACY_SIGMA to ERP_ALPHA. All mappings have been validated by the
data stewardship team unless otherwise noted.

### 4.2 Migration Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1473 | Completed |
| Successfully mapped | 988 | Verified |
| Excluded from scope | 296 | Documented |
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

| Source Code (LEGACY_SIGMA) | Target Code (ERP_ALPHA) | Verification | Notes |
|------------------------------|------------------------------|--------------|-------|
| SIG-30-PVA-ZMF8 | Sodium Chloride 70% Grade B | data_steward | Cross-referenced with transactions |
| SIG-44-SRN-1MKF | Fructose Grade A | data_steward | Historical match confirmed |
| SIG-41-SWO-23GD | Resistant Starch | domain_expert | Verified via product specs |
| SIG-79-HZP-CLBR | Casein 25% Pharma Grade | data_steward | Verified via product specs |
| SIG-29-CYR-T4UF | Ascorbic Acid | data_steward | Verified via product specs |
| SIG-16-QDM-JLQM | Sunflower Oil 98% Premium | data_steward | Confirmed by domain expert |
| SIG-41-LTG-3D5I | Cyclodextrin | system_admin | Confirmed by domain expert |
| SIG-56-ZVH-GATJ | Pea Protein 99.5% | data_steward | Cross-referenced with transactions |
| SIG-48-UJX-49KW | Ascorbic Acid Grade B | system_admin | Cross-referenced with transactions |
| SIG-44-MHK-SRCB | Lactic Acid | system_admin | Verified via product specs |
| SIG-74-HUK-JA04 | Ascorbic Acid Standard | data_steward | Cross-referenced with transactions |
| SIG-95-GQL-A26Y | Citric Acid 70% | domain_expert | Confirmed by domain expert |
| SIG-71-VGV-8K52 | Ascorbic Acid Pharma Grade | data_steward | Cross-referenced with transactions |
| SIG-86-VGU-A4FE | Coconut Oil Food Grade | system_admin | Historical match confirmed |
| SIG-61-XKV-ODPX | Palm Oil 98% | data_steward | Confirmed by domain expert |
| SIG-53-AHT-MGFX | Rapeseed Oil | data_steward | Historical match confirmed |
| SIG-26-DML-NZS4 | Dextrose Food Grade | domain_expert | Cross-referenced with transactions |
| SIG-51-LVQ-VS8Q | Wheat Gluten 98% Premium | system_admin | Auto-mapped, validated |
| SIG-37-NAI-M1G9 | Sodium Benzoate 25% Standard | system_admin | Verified via product specs |
| SIG-57-NGZ-ILDZ | Coconut Oil | domain_expert | Confirmed by domain expert |
| SIG-50-FUX-7S9T | Coconut Oil 98% | system_admin | Historical match confirmed |
| SIG-13-JUR-FV2B | Sodium Benzoate 99.5% Grade A | data_steward | Auto-mapped, validated |
| SIG-92-VAB-1JHU | Cyclodextrin 98% Pharma Grade | data_steward | Auto-mapped, validated |
| SIG-52-NBD-2SF6 | Coconut Oil Grade A | data_steward | Confirmed by domain expert |
| SIG-45-IJY-KUT6 | Dextrose Standard | domain_expert | Confirmed by domain expert |
| SIG-60-WEX-2G05 | Lactic Acid 99.5% Grade B | domain_expert | Auto-mapped, validated |
| SIG-68-CNV-EOUU | Lactic Acid | system_admin | Verified via product specs |
| SIG-24-LEE-BXW7 | Coconut Oil 99.5% Pharma Grade | system_admin | Verified via product specs |
| SIG-32-BYW-WPR9 | Potassium Sorbate | domain_expert | Historical match confirmed |
| SIG-12-ANK-TJ9A | Sodium Benzoate 99.5% | data_steward | Verified via product specs |
| SIG-10-TIC-7Q1D | Wheat Gluten | data_steward | Auto-mapped, validated |
| SIG-76-CCF-UYHN | Sodium Benzoate Pharma Grade | domain_expert | Auto-mapped, validated |
| SIG-66-LJV-5E3H | Isoglucose | domain_expert | Cross-referenced with transactions |
| SIG-37-PEJ-WFOY | Soy Isolate 70% | domain_expert | Auto-mapped, validated |
| SIG-50-NZZ-E4UN | Soy Isolate 25% Technical | domain_expert | Verified via product specs |
| SIG-79-ZUT-1IAO | Fructose | data_steward | Historical match confirmed |
| SIG-73-YLS-BYGH | Rapeseed Oil | system_admin | Cross-referenced with transactions |
| SIG-19-HIY-M5FC | Glucose Syrup | domain_expert | Verified via product specs |
| SIG-22-VQM-AGKC | Sorbic Acid 25% Grade B | domain_expert | Historical match confirmed |
| SIG-22-DOP-7UDK | Resistant Starch Pharma Grade | system_admin | Verified via product specs |
| SIG-57-QDA-RQ8R | Casein Standard | domain_expert | Cross-referenced with transactions |
| SIG-44-HRR-WZP6 | Sodium Chloride 70% | data_steward | Auto-mapped, validated |
| SIG-16-LZG-DGBK | Casein 25% Grade B | domain_expert | Cross-referenced with transactions |
| SIG-13-EJJ-5506 | Calcium Carbonate 98% | system_admin | Auto-mapped, validated |
| SIG-83-KGL-Q4QE | Sodium Benzoate 99.5% | domain_expert | Cross-referenced with transactions |
| SIG-35-SYQ-HZY7 | Palm Oil Standard | data_steward | Confirmed by domain expert |
| SIG-58-EEN-BKJF | Maltodextrin DE5 Grade A | data_steward | Verified via product specs |
| SIG-19-TPS-MSKY | Sorbic Acid Food Grade | domain_expert | Verified via product specs |
| SIG-80-EUW-QTKC | Lactic Acid 98% | data_steward | Confirmed by domain expert |
| SIG-85-SIL-CNEA | Citric Acid | domain_expert | Auto-mapped, validated |
| SIG-60-GHI-04X0 | Citric Acid Pharma Grade | data_steward | Verified via product specs |
| SIG-94-QLF-7SH2 | Soy Isolate 99.5% Standard | data_steward | Confirmed by domain expert |
| SIG-39-GGG-HIWF | Palm Oil 98% | system_admin | Verified via product specs |
| SIG-98-OOK-FHJ4 | Sunflower Oil 50% Grade A | data_steward | Historical match confirmed |
| SIG-66-ZOH-E8TV | Sorbic Acid 98% | data_steward | Auto-mapped, validated |
| SIG-76-QBY-ERKM | Resistant Starch 98% Pharma Grade | data_steward | Historical match confirmed |
| SIG-42-AJS-6RPK | Citric Acid 50% Grade A | system_admin | Auto-mapped, validated |
| SIG-36-FSA-X73Q | Maltodextrin DE20 | system_admin | Confirmed by domain expert |
| SIG-83-PHT-N27M | Wheat Gluten Grade B | system_admin | Auto-mapped, validated |
| SIG-60-TMF-XHW0 | Sodium Benzoate | data_steward | Auto-mapped, validated |
| SIG-30-EKM-GB1A | Lactic Acid Food Grade | system_admin | Confirmed by domain expert |
| SIG-66-FRL-CVIT | Dextrin Pharma Grade | domain_expert | Auto-mapped, validated |
| SIG-63-TFP-OMUW | Citric Acid 99.5% | data_steward | Verified via product specs |
| SIG-51-YTN-F537 | Dextrose 25% | domain_expert | Cross-referenced with transactions |
| SIG-46-SVJ-5IZO | Rapeseed Oil Technical | data_steward | Confirmed by domain expert |
| SIG-91-GMY-Q91Y | Citric Acid 99.5% | domain_expert | Cross-referenced with transactions |
| SIG-18-KSV-TA83 | Maltodextrin DE5 Food Grade | data_steward | Confirmed by domain expert |
| SIG-37-ZOD-1VME | Fructose 25% | system_admin | Confirmed by domain expert |
| SIG-72-YEU-SCIQ | Calcium Carbonate 50% Grade B | data_steward | Historical match confirmed |
| SIG-37-CWM-V4K0 | Soy Isolate 25% | data_steward | Historical match confirmed |
| SIG-17-UCW-S6NB | Citric Acid Grade B | system_admin | Auto-mapped, validated |
| SIG-47-SRN-QNYY | Pea Protein Grade A | data_steward | Cross-referenced with transactions |
| SIG-27-RTX-YEAW | Rapeseed Oil 99.5% | data_steward | Confirmed by domain expert |
| SIG-19-BHQ-S1GD | Glucose Syrup 98% Food Grade | system_admin | Auto-mapped, validated |
| SIG-45-ADT-8MFS | Soy Isolate 25% Pharma Grade | domain_expert | Verified via product specs |
| SIG-56-BPD-M0A6 | Coconut Oil 98% Grade A | system_admin | Confirmed by domain expert |
| SIG-40-KVV-E07S | Dextrin 50% | system_admin | Verified via product specs |
| SIG-42-AYY-K71K | Sodium Chloride 98% Grade B | domain_expert | Auto-mapped, validated |
| SIG-37-JLF-9KYP | Soy Isolate 99.5% Premium | data_steward | Historical match confirmed |
| SIG-31-CWE-03UX | Pea Protein Grade B | data_steward | Auto-mapped, validated |
| SIG-36-ZWC-F2K1 | Soy Isolate 98% | domain_expert | Verified via product specs |
| SIG-13-CAZ-HXXP | Soy Isolate 25% | domain_expert | Confirmed by domain expert |
| SIG-65-BAQ-940V | Dextrin | domain_expert | Cross-referenced with transactions |
| SIG-68-SYL-8192 | Wheat Gluten Grade B | system_admin | Auto-mapped, validated |
| SIG-76-YLU-7DL9 | Glucose Syrup 70% | data_steward | Confirmed by domain expert |
| SIG-49-UKY-6H3R | Coconut Oil 50% | system_admin | Historical match confirmed |
| SIG-16-FQO-8S1S | Sunflower Oil Standard | domain_expert | Historical match confirmed |
| SIG-82-TQD-ODWH | Casein Grade A | domain_expert | Historical match confirmed |
| SIG-97-PYI-8W9Z | Ascorbic Acid 99.5% Premium | system_admin | Confirmed by domain expert |
| SIG-78-WDE-NNV9 | Wheat Gluten 50% Pharma Grade | data_steward | Auto-mapped, validated |
| SIG-70-YBK-DUQ6 | Soy Isolate | data_steward | Confirmed by domain expert |
| SIG-45-PNR-H9Q3 | Cyclodextrin Pharma Grade | data_steward | Confirmed by domain expert |
| SIG-25-VPE-TOC1 | Sodium Benzoate Grade A | domain_expert | Cross-referenced with transactions |
| SIG-29-BJH-NXI0 | Potassium Sorbate | data_steward | Cross-referenced with transactions |
| SIG-96-DUH-99Q6 | Sodium Benzoate 25% | system_admin | Auto-mapped, validated |
| SIG-60-IRZ-OTKZ | Casein Premium | domain_expert | Cross-referenced with transactions |
| SIG-48-GDK-Y8XN | Calcium Carbonate Standard | system_admin | Historical match confirmed |
| SIG-98-CGL-FHWJ | Ascorbic Acid Technical | data_steward | Cross-referenced with transactions |
| SIG-53-MEZ-6IT1 | Sodium Chloride | system_admin | Historical match confirmed |
| SIG-41-HMT-W0GK | Casein | system_admin | Auto-mapped, validated |
| SIG-42-BEO-614U | Potassium Sorbate Technical | system_admin | Confirmed by domain expert |
| SIG-59-LNO-OJGF | Glucose Syrup Grade A | system_admin | Confirmed by domain expert |
| SIG-20-OVW-HRUP | Coconut Oil 99.5% Pharma Grade | data_steward | Cross-referenced with transactions |
| SIG-94-JCX-NJ62 | Isoglucose 70% | system_admin | Historical match confirmed |
| SIG-11-SLQ-KF5B | Dextrose Food Grade | domain_expert | Verified via product specs |
| SIG-71-COB-BL7A | Sodium Benzoate | system_admin | Verified via product specs |
| SIG-82-ZPY-WR2F | Palm Oil 50% | data_steward | Verified via product specs |
| SIG-73-AXY-5E8O | Sorbic Acid 70% | system_admin | Confirmed by domain expert |
| SIG-30-LJO-TN4Y | Dextrin Food Grade | data_steward | Confirmed by domain expert |
| SIG-76-AAU-3VM8 | Sodium Chloride Standard | system_admin | Historical match confirmed |
| SIG-58-HNG-1XJ7 | Isoglucose Premium | data_steward | Cross-referenced with transactions |
| SIG-30-MPO-SJEV | Pea Protein Standard | domain_expert | Verified via product specs |
| SIG-55-CTS-U5X0 | Sodium Chloride 25% Premium | data_steward | Historical match confirmed |
| SIG-83-HEH-XF50 | Calcium Carbonate Grade B | domain_expert | Historical match confirmed |
| SIG-66-AQR-B68Q | Fructose Food Grade | system_admin | Cross-referenced with transactions |
| SIG-54-CMF-PK48 | Ascorbic Acid 70% | data_steward | Historical match confirmed |
| SIG-70-IKQ-7KBN | Dextrose 25% Technical | data_steward | Cross-referenced with transactions |
| SIG-27-UKP-V2ME | Isoglucose Food Grade | system_admin | Auto-mapped, validated |
| SIG-85-STS-67D6 | Dextrin 70% | data_steward | Cross-referenced with transactions |
| SIG-72-JEH-P5K7 | Pea Protein 50% | system_admin | Verified via product specs |
| SIG-36-ABO-ZBYW | Citric Acid | system_admin | Verified via product specs |
| SIG-22-TOX-02GV | Sunflower Oil Grade A | system_admin | Cross-referenced with transactions |
| SIG-79-RTU-R8IQ | Lactic Acid 98% Premium | system_admin | Auto-mapped, validated |
| SIG-10-KDB-LGYT | Ascorbic Acid Premium | system_admin | Auto-mapped, validated |
| SIG-88-AGF-FF5L | Glucose Syrup Technical | system_admin | Verified via product specs |
| SIG-25-WDK-CWCD | Rapeseed Oil Technical | data_steward | Auto-mapped, validated |
| SIG-78-AVK-U9PX | Glucose Syrup 98% Standard | system_admin | Historical match confirmed |
| SIG-61-KUY-VFFK | Soy Isolate Grade A | data_steward | Confirmed by domain expert |
| SIG-51-IYK-630P | Isoglucose 50% Technical | data_steward | Historical match confirmed |
| SIG-79-IHV-JKPQ | Rapeseed Oil | system_admin | Verified via product specs |
| SIG-79-OZQ-4I2N | Calcium Carbonate | domain_expert | Auto-mapped, validated |
| SIG-78-YEH-31XY | Sodium Benzoate 99.5% Technical | domain_expert | Cross-referenced with transactions |
| SIG-84-BFP-RD5B | Palm Oil | domain_expert | Confirmed by domain expert |
| SIG-19-QLH-ILRZ | Calcium Carbonate 70% Premium | domain_expert | Cross-referenced with transactions |
| SIG-52-EML-H8JV | Ascorbic Acid Standard | data_steward | Verified via product specs |
| SIG-12-OAV-ALF4 | Citric Acid Food Grade | data_steward | Auto-mapped, validated |
| SIG-58-NYA-2O4M | Soy Isolate Premium | data_steward | Cross-referenced with transactions |
| SIG-21-EAX-PC8Q | Wheat Gluten Grade B | data_steward | Cross-referenced with transactions |
| SIG-39-QZD-93EZ | Glucose Syrup 98% | data_steward | Confirmed by domain expert |
| SIG-29-DTY-HFJL | Rapeseed Oil 70% Premium | data_steward | Confirmed by domain expert |
| SIG-11-RGJ-D3IR | Citric Acid 99.5% | system_admin | Auto-mapped, validated |
| SIG-32-TTU-44MW | Palm Oil | domain_expert | Confirmed by domain expert |
| SIG-21-KSF-Z6X4 | Rapeseed Oil | domain_expert | Cross-referenced with transactions |
| SIG-53-MPZ-77TN | Lactic Acid | domain_expert | Cross-referenced with transactions |
| SIG-47-HDT-7PPC | Palm Oil 98% | data_steward | Verified via product specs |
| SIG-44-FWT-OA3N | Fructose Grade B | domain_expert | Cross-referenced with transactions |
| SIG-35-TKX-8TRE | Ascorbic Acid 70% | data_steward | Auto-mapped, validated |
| SIG-68-PIZ-R6Q5 | Citric Acid | system_admin | Historical match confirmed |
| SIG-16-CAW-LD7M | Lactic Acid 70% Pharma Grade | data_steward | Verified via product specs |
| SIG-43-NCZ-FT9Z | Potassium Sorbate Grade A | domain_expert | Verified via product specs |
| SIG-94-KAU-6F8H | Sodium Chloride | data_steward | Auto-mapped, validated |
| SIG-98-NIJ-5N8C | Fructose | data_steward | Auto-mapped, validated |
| SIG-23-OPT-7QHV | Isoglucose | domain_expert | Confirmed by domain expert |
| SIG-15-QIT-5CZE | Soy Isolate 98% Food Grade | system_admin | Verified via product specs |
| SIG-84-PAS-5S3O | Sodium Benzoate Grade A | system_admin | Confirmed by domain expert |
| SIG-45-ZTJ-PA16 | Ascorbic Acid | data_steward | Cross-referenced with transactions |
| SIG-71-WDX-2GRR | Glucose Syrup 98% Grade A | system_admin | Verified via product specs |
| SIG-33-FUV-53NO | Rapeseed Oil 98% | data_steward | Verified via product specs |
| SIG-44-UIE-SASC | Casein | system_admin | Historical match confirmed |
| SIG-54-LIP-WKBS | Maltodextrin DE10 | data_steward | Verified via product specs |
| SIG-48-LHY-R0O8 | Rapeseed Oil Grade A | system_admin | Cross-referenced with transactions |
| SIG-16-JKI-B4JG | Pea Protein 98% Grade B | system_admin | Confirmed by domain expert |
| SIG-88-XZP-H10B | Calcium Carbonate | data_steward | Confirmed by domain expert |
| SIG-40-NOU-7O0G | Soy Isolate Food Grade | system_admin | Historical match confirmed |
| SIG-34-UJK-TJA6 | Glucose Syrup 70% | system_admin | Cross-referenced with transactions |
| SIG-12-BIH-AKGD | Dextrose Grade A | data_steward | Confirmed by domain expert |
| SIG-56-CMM-ODF7 | Cyclodextrin Food Grade | domain_expert | Auto-mapped, validated |
| SIG-99-OQS-ADHF | Lactic Acid | data_steward | Cross-referenced with transactions |
| SIG-30-RXC-HFDI | Potassium Sorbate | data_steward | Cross-referenced with transactions |
| SIG-51-KQC-QY9M | Coconut Oil Pharma Grade | system_admin | Historical match confirmed |
| SIG-41-OMW-SN1T | Dextrose 25% | system_admin | Confirmed by domain expert |
| SIG-85-FAV-D2EE | Dextrose Grade B | data_steward | Cross-referenced with transactions |
| SIG-49-OHU-U248 | Resistant Starch Grade B | domain_expert | Confirmed by domain expert |
| SIG-75-GUI-J643 | Lactic Acid Grade A | system_admin | Auto-mapped, validated |
| SIG-79-GLV-IEST | Dextrin Grade A | data_steward | Historical match confirmed |
| SIG-88-EEY-HOGD | Citric Acid 99.5% Pharma Grade | system_admin | Auto-mapped, validated |
| SIG-36-BVE-5U7D | Maltodextrin DE10 Premium | domain_expert | Historical match confirmed |
| SIG-47-YTF-UPMT | Maltodextrin DE20 | domain_expert | Cross-referenced with transactions |
| SIG-51-HLJ-TN1E | Fructose Grade A | data_steward | Historical match confirmed |
| SIG-25-ABB-2SBA | Glucose Syrup | domain_expert | Verified via product specs |
| SIG-24-MFK-ZAUG | Citric Acid Premium | domain_expert | Confirmed by domain expert |
| SIG-12-RDG-0JI1 | Isoglucose | data_steward | Confirmed by domain expert |
| SIG-60-QPM-2TRI | Soy Isolate | data_steward | Verified via product specs |
| SIG-99-QXY-X4NT | Potassium Sorbate Standard | data_steward | Auto-mapped, validated |
| SIG-79-SPO-WT80 | Citric Acid | data_steward | Verified via product specs |
| SIG-91-UWU-GPZB | Citric Acid 25% Technical | system_admin | Cross-referenced with transactions |
| SIG-27-WVB-8FZQ | Isoglucose | data_steward | Cross-referenced with transactions |
| SIG-43-GRJ-P3HT | Soy Isolate 50% Grade B | domain_expert | Confirmed by domain expert |
| SIG-36-XEW-9SSB | Pea Protein | system_admin | Cross-referenced with transactions |
| SIG-68-ELC-6AVE | Wheat Gluten Grade A | domain_expert | Confirmed by domain expert |
| SIG-95-LLS-0RNG | Palm Oil 25% Grade A | data_steward | Verified via product specs |
| SIG-16-FVU-3EBQ | Maltodextrin DE18 Pharma Grade | system_admin | Verified via product specs |
| SIG-39-OZI-N968 | Lactic Acid 50% Grade A | domain_expert | Verified via product specs |
| SIG-22-XCC-QSNV | Rapeseed Oil Grade A | domain_expert | Confirmed by domain expert |
| SIG-85-WWC-01LO | Calcium Carbonate 50% Pharma Grade | domain_expert | Verified via product specs |
| SIG-83-BZY-VHAE | Sodium Benzoate 25% Grade B | data_steward | Verified via product specs |
| SIG-63-KXZ-46Q1 | Potassium Sorbate 98% Grade B | domain_expert | Auto-mapped, validated |
| SIG-83-PIY-NKQE | Coconut Oil | data_steward | Verified via product specs |
| SIG-90-SZM-PZJ4 | Sorbic Acid 50% Standard | system_admin | Cross-referenced with transactions |
| SIG-14-MOL-USHF | Citric Acid | data_steward | Confirmed by domain expert |
| SIG-84-VYG-QI55 | Potassium Sorbate | system_admin | Auto-mapped, validated |
| SIG-39-FND-AALU | Citric Acid 70% | system_admin | Historical match confirmed |
| SIG-16-YRD-5C3Z | Maltodextrin DE25 | data_steward | Confirmed by domain expert |
| SIG-84-EIB-2MOT | Soy Isolate | domain_expert | Cross-referenced with transactions |
| SIG-47-LBV-Y27V | Sorbic Acid Food Grade | domain_expert | Confirmed by domain expert |
| SIG-57-HAE-WNSM | Glucose Syrup 98% | system_admin | Cross-referenced with transactions |
| SIG-78-NWO-RO6D | Maltodextrin DE10 | data_steward | Cross-referenced with transactions |
| SIG-80-QNF-AHPO | Dextrin 70% | domain_expert | Historical match confirmed |
| SIG-66-RQA-05UV | Lactic Acid Food Grade | domain_expert | Confirmed by domain expert |
| SIG-47-HPA-L2FX | Ascorbic Acid 98% Pharma Grade | system_admin | Historical match confirmed |
| SIG-57-YOY-F7N2 | Coconut Oil Standard | data_steward | Historical match confirmed |
| SIG-44-QME-TTIM | Fructose Technical | system_admin | Confirmed by domain expert |
| SIG-56-LHF-WMFP | Glucose Syrup 25% | domain_expert | Verified via product specs |
| SIG-34-GNA-EHC2 | Ascorbic Acid | system_admin | Verified via product specs |
| SIG-73-UUF-1F99 | Lactic Acid | system_admin | Historical match confirmed |
| SIG-64-QID-BCT3 | Sodium Benzoate Pharma Grade | data_steward | Auto-mapped, validated |
| SIG-48-IWQ-OJ98 | Sodium Benzoate Grade B | domain_expert | Historical match confirmed |
| SIG-94-MGT-4WYA | Potassium Sorbate Technical | data_steward | Historical match confirmed |
| SIG-40-OEJ-4XCR | Coconut Oil 70% | data_steward | Historical match confirmed |
| SIG-26-PJJ-DUD8 | Soy Isolate 98% Premium | data_steward | Verified via product specs |
| SIG-82-OMQ-EPBO | Sodium Benzoate 99.5% Technical | domain_expert | Verified via product specs |
| SIG-68-VDM-0UT1 | Glucose Syrup | domain_expert | Verified via product specs |
| SIG-61-HXH-PFBC | Maltodextrin DE25 | data_steward | Historical match confirmed |
| SIG-13-WHV-DDIN | Lactic Acid Food Grade | domain_expert | Auto-mapped, validated |
| SIG-47-NVU-R3XU | Casein 98% Grade B | data_steward | Verified via product specs |
| SIG-64-BPY-A8RD | Coconut Oil 25% Grade A | system_admin | Confirmed by domain expert |
| SIG-39-UPB-Q8DA | Sodium Chloride Technical | domain_expert | Confirmed by domain expert |
| SIG-60-ZEV-V2NY | Casein Grade B | domain_expert | Confirmed by domain expert |
| SIG-37-MXA-3C7Q | Palm Oil Grade B | domain_expert | Cross-referenced with transactions |
| SIG-85-VFA-F0TJ | Soy Isolate Standard | system_admin | Historical match confirmed |
| SIG-42-LOE-5XD8 | Sodium Benzoate 50% Technical | system_admin | Confirmed by domain expert |
| SIG-78-OGT-WEKQ | Ascorbic Acid Standard | domain_expert | Historical match confirmed |
| SIG-81-SBE-HL1C | Resistant Starch 70% Technical | system_admin | Confirmed by domain expert |
| SIG-64-LXA-3LJO | Sodium Benzoate 98% Pharma Grade | system_admin | Auto-mapped, validated |
| SIG-24-SWK-GROA | Wheat Gluten 98% | system_admin | Historical match confirmed |
| SIG-47-QLD-IL46 | Potassium Sorbate 50% Technical | system_admin | Confirmed by domain expert |
| SIG-80-PTU-ILTR | Soy Isolate Grade B | data_steward | Verified via product specs |
| SIG-34-IKF-VQJA | Citric Acid 70% Food Grade | domain_expert | Historical match confirmed |
| SIG-92-DNQ-WJAT | Fructose 99.5% Grade A | system_admin | Cross-referenced with transactions |
| SIG-73-WMX-7XJJ | Potassium Sorbate 25% Pharma Grade | data_steward | Verified via product specs |
| SIG-20-UMV-LJM6 | Lactic Acid 50% Premium | data_steward | Verified via product specs |
| SIG-65-XHR-R1SP | Casein 98% Technical | system_admin | Cross-referenced with transactions |
| SIG-99-VAH-2H31 | Sorbic Acid | data_steward | Verified via product specs |
| SIG-71-FNO-CX9K | Rapeseed Oil 50% Food Grade | domain_expert | Verified via product specs |
| SIG-29-KJI-GJKC | Resistant Starch 98% | system_admin | Confirmed by domain expert |
| SIG-86-AKS-BEQE | Lactic Acid Standard | domain_expert | Confirmed by domain expert |
| SIG-67-TPL-WT5F | Wheat Gluten 99.5% Grade A | system_admin | Historical match confirmed |
| SIG-92-ZTO-VZGU | Sodium Benzoate 99.5% Grade A | system_admin | Historical match confirmed |
| SIG-61-IQH-EKWH | Maltodextrin DE10 | system_admin | Historical match confirmed |
| SIG-21-HVD-EZVS | Ascorbic Acid 50% | system_admin | Confirmed by domain expert |
| SIG-36-ZKX-4SE4 | Dextrose Grade A | domain_expert | Historical match confirmed |
| SIG-26-KHF-99OH | Palm Oil 50% | system_admin | Verified via product specs |
| SIG-46-YHU-BU2J | Potassium Sorbate 98% | system_admin | Confirmed by domain expert |
| SIG-36-MYP-7NC2 | Resistant Starch 70% Food Grade | data_steward | Historical match confirmed |
| SIG-80-WEB-2C7R | Ascorbic Acid | domain_expert | Verified via product specs |
| SIG-45-CWR-EI9N | Pea Protein | system_admin | Historical match confirmed |
| SIG-12-NAY-4AKW | Glucose Syrup | data_steward | Auto-mapped, validated |
| SIG-34-JQN-ROWX | Soy Isolate Grade B | domain_expert | Historical match confirmed |
| SIG-27-FHX-VO6Y | Palm Oil 70% Premium | domain_expert | Auto-mapped, validated |
| SIG-53-LJE-NZKR | Lactic Acid Grade B | data_steward | Historical match confirmed |
| SIG-64-VUE-OGQ2 | Lactic Acid 98% | data_steward | Cross-referenced with transactions |
| SIG-77-LFQ-EKT4 | Potassium Sorbate | data_steward | Historical match confirmed |
| SIG-24-CXH-R2TY | Palm Oil Pharma Grade | domain_expert | Confirmed by domain expert |
| SIG-64-TCV-R5SR | Coconut Oil 98% Technical | data_steward | Confirmed by domain expert |
| SIG-39-JMB-X1VA | Casein Grade A | data_steward | Auto-mapped, validated |
| SIG-65-RQH-9Y5B | Coconut Oil 98% | data_steward | Confirmed by domain expert |
| SIG-43-KEL-FPY6 | Dextrose | domain_expert | Verified via product specs |
| SIG-57-RQB-VIKB | Sodium Chloride | system_admin | Cross-referenced with transactions |
| SIG-13-CGO-2Y4L | Isoglucose Technical | data_steward | Cross-referenced with transactions |
| SIG-13-FYG-4NN9 | Calcium Carbonate 70% | domain_expert | Verified via product specs |
| SIG-27-QBE-DEK4 | Palm Oil 99.5% Grade A | system_admin | Auto-mapped, validated |
| SIG-97-LME-ZEH9 | Resistant Starch 50% | data_steward | Verified via product specs |
| SIG-60-KAS-IVMD | Ascorbic Acid Pharma Grade | domain_expert | Verified via product specs |
| SIG-99-GVJ-VPM6 | Resistant Starch Food Grade | system_admin | Cross-referenced with transactions |
| SIG-20-CGL-C8HS | Sorbic Acid 70% | data_steward | Historical match confirmed |
| SIG-68-DWS-MNR6 | Sodium Benzoate Food Grade | domain_expert | Cross-referenced with transactions |
| SIG-86-VCP-SVOL | Sodium Benzoate 70% | domain_expert | Cross-referenced with transactions |
| SIG-80-MLG-VDQ0 | Sorbic Acid Standard | system_admin | Confirmed by domain expert |
| SIG-63-JJG-1TCH | Wheat Gluten 50% | domain_expert | Verified via product specs |
| SIG-78-LTE-H4VL | Wheat Gluten Food Grade | system_admin | Cross-referenced with transactions |
| SIG-50-JOR-LO4P | Dextrose Grade B | system_admin | Verified via product specs |
| SIG-55-DCV-7OXN | Citric Acid 25% | domain_expert | Confirmed by domain expert |
| SIG-20-BPG-W8VL | Pea Protein | system_admin | Verified via product specs |
| SIG-37-WYK-X3LH | Calcium Carbonate 98% | domain_expert | Cross-referenced with transactions |
| SIG-64-LSR-RORA | Casein Grade B | data_steward | Verified via product specs |
| SIG-40-PLP-7A3U | Wheat Gluten Food Grade | data_steward | Confirmed by domain expert |
| SIG-52-FHA-5PI2 | Citric Acid Premium | system_admin | Historical match confirmed |
| SIG-56-SME-QSOD | Ascorbic Acid | data_steward | Verified via product specs |
| SIG-61-MHS-BQG3 | Palm Oil 99.5% | data_steward | Cross-referenced with transactions |
| SIG-23-IEJ-V2T3 | Sodium Benzoate | data_steward | Confirmed by domain expert |
| SIG-12-JLN-YFH3 | Potassium Sorbate 70% | data_steward | Cross-referenced with transactions |
| SIG-83-XMM-APXP | Dextrose Technical | data_steward | Cross-referenced with transactions |
| SIG-89-TVE-WANI | Potassium Sorbate Standard | domain_expert | Verified via product specs |
| SIG-85-FIY-2QW4 | Dextrose Food Grade | data_steward | Cross-referenced with transactions |
| SIG-23-UKD-B8UO | Sodium Benzoate 98% | system_admin | Verified via product specs |
| SIG-63-YJW-AP00 | Fructose 99.5% Technical | domain_expert | Historical match confirmed |
| SIG-76-GDP-2JN8 | Sorbic Acid 50% Grade A | system_admin | Cross-referenced with transactions |
| SIG-24-OUE-RXOK | Sorbic Acid 50% Food Grade | data_steward | Cross-referenced with transactions |
| SIG-26-ADB-B4F0 | Soy Isolate 99.5% | domain_expert | Cross-referenced with transactions |
| SIG-48-ZZX-UQIO | Rapeseed Oil Grade A | system_admin | Auto-mapped, validated |
| SIG-62-GDA-2IVD | Cyclodextrin | system_admin | Auto-mapped, validated |
| SIG-30-UET-0Q2O | Dextrose Standard | domain_expert | Confirmed by domain expert |
| SIG-39-SLB-MLCB | Calcium Carbonate | domain_expert | Auto-mapped, validated |
| SIG-76-RKG-E8RT | Dextrose 99.5% | domain_expert | Confirmed by domain expert |
| SIG-87-YFT-P51V | Sodium Benzoate 98% | system_admin | Auto-mapped, validated |
| SIG-92-CZO-O9ON | Resistant Starch 50% | domain_expert | Historical match confirmed |
| SIG-79-IKL-24HE | Cyclodextrin | system_admin | Confirmed by domain expert |
| SIG-88-VVU-EL88 | Dextrose 70% | data_steward | Auto-mapped, validated |
| SIG-50-XSG-WQVA | Dextrin 70% Pharma Grade | system_admin | Historical match confirmed |
| SIG-82-GZF-51ZF | Fructose 99.5% Technical | system_admin | Auto-mapped, validated |
| SIG-24-VEK-YPIS | Ascorbic Acid Technical | system_admin | Verified via product specs |
| SIG-35-SZU-VMRU | Sunflower Oil Grade B | system_admin | Verified via product specs |
| SIG-24-PBC-613L | Lactic Acid 25% Premium | data_steward | Historical match confirmed |
| SIG-62-BTJ-PQV9 | Dextrose Technical | domain_expert | Cross-referenced with transactions |
| SIG-41-HXT-0U1R | Soy Isolate 50% Food Grade | domain_expert | Cross-referenced with transactions |
| SIG-83-OTU-QZB6 | Dextrin 98% | system_admin | Verified via product specs |
| SIG-66-MYF-XDYQ | Soy Isolate Food Grade | domain_expert | Verified via product specs |
| SIG-63-KMB-9J7M | Isoglucose 70% | domain_expert | Cross-referenced with transactions |
| SIG-16-IYP-EOZP | Calcium Carbonate | system_admin | Confirmed by domain expert |
| SIG-71-CWF-DGP5 | Maltodextrin DE15 | data_steward | Cross-referenced with transactions |
| SIG-27-SJP-0JO4 | Resistant Starch 50% | system_admin | Auto-mapped, validated |
| SIG-88-RKE-8R7A | Fructose 50% Standard | system_admin | Confirmed by domain expert |
| SIG-14-WZC-EEWK | Maltodextrin DE20 | data_steward | Auto-mapped, validated |
| SIG-94-IBE-STPB | Calcium Carbonate 98% | system_admin | Verified via product specs |
| SIG-76-IIX-V2Y9 | Cyclodextrin 70% Food Grade | data_steward | Confirmed by domain expert |
| SIG-75-DRM-1CLN | Resistant Starch 50% Standard | data_steward | Auto-mapped, validated |
| SIG-48-ASO-8G0Y | Maltodextrin DE20 | system_admin | Auto-mapped, validated |
| SIG-29-RWA-CHL8 | Citric Acid | domain_expert | Confirmed by domain expert |
| SIG-13-TIV-U5CX | Sodium Chloride 25% Food Grade | domain_expert | Historical match confirmed |
| SIG-18-SSS-CTEL | Resistant Starch 98% Grade B | system_admin | Cross-referenced with transactions |
| SIG-77-TUK-IN2B | Pea Protein 70% Premium | domain_expert | Auto-mapped, validated |
| SIG-23-BLM-EZKX | Sodium Chloride | domain_expert | Cross-referenced with transactions |
| SIG-63-MOD-EKOJ | Lactic Acid | data_steward | Cross-referenced with transactions |
| SIG-79-RKA-P64T | Wheat Gluten 99.5% | system_admin | Verified via product specs |
| SIG-73-KLZ-PDKU | Isoglucose Grade B | domain_expert | Cross-referenced with transactions |
| SIG-16-MNF-F4AF | Isoglucose 99.5% | domain_expert | Auto-mapped, validated |
| SIG-12-HNK-0H4F | Soy Isolate Food Grade | domain_expert | Verified via product specs |
| SIG-44-HTV-P84J | Lactic Acid | data_steward | Confirmed by domain expert |
| SIG-24-NPE-GDMB | Rapeseed Oil 70% Technical | domain_expert | Auto-mapped, validated |
| SIG-50-SVK-9TOS | Coconut Oil 70% Grade A | domain_expert | Verified via product specs |
| SIG-80-QOK-BKBF | Fructose 70% | system_admin | Verified via product specs |
| SIG-86-HYW-79YR | Casein Grade A | domain_expert | Cross-referenced with transactions |
| SIG-87-DSD-DF5J | Potassium Sorbate | domain_expert | Confirmed by domain expert |
| SIG-29-YUO-5FO9 | Resistant Starch Grade A | domain_expert | Auto-mapped, validated |
| SIG-67-VXU-FPWB | Pea Protein 99.5% Premium | data_steward | Auto-mapped, validated |
| SIG-93-ZCF-6HM3 | Ascorbic Acid Premium | system_admin | Cross-referenced with transactions |
| SIG-42-IEF-RFC9 | Ascorbic Acid 98% | system_admin | Confirmed by domain expert |
| SIG-86-DMG-XSKY | Isoglucose 98% | system_admin | Auto-mapped, validated |
| SIG-20-UGT-P0LW | Wheat Gluten Grade A | data_steward | Confirmed by domain expert |
| SIG-36-TML-VS0J | Dextrin Grade B | system_admin | Auto-mapped, validated |
| SIG-53-TLC-AZKT | Sunflower Oil Technical | domain_expert | Cross-referenced with transactions |
| SIG-13-IPI-71PJ | Cyclodextrin | system_admin | Historical match confirmed |
| SIG-15-PFO-2W85 | Lactic Acid Technical | data_steward | Auto-mapped, validated |
| SIG-61-CIV-LFWA | Soy Isolate 99.5% Grade A | domain_expert | Verified via product specs |
| SIG-38-YGZ-FBOJ | Sodium Benzoate | system_admin | Verified via product specs |
| SIG-15-FOA-70S8 | Wheat Gluten 70% | data_steward | Historical match confirmed |
| SIG-97-XJT-7TBU | Coconut Oil 25% Grade B | domain_expert | Auto-mapped, validated |
| SIG-93-DAB-6LKS | Sunflower Oil | system_admin | Verified via product specs |
| SIG-11-QDU-30PE | Sunflower Oil Standard | domain_expert | Verified via product specs |
| SIG-58-SBP-KRSZ | Wheat Gluten 25% Food Grade | domain_expert | Auto-mapped, validated |
| SIG-27-QBW-ROGA | Lactic Acid Food Grade | domain_expert | Confirmed by domain expert |
| SIG-77-CMG-ORNE | Coconut Oil 25% | system_admin | Auto-mapped, validated |
| SIG-82-JMP-PVGN | Dextrose | system_admin | Confirmed by domain expert |
| SIG-82-IYU-XY3P | Casein Technical | domain_expert | Historical match confirmed |
| SIG-37-PYQ-815V | Sunflower Oil 70% Food Grade | data_steward | Cross-referenced with transactions |
| SIG-20-OAV-1IKJ | Casein 50% Premium | data_steward | Historical match confirmed |
| SIG-20-XIG-T8ME | Calcium Carbonate 50% Food Grade | domain_expert | Cross-referenced with transactions |
| SIG-37-HHT-38YO | Sodium Benzoate Food Grade | system_admin | Verified via product specs |
| SIG-63-LNS-ECTA | Palm Oil Food Grade | system_admin | Verified via product specs |
| SIG-91-WVE-3ESP | Wheat Gluten Grade A | domain_expert | Verified via product specs |
| SIG-78-RAG-D2IP | Rapeseed Oil Pharma Grade | data_steward | Confirmed by domain expert |
| SIG-92-RZH-LRHH | Resistant Starch Standard | data_steward | Cross-referenced with transactions |
| SIG-94-TOI-OFNK | Wheat Gluten 25% Standard | domain_expert | Verified via product specs |
| SIG-77-LSN-T27F | Sodium Chloride Technical | domain_expert | Auto-mapped, validated |
| SIG-27-NTH-I37Y | Potassium Sorbate | system_admin | Cross-referenced with transactions |
| SIG-84-MGK-H2ME | Dextrin 98% Food Grade | system_admin | Cross-referenced with transactions |
| SIG-39-DJJ-3SY8 | Sunflower Oil | domain_expert | Confirmed by domain expert |
| SIG-82-UMX-OJ7L | Sunflower Oil 50% Pharma Grade | system_admin | Historical match confirmed |
| SIG-22-SKR-CTIC | Sunflower Oil Pharma Grade | domain_expert | Confirmed by domain expert |
| SIG-67-MFG-46DE | Casein 25% Grade A | system_admin | Verified via product specs |
| SIG-38-YTD-7BST | Dextrin Technical | data_steward | Auto-mapped, validated |
| SIG-58-LWY-Q8P6 | Cyclodextrin Standard | domain_expert | Auto-mapped, validated |
| SIG-91-FOC-36I6 | Sodium Benzoate Grade A | data_steward | Verified via product specs |
| SIG-84-DSO-4S47 | Wheat Gluten | domain_expert | Auto-mapped, validated |
| SIG-99-IMJ-KFOM | Maltodextrin DE18 | domain_expert | Confirmed by domain expert |
| SIG-42-STL-CX7L | Sunflower Oil Grade A | data_steward | Confirmed by domain expert |
| SIG-50-ABM-7VSK | Potassium Sorbate 50% Food Grade | system_admin | Verified via product specs |
| SIG-95-APX-PWFS | Soy Isolate 50% Premium | domain_expert | Auto-mapped, validated |
| SIG-52-ITT-ELH9 | Resistant Starch 70% | system_admin | Cross-referenced with transactions |
| SIG-64-IEU-FRGN | Resistant Starch | domain_expert | Historical match confirmed |
| SIG-80-WKN-N0SS | Potassium Sorbate Food Grade | domain_expert | Cross-referenced with transactions |
| SIG-41-QPX-D1RL | Citric Acid | system_admin | Confirmed by domain expert |
| SIG-89-ISH-EQW6 | Soy Isolate Premium | data_steward | Confirmed by domain expert |
| SIG-61-PIG-0DBF | Resistant Starch 70% | domain_expert | Confirmed by domain expert |
| SIG-56-NOU-ZR98 | Fructose Premium | domain_expert | Confirmed by domain expert |
| SIG-90-SJW-O06V | Dextrose | system_admin | Historical match confirmed |
| SIG-47-UCC-EFEL | Sodium Chloride 70% | system_admin | Verified via product specs |
| SIG-62-YMZ-RQQI LLC | Atlas Industries LLC | data_steward | Confirmed by domain expert |
| SIG-93-TEG-8CN0 SARL | Catalyst Logistics SA | domain_expert | Auto-mapped, validated |
| SIG-56-EAF-SHQE Group | Premier Commodities Group | data_steward | Historical match confirmed |
| SIG-42-NMJ-RACV International | Prime Partners | system_admin | Confirmed by domain expert |
| SIG-97-TPD-0NJR LLC | Global Distribution LLC | domain_expert | Auto-mapped, validated |
| SIG-82-YQL-Q0L4 NV | Pinnacle Commodities BV | system_admin | Confirmed by domain expert |
| SIG-56-ZQV-YINP SA | Atlas Trading SA | data_steward | Verified via product specs |
| SIG-79-TAG-A44Y | Horizon Trading | system_admin | Historical match confirmed |
| SIG-59-VFK-OOZW SA | Stellar Distribution SA | system_admin | Verified via product specs |
| SIG-41-LKO-OD4P Ltd. | Pinnacle Ingredients Ltd. | data_steward | Historical match confirmed |
| SIG-86-XWS-MOPG Corp. | Central Solutions | data_steward | Confirmed by domain expert |
| SIG-84-EQC-XHMK Holdings | Pacific Logistics | data_steward | Confirmed by domain expert |
| SIG-71-KJM-D5G1 Holdings | Quantum Ingredients | domain_expert | Historical match confirmed |
| SIG-63-DWD-X8UB | Continental Enterprise Holdings | data_steward | Auto-mapped, validated |
| SIG-53-DUL-C550 Group | Core Chemicals International | system_admin | Auto-mapped, validated |
| SIG-17-FUU-SGT6 KG | Catalyst Manufacturing GmbH | data_steward | Confirmed by domain expert |
| SIG-26-PVD-6QGC AG | Pacific Chemicals AG | data_steward | Confirmed by domain expert |
| SIG-61-FGJ-AO1L NV | Pacific Distribution NV | domain_expert | Verified via product specs |
| SIG-87-OKN-L3O4 | Pacific Distribution International | system_admin | Confirmed by domain expert |
| SIG-54-QHS-YUMN | Premier Enterprise International | domain_expert | Historical match confirmed |
| SIG-70-SAQ-KIAC | Pinnacle Distribution KG | domain_expert | Auto-mapped, validated |
| SIG-22-RFO-RZQE | Stratos Enterprise International | system_admin | Auto-mapped, validated |
| SIG-23-LAS-L2MX Holdings | Vertex Enterprise Holdings | data_steward | Verified via product specs |
| SIG-44-LEF-PDJN SARL | Prime Chemicals | data_steward | Auto-mapped, validated |
| SIG-14-HVI-T0Z6 SARL | Vanguard Logistics SARL | system_admin | Auto-mapped, validated |
| SIG-81-LVQ-2J60 | Stratos Trading BV | data_steward | Cross-referenced with transactions |
| SIG-95-HLU-HD5X GmbH | Baltic Enterprise KG | domain_expert | Historical match confirmed |
| SIG-99-TBJ-83YG KG | Quantum Manufacturing KG | data_steward | Cross-referenced with transactions |
| SIG-98-WXH-VOMX | Continental Manufacturing AG | domain_expert | Auto-mapped, validated |
| SIG-42-SPP-A6C6 | Atlas Ingredients PLC | data_steward | Verified via product specs |
| SIG-85-SQB-MODP BV | Vertex Distribution NV | domain_expert | Verified via product specs |
| SIG-48-JXQ-RFSL LLC | Atlas Manufacturing | system_admin | Auto-mapped, validated |
| SIG-62-JPL-NU17 Holdings | Zenith Manufacturing | system_admin | Confirmed by domain expert |
| SIG-51-BUX-VLME Group | Atlas Logistics International | domain_expert | Cross-referenced with transactions |
| SIG-64-MMA-YU3T NV | Stratos Supply | domain_expert | Auto-mapped, validated |
| SIG-65-IJJ-DXAJ SA | Global Processing SAS | system_admin | Verified via product specs |
| SIG-88-RGQ-WZOI | Horizon Partners Group | data_steward | Verified via product specs |
| SIG-23-WOJ-YTND International | Apex Solutions | system_admin | Cross-referenced with transactions |
| SIG-92-FQX-S1BC | Core Manufacturing Holdings | system_admin | Historical match confirmed |
| SIG-35-BYM-BYQ7 Inc. | Pinnacle Trading | domain_expert | Auto-mapped, validated |
| SIG-56-JML-GDXB | Elite Distribution | data_steward | Auto-mapped, validated |
| SIG-70-YLY-65JU PLC | Prime Supply | data_steward | Historical match confirmed |
| SIG-93-ABB-76KE | Prism Distribution BV | domain_expert | Cross-referenced with transactions |
| SIG-51-ZHS-W8WR International | Meridian Trading | domain_expert | Cross-referenced with transactions |
| SIG-25-KUC-FYE7 Ltd. | Quantum Processing Ltd. | system_admin | Verified via product specs |
| SIG-72-JWR-R2ZI BV | Prism Ingredients | system_admin | Historical match confirmed |
| SIG-86-JBA-HCDI | Stellar Supply | system_admin | Cross-referenced with transactions |
| SIG-32-DNR-U0SL | Meridian Solutions KG | domain_expert | Confirmed by domain expert |
| SIG-63-OTU-T27J Corp. | Apex Chemicals | domain_expert | Auto-mapped, validated |
| SIG-49-LWO-P3PY | Global Enterprise NV | domain_expert | Verified via product specs |
| SIG-11-LPV-TM1Q International | Vanguard Enterprise International | system_admin | Historical match confirmed |
| SIG-32-VLW-1KKT NV | Global Logistics | domain_expert | Verified via product specs |
| SIG-55-OVK-B4MF GmbH | Continental Enterprise KG | data_steward | Cross-referenced with transactions |
| SIG-89-WUP-8NG0 | Core Logistics Holdings | data_steward | Cross-referenced with transactions |
| SIG-31-CWH-OC2T | Core Chemicals | data_steward | Confirmed by domain expert |
| SIG-18-CIG-ZUL8 Holdings | Nexus Industries Group | data_steward | Auto-mapped, validated |
| SIG-58-WYL-XCXB | Vertex Solutions BV | data_steward | Historical match confirmed |
| SIG-78-WKT-9TDY SAS | Nordic Ingredients SA | data_steward | Verified via product specs |
| SIG-39-WTU-81JC | Vertex Distribution AG | system_admin | Auto-mapped, validated |
| SIG-75-XPL-QWB7 GmbH | Catalyst Commodities GmbH | domain_expert | Cross-referenced with transactions |
| SIG-62-NKL-SM8R | Apex Trading Group | system_admin | Auto-mapped, validated |
| SIG-79-IWJ-YNSA | Continental Ingredients | data_steward | Verified via product specs |
| SIG-14-WWQ-VPK2 SARL | Stratos Ingredients SARL | domain_expert | Auto-mapped, validated |
| SIG-27-QTK-7Y6C | Baltic Commodities Inc. | system_admin | Cross-referenced with transactions |
| SIG-93-YGI-KLQ0 | Catalyst Industries International | system_admin | Auto-mapped, validated |
| SIG-70-EXR-LD0M | Pinnacle Commodities | system_admin | Historical match confirmed |
| SIG-12-QLD-RUJ3 Inc. | Premier Solutions LLC | data_steward | Auto-mapped, validated |
| SIG-74-LEZ-GZA2 AG | Global Ingredients AG | system_admin | Historical match confirmed |
| SIG-40-CXK-QT2E Group | Nexus Enterprise International | domain_expert | Auto-mapped, validated |
| SIG-96-ANZ-BP7C SA | Atlantic Partners SARL | data_steward | Cross-referenced with transactions |
| SIG-28-FYV-P1ZR Group | Apex Chemicals | system_admin | Confirmed by domain expert |
| SIG-40-RSD-JF0U | Pinnacle Solutions Corp. | system_admin | Confirmed by domain expert |
| SIG-83-TNT-G0Q1 AG | Atlas Chemicals | system_admin | Historical match confirmed |
| SIG-88-RUZ-O3Q0 | Baltic Chemicals Group | domain_expert | Historical match confirmed |
| SIG-58-BDP-AYRN | Premier Industries Group | data_steward | Confirmed by domain expert |
| SIG-29-BKQ-HXCX Group | Prism Ingredients | domain_expert | Cross-referenced with transactions |
| SIG-60-FRA-PB5V Holdings | Apex Commodities Holdings | system_admin | Cross-referenced with transactions |
| SIG-28-AOC-YRBZ Corp. | Baltic Solutions | data_steward | Auto-mapped, validated |
| SIG-81-AXG-9CBI AG | Apex Ingredients AG | domain_expert | Historical match confirmed |
| SIG-54-ZOX-KCNY SAS | Vertex Distribution SA | system_admin | Cross-referenced with transactions |
| SIG-31-MAP-SEFM | Central Manufacturing NV | system_admin | Verified via product specs |
| SIG-65-ONA-WQOF Corp. | Zenith Trading LLC | system_admin | Auto-mapped, validated |
| SIG-54-ZFB-4REP Inc. | Nexus Distribution | domain_expert | Auto-mapped, validated |
| SIG-76-COR-DQEF GmbH | Pinnacle Ingredients AG | system_admin | Confirmed by domain expert |
| SIG-82-POX-I1CU | Nordic Ingredients | data_steward | Historical match confirmed |
| SIG-67-MFU-QOZ9 Group | Horizon Logistics International | system_admin | Cross-referenced with transactions |
| SIG-59-CFT-59LL Holdings | Quantum Solutions Group | system_admin | Cross-referenced with transactions |
| SIG-81-EKU-R7CX Group | Catalyst Enterprise International | system_admin | Auto-mapped, validated |
| SIG-45-JPK-8INR | Global Solutions International | data_steward | Historical match confirmed |
| SIG-60-XUT-HTI7 | Pacific Ingredients BV | domain_expert | Historical match confirmed |
| SIG-91-GKA-MSWV | Atlas Solutions BV | system_admin | Historical match confirmed |
| SIG-53-OGW-YU4I Ltd. | Nordic Industries Ltd. | domain_expert | Confirmed by domain expert |
| SIG-83-MZM-HGMN GmbH | Horizon Industries | system_admin | Cross-referenced with transactions |
| SIG-58-DDZ-4JKE International | Nexus Processing International | domain_expert | Historical match confirmed |
| SIG-17-BCC-01JW | Atlantic Partners | system_admin | Confirmed by domain expert |
| SIG-50-HWB-Y27E Ltd. | Quantum Commodities PLC | system_admin | Verified via product specs |
| SIG-55-GSW-Z8Y2 Ltd. | Baltic Processing PLC | domain_expert | Auto-mapped, validated |
| SIG-51-HOK-PC9S Holdings | Nexus Chemicals Group | domain_expert | Cross-referenced with transactions |
| SIG-31-LDA-I5LG Ltd. | Prism Materials Ltd. | domain_expert | Cross-referenced with transactions |
| SIG-94-OAX-GACW Ltd. | Nexus Ingredients PLC | domain_expert | Auto-mapped, validated |
| SIG-68-SJS-K3N3 | Continental Solutions | domain_expert | Verified via product specs |
| SIG-36-FMG-DSYM Group | Stellar Commodities | data_steward | Confirmed by domain expert |
| SIG-59-ZZK-AYAJ PLC | Catalyst Industries | system_admin | Auto-mapped, validated |
| SIG-86-XNZ-5Q7H | Atlas Manufacturing | data_steward | Confirmed by domain expert |
| SIG-97-PAD-AUZ7 | Atlas Industries Group | system_admin | Confirmed by domain expert |
| SIG-14-TOH-IPJ4 | Stratos Distribution Group | domain_expert | Confirmed by domain expert |
| SIG-18-ANT-0DK4 GmbH | Atlantic Industries AG | system_admin | Verified via product specs |
| SIG-16-GDL-YC2T LLC | Prism Solutions Corp. | system_admin | Verified via product specs |
| SIG-38-QCS-G19Q Holdings | Atlantic Processing International | system_admin | Confirmed by domain expert |
| SIG-37-YMX-1ATI SARL | Quantum Trading SA | domain_expert | Historical match confirmed |
| SIG-45-ZZU-GRXH International | Atlantic Industries | domain_expert | Cross-referenced with transactions |
| SIG-12-JYK-S9KT Group | Elite Solutions | system_admin | Verified via product specs |
| SIG-41-ZTZ-VNMI Holdings | Central Ingredients | system_admin | Historical match confirmed |
| SIG-34-TUW-UWNZ Group | Premier Enterprise International | data_steward | Historical match confirmed |
| SIG-73-XKX-JG0D SAS | Baltic Ingredients SA | system_admin | Cross-referenced with transactions |
| SIG-94-CCX-H0AN International | Baltic Distribution Group | system_admin | Confirmed by domain expert |
| SIG-40-JOQ-S1CO KG | Zenith Trading | domain_expert | Historical match confirmed |
| SIG-59-IWS-F4PJ | Stellar Distribution International | data_steward | Historical match confirmed |
| SIG-83-BZN-2A0N KG | Premier Trading KG | domain_expert | Historical match confirmed |
| SIG-55-ICI-Z2GP GmbH | Quantum Commodities | domain_expert | Confirmed by domain expert |
| SIG-68-HOK-ETCC | Pinnacle Enterprise AG | domain_expert | Confirmed by domain expert |
| SIG-37-AVX-CY7Q SAS | Catalyst Commodities SAS | data_steward | Verified via product specs |
| SIG-31-YNJ-FQMJ Holdings | Stellar Processing Holdings | data_steward | Verified via product specs |
| SIG-28-KHD-E4FM NV | Atlas Materials BV | domain_expert | Historical match confirmed |
| SIG-88-MKW-I0IO NV | Continental Materials NV | domain_expert | Confirmed by domain expert |
| SIG-60-GCS-MZ2C Ltd. | Prime Processing Ltd. | data_steward | Confirmed by domain expert |
| SIG-86-QTB-N3VO International | Stellar Partners | data_steward | Cross-referenced with transactions |
| SIG-13-RWR-7JHQ SA | Horizon Materials SAS | domain_expert | Historical match confirmed |
| SIG-28-OZR-B7E8 Group | Meridian Distribution | system_admin | Verified via product specs |
| SIG-39-JXL-BQ85 SARL | Nexus Solutions SAS | system_admin | Cross-referenced with transactions |
| SIG-99-PXI-1L7K | Pinnacle Chemicals | data_steward | Confirmed by domain expert |
| SIG-89-RGS-FIRM Holdings | Atlantic Industries | domain_expert | Verified via product specs |
| SIG-77-TQY-IC8H Holdings | Stellar Manufacturing Group | system_admin | Historical match confirmed |
| SIG-39-ZIX-L5KV International | Apex Materials Group | domain_expert | Confirmed by domain expert |
| SIG-59-HZI-WDX6 Group | Horizon Partners International | data_steward | Historical match confirmed |
| SIG-92-AXW-GPAG | Elite Trading | system_admin | Cross-referenced with transactions |
| SIG-36-PWY-HJFC International | Continental Processing Group | data_steward | Cross-referenced with transactions |
| SIG-90-ZPA-GKE1 BV | Elite Materials NV | data_steward | Cross-referenced with transactions |
| SIG-15-TGS-WDIJ Group | Vanguard Ingredients | system_admin | Auto-mapped, validated |
| SIG-40-BRW-FV7U | Nexus Supply Group | data_steward | Historical match confirmed |
| SIG-82-DAB-YHKJ | Pacific Industries Ltd. | system_admin | Cross-referenced with transactions |
| SIG-14-HQE-PUWC | Stratos Partners SAS | domain_expert | Cross-referenced with transactions |
| SIG-32-WFB-DVCF International | Atlas Logistics International | data_steward | Historical match confirmed |
| SIG-44-HLB-IC48 SARL | Nexus Ingredients | data_steward | Cross-referenced with transactions |
| SIG-57-RYP-D466 | Central Manufacturing PLC | data_steward | Historical match confirmed |
| SIG-41-LVX-8RWD SAS | Premier Trading SA | system_admin | Confirmed by domain expert |
| SIG-79-DZB-60U2 International | Prism Materials International | system_admin | Historical match confirmed |
| SIG-64-GUK-32QL SARL | Quantum Processing SA | domain_expert | Historical match confirmed |
| SIG-35-VQC-JQ0H AG | Continental Ingredients | data_steward | Auto-mapped, validated |
| SIG-77-WCC-DNFC Holdings | Global Processing Holdings | data_steward | Confirmed by domain expert |
| SIG-47-BQW-HBQI NV | Nordic Enterprise | system_admin | Auto-mapped, validated |
| SIG-46-YOE-MYAX SA | Pacific Enterprise SAS | system_admin | Cross-referenced with transactions |
| SIG-69-FIT-Y3OC International | Premier Solutions Holdings | domain_expert | Historical match confirmed |
| SIG-59-HVI-BACX Group | Premier Distribution Group | system_admin | Confirmed by domain expert |
| SIG-19-KAW-QNPA | Continental Manufacturing Inc. | domain_expert | Auto-mapped, validated |
| SIG-41-VXU-J3AN | Baltic Industries BV | data_steward | Historical match confirmed |
| SIG-17-UCE-6H7J Corp. | Atlas Partners Corp. | domain_expert | Verified via product specs |
| SIG-63-LZV-C5BN | Core Chemicals | data_steward | Auto-mapped, validated |
| SIG-52-CQW-KL19 | Nexus Trading Group | data_steward | Confirmed by domain expert |
| SIG-17-GFH-X0JO PLC | Prism Manufacturing PLC | system_admin | Auto-mapped, validated |
| SIG-17-ZBZ-BJS4 SARL | Nordic Industries | domain_expert | Auto-mapped, validated |
| SIG-83-OGL-6IBH Group | Vanguard Logistics | domain_expert | Auto-mapped, validated |
| SIG-58-CJW-XYEP BV | Zenith Materials NV | domain_expert | Cross-referenced with transactions |
| SIG-53-NHM-OFA2 | Meridian Ingredients GmbH | system_admin | Verified via product specs |
| SIG-98-SID-2107 GmbH | Prism Chemicals KG | data_steward | Confirmed by domain expert |
| SIG-27-DQT-IQ97 | Catalyst Distribution | data_steward | Confirmed by domain expert |
| SIG-99-CTB-8OFG Group | Vertex Distribution Holdings | system_admin | Confirmed by domain expert |
| SIG-83-BQM-NXXK PLC | Central Commodities Ltd. | system_admin | Historical match confirmed |
| SIG-43-AAR-M0YW | Atlantic Supply | domain_expert | Confirmed by domain expert |
| SIG-58-MRH-P47P | Pacific Industries Group | domain_expert | Confirmed by domain expert |
| SIG-36-XXX-LH5B NV | Premier Manufacturing NV | data_steward | Verified via product specs |
| SIG-52-JLE-5KJF SAS | Catalyst Industries | data_steward | Historical match confirmed |
| SIG-85-CHF-5W9X SA | Stellar Supply | data_steward | Historical match confirmed |
| SIG-61-YSE-8JLK SARL | Pinnacle Materials SA | domain_expert | Auto-mapped, validated |
| SIG-94-MUO-QFTQ | Continental Enterprise Group | system_admin | Cross-referenced with transactions |
| SIG-85-GWL-FUXA | Apex Manufacturing | system_admin | Historical match confirmed |
| SIG-77-RVO-CE8D Inc. | Baltic Commodities | data_steward | Historical match confirmed |
| SIG-58-LVK-OFDU KG | Pacific Materials | domain_expert | Verified via product specs |
| SIG-83-TEU-OH8F Group | Vanguard Distribution | domain_expert | Confirmed by domain expert |
| SIG-72-OHB-75ML SAS | Zenith Enterprise | system_admin | Historical match confirmed |
| SIG-59-HRE-WMJT | Central Partners | domain_expert | Historical match confirmed |
| SIG-78-TUT-T3NS | Meridian Chemicals AG | data_steward | Cross-referenced with transactions |
| SIG-29-LEJ-26GF Group | Nordic Manufacturing Holdings | system_admin | Verified via product specs |
| SIG-48-MQG-OVJU SAS | Zenith Distribution SARL | system_admin | Cross-referenced with transactions |
| SIG-41-ZGH-C0Y2 Holdings | Stratos Materials International | system_admin | Historical match confirmed |
| SIG-40-DEO-UM9B International | Vanguard Distribution | data_steward | Historical match confirmed |
| SIG-99-AYV-D18J International | Prime Solutions | system_admin | Verified via product specs |
| SIG-85-CBK-XO7I | Baltic Supply Holdings | data_steward | Auto-mapped, validated |
| SIG-59-HNQ-A8N5 Ltd. | Premier Supply PLC | data_steward | Auto-mapped, validated |
| SIG-68-BSO-NW8J Group | Meridian Distribution | system_admin | Historical match confirmed |
| SIG-43-MIT-DWCJ SA | Pacific Commodities SAS | system_admin | Historical match confirmed |
| SIG-98-OXJ-W0H6 SAS | Premier Materials SAS | domain_expert | Cross-referenced with transactions |
| SIG-58-FND-MEQW Ltd. | Horizon Logistics | data_steward | Cross-referenced with transactions |
| SIG-78-QFN-H3BV | Premier Logistics AG | data_steward | Cross-referenced with transactions |
| SIG-60-GZP-BB7N NV | Global Partners | system_admin | Confirmed by domain expert |
| SIG-50-GYK-UH5P | Core Manufacturing | data_steward | Historical match confirmed |
| SIG-22-HKE-ONVA | Nordic Distribution | system_admin | Confirmed by domain expert |
| SIG-64-ILX-G2AZ PLC | Prime Partners PLC | data_steward | Auto-mapped, validated |
| SIG-24-PDE-AZV1 PLC | Quantum Trading | domain_expert | Historical match confirmed |
| SIG-53-VTO-Y7V6 NV | Central Materials NV | data_steward | Historical match confirmed |
| SIG-86-JSN-H9KJ SA | Elite Logistics SA | data_steward | Verified via product specs |
| SIG-32-DTD-L7TD International | Core Processing Holdings | system_admin | Historical match confirmed |
| SIG-60-RUC-CU6A | Pacific Enterprise International | data_steward | Auto-mapped, validated |
| SIG-92-FQW-WCF5 SARL | Meridian Logistics | domain_expert | Historical match confirmed |
| SIG-99-CEZ-35MR | Vertex Industries BV | data_steward | Confirmed by domain expert |
| SIG-66-IYP-1A2W | Pinnacle Processing | domain_expert | Historical match confirmed |
| SIG-12-HNO-R9V0 AG | Vertex Commodities | data_steward | Confirmed by domain expert |
| SIG-95-QUH-2TS2 | Catalyst Supply Holdings | system_admin | Cross-referenced with transactions |
| SIG-27-IRG-QSO9 International | Atlantic Distribution Group | system_admin | Cross-referenced with transactions |
| SIG-88-DDB-92XS Holdings | Nexus Processing Holdings | system_admin | Verified via product specs |
| SIG-76-RWX-Q314 International | Premier Enterprise Group | data_steward | Historical match confirmed |
| SIG-94-AWA-77SY Holdings | Catalyst Ingredients International | domain_expert | Cross-referenced with transactions |
| SIG-59-FNZ-ZVBE Ltd. | Prime Commodities | domain_expert | Cross-referenced with transactions |
| SIG-27-KMU-WPWH GmbH | Pacific Materials KG | system_admin | Verified via product specs |
| SIG-56-FFG-XS2P | Stellar Distribution | domain_expert | Verified via product specs |
| SIG-20-GZD-R03A SARL | Nordic Processing SAS | system_admin | Historical match confirmed |
| SIG-12-USU-9HWB GmbH | Core Trading | domain_expert | Confirmed by domain expert |
| SIG-13-QNH-MZKO SAS | Atlas Commodities SAS | data_steward | Historical match confirmed |
| SIG-83-OBQ-GEIL GmbH | Global Processing KG | system_admin | Confirmed by domain expert |
| SIG-77-LKE-KW49 | Zenith Industries Corp. | domain_expert | Verified via product specs |
| SIG-83-FWQ-4QAN Holdings | Apex Trading Holdings | system_admin | Auto-mapped, validated |
| SIG-28-MAP-2EOP Holdings | Vertex Distribution | domain_expert | Historical match confirmed |
| SIG-58-NUP-5DTV Group | Baltic Manufacturing | system_admin | Auto-mapped, validated |
| SIG-48-YBV-ZD0Y | Quantum Trading Holdings | system_admin | Confirmed by domain expert |
| SIG-72-FHF-DYSG | Stellar Manufacturing Holdings | domain_expert | Historical match confirmed |
| SIG-16-ZDY-GYTX Holdings | Baltic Trading Holdings | data_steward | Auto-mapped, validated |
| SIG-86-VFH-L4DY Holdings | Catalyst Supply Holdings | data_steward | Auto-mapped, validated |
| SIG-98-CTS-XPY5 | Atlas Supply Corp. | domain_expert | Historical match confirmed |
| SIG-58-GKH-LOY0 Group | Atlantic Processing Holdings | system_admin | Auto-mapped, validated |
| SIG-73-BSB-YCKN Group | Baltic Processing | data_steward | Historical match confirmed |
| SIG-97-BXB-U2Y7 Ltd. | Core Partners PLC | domain_expert | Auto-mapped, validated |
| SIG-13-ZIB-S8MV International | Vertex Chemicals | data_steward | Verified via product specs |
| SIG-14-FNK-JNLM NV | Vanguard Industries BV | data_steward | Historical match confirmed |
| SIG-68-BSB-VSIA | Prime Logistics International | data_steward | Verified via product specs |
| SIG-20-MSW-TMXG | Apex Logistics Inc. | data_steward | Cross-referenced with transactions |
| SIG-27-MIG-RYBN | Atlantic Materials | data_steward | Verified via product specs |
| SIG-84-MUG-BUXR | Core Supply Co. | system_admin | Auto-mapped, validated |
| SIG-79-UGU-7OFC | Catalyst Logistics | domain_expert | Confirmed by domain expert |
| SIG-35-HUP-NW3M | Elite Logistics | system_admin | Verified via product specs |
| SIG-10-HXN-BKWJ | Premier Supply Co. | domain_expert | Verified via product specs |
| SIG-13-ZRN-WZGO | Baltic Supply Co. | domain_expert | Verified via product specs |
| SIG-93-CZZ-ZGWF | Stratos Logistics | domain_expert | Confirmed by domain expert |
| SIG-64-RFK-TW5N | Core Materials | data_steward | Confirmed by domain expert |
| SIG-83-SGE-Q8I0 | Elite Sourcing | system_admin | Verified via product specs |
| SIG-47-MLZ-TPP5 | Vertex Materials | domain_expert | Cross-referenced with transactions |
| SIG-77-GUM-TVUW | Vertex Logistics | system_admin | Confirmed by domain expert |
| SIG-84-NJC-6XAS | Stellar Sourcing | system_admin | Confirmed by domain expert |
| SIG-89-GUQ-OU40 | Vertex Materials | data_steward | Confirmed by domain expert |
| SIG-60-OBI-GVJP | Nexus Sourcing | data_steward | Historical match confirmed |
| SIG-40-XXD-GE9O | Central Logistics | system_admin | Verified via product specs |
| SIG-59-ECO-OXB3 | Global Logistics | system_admin | Cross-referenced with transactions |
| SIG-85-TWH-HQKB | Pinnacle Sourcing | data_steward | Confirmed by domain expert |
| SIG-96-EVO-10JM | Continental Sourcing | system_admin | Historical match confirmed |
| SIG-96-POT-WDYM | Elite Supply Co. | system_admin | Auto-mapped, validated |
| SIG-98-HZM-47LK | Vertex Sourcing | system_admin | Auto-mapped, validated |
| SIG-27-VCT-2O4S | Quantum Supply Co. | data_steward | Confirmed by domain expert |
| SIG-54-OTO-2MVK | Zenith Supply Co. | system_admin | Cross-referenced with transactions |
| SIG-42-QVG-422I | Zenith Supply Co. | domain_expert | Cross-referenced with transactions |
| SIG-15-YBX-K4SY | Atlas Supply Co. | system_admin | Verified via product specs |
| SIG-29-XAN-WDDA | Catalyst Logistics | system_admin | Confirmed by domain expert |
| SIG-34-LLF-EQC4 | Meridian Logistics | data_steward | Auto-mapped, validated |
| SIG-44-NAF-R7O0 | Global Sourcing | domain_expert | Verified via product specs |
| SIG-39-KYF-P35A | Vertex Sourcing | data_steward | Cross-referenced with transactions |
| SIG-90-XNG-UYZN | Atlas Supply Co. | domain_expert | Verified via product specs |
| SIG-20-FYS-JNIL | Baltic Supply Co. | data_steward | Auto-mapped, validated |
| SIG-57-CCU-W7CL | Continental Supply Co. | system_admin | Cross-referenced with transactions |
| SIG-48-LUB-IGA7 | Nexus Logistics | data_steward | Historical match confirmed |
| SIG-79-DHA-SUOB | Stellar Logistics | system_admin | Historical match confirmed |
| SIG-33-IHK-2GVW | Vertex Logistics | data_steward | Confirmed by domain expert |
| SIG-39-BHZ-K8SS | Stellar Materials | domain_expert | Verified via product specs |
| SIG-48-BCW-76F8 | Elite Logistics | system_admin | Cross-referenced with transactions |
| SIG-69-UAZ-1ODW | Prism Sourcing | system_admin | Confirmed by domain expert |
| SIG-60-NXS-8BAO | Premier Supply Co. | domain_expert | Verified via product specs |
| SIG-98-YBY-PFKQ | Continental Supply Co. | domain_expert | Auto-mapped, validated |
| SIG-68-GHA-D32X | Nexus Logistics | system_admin | Cross-referenced with transactions |
| SIG-12-JHE-FNCL | Atlantic Supply Co. | domain_expert | Verified via product specs |
| SIG-39-ARU-8X3V | Core Logistics | data_steward | Cross-referenced with transactions |
| SIG-75-KAH-G7BB | Atlas Logistics | domain_expert | Verified via product specs |
| SIG-98-DBG-MTO5 | Prime Supply Co. | system_admin | Auto-mapped, validated |
| SIG-19-RDF-86GH | Stratos Sourcing | data_steward | Cross-referenced with transactions |
| SIG-67-JNR-XNTM | Quantum Supply Co. | data_steward | Historical match confirmed |
| SIG-89-PFV-OOFP | Quantum Sourcing | data_steward | Auto-mapped, validated |
| SIG-39-QPC-OLQF | Baltic Logistics | system_admin | Verified via product specs |
| SIG-38-TDY-99S2 | Prism Sourcing | domain_expert | Cross-referenced with transactions |
| SIG-33-VWP-VX5U | Central Logistics | data_steward | Auto-mapped, validated |
| SIG-97-KNV-Q7J8 | Premier Supply Co. | system_admin | Verified via product specs |
| SIG-96-UYO-0BNC | Apex Supply Co. | data_steward | Historical match confirmed |
| SIG-89-YWW-NUVL | Stratos Supply Co. | domain_expert | Historical match confirmed |
| SIG-46-MBC-QSXJ | Premier Materials | data_steward | Verified via product specs |
| SIG-97-JHL-5AAT | Apex Logistics | system_admin | Historical match confirmed |
| SIG-40-YZP-9CC3 | Premier Logistics | data_steward | Auto-mapped, validated |
| SIG-12-DBI-8UY5 | Central Materials | system_admin | Historical match confirmed |
| SIG-59-VHS-XGCF | Apex Logistics | domain_expert | Confirmed by domain expert |
| SIG-74-ZGY-ZA9S | Pacific Sourcing | data_steward | Historical match confirmed |
| SIG-46-SZM-WPIS | Catalyst Sourcing | data_steward | Confirmed by domain expert |
| SIG-42-HLS-D63Y | Prism Logistics | domain_expert | Cross-referenced with transactions |
| SIG-20-XOX-HJFN | Nexus Materials | system_admin | Auto-mapped, validated |
| SIG-73-KSW-UVZU | Meridian Logistics | system_admin | Cross-referenced with transactions |
| SIG-10-PGH-BTUF | Horizon Sourcing | domain_expert | Cross-referenced with transactions |
| SIG-74-YOY-6KGI | Central Sourcing | data_steward | Historical match confirmed |
| SIG-78-QOY-5RIX | Elite Supply Co. | data_steward | Historical match confirmed |
| SIG-52-QAA-30TZ | Atlantic Sourcing | data_steward | Historical match confirmed |
| SIG-55-IGH-IT3A | Elite Supply Co. | data_steward | Cross-referenced with transactions |
| SIG-52-LXJ-ZU4J | Pinnacle Supply Co. | domain_expert | Auto-mapped, validated |
| SIG-83-CDB-3QOI | Core Sourcing | domain_expert | Auto-mapped, validated |
| SIG-52-HZA-742D | Horizon Materials | data_steward | Confirmed by domain expert |
| SIG-22-HSE-KSCU | Continental Logistics | system_admin | Verified via product specs |
| SIG-43-FST-BKJ7 | Atlantic Sourcing | data_steward | Auto-mapped, validated |
| SIG-55-DBH-2QS3 | Catalyst Sourcing | data_steward | Historical match confirmed |
| SIG-36-RVG-E4FG | Zenith Supply Co. | data_steward | Confirmed by domain expert |
| SIG-56-XKR-5XPI | Nordic Logistics | system_admin | Historical match confirmed |
| SIG-75-QRF-XA0H | Continental Logistics | data_steward | Cross-referenced with transactions |
| SIG-57-GUP-S7UK | Baltic Supply Co. | domain_expert | Cross-referenced with transactions |
| SIG-66-DRZ-QEHY | Prism Sourcing | domain_expert | Historical match confirmed |
| SIG-72-YVG-ZCUK | Meridian Sourcing | system_admin | Auto-mapped, validated |
| SIG-37-ULH-Q8G9 | Nordic Supply Co. | data_steward | Verified via product specs |
| SIG-70-DIO-0E7N | Baltic Supply Co. | data_steward | Historical match confirmed |
| SIG-54-BLS-33OX | Pacific Materials | data_steward | Auto-mapped, validated |
| SIG-13-PHC-GSY7 | Quantum Supply Co. | system_admin | Confirmed by domain expert |
| SIG-23-PGX-VBNK | Stellar Supply Co. | data_steward | Historical match confirmed |
| SIG-81-AMW-NE5V | Stratos Materials | domain_expert | Confirmed by domain expert |
| SIG-16-VOB-VAOG | Nexus Materials | data_steward | Auto-mapped, validated |
| SIG-39-UNC-LQ6C | Elite Materials | system_admin | Auto-mapped, validated |
| SIG-50-BLC-3NYL | Apex Sourcing | domain_expert | Auto-mapped, validated |
| SIG-21-DOL-82H3 | Atlas Sourcing | data_steward | Auto-mapped, validated |
| SIG-62-AQF-O1V3 | Pacific Materials | data_steward | Cross-referenced with transactions |
| SIG-97-BAE-XNL8 | Vertex Logistics | system_admin | Auto-mapped, validated |
| SIG-43-TPO-RSBY | Continental Logistics | system_admin | Cross-referenced with transactions |
| SIG-56-YYA-I8SV | Pinnacle Materials | domain_expert | Verified via product specs |
| SIG-90-YRJ-4LRE | Pacific Supply Co. | domain_expert | Cross-referenced with transactions |
| SIG-28-SOZ-K6XK | Horizon Logistics | system_admin | Confirmed by domain expert |
| SIG-43-TBS-C6P3 | Quantum Logistics | data_steward | Verified via product specs |
| SIG-83-ILY-GUL2 | Apex Sourcing | domain_expert | Confirmed by domain expert |
| SIG-86-EKJ-RFVB | Meridian Materials | system_admin | Historical match confirmed |
| SIG-94-DAC-86F9 | Stellar Logistics | data_steward | Historical match confirmed |
| SIG-40-DFI-FC5R | Prism Supply Co. | data_steward | Cross-referenced with transactions |
| SIG-22-SOG-POO8 | Apex Logistics | data_steward | Confirmed by domain expert |
| SIG-15-GJL-MVIC | Premier Supply Co. | domain_expert | Historical match confirmed |
| SIG-75-GGJ-DK9O | Zenith Logistics | domain_expert | Historical match confirmed |
| SIG-98-LSP-BA0T | Pinnacle Sourcing | system_admin | Historical match confirmed |
| SIG-27-BVB-SWG6 | Horizon Sourcing | data_steward | Verified via product specs |
| SIG-83-GEN-QNXZ | Vertex Sourcing | domain_expert | Verified via product specs |
| SIG-70-KJX-6V9L | Stratos Sourcing | domain_expert | Auto-mapped, validated |
| SIG-30-YVL-ML15 | Pinnacle Materials | system_admin | Confirmed by domain expert |
| SIG-38-BKW-2ZX1 | Pacific Materials | data_steward | Historical match confirmed |
| SIG-86-PYU-PCGN | Continental Supply Co. | system_admin | Confirmed by domain expert |
| SIG-93-AHJ-EAD0 | Nexus Materials | domain_expert | Auto-mapped, validated |
| SIG-63-MSP-S6JE | Core Materials | data_steward | Cross-referenced with transactions |
| SIG-19-GAY-Z6O1 | Atlas Materials | domain_expert | Auto-mapped, validated |
| SIG-10-WVJ-8X4Y | Meridian Supply Co. | domain_expert | Historical match confirmed |
| SIG-78-RHA-RJD1 | Nordic Logistics | system_admin | Cross-referenced with transactions |
| SIG-58-MPE-EIKZ | Atlantic Supply Co. | system_admin | Cross-referenced with transactions |
| SIG-97-UWA-JWLN | Catalyst Materials | system_admin | Auto-mapped, validated |
| SIG-71-AYH-7PWP | Zenith Sourcing | system_admin | Historical match confirmed |
| SIG-35-IQA-J92D | Continental Sourcing | domain_expert | Cross-referenced with transactions |
| SIG-38-FPC-A25N | Stratos Sourcing | system_admin | Auto-mapped, validated |
| SIG-65-TTX-PCJA | Pinnacle Logistics | system_admin | Auto-mapped, validated |
| SIG-66-UEK-CKJ1 | Premier Supply Co. | domain_expert | Historical match confirmed |
| SIG-14-XJN-JI7U | Atlantic Materials | data_steward | Auto-mapped, validated |
| SIG-28-SXX-AKUN | Meridian Materials | data_steward | Auto-mapped, validated |
| SIG-74-WMW-Q37H | Pinnacle Materials | data_steward | Auto-mapped, validated |
| SIG-59-TEL-K01C | Prism Materials | domain_expert | Confirmed by domain expert |
| SIG-26-NTJ-I6T6 | Central Logistics | domain_expert | Verified via product specs |
| SIG-94-WFR-FI07 | Elite Logistics | domain_expert | Confirmed by domain expert |
| SIG-21-KXC-KAGD | Premier Logistics | domain_expert | Auto-mapped, validated |
| SIG-62-DCP-L2AF | Nexus Logistics | domain_expert | Verified via product specs |
| SIG-21-DAC-5SA1 | Global Logistics | system_admin | Cross-referenced with transactions |
| SIG-66-HXC-DMKU | Core Sourcing | data_steward | Confirmed by domain expert |
| SIG-32-ETO-4DT1 | Elite Materials | domain_expert | Confirmed by domain expert |
| SIG-90-AUH-5HQ5 | Vertex Sourcing | data_steward | Confirmed by domain expert |
| SIG-70-ROA-COR7 | Global Materials | domain_expert | Historical match confirmed |
| SIG-76-GFL-RYI0 | Vertex Materials | domain_expert | Auto-mapped, validated |
| SIG-96-AIP-QDS0 | Catalyst Sourcing | data_steward | Cross-referenced with transactions |
| SIG-50-QXM-GFI4 | Nexus Materials | data_steward | Cross-referenced with transactions |
| SIG-30-IBO-NKXL | Pacific Logistics | domain_expert | Cross-referenced with transactions |
| SIG-55-KQD-CQMQ | Pacific Sourcing | domain_expert | Auto-mapped, validated |
| SIG-46-DGC-R6Z2 | Quantum Supply Co. | domain_expert | Verified via product specs |
| SIG-60-IXG-GXQ7 | Pacific Sourcing | system_admin | Confirmed by domain expert |
| SIG-60-OHC-5EQB | Meridian Logistics | data_steward | Auto-mapped, validated |
| SIG-76-ESC-PNV7 | Prism Sourcing | system_admin | Confirmed by domain expert |
| SIG-61-ZIT-092H | Vanguard Materials | system_admin | Auto-mapped, validated |
| SIG-14-GCI-G4Q9 | Stratos Logistics | system_admin | Confirmed by domain expert |
| SIG-17-ITM-ARYQ | Catalyst Supply Co. | system_admin | Auto-mapped, validated |
| SIG-20-RSZ-19RE | Pinnacle Supply Co. | domain_expert | Verified via product specs |
| SIG-62-BUT-A292 | Atlantic Materials | domain_expert | Cross-referenced with transactions |
| SIG-26-LKL-4NI1 | Atlas Supply Co. | domain_expert | Confirmed by domain expert |
| SIG-98-OYH-5RPI | Atlantic Supply Co. | data_steward | Auto-mapped, validated |
| SIG-86-NGE-LKTW | Quantum Supply Co. | domain_expert | Verified via product specs |
| SIG-73-YMY-EMYO | Baltic Materials | data_steward | Verified via product specs |
| SIG-68-BPW-3DSD | Pacific Materials | data_steward | Cross-referenced with transactions |
| SIG-30-QPI-FZVD | Stellar Supply Co. | system_admin | Auto-mapped, validated |
| SIG-55-FLO-S4MU | Stratos Logistics | data_steward | Confirmed by domain expert |
| SIG-67-NQK-GXJE | Core Logistics | data_steward | Historical match confirmed |
| SIG-66-OHB-GQIX | Elite Logistics | domain_expert | Verified via product specs |
| SIG-40-DVL-7PTV | Premier Logistics | system_admin | Verified via product specs |
| SIG-19-PNU-HKF3 | Atlantic Sourcing | domain_expert | Cross-referenced with transactions |
| SIG-23-TWA-K947 | Pinnacle Supply Co. | domain_expert | Auto-mapped, validated |
| SIG-53-USG-KW3Q | Baltic Sourcing | domain_expert | Historical match confirmed |
| SIG-33-IWB-UV4J | Core Sourcing | data_steward | Historical match confirmed |
| SIG-47-TWQ-0FLA | Premier Sourcing | system_admin | Historical match confirmed |
| SIG-72-KAT-NI1G | Prime Materials | system_admin | Auto-mapped, validated |
| SIG-52-NEO-FFB3 | Central Materials | domain_expert | Confirmed by domain expert |
| SIG-68-LYO-7YQ5 | Stratos Materials | data_steward | Verified via product specs |
| SIG-47-TCL-S6FG | Meridian Materials | domain_expert | Auto-mapped, validated |
| SIG-90-ALF-TQ8F | Atlantic Sourcing | data_steward | Historical match confirmed |
| SIG-51-MQP-ZO0K | Baltic Sourcing | system_admin | Verified via product specs |
| SIG-11-EIQ-WD14 | Atlas Materials | system_admin | Verified via product specs |
| SIG-90-NFZ-XRLG | Nexus Sourcing | domain_expert | Historical match confirmed |
| SIG-40-WLB-9IFD | Vanguard Supply Co. | data_steward | Historical match confirmed |
| SIG-52-QOU-LC66 | Catalyst Materials | system_admin | Verified via product specs |
| SIG-39-EWA-Q37M | Atlantic Logistics | data_steward | Cross-referenced with transactions |
| SIG-99-AZM-B4OF | Apex Sourcing | data_steward | Verified via product specs |
| SIG-50-PNF-Z2E8 | Apex Supply Co. | system_admin | Confirmed by domain expert |
| SIG-71-FHA-CSOA | Apex Supply Co. | domain_expert | Confirmed by domain expert |
| SIG-60-VTH-H7AM | Atlas Sourcing | system_admin | Cross-referenced with transactions |
| SIG-42-BSJ-L2CG | Vanguard Logistics | domain_expert | Auto-mapped, validated |
| SIG-79-UJC-1RKG | Nordic Materials | domain_expert | Verified via product specs |
| SIG-80-OEM-5LVP | Pinnacle Sourcing | domain_expert | Confirmed by domain expert |
| SIG-27-FHB-EY0E | Atlas Supply Co. | domain_expert | Verified via product specs |
| SIG-23-CJO-TSA9 | Meridian Logistics | domain_expert | Cross-referenced with transactions |
| SIG-92-ZAC-Y2PV | Pinnacle Supply Co. | system_admin | Historical match confirmed |
| SIG-91-MIT-AG2L | Pacific Logistics | data_steward | Cross-referenced with transactions |
| SIG-46-AAW-27BR | Stellar Logistics | data_steward | Cross-referenced with transactions |
| SIG-58-BDQ-I1V3 | Core Supply Co. | system_admin | Cross-referenced with transactions |
| SIG-58-MKV-8WKD | Vanguard Supply Co. | data_steward | Confirmed by domain expert |
| SIG-39-CJT-QHM3 | Stellar Materials | system_admin | Cross-referenced with transactions |
| SIG-63-NTB-209C | Zenith Supply Co. | data_steward | Historical match confirmed |
| SIG-45-JPK-6R81 | Nexus Materials | system_admin | Historical match confirmed |
| SIG-94-XEY-KPJ5 | Atlantic Sourcing | data_steward | Historical match confirmed |
| SIG-48-AKK-L4CQ | Prism Logistics | system_admin | Auto-mapped, validated |
| SIG-42-FYL-6VKE | Catalyst Materials | system_admin | Cross-referenced with transactions |
| SIG-44-OML-OIX0 | Prime Materials | data_steward | Historical match confirmed |
| SIG-43-XDN-7VEU | Vat Reduced GB 15% | domain_expert | Auto-mapped, validated |
| SIG-37-QAD-9FMK | Excise NL 0% | domain_expert | Cross-referenced with transactions |
| SIG-57-YNC-H4UX | Excise DE 21% | data_steward | Cross-referenced with transactions |
| SIG-87-SQR-587P | Vat Standard NL 25% | domain_expert | Verified via product specs |
| SIG-87-QEL-QGIW | Customs Duty FR 7% | system_admin | Cross-referenced with transactions |
| SIG-48-OWU-RTGZ | Withholding GB 5% | domain_expert | Verified via product specs |
| SIG-51-CZK-SBJH | Customs Duty CN 0% | system_admin | Confirmed by domain expert |
| SIG-48-KTU-I0WF | Vat Standard GB 21% | system_admin | Confirmed by domain expert |
| SIG-44-UKH-MO4F | Vat Standard DE 19% | data_steward | Auto-mapped, validated |
| SIG-94-NQF-0YQV | Withholding US 25% | domain_expert | Verified via product specs |
| SIG-67-RMU-WA6Y | Customs Duty GB 5% | system_admin | Confirmed by domain expert |
| SIG-77-AEN-CA8D | Vat Standard NL 20% | system_admin | Confirmed by domain expert |
| SIG-47-UEJ-M3SA | Withholding BR 15% | system_admin | Confirmed by domain expert |
| SIG-81-LGY-1IAH | Vat Standard NL 20% | domain_expert | Cross-referenced with transactions |
| SIG-63-KZG-DVKO | Withholding US 0% | system_admin | Verified via product specs |
| SIG-70-HCT-Q44C | Vat Reduced CN 21% | domain_expert | Confirmed by domain expert |
| SIG-95-LOJ-S1L2 | Withholding NL 7% | domain_expert | Verified via product specs |
| SIG-41-EOV-7THY | Excise IN 21% | data_steward | Historical match confirmed |
| SIG-33-DJA-PDEO | Vat Standard NL 19% | domain_expert | Historical match confirmed |
| SIG-93-VLZ-VI4P | Vat Standard DE 10% | data_steward | Cross-referenced with transactions |
| SIG-33-OUH-D09D | Vat Standard US 5% | domain_expert | Historical match confirmed |
| SIG-54-MUH-KY6K | Excise FR 0% | domain_expert | Auto-mapped, validated |
| SIG-27-GRI-K7JV | Excise BR 10% | domain_expert | Verified via product specs |
| SIG-97-QNX-7TWO | Excise IN 15% | system_admin | Confirmed by domain expert |
| SIG-73-GRJ-1VRU | Vat Standard GB 21% | domain_expert | Auto-mapped, validated |
| SIG-99-NVH-7WS3 | Excise IN 25% | domain_expert | Auto-mapped, validated |
| SIG-30-PPI-DU4D | Vat Reduced BR 21% | system_admin | Historical match confirmed |
| SIG-34-NMZ-KBWT | Vat Standard BR 0% | domain_expert | Verified via product specs |
| SIG-98-NDY-OCEW | Vat Standard FR 25% | domain_expert | Confirmed by domain expert |
| SIG-97-MKG-5MHN | Vat Reduced CN 19% | domain_expert | Auto-mapped, validated |
| SIG-67-GQM-MLNT | Withholding GB 21% | data_steward | Cross-referenced with transactions |
| SIG-78-MNL-57SN | Vat Reduced BR 25% | data_steward | Confirmed by domain expert |
| SIG-75-AOD-U2ER | Vat Standard DE 7% | data_steward | Historical match confirmed |
| SIG-99-BQS-KC4Q | Vat Standard BR 0% | system_admin | Verified via product specs |
| SIG-55-EGS-MYD1 | Vat Standard GB 20% | data_steward | Cross-referenced with transactions |
| SIG-22-THR-75G4 | Customs Duty IN 5% | system_admin | Confirmed by domain expert |
| SIG-83-TFE-M3DZ | Customs Duty DE 5% | system_admin | Confirmed by domain expert |
| SIG-76-SFN-GRTJ | Vat Reduced GB 19% | system_admin | Auto-mapped, validated |
| SIG-74-SAC-3HZG | Excise BR 15% | system_admin | Confirmed by domain expert |
| SIG-72-TXC-IWF9 | Vat Reduced FR 25% | data_steward | Verified via product specs |
| SIG-62-JTP-RUMX | Vat Standard US 10% | system_admin | Verified via product specs |
| SIG-97-MAR-CXAJ | Withholding NL 7% | data_steward | Confirmed by domain expert |
| SIG-44-ZGN-CNIV | Excise NL 7% | system_admin | Auto-mapped, validated |
| SIG-98-AVJ-SOX9 | Customs Duty DE 15% | system_admin | Cross-referenced with transactions |
| SIG-87-KZL-I3ZY | Excise US 15% | system_admin | Cross-referenced with transactions |
| SIG-27-EAF-CA57 | Withholding DE 25% | system_admin | Auto-mapped, validated |
| SIG-30-UPN-JYVW | Withholding US 10% | data_steward | Historical match confirmed |
| SIG-52-FQK-88IF | Excise NL 21% | domain_expert | Verified via product specs |
| SIG-97-SMQ-9SG6 | Excise US 19% | data_steward | Historical match confirmed |
| SIG-32-NVJ-H1RC | Excise DE 21% | domain_expert | Auto-mapped, validated |
| SIG-13-DJH-ML2N | Withholding FR 21% | domain_expert | Historical match confirmed |
| SIG-51-RJJ-5BIE | Vat Reduced BR 7% | domain_expert | Auto-mapped, validated |
| SIG-50-TGM-XVD2 | Vat Reduced IN 20% | data_steward | Cross-referenced with transactions |
| SIG-75-CPF-OOJ3 | Vat Reduced BR 0% | system_admin | Cross-referenced with transactions |
| SIG-20-IMA-GJKF | Vat Standard NL 5% | data_steward | Historical match confirmed |
| SIG-34-TKJ-QFOY | Vat Reduced BR 15% | domain_expert | Historical match confirmed |
| SIG-10-NNQ-6CGO | Vat Reduced FR 0% | data_steward | Verified via product specs |
| SIG-49-FLB-3KJ2 | Customs Duty US 10% | system_admin | Cross-referenced with transactions |
| SIG-89-KYU-M9RA | Customs Duty CN 10% | system_admin | Verified via product specs |
| SIG-90-NAM-FDV1 | Excise IN 20% | system_admin | Historical match confirmed |
| SIG-43-KPC-8R3Y | Vat Reduced BR 21% | system_admin | Auto-mapped, validated |
| SIG-43-KWZ-BU3P | Vat Standard DE 19% | domain_expert | Cross-referenced with transactions |
| SIG-55-OPY-GVTN | Vat Reduced NL 19% | data_steward | Auto-mapped, validated |
| SIG-59-JAB-QS66 | Customs Duty US 15% | system_admin | Verified via product specs |
| SIG-74-EPP-R9AG | Vat Reduced US 19% | system_admin | Verified via product specs |
| SIG-44-NHM-IY9D | Withholding FR 5% | data_steward | Confirmed by domain expert |
| SIG-28-HHW-S34S | Excise NL 20% | domain_expert | Cross-referenced with transactions |
| SIG-31-BWX-FDET | Vat Standard IN 10% | system_admin | Cross-referenced with transactions |
| SIG-72-CRV-0OZ3 | Customs Duty CN 25% | system_admin | Verified via product specs |
| SIG-52-LHT-XBI2 | Customs Duty US 19% | domain_expert | Auto-mapped, validated |
| SIG-42-QOC-A3JP | Vat Standard CN 10% | system_admin | Cross-referenced with transactions |
| SIG-73-SXI-8HSL | Customs Duty DE 5% | data_steward | Verified via product specs |
| SIG-22-ADK-3T78 | Excise DE 10% | data_steward | Confirmed by domain expert |
| SIG-30-MCM-OXZ5 | Excise GB 0% | domain_expert | Historical match confirmed |
| SIG-88-YRN-7S19 | Vat Reduced CN 5% | system_admin | Cross-referenced with transactions |
| SIG-51-MVX-XKUB | Vat Reduced BR 15% | domain_expert | Historical match confirmed |
| SIG-19-JRR-02SD | Customs Duty IN 25% | system_admin | Auto-mapped, validated |
| SIG-20-CDH-FE8F | Excise US 20% | domain_expert | Confirmed by domain expert |
| SIG-83-SCO-PIKN | Excise NL 15% | data_steward | Cross-referenced with transactions |
| SIG-92-NWY-1FV5 | Vat Standard US 7% | data_steward | Historical match confirmed |
| SIG-72-IQP-IKAX | Customs Duty IN 21% | system_admin | Historical match confirmed |
| SIG-11-HHQ-JHKO | Customs Duty BR 7% | data_steward | Verified via product specs |
| SIG-49-VSP-V4PV | Withholding BR 10% | system_admin | Historical match confirmed |
| SIG-31-LNL-F2NC | Vat Standard NL 20% | data_steward | Auto-mapped, validated |
| SIG-30-PKD-LW8B | Vat Standard NL 19% | system_admin | Historical match confirmed |
| SIG-98-QRC-XOOW | Customs Duty DE 0% | domain_expert | Auto-mapped, validated |
| SIG-38-LEZ-M2KS | Vat Reduced CN 19% | domain_expert | Auto-mapped, validated |
| SIG-92-SMV-JF74 | Vat Reduced NL 0% | domain_expert | Verified via product specs |
| SIG-20-GIF-RAEQ | Excise DE 10% | data_steward | Confirmed by domain expert |
| SIG-53-IAB-UGH9 | Customs Duty CN 25% | system_admin | Auto-mapped, validated |
| SIG-30-PQC-HUIU | Withholding FR 5% | data_steward | Historical match confirmed |
| SIG-51-DNC-4AET | Vat Standard IN 5% | data_steward | Historical match confirmed |
| SIG-47-MRM-FIIH | Vat Reduced US 7% | domain_expert | Auto-mapped, validated |
| SIG-38-ZZL-D5F0 | Customs Duty GB 0% | system_admin | Historical match confirmed |
| SIG-23-FHN-ZAFZ | Customs Duty GB 5% | system_admin | Cross-referenced with transactions |
| SIG-15-HZV-LHQ2 | Customs Duty CN 7% | data_steward | Verified via product specs |
| SIG-90-RCW-71K4 | Customs Duty DE 0% | data_steward | Historical match confirmed |
| SIG-28-MGE-0MBB | Customs Duty DE 20% | data_steward | Verified via product specs |
| SIG-98-LPL-XFDL | Vat Standard GB 19% | data_steward | Auto-mapped, validated |
| SIG-47-TWK-RYLY | Customs Duty FR 7% | data_steward | Auto-mapped, validated |
| SIG-48-BCI-7SYR | Vat Standard IN 19% | system_admin | Auto-mapped, validated |
| SIG-47-UOO-GQED | Withholding CN 20% | data_steward | Verified via product specs |
| SIG-25-WCC-PPMH | Excise US 7% | domain_expert | Historical match confirmed |
| SIG-76-XDH-Q3Q4 | Vat Standard NL 5% | data_steward | Cross-referenced with transactions |
| SIG-45-NEB-M5RE | Withholding BR 20% | domain_expert | Verified via product specs |
| SIG-55-NJY-I13Y | Vat Reduced CN 19% | domain_expert | Cross-referenced with transactions |
| SIG-41-SEX-2DFF | Customs Duty NL 5% | domain_expert | Historical match confirmed |
| SIG-58-EJN-NRGO | Customs Duty IN 20% | domain_expert | Historical match confirmed |
| SIG-89-HHQ-75TJ | Excise GB 5% | data_steward | Verified via product specs |
| SIG-24-KLH-SHKW | Customs Duty GB 15% | data_steward | Confirmed by domain expert |
| SIG-26-WVS-AQ3B | Vat Reduced FR 20% | data_steward | Cross-referenced with transactions |
| SIG-15-IUN-M051 | Vat Standard US 21% | domain_expert | Auto-mapped, validated |
| SIG-59-OPA-P4E0 | Excise US 5% | system_admin | Cross-referenced with transactions |
| SIG-75-NYN-Q2N4 | Customs Duty GB 5% | system_admin | Historical match confirmed |
| SIG-42-EYO-WK0H | Vat Standard NL 20% | data_steward | Historical match confirmed |
| SIG-38-OTV-E78M | Withholding CN 0% | domain_expert | Verified via product specs |
| SIG-49-YEY-OY3L | Customs Duty CN 0% | domain_expert | Confirmed by domain expert |
| SIG-58-SWU-PQGW | Excise CN 21% | domain_expert | Auto-mapped, validated |
| SIG-46-BCJ-SSEN | Customs Duty GB 0% | system_admin | Cross-referenced with transactions |
| SIG-79-PSV-943Y | Excise DE 21% | data_steward | Confirmed by domain expert |
| SIG-97-FYC-MHAR | Withholding IN 10% | domain_expert | Auto-mapped, validated |
| SIG-45-QQC-Z4N0 | Excise CN 20% | domain_expert | Historical match confirmed |
| SIG-53-NKW-4MNF | Vat Reduced GB 15% | domain_expert | Historical match confirmed |
| SIG-65-SCG-WZ5H | Excise CN 25% | data_steward | Verified via product specs |
| SIG-56-BHM-X0GI | Excise NL 0% | domain_expert | Verified via product specs |
| SIG-92-KVS-DDEE | Withholding NL 19% | system_admin | Cross-referenced with transactions |
| SIG-65-QKW-Y1YW | Vat Reduced NL 25% | domain_expert | Confirmed by domain expert |
| SIG-95-UXH-C9M4 | Customs Duty NL 7% | data_steward | Confirmed by domain expert |
| SIG-74-VWV-7YSU | Vat Reduced GB 0% | system_admin | Auto-mapped, validated |
| SIG-31-FGA-64VZ | Withholding NL 20% | domain_expert | Cross-referenced with transactions |
| SIG-53-ZZI-QU56 | Excise FR 19% | system_admin | Verified via product specs |
| SIG-13-XOQ-WLDV | Withholding IN 20% | domain_expert | Cross-referenced with transactions |
| SIG-67-YOR-JCUH | Excise FR 21% | domain_expert | Historical match confirmed |
| SIG-76-RUI-UC1S | Customs Duty NL 25% | domain_expert | Verified via product specs |
| SIG-56-MIF-2O9D | Customs Duty GB 7% | domain_expert | Confirmed by domain expert |
| SIG-92-RHW-233J | Customs Duty IN 5% | domain_expert | Verified via product specs |
| SIG-30-TUW-0P7F | Customs Duty NL 21% | domain_expert | Historical match confirmed |
| SIG-80-ZKZ-ANXJ | Withholding NL 5% | domain_expert | Verified via product specs |
| SIG-81-SZZ-3RNH | Vat Standard NL 19% | data_steward | Confirmed by domain expert |
| SIG-31-GVB-1WH0 | Customs Duty US 20% | system_admin | Historical match confirmed |
| SIG-42-UMA-WZ7F | Customs Duty DE 15% | system_admin | Auto-mapped, validated |
| SIG-69-MNI-DH5B | Excise NL 10% | system_admin | Cross-referenced with transactions |
| SIG-35-RSV-01YT | Vat Reduced GB 25% | domain_expert | Auto-mapped, validated |
| SIG-46-DQX-JN7N | Customs Duty BR 15% | system_admin | Historical match confirmed |
| SIG-21-VZE-Q2WM | Withholding NL 15% | domain_expert | Historical match confirmed |
| SIG-20-IKV-891D | Vat Reduced NL 15% | domain_expert | Historical match confirmed |
| SIG-51-HUK-F1HG | Customs Duty DE 20% | system_admin | Confirmed by domain expert |
| SIG-65-QDW-KJG8 | Withholding NL 21% | data_steward | Historical match confirmed |
| SIG-92-PYF-X5ZO | Vat Reduced IN 25% | system_admin | Cross-referenced with transactions |
| SIG-94-MKW-LH8F | Customs Duty CN 19% | domain_expert | Confirmed by domain expert |
| SIG-69-TRZ-SFLQ | Excise FR 21% | domain_expert | Historical match confirmed |
| SIG-49-DCM-ASFC | Vat Standard US 15% | domain_expert | Confirmed by domain expert |
| SIG-43-SSK-5L22 | Vat Standard FR 0% | system_admin | Cross-referenced with transactions |
| SIG-73-RIN-8RXQ | Customs Duty FR 25% | system_admin | Cross-referenced with transactions |
| SIG-94-AFM-7IJJ | Vat Reduced FR 5% | system_admin | Confirmed by domain expert |
| SIG-73-DNT-OVXU | Vat Reduced IN 5% | system_admin | Verified via product specs |
| SIG-48-WVJ-F5TN | Vat Standard CN 19% | domain_expert | Auto-mapped, validated |
| SIG-40-IFK-RPIG | Vat Standard DE 7% | domain_expert | Historical match confirmed |
| SIG-56-MNF-4JPL | Vat Standard CN 19% | domain_expert | Auto-mapped, validated |

#### 4.3.3 Excluded Mappings

Provisional mappings pending business validation:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-2824-A | Invalid Entry 859 | Data quality insufficient |
| NOISE-4657-C | Invalid Entry 854 | Out of scope per business decision |
| NOISE-9935-B | Invalid Entry 704 | Out of scope per business decision |
| NOISE-1488-B | Invalid Entry 323 | Duplicate detected |
| NOISE-1434-D | Invalid Entry 833 | Duplicate detected |
| NOISE-4611-H | Invalid Entry 703 | Pending validation |
| NOISE-3615-G | Invalid Entry 448 | Superseded by newer mapping |
| NOISE-4527-F | Invalid Entry 204 | Pending validation |
| NOISE-2584-F | Invalid Entry 967 | Duplicate detected |
| NOISE-5333-A | Invalid Entry 847 | Pending validation |
| NOISE-3045-G | Invalid Entry 180 | Out of scope per business decision |
| NOISE-6925-D | Invalid Entry 821 | Out of scope per business decision |
| NOISE-4733-E | Invalid Entry 181 | Duplicate detected |
| NOISE-7227-E | Invalid Entry 564 | Duplicate detected |
| NOISE-7065-F | Invalid Entry 314 | Pending validation |
| NOISE-2169-C | Invalid Entry 646 | Pending validation |
| NOISE-8573-G | Invalid Entry 376 | Out of scope per business decision |
| NOISE-6313-A | Invalid Entry 334 | Superseded by newer mapping |
| NOISE-7572-E | Invalid Entry 167 | Superseded by newer mapping |
| NOISE-6155-D | Invalid Entry 771 | Duplicate detected |
| NOISE-8517-C | Invalid Entry 371 | Pending validation |
| NOISE-9830-E | Invalid Entry 864 | Superseded by newer mapping |
| NOISE-7543-F | Invalid Entry 324 | Pending validation |
| NOISE-9085-B | Invalid Entry 873 | Data quality insufficient |
| NOISE-3504-C | Invalid Entry 911 | Out of scope per business decision |
| NOISE-2040-G | Invalid Entry 490 | Pending validation |
| NOISE-9669-E | Invalid Entry 666 | Pending validation |
| NOISE-2876-E | Invalid Entry 887 | Pending validation |
| NOISE-5808-G | Invalid Entry 261 | Superseded by newer mapping |
| NOISE-5315-C | Invalid Entry 619 | Pending validation |
| NOISE-5889-D | Invalid Entry 256 | Data quality insufficient |
| NOISE-9837-A | Invalid Entry 713 | Superseded by newer mapping |
| NOISE-1319-B | Invalid Entry 471 | Duplicate detected |
| NOISE-1949-D | Invalid Entry 999 | Duplicate detected |
| NOISE-2403-H | Invalid Entry 935 | Out of scope per business decision |
| NOISE-3060-C | Invalid Entry 775 | Data quality insufficient |
| NOISE-3705-E | Invalid Entry 640 | Pending validation |
| NOISE-4470-D | Invalid Entry 830 | Data quality insufficient |
| NOISE-7118-H | Invalid Entry 629 | Duplicate detected |
| NOISE-5061-D | Invalid Entry 165 | Pending validation |
| NOISE-4770-D | Invalid Entry 107 | Data quality insufficient |
| NOISE-1964-D | Invalid Entry 169 | Superseded by newer mapping |
| NOISE-2160-D | Invalid Entry 385 | Pending validation |
| NOISE-9834-C | Invalid Entry 840 | Superseded by newer mapping |
| NOISE-8744-D | Invalid Entry 903 | Data quality insufficient |
| NOISE-4119-B | Invalid Entry 199 | Pending validation |
| NOISE-7939-G | Invalid Entry 578 | Out of scope per business decision |
| NOISE-2612-A | Invalid Entry 512 | Out of scope per business decision |
| NOISE-5073-D | Invalid Entry 294 | Duplicate detected |
| NOISE-3296-G | Invalid Entry 287 | Pending validation |
| NOISE-5092-B | Invalid Entry 553 | Data quality insufficient |
| NOISE-1828-A | Invalid Entry 195 | Out of scope per business decision |
| NOISE-7658-H | Invalid Entry 592 | Duplicate detected |
| NOISE-1960-C | Invalid Entry 488 | Pending validation |
| NOISE-5345-H | Invalid Entry 392 | Out of scope per business decision |
| NOISE-8973-C | Invalid Entry 294 | Pending validation |
| NOISE-1958-A | Invalid Entry 865 | Duplicate detected |
| NOISE-1821-H | Invalid Entry 614 | Data quality insufficient |
| NOISE-1931-B | Invalid Entry 971 | Duplicate detected |
| NOISE-2113-D | Invalid Entry 513 | Data quality insufficient |
| NOISE-5033-A | Invalid Entry 734 | Superseded by newer mapping |
| NOISE-9565-F | Invalid Entry 367 | Out of scope per business decision |
| NOISE-6147-D | Invalid Entry 371 | Superseded by newer mapping |
| NOISE-5915-H | Invalid Entry 423 | Data quality insufficient |
| NOISE-8508-B | Invalid Entry 175 | Pending validation |
| NOISE-9288-E | Invalid Entry 235 | Data quality insufficient |
| NOISE-5002-F | Invalid Entry 391 | Data quality insufficient |
| NOISE-9900-E | Invalid Entry 726 | Pending validation |
| NOISE-5905-B | Invalid Entry 999 | Superseded by newer mapping |
| NOISE-2891-B | Invalid Entry 860 | Out of scope per business decision |
| NOISE-5462-E | Invalid Entry 719 | Data quality insufficient |
| NOISE-6617-D | Invalid Entry 803 | Data quality insufficient |
| NOISE-9004-E | Invalid Entry 966 | Out of scope per business decision |
| NOISE-7939-E | Invalid Entry 145 | Data quality insufficient |
| NOISE-3143-E | Invalid Entry 265 | Out of scope per business decision |
| NOISE-8007-A | Invalid Entry 214 | Out of scope per business decision |
| NOISE-3442-A | Invalid Entry 954 | Out of scope per business decision |
| NOISE-3426-G | Invalid Entry 230 | Pending validation |
| NOISE-6974-A | Invalid Entry 466 | Superseded by newer mapping |
| NOISE-5088-B | Invalid Entry 462 | Superseded by newer mapping |
| NOISE-3532-D | Invalid Entry 985 | Duplicate detected |
| NOISE-7755-A | Invalid Entry 283 | Pending validation |
| NOISE-5065-E | Invalid Entry 263 | Duplicate detected |
| NOISE-1634-H | Invalid Entry 327 | Superseded by newer mapping |
| NOISE-6728-E | Invalid Entry 940 | Superseded by newer mapping |
| NOISE-1387-D | Invalid Entry 508 | Superseded by newer mapping |
| NOISE-2137-E | Invalid Entry 459 | Data quality insufficient |
| NOISE-9785-F | Invalid Entry 128 | Duplicate detected |
| NOISE-3925-E | Invalid Entry 139 | Pending validation |
| NOISE-8119-F | Invalid Entry 846 | Duplicate detected |
| NOISE-9379-B | Invalid Entry 494 | Superseded by newer mapping |
| NOISE-5173-A | Invalid Entry 825 | Pending validation |
| NOISE-9518-D | Invalid Entry 472 | Duplicate detected |
| NOISE-6409-F | Invalid Entry 779 | Superseded by newer mapping |
| NOISE-5920-E | Invalid Entry 782 | Superseded by newer mapping |
| NOISE-7592-E | Invalid Entry 667 | Pending validation |
| NOISE-7888-G | Invalid Entry 793 | Out of scope per business decision |
| NOISE-5930-G | Invalid Entry 661 | Pending validation |
| NOISE-5700-D | Invalid Entry 540 | Out of scope per business decision |
| NOISE-6279-H | Invalid Entry 552 | Data quality insufficient |
| NOISE-4501-H | Invalid Entry 912 | Pending validation |
| NOISE-2389-E | Invalid Entry 627 | Out of scope per business decision |
| NOISE-2530-D | Invalid Entry 788 | Duplicate detected |
| NOISE-4262-C | Invalid Entry 125 | Superseded by newer mapping |
| NOISE-8784-B | Invalid Entry 566 | Data quality insufficient |
| NOISE-4185-G | Invalid Entry 606 | Pending validation |
| NOISE-3417-A | Invalid Entry 868 | Out of scope per business decision |
| NOISE-4585-C | Invalid Entry 923 | Duplicate detected |
| NOISE-1822-D | Invalid Entry 968 | Out of scope per business decision |
| NOISE-3184-H | Invalid Entry 783 | Pending validation |
| NOISE-6198-H | Invalid Entry 727 | Out of scope per business decision |
| NOISE-9976-H | Invalid Entry 262 | Pending validation |
| NOISE-5246-D | Invalid Entry 960 | Out of scope per business decision |
| NOISE-8939-D | Invalid Entry 381 | Superseded by newer mapping |
| NOISE-5681-D | Invalid Entry 378 | Pending validation |
| NOISE-9849-B | Invalid Entry 241 | Pending validation |
| NOISE-7275-C | Invalid Entry 823 | Data quality insufficient |
| NOISE-7797-G | Invalid Entry 438 | Superseded by newer mapping |
| NOISE-7812-A | Invalid Entry 311 | Pending validation |
| NOISE-1320-G | Invalid Entry 588 | Duplicate detected |
| NOISE-5892-G | Invalid Entry 973 | Out of scope per business decision |
| NOISE-9947-D | Invalid Entry 599 | Duplicate detected |
| NOISE-8140-H | Invalid Entry 129 | Out of scope per business decision |
| NOISE-7624-C | Invalid Entry 960 | Out of scope per business decision |
| NOISE-9751-A | Invalid Entry 503 | Data quality insufficient |
| NOISE-1444-B | Invalid Entry 758 | Pending validation |
| NOISE-8564-C | Invalid Entry 151 | Out of scope per business decision |
| NOISE-6363-D | Invalid Entry 565 | Data quality insufficient |
| NOISE-7211-E | Invalid Entry 870 | Duplicate detected |
| NOISE-2341-H | Invalid Entry 119 | Data quality insufficient |
| NOISE-6733-D | Invalid Entry 765 | Duplicate detected |
| NOISE-1659-A | Invalid Entry 353 | Pending validation |
| NOISE-3496-D | Invalid Entry 229 | Out of scope per business decision |
| NOISE-2874-D | Invalid Entry 576 | Superseded by newer mapping |
| NOISE-3749-B | Invalid Entry 896 | Duplicate detected |
| NOISE-2771-A | Invalid Entry 419 | Out of scope per business decision |
| NOISE-7149-G | Invalid Entry 832 | Superseded by newer mapping |
| NOISE-4978-B | Invalid Entry 813 | Superseded by newer mapping |
| NOISE-2983-A | Invalid Entry 455 | Duplicate detected |
| NOISE-7071-B | Invalid Entry 618 | Out of scope per business decision |
| NOISE-7882-H | Invalid Entry 208 | Superseded by newer mapping |
| NOISE-8532-C | Invalid Entry 545 | Data quality insufficient |
| NOISE-9548-E | Invalid Entry 730 | Data quality insufficient |
| NOISE-8616-G | Invalid Entry 945 | Out of scope per business decision |
| NOISE-6280-D | Invalid Entry 950 | Pending validation |
| NOISE-8385-D | Invalid Entry 868 | Data quality insufficient |
| NOISE-7209-F | Invalid Entry 129 | Duplicate detected |
| NOISE-3979-H | Invalid Entry 317 | Out of scope per business decision |
| NOISE-6576-E | Invalid Entry 710 | Superseded by newer mapping |
| NOISE-1166-D | Invalid Entry 187 | Data quality insufficient |
| NOISE-7658-H | Invalid Entry 668 | Out of scope per business decision |
| NOISE-8800-H | Invalid Entry 558 | Out of scope per business decision |
| NOISE-5820-D | Invalid Entry 514 | Pending validation |
| NOISE-7046-H | Invalid Entry 666 | Superseded by newer mapping |
| NOISE-7971-F | Invalid Entry 460 | Superseded by newer mapping |
| NOISE-6023-E | Invalid Entry 336 | Superseded by newer mapping |
| NOISE-4155-F | Invalid Entry 222 | Duplicate detected |
| NOISE-4033-D | Invalid Entry 321 | Out of scope per business decision |
| NOISE-9595-E | Invalid Entry 202 | Duplicate detected |
| NOISE-4727-F | Invalid Entry 283 | Duplicate detected |
| NOISE-9751-C | Invalid Entry 380 | Out of scope per business decision |
| NOISE-5786-C | Invalid Entry 753 | Superseded by newer mapping |
| NOISE-1200-E | Invalid Entry 580 | Out of scope per business decision |
| NOISE-6582-C | Invalid Entry 152 | Pending validation |
| NOISE-2869-B | Invalid Entry 510 | Out of scope per business decision |
| NOISE-1878-C | Invalid Entry 252 | Out of scope per business decision |
| NOISE-2395-D | Invalid Entry 221 | Data quality insufficient |
| NOISE-4697-G | Invalid Entry 561 | Pending validation |
| NOISE-8025-E | Invalid Entry 682 | Data quality insufficient |
| NOISE-2625-D | Invalid Entry 740 | Superseded by newer mapping |
| NOISE-2330-C | Invalid Entry 345 | Superseded by newer mapping |
| NOISE-2229-C | Invalid Entry 102 | Pending validation |
| NOISE-8699-E | Invalid Entry 133 | Duplicate detected |
| NOISE-5632-H | Invalid Entry 172 | Out of scope per business decision |
| NOISE-4241-G | Invalid Entry 217 | Data quality insufficient |
| NOISE-3441-E | Invalid Entry 946 | Pending validation |
| NOISE-1977-C | Invalid Entry 911 | Data quality insufficient |
| NOISE-5728-H | Invalid Entry 227 | Out of scope per business decision |
| NOISE-5982-G | Invalid Entry 378 | Duplicate detected |
| NOISE-9090-H | Invalid Entry 182 | Data quality insufficient |
| NOISE-8078-F | Invalid Entry 718 | Pending validation |
| NOISE-2496-D | Invalid Entry 790 | Out of scope per business decision |
| NOISE-1339-E | Invalid Entry 690 | Out of scope per business decision |
| NOISE-8708-H | Invalid Entry 384 | Duplicate detected |
| NOISE-8141-H | Invalid Entry 193 | Pending validation |
| NOISE-7690-F | Invalid Entry 428 | Out of scope per business decision |
| NOISE-6403-G | Invalid Entry 810 | Data quality insufficient |
| NOISE-7561-A | Invalid Entry 565 | Superseded by newer mapping |
| NOISE-5135-F | Invalid Entry 218 | Pending validation |
| NOISE-1018-H | Invalid Entry 523 | Data quality insufficient |
| NOISE-9494-F | Invalid Entry 737 | Duplicate detected |
| NOISE-8242-A | Invalid Entry 308 | Duplicate detected |
| NOISE-3146-E | Invalid Entry 548 | Out of scope per business decision |
| NOISE-1472-D | Invalid Entry 826 | Duplicate detected |
| NOISE-1224-G | Invalid Entry 195 | Superseded by newer mapping |
| NOISE-8560-B | Invalid Entry 763 | Data quality insufficient |
| NOISE-5781-E | Invalid Entry 525 | Pending validation |
| NOISE-4993-H | Invalid Entry 664 | Out of scope per business decision |
| NOISE-4122-C | Invalid Entry 984 | Pending validation |
| NOISE-7798-F | Invalid Entry 906 | Data quality insufficient |
| NOISE-1042-E | Invalid Entry 843 | Superseded by newer mapping |
| NOISE-9022-C | Invalid Entry 557 | Data quality insufficient |
| NOISE-6654-F | Invalid Entry 665 | Data quality insufficient |
| NOISE-8460-F | Invalid Entry 990 | Out of scope per business decision |
| NOISE-4912-G | Invalid Entry 339 | Pending validation |
| NOISE-6213-H | Invalid Entry 822 | Data quality insufficient |
| NOISE-3492-H | Invalid Entry 137 | Data quality insufficient |
| NOISE-6439-B | Invalid Entry 995 | Superseded by newer mapping |
| NOISE-9617-H | Invalid Entry 115 | Duplicate detected |
| NOISE-3529-B | Invalid Entry 580 | Superseded by newer mapping |
| NOISE-7512-B | Invalid Entry 972 | Pending validation |
| NOISE-9742-G | Invalid Entry 424 | Pending validation |
| NOISE-1588-B | Invalid Entry 340 | Out of scope per business decision |
| NOISE-2480-G | Invalid Entry 200 | Duplicate detected |
| NOISE-3725-E | Invalid Entry 129 | Pending validation |
| NOISE-1919-E | Invalid Entry 467 | Duplicate detected |
| NOISE-3385-D | Invalid Entry 643 | Superseded by newer mapping |
| NOISE-3950-C | Invalid Entry 279 | Pending validation |
| NOISE-7267-D | Invalid Entry 609 | Data quality insufficient |
| NOISE-4804-H | Invalid Entry 753 | Pending validation |
| NOISE-5183-A | Invalid Entry 923 | Duplicate detected |
| NOISE-9955-C | Invalid Entry 175 | Pending validation |
| NOISE-5901-G | Invalid Entry 806 | Out of scope per business decision |
| NOISE-5949-D | Invalid Entry 493 | Data quality insufficient |
| NOISE-4886-G | Invalid Entry 685 | Out of scope per business decision |
| NOISE-5847-E | Invalid Entry 122 | Superseded by newer mapping |
| NOISE-1132-A | Invalid Entry 720 | Pending validation |
| NOISE-4770-F | Invalid Entry 324 | Pending validation |
| NOISE-5106-C | Invalid Entry 743 | Superseded by newer mapping |
| NOISE-1645-E | Invalid Entry 907 | Out of scope per business decision |
| NOISE-6977-C | Invalid Entry 192 | Data quality insufficient |
| NOISE-7807-C | Invalid Entry 305 | Out of scope per business decision |
| NOISE-6994-E | Invalid Entry 950 | Duplicate detected |
| NOISE-8894-E | Invalid Entry 864 | Out of scope per business decision |
| NOISE-8673-B | Invalid Entry 244 | Data quality insufficient |
| NOISE-7511-F | Invalid Entry 192 | Pending validation |
| NOISE-5332-B | Invalid Entry 565 | Out of scope per business decision |
| NOISE-5295-G | Invalid Entry 942 | Superseded by newer mapping |
| NOISE-4830-H | Invalid Entry 125 | Data quality insufficient |
| NOISE-6374-D | Invalid Entry 763 | Pending validation |
| NOISE-8606-E | Invalid Entry 764 | Data quality insufficient |
| NOISE-3290-A | Invalid Entry 138 | Superseded by newer mapping |
| NOISE-2902-B | Invalid Entry 340 | Duplicate detected |
| NOISE-7367-H | Invalid Entry 479 | Data quality insufficient |
| NOISE-3531-G | Invalid Entry 770 | Data quality insufficient |
| NOISE-7686-E | Invalid Entry 133 | Out of scope per business decision |
| NOISE-8264-H | Invalid Entry 341 | Superseded by newer mapping |
| NOISE-7018-F | Invalid Entry 162 | Superseded by newer mapping |
| NOISE-4109-B | Invalid Entry 968 | Duplicate detected |
| NOISE-4475-A | Invalid Entry 151 | Superseded by newer mapping |
| NOISE-3063-D | Invalid Entry 170 | Data quality insufficient |
| NOISE-4538-D | Invalid Entry 436 | Duplicate detected |
| NOISE-1046-E | Invalid Entry 979 | Superseded by newer mapping |
| NOISE-9850-E | Invalid Entry 917 | Duplicate detected |
| NOISE-1422-C | Invalid Entry 115 | Superseded by newer mapping |
| NOISE-6304-A | Invalid Entry 278 | Superseded by newer mapping |
| NOISE-3076-G | Invalid Entry 638 | Out of scope per business decision |
| NOISE-2041-H | Invalid Entry 559 | Superseded by newer mapping |
| NOISE-2786-H | Invalid Entry 615 | Duplicate detected |
| NOISE-1710-E | Invalid Entry 569 | Data quality insufficient |
| NOISE-8847-G | Invalid Entry 536 | Out of scope per business decision |
| NOISE-8267-B | Invalid Entry 182 | Superseded by newer mapping |
| NOISE-3430-B | Invalid Entry 229 | Superseded by newer mapping |
| NOISE-9984-F | Invalid Entry 490 | Duplicate detected |
| NOISE-5831-H | Invalid Entry 617 | Out of scope per business decision |
| NOISE-2624-B | Invalid Entry 973 | Superseded by newer mapping |
| NOISE-4522-G | Invalid Entry 562 | Data quality insufficient |
| NOISE-6553-H | Invalid Entry 508 | Data quality insufficient |
| NOISE-2557-F | Invalid Entry 537 | Superseded by newer mapping |
| NOISE-5176-F | Invalid Entry 256 | Data quality insufficient |
| NOISE-2494-B | Invalid Entry 195 | Out of scope per business decision |
| NOISE-7105-C | Invalid Entry 669 | Superseded by newer mapping |
| NOISE-6400-B | Invalid Entry 520 | Duplicate detected |
| NOISE-7929-A | Invalid Entry 394 | Out of scope per business decision |
| NOISE-6761-B | Invalid Entry 691 | Data quality insufficient |
| NOISE-3535-H | Invalid Entry 329 | Superseded by newer mapping |
| NOISE-7022-B | Invalid Entry 880 | Out of scope per business decision |
| NOISE-4705-G | Invalid Entry 965 | Data quality insufficient |
| NOISE-1430-E | Invalid Entry 129 | Superseded by newer mapping |
| NOISE-6062-F | Invalid Entry 459 | Pending validation |
| NOISE-3347-G | Invalid Entry 171 | Duplicate detected |
| NOISE-1502-B | Invalid Entry 864 | Data quality insufficient |
| NOISE-7163-G | Invalid Entry 564 | Data quality insufficient |
| NOISE-7062-E | Invalid Entry 838 | Pending validation |
| NOISE-2391-A | Invalid Entry 259 | Pending validation |
| NOISE-1815-B | Invalid Entry 378 | Out of scope per business decision |
| NOISE-7947-H | Invalid Entry 721 | Duplicate detected |
| NOISE-5475-D | Invalid Entry 873 | Duplicate detected |
| NOISE-6655-G | Invalid Entry 213 | Data quality insufficient |
| NOISE-8972-E | Invalid Entry 146 | Pending validation |
| NOISE-1897-A | Invalid Entry 309 | Duplicate detected |
| NOISE-3248-E | Invalid Entry 396 | Superseded by newer mapping |
| NOISE-1126-H | Invalid Entry 864 | Duplicate detected |
| NOISE-3116-G | Invalid Entry 645 | Data quality insufficient |
| NOISE-6802-B | Invalid Entry 506 | Duplicate detected |
| NOISE-1307-H | Invalid Entry 179 | Out of scope per business decision |

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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230813_000000`
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
| Technical Lead | Sarah Chen (Data Governance) | sarah@company.com | +1-555-0102 |
| Business Owner | James Wilson (Finance) | james@company.com | +1-555-0103 |
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
