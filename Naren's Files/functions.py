import numpy as np
import itertools
import matplotlib.pyplot as plt

def distance(A, B):
    return np.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

def get_adj_matrix(coords_array):

    number_of_nodes = len(coords_array)
    adj_matrix = np.zeros((number_of_nodes, number_of_nodes))
    for i in range(number_of_nodes):
        for j in range(i, number_of_nodes):
            adj_matrix[i][j] = distance(coords_array[i], coords_array[j])
            adj_matrix[j][i] = adj_matrix[i][j]
    return adj_matrix

def calculate_cost(adj_matrix, solution):
    cost = 0
    for i in range(len(solution)):
        a = i%len(solution)
        b = (i+1)%len(solution)
        cost += adj_matrix[solution[a]][solution[b]]

    return cost

def brute_force(coords_array, starting_node):
    number_of_nodes = len(coords_array)
    initial_order = range(0, number_of_nodes)
    all_paths = [list(x) for x in itertools.permutations(initial_order)]
    adj_matrix = get_adj_matrix(coords_array)
    best_path = all_paths[0]
    best_cost = calculate_cost(adj_matrix, all_paths[0])*1000
    for path in all_paths:
        if path[0] != starting_node:
            continue
        current_cost = calculate_cost(adj_matrix, path)
        if current_cost < best_cost:
            best_path = path
            best_cost = current_cost
    print("Brute force:", best_path, best_cost)
    return best_path
	
def plot_solution(name, coords_array, solution):
    plt.scatter(coords_array[:, 0], coords_array[:, 1], s=200)
    for i in range(len(coords_array)):
        plt.annotate(i, (coords_array[i, 0] + 0.15, coords_array[i, 1] + 0.15), size=16, color='r')

    plt.xlim([min(coords_array[:, 0]) - 1, max(coords_array[:, 0]) + 1])
    plt.ylim([min(coords_array[:, 1]) - 1, max(coords_array[:, 1]) + 1])
    for i in range(len(solution)):
        a = i%len(solution)
        b = (i+1)%len(solution)
        A = solution[a]
        B = solution[b]
        plt.plot([coords_array[A, 0], coords_array[B, 0]], [coords_array[A, 1], coords_array[B, 1]], c='r')

    cost = calculate_cost(get_adj_matrix(coords_array), solution)
    title_string = "Cost:" + str(cost)
    title_string += "\n" + str(solution)
    plt.title(title_string)
    plt.savefig(name + '.png')
    plt.clf()
	
def binary_state_to_points_order(binary_state):
    points_order = []
    number_of_points = int(np.sqrt(len(binary_state)))
    for p in range(number_of_points):
        for j in range(number_of_points):
            if binary_state[(number_of_points) * p + j] == 1:
                points_order.append(j)
    return points_order