import json
import numpy as np
from sklearn.linear_model import LinearRegression

ground = np.array([
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

detector = np.array([
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
    detector.reshape(-1,1),
    ground
)

with open(
    "QMVA-15B-DetectorData.json"
) as f:

    data = json.load(f)

predictions = []

for row in data:

    pred = model.predict(
        [[row["detector_y"]]]
    )[0]

    predictions.append({
        "true_ground":
            row["true_ground"],
        "predicted_ground":
            float(pred)
    })

with open(
    "QMVA-15C-Recovery.json",
    "w"
) as f:

    json.dump(
        predictions,
        f,
        indent=2
    )

print("Saved QMVA-15C-Recovery.json")

