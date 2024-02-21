'''

Hill Climbing Algorithm for Budgeted Purchase Problem
Author: Marcus Chau

'''
import random
import os
import sys


def read_input_data(file_path):
    """
    Reads input data from the file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    parts = lines[0].split()
    target, budget, flag, num_restarts = int(parts[0]), int(parts[1]), parts[2], int(parts[3])
    items = [(name, int(value), int(cost)) for name, value, cost in (line.split() for line in lines[1:])]

    return target, budget, flag, num_restarts, items


def calculate_totals(state, items):
    """
    Calculates total value and cost of the selected items.
    """
    total_value = sum(value for (name, value, cost), selected in zip(items, state) if selected)
    total_cost = sum(cost for (name, value, cost), selected in zip(items, state) if selected)
    return total_value, total_cost


def evaluate_error(state, items, target, budget):
    """
    Calculates error for the given state.
    """
    total_value, total_cost = calculate_totals(state, items)
    error_cost = max(0, total_cost - budget)
    error_value = max(0, target - total_value)
    return error_cost + error_value


def hill_climbing(items, target, budget, flag):
    """
    Performs the hill climbing algorithm.
    """
    current_state = [random.choice([True, False]) for _ in items]

    if flag == 'V':
        print_state(current_state, items, "Initial State")

    while True:
        neighbors = [current_state[:i] + [not current_state[i]] + current_state[i+1:] for i in range(len(items))]

        best_neighbor = min(neighbors, key=lambda state: evaluate_error(state, items, target, budget))
        best_error = evaluate_error(best_neighbor, items, target, budget)

        if best_error >= evaluate_error(current_state, items, target, budget):
            return current_state

        if flag == 'V':
            print_state(best_neighbor, items, "Next State")

        current_state = best_neighbor


def print_state(state, items, description):
    """
    Prints the state of the algorithm.
    """
    total_value, total_cost = calculate_totals(state, items)
    state_items = ' '.join(name for (name, _, _), selected in zip(items, state) if selected)
    print(f"{description}: {{{state_items}}}. Value = {total_value}. Cost = {total_cost}.")


def run_with_random_restarts(file_path):
    """
    Runs the algorithm with random restarts.
    """
    target, budget, flag, num_restarts, items = read_input_data(file_path)
    best_state, best_error = None, float('inf')

    for _ in range(num_restarts):
        state = hill_climbing(items, target, budget, flag)
        error = evaluate_error(state, items, target, budget)

        if error < best_error:
            best_error = error
            best_state = state

    return best_state, items, flag, target, budget


def main():
    """
    Main function to run the algorithm.
    """
    file_path = 'testHC.txt'

    if not os.path.isfile(file_path):
        print('Error: File does not exist.')
        sys.exit(1)

    state, items, flag, target, budget = run_with_random_restarts(file_path)
    if evaluate_error(state, items, target, budget) != 0:
        print("No solution found.")
    else:
        print("Found solution:")
        print_state(state, items, "Solution")


if __name__ == "__main__":
    main()
