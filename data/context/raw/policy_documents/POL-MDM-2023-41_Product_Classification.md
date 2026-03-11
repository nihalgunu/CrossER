# POL-MDM-2024-24: Product Classification and Entity Resolution Policy

**Effective Date:** January 13, 2023
**Supersedes:** POL-MDM-2021-45
**Classification:** Internal Use Only
**Document Owner:** Master Data Governance Office
**Review Cycle:** Annual

---

## 1. Purpose and Scope

### 1.1 Purpose

This policy establishes the standards, procedures, and governance framework for
product classification and entity resolution across all enterprise resource
planning (ERP) systems operated by Company and its subsidiaries. The policy
ensures consistent treatment of master data entities to support accurate
financial reporting, regulatory compliance, and operational efficiency.

### 1.2 Scope

This policy applies to:

a) All product master data records across ERP_ALPHA, ERP_BETA, ERP_GAMMA,
   ERP_DELTA, and any legacy systems including LEGACY_SIGMA;

b) All personnel responsible for creating, maintaining, or utilizing product
   master data, including but not limited to data stewards, system
   administrators, procurement specialists, and finance personnel;

c) All automated systems and integration processes that create, modify, or
   consume product master data;

d) All geographic regions and business units, with specific regional
   variations documented in Appendix A.

### 1.3 Exclusions

This policy does not apply to:
- Transactional data (e.g., individual purchase orders, invoices)
- Customer master data (governed by POL-CRM-2023-01)
- Employee master data (governed by POL-HR-2023-05)

---

## 2. Definitions

For purposes of this policy, the following definitions apply:

**2.1 "Entity"** means a discrete record in any enterprise system that
represents a real-world product, supplier, legal entity, or tax classification.

**2.2 "Entity Resolution"** means the process of determining whether two or
more records across systems represent the same real-world entity.

**2.3 "Classification Code"** means the tariff, commodity, or regulatory code
assigned to a product for customs, tax, or compliance purposes.

**2.4 "Master Record"** means the authoritative version of an entity record
maintained in the system of record (typically ERP_ALPHA).

**2.5 "Concentration"** means the percentage by weight of the active ingredient
or primary compound in a product formulation.

**2.6 "Grade"** means the quality designation assigned to a product, including
but not limited to "Food Grade," "Technical Grade," "Pharma Grade," and
standard grade designations (Grade A, Grade B, etc.).

**2.7 "Dextrose Equivalent (DE)"** means the measure of reducing sugars in a
starch hydrolysate, expressed as a percentage relative to pure dextrose.

---

## 3. Classification Standards

### 3.1 Concentration-Based Differentiation

**3.1.1** Products containing the same base compound but with different
concentration values SHALL be classified as DISTINCT entities for purposes
of:
- Regulatory compliance and reporting
- Pricing and commercial terms
- Inventory management and tracking
- Quality control and specifications

**3.1.2** The following concentration thresholds define distinct products:
- Difference of 5 percentage points or greater: ALWAYS distinct
- Difference of 1-4 percentage points: Subject to business review
- Difference of less than 1 percentage point: May be consolidated

**Example:** Citric Acid 70% and Citric Acid 99.5% are DISTINCT products
requiring separate master data records, separate pricing, and separate
inventory tracking.

### 3.2 Grade-Based Differentiation

**3.2.1** Products with different grade designations SHALL be maintained as
separate entities regardless of other attribute similarities.

**3.2.2** The following grade designations define distinct products:
- Food Grade vs. Technical Grade
- Pharma Grade vs. Food Grade
- Grade A vs. Grade B vs. Grade C
- Premium vs. Standard

**3.2.3** Regional grade designations (e.g., "Lebensmittelqualität" in German)
SHALL be mapped to their English equivalents but maintained as the same
underlying product when specifications match.

### 3.3 DE-Based Classification (Starch Products)

**3.3.1** For maltodextrin and other starch hydrolysates, the Dextrose
Equivalent (DE) value determines regulatory classification:

| DE Range | Classification | Tariff Code |
|----------|---------------|-------------|
| DE < 20 | Maltodextrin | CN 1702.30 |
| DE >= 20 | Glucose Syrup | CN 1702.90 |

