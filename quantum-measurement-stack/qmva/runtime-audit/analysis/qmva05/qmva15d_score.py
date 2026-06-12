import json
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

with open(
    "QMVA-15C-Recovery.json"
) as f:

    data = json.load(f)

truth = np.array([
    x["true_ground"]
    for x in data
])

pred = np.array([
    x["predicted_ground"]
    for x in data
])

mae = mean_absolute_error(
    truth,
    pred
)

rmse = np.sqrt(
    mean_squared_error(
        truth,
        pred
    )
)

r2 = r2_score(
    truth,
    pred
)

print()
print("QMVA-15 Blind Recovery")
print("----------------------")
print("MAE =", mae)
print("RMSE =", rmse)
print("R² =", r2)
