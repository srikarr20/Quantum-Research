# EVIDENCE-016

## Title

Detector-Plane Entropy Compression

## Audit

QMVA-03

## Objective

Quantify information compression between
continuous detector-plane measurements
and binary state assignments.

## Detector Representation

Projected detector-plane coordinates
obtained from:

- I_g
- Q_g
- I_e
- Q_e

after rotation into the discrimination basis.

## Binary Representation

Ground

or

Excited

## Measured Results

Detector Entropy:

6.8411 bits

Binary Entropy:

1.0000 bit

Compression Ratio:

0.1462

Information Loss:

0.8538

85.38%

## Interpretation

The detector-plane representation contains
substantially more observable information
than the final binary state assignment.

Approximately 85.4% of detector-plane
representation entropy is removed during
threshold-based classification.

## QMVA Interpretation

The dominant information-compression
boundary occurs between:

Detector Plane
        ↓
Threshold Classification
        ↓
Binary Outcome

This compression occurs before higher-level
software layers such as counts,
probabilities, or expectation values.

