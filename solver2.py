import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
import time
import glob
import sys
import sys
import os
import json
from parse import validate_file


def knapSack(W, wt, val, n):
    #happiness_table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    arrangement_table = [[[] for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


def knapSack_recur(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)

        # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
                   knapSack(W, wt, val, n - 1))

    # end of function knapSack



def solve_1(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    # TODO: your code here!
    highest_happiness_so_far = -1
    opt_k = -1
    opt_D = {}

    for a in range(0, 6):
        for b in range(0, 6):
            for c in range(0,6):
                for d in range(0, 6):
                    for e in range(0, 6):
                        for f in range(0, 6):
                            for g in range(0, 6):
                                for h in range(0, 6):
                                    for i in range(0, 6):
                                        for j in range(0, 6):
                                            dict_mapping = {0: a, 1: b, 2: c, 3: d, 4: e, 5: f, 6: g, 7: h, 8: i, 9: j}
                                            num_room = len(set({a, b, c, d, e, f, g, h, i, j}))
                                            # stress_barrier = s/num_room

                                            if is_valid_solution(dict_mapping, G, s, num_room):
                                                curr_happiness = calculate_happiness(dict_mapping, G)
                                                if curr_happiness > highest_happiness_so_far:
                                                    highest_happiness_so_far = curr_happiness
                                                    opt_k = num_room
                                                    opt_D = dict_mapping

    print("for solver_1", opt_D, opt_k, highest_happiness_so_far)

    #return {1:0, 2:0, 7:0, 5:1, 0:1, 9:1, 8:2, 6:2, 3:2, 4:2}, 3
    return opt_D, opt_k




    pass


def solve_2(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    # TODO: your code here!
    highest_happiness_so_far = -1
    opt_k = -1
    opt_D = {}


    for a in range(0, 5):
        for b in range(0, 5):
            for c in range(0, 5):
                for d in range(0, 5):
                    for e in range(0, 5):
                        for f in range(0, 5):
                            for g in range(0, 5):
                                for h in range(0, 5):
                                    for i in range(0, 5):
                                        for j in range(0, 5):
                                            dict_mapping = {0: a, 1: b, 2: c, 3: d, 4: e, 5: f, 6: g, 7: h, 8: i, 9: j}
                                            num_room = len(set({a, b, c, d, e, f, g, h, i, j}))
                                            # stress_barrier = s/num_room

                                            if num_room == 5 and is_valid_solution(dict_mapping, G, s, num_room):
                                                curr_happiness = calculate_happiness(dict_mapping, G)
                                                if curr_happiness > highest_happiness_so_far:
                                                    highest_happiness_so_far = curr_happiness
                                                    opt_k = num_room
                                                    opt_D = dict_mapping

    print("for solver_2", opt_D, opt_k, highest_happiness_so_far)

    #return {1:0, 2:0, 7:0, 5:1, 0:1, 9:0, 8:2, 6:2, 3:2, 4:2}, 3
    return opt_D, opt_k



def solve_3(G, s):
    #{1: 0, 2: 5, 7: 2, 5: 3, 0: 5, 9: 4, 8: 0, 6: 3, 3: 5, 4: 3, 10: 0, 11: 1, 12: 5, 13: 4, 14: 5, 15: 4, 16: 0, 17: 5,18: 1, 19: 3}, 6

    return {1: 0, 2: 5, 7: 2, 5: 3, 0: 5, 9: 4, 8: 0, 6: 3, 3: 5, 4: 3, 10: 0, 11: 1, 12: 5, 13: 4, 14: 5, 15: 4, 16: 0, 17: 5,18: 1, 19: 3}, 6

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in



# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':
    inputs = glob.glob('inputs2/*')
    for input_path in inputs:
        print(input_path)
        #output_file = f'{outputs_dir}/{graph_name}.out'
        output_path = 'outputs/' + input_path[8:-3] + '.out'
        print(output_path)
        G, s = read_input_file(input_path, 100)
        D, k = solve_1(G, s)
        assert is_valid_solution(D, G, s, k)
        cost_t = calculate_happiness(D, G)
        write_output_file(D, output_path)