**3.3.2** Products with different DE values SHALL be treated as distinct
entities even when other attributes match.

**3.3.3** DE values shall be verified against Certificate of Analysis (CoA)
documentation before entity resolution decisions.


### 3.4 Specific Classification Rules

The following rules have been established by the Data Governance Council
and are binding for all entity resolution decisions:


**Rule 3.4.1 (Classification):**

*Condition:* When maltodextrin product has dextrose_equivalent > 20

*Action:* Classify under CN 1702.90, not CN 1702.30

*Rationale:* EU Combined Nomenclature distinguishes maltodextrin by DE threshold. Products above DE 20 fall under a different tariff heading, affecting duty rates.


**Rule 3.4.2 (Classification):**

*Condition:* When glucose syrup has fructose content > 50%

*Action:* Reclassify as high-fructose corn syrup under HTS 1702.60

*Rationale:* US customs distinguishes glucose syrups by fructose content. High fructose content changes tariff classification.


**Rule 3.4.3 (Classification):**

*Condition:* When protein content >= 90% by dry weight

*Action:* Classify as isolate (CN 3504.00.90), not concentrate (CN 3504.00.10)

*Rationale:* Protein products are classified differently based on concentration. Isolates require different labeling and documentation.


**Rule 3.4.4 (Regional Override):**

*Condition:* Products with multiple concentration variants sold in Germany

*Action:* Maintain separate master data records for each concentration variant even if global system consolidates them

*Rationale:* German subsidiary requires separate records for VAT documentation purposes. Each concentration variant must have distinct invoicing codes.


**Rule 3.4.5 (Regional Override):**

*Condition:* Food-grade vs technical-grade variants of same chemical compound

*Action:* Treat as separate products regardless of chemical equivalence

*Rationale:* FDA regulations require separate tracking of food-grade and technical-grade materials. Cannot be consolidated in master data.


**Rule 3.4.6 (Regional Override):**

*Condition:* Supplier with both import license and local production capability

*Action:* Create separate supplier records for import and local supply chains

*Rationale:* Brazilian ANVISA regulations require separate documentation pathways for imported vs domestically produced materials.


**Rule 3.4.7 (Temporal Validity):**

*Condition:* Product formulation changed after specified date

*Action:* Products with same code before and after formulation change date should not be matched

*Rationale:* Regulatory changes in 2024 required reformulation of certain products. Pre-2024 and post-2024 versions are legally distinct products.


**Rule 3.4.8 (Temporal Validity):**

*Condition:* Tax codes created before Brexit transition period end

*Action:* Pre-2021 EU VAT codes should not match post-2021 UK VAT codes even if rates are identical

*Rationale:* Post-Brexit, UK VAT codes are legally separate from EU VAT system. Historical EU codes should not be linked to current UK codes.


**Rule 3.4.9 (Temporal Validity):**

*Condition:* Supplier qualification expired without renewal

*Action:* Expired supplier records should not match renewed supplier records with same company

*Rationale:* Quality management requires treating re-qualified suppliers as new entities for audit trail purposes.


**Rule 3.4.10 (Threshold Based):**

*Condition:* Concentration difference > 5 percentage points

*Action:* Treat as different products regardless of other attribute similarity

*Rationale:* Application specifications differ significantly at different concentrations. 25% vs 30% solutions have different use cases.


**Rule 3.4.11 (Threshold Based):**

*Condition:* Grade designation differs (e.g., Grade A vs Grade B, Food vs Technical)

*Action:* Never merge products with different grade designations

*Rationale:* Grade designations indicate different quality levels and regulatory requirements. Cross-grade matching is always incorrect.


**Rule 3.4.12 (Regulatory Compliance):**

*Condition:* Entity has organic or non-GMO certification

*Action:* Do not merge with non-certified equivalents even if otherwise identical

*Rationale:* Certification chain of custody requirements mandate separate tracking of certified and non-certified materials.


**Rule 3.4.13 (Regulatory Compliance):**

*Condition:* Product classified as dual-use under export control regulations

