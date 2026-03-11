# Migration Runbook: ERP Gamma Acquisition Integration

**Document ID**: RB-GAMMA_INTEGRATION_2022-8425
**Version**: 2.4
**Last Updated**: 2023-04-24
**Classification**: Internal Use Only

---


## Executive Summary

This runbook provides the complete operational procedures for the ERP Gamma Acquisition Integration project.
The migration involves transitioning master data and transactional records from ERP_GAMMA
to ERP_ALPHA while maintaining data integrity and business continuity.

**Project Timeline**: 2023-01-10 to 2023-05-16
**Business Sponsor**: Corporate Development
**Technical Owner**: M&A Integration Team

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
|   ERP_GAMMA       |     |   ETL Layer      |     |   ERP_ALPHA       |
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
ERP_GAMMA to ERP_ALPHA. All mappings have been validated by the
data stewardship team unless otherwise noted.

### 4.2 Migration Statistics

| Category | Count | Status |
|----------|-------|--------|
| Total entities assessed | 1440 | Completed |
| Successfully mapped | 972 | Verified |
| Excluded from scope | 291 | Documented |
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

| Source Code (ERP_GAMMA) | Target Code (ERP_ALPHA) | Verification | Notes |
|------------------------------|------------------------------|--------------|-------|
| SO-CH-70-GR-B-821 | Sodium Chloride 70% Grade B | domain_expert | Cross-referenced with transactions |
| FR-GR-A-600 | Fructose Grade A | data_steward | Historical match confirmed |
| RE-ST-223 | Resistant Starch | data_steward | Cross-referenced with transactions |
| AS-AC-782 | Ascorbic Acid | domain_expert | Auto-mapped, validated |
| SU-OI-98-PR-692 | Sunflower Oil 98% Premium | system_admin | Cross-referenced with transactions |
| CY-763 | Cyclodextrin | data_steward | Cross-referenced with transactions |
| PE-PR-99.5-863 | Pea Protein 99.5% | system_admin | Historical match confirmed |
| AS-AC-GR-B-395 | Ascorbic Acid Grade B | data_steward | Historical match confirmed |
| LA-AC-690 | Lactic Acid | domain_expert | Confirmed by domain expert |
| AS-AC-PH-GR-192 | Ascorbic Acid Pharma Grade | system_admin | Verified via product specs |
| CO-OI-FO-GR-162 | Coconut Oil Food Grade | data_steward | Verified via product specs |
| RA-OI-258 | Rapeseed Oil | system_admin | Verified via product specs |
| SO-BE-25-ST-520 | Sodium Benzoate 25% Standard | system_admin | Historical match confirmed |
| CO-OI-966 | Coconut Oil | data_steward | Confirmed by domain expert |
| CO-OI-98-890 | Coconut Oil 98% | domain_expert | Verified via product specs |
| SO-BE-99.5-GR-A-143 | Sodium Benzoate 99.5% Grade A | domain_expert | Confirmed by domain expert |
| SO-BE-99.5-ST-342 | Sodium Benzoate 99.5% Standard | system_admin | Cross-referenced with transactions |
| CY-98-PH-GR-614 | Cyclodextrin 98% Pharma Grade | domain_expert | Historical match confirmed |
| CO-OI-GR-A-370 | Coconut Oil Grade A | domain_expert | Confirmed by domain expert |
| SO-AC-PH-GR-274 | Sorbic Acid Pharma Grade | system_admin | Historical match confirmed |
| DE-ST-385 | Dextrose Standard | domain_expert | Cross-referenced with transactions |
| LA-AC-99.5-GR-B-756 | Lactic Acid 99.5% Grade B | domain_expert | Cross-referenced with transactions |
| LA-AC-393 | Lactic Acid | domain_expert | Auto-mapped, validated |
| PO-SO-560 | Potassium Sorbate | domain_expert | Cross-referenced with transactions |
| SO-BE-99.5-195 | Sodium Benzoate 99.5% | domain_expert | Confirmed by domain expert |
| SO-BE-PH-GR-647 | Sodium Benzoate Pharma Grade | system_admin | Historical match confirmed |
| PA-OI-50-PR-573 | Palm Oil 50% Premium | system_admin | Verified via product specs |
| IS-878 | Isoglucose | data_steward | Verified via product specs |
| SO-IS-25-TE-320 | Soy Isolate 25% Technical | system_admin | Cross-referenced with transactions |
| FR-108 | Fructose | system_admin | Verified via product specs |
| RA-OI-745 | Rapeseed Oil | domain_expert | Confirmed by domain expert |
| RE-ST-463 | Resistant Starch | system_admin | Verified via product specs |
| FR-278 | Fructose | data_steward | Confirmed by domain expert |
| GL-SY-371 | Glucose Syrup | data_steward | Auto-mapped, validated |
| SO-AC-25-GR-B-198 | Sorbic Acid 25% Grade B | system_admin | Auto-mapped, validated |
| CA-ST-375 | Casein Standard | system_admin | Verified via product specs |
| CA-CA-98-785 | Calcium Carbonate 98% | system_admin | Cross-referenced with transactions |
| PA-OI-ST-879 | Palm Oil Standard | domain_expert | Cross-referenced with transactions |
| MA-DE-GR-A-871 | Maltodextrin DE5 Grade A | domain_expert | Verified via product specs |
| SO-AC-FO-GR-175 | Sorbic Acid Food Grade | data_steward | Cross-referenced with transactions |
| LA-AC-98-226 | Lactic Acid 98% | system_admin | Verified via product specs |
| AS-AC-279 | Ascorbic Acid | system_admin | Verified via product specs |
| CO-OI-25-ST-613 | Coconut Oil 25% Standard | system_admin | Cross-referenced with transactions |
| CI-AC-634 | Citric Acid | domain_expert | Historical match confirmed |
| CI-AC-PH-GR-209 | Citric Acid Pharma Grade | system_admin | Auto-mapped, validated |
| LA-AC-GR-A-486 | Lactic Acid Grade A | data_steward | Auto-mapped, validated |
| PA-OI-98-587 | Palm Oil 98% | domain_expert | Cross-referenced with transactions |
| SU-OI-50-GR-A-521 | Sunflower Oil 50% Grade A | data_steward | Historical match confirmed |
| SO-AC-98-741 | Sorbic Acid 98% | data_steward | Confirmed by domain expert |
| RE-ST-98-PH-GR-372 | Resistant Starch 98% Pharma Grade | domain_expert | Confirmed by domain expert |
| DE-635 | Dextrin | domain_expert | Verified via product specs |
| MA-DE-641 | Maltodextrin DE20 | domain_expert | Auto-mapped, validated |
| DE-25-TE-737 | Dextrose 25% Technical | data_steward | Verified via product specs |
| LA-AC-FO-GR-553 | Lactic Acid Food Grade | data_steward | Cross-referenced with transactions |
| SO-AC-852 | Sorbic Acid | system_admin | Auto-mapped, validated |
| DE-PH-GR-282 | Dextrin Pharma Grade | domain_expert | Auto-mapped, validated |
| CI-AC-99.5-638 | Citric Acid 99.5% | domain_expert | Confirmed by domain expert |
| SO-BE-PR-691 | Sodium Benzoate Premium | domain_expert | Cross-referenced with transactions |
| DE-515 | Dextrose | data_steward | Verified via product specs |
| CO-OI-ST-153 | Coconut Oil Standard | system_admin | Cross-referenced with transactions |
| CI-AC-99.5-440 | Citric Acid 99.5% | domain_expert | Verified via product specs |
| RE-ST-GR-B-598 | Resistant Starch Grade B | data_steward | Auto-mapped, validated |
| CA-CA-50-GR-B-200 | Calcium Carbonate 50% Grade B | system_admin | Historical match confirmed |
| SO-IS-25-323 | Soy Isolate 25% | data_steward | Auto-mapped, validated |
| RA-OI-99.5-602 | Rapeseed Oil 99.5% | system_admin | Historical match confirmed |
| GL-SY-98-FO-GR-198 | Glucose Syrup 98% Food Grade | domain_expert | Verified via product specs |
| SO-IS-25-PH-GR-832 | Soy Isolate 25% Pharma Grade | system_admin | Historical match confirmed |
| DE-GR-A-250 | Dextrose Grade A | system_admin | Historical match confirmed |
| SO-CH-GR-A-776 | Sodium Chloride Grade A | data_steward | Cross-referenced with transactions |
| CO-OI-98-GR-A-763 | Coconut Oil 98% Grade A | data_steward | Verified via product specs |
| RE-ST-TE-614 | Resistant Starch Technical | system_admin | Auto-mapped, validated |
| DE-50-891 | Dextrin 50% | domain_expert | Confirmed by domain expert |
| SO-CH-98-GR-B-961 | Sodium Chloride 98% Grade B | data_steward | Verified via product specs |
| GL-SY-TE-803 | Glucose Syrup Technical | system_admin | Confirmed by domain expert |
| SO-IS-99.5-PR-187 | Soy Isolate 99.5% Premium | domain_expert | Cross-referenced with transactions |
| PE-PR-GR-B-793 | Pea Protein Grade B | domain_expert | Auto-mapped, validated |
| SO-IS-98-430 | Soy Isolate 98% | data_steward | Verified via product specs |
| DE-840 | Dextrin | data_steward | Cross-referenced with transactions |
| WH-GL-GR-B-926 | Wheat Gluten Grade B | system_admin | Historical match confirmed |
| GL-SY-70-549 | Glucose Syrup 70% | system_admin | Historical match confirmed |
| SU-OI-ST-338 | Sunflower Oil Standard | data_steward | Cross-referenced with transactions |
| SO-IS-25-ST-345 | Soy Isolate 25% Standard | domain_expert | Verified via product specs |
| AS-AC-99.5-PR-761 | Ascorbic Acid 99.5% Premium | data_steward | Confirmed by domain expert |
| SO-IS-GR-A-940 | Soy Isolate Grade A | domain_expert | Verified via product specs |
| DE-TE-380 | Dextrin Technical | domain_expert | Verified via product specs |
| PA-OI-632 | Palm Oil | domain_expert | Verified via product specs |
| PO-SO-763 | Potassium Sorbate | domain_expert | Confirmed by domain expert |
| FR-99.5-PH-GR-378 | Fructose 99.5% Pharma Grade | domain_expert | Verified via product specs |
| SO-BE-700 | Sodium Benzoate | data_steward | Auto-mapped, validated |
| PA-OI-70-GR-B-781 | Palm Oil 70% Grade B | domain_expert | Verified via product specs |
| SO-BE-25-774 | Sodium Benzoate 25% | domain_expert | Cross-referenced with transactions |
| SO-CH-70-365 | Sodium Chloride 70% | system_admin | Historical match confirmed |
| CA-PR-568 | Casein Premium | system_admin | Auto-mapped, validated |
| SO-CH-99.5-618 | Sodium Chloride 99.5% | system_admin | Historical match confirmed |
| AS-AC-TE-342 | Ascorbic Acid Technical | domain_expert | Auto-mapped, validated |
| FR-25-GR-B-641 | Fructose 25% Grade B | system_admin | Historical match confirmed |
| SO-CH-758 | Sodium Chloride | system_admin | Verified via product specs |
| DE-ST-213 | Dextrin Standard | data_steward | Verified via product specs |
| CO-OI-358 | Coconut Oil | system_admin | Verified via product specs |
| CO-OI-99.5-PH-GR-944 | Coconut Oil 99.5% Pharma Grade | domain_expert | Confirmed by domain expert |
| IS-70-838 | Isoglucose 70% | system_admin | Historical match confirmed |
| DE-FO-GR-588 | Dextrose Food Grade | system_admin | Confirmed by domain expert |
| PA-OI-50-273 | Palm Oil 50% | system_admin | Cross-referenced with transactions |
| AS-AC-98-PR-217 | Ascorbic Acid 98% Premium | domain_expert | Historical match confirmed |
| SO-AC-70-785 | Sorbic Acid 70% | system_admin | Auto-mapped, validated |
| SO-CH-ST-522 | Sodium Chloride Standard | system_admin | Cross-referenced with transactions |
| IS-PR-125 | Isoglucose Premium | domain_expert | Cross-referenced with transactions |
| CI-AC-25-GR-A-669 | Citric Acid 25% Grade A | data_steward | Historical match confirmed |
| SO-CH-25-PR-784 | Sodium Chloride 25% Premium | data_steward | Auto-mapped, validated |
| CA-CA-GR-B-761 | Calcium Carbonate Grade B | domain_expert | Historical match confirmed |
| SO-IS-275 | Soy Isolate | system_admin | Auto-mapped, validated |
| DE-602 | Dextrose | domain_expert | Verified via product specs |
| WH-GL-830 | Wheat Gluten | data_steward | Confirmed by domain expert |
| FR-FO-GR-823 | Fructose Food Grade | domain_expert | Cross-referenced with transactions |
| AS-AC-70-133 | Ascorbic Acid 70% | system_admin | Confirmed by domain expert |
| SO-IS-50-GR-B-983 | Soy Isolate 50% Grade B | data_steward | Confirmed by domain expert |
| CY-926 | Cyclodextrin | domain_expert | Verified via product specs |
| AS-AC-165 | Ascorbic Acid | domain_expert | Confirmed by domain expert |
| DE-25-TE-949 | Dextrose 25% Technical | system_admin | Auto-mapped, validated |
| IS-FO-GR-555 | Isoglucose Food Grade | domain_expert | Confirmed by domain expert |
| DE-70-856 | Dextrin 70% | domain_expert | Auto-mapped, validated |
| PE-PR-50-128 | Pea Protein 50% | system_admin | Confirmed by domain expert |
| SO-CH-PR-862 | Sodium Chloride Premium | domain_expert | Confirmed by domain expert |
| CI-AC-215 | Citric Acid | data_steward | Historical match confirmed |
| GL-SY-TE-601 | Glucose Syrup Technical | data_steward | Historical match confirmed |
| RA-OI-TE-584 | Rapeseed Oil Technical | system_admin | Confirmed by domain expert |
| GL-SY-98-ST-578 | Glucose Syrup 98% Standard | domain_expert | Verified via product specs |
| IS-50-TE-886 | Isoglucose 50% Technical | domain_expert | Historical match confirmed |
| SO-BE-99.5-TE-213 | Sodium Benzoate 99.5% Technical | system_admin | Cross-referenced with transactions |
| SO-BE-GR-B-914 | Sodium Benzoate Grade B | data_steward | Verified via product specs |
| DE-TE-414 | Dextrin Technical | domain_expert | Verified via product specs |
| AS-AC-ST-243 | Ascorbic Acid Standard | data_steward | Verified via product specs |
| CI-AC-FO-GR-293 | Citric Acid Food Grade | domain_expert | Verified via product specs |
| WH-GL-GR-B-129 | Wheat Gluten Grade B | system_admin | Cross-referenced with transactions |
| CA-TE-562 | Casein Technical | data_steward | Cross-referenced with transactions |
| GL-SY-98-939 | Glucose Syrup 98% | system_admin | Cross-referenced with transactions |
| RA-OI-70-PR-405 | Rapeseed Oil 70% Premium | domain_expert | Cross-referenced with transactions |
| CI-AC-99.5-469 | Citric Acid 99.5% | domain_expert | Cross-referenced with transactions |
| PA-OI-383 | Palm Oil | system_admin | Verified via product specs |
| RA-OI-431 | Rapeseed Oil | system_admin | Cross-referenced with transactions |
| PA-OI-98-856 | Palm Oil 98% | data_steward | Auto-mapped, validated |
| FR-GR-B-231 | Fructose Grade B | data_steward | Auto-mapped, validated |
| AS-AC-70-347 | Ascorbic Acid 70% | data_steward | Confirmed by domain expert |
| CI-AC-857 | Citric Acid | domain_expert | Confirmed by domain expert |
| LA-AC-70-PH-GR-221 | Lactic Acid 70% Pharma Grade | domain_expert | Historical match confirmed |
| PO-SO-GR-A-715 | Potassium Sorbate Grade A | system_admin | Historical match confirmed |
| SO-CH-881 | Sodium Chloride | data_steward | Confirmed by domain expert |
| FR-113 | Fructose | data_steward | Confirmed by domain expert |
| SO-BE-GR-A-760 | Sodium Benzoate Grade A | system_admin | Verified via product specs |
| FR-GR-B-311 | Fructose Grade B | domain_expert | Verified via product specs |
| AS-AC-130 | Ascorbic Acid | system_admin | Confirmed by domain expert |
| PE-PR-PR-428 | Pea Protein Premium | data_steward | Verified via product specs |
| FR-124 | Fructose | domain_expert | Cross-referenced with transactions |
| RA-OI-98-679 | Rapeseed Oil 98% | domain_expert | Cross-referenced with transactions |
| PO-SO-50-GR-B-154 | Potassium Sorbate 50% Grade B | system_admin | Historical match confirmed |
| MA-DE-944 | Maltodextrin DE10 | system_admin | Confirmed by domain expert |
| PA-OI-70-780 | Palm Oil 70% | system_admin | Historical match confirmed |
| PE-PR-98-GR-B-195 | Pea Protein 98% Grade B | system_admin | Historical match confirmed |
| SO-IS-FO-GR-334 | Soy Isolate Food Grade | data_steward | Verified via product specs |
| GL-SY-70-655 | Glucose Syrup 70% | system_admin | Verified via product specs |
| DE-GR-A-351 | Dextrose Grade A | system_admin | Confirmed by domain expert |
| LA-AC-554 | Lactic Acid | domain_expert | Historical match confirmed |
| CA-CA-50-GR-A-195 | Calcium Carbonate 50% Grade A | domain_expert | Verified via product specs |
| PO-SO-339 | Potassium Sorbate | data_steward | Auto-mapped, validated |
| LA-AC-TE-651 | Lactic Acid Technical | data_steward | Auto-mapped, validated |
| DE-25-260 | Dextrose 25% | domain_expert | Auto-mapped, validated |
| DE-GR-B-942 | Dextrose Grade B | system_admin | Cross-referenced with transactions |
| RE-ST-GR-B-677 | Resistant Starch Grade B | domain_expert | Confirmed by domain expert |
| LA-AC-GR-A-949 | Lactic Acid Grade A | domain_expert | Cross-referenced with transactions |
| DE-GR-A-512 | Dextrin Grade A | data_steward | Cross-referenced with transactions |
| AS-AC-99.5-619 | Ascorbic Acid 99.5% | system_admin | Confirmed by domain expert |
| SO-CH-98-657 | Sodium Chloride 98% | system_admin | Confirmed by domain expert |
| SO-CH-752 | Sodium Chloride | domain_expert | Confirmed by domain expert |
| PE-PR-25-PH-GR-591 | Pea Protein 25% Pharma Grade | data_steward | Confirmed by domain expert |
| PE-PR-TE-718 | Pea Protein Technical | data_steward | Verified via product specs |
| MA-DE-PR-303 | Maltodextrin DE10 Premium | data_steward | Verified via product specs |
| GL-SY-533 | Glucose Syrup | system_admin | Auto-mapped, validated |
| SO-IS-354 | Soy Isolate | data_steward | Historical match confirmed |
| RE-ST-676 | Resistant Starch | data_steward | Auto-mapped, validated |
| PO-SO-ST-111 | Potassium Sorbate Standard | data_steward | Verified via product specs |
| LA-AC-FO-GR-469 | Lactic Acid Food Grade | data_steward | Historical match confirmed |
| CI-AC-25-TE-484 | Citric Acid 25% Technical | domain_expert | Auto-mapped, validated |
| DE-50-727 | Dextrin 50% | system_admin | Confirmed by domain expert |
| IS-230 | Isoglucose | system_admin | Auto-mapped, validated |
| SO-IS-50-GR-B-346 | Soy Isolate 50% Grade B | domain_expert | Confirmed by domain expert |
| PE-PR-929 | Pea Protein | system_admin | Verified via product specs |
| WH-GL-GR-A-583 | Wheat Gluten Grade A | domain_expert | Confirmed by domain expert |
| PA-OI-25-GR-A-241 | Palm Oil 25% Grade A | domain_expert | Historical match confirmed |
| RA-OI-GR-A-272 | Rapeseed Oil Grade A | system_admin | Confirmed by domain expert |
| DE-70-GR-A-741 | Dextrose 70% Grade A | data_steward | Auto-mapped, validated |
| SO-BE-25-GR-B-233 | Sodium Benzoate 25% Grade B | data_steward | Cross-referenced with transactions |
| SO-BE-50-924 | Sodium Benzoate 50% | data_steward | Historical match confirmed |
| CO-OI-977 | Coconut Oil | domain_expert | Auto-mapped, validated |
| FR-194 | Fructose | data_steward | Historical match confirmed |
| CI-AC-538 | Citric Acid | domain_expert | Historical match confirmed |
| SO-CH-TE-286 | Sodium Chloride Technical | data_steward | Auto-mapped, validated |
| PO-SO-202 | Potassium Sorbate | data_steward | Cross-referenced with transactions |
| CI-AC-70-265 | Citric Acid 70% | domain_expert | Historical match confirmed |
| MA-DE-569 | Maltodextrin DE25 | data_steward | Cross-referenced with transactions |
| SO-AC-FO-GR-286 | Sorbic Acid Food Grade | system_admin | Cross-referenced with transactions |
| GL-SY-98-749 | Glucose Syrup 98% | data_steward | Historical match confirmed |
| MA-DE-951 | Maltodextrin DE10 | system_admin | Historical match confirmed |
| SO-CH-201 | Sodium Chloride | system_admin | Cross-referenced with transactions |
| LA-AC-FO-GR-687 | Lactic Acid Food Grade | domain_expert | Cross-referenced with transactions |
| SO-CH-70-317 | Sodium Chloride 70% | system_admin | Verified via product specs |
| FR-TE-414 | Fructose Technical | data_steward | Confirmed by domain expert |
| LA-AC-893 | Lactic Acid | domain_expert | Cross-referenced with transactions |
| SO-BE-PH-GR-831 | Sodium Benzoate Pharma Grade | system_admin | Confirmed by domain expert |
| CO-OI-98-FO-GR-748 | Coconut Oil 98% Food Grade | data_steward | Cross-referenced with transactions |
| SO-BE-GR-B-936 | Sodium Benzoate Grade B | domain_expert | Verified via product specs |
| PO-SO-TE-239 | Potassium Sorbate Technical | data_steward | Verified via product specs |
| RA-OI-GR-B-834 | Rapeseed Oil Grade B | data_steward | Verified via product specs |
| CO-OI-70-701 | Coconut Oil 70% | domain_expert | Confirmed by domain expert |
| CA-CA-25-PH-GR-684 | Calcium Carbonate 25% Pharma Grade | data_steward | Confirmed by domain expert |
| MA-DE-GR-B-565 | Maltodextrin DE5 Grade B | data_steward | Confirmed by domain expert |
| SO-IS-98-PR-717 | Soy Isolate 98% Premium | domain_expert | Cross-referenced with transactions |
| SO-BE-99.5-TE-953 | Sodium Benzoate 99.5% Technical | system_admin | Cross-referenced with transactions |
| MA-DE-437 | Maltodextrin DE25 | domain_expert | Verified via product specs |
| CA-CA-GR-B-162 | Calcium Carbonate Grade B | data_steward | Auto-mapped, validated |
| SO-CH-TE-223 | Sodium Chloride Technical | system_admin | Confirmed by domain expert |
| PA-OI-GR-B-690 | Palm Oil Grade B | domain_expert | Historical match confirmed |
| RE-ST-PR-679 | Resistant Starch Premium | system_admin | Historical match confirmed |
| SO-BE-50-TE-276 | Sodium Benzoate 50% Technical | domain_expert | Historical match confirmed |
| AS-AC-ST-686 | Ascorbic Acid Standard | data_steward | Auto-mapped, validated |
| GL-SY-FO-GR-600 | Glucose Syrup Food Grade | domain_expert | Verified via product specs |
| SO-BE-98-PH-GR-434 | Sodium Benzoate 98% Pharma Grade | domain_expert | Auto-mapped, validated |
| WH-GL-98-511 | Wheat Gluten 98% | data_steward | Historical match confirmed |
| PO-SO-50-TE-282 | Potassium Sorbate 50% Technical | data_steward | Historical match confirmed |
| PE-PR-302 | Pea Protein | data_steward | Auto-mapped, validated |
| PO-SO-GR-B-511 | Potassium Sorbate Grade B | system_admin | Historical match confirmed |
| CI-AC-70-FO-GR-198 | Citric Acid 70% Food Grade | domain_expert | Confirmed by domain expert |
| FR-99.5-GR-A-438 | Fructose 99.5% Grade A | system_admin | Verified via product specs |
| PO-SO-25-PH-GR-260 | Potassium Sorbate 25% Pharma Grade | data_steward | Auto-mapped, validated |
| SO-BE-667 | Sodium Benzoate | data_steward | Auto-mapped, validated |
| LA-AC-50-PR-288 | Lactic Acid 50% Premium | system_admin | Auto-mapped, validated |
| CA-98-TE-238 | Casein 98% Technical | domain_expert | Auto-mapped, validated |
| RE-ST-98-445 | Resistant Starch 98% | domain_expert | Verified via product specs |
| CA-CA-99.5-FO-GR-839 | Calcium Carbonate 99.5% Food Grade | system_admin | Historical match confirmed |
| FR-99.5-FO-GR-963 | Fructose 99.5% Food Grade | system_admin | Historical match confirmed |
| LA-AC-ST-823 | Lactic Acid Standard | domain_expert | Auto-mapped, validated |
| WH-GL-99.5-GR-A-933 | Wheat Gluten 99.5% Grade A | data_steward | Auto-mapped, validated |
| SO-BE-99.5-TE-484 | Sodium Benzoate 99.5% Technical | data_steward | Confirmed by domain expert |
| SO-BE-99.5-GR-A-930 | Sodium Benzoate 99.5% Grade A | domain_expert | Confirmed by domain expert |
| MA-DE-933 | Maltodextrin DE10 | system_admin | Historical match confirmed |
| AS-AC-50-321 | Ascorbic Acid 50% | system_admin | Confirmed by domain expert |
| SO-IS-432 | Soy Isolate | system_admin | Auto-mapped, validated |
| DE-GR-A-472 | Dextrose Grade A | system_admin | Auto-mapped, validated |
| CO-OI-70-GR-A-836 | Coconut Oil 70% Grade A | domain_expert | Historical match confirmed |
| CA-CA-50-260 | Calcium Carbonate 50% | data_steward | Confirmed by domain expert |
| PA-OI-50-497 | Palm Oil 50% | data_steward | Cross-referenced with transactions |
| PO-SO-98-216 | Potassium Sorbate 98% | system_admin | Auto-mapped, validated |
| AS-AC-439 | Ascorbic Acid | domain_expert | Cross-referenced with transactions |
| GL-SY-609 | Glucose Syrup | domain_expert | Verified via product specs |
| CA-CA-99.5-291 | Calcium Carbonate 99.5% | system_admin | Confirmed by domain expert |
| LA-AC-GR-B-700 | Lactic Acid Grade B | data_steward | Auto-mapped, validated |
| PO-SO-604 | Potassium Sorbate | system_admin | Confirmed by domain expert |
| PA-OI-PH-GR-124 | Palm Oil Pharma Grade | system_admin | Confirmed by domain expert |
| PE-PR-PR-775 | Pea Protein Premium | domain_expert | Confirmed by domain expert |
| CO-OI-98-TE-864 | Coconut Oil 98% Technical | domain_expert | Confirmed by domain expert |
| CO-OI-98-876 | Coconut Oil 98% | domain_expert | Confirmed by domain expert |
| RE-ST-99.5-242 | Resistant Starch 99.5% | system_admin | Cross-referenced with transactions |
| SO-CH-354 | Sodium Chloride | system_admin | Cross-referenced with transactions |
| CO-OI-25-TE-157 | Coconut Oil 25% Technical | system_admin | Confirmed by domain expert |
| LA-AC-98-GR-A-841 | Lactic Acid 98% Grade A | system_admin | Auto-mapped, validated |
| PE-PR-25-472 | Pea Protein 25% | domain_expert | Historical match confirmed |
| CA-CA-70-883 | Calcium Carbonate 70% | domain_expert | Historical match confirmed |
| RE-ST-50-692 | Resistant Starch 50% | domain_expert | Cross-referenced with transactions |
| RE-ST-FO-GR-727 | Resistant Starch Food Grade | data_steward | Confirmed by domain expert |
| SO-AC-70-542 | Sorbic Acid 70% | data_steward | Auto-mapped, validated |
| WH-GL-944 | Wheat Gluten | domain_expert | Verified via product specs |
| SO-BE-FO-GR-650 | Sodium Benzoate Food Grade | domain_expert | Cross-referenced with transactions |
| WH-GL-123 | Wheat Gluten | data_steward | Auto-mapped, validated |
| SO-AC-ST-392 | Sorbic Acid Standard | system_admin | Confirmed by domain expert |
| WH-GL-50-865 | Wheat Gluten 50% | domain_expert | Verified via product specs |
| DE-GR-B-244 | Dextrose Grade B | system_admin | Historical match confirmed |
| CI-AC-25-863 | Citric Acid 25% | system_admin | Auto-mapped, validated |
| PE-PR-746 | Pea Protein | domain_expert | Cross-referenced with transactions |
| CA-CA-98-928 | Calcium Carbonate 98% | system_admin | Auto-mapped, validated |
| CA-GR-B-950 | Casein Grade B | domain_expert | Verified via product specs |
| WH-GL-FO-GR-876 | Wheat Gluten Food Grade | data_steward | Confirmed by domain expert |
| CI-AC-PR-827 | Citric Acid Premium | data_steward | Cross-referenced with transactions |
| SO-CH-25-556 | Sodium Chloride 25% | system_admin | Cross-referenced with transactions |
| CO-OI-25-FO-GR-778 | Coconut Oil 25% Food Grade | system_admin | Historical match confirmed |
| AS-AC-573 | Ascorbic Acid | data_steward | Verified via product specs |
| SU-OI-GR-B-259 | Sunflower Oil Grade B | domain_expert | Historical match confirmed |
| PA-OI-99.5-867 | Palm Oil 99.5% | data_steward | Cross-referenced with transactions |
| SO-BE-824 | Sodium Benzoate | domain_expert | Historical match confirmed |
| PO-SO-70-899 | Potassium Sorbate 70% | data_steward | Historical match confirmed |
| PO-SO-ST-914 | Potassium Sorbate Standard | data_steward | Cross-referenced with transactions |
| DE-FO-GR-183 | Dextrose Food Grade | system_admin | Historical match confirmed |
| SO-BE-98-410 | Sodium Benzoate 98% | domain_expert | Cross-referenced with transactions |
| FR-99.5-TE-579 | Fructose 99.5% Technical | domain_expert | Verified via product specs |
| GL-SY-99.5-GR-B-358 | Glucose Syrup 99.5% Grade B | system_admin | Verified via product specs |
| SO-AC-50-FO-GR-250 | Sorbic Acid 50% Food Grade | domain_expert | Historical match confirmed |
| RA-OI-GR-A-980 | Rapeseed Oil Grade A | domain_expert | Historical match confirmed |
| DE-ST-999 | Dextrose Standard | data_steward | Verified via product specs |
| CA-CA-947 | Calcium Carbonate | domain_expert | Auto-mapped, validated |
| PA-OI-98-GR-A-940 | Palm Oil 98% Grade A | data_steward | Verified via product specs |
| RE-ST-50-232 | Resistant Starch 50% | system_admin | Confirmed by domain expert |
| DE-70-PH-GR-978 | Dextrin 70% Pharma Grade | system_admin | Historical match confirmed |
| LA-AC-25-819 | Lactic Acid 25% | system_admin | Verified via product specs |
| SO-AC-PH-GR-620 | Sorbic Acid Pharma Grade | system_admin | Cross-referenced with transactions |
| FR-99.5-TE-779 | Fructose 99.5% Technical | system_admin | Historical match confirmed |
| PE-PR-25-185 | Pea Protein 25% | data_steward | Historical match confirmed |
| AS-AC-TE-868 | Ascorbic Acid Technical | domain_expert | Confirmed by domain expert |
| SO-BE-708 | Sodium Benzoate | system_admin | Confirmed by domain expert |
| PA-OI-GR-B-326 | Palm Oil Grade B | system_admin | Auto-mapped, validated |
| LA-AC-25-PR-377 | Lactic Acid 25% Premium | domain_expert | Verified via product specs |
| DE-TE-956 | Dextrose Technical | domain_expert | Verified via product specs |
| DE-98-512 | Dextrin 98% | data_steward | Auto-mapped, validated |
| SO-IS-FO-GR-437 | Soy Isolate Food Grade | system_admin | Auto-mapped, validated |
| MA-DE-873 | Maltodextrin DE15 | system_admin | Verified via product specs |
| RE-ST-50-526 | Resistant Starch 50% | data_steward | Verified via product specs |
| FR-50-ST-938 | Fructose 50% Standard | domain_expert | Cross-referenced with transactions |
| MA-DE-516 | Maltodextrin DE20 | data_steward | Auto-mapped, validated |
| CA-CA-98-485 | Calcium Carbonate 98% | domain_expert | Confirmed by domain expert |
| IS-641 | Isoglucose | data_steward | Verified via product specs |
| AS-AC-FO-GR-835 | Ascorbic Acid Food Grade | system_admin | Auto-mapped, validated |
| MA-DE-161 | Maltodextrin DE20 | system_admin | Confirmed by domain expert |
| SO-CH-257 | Sodium Chloride | domain_expert | Auto-mapped, validated |
| DE-706 | Dextrin | domain_expert | Verified via product specs |
| SO-CH-25-FO-GR-400 | Sodium Chloride 25% Food Grade | system_admin | Historical match confirmed |
| PE-PR-70-PR-387 | Pea Protein 70% Premium | data_steward | Historical match confirmed |
| SO-CH-115 | Sodium Chloride | domain_expert | Verified via product specs |
| SO-IS-PR-309 | Soy Isolate Premium | system_admin | Verified via product specs |
| SO-CH-892 | Sodium Chloride | data_steward | Verified via product specs |
| LA-AC-471 | Lactic Acid | data_steward | Confirmed by domain expert |
| WH-GL-99.5-557 | Wheat Gluten 99.5% | data_steward | Verified via product specs |
| GL-SY-99.5-FO-GR-825 | Glucose Syrup 99.5% Food Grade | data_steward | Confirmed by domain expert |
| MA-DE-799 | Maltodextrin DE10 | data_steward | Cross-referenced with transactions |
| SO-BE-964 | Sodium Benzoate | system_admin | Confirmed by domain expert |
| IS-GR-B-640 | Isoglucose Grade B | data_steward | Confirmed by domain expert |
| IS-99.5-305 | Isoglucose 99.5% | domain_expert | Verified via product specs |
| CO-OI-70-GR-A-633 | Coconut Oil 70% Grade A | domain_expert | Historical match confirmed |
| GL-SY-25-722 | Glucose Syrup 25% | data_steward | Verified via product specs |
| SU-OI-GR-A-224 | Sunflower Oil Grade A | system_admin | Verified via product specs |
| CI-AC-ST-565 | Citric Acid Standard | system_admin | Verified via product specs |
| CA-GR-A-380 | Casein Grade A | system_admin | Auto-mapped, validated |
| PO-SO-480 | Potassium Sorbate | system_admin | Verified via product specs |
| RE-ST-GR-A-614 | Resistant Starch Grade A | system_admin | Verified via product specs |
| AS-AC-PR-778 | Ascorbic Acid Premium | domain_expert | Cross-referenced with transactions |
| SO-CH-99.5-GR-A-206 | Sodium Chloride 99.5% Grade A | domain_expert | Cross-referenced with transactions |
| WH-GL-GR-A-924 | Wheat Gluten Grade A | system_admin | Confirmed by domain expert |
| DE-GR-B-157 | Dextrin Grade B | data_steward | Auto-mapped, validated |
| SU-OI-TE-705 | Sunflower Oil Technical | system_admin | Auto-mapped, validated |
| PE-PR-251 | Pea Protein | data_steward | Historical match confirmed |
| LA-AC-TE-761 | Lactic Acid Technical | data_steward | Cross-referenced with transactions |
| MA-DE-640 | Maltodextrin DE15 | system_admin | Confirmed by domain expert |
| SO-IS-99.5-GR-A-499 | Soy Isolate 99.5% Grade A | domain_expert | Confirmed by domain expert |
| SO-BE-355 | Sodium Benzoate | system_admin | Auto-mapped, validated |
| SO-IS-99.5-141 | Soy Isolate 99.5% | data_steward | Historical match confirmed |
| SU-OI-251 | Sunflower Oil | domain_expert | Cross-referenced with transactions |
| SU-OI-ST-194 | Sunflower Oil Standard | data_steward | Historical match confirmed |
| PO-SO-768 | Potassium Sorbate | system_admin | Historical match confirmed |
| CO-OI-25-252 | Coconut Oil 25% | domain_expert | Auto-mapped, validated |
| CA-TE-336 | Casein Technical | domain_expert | Historical match confirmed |
| SU-OI-70-FO-GR-432 | Sunflower Oil 70% Food Grade | system_admin | Auto-mapped, validated |
| CA-50-PR-226 | Casein 50% Premium | data_steward | Cross-referenced with transactions |
| IS-GR-B-649 | Isoglucose Grade B | domain_expert | Confirmed by domain expert |
| LA-AC-891 | Lactic Acid | data_steward | Historical match confirmed |
| RE-ST-ST-711 | Resistant Starch Standard | system_admin | Historical match confirmed |
| RE-ST-575 | Resistant Starch | system_admin | Historical match confirmed |
| SO-CH-TE-789 | Sodium Chloride Technical | domain_expert | Verified via product specs |
| CO-OI-98-PR-329 | Coconut Oil 98% Premium | domain_expert | Cross-referenced with transactions |
| DE-98-FO-GR-211 | Dextrin 98% Food Grade | system_admin | Confirmed by domain expert |
| SU-OI-423 | Sunflower Oil | system_admin | Historical match confirmed |
| CA-25-GR-A-885 | Casein 25% Grade A | data_steward | Verified via product specs |
| DE-TE-340 | Dextrin Technical | domain_expert | Cross-referenced with transactions |
| CY-ST-539 | Cyclodextrin Standard | domain_expert | Confirmed by domain expert |
| CA-25-TE-580 | Casein 25% Technical | domain_expert | Verified via product specs |
| WH-GL-403 | Wheat Gluten | data_steward | Verified via product specs |
| SU-OI-GR-A-704 | Sunflower Oil Grade A | domain_expert | Historical match confirmed |
| CA-CA-FO-GR-685 | Calcium Carbonate Food Grade | domain_expert | Verified via product specs |
| FR-ST-953 | Fructose Standard | data_steward | Historical match confirmed |
| RE-ST-796 | Resistant Starch | system_admin | Verified via product specs |
| PO-SO-FO-GR-989 | Potassium Sorbate Food Grade | system_admin | Verified via product specs |
| CI-AC-596 | Citric Acid | data_steward | Verified via product specs |
| SO-IS-PR-242 | Soy Isolate Premium | data_steward | Auto-mapped, validated |
| PE-PR-ST-174 | Pea Protein Standard | data_steward | Cross-referenced with transactions |
| FR-PR-267 | Fructose Premium | system_admin | Cross-referenced with transactions |
| CI-AC-FO-GR-977 | Citric Acid Food Grade | data_steward | Historical match confirmed |
| AT-IN-327 | Atlas Industries LLC | domain_expert | Confirmed by domain expert |
| PR-PA-823 International | Prime Partners | domain_expert | Historical match confirmed |
| GL-DI-615 Corp. | Global Distribution LLC | system_admin | Verified via product specs |
| ST-DI-782 SA | Stellar Distribution SA | domain_expert | Confirmed by domain expert |
| ST-IN-505 SA | Stratos Ingredients SARL | domain_expert | Auto-mapped, validated |
| ME-SO-413 | Meridian Solutions Ltd. | domain_expert | Auto-mapped, validated |
| PA-LO-382 Group | Pacific Logistics | domain_expert | Verified via product specs |
| ST-SU-323 Group | Stratos Supply Group | data_steward | Historical match confirmed |
| QU-IN-923 International | Quantum Ingredients | data_steward | Verified via product specs |
| CO-CH-289 Group | Core Chemicals International | domain_expert | Confirmed by domain expert |
| CE-TR-144 International | Central Trading Group | data_steward | Verified via product specs |
| PA-CH-795 | Pacific Chemicals AG | data_steward | Cross-referenced with transactions |
| PA-DI-201 NV | Pacific Distribution NV | data_steward | Cross-referenced with transactions |
| PR-EN-361 International | Premier Enterprise International | system_admin | Verified via product specs |
| HO-MA-349 | Horizon Materials PLC | data_steward | Verified via product specs |
| PI-DI-518 | Pinnacle Distribution KG | domain_expert | Historical match confirmed |
| VE-EN-393 Group | Vertex Enterprise Holdings | system_admin | Verified via product specs |
| PR-CH-565 SAS | Prime Chemicals | data_steward | Verified via product specs |
| ST-TR-340 BV | Stratos Trading BV | system_admin | Confirmed by domain expert |
| BA-EN-363 KG | Baltic Enterprise KG | data_steward | Verified via product specs |
| PR-LO-245 Ltd. | Premier Logistics Ltd. | data_steward | Cross-referenced with transactions |
| QU-MA-180 | Quantum Manufacturing KG | domain_expert | Cross-referenced with transactions |
| AT-MA-796 LLC | Atlas Manufacturing | domain_expert | Historical match confirmed |
| AT-MA-324 International | Atlantic Manufacturing | system_admin | Cross-referenced with transactions |
| ZE-MA-359 Group | Zenith Manufacturing | system_admin | Verified via product specs |
| AT-LO-410 Holdings | Atlas Logistics International | system_admin | Auto-mapped, validated |
| CE-PR-134 | Central Processing | system_admin | Cross-referenced with transactions |
| GL-PR-596 | Global Processing SAS | data_steward | Auto-mapped, validated |
| HO-PA-330 Holdings | Horizon Partners Group | domain_expert | Auto-mapped, validated |
| AP-SO-704 | Apex Solutions | domain_expert | Auto-mapped, validated |
| PI-CH-997 SAS | Pinnacle Chemicals SA | system_admin | Historical match confirmed |
| CO-MA-845 Holdings | Core Manufacturing Holdings | data_steward | Cross-referenced with transactions |
| PI-IN-244 | Pinnacle Industries SAS | domain_expert | Verified via product specs |
| PR-MA-826 Corp. | Prism Manufacturing LLC | domain_expert | Historical match confirmed |
| ZE-PA-511 PLC | Zenith Partners PLC | domain_expert | Verified via product specs |
| EL-DI-554 International | Elite Distribution | system_admin | Verified via product specs |
| PR-SU-935 Ltd. | Prime Supply | data_steward | Cross-referenced with transactions |
| ME-TR-587 | Meridian Trading | system_admin | Verified via product specs |
| PR-IN-608 BV | Prism Ingredients | system_admin | Verified via product specs |
| ME-SO-760 GmbH | Meridian Solutions KG | data_steward | Verified via product specs |
| EL-CH-346 GmbH | Elite Chemicals AG | data_steward | Historical match confirmed |
| GL-EN-914 NV | Global Enterprise NV | system_admin | Auto-mapped, validated |
| CE-SU-700 Group | Central Supply Holdings | data_steward | Auto-mapped, validated |
| GL-LO-196 NV | Global Logistics | data_steward | Cross-referenced with transactions |
| CO-EN-642 AG | Continental Enterprise KG | data_steward | Auto-mapped, validated |
| CO-LO-919 Holdings | Core Logistics Holdings | data_steward | Verified via product specs |
| BA-TR-377 NV | Baltic Trading BV | domain_expert | Auto-mapped, validated |
| NO-IN-155 SA | Nordic Ingredients SA | domain_expert | Historical match confirmed |
| VE-DI-139 KG | Vertex Distribution AG | data_steward | Auto-mapped, validated |
| PR-LO-104 KG | Premier Logistics GmbH | data_steward | Verified via product specs |
| QU-TR-219 International | Quantum Trading | data_steward | Verified via product specs |
| CA-CO-549 GmbH | Catalyst Commodities GmbH | system_admin | Historical match confirmed |
| BA-IN-777 Inc. | Baltic Ingredients | system_admin | Auto-mapped, validated |
| AP-TR-571 Group | Apex Trading Group | data_steward | Auto-mapped, validated |
| CO-IN-915 KG | Continental Ingredients | domain_expert | Auto-mapped, validated |
| NE-DI-555 | Nexus Distribution | system_admin | Verified via product specs |
| ST-IN-592 SA | Stratos Ingredients SARL | data_steward | Auto-mapped, validated |
| CA-IN-566 International | Catalyst Industries International | data_steward | Verified via product specs |
| VA-MA-537 Holdings | Vanguard Materials Group | domain_expert | Confirmed by domain expert |
| PI-CO-717 | Pinnacle Commodities | data_steward | Cross-referenced with transactions |
| PR-SO-769 LLC | Premier Solutions LLC | system_admin | Verified via product specs |
| CO-SU-445 LLC | Core Supply | domain_expert | Historical match confirmed |
| AP-CH-159 LLC | Apex Chemicals | system_admin | Auto-mapped, validated |
| GL-IN-218 | Global Ingredients AG | domain_expert | Auto-mapped, validated |
| NE-EN-400 Group | Nexus Enterprise International | domain_expert | Cross-referenced with transactions |
| AP-CH-166 International | Apex Chemicals | data_steward | Historical match confirmed |
| PI-SO-581 Inc. | Pinnacle Solutions Corp. | system_admin | Auto-mapped, validated |
| AT-CH-900 AG | Atlas Chemicals | data_steward | Verified via product specs |
| PR-IN-695 Holdings | Premier Industries Group | domain_expert | Historical match confirmed |
| AT-CO-808 GmbH | Atlantic Commodities | system_admin | Auto-mapped, validated |
| PR-IN-149 Holdings | Prism Ingredients | system_admin | Cross-referenced with transactions |
| BA-SO-835 Corp. | Baltic Solutions | data_steward | Confirmed by domain expert |
| VE-DI-556 SA | Vertex Distribution SA | data_steward | Verified via product specs |
| CE-MA-931 | Central Manufacturing NV | system_admin | Historical match confirmed |
| ZE-TR-981 | Zenith Trading LLC | data_steward | Historical match confirmed |
| NE-DI-555 Corp. | Nexus Distribution | data_steward | Historical match confirmed |
| PI-IN-388 | Pinnacle Ingredients AG | data_steward | Historical match confirmed |
| ZE-PR-190 BV | Zenith Processing | system_admin | Confirmed by domain expert |
| CO-CH-401 Inc. | Continental Chemicals Inc. | domain_expert | Confirmed by domain expert |
| HO-LO-514 International | Horizon Logistics International | data_steward | Cross-referenced with transactions |
| QU-SO-509 | Quantum Solutions Group | system_admin | Auto-mapped, validated |
| NO-MA-529 | Nordic Manufacturing | domain_expert | Auto-mapped, validated |
| GL-SO-534 Holdings | Global Solutions International | system_admin | Historical match confirmed |
| NO-IN-797 | Nordic Industries Ltd. | domain_expert | Historical match confirmed |
| HO-PA-675 | Horizon Partners Ltd. | system_admin | Verified via product specs |
| HO-IN-142 AG | Horizon Industries | domain_expert | Auto-mapped, validated |
| NE-PR-315 Holdings | Nexus Processing International | system_admin | Auto-mapped, validated |
| QU-CO-993 | Quantum Commodities PLC | domain_expert | Auto-mapped, validated |
| NE-CH-574 Group | Nexus Chemicals Group | domain_expert | Verified via product specs |
| ZE-PA-718 LLC | Zenith Partners Corp. | data_steward | Cross-referenced with transactions |
| CA-CO-939 | Catalyst Commodities | domain_expert | Cross-referenced with transactions |
| PR-MA-669 Ltd. | Prism Materials Ltd. | system_admin | Cross-referenced with transactions |
| VE-IN-644 Ltd. | Vertex Ingredients | domain_expert | Historical match confirmed |
| CO-SO-525 BV | Continental Solutions | domain_expert | Cross-referenced with transactions |
| ST-CO-650 International | Stellar Commodities | system_admin | Historical match confirmed |
| NE-CO-575 Holdings | Nexus Commodities International | system_admin | Auto-mapped, validated |
| PI-DI-618 NV | Pinnacle Distribution | system_admin | Historical match confirmed |
| CA-IN-236 PLC | Catalyst Industries | system_admin | Historical match confirmed |
| AT-IN-931 | Atlas Industries Group | data_steward | Verified via product specs |
| QU-PA-832 NV | Quantum Partners | data_steward | Verified via product specs |
| ST-DI-517 Holdings | Stratos Distribution Group | system_admin | Verified via product specs |
| PA-SU-946 Group | Pacific Supply | domain_expert | Confirmed by domain expert |
| PR-SO-362 | Prism Solutions Corp. | data_steward | Auto-mapped, validated |
| VE-CO-558 | Vertex Commodities | domain_expert | Confirmed by domain expert |
| AT-PR-442 | Atlantic Processing International | domain_expert | Auto-mapped, validated |
| QU-TR-490 SARL | Quantum Trading SA | data_steward | Cross-referenced with transactions |
| CE-MA-604 | Central Manufacturing Holdings | data_steward | Auto-mapped, validated |
| NO-MA-994 | Nordic Materials Holdings | domain_expert | Confirmed by domain expert |
| AT-TR-553 | Atlantic Trading BV | domain_expert | Cross-referenced with transactions |
| EL-SO-163 | Elite Solutions | data_steward | Cross-referenced with transactions |
| AT-LO-568 SA | Atlantic Logistics SAS | domain_expert | Cross-referenced with transactions |
| ST-PR-265 Corp. | Stratos Processing | data_steward | Historical match confirmed |
| CE-IN-169 Group | Central Ingredients | data_steward | Historical match confirmed |
| HO-PA-995 Group | Horizon Partners | domain_expert | Cross-referenced with transactions |
| PR-EN-954 Holdings | Premier Enterprise International | system_admin | Verified via product specs |
| BA-IN-585 SARL | Baltic Ingredients SA | system_admin | Auto-mapped, validated |
| ZE-TR-467 AG | Zenith Trading | system_admin | Confirmed by domain expert |
| EL-LO-432 Holdings | Elite Logistics Holdings | system_admin | Cross-referenced with transactions |
| PR-SO-102 | Prime Solutions Holdings | domain_expert | Auto-mapped, validated |
| ST-DI-556 Holdings | Stellar Distribution International | data_steward | Auto-mapped, validated |
| NE-DI-240 Ltd. | Nexus Distribution PLC | domain_expert | Cross-referenced with transactions |
| CA-CO-128 SAS | Catalyst Commodities SAS | system_admin | Verified via product specs |
| NE-PA-401 | Nexus Partners GmbH | domain_expert | Cross-referenced with transactions |
| CO-MA-726 NV | Continental Materials NV | data_steward | Cross-referenced with transactions |
| ST-PA-504 | Stellar Partners | data_steward | Confirmed by domain expert |
| ME-DI-790 Group | Meridian Distribution | system_admin | Verified via product specs |
| PR-TR-294 | Premier Trading Group | data_steward | Auto-mapped, validated |
| NE-SO-511 | Nexus Solutions SAS | domain_expert | Confirmed by domain expert |
| AT-IN-899 Group | Atlantic Industries | system_admin | Verified via product specs |
| ST-MA-670 Group | Stellar Manufacturing Group | system_admin | Historical match confirmed |
| ZE-MA-316 | Zenith Manufacturing PLC | domain_expert | Auto-mapped, validated |
| CO-CH-610 | Core Chemicals AG | system_admin | Auto-mapped, validated |
| AP-MA-145 International | Apex Materials Group | domain_expert | Confirmed by domain expert |
| HO-PA-149 International | Horizon Partners International | domain_expert | Confirmed by domain expert |
| CO-PR-215 Group | Continental Processing Group | system_admin | Verified via product specs |
| EL-MA-344 NV | Elite Materials NV | system_admin | Verified via product specs |
| BA-SO-682 International | Baltic Solutions International | domain_expert | Auto-mapped, validated |
| NE-SU-335 | Nexus Supply Group | system_admin | Auto-mapped, validated |
| PA-IN-447 | Pacific Industries Ltd. | domain_expert | Confirmed by domain expert |
| ST-PA-980 | Stratos Partners SAS | data_steward | Cross-referenced with transactions |
| AT-LO-132 | Atlas Logistics International | system_admin | Historical match confirmed |
| NE-IN-874 SA | Nexus Ingredients | domain_expert | Cross-referenced with transactions |
| PR-IN-195 KG | Prism Ingredients | data_steward | Verified via product specs |
| CE-MA-338 | Central Manufacturing PLC | system_admin | Confirmed by domain expert |
| PR-MA-359 | Prism Materials International | data_steward | Verified via product specs |
| QU-PR-732 SA | Quantum Processing SA | domain_expert | Historical match confirmed |
| CO-IN-363 AG | Continental Ingredients | domain_expert | Auto-mapped, validated |
| CE-MA-847 | Central Manufacturing Holdings | domain_expert | Cross-referenced with transactions |
| GL-PR-906 | Global Processing Holdings | data_steward | Cross-referenced with transactions |
| PA-EN-915 | Pacific Enterprise SAS | data_steward | Confirmed by domain expert |
| NO-MA-484 BV | Nordic Manufacturing NV | domain_expert | Cross-referenced with transactions |
| PR-SO-400 | Premier Solutions Holdings | domain_expert | Auto-mapped, validated |
| CO-MA-993 Corp. | Continental Manufacturing Inc. | system_admin | Verified via product specs |
| NE-EN-710 NV | Nexus Enterprise | system_admin | Auto-mapped, validated |
| BA-IN-897 BV | Baltic Industries BV | data_steward | Cross-referenced with transactions |
| AT-PA-546 Corp. | Atlas Partners Corp. | system_admin | Historical match confirmed |
| EL-PA-851 | Elite Partners International | domain_expert | Auto-mapped, validated |
| NE-TR-634 International | Nexus Trading Group | data_steward | Verified via product specs |
| PR-MA-448 | Prism Manufacturing PLC | domain_expert | Historical match confirmed |
| NO-LO-598 Holdings | Nordic Logistics | domain_expert | Cross-referenced with transactions |
| VA-LO-190 International | Vanguard Logistics | system_admin | Verified via product specs |
| AT-MA-694 Holdings | Atlas Materials Holdings | domain_expert | Verified via product specs |
| AT-DI-544 | Atlantic Distribution | system_admin | Confirmed by domain expert |
| ZE-MA-924 | Zenith Materials NV | system_admin | Confirmed by domain expert |
| QU-EN-736 NV | Quantum Enterprise NV | data_steward | Historical match confirmed |
| GL-CH-617 SARL | Global Chemicals | system_admin | Historical match confirmed |
| PR-CH-121 KG | Prism Chemicals KG | domain_expert | Auto-mapped, validated |
| AT-PR-500 International | Atlantic Processing | system_admin | Auto-mapped, validated |
| VA-IN-954 PLC | Vanguard Industries PLC | data_steward | Auto-mapped, validated |
| VE-DI-822 Group | Vertex Distribution Holdings | data_steward | Verified via product specs |
| CE-CO-433 | Central Commodities Ltd. | domain_expert | Historical match confirmed |
| AT-SU-132 | Atlantic Supply | data_steward | Confirmed by domain expert |
| ME-TR-366 International | Meridian Trading Holdings | system_admin | Historical match confirmed |
| PI-LO-710 NV | Pinnacle Logistics BV | system_admin | Cross-referenced with transactions |
| PA-IN-136 | Pacific Industries Group | data_steward | Cross-referenced with transactions |
| PR-MA-114 BV | Premier Manufacturing NV | data_steward | Cross-referenced with transactions |
| CA-IN-146 SA | Catalyst Industries | domain_expert | Auto-mapped, validated |
| PR-PA-671 SA | Premier Partners | data_steward | Auto-mapped, validated |
| ST-SU-125 SA | Stellar Supply | system_admin | Cross-referenced with transactions |
| ST-SU-950 SAS | Stratos Supply SAS | data_steward | Verified via product specs |
| PI-MA-367 SA | Pinnacle Materials SA | system_admin | Confirmed by domain expert |
| ST-CO-827 Holdings | Stratos Commodities International | system_admin | Confirmed by domain expert |
| AP-MA-984 | Apex Manufacturing | domain_expert | Confirmed by domain expert |
| PA-MA-742 KG | Pacific Materials | domain_expert | Auto-mapped, validated |
| VA-PA-407 | Vanguard Partners PLC | data_steward | Verified via product specs |
| VA-DI-229 | Vanguard Distribution | system_admin | Cross-referenced with transactions |
| PI-LO-946 | Pinnacle Logistics International | system_admin | Historical match confirmed |
| CE-PA-586 SARL | Central Partners | domain_expert | Verified via product specs |
| ME-CH-956 KG | Meridian Chemicals AG | data_steward | Historical match confirmed |
| PR-EN-809 Holdings | Prime Enterprise Holdings | data_steward | Auto-mapped, validated |
| NO-MA-452 | Nordic Manufacturing Holdings | domain_expert | Auto-mapped, validated |
| VE-LO-902 Group | Vertex Logistics Holdings | domain_expert | Cross-referenced with transactions |
| PR-CO-800 Corp. | Prism Commodities Corp. | system_admin | Confirmed by domain expert |
| ZE-DI-241 | Zenith Distribution SARL | domain_expert | Confirmed by domain expert |
| VA-DI-105 | Vanguard Distribution | data_steward | Confirmed by domain expert |
| CO-IN-421 | Core Ingredients | domain_expert | Historical match confirmed |
| PR-SO-284 Group | Prime Solutions | data_steward | Cross-referenced with transactions |
| BA-SU-479 | Baltic Supply Holdings | domain_expert | Cross-referenced with transactions |
| PR-CH-334 GmbH | Premier Chemicals | data_steward | Cross-referenced with transactions |
| PR-MA-844 | Premier Materials SAS | data_steward | Historical match confirmed |
| HO-LO-534 PLC | Horizon Logistics | data_steward | Auto-mapped, validated |
| PR-LO-801 AG | Premier Logistics AG | system_admin | Confirmed by domain expert |
| GL-PA-520 BV | Global Partners | data_steward | Confirmed by domain expert |
| CO-MA-371 | Core Manufacturing | data_steward | Auto-mapped, validated |
| NO-DI-180 Ltd. | Nordic Distribution | system_admin | Confirmed by domain expert |
| PR-PA-794 PLC | Prime Partners PLC | domain_expert | Historical match confirmed |
| QU-TR-440 | Quantum Trading | domain_expert | Verified via product specs |
| CE-MA-423 BV | Central Materials NV | system_admin | Auto-mapped, validated |
| CE-LO-195 | Central Logistics International | domain_expert | Auto-mapped, validated |
| EL-LO-712 SA | Elite Logistics SA | domain_expert | Verified via product specs |
| HO-DI-531 Group | Horizon Distribution Holdings | data_steward | Historical match confirmed |
| PI-PR-193 | Pinnacle Processing | domain_expert | Auto-mapped, validated |
| VE-CO-290 AG | Vertex Commodities | data_steward | Verified via product specs |
| CA-SU-512 Holdings | Catalyst Supply Holdings | data_steward | Historical match confirmed |
| CO-DI-629 BV | Core Distribution | data_steward | Verified via product specs |
| AP-CH-617 LLC | Apex Chemicals | data_steward | Verified via product specs |
| PR-EN-875 Group | Premier Enterprise Group | domain_expert | Auto-mapped, validated |
| NO-DI-582 AG | Nordic Distribution | domain_expert | Auto-mapped, validated |
| PR-CO-156 PLC | Prime Commodities | data_steward | Confirmed by domain expert |
| PA-MA-412 GmbH | Pacific Materials KG | system_admin | Auto-mapped, validated |
| ST-DI-183 Inc. | Stellar Distribution | system_admin | Verified via product specs |
| NO-PR-828 SA | Nordic Processing SAS | domain_expert | Historical match confirmed |
| QU-PR-593 International | Quantum Processing | domain_expert | Cross-referenced with transactions |
| QU-PA-830 Group | Quantum Partners Group | domain_expert | Verified via product specs |
| GL-PR-599 | Global Processing KG | domain_expert | Cross-referenced with transactions |
| ZE-IN-456 LLC | Zenith Industries Corp. | domain_expert | Auto-mapped, validated |
| PI-IN-444 | Pinnacle Industries | domain_expert | Verified via product specs |
| AP-TR-161 International | Apex Trading Holdings | domain_expert | Verified via product specs |
| PR-PA-998 Holdings | Premier Partners Group | domain_expert | Historical match confirmed |
| ST-SO-965 | Stratos Solutions | data_steward | Historical match confirmed |
| VE-DI-578 International | Vertex Distribution | system_admin | Verified via product specs |
| BA-MA-518 Group | Baltic Manufacturing | domain_expert | Confirmed by domain expert |
| QU-TR-981 Group | Quantum Trading Holdings | system_admin | Confirmed by domain expert |
| ST-MA-621 International | Stellar Manufacturing Holdings | domain_expert | Verified via product specs |
| BA-TR-619 | Baltic Trading Holdings | data_steward | Cross-referenced with transactions |
| CA-SU-681 Group | Catalyst Supply Holdings | data_steward | Historical match confirmed |
| AT-SU-661 Corp. | Atlas Supply Corp. | system_admin | Auto-mapped, validated |
| PR-PA-624 PLC | Premier Partners | domain_expert | Verified via product specs |
| AT-PR-985 International | Atlantic Processing Holdings | data_steward | Cross-referenced with transactions |
| BA-PR-950 | Baltic Processing | system_admin | Confirmed by domain expert |
| CO-PA-308 | Core Partners PLC | domain_expert | Verified via product specs |
| VE-CH-841 Group | Vertex Chemicals | system_admin | Auto-mapped, validated |
| ST-TR-590 | Stratos Trading Holdings | data_steward | Verified via product specs |
| VA-IN-429 | Vanguard Industries BV | data_steward | Historical match confirmed |
| AT-IN-716 Corp. | Atlas Industries LLC | data_steward | Verified via product specs |
| PR-LO-109 Group | Prime Logistics International | system_admin | Confirmed by domain expert |
| AP-LO-197 Corp. | Apex Logistics Inc. | system_admin | Auto-mapped, validated |
| PR-LO-105 | Prime Logistics | system_admin | Historical match confirmed |
| PI-MA-680 | Pinnacle Materials | system_admin | Cross-referenced with transactions |
| AT-MA-457 | Atlantic Materials | data_steward | Historical match confirmed |
| PR-SU-CO-624 | Premier Supply Co. | data_steward | Cross-referenced with transactions |
| CA-LO-967 | Catalyst Logistics | domain_expert | Auto-mapped, validated |
| PR-SU-CO-176 | Premier Supply Co. | system_admin | Auto-mapped, validated |
| PR-MA-609 | Prism Materials | system_admin | Verified via product specs |
| PR-MA-665 | Prism Materials | system_admin | Historical match confirmed |
| ST-LO-181 | Stratos Logistics | domain_expert | Auto-mapped, validated |
| CO-MA-245 | Core Materials | data_steward | Confirmed by domain expert |
| EL-SO-358 | Elite Sourcing | domain_expert | Auto-mapped, validated |
| VE-MA-298 | Vertex Materials | system_admin | Cross-referenced with transactions |
| ME-MA-977 | Meridian Materials | system_admin | Historical match confirmed |
| VE-LO-437 | Vertex Logistics | data_steward | Historical match confirmed |
| ST-SO-491 | Stellar Sourcing | data_steward | Cross-referenced with transactions |
| VE-MA-260 | Vertex Materials | domain_expert | Verified via product specs |
| GL-LO-669 | Global Logistics | system_admin | Cross-referenced with transactions |
| PI-SO-922 | Pinnacle Sourcing | system_admin | Verified via product specs |
| VA-MA-502 | Vanguard Materials | system_admin | Confirmed by domain expert |
| CO-SO-101 | Continental Sourcing | data_steward | Verified via product specs |
| VE-SO-401 | Vertex Sourcing | domain_expert | Historical match confirmed |
| QU-SU-CO-774 | Quantum Supply Co. | data_steward | Auto-mapped, validated |
| ME-LO-192 | Meridian Logistics | system_admin | Confirmed by domain expert |
| PR-MA-295 | Prism Materials | domain_expert | Historical match confirmed |
| GL-SO-841 | Global Sourcing | data_steward | Historical match confirmed |
| VE-SO-701 | Vertex Sourcing | data_steward | Confirmed by domain expert |
| AT-SU-CO-707 | Atlas Supply Co. | system_admin | Cross-referenced with transactions |
| BA-SU-CO-569 | Baltic Supply Co. | data_steward | Cross-referenced with transactions |
| NE-LO-499 | Nexus Logistics | system_admin | Verified via product specs |
| ST-LO-422 | Stellar Logistics | domain_expert | Auto-mapped, validated |
| PR-LO-420 | Premier Logistics | data_steward | Confirmed by domain expert |
| AP-MA-498 | Apex Materials | data_steward | Verified via product specs |
| VE-LO-665 | Vertex Logistics | data_steward | Historical match confirmed |
| ST-MA-282 | Stellar Materials | domain_expert | Confirmed by domain expert |
| NE-LO-300 | Nexus Logistics | system_admin | Verified via product specs |
| PR-SO-441 | Prism Sourcing | system_admin | Cross-referenced with transactions |
| ST-SO-673 | Stratos Sourcing | domain_expert | Auto-mapped, validated |
| PR-SU-CO-232 | Premier Supply Co. | system_admin | Historical match confirmed |
| CO-SU-CO-318 | Continental Supply Co. | system_admin | Auto-mapped, validated |
| NE-LO-735 | Nexus Logistics | system_admin | Confirmed by domain expert |
| AT-SU-CO-864 | Atlantic Supply Co. | data_steward | Historical match confirmed |
| AT-LO-592 | Atlas Logistics | domain_expert | Historical match confirmed |
| AT-MA-704 | Atlantic Materials | system_admin | Confirmed by domain expert |
| PR-SU-CO-920 | Prime Supply Co. | system_admin | Historical match confirmed |
| QU-SU-CO-959 | Quantum Supply Co. | domain_expert | Cross-referenced with transactions |
| QU-SO-233 | Quantum Sourcing | domain_expert | Verified via product specs |
| PR-SO-277 | Prism Sourcing | domain_expert | Verified via product specs |
| NO-SU-CO-376 | Nordic Supply Co. | system_admin | Historical match confirmed |
| PR-SU-CO-573 | Premier Supply Co. | system_admin | Verified via product specs |
| AP-SU-CO-755 | Apex Supply Co. | domain_expert | Historical match confirmed |
| AP-SO-122 | Apex Sourcing | data_steward | Verified via product specs |
| ST-SU-CO-731 | Stratos Supply Co. | domain_expert | Auto-mapped, validated |
| PR-MA-581 | Premier Materials | data_steward | Cross-referenced with transactions |
| AP-LO-246 | Apex Logistics | system_admin | Historical match confirmed |
| PR-LO-745 | Premier Logistics | system_admin | Auto-mapped, validated |
| EL-LO-372 | Elite Logistics | domain_expert | Confirmed by domain expert |
| CE-MA-213 | Central Materials | data_steward | Auto-mapped, validated |
| AP-LO-406 | Apex Logistics | domain_expert | Confirmed by domain expert |
| NO-SO-478 | Nordic Sourcing | data_steward | Auto-mapped, validated |
| PA-SO-658 | Pacific Sourcing | data_steward | Historical match confirmed |
| ST-SO-771 | Stratos Sourcing | data_steward | Cross-referenced with transactions |
| PR-LO-704 | Prism Logistics | data_steward | Cross-referenced with transactions |
| CA-MA-370 | Catalyst Materials | domain_expert | Cross-referenced with transactions |
| ME-LO-901 | Meridian Logistics | system_admin | Auto-mapped, validated |
| PR-MA-367 | Prime Materials | system_admin | Cross-referenced with transactions |
| CE-SO-153 | Central Sourcing | domain_expert | Cross-referenced with transactions |
| EL-SU-CO-921 | Elite Supply Co. | domain_expert | Historical match confirmed |
| AT-SO-915 | Atlantic Sourcing | data_steward | Verified via product specs |
| PI-SU-CO-207 | Pinnacle Supply Co. | system_admin | Auto-mapped, validated |
| HO-MA-854 | Horizon Materials | domain_expert | Auto-mapped, validated |
| CO-LO-944 | Continental Logistics | domain_expert | Auto-mapped, validated |
| AT-SO-165 | Atlantic Sourcing | domain_expert | Confirmed by domain expert |
| NO-LO-302 | Nordic Logistics | system_admin | Auto-mapped, validated |
| CO-LO-285 | Continental Logistics | data_steward | Cross-referenced with transactions |
| BA-SU-CO-430 | Baltic Supply Co. | system_admin | Historical match confirmed |
| PR-SO-388 | Prism Sourcing | domain_expert | Historical match confirmed |
| ME-SO-242 | Meridian Sourcing | system_admin | Cross-referenced with transactions |
| NO-SU-CO-153 | Nordic Supply Co. | system_admin | Cross-referenced with transactions |
| BA-SU-CO-583 | Baltic Supply Co. | data_steward | Verified via product specs |
| VE-SU-CO-237 | Vertex Supply Co. | system_admin | Cross-referenced with transactions |
| HO-LO-699 | Horizon Logistics | system_admin | Confirmed by domain expert |
| PA-MA-664 | Pacific Materials | system_admin | Verified via product specs |
| NE-SO-810 | Nexus Sourcing | data_steward | Cross-referenced with transactions |
| HO-SO-924 | Horizon Sourcing | system_admin | Historical match confirmed |
| ST-MA-641 | Stratos Materials | system_admin | Verified via product specs |
| NE-MA-103 | Nexus Materials | domain_expert | Verified via product specs |
| CO-LO-520 | Core Logistics | data_steward | Cross-referenced with transactions |
| AP-SO-687 | Apex Sourcing | domain_expert | Auto-mapped, validated |
| AT-SO-658 | Atlas Sourcing | system_admin | Verified via product specs |
| PA-MA-602 | Pacific Materials | domain_expert | Confirmed by domain expert |
| CO-LO-137 | Continental Logistics | domain_expert | Cross-referenced with transactions |
| PA-SU-CO-864 | Pacific Supply Co. | system_admin | Verified via product specs |
| HO-LO-886 | Horizon Logistics | data_steward | Historical match confirmed |
| QU-LO-333 | Quantum Logistics | system_admin | Confirmed by domain expert |
| ST-LO-927 | Stellar Logistics | system_admin | Historical match confirmed |
| PR-SU-CO-333 | Prism Supply Co. | domain_expert | Historical match confirmed |
| PR-SU-CO-832 | Prism Supply Co. | system_admin | Cross-referenced with transactions |
| AT-LO-914 | Atlas Logistics | system_admin | Confirmed by domain expert |
| CE-SU-CO-752 | Central Supply Co. | system_admin | Confirmed by domain expert |
| PR-SU-CO-187 | Premier Supply Co. | data_steward | Cross-referenced with transactions |
| ZE-LO-372 | Zenith Logistics | data_steward | Historical match confirmed |
| PI-SO-251 | Pinnacle Sourcing | domain_expert | Cross-referenced with transactions |
| PI-MA-133 | Pinnacle Materials | system_admin | Confirmed by domain expert |
| PA-MA-102 | Pacific Materials | system_admin | Verified via product specs |
| AT-MA-739 | Atlas Materials | domain_expert | Confirmed by domain expert |
| CO-MA-295 | Core Materials | system_admin | Confirmed by domain expert |
| AT-MA-510 | Atlas Materials | domain_expert | Cross-referenced with transactions |
| ME-SU-CO-314 | Meridian Supply Co. | domain_expert | Auto-mapped, validated |
| NO-LO-524 | Nordic Logistics | domain_expert | Verified via product specs |
| AT-SU-CO-755 | Atlantic Supply Co. | domain_expert | Verified via product specs |
| ZE-LO-524 | Zenith Logistics | system_admin | Confirmed by domain expert |
| CA-MA-271 | Catalyst Materials | domain_expert | Auto-mapped, validated |
| QU-MA-886 | Quantum Materials | system_admin | Auto-mapped, validated |
| CO-SO-442 | Continental Sourcing | data_steward | Historical match confirmed |
| VA-MA-951 | Vanguard Materials | system_admin | Auto-mapped, validated |
| CA-MA-129 | Catalyst Materials | domain_expert | Cross-referenced with transactions |
| PI-LO-142 | Pinnacle Logistics | data_steward | Verified via product specs |
| PR-SU-CO-552 | Premier Supply Co. | domain_expert | Historical match confirmed |
| ME-LO-583 | Meridian Logistics | domain_expert | Auto-mapped, validated |
| AT-MA-246 | Atlantic Materials | data_steward | Verified via product specs |
| ME-MA-989 | Meridian Materials | system_admin | Auto-mapped, validated |
| PI-MA-112 | Pinnacle Materials | data_steward | Verified via product specs |
| PR-MA-428 | Prism Materials | system_admin | Verified via product specs |
| AT-SO-790 | Atlas Sourcing | system_admin | Verified via product specs |
| CE-LO-713 | Central Logistics | domain_expert | Auto-mapped, validated |
| EL-LO-188 | Elite Logistics | system_admin | Verified via product specs |
| PR-LO-351 | Premier Logistics | domain_expert | Cross-referenced with transactions |
| CO-SO-534 | Core Sourcing | system_admin | Confirmed by domain expert |
| NE-LO-125 | Nexus Logistics | domain_expert | Auto-mapped, validated |
| GL-LO-494 | Global Logistics | domain_expert | Cross-referenced with transactions |
| EL-MA-832 | Elite Materials | domain_expert | Verified via product specs |
| PI-SO-767 | Pinnacle Sourcing | system_admin | Auto-mapped, validated |
| VE-SO-366 | Vertex Sourcing | domain_expert | Historical match confirmed |
| VE-MA-682 | Vertex Materials | system_admin | Confirmed by domain expert |
| NE-MA-849 | Nexus Materials | domain_expert | Verified via product specs |
| PA-LO-674 | Pacific Logistics | system_admin | Verified via product specs |
| PA-SO-568 | Pacific Sourcing | system_admin | Confirmed by domain expert |
| QU-SU-CO-890 | Quantum Supply Co. | data_steward | Auto-mapped, validated |
| PA-SO-999 | Pacific Sourcing | domain_expert | Cross-referenced with transactions |
| PR-LO-393 | Premier Logistics | data_steward | Cross-referenced with transactions |
| PR-SO-270 | Prism Sourcing | system_admin | Historical match confirmed |
| PI-SU-CO-216 | Pinnacle Supply Co. | data_steward | Confirmed by domain expert |
| AT-MA-363 | Atlantic Materials | system_admin | Cross-referenced with transactions |
| AT-SU-CO-808 | Atlas Supply Co. | domain_expert | Auto-mapped, validated |
| NO-SU-CO-498 | Nordic Supply Co. | domain_expert | Auto-mapped, validated |
| AT-SU-CO-945 | Atlas Supply Co. | data_steward | Verified via product specs |
| AT-SU-CO-645 | Atlantic Supply Co. | domain_expert | Auto-mapped, validated |
| ST-MA-342 | Stratos Materials | domain_expert | Verified via product specs |
| HO-LO-948 | Horizon Logistics | system_admin | Historical match confirmed |
| BA-MA-998 | Baltic Materials | domain_expert | Verified via product specs |
| PA-MA-435 | Pacific Materials | system_admin | Confirmed by domain expert |
| ST-LO-136 | Stratos Logistics | domain_expert | Auto-mapped, validated |
| QU-SU-CO-890 | Quantum Supply Co. | domain_expert | Cross-referenced with transactions |
| AP-SU-CO-787 | Apex Supply Co. | system_admin | Confirmed by domain expert |
| PR-LO-862 | Premier Logistics | domain_expert | Auto-mapped, validated |
| QU-SO-261 | Quantum Sourcing | domain_expert | Historical match confirmed |
| AT-SO-226 | Atlantic Sourcing | system_admin | Historical match confirmed |
| PI-SU-CO-998 | Pinnacle Supply Co. | system_admin | Cross-referenced with transactions |
| BA-SO-776 | Baltic Sourcing | data_steward | Historical match confirmed |
| PR-SO-757 | Premier Sourcing | domain_expert | Verified via product specs |
| PR-MA-605 | Prime Materials | data_steward | Auto-mapped, validated |
| CE-SO-204 | Central Sourcing | domain_expert | Historical match confirmed |
| CE-MA-981 | Central Materials | data_steward | Auto-mapped, validated |
| AT-SO-339 | Atlantic Sourcing | domain_expert | Historical match confirmed |
| BA-SO-633 | Baltic Sourcing | data_steward | Verified via product specs |
| VE-LO-693 | Vertex Logistics | data_steward | Cross-referenced with transactions |
| AT-MA-893 | Atlas Materials | system_admin | Verified via product specs |
| NE-SO-476 | Nexus Sourcing | domain_expert | Verified via product specs |
| PR-MA-686 | Prism Materials | system_admin | Historical match confirmed |
| AT-MA-245 | Atlas Materials | system_admin | Historical match confirmed |
| QU-LO-616 | Quantum Logistics | domain_expert | Auto-mapped, validated |
| VE-MA-908 | Vertex Materials | domain_expert | Confirmed by domain expert |
| AT-LO-628 | Atlantic Logistics | domain_expert | Confirmed by domain expert |
| AP-SO-576 | Apex Sourcing | domain_expert | Historical match confirmed |
| AP-SU-CO-722 | Apex Supply Co. | domain_expert | Historical match confirmed |
| AP-SU-CO-814 | Apex Supply Co. | data_steward | Verified via product specs |
| AT-SO-260 | Atlas Sourcing | system_admin | Cross-referenced with transactions |
| VA-LO-248 | Vanguard Logistics | system_admin | Confirmed by domain expert |
| NO-MA-958 | Nordic Materials | data_steward | Cross-referenced with transactions |
| PI-SO-952 | Pinnacle Sourcing | system_admin | Cross-referenced with transactions |
| ME-LO-731 | Meridian Logistics | system_admin | Auto-mapped, validated |
| PI-SU-CO-364 | Pinnacle Supply Co. | data_steward | Historical match confirmed |
| PA-LO-434 | Pacific Logistics | system_admin | Confirmed by domain expert |
| ST-LO-637 | Stellar Logistics | domain_expert | Confirmed by domain expert |
| CO-SU-CO-353 | Core Supply Co. | domain_expert | Verified via product specs |
| ST-MA-703 | Stratos Materials | domain_expert | Confirmed by domain expert |
| NE-SO-394 | Nexus Sourcing | system_admin | Verified via product specs |
| VA-SU-CO-459 | Vanguard Supply Co. | system_admin | Verified via product specs |
| VE-SU-CO-566 | Vertex Supply Co. | system_admin | Historical match confirmed |
| ST-MA-730 | Stellar Materials | domain_expert | Verified via product specs |
| AT-SU-CO-811 | Atlas Supply Co. | data_steward | Cross-referenced with transactions |
| ZE-SU-CO-723 | Zenith Supply Co. | data_steward | Verified via product specs |
| PR-LO-360 | Prism Logistics | data_steward | Historical match confirmed |
| PA-SU-CO-905 | Pacific Supply Co. | system_admin | Auto-mapped, validated |
| PR-MA-161 | Prime Materials | domain_expert | Confirmed by domain expert |
| VA-RE-G-15-665 | Vat Reduced GB 15% | data_steward | Confirmed by domain expert |
| EX-N-0-751 | Excise NL 0% | domain_expert | Auto-mapped, validated |
| EX-D-7-182 | Excise DE 7% | domain_expert | Verified via product specs |
| VA-ST-N-25-114 | Vat Standard NL 25% | system_admin | Historical match confirmed |
| WI-G-5-718 | Withholding GB 5% | data_steward | Verified via product specs |
| VA-RE-N-7-243 | Vat Reduced NL 7% | domain_expert | Verified via product specs |
| CU-DU-C-0-728 | Customs Duty CN 0% | domain_expert | Auto-mapped, validated |
| VA-ST-G-21-683 | Vat Standard GB 21% | data_steward | Historical match confirmed |
| CU-DU-B-15-379 | Customs Duty BR 15% | domain_expert | Auto-mapped, validated |
| VA-ST-D-19-529 | Vat Standard DE 19% | data_steward | Confirmed by domain expert |
| VA-ST-I-0-862 | Vat Standard IN 0% | domain_expert | Confirmed by domain expert |
| CU-DU-G-5-599 | Customs Duty GB 5% | data_steward | Auto-mapped, validated |
| VA-ST-N-20-984 | Vat Standard NL 20% | system_admin | Confirmed by domain expert |
| VA-ST-N-20-275 | Vat Standard NL 20% | domain_expert | Historical match confirmed |
| WI-U-0-465 | Withholding US 0% | data_steward | Verified via product specs |
| VA-ST-D-10-295 | Vat Standard DE 10% | system_admin | Verified via product specs |
| EX-F-0-883 | Excise FR 0% | domain_expert | Auto-mapped, validated |
| VA-RE-G-25-207 | Vat Reduced GB 25% | domain_expert | Historical match confirmed |
| EX-B-10-648 | Excise BR 10% | system_admin | Verified via product specs |
| EX-I-15-456 | Excise IN 15% | system_admin | Verified via product specs |
| WI-B-5-537 | Withholding BR 5% | domain_expert | Auto-mapped, validated |
| VA-RE-B-21-369 | Vat Reduced BR 21% | domain_expert | Confirmed by domain expert |
| VA-ST-B-0-553 | Vat Standard BR 0% | data_steward | Cross-referenced with transactions |
| VA-ST-F-25-272 | Vat Standard FR 25% | data_steward | Confirmed by domain expert |
| VA-RE-C-19-228 | Vat Reduced CN 19% | domain_expert | Historical match confirmed |
| VA-ST-F-19-413 | Vat Standard FR 19% | system_admin | Auto-mapped, validated |
| CU-DU-F-19-568 | Customs Duty FR 19% | domain_expert | Cross-referenced with transactions |
| VA-RE-B-10-727 | Vat Reduced BR 10% | data_steward | Cross-referenced with transactions |
| WI-G-21-298 | Withholding GB 21% | domain_expert | Confirmed by domain expert |
| VA-RE-B-25-739 | Vat Reduced BR 25% | data_steward | Cross-referenced with transactions |
| VA-ST-G-20-932 | Vat Standard GB 20% | data_steward | Verified via product specs |
| CU-DU-I-5-731 | Customs Duty IN 5% | domain_expert | Cross-referenced with transactions |
| CU-DU-D-5-375 | Customs Duty DE 5% | domain_expert | Auto-mapped, validated |
| VA-RE-G-19-221 | Vat Reduced GB 19% | system_admin | Cross-referenced with transactions |
| EX-B-15-715 | Excise BR 15% | data_steward | Verified via product specs |
| VA-RE-F-25-555 | Vat Reduced FR 25% | domain_expert | Cross-referenced with transactions |
| VA-RE-I-5-252 | Vat Reduced IN 5% | system_admin | Historical match confirmed |
| VA-RE-F-25-707 | Vat Reduced FR 25% | system_admin | Historical match confirmed |
| VA-ST-U-10-638 | Vat Standard US 10% | system_admin | Auto-mapped, validated |
| WI-N-7-197 | Withholding NL 7% | domain_expert | Cross-referenced with transactions |
| EX-N-7-638 | Excise NL 7% | system_admin | Verified via product specs |
| EX-U-15-972 | Excise US 15% | domain_expert | Auto-mapped, validated |
| WI-D-25-711 | Withholding DE 25% | system_admin | Confirmed by domain expert |
| WI-U-10-721 | Withholding US 10% | domain_expert | Confirmed by domain expert |
| EX-N-21-396 | Excise NL 21% | system_admin | Auto-mapped, validated |
| CU-DU-B-7-760 | Customs Duty BR 7% | domain_expert | Auto-mapped, validated |
| EX-U-19-672 | Excise US 19% | data_steward | Historical match confirmed |
| VA-RE-G-25-615 | Vat Reduced GB 25% | domain_expert | Historical match confirmed |
| WI-F-19-763 | Withholding FR 19% | system_admin | Verified via product specs |
| WI-F-21-666 | Withholding FR 21% | system_admin | Cross-referenced with transactions |
| VA-RE-B-7-231 | Vat Reduced BR 7% | system_admin | Verified via product specs |
| VA-RE-I-20-892 | Vat Reduced IN 20% | system_admin | Historical match confirmed |
| VA-RE-F-0-158 | Vat Reduced FR 0% | domain_expert | Verified via product specs |
| CU-DU-U-10-283 | Customs Duty US 10% | system_admin | Confirmed by domain expert |
| EX-I-20-615 | Excise IN 20% | system_admin | Historical match confirmed |
| VA-RE-N-19-835 | Vat Reduced NL 19% | system_admin | Historical match confirmed |
| CU-DU-U-15-275 | Customs Duty US 15% | data_steward | Auto-mapped, validated |
| WI-F-5-421 | Withholding FR 5% | domain_expert | Cross-referenced with transactions |
| EX-B-25-579 | Excise BR 25% | system_admin | Auto-mapped, validated |
| EX-N-20-817 | Excise NL 20% | system_admin | Historical match confirmed |
| VA-ST-I-10-511 | Vat Standard IN 10% | domain_expert | Historical match confirmed |
| CU-DU-C-25-424 | Customs Duty CN 25% | domain_expert | Historical match confirmed |
| CU-DU-U-19-893 | Customs Duty US 19% | data_steward | Auto-mapped, validated |
| VA-ST-C-10-748 | Vat Standard CN 10% | system_admin | Verified via product specs |
| CU-DU-D-5-294 | Customs Duty DE 5% | domain_expert | Cross-referenced with transactions |
| EX-D-10-430 | Excise DE 10% | data_steward | Historical match confirmed |
| EX-G-25-188 | Excise GB 25% | data_steward | Verified via product specs |
| CU-DU-I-25-812 | Customs Duty IN 25% | system_admin | Cross-referenced with transactions |
| EX-U-20-144 | Excise US 20% | domain_expert | Historical match confirmed |
| CU-DU-I-21-633 | Customs Duty IN 21% | data_steward | Cross-referenced with transactions |
| CU-DU-B-7-411 | Customs Duty BR 7% | system_admin | Cross-referenced with transactions |
| WI-B-10-184 | Withholding BR 10% | data_steward | Verified via product specs |
| VA-RE-B-19-480 | Vat Reduced BR 19% | data_steward | Verified via product specs |
| VA-ST-N-19-482 | Vat Standard NL 19% | system_admin | Verified via product specs |
| CU-DU-D-0-383 | Customs Duty DE 0% | data_steward | Confirmed by domain expert |
| VA-RE-C-19-648 | Vat Reduced CN 19% | system_admin | Auto-mapped, validated |
| VA-ST-N-5-804 | Vat Standard NL 5% | domain_expert | Historical match confirmed |
| EX-N-19-830 | Excise NL 19% | data_steward | Auto-mapped, validated |
| CU-DU-C-25-616 | Customs Duty CN 25% | data_steward | Cross-referenced with transactions |
| WI-F-5-977 | Withholding FR 5% | system_admin | Confirmed by domain expert |
| VA-ST-F-20-240 | Vat Standard FR 20% | data_steward | Confirmed by domain expert |
| EX-B-19-908 | Excise BR 19% | system_admin | Verified via product specs |
| VA-ST-I-5-735 | Vat Standard IN 5% | data_steward | Cross-referenced with transactions |
| CU-DU-F-15-864 | Customs Duty FR 15% | system_admin | Auto-mapped, validated |
| CU-DU-G-0-297 | Customs Duty GB 0% | system_admin | Auto-mapped, validated |
| EX-C-21-240 | Excise CN 21% | system_admin | Verified via product specs |
| VA-RE-B-10-482 | Vat Reduced BR 10% | domain_expert | Cross-referenced with transactions |
| CU-DU-G-5-181 | Customs Duty GB 5% | data_steward | Verified via product specs |
| CU-DU-C-7-106 | Customs Duty CN 7% | system_admin | Verified via product specs |
| VA-RE-N-20-326 | Vat Reduced NL 20% | system_admin | Confirmed by domain expert |
| CU-DU-D-0-955 | Customs Duty DE 0% | domain_expert | Historical match confirmed |
| VA-ST-G-19-277 | Vat Standard GB 19% | system_admin | Auto-mapped, validated |
| CU-DU-F-7-469 | Customs Duty FR 7% | data_steward | Historical match confirmed |
| VA-ST-I-19-287 | Vat Standard IN 19% | system_admin | Confirmed by domain expert |
| WI-C-20-252 | Withholding CN 20% | system_admin | Cross-referenced with transactions |
| EX-U-7-320 | Excise US 7% | data_steward | Confirmed by domain expert |
| VA-ST-N-5-192 | Vat Standard NL 5% | domain_expert | Auto-mapped, validated |
| VA-RE-C-19-810 | Vat Reduced CN 19% | data_steward | Verified via product specs |
| CU-DU-N-5-217 | Customs Duty NL 5% | system_admin | Verified via product specs |
| EX-G-5-484 | Excise GB 5% | system_admin | Verified via product specs |
| EX-B-19-306 | Excise BR 19% | data_steward | Verified via product specs |
| VA-RE-N-5-825 | Vat Reduced NL 5% | data_steward | Confirmed by domain expert |
| VA-ST-G-19-945 | Vat Standard GB 19% | domain_expert | Auto-mapped, validated |
| EX-N-21-216 | Excise NL 21% | data_steward | Cross-referenced with transactions |
| CU-DU-B-20-301 | Customs Duty BR 20% | domain_expert | Cross-referenced with transactions |
| EX-U-5-517 | Excise US 5% | system_admin | Verified via product specs |
| CU-DU-G-5-714 | Customs Duty GB 5% | data_steward | Verified via product specs |
| VA-ST-N-20-162 | Vat Standard NL 20% | data_steward | Auto-mapped, validated |
| WI-C-0-413 | Withholding CN 0% | domain_expert | Cross-referenced with transactions |
| WI-B-20-331 | Withholding BR 20% | system_admin | Confirmed by domain expert |
| EX-C-21-179 | Excise CN 21% | domain_expert | Cross-referenced with transactions |
| VA-RE-C-10-444 | Vat Reduced CN 10% | data_steward | Confirmed by domain expert |
| CU-DU-G-0-770 | Customs Duty GB 0% | system_admin | Verified via product specs |
| VA-RE-F-10-219 | Vat Reduced FR 10% | domain_expert | Verified via product specs |
| WI-I-10-242 | Withholding IN 10% | system_admin | Cross-referenced with transactions |
| EX-C-20-948 | Excise CN 20% | system_admin | Cross-referenced with transactions |
| VA-RE-N-0-932 | Vat Reduced NL 0% | domain_expert | Historical match confirmed |
| VA-RE-G-15-592 | Vat Reduced GB 15% | data_steward | Cross-referenced with transactions |
| EX-C-25-332 | Excise CN 25% | data_steward | Confirmed by domain expert |
| EX-N-0-354 | Excise NL 0% | system_admin | Auto-mapped, validated |
| VA-RE-N-25-962 | Vat Reduced NL 25% | data_steward | Verified via product specs |
| CU-DU-N-7-394 | Customs Duty NL 7% | domain_expert | Auto-mapped, validated |
| WI-G-15-758 | Withholding GB 15% | domain_expert | Auto-mapped, validated |
| VA-RE-G-0-937 | Vat Reduced GB 0% | system_admin | Cross-referenced with transactions |
| WI-N-20-376 | Withholding NL 20% | domain_expert | Verified via product specs |
| EX-F-19-312 | Excise FR 19% | data_steward | Cross-referenced with transactions |
| WI-I-20-664 | Withholding IN 20% | domain_expert | Historical match confirmed |
| EX-F-21-883 | Excise FR 21% | data_steward | Historical match confirmed |
| CU-DU-N-25-811 | Customs Duty NL 25% | domain_expert | Confirmed by domain expert |
| CU-DU-G-7-636 | Customs Duty GB 7% | domain_expert | Verified via product specs |
| CU-DU-I-5-886 | Customs Duty IN 5% | data_steward | Verified via product specs |
| WI-N-21-538 | Withholding NL 21% | system_admin | Cross-referenced with transactions |
| CU-DU-N-21-524 | Customs Duty NL 21% | system_admin | Verified via product specs |
| WI-N-5-784 | Withholding NL 5% | domain_expert | Historical match confirmed |
| VA-ST-N-19-883 | Vat Standard NL 19% | domain_expert | Confirmed by domain expert |
| CU-DU-N-15-558 | Customs Duty NL 15% | system_admin | Verified via product specs |
| VA-ST-N-20-254 | Vat Standard NL 20% | system_admin | Cross-referenced with transactions |
| EX-N-10-872 | Excise NL 10% | domain_expert | Verified via product specs |
| WI-N-15-362 | Withholding NL 15% | data_steward | Cross-referenced with transactions |
| CU-DU-D-20-742 | Customs Duty DE 20% | domain_expert | Verified via product specs |
| WI-N-21-724 | Withholding NL 21% | domain_expert | Historical match confirmed |
| VA-RE-I-25-366 | Vat Reduced IN 25% | system_admin | Verified via product specs |
| VA-ST-U-15-204 | Vat Standard US 15% | system_admin | Cross-referenced with transactions |
| VA-ST-F-0-740 | Vat Standard FR 0% | domain_expert | Confirmed by domain expert |
| CU-DU-F-25-387 | Customs Duty FR 25% | domain_expert | Verified via product specs |
| VA-RE-I-5-890 | Vat Reduced IN 5% | data_steward | Verified via product specs |
| WI-F-15-675 | Withholding FR 15% | data_steward | Verified via product specs |
| VA-ST-D-7-855 | Vat Standard DE 7% | data_steward | Cross-referenced with transactions |
| VA-ST-C-19-533 | Vat Standard CN 19% | data_steward | Historical match confirmed |

