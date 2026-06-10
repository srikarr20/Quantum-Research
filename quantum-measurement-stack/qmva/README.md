# Quantum Measurement Visibility Audit (QMVA)

## Overview

The Quantum Measurement Visibility Audit (QMVA) framework provides a platform-neutral methodology for evaluating how quantum software ecosystems represent, abstract, or expose the measurement process.

QMVA focuses on measurement visibility rather than algorithmic performance, computational efficiency, or physical correctness.

The framework seeks to identify:

- Measurement abstraction boundaries
- Detector representation
- Detector-chain visibility
- Provenance visibility
- Correlation visibility
- Information-loss localization capability

QMVA operates alongside the Quantum Measurement Stack (QMS).

- QMCTB benchmarks evaluate measurement behavior.
- QMVA audits evaluate measurement visibility.

Together they provide complementary perspectives on quantum measurement integrity.

---

## Current Audits

### Qiskit Aer

Status: In Progress

Objective:

Evaluate how Qiskit Aer represents measurement uncertainty, readout calibration, and detector-related information within its simulation framework.

---

## Planned Audits

- Qiskit Runtime
- Qiskit Core SDK
- Cirq
- PennyLane
- Strawberry Fields
- Perceval
- QuTiP
- Amazon Braket

---

## Repository Structure

methodology/
- QMVA audit methodology

qiskit-aer/
- Qiskit Aer audit reports
- supporting evidence
- figures

---

## Guiding Principle

QMVA documents measurement visibility.

Abstractions are treated as design choices rather than deficiencies.

The purpose of the framework is to identify where information is visible, where it is hidden, and where measurement boundaries occur.
