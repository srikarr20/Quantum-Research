from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

print("\n=== Quantum Ground Sequence Demo ===\n")

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

print("Circuit A : H -> X")
print(state_a)

print("\nCircuit B : X -> H")
print(state_b)

print("\nObservation:")
print("Different excitation sequences can produce different state histories.")
print("The program studies the sequence, not only the final measurement.")
