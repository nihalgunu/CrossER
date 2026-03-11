# Migration Runbook: Regional Operations Consolidation

**Document ID**: RB-DELTA_CONSOLIDATION_2023-5744
**Version**: 2.0
**Last Updated**: 2023-07-18
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the Regional Operations Consolidation project.
The migration involves transitioning master data and transactional records from ERP_DELTA
to ERP_ALPHA while maintaining data integrity and business continuity.

**Project Timeline**: 2023-04-15 to 2023-09-18
**Business Sponsor**: Operations Excellence
**Technical Owner**: Regional IT

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
|   ERP_DELTA       |     |   ETL Layer      |     |   ERP_ALPHA       |
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
ERP_DELTA to ERP_ALPHA. All mappings have been validated by the
data stewardship team unless otherwise noted.

### 4.2 Migration Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1343 | Completed |
| Successfully mapped | 951 | Verified |
| Excluded from scope | 285 | Documented |
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

| Source Code (ERP_DELTA) | Target Code (ERP_ALPHA) | Verification | Notes |
|------------------------------|------------------------------|--------------|-------|
| sodium chloride 70% standard | Sodium Chloride 70% Grade B | data_steward | Cross-referenced with transactions |
| resistant starch | Resistant Starch | data_steward | Verified via product specs |
| casein 25% pharma grade | Casein 25% Pharma Grade | data_steward | Verified via product specs |
| ascorbic acid | Ascorbic Acid | data_steward | Confirmed by domain expert |
| isoglucose 70% | Isoglucose 70% | domain_expert | Cross-referenced with transactions |
| pea protein 50% | Pea Protein 50% | data_steward | Auto-mapped, validated |
| sunflower oil 98% premium | Sunflower Oil 98% Premium | data_steward | Historical match confirmed |
| pea protein 99.5% | Pea Protein 99.5% | data_steward | Cross-referenced with transactions |
| ascorbic acid standard | Ascorbic Acid Grade B | data_steward | Historical match confirmed |
| citric acid 70% | Citric Acid 70% | data_steward | Auto-mapped, validated |
| ascorbic acid pharma grade | Ascorbic Acid Pharma Grade | system_admin | Auto-mapped, validated |
| coconut oil food grade | Coconut Oil Food Grade | domain_expert | Verified via product specs |
| palm oil 98% | Palm Oil 98% | domain_expert | Auto-mapped, validated |
| rapeseed oil | Rapeseed Oil | system_admin | Auto-mapped, validated |
| wheat gluten 98% premium | Wheat Gluten 98% Premium | data_steward | Cross-referenced with transactions |
| sodium benzoate 99.5% premium | Sodium Benzoate 99.5% Grade A | domain_expert | Confirmed by domain expert |
| sodium benzoate 99.5% standard | Sodium Benzoate 99.5% Standard | system_admin | Verified via product specs |
| cyclodextrin 98% pharma grade | Cyclodextrin 98% Pharma Grade | data_steward | Cross-referenced with transactions |
| coconut oil premium | Coconut Oil Grade A | domain_expert | Verified via product specs |
| dextrose standard | Dextrose Standard | data_steward | Cross-referenced with transactions |
| lactic acid | Lactic Acid | data_steward | Verified via product specs |
| potassium sorbate | Potassium Sorbate | data_steward | Auto-mapped, validated |
| sodium benzoate 99.5% | Sodium Benzoate 99.5% | domain_expert | Auto-mapped, validated |
| wheat gluten | Wheat Gluten | domain_expert | Verified via product specs |
| palm oil 50% premium | Palm Oil 50% Premium | data_steward | Auto-mapped, validated |
| isoglucose | Isoglucose | system_admin | Verified via product specs |
| pea protein pharma grade | Pea Protein Pharma Grade | data_steward | Auto-mapped, validated |
| soy isolate 70% | Soy Isolate 70% | domain_expert | Historical match confirmed |
| soy isolate 25% tech grade | Soy Isolate 25% Technical | data_steward | Verified via product specs |
| rapeseed oil | Rapeseed Oil | data_steward | Historical match confirmed |
| resistant starch | Resistant Starch | data_steward | Historical match confirmed |
| glucose syrup | Glucose Syrup | system_admin | Confirmed by domain expert |
| resistant starch pharma grade | Resistant Starch Pharma Grade | domain_expert | Confirmed by domain expert |
| casein standard | Casein Standard | system_admin | Confirmed by domain expert |
| sodium benzoate 99.5% | Sodium Benzoate 99.5% | domain_expert | Auto-mapped, validated |
| maltodextrin de5 premium | Maltodextrin DE5 Grade A | data_steward | Confirmed by domain expert |
| rapeseed oil 70% standard | Rapeseed Oil 70% Grade B | data_steward | Verified via product specs |
| sorbic acid food grade | Sorbic Acid Food Grade | data_steward | Verified via product specs |
| lactic acid 98% | Lactic Acid 98% | system_admin | Historical match confirmed |
| ascorbic acid | Ascorbic Acid | data_steward | Verified via product specs |
| coconut oil 25% standard | Coconut Oil 25% Standard | system_admin | Auto-mapped, validated |
| citric acid | Citric Acid | domain_expert | Auto-mapped, validated |
| citric acid pharma grade | Citric Acid Pharma Grade | domain_expert | Historical match confirmed |
| soy isolate 99.5% standard | Soy Isolate 99.5% Standard | system_admin | Historical match confirmed |
| palm oil 98% | Palm Oil 98% | data_steward | Cross-referenced with transactions |
| sunflower oil 50% premium | Sunflower Oil 50% Grade A | domain_expert | Cross-referenced with transactions |
| sorbic acid 98% | Sorbic Acid 98% | domain_expert | Confirmed by domain expert |
| ascorbic acid 99.5% | Ascorbic Acid 99.5% | data_steward | Confirmed by domain expert |
| resistant starch 98% pharma grade | Resistant Starch 98% Pharma Grade | domain_expert | Historical match confirmed |
| sodium benzoate | Sodium Benzoate | domain_expert | Historical match confirmed |
| dextrose 25% tech grade | Dextrose 25% Technical | system_admin | Auto-mapped, validated |
| lactic acid food grade | Lactic Acid Food Grade | system_admin | Cross-referenced with transactions |
| sorbic acid | Sorbic Acid | system_admin | Verified via product specs |
| rapeseed oil tech grade | Rapeseed Oil Technical | data_steward | Auto-mapped, validated |
| dextrin pharma grade | Dextrin Pharma Grade | data_steward | Confirmed by domain expert |
| citric acid 99.5% | Citric Acid 99.5% | domain_expert | Verified via product specs |
| sodium benzoate premium | Sodium Benzoate Premium | data_steward | Confirmed by domain expert |
| dextrose 25% | Dextrose 25% | system_admin | Verified via product specs |
| dextrose | Dextrose | system_admin | Cross-referenced with transactions |
| rapeseed oil tech grade | Rapeseed Oil Technical | data_steward | Cross-referenced with transactions |
| citric acid 99.5% | Citric Acid 99.5% | system_admin | Cross-referenced with transactions |
| resistant starch standard | Resistant Starch Grade B | domain_expert | Cross-referenced with transactions |
| fructose 25% | Fructose 25% | system_admin | Auto-mapped, validated |
| soy isolate 25% | Soy Isolate 25% | domain_expert | Auto-mapped, validated |
| rapeseed oil 99.5% | Rapeseed Oil 99.5% | system_admin | Cross-referenced with transactions |
| glucose syrup 98% food grade | Glucose Syrup 98% Food Grade | data_steward | Confirmed by domain expert |
| soy isolate | Soy Isolate | data_steward | Historical match confirmed |
| dextrose premium | Dextrose Grade A | data_steward | Verified via product specs |
| sodium chloride premium | Sodium Chloride Grade A | data_steward | Auto-mapped, validated |
| dextrin 50% | Dextrin 50% | system_admin | Auto-mapped, validated |
| sodium chloride 98% standard | Sodium Chloride 98% Grade B | domain_expert | Verified via product specs |
| glucose syrup tech grade | Glucose Syrup Technical | domain_expert | Confirmed by domain expert |
| soy isolate 99.5% premium | Soy Isolate 99.5% Premium | domain_expert | Cross-referenced with transactions |
| pea protein standard | Pea Protein Grade B | domain_expert | Verified via product specs |
| soy isolate 25% | Soy Isolate 25% | domain_expert | Historical match confirmed |
| dextrin | Dextrin | system_admin | Verified via product specs |
| wheat gluten standard | Wheat Gluten Grade B | system_admin | Cross-referenced with transactions |
| sunflower oil standard | Sunflower Oil Grade B | domain_expert | Historical match confirmed |
| sunflower oil standard | Sunflower Oil Standard | system_admin | Verified via product specs |
| casein premium | Casein Grade A | system_admin | Confirmed by domain expert |
| dextrin tech grade | Dextrin Technical | domain_expert | Confirmed by domain expert |
| wheat gluten 50% pharma grade | Wheat Gluten 50% Pharma Grade | system_admin | Verified via product specs |
| soy isolate | Soy Isolate | data_steward | Cross-referenced with transactions |
| sodium benzoate premium | Sodium Benzoate Grade A | system_admin | Auto-mapped, validated |
| potassium sorbate | Potassium Sorbate | data_steward | Verified via product specs |
| fructose 99.5% pharma grade | Fructose 99.5% Pharma Grade | data_steward | Auto-mapped, validated |
| sodium benzoate | Sodium Benzoate | data_steward | Verified via product specs |
| sodium benzoate 25% | Sodium Benzoate 25% | data_steward | Verified via product specs |
| calcium carbonate standard | Calcium Carbonate Standard | data_steward | Historical match confirmed |
| ascorbic acid tech grade | Ascorbic Acid Technical | domain_expert | Auto-mapped, validated |
| fructose 25% standard | Fructose 25% Grade B | data_steward | Confirmed by domain expert |
| casein | Casein | data_steward | Cross-referenced with transactions |
| coconut oil | Coconut Oil | system_admin | Confirmed by domain expert |
| potassium sorbate tech grade | Potassium Sorbate Technical | data_steward | Verified via product specs |
| glucose syrup premium | Glucose Syrup Grade A | domain_expert | Auto-mapped, validated |
| isoglucose 70% | Isoglucose 70% | system_admin | Historical match confirmed |
| ascorbic acid 50% tech grade | Ascorbic Acid 50% Technical | domain_expert | Auto-mapped, validated |
| dextrose food grade | Dextrose Food Grade | system_admin | Verified via product specs |
| sodium benzoate | Sodium Benzoate | system_admin | Cross-referenced with transactions |
| palm oil 50% | Palm Oil 50% | data_steward | Cross-referenced with transactions |
| ascorbic acid 98% premium | Ascorbic Acid 98% Premium | data_steward | Auto-mapped, validated |
| sorbic acid 70% | Sorbic Acid 70% | system_admin | Cross-referenced with transactions |
| pea protein standard | Pea Protein Standard | domain_expert | Historical match confirmed |
| citric acid 25% premium | Citric Acid 25% Grade A | data_steward | Verified via product specs |
| sodium chloride 25% premium | Sodium Chloride 25% Premium | data_steward | Auto-mapped, validated |
| calcium carbonate standard | Calcium Carbonate Grade B | system_admin | Historical match confirmed |
| soy isolate | Soy Isolate | domain_expert | Auto-mapped, validated |
| potassium sorbate | Potassium Sorbate | data_steward | Historical match confirmed |
| cyclodextrin pharma grade | Cyclodextrin Pharma Grade | data_steward | Historical match confirmed |
| fructose food grade | Fructose Food Grade | data_steward | Auto-mapped, validated |
| citric acid | Citric Acid | domain_expert | Cross-referenced with transactions |
| ascorbic acid 70% | Ascorbic Acid 70% | data_steward | Historical match confirmed |
| sorbic acid 98% | Sorbic Acid 98% | domain_expert | Verified via product specs |
| cyclodextrin | Cyclodextrin | data_steward | Auto-mapped, validated |
| isoglucose food grade | Isoglucose Food Grade | data_steward | Auto-mapped, validated |
| dextrin 70% | Dextrin 70% | domain_expert | Confirmed by domain expert |
| citric acid | Citric Acid | system_admin | Confirmed by domain expert |
| sunflower oil premium | Sunflower Oil Grade A | domain_expert | Confirmed by domain expert |
| sodium benzoate 98% standard | Sodium Benzoate 98% Standard | data_steward | Verified via product specs |
| lactic acid 98% premium | Lactic Acid 98% Premium | system_admin | Historical match confirmed |
| ascorbic acid premium | Ascorbic Acid Premium | domain_expert | Historical match confirmed |
| glucose syrup tech grade | Glucose Syrup Technical | data_steward | Auto-mapped, validated |
| rapeseed oil tech grade | Rapeseed Oil Technical | data_steward | Historical match confirmed |
| glucose syrup 98% standard | Glucose Syrup 98% Standard | system_admin | Verified via product specs |
| soy isolate premium | Soy Isolate Grade A | system_admin | Auto-mapped, validated |
| rapeseed oil | Rapeseed Oil | system_admin | Cross-referenced with transactions |
| sodium benzoate 99.5% tech grade | Sodium Benzoate 99.5% Technical | data_steward | Confirmed by domain expert |
| dextrose | Dextrose | data_steward | Auto-mapped, validated |
| palm oil | Palm Oil | domain_expert | Cross-referenced with transactions |
| sorbic acid 25% pharma grade | Sorbic Acid 25% Pharma Grade | system_admin | Cross-referenced with transactions |
| ascorbic acid standard | Ascorbic Acid Standard | data_steward | Auto-mapped, validated |
| citric acid food grade | Citric Acid Food Grade | system_admin | Confirmed by domain expert |
| soy isolate premium | Soy Isolate Premium | data_steward | Verified via product specs |
| wheat gluten standard | Wheat Gluten Grade B | system_admin | Confirmed by domain expert |
| glucose syrup 98% | Glucose Syrup 98% | domain_expert | Cross-referenced with transactions |
| rapeseed oil 70% premium | Rapeseed Oil 70% Premium | data_steward | Historical match confirmed |
| citric acid 99.5% | Citric Acid 99.5% | domain_expert | Verified via product specs |
| rapeseed oil | Rapeseed Oil | domain_expert | Cross-referenced with transactions |
| palm oil 98% | Palm Oil 98% | data_steward | Auto-mapped, validated |
| fructose standard | Fructose Grade B | data_steward | Historical match confirmed |
| lactic acid 70% pharma grade | Lactic Acid 70% Pharma Grade | system_admin | Confirmed by domain expert |
| potassium sorbate premium | Potassium Sorbate Grade A | domain_expert | Historical match confirmed |
| sodium chloride | Sodium Chloride | data_steward | Auto-mapped, validated |
| fructose | Fructose | domain_expert | Confirmed by domain expert |
| fructose standard | Fructose Grade B | data_steward | Confirmed by domain expert |
| ascorbic acid | Ascorbic Acid | system_admin | Cross-referenced with transactions |
| pea protein premium | Pea Protein Premium | domain_expert | Auto-mapped, validated |
| fructose | Fructose | domain_expert | Cross-referenced with transactions |
| rapeseed oil 98% | Rapeseed Oil 98% | data_steward | Verified via product specs |
| rapeseed oil 98% standard | Rapeseed Oil 98% Standard | system_admin | Auto-mapped, validated |
| casein | Casein | system_admin | Auto-mapped, validated |
| potassium sorbate 50% standard | Potassium Sorbate 50% Grade B | data_steward | Historical match confirmed |
| rapeseed oil premium | Rapeseed Oil Grade A | domain_expert | Confirmed by domain expert |
| pea protein 98% standard | Pea Protein 98% Grade B | domain_expert | Verified via product specs |
| dextrose premium | Dextrose Grade A | system_admin | Verified via product specs |
| lactic acid | Lactic Acid | data_steward | Historical match confirmed |
| calcium carbonate 50% premium | Calcium Carbonate 50% Grade A | domain_expert | Historical match confirmed |
| lactic acid tech grade | Lactic Acid Technical | domain_expert | Historical match confirmed |
| coconut oil pharma grade | Coconut Oil Pharma Grade | system_admin | Cross-referenced with transactions |
| isoglucose 70% food grade | Isoglucose 70% Food Grade | domain_expert | Cross-referenced with transactions |
| dextrose 25% | Dextrose 25% | data_steward | Historical match confirmed |
| dextrose standard | Dextrose Grade B | data_steward | Confirmed by domain expert |
| resistant starch standard | Resistant Starch Grade B | domain_expert | Confirmed by domain expert |
| lactic acid premium | Lactic Acid Grade A | system_admin | Confirmed by domain expert |
| dextrin premium | Dextrin Grade A | system_admin | Confirmed by domain expert |
| soy isolate 70% | Soy Isolate 70% | domain_expert | Verified via product specs |
| pea protein 25% pharma grade | Pea Protein 25% Pharma Grade | data_steward | Auto-mapped, validated |
| citric acid 99.5% pharma grade | Citric Acid 99.5% Pharma Grade | domain_expert | Auto-mapped, validated |
| pea protein tech grade | Pea Protein Technical | data_steward | Verified via product specs |
| fructose premium | Fructose Grade A | domain_expert | Cross-referenced with transactions |
| glucose syrup | Glucose Syrup | system_admin | Confirmed by domain expert |
| citric acid premium | Citric Acid Premium | domain_expert | Cross-referenced with transactions |
| resistant starch | Resistant Starch | system_admin | Confirmed by domain expert |
| potassium sorbate standard | Potassium Sorbate Standard | system_admin | Confirmed by domain expert |
| citric acid | Citric Acid | domain_expert | Confirmed by domain expert |
| lactic acid food grade | Lactic Acid Food Grade | domain_expert | Cross-referenced with transactions |
| citric acid 25% tech grade | Citric Acid 25% Technical | data_steward | Verified via product specs |
| dextrin 50% | Dextrin 50% | system_admin | Verified via product specs |
| isoglucose | Isoglucose | data_steward | Verified via product specs |
| sunflower oil 70% | Sunflower Oil 70% | system_admin | Verified via product specs |
| pea protein | Pea Protein | system_admin | Historical match confirmed |
| rapeseed oil | Rapeseed Oil | data_steward | Cross-referenced with transactions |
| wheat gluten premium | Wheat Gluten Grade A | domain_expert | Cross-referenced with transactions |
| maltodextrin de18 pharma grade | Maltodextrin DE18 Pharma Grade | domain_expert | Verified via product specs |
| dextrose 70% premium | Dextrose 70% Grade A | domain_expert | Auto-mapped, validated |
| calcium carbonate 50% pharma grade | Calcium Carbonate 50% Pharma Grade | domain_expert | Historical match confirmed |
| rapeseed oil 50% standard | Rapeseed Oil 50% Standard | domain_expert | Confirmed by domain expert |
| sodium benzoate 25% standard | Sodium Benzoate 25% Grade B | system_admin | Auto-mapped, validated |
| sodium benzoate 50% | Sodium Benzoate 50% | system_admin | Confirmed by domain expert |
| coconut oil | Coconut Oil | domain_expert | Cross-referenced with transactions |
| fructose | Fructose | system_admin | Verified via product specs |
| citric acid | Citric Acid | domain_expert | Auto-mapped, validated |
| dextrin premium | Dextrin Premium | system_admin | Cross-referenced with transactions |
| maltodextrin de25 | Maltodextrin DE25 | domain_expert | Cross-referenced with transactions |
| sorbic acid food grade | Sorbic Acid Food Grade | system_admin | Auto-mapped, validated |
| lactic acid food grade | Lactic Acid Food Grade | domain_expert | Cross-referenced with transactions |
| coconut oil standard | Coconut Oil Standard | system_admin | Auto-mapped, validated |
| fructose tech grade | Fructose Technical | domain_expert | Verified via product specs |
| ascorbic acid | Ascorbic Acid | data_steward | Verified via product specs |
| lactic acid | Lactic Acid | domain_expert | Confirmed by domain expert |
| coconut oil 98% food grade | Coconut Oil 98% Food Grade | data_steward | Verified via product specs |
| potassium sorbate tech grade | Potassium Sorbate Technical | system_admin | Confirmed by domain expert |
| rapeseed oil standard | Rapeseed Oil Grade B | domain_expert | Verified via product specs |
| calcium carbonate 25% pharma grade | Calcium Carbonate 25% Pharma Grade | data_steward | Confirmed by domain expert |
| maltodextrin de5 standard | Maltodextrin DE5 Grade B | data_steward | Verified via product specs |
| glucose syrup | Glucose Syrup | data_steward | Confirmed by domain expert |
| maltodextrin de25 | Maltodextrin DE25 | domain_expert | Cross-referenced with transactions |
| lactic acid food grade | Lactic Acid Food Grade | system_admin | Verified via product specs |
| casein 98% standard | Casein 98% Grade B | data_steward | Confirmed by domain expert |
| casein standard | Casein Grade B | system_admin | Historical match confirmed |
| resistant starch tech grade | Resistant Starch Technical | system_admin | Auto-mapped, validated |
| palm oil standard | Palm Oil Grade B | system_admin | Historical match confirmed |
| soy isolate standard | Soy Isolate Standard | data_steward | Auto-mapped, validated |
| ascorbic acid standard | Ascorbic Acid Standard | data_steward | Confirmed by domain expert |
| dextrose 50% | Dextrose 50% | domain_expert | Cross-referenced with transactions |
| resistant starch 70% tech grade | Resistant Starch 70% Technical | data_steward | Auto-mapped, validated |
| glucose syrup food grade | Glucose Syrup Food Grade | data_steward | Confirmed by domain expert |
| pea protein premium | Pea Protein Premium | domain_expert | Auto-mapped, validated |
| sodium benzoate 98% pharma grade | Sodium Benzoate 98% Pharma Grade | system_admin | Auto-mapped, validated |
| wheat gluten 98% | Wheat Gluten 98% | data_steward | Historical match confirmed |
| potassium sorbate 50% tech grade | Potassium Sorbate 50% Technical | domain_expert | Confirmed by domain expert |
| pea protein | Pea Protein | system_admin | Confirmed by domain expert |
| potassium sorbate standard | Potassium Sorbate Grade B | domain_expert | Historical match confirmed |
| sodium chloride 98% standard | Sodium Chloride 98% Standard | data_steward | Confirmed by domain expert |
| fructose 99.5% premium | Fructose 99.5% Grade A | system_admin | Auto-mapped, validated |
| potassium sorbate 25% pharma grade | Potassium Sorbate 25% Pharma Grade | domain_expert | Historical match confirmed |
| sodium benzoate 50% | Sodium Benzoate 50% | domain_expert | Historical match confirmed |
| sodium benzoate | Sodium Benzoate | domain_expert | Historical match confirmed |
| sorbic acid | Sorbic Acid | data_steward | Auto-mapped, validated |
| resistant starch 98% | Resistant Starch 98% | system_admin | Auto-mapped, validated |
| calcium carbonate 99.5% food grade | Calcium Carbonate 99.5% Food Grade | domain_expert | Cross-referenced with transactions |
| fructose 99.5% food grade | Fructose 99.5% Food Grade | domain_expert | Historical match confirmed |
| lactic acid standard | Lactic Acid Standard | data_steward | Historical match confirmed |
| resistant starch tech grade | Resistant Starch Technical | data_steward | Historical match confirmed |
| wheat gluten 99.5% premium | Wheat Gluten 99.5% Grade A | system_admin | Historical match confirmed |
| sodium benzoate 99.5% tech grade | Sodium Benzoate 99.5% Technical | data_steward | Historical match confirmed |
| sodium benzoate 99.5% premium | Sodium Benzoate 99.5% Grade A | domain_expert | Verified via product specs |
| ascorbic acid 50% | Ascorbic Acid 50% | system_admin | Auto-mapped, validated |
| potassium sorbate 50% tech grade | Potassium Sorbate 50% Technical | domain_expert | Cross-referenced with transactions |
| calcium carbonate 50% | Calcium Carbonate 50% | system_admin | Confirmed by domain expert |
| palm oil 50% | Palm Oil 50% | system_admin | Auto-mapped, validated |
| potassium sorbate 98% | Potassium Sorbate 98% | domain_expert | Confirmed by domain expert |
| resistant starch 70% food grade | Resistant Starch 70% Food Grade | system_admin | Historical match confirmed |
| ascorbic acid | Ascorbic Acid | data_steward | Confirmed by domain expert |
| pea protein | Pea Protein | data_steward | Auto-mapped, validated |
| glucose syrup | Glucose Syrup | domain_expert | Verified via product specs |
| calcium carbonate 99.5% | Calcium Carbonate 99.5% | domain_expert | Auto-mapped, validated |
| soy isolate standard | Soy Isolate Grade B | domain_expert | Confirmed by domain expert |
| palm oil 70% premium | Palm Oil 70% Premium | domain_expert | Historical match confirmed |
| lactic acid standard | Lactic Acid Grade B | system_admin | Historical match confirmed |
| palm oil food grade | Palm Oil Food Grade | system_admin | Auto-mapped, validated |
| lactic acid 98% | Lactic Acid 98% | system_admin | Verified via product specs |
| pea protein | Pea Protein | system_admin | Auto-mapped, validated |
| potassium sorbate | Potassium Sorbate | data_steward | Cross-referenced with transactions |
| palm oil pharma grade | Palm Oil Pharma Grade | domain_expert | Historical match confirmed |
| soy isolate tech grade | Soy Isolate Technical | domain_expert | Verified via product specs |
| coconut oil 98% tech grade | Coconut Oil 98% Technical | data_steward | Verified via product specs |
| casein premium | Casein Grade A | system_admin | Confirmed by domain expert |
| coconut oil 98% | Coconut Oil 98% | domain_expert | Cross-referenced with transactions |
| dextrose | Dextrose | system_admin | Auto-mapped, validated |
| sodium chloride | Sodium Chloride | domain_expert | Verified via product specs |
| coconut oil 25% tech grade | Coconut Oil 25% Technical | domain_expert | Confirmed by domain expert |
| lactic acid 98% premium | Lactic Acid 98% Grade A | domain_expert | Confirmed by domain expert |
| isoglucose tech grade | Isoglucose Technical | data_steward | Auto-mapped, validated |
| pea protein 25% | Pea Protein 25% | system_admin | Auto-mapped, validated |
| calcium carbonate 70% | Calcium Carbonate 70% | domain_expert | Historical match confirmed |
| palm oil 99.5% premium | Palm Oil 99.5% Grade A | system_admin | Historical match confirmed |
| resistant starch 50% | Resistant Starch 50% | domain_expert | Verified via product specs |
| ascorbic acid pharma grade | Ascorbic Acid Pharma Grade | system_admin | Cross-referenced with transactions |
| resistant starch food grade | Resistant Starch Food Grade | system_admin | Cross-referenced with transactions |
| sorbic acid 70% | Sorbic Acid 70% | data_steward | Verified via product specs |
| wheat gluten | Wheat Gluten | domain_expert | Auto-mapped, validated |
| sodium benzoate food grade | Sodium Benzoate Food Grade | domain_expert | Confirmed by domain expert |
| wheat gluten | Wheat Gluten | domain_expert | Confirmed by domain expert |
| sodium benzoate 70% | Sodium Benzoate 70% | data_steward | Cross-referenced with transactions |
| sorbic acid standard | Sorbic Acid Standard | data_steward | Auto-mapped, validated |
| citric acid 25% | Citric Acid 25% | system_admin | Verified via product specs |
| pea protein | Pea Protein | data_steward | Auto-mapped, validated |
| calcium carbonate 98% | Calcium Carbonate 98% | system_admin | Confirmed by domain expert |
| wheat gluten food grade | Wheat Gluten Food Grade | data_steward | Verified via product specs |
| citric acid premium | Citric Acid Premium | system_admin | Historical match confirmed |
| coconut oil 25% food grade | Coconut Oil 25% Food Grade | system_admin | Verified via product specs |
| palm oil 99.5% | Palm Oil 99.5% | system_admin | Verified via product specs |
| sodium benzoate | Sodium Benzoate | data_steward | Auto-mapped, validated |
| dextrose tech grade | Dextrose Technical | domain_expert | Historical match confirmed |
| potassium sorbate standard | Potassium Sorbate Standard | system_admin | Verified via product specs |
| dextrose food grade | Dextrose Food Grade | data_steward | Confirmed by domain expert |
| sorbic acid 50% food grade | Sorbic Acid 50% Food Grade | data_steward | Historical match confirmed |
| soy isolate 99.5% | Soy Isolate 99.5% | data_steward | Auto-mapped, validated |
| rapeseed oil premium | Rapeseed Oil Grade A | domain_expert | Verified via product specs |
| cyclodextrin | Cyclodextrin | data_steward | Confirmed by domain expert |
| dextrose standard | Dextrose Standard | system_admin | Cross-referenced with transactions |
| glucose syrup 25% | Glucose Syrup 25% | data_steward | Verified via product specs |
| calcium carbonate | Calcium Carbonate | domain_expert | Auto-mapped, validated |
| resistant starch tech grade | Resistant Starch Technical | domain_expert | Verified via product specs |
| dextrose 99.5% | Dextrose 99.5% | domain_expert | Verified via product specs |
| sodium benzoate 98% | Sodium Benzoate 98% | system_admin | Verified via product specs |
| palm oil 98% premium | Palm Oil 98% Grade A | data_steward | Verified via product specs |
| sodium benzoate 50% | Sodium Benzoate 50% | system_admin | Cross-referenced with transactions |
| resistant starch 50% | Resistant Starch 50% | domain_expert | Cross-referenced with transactions |
| dextrose 70% | Dextrose 70% | system_admin | Auto-mapped, validated |
| dextrin 70% pharma grade | Dextrin 70% Pharma Grade | system_admin | Historical match confirmed |
| sorbic acid pharma grade | Sorbic Acid Pharma Grade | domain_expert | Verified via product specs |
| pea protein | Pea Protein | data_steward | Cross-referenced with transactions |
| fructose 99.5% tech grade | Fructose 99.5% Technical | system_admin | Auto-mapped, validated |
| pea protein 25% | Pea Protein 25% | system_admin | Historical match confirmed |
| ascorbic acid tech grade | Ascorbic Acid Technical | system_admin | Confirmed by domain expert |
| sodium benzoate | Sodium Benzoate | domain_expert | Cross-referenced with transactions |
| lactic acid 25% premium | Lactic Acid 25% Premium | system_admin | Historical match confirmed |
| dextrose tech grade | Dextrose Technical | data_steward | Verified via product specs |
| dextrin 98% | Dextrin 98% | data_steward | Verified via product specs |
| soy isolate food grade | Soy Isolate Food Grade | domain_expert | Verified via product specs |
| calcium carbonate | Calcium Carbonate | data_steward | Historical match confirmed |
| resistant starch 50% | Resistant Starch 50% | system_admin | Verified via product specs |
| potassium sorbate 50% standard | Potassium Sorbate 50% Standard | system_admin | Cross-referenced with transactions |
| palm oil | Palm Oil | system_admin | Verified via product specs |
| fructose 50% standard | Fructose 50% Standard | domain_expert | Verified via product specs |
| maltodextrin de20 | Maltodextrin DE20 | data_steward | Cross-referenced with transactions |
| isoglucose | Isoglucose | system_admin | Confirmed by domain expert |
| cyclodextrin 70% food grade | Cyclodextrin 70% Food Grade | domain_expert | Cross-referenced with transactions |
| ascorbic acid food grade | Ascorbic Acid Food Grade | data_steward | Cross-referenced with transactions |
| sodium chloride | Sodium Chloride | system_admin | Cross-referenced with transactions |
| dextrin | Dextrin | system_admin | Historical match confirmed |
| pea protein 70% premium | Pea Protein 70% Premium | system_admin | Cross-referenced with transactions |
| soy isolate premium | Soy Isolate Premium | domain_expert | Verified via product specs |
| sodium chloride | Sodium Chloride | data_steward | Historical match confirmed |
| lactic acid | Lactic Acid | data_steward | Historical match confirmed |
| glucose syrup 99.5% food grade | Glucose Syrup 99.5% Food Grade | domain_expert | Cross-referenced with transactions |
| sodium benzoate | Sodium Benzoate | domain_expert | Cross-referenced with transactions |
| isoglucose standard | Isoglucose Grade B | data_steward | Confirmed by domain expert |
| lactic acid | Lactic Acid | data_steward | Verified via product specs |
| rapeseed oil 70% tech grade | Rapeseed Oil 70% Technical | domain_expert | Cross-referenced with transactions |
| glucose syrup 25% | Glucose Syrup 25% | system_admin | Historical match confirmed |
| sunflower oil premium | Sunflower Oil Grade A | domain_expert | Verified via product specs |
| fructose 70% | Fructose 70% | data_steward | Cross-referenced with transactions |
| citric acid standard | Citric Acid Standard | data_steward | Confirmed by domain expert |
| casein premium | Casein Grade A | domain_expert | Confirmed by domain expert |
| potassium sorbate | Potassium Sorbate | system_admin | Verified via product specs |
| resistant starch premium | Resistant Starch Grade A | system_admin | Auto-mapped, validated |
| ascorbic acid premium | Ascorbic Acid Premium | data_steward | Auto-mapped, validated |
| sodium chloride 99.5% premium | Sodium Chloride 99.5% Grade A | data_steward | Auto-mapped, validated |
| palm oil 70% tech grade | Palm Oil 70% Technical | system_admin | Confirmed by domain expert |
| wheat gluten premium | Wheat Gluten Grade A | data_steward | Cross-referenced with transactions |
| cyclodextrin | Cyclodextrin | system_admin | Auto-mapped, validated |
| lactic acid tech grade | Lactic Acid Technical | system_admin | Verified via product specs |
| potassium sorbate | Potassium Sorbate | domain_expert | Cross-referenced with transactions |
| sorbic acid 25% standard | Sorbic Acid 25% Grade B | data_steward | Cross-referenced with transactions |
| wheat gluten 70% | Wheat Gluten 70% | system_admin | Historical match confirmed |
| soy isolate 99.5% | Soy Isolate 99.5% | data_steward | Cross-referenced with transactions |
| coconut oil 25% standard | Coconut Oil 25% Grade B | system_admin | Verified via product specs |
| potassium sorbate | Potassium Sorbate | system_admin | Auto-mapped, validated |
| coconut oil 25% | Coconut Oil 25% | data_steward | Confirmed by domain expert |
| dextrose | Dextrose | data_steward | Historical match confirmed |
| sunflower oil 70% food grade | Sunflower Oil 70% Food Grade | domain_expert | Verified via product specs |
| casein 50% premium | Casein 50% Premium | domain_expert | Historical match confirmed |
| lactic acid | Lactic Acid | system_admin | Historical match confirmed |
| palm oil food grade | Palm Oil Food Grade | domain_expert | Confirmed by domain expert |
| resistant starch standard | Resistant Starch Standard | system_admin | Verified via product specs |
| resistant starch | Resistant Starch | domain_expert | Historical match confirmed |
| sodium chloride tech grade | Sodium Chloride Technical | domain_expert | Confirmed by domain expert |
| coconut oil 98% premium | Coconut Oil 98% Premium | data_steward | Confirmed by domain expert |
| potassium sorbate food grade | Potassium Sorbate Food Grade | data_steward | Confirmed by domain expert |
| sunflower oil | Sunflower Oil | domain_expert | Cross-referenced with transactions |
| sunflower oil 50% pharma grade | Sunflower Oil 50% Pharma Grade | domain_expert | Auto-mapped, validated |
| dextrin tech grade | Dextrin Technical | system_admin | Historical match confirmed |
| cyclodextrin standard | Cyclodextrin Standard | domain_expert | Auto-mapped, validated |
| casein 25% tech grade | Casein 25% Technical | data_steward | Historical match confirmed |
| sodium benzoate premium | Sodium Benzoate Grade A | domain_expert | Auto-mapped, validated |
| sunflower oil premium | Sunflower Oil Grade A | system_admin | Verified via product specs |
| fructose standard | Fructose Standard | domain_expert | Historical match confirmed |
| soy isolate 50% premium | Soy Isolate 50% Premium | data_steward | Auto-mapped, validated |
| resistant starch 70% | Resistant Starch 70% | system_admin | Historical match confirmed |
| resistant starch | Resistant Starch | system_admin | Cross-referenced with transactions |
| potassium sorbate food grade | Potassium Sorbate Food Grade | domain_expert | Cross-referenced with transactions |
| citric acid | Citric Acid | system_admin | Auto-mapped, validated |
| soy isolate premium | Soy Isolate Premium | system_admin | Cross-referenced with transactions |
| pea protein standard | Pea Protein Standard | system_admin | Auto-mapped, validated |
| resistant starch 70% | Resistant Starch 70% | domain_expert | Confirmed by domain expert |
| fructose premium | Fructose Premium | system_admin | Verified via product specs |
| dextrose | Dextrose | data_steward | Historical match confirmed |
| dextrose | Dextrose | system_admin | Historical match confirmed |
| sodium chloride 70% | Sodium Chloride 70% | domain_expert | Cross-referenced with transactions |
| catalyst logistics SA | Catalyst Logistics SA | data_steward | Verified via product specs |
| global distribution Corp. | Global Distribution LLC | data_steward | Auto-mapped, validated |
| stellar distribution SA | Stellar Distribution SA | domain_expert | Auto-mapped, validated |
| pinnacle ingredients Ltd. | Pinnacle Ingredients Ltd. | domain_expert | Confirmed by domain expert |
| central solutions | Central Solutions | system_admin | Auto-mapped, validated |
| stratos ingredients | Stratos Ingredients SARL | data_steward | Cross-referenced with transactions |
| pacific logistics Holdings | Pacific Logistics | domain_expert | Cross-referenced with transactions |
| quantum ingredients Holdings | Quantum Ingredients | data_steward | Cross-referenced with transactions |
| core chemicals Group | Core Chemicals International | domain_expert | Confirmed by domain expert |
| continental solutions SARL | Continental Solutions SARL | system_admin | Historical match confirmed |
| pacific chemicals AG | Pacific Chemicals AG | domain_expert | Verified via product specs |
| pacific distribution Group | Pacific Distribution International | domain_expert | Cross-referenced with transactions |
| premier enterprise International | Premier Enterprise International | system_admin | Verified via product specs |
| horizon materials | Horizon Materials PLC | domain_expert | Confirmed by domain expert |
| vertex enterprise Holdings | Vertex Enterprise Holdings | data_steward | Historical match confirmed |
| prime chemicals SA | Prime Chemicals | domain_expert | Auto-mapped, validated |
| stratos trading | Stratos Trading BV | data_steward | Confirmed by domain expert |
| baltic enterprise KG | Baltic Enterprise KG | domain_expert | Cross-referenced with transactions |
| premier logistics Ltd. | Premier Logistics Ltd. | data_steward | Confirmed by domain expert |
| quantum manufacturing GmbH | Quantum Manufacturing KG | data_steward | Auto-mapped, validated |
| continental manufacturing AG | Continental Manufacturing AG | system_admin | Confirmed by domain expert |
| atlas ingredients PLC | Atlas Ingredients PLC | data_steward | Auto-mapped, validated |
| vertex distribution NV | Vertex Distribution NV | domain_expert | Verified via product specs |
| atlas manufacturing | Atlas Manufacturing | system_admin | Verified via product specs |
| atlantic manufacturing Group | Atlantic Manufacturing | domain_expert | Cross-referenced with transactions |
| zenith manufacturing Group | Zenith Manufacturing | domain_expert | Verified via product specs |
| central processing PLC | Central Processing | system_admin | Historical match confirmed |
| stratos supply BV | Stratos Supply | domain_expert | Historical match confirmed |
| stratos supply NV | Stratos Supply | system_admin | Cross-referenced with transactions |
| global processing | Global Processing SAS | data_steward | Cross-referenced with transactions |
| pinnacle supply Holdings | Pinnacle Supply Holdings | domain_expert | Confirmed by domain expert |
| pinnacle industries SAS | Pinnacle Industries SAS | system_admin | Cross-referenced with transactions |
| pinnacle trading Inc. | Pinnacle Trading | domain_expert | Confirmed by domain expert |
| zenith partners | Zenith Partners PLC | data_steward | Cross-referenced with transactions |
| prime supply PLC | Prime Supply | domain_expert | Confirmed by domain expert |
| meridian trading Group | Meridian Trading | system_admin | Historical match confirmed |
| global chemicals Ltd. | Global Chemicals Ltd. | domain_expert | Auto-mapped, validated |
| prism ingredients NV | Prism Ingredients | domain_expert | Cross-referenced with transactions |
| meridian solutions GmbH | Meridian Solutions KG | system_admin | Auto-mapped, validated |
| apex chemicals Inc. | Apex Chemicals | system_admin | Confirmed by domain expert |
| nordic ingredients | Nordic Ingredients PLC | domain_expert | Historical match confirmed |
| global enterprise NV | Global Enterprise NV | domain_expert | Auto-mapped, validated |
| vanguard enterprise International | Vanguard Enterprise International | system_admin | Cross-referenced with transactions |
| global logistics | Global Logistics | domain_expert | Cross-referenced with transactions |
| continental enterprise GmbH | Continental Enterprise KG | domain_expert | Historical match confirmed |
| core logistics Group | Core Logistics Holdings | data_steward | Auto-mapped, validated |
| core chemicals Holdings | Core Chemicals | system_admin | Cross-referenced with transactions |
| nexus industries | Nexus Industries Group | domain_expert | Verified via product specs |
| vertex solutions NV | Vertex Solutions BV | system_admin | Auto-mapped, validated |
| nordic ingredients SARL | Nordic Ingredients SA | data_steward | Auto-mapped, validated |
| atlantic trading | Atlantic Trading | domain_expert | Verified via product specs |
| premier logistics KG | Premier Logistics GmbH | data_steward | Verified via product specs |
| apex trading | Apex Trading Group | domain_expert | Verified via product specs |
| continental ingredients AG | Continental Ingredients | system_admin | Cross-referenced with transactions |
| nexus distribution AG | Nexus Distribution | domain_expert | Auto-mapped, validated |
| catalyst industries Holdings | Catalyst Industries International | data_steward | Cross-referenced with transactions |
| pinnacle commodities BV | Pinnacle Commodities | domain_expert | Verified via product specs |
| premier solutions Corp. | Premier Solutions LLC | data_steward | Historical match confirmed |
| core supply | Core Supply | system_admin | Cross-referenced with transactions |
| apex chemicals Inc. | Apex Chemicals | domain_expert | Historical match confirmed |
| nexus enterprise | Nexus Enterprise International | domain_expert | Auto-mapped, validated |
| apex chemicals International | Apex Chemicals | domain_expert | Confirmed by domain expert |
| atlas chemicals GmbH | Atlas Chemicals | system_admin | Verified via product specs |
| baltic chemicals | Baltic Chemicals Group | domain_expert | Confirmed by domain expert |
| premier industries Holdings | Premier Industries Group | data_steward | Auto-mapped, validated |
| atlantic commodities | Atlantic Commodities | domain_expert | Historical match confirmed |
| prism ingredients | Prism Ingredients | data_steward | Historical match confirmed |
| baltic solutions Inc. | Baltic Solutions | system_admin | Verified via product specs |
| apex ingredients KG | Apex Ingredients AG | data_steward | Auto-mapped, validated |
| vertex distribution SAS | Vertex Distribution SA | domain_expert | Cross-referenced with transactions |
| central manufacturing NV | Central Manufacturing NV | system_admin | Verified via product specs |
| zenith trading LLC | Zenith Trading LLC | domain_expert | Verified via product specs |
| nexus distribution Corp. | Nexus Distribution | data_steward | Auto-mapped, validated |
| meridian chemicals Holdings | Meridian Chemicals International | system_admin | Historical match confirmed |
| pinnacle ingredients GmbH | Pinnacle Ingredients AG | system_admin | Auto-mapped, validated |
| nordic ingredients KG | Nordic Ingredients | system_admin | Verified via product specs |
| continental chemicals Corp. | Continental Chemicals Inc. | domain_expert | Confirmed by domain expert |
| horizon logistics International | Horizon Logistics International | data_steward | Verified via product specs |
| pinnacle chemicals Ltd. | Pinnacle Chemicals PLC | domain_expert | Historical match confirmed |
| nordic manufacturing Group | Nordic Manufacturing | data_steward | Auto-mapped, validated |
| catalyst enterprise | Catalyst Enterprise International | system_admin | Confirmed by domain expert |
| global solutions Group | Global Solutions International | domain_expert | Auto-mapped, validated |
| pacific ingredients NV | Pacific Ingredients BV | system_admin | Verified via product specs |
| atlas solutions | Atlas Solutions BV | data_steward | Verified via product specs |
| atlas enterprise | Atlas Enterprise International | domain_expert | Confirmed by domain expert |
| horizon partners Ltd. | Horizon Partners Ltd. | system_admin | Auto-mapped, validated |
| horizon industries KG | Horizon Industries | domain_expert | Historical match confirmed |
| baltic processing | Baltic Processing PLC | system_admin | Historical match confirmed |
| nexus chemicals Group | Nexus Chemicals Group | data_steward | Auto-mapped, validated |
| zenith partners Inc. | Zenith Partners Corp. | domain_expert | Historical match confirmed |
| prism industries Corp. | Prism Industries | domain_expert | Cross-referenced with transactions |
| prism materials | Prism Materials Ltd. | system_admin | Verified via product specs |
| core materials NV | Core Materials | system_admin | Auto-mapped, validated |
| nexus ingredients Ltd. | Nexus Ingredients PLC | domain_expert | Verified via product specs |
| vertex ingredients | Vertex Ingredients | system_admin | Historical match confirmed |
| continental solutions | Continental Solutions | data_steward | Confirmed by domain expert |
| stellar commodities Holdings | Stellar Commodities | domain_expert | Verified via product specs |
| continental commodities | Continental Commodities GmbH | system_admin | Historical match confirmed |
| atlas industries Holdings | Atlas Industries Group | data_steward | Historical match confirmed |
| vertex commodities AG | Vertex Commodities | domain_expert | Historical match confirmed |
| atlantic processing Holdings | Atlantic Processing International | data_steward | Cross-referenced with transactions |
| quantum trading SARL | Quantum Trading SA | data_steward | Confirmed by domain expert |
| atlantic industries International | Atlantic Industries | data_steward | Confirmed by domain expert |
| central manufacturing Group | Central Manufacturing Holdings | domain_expert | Auto-mapped, validated |
| pinnacle supply | Pinnacle Supply International | system_admin | Auto-mapped, validated |
| atlantic trading BV | Atlantic Trading BV | system_admin | Historical match confirmed |
| elite solutions Holdings | Elite Solutions | system_admin | Verified via product specs |
| atlantic logistics SARL | Atlantic Logistics SAS | system_admin | Confirmed by domain expert |
| stratos processing LLC | Stratos Processing | data_steward | Auto-mapped, validated |
| central ingredients International | Central Ingredients | domain_expert | Cross-referenced with transactions |
| pacific industries International | Pacific Industries Holdings | domain_expert | Historical match confirmed |
| premier industries SARL | Premier Industries SAS | system_admin | Auto-mapped, validated |
| global trading PLC | Global Trading Ltd. | domain_expert | Cross-referenced with transactions |
| premier enterprise Holdings | Premier Enterprise International | data_steward | Historical match confirmed |
| baltic ingredients | Baltic Ingredients SA | data_steward | Verified via product specs |
| zenith trading GmbH | Zenith Trading | system_admin | Cross-referenced with transactions |
| prime solutions | Prime Solutions Holdings | data_steward | Confirmed by domain expert |
| stellar distribution | Stellar Distribution International | system_admin | Cross-referenced with transactions |
| premier trading GmbH | Premier Trading KG | domain_expert | Historical match confirmed |
| nexus distribution Ltd. | Nexus Distribution PLC | data_steward | Auto-mapped, validated |
| central logistics SA | Central Logistics | domain_expert | Verified via product specs |
| prism chemicals | Prism Chemicals PLC | system_admin | Cross-referenced with transactions |
| pinnacle enterprise KG | Pinnacle Enterprise AG | domain_expert | Historical match confirmed |
| stellar processing | Stellar Processing Holdings | data_steward | Verified via product specs |
| stellar partners Holdings | Stellar Partners | system_admin | Auto-mapped, validated |
| meridian distribution Group | Meridian Distribution | domain_expert | Confirmed by domain expert |
| horizon trading Ltd. | Horizon Trading Ltd. | data_steward | Cross-referenced with transactions |
| prism logistics BV | Prism Logistics BV | data_steward | Historical match confirmed |
| atlantic industries International | Atlantic Industries | system_admin | Verified via product specs |
| stellar manufacturing International | Stellar Manufacturing Group | data_steward | Auto-mapped, validated |
| zenith manufacturing PLC | Zenith Manufacturing PLC | system_admin | Verified via product specs |
| apex materials Group | Apex Materials Group | domain_expert | Cross-referenced with transactions |
| horizon partners | Horizon Partners International | data_steward | Verified via product specs |
| elite trading Group | Elite Trading | domain_expert | Confirmed by domain expert |
| continental processing Group | Continental Processing Group | data_steward | Cross-referenced with transactions |
| elite materials NV | Elite Materials NV | data_steward | Verified via product specs |
| baltic solutions Group | Baltic Solutions International | domain_expert | Verified via product specs |
| nexus supply | Nexus Supply Group | system_admin | Verified via product specs |
| pacific industries Ltd. | Pacific Industries Ltd. | domain_expert | Verified via product specs |
| stratos partners SA | Stratos Partners SAS | domain_expert | Confirmed by domain expert |
| nexus ingredients SAS | Nexus Ingredients | domain_expert | Confirmed by domain expert |
| prism ingredients AG | Prism Ingredients | data_steward | Confirmed by domain expert |
| premier trading SARL | Premier Trading SA | system_admin | Auto-mapped, validated |
| prism materials International | Prism Materials International | data_steward | Verified via product specs |
| quantum processing SARL | Quantum Processing SA | system_admin | Historical match confirmed |
| continental ingredients | Continental Ingredients | system_admin | Auto-mapped, validated |
| central manufacturing | Central Manufacturing Holdings | data_steward | Verified via product specs |
| stratos processing | Stratos Processing | data_steward | Confirmed by domain expert |
| premier distribution Group | Premier Distribution Group | domain_expert | Cross-referenced with transactions |
| continental manufacturing Inc. | Continental Manufacturing Inc. | data_steward | Cross-referenced with transactions |
| nexus enterprise NV | Nexus Enterprise | domain_expert | Verified via product specs |
| baltic industries NV | Baltic Industries BV | system_admin | Cross-referenced with transactions |
| atlas partners | Atlas Partners Corp. | system_admin | Confirmed by domain expert |
| elite partners | Elite Partners International | data_steward | Historical match confirmed |
| prism manufacturing Ltd. | Prism Manufacturing PLC | system_admin | Verified via product specs |
| nordic logistics Group | Nordic Logistics | data_steward | Verified via product specs |
| atlas materials | Atlas Materials Holdings | data_steward | Confirmed by domain expert |
| atlantic distribution Holdings | Atlantic Distribution | domain_expert | Verified via product specs |
| zenith materials | Zenith Materials NV | system_admin | Historical match confirmed |
| quantum enterprise BV | Quantum Enterprise NV | data_steward | Auto-mapped, validated |
| global chemicals SARL | Global Chemicals | domain_expert | Historical match confirmed |
| meridian ingredients GmbH | Meridian Ingredients GmbH | domain_expert | Cross-referenced with transactions |
| atlantic processing | Atlantic Processing | domain_expert | Confirmed by domain expert |
| vanguard industries PLC | Vanguard Industries PLC | data_steward | Auto-mapped, validated |
| atlantic supply | Atlantic Supply | system_admin | Auto-mapped, validated |
| meridian trading Group | Meridian Trading Holdings | domain_expert | Confirmed by domain expert |
| pinnacle logistics | Pinnacle Logistics BV | data_steward | Verified via product specs |
| pacific industries | Pacific Industries Group | domain_expert | Historical match confirmed |
| prime materials LLC | Prime Materials Inc. | data_steward | Verified via product specs |
| premier manufacturing BV | Premier Manufacturing NV | data_steward | Verified via product specs |
| catalyst industries SAS | Catalyst Industries | data_steward | Historical match confirmed |
| premier partners SARL | Premier Partners | system_admin | Confirmed by domain expert |
| pinnacle materials SARL | Pinnacle Materials SA | system_admin | Auto-mapped, validated |
| vanguard supply NV | Vanguard Supply | data_steward | Auto-mapped, validated |
| stratos commodities Holdings | Stratos Commodities International | system_admin | Historical match confirmed |
| continental enterprise International | Continental Enterprise Group | domain_expert | Auto-mapped, validated |
| apex manufacturing KG | Apex Manufacturing | domain_expert | Historical match confirmed |
| apex processing Holdings | Apex Processing | data_steward | Cross-referenced with transactions |
| pacific materials GmbH | Pacific Materials | data_steward | Auto-mapped, validated |
| vanguard partners Ltd. | Vanguard Partners PLC | domain_expert | Verified via product specs |
| vanguard distribution International | Vanguard Distribution | data_steward | Historical match confirmed |
| pinnacle logistics International | Pinnacle Logistics International | data_steward | Confirmed by domain expert |
| central partners SARL | Central Partners | system_admin | Auto-mapped, validated |
| vertex logistics Holdings | Vertex Logistics Holdings | system_admin | Cross-referenced with transactions |
| stratos materials Holdings | Stratos Materials International | system_admin | Confirmed by domain expert |
| quantum processing PLC | Quantum Processing Ltd. | domain_expert | Auto-mapped, validated |
| vanguard distribution | Vanguard Distribution | system_admin | Confirmed by domain expert |
| core ingredients | Core Ingredients | system_admin | Auto-mapped, validated |
| baltic supply | Baltic Supply Holdings | domain_expert | Auto-mapped, validated |
| premier chemicals KG | Premier Chemicals | data_steward | Verified via product specs |
| premier supply PLC | Premier Supply PLC | data_steward | Confirmed by domain expert |
| meridian distribution Holdings | Meridian Distribution | system_admin | Verified via product specs |
| premier materials | Premier Materials SAS | system_admin | Cross-referenced with transactions |
| horizon logistics PLC | Horizon Logistics | data_steward | Verified via product specs |
| premier logistics | Premier Logistics AG | domain_expert | Historical match confirmed |
| stratos materials Group | Stratos Materials Group | domain_expert | Auto-mapped, validated |
| global partners BV | Global Partners | domain_expert | Cross-referenced with transactions |
| nexus partners SARL | Nexus Partners SAS | system_admin | Historical match confirmed |
| core manufacturing SA | Core Manufacturing | domain_expert | Historical match confirmed |
| continental processing SA | Continental Processing | system_admin | Verified via product specs |
| baltic chemicals AG | Baltic Chemicals AG | system_admin | Historical match confirmed |
| atlantic trading PLC | Atlantic Trading | domain_expert | Confirmed by domain expert |
| central materials BV | Central Materials NV | data_steward | Verified via product specs |
| central logistics International | Central Logistics International | domain_expert | Historical match confirmed |
| continental partners | Continental Partners GmbH | domain_expert | Confirmed by domain expert |
| core processing Group | Core Processing Holdings | system_admin | Verified via product specs |
| pacific enterprise | Pacific Enterprise International | domain_expert | Cross-referenced with transactions |
| vanguard chemicals | Vanguard Chemicals SAS | system_admin | Verified via product specs |
| vertex industries NV | Vertex Industries BV | data_steward | Confirmed by domain expert |
| pinnacle processing | Pinnacle Processing | system_admin | Confirmed by domain expert |
| vertex commodities KG | Vertex Commodities | domain_expert | Auto-mapped, validated |
| catalyst supply Holdings | Catalyst Supply Holdings | domain_expert | Verified via product specs |
| core distribution BV | Core Distribution | system_admin | Cross-referenced with transactions |
| premier enterprise | Premier Enterprise Group | data_steward | Verified via product specs |
| nordic distribution AG | Nordic Distribution | data_steward | Auto-mapped, validated |
| catalyst ingredients | Catalyst Ingredients International | data_steward | Verified via product specs |
| prime commodities PLC | Prime Commodities | domain_expert | Historical match confirmed |
| pacific materials | Pacific Materials KG | domain_expert | Verified via product specs |
| stellar distribution Corp. | Stellar Distribution | data_steward | Cross-referenced with transactions |
| nordic processing SAS | Nordic Processing SAS | data_steward | Auto-mapped, validated |
| core trading KG | Core Trading | domain_expert | Auto-mapped, validated |
| atlantic chemicals SAS | Atlantic Chemicals SAS | domain_expert | Confirmed by domain expert |
| catalyst processing Holdings | Catalyst Processing International | system_admin | Confirmed by domain expert |
| quantum processing International | Quantum Processing | data_steward | Confirmed by domain expert |
| quantum partners Group | Quantum Partners Group | domain_expert | Auto-mapped, validated |
| zenith partners Inc. | Zenith Partners LLC | system_admin | Historical match confirmed |
| zenith industries | Zenith Industries Corp. | data_steward | Cross-referenced with transactions |
| pinnacle industries KG | Pinnacle Industries | data_steward | Verified via product specs |
| premier partners Group | Premier Partners Group | system_admin | Confirmed by domain expert |
| stratos solutions | Stratos Solutions | data_steward | Verified via product specs |
| vertex distribution International | Vertex Distribution | data_steward | Auto-mapped, validated |
| quantum trading Holdings | Quantum Trading Holdings | data_steward | Auto-mapped, validated |
| nexus logistics International | Nexus Logistics International | system_admin | Verified via product specs |
| stellar manufacturing International | Stellar Manufacturing Holdings | data_steward | Confirmed by domain expert |
| catalyst supply Holdings | Catalyst Supply Holdings | domain_expert | Confirmed by domain expert |
| atlas supply | Atlas Supply Corp. | domain_expert | Verified via product specs |
| baltic processing Holdings | Baltic Processing | domain_expert | Cross-referenced with transactions |
| continental materials Corp. | Continental Materials | system_admin | Historical match confirmed |
| vertex chemicals International | Vertex Chemicals | system_admin | Verified via product specs |
| vanguard industries BV | Vanguard Industries BV | domain_expert | Historical match confirmed |
| atlas industries | Atlas Industries LLC | data_steward | Verified via product specs |
| prime logistics Group | Prime Logistics International | system_admin | Auto-mapped, validated |
| apex logistics LLC | Apex Logistics Inc. | system_admin | Confirmed by domain expert |
| prime logistics | Prime Logistics | system_admin | Cross-referenced with transactions |
| atlantic materials | Atlantic Materials | system_admin | Verified via product specs |
| core supply | Core Supply Co. | domain_expert | Confirmed by domain expert |
| premier supply | Premier Supply Co. | domain_expert | Verified via product specs |
| premier supply | Premier Supply Co. | data_steward | Auto-mapped, validated |
| prism materials | Prism Materials | domain_expert | Historical match confirmed |
| stratos logistics | Stratos Logistics | system_admin | Cross-referenced with transactions |
| core materials | Core Materials | data_steward | Auto-mapped, validated |
| vertex materials | Vertex Materials | system_admin | Confirmed by domain expert |
| meridian materials | Meridian Materials | system_admin | Confirmed by domain expert |
| vertex logistics | Vertex Logistics | domain_expert | Confirmed by domain expert |
| nexus sourcing | Nexus Sourcing | domain_expert | Auto-mapped, validated |
| central logistics | Central Logistics | system_admin | Cross-referenced with transactions |
| pinnacle sourcing | Pinnacle Sourcing | domain_expert | Verified via product specs |
| elite sourcing | Elite Sourcing | data_steward | Auto-mapped, validated |
| vanguard materials | Vanguard Materials | domain_expert | Confirmed by domain expert |
| quantum supply | Quantum Supply Co. | system_admin | Historical match confirmed |
| zenith supply | Zenith Supply Co. | domain_expert | Confirmed by domain expert |
| zenith supply | Zenith Supply Co. | system_admin | Historical match confirmed |
| atlas supply | Atlas Supply Co. | domain_expert | Verified via product specs |
| prism materials | Prism Materials | domain_expert | Cross-referenced with transactions |
| atlas supply | Atlas Supply Co. | system_admin | Auto-mapped, validated |
| nexus logistics | Nexus Logistics | system_admin | Confirmed by domain expert |
| stellar logistics | Stellar Logistics | system_admin | Verified via product specs |
| vertex materials | Vertex Materials | domain_expert | Confirmed by domain expert |
| quantum supply | Quantum Supply Co. | data_steward | Verified via product specs |
| nexus logistics | Nexus Logistics | domain_expert | Cross-referenced with transactions |
| elite logistics | Elite Logistics | system_admin | Verified via product specs |
| stratos sourcing | Stratos Sourcing | data_steward | Auto-mapped, validated |
| continental supply | Continental Supply Co. | data_steward | Cross-referenced with transactions |
| nexus logistics | Nexus Logistics | domain_expert | Auto-mapped, validated |
| horizon materials | Horizon Materials | domain_expert | Verified via product specs |
| quantum sourcing | Quantum Sourcing | domain_expert | Historical match confirmed |
| atlas logistics | Atlas Logistics | domain_expert | Historical match confirmed |
| prime supply | Prime Supply Co. | domain_expert | Historical match confirmed |
| stratos sourcing | Stratos Sourcing | domain_expert | Cross-referenced with transactions |
| quantum supply | Quantum Supply Co. | system_admin | Historical match confirmed |
| quantum sourcing | Quantum Sourcing | system_admin | Historical match confirmed |
| baltic logistics | Baltic Logistics | domain_expert | Cross-referenced with transactions |
| prism sourcing | Prism Sourcing | system_admin | Cross-referenced with transactions |
| central logistics | Central Logistics | domain_expert | Cross-referenced with transactions |
| premier supply | Premier Supply Co. | data_steward | Historical match confirmed |
| apex supply | Apex Supply Co. | data_steward | Auto-mapped, validated |
| apex sourcing | Apex Sourcing | data_steward | Cross-referenced with transactions |
| apex logistics | Apex Logistics | domain_expert | Cross-referenced with transactions |
| elite logistics | Elite Logistics | data_steward | Historical match confirmed |
| central materials | Central Materials | data_steward | Verified via product specs |
| apex logistics | Apex Logistics | system_admin | Historical match confirmed |
| nordic sourcing | Nordic Sourcing | domain_expert | Verified via product specs |
| catalyst supply | Catalyst Supply Co. | data_steward | Historical match confirmed |
| catalyst sourcing | Catalyst Sourcing | system_admin | Historical match confirmed |
| prism logistics | Prism Logistics | system_admin | Historical match confirmed |
| catalyst materials | Catalyst Materials | domain_expert | Historical match confirmed |
| central sourcing | Central Sourcing | domain_expert | Historical match confirmed |
| elite supply | Elite Supply Co. | domain_expert | Historical match confirmed |
| pinnacle supply | Pinnacle Supply Co. | system_admin | Historical match confirmed |
| core sourcing | Core Sourcing | system_admin | Confirmed by domain expert |
| horizon materials | Horizon Materials | system_admin | Historical match confirmed |
| vanguard supply | Vanguard Supply Co. | domain_expert | Confirmed by domain expert |
| catalyst sourcing | Catalyst Sourcing | data_steward | Historical match confirmed |
| zenith supply | Zenith Supply Co. | domain_expert | Verified via product specs |
| nordic logistics | Nordic Logistics | domain_expert | Confirmed by domain expert |
| atlas logistics | Atlas Logistics | system_admin | Confirmed by domain expert |
| continental logistics | Continental Logistics | data_steward | Confirmed by domain expert |
| prism sourcing | Prism Sourcing | domain_expert | Confirmed by domain expert |
| meridian sourcing | Meridian Sourcing | data_steward | Cross-referenced with transactions |
| nordic supply | Nordic Supply Co. | domain_expert | Cross-referenced with transactions |
| stratos materials | Stratos Materials | data_steward | Historical match confirmed |
| baltic supply | Baltic Supply Co. | system_admin | Verified via product specs |
| vertex supply | Vertex Supply Co. | domain_expert | Historical match confirmed |
| quantum supply | Quantum Supply Co. | system_admin | Verified via product specs |
| nexus sourcing | Nexus Sourcing | domain_expert | Cross-referenced with transactions |
| horizon sourcing | Horizon Sourcing | system_admin | Cross-referenced with transactions |
| nexus materials | Nexus Materials | system_admin | Cross-referenced with transactions |
| core logistics | Core Logistics | system_admin | Auto-mapped, validated |
| baltic supply | Baltic Supply Co. | system_admin | Cross-referenced with transactions |
| apex sourcing | Apex Sourcing | domain_expert | Historical match confirmed |
| atlas sourcing | Atlas Sourcing | domain_expert | Historical match confirmed |
| pacific materials | Pacific Materials | data_steward | Verified via product specs |
| vertex logistics | Vertex Logistics | domain_expert | Auto-mapped, validated |
| continental logistics | Continental Logistics | data_steward | Cross-referenced with transactions |
| pacific supply | Pacific Supply Co. | data_steward | Confirmed by domain expert |
| horizon logistics | Horizon Logistics | system_admin | Verified via product specs |
| central logistics | Central Logistics | domain_expert | Verified via product specs |
| nexus materials | Nexus Materials | system_admin | Confirmed by domain expert |
| apex sourcing | Apex Sourcing | system_admin | Cross-referenced with transactions |
| meridian materials | Meridian Materials | domain_expert | Auto-mapped, validated |
| stellar logistics | Stellar Logistics | data_steward | Historical match confirmed |
| prism materials | Prism Materials | domain_expert | Confirmed by domain expert |
| apex logistics | Apex Logistics | domain_expert | Auto-mapped, validated |
| prism supply | Prism Supply Co. | data_steward | Confirmed by domain expert |
| atlas logistics | Atlas Logistics | domain_expert | Historical match confirmed |
| zenith logistics | Zenith Logistics | domain_expert | Auto-mapped, validated |
| pinnacle sourcing | Pinnacle Sourcing | domain_expert | Verified via product specs |
| vertex sourcing | Vertex Sourcing | data_steward | Verified via product specs |
| stratos sourcing | Stratos Sourcing | data_steward | Verified via product specs |
| atlas materials | Atlas Materials | data_steward | Confirmed by domain expert |
| continental supply | Continental Supply Co. | domain_expert | Auto-mapped, validated |
| nexus materials | Nexus Materials | domain_expert | Historical match confirmed |
| atlas materials | Atlas Materials | data_steward | Cross-referenced with transactions |
| zenith logistics | Zenith Logistics | data_steward | Cross-referenced with transactions |
| quantum materials | Quantum Materials | domain_expert | Historical match confirmed |
| zenith sourcing | Zenith Sourcing | domain_expert | Auto-mapped, validated |
| stratos sourcing | Stratos Sourcing | domain_expert | Confirmed by domain expert |
| pinnacle logistics | Pinnacle Logistics | system_admin | Confirmed by domain expert |
| meridian logistics | Meridian Logistics | system_admin | Verified via product specs |
| atlantic materials | Atlantic Materials | data_steward | Auto-mapped, validated |
| meridian materials | Meridian Materials | domain_expert | Auto-mapped, validated |
| pinnacle materials | Pinnacle Materials | system_admin | Historical match confirmed |
| central logistics | Central Logistics | data_steward | Historical match confirmed |
| nexus logistics | Nexus Logistics | data_steward | Auto-mapped, validated |
| global logistics | Global Logistics | system_admin | Verified via product specs |
| core sourcing | Core Sourcing | domain_expert | Historical match confirmed |
| elite materials | Elite Materials | domain_expert | Historical match confirmed |
| pinnacle sourcing | Pinnacle Sourcing | data_steward | Cross-referenced with transactions |
| vertex sourcing | Vertex Sourcing | system_admin | Confirmed by domain expert |
| vertex materials | Vertex Materials | domain_expert | Historical match confirmed |
| pacific sourcing | Pacific Sourcing | domain_expert | Cross-referenced with transactions |
| quantum supply | Quantum Supply Co. | domain_expert | Confirmed by domain expert |
| premier logistics | Premier Logistics | data_steward | Confirmed by domain expert |
| prism sourcing | Prism Sourcing | domain_expert | Cross-referenced with transactions |
| nordic supply | Nordic Supply Co. | data_steward | Cross-referenced with transactions |
| stratos logistics | Stratos Logistics | domain_expert | Cross-referenced with transactions |
| elite sourcing | Elite Sourcing | domain_expert | Auto-mapped, validated |
| catalyst supply | Catalyst Supply Co. | data_steward | Verified via product specs |
| vertex materials | Vertex Materials | system_admin | Historical match confirmed |
| pinnacle supply | Pinnacle Supply Co. | system_admin | Verified via product specs |
| atlantic materials | Atlantic Materials | data_steward | Confirmed by domain expert |
| nordic supply | Nordic Supply Co. | data_steward | Historical match confirmed |
| atlas supply | Atlas Supply Co. | domain_expert | Auto-mapped, validated |
| quantum supply | Quantum Supply Co. | data_steward | Verified via product specs |
| pacific materials | Pacific Materials | system_admin | Historical match confirmed |
| stellar supply | Stellar Supply Co. | system_admin | Cross-referenced with transactions |
| pacific materials | Pacific Materials | data_steward | Cross-referenced with transactions |
| stratos logistics | Stratos Logistics | domain_expert | Confirmed by domain expert |
| quantum supply | Quantum Supply Co. | domain_expert | Auto-mapped, validated |
| elite logistics | Elite Logistics | system_admin | Historical match confirmed |
| apex supply | Apex Supply Co. | domain_expert | Cross-referenced with transactions |
| premier logistics | Premier Logistics | system_admin | Auto-mapped, validated |
| pinnacle supply | Pinnacle Supply Co. | domain_expert | Confirmed by domain expert |
| baltic sourcing | Baltic Sourcing | domain_expert | Confirmed by domain expert |
| elite materials | Elite Materials | data_steward | Historical match confirmed |
| core sourcing | Core Sourcing | system_admin | Auto-mapped, validated |
| premier sourcing | Premier Sourcing | data_steward | Confirmed by domain expert |
| quantum materials | Quantum Materials | domain_expert | Confirmed by domain expert |
| meridian materials | Meridian Materials | system_admin | Historical match confirmed |
| vertex logistics | Vertex Logistics | data_steward | Historical match confirmed |
| nexus sourcing | Nexus Sourcing | data_steward | Verified via product specs |
| baltic sourcing | Baltic Sourcing | system_admin | Auto-mapped, validated |
| atlantic materials | Atlantic Materials | system_admin | Auto-mapped, validated |
| vanguard supply | Vanguard Supply Co. | domain_expert | Confirmed by domain expert |
| prism materials | Prism Materials | system_admin | Historical match confirmed |
| atlas materials | Atlas Materials | system_admin | Historical match confirmed |
| quantum logistics | Quantum Logistics | data_steward | Cross-referenced with transactions |
| vertex materials | Vertex Materials | data_steward | Verified via product specs |
| atlantic logistics | Atlantic Logistics | domain_expert | Verified via product specs |
| prime sourcing | Prime Sourcing | domain_expert | Historical match confirmed |
| stratos supply | Stratos Supply Co. | domain_expert | Verified via product specs |
| atlas materials | Atlas Materials | domain_expert | Auto-mapped, validated |
| apex supply | Apex Supply Co. | domain_expert | Auto-mapped, validated |
| vanguard logistics | Vanguard Logistics | domain_expert | Cross-referenced with transactions |
| atlas supply | Atlas Supply Co. | data_steward | Cross-referenced with transactions |
| pinnacle supply | Pinnacle Supply Co. | data_steward | Verified via product specs |
| stellar logistics | Stellar Logistics | domain_expert | Confirmed by domain expert |
| core supply | Core Supply Co. | domain_expert | Confirmed by domain expert |
| nexus sourcing | Nexus Sourcing | domain_expert | Auto-mapped, validated |
| stellar materials | Stellar Materials | data_steward | Confirmed by domain expert |
| atlas supply | Atlas Supply Co. | domain_expert | Confirmed by domain expert |
| atlantic sourcing | Atlantic Sourcing | data_steward | Verified via product specs |
| prism logistics | Prism Logistics | domain_expert | Cross-referenced with transactions |
| catalyst materials | Catalyst Materials | domain_expert | Auto-mapped, validated |
| pacific supply | Pacific Supply Co. | data_steward | Confirmed by domain expert |
| prime materials | Prime Materials | domain_expert | Cross-referenced with transactions |
| vat reduced gb 15% | Vat Reduced GB 15% | domain_expert | Historical match confirmed |
| excise nl 0% | Excise NL 0% | domain_expert | Confirmed by domain expert |
| excise de 7% | Excise DE 7% | system_admin | Auto-mapped, validated |
| withholding gb 5% | Withholding GB 5% | system_admin | Verified via product specs |
| vat standard gb 21% | Vat Standard GB 21% | domain_expert | Cross-referenced with transactions |
| customs duty fr 19% | Customs Duty FR 19% | domain_expert | Verified via product specs |
| vat standard nl 20% | Vat Standard NL 20% | domain_expert | Verified via product specs |
| withholding br 15% | Withholding BR 15% | domain_expert | Confirmed by domain expert |
| vat standard nl 20% | Vat Standard NL 20% | data_steward | Historical match confirmed |
| withholding us 0% | Withholding US 0% | domain_expert | Cross-referenced with transactions |
| vat reduced cn 21% | Vat Reduced CN 21% | data_steward | Confirmed by domain expert |
| excise in 21% | Excise IN 21% | domain_expert | Cross-referenced with transactions |
| vat standard nl 19% | Vat Standard NL 19% | system_admin | Historical match confirmed |
| vat standard de 10% | Vat Standard DE 10% | data_steward | Cross-referenced with transactions |
| vat standard us 5% | Vat Standard US 5% | domain_expert | Auto-mapped, validated |
| excise fr 0% | Excise FR 0% | domain_expert | Confirmed by domain expert |
| vat standard gb 5% | Vat Standard GB 5% | domain_expert | Auto-mapped, validated |
| vat reduced gb 25% | Vat Reduced GB 25% | data_steward | Cross-referenced with transactions |
| excise in 15% | Excise IN 15% | domain_expert | Cross-referenced with transactions |
| vat standard gb 21% | Vat Standard GB 21% | system_admin | Confirmed by domain expert |
| excise in 25% | Excise IN 25% | domain_expert | Verified via product specs |
| excise gb 19% | Excise GB 19% | data_steward | Auto-mapped, validated |
| vat standard br 0% | Vat Standard BR 0% | data_steward | Verified via product specs |
| vat standard fr 25% | Vat Standard FR 25% | system_admin | Auto-mapped, validated |
| vat standard fr 19% | Vat Standard FR 19% | system_admin | Confirmed by domain expert |
| customs duty fr 19% | Customs Duty FR 19% | system_admin | Auto-mapped, validated |
| vat reduced br 10% | Vat Reduced BR 10% | domain_expert | Verified via product specs |
| withholding gb 21% | Withholding GB 21% | domain_expert | Cross-referenced with transactions |
| vat reduced br 25% | Vat Reduced BR 25% | data_steward | Cross-referenced with transactions |
| vat standard de 7% | Vat Standard DE 7% | data_steward | Auto-mapped, validated |
| customs duty br 5% | Customs Duty BR 5% | system_admin | Verified via product specs |
| vat standard gb 20% | Vat Standard GB 20% | data_steward | Verified via product specs |
| customs duty de 5% | Customs Duty DE 5% | domain_expert | Historical match confirmed |
| vat reduced gb 19% | Vat Reduced GB 19% | data_steward | Auto-mapped, validated |
| excise br 15% | Excise BR 15% | domain_expert | Verified via product specs |
| vat reduced in 5% | Vat Reduced IN 5% | system_admin | Cross-referenced with transactions |
| vat standard us 10% | Vat Standard US 10% | data_steward | Auto-mapped, validated |
| withholding nl 7% | Withholding NL 7% | domain_expert | Confirmed by domain expert |
| excise nl 7% | Excise NL 7% | domain_expert | Historical match confirmed |
| excise us 15% | Excise US 15% | domain_expert | Cross-referenced with transactions |
| withholding de 25% | Withholding DE 25% | domain_expert | Verified via product specs |
| withholding us 10% | Withholding US 10% | data_steward | Historical match confirmed |
| excise nl 21% | Excise NL 21% | data_steward | Historical match confirmed |
| withholding fr 19% | Withholding FR 19% | system_admin | Cross-referenced with transactions |
| withholding fr 21% | Withholding FR 21% | data_steward | Confirmed by domain expert |
| vat reduced in 20% | Vat Reduced IN 20% | domain_expert | Auto-mapped, validated |
| vat standard nl 5% | Vat Standard NL 5% | data_steward | Auto-mapped, validated |
| vat reduced br 15% | Vat Reduced BR 15% | system_admin | Confirmed by domain expert |
| vat reduced fr 0% | Vat Reduced FR 0% | data_steward | Historical match confirmed |
| customs duty us 10% | Customs Duty US 10% | data_steward | Cross-referenced with transactions |
| customs duty cn 10% | Customs Duty CN 10% | data_steward | Verified via product specs |
| excise in 20% | Excise IN 20% | system_admin | Cross-referenced with transactions |
| vat reduced br 21% | Vat Reduced BR 21% | system_admin | Confirmed by domain expert |
| vat reduced nl 19% | Vat Reduced NL 19% | system_admin | Cross-referenced with transactions |
| customs duty us 15% | Customs Duty US 15% | domain_expert | Auto-mapped, validated |
| vat reduced us 19% | Vat Reduced US 19% | system_admin | Auto-mapped, validated |
| excise br 25% | Excise BR 25% | system_admin | Historical match confirmed |
| excise nl 20% | Excise NL 20% | data_steward | Confirmed by domain expert |
| vat standard in 10% | Vat Standard IN 10% | system_admin | Historical match confirmed |
| customs duty cn 25% | Customs Duty CN 25% | data_steward | Historical match confirmed |
| customs duty nl 15% | Customs Duty NL 15% | data_steward | Auto-mapped, validated |
| vat reduced de 5% | Vat Reduced DE 5% | data_steward | Confirmed by domain expert |
| vat standard cn 10% | Vat Standard CN 10% | domain_expert | Confirmed by domain expert |
| customs duty de 5% | Customs Duty DE 5% | system_admin | Auto-mapped, validated |
| excise gb 0% | Excise GB 0% | domain_expert | Verified via product specs |
| excise gb 25% | Excise GB 25% | data_steward | Historical match confirmed |
| vat standard de 21% | Vat Standard DE 21% | system_admin | Verified via product specs |
| vat reduced br 15% | Vat Reduced BR 15% | system_admin | Historical match confirmed |
| customs duty in 25% | Customs Duty IN 25% | system_admin | Cross-referenced with transactions |
| withholding nl 5% | Withholding NL 5% | data_steward | Historical match confirmed |
| excise us 20% | Excise US 20% | domain_expert | Verified via product specs |
| customs duty in 21% | Customs Duty IN 21% | system_admin | Cross-referenced with transactions |
| customs duty br 7% | Customs Duty BR 7% | domain_expert | Auto-mapped, validated |
| withholding br 10% | Withholding BR 10% | system_admin | Auto-mapped, validated |
| vat standard nl 20% | Vat Standard NL 20% | data_steward | Cross-referenced with transactions |
| vat standard nl 19% | Vat Standard NL 19% | domain_expert | Confirmed by domain expert |
| customs duty de 0% | Customs Duty DE 0% | domain_expert | Cross-referenced with transactions |
| vat standard nl 5% | Vat Standard NL 5% | system_admin | Cross-referenced with transactions |
| customs duty cn 25% | Customs Duty CN 25% | domain_expert | Historical match confirmed |
| withholding fr 5% | Withholding FR 5% | domain_expert | Auto-mapped, validated |
| vat standard in 5% | Vat Standard IN 5% | system_admin | Confirmed by domain expert |
| customs duty fr 15% | Customs Duty FR 15% | domain_expert | Auto-mapped, validated |
| customs duty gb 0% | Customs Duty GB 0% | system_admin | Historical match confirmed |
| excise cn 21% | Excise CN 21% | data_steward | Verified via product specs |
| vat reduced br 10% | Vat Reduced BR 10% | system_admin | Auto-mapped, validated |
| vat standard cn 0% | Vat Standard CN 0% | domain_expert | Verified via product specs |
| customs duty gb 5% | Customs Duty GB 5% | data_steward | Verified via product specs |
| customs duty cn 7% | Customs Duty CN 7% | domain_expert | Confirmed by domain expert |
| vat reduced nl 20% | Vat Reduced NL 20% | system_admin | Confirmed by domain expert |
| customs duty de 20% | Customs Duty DE 20% | system_admin | Auto-mapped, validated |
| vat standard gb 19% | Vat Standard GB 19% | data_steward | Verified via product specs |
| customs duty fr 7% | Customs Duty FR 7% | system_admin | Cross-referenced with transactions |
| vat standard in 19% | Vat Standard IN 19% | data_steward | Cross-referenced with transactions |
| withholding cn 20% | Withholding CN 20% | system_admin | Historical match confirmed |
| excise us 7% | Excise US 7% | system_admin | Cross-referenced with transactions |
| vat standard nl 5% | Vat Standard NL 5% | system_admin | Confirmed by domain expert |
| withholding br 20% | Withholding BR 20% | data_steward | Verified via product specs |
| vat reduced cn 19% | Vat Reduced CN 19% | system_admin | Confirmed by domain expert |
| customs duty in 20% | Customs Duty IN 20% | domain_expert | Historical match confirmed |
| excise gb 5% | Excise GB 5% | system_admin | Verified via product specs |
| vat standard us 19% | Vat Standard US 19% | system_admin | Verified via product specs |
| vat reduced nl 5% | Vat Reduced NL 5% | data_steward | Cross-referenced with transactions |
| vat reduced fr 20% | Vat Reduced FR 20% | domain_expert | Cross-referenced with transactions |
| vat standard gb 19% | Vat Standard GB 19% | data_steward | Historical match confirmed |
| excise nl 21% | Excise NL 21% | data_steward | Auto-mapped, validated |
| vat standard us 21% | Vat Standard US 21% | data_steward | Verified via product specs |
| customs duty br 20% | Customs Duty BR 20% | data_steward | Verified via product specs |
| excise us 5% | Excise US 5% | system_admin | Confirmed by domain expert |
| customs duty gb 5% | Customs Duty GB 5% | system_admin | Cross-referenced with transactions |
| vat standard nl 20% | Vat Standard NL 20% | domain_expert | Auto-mapped, validated |
| customs duty cn 0% | Customs Duty CN 0% | system_admin | Cross-referenced with transactions |
| excise cn 21% | Excise CN 21% | data_steward | Verified via product specs |
| vat reduced cn 10% | Vat Reduced CN 10% | system_admin | Cross-referenced with transactions |
| customs duty gb 0% | Customs Duty GB 0% | data_steward | Cross-referenced with transactions |
| excise de 21% | Excise DE 21% | system_admin | Verified via product specs |
| excise cn 20% | Excise CN 20% | system_admin | Confirmed by domain expert |
| vat reduced nl 0% | Vat Reduced NL 0% | domain_expert | Historical match confirmed |
| vat reduced cn 15% | Vat Reduced CN 15% | domain_expert | Verified via product specs |
| vat reduced cn 0% | Vat Reduced CN 0% | data_steward | Confirmed by domain expert |
| vat reduced gb 15% | Vat Reduced GB 15% | data_steward | Confirmed by domain expert |
| withholding nl 19% | Withholding NL 19% | domain_expert | Confirmed by domain expert |
| vat reduced nl 25% | Vat Reduced NL 25% | domain_expert | Confirmed by domain expert |
| withholding gb 15% | Withholding GB 15% | domain_expert | Cross-referenced with transactions |
| vat reduced gb 0% | Vat Reduced GB 0% | domain_expert | Auto-mapped, validated |
| withholding nl 20% | Withholding NL 20% | domain_expert | Historical match confirmed |
| withholding in 20% | Withholding IN 20% | data_steward | Confirmed by domain expert |
| excise fr 21% | Excise FR 21% | domain_expert | Cross-referenced with transactions |
| customs duty gb 7% | Customs Duty GB 7% | system_admin | Auto-mapped, validated |
| withholding nl 21% | Withholding NL 21% | data_steward | Historical match confirmed |
| vat reduced us 21% | Vat Reduced US 21% | system_admin | Cross-referenced with transactions |
| customs duty nl 21% | Customs Duty NL 21% | domain_expert | Auto-mapped, validated |
| customs duty nl 15% | Customs Duty NL 15% | domain_expert | Verified via product specs |
| vat standard nl 20% | Vat Standard NL 20% | data_steward | Verified via product specs |
| customs duty br 21% | Customs Duty BR 21% | domain_expert | Cross-referenced with transactions |
| vat reduced gb 25% | Vat Reduced GB 25% | data_steward | Auto-mapped, validated |
| customs duty br 15% | Customs Duty BR 15% | system_admin | Historical match confirmed |
| withholding nl 15% | Withholding NL 15% | system_admin | Auto-mapped, validated |
| vat reduced fr 20% | Vat Reduced FR 20% | domain_expert | Cross-referenced with transactions |
| withholding us 21% | Withholding US 21% | system_admin | Verified via product specs |
| customs duty de 20% | Customs Duty DE 20% | data_steward | Auto-mapped, validated |
| customs duty de 7% | Customs Duty DE 7% | domain_expert | Cross-referenced with transactions |
| withholding nl 21% | Withholding NL 21% | data_steward | Confirmed by domain expert |
| vat reduced in 25% | Vat Reduced IN 25% | data_steward | Cross-referenced with transactions |
| excise fr 21% | Excise FR 21% | data_steward | Auto-mapped, validated |
| vat standard us 15% | Vat Standard US 15% | domain_expert | Verified via product specs |
| vat standard fr 0% | Vat Standard FR 0% | domain_expert | Verified via product specs |
| customs duty fr 25% | Customs Duty FR 25% | data_steward | Confirmed by domain expert |
| vat reduced in 5% | Vat Reduced IN 5% | data_steward | Cross-referenced with transactions |
| withholding fr 15% | Withholding FR 15% | data_steward | Cross-referenced with transactions |
| customs duty nl 15% | Customs Duty NL 15% | domain_expert | Historical match confirmed |
| vat standard de 7% | Vat Standard DE 7% | system_admin | Cross-referenced with transactions |
| vat standard cn 19% | Vat Standard CN 19% | domain_expert | Historical match confirmed |
| vat standard in 0% | Vat Standard IN 0% | system_admin | Historical match confirmed |

