from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

print("\n=== Quantum Ground Benchmark QG-04 ===")
print("Excitation History Depth (EHD)\n")

history = []

state = Statevector.from_label("0")
history.append(("Initial", state))

ehd = 0

# Event 1
h = QuantumCircuit(1)
h.h(0)

state = state.evolve(h)
ehd += 1
history.append(("After H", state))

# Event 2
x = QuantumCircuit(1)
x.x(0)

state = state.evolve(x)
ehd += 1
history.append(("After X", state))

print("History:\n")

for step, (label, s) in enumerate(history):
    print(f"Step {step}: {label}")
    print(s)
    print()

print("Metrics")
print("-------")
print(f"Excitation History Depth (EHD): {ehd}")
print(f"Final State Dimension: {len(state)}")

print("\nInterpretation")
print("EHD measures the number of excitation events")
print("required to reach the final state.")
