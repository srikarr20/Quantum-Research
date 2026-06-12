import numpy as np
import json

detector = np.load(
    "QMVA-07C-HyperVolume.npy"
)

detector_values = int(np.prod(detector.shape))

daq_values = 4 * 50000

ratio = detector_values / daq_values

result = {

    "detector_shape":
        list(detector.shape),

    "detector_values":
        detector_values,

    "daq_values":
        daq_values,

    "information_ratio":
        ratio
}

with open(
    "QMVA-16E-InformationBudget.json",
    "w"
) as f:

    json.dump(
        result,
        f,
        indent=2
    )

print(json.dumps(result,indent=2))
