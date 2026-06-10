# EVIDENCE-002

## Component

basic_device_readout_errors

## Source

Qiskit Aer

## Observation

Backend calibration parameters are converted into assignment probability matrices.

Examples:

- prob_meas1_prep0
- prob_meas0_prep1

These values are transformed into ReadoutError objects.

## Visibility

Visible:
- Calibration-derived assignment probabilities
- Readout characterization

Not Explicitly Visible:
- Detector architecture
- Analog electronics
- Signal conversion chain
- ADC
- Firmware
- DAQ

## QMVA Classification

Readout Visibility: E3

Detector Visibility: E0

Provenance Visibility: E0

## Notes

Detector-chain behavior is compressed into statistical readout parameters before entering the simulation layer.
