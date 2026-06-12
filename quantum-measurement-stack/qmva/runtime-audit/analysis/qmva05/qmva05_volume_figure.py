import numpy as np
import matplotlib.pyplot as plt

V = np.load("QMVA-05A-DPDV.npy")

frames = [0,25,50,75,99]

for f in frames:

    plt.figure(figsize=(6,5))

    plt.imshow(
        V[f],
        origin="lower",
        aspect="auto"
    )

    plt.colorbar()

    plt.title(
        f"Detector Plane Frame {f}"
    )

    plt.tight_layout()

    out = f"QMVA-05-frame-{f}.png"

    plt.savefig(
        out,
        dpi=300
    )

    print("Saved:", out)

