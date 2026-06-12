# Quantum Measurement Visibility Audit (QMVA)

## Overview

QMVA is a methodology for evaluating information
visibility, retention, projection, and packaging
across quantum software stacks.

## Methodology

See:

- methodology/

## Framework

- QMVA-SCORECARD.md
- QMVA-QUESTIONS.md
- AUDIT-REGISTRY.md

## Completed Audits

### QMVA-01

Target:
Qiskit Aer

Key Finding:

Information reduction was not observed
within the Aer simulation core.

Information reduction was observed at:

- Projection Boundaries
- Packaging Boundaries

Artifacts:

- QMVA-REPORT-01.md
- evidence/

## Planned Audits

- IBM Runtime
- Cirq
- PennyLane
- Amazon Braket


## Archival Record

Zenodo:
https://zenodo.org/records/20653104

Release:
qmva-v0.5

Branch:
qmva03-release

