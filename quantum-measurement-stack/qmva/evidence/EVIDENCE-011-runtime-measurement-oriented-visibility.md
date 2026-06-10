# EVIDENCE-011

## Title

Runtime Measurement-Oriented Visibility

## Observation

IBM Runtime source primarily exposes:

- PrimitiveResult
- PubResult
- SamplerPubResult
- EstimatorPubResult
- DataBin
- BitArray

through serialization, transport,
and reconstruction layers.

## Negative Findings

No direct references identified for:

- statevector
- density_matrix

within the audited Runtime source tree.

## Interpretation

Runtime visibility is centered on
primitive-result containers rather than
direct simulator-state representations.

## QMVA Relevance

Suggests a visibility shift from:

Aer:
    Rich state representations

to

Runtime:
    Measurement-oriented result containers

