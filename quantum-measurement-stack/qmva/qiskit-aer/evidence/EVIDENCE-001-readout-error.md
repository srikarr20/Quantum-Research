# EVIDENCE-001

## Component

ReadoutError

## Source

Qiskit Aer

## Observation

ReadoutError represents measurement uncertainty through assignment probability matrices.

Probabilities are expressed as:

P(measured_state | ideal_state)

rather than detector-chain representations.

## Visibility

Visible:
- Assignment probabilities
- Measurement outcome statistics

Not Explicitly Visible:
- Detector architecture
- Detector technology
- Front-end electronics
- ADC
- Firmware
- DAQ

## QMVA Classification

Readout Visibility: E3

Detector Visibility: E0

Detector Chain Visibility: E0

## Notes

This component models the effects of measurement uncertainty but does not expose the physical detector chain responsible for those effects.
