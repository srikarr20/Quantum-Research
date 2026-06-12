import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from scipy.io import loadmat

# ---------------------------------------
# locate dataset
# ---------------------------------------

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

d = loadmat(DATA)

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

fractions = np.linspace(0,1,11)

for frac in fractions:

    ng = int(50000 * frac)
    ne = 50000 - ng

    idxg = np.random.choice(len(Ig), ng, replace=False)
    idxe = np.random.choice(len(Ie), ne, replace=False)

    I = np.concatenate([
        Ig[idxg],
        Ie[idxe]
    ])

    Q = np.concatenate([
        Qg[idxg],
        Qe[idxe]
    ])

    # -----------------------------------
    # Original IQ density
    # -----------------------------------

    IQ, xedges, yedges = np.histogram2d(
        I,
        Q,
        bins=128
    )

    # -----------------------------------
    # Detector field
    # -----------------------------------

    DET, _, _ = np.histogram2d(
        I,
        Q,
        bins=64
    )

    # -----------------------------------
    # Reconstruction
    # -----------------------------------

    RECON = np.kron(
        DET,
        np.ones((2,2))
    )

    # -----------------------------------
    # Plot
    # -----------------------------------

    fig, ax = plt.subplots(
        1,
        3,
        figsize=(15,5)
    )

    ax[0].imshow(
        IQ.T,
        origin="lower",
        aspect="auto"
    )
    ax[0].set_title(
        "Original IQ"
    )

    ax[1].imshow(
        DET.T,
        origin="lower",
        aspect="auto"
    )
    ax[1].set_title(
        "Detector Plane"
    )

    ax[2].imshow(
        RECON.T,
        origin="lower",
        aspect="auto"
    )
    ax[2].set_title(
        "Reconstructed IQ"
    )

    plt.suptitle(
        f"{int(frac*100)}G"
    )

    plt.tight_layout()

    plt.savefig(
        f"QMVA11A-{int(frac*100):03d}G.png",
        dpi=200
    )

    plt.close()

print("Done.")
