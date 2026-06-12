import json
import numpy as np

D = json.load(
    open(
        "QMVA-17A-DetectorTopology.json"
    )
)

Q = json.load(
    open(
        "QMVA-17B-IQTopology.json"
    )
)

det_entropy = [
    x["entropy"]
    for x in D
]

iq_entropy = [
    x["entropy"]
    for x in Q
]

print()
print(
    "Detector Entropy Span:",
    max(det_entropy)-min(det_entropy)
)

print(
    "IQ Entropy Span:",
    max(iq_entropy)-min(iq_entropy)
)

print()

print(
    "Detector Radius Span:",
    max(
        x["radius"] for x in D
    )
    -
    min(
        x["radius"] for x in D
    )
)

print(
    "IQ Radius Span:",
    max(
        x["radius"] for x in Q
    )
    -
    min(
        x["radius"] for x in Q
    )
)
