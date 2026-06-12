from scipy.io import loadmat
import numpy as np

freqs = [0,10,50,250,500,1000]

print()
print("Freq(Hz)   Error      VRI       QNDFid")
print("-----------------------------------------")

for f in freqs:

    fn = f"runtime-audit/datasets/ISTA-AllOptical-Readout/AllopticalSCQreadout_data/Fig_4a/IQblobs_{f}Hz.mat"

    d = loadmat(fn)

    theta = float(d["angle"])
    threshold = float(d["threshold"])

    Ig = d["I_g"].flatten()
    Qg = d["Q_g"].flatten()

    Ie = d["I_e"].flatten()
    Qe = d["Q_e"].flatten()

    Rg = Ig*np.cos(theta) - Qg*np.sin(theta)
    Re = Ie*np.cos(theta) - Qe*np.sin(theta)

    gerr = np.mean(Rg > threshold)
    eerr = np.mean(Re < threshold)

    err = (gerr + eerr)/2
    vri = 1 - err

    qnd = float(d["QNDFid"])

    print(f"{f:7d}   {err:0.5f}   {vri:0.5f}   {qnd:0.5f}")
