from scipy.io import loadmat
import numpy as np

d = loadmat("IQblobs_0Hz.mat")

print("\nVARIABLES\n")

for k in d:

    if k.startswith("__"):
        continue

    x = d[k]

    print()
    print(k)

    print("shape =", x.shape)

    try:
        print("min =", np.min(x))
        print("max =", np.max(x))
        print("mean =", np.mean(x))
        print("std =", np.std(x))
    except:
        pass
