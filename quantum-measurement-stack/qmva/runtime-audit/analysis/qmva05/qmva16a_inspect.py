import numpy as np

for f in [
    "QMVA-05B-fixed-volume.npy",
    "QMVA-07A-HyperVolume.npy",
    "QMVA-07B-HyperVolume.npy",
    "QMVA-07C-HyperVolume.npy"
]:

    try:
        x=np.load(f)

        print()
        print(f)
        print("shape =",x.shape)
        print("dtype =",x.dtype)

    except Exception as e:
        print(f,e)
