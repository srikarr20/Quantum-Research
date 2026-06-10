# QMVA-03

## Title

All-Optical Superconducting Qubit Readout Audit

## Dataset

All-Optical Superconducting Qubit Readout

Zenodo:
https://zenodo.org/records/14033026

## Objective

Determine where information visibility changes
between detector-plane measurements and
binary state assignment.

---

## Dataset Structure

Observed detector-plane variables:

- I_g
- Q_g
- I_e
- Q_e

Observed classification variables:

- angle
- threshold

Observed measurement metrics:

- Pgg
- Pee
- QNDFid

---

## Findings

### FINDING-01

Detector-plane measurement coordinates are
exposed prior to classification.

Evidence:

EVIDENCE-012

50,000 ground-state measurements.

50,000 excited-state measurements.

---

### FINDING-02

An explicit projection boundary exists.

Evidence:

angle = 3.1254224

Detector-plane coordinates are rotated
into a discrimination basis.

---

### FINDING-03

An explicit classification boundary exists.

Evidence:

threshold = -5.844e-06

Continuous detector-plane coordinates
are converted into binary state labels.

---

### FINDING-04

Classification introduces measurable
information reduction.

Measured:

Ground Misclassification = 1.03%

Excited Misclassification = 8.56%

Average Misclassification = 4.797%

---

## Published Metrics

Pgg     = 0.98452

Pee     = 0.84438

QNDFid  = 0.91445

---

## QMVA Interpretation

The detector does not directly produce
binary outcomes.

Instead the measurement stack produces
continuous detector-plane coordinates.

Binary outcomes emerge after projection
and threshold-based classification.

## Supporting Evidence

- EVIDENCE-012


---

### FINDING-05

Visibility retention remains high after
classification.

Evidence:

EVIDENCE-013

Measured:

VRI = 0.95203

Interpretation:

Approximately 95.2% of detector-plane
visibility survives threshold-based
classification.


---

### FINDING-06

A significant abstraction compression boundary
exists between detector-plane measurements and
user-visible outcomes.

Evidence:

EVIDENCE-014

Detector-plane data consists of continuous
IQ coordinates.

User-visible outcomes consist of binary
state assignments.


---

### FINDING-07

Visibility Retention Index (VRI) and
Quantum Non-Demolition Fidelity (QNDFid)
decrease together across the frequency sweep.

Evidence:

EVIDENCE-015

Measured:

0 Hz

    VRI     = 0.95203
    QNDFid  = 0.91445

1000 Hz

    VRI     = 0.76013
    QNDFid  = 0.69235

Interpretation:

Detector-plane visibility and measurement
fidelity exhibit a strong positive relationship.


---

### FINDING-08

The dominant information-compression boundary
occurs at threshold-based classification.

Evidence:

EVIDENCE-016

Measured:

Detector Entropy = 6.8411 bits

Binary Entropy   = 1.0000 bit

Compression Ratio = 0.1462

Information Loss = 85.38%

Interpretation:

Approximately 85.4% of detector-plane
representation entropy is removed when
continuous detector measurements are
converted into binary outcomes.

