import numpy as np
import json
from scipy.stats import entropy

V = np.load(
    "QMVA-07C-HyperVolume.npy"
)

results = []

for mix in range(V.shape[0]):

    volume = V[mix]

    frame = volume.mean(axis=0)

    p = frame.flatten()
    p = p / p.sum()

    H = entropy(p)

    y,x = np.indices(frame.shape)

    cx = (x*frame).sum()/frame.sum()
    cy = (y*frame).sum()/frame.sum()

    r = np.sqrt(
        (x-cx)**2 +
        (y-cy)**2
    )

    radius = (
        r*frame
    ).sum()/frame.sum()

    results.append({

        "mix": int(mix),
        "entropy": float(H),
        "centroid_x": float(cx),
        "centroid_y": float(cy),
        "radius": float(radius)
    })

with open(
    "QMVA-17A-DetectorTopology.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print(
    json.dumps(
        results,
        indent=2
    )
)
