# EVIDENCE-004

Title:
Primitive Projection Boundary

Observation:

Aer supports richer representations including:

- statevector
- density matrix
- amplitudes
- probabilities
- expectation values
- conditional states
- per-shot states

However, Primitive APIs selectively request
specific representations.

Sampler:
    save_probabilities_dict()
    -> QuasiDistribution

Estimator:
    save_expectation_value()
    -> Expectation Values

Finding:

Information reduction occurs through
representation selection at the Primitive API layer,
rather than through limitations of the Aer simulator core.

QMVA Classification:

Primitive Information Projection Boundary
