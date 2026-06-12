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

Dg = Rg - threshold
De = Re - threshold

print()
print("Ground Distance Statistics")
print("--------------------------")
print("Mean:", np.mean(np.abs(Dg)))
print("Median:", np.median(np.abs(Dg)))
print()

print("Excited Distance Statistics")
print("---------------------------")
print("Mean:", np.mean(np.abs(De)))
print("Median:", np.median(np.abs(De)))
print()

near = np.sum(np.abs(np.concatenate([Dg,De])) < 1e-5)

print("Near-threshold shots:", near)
print("Total shots:", len(Dg)+len(De))
print("Fraction:", near/(len(Dg)+len(De)))
