import numpy as np

from scipy.io import loadmat

from sklearn.linear_model import LogisticRegression
from sklearn.mixture import GaussianMixture

DATA = "/Users/rallabandisailesh/Desktop/Quantum-Research/quantum-measurement-stack/qmva/runtime-audit/datasets/ISTA-AllOptical-Readout/AllopticalSCQreadout_data/Fig_4a/IQblobs_0Hz.mat"

d = loadmat(DATA)

I_g = d["I_g"].flatten()
Q_g = d["Q_g"].flatten()

I_e = d["I_e"].flatten()
Q_e = d["Q_e"].flatten()

g = np.column_stack([I_g,Q_g])
e = np.column_stack([I_e,Q_e])

X = np.vstack([g,e])

y = np.concatenate([
    np.zeros(len(g)),
    np.ones(len(e))
])

print()
print("Dataset shape")
print(X.shape)

# ----------------------------------------
# Logistic
# ----------------------------------------

lr = LogisticRegression(
    max_iter=1000
)

lr.fit(X,y)

p_lr = lr.predict_proba(X)

print()
print("Logistic classes")
print(lr.classes_)

print()
print("Mean probability")
print(np.mean(p_lr[:,1]))

pred_lr = (p_lr[:,1] > 0.5)

print()
print("Logistic error")
print(np.mean(pred_lr != y))

# ----------------------------------------
# GMM
# ----------------------------------------

gmm = GaussianMixture(
    n_components=2,
    covariance_type="full",
    random_state=0
)

gmm.fit(X)

print()
print("GMM means")
print(gmm.means_)

p_gmm = gmm.predict_proba(X)

print()
print("Mean GMM probabilities")
print(np.mean(p_gmm[:,0]))
print(np.mean(p_gmm[:,1]))

pred0 = (p_gmm[:,0] > 0.5)
pred1 = (p_gmm[:,1] > 0.5)

print()
print("Error using cluster 0")
print(np.mean(pred0 != y))

print()
print("Error using cluster 1")
print(np.mean(pred1 != y))
