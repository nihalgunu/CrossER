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
| Total entities assessed | 254 | Completed |
| Successfully mapped | 50 | Verified |
| Excluded from scope | 15 | Documented |
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

#### 4.3.3 Excluded Mappings

The following mappings were identified but NOT migrated due to data quality issues:

| Source Code | Target Code | Reason for Exclusion |
|-------------|-------------|---------------------|
| NOISE-2824-A | Invalid Entry 859 | Superseded by newer mapping |
| NOISE-4657-C | Invalid Entry 854 | Data quality insufficient |
| NOISE-9935-B | Invalid Entry 704 | Pending validation |
| NOISE-1488-B | Invalid Entry 323 | Out of scope per business decision |
| NOISE-1434-D | Invalid Entry 833 | Pending validation |
| NOISE-4611-H | Invalid Entry 703 | Out of scope per business decision |
| NOISE-3615-G | Invalid Entry 448 | Superseded by newer mapping |
| NOISE-4527-F | Invalid Entry 204 | Out of scope per business decision |
| NOISE-2584-F | Invalid Entry 967 | Out of scope per business decision |
| NOISE-5333-A | Invalid Entry 847 | Superseded by newer mapping |
| NOISE-3045-G | Invalid Entry 180 | Out of scope per business decision |
| NOISE-6925-D | Invalid Entry 821 | Data quality insufficient |
| NOISE-4733-E | Invalid Entry 181 | Duplicate detected |
| NOISE-7227-E | Invalid Entry 564 | Superseded by newer mapping |
| NOISE-7065-F | Invalid Entry 314 | Duplicate detected |

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
