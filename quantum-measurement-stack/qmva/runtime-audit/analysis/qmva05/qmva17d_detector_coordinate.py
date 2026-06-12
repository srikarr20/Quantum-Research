import json
import numpy as np
from scipy.stats import spearmanr
from sklearn.metrics import r2_score

D = json.load(
    open(
        "QMVA-17A-DetectorTopology.json"
    )
)

mix = np.linspace(
    0,
    1,
    len(D)
)

coord = np.array([
    x["centroid_x"]
    for x in D
])

coord = (
    coord - coord.min()
) / (
    coord.max() - coord.min()
)

coord = 1 - coord

rho,_ = spearmanr(
    mix,
    coord
)

r2 = r2_score(
    mix,
    coord
)

print()
print("Detector Coordinate")
print("-------------------")
print("Spearman rho =",rho)
print("R² =",r2)
