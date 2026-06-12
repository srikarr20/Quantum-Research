import json

hidden_states = [
    0.07,
    0.13,
    0.22,
    0.41,
    0.58,
    0.73,
    0.91
]

with open(
    "QMVA-15A-HiddenStates.json",
    "w"
) as f:
    json.dump(
        hidden_states,
        f,
        indent=2
    )

print("Saved QMVA-15A-HiddenStates.json")
