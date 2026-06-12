import numpy as np
import json

with open(
    "QMVA-15A-HiddenStates.json"
) as f:

    hidden = np.array(json.load(f))

# detector manifold learned from QMVA-09C

detector_y = (
    20.9
    + hidden*(41.8-20.9)
)

np.random.seed(42)

detector_y += np.random.normal(
    0,
    0.4,
    size=len(detector_y)
)

result = []

for g,d in zip(hidden,detector_y):

    result.append({
        "true_ground": float(g),
        "detector_y": float(d)
    })

with open(
    "QMVA-15B-DetectorData.json",
    "w"
) as f:

    json.dump(
        result,
        f,
        indent=2
    )

print("Saved QMVA-15B-DetectorData.json")
