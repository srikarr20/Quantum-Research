import json
import matplotlib.pyplot as plt

with open("../../artifacts/QMVA-04C-confidence-gating.json") as f:
    data = json.load(f)

retention = [100 * d["retention"] for d in data]
error = [100 * d["total_error"] for d in data]
labels = [f"z≥{d['z_cut']:.0f}σ" for d in data]

plt.figure(figsize=(8,5))

plt.plot(
    retention,
    error,
    "o-",
    linewidth=2,
    markersize=8
)

for x, y, label in zip(retention, error, labels):
    plt.annotate(
        label,
        (x, y),
        textcoords="offset points",
        xytext=(8,8)
    )

plt.xlabel("Measurement Retention (%)")
plt.ylabel("Classification Error (%)")
plt.title("QMVA-04C Accuracy–Retention Frontier")

plt.grid(alpha=0.3)
plt.tight_layout()

OUT = "../../artifacts/QMVA-04C-AccuracyRetention.png"

plt.savefig(OUT, dpi=300)

print()
print("Saved:")
print(OUT)

plt.show()
