import json
import numpy as np

V = np.load(
    "QMVA-05B-fixed-volume.npy"
)

centroid_x = []
centroid_y = []

entropy = []

for frame in V:

    total = frame.sum()

    if total == 0:
        continue

    y,x = np.indices(frame.shape)

    cx = (x * frame).sum() / total
    cy = (y * frame).sum() / total

    centroid_x.append(cx)
    centroid_y.append(cy)

    p = frame.flatten()
    p = p / p.sum()

    p = p[p > 0]

    H = -np.sum(
        p * np.log2(p)
    )

    entropy.append(H)

result = {

    "centroid_x_mean":
        float(np.mean(centroid_x)),

    "centroid_x_std":
        float(np.std(centroid_x)),

    "centroid_y_mean":
        float(np.mean(centroid_y)),

    "centroid_y_std":
        float(np.std(centroid_y)),

    "entropy_mean":
        float(np.mean(entropy)),

    "entropy_std":
        float(np.std(entropy))
}

print()
print("=== QMVA-05B Drift Metrics ===")
print()

print(
    json.dumps(
        result,
        indent=2
    )
)

with open(
    "QMVA-05B-drift-metrics.json",
    "w"
) as f:

    json.dump(
        result,
        f,
        indent=2
    )
