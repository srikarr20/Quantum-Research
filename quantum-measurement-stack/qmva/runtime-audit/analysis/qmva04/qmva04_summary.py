import json

with open("../../artifacts/QMVA-04C-confidence-gating.json") as f:
    data = json.load(f)

baseline = data[0]
best = data[1]   # z >= 1σ

improvement = (
    (baseline["total_error"] - best["total_error"])
    / baseline["total_error"]
)

summary = {
    "baseline_error":
        baseline["total_error"],

    "confidence_error":
        best["total_error"],

    "retention":
        best["retention"],

    "relative_error_reduction":
        improvement
}

print(json.dumps(summary, indent=2))

with open(
    "../../artifacts/QMVA-04-SUMMARY.json",
    "w"
) as f:
    json.dump(summary, f, indent=2)
