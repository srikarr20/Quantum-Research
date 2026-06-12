import imageio.v2 as imageio

frames = []

for g in range(0,101,10):

    frames.append(
        imageio.imread(
            f"QMVA11A-{g:03d}G.png"
        )
    )

imageio.mimsave(
    "QMVA11B-DetectorMovie.gif",
    frames,
    duration=0.8
)

print("Saved QMVA11B-DetectorMovie.gif")