#### 4.3.3 Excluded Mappings

Provisional mappings pending business validation:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-2695-H | Invalid Entry 935 | Data quality insufficient |
| NOISE-7201-A | Invalid Entry 465 | Out of scope per business decision |
| NOISE-1187-G | Invalid Entry 840 | Data quality insufficient |
| NOISE-3966-C | Invalid Entry 886 | Data quality insufficient |
| NOISE-5183-H | Invalid Entry 497 | Pending validation |
| NOISE-7360-G | Invalid Entry 894 | Superseded by newer mapping |
| NOISE-5011-B | Invalid Entry 278 | Pending validation |
| NOISE-4353-A | Invalid Entry 311 | Data quality insufficient |
| NOISE-1384-F | Invalid Entry 437 | Data quality insufficient |
| NOISE-7519-C | Invalid Entry 321 | Out of scope per business decision |
| NOISE-9108-E | Invalid Entry 499 | Superseded by newer mapping |
| NOISE-8585-B | Invalid Entry 760 | Out of scope per business decision |
| NOISE-6153-F | Invalid Entry 183 | Data quality insufficient |
| NOISE-2039-B | Invalid Entry 787 | Out of scope per business decision |
| NOISE-4363-F | Invalid Entry 644 | Pending validation |
| NOISE-7185-F | Invalid Entry 709 | Duplicate detected |
| NOISE-8157-A | Invalid Entry 298 | Data quality insufficient |
| NOISE-7044-B | Invalid Entry 780 | Data quality insufficient |
| NOISE-4012-E | Invalid Entry 738 | Out of scope per business decision |
| NOISE-5680-A | Invalid Entry 309 | Superseded by newer mapping |
| NOISE-5824-A | Invalid Entry 979 | Duplicate detected |
| NOISE-4182-D | Invalid Entry 861 | Data quality insufficient |
| NOISE-2897-H | Invalid Entry 291 | Out of scope per business decision |
| NOISE-3286-A | Invalid Entry 952 | Data quality insufficient |
| NOISE-7816-H | Invalid Entry 197 | Out of scope per business decision |
| NOISE-1318-G | Invalid Entry 976 | Data quality insufficient |
| NOISE-6162-H | Invalid Entry 463 | Duplicate detected |
| NOISE-4022-C | Invalid Entry 148 | Out of scope per business decision |
| NOISE-4286-B | Invalid Entry 564 | Out of scope per business decision |
| NOISE-6616-E | Invalid Entry 783 | Out of scope per business decision |
| NOISE-9718-C | Invalid Entry 217 | Superseded by newer mapping |
| NOISE-1856-A | Invalid Entry 675 | Pending validation |
| NOISE-3716-D | Invalid Entry 760 | Superseded by newer mapping |
| NOISE-9218-A | Invalid Entry 200 | Data quality insufficient |
| NOISE-4001-B | Invalid Entry 329 | Data quality insufficient |
| NOISE-8212-G | Invalid Entry 454 | Data quality insufficient |
| NOISE-7043-B | Invalid Entry 666 | Out of scope per business decision |
| NOISE-7924-E | Invalid Entry 248 | Pending validation |
| NOISE-4535-H | Invalid Entry 649 | Data quality insufficient |
| NOISE-7519-C | Invalid Entry 485 | Out of scope per business decision |
| NOISE-5353-F | Invalid Entry 553 | Duplicate detected |
| NOISE-9921-A | Invalid Entry 784 | Pending validation |
| NOISE-7797-D | Invalid Entry 494 | Data quality insufficient |
| NOISE-7695-F | Invalid Entry 955 | Duplicate detected |
| NOISE-9304-H | Invalid Entry 422 | Pending validation |
| NOISE-8763-B | Invalid Entry 929 | Pending validation |
| NOISE-8090-H | Invalid Entry 359 | Superseded by newer mapping |
| NOISE-5886-B | Invalid Entry 362 | Data quality insufficient |
| NOISE-6589-D | Invalid Entry 419 | Out of scope per business decision |
| NOISE-2550-C | Invalid Entry 762 | Superseded by newer mapping |
| NOISE-8697-C | Invalid Entry 495 | Data quality insufficient |
| NOISE-6976-F | Invalid Entry 935 | Out of scope per business decision |
| NOISE-7024-B | Invalid Entry 396 | Duplicate detected |
| NOISE-5328-G | Invalid Entry 407 | Pending validation |
| NOISE-7165-G | Invalid Entry 236 | Out of scope per business decision |
| NOISE-8405-B | Invalid Entry 355 | Pending validation |
| NOISE-5454-H | Invalid Entry 914 | Data quality insufficient |
| NOISE-4306-E | Invalid Entry 665 | Duplicate detected |
| NOISE-8848-H | Invalid Entry 951 | Pending validation |
| NOISE-7465-H | Invalid Entry 778 | Data quality insufficient |
| NOISE-4632-G | Invalid Entry 454 | Data quality insufficient |
| NOISE-9566-H | Invalid Entry 507 | Data quality insufficient |
| NOISE-5572-G | Invalid Entry 926 | Pending validation |
| NOISE-5525-G | Invalid Entry 264 | Pending validation |
| NOISE-6253-H | Invalid Entry 979 | Duplicate detected |
| NOISE-6802-B | Invalid Entry 445 | Duplicate detected |
| NOISE-4200-B | Invalid Entry 665 | Superseded by newer mapping |
| NOISE-2844-A | Invalid Entry 225 | Out of scope per business decision |
| NOISE-5553-D | Invalid Entry 930 | Superseded by newer mapping |
| NOISE-4770-H | Invalid Entry 146 | Data quality insufficient |
| NOISE-8843-H | Invalid Entry 573 | Duplicate detected |
| NOISE-2826-B | Invalid Entry 191 | Duplicate detected |
| NOISE-5809-E | Invalid Entry 161 | Duplicate detected |
| NOISE-2430-B | Invalid Entry 189 | Superseded by newer mapping |
| NOISE-7373-E | Invalid Entry 425 | Out of scope per business decision |
| NOISE-4383-B | Invalid Entry 118 | Duplicate detected |
| NOISE-9920-F | Invalid Entry 125 | Superseded by newer mapping |
| NOISE-6160-G | Invalid Entry 864 | Data quality insufficient |
| NOISE-6012-H | Invalid Entry 270 | Pending validation |
| NOISE-9728-E | Invalid Entry 844 | Pending validation |
| NOISE-8273-A | Invalid Entry 802 | Superseded by newer mapping |
| NOISE-9758-G | Invalid Entry 134 | Duplicate detected |
| NOISE-9656-A | Invalid Entry 648 | Superseded by newer mapping |
| NOISE-1232-G | Invalid Entry 310 | Duplicate detected |
| NOISE-9443-E | Invalid Entry 381 | Pending validation |
| NOISE-5734-F | Invalid Entry 996 | Data quality insufficient |
| NOISE-8395-H | Invalid Entry 544 | Out of scope per business decision |
| NOISE-1587-A | Invalid Entry 169 | Duplicate detected |
| NOISE-7551-F | Invalid Entry 718 | Out of scope per business decision |
| NOISE-9257-D | Invalid Entry 324 | Duplicate detected |
| NOISE-2292-H | Invalid Entry 118 | Data quality insufficient |
| NOISE-4388-C | Invalid Entry 843 | Data quality insufficient |
| NOISE-5394-F | Invalid Entry 886 | Out of scope per business decision |
| NOISE-3956-F | Invalid Entry 959 | Out of scope per business decision |
| NOISE-1748-C | Invalid Entry 521 | Duplicate detected |
| NOISE-7398-A | Invalid Entry 100 | Duplicate detected |
| NOISE-4835-A | Invalid Entry 233 | Superseded by newer mapping |
| NOISE-4537-D | Invalid Entry 859 | Data quality insufficient |
| NOISE-1729-D | Invalid Entry 459 | Data quality insufficient |
| NOISE-3509-C | Invalid Entry 985 | Pending validation |
| NOISE-9225-D | Invalid Entry 537 | Pending validation |
| NOISE-9667-A | Invalid Entry 202 | Out of scope per business decision |
| NOISE-8827-H | Invalid Entry 661 | Out of scope per business decision |
| NOISE-5267-G | Invalid Entry 969 | Pending validation |
| NOISE-7511-F | Invalid Entry 525 | Superseded by newer mapping |
| NOISE-9463-D | Invalid Entry 204 | Out of scope per business decision |
| NOISE-7670-C | Invalid Entry 747 | Superseded by newer mapping |
| NOISE-7342-A | Invalid Entry 844 | Duplicate detected |
| NOISE-8726-C | Invalid Entry 767 | Pending validation |
| NOISE-3722-D | Invalid Entry 683 | Duplicate detected |
| NOISE-1315-D | Invalid Entry 529 | Data quality insufficient |
| NOISE-9484-H | Invalid Entry 817 | Data quality insufficient |
| NOISE-8498-B | Invalid Entry 893 | Duplicate detected |
| NOISE-1588-H | Invalid Entry 141 | Data quality insufficient |
| NOISE-9684-C | Invalid Entry 377 | Superseded by newer mapping |
| NOISE-3213-F | Invalid Entry 275 | Pending validation |
| NOISE-5852-G | Invalid Entry 457 | Superseded by newer mapping |
| NOISE-4354-F | Invalid Entry 768 | Duplicate detected |
| NOISE-9355-G | Invalid Entry 105 | Superseded by newer mapping |
| NOISE-2156-F | Invalid Entry 110 | Data quality insufficient |
| NOISE-4819-C | Invalid Entry 880 | Superseded by newer mapping |
| NOISE-7801-B | Invalid Entry 440 | Pending validation |
| NOISE-7333-C | Invalid Entry 338 | Duplicate detected |
| NOISE-7216-F | Invalid Entry 266 | Duplicate detected |
| NOISE-6497-F | Invalid Entry 633 | Out of scope per business decision |
| NOISE-3904-H | Invalid Entry 427 | Out of scope per business decision |
| NOISE-3574-B | Invalid Entry 500 | Data quality insufficient |
| NOISE-9663-D | Invalid Entry 925 | Out of scope per business decision |
| NOISE-3066-E | Invalid Entry 702 | Out of scope per business decision |
| NOISE-2244-D | Invalid Entry 461 | Out of scope per business decision |
| NOISE-4784-F | Invalid Entry 378 | Superseded by newer mapping |
| NOISE-1670-C | Invalid Entry 512 | Data quality insufficient |
| NOISE-9306-E | Invalid Entry 654 | Duplicate detected |
| NOISE-4952-B | Invalid Entry 374 | Out of scope per business decision |
| NOISE-8758-H | Invalid Entry 671 | Data quality insufficient |
| NOISE-5416-F | Invalid Entry 157 | Data quality insufficient |
| NOISE-2286-H | Invalid Entry 650 | Data quality insufficient |
| NOISE-2114-G | Invalid Entry 942 | Data quality insufficient |
| NOISE-9162-C | Invalid Entry 202 | Data quality insufficient |
| NOISE-6748-G | Invalid Entry 647 | Duplicate detected |
| NOISE-7516-A | Invalid Entry 991 | Superseded by newer mapping |
| NOISE-8463-A | Invalid Entry 829 | Superseded by newer mapping |
| NOISE-8251-A | Invalid Entry 306 | Superseded by newer mapping |
| NOISE-9785-F | Invalid Entry 147 | Superseded by newer mapping |
| NOISE-4875-C | Invalid Entry 856 | Superseded by newer mapping |
| NOISE-5921-C | Invalid Entry 448 | Pending validation |
| NOISE-5680-E | Invalid Entry 779 | Duplicate detected |
| NOISE-1021-C | Invalid Entry 556 | Superseded by newer mapping |
| NOISE-6350-C | Invalid Entry 608 | Out of scope per business decision |
| NOISE-7656-B | Invalid Entry 247 | Superseded by newer mapping |
| NOISE-9580-G | Invalid Entry 515 | Out of scope per business decision |
| NOISE-4122-B | Invalid Entry 266 | Out of scope per business decision |
| NOISE-8899-F | Invalid Entry 434 | Data quality insufficient |
| NOISE-8039-E | Invalid Entry 896 | Superseded by newer mapping |
| NOISE-3344-F | Invalid Entry 232 | Duplicate detected |
| NOISE-5476-E | Invalid Entry 830 | Data quality insufficient |
| NOISE-5985-B | Invalid Entry 855 | Data quality insufficient |
| NOISE-8363-G | Invalid Entry 185 | Pending validation |
| NOISE-1212-B | Invalid Entry 297 | Out of scope per business decision |
| NOISE-1973-B | Invalid Entry 258 | Data quality insufficient |
| NOISE-6610-A | Invalid Entry 963 | Out of scope per business decision |
| NOISE-8883-E | Invalid Entry 587 | Duplicate detected |
| NOISE-6931-E | Invalid Entry 810 | Duplicate detected |
| NOISE-5943-A | Invalid Entry 429 | Out of scope per business decision |
| NOISE-6875-F | Invalid Entry 190 | Data quality insufficient |
| NOISE-3428-C | Invalid Entry 278 | Duplicate detected |
| NOISE-1893-E | Invalid Entry 590 | Pending validation |
| NOISE-9761-D | Invalid Entry 666 | Superseded by newer mapping |
| NOISE-1895-E | Invalid Entry 614 | Out of scope per business decision |
| NOISE-8892-D | Invalid Entry 744 | Out of scope per business decision |
| NOISE-1546-G | Invalid Entry 537 | Out of scope per business decision |
| NOISE-7525-F | Invalid Entry 653 | Out of scope per business decision |
| NOISE-6024-F | Invalid Entry 547 | Duplicate detected |
| NOISE-5415-C | Invalid Entry 272 | Superseded by newer mapping |
| NOISE-1296-E | Invalid Entry 949 | Superseded by newer mapping |
| NOISE-9715-B | Invalid Entry 754 | Pending validation |
| NOISE-6367-E | Invalid Entry 701 | Out of scope per business decision |
| NOISE-2992-E | Invalid Entry 570 | Out of scope per business decision |
| NOISE-8004-G | Invalid Entry 131 | Pending validation |
| NOISE-6982-C | Invalid Entry 353 | Duplicate detected |
| NOISE-8399-E | Invalid Entry 965 | Out of scope per business decision |
| NOISE-5120-H | Invalid Entry 627 | Data quality insufficient |
| NOISE-8185-F | Invalid Entry 512 | Duplicate detected |
| NOISE-3784-A | Invalid Entry 954 | Pending validation |
| NOISE-6450-G | Invalid Entry 156 | Data quality insufficient |
| NOISE-2951-B | Invalid Entry 288 | Pending validation |
| NOISE-9572-E | Invalid Entry 808 | Out of scope per business decision |
| NOISE-6644-B | Invalid Entry 632 | Duplicate detected |
| NOISE-8626-F | Invalid Entry 235 | Superseded by newer mapping |
| NOISE-7339-F | Invalid Entry 705 | Out of scope per business decision |
| NOISE-5705-D | Invalid Entry 971 | Out of scope per business decision |
| NOISE-4719-F | Invalid Entry 489 | Duplicate detected |
| NOISE-2538-H | Invalid Entry 236 | Duplicate detected |
| NOISE-3606-B | Invalid Entry 277 | Duplicate detected |
| NOISE-6743-F | Invalid Entry 226 | Duplicate detected |
| NOISE-3029-C | Invalid Entry 363 | Pending validation |
| NOISE-9816-H | Invalid Entry 627 | Out of scope per business decision |
| NOISE-6330-G | Invalid Entry 371 | Pending validation |
| NOISE-6041-G | Invalid Entry 931 | Duplicate detected |
| NOISE-2307-D | Invalid Entry 418 | Duplicate detected |
| NOISE-7153-E | Invalid Entry 183 | Out of scope per business decision |
| NOISE-2805-E | Invalid Entry 292 | Superseded by newer mapping |
| NOISE-9380-F | Invalid Entry 648 | Superseded by newer mapping |
| NOISE-9899-H | Invalid Entry 215 | Data quality insufficient |
| NOISE-6945-H | Invalid Entry 606 | Duplicate detected |
| NOISE-4286-B | Invalid Entry 616 | Duplicate detected |
| NOISE-5713-D | Invalid Entry 901 | Pending validation |
| NOISE-7367-G | Invalid Entry 668 | Duplicate detected |
| NOISE-9452-F | Invalid Entry 372 | Pending validation |
| NOISE-3087-C | Invalid Entry 570 | Duplicate detected |
| NOISE-8628-F | Invalid Entry 445 | Data quality insufficient |
| NOISE-3226-A | Invalid Entry 103 | Superseded by newer mapping |
| NOISE-6079-B | Invalid Entry 268 | Duplicate detected |
| NOISE-5581-D | Invalid Entry 807 | Superseded by newer mapping |
| NOISE-3088-B | Invalid Entry 768 | Data quality insufficient |
| NOISE-4853-C | Invalid Entry 361 | Pending validation |
| NOISE-3149-F | Invalid Entry 584 | Duplicate detected |
| NOISE-4996-F | Invalid Entry 679 | Out of scope per business decision |
| NOISE-7759-F | Invalid Entry 904 | Duplicate detected |
| NOISE-3713-D | Invalid Entry 812 | Pending validation |
| NOISE-4362-H | Invalid Entry 573 | Out of scope per business decision |
| NOISE-6187-G | Invalid Entry 105 | Data quality insufficient |
| NOISE-6615-F | Invalid Entry 498 | Duplicate detected |
| NOISE-8795-D | Invalid Entry 987 | Data quality insufficient |
| NOISE-8365-A | Invalid Entry 569 | Duplicate detected |
| NOISE-3907-A | Invalid Entry 830 | Out of scope per business decision |
| NOISE-7301-A | Invalid Entry 346 | Data quality insufficient |
| NOISE-6633-C | Invalid Entry 608 | Superseded by newer mapping |
| NOISE-2036-F | Invalid Entry 722 | Data quality insufficient |
| NOISE-6012-C | Invalid Entry 657 | Out of scope per business decision |
| NOISE-2722-F | Invalid Entry 993 | Out of scope per business decision |
| NOISE-5185-D | Invalid Entry 959 | Pending validation |
| NOISE-4427-B | Invalid Entry 358 | Pending validation |
| NOISE-6661-B | Invalid Entry 325 | Pending validation |
| NOISE-8469-F | Invalid Entry 364 | Data quality insufficient |
| NOISE-1247-D | Invalid Entry 674 | Superseded by newer mapping |
| NOISE-2652-A | Invalid Entry 472 | Out of scope per business decision |
| NOISE-5902-D | Invalid Entry 241 | Duplicate detected |
| NOISE-9302-H | Invalid Entry 216 | Out of scope per business decision |
| NOISE-9919-G | Invalid Entry 204 | Duplicate detected |
| NOISE-6207-C | Invalid Entry 430 | Out of scope per business decision |
| NOISE-4132-E | Invalid Entry 835 | Superseded by newer mapping |
| NOISE-5066-D | Invalid Entry 728 | Data quality insufficient |
| NOISE-4371-B | Invalid Entry 684 | Out of scope per business decision |
| NOISE-4689-C | Invalid Entry 849 | Pending validation |
| NOISE-9445-F | Invalid Entry 557 | Pending validation |
| NOISE-6307-E | Invalid Entry 523 | Superseded by newer mapping |
| NOISE-7203-E | Invalid Entry 828 | Superseded by newer mapping |
| NOISE-9602-C | Invalid Entry 289 | Superseded by newer mapping |
| NOISE-6911-A | Invalid Entry 824 | Duplicate detected |
| NOISE-8833-C | Invalid Entry 813 | Duplicate detected |
| NOISE-1166-B | Invalid Entry 594 | Duplicate detected |
| NOISE-2192-G | Invalid Entry 522 | Superseded by newer mapping |
| NOISE-7785-D | Invalid Entry 641 | Data quality insufficient |
| NOISE-5160-A | Invalid Entry 156 | Out of scope per business decision |
| NOISE-7961-C | Invalid Entry 853 | Duplicate detected |
| NOISE-7403-G | Invalid Entry 550 | Duplicate detected |
| NOISE-7607-F | Invalid Entry 655 | Out of scope per business decision |
| NOISE-7040-F | Invalid Entry 654 | Superseded by newer mapping |
| NOISE-9011-D | Invalid Entry 573 | Pending validation |
| NOISE-8767-A | Invalid Entry 418 | Duplicate detected |
| NOISE-5051-F | Invalid Entry 412 | Data quality insufficient |
| NOISE-7549-E | Invalid Entry 578 | Superseded by newer mapping |
| NOISE-5642-C | Invalid Entry 680 | Data quality insufficient |
| NOISE-7870-B | Invalid Entry 684 | Out of scope per business decision |
| NOISE-4688-G | Invalid Entry 304 | Data quality insufficient |
| NOISE-7574-A | Invalid Entry 680 | Data quality insufficient |
| NOISE-1937-E | Invalid Entry 696 | Superseded by newer mapping |
| NOISE-5927-D | Invalid Entry 780 | Pending validation |
| NOISE-8461-D | Invalid Entry 310 | Out of scope per business decision |
| NOISE-6917-D | Invalid Entry 540 | Out of scope per business decision |
| NOISE-9318-H | Invalid Entry 993 | Out of scope per business decision |
| NOISE-6998-C | Invalid Entry 120 | Duplicate detected |
| NOISE-9406-A | Invalid Entry 389 | Pending validation |
| NOISE-3992-B | Invalid Entry 242 | Data quality insufficient |
| NOISE-7725-E | Invalid Entry 516 | Out of scope per business decision |
| NOISE-7971-F | Invalid Entry 649 | Pending validation |
| NOISE-8940-D | Invalid Entry 245 | Duplicate detected |
| NOISE-7976-A | Invalid Entry 369 | Out of scope per business decision |
| NOISE-1707-F | Invalid Entry 391 | Out of scope per business decision |
| NOISE-8335-E | Invalid Entry 545 | Superseded by newer mapping |
| NOISE-3987-H | Invalid Entry 487 | Pending validation |
| NOISE-3470-B | Invalid Entry 937 | Data quality insufficient |
| NOISE-3136-B | Invalid Entry 362 | Pending validation |
| NOISE-6115-A | Invalid Entry 663 | Out of scope per business decision |

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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230718_000000`
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
| Technical Lead | Maria Garcia (Supply Chain) | maria@company.com | +1-555-0102 |
| Business Owner | Lisa Rodriguez (Quality Assurance) | lisa@company.com | +1-555-0103 |
| Data Steward | James Wilson (Finance) | james@company.com | +1-555-0104 |

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
