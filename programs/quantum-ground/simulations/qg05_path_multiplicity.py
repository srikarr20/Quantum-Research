from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

print("\n=== Quantum Ground Benchmark QG-05 ===")
print("Excitation Path Multiplicity (EPM)\n")

# Path A
path_a = QuantumCircuit(1)
path_a.h(0)

# Path B
path_b = QuantumCircuit(1)
path_b.h(0)
path_b.x(0)

state_a = Statevector.from_instruction(path_a)
state_b = Statevector.from_instruction(path_b)

print("Path A: H")
print(state_a)
print()

print("Path B: H -> X")
print(state_b)
print()

equivalent = state_a.equiv(state_b)

print("Equivalent Final States?")
print(equivalent)

if equivalent:
    epm = 2
else:
    epm = 1

print("\nMetrics")
print("-------")
print(f"Excitation Path Multiplicity (EPM): {epm}")

print("\nInterpretation")
print("EPM counts distinct excitation paths")
print("that converge to equivalent final states.")
