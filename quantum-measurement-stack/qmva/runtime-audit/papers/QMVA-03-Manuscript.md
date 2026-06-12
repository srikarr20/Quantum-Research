# QMVA-03: Detector-Plane Confidence Calibration Using Real Superconducting Qubit Readout Data

## Abstract

Quantum measurements are commonly reduced to binary outcomes through threshold-based classification of detector signals. This abstraction simplifies downstream processing but may discard information present at the detector plane. QMVA-03 (Quantum Measurement Visibility Audit 03) investigates the extent of information compression during this process using a real superconducting qubit readout dataset from the ISTA All-Optical Readout experiment.

Using 100,000 detector events, we quantify detector-plane entropy, analyze classification-boundary structure, construct confidence metrics based on detector-space distance, and evaluate confidence-calibrated measurement outcomes. Results show that detector-plane entropy substantially exceeds binary outcome entropy and that detector-plane confidence strongly predicts classification correctness. Confidence-based filtering reduces classification error while preserving the majority of detector events.

These findings demonstrate that detector-plane metadata contains predictive information not represented in conventional binary measurement outcomes and can be transformed into probability-aware measurement outputs.

## 1. Introduction

Modern quantum measurement systems typically transform analog detector responses into discrete outcomes. In superconducting qubit readout, IQ detector measurements are projected onto a classification axis and thresholded to produce binary state assignments.

While this abstraction is operationally effective, it raises a fundamental question:

How much information present at the detector plane is discarded when measurements are reduced to binary outcomes?

QMVA-03 addresses this question through an instrument-level audit of detector-plane visibility using a real superconducting qubit readout dataset. The objective is not to replace standard measurement methods, but to quantify the information retained and lost across the measurement abstraction boundary.

## 2. Dataset

The analysis uses the ISTA All-Optical Superconducting Qubit Readout dataset.

The primary dataset contains:

* Ground-state preparation measurements
* Excited-state preparation measurements
* IQ detector-plane coordinates
* Classification rotation angle
* Classification threshold
* Published QND fidelity metrics

The 0 Hz dataset contains:

* 50,000 ground-state events
* 50,000 excited-state events
* Total: 100,000 detector events

## 3. Detector-Plane Representation

Detector outcomes are represented as IQ coordinates.

A standard measurement pipeline performs:

1. IQ acquisition
2. Axis rotation
3. Projection onto a single classification dimension
4. Threshold classification
5. Binary outcome generation

QMVA-03 examines the information retained before the final thresholding stage.

The detector-plane classification boundary is reconstructed using the published rotation angle and threshold parameters.

## 4. Entropy Analysis

Detector-plane information content was estimated using detector-space distributions and compared against binary outcome entropy.

Results:

* Detector-plane entropy: 6.84 bits
* Binary outcome entropy: 1.00 bit

This corresponds to approximately 85% compression when detector-plane measurements are reduced to binary outcomes.

The result demonstrates that binary classification discards substantial detector-plane structure.

## 5. Confidence Structure

Detector confidence was defined using signed distance from the classification threshold.

Measurements near the classification boundary exhibit greater ambiguity than measurements located deep within detector clusters.

Analysis identified:

* Near-threshold shots: 787
* Total shots: 100,000
* Fraction: 0.787%

These events represent detector outcomes most vulnerable to classification uncertainty.

## 6. Confidence Filtering

Detector confidence was used as a quality metric for measurement selection.

Original classification error:

* Ground error: 1.03%
* Excited error: 8.56%
* Total error: 4.80%

After removing low-confidence events:

* Ground error: 0.72%
* Excited error: 6.29%
* Total error: 3.50%

Retention:

* Ground shots retained: 94.72%
* Excited shots retained: 89.71%
* Total retained: 92.22%

This corresponds to approximately 27% relative error reduction while preserving more than 92% of detector events.

## 7. Confidence Calibration

Detector confidence was calibrated using cluster-relative distance expressed in standard deviations (σ).

Observed accuracy by confidence band:

| Confidence Band | Accuracy |
| --------------- | -------- |
| 0.0–0.5σ        | 65.89%   |
| 0.5–1.0σ        | 83.51%   |
| 1.0–1.5σ        | 91.60%   |
| 1.5–2.0σ        | 95.85%   |
| 2.0–3.0σ        | 98.48%   |
| 3.0–5.0σ        | 98.80%   |

The relationship is monotonic:

Higher detector-plane confidence corresponds to higher observed classification accuracy.

This enables construction of a probability-aware measurement model.

## 8. Probability-Aware Readout

Traditional readout returns:

State = Ground or Excited

The calibrated detector-plane model enables augmented outputs:

State

Confidence (σ)

Predicted Accuracy

For example:

Excited, 2.4σ, Predicted Accuracy ≈ 98.5%

This representation preserves information discarded by conventional binary thresholding.

## 9. Discussion

QMVA-03 demonstrates that detector-plane measurements contain predictive metadata beyond binary measurement outcomes.

Three observations emerge:

1. Detector-plane information exceeds binary information content.

2. Detector-plane confidence predicts measurement correctness.

3. Detector-plane confidence can be converted into calibrated probability estimates.

These findings suggest that detector-plane information may serve as a useful measurement-quality resource for downstream analysis, calibration, and runtime decision systems.

## 10. Conclusion

Using 100,000 real superconducting qubit detector events, QMVA-03 quantified detector-plane information retention across the measurement abstraction boundary.

The study found:

* Detector-plane entropy exceeds binary outcome entropy.
* Confidence metrics derived from detector geometry predict correctness.
* Confidence-based filtering reduces classification error.
* Detector-plane confidence can be calibrated into probability-aware measurement outputs.

The results establish a reproducible framework for detector-plane visibility auditing and provide evidence that detector-plane metadata contains operationally useful information beyond conventional binary measurement outcomes.

## Data Availability

Zenodo Record:
https://zenodo.org/records/20653104

Repository:
https://github.com/srikarr20/Quantum-Research

Release:
qmva-v0.5

