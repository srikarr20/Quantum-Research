# QMVA-02

## Target

IBM Runtime

## Status

In Progress

## Objective

Determine how information visibility changes
between local simulator execution and
Runtime-mediated execution.

---

## Findings

### Finding 01

Runtime preserves the primitive result model:

    DataBin
        ↓
    PubResult
        ↓
    PrimitiveResult

Observed in:

- qiskit_ibm_runtime/utils/json.py
- executor_sampler/converters.py
- executor_estimator/post_processor_v0_1.py

---

### Finding 02

Runtime serializes and reconstructs
primitive result containers.

Observed:

- PrimitiveResult
- PubResult
- DataBin

This introduces a transport layer between
execution and user visibility.

---

### Finding 03

Runtime uses BitArray-based measurement
containers.

Observed:

- BitArray
- DataBin

within Runtime result handling.

---

### Finding 04

No explicit "pershot" references have been
identified within Runtime source.

This contrasts with Aer, where pershot=True
is explicitly supported for multiple save
instructions.

---

## Working Model

Aer

    Rich State
        ↓
    DataBin
        ↓
    PubResult
        ↓
    PrimitiveResult

Runtime

    PrimitiveResult
        ↓
    Serialization
        ↓
    Transport
        ↓
    Reconstruction
        ↓
    User Result


---

### Finding 05

Runtime visibility appears centered on
primitive-result containers rather than
direct simulator-state representations.

Observed:

- PrimitiveResult
- PubResult
- SamplerPubResult
- EstimatorPubResult
- DataBin
- BitArray

No direct references identified for:

- statevector
- density_matrix

within the audited Runtime source tree.

Reference:

EVIDENCE-011 Runtime Measurement-Oriented Visibility

