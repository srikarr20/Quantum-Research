import json
import numpy as np

from pathlib import Path
from scipy.io import loadmat

# -----------------------------------------
# Locate dataset
# -----------------------------------------

ROOT = Path(__file__).resolve()

DATA = None

for parent in ROOT.parents:

    candidate = (
        parent
        / "runtime-audit"
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

# -----------------------------------------
# Load
# -----------------------------------------

d = loadmat(DATA)

I_g = d["I_g"].flatten()
Q_g = d["Q_g"].flatten()

I_e = d["I_e"].flatten()
Q_e = d["Q_e"].flatten()

I = np.concatenate([I_g, I_e])
Q = np.concatenate([Q_g, Q_e])

# -----------------------------------------
# Global detector plane
# -----------------------------------------

Imin = np.min(I)
Imax = np.max(I)

Qmin = np.min(Q)
Qmax = np.max(Q)

# -----------------------------------------
# Build volume
# -----------------------------------------

N_FRAMES = 100
GRID = 64

shots_per_frame = len(I) // N_FRAMES

volume = []

for frame in range(N_FRAMES):

    start = frame * shots_per_frame
    stop = start + shots_per_frame

    Ii = I[start:stop]
    Qi = Q[start:stop]

    H, _, _ = np.histogram2d(
        Ii,
        Qi,
        bins=GRID,
        range=[
            [Imin, Imax],
            [Qmin, Qmax]
        ]
    )

    volume.append(H)

volume = np.array(volume)

np.save(
    "QMVA-05B-fixed-volume.npy",
    volume
)

meta = {
    "shape": list(volume.shape),
    "Imin": float(Imin),
    "Imax": float(Imax),
    "Qmin": float(Qmin),
    "Qmax": float(Qmax)
}

with open(
    "QMVA-05B-fixed-volume.json",
    "w"
) as f:
    json.dump(meta, f, indent=2)

print()
print("Volume shape:")
print(volume.shape)

print()
print("Saved:")
print("QMVA-05B-fixed-volume.npy")
