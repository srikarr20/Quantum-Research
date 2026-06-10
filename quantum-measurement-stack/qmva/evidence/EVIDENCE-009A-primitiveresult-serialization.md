# EVIDENCE-009A

## Title

PrimitiveResult Serialization

## Observation

IBM Runtime explicitly serializes
PrimitiveResult objects.

Observed:

qiskit_ibm_runtime/utils/json.py

    PrimitiveResult

## Finding

PrimitiveResult objects are transformed
into transportable formats before delivery
to users.

## QMVA Classification

Serialization Boundary

