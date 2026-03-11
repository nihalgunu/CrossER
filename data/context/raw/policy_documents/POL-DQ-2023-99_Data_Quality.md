# POL-DQ-2022-46: Enterprise Data Quality Policy

**Effective Date:** January 1, 2023
**Classification:** Internal Use Only
**Document Owner:** Data Quality Management Office

---

## 1. Purpose

This policy establishes data quality standards and governance procedures
for all enterprise master data, with particular emphasis on product,
supplier, legal entity, and tax code master data.

## 2. Data Quality Dimensions

### 2.1 Completeness

All mandatory attributes must be populated according to system requirements.
Completeness thresholds by system:

| System | Required Completeness |
|--------|----------------------|
| ERP_ALPHA | 95% |
| ERP_BETA | 90% |
| ERP_GAMMA | 60% |
| ERP_DELTA | 50% |

### 2.2 Accuracy

Data values must correctly represent the real-world entity. Accuracy
is verified through:
- Source document validation
- Specification matching
- Expert review

### 2.3 Consistency

Data must be consistent across systems. Inconsistencies require
resolution through the entity resolution process.

### 2.4 Timeliness

Data must be updated within 24 hours of receiving authoritative changes.

---

## 3. Quality Monitoring

[Standard monitoring procedures omitted for brevity]

---

## 4. Issue Resolution

[Standard issue resolution procedures omitted for brevity]

---

*Document ID: POL-DQ-2022-46*
