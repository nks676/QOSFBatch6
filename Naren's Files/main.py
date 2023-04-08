import time
import numpy as np
import functions
from solver import ForestTSPSolver

def main():
    nodes_array = np.array([[10, 47], [26, 19], [40, 36], [6, 9]])
    tsp_matrix = functions.get_adj_matrix(nodes_array)
    starting_node = 0

    print("Brute Force solution")
    start_time = time.time()
    bf_start_time = start_time
    brute_force_solution = functions.brute_force(nodes_array, starting_node)
    end_time = time.time()
    calculation_time = end_time - start_time
    print("Calculation time:", calculation_time)
    functions.plot_solution('brute_force_' + str(start_time), nodes_array, brute_force_solution)

    print("QAOA solution - Forest")
    start_time = time.time()
    forest_solver = ForestTSPSolver(tsp_matrix, starting_node=starting_node)
    forest_solution, forest_distribution = forest_solver.solve_tsp()
    end_time = time.time()
    calculation_time = end_time - start_time
    print("Calculation time:", calculation_time)
    costs = [(sol, functions.calculate_cost(tsp_matrix, sol), forest_distribution[sol]) for sol in forest_distribution]
    print("Forest:")
    for cost in costs:
        print(cost)
    functions.plot_solution('forest_' + str(bf_start_time), nodes_array, forest_solution)


if __name__ == '__main__':
    main()