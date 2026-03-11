# Gamma Integration 2022 - Migration Notes

> **Last Updated:** 2022-09-28
> **Owner:** IT Operations

## Migration Architecture

This migration uses a **multi-hop staging approach**:

```
ERP_GAMMA --> Internal Codes --> Master Groups --> ERP_ALPHA
```

**IMPORTANT**: Direct source-to-target mappings DO NOT exist in this migration.
All entities flow through the internal code layer.

### Staging Layer Design

1. **Source Extraction**: Entities extracted from ERP_GAMMA
2. **Internal Code Assignment**: Each entity receives IC-XXXX code
3. **Master Group Consolidation**: Similar entities grouped into MG-XXXX
4. **Target Assignment**: MDM registry determines final target

### Code Lookup Process

To find the target entity for a ERP_GAMMA entity:
1. Look up the source code in the runbook (source -> IC-XXXX)
2. Look up the IC-XXXX in the consolidation spreadsheet (IC -> MG)
3. Look up the MG-XXXX in the MDM registry (MG -> Target)

## Internal Code Batches

Entities were staged in batches. Each batch has a specific code range:

| Batch | Code Range | Source System | Staging Date |
|-------|-----------|---------------|--------------|
| Batch 1 | IC-1000 to IC-1999 | ERP_GAMMA | 2022-03-15 |
| Batch 2 | IC-2000 to IC-2999 | ERP_GAMMA | 2022-04-01 |
| Batch 3 | IC-3000 to IC-3999 | ERP_GAMMA | 2022-05-15 |
| Batch 4 | IC-4000 to IC-4999 | ERP_GAMMA | 2022-06-01 |


## Sample Code Chains

The following examples show the multi-hop structure for ERP_GAMMA entities.
**Note:** These are structural examples only. For actual lookups, use
the appropriate source documents.


### Example 1: 2-Hop Chain

```
Source Entity → BC-1002 → MR-1003 → [Target]
```

**Hop Details:**
- Hop 1: BC-1002 (assigned by Product Management)
- Hop 2: MR-1003 (assigned by Data Governance)

**Target Resolution**: Look up final IC code in MDM registry

### Example 2: 1-Hop Chain

```
Source Entity → BC-1007 → [Target]
```

**Hop Details:**
- Hop 1: BC-1007 (assigned by Supply Chain)

**Target Resolution**: Look up final IC code in MDM registry

### Example 3: 2-Hop Chain

```
Source Entity → IC-1011 → XR-1012 → [Target]
```

**Hop Details:**
- Hop 1: IC-1011 (assigned by Product Management)
- Hop 2: XR-1012 (assigned by Supply Chain)

**Target Resolution**: Look up final IC code in MDM registry

### Example 4: 2-Hop Chain

```
Source Entity → IC-1025 → XR-1026 → [Target]
```

**Hop Details:**
- Hop 1: IC-1025 (assigned by Operations)
- Hop 2: XR-1026 (assigned by Supply Chain)

**Target Resolution**: Look up final IC code in MDM registry

### Example 5: 3-Hop Chain

```
Source Entity → TC-1036 → PC-1037 → XR-1038 → [Target]
```

**Hop Details:**
- Hop 1: TC-1036 (assigned by Data Governance)
- Hop 2: PC-1037 (assigned by Compliance)
- Hop 3: XR-1038 (assigned by IT Infrastructure)

**Target Resolution**: Look up final IC code in MDM registry

## Master Group Rules

Master groups (MG-XXXX) consolidate multiple internal codes:

- **Single Source**: IC codes from same source entity → same MG
- **Multi Source**: IC codes from equivalent entities across systems → same MG
- **Target Resolution**: MG code determines single target entity

### Master Group Lookup

The master group for an internal code can be found in:
- Consolidation spreadsheet (CONSOL_MASTER_*.csv)
- MDM Registry API (`GET /api/v1/groups/{ic_code}`)

## Known Issues

1. **Gap in IC-3500 to IC-3600**: These codes were reserved but not used.
   If you encounter them, check the exception log.

2. **Duplicate MG assignments**: Some IC codes appear in multiple MGs
   due to product splits. Use the most recent assignment.

3. **Circular references**: Some XR- codes point to each other.
   Break the cycle by using the lower-numbered code as canonical.

## Related Pages

- [Data Quality Standards](/wiki/data-quality)
- [Internal Code Registry](/wiki/ic-registry)
- [Entity Lifecycle Management](/wiki/entity-lifecycle)

---

*This page is maintained by IT Operations.*
