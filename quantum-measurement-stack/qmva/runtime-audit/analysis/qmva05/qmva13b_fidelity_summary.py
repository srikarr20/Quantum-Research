import json

summary = {

    "QMVA09C": {
        "spearman_rho": 1.0,
        "r2": 0.9904
    },

    "QMVA10A": {
        "mae": 0.0293,
        "rmse": 0.0375,
        "r2": 0.9847
    },

    "QMVA12A": {
        "blind_prediction_r2": 0.9898
    }

}

with open(
    "QMVA-13B-FidelitySummary.json",
    "w"
) as f:

    json.dump(
        summary,
        f,
        indent=2
    )

print("Saved QMVA-13B-FidelitySummary.json")
