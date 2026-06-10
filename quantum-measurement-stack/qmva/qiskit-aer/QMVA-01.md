# QMVA-01

## Platform

Qiskit Aer

## Status

Draft

---

# Objective

Evaluate how Qiskit Aer represents measurement uncertainty and determine where detector-related information becomes abstracted within the simulation stack.

---

# Scope

This audit examines:

- ReadoutError
- NoiseModel
- basic_device_readout_errors

within the Qiskit Aer codebase.

---

# Evidence Summary

## ReadoutError

Qiskit Aer represents measurement uncertainty through assignment probability matrices.

Measurement outcomes are modeled as conditional probabilities between ideal outcomes and observed outcomes.

---

## NoiseModel

Qiskit Aer incorporates:

- gate errors
- thermal relaxation
- T1
- T2
- backend calibration data
- readout errors

into simulation noise models.

---

## basic_device_readout_errors

Backend readout calibration parameters are transformed into assignment probability matrices.

Examples:

- prob_meas1_prep0
- prob_meas0_prep1

These values are converted into ReadoutError objects.

---

# Findings

## QMV-AER-001

Qiskit Aer models measurement uncertainty through calibrated assignment probabilities.

Measurement behavior is represented statistically through readout error matrices.

---

## QMV-AER-002

Detector-plane mechanisms are not represented as explicit simulation objects.

The following elements are not directly modeled within the readout abstraction:

- detector architecture
- signal conversion chain
- front-end electronics
- digitization
- firmware
- DAQ

Their aggregate effects are represented through calibration-derived probabilities.

---

# Abstraction Boundary

Physical Backend

↓

Calibration Data

↓

Readout Assignment Probabilities

↓

ReadoutError Matrix

↓

Simulation Output

Detector-chain information is compressed into statistical measurement representations.

---

# QMS Interpretation

From a Quantum Measurement Stack perspective, Aer models the observable effects of measurement degradation rather than the causal provenance of measurement degradation.

This distinction identifies the first measurement abstraction boundary observed within QMVA.

---

# Next Steps

- Audit Qiskit Runtime
- Audit Sampler primitives
- Audit Estimator primitives
- Compare simulator visibility versus runtime visibility
- Define QMVA visibility scoring framework


## Figure 1

See:

figures/FIGURE-001-measurement-abstraction-boundary.mmd

This figure illustrates the identified abstraction boundary between backend calibration information and detector-chain provenance representation.


