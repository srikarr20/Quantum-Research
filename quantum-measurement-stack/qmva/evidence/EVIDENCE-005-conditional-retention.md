# EVIDENCE-005

## Title

Conditional State Retention

## Observation

Aer explicitly supports conditional retention
of quantum state information.

Verified through tests using:

- save_statevector(..., conditional=True)
- save_density_matrix(..., conditional=True)
- save_statevector_dict(..., conditional=True)
- SaveAmplitudes(..., conditional=True)
- SaveExpectationValue(..., conditional=True)

## Finding

Information can be preserved separately
for distinct measurement branches.

## QMVA Classification

Conditional Information Retention
