import numpy as np

files = [
    "QMVA-05A-DPDV.npy",
    "QMVA-05B-fixed-volume.npy",
    "QMVA-07A-HyperVolume.npy",
    "QMVA-07B-HyperVolume.npy",
    "QMVA-07C-HyperVolume.npy"
]

for f in files:

    try:

        x = np.load(f)

        print()
        print(f)

        print("shape =", x.shape)

        if len(x.shape) >= 3:

            print(
                "frame mean std =",
                np.std(
                    x.reshape(
                        x.shape[0],
                        -1
                    ).mean(axis=1)
                )
            )

    except Exception as e:

        print(f,e)
