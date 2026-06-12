import numpy as np
import json
from scipy.stats import entropy

V = np.load(
    "QMVA-07C-HyperVolume.npy"
)

results = []

for i in range(V.shape[0]):

    volume = V[i]

    p = volume.flatten()

    p = p / p.sum()

    H = entropy(p)

    results.append({
        "mixture": i,
        "entropy": float(H),
        "mean": float(volume.mean()),
        "std": float(volume.std()),
        "max": float(volume.max())
    })

with open(
    "QMVA-16A-VolumeInformation.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-16A-VolumeInformation.json")
