from scipy.io import loadmat
import numpy as np

d = loadmat(
"runtime-audit/datasets/ISTA-AllOptical-Readout/AllopticalSCQreadout_data/Fig_4a/IQblobs_0Hz.mat"
)

theta = d["angle"][0,0]
threshold = d["threshold"][0,0]

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

Rg = Ig*np.cos(theta) - Qg*np.sin(theta)
Re = Ie*np.cos(theta) - Qe*np.sin(theta)

all_points = np.concatenate([Rg, Re])

hist, _ = np.histogram(all_points, bins=200)

p = hist / np.sum(hist)
p = p[p > 0]

H_detector = -np.sum(p * np.log2(p))

print()
print("Detector Entropy")
print("----------------")
print(H_detector)
print()
