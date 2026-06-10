# EVIDENCE-015

## Title

Visibility Retention and QND Fidelity Correlation

## Audit

QMVA-03

## Dataset

All-Optical Superconducting Qubit Readout

## Observation

Visibility Retention Index (VRI) and
Quantum Non-Demolition Fidelity (QNDFid)
decrease together across the frequency sweep.

## Measured Results

Frequency (Hz) | VRI | QNDFid
------------- | ----- | -------
0             | 0.95203 | 0.91445
10            | 0.94680 | 0.90829
50            | 0.93571 | 0.89846
250           | 0.88501 | 0.84371
500           | 0.83034 | 0.78324
1000          | 0.76013 | 0.69235

## Interpretation

As frequency increases:

- Classification error increases
- Visibility retention decreases
- QND fidelity decreases

The two metrics exhibit a common trend
across all measured operating conditions.

## QMVA Interpretation

Detector-plane visibility appears to track
measurement fidelity.

The data suggest that visibility retention
may serve as a measurement-quality indicator.

