# EVIDENCE-004

## Title

Primitive Projection Boundary

## Repository

Qiskit Aer

## Observation

Primitive APIs do not expose all information preserved by Aer.

Instead, they select specific simulator representations prior to result delivery.

## Evidence

### Sampler

File:
qiskit_aer/primitives/sampler.py

Observed:

    circuit.save_probabilities_dict(qargs)

followed by:

    probabilities = result.data(i)["probabilities"]

and conversion into:

    QuasiDistribution(...)

Information flow:

    Quantum State
         ↓
    save_probabilities_dict
         ↓
    probabilities
         ↓
    QuasiDistribution
         ↓
    SamplerResult

### Estimator

File:
qiskit_aer/primitives/estimator.py

Observed:

    circuit.save_expectation_value(
        observable,
        self._layouts[i]
    )

followed by:

    result.data(i)["expectation_value"]

Information flow:

    Quantum State
         ↓
    save_expectation_value
         ↓
    expectation_value
         ↓
    EstimatorResult

## Interpretation

Aer supports richer representations including:

- statevector
- density matrix
- amplitudes
- probabilities
- expectation values
- conditional states
- per-shot states

Primitive APIs request only specific projections.

Therefore information reduction occurs through
representation selection rather than simulator limitation.

## QMVA Classification

Primitive Information Projection Boundary

