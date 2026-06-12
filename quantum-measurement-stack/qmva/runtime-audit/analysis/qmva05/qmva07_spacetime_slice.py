import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------
# Load hypervolume
# ---------------------------------------

H = np.load(
    "QMVA-07C-HyperVolume.npy"
)

print("Hypervolume shape:")
print(H.shape)

# Expected:
# (11,100,64,64)

# ---------------------------------------
# Fixed detector row
# ---------------------------------------

y0 = 32

# ---------------------------------------
# Build spacetime slices
# ---------------------------------------

fig, axes = plt.subplots(
    3,
    4,
    figsize=(16,10)
)

axes = axes.ravel()

for m in range(11):

    ax = axes[m]

    # shape:
    # time,x

    spacetime = H[m,:,y0,:]

    ax.imshow(
        spacetime,
        aspect="auto",
        origin="lower",
        cmap="viridis"
    )

    ax.set_title(
        f"{m*10}G"
    )

    ax.set_xlabel("Detector X")

    ax.set_ylabel("Time")

# remove empty panel

axes[-1].axis("off")

plt.tight_layout()

plt.savefig(
    "QMVA-07E-Spacetime-Slices.png",
    dpi=300
)

print()
print("Saved:")
print("QMVA-07E-Spacetime-Slices.png")
