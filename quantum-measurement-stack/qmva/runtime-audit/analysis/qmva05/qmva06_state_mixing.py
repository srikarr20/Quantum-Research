import json
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from scipy.io import loadmat
from scipy.stats import gaussian_kde

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
# KDE Grid
# --------------------------------------------------

Iall = np.concatenate([Ig, Ie])
Qall = np.concatenate([Qg, Qe])

xmin = np.min(Iall)
xmax = np.max(Iall)

ymin = np.min(Qall)
ymax = np.max(Qall)

GRID = 200

x = np.linspace(xmin, xmax, GRID)
y = np.linspace(ymin, ymax, GRID)

X, Y = np.meshgrid(x, y)

POS = np.vstack([X.ravel(), Y.ravel()])

# --------------------------------------------------
# Mixtures
# --------------------------------------------------

mixtures = [

    ("100G", 1.00),
    ("75G25E", 0.75),
    ("50G50E", 0.50),
    ("25G75E", 0.25),
    ("100E", 0.00),
]

results = []

fig, axes = plt.subplots(
    1,
    5,
    figsize=(22,4)
)

for ax, (label, frac_ground) in zip(axes, mixtures):

    n = 50000

    ng = int(n * frac_ground)
    ne = n - ng

    idxg = np.random.choice(
        len(Ig),
        ng,
        replace=False
    )

    idxe = np.random.choice(
        len(Ie),
        ne,
        replace=False
    )

    I = np.concatenate([
        Ig[idxg],
        Ie[idxe]
    ])

    Q = np.concatenate([
        Qg[idxg],
        Qe[idxe]
    ])

    kde = gaussian_kde(
        np.vstack([I, Q])
    )

    Z = kde(POS).reshape(X.shape)

    ax.imshow(
        Z,
        origin="lower",
        aspect="auto"
    )

    ax.set_title(label)

    cx = np.mean(I)
    cy = np.mean(Q)

    results.append({

        "mixture": label,
        "ground_fraction": frac_ground,
        "centroid_I": float(cx),
        "centroid_Q": float(cy)
    })

plt.tight_layout()

plt.savefig(
    "QMVA-06A-State-Mixing-Atlas.png",
    dpi=300
)

with open(
    "QMVA-06A-State-Mixing.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-06A-State-Mixing-Atlas.png")
print("QMVA-06A-State-Mixing.json")
