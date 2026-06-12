import json
import numpy as np

V = np.load("QMVA-05A-DPDV.npy")

# --------------------------------------------------
# FRAME CORRELATION
# --------------------------------------------------

ref = V[0].flatten()

corr = []

for frame in V:

    c = np.corrcoef(
        ref,
        frame.flatten()
    )[0,1]

    corr.append(float(c))

# --------------------------------------------------
# ENTROPY
# --------------------------------------------------

entropy = []

for frame in V:

    p = frame.flatten()

    p = p / p.sum()

    p = p[p > 0]

    H = -np.sum(
        p * np.log2(p)
    )

    entropy.append(float(H))

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

result = {

    "frame_correlation_mean":
        float(np.mean(corr)),

    "frame_correlation_min":
        float(np.min(corr)),

    "frame_correlation_max":
        float(np.max(corr)),

    "entropy_mean":
        float(np.mean(entropy)),

    "entropy_std":
        float(np.std(entropy))
}

print()
print("=== QMVA-05 Dynamics ===")
print()

print(
    json.dumps(
        result,
        indent=2
    )
)

with open(
    "QMVA-05A-dynamics.json",
    "w"
) as f:

    json.dump(
        result,
        f,
        indent=2
    )
