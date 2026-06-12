import json
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from scipy.io import loadmat

# ---------------------------------------
# Locate dataset
# ---------------------------------------

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

# ---------------------------------------
# Load
# ---------------------------------------

d = loadmat(DATA)

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

# ---------------------------------------
# Detector lattice
# ---------------------------------------

BINS = 128

Iall = np.concatenate([Ig, Ie])
Qall = np.concatenate([Qg, Qe])

xmin = np.min(Iall)
xmax = np.max(Iall)

ymin = np.min(Qall)
ymax = np.max(Qall)

fractions = np.linspace(0,1,11)

hyper = []

fig, axes = plt.subplots(
    2,
    6,
    figsize=(18,6)
)

axes = axes.ravel()

summary = []

for ax, frac in zip(axes, fractions):

    N = 50000

    ng = int(N * frac)
    ne = N - ng

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

    H, xe, ye = np.histogram2d(
        I,
        Q,
        bins=BINS,
        range=[
            [xmin,xmax],
            [ymin,ymax]
        ]
    )

    hyper.append(H)

    ax.imshow(
        H.T,
        origin="lower"
    )

    ax.set_title(
        f"{int(frac*100)}G"
    )

    y,x = np.indices(H.shape)

    total = H.sum()

    cx = (x*H).sum()/total
    cy = (y*H).sum()/total

    summary.append({

        "ground_fraction":
            float(frac),

        "centroid_x":
            float(cx),

        "centroid_y":
            float(cy)
    })

plt.tight_layout()

plt.savefig(
    "QMVA-07B-Occupancy-Field.png",
    dpi=300
)

hyper = np.array(hyper)

np.save(
    "QMVA-07B-HyperVolume.npy",
    hyper
)

with open(
    "QMVA-07B-summary.json",
    "w"
) as f:

    json.dump(
        summary,
        f,
        indent=2
    )

print()
print("Hypervolume shape:")
print(hyper.shape)

print()
print("Saved:")
print("QMVA-07B-Occupancy-Field.png")
print("QMVA-07B-HyperVolume.npy")
print("QMVA-07B-summary.json")
