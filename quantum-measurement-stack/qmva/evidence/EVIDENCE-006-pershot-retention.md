# EVIDENCE-006

## Title

Per-Shot Information Retention

## Observation

Aer explicitly supports per-shot retention.

Verified through tests using:

- save_statevector(..., pershot=True)
- save_density_matrix(..., pershot=True)
- save_statevector_dict(..., pershot=True)
- SaveAmplitudes(..., pershot=True)
- SaveExpectationValue(..., pershot=True)

## Finding

Information may be retained at the
individual-shot level rather than only
through aggregated statistics.

## QMVA Classification

Per-Shot Information Retention
