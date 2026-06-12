import json
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------
# Load detector volume
# ---------------------------------------

V = np.load("QMVA-05A-DPDV.npy")

print("Volume shape:", V.shape)

# (100,64,64)

flow = []

left_occ = []
right_occ = []

for frame in V:

    nx = frame.shape[1]

    # detector split

    left = frame[:, :nx//2]
    right = frame[:, nx//2:]

    L = float(left.sum())
    R = float(right.sum())

    left_occ.append(L)
    right_occ.append(R)

    total = L + R

    if total > 0:
        flow.append(R / total)
    else:
        flow.append(0.0)

flow = np.array(flow)

# ---------------------------------------
# Metrics
# ---------------------------------------

results = {

    "flow_mean":
        float(np.mean(flow)),

    "flow_std":
        float(np.std(flow)),

    "flow_min":
        float(np.min(flow)),

    "flow_max":
        float(np.max(flow))
}

print()
print(json.dumps(results, indent=2))

# ---------------------------------------
# Plot
# ---------------------------------------

plt.figure(figsize=(10,5))

plt.plot(flow)

plt.xlabel("Frame")
plt.ylabel("Right Occupancy Fraction")

plt.title(
    "QMVA-08A Detector Occupancy Flow"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "QMVA-08A-Occupancy-Flow.png",
    dpi=300
)

# ---------------------------------------
# Save
# ---------------------------------------

np.save(
    "QMVA-08A-flow.npy",
    flow
)

with open(
    "QMVA-08A-flow.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-08A-Occupancy-Flow.png")
print("QMVA-08A-flow.npy")
print("QMVA-08A-flow.json")
