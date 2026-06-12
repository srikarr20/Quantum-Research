import json
import numpy as np
from scipy.io import loadmat

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

DATA = "../../datasets/ISTA-AllOptical-Readout/AllopticalSCQreadout_data/Fig_4a/IQblobs_0Hz.mat"

d = loadmat(DATA)

I_g = d["I_g"].flatten()
Q_g = d["Q_g"].flatten()

I_e = d["I_e"].flatten()
Q_e = d["Q_e"].flatten()

g = np.column_stack([I_g, Q_g])
e = np.column_stack([I_e, Q_e])

theta = float(d["angle"].item())
threshold = float(d["threshold"].item())

# --------------------------------------------------
# ROTATION
# --------------------------------------------------

def rotate(points, theta):
    c = np.cos(theta)
    s = np.sin(theta)

    R = np.array([
        [c, -s],
        [s,  c]
    ])

    return points @ R.T

# --------------------------------------------------
# CONFIDENCE TABLE
# --------------------------------------------------

CAL = [
    (0.0,0.5,0.65885),
    (0.5,1.0,0.83512),
    (1.0,1.5,0.91604),
    (1.5,2.0,0.95845),
    (2.0,3.0,0.98482),
    (3.0,5.0,0.98804),
    (5.0,10.0,0.98058),
]

def lookup_accuracy(z):

    for z0,z1,p in CAL:
        if z0 <= z < z1:
            return p

    return CAL[-1][2]

# --------------------------------------------------
# NOISE SWEEP
# --------------------------------------------------

noise_levels = [
    0,
    1e-5,
    2e-5,
    5e-5,
    1e-4,
    2e-4
]

results = []

for noise in noise_levels:

    binary_vals = []
    prob_vals = []

    for trial in range(50):

        rng = np.random.default_rng(trial)

        g_noisy = g + rng.normal(
            scale=noise,
            size=g.shape
        )

        e_noisy = e + rng.normal(
            scale=noise,
            size=e.shape
        )

        g_rot = rotate(g_noisy, theta)
        e_rot = rotate(e_noisy, theta)

        g_dist = g_rot[:,0] - threshold
        e_dist = e_rot[:,0] - threshold

        g_sigma = np.std(g_dist)
        e_sigma = np.std(e_dist)

        # binary

        binary = (
            np.sum(g_dist > 0)
            +
            np.sum(e_dist > 0)
        ) / (len(g_dist) + len(e_dist))

        binary_vals.append(binary)

        # probability

        probs = []

        for d0 in g_dist:

            z = abs(d0)/g_sigma
            acc = lookup_accuracy(z)

            probs.append(
                acc if d0 > 0
                else 1.0 - acc
            )

        for d0 in e_dist:

            z = abs(d0)/e_sigma
            acc = lookup_accuracy(z)

            probs.append(
                acc if d0 > 0
                else 1.0 - acc
            )

        prob_vals.append(
            np.mean(probs)
        )

    results.append({

        "noise": noise,

        "binary_mean":
            float(np.mean(binary_vals)),

        "binary_std":
            float(np.std(binary_vals)),

        "prob_mean":
            float(np.mean(prob_vals)),

        "prob_std":
            float(np.std(prob_vals))
    })

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

print()
print("=== QMVA-04B Variance Test ===")
print()

for r in results:

    print(
        f"noise={r['noise']:.1e} "
        f"binary_std={r['binary_std']:.6f} "
        f"prob_std={r['prob_std']:.6f}"
    )

with open(
    "../../artifacts/QMVA-04B-variance-test.json",
    "w"
) as f:

    json.dump(results, f, indent=2)

print()
print("Saved:")
print("../../artifacts/QMVA-04B-variance-test.json")
