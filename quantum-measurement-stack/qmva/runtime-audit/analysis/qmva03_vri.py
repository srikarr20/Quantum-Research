from scipy.io import loadmat
import numpy as np

d = loadmat(
    "runtime-audit/datasets/ISTA-AllOptical-Readout/AllopticalSCQreadout_data/Fig_4a/IQblobs_0Hz.mat"
)

theta = float(d["angle"])
threshold = float(d["threshold"])

Ig = d["I_g"].flatten()
Qg = d["Q_g"].flatten()

Ie = d["I_e"].flatten()
Qe = d["Q_e"].flatten()

Rg = Ig*np.cos(theta) - Qg*np.sin(theta)
Re = Ie*np.cos(theta) - Qe*np.sin(theta)

ground_error = np.mean(Rg > threshold)
excited_error = np.mean(Re < threshold)

accuracy = 1 - (ground_error + excited_error)/2

print()
print("QMVA-03 Visibility Retention")
print("----------------------------")
print("Ground Error:", ground_error)
print("Excited Error:", excited_error)
print("Average Error:", (ground_error + excited_error)/2)
print("Visibility Retention Index:", accuracy)
print()
