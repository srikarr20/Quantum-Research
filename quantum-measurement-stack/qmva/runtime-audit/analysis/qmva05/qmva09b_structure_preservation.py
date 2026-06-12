import json
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from scipy.io import loadmat
from scipy.stats import entropy

# ----------------------------------------
# Locate dataset
# ----------------------------------------

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

# ----------------------------------------
# Load
# ----------------------------------------

d = loadmat(DATA)

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

fractions = [1.0, 0.75, 0.50, 0.25, 0.0]

results = []

for frac in fractions:

    ng = int(50000 * frac)
    ne = 50000 - ng

    idxg = np.random.choice(
        len(Ig),
        ng,
        replace=False
    ) if ng > 0 else np.array([], dtype=int)

    idxe = np.random.choice(
        len(Ie),
        ne,
        replace=False
    ) if ne > 0 else np.array([], dtype=int)

    I = np.concatenate([
        Ig[idxg] if ng > 0 else np.array([]),
        Ie[idxe] if ne > 0 else np.array([])
    ])

    Q = np.concatenate([
        Qg[idxg] if ng > 0 else np.array([]),
        Qe[idxe] if ne > 0 else np.array([])
    ])

    # ----------------------------
    # Dataset metrics
    # ----------------------------

    dataset_x = float(np.mean(I))
    dataset_y = float(np.mean(Q))

    hist, _ = np.histogram(
        I,
        bins=128,
        density=True
    )

    dataset_entropy = float(
        entropy(hist + 1e-12)
    )

    # ----------------------------
    # Detector occupancy field
    # ----------------------------

    H, _, _ = np.histogram2d(
        I,
        Q,
        bins=64
    )

    y, x = np.indices(H.shape)

    total = H.sum()

    cx = float((x * H).sum() / total)
    cy = float((y * H).sum() / total)

    detector_entropy = float(
        entropy(
            H.flatten() / total
        )
    )

    results.append({

        "ground_fraction": frac,

        "dataset_x": dataset_x,
        "dataset_y": dataset_y,
        "dataset_entropy": dataset_entropy,

        "detector_x": cx,
        "detector_y": cy,
        "detector_entropy": detector_entropy
    })

# ----------------------------------------
# Save
# ----------------------------------------

with open(
    "QMVA-09B-structure-preservation.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

# ----------------------------------------
# Plot
# ----------------------------------------

dataset_traj = [
    r["dataset_x"]
    for r in results
]

detector_traj = [
    r["detector_x"]
    for r in results
]

plt.figure(figsize=(8,5))

plt.plot(
    fractions,
    dataset_traj,
    marker="o",
    label="Dataset Space"
)

plt.plot(
    fractions,
    detector_traj,
    marker="s",
    label="Detector Space"
)

plt.xlabel("Ground Fraction")

plt.ylabel("Trajectory Coordinate")

plt.title(
    "QMVA-09B Structure Preservation"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "QMVA-09B-Structure-Preservation.png",
    dpi=300
)

print()
print("Saved:")
print("QMVA-09B-structure-preservation.json")
print("QMVA-09B-Structure-Preservation.png")
