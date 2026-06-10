# EVIDENCE-012

## Title

Detector-Plane Classification Boundary

## Audit

QMVA-03

## Dataset

All-Optical Superconducting Qubit Readout

Zenodo Record:
https://zenodo.org/records/14033026

## Observation

The dataset exposes detector-plane measurement
coordinates prior to state discrimination.

Variables:

- I_g
- Q_g
- I_e
- Q_e

Each state contains 50,000 measurement records.

## Projection Boundary

The experiment exposes an explicit projection step.

Evidence:

angle = 3.1254224

The detector-plane coordinates are rotated into
a discrimination basis before classification.

## Classification Boundary

Evidence:

threshold = -5.844e-06

The rotated detector-plane coordinates are
converted into binary state assignments using
an explicit threshold.

## Measured Results

Ground Center:

( 8.81e-05 , -2.691e-04 )

Excited Center:

(-7.30e-05 , -2.718e-04 )

Cluster Separation:

1.61167e-04

Ground Misclassification:

1.03%

Excited Misclassification:

8.56%

Average Misclassification:

4.797%

## Published Metrics

Pgg     = 0.98452

Pee     = 0.84438

QNDFid  = 0.91445

## QMVA Interpretation

The detector produces continuous measurement-space
coordinates prior to classification.

Information reduction occurs at an explicit
projection and threshold boundary rather than
at the detector itself.

