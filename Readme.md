# Genetic Algorithm for the Travelling Salesman Problem

## 📌 Overview

This project implements a Genetic Algorithm (GA) from scratch to solve the Travelling Salesman Problem (TSP), a well-known NP-hard combinatorial optimization problem.

The goal is to find the shortest possible route that visits each city exactly once and returns to the origin city.

## 🧬 Methodology

The implemented Genetic Algorithm follows these steps:

1. Random population initialization

2. Fitness evaluation (inverse of total route distance)

3. Roulette-wheel selection

4. Ordered crossover (OX-inspired)

5. Swap mutation

6. Generational replacement

📊 Results

The algorithm shows clear convergence behavior:

- Rapid improvement during early generations

- Gradual stabilization toward a local optimum

- Visualization of route improvement

🧠 Concepts Demonstrated

- Evolutionary computation
- Combinatorial optimization
- Probabilistic selection mechanisms
- Convergence analysis

## 🛠 Technologies

. Python
. Numpy
. Matplotlib

## Future Improvements

. Elitism
. Tournament selection
. Adaptive mutation rate
. Comparaison with Simulated Annealing
. Parallel implementation
