from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

print("\n=== Quantum Ground Benchmark QG-01 ===")
print("Same Gates, Different Excitation Histories\n")

# Circuit A
qc_a = QuantumCircuit(1)
qc_a.h(0)
qc_a.x(0)

# Circuit B
qc_b = QuantumCircuit(1)
qc_b.x(0)
qc_b.h(0)

state_a = Statevector.from_instruction(qc_a)
state_b = Statevector.from_instruction(qc_b)

print("Circuit A : H → X")
print(state_a)

print("\nCircuit B : X → H")
print(state_b)

print("\nEquivalent Final States?")
print(state_a.equiv(state_b))

print("\nInterpretation:")
print("QG-01 examines whether excitation history")
print("contains information beyond final measurement.")
