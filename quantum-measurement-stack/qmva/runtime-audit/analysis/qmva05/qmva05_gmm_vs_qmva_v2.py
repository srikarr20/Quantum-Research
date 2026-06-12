import json
import numpy as np

from pathlib import Path
from scipy.io import loadmat

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.mixture import GaussianMixture
from sklearn.metrics import brier_score_loss

# --------------------------------------------------
# FIND DATASET
# --------------------------------------------------

ROOT = Path(__file__).resolve()

DATA = None

for parent in ROOT.parents:

    candidate = (
        parent
        / "runtime-audit"
        / "datasets"
        / "ISTA-AllOptical-Readout"
        / "AllopticalSCQreadout_data"
        / "Fig_4a"
        / "IQblobs_0Hz.mat"
    )

    if candidate.exists():
        DATA = candidate
        break

if DATA is None:
    raise FileNotFoundError(
        "Could not locate IQblobs_0Hz.mat"
    )

print()
print("Using dataset:")
print(DATA)

# --------------------------------------------------
# LOAD
# --------------------------------------------------

d = loadmat(DATA)

I_g = d["I_g"].flatten()
Q_g = d["Q_g"].flatten()

I_e = d["I_e"].flatten()
Q_e = d["Q_e"].flatten()

theta = float(d["angle"].item())
threshold = float(d["threshold"].item())

g = np.column_stack([I_g, Q_g])
e = np.column_stack([I_e, Q_e])

X_raw = np.vstack([g, e])

y = np.concatenate([
    np.zeros(len(g)),
    np.ones(len(e))
])

# --------------------------------------------------
# ROTATE INTO DETECTOR FRAME
# --------------------------------------------------

c = np.cos(theta)
s = np.sin(theta)

R = np.array([
    [c, -s],
    [s,  c]
])

X_rot = X_raw @ R.T

dist = X_rot[:,0] - threshold

# --------------------------------------------------
# STANDARDIZE
# --------------------------------------------------

scaler = StandardScaler()

X = scaler.fit_transform(X_rot)

# --------------------------------------------------
# THRESHOLD
# --------------------------------------------------

pred_thresh = (dist > 0).astype(int)

err_thresh = np.mean(
    pred_thresh != y
)

# --------------------------------------------------
# LOGISTIC REGRESSION
# --------------------------------------------------

lr = LogisticRegression(
    max_iter=2000
)

lr.fit(X, y)

p_lr = lr.predict_proba(X)[:,1]

err_lr = np.mean(
    (p_lr > 0.5) != y
)

brier_lr = brier_score_loss(
    y,
    p_lr
)

# --------------------------------------------------
# SUPERVISED GMM
# --------------------------------------------------

gmm_g = GaussianMixture(
    n_components=1,
    covariance_type="full",
    random_state=0
)

gmm_e = GaussianMixture(
    n_components=1,
    covariance_type="full",
    random_state=0
)

gmm_g.fit(X[y==0])
gmm_e.fit(X[y==1])

logp_g = gmm_g.score_samples(X)
logp_e = gmm_e.score_samples(X)

p_e = np.exp(logp_e)
p_g = np.exp(logp_g)

p_gmm = p_e / (p_e + p_g)

err_gmm = np.mean(
    (p_gmm > 0.5) != y
)

brier_gmm = brier_score_loss(
    y,
    p_gmm
)

# --------------------------------------------------
# QMVA CONFIDENCE
# --------------------------------------------------

g_dist = dist[:len(g)]
e_dist = dist[len(g):]

g_sigma = np.std(g_dist)
e_sigma = np.std(e_dist)

CAL = [
    (0.0,0.5,0.65885),
    (0.5,1.0,0.83512),
    (1.0,1.5,0.91604),
    (1.5,2.0,0.95845),
    (2.0,3.0,0.98482),
    (3.0,5.0,0.98804),
    (5.0,10.0,0.98058),
]

def lookup(z):

    for z0,z1,p in CAL:
        if z0 <= z < z1:
            return p

    return CAL[-1][2]

p_qmva = []

for i,d0 in enumerate(dist):

    sigma = (
        g_sigma
        if y[i] == 0
        else e_sigma
    )

    z = abs(d0) / sigma

    acc = lookup(z)

    if d0 > 0:
        p_qmva.append(acc)
    else:
        p_qmva.append(1.0 - acc)

p_qmva = np.array(p_qmva)

err_qmva = np.mean(
    (p_qmva > 0.5) != y
)

brier_qmva = brier_score_loss(
    y,
    p_qmva
)

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

result = {

    "threshold_error":
        float(err_thresh),

    "logistic_error":
        float(err_lr),

    "gmm_error":
        float(err_gmm),

    "qmva_error":
        float(err_qmva),

    "logistic_brier":
        float(brier_lr),

    "gmm_brier":
        float(brier_gmm),

    "qmva_brier":
        float(brier_qmva)
}

print()
print("=== QMVA-05A Benchmark v2 ===")
print()

print(json.dumps(result, indent=2))

with open(
    "../../artifacts/QMVA-05A-benchmark-v2.json",
    "w"
) as f:

    json.dump(result, f, indent=2)

print()
print("Saved:")
print("../../artifacts/QMVA-05A-benchmark-v2.json")
