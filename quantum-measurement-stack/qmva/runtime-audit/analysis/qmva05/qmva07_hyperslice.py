import numpy as np
import matplotlib.pyplot as plt

H = np.load(
    "QMVA-07C-HyperVolume.npy"
)

print(H.shape)

# ----------------------------------------
# Fix y slice
# ----------------------------------------

y0 = 32

slice_data = H[:,:,:,y0]

# shape:
# mixture,time,x

# average over x for display

display = slice_data.mean(axis=2)

plt.figure(figsize=(10,6))

plt.imshow(
    display,
    aspect="auto",
    origin="lower"
)

plt.xlabel("Time Frame")
plt.ylabel("Ground Fraction Index")

plt.title(
    "QMVA-07D Detector HyperSlice"
)

plt.colorbar()

plt.tight_layout()

plt.savefig(
    "QMVA-07D-HyperSlice.png",
    dpi=300
)

print()
print("Saved:")
print("QMVA-07D-HyperSlice.png")
