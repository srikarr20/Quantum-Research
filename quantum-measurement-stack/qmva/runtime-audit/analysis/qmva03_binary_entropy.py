import numpy as np

p0 = 0.5
p1 = 0.5

H_binary = -(p0*np.log2(p0)+p1*np.log2(p1))

print()
print("Binary Entropy")
print("--------------")
print(H_binary)
print()
