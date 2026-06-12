import json
import numpy as np
from scipy.io import loadmat

DATA = "../../datasets/ISTA-AllOptical-Readout/AllopticalSCQreadout_data/Fig_4a/IQblobs_0Hz.mat"

d = loadmat(DATA)

I_g = d["I_g"].flatten()
Q_g = d["Q_g"].flatten()

I_e = d["I_e"].flatten()
Q_e = d["Q_e"].flatten()

theta = float(d["angle"].item())
threshold = float(d["threshold"].item())

g = np.column_stack([I_g,Q_g])
e = np.column_stack([I_e,Q_e])

def rotate(points, theta):

    c = np.cos(theta)
    s = np.sin(theta)

    R = np.array([
        [c,-s],
        [s, c]
    ])

    return points @ R.T

g_rot = rotate(g, theta)
e_rot = rotate(e, theta)

g_dist = g_rot[:,0] - threshold
e_dist = e_rot[:,0] - threshold

g_sigma = np.std(g_dist)
e_sigma = np.std(e_dist)

thresholds = [0.0, 1.0, 2.0]

results = []

for zcut in thresholds:

    g_keep = np.abs(g_dist)/g_sigma >= zcut
    e_keep = np.abs(e_dist)/e_sigma >= zcut

    g_use = g_dist[g_keep]
    e_use = e_dist[e_keep]

    ground_error = np.mean(g_use > 0)
    excited_error = np.mean(e_use < 0)

    total_error = (
        ground_error +
        excited_error
    ) / 2.0

    retention = (
        len(g_use) +
        len(e_use)
    ) / (
        len(g_dist) +
        len(e_dist)
    )

    results.append({

        "z_cut": zcut,

        "ground_error":
            float(ground_error),

        "excited_error":
            float(excited_error),

        "total_error":
            float(total_error),

        "retention":
            float(retention)
    })

print()
print("=== QMVA-04C Confidence Gating ===")
print()

for r in results:

    print(
        f"z>={r['z_cut']:.1f}  "
        f"error={r['total_error']:.5f}  "
        f"retention={r['retention']:.3f}"
    )

with open(
    "../../artifacts/QMVA-04C-confidence-gating.json",
    "w"
) as f:

    json.dump(results, f, indent=2)

print()
print("Saved:")
print("../../artifacts/QMVA-04C-confidence-gating.json")
