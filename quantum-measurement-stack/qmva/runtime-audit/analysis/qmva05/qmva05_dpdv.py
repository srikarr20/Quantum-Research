import json
import numpy as np

from pathlib import Path
from scipy.io import loadmat

# --------------------------------------------------
# FIND DATASET
# --------------------------------------------------

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

# --------------------------------------------------
# LOAD
# --------------------------------------------------

d = loadmat(DATA)

I_g = d["I_g"].flatten()
Q_g = d["Q_g"].flatten()

I_e = d["I_e"].flatten()
Q_e = d["Q_e"].flatten()

I = np.concatenate([I_g, I_e])
Q = np.concatenate([Q_g, Q_e])

# --------------------------------------------------
# DPDV PARAMETERS
# --------------------------------------------------

N_FRAMES = 100
SHOTS_PER_FRAME = len(I) // N_FRAMES

GRID = 64

# --------------------------------------------------
# BUILD VOLUME
# --------------------------------------------------

volume = []

for frame in range(N_FRAMES):

    start = frame * SHOTS_PER_FRAME
    stop = start + SHOTS_PER_FRAME

    Ii = I[start:stop]
    Qi = Q[start:stop]

    H, xe, ye = np.histogram2d(
        Ii,
        Qi,
        bins=GRID
    )

    volume.append(H)

volume = np.array(volume)

print()
print("Volume shape:")
print(volume.shape)

# --------------------------------------------------
# SAVE
# --------------------------------------------------

np.save(
    "QMVA-05A-DPDV.npy",
    volume
)

meta = {

    "frames": int(volume.shape[0]),
    "grid_x": int(volume.shape[1]),
    "grid_y": int(volume.shape[2]),
    "shots": int(len(I))
}

with open(
    "QMVA-05A-DPDV.json",
    "w"
) as f:

    json.dump(meta, f, indent=2)

print()
print("Saved:")
print("QMVA-05A-DPDV.npy")
print("QMVA-05A-DPDV.json")
