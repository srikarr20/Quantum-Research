H_detector = float(input("Detector entropy: "))
H_binary = 1.0

print()
print("Compression Ratio")
print("-----------------")
print(H_binary / H_detector)
print()

print("Information Loss")
print("----------------")
print(1 - (H_binary / H_detector))
print()
