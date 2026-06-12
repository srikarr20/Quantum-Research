import matplotlib.pyplot as plt

freq = [0,10,50,250,500,1000]

vri = [
0.95203,
0.94680,
0.93571,
0.88501,
0.83034,
0.76013
]

qnd = [
0.91445,
0.90829,
0.89846,
0.84371,
0.78324,
0.69235
]

plt.figure(figsize=(8,5))

plt.plot(freq,vri,marker='o',label='VRI')
plt.plot(freq,qnd,marker='o',label='QNDFid')

plt.xlabel("Frequency (Hz)")
plt.ylabel("Metric Value")
plt.title("QMVA-03 Visibility Retention vs QND Fidelity")
plt.legend()

plt.savefig(
"runtime-audit/artifacts/QMVA-03/QMVA-03-VRI-QNDFid.png",
dpi=300,
bbox_inches="tight"
)

print("Saved figure")
