import json
import matplotlib.pyplot as plt

with open(
    "QMVA-14A-Recovery.json"
) as f:

    data = json.load(f)

x = [
    d["detector_y"]
    for d in data
]

y = [
    d["predicted_ground"]
    for d in data
]

plt.figure(figsize=(8,5))

plt.plot(
    x,
    y,
    "o-"
)

plt.xlabel("Detector Y")
plt.ylabel("Predicted Ground Fraction")

plt.title(
    "QMVA-14B Detector-Only Recovery"
)

plt.grid(True)

plt.savefig(
    "QMVA-14B-RecoveryCurve.png",
    dpi=200
)

plt.close()

print(
    "Saved QMVA-14B-RecoveryCurve.png"
)
