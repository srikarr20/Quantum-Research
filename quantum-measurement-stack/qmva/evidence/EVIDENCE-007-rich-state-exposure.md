# EVIDENCE-007

## Title

Rich State Exposure

## Observation

Aer exposes multiple state representations.

Verified through dedicated integration tests:

- save_statevector()
- save_density_matrix()
- save_amplitudes()
- save_probabilities()
- save_expectation_value()

## Finding

Aer supports richer state representations
than those typically surfaced through
Sampler and Estimator interfaces.

## QMVA Classification

Rich State Exposure
