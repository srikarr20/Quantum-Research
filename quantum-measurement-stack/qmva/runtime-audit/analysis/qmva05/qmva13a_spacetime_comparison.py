import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np

fractions = [
    "000","010","020","030","040",
    "050","060","070","080","090","100"
]

frames = []

for frac in fractions:

    img = imageio.imread(
        f"QMVA11A-{frac}G.png"
    )

    fig, ax = plt.subplots(
        1,1,
        figsize=(12,4)
    )

    ax.imshow(img)

    ax.set_title(
        f"Ground Fraction {int(frac)}%"
    )

    ax.axis("off")

    tmp = f"_tmp_{frac}.png"

    plt.savefig(
        tmp,
        bbox_inches="tight"
    )

    plt.close()

    frames.append(
        imageio.imread(tmp)
    )

imageio.mimsave(
    "QMVA-13A-SpacetimeComparison.gif",
    frames,
    duration=1.0
)

print()
print("Saved:")
print("QMVA-13A-SpacetimeComparison.gif")