#### 4.3.3 Excluded Mappings

Deprecated mappings (superseded by newer records):

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-1510-A | Invalid Entry 590 | Data quality insufficient |
| NOISE-2768-H | Invalid Entry 829 | Out of scope per business decision |
| NOISE-2323-F | Invalid Entry 722 | Superseded by newer mapping |
| NOISE-3067-E | Invalid Entry 739 | Out of scope per business decision |
| NOISE-6327-G | Invalid Entry 711 | Duplicate detected |
| NOISE-8433-G | Invalid Entry 201 | Duplicate detected |
| NOISE-4522-G | Invalid Entry 562 | Out of scope per business decision |
| NOISE-6553-H | Invalid Entry 508 | Superseded by newer mapping |
| NOISE-2557-F | Invalid Entry 537 | Data quality insufficient |
| NOISE-5176-F | Invalid Entry 256 | Pending validation |
| NOISE-2494-B | Invalid Entry 195 | Superseded by newer mapping |
| NOISE-7105-C | Invalid Entry 669 | Duplicate detected |
| NOISE-6400-B | Invalid Entry 520 | Out of scope per business decision |
| NOISE-7929-A | Invalid Entry 394 | Duplicate detected |
| NOISE-6761-B | Invalid Entry 691 | Superseded by newer mapping |
| NOISE-3535-H | Invalid Entry 329 | Duplicate detected |
| NOISE-7022-B | Invalid Entry 880 | Superseded by newer mapping |
| NOISE-4705-G | Invalid Entry 965 | Pending validation |
| NOISE-1430-E | Invalid Entry 129 | Pending validation |
| NOISE-6062-F | Invalid Entry 459 | Data quality insufficient |
| NOISE-3347-G | Invalid Entry 171 | Out of scope per business decision |
| NOISE-1502-B | Invalid Entry 864 | Out of scope per business decision |
| NOISE-7163-G | Invalid Entry 564 | Pending validation |
| NOISE-7062-E | Invalid Entry 838 | Duplicate detected |
| NOISE-2391-A | Invalid Entry 259 | Superseded by newer mapping |
| NOISE-1815-B | Invalid Entry 378 | Pending validation |
| NOISE-7947-H | Invalid Entry 721 | Out of scope per business decision |
| NOISE-5475-D | Invalid Entry 873 | Pending validation |
| NOISE-6655-G | Invalid Entry 213 | Pending validation |
| NOISE-8972-E | Invalid Entry 146 | Out of scope per business decision |
| NOISE-1897-A | Invalid Entry 309 | Out of scope per business decision |
| NOISE-3248-E | Invalid Entry 396 | Data quality insufficient |
| NOISE-1126-H | Invalid Entry 864 | Data quality insufficient |
| NOISE-3116-G | Invalid Entry 645 | Superseded by newer mapping |
| NOISE-6802-B | Invalid Entry 506 | Pending validation |
| NOISE-1307-H | Invalid Entry 179 | Out of scope per business decision |
| NOISE-8033-G | Invalid Entry 826 | Data quality insufficient |
| NOISE-2887-G | Invalid Entry 121 | Data quality insufficient |
| NOISE-8538-F | Invalid Entry 190 | Pending validation |
| NOISE-4986-G | Invalid Entry 703 | Out of scope per business decision |
| NOISE-2288-G | Invalid Entry 991 | Out of scope per business decision |
| NOISE-6562-D | Invalid Entry 441 | Data quality insufficient |
| NOISE-9363-B | Invalid Entry 643 | Pending validation |
| NOISE-6724-F | Invalid Entry 844 | Duplicate detected |
| NOISE-2684-C | Invalid Entry 362 | Data quality insufficient |
| NOISE-3504-B | Invalid Entry 281 | Duplicate detected |
| NOISE-8354-F | Invalid Entry 984 | Duplicate detected |
| NOISE-8205-B | Invalid Entry 580 | Pending validation |
| NOISE-5961-E | Invalid Entry 705 | Out of scope per business decision |
| NOISE-9312-B | Invalid Entry 417 | Data quality insufficient |
| NOISE-1616-A | Invalid Entry 477 | Out of scope per business decision |
| NOISE-2479-G | Invalid Entry 573 | Duplicate detected |
| NOISE-1672-H | Invalid Entry 929 | Out of scope per business decision |
| NOISE-4084-F | Invalid Entry 719 | Superseded by newer mapping |
| NOISE-3471-A | Invalid Entry 561 | Pending validation |
| NOISE-2381-C | Invalid Entry 140 | Superseded by newer mapping |
| NOISE-8172-H | Invalid Entry 636 | Duplicate detected |
| NOISE-3600-F | Invalid Entry 481 | Out of scope per business decision |
| NOISE-7697-F | Invalid Entry 795 | Duplicate detected |
| NOISE-6482-B | Invalid Entry 437 | Duplicate detected |
| NOISE-7333-E | Invalid Entry 358 | Data quality insufficient |
| NOISE-6461-B | Invalid Entry 696 | Out of scope per business decision |
| NOISE-6082-G | Invalid Entry 232 | Out of scope per business decision |
| NOISE-2388-E | Invalid Entry 672 | Out of scope per business decision |
| NOISE-6381-C | Invalid Entry 786 | Duplicate detected |
| NOISE-7937-F | Invalid Entry 118 | Data quality insufficient |
| NOISE-3953-D | Invalid Entry 449 | Superseded by newer mapping |
| NOISE-4711-C | Invalid Entry 258 | Duplicate detected |
| NOISE-2657-A | Invalid Entry 777 | Superseded by newer mapping |
| NOISE-3147-G | Invalid Entry 257 | Data quality insufficient |
| NOISE-3712-H | Invalid Entry 144 | Duplicate detected |
| NOISE-4891-H | Invalid Entry 725 | Pending validation |
| NOISE-8355-D | Invalid Entry 646 | Out of scope per business decision |
| NOISE-8684-D | Invalid Entry 476 | Pending validation |
| NOISE-8564-E | Invalid Entry 896 | Data quality insufficient |
| NOISE-9641-G | Invalid Entry 265 | Pending validation |
| NOISE-3267-E | Invalid Entry 153 | Data quality insufficient |
| NOISE-2680-B | Invalid Entry 391 | Superseded by newer mapping |
| NOISE-5469-H | Invalid Entry 625 | Data quality insufficient |
| NOISE-2502-D | Invalid Entry 936 | Data quality insufficient |
| NOISE-1436-G | Invalid Entry 154 | Duplicate detected |
| NOISE-7126-D | Invalid Entry 495 | Data quality insufficient |
| NOISE-4678-A | Invalid Entry 426 | Data quality insufficient |
| NOISE-6493-C | Invalid Entry 240 | Duplicate detected |
| NOISE-8740-C | Invalid Entry 877 | Superseded by newer mapping |
| NOISE-1086-B | Invalid Entry 119 | Pending validation |
| NOISE-3449-G | Invalid Entry 213 | Data quality insufficient |
| NOISE-5934-B | Invalid Entry 148 | Pending validation |
| NOISE-8489-B | Invalid Entry 213 | Pending validation |
| NOISE-9782-A | Invalid Entry 747 | Superseded by newer mapping |
| NOISE-4963-C | Invalid Entry 398 | Data quality insufficient |
| NOISE-6780-D | Invalid Entry 684 | Out of scope per business decision |
| NOISE-2402-F | Invalid Entry 169 | Duplicate detected |
| NOISE-9312-A | Invalid Entry 499 | Data quality insufficient |
| NOISE-7338-F | Invalid Entry 359 | Out of scope per business decision |
| NOISE-2106-F | Invalid Entry 346 | Out of scope per business decision |
| NOISE-6447-C | Invalid Entry 145 | Data quality insufficient |
| NOISE-6546-C | Invalid Entry 950 | Superseded by newer mapping |
| NOISE-8840-C | Invalid Entry 930 | Data quality insufficient |
| NOISE-8498-A | Invalid Entry 400 | Pending validation |
| NOISE-4268-A | Invalid Entry 423 | Out of scope per business decision |
| NOISE-7524-H | Invalid Entry 359 | Duplicate detected |
| NOISE-4131-E | Invalid Entry 465 | Data quality insufficient |
| NOISE-6438-E | Invalid Entry 227 | Out of scope per business decision |
| NOISE-7553-H | Invalid Entry 495 | Data quality insufficient |
| NOISE-9129-H | Invalid Entry 476 | Out of scope per business decision |
| NOISE-2353-G | Invalid Entry 180 | Data quality insufficient |
| NOISE-3956-E | Invalid Entry 428 | Pending validation |
| NOISE-6372-E | Invalid Entry 413 | Out of scope per business decision |
| NOISE-7981-C | Invalid Entry 806 | Out of scope per business decision |
| NOISE-8325-A | Invalid Entry 844 | Out of scope per business decision |
| NOISE-8126-E | Invalid Entry 754 | Pending validation |
| NOISE-7655-F | Invalid Entry 625 | Superseded by newer mapping |
| NOISE-3339-H | Invalid Entry 135 | Pending validation |
| NOISE-4866-F | Invalid Entry 470 | Pending validation |
| NOISE-1530-C | Invalid Entry 795 | Duplicate detected |
| NOISE-7095-H | Invalid Entry 881 | Out of scope per business decision |
| NOISE-3255-F | Invalid Entry 507 | Out of scope per business decision |
| NOISE-5566-D | Invalid Entry 216 | Pending validation |
| NOISE-4048-H | Invalid Entry 630 | Data quality insufficient |
| NOISE-2929-E | Invalid Entry 893 | Duplicate detected |
| NOISE-8311-D | Invalid Entry 726 | Duplicate detected |
| NOISE-9047-D | Invalid Entry 225 | Out of scope per business decision |
| NOISE-8406-C | Invalid Entry 830 | Superseded by newer mapping |
| NOISE-6236-F | Invalid Entry 826 | Out of scope per business decision |
| NOISE-9882-E | Invalid Entry 407 | Out of scope per business decision |
| NOISE-3852-F | Invalid Entry 620 | Out of scope per business decision |
| NOISE-4292-C | Invalid Entry 342 | Data quality insufficient |
| NOISE-6912-F | Invalid Entry 578 | Pending validation |
| NOISE-2412-B | Invalid Entry 416 | Superseded by newer mapping |
| NOISE-8842-G | Invalid Entry 887 | Superseded by newer mapping |
| NOISE-2208-C | Invalid Entry 424 | Duplicate detected |
| NOISE-8632-F | Invalid Entry 231 | Duplicate detected |
| NOISE-3981-C | Invalid Entry 543 | Superseded by newer mapping |
| NOISE-3034-C | Invalid Entry 411 | Superseded by newer mapping |
| NOISE-6286-D | Invalid Entry 454 | Pending validation |
| NOISE-2292-E | Invalid Entry 301 | Pending validation |
| NOISE-3050-E | Invalid Entry 729 | Duplicate detected |
| NOISE-9234-C | Invalid Entry 706 | Out of scope per business decision |
| NOISE-3804-F | Invalid Entry 962 | Data quality insufficient |
| NOISE-1464-B | Invalid Entry 146 | Pending validation |
| NOISE-4453-G | Invalid Entry 732 | Data quality insufficient |
| NOISE-9938-E | Invalid Entry 757 | Data quality insufficient |
| NOISE-5012-G | Invalid Entry 404 | Data quality insufficient |
| NOISE-1981-C | Invalid Entry 550 | Out of scope per business decision |
| NOISE-8609-D | Invalid Entry 448 | Pending validation |
| NOISE-6121-F | Invalid Entry 851 | Superseded by newer mapping |
| NOISE-3142-F | Invalid Entry 627 | Out of scope per business decision |
| NOISE-6228-D | Invalid Entry 577 | Data quality insufficient |
| NOISE-8366-D | Invalid Entry 244 | Pending validation |
| NOISE-5754-G | Invalid Entry 984 | Pending validation |
| NOISE-5067-C | Invalid Entry 933 | Data quality insufficient |
| NOISE-6123-D | Invalid Entry 881 | Out of scope per business decision |
| NOISE-9433-H | Invalid Entry 610 | Out of scope per business decision |
| NOISE-1379-B | Invalid Entry 502 | Data quality insufficient |
| NOISE-4944-D | Invalid Entry 697 | Out of scope per business decision |
| NOISE-1828-E | Invalid Entry 606 | Pending validation |
| NOISE-8710-E | Invalid Entry 649 | Pending validation |
| NOISE-8060-C | Invalid Entry 370 | Superseded by newer mapping |
| NOISE-6995-A | Invalid Entry 510 | Out of scope per business decision |
| NOISE-4189-F | Invalid Entry 666 | Superseded by newer mapping |
| NOISE-7329-H | Invalid Entry 882 | Superseded by newer mapping |
| NOISE-2946-C | Invalid Entry 199 | Pending validation |
| NOISE-6555-F | Invalid Entry 873 | Duplicate detected |
| NOISE-9341-G | Invalid Entry 612 | Pending validation |
| NOISE-1637-C | Invalid Entry 830 | Duplicate detected |
| NOISE-9508-H | Invalid Entry 252 | Duplicate detected |
| NOISE-3290-F | Invalid Entry 727 | Duplicate detected |
| NOISE-7438-E | Invalid Entry 707 | Duplicate detected |
| NOISE-9351-H | Invalid Entry 825 | Duplicate detected |
| NOISE-8780-A | Invalid Entry 477 | Pending validation |
| NOISE-2795-G | Invalid Entry 697 | Pending validation |
| NOISE-1436-H | Invalid Entry 371 | Duplicate detected |
| NOISE-4728-A | Invalid Entry 697 | Out of scope per business decision |
| NOISE-9589-G | Invalid Entry 251 | Pending validation |
| NOISE-2800-D | Invalid Entry 119 | Out of scope per business decision |
| NOISE-7861-C | Invalid Entry 522 | Data quality insufficient |
| NOISE-9221-H | Invalid Entry 993 | Out of scope per business decision |
| NOISE-3262-D | Invalid Entry 674 | Duplicate detected |
| NOISE-8837-G | Invalid Entry 421 | Duplicate detected |
| NOISE-9734-F | Invalid Entry 659 | Pending validation |
| NOISE-5331-H | Invalid Entry 296 | Data quality insufficient |
| NOISE-5890-D | Invalid Entry 404 | Data quality insufficient |
| NOISE-4396-H | Invalid Entry 424 | Data quality insufficient |
| NOISE-5480-E | Invalid Entry 224 | Out of scope per business decision |
| NOISE-9899-G | Invalid Entry 504 | Out of scope per business decision |
| NOISE-5758-A | Invalid Entry 394 | Data quality insufficient |
| NOISE-8247-E | Invalid Entry 865 | Superseded by newer mapping |
| NOISE-4310-E | Invalid Entry 675 | Data quality insufficient |
| NOISE-2789-D | Invalid Entry 348 | Duplicate detected |
| NOISE-9700-D | Invalid Entry 753 | Pending validation |
| NOISE-2641-G | Invalid Entry 438 | Data quality insufficient |
| NOISE-3252-A | Invalid Entry 663 | Out of scope per business decision |
| NOISE-8793-H | Invalid Entry 766 | Pending validation |
| NOISE-6262-E | Invalid Entry 761 | Out of scope per business decision |
| NOISE-4804-A | Invalid Entry 279 | Data quality insufficient |
| NOISE-1595-G | Invalid Entry 906 | Superseded by newer mapping |
| NOISE-5742-A | Invalid Entry 109 | Superseded by newer mapping |
| NOISE-2758-F | Invalid Entry 391 | Pending validation |
| NOISE-9901-H | Invalid Entry 237 | Out of scope per business decision |
| NOISE-5470-D | Invalid Entry 928 | Pending validation |
| NOISE-3662-H | Invalid Entry 763 | Out of scope per business decision |
| NOISE-4050-A | Invalid Entry 854 | Pending validation |
| NOISE-4164-C | Invalid Entry 725 | Pending validation |
| NOISE-9442-F | Invalid Entry 188 | Data quality insufficient |
| NOISE-2562-C | Invalid Entry 243 | Data quality insufficient |
| NOISE-5064-A | Invalid Entry 367 | Pending validation |
| NOISE-8319-E | Invalid Entry 437 | Duplicate detected |
| NOISE-1187-E | Invalid Entry 769 | Duplicate detected |
| NOISE-4871-A | Invalid Entry 783 | Pending validation |
| NOISE-6026-C | Invalid Entry 515 | Out of scope per business decision |
| NOISE-6095-B | Invalid Entry 754 | Out of scope per business decision |
| NOISE-4618-D | Invalid Entry 236 | Superseded by newer mapping |
| NOISE-8454-F | Invalid Entry 525 | Out of scope per business decision |
| NOISE-9806-D | Invalid Entry 880 | Data quality insufficient |
| NOISE-2341-H | Invalid Entry 640 | Data quality insufficient |
| NOISE-2838-A | Invalid Entry 948 | Data quality insufficient |
| NOISE-4312-C | Invalid Entry 268 | Data quality insufficient |
| NOISE-8239-B | Invalid Entry 796 | Superseded by newer mapping |
| NOISE-9008-B | Invalid Entry 622 | Duplicate detected |
| NOISE-8429-C | Invalid Entry 625 | Data quality insufficient |
| NOISE-1945-H | Invalid Entry 788 | Pending validation |
| NOISE-1356-G | Invalid Entry 360 | Pending validation |
| NOISE-4570-B | Invalid Entry 146 | Data quality insufficient |
| NOISE-2044-A | Invalid Entry 170 | Duplicate detected |
| NOISE-5703-G | Invalid Entry 284 | Data quality insufficient |
| NOISE-7887-F | Invalid Entry 491 | Pending validation |
| NOISE-7154-B | Invalid Entry 799 | Data quality insufficient |
| NOISE-6697-B | Invalid Entry 282 | Out of scope per business decision |
| NOISE-9664-C | Invalid Entry 845 | Superseded by newer mapping |
| NOISE-1372-E | Invalid Entry 574 | Out of scope per business decision |
| NOISE-9715-G | Invalid Entry 943 | Superseded by newer mapping |
| NOISE-8546-F | Invalid Entry 258 | Out of scope per business decision |
| NOISE-2848-A | Invalid Entry 928 | Out of scope per business decision |
| NOISE-1256-D | Invalid Entry 311 | Out of scope per business decision |
| NOISE-1550-H | Invalid Entry 712 | Superseded by newer mapping |
| NOISE-1724-G | Invalid Entry 549 | Out of scope per business decision |
| NOISE-4559-A | Invalid Entry 243 | Out of scope per business decision |
| NOISE-4836-F | Invalid Entry 691 | Pending validation |
| NOISE-6253-D | Invalid Entry 409 | Duplicate detected |
| NOISE-9540-D | Invalid Entry 523 | Superseded by newer mapping |
| NOISE-1998-C | Invalid Entry 741 | Superseded by newer mapping |
| NOISE-9120-A | Invalid Entry 452 | Duplicate detected |
| NOISE-6222-G | Invalid Entry 518 | Superseded by newer mapping |
| NOISE-7167-C | Invalid Entry 872 | Superseded by newer mapping |
| NOISE-4948-D | Invalid Entry 407 | Out of scope per business decision |
| NOISE-1944-G | Invalid Entry 526 | Pending validation |
| NOISE-3196-G | Invalid Entry 348 | Out of scope per business decision |
| NOISE-6411-B | Invalid Entry 560 | Data quality insufficient |
| NOISE-9775-D | Invalid Entry 152 | Data quality insufficient |
| NOISE-1647-B | Invalid Entry 292 | Data quality insufficient |
| NOISE-4555-H | Invalid Entry 313 | Data quality insufficient |
| NOISE-1251-D | Invalid Entry 294 | Pending validation |
| NOISE-8846-D | Invalid Entry 812 | Out of scope per business decision |
| NOISE-4350-G | Invalid Entry 345 | Superseded by newer mapping |
| NOISE-5637-G | Invalid Entry 577 | Data quality insufficient |
| NOISE-6886-E | Invalid Entry 367 | Data quality insufficient |
| NOISE-9147-H | Invalid Entry 200 | Superseded by newer mapping |
| NOISE-4328-F | Invalid Entry 420 | Pending validation |
| NOISE-4625-C | Invalid Entry 116 | Superseded by newer mapping |
| NOISE-7841-E | Invalid Entry 256 | Pending validation |
| NOISE-4768-G | Invalid Entry 683 | Duplicate detected |
| NOISE-6530-E | Invalid Entry 881 | Out of scope per business decision |
| NOISE-9037-H | Invalid Entry 272 | Duplicate detected |
| NOISE-3293-H | Invalid Entry 288 | Out of scope per business decision |
| NOISE-1962-A | Invalid Entry 959 | Superseded by newer mapping |
| NOISE-1794-A | Invalid Entry 522 | Pending validation |
| NOISE-4791-B | Invalid Entry 824 | Duplicate detected |
| NOISE-4583-H | Invalid Entry 482 | Pending validation |
| NOISE-8916-H | Invalid Entry 116 | Duplicate detected |
| NOISE-7739-A | Invalid Entry 117 | Superseded by newer mapping |
| NOISE-5501-E | Invalid Entry 117 | Out of scope per business decision |
| NOISE-8054-C | Invalid Entry 209 | Out of scope per business decision |
| NOISE-3439-D | Invalid Entry 296 | Pending validation |
| NOISE-5135-F | Invalid Entry 373 | Duplicate detected |
| NOISE-7112-G | Invalid Entry 570 | Duplicate detected |
| NOISE-4700-E | Invalid Entry 800 | Data quality insufficient |
| NOISE-1519-B | Invalid Entry 515 | Data quality insufficient |
| NOISE-8798-A | Invalid Entry 752 | Pending validation |
| NOISE-3807-B | Invalid Entry 611 | Pending validation |
| NOISE-6427-B | Invalid Entry 640 | Duplicate detected |
| NOISE-4463-H | Invalid Entry 377 | Duplicate detected |
| NOISE-5593-A | Invalid Entry 283 | Duplicate detected |
| NOISE-4394-C | Invalid Entry 870 | Pending validation |
| NOISE-5903-C | Invalid Entry 677 | Pending validation |
| NOISE-7375-F | Invalid Entry 493 | Pending validation |
| NOISE-2284-F | Invalid Entry 154 | Duplicate detected |
| NOISE-4803-B | Invalid Entry 448 | Out of scope per business decision |
| NOISE-7499-F | Invalid Entry 130 | Out of scope per business decision |
| NOISE-9038-D | Invalid Entry 464 | Out of scope per business decision |
| NOISE-8075-C | Invalid Entry 796 | Pending validation |

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
3. Execute rollback script: `./scripts/rollback_full.sh --timestamp=20230424_000000`
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
| Technical Lead | Lisa Rodriguez (Quality Assurance) | lisa@company.com | +1-555-0102 |
| Business Owner | Maria Garcia (Supply Chain) | maria@company.com | +1-555-0103 |
| Data Steward | John Smith (IT Infrastructure) | john@company.com | +1-555-0104 |

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