*Action:* Maintain separate records for controlled and uncontrolled variants

*Rationale:* Export control compliance requires separate documentation for dual-use chemicals.


**Rule 3.4.14 (Regulatory Compliance):**

*Condition:* Entity associated with sanctioned jurisdiction or ownership

*Action:* Do not merge with unsanctioned entities even if representing same legal person

*Rationale:* Sanctions compliance requires maintaining separate records to track pre-sanction vs post-sanction relationships.


---

## 4. Entity Resolution Procedures

### 4.1 General Principles

**4.1.1** Entity resolution decisions SHALL be based on the following
hierarchy of evidence (in order of priority):

1. Official migration mapping tables maintained by IT
2. Certificate of Analysis or product specification match
3. Historical transaction correlation analysis
4. Expert review by qualified data steward

**4.1.2** String similarity alone is NOT sufficient basis for entity
resolution. Two records with highly similar names may represent distinct
products due to specification differences.

**4.1.3** Two records with dissimilar names may represent the same product
due to:
- Regional naming conventions (German vs. English)
- Legacy coding conventions
- Abbreviation practices by system

### 4.2 Cross-System Mapping

**4.2.1** When resolving entities across systems, the following system-
specific considerations apply:

| System | Naming Convention | Code Format | Notes |
|--------|------------------|-------------|-------|
| ERP_ALPHA | Formal English | PRD-XXXX | System of record |
| ERP_BETA | German formal | EU-XXXX | Translate to English |
| ERP_GAMMA | Abbreviated | ACQ-XXX-XXX | Use mapping table |
| ERP_DELTA | Informal | REG-XXXX | Verify specifications |
| LEGACY_SIGMA | Cryptic codes | SIG-XX-XXX-XXXX | MUST use migration table |

**4.2.2** LEGACY_SIGMA codes are NOT interpretable from the code structure.
Resolution MUST reference the official SIGMA_DECOMMISSION migration mapping
maintained by IT Infrastructure.

### 4.3 Decision Authority

| Decision Type | Authority Level | Documentation |
|--------------|-----------------|---------------|
| Automated match (exact spec) | System | Audit log |
| Automated match (fuzzy) | Data Steward review | Sign-off required |
| Manual match | Domain Expert | Business justification |
| Exception/Override | Data Governance Lead | Approval workflow |


### 4.4 Authoritative Mapping Reference

The following cross-system mappings are documented and approved. These
mappings take precedence over any automated matching algorithms:

| Source System | Source Code | Target System | Target Code | Status |
|--------------|-------------|---------------|-------------|--------|
| LEGACY_SIGMA | SIG-30-PVA-ZMF8 | ERP_ALPHA | Sodium Chloride 70% Grade B | Approved |
| ERP_GAMMA | SO-CH-70-GR-B-821 | ERP_ALPHA | Sodium Chloride 70% Grade B | Approved |
| ERP_DELTA | sodium chloride 70% standard | ERP_ALPHA | Sodium Chloride 70% Grade B | Approved |
| LEGACY_SIGMA | SIG-44-SRN-1MKF | ERP_ALPHA | Fructose Grade A | Approved |
| ERP_GAMMA | FR-GR-A-600 | ERP_ALPHA | Fructose Grade A | Approved |
| LEGACY_SIGMA | SIG-41-SWO-23GD | ERP_ALPHA | Resistant Starch | Approved |
| ERP_GAMMA | RE-ST-223 | ERP_ALPHA | Resistant Starch | Approved |
| ERP_BETA | Resistente Stärke | ERP_ALPHA | Resistant Starch | Approved |
| ERP_DELTA | resistant starch | ERP_ALPHA | Resistant Starch | Approved |
| LEGACY_SIGMA | SIG-79-HZP-CLBR | ERP_ALPHA | Casein 25% Pharma Grade | Approved |
| ERP_BETA | Kasein 25% Pharmazeutisch rein | ERP_ALPHA | Casein 25% Pharma Grade | Approved |
| ERP_DELTA | casein 25% pharma grade | ERP_ALPHA | Casein 25% Pharma Grade | Approved |
| LEGACY_SIGMA | SIG-29-CYR-T4UF | ERP_ALPHA | Ascorbic Acid | Approved |
| ERP_GAMMA | AS-AC-782 | ERP_ALPHA | Ascorbic Acid | Approved |
| ERP_BETA | Ascorbic Acid | ERP_ALPHA | Ascorbic Acid | Approved |
| ERP_DELTA | ascorbic acid | ERP_ALPHA | Ascorbic Acid | Approved |
| ERP_DELTA | isoglucose 70% | ERP_ALPHA | Isoglucose 70% | Approved |
| ERP_DELTA | pea protein 50% | ERP_ALPHA | Pea Protein 50% | Approved |
| LEGACY_SIGMA | SIG-16-QDM-JLQM | ERP_ALPHA | Sunflower Oil 98% Premium | Approved |
| ERP_GAMMA | SU-OI-98-PR-692 | ERP_ALPHA | Sunflower Oil 98% Premium | Approved |

*Note: For complete mapping tables, refer to the IT-maintained migration
documentation or query the entity resolution service API.*


---

## 5. Regional Variations

### 5.1 European Union (ERP_BETA)

**5.1.1** German subsidiary entities must maintain separate records for
VAT documentation purposes when:
- Entity operates under German Handelsregister registration
- Products require German-language labeling for market access
- Regulatory filings are submitted to German authorities

**5.1.2** German/English name equivalents SHALL be treated as the same
product when specifications match:

| German Name | English Equivalent |
|-------------|-------------------|
| Zitronensäure | Citric Acid |
| Maltodextrin-Pulver | Maltodextrin |
| Resistente Stärke | Resistant Starch |
| Natriumchlorid | Sodium Chloride |

### 5.2 United States

**5.2.1** FDA-regulated products require separate tracking for:
- Food Grade vs. non-food applications
- Products requiring GRAS (Generally Recognized as Safe) status
- Products with specific FDA facility registration requirements

### 5.3 Brazil

**5.3.1** ANVISA-regulated products require:
- Separate master records for import vs. domestic supply chain
- Portuguese-language product descriptions for regulatory filings

---

## 6. Compliance and Enforcement

### 6.1 Monitoring

The Data Governance Office shall conduct quarterly audits of entity
resolution decisions to ensure compliance with this policy. Audit findings
shall be reported to the Data Governance Council.

### 6.2 Non-Compliance

Failure to comply with this policy may result in:
- Data quality exceptions flagged in system
- Escalation to management
- Required remediation training
- In severe cases, restriction of system access

### 6.3 Exception Process

Exceptions to this policy require:
1. Written business justification
2. Risk assessment by Compliance
3. Approval by Data Governance Lead
4. Documentation in exception register

---

## 7. Related Policies and Procedures

- POL-DQ-2023-01: Data Quality Standards
- POL-INT-2023-05: System Integration Standards
- POL-REG-2023-02: Regulatory Compliance Framework
- PROC-MDM-001: Master Data Creation Procedure
- PROC-MDM-002: Entity Resolution Procedure
- PROC-MDM-003: Data Stewardship Guidelines

---

## Appendix A: Regional Regulatory Requirements

[Detailed regional requirements omitted for brevity]

## Appendix B: Classification Code Reference

[Full tariff code mapping omitted for brevity]

## Appendix C: Approval Signatures

| Role | Name | Date | Signature |
|------|------|------|-----------|
| VP Data Governance | [Name] | [Date] | [Approved] |
| Chief Compliance Officer | [Name] | [Date] | [Approved] |
| IT Director | [Name] | [Date] | [Approved] |

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2022-01-15 | Data Governance | Initial publication |
| 1.1 | 2022-06-01 | Compliance | Added regional variations |
| 2.0 | 2023-01-01 | Data Governance | Major revision |
| 2.1 | 2023-06-15 | Data Governance | Updated DE thresholds |
| 2.2 | 2023-09-01 | Data Governance | Added LEGACY_SIGMA section |

---

*This document is maintained by the Master Data Governance Office.
For questions or clarifications, contact mdm-governance@company.com.*

*Document ID: {policy_num} | Classification: Internal Use Only*
