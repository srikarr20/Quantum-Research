import json
import numpy as np
import matplotlib.pyplot as plt

V = np.load("QMVA-05A-DPDV.npy")

peak_x = []
peak_y = []
peak_v = []

for frame in V:

    iy, ix = np.unravel_index(
        np.argmax(frame),
        frame.shape
    )

    peak_x.append(ix)
    peak_y.append(iy)
    peak_v.append(frame[iy,ix])

peak_x = np.array(peak_x)
peak_y = np.array(peak_y)

cx = np.mean(peak_x)
cy = np.mean(peak_y)

radius = np.sqrt(
    (peak_x-cx)**2
    +
    (peak_y-cy)**2
)

results = {

    "mean_peak_x": float(cx),
    "mean_peak_y": float(cy),

    "mean_radius":
        float(np.mean(radius)),

    "max_radius":
        float(np.max(radius)),

    "radius_std":
        float(np.std(radius))
}

print(json.dumps(results, indent=2))

plt.figure(figsize=(8,8))

plt.scatter(
    peak_x,
    peak_y,
    alpha=0.7
)

plt.scatter(
    [cx],
    [cy],
    marker="x",
    s=200
)

plt.xlabel("Detector X")
plt.ylabel("Detector Y")

plt.title(
    "QMVA-08B Manifold Persistence"
)

plt.tight_layout()

plt.savefig(
    "QMVA-08B-Manifold-Persistence.png",
    dpi=300
)

with open(
    "QMVA-08B-Manifold-Persistence.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-08B-Manifold-Persistence.png")
print("QMVA-08B-Manifold-Persistence.json")
