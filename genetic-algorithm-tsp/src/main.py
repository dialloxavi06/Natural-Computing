import numpy as np
import matplotlib.pyplot as plt
from tsp import generate_cities, compute_distance_matrix, route_distance
from genetic_algorithm import initialize_population, selection, crossover, mutate

def run_ga(n_cities=20, pop_size=100, generations=300):
    cities = generate_cities(n_cities)
    dist_matrix = compute_distance_matrix(cities)

    population = initialize_population(pop_size, n_cities)

    best_distances = []

    for gen in range(generations):
        fitness_scores = np.array([1 / route_distance(ind, dist_matrix) for ind in population])
        new_population = []

        for _ in range(pop_size):
            parent1 = selection(population, fitness_scores)
            parent2 = selection(population, fitness_scores)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = np.array(new_population)

        best_individual = min(population, key=lambda ind: route_distance(ind, dist_matrix))
        best_distance = route_distance(best_individual, dist_matrix)
        best_distances.append(best_distance)

        print(f"Generation {gen}: Best Distance = {best_distance:.4f}")

    return cities, best_individual, best_distances


def plot_route(cities, route):
    ordered = cities[route]
    ordered = np.vstack([ordered, ordered[0]])

    plt.figure()
    plt.plot(ordered[:, 0], ordered[:, 1], marker='o')
    plt.title("Best TSP Route")
    plt.show()


if __name__ == "__main__":
    cities, best_route, history = run_ga()
    plot_route(cities, best_route)

    plt.figure()
    plt.plot(history)
    plt.title("Convergence Curve")
    plt.xlabel("Generation")
    plt.ylabel("Best Distance")
    plt.show()