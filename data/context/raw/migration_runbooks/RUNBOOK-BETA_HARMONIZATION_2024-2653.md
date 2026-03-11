# Migration Runbook: European Subsidiary Harmonization

**Document ID**: RB-BETA_HARMONIZATION_2024-1353
**Version**: 2.0
**Last Updated**: 2023-06-10
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the European Subsidiary Harmonization project.
The migration involves transitioning master data and transactional records from ERP_BETA
to ERP_ALPHA while maintaining data integrity and business continuity.

**Project Timeline**: 2023-03-11 to 2023-08-01
**Business Sponsor**: Group Finance
**Technical Owner**: EU Operations

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
|   ERP_BETA       |     |   ETL Layer      |     |   ERP_ALPHA       |
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
ERP_BETA to ERP_ALPHA. All mappings have been validated by the
data stewardship team unless otherwise noted.

### 4.2 Migration Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1384 | Completed |
| Successfully mapped | 932 | Verified |
| Excluded from scope | 279 | Documented |
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

| Source Code (ERP_BETA) | Target Code (ERP_ALPHA) | Verification | Notes |
|------------------------------|------------------------------|--------------|-------|
| Resistente Stärke | Resistant Starch | system_admin | Verified via product specs |
| Kasein 25% Pharmazeutisch rein | Casein 25% Pharma Grade | domain_expert | Auto-mapped, validated |
| Ascorbic Acid | Ascorbic Acid | domain_expert | Verified via product specs |
| Sonnenblumenöl 98% Premiumqualität | Sunflower Oil 98% Premium | system_admin | Auto-mapped, validated |
| Pea Protein 99.5% | Pea Protein 99.5% | system_admin | Verified via product specs |
| Lactic Acid | Lactic Acid | system_admin | Cross-referenced with transactions |
| Ascorbic Acid Standardqualität | Ascorbic Acid Standard | data_steward | Verified via product specs |
| Zitronensäure 70% | Citric Acid 70% | system_admin | Confirmed by domain expert |
| Ascorbic Acid Pharmazeutisch rein | Ascorbic Acid Pharma Grade | domain_expert | Auto-mapped, validated |
| Coconut Oil Lebensmittelrein | Coconut Oil Food Grade | system_admin | Confirmed by domain expert |
| Palmfett 98% | Palm Oil 98% | domain_expert | Confirmed by domain expert |
| Traubenzucker Lebensmittelrein | Dextrose Food Grade | data_steward | Historical match confirmed |
| Weizenklebereiweiß 98% Premiumqualität | Wheat Gluten 98% Premium | data_steward | Verified via product specs |
| Natriumbenzoat 25% Standardqualität | Sodium Benzoate 25% Standard | data_steward | Cross-referenced with transactions |
| Coconut Oil 98% | Coconut Oil 98% | data_steward | Historical match confirmed |
| Natriumbenzoat 99.5% Qualitätsstufe I | Sodium Benzoate 99.5% Grade A | domain_expert | Confirmed by domain expert |
| Cyclodextrin 98% Pharmazeutisch rein | Cyclodextrin 98% Pharma Grade | data_steward | Verified via product specs |
| Coconut Oil Qualitätsstufe I | Coconut Oil Grade A | domain_expert | Verified via product specs |
| Traubenzucker Standardqualität | Dextrose Standard | domain_expert | Confirmed by domain expert |
| Lactic Acid 99.5% Qualitätsstufe II | Lactic Acid 99.5% Grade B | domain_expert | Auto-mapped, validated |
| Coconut Oil 99.5% Pharmazeutisch rein | Coconut Oil 99.5% Pharma Grade | system_admin | Auto-mapped, validated |
| Kaliumsorbat | Potassium Sorbate | domain_expert | Auto-mapped, validated |
| Natriumbenzoat 99.5% | Sodium Benzoate 99.5% | domain_expert | Auto-mapped, validated |
| Weizenklebereiweiß | Wheat Gluten | data_steward | Verified via product specs |
| Natriumbenzoat Pharmazeutisch rein | Sodium Benzoate Pharma Grade | data_steward | Historical match confirmed |
| Soja Isolate 70% | Soy Isolate 70% | data_steward | Verified via product specs |
| Soja Isolate 25% Technische Qualität | Soy Isolate 25% Technical | domain_expert | Verified via product specs |
| Calcium Carbonate 25% | Calcium Carbonate 25% | domain_expert | Auto-mapped, validated |
| Fructose | Fructose | domain_expert | Auto-mapped, validated |
| Rapsöl | Rapeseed Oil | data_steward | Historical match confirmed |
| Resistente Stärke | Resistant Starch | domain_expert | Cross-referenced with transactions |
| Fructose | Fructose | data_steward | Cross-referenced with transactions |
| Glukosesirup Syrup | Glucose Syrup | data_steward | Cross-referenced with transactions |
| Resistente Stärke Pharmazeutisch rein | Resistant Starch Pharma Grade | domain_expert | Auto-mapped, validated |
| Kasein Standardqualität | Casein Standard | system_admin | Cross-referenced with transactions |
| Calcium Carbonate 98% | Calcium Carbonate 98% | domain_expert | Verified via product specs |
| Palmfett Standardqualität | Palm Oil Standard | data_steward | Historical match confirmed |
| Maltodextrin-Pulver DE5 Qualitätsstufe I | Maltodextrin DE5 Grade A | data_steward | Auto-mapped, validated |
| Rapsöl 70% Qualitätsstufe II | Rapeseed Oil 70% Grade B | system_admin | Confirmed by domain expert |
| Sorbinsäure Lebensmittelrein | Sorbic Acid Food Grade | domain_expert | Auto-mapped, validated |
| Ascorbic Acid | Ascorbic Acid | data_steward | Confirmed by domain expert |
| Coconut Oil 25% Standardqualität | Coconut Oil 25% Standard | system_admin | Verified via product specs |
| Zitronensäure Pharmazeutisch rein | Citric Acid Pharma Grade | data_steward | Confirmed by domain expert |
| Sonnenblumenöl 50% Qualitätsstufe I | Sunflower Oil 50% Grade A | domain_expert | Historical match confirmed |
| Sorbinsäure 98% | Sorbic Acid 98% | domain_expert | Cross-referenced with transactions |
| Zitronensäure 50% Qualitätsstufe I | Citric Acid 50% Grade A | data_steward | Historical match confirmed |
| Dextrin | Dextrin | data_steward | Auto-mapped, validated |
| Maltodextrin-Pulver DE20 | Maltodextrin DE20 | system_admin | Confirmed by domain expert |
| Natriumbenzoat | Sodium Benzoate | system_admin | Historical match confirmed |
| Traubenzucker 25% Technische Qualität | Dextrose 25% Technical | data_steward | Historical match confirmed |
| Lactic Acid Lebensmittelrein | Lactic Acid Food Grade | data_steward | Historical match confirmed |
| Sorbinsäure | Sorbic Acid | domain_expert | Confirmed by domain expert |
| Rapsöl Technische Qualität | Rapeseed Oil Technical | domain_expert | Cross-referenced with transactions |
| Dextrin Pharmazeutisch rein | Dextrin Pharma Grade | data_steward | Historical match confirmed |
| Zitronensäure 99.5% | Citric Acid 99.5% | system_admin | Cross-referenced with transactions |
| Traubenzucker 25% | Dextrose 25% | system_admin | Verified via product specs |
| Traubenzucker | Dextrose | domain_expert | Cross-referenced with transactions |
| Resistente Stärke Qualitätsstufe II | Resistant Starch Grade B | domain_expert | Historical match confirmed |
| Fructose 25% | Fructose 25% | domain_expert | Verified via product specs |
| Calcium Carbonate 50% Qualitätsstufe II | Calcium Carbonate 50% Grade B | data_steward | Cross-referenced with transactions |
| Soja Isolate 25% | Soy Isolate 25% | data_steward | Cross-referenced with transactions |
| Zitronensäure Qualitätsstufe II | Citric Acid Grade B | domain_expert | Verified via product specs |
| Pea Protein Qualitätsstufe I | Pea Protein Grade A | data_steward | Cross-referenced with transactions |
| Rapsöl 99.5% | Rapeseed Oil 99.5% | data_steward | Cross-referenced with transactions |
| Glukosesirup Syrup 98% Lebensmittelrein | Glucose Syrup 98% Food Grade | domain_expert | Cross-referenced with transactions |
| Traubenzucker 99.5% Qualitätsstufe II | Dextrose 99.5% Grade B | data_steward | Auto-mapped, validated |
| Soja Isolate 25% Pharmazeutisch rein | Soy Isolate 25% Pharma Grade | data_steward | Auto-mapped, validated |
| Soja Isolate | Soy Isolate | system_admin | Auto-mapped, validated |
| Traubenzucker Qualitätsstufe I | Dextrose Grade A | system_admin | Confirmed by domain expert |
| Resistente Stärke Technische Qualität | Resistant Starch Technical | domain_expert | Confirmed by domain expert |
| Dextrin 50% | Dextrin 50% | data_steward | Verified via product specs |
| Glukosesirup Syrup Technische Qualität | Glucose Syrup Technical | system_admin | Cross-referenced with transactions |
| Soja Isolate 99.5% Premiumqualität | Soy Isolate 99.5% Premium | system_admin | Auto-mapped, validated |
| Soja Isolate 98% | Soy Isolate 98% | system_admin | Verified via product specs |
| Dextrin | Dextrin | system_admin | Historical match confirmed |
| Glukosesirup Syrup 70% | Glucose Syrup 70% | system_admin | Verified via product specs |
| Sonnenblumenöl Qualitätsstufe II | Sunflower Oil Grade B | domain_expert | Verified via product specs |
| Sonnenblumenöl Standardqualität | Sunflower Oil Standard | system_admin | Cross-referenced with transactions |
| Ascorbic Acid 99.5% Premiumqualität | Ascorbic Acid 99.5% Premium | system_admin | Cross-referenced with transactions |
| Dextrin Technische Qualität | Dextrin Technical | system_admin | Auto-mapped, validated |
| Palmfett | Palm Oil | data_steward | Cross-referenced with transactions |
| Natriumbenzoat Qualitätsstufe I | Sodium Benzoate Grade A | data_steward | Auto-mapped, validated |
| Traubenzucker 25% | Dextrose 25% | domain_expert | Historical match confirmed |
| Kaliumsorbat | Potassium Sorbate | system_admin | Historical match confirmed |
| Natriumbenzoat | Sodium Benzoate | system_admin | Confirmed by domain expert |
| Natriumbenzoat 25% | Sodium Benzoate 25% | data_steward | Auto-mapped, validated |
| Natriumchlorid 70% | Sodium Chloride 70% | domain_expert | Auto-mapped, validated |
| Kasein Premiumqualität | Casein Premium | domain_expert | Confirmed by domain expert |
| Calcium Carbonate Standardqualität | Calcium Carbonate Standard | domain_expert | Cross-referenced with transactions |
| Natriumchlorid 99.5% | Sodium Chloride 99.5% | system_admin | Confirmed by domain expert |
| Ascorbic Acid Technische Qualität | Ascorbic Acid Technical | domain_expert | Historical match confirmed |
| Natriumchlorid | Sodium Chloride | system_admin | Verified via product specs |
| Dextrin Standardqualität | Dextrin Standard | data_steward | Confirmed by domain expert |
| Kasein | Casein | data_steward | Verified via product specs |
| Isoglucose 70% | Isoglucose 70% | system_admin | Cross-referenced with transactions |
| Ascorbic Acid 50% Technische Qualität | Ascorbic Acid 50% Technical | domain_expert | Auto-mapped, validated |
| Traubenzucker Lebensmittelrein | Dextrose Food Grade | system_admin | Historical match confirmed |
| Natriumbenzoat | Sodium Benzoate | domain_expert | Verified via product specs |
| Palmfett 50% | Palm Oil 50% | domain_expert | Confirmed by domain expert |
| Ascorbic Acid 98% Premiumqualität | Ascorbic Acid 98% Premium | domain_expert | Cross-referenced with transactions |
| Sorbinsäure 70% | Sorbic Acid 70% | data_steward | Confirmed by domain expert |
| Dextrin Lebensmittelrein | Dextrin Food Grade | system_admin | Verified via product specs |
| Natriumchlorid Standardqualität | Sodium Chloride Standard | data_steward | Verified via product specs |
| Isoglucose Premiumqualität | Isoglucose Premium | system_admin | Verified via product specs |
| Calcium Carbonate Qualitätsstufe II | Calcium Carbonate Grade B | system_admin | Confirmed by domain expert |
| Kaliumsorbat | Potassium Sorbate | data_steward | Historical match confirmed |
| Weizenklebereiweiß | Wheat Gluten | domain_expert | Cross-referenced with transactions |
| Zitronensäure | Citric Acid | domain_expert | Confirmed by domain expert |
| Ascorbic Acid 70% | Ascorbic Acid 70% | domain_expert | Verified via product specs |
| Cyclodextrin | Cyclodextrin | domain_expert | Historical match confirmed |
| Traubenzucker 25% Technische Qualität | Dextrose 25% Technical | system_admin | Historical match confirmed |
| Isoglucose Lebensmittelrein | Isoglucose Food Grade | system_admin | Auto-mapped, validated |
| Dextrin 70% | Dextrin 70% | system_admin | Historical match confirmed |
| Zitronensäure | Citric Acid | data_steward | Historical match confirmed |
| Natriumbenzoat 98% Standardqualität | Sodium Benzoate 98% Standard | system_admin | Historical match confirmed |
| Lactic Acid 98% Premiumqualität | Lactic Acid 98% Premium | system_admin | Confirmed by domain expert |
| Ascorbic Acid Premiumqualität | Ascorbic Acid Premium | system_admin | Cross-referenced with transactions |
| Rapsöl Technische Qualität | Rapeseed Oil Technical | domain_expert | Verified via product specs |
| Soja Isolate Qualitätsstufe I | Soy Isolate Grade A | system_admin | Verified via product specs |
| Rapsöl | Rapeseed Oil | domain_expert | Auto-mapped, validated |
| Calcium Carbonate | Calcium Carbonate | system_admin | Cross-referenced with transactions |
| Natriumbenzoat 99.5% Technische Qualität | Sodium Benzoate 99.5% Technical | system_admin | Historical match confirmed |
| Natriumbenzoat Qualitätsstufe II | Sodium Benzoate Grade B | domain_expert | Confirmed by domain expert |
| Palmfett | Palm Oil | data_steward | Auto-mapped, validated |
| Calcium Carbonate 70% Premiumqualität | Calcium Carbonate 70% Premium | system_admin | Auto-mapped, validated |
| Soja Isolate Premiumqualität | Soy Isolate Premium | system_admin | Historical match confirmed |
| Palmfett Lebensmittelrein | Palm Oil Food Grade | system_admin | Cross-referenced with transactions |
| Weizenklebereiweiß Qualitätsstufe II | Wheat Gluten Grade B | system_admin | Confirmed by domain expert |
| Kasein Technische Qualität | Casein Technical | system_admin | Historical match confirmed |
| Glukosesirup Syrup 98% | Glucose Syrup 98% | domain_expert | Cross-referenced with transactions |
| Rapsöl 70% Premiumqualität | Rapeseed Oil 70% Premium | data_steward | Cross-referenced with transactions |
| Palmfett | Palm Oil | system_admin | Verified via product specs |
| Zitronensäure | Citric Acid | system_admin | Historical match confirmed |
| Lactic Acid 70% Pharmazeutisch rein | Lactic Acid 70% Pharma Grade | domain_expert | Cross-referenced with transactions |
| Kaliumsorbat Qualitätsstufe I | Potassium Sorbate Grade A | domain_expert | Verified via product specs |
| Natriumchlorid | Sodium Chloride | data_steward | Historical match confirmed |
| Fructose | Fructose | system_admin | Cross-referenced with transactions |
| Natriumbenzoat Qualitätsstufe I | Sodium Benzoate Grade A | system_admin | Verified via product specs |
| Fructose Qualitätsstufe II | Fructose Grade B | system_admin | Confirmed by domain expert |
| Ascorbic Acid | Ascorbic Acid | system_admin | Cross-referenced with transactions |
| Fructose | Fructose | data_steward | Confirmed by domain expert |
| Glukosesirup Syrup 98% Qualitätsstufe I | Glucose Syrup 98% Grade A | data_steward | Confirmed by domain expert |
| Rapsöl 98% | Rapeseed Oil 98% | system_admin | Verified via product specs |
| Kasein | Casein | system_admin | Verified via product specs |
| Rapsöl Qualitätsstufe I | Rapeseed Oil Grade A | domain_expert | Verified via product specs |
| Pea Protein 98% Qualitätsstufe II | Pea Protein 98% Grade B | system_admin | Cross-referenced with transactions |
| Calcium Carbonate | Calcium Carbonate | domain_expert | Auto-mapped, validated |
| Glukosesirup Syrup 70% | Glucose Syrup 70% | system_admin | Cross-referenced with transactions |
| Traubenzucker Qualitätsstufe I | Dextrose Grade A | data_steward | Auto-mapped, validated |
| Lactic Acid | Lactic Acid | data_steward | Auto-mapped, validated |
| Kaliumsorbat | Potassium Sorbate | data_steward | Historical match confirmed |
| Lactic Acid Technische Qualität | Lactic Acid Technical | domain_expert | Cross-referenced with transactions |
| Isoglucose 70% Lebensmittelrein | Isoglucose 70% Food Grade | data_steward | Historical match confirmed |
| Traubenzucker 25% | Dextrose 25% | domain_expert | Cross-referenced with transactions |
| Traubenzucker Qualitätsstufe II | Dextrose Grade B | domain_expert | Verified via product specs |
| Sorbinsäure Qualitätsstufe II | Sorbic Acid Grade B | domain_expert | Historical match confirmed |
| Resistente Stärke Qualitätsstufe II | Resistant Starch Grade B | data_steward | Historical match confirmed |
| Lactic Acid Qualitätsstufe I | Lactic Acid Grade A | domain_expert | Historical match confirmed |
| Dextrin Qualitätsstufe I | Dextrin Grade A | system_admin | Cross-referenced with transactions |
| Natriumchlorid 98% | Sodium Chloride 98% | system_admin | Verified via product specs |
| Natriumchlorid | Sodium Chloride | system_admin | Historical match confirmed |
| Pea Protein 25% Pharmazeutisch rein | Pea Protein 25% Pharma Grade | domain_expert | Confirmed by domain expert |
| Maltodextrin-Pulver DE10 Premiumqualität | Maltodextrin DE10 Premium | system_admin | Historical match confirmed |
| Maltodextrin-Pulver DE20 | Maltodextrin DE20 | system_admin | Verified via product specs |
| Fructose Qualitätsstufe I | Fructose Grade A | system_admin | Verified via product specs |
| Glukosesirup Syrup | Glucose Syrup | domain_expert | Auto-mapped, validated |
| Isoglucose | Isoglucose | domain_expert | Auto-mapped, validated |
| Soja Isolate | Soy Isolate | data_steward | Verified via product specs |
| Calcium Carbonate 98% Standardqualität | Calcium Carbonate 98% Standard | domain_expert | Cross-referenced with transactions |
| Resistente Stärke | Resistant Starch | data_steward | Confirmed by domain expert |
| Kaliumsorbat Standardqualität | Potassium Sorbate Standard | system_admin | Historical match confirmed |
| Zitronensäure | Citric Acid | system_admin | Auto-mapped, validated |
| Lactic Acid Lebensmittelrein | Lactic Acid Food Grade | data_steward | Confirmed by domain expert |
| Zitronensäure 25% Technische Qualität | Citric Acid 25% Technical | system_admin | Verified via product specs |
| Dextrin 50% | Dextrin 50% | system_admin | Historical match confirmed |
| Isoglucose | Isoglucose | domain_expert | Auto-mapped, validated |
| Soja Isolate 50% Qualitätsstufe II | Soy Isolate 50% Grade B | domain_expert | Confirmed by domain expert |
| Rapsöl | Rapeseed Oil | system_admin | Verified via product specs |
| Maltodextrin-Pulver DE18 Pharmazeutisch rein | Maltodextrin DE18 Pharma Grade | domain_expert | Cross-referenced with transactions |
| Rapsöl Qualitätsstufe I | Rapeseed Oil Grade A | system_admin | Cross-referenced with transactions |
| Traubenzucker 70% Qualitätsstufe I | Dextrose 70% Grade A | system_admin | Historical match confirmed |
| Calcium Carbonate 50% Pharmazeutisch rein | Calcium Carbonate 50% Pharma Grade | domain_expert | Cross-referenced with transactions |
| Natriumbenzoat 25% Qualitätsstufe II | Sodium Benzoate 25% Grade B | domain_expert | Cross-referenced with transactions |
| Rapsöl 99.5% Technische Qualität | Rapeseed Oil 99.5% Technical | system_admin | Verified via product specs |
| Kaliumsorbat 98% Qualitätsstufe II | Potassium Sorbate 98% Grade B | domain_expert | Cross-referenced with transactions |
| Natriumbenzoat 50% | Sodium Benzoate 50% | system_admin | Confirmed by domain expert |
| Coconut Oil | Coconut Oil | system_admin | Confirmed by domain expert |
| Fructose | Fructose | system_admin | Verified via product specs |
| Sorbinsäure 50% Standardqualität | Sorbic Acid 50% Standard | data_steward | Verified via product specs |
| Rapsöl 99.5% | Rapeseed Oil 99.5% | data_steward | Confirmed by domain expert |
| Zitronensäure | Citric Acid | domain_expert | Auto-mapped, validated |
| Natriumchlorid Technische Qualität | Sodium Chloride Technical | system_admin | Auto-mapped, validated |
| Kaliumsorbat | Potassium Sorbate | system_admin | Cross-referenced with transactions |
| Dextrin Premiumqualität | Dextrin Premium | domain_expert | Confirmed by domain expert |
| Zitronensäure 70% | Citric Acid 70% | data_steward | Cross-referenced with transactions |
| Maltodextrin-Pulver DE25 | Maltodextrin DE25 | domain_expert | Cross-referenced with transactions |
| Maltodextrin-Pulver DE10 | Maltodextrin DE10 | data_steward | Auto-mapped, validated |
| Dextrin 70% | Dextrin 70% | system_admin | Historical match confirmed |
| Lactic Acid Lebensmittelrein | Lactic Acid Food Grade | domain_expert | Cross-referenced with transactions |
| Ascorbic Acid 98% Pharmazeutisch rein | Ascorbic Acid 98% Pharma Grade | data_steward | Auto-mapped, validated |
| Natriumchlorid 70% | Sodium Chloride 70% | system_admin | Historical match confirmed |
| Fructose Technische Qualität | Fructose Technical | system_admin | Confirmed by domain expert |
| Ascorbic Acid | Ascorbic Acid | system_admin | Verified via product specs |
| Lactic Acid | Lactic Acid | domain_expert | Confirmed by domain expert |
| Coconut Oil 98% Lebensmittelrein | Coconut Oil 98% Food Grade | domain_expert | Verified via product specs |
| Kaliumsorbat Technische Qualität | Potassium Sorbate Technical | domain_expert | Verified via product specs |
| Maltodextrin-Pulver DE5 Qualitätsstufe II | Maltodextrin DE5 Grade B | system_admin | Cross-referenced with transactions |
| Soja Isolate 98% Premiumqualität | Soy Isolate 98% Premium | domain_expert | Verified via product specs |
| Lactic Acid 99.5% | Lactic Acid 99.5% | system_admin | Historical match confirmed |
| Glukosesirup Syrup | Glucose Syrup | system_admin | Verified via product specs |
| Maltodextrin-Pulver DE25 | Maltodextrin DE25 | system_admin | Cross-referenced with transactions |
| Calcium Carbonate Qualitätsstufe II | Calcium Carbonate Grade B | system_admin | Historical match confirmed |
| Lactic Acid Lebensmittelrein | Lactic Acid Food Grade | system_admin | Cross-referenced with transactions |
| Kasein 98% Qualitätsstufe II | Casein 98% Grade B | domain_expert | Auto-mapped, validated |
| Resistente Stärke Technische Qualität | Resistant Starch Technical | domain_expert | Auto-mapped, validated |
| Resistente Stärke Technische Qualität | Resistant Starch Technical | domain_expert | Historical match confirmed |
| Kasein Qualitätsstufe I | Casein Grade A | domain_expert | Cross-referenced with transactions |
| Palmfett Qualitätsstufe II | Palm Oil Grade B | data_steward | Auto-mapped, validated |
| Maltodextrin-Pulver DE25 | Maltodextrin DE25 | data_steward | Auto-mapped, validated |
| Soja Isolate Standardqualität | Soy Isolate Standard | system_admin | Auto-mapped, validated |
| Natriumbenzoat 50% Technische Qualität | Sodium Benzoate 50% Technical | system_admin | Verified via product specs |
| Traubenzucker 50% | Dextrose 50% | system_admin | Historical match confirmed |
| Resistente Stärke 70% Technische Qualität | Resistant Starch 70% Technical | data_steward | Auto-mapped, validated |
| Glukosesirup Syrup Lebensmittelrein | Glucose Syrup Food Grade | system_admin | Confirmed by domain expert |
| Pea Protein Premiumqualität | Pea Protein Premium | system_admin | Historical match confirmed |
| Weizenklebereiweiß 98% | Wheat Gluten 98% | domain_expert | Cross-referenced with transactions |
| Kaliumsorbat Qualitätsstufe II | Potassium Sorbate Grade B | domain_expert | Auto-mapped, validated |
| Zitronensäure 70% Lebensmittelrein | Citric Acid 70% Food Grade | domain_expert | Confirmed by domain expert |
| Natriumchlorid 98% Standardqualität | Sodium Chloride 98% Standard | domain_expert | Verified via product specs |
| Natriumbenzoat 50% | Sodium Benzoate 50% | data_steward | Confirmed by domain expert |
| Lactic Acid 50% Premiumqualität | Lactic Acid 50% Premium | system_admin | Cross-referenced with transactions |
| Kasein 98% Technische Qualität | Casein 98% Technical | domain_expert | Historical match confirmed |
| Sorbinsäure | Sorbic Acid | data_steward | Cross-referenced with transactions |
| Rapsöl 50% Lebensmittelrein | Rapeseed Oil 50% Food Grade | domain_expert | Historical match confirmed |
| Resistente Stärke 98% | Resistant Starch 98% | system_admin | Verified via product specs |
| Fructose 99.5% Lebensmittelrein | Fructose 99.5% Food Grade | data_steward | Verified via product specs |
| Lactic Acid Standardqualität | Lactic Acid Standard | system_admin | Cross-referenced with transactions |
| Resistente Stärke Technische Qualität | Resistant Starch Technical | domain_expert | Cross-referenced with transactions |
| Weizenklebereiweiß 99.5% Qualitätsstufe I | Wheat Gluten 99.5% Grade A | system_admin | Historical match confirmed |
| Natriumbenzoat 99.5% Technische Qualität | Sodium Benzoate 99.5% Technical | domain_expert | Auto-mapped, validated |
| Natriumbenzoat 99.5% Qualitätsstufe I | Sodium Benzoate 99.5% Grade A | domain_expert | Confirmed by domain expert |
| Maltodextrin-Pulver DE10 | Maltodextrin DE10 | domain_expert | Cross-referenced with transactions |
| Ascorbic Acid 50% | Ascorbic Acid 50% | system_admin | Auto-mapped, validated |
| Traubenzucker Qualitätsstufe I | Dextrose Grade A | system_admin | Confirmed by domain expert |
| Kaliumsorbat 50% Technische Qualität | Potassium Sorbate 50% Technical | system_admin | Historical match confirmed |
| Coconut Oil 70% Qualitätsstufe I | Coconut Oil 70% Grade A | data_steward | Verified via product specs |
| Kaliumsorbat 98% | Potassium Sorbate 98% | data_steward | Cross-referenced with transactions |
| Resistente Stärke 70% Lebensmittelrein | Resistant Starch 70% Food Grade | domain_expert | Historical match confirmed |
| Ascorbic Acid | Ascorbic Acid | data_steward | Confirmed by domain expert |
| Glukosesirup Syrup | Glucose Syrup | data_steward | Historical match confirmed |
| Calcium Carbonate 99.5% | Calcium Carbonate 99.5% | domain_expert | Confirmed by domain expert |
| Palmfett 70% Premiumqualität | Palm Oil 70% Premium | system_admin | Historical match confirmed |
| Lactic Acid Qualitätsstufe II | Lactic Acid Grade B | system_admin | Confirmed by domain expert |
| Lactic Acid 98% | Lactic Acid 98% | domain_expert | Auto-mapped, validated |
| Kaliumsorbat | Potassium Sorbate | domain_expert | Cross-referenced with transactions |
| Pea Protein Premiumqualität | Pea Protein Premium | system_admin | Verified via product specs |
| Coconut Oil 98% Technische Qualität | Coconut Oil 98% Technical | domain_expert | Auto-mapped, validated |
| Coconut Oil 98% | Coconut Oil 98% | data_steward | Verified via product specs |
| Traubenzucker | Dextrose | data_steward | Verified via product specs |
| Natriumchlorid | Sodium Chloride | domain_expert | Confirmed by domain expert |
| Coconut Oil 25% Technische Qualität | Coconut Oil 25% Technical | system_admin | Cross-referenced with transactions |
| Lactic Acid 98% Qualitätsstufe I | Lactic Acid 98% Grade A | system_admin | Historical match confirmed |
| Calcium Carbonate 70% | Calcium Carbonate 70% | data_steward | Cross-referenced with transactions |
| Palmfett 99.5% Qualitätsstufe I | Palm Oil 99.5% Grade A | system_admin | Historical match confirmed |
| Resistente Stärke 50% | Resistant Starch 50% | domain_expert | Auto-mapped, validated |
| Ascorbic Acid Pharmazeutisch rein | Ascorbic Acid Pharma Grade | system_admin | Confirmed by domain expert |
| Resistente Stärke Lebensmittelrein | Resistant Starch Food Grade | system_admin | Auto-mapped, validated |
| Sorbinsäure 70% | Sorbic Acid 70% | system_admin | Verified via product specs |
| Natriumbenzoat Lebensmittelrein | Sodium Benzoate Food Grade | domain_expert | Auto-mapped, validated |
| Weizenklebereiweiß | Wheat Gluten | data_steward | Auto-mapped, validated |
| Sorbinsäure Standardqualität | Sorbic Acid Standard | domain_expert | Cross-referenced with transactions |
| Weizenklebereiweiß Lebensmittelrein | Wheat Gluten Food Grade | domain_expert | Confirmed by domain expert |
| Traubenzucker Qualitätsstufe II | Dextrose Grade B | data_steward | Confirmed by domain expert |
| Pea Protein | Pea Protein | data_steward | Cross-referenced with transactions |
| Calcium Carbonate 98% | Calcium Carbonate 98% | domain_expert | Auto-mapped, validated |
| Kasein Qualitätsstufe II | Casein Grade B | data_steward | Verified via product specs |
| Weizenklebereiweiß Lebensmittelrein | Wheat Gluten Food Grade | system_admin | Auto-mapped, validated |
| Zitronensäure Premiumqualität | Citric Acid Premium | system_admin | Historical match confirmed |
| Natriumchlorid 25% | Sodium Chloride 25% | system_admin | Cross-referenced with transactions |
| Coconut Oil 25% Lebensmittelrein | Coconut Oil 25% Food Grade | system_admin | Cross-referenced with transactions |
| Sonnenblumenöl Qualitätsstufe II | Sunflower Oil Grade B | system_admin | Cross-referenced with transactions |
| Natriumbenzoat | Sodium Benzoate | system_admin | Confirmed by domain expert |
| Kaliumsorbat Standardqualität | Potassium Sorbate Standard | system_admin | Auto-mapped, validated |
| Traubenzucker Lebensmittelrein | Dextrose Food Grade | domain_expert | Cross-referenced with transactions |
| Fructose 99.5% Technische Qualität | Fructose 99.5% Technical | domain_expert | Cross-referenced with transactions |
| Glukosesirup Syrup 99.5% Qualitätsstufe II | Glucose Syrup 99.5% Grade B | data_steward | Auto-mapped, validated |
| Sorbinsäure 50% Qualitätsstufe I | Sorbic Acid 50% Grade A | domain_expert | Historical match confirmed |
| Sorbinsäure 50% Lebensmittelrein | Sorbic Acid 50% Food Grade | domain_expert | Verified via product specs |
| Soja Isolate 99.5% | Soy Isolate 99.5% | domain_expert | Confirmed by domain expert |
| Rapsöl Qualitätsstufe I | Rapeseed Oil Grade A | system_admin | Confirmed by domain expert |
| Cyclodextrin | Cyclodextrin | data_steward | Verified via product specs |
| Traubenzucker Standardqualität | Dextrose Standard | domain_expert | Historical match confirmed |
| Traubenzucker 99.5% | Dextrose 99.5% | data_steward | Historical match confirmed |
| Palmfett 98% Qualitätsstufe I | Palm Oil 98% Grade A | data_steward | Auto-mapped, validated |
| Natriumbenzoat 50% | Sodium Benzoate 50% | system_admin | Auto-mapped, validated |
| Traubenzucker 70% | Dextrose 70% | domain_expert | Verified via product specs |
| Dextrin 70% Pharmazeutisch rein | Dextrin 70% Pharma Grade | system_admin | Confirmed by domain expert |
| Fructose 99.5% Technische Qualität | Fructose 99.5% Technical | data_steward | Historical match confirmed |
| Pea Protein 25% | Pea Protein 25% | system_admin | Auto-mapped, validated |
| Ascorbic Acid Technische Qualität | Ascorbic Acid Technical | data_steward | Confirmed by domain expert |
| Palmfett Qualitätsstufe II | Palm Oil Grade B | domain_expert | Cross-referenced with transactions |
| Traubenzucker Technische Qualität | Dextrose Technical | data_steward | Historical match confirmed |
| Soja Isolate Lebensmittelrein | Soy Isolate Food Grade | domain_expert | Historical match confirmed |
| Isoglucose 70% | Isoglucose 70% | system_admin | Historical match confirmed |
| Maltodextrin-Pulver DE15 | Maltodextrin DE15 | system_admin | Cross-referenced with transactions |
| Resistente Stärke 50% | Resistant Starch 50% | domain_expert | Cross-referenced with transactions |
| Palmfett | Palm Oil | data_steward | Historical match confirmed |
| Maltodextrin-Pulver DE20 | Maltodextrin DE20 | data_steward | Confirmed by domain expert |
| Calcium Carbonate 98% | Calcium Carbonate 98% | system_admin | Historical match confirmed |
| Lactic Acid | Lactic Acid | system_admin | Verified via product specs |
| Isoglucose | Isoglucose | domain_expert | Auto-mapped, validated |
| Cyclodextrin 70% Lebensmittelrein | Cyclodextrin 70% Food Grade | domain_expert | Verified via product specs |
| Ascorbic Acid Lebensmittelrein | Ascorbic Acid Food Grade | data_steward | Auto-mapped, validated |
| Dextrin | Dextrin | data_steward | Verified via product specs |
| Natriumchlorid 25% Lebensmittelrein | Sodium Chloride 25% Food Grade | system_admin | Auto-mapped, validated |
| Pea Protein 70% Premiumqualität | Pea Protein 70% Premium | domain_expert | Auto-mapped, validated |
| Natriumchlorid | Sodium Chloride | domain_expert | Verified via product specs |
| Weizenklebereiweiß 99.5% | Wheat Gluten 99.5% | domain_expert | Confirmed by domain expert |
| Glukosesirup Syrup 99.5% Lebensmittelrein | Glucose Syrup 99.5% Food Grade | data_steward | Verified via product specs |
| Isoglucose Qualitätsstufe II | Isoglucose Grade B | domain_expert | Cross-referenced with transactions |
| Glukosesirup Syrup 25% | Glucose Syrup 25% | domain_expert | Confirmed by domain expert |
| Sonnenblumenöl Qualitätsstufe I | Sunflower Oil Grade A | data_steward | Auto-mapped, validated |
| Fructose 70% | Fructose 70% | data_steward | Verified via product specs |
| Zitronensäure Standardqualität | Citric Acid Standard | system_admin | Verified via product specs |
| Kaliumsorbat | Potassium Sorbate | data_steward | Verified via product specs |
| Resistente Stärke Qualitätsstufe I | Resistant Starch Grade A | system_admin | Verified via product specs |
| Pea Protein 99.5% Premiumqualität | Pea Protein 99.5% Premium | data_steward | Historical match confirmed |
| Ascorbic Acid Premiumqualität | Ascorbic Acid Premium | data_steward | Confirmed by domain expert |
| Natriumchlorid 99.5% Qualitätsstufe I | Sodium Chloride 99.5% Grade A | data_steward | Historical match confirmed |
| Palmfett 70% Technische Qualität | Palm Oil 70% Technical | domain_expert | Cross-referenced with transactions |
| Weizenklebereiweiß Qualitätsstufe I | Wheat Gluten Grade A | system_admin | Historical match confirmed |
| Dextrin Qualitätsstufe II | Dextrin Grade B | system_admin | Confirmed by domain expert |
| Sonnenblumenöl Technische Qualität | Sunflower Oil Technical | domain_expert | Cross-referenced with transactions |
| Pea Protein | Pea Protein | data_steward | Cross-referenced with transactions |
| Cyclodextrin | Cyclodextrin | system_admin | Cross-referenced with transactions |
| Lactic Acid Technische Qualität | Lactic Acid Technical | domain_expert | Auto-mapped, validated |
| Maltodextrin-Pulver DE15 | Maltodextrin DE15 | system_admin | Auto-mapped, validated |
| Kaliumsorbat | Potassium Sorbate | system_admin | Historical match confirmed |
| Natriumbenzoat | Sodium Benzoate | system_admin | Verified via product specs |
| Weizenklebereiweiß 70% | Wheat Gluten 70% | domain_expert | Auto-mapped, validated |
| Sonnenblumenöl | Sunflower Oil | data_steward | Confirmed by domain expert |
| Coconut Oil 25% | Coconut Oil 25% | system_admin | Historical match confirmed |
| Kasein Technische Qualität | Casein Technical | domain_expert | Historical match confirmed |
| Sonnenblumenöl 70% Lebensmittelrein | Sunflower Oil 70% Food Grade | domain_expert | Historical match confirmed |
| Kasein 50% Premiumqualität | Casein 50% Premium | system_admin | Cross-referenced with transactions |
| Isoglucose Qualitätsstufe II | Isoglucose Grade B | data_steward | Verified via product specs |
| Maltodextrin-Pulver DE18 | Maltodextrin DE18 | domain_expert | Cross-referenced with transactions |
| Lactic Acid | Lactic Acid | system_admin | Confirmed by domain expert |
| Palmfett Lebensmittelrein | Palm Oil Food Grade | data_steward | Historical match confirmed |
| Weizenklebereiweiß Qualitätsstufe I | Wheat Gluten Grade A | domain_expert | Auto-mapped, validated |
| Rapsöl Pharmazeutisch rein | Rapeseed Oil Pharma Grade | data_steward | Auto-mapped, validated |
| Resistente Stärke | Resistant Starch | data_steward | Auto-mapped, validated |
| Natriumchlorid Technische Qualität | Sodium Chloride Technical | domain_expert | Confirmed by domain expert |
| Kaliumsorbat | Potassium Sorbate | system_admin | Auto-mapped, validated |
| Sonnenblumenöl | Sunflower Oil | system_admin | Historical match confirmed |
| Sonnenblumenöl Pharmazeutisch rein | Sunflower Oil Pharma Grade | system_admin | Confirmed by domain expert |
| Cyclodextrin Standardqualität | Cyclodextrin Standard | data_steward | Auto-mapped, validated |
| Kasein 25% Technische Qualität | Casein 25% Technical | system_admin | Confirmed by domain expert |
| Maltodextrin-Pulver DE30 Standardqualität | Maltodextrin DE30 Standard | domain_expert | Confirmed by domain expert |
| Natriumbenzoat Qualitätsstufe I | Sodium Benzoate Grade A | data_steward | Confirmed by domain expert |
| Weizenklebereiweiß | Wheat Gluten | system_admin | Verified via product specs |
| Maltodextrin-Pulver DE18 | Maltodextrin DE18 | data_steward | Confirmed by domain expert |
| Sonnenblumenöl Qualitätsstufe I | Sunflower Oil Grade A | system_admin | Historical match confirmed |
| Kaliumsorbat 50% Lebensmittelrein | Potassium Sorbate 50% Food Grade | system_admin | Auto-mapped, validated |
| Fructose Standardqualität | Fructose Standard | data_steward | Historical match confirmed |
| Soja Isolate 50% Premiumqualität | Soy Isolate 50% Premium | domain_expert | Cross-referenced with transactions |
| Resistente Stärke 70% | Resistant Starch 70% | data_steward | Cross-referenced with transactions |
| Isoglucose 25% Standardqualität | Isoglucose 25% Standard | system_admin | Auto-mapped, validated |
| Resistente Stärke | Resistant Starch | data_steward | Auto-mapped, validated |
| Kaliumsorbat Lebensmittelrein | Potassium Sorbate Food Grade | system_admin | Verified via product specs |
| Zitronensäure | Citric Acid | domain_expert | Verified via product specs |
| Soja Isolate Premiumqualität | Soy Isolate Premium | system_admin | Cross-referenced with transactions |
| Pea Protein Standardqualität | Pea Protein Standard | domain_expert | Confirmed by domain expert |
| Resistente Stärke 70% | Resistant Starch 70% | data_steward | Auto-mapped, validated |
| Fructose Premiumqualität | Fructose Premium | system_admin | Auto-mapped, validated |
| Zitronensäure Lebensmittelrein | Citric Acid Food Grade | data_steward | Historical match confirmed |
| Dextrin Technische Qualität | Dextrin Technical | system_admin | Auto-mapped, validated |
| Natriumbenzoat Pharmazeutisch rein | Sodium Benzoate Pharma Grade | system_admin | Confirmed by domain expert |
| Premier Rohstoffe Holdings | Premier Commodities Group | system_admin | Confirmed by domain expert |
| Pinnacle Rohstoffe NV | Pinnacle Commodities BV | domain_expert | Historical match confirmed |
| Atlas Handel SARL | Atlas Trading SA | system_admin | Cross-referenced with transactions |
| Horizon Handel KG | Horizon Trading | domain_expert | Confirmed by domain expert |
| Stellar Vertrieb | Stellar Distribution SA | domain_expert | Cross-referenced with transactions |
| Pinnacle Ingredients | Pinnacle Ingredients Ltd. | data_steward | Historical match confirmed |
| Stratos Ingredients | Stratos Ingredients SARL | data_steward | Cross-referenced with transactions |
| Pacific Logistik | Pacific Logistics | data_steward | Confirmed by domain expert |
| Stratos Versorgung | Stratos Supply Group | data_steward | Confirmed by domain expert |
| Quantum Ingredients | Quantum Ingredients | system_admin | Auto-mapped, validated |
| Core Chemicals International | Core Chemicals International | domain_expert | Auto-mapped, validated |
| Catalyst Manufacturing GmbH | Catalyst Manufacturing GmbH | system_admin | Auto-mapped, validated |
| Pacific Chemicals GmbH | Pacific Chemicals AG | system_admin | Auto-mapped, validated |
| Pacific Vertrieb NV | Pacific Distribution NV | data_steward | Verified via product specs |
| Pacific Vertrieb Group | Pacific Distribution International | data_steward | Historical match confirmed |
| Premier Enterprise Holdings | Premier Enterprise International | system_admin | Cross-referenced with transactions |
| Vertex Enterprise Group | Vertex Enterprise Holdings | data_steward | Verified via product specs |
| Prime Chemicals SAS | Prime Chemicals | system_admin | Confirmed by domain expert |
| Vanguard Logistik SA | Vanguard Logistics SARL | system_admin | Historical match confirmed |
| Stratos Handel | Stratos Trading BV | data_steward | Cross-referenced with transactions |
| Baltic Enterprise | Baltic Enterprise KG | domain_expert | Verified via product specs |
| Premier Logistik | Premier Logistics Ltd. | data_steward | Auto-mapped, validated |
| Quantum Manufacturing | Quantum Manufacturing KG | domain_expert | Confirmed by domain expert |
| Atlas Ingredients Ltd. | Atlas Ingredients PLC | data_steward | Auto-mapped, validated |
| Vertex Vertrieb NV | Vertex Distribution NV | data_steward | Cross-referenced with transactions |
| Atlas Manufacturing Corp. | Atlas Manufacturing | domain_expert | Auto-mapped, validated |
| Atlantic Manufacturing International | Atlantic Manufacturing | data_steward | Verified via product specs |
| Zenith Manufacturing International | Zenith Manufacturing | domain_expert | Confirmed by domain expert |
| Stratos Versorgung BV | Stratos Supply | domain_expert | Historical match confirmed |
| Global Verarbeitung SAS | Global Processing SAS | domain_expert | Confirmed by domain expert |
| Apex Solutions International | Apex Solutions | system_admin | Cross-referenced with transactions |
| Pinnacle Chemicals SAS | Pinnacle Chemicals SA | system_admin | Historical match confirmed |
| Core Manufacturing | Core Manufacturing Holdings | system_admin | Confirmed by domain expert |
| Pinnacle Industrien SAS | Pinnacle Industries SAS | data_steward | Auto-mapped, validated |
| Pinnacle Handel Inc. | Pinnacle Trading | data_steward | Cross-referenced with transactions |
| Elite Vertrieb International | Elite Distribution | data_steward | Confirmed by domain expert |
| Prime Versorgung | Prime Supply | system_admin | Confirmed by domain expert |
| Prism Vertrieb NV | Prism Distribution BV | system_admin | Cross-referenced with transactions |
| Prism Ingredients NV | Prism Ingredients | data_steward | Confirmed by domain expert |
| Core Rohstoffe | Core Commodities BV | system_admin | Cross-referenced with transactions |
| Stellar Versorgung NV | Stellar Supply | system_admin | Confirmed by domain expert |
| Meridian Solutions | Meridian Solutions KG | data_steward | Historical match confirmed |
| Apex Chemicals | Apex Chemicals | domain_expert | Confirmed by domain expert |
| Pinnacle Verarbeitung | Pinnacle Processing International | data_steward | Confirmed by domain expert |
| Elite Chemicals KG | Elite Chemicals AG | domain_expert | Auto-mapped, validated |
| Nordic Ingredients | Nordic Ingredients PLC | data_steward | Cross-referenced with transactions |
| Global Enterprise NV | Global Enterprise NV | system_admin | Historical match confirmed |
| Vanguard Enterprise Group | Vanguard Enterprise International | data_steward | Historical match confirmed |
| Continental Enterprise GmbH | Continental Enterprise KG | data_steward | Historical match confirmed |
| Core Logistik Holdings | Core Logistics Holdings | domain_expert | Historical match confirmed |
| Core Chemicals Holdings | Core Chemicals | data_steward | Auto-mapped, validated |
| Baltic Handel NV | Baltic Trading BV | domain_expert | Cross-referenced with transactions |
| Vertex Solutions NV | Vertex Solutions BV | domain_expert | Cross-referenced with transactions |
| Nordic Ingredients SARL | Nordic Ingredients SA | domain_expert | Historical match confirmed |
| Catalyst Rohstoffe GmbH | Catalyst Commodities GmbH | system_admin | Historical match confirmed |
| Apex Handel International | Apex Trading Group | data_steward | Confirmed by domain expert |
| Continental Ingredients | Continental Ingredients | data_steward | Historical match confirmed |
| Nexus Vertrieb KG | Nexus Distribution | system_admin | Auto-mapped, validated |
| Catalyst Industrien International | Catalyst Industries International | data_steward | Verified via product specs |
| Vanguard Werkstoffe Group | Vanguard Materials Group | domain_expert | Historical match confirmed |
| Pinnacle Rohstoffe NV | Pinnacle Commodities | system_admin | Cross-referenced with transactions |
| Premier Solutions | Premier Solutions LLC | data_steward | Cross-referenced with transactions |
| Apex Chemicals Corp. | Apex Chemicals | domain_expert | Historical match confirmed |
| Global Ingredients GmbH | Global Ingredients AG | system_admin | Verified via product specs |
| Nexus Enterprise Group | Nexus Enterprise International | data_steward | Historical match confirmed |
| Apex Chemicals International | Apex Chemicals | domain_expert | Confirmed by domain expert |
| Pinnacle Solutions Corp. | Pinnacle Solutions Corp. | domain_expert | Auto-mapped, validated |
| Atlas Chemicals | Atlas Chemicals | domain_expert | Cross-referenced with transactions |
| Premier Industrien Group | Premier Industries Group | data_steward | Cross-referenced with transactions |
| Atlantic Rohstoffe GmbH | Atlantic Commodities | system_admin | Historical match confirmed |
| Prism Ingredients | Prism Ingredients | data_steward | Historical match confirmed |
| Apex Rohstoffe Holdings | Apex Commodities Holdings | system_admin | Confirmed by domain expert |
| Apex Ingredients KG | Apex Ingredients AG | system_admin | Auto-mapped, validated |
| Nexus Vertrieb | Nexus Distribution | system_admin | Historical match confirmed |
| Pinnacle Ingredients KG | Pinnacle Ingredients AG | system_admin | Auto-mapped, validated |
| Continental Chemicals Inc. | Continental Chemicals Inc. | system_admin | Confirmed by domain expert |
| Pinnacle Chemicals Ltd. | Pinnacle Chemicals PLC | system_admin | Verified via product specs |
| Catalyst Enterprise International | Catalyst Enterprise International | domain_expert | Historical match confirmed |
| Global Solutions Group | Global Solutions International | domain_expert | Confirmed by domain expert |
| Pacific Ingredients BV | Pacific Ingredients BV | data_steward | Historical match confirmed |
| Atlas Solutions NV | Atlas Solutions BV | data_steward | Verified via product specs |
| Atlas Enterprise International | Atlas Enterprise International | domain_expert | Cross-referenced with transactions |
| Stratos Chemicals | Stratos Chemicals | domain_expert | Verified via product specs |
| Nordic Industrien PLC | Nordic Industries Ltd. | system_admin | Cross-referenced with transactions |
| Horizon Partners Ltd. | Horizon Partners Ltd. | domain_expert | Confirmed by domain expert |
| Horizon Industrien GmbH | Horizon Industries | data_steward | Auto-mapped, validated |
| Atlantic Partners NV | Atlantic Partners | system_admin | Cross-referenced with transactions |
| Quantum Rohstoffe PLC | Quantum Commodities PLC | domain_expert | Historical match confirmed |
| Prism Industrien | Prism Industries | data_steward | Auto-mapped, validated |
| Prism Werkstoffe Ltd. | Prism Materials Ltd. | system_admin | Historical match confirmed |
| Core Werkstoffe | Core Materials | data_steward | Confirmed by domain expert |
| Nexus Ingredients PLC | Nexus Ingredients PLC | domain_expert | Auto-mapped, validated |
| Vertex Ingredients | Vertex Ingredients | system_admin | Cross-referenced with transactions |
| Continental Solutions NV | Continental Solutions | data_steward | Cross-referenced with transactions |
| Stellar Rohstoffe | Stellar Commodities | data_steward | Historical match confirmed |
| Nexus Rohstoffe Group | Nexus Commodities International | system_admin | Auto-mapped, validated |
| Pinnacle Handel | Pinnacle Trading Group | data_steward | Confirmed by domain expert |
| Catalyst Industrien PLC | Catalyst Industries | domain_expert | Confirmed by domain expert |
| Continental Rohstoffe GmbH | Continental Commodities GmbH | system_admin | Auto-mapped, validated |
| Global Werkstoffe BV | Global Materials NV | domain_expert | Confirmed by domain expert |
| Atlas Industrien International | Atlas Industries Group | data_steward | Verified via product specs |
| Quantum Partners NV | Quantum Partners | data_steward | Auto-mapped, validated |
| Atlantic Industrien GmbH | Atlantic Industries AG | data_steward | Auto-mapped, validated |
| Vertex Rohstoffe | Vertex Commodities | data_steward | Auto-mapped, validated |
| Atlantic Industrien Group | Atlantic Industries | system_admin | Verified via product specs |
| Nordic Werkstoffe | Nordic Materials Holdings | domain_expert | Cross-referenced with transactions |
| Atlantic Handel BV | Atlantic Trading BV | domain_expert | Confirmed by domain expert |
| Elite Solutions Group | Elite Solutions | domain_expert | Historical match confirmed |
| Atlantic Logistik SAS | Atlantic Logistics SAS | domain_expert | Auto-mapped, validated |
| Central Ingredients International | Central Ingredients | system_admin | Confirmed by domain expert |
| Premier Industrien SAS | Premier Industries SAS | system_admin | Verified via product specs |
| Global Handel Ltd. | Global Trading Ltd. | domain_expert | Cross-referenced with transactions |
| Horizon Partners International | Horizon Partners | system_admin | Historical match confirmed |
| Premier Enterprise | Premier Enterprise International | system_admin | Historical match confirmed |
| Zenith Handel | Zenith Trading | domain_expert | Verified via product specs |
| Elite Logistik Group | Elite Logistics Holdings | data_steward | Auto-mapped, validated |
| Stellar Vertrieb | Stellar Distribution International | system_admin | Cross-referenced with transactions |
| Premier Handel AG | Premier Trading KG | system_admin | Cross-referenced with transactions |
| Quantum Rohstoffe | Quantum Commodities | system_admin | Confirmed by domain expert |
| Nexus Vertrieb PLC | Nexus Distribution PLC | system_admin | Verified via product specs |
| Prism Chemicals | Prism Chemicals PLC | domain_expert | Auto-mapped, validated |
| Core Partners | Core Partners | data_steward | Confirmed by domain expert |
| Catalyst Rohstoffe SA | Catalyst Commodities SAS | data_steward | Verified via product specs |
| Nexus Partners | Nexus Partners GmbH | domain_expert | Confirmed by domain expert |
| Continental Werkstoffe BV | Continental Materials NV | data_steward | Verified via product specs |
| Stellar Partners | Stellar Partners | system_admin | Historical match confirmed |
| Meridian Vertrieb International | Meridian Distribution | domain_expert | Auto-mapped, validated |
| Premier Handel Group | Premier Trading Group | system_admin | Confirmed by domain expert |
| Horizon Handel PLC | Horizon Trading Ltd. | domain_expert | Confirmed by domain expert |
| Pinnacle Chemicals | Pinnacle Chemicals | system_admin | Historical match confirmed |
| Atlantic Industrien International | Atlantic Industries | domain_expert | Cross-referenced with transactions |
| Stellar Manufacturing Holdings | Stellar Manufacturing Group | domain_expert | Verified via product specs |
| Zenith Manufacturing Ltd. | Zenith Manufacturing PLC | system_admin | Cross-referenced with transactions |
| Core Chemicals AG | Core Chemicals AG | domain_expert | Confirmed by domain expert |
| Apex Werkstoffe | Apex Materials Group | domain_expert | Cross-referenced with transactions |
| Horizon Partners Holdings | Horizon Partners International | data_steward | Historical match confirmed |
| Elite Handel Holdings | Elite Trading | system_admin | Verified via product specs |
| Continental Verarbeitung Holdings | Continental Processing Group | system_admin | Confirmed by domain expert |
| Elite Werkstoffe | Elite Materials NV | data_steward | Historical match confirmed |
| Vanguard Ingredients | Vanguard Ingredients | system_admin | Auto-mapped, validated |
| Nexus Versorgung | Nexus Supply Group | domain_expert | Cross-referenced with transactions |
| Pacific Industrien | Pacific Industries Ltd. | data_steward | Auto-mapped, validated |
| Stratos Partners SAS | Stratos Partners SAS | domain_expert | Historical match confirmed |
| Atlas Logistik International | Atlas Logistics International | data_steward | Historical match confirmed |
| Nexus Ingredients SAS | Nexus Ingredients | data_steward | Cross-referenced with transactions |
| Prism Ingredients | Prism Ingredients | system_admin | Confirmed by domain expert |
| Central Manufacturing Ltd. | Central Manufacturing PLC | domain_expert | Auto-mapped, validated |
| Nordic Chemicals BV | Nordic Chemicals | data_steward | Confirmed by domain expert |
| Prism Werkstoffe | Prism Materials International | domain_expert | Cross-referenced with transactions |
| Quantum Verarbeitung SA | Quantum Processing SA | data_steward | Auto-mapped, validated |
| Global Verarbeitung Group | Global Processing Holdings | domain_expert | Verified via product specs |
| Stratos Verarbeitung LLC | Stratos Processing | system_admin | Confirmed by domain expert |
| Pacific Enterprise SARL | Pacific Enterprise SAS | domain_expert | Cross-referenced with transactions |
| Nordic Manufacturing NV | Nordic Manufacturing NV | domain_expert | Cross-referenced with transactions |
| Premier Vertrieb | Premier Distribution Group | domain_expert | Cross-referenced with transactions |
| Continental Manufacturing | Continental Manufacturing Inc. | data_steward | Verified via product specs |
| Nexus Enterprise BV | Nexus Enterprise | data_steward | Historical match confirmed |
| Baltic Industrien NV | Baltic Industries BV | system_admin | Cross-referenced with transactions |
| Atlas Partners | Atlas Partners Corp. | domain_expert | Cross-referenced with transactions |
| Vertex Handel Holdings | Vertex Trading Group | system_admin | Cross-referenced with transactions |
| Vanguard Logistik International | Vanguard Logistics | system_admin | Confirmed by domain expert |
| Atlantic Vertrieb Holdings | Atlantic Distribution | domain_expert | Cross-referenced with transactions |
| Global Chemicals SAS | Global Chemicals | system_admin | Cross-referenced with transactions |
| Meridian Ingredients | Meridian Ingredients GmbH | domain_expert | Cross-referenced with transactions |
| Prism Chemicals AG | Prism Chemicals KG | domain_expert | Auto-mapped, validated |
| Atlantic Verarbeitung Holdings | Atlantic Processing | domain_expert | Confirmed by domain expert |
| Vertex Vertrieb Group | Vertex Distribution Holdings | data_steward | Cross-referenced with transactions |
| Central Rohstoffe PLC | Central Commodities Ltd. | system_admin | Auto-mapped, validated |
| Atlantic Versorgung LLC | Atlantic Supply | system_admin | Confirmed by domain expert |
| Pinnacle Logistik BV | Pinnacle Logistics BV | system_admin | Verified via product specs |
| Premier Manufacturing NV | Premier Manufacturing NV | system_admin | Historical match confirmed |
| Catalyst Industrien SARL | Catalyst Industries | domain_expert | Verified via product specs |
| Premier Partners SARL | Premier Partners | domain_expert | Historical match confirmed |
| Stellar Versorgung SA | Stellar Supply | domain_expert | Auto-mapped, validated |
| Stratos Versorgung SA | Stratos Supply SAS | data_steward | Verified via product specs |
| Pinnacle Werkstoffe SARL | Pinnacle Materials SA | system_admin | Verified via product specs |
| Vanguard Versorgung BV | Vanguard Supply | system_admin | Auto-mapped, validated |
| Continental Enterprise Holdings | Continental Enterprise Group | system_admin | Confirmed by domain expert |
| Apex Manufacturing | Apex Manufacturing | data_steward | Auto-mapped, validated |
| Apex Verarbeitung | Apex Processing | data_steward | Auto-mapped, validated |
| Pacific Werkstoffe GmbH | Pacific Materials | domain_expert | Auto-mapped, validated |
| Vanguard Vertrieb International | Vanguard Distribution | data_steward | Cross-referenced with transactions |
| Zenith Enterprise SARL | Zenith Enterprise | data_steward | Cross-referenced with transactions |
| Nordic Manufacturing Group | Nordic Manufacturing Holdings | data_steward | Auto-mapped, validated |
| Vertex Logistik Group | Vertex Logistics Holdings | data_steward | Cross-referenced with transactions |
| Global Ingredients NV | Global Ingredients BV | data_steward | Historical match confirmed |
| Quantum Verarbeitung PLC | Quantum Processing Ltd. | data_steward | Confirmed by domain expert |
| Vanguard Vertrieb | Vanguard Distribution | system_admin | Verified via product specs |
| Core Ingredients International | Core Ingredients | data_steward | Historical match confirmed |
| Baltic Versorgung | Baltic Supply Holdings | domain_expert | Verified via product specs |
| Premier Chemicals | Premier Chemicals | system_admin | Cross-referenced with transactions |
| Premier Versorgung PLC | Premier Supply PLC | system_admin | Confirmed by domain expert |
| Meridian Vertrieb International | Meridian Distribution | data_steward | Auto-mapped, validated |
| Premier Logistik KG | Premier Logistics AG | domain_expert | Verified via product specs |
| Global Partners NV | Global Partners | data_steward | Cross-referenced with transactions |
| Nexus Partners SAS | Nexus Partners SAS | data_steward | Verified via product specs |
| Core Manufacturing | Core Manufacturing | domain_expert | Confirmed by domain expert |
| Nordic Vertrieb | Nordic Distribution | system_admin | Cross-referenced with transactions |
| Baltic Chemicals AG | Baltic Chemicals AG | data_steward | Historical match confirmed |
| Quantum Handel Ltd. | Quantum Trading | system_admin | Cross-referenced with transactions |
| Central Werkstoffe NV | Central Materials NV | data_steward | Verified via product specs |
| Central Logistik Holdings | Central Logistics International | domain_expert | Confirmed by domain expert |
| Elite Logistik | Elite Logistics SA | system_admin | Cross-referenced with transactions |
| Continental Partners KG | Continental Partners GmbH | system_admin | Confirmed by domain expert |
| Horizon Vertrieb International | Horizon Distribution Holdings | system_admin | Confirmed by domain expert |
| Vanguard Chemicals SAS | Vanguard Chemicals SAS | system_admin | Auto-mapped, validated |
| Vertex Industrien NV | Vertex Industries BV | data_steward | Historical match confirmed |
| Pinnacle Verarbeitung | Pinnacle Processing | data_steward | Verified via product specs |
| Vertex Rohstoffe GmbH | Vertex Commodities | system_admin | Confirmed by domain expert |
| Catalyst Versorgung International | Catalyst Supply Holdings | domain_expert | Confirmed by domain expert |
| Core Vertrieb | Core Distribution | data_steward | Auto-mapped, validated |
| Nexus Verarbeitung Group | Nexus Processing Holdings | data_steward | Auto-mapped, validated |
| Catalyst Ingredients Holdings | Catalyst Ingredients International | system_admin | Cross-referenced with transactions |
| Prime Rohstoffe PLC | Prime Commodities | data_steward | Verified via product specs |
| Stellar Vertrieb | Stellar Distribution | system_admin | Confirmed by domain expert |
| Nordic Verarbeitung | Nordic Processing SAS | domain_expert | Cross-referenced with transactions |
| Atlantic Chemicals SAS | Atlantic Chemicals SAS | system_admin | Cross-referenced with transactions |
| Global Verarbeitung GmbH | Global Processing KG | data_steward | Historical match confirmed |
| Zenith Industrien LLC | Zenith Industries Corp. | data_steward | Confirmed by domain expert |
| Apex Handel | Apex Trading Holdings | data_steward | Confirmed by domain expert |
| Premier Partners | Premier Partners Group | domain_expert | Historical match confirmed |
| Vertex Vertrieb Holdings | Vertex Distribution | data_steward | Confirmed by domain expert |
| Baltic Manufacturing | Baltic Manufacturing | data_steward | Cross-referenced with transactions |
| Quantum Handel International | Quantum Trading Holdings | domain_expert | Confirmed by domain expert |
| Stellar Manufacturing Group | Stellar Manufacturing Holdings | data_steward | Confirmed by domain expert |
| Baltic Handel | Baltic Trading Holdings | system_admin | Cross-referenced with transactions |
| Catalyst Versorgung International | Catalyst Supply Holdings | system_admin | Verified via product specs |
| Atlantic Verarbeitung Group | Atlantic Processing Holdings | system_admin | Auto-mapped, validated |
| Baltic Verarbeitung Group | Baltic Processing | data_steward | Cross-referenced with transactions |
| Core Partners Ltd. | Core Partners PLC | domain_expert | Historical match confirmed |
| Vertex Chemicals | Vertex Chemicals | domain_expert | Historical match confirmed |
| Vanguard Industrien | Vanguard Industries BV | domain_expert | Confirmed by domain expert |
| Prime Logistik | Prime Logistics | domain_expert | Auto-mapped, validated |
| Pinnacle Werkstoffe | Pinnacle Materials | system_admin | Historical match confirmed |
| Atlantic Werkstoffe | Atlantic Materials | system_admin | Cross-referenced with transactions |
| Core Versorgung GmbH | Core Supply Co. | data_steward | Confirmed by domain expert |
| Catalyst Logistik | Catalyst Logistics | domain_expert | Historical match confirmed |
| Elite Logistik | Elite Logistics | domain_expert | Historical match confirmed |
| Baltic Versorgung GmbH | Baltic Supply Co. | domain_expert | Historical match confirmed |
| Stratos Logistik | Stratos Logistics | data_steward | Historical match confirmed |
| Core Werkstoffe | Core Materials | data_steward | Confirmed by domain expert |
| Vertex Werkstoffe | Vertex Materials | data_steward | Cross-referenced with transactions |
| Meridian Werkstoffe | Meridian Materials | system_admin | Historical match confirmed |
| Vertex Logistik | Vertex Logistics | domain_expert | Confirmed by domain expert |
| Horizon Versorgung GmbH | Horizon Supply Co. | system_admin | Auto-mapped, validated |
| Stellar Sourcing | Stellar Sourcing | domain_expert | Auto-mapped, validated |
| Nexus Sourcing | Nexus Sourcing | system_admin | Auto-mapped, validated |
| Global Logistik | Global Logistics | domain_expert | Confirmed by domain expert |
| Pinnacle Sourcing | Pinnacle Sourcing | data_steward | Verified via product specs |
| Elite Sourcing | Elite Sourcing | domain_expert | Historical match confirmed |
| Vanguard Werkstoffe | Vanguard Materials | data_steward | Verified via product specs |
| Continental Sourcing | Continental Sourcing | system_admin | Historical match confirmed |
| Quantum Versorgung GmbH | Quantum Supply Co. | system_admin | Verified via product specs |
| Zenith Versorgung GmbH | Zenith Supply Co. | data_steward | Historical match confirmed |
| Atlas Versorgung GmbH | Atlas Supply Co. | system_admin | Cross-referenced with transactions |
| Catalyst Logistik | Catalyst Logistics | data_steward | Verified via product specs |
| Prism Werkstoffe | Prism Materials | data_steward | Verified via product specs |
| Global Sourcing | Global Sourcing | data_steward | Verified via product specs |
| Vertex Sourcing | Vertex Sourcing | data_steward | Confirmed by domain expert |
| Atlas Versorgung GmbH | Atlas Supply Co. | system_admin | Verified via product specs |
| Continental Versorgung GmbH | Continental Supply Co. | domain_expert | Verified via product specs |
| Nexus Logistik | Nexus Logistics | domain_expert | Confirmed by domain expert |
| Stellar Logistik | Stellar Logistics | system_admin | Historical match confirmed |
| Premier Logistik | Premier Logistics | domain_expert | Cross-referenced with transactions |
| Apex Werkstoffe | Apex Materials | data_steward | Cross-referenced with transactions |
| Vertex Logistik | Vertex Logistics | domain_expert | Verified via product specs |
| Stellar Werkstoffe | Stellar Materials | system_admin | Cross-referenced with transactions |
| Quantum Versorgung GmbH | Quantum Supply Co. | domain_expert | Cross-referenced with transactions |
| Nexus Logistik | Nexus Logistics | system_admin | Confirmed by domain expert |
| Elite Logistik | Elite Logistics | system_admin | Confirmed by domain expert |
| Prism Sourcing | Prism Sourcing | domain_expert | Verified via product specs |
| Stratos Sourcing | Stratos Sourcing | domain_expert | Auto-mapped, validated |
| Premier Versorgung GmbH | Premier Supply Co. | domain_expert | Auto-mapped, validated |
| Continental Versorgung GmbH | Continental Supply Co. | data_steward | Verified via product specs |
| Nexus Logistik | Nexus Logistics | system_admin | Confirmed by domain expert |
| Atlas Logistik | Atlas Logistics | domain_expert | Auto-mapped, validated |
| Prime Versorgung GmbH | Prime Supply Co. | data_steward | Historical match confirmed |
| Quantum Versorgung GmbH | Quantum Supply Co. | system_admin | Confirmed by domain expert |
| Stellar Logistik | Stellar Logistics | system_admin | Confirmed by domain expert |
| Quantum Sourcing | Quantum Sourcing | domain_expert | Confirmed by domain expert |
| Prism Sourcing | Prism Sourcing | data_steward | Cross-referenced with transactions |
| Central Logistik | Central Logistics | system_admin | Historical match confirmed |
| Premier Versorgung GmbH | Premier Supply Co. | system_admin | Historical match confirmed |
| Apex Versorgung GmbH | Apex Supply Co. | domain_expert | Verified via product specs |
| Stratos Versorgung GmbH | Stratos Supply Co. | system_admin | Cross-referenced with transactions |
| Apex Logistik | Apex Logistics | system_admin | Confirmed by domain expert |
| Premier Logistik | Premier Logistics | data_steward | Confirmed by domain expert |
| Central Werkstoffe | Central Materials | data_steward | Auto-mapped, validated |
| Zenith Logistik | Zenith Logistics | system_admin | Historical match confirmed |
| Nordic Sourcing | Nordic Sourcing | domain_expert | Cross-referenced with transactions |
| Stellar Sourcing | Stellar Sourcing | domain_expert | Auto-mapped, validated |
| Pacific Sourcing | Pacific Sourcing | domain_expert | Cross-referenced with transactions |
| Stratos Sourcing | Stratos Sourcing | system_admin | Verified via product specs |
| Prism Logistik | Prism Logistics | data_steward | Historical match confirmed |
| Nexus Werkstoffe | Nexus Materials | domain_expert | Verified via product specs |
| Meridian Logistik | Meridian Logistics | data_steward | Verified via product specs |
| Prime Werkstoffe | Prime Materials | data_steward | Auto-mapped, validated |
| Horizon Sourcing | Horizon Sourcing | data_steward | Confirmed by domain expert |
| Central Sourcing | Central Sourcing | data_steward | Confirmed by domain expert |
| Atlantic Sourcing | Atlantic Sourcing | data_steward | Verified via product specs |
| Horizon Werkstoffe | Horizon Materials | domain_expert | Historical match confirmed |
| Vanguard Versorgung GmbH | Vanguard Supply Co. | domain_expert | Historical match confirmed |
| Continental Logistik | Continental Logistics | data_steward | Verified via product specs |
| Atlantic Sourcing | Atlantic Sourcing | data_steward | Auto-mapped, validated |
| Catalyst Sourcing | Catalyst Sourcing | data_steward | Cross-referenced with transactions |
| Zenith Versorgung GmbH | Zenith Supply Co. | system_admin | Confirmed by domain expert |
| Nordic Logistik | Nordic Logistics | data_steward | Verified via product specs |
| Atlas Logistik | Atlas Logistics | data_steward | Confirmed by domain expert |
| Baltic Versorgung GmbH | Baltic Supply Co. | data_steward | Historical match confirmed |
| Prism Sourcing | Prism Sourcing | data_steward | Auto-mapped, validated |
| Meridian Sourcing | Meridian Sourcing | data_steward | Confirmed by domain expert |
| Stratos Werkstoffe | Stratos Materials | system_admin | Confirmed by domain expert |
| Baltic Versorgung GmbH | Baltic Supply Co. | domain_expert | Historical match confirmed |
| Vertex Versorgung GmbH | Vertex Supply Co. | system_admin | Auto-mapped, validated |
| Horizon Logistik | Horizon Logistics | system_admin | Cross-referenced with transactions |
| Pacific Werkstoffe | Pacific Materials | system_admin | Historical match confirmed |
| Quantum Versorgung GmbH | Quantum Supply Co. | system_admin | Cross-referenced with transactions |
| Pacific Werkstoffe | Pacific Materials | data_steward | Historical match confirmed |
| Stellar Versorgung GmbH | Stellar Supply Co. | system_admin | Confirmed by domain expert |
| Horizon Sourcing | Horizon Sourcing | domain_expert | Historical match confirmed |
| Nexus Werkstoffe | Nexus Materials | domain_expert | Verified via product specs |
| Baltic Versorgung GmbH | Baltic Supply Co. | data_steward | Confirmed by domain expert |
| Apex Sourcing | Apex Sourcing | domain_expert | Cross-referenced with transactions |
| Atlas Sourcing | Atlas Sourcing | domain_expert | Cross-referenced with transactions |
| Pacific Versorgung GmbH | Pacific Supply Co. | system_admin | Confirmed by domain expert |
| Nexus Werkstoffe | Nexus Materials | domain_expert | Historical match confirmed |
| Apex Sourcing | Apex Sourcing | data_steward | Verified via product specs |
| Meridian Werkstoffe | Meridian Materials | system_admin | Verified via product specs |
| Stellar Logistik | Stellar Logistics | domain_expert | Auto-mapped, validated |
| Prism Werkstoffe | Prism Materials | domain_expert | Cross-referenced with transactions |
| Prism Versorgung GmbH | Prism Supply Co. | data_steward | Cross-referenced with transactions |
| Atlas Logistik | Atlas Logistics | domain_expert | Verified via product specs |
| Central Versorgung GmbH | Central Supply Co. | domain_expert | Cross-referenced with transactions |
| Zenith Logistik | Zenith Logistics | system_admin | Auto-mapped, validated |
| Horizon Sourcing | Horizon Sourcing | system_admin | Confirmed by domain expert |
| Vertex Sourcing | Vertex Sourcing | domain_expert | Confirmed by domain expert |
| Pacific Werkstoffe | Pacific Materials | system_admin | Auto-mapped, validated |
| Atlas Werkstoffe | Atlas Materials | domain_expert | Auto-mapped, validated |
| Nexus Werkstoffe | Nexus Materials | system_admin | Cross-referenced with transactions |
| Meridian Versorgung GmbH | Meridian Supply Co. | data_steward | Confirmed by domain expert |
| Nordic Logistik | Nordic Logistics | system_admin | Verified via product specs |
| Atlantic Versorgung GmbH | Atlantic Supply Co. | data_steward | Cross-referenced with transactions |
| Zenith Logistik | Zenith Logistics | system_admin | Cross-referenced with transactions |
| Catalyst Werkstoffe | Catalyst Materials | domain_expert | Verified via product specs |
| Continental Sourcing | Continental Sourcing | domain_expert | Verified via product specs |
| Stratos Sourcing | Stratos Sourcing | data_steward | Auto-mapped, validated |
| Catalyst Werkstoffe | Catalyst Materials | domain_expert | Auto-mapped, validated |
| Pinnacle Logistik | Pinnacle Logistics | system_admin | Confirmed by domain expert |
| Premier Versorgung GmbH | Premier Supply Co. | domain_expert | Verified via product specs |
| Atlantic Werkstoffe | Atlantic Materials | system_admin | Confirmed by domain expert |
| Meridian Werkstoffe | Meridian Materials | data_steward | Confirmed by domain expert |
| Central Logistik | Central Logistics | domain_expert | Confirmed by domain expert |
| Elite Logistik | Elite Logistics | domain_expert | Verified via product specs |
| Premier Logistik | Premier Logistics | data_steward | Cross-referenced with transactions |
| Core Sourcing | Core Sourcing | domain_expert | Historical match confirmed |
| Elite Werkstoffe | Elite Materials | data_steward | Verified via product specs |
| Pinnacle Sourcing | Pinnacle Sourcing | data_steward | Confirmed by domain expert |
| Vertex Sourcing | Vertex Sourcing | system_admin | Confirmed by domain expert |
| Global Werkstoffe | Global Materials | data_steward | Confirmed by domain expert |
| Vertex Werkstoffe | Vertex Materials | system_admin | Verified via product specs |
| Baltic Logistik | Baltic Logistics | system_admin | Confirmed by domain expert |
| Quantum Versorgung GmbH | Quantum Supply Co. | data_steward | Confirmed by domain expert |
| Prism Sourcing | Prism Sourcing | data_steward | Historical match confirmed |
| Vanguard Werkstoffe | Vanguard Materials | domain_expert | Auto-mapped, validated |
| Stratos Logistik | Stratos Logistics | data_steward | Confirmed by domain expert |
| Elite Sourcing | Elite Sourcing | data_steward | Historical match confirmed |
| Atlantic Werkstoffe | Atlantic Materials | system_admin | Verified via product specs |
| Atlas Versorgung GmbH | Atlas Supply Co. | data_steward | Auto-mapped, validated |
| Nordic Versorgung GmbH | Nordic Supply Co. | data_steward | Verified via product specs |
| Stratos Werkstoffe | Stratos Materials | domain_expert | Auto-mapped, validated |
| Horizon Logistik | Horizon Logistics | data_steward | Verified via product specs |
| Baltic Werkstoffe | Baltic Materials | data_steward | Confirmed by domain expert |
| Quantum Versorgung GmbH | Quantum Supply Co. | data_steward | Auto-mapped, validated |
| Baltic Werkstoffe | Baltic Materials | system_admin | Cross-referenced with transactions |
| Pacific Werkstoffe | Pacific Materials | data_steward | Cross-referenced with transactions |
| Pacific Werkstoffe | Pacific Materials | system_admin | Auto-mapped, validated |
| Stratos Logistik | Stratos Logistics | data_steward | Historical match confirmed |
| Core Logistik | Core Logistics | data_steward | Cross-referenced with transactions |
| Quantum Versorgung GmbH | Quantum Supply Co. | system_admin | Cross-referenced with transactions |
| Elite Logistik | Elite Logistics | system_admin | Cross-referenced with transactions |
| Premier Logistik | Premier Logistics | data_steward | Verified via product specs |
| Baltic Sourcing | Baltic Sourcing | data_steward | Cross-referenced with transactions |
| Elite Werkstoffe | Elite Materials | domain_expert | Verified via product specs |
| Core Sourcing | Core Sourcing | domain_expert | Historical match confirmed |
| Premier Sourcing | Premier Sourcing | data_steward | Auto-mapped, validated |
| Central Werkstoffe | Central Materials | domain_expert | Confirmed by domain expert |
| Baltic Sourcing | Baltic Sourcing | domain_expert | Confirmed by domain expert |
| Vertex Logistik | Vertex Logistics | domain_expert | Cross-referenced with transactions |
| Baltic Sourcing | Baltic Sourcing | domain_expert | Confirmed by domain expert |
| Atlantic Werkstoffe | Atlantic Materials | data_steward | Cross-referenced with transactions |
| Prism Werkstoffe | Prism Materials | domain_expert | Historical match confirmed |
| Atlas Werkstoffe | Atlas Materials | system_admin | Auto-mapped, validated |
| Vertex Werkstoffe | Vertex Materials | system_admin | Auto-mapped, validated |
| Stratos Versorgung GmbH | Stratos Supply Co. | data_steward | Verified via product specs |
| Apex Versorgung GmbH | Apex Supply Co. | data_steward | Historical match confirmed |
| Atlas Werkstoffe | Atlas Materials | system_admin | Confirmed by domain expert |
| Apex Versorgung GmbH | Apex Supply Co. | system_admin | Auto-mapped, validated |
| Vanguard Logistik | Vanguard Logistics | domain_expert | Confirmed by domain expert |
| Pinnacle Sourcing | Pinnacle Sourcing | data_steward | Historical match confirmed |
| Meridian Logistik | Meridian Logistics | data_steward | Verified via product specs |
| Pinnacle Versorgung GmbH | Pinnacle Supply Co. | system_admin | Verified via product specs |
| Pacific Logistik | Pacific Logistics | system_admin | Confirmed by domain expert |
| Stellar Logistik | Stellar Logistics | data_steward | Historical match confirmed |
| Stratos Werkstoffe | Stratos Materials | system_admin | Verified via product specs |
| Vanguard Versorgung GmbH | Vanguard Supply Co. | data_steward | Historical match confirmed |
| Vertex Versorgung GmbH | Vertex Supply Co. | system_admin | Cross-referenced with transactions |
| Stellar Werkstoffe | Stellar Materials | domain_expert | Auto-mapped, validated |
| Atlas Versorgung GmbH | Atlas Supply Co. | data_steward | Cross-referenced with transactions |
| Nexus Werkstoffe | Nexus Materials | domain_expert | Verified via product specs |
| Catalyst Werkstoffe | Catalyst Materials | domain_expert | Historical match confirmed |
| Prime Werkstoffe | Prime Materials | data_steward | Cross-referenced with transactions |
| Vat Reduced GB 15% | Vat Reduced GB 15% | system_admin | Auto-mapped, validated |
| Vat Standardqualität NL 25% | Vat Standard NL 25% | data_steward | Auto-mapped, validated |
| Customs Duty FR 7% | Customs Duty FR 7% | data_steward | Confirmed by domain expert |
| Withholding GB 5% | Withholding GB 5% | domain_expert | Verified via product specs |
| Customs Duty CN 0% | Customs Duty CN 0% | data_steward | Historical match confirmed |
| Vat Standardqualität GB 21% | Vat Standard GB 21% | data_steward | Verified via product specs |
| Customs Duty BR 15% | Customs Duty BR 15% | system_admin | Confirmed by domain expert |
| Vat Standardqualität DE 19% | Vat Standard DE 19% | system_admin | Confirmed by domain expert |
| Vat Standardqualität IN 0% | Vat Standard IN 0% | data_steward | Confirmed by domain expert |
| Customs Duty GB 5% | Customs Duty GB 5% | domain_expert | Cross-referenced with transactions |
| Customs Duty FR 19% | Customs Duty FR 19% | data_steward | Cross-referenced with transactions |
| Vat Standardqualität NL 20% | Vat Standard NL 20% | data_steward | Cross-referenced with transactions |
| Withholding BR 0% | Withholding BR 0% | data_steward | Verified via product specs |
| Withholding BR 15% | Withholding BR 15% | system_admin | Historical match confirmed |
| Vat Standardqualität NL 20% | Vat Standard NL 20% | data_steward | Verified via product specs |
| Withholding US 0% | Withholding US 0% | data_steward | Historical match confirmed |
| Vat Reduced CN 21% | Vat Reduced CN 21% | system_admin | Historical match confirmed |
| Vat Standardqualität DE 10% | Vat Standard DE 10% | system_admin | Confirmed by domain expert |
| Vat Standardqualität US 5% | Vat Standard US 5% | system_admin | Verified via product specs |
| Vat Standardqualität GB 5% | Vat Standard GB 5% | data_steward | Auto-mapped, validated |
| Vat Standardqualität GB 21% | Vat Standard GB 21% | domain_expert | Historical match confirmed |
| Excise IN 25% | Excise IN 25% | data_steward | Confirmed by domain expert |
| Vat Reduced BR 21% | Vat Reduced BR 21% | domain_expert | Verified via product specs |
| Excise GB 19% | Excise GB 19% | domain_expert | Verified via product specs |
| Vat Standardqualität FR 25% | Vat Standard FR 25% | system_admin | Confirmed by domain expert |
| Vat Standardqualität FR 19% | Vat Standard FR 19% | domain_expert | Historical match confirmed |
| Customs Duty FR 19% | Customs Duty FR 19% | data_steward | Historical match confirmed |
| Vat Reduced BR 10% | Vat Reduced BR 10% | domain_expert | Verified via product specs |
| Vat Reduced BR 25% | Vat Reduced BR 25% | data_steward | Verified via product specs |
| Vat Standardqualität BR 0% | Vat Standard BR 0% | domain_expert | Cross-referenced with transactions |
| Vat Standardqualität GB 20% | Vat Standard GB 20% | domain_expert | Cross-referenced with transactions |
| Customs Duty IN 5% | Customs Duty IN 5% | system_admin | Cross-referenced with transactions |
| Customs Duty DE 5% | Customs Duty DE 5% | system_admin | Confirmed by domain expert |
| Vat Reduced GB 19% | Vat Reduced GB 19% | data_steward | Cross-referenced with transactions |
| Excise BR 15% | Excise BR 15% | domain_expert | Auto-mapped, validated |
| Vat Reduced FR 25% | Vat Reduced FR 25% | domain_expert | Confirmed by domain expert |
| Vat Standardqualität US 10% | Vat Standard US 10% | data_steward | Historical match confirmed |
| Withholding NL 7% | Withholding NL 7% | data_steward | Historical match confirmed |
| Excise NL 7% | Excise NL 7% | domain_expert | Auto-mapped, validated |
| Customs Duty DE 15% | Customs Duty DE 15% | system_admin | Confirmed by domain expert |
| Excise US 15% | Excise US 15% | system_admin | Cross-referenced with transactions |
| Withholding US 10% | Withholding US 10% | system_admin | Verified via product specs |
| Excise NL 21% | Excise NL 21% | data_steward | Cross-referenced with transactions |
| Excise US 19% | Excise US 19% | data_steward | Verified via product specs |
| Vat Reduced GB 25% | Vat Reduced GB 25% | domain_expert | Confirmed by domain expert |
| Withholding FR 19% | Withholding FR 19% | domain_expert | Historical match confirmed |
| Vat Reduced BR 7% | Vat Reduced BR 7% | domain_expert | Verified via product specs |
| Vat Reduced IN 20% | Vat Reduced IN 20% | domain_expert | Auto-mapped, validated |
| Vat Reduced BR 0% | Vat Reduced BR 0% | domain_expert | Verified via product specs |
| Vat Reduced FR 0% | Vat Reduced FR 0% | system_admin | Cross-referenced with transactions |
| Customs Duty US 10% | Customs Duty US 10% | domain_expert | Confirmed by domain expert |
| Customs Duty CN 10% | Customs Duty CN 10% | system_admin | Confirmed by domain expert |
| Vat Standardqualität DE 19% | Vat Standard DE 19% | domain_expert | Cross-referenced with transactions |
| Withholding CN 15% | Withholding CN 15% | data_steward | Auto-mapped, validated |
| Vat Reduced NL 19% | Vat Reduced NL 19% | data_steward | Auto-mapped, validated |
| Vat Reduced US 19% | Vat Reduced US 19% | data_steward | Verified via product specs |
| Withholding FR 5% | Withholding FR 5% | domain_expert | Confirmed by domain expert |
| Excise BR 25% | Excise BR 25% | system_admin | Historical match confirmed |
| Excise NL 20% | Excise NL 20% | domain_expert | Confirmed by domain expert |
| Vat Standardqualität IN 10% | Vat Standard IN 10% | system_admin | Auto-mapped, validated |
| Customs Duty CN 25% | Customs Duty CN 25% | system_admin | Confirmed by domain expert |
| Customs Duty US 19% | Customs Duty US 19% | domain_expert | Auto-mapped, validated |
| Vat Reduced DE 5% | Vat Reduced DE 5% | domain_expert | Historical match confirmed |
| Vat Standardqualität CN 10% | Vat Standard CN 10% | domain_expert | Cross-referenced with transactions |
| Excise DE 10% | Excise DE 10% | system_admin | Confirmed by domain expert |
| Excise GB 25% | Excise GB 25% | data_steward | Historical match confirmed |
| Vat Reduced CN 5% | Vat Reduced CN 5% | system_admin | Auto-mapped, validated |
| Customs Duty IN 25% | Customs Duty IN 25% | domain_expert | Auto-mapped, validated |
| Withholding NL 5% | Withholding NL 5% | data_steward | Cross-referenced with transactions |
| Excise US 20% | Excise US 20% | domain_expert | Cross-referenced with transactions |
| Excise NL 15% | Excise NL 15% | system_admin | Confirmed by domain expert |
| Customs Duty BR 7% | Customs Duty BR 7% | data_steward | Cross-referenced with transactions |
| Withholding BR 10% | Withholding BR 10% | domain_expert | Auto-mapped, validated |
| Vat Standardqualität NL 20% | Vat Standard NL 20% | domain_expert | Verified via product specs |
| Vat Standardqualität NL 19% | Vat Standard NL 19% | system_admin | Auto-mapped, validated |
| Vat Reduced CN 19% | Vat Reduced CN 19% | domain_expert | Auto-mapped, validated |
| Vat Reduced NL 0% | Vat Reduced NL 0% | domain_expert | Cross-referenced with transactions |
| Vat Standardqualität NL 5% | Vat Standard NL 5% | system_admin | Verified via product specs |
| Excise DE 10% | Excise DE 10% | system_admin | Auto-mapped, validated |
| Customs Duty CN 25% | Customs Duty CN 25% | data_steward | Auto-mapped, validated |
| Withholding FR 5% | Withholding FR 5% | domain_expert | Confirmed by domain expert |
| Vat Reduced BR 7% | Vat Reduced BR 7% | system_admin | Confirmed by domain expert |
| Excise BR 19% | Excise BR 19% | system_admin | Historical match confirmed |
| Vat Standardqualität IN 5% | Vat Standard IN 5% | system_admin | Cross-referenced with transactions |
| Customs Duty FR 15% | Customs Duty FR 15% | data_steward | Verified via product specs |
| Vat Reduced BR 10% | Vat Reduced BR 10% | domain_expert | Confirmed by domain expert |
| Vat Standardqualität CN 0% | Vat Standard CN 0% | domain_expert | Confirmed by domain expert |
| Customs Duty GB 5% | Customs Duty GB 5% | data_steward | Confirmed by domain expert |
| Customs Duty CN 7% | Customs Duty CN 7% | system_admin | Auto-mapped, validated |
| Customs Duty FR 7% | Customs Duty FR 7% | data_steward | Confirmed by domain expert |
| Vat Standardqualität IN 19% | Vat Standard IN 19% | data_steward | Historical match confirmed |
| Excise US 7% | Excise US 7% | system_admin | Verified via product specs |
| Vat Standardqualität NL 5% | Vat Standard NL 5% | system_admin | Cross-referenced with transactions |
| Vat Reduced CN 19% | Vat Reduced CN 19% | domain_expert | Historical match confirmed |
| Customs Duty IN 20% | Customs Duty IN 20% | data_steward | Cross-referenced with transactions |
| Excise GB 5% | Excise GB 5% | system_admin | Confirmed by domain expert |
| Customs Duty GB 15% | Customs Duty GB 15% | domain_expert | Verified via product specs |
| Excise BR 19% | Excise BR 19% | domain_expert | Confirmed by domain expert |
| Vat Reduced NL 5% | Vat Reduced NL 5% | system_admin | Verified via product specs |
| Vat Reduced FR 20% | Vat Reduced FR 20% | data_steward | Historical match confirmed |
| Vat Standardqualität GB 19% | Vat Standard GB 19% | data_steward | Confirmed by domain expert |
| Vat Standardqualität US 21% | Vat Standard US 21% | domain_expert | Auto-mapped, validated |
| Customs Duty BR 20% | Customs Duty BR 20% | domain_expert | Auto-mapped, validated |
| Excise US 5% | Excise US 5% | domain_expert | Confirmed by domain expert |
| Customs Duty GB 5% | Customs Duty GB 5% | domain_expert | Historical match confirmed |
| Withholding CN 0% | Withholding CN 0% | system_admin | Confirmed by domain expert |
| Customs Duty CN 0% | Customs Duty CN 0% | domain_expert | Cross-referenced with transactions |
| Vat Reduced FR 10% | Vat Reduced FR 10% | system_admin | Verified via product specs |
| Excise DE 21% | Excise DE 21% | data_steward | Cross-referenced with transactions |
| Withholding IN 10% | Withholding IN 10% | data_steward | Auto-mapped, validated |
| Excise CN 20% | Excise CN 20% | domain_expert | Historical match confirmed |
| Vat Reduced CN 15% | Vat Reduced CN 15% | system_admin | Cross-referenced with transactions |
| Vat Reduced GB 15% | Vat Reduced GB 15% | data_steward | Historical match confirmed |
| Excise CN 25% | Excise CN 25% | data_steward | Cross-referenced with transactions |
| Vat Reduced NL 25% | Vat Reduced NL 25% | data_steward | Confirmed by domain expert |
| Customs Duty NL 7% | Customs Duty NL 7% | data_steward | Verified via product specs |
| Withholding GB 15% | Withholding GB 15% | system_admin | Auto-mapped, validated |
| Excise FR 19% | Excise FR 19% | data_steward | Auto-mapped, validated |
| Customs Duty GB 7% | Customs Duty GB 7% | system_admin | Auto-mapped, validated |
| Customs Duty IN 5% | Customs Duty IN 5% | data_steward | Historical match confirmed |
| Withholding NL 21% | Withholding NL 21% | system_admin | Verified via product specs |
| Vat Reduced US 21% | Vat Reduced US 21% | domain_expert | Historical match confirmed |
| Withholding NL 5% | Withholding NL 5% | domain_expert | Confirmed by domain expert |
| Vat Standardqualität NL 19% | Vat Standard NL 19% | system_admin | Cross-referenced with transactions |
| Customs Duty NL 15% | Customs Duty NL 15% | system_admin | Auto-mapped, validated |
| Vat Standardqualität NL 20% | Vat Standard NL 20% | data_steward | Historical match confirmed |
| Customs Duty DE 15% | Customs Duty DE 15% | data_steward | Auto-mapped, validated |
| Customs Duty BR 21% | Customs Duty BR 21% | system_admin | Verified via product specs |
| Vat Reduced GB 25% | Vat Reduced GB 25% | data_steward | Verified via product specs |
| Customs Duty BR 15% | Customs Duty BR 15% | data_steward | Verified via product specs |
| Vat Reduced FR 20% | Vat Reduced FR 20% | domain_expert | Cross-referenced with transactions |
| Vat Standardqualität FR 25% | Vat Standard FR 25% | domain_expert | Confirmed by domain expert |
| Customs Duty DE 20% | Customs Duty DE 20% | domain_expert | Confirmed by domain expert |
| Withholding NL 21% | Withholding NL 21% | data_steward | Auto-mapped, validated |
| Vat Reduced IN 25% | Vat Reduced IN 25% | data_steward | Verified via product specs |
| Customs Duty CN 19% | Customs Duty CN 19% | domain_expert | Cross-referenced with transactions |
| Excise FR 21% | Excise FR 21% | domain_expert | Cross-referenced with transactions |
| Vat Standardqualität FR 0% | Vat Standard FR 0% | data_steward | Verified via product specs |
| Customs Duty FR 25% | Customs Duty FR 25% | domain_expert | Confirmed by domain expert |
| Withholding FR 15% | Withholding FR 15% | system_admin | Cross-referenced with transactions |
| Vat Standardqualität DE 7% | Vat Standard DE 7% | domain_expert | Auto-mapped, validated |
| Vat Standardqualität CN 19% | Vat Standard CN 19% | domain_expert | Verified via product specs |
| Vat Standardqualität IN 0% | Vat Standard IN 0% | data_steward | Historical match confirmed |

#### 4.3.3 Excluded Mappings

The following mappings were identified but NOT migrated due to data quality issues:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-4121-F | Invalid Entry 859 | Superseded by newer mapping |
| NOISE-1050-E | Invalid Entry 370 | Out of scope per business decision |
| NOISE-9441-D | Invalid Entry 202 | Data quality insufficient |
| NOISE-2644-F | Invalid Entry 507 | Duplicate detected |
| NOISE-1440-E | Invalid Entry 667 | Pending validation |
| NOISE-7918-F | Invalid Entry 525 | Duplicate detected |
| NOISE-8672-H | Invalid Entry 282 | Superseded by newer mapping |
| NOISE-8821-D | Invalid Entry 541 | Superseded by newer mapping |
| NOISE-8104-C | Invalid Entry 934 | Data quality insufficient |
| NOISE-5335-D | Invalid Entry 612 | Pending validation |
| NOISE-6233-H | Invalid Entry 328 | Data quality insufficient |
| NOISE-1875-E | Invalid Entry 433 | Pending validation |
| NOISE-4879-F | Invalid Entry 784 | Out of scope per business decision |
| NOISE-2183-C | Invalid Entry 784 | Out of scope per business decision |
| NOISE-4554-F | Invalid Entry 733 | Duplicate detected |
| NOISE-9777-H | Invalid Entry 401 | Pending validation |
| NOISE-1207-B | Invalid Entry 895 | Out of scope per business decision |
| NOISE-9600-H | Invalid Entry 917 | Data quality insufficient |
| NOISE-6949-G | Invalid Entry 875 | Pending validation |
| NOISE-9980-G | Invalid Entry 406 | Pending validation |
| NOISE-1057-F | Invalid Entry 226 | Duplicate detected |
| NOISE-6434-D | Invalid Entry 675 | Pending validation |
| NOISE-2407-H | Invalid Entry 838 | Data quality insufficient |
| NOISE-2368-F | Invalid Entry 698 | Duplicate detected |
| NOISE-8670-A | Invalid Entry 542 | Duplicate detected |
| NOISE-6301-H | Invalid Entry 226 | Pending validation |
| NOISE-6030-F | Invalid Entry 605 | Superseded by newer mapping |
| NOISE-5116-E | Invalid Entry 692 | Pending validation |
| NOISE-7422-C | Invalid Entry 726 | Duplicate detected |
| NOISE-7131-C | Invalid Entry 503 | Data quality insufficient |
| NOISE-4101-G | Invalid Entry 888 | Superseded by newer mapping |
| NOISE-3818-C | Invalid Entry 158 | Data quality insufficient |
| NOISE-9981-H | Invalid Entry 594 | Duplicate detected |
| NOISE-1595-A | Invalid Entry 682 | Out of scope per business decision |
| NOISE-9706-E | Invalid Entry 884 | Duplicate detected |
| NOISE-4904-A | Invalid Entry 654 | Superseded by newer mapping |
| NOISE-3503-B | Invalid Entry 491 | Out of scope per business decision |
| NOISE-3422-A | Invalid Entry 606 | Duplicate detected |
| NOISE-2298-E | Invalid Entry 859 | Superseded by newer mapping |
| NOISE-2948-A | Invalid Entry 343 | Superseded by newer mapping |
| NOISE-5024-E | Invalid Entry 522 | Superseded by newer mapping |
| NOISE-7535-G | Invalid Entry 972 | Data quality insufficient |
| NOISE-1934-H | Invalid Entry 994 | Superseded by newer mapping |
| NOISE-2216-G | Invalid Entry 511 | Superseded by newer mapping |
| NOISE-5622-G | Invalid Entry 636 | Out of scope per business decision |
| NOISE-7281-D | Invalid Entry 265 | Data quality insufficient |
| NOISE-9818-E | Invalid Entry 527 | Pending validation |
| NOISE-9977-A | Invalid Entry 685 | Data quality insufficient |
| NOISE-4595-E | Invalid Entry 851 | Duplicate detected |
| NOISE-6446-B | Invalid Entry 841 | Duplicate detected |
| NOISE-1334-E | Invalid Entry 941 | Superseded by newer mapping |
| NOISE-4511-F | Invalid Entry 290 | Superseded by newer mapping |
| NOISE-7408-F | Invalid Entry 349 | Superseded by newer mapping |
| NOISE-7808-E | Invalid Entry 821 | Superseded by newer mapping |
| NOISE-5655-A | Invalid Entry 644 | Pending validation |
| NOISE-9039-A | Invalid Entry 112 | Duplicate detected |
| NOISE-1212-H | Invalid Entry 152 | Pending validation |
| NOISE-4311-C | Invalid Entry 242 | Out of scope per business decision |
| NOISE-7554-F | Invalid Entry 834 | Out of scope per business decision |
| NOISE-2656-E | Invalid Entry 457 | Superseded by newer mapping |
| NOISE-6396-D | Invalid Entry 845 | Superseded by newer mapping |
| NOISE-7782-B | Invalid Entry 676 | Pending validation |
| NOISE-5653-A | Invalid Entry 670 | Out of scope per business decision |
| NOISE-3274-D | Invalid Entry 160 | Pending validation |
| NOISE-5655-H | Invalid Entry 726 | Superseded by newer mapping |
| NOISE-1107-A | Invalid Entry 669 | Superseded by newer mapping |
| NOISE-1714-D | Invalid Entry 595 | Data quality insufficient |
| NOISE-1985-F | Invalid Entry 988 | Superseded by newer mapping |
| NOISE-8728-E | Invalid Entry 173 | Data quality insufficient |
| NOISE-2494-A | Invalid Entry 920 | Superseded by newer mapping |
| NOISE-1098-D | Invalid Entry 911 | Data quality insufficient |
| NOISE-5730-G | Invalid Entry 525 | Data quality insufficient |
| NOISE-4629-H | Invalid Entry 793 | Duplicate detected |
| NOISE-8593-C | Invalid Entry 396 | Data quality insufficient |
| NOISE-7517-C | Invalid Entry 269 | Pending validation |
| NOISE-1367-F | Invalid Entry 907 | Duplicate detected |
| NOISE-1785-E | Invalid Entry 849 | Data quality insufficient |
| NOISE-4499-B | Invalid Entry 216 | Out of scope per business decision |
| NOISE-3461-A | Invalid Entry 581 | Superseded by newer mapping |
| NOISE-5565-B | Invalid Entry 361 | Duplicate detected |
| NOISE-7137-H | Invalid Entry 799 | Data quality insufficient |
| NOISE-8462-G | Invalid Entry 599 | Out of scope per business decision |
| NOISE-1539-D | Invalid Entry 970 | Superseded by newer mapping |
| NOISE-3671-D | Invalid Entry 337 | Superseded by newer mapping |
| NOISE-4008-C | Invalid Entry 580 | Out of scope per business decision |
| NOISE-7540-G | Invalid Entry 937 | Duplicate detected |
| NOISE-2981-A | Invalid Entry 728 | Duplicate detected |
| NOISE-4338-D | Invalid Entry 226 | Data quality insufficient |
| NOISE-4913-E | Invalid Entry 684 | Duplicate detected |
| NOISE-4054-B | Invalid Entry 574 | Data quality insufficient |
| NOISE-3588-A | Invalid Entry 641 | Out of scope per business decision |
| NOISE-4111-H | Invalid Entry 398 | Duplicate detected |
| NOISE-3628-E | Invalid Entry 513 | Duplicate detected |
| NOISE-9207-H | Invalid Entry 305 | Data quality insufficient |
| NOISE-2934-A | Invalid Entry 636 | Pending validation |
| NOISE-1639-B | Invalid Entry 977 | Pending validation |
| NOISE-4120-F | Invalid Entry 838 | Superseded by newer mapping |
| NOISE-8959-E | Invalid Entry 965 | Duplicate detected |
| NOISE-6810-C | Invalid Entry 979 | Pending validation |
| NOISE-4018-B | Invalid Entry 918 | Pending validation |
| NOISE-7845-H | Invalid Entry 265 | Duplicate detected |
| NOISE-8222-F | Invalid Entry 119 | Out of scope per business decision |
| NOISE-4860-B | Invalid Entry 169 | Data quality insufficient |
| NOISE-6643-H | Invalid Entry 585 | Data quality insufficient |
| NOISE-5157-D | Invalid Entry 252 | Duplicate detected |
| NOISE-7832-C | Invalid Entry 526 | Out of scope per business decision |
| NOISE-8368-H | Invalid Entry 367 | Superseded by newer mapping |
| NOISE-5429-C | Invalid Entry 697 | Data quality insufficient |
| NOISE-1985-E | Invalid Entry 598 | Out of scope per business decision |
| NOISE-4588-C | Invalid Entry 480 | Superseded by newer mapping |
| NOISE-7625-C | Invalid Entry 608 | Superseded by newer mapping |
| NOISE-8063-A | Invalid Entry 310 | Pending validation |
| NOISE-3723-G | Invalid Entry 460 | Duplicate detected |
| NOISE-7916-F | Invalid Entry 305 | Pending validation |
| NOISE-1751-D | Invalid Entry 567 | Pending validation |
| NOISE-7425-E | Invalid Entry 913 | Pending validation |
| NOISE-4112-H | Invalid Entry 705 | Pending validation |
| NOISE-2346-E | Invalid Entry 664 | Duplicate detected |
| NOISE-2345-F | Invalid Entry 479 | Superseded by newer mapping |
| NOISE-2267-D | Invalid Entry 676 | Out of scope per business decision |
| NOISE-4431-H | Invalid Entry 451 | Pending validation |
| NOISE-9317-A | Invalid Entry 220 | Superseded by newer mapping |
| NOISE-9774-E | Invalid Entry 399 | Pending validation |
| NOISE-8483-F | Invalid Entry 287 | Superseded by newer mapping |
| NOISE-3996-A | Invalid Entry 724 | Out of scope per business decision |
| NOISE-7720-F | Invalid Entry 799 | Out of scope per business decision |
| NOISE-7897-D | Invalid Entry 357 | Data quality insufficient |
| NOISE-3919-A | Invalid Entry 997 | Data quality insufficient |
| NOISE-1247-B | Invalid Entry 459 | Out of scope per business decision |
| NOISE-8710-F | Invalid Entry 677 | Out of scope per business decision |
| NOISE-4314-H | Invalid Entry 365 | Data quality insufficient |
| NOISE-5445-A | Invalid Entry 119 | Out of scope per business decision |
| NOISE-9075-B | Invalid Entry 976 | Duplicate detected |
| NOISE-7609-F | Invalid Entry 383 | Pending validation |
| NOISE-6349-H | Invalid Entry 209 | Superseded by newer mapping |
| NOISE-9557-H | Invalid Entry 795 | Data quality insufficient |
| NOISE-5409-H | Invalid Entry 706 | Duplicate detected |
| NOISE-8665-B | Invalid Entry 706 | Duplicate detected |
| NOISE-3005-B | Invalid Entry 794 | Pending validation |
| NOISE-4508-C | Invalid Entry 883 | Pending validation |
| NOISE-3721-E | Invalid Entry 504 | Duplicate detected |
| NOISE-6271-B | Invalid Entry 813 | Duplicate detected |
| NOISE-9708-F | Invalid Entry 173 | Pending validation |
| NOISE-8545-H | Invalid Entry 813 | Duplicate detected |
| NOISE-8319-F | Invalid Entry 313 | Out of scope per business decision |
| NOISE-1688-F | Invalid Entry 439 | Pending validation |
| NOISE-7979-B | Invalid Entry 394 | Pending validation |
| NOISE-5917-F | Invalid Entry 833 | Out of scope per business decision |
| NOISE-4452-F | Invalid Entry 830 | Superseded by newer mapping |
| NOISE-6869-E | Invalid Entry 527 | Duplicate detected |
| NOISE-6720-B | Invalid Entry 192 | Superseded by newer mapping |
| NOISE-9895-G | Invalid Entry 237 | Pending validation |
| NOISE-2511-E | Invalid Entry 945 | Superseded by newer mapping |
| NOISE-7912-A | Invalid Entry 340 | Out of scope per business decision |
| NOISE-2583-H | Invalid Entry 163 | Pending validation |
| NOISE-3659-E | Invalid Entry 863 | Out of scope per business decision |
| NOISE-1293-G | Invalid Entry 577 | Data quality insufficient |
| NOISE-8126-A | Invalid Entry 355 | Data quality insufficient |
| NOISE-2847-A | Invalid Entry 369 | Out of scope per business decision |
| NOISE-9636-F | Invalid Entry 886 | Duplicate detected |
| NOISE-6176-H | Invalid Entry 149 | Data quality insufficient |
| NOISE-1935-F | Invalid Entry 220 | Data quality insufficient |
| NOISE-7972-E | Invalid Entry 691 | Superseded by newer mapping |
| NOISE-3282-E | Invalid Entry 388 | Superseded by newer mapping |
| NOISE-5209-H | Invalid Entry 140 | Out of scope per business decision |
| NOISE-2763-H | Invalid Entry 736 | Out of scope per business decision |
| NOISE-3031-A | Invalid Entry 200 | Out of scope per business decision |
| NOISE-4914-C | Invalid Entry 717 | Duplicate detected |
| NOISE-4267-E | Invalid Entry 939 | Out of scope per business decision |
| NOISE-8814-A | Invalid Entry 101 | Data quality insufficient |
| NOISE-7686-G | Invalid Entry 119 | Pending validation |
| NOISE-7896-F | Invalid Entry 565 | Pending validation |
| NOISE-9177-H | Invalid Entry 743 | Pending validation |
| NOISE-8998-C | Invalid Entry 731 | Out of scope per business decision |
| NOISE-9498-E | Invalid Entry 619 | Duplicate detected |
| NOISE-5454-E | Invalid Entry 857 | Superseded by newer mapping |
| NOISE-5704-D | Invalid Entry 137 | Out of scope per business decision |
| NOISE-9093-F | Invalid Entry 962 | Data quality insufficient |
| NOISE-3163-E | Invalid Entry 187 | Data quality insufficient |
| NOISE-8080-F | Invalid Entry 692 | Pending validation |
| NOISE-6486-A | Invalid Entry 498 | Duplicate detected |
| NOISE-9670-F | Invalid Entry 951 | Data quality insufficient |
| NOISE-8511-E | Invalid Entry 174 | Data quality insufficient |
| NOISE-8120-F | Invalid Entry 228 | Duplicate detected |
| NOISE-7481-H | Invalid Entry 187 | Superseded by newer mapping |
| NOISE-4487-D | Invalid Entry 940 | Superseded by newer mapping |
| NOISE-6338-H | Invalid Entry 965 | Out of scope per business decision |
| NOISE-4541-A | Invalid Entry 441 | Pending validation |
| NOISE-8924-E | Invalid Entry 666 | Superseded by newer mapping |
| NOISE-2605-F | Invalid Entry 454 | Superseded by newer mapping |
| NOISE-1055-C | Invalid Entry 595 | Out of scope per business decision |
| NOISE-3500-F | Invalid Entry 239 | Out of scope per business decision |
| NOISE-7321-B | Invalid Entry 333 | Duplicate detected |
| NOISE-4308-F | Invalid Entry 665 | Out of scope per business decision |
| NOISE-9883-D | Invalid Entry 533 | Out of scope per business decision |
| NOISE-7460-B | Invalid Entry 730 | Duplicate detected |
| NOISE-7318-D | Invalid Entry 385 | Superseded by newer mapping |
| NOISE-8296-A | Invalid Entry 627 | Data quality insufficient |
| NOISE-7474-D | Invalid Entry 970 | Pending validation |
| NOISE-1692-G | Invalid Entry 638 | Pending validation |
| NOISE-7681-C | Invalid Entry 333 | Pending validation |
| NOISE-4601-C | Invalid Entry 797 | Pending validation |
| NOISE-2487-C | Invalid Entry 802 | Out of scope per business decision |
| NOISE-7798-F | Invalid Entry 892 | Data quality insufficient |
| NOISE-4310-D | Invalid Entry 209 | Pending validation |
| NOISE-3967-H | Invalid Entry 987 | Pending validation |
| NOISE-6236-C | Invalid Entry 104 | Pending validation |
| NOISE-9408-B | Invalid Entry 669 | Data quality insufficient |
| NOISE-6876-H | Invalid Entry 777 | Data quality insufficient |
| NOISE-3254-H | Invalid Entry 350 | Superseded by newer mapping |
| NOISE-8130-E | Invalid Entry 246 | Out of scope per business decision |
| NOISE-9078-B | Invalid Entry 647 | Duplicate detected |
| NOISE-2877-B | Invalid Entry 691 | Data quality insufficient |
| NOISE-5406-E | Invalid Entry 458 | Superseded by newer mapping |
| NOISE-7210-H | Invalid Entry 361 | Pending validation |
| NOISE-9224-B | Invalid Entry 690 | Duplicate detected |
| NOISE-5145-B | Invalid Entry 998 | Data quality insufficient |
| NOISE-5592-B | Invalid Entry 261 | Duplicate detected |
| NOISE-8676-A | Invalid Entry 403 | Out of scope per business decision |
| NOISE-2894-C | Invalid Entry 743 | Data quality insufficient |
| NOISE-2979-H | Invalid Entry 223 | Duplicate detected |
| NOISE-4964-A | Invalid Entry 500 | Duplicate detected |
| NOISE-9141-F | Invalid Entry 243 | Superseded by newer mapping |
| NOISE-2073-D | Invalid Entry 950 | Pending validation |
| NOISE-8553-B | Invalid Entry 491 | Duplicate detected |
| NOISE-8204-C | Invalid Entry 677 | Superseded by newer mapping |
| NOISE-5810-H | Invalid Entry 938 | Superseded by newer mapping |
| NOISE-8788-E | Invalid Entry 849 | Superseded by newer mapping |
| NOISE-3655-C | Invalid Entry 738 | Superseded by newer mapping |
| NOISE-2241-B | Invalid Entry 195 | Superseded by newer mapping |
| NOISE-4198-D | Invalid Entry 245 | Pending validation |
| NOISE-8557-F | Invalid Entry 268 | Duplicate detected |
| NOISE-3598-A | Invalid Entry 865 | Superseded by newer mapping |
| NOISE-6985-G | Invalid Entry 226 | Superseded by newer mapping |
| NOISE-3779-E | Invalid Entry 176 | Out of scope per business decision |
| NOISE-7331-G | Invalid Entry 696 | Duplicate detected |
| NOISE-4605-E | Invalid Entry 101 | Out of scope per business decision |
| NOISE-8419-E | Invalid Entry 498 | Out of scope per business decision |
| NOISE-2893-E | Invalid Entry 547 | Out of scope per business decision |
| NOISE-2173-G | Invalid Entry 838 | Superseded by newer mapping |
| NOISE-8759-D | Invalid Entry 682 | Duplicate detected |
| NOISE-5029-E | Invalid Entry 810 | Duplicate detected |
| NOISE-9342-D | Invalid Entry 962 | Superseded by newer mapping |
| NOISE-1189-A | Invalid Entry 916 | Out of scope per business decision |
| NOISE-7785-C | Invalid Entry 259 | Pending validation |
| NOISE-2576-A | Invalid Entry 112 | Out of scope per business decision |
| NOISE-7894-D | Invalid Entry 364 | Duplicate detected |
| NOISE-3060-B | Invalid Entry 987 | Data quality insufficient |
| NOISE-5542-C | Invalid Entry 782 | Duplicate detected |
| NOISE-3785-B | Invalid Entry 192 | Data quality insufficient |
| NOISE-6588-D | Invalid Entry 860 | Duplicate detected |
| NOISE-3413-A | Invalid Entry 847 | Duplicate detected |
| NOISE-3116-H | Invalid Entry 528 | Pending validation |
| NOISE-1089-F | Invalid Entry 899 | Data quality insufficient |
| NOISE-9995-A | Invalid Entry 162 | Superseded by newer mapping |
| NOISE-7766-G | Invalid Entry 858 | Data quality insufficient |
| NOISE-3283-B | Invalid Entry 224 | Data quality insufficient |
| NOISE-6879-G | Invalid Entry 264 | Out of scope per business decision |
| NOISE-6448-A | Invalid Entry 740 | Superseded by newer mapping |
| NOISE-5529-E | Invalid Entry 140 | Pending validation |
| NOISE-6140-H | Invalid Entry 618 | Superseded by newer mapping |
| NOISE-1177-E | Invalid Entry 913 | Data quality insufficient |
| NOISE-4229-B | Invalid Entry 370 | Pending validation |
| NOISE-3699-C | Invalid Entry 626 | Data quality insufficient |
| NOISE-3193-F | Invalid Entry 139 | Duplicate detected |
| NOISE-8901-C | Invalid Entry 316 | Superseded by newer mapping |
| NOISE-3604-C | Invalid Entry 775 | Out of scope per business decision |
| NOISE-7948-E | Invalid Entry 875 | Duplicate detected |
| NOISE-7899-B | Invalid Entry 705 | Superseded by newer mapping |
| NOISE-2458-A | Invalid Entry 928 | Duplicate detected |
| NOISE-9373-F | Invalid Entry 845 | Data quality insufficient |
| NOISE-2008-E | Invalid Entry 827 | Out of scope per business decision |
| NOISE-2797-B | Invalid Entry 451 | Pending validation |
| NOISE-6244-A | Invalid Entry 705 | Superseded by newer mapping |
| NOISE-2688-D | Invalid Entry 291 | Superseded by newer mapping |
| NOISE-3818-C | Invalid Entry 908 | Superseded by newer mapping |
| NOISE-4313-D | Invalid Entry 312 | Data quality insufficient |
| NOISE-4620-F | Invalid Entry 747 | Out of scope per business decision |
| NOISE-4777-F | Invalid Entry 291 | Out of scope per business decision |

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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230610_000000`
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
| Technical Lead | John Smith (IT Infrastructure) | john@company.com | +1-555-0102 |
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
