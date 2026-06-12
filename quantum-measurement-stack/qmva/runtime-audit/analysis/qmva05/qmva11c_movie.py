import imageio.v2 as imageio

images = [
    "QMVA11A-000G.png",
    "QMVA11A-010G.png",
    "QMVA11A-020G.png",
    "QMVA11A-030G.png",
    "QMVA11A-040G.png",
    "QMVA11A-050G.png",
    "QMVA11A-060G.png",
    "QMVA11A-070G.png",
    "QMVA11A-080G.png",
    "QMVA11A-090G.png",
    "QMVA11A-100G.png"
]

frames = []

for img in images:
    print("Loading:", img)
    frames.append(imageio.imread(img))

imageio.mimsave(
    "QMVA-11C-Detector-Reconstruction.gif",
    frames,
    duration=0.8
)

print()
print("Saved:")
print("QMVA-11C-Detector-Reconstruction.gif")
