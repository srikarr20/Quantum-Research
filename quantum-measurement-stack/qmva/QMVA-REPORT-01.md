# QMVA Report 01

## Repository

Qiskit Aer

## Audit Target

Frozen repository state documented in EVIDENCE-000.

## Objective

Determine where information reduction occurs between
Aer simulation internals and user-facing interfaces.

---

## Findings

### EVIDENCE-004
Primitive Projection Boundary

Primitive APIs request specific representations
from Aer rather than exposing the complete simulator state.

Examples:

- save_probabilities_dict()
- save_expectation_value()

---

### EVIDENCE-005
Conditional Retention

Aer supports retention of information
conditioned on measurement branches.

Examples:

- save_statevector(..., conditional=True)
- save_density_matrix(..., conditional=True)

---

### EVIDENCE-006
Per-Shot Retention

Aer supports retention of information
at the individual-shot level.

Examples:

- save_statevector(..., pershot=True)
- save_density_matrix(..., pershot=True)

---

### EVIDENCE-007
Rich State Exposure

Aer exposes multiple internal representations:

- Statevector
- Density Matrix
- Amplitudes
- Probabilities
- Expectation Values

These capabilities are validated by dedicated tests.

---

### EVIDENCE-008
Result Packaging Boundary

Projected information is packaged into:

- QuasiDistribution
- BitArray
- DataBin
- SamplerResult
- EstimatorResult

before exposure to users.

---

## Information Flow

Aer Internal State
        ↓
Projection Boundary
        ↓
Packaging Boundary
        ↓
User Interface

---

## QMVA Conclusion

The audit found no evidence that Aer discards
quantum state information within its simulation core.

Instead, information reduction primarily occurs through:

1. Projection selection
2. Result packaging

The user-facing abstraction exposes selected
representations of a richer underlying state space.

This distinction is important when evaluating
measurement visibility and information accessibility
within quantum software stacks.


---

## Subsequent Findings

Later audits identified additional
serialization and transport boundaries:

- EVIDENCE-009A PrimitiveResult Serialization
- EVIDENCE-009B PubResult Serialization
- EVIDENCE-009C DataBin Serialization
- EVIDENCE-010 Runtime DataBin Transport

These findings extend the original
projection and packaging analysis into
Runtime-mediated execution environments.

