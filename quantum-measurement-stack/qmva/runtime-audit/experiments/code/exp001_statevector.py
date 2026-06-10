from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)

qc.save_statevector()

backend = AerSimulator()

result = backend.run(qc).result()

print(result.data(0))
