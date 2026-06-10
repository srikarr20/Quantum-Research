# EVIDENCE-010

## Title

Runtime DataBin Transport Layer

## Observation

IBM Runtime reconstructs DataBin objects
during result decoding and transport.

Observed locations:

qiskit_ibm_runtime/utils/json.py

    DataBin serialization
    DataBin deserialization

qiskit_ibm_runtime/decoders/executor_estimator/post_processor_v0_1.py

    DataBin(...)

qiskit_ibm_runtime/decoders/executor_sampler/converters.py

    DataBin(...)

## Finding

Runtime uses DataBin as a transport and
reconstruction container between execution
results and user-facing objects.

## QMVA Classification

Transport Boundary

