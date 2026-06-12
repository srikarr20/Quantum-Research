import numpy as np
import matplotlib.pyplot as plt

V = np.load(
    "QMVA-05B-fixed-volume.npy"
)

cxs = []
cys = []

for frame in V:

    total = frame.sum()

    y,x = np.indices(frame.shape)

    cx = (x * frame).sum() / total
    cy = (y * frame).sum() / total

    cxs.append(cx)
    cys.append(cy)

plt.figure(figsize=(8,5))

plt.plot(
    cxs,
    label="Centroid X"
)

plt.plot(
    cys,
    label="Centroid Y"
)

plt.xlabel("Frame")
plt.ylabel("Detector Centroid")

plt.title(
    "QMVA-05B Detector Plane Drift"
)

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "QMVA-05B-Centroid-Drift.png",
    dpi=300
)

print()
print("Saved:")
print("QMVA-05B-Centroid-Drift.png")
