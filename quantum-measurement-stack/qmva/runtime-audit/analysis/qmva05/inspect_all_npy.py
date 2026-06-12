import numpy as np
import glob

for f in sorted(glob.glob("*.npy")):

    x = np.load(f)

    print()
    print("="*60)
    print(f)
    print("="*60)

    print("shape =", x.shape)
    print("dtype =", x.dtype)

    print("min =", x.min())
    print("max =", x.max())
    print("mean =", x.mean())
    print("std =", x.std())
