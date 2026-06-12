import json
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from scipy.io import loadmat

# ----------------------------------
# Locate dataset
# ----------------------------------

DATA = None

for parent in Path(__file__).resolve().parents:

    candidate = (
        parent /
        "datasets" /
        "ISTA-AllOptical-Readout" /
        "AllopticalSCQreadout_data" /
        "Fig_4a" /
        "IQblobs_0Hz.mat"
    )

    if candidate.exists():
        DATA = candidate
        break

if DATA is None:
    raise RuntimeError("Dataset not found")

print("Using:", DATA)

# ----------------------------------
# Load
# ----------------------------------

d = loadmat(DATA)

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

# ----------------------------------
# Generate detector coordinates
# ----------------------------------

fractions = np.linspace(0, 1, 21)

detector_y = []

for frac in fractions:

    ng = int(50000 * frac)
    ne = 50000 - ng

    if ng > 0:
        idxg = np.random.choice(
            len(Ig),
            ng,
            replace=False
        )

        Ig_sel = Ig[idxg]
        Qg_sel = Qg[idxg]

    else:

        Ig_sel = np.array([])
        Qg_sel = np.array([])

    if ne > 0:

        idxe = np.random.choice(
            len(Ie),
            ne,
            replace=False
        )

        Ie_sel = Ie[idxe]
        Qe_sel = Qe[idxe]

    else:

        Ie_sel = np.array([])
        Qe_sel = np.array([])

    I = np.concatenate([Ig_sel, Ie_sel])
    Q = np.concatenate([Qg_sel, Qe_sel])

    H, _, _ = np.histogram2d(
        I,
        Q,
        bins=64
    )

    y, x = np.indices(H.shape)

    total = H.sum()

    cy = (y * H).sum() / total

    detector_y.append(cy)

detector_y = np.array(detector_y)

# ----------------------------------
# Learn mapping
# ----------------------------------

coef = np.polyfit(
    detector_y,
    fractions,
    1
)

estimated = np.polyval(
    coef,
    detector_y
)

# ----------------------------------
# Reconstruction error
# ----------------------------------

mae = np.mean(
    np.abs(
        estimated - fractions
    )
)

rmse = np.sqrt(
    np.mean(
        (estimated - fractions) ** 2
    )
)

r2 = 1 - (
    np.sum(
        (fractions - estimated) ** 2
    )
    /
    np.sum(
        (fractions - fractions.mean()) ** 2
    )
)

# ----------------------------------
# Save
# ----------------------------------

results = {

    "mae": float(mae),
    "rmse": float(rmse),
    "r2": float(r2),

    "slope": float(coef[0]),
    "intercept": float(coef[1])
}

with open(
    "QMVA-10A-reconstruction.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

# ----------------------------------
# Plot
# ----------------------------------

plt.figure(figsize=(7,6))

plt.scatter(
    fractions,
    estimated,
    s=80
)

plt.plot(
    [0,1],
    [0,1],
    "--",
    linewidth=2
)

plt.xlabel(
    "Actual Ground Fraction"
)

plt.ylabel(
    "Reconstructed Fraction"
)

plt.title(
    f"QMVA-10A Reconstruction\nR²={r2:.4f}"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "QMVA-10A-Reconstruction.png",
    dpi=300
)

print()
print("MAE =", mae)
print("RMSE =", rmse)
print("R² =", r2)

print()
print("Saved:")
print("QMVA-10A-reconstruction.json")
print("QMVA-10A-Reconstruction.png")
