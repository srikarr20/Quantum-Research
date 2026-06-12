import json
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from scipy.io import loadmat
from scipy.stats import spearmanr

# ----------------------------------------
# Find dataset
# ----------------------------------------

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

# ----------------------------------------
# Load
# ----------------------------------------

d = loadmat(DATA)

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

fractions = np.linspace(0.0, 1.0, 11)

detector_y = []

for frac in fractions:

    ng = int(50000 * frac)
    ne = 50000 - ng

    if ng > 0:
        idxg = np.random.choice(len(Ig), ng, replace=False)
        Ig_sel = Ig[idxg]
        Qg_sel = Qg[idxg]
    else:
        Ig_sel = np.array([])
        Qg_sel = np.array([])

    if ne > 0:
        idxe = np.random.choice(len(Ie), ne, replace=False)
        Ie_sel = Ie[idxe]
        Qe_sel = Qe[idxe]
    else:
        Ie_sel = np.array([])
        Qe_sel = np.array([])

    I = np.concatenate([Ig_sel, Ie_sel])
    Q = np.concatenate([Qg_sel, Qe_sel])

    H, _, _ = np.histogram2d(I, Q, bins=64)

    y, x = np.indices(H.shape)

    total = H.sum()

    cy = (y * H).sum() / total

    detector_y.append(float(cy))

detector_y = np.array(detector_y)

# ----------------------------------------
# Correlation
# ----------------------------------------

rho, pvalue = spearmanr(
    fractions,
    detector_y
)

coef = np.polyfit(
    fractions,
    detector_y,
    1
)

fit = np.polyval(
    coef,
    fractions
)

ss_res = np.sum(
    (detector_y - fit) ** 2
)

ss_tot = np.sum(
    (detector_y - detector_y.mean()) ** 2
)

r2 = 1.0 - ss_res / ss_tot

# ----------------------------------------
# Save
# ----------------------------------------

results = {
    "spearman_rho": float(rho),
    "spearman_p": float(pvalue),
    "r2": float(r2),
    "slope": float(coef[0]),
    "intercept": float(coef[1]),
    "fractions": fractions.tolist(),
    "detector_y": detector_y.tolist()
}

with open("QMVA-09C-state-order.json", "w") as f:
    json.dump(results, f, indent=2)

# ----------------------------------------
# Plot
# ----------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    fractions,
    detector_y,
    s=80,
    label="Detector Coordinate"
)

plt.plot(
    fractions,
    fit,
    linewidth=2,
    label=f"Fit R²={r2:.4f}"
)

plt.xlabel("Ground Fraction")
plt.ylabel("Detector Y Coordinate")

plt.title(
    "QMVA-09C State Order Preservation"
)

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    "QMVA-09C-StateOrder.png",
    dpi=300
)

print()
print("Spearman rho =", rho)
print("R² =", r2)

print()
print("Saved:")
print("QMVA-09C-state-order.json")
print("QMVA-09C-StateOrder.png")
