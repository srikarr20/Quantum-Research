import json
import matplotlib.pyplot as plt

# ----------------------------------------
# LOAD RESULTS
# ----------------------------------------

with open("../../artifacts/QMVA-04B-variance-test.json") as f:
    data = json.load(f)

noise = [d["noise"] for d in data]
binary_std = [d["binary_std"] for d in data]
prob_std = [d["prob_std"] for d in data]

# ----------------------------------------
# PLOT
# ----------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    noise,
    binary_std,
    "o-",
    linewidth=2,
    label="Binary Threshold"
)

plt.plot(
    noise,
    prob_std,
    "s-",
    linewidth=2,
    label="Confidence-Aware"
)

plt.xlabel("Detector Noise")
plt.ylabel("Estimator Standard Deviation")
plt.title("QMVA-04B Variance Reduction Under Noise")

plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()

OUT = "../../artifacts/QMVA-04B-VarianceReduction.png"

plt.savefig(OUT, dpi=300)

print()
print("Saved:")
print(OUT)

plt.show()
