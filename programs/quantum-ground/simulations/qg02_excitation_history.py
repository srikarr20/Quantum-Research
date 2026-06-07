from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

print("\n=== Quantum Ground QG-02 ===\n")

history = []

# Initial state
state = Statevector.from_label("0")
history.append(("Initial", state))

# H gate as its own circuit
h_circuit = QuantumCircuit(1)
h_circuit.h(0)

state = state.evolve(h_circuit)
history.append(("After H", state))

# X gate as its own circuit
x_circuit = QuantumCircuit(1)
x_circuit.x(0)

state = state.evolve(x_circuit)
history.append(("After X", state))

for label, s in history:
    print(label)
    print(s)
    print()

