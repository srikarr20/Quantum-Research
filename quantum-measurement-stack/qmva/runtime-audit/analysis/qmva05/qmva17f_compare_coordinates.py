import json
import numpy as np

D = json.load(
    open(
        "QMVA-17A-DetectorTopology.json"
    )
)

Q = json.load(
    open(
        "QMVA-17B-IQTopology.json"
    )
)

print()
print("Mix    DetectorX      IQX")

for i in range(len(D)):

    dx = D[i]["centroid_x"]
    qx = Q[i]["centroid_x"]

    print(
        f"{i:2d}   "
        f"{dx:10.6f}   "
        f"{qx: .8e}"
    )
