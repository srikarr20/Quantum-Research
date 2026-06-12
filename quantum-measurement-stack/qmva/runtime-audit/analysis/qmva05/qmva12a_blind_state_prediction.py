import numpy as np
import json
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# -----------------------------------
# TRAINING DATA
# -----------------------------------

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

# -----------------------------------
# TRAIN MODEL
# -----------------------------------

model = LinearRegression()

model.fit(
    detector_y.reshape(-1,1),
    ground_fraction
)

train_pred = model.predict(
    detector_y.reshape(-1,1)
)

r2 = r2_score(
    ground_fraction,
    train_pred
)

print()
print("Training R² =", round(r2,4))
print()

# -----------------------------------
# HIDDEN TEST SET
# -----------------------------------

hidden_detector_y = np.array([
    24.7,
    27.5,
    31.5,
    35.1,
    38.2
])

predicted = model.predict(
    hidden_detector_y.reshape(-1,1)
)

print("Blind Predictions")
print("-----------------")

for d,p in zip(hidden_detector_y,predicted):

    print(
        f"DetectorY={d:.2f} -> Ground={p:.3f}"
    )

# -----------------------------------
# SAVE
# -----------------------------------

results = []

for d,p in zip(hidden_detector_y,predicted):

    results.append({
        "detector_y": float(d),
        "predicted_ground_fraction": float(p)
    })

with open(
    "QMVA-12A-blind-predictions.json",
    "w"
) as f:

    json.dump(
        {
            "training_r2": float(r2),
            "predictions": results
        },
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-12A-blind-predictions.json")
