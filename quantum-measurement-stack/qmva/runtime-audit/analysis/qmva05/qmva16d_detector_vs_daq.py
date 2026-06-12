import numpy as np
import json
from scipy.io import loadmat
from scipy.stats import entropy

# ------------------------------------
# DETECTOR SIDE
# ------------------------------------

V = np.load(
    "QMVA-07C-HyperVolume.npy"
)

detector_entropy = []

for mix in range(V.shape[0]):

    volume = V[mix]

    p = volume.flatten()

    p = p / p.sum()

    detector_entropy.append(
        entropy(p)
    )

detector_entropy_span = (
    max(detector_entropy)
    -
    min(detector_entropy)
)

# ------------------------------------
# DAQ SIDE
# ------------------------------------

d = loadmat(
    "../../../datasets/ISTA-AllOptical-Readout/AllopticalSCQreadout_data/Fig_4a/IQblobs_0Hz.mat"
)

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

daq_entropy = []

fractions = np.linspace(
    0,
    1,
    11
)

for frac in fractions:

    ng = int(
        frac * 50000
    )

    ne = 50000 - ng

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

    H,_,_ = np.histogram2d(
        I,
        Q,
        bins=64
    )

    p = H.flatten()

    p = p / p.sum()

    daq_entropy.append(
        entropy(p)
    )

daq_entropy_span = (
    max(daq_entropy)
    -
    min(daq_entropy)
)

# ------------------------------------
# SAVE
# ------------------------------------

result = {

    "detector_entropy_span":
        float(detector_entropy_span),

    "daq_entropy_span":
        float(daq_entropy_span),

    "detector_entropy":
        detector_entropy,

    "daq_entropy":
        daq_entropy
}

with open(
    "QMVA-16D-DetectorVsDAQ.json",
    "w"
) as f:

    json.dump(
        result,
        f,
        indent=2
    )

print()
print(
    json.dumps(
        result,
        indent=2
    )
)
