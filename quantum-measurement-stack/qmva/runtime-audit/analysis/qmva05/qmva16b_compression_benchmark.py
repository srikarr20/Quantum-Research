import json
import numpy as np

from scipy.stats import entropy
from scipy.fftpack import dct, idct

# ---------------------------------
# Load detector manifold
# ---------------------------------

V = np.load(
    "QMVA-07C-HyperVolume.npy"
)

results = []

# ---------------------------------
# DCT compression helper
# ---------------------------------

def dct2(x):

    return dct(
        dct(
            x.T,
            norm="ortho"
        ).T,
        norm="ortho"
    )

def idct2(x):

    return idct(
        idct(
            x.T,
            norm="ortho"
        ).T,
        norm="ortho"
    )

# ---------------------------------
# Evaluate each mixture
# ---------------------------------

for mix in range(V.shape[0]):

    volume = V[mix]

    original = volume.mean(axis=0)

    # -----------------------------
    # DPI metrics
    # -----------------------------

    p = original.flatten()
    p = p / p.sum()

    H_original = entropy(p)

    # -----------------------------
    # Sparse reconstruction
    # -----------------------------

    C = dct2(original)

    flat = np.abs(C).flatten()

    thresh = np.percentile(
        flat,
        90
    )

    C_sparse = C.copy()

    C_sparse[
        np.abs(C_sparse) < thresh
    ] = 0

    recon = idct2(C_sparse)

    recon[recon < 0] = 0

    q = recon.flatten()

    q = q / q.sum()

    H_recon = entropy(q)

    # -----------------------------
    # retention
    # -----------------------------

    entropy_retention = (
        H_recon / H_original
    )

    mse = np.mean(
        (original - recon)**2
    )

    results.append({

        "mixture":
            int(mix),

        "entropy_original":
            float(H_original),

        "entropy_reconstructed":
            float(H_recon),

        "entropy_retention":
            float(entropy_retention),

        "mse":
            float(mse)
    })

# ---------------------------------
# Save
# ---------------------------------

with open(
    "QMVA-16B-CompressionBenchmark.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-16B-CompressionBenchmark.json")
