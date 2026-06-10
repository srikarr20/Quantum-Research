# EVIDENCE-009C

## Title

DataBin Serialization

## Observation

IBM Runtime explicitly serializes
DataBin objects.

Observed:

qiskit_ibm_runtime/utils/json.py

    DataBin

## Finding

Underlying primitive data is packaged
inside DataBin containers before transport.

## QMVA Classification

Data Packaging Boundary

