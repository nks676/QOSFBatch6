# QOSFBatch6
# Benchmarking Variations of the Quantum Approximate Optimization Algorithm on the Travelling Salesman Problem
#### Naren Sathishkumar∗, Siddarth Chander∗, Affan Hussein∗ and Kostas Blekos
## Abstract:
The Quantum Approximate Optimization Algorithm (QAOA) was created in
order to approximate solutions for combinatorial optimization problems. It
utilizes a unitary transformation to prepare a quantum state that encodes the
answer to the given problem, with the parameters of the unitary optimized
through a classical optimizer. In this study, we evaluate the performance of
QAOA on the NP-hard Travelling Salesman Problem and compare the original
algorithm from Farhi  to two variations: Warm-Start QAOA and QAOA+
. The Travelling Salesperson Problem involves finding the shortest possible
route between a given set of cities and their respective distances. It can be
formulated as a quantum problem in Qiskit and other software to be solved
using QAOA. Warm-Start QAOA involves initializing the parameters of QAOA
based on the solution to a relaxed or simplified version of the combinatorial
problem. In contrast, QAOA+ is comprised of an extension of the standard
QAOA p=1 layer, complemented by an additional multiparameter problem-
independent layer. This enhancement is specifically designed to improve the
approximation ratios and reduce the circuit complexity when compared to the
standard QAOA with p=2. Through our analysis of the results, we provide
insights into the strengths and weaknesses of these variations of QAOA for
solving the Travelling Salesman Problem
