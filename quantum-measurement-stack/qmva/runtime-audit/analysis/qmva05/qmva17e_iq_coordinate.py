import json
import numpy as np
from scipy.stats import spearmanr
from sklearn.metrics import r2_score

Q = json.load(
    open(
        "QMVA-17B-IQTopology.json"
    )
)

mix = np.linspace(
    0,
    1,
    len(Q)
)

coord = np.array([
    x["centroid_x"]
    for x in Q
])

coord = (
    coord - coord.min()
) / (
    coord.max() - coord.min()
)

rho,_ = spearmanr(
    mix,
    coord
)

r2 = r2_score(
    mix,
    coord
)

print()
print("IQ Coordinate")
print("-------------")
print("Spearman rho =",rho)
print("R² =",r2)
