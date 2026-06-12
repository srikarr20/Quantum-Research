import json
import numpy as np
from scipy.io import loadmat
from scipy.stats import entropy

d = loadmat(
    "IQblobs_0Hz.mat"
)

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

fractions = np.linspace(
    0,
    1,
    11
)

results = []

for i,f in enumerate(fractions):

    ng = int(f*50000)
    ne = 50000-ng

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

    H2d,xe,ye = np.histogram2d(
        I,
        Q,
        bins=64
    )

    p = H2d.flatten()

    p = p/p.sum()

    H = entropy(p)

    cx = np.mean(I)
    cy = np.mean(Q)

    radius = np.mean(
        np.sqrt(
            (I-cx)**2 +
            (Q-cy)**2
        )
    )

    results.append({

        "mix": int(i),
        "entropy": float(H),
        "centroid_x": float(cx),
        "centroid_y": float(cy),
        "radius": float(radius)
    })

with open(
    "QMVA-17B-IQTopology.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print(
    json.dumps(
        results,
        indent=2
    )
)
