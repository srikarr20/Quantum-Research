import numpy as np
import json
from sklearn.linear_model import LinearRegression

# -----------------------------
# Training manifold
# -----------------------------

ground_fraction = np.array([
    0.0,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0
])

detector_y = np.array([
    20.9,
    23.2,
    26.0,
    28.4,
    29.8,
    33.3,
    34.5,
    37.0,
    39.6,
    40.0,
    41.8
])

model = LinearRegression()
model.fit(
    detector_y.reshape(-1,1),
    ground_fraction
)

# -----------------------------
# Hidden detector coordinates
# -----------------------------

hidden_detector_y = np.array([
    22.5,
    24.8,
    27.1,
    30.7,
    34.2,
    38.1,
    41.0
])

pred = model.predict(
    hidden_detector_y.reshape(-1,1)
)

results = []

print()
print("QMVA-14A Detector Recovery")
print("--------------------------")

for d,p in zip(hidden_detector_y,pred):

    print(
        f"DetectorY={d:.2f}"
        f"  Predicted Ground={p:.3f}"
    )

    results.append({
        "detector_y": float(d),
        "predicted_ground": float(p)
    })

with open(
    "QMVA-14A-Recovery.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-14A-Recovery.json")
