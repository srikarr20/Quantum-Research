import json
import numpy as np
from scipy.io import loadmat

# --------------------------------------------------
# DATA
# --------------------------------------------------

DATA = "../datasets/ISTA-AllOptical-Readout/AllopticalSCQreadout_data/Fig_4a/IQblobs_0Hz.mat"

d = loadmat(DATA)

g = d["g"]
e = d["e"]

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

g_rot = rotate(g, theta)
e_rot = rotate(e, theta)

# --------------------------------------------------
# DISTANCE FROM THRESHOLD
# --------------------------------------------------

g_dist = g_rot[:,0] - threshold
e_dist = e_rot[:,0] - threshold

# --------------------------------------------------
# CLUSTER WIDTHS
# --------------------------------------------------

g_sigma = np.std(g_dist)
e_sigma = np.std(e_dist)

# --------------------------------------------------
# CALIBRATION TABLE
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
# PROBABILITY ESTIMATOR
# --------------------------------------------------

probs = []

# ground shots

for d0 in g_dist:

    z = abs(d0)/g_sigma
    acc = lookup_accuracy(z)

    pred_excited = d0 > 0

    if pred_excited:
        probs.append(acc)
    else:
        probs.append(1.0 - acc)

# excited shots

for d0 in e_dist:

    z = abs(d0)/e_sigma
    acc = lookup_accuracy(z)

    pred_excited = d0 > 0

    if pred_excited:
        probs.append(acc)
    else:
        probs.append(1.0 - acc)

probs = np.array(probs)

# --------------------------------------------------
# BINARY ESTIMATOR
# --------------------------------------------------

binary_excited = (
    np.sum(g_dist > 0)
    +
    np.sum(e_dist > 0)
) / (len(g_dist) + len(e_dist))

# --------------------------------------------------
# PROBABILITY ESTIMATOR
# --------------------------------------------------

prob_excited = np.mean(probs)

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

result = {

    "binary_excited_population":
        float(binary_excited),

    "probability_excited_population":
        float(prob_excited),

    "difference":
        float(prob_excited - binary_excited),

    "mean_probability":
        float(np.mean(probs)),

    "median_probability":
        float(np.median(probs)),

    "effective_shots":
        float(np.sum(probs))
}

print()
print("=== QMVA-04A Population Estimator ===")
print()
print(json.dumps(result, indent=2))

with open(
    "../../artifacts/QMVA-04A-population-estimator.json",
    "w"
) as f:

    json.dump(result, f, indent=2)

print()
print("Saved:")
print("../../artifacts/QMVA-04A-population-estimator.json")
