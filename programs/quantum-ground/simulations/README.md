# Quantum Ground Simulations

This module contains computational artifacts for the Quantum Ground
research program.

## Benchmarks

### QG-01: Sequence Dependence

Demonstrates that gate ordering affects quantum state evolution.

File:
qg01_sequence_dependence.py

### QG-02: Excitation History

Tracks intermediate states during state evolution.

File:
qg02_excitation_history.py

### QG-03: Excitation Sequence Graph

Represents state evolution as a directed sequence graph.

File:
qg03_excitation_graph.py

## Research Goal

Shift analysis from:

Input → Output

to:

State → Excitation Event → State → Excitation Event → State

and investigate whether preserved excitation histories contain
information not captured by final measurements alone.

