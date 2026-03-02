import numpy as np

def generate_cities(n_cities, seed=42):
    np.random.seed(seed)
    return np.random.rand(n_cities, 2)  # coordonnées (x,y)


def compute_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.linalg.norm(cities[i] - cities[j])

    return dist_matrix


def route_distance(route, dist_matrix):
    total_distance = 0
    for i in range(len(route)):
        total_distance += dist_matrix[route[i], route[(i + 1) % len(route)]]
    return total_distance