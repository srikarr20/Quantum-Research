# QMVA-03 Final Results

## Dataset

ISTA All-Optical Superconducting Qubit Readout

## Finding 1: Information Compression

Detector Entropy:
6.8411 bits

Binary Entropy:
1.0000 bit

Compression:
85.38%

Conclusion:
Detector-plane information is lost during
binary threshold classification.

---

## Finding 2: Confidence Structure

Near-threshold shots:
787

Total shots:
100000

Fraction:
0.00787

Conclusion:
Detector-plane ambiguity can be identified.

---

## Finding 3: Confidence Filtering

Original Error:
0.04797

Filtered Error:
0.03503

Relative Improvement:
26.98%

Shot Retention:
92.215%

Conclusion:
Detector-plane confidence improves
measurement quality.

---

## Finding 4: Confidence Calibration

0.0–0.5σ -> 65.89%

0.5–1.0σ -> 83.51%

1.0–1.5σ -> 91.60%

1.5–2.0σ -> 95.85%

2.0–3.0σ -> 98.48%

3.0–5.0σ -> 98.80%

Conclusion:
Detector-plane confidence predicts
measurement correctness.

---

## Final Conclusion

Detector-plane measurements contain
predictive metadata discarded by binary
classification.

Retaining detector-plane information
enables:

- confidence-aware readout
- probability-aware measurement
- improved classification performance
- detector-level measurement auditing

