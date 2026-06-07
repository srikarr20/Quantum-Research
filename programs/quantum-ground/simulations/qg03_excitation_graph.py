from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

history = []

state = Statevector.from_label("0")
history.append(("S0", "Initial", state))

h = QuantumCircuit(1)
h.h(0)

state = state.evolve(h)
history.append(("S1", "H", state))

x = QuantumCircuit(1)
x.x(0)

state = state.evolve(x)
history.append(("S2", "X", state))

print("\n=== Excitation Sequence Graph ===\n")

for node, event, s in history:
    print(f"{node} | {event}")
    print(s)
    print()

print("Graph:")
print("S0 --H--> S1 --X--> S2")
