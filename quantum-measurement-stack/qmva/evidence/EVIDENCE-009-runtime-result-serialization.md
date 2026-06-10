# EVIDENCE-009

## Title

Runtime Result Serialization Boundary

## Observation

IBM Runtime explicitly serializes and
deserializes primitive result containers.

Observed objects:

- PrimitiveResult
- PubResult
- SamplerPubResult
- EstimatorPubResult
- DataBin

Observed locations:

qiskit_ibm_runtime/utils/json.py

Evidence:

Serialization handlers exist for:

- PrimitiveResult
- PubResult
- SamplerPubResult
- EstimatorPubResult
- DataBin

Deserialization handlers exist for:

- PrimitiveResult(...)
- PubResult(...)
- SamplerPubResult(...)
- EstimatorPubResult(...)
- DataBin(...)

## Finding

Runtime introduces an additional boundary:

    Simulator Result
          ↓
    Runtime Container
          ↓
    JSON Serialization
          ↓
    Cloud Transport
          ↓
    User Result

## QMVA Interpretation

Information is not transferred directly from
the simulator to the user.

Runtime converts results into transportable
container formats before delivery.

This creates an additional visibility layer
that does not exist in local Aer execution.

## QMVA Classification

Serialization Boundary

