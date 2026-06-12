import json
import numpy as np
from scipy.io import loadmat
from pathlib import Path

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

d = loadmat(DATA)

I_g = d["I_g"].flatten()
Q_g = d["Q_g"].flatten()

I_e = d["I_e"].flatten()
Q_e = d["Q_e"].flatten()

cx_g = np.mean(I_g)
cy_g = np.mean(Q_g)

cx_e = np.mean(I_e)
cy_e = np.mean(Q_e)

sep = np.sqrt(
    (cx_g-cx_e)**2 +
    (cy_g-cy_e)**2
)

result = {

    "ground_centroid":
        [float(cx_g), float(cy_g)],

    "excited_centroid":
        [float(cx_e), float(cy_e)],

    "manifold_separation":
        float(sep),

    "ground_entropy":
        float(np.log2(len(I_g))),

    "excited_entropy":
        float(np.log2(len(I_e)))
}

print()
print("=== QMVA-05C Detector Manifolds ===")
print()

print(
    json.dumps(
        result,
        indent=2
    )
)

with open(
    "QMVA-05C-manifolds.json",
    "w"
) as f:

    json.dump(
        result,
        f,
        indent=2
    )
