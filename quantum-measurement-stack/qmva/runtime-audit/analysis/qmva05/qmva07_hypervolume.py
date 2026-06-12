import json
import numpy as np

# ----------------------------------------
# Load detector volume
# ----------------------------------------

V = np.load("QMVA-05A-DPDV.npy")

print("Base volume shape:", V.shape)

# (100,64,64)

# ----------------------------------------
# Mixtures
# ----------------------------------------

fractions = np.linspace(0,1,11)

hyper = []

summary = []

for frac in fractions:

    # occupancy transfer model

    mixed = (
        frac * V
        +
        (1-frac) * np.flip(V, axis=2)
    )

    hyper.append(mixed)

    total = mixed.sum()

    t,y,x = np.indices(mixed.shape)

    cx = float((x*mixed).sum()/total)
    cy = float((y*mixed).sum()/total)

    summary.append({

        "ground_fraction": float(frac),
        "centroid_x": cx,
        "centroid_y": cy
    })

hyper = np.array(hyper)

print("Hypervolume shape:")
print(hyper.shape)

np.save(
    "QMVA-07C-HyperVolume.npy",
    hyper
)

with open(
    "QMVA-07C-summary.json",
    "w"
) as f:

    json.dump(
        summary,
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-07C-HyperVolume.npy")
print("QMVA-07C-summary.json")
