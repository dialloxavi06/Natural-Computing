import numpy as np
from tsp import route_distance


def initialize_population(pop_size, n_cities):
    population = []
    for _ in range(pop_size):
        individual = np.random.permutation(n_cities)
        population.append(individual)
    return np.array(population)


def fitness(individual, dist_matrix):
    return 1 / route_distance(individual, dist_matrix)


def selection(population, fitness_scores):
    probabilities = fitness_scores / fitness_scores.sum()
    idx = np.random.choice(len(population), p=probabilities)
    return population[idx]


def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(np.random.choice(range(size), 2, replace=False))

    child = -np.ones(size, dtype=int)
    child[start:end] = parent1[start:end]

    pointer = 0
    for gene in parent2:
        if gene not in child:
            while child[pointer] != -1:
                pointer += 1
            child[pointer] = gene

    return child


def mutate(individual, mutation_rate=0.01):
    if np.random.rand() < mutation_rate:
        i, j = np.random.choice(len(individual), 2, replace=False)
        individual[i], individual[j] = individual[j], individual[i]
    return individual