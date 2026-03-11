# Classification Guidelines: Proteins

> **Last Updated:** 2024-01-10
> **Owner:** Compliance Team

## Classification Logic

Products in the proteins category follow these classification rules.
**Note:** Classification determines the target entity assignment.

### Concentration-Based Assignment

The internal code registry uses concentration to determine target assignment:

| Concentration Range | Internal Code Suffix | Target Category |
|--------------------|---------------------|-----------------|
| 0-25% | -LOW | Diluted products line |
| 26-50% | -MID | Standard products line |
| 51-75% | -STD | Concentrated products line |
| 76-100% | -PUR | Pure products line |

**Example:** An entity with internal code `IC-1234-STD` maps to the
concentrated products line in the target system.

### Grade-Based Differentiation

Internal codes also encode grade information:

| Grade | Code Pattern | Target Assignment |
|-------|-------------|-------------------|
| Food Grade | Contains "FG" | Food-grade product entities |
| Technical Grade | Contains "TG" | Technical-grade product entities |
| Pharma Grade | Contains "PG" | Pharmaceutical product entities |


### Inference Rules

The following rules are used when explicit mappings don't exist:

1. **Category Inheritance**: If an internal code belongs to master group MG-XXXX,
   all entities in that group share the same target category.

2. **Temporal Rules**: Entities staged before 2023-01-01 use legacy target
   assignments. Entities staged after use the current MDM registry.

3. **Regional Override**: Internal codes with region suffixes (-DE, -US, -CN)
   override the default target and map to regional variants.

### Cross-Reference Resolution

When an internal code is marked as XR- (cross-reference):
1. Look up the canonical internal code in the alias table
2. Use the canonical code for target assignment
3. The XR- code is considered deprecated after resolution


## Important Exceptions

**Grandfathered Entities**: Entities created before 2021-06-01 may not follow
current naming conventions. These require lookup in the legacy mapping table.

**Merged Entities**: If two internal codes resolve to the same target, the
earlier code is considered canonical and the later is marked as alias.

## Related Pages

- [Data Quality Standards](/wiki/data-quality)
- [System Integration Guide](/wiki/integration-guide)
- [Internal Code Registry](/wiki/ic-registry)

---

*For questions about classification, contact compliance@company.com*
