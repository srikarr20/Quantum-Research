# Runtime Audit Findings

## Confirmed

- Runtime preserves PrimitiveResult structures.
- Runtime preserves PubResult structures.
- Runtime preserves DataBin structures.
- Runtime serializes and reconstructs result containers.
- Runtime transports BitArray measurement data.

## Observed Differences from Aer

- Aer explicitly exposes pershot retention.
- Runtime source contains no explicit pershot references.
- Runtime introduces a transport and serialization layer.

## QMVA Interpretation

Runtime appears to preserve measurement-result
structures while introducing additional
serialization boundaries between execution
and user visibility.

