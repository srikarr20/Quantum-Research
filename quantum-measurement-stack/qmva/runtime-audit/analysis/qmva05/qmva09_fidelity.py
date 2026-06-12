import json
import numpy as np

from pathlib import Path
from scipy.io import loadmat
from scipy.stats import entropy

# --------------------------------------------------
# Locate dataset
# --------------------------------------------------

ROOT = Path(__file__).resolve()

DATA = None

for parent in ROOT.parents:

    candidate = (
        parent
        / "datasets"
        / "ISTA-AllOptical-Readout"
        / "AllopticalSCQreadout_data"
        / "Fig_4a"
        / "IQblobs_0Hz.mat"
    )

    if candidate.exists():
        DATA = candidate
        break

if DATA is None:
    raise RuntimeError("Dataset not found")

print("Using:", DATA)

# --------------------------------------------------
# Load
# --------------------------------------------------

d = loadmat(DATA)

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

# --------------------------------------------------
# DATASET SPACE
# --------------------------------------------------

g_centroid = [
    float(np.mean(Ig)),
    float(np.mean(Qg))
]

e_centroid = [
    float(np.mean(Ie)),
    float(np.mean(Qe))
]

dataset_sep = float(
    np.linalg.norm(
        np.array(g_centroid)
        -
        np.array(e_centroid)
    )
)

# --------------------------------------------------
# DETECTOR SPACE
# --------------------------------------------------

V = np.load("QMVA-05B-fixed-volume.npy")

mean_frame = np.mean(V, axis=0)

y, x = np.indices(mean_frame.shape)

total = mean_frame.sum()

detector_centroid = [

    float((x * mean_frame).sum() / total),

    float((y * mean_frame).sum() / total)
]

# split detector manifolds

upper = mean_frame[32:, :]
lower = mean_frame[:32, :]

upper_occ = float(upper.sum())
lower_occ = float(lower.sum())

detector_sep = abs(
    upper_occ - lower_occ
)

# --------------------------------------------------
# ENTROPY
# --------------------------------------------------

g_hist, _ = np.histogram(
    Ig,
    bins=128,
    density=True
)

e_hist, _ = np.histogram(
    Ie,
    bins=128,
    density=True
)

g_entropy = float(
    entropy(g_hist + 1e-12)
)

e_entropy = float(
    entropy(e_hist + 1e-12)
)

detector_entropy = float(
    entropy(
        mean_frame.flatten()
        /
        mean_frame.sum()
    )
)

# --------------------------------------------------
# Results
# --------------------------------------------------

results = {

    "dataset": {

        "ground_centroid":
            g_centroid,

        "excited_centroid":
            e_centroid,

        "state_separation":
            dataset_sep,

        "ground_entropy":
            g_entropy,

        "excited_entropy":
            e_entropy
    },

    "detector": {

        "centroid":
            detector_centroid,

        "occupancy_difference":
            detector_sep,

        "entropy":
            detector_entropy
    }
}

print()
print(json.dumps(results, indent=2))

with open(
    "QMVA-09A-fidelity-table.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-09A-fidelity-table.json")
