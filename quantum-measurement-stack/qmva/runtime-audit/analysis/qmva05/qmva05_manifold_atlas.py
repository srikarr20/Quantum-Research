import numpy as np
import matplotlib.pyplot as plt

from scipy.io import loadmat
from scipy.stats import gaussian_kde
from pathlib import Path

ROOT = Path(__file__).resolve()

DATA = None

for parent in ROOT.parents:
    candidate = (
        parent
        / "datasets"
        / "ISTA-AllOptical-Readout"
        / "AllopticalSCQreadout_data"
        / "Fig_4a"
        / "IQblobs_0Hz.mat"
    )

    if candidate.exists():
        DATA = candidate
        break

if DATA is None:
    raise RuntimeError("Could not locate IQblobs_0Hz.mat")

print("Using:", DATA)

d = loadmat(DATA)

I_g = d["I_g"].flatten()
Q_g = d["Q_g"].flatten()

I_e = d["I_e"].flatten()
Q_e = d["Q_e"].flatten()

I_all = np.concatenate([I_g, I_e])
Q_all = np.concatenate([Q_g, Q_e])

xmin, xmax = np.min(I_all), np.max(I_all)
ymin, ymax = np.min(Q_all), np.max(Q_all)

GRID = 200

x = np.linspace(xmin, xmax, GRID)
y = np.linspace(ymin, ymax, GRID)

X, Y = np.meshgrid(x, y)

POS = np.vstack([X.ravel(), Y.ravel()])

kg = gaussian_kde(np.vstack([I_g, Q_g]))
ke = gaussian_kde(np.vstack([I_e, Q_e]))

Zg = kg(POS).reshape(X.shape)
Ze = ke(POS).reshape(X.shape)

Zd = Ze - Zg

cgx = np.mean(I_g)
cgy = np.mean(Q_g)

cex = np.mean(I_e)
cey = np.mean(Q_e)

fig, ax = plt.subplots(
    2,
    2,
    figsize=(12,10)
)

im0 = ax[0,0].imshow(
    Zg,
    origin="lower",
    aspect="auto"
)
ax[0,0].set_title("Ground Detector Manifold")
plt.colorbar(im0, ax=ax[0,0])

im1 = ax[0,1].imshow(
    Ze,
    origin="lower",
    aspect="auto"
)
ax[0,1].set_title("Excited Detector Manifold")
plt.colorbar(im1, ax=ax[0,1])

im2 = ax[1,0].imshow(
    Zd,
    origin="lower",
    aspect="auto"
)
ax[1,0].set_title("Difference Map")
plt.colorbar(im2, ax=ax[1,0])

ax[1,1].scatter(
    I_g,
    Q_g,
    s=1,
    alpha=0.1,
    label="Ground"
)

ax[1,1].scatter(
    I_e,
    Q_e,
    s=1,
    alpha=0.1,
    label="Excited"
)

ax[1,1].scatter(
    [cgx],
    [cgy],
    s=150,
    marker="x",
    label="Ground Centroid"
)

ax[1,1].scatter(
    [cex],
    [cey],
    s=150,
    marker="x",
    label="Excited Centroid"
)

ax[1,1].plot(
    [cgx, cex],
    [cgy, cey],
    linewidth=2
)

ax[1,1].legend()
ax[1,1].set_title("Detector Manifold Atlas")

plt.tight_layout()

plt.savefig(
    "QMVA-05D-Detector-Manifold-Atlas.png",
    dpi=300
)

print()
print("Saved:")
print("QMVA-05D-Detector-Manifold-Atlas.png")
