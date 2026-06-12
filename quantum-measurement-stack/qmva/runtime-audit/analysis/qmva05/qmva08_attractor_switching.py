import json
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------
# Load detector volume
# ---------------------------------------

V = np.load("QMVA-05A-DPDV.npy")

# ---------------------------------------
# Find peak location per frame
# ---------------------------------------

states = []

peak_x = []
peak_y = []

for frame in V:

    iy, ix = np.unravel_index(
        np.argmax(frame),
        frame.shape
    )

    peak_x.append(ix)
    peak_y.append(iy)

    # attractor assignment

    if iy > 30:
        states.append(1)  # upper
    else:
        states.append(0)  # lower

states = np.array(states)

# ---------------------------------------
# Occupancy fractions
# ---------------------------------------

upper_fraction = float(np.mean(states))
lower_fraction = 1.0 - upper_fraction

# ---------------------------------------
# Count switches
# ---------------------------------------

switches = np.sum(
    states[1:] != states[:-1]
)

# ---------------------------------------
# Dwell times
# ---------------------------------------

dwell_times = []

current = states[0]
length = 1

for s in states[1:]:

    if s == current:

        length += 1

    else:

        dwell_times.append(length)

        current = s
        length = 1

dwell_times.append(length)

dwell_times = np.array(dwell_times)

# ---------------------------------------
# Results
# ---------------------------------------

results = {

    "upper_fraction":
        upper_fraction,

    "lower_fraction":
        lower_fraction,

    "switch_count":
        int(switches),

    "mean_dwell_time":
        float(np.mean(dwell_times)),

    "median_dwell_time":
        float(np.median(dwell_times)),

    "max_dwell_time":
        int(np.max(dwell_times)),

    "num_segments":
        int(len(dwell_times))
}

print()
print("=== QMVA-08C Attractor Switching ===")
print()
print(json.dumps(results, indent=2))

# ---------------------------------------
# State trajectory
# ---------------------------------------

plt.figure(figsize=(12,4))

plt.step(
    np.arange(len(states)),
    states,
    where="mid"
)

plt.yticks(
    [0,1],
    ["Lower","Upper"]
)

plt.xlabel("Frame")
plt.ylabel("Detector Attractor")

plt.title(
    "QMVA-08C Detector Attractor Switching"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "QMVA-08C-Attractor-Switching.png",
    dpi=300
)

# ---------------------------------------
# Dwell histogram
# ---------------------------------------

plt.figure(figsize=(8,4))

plt.hist(
    dwell_times,
    bins=20
)

plt.xlabel("Dwell Time")
plt.ylabel("Count")

plt.title(
    "QMVA-08C Dwell Time Distribution"
)

plt.tight_layout()

plt.savefig(
    "QMVA-08C-Dwell-Histogram.png",
    dpi=300
)

# ---------------------------------------
# Save
# ---------------------------------------

with open(
    "QMVA-08C-attractor-switching.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=2
    )

print()
print("Saved:")
print("QMVA-08C-Attractor-Switching.png")
print("QMVA-08C-Dwell-Histogram.png")
print("QMVA-08C-attractor-switching.json")
