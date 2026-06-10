# DPI Mapping for QMVA-03

## Detector Plane

Raw Variables:

- I_g
- Q_g
- I_e
- Q_e

## DPI Layer

Per-shot detector coordinates.

Observable structure:

- Cluster centers
- Cluster variance
- Threshold distance
- Confidence
- Overlap regions

## Classification Layer

Variables:

- angle
- threshold

Transforms detector-plane coordinates
into binary assignments.

## Outcome Layer

Ground

Excited

## QMVA Finding

Detector-plane entropy:

6.8411 bits

Outcome entropy:

1.0000 bit

Approximate representation loss:

85.38%

## DPI Objective

Retain detector-plane visibility
before threshold-based compression.

