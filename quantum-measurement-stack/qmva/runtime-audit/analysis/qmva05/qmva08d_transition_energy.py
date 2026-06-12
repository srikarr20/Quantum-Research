import json
import numpy as np
import matplotlib.pyplot as plt

V = np.load("QMVA-05B-fixed-volume.npy")

print("Volume shape:", V.shape)

energy = []

for i in range(1, len(V)):
    e = np.sum(np.abs(V[i] - V[i - 1]))
    energy.append(e)

energy = np.array(energy)

peak_idx = int(np.argmax(energy)) + 1
peak_energy = float(np.max(energy))

baseline = float(np.median(energy))
ratio = peak_energy / baseline

results = {
    "peak_frame": peak_idx,
    "peak_energy": peak_energy,
    "baseline_energy": baseline,
    "peak_to_baseline_ratio": ratio
}

print("\n=== QMVA-08D Transition Energy ===\n")
print(json.dumps(results, indent=2))

with open("QMVA-08D-transition-energy.json", "w") as f:
    json.dump(results, f, indent=2)

plt.figure(figsize=(10,5))

plt.plot(np.arange(1, len(V)), energy, lw=2)

plt.axvline(
    peak_idx,
    color="red",
    linestyle="--",
    label=f"Peak Frame {peak_idx}"
)

plt.xlabel("Frame")
plt.ylabel("Transition Energy")
plt.title("QMVA-08D Detector Transition Energy")

plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "QMVA-08D-Transition-Energy.png",
    dpi=300
)

plt.close()

print("\nSaved:")
print("QMVA-08D-transition-energy.json")
print("QMVA-08D-Transition-Energy.png")
