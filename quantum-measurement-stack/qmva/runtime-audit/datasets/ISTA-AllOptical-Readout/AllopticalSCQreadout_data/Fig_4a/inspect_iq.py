from scipy.io import loadmat

files = [
    "IQblobs_0Hz.mat",
    "IQblobs_10Hz.mat",
    "IQblobs_50Hz.mat",
    "IQblobs_250Hz.mat",
    "IQblobs_500Hz.mat",
    "IQblobs_1000Hz.mat"
]

for f in files:

    print()
    print("="*70)
    print(f)
    print("="*70)

    d = loadmat(f)

    for k in sorted(d.keys()):

        if k.startswith("__"):
            continue

        try:
            print(
                k,
                d[k].shape,
                d[k].dtype
            )
        except:
            print(k)
