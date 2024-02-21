'''

Iterative Deepening Algorithm for Budgeted Purchase Problem
Author: Marcus Chau

'''
import os, sys


def read_input_data(file_path):
    """
    Reads input data from the file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extracting the first two values as integers and the third as a string
    parts = lines[0].split()
    target, budget = int(parts[0]), int(parts[1])
    flag = parts[2] if len(parts) > 2 else 'C'  # Defaulting to 'C' if flag is not provided

    items = [(name, int(value), int(cost)) for name, value, cost in (line.split() for line in lines[1:])]

    return target, budget, flag, items


def search_with_iterative_deepening(target, budget, items, depth, current_set=[], total_value=0, total_cost=0, verbose=False):
    """
    Performs the iterative deepening search.
    """
    if total_cost > budget:
        return None
    if total_value >= target and total_cost <= budget:
        return current_set

    if depth == 0:
        return None

    for index, (name, value, cost) in enumerate(items):
        new_set = current_set + [name]
        new_value, new_cost = total_value + value, total_cost + cost

        if verbose:
            item_list = ' '.join(f'{{{name}}}' for name in new_set)
            print(f"{item_list}. Value = {new_value}. Cost = {new_cost}.")

        result = search_with_iterative_deepening(target, budget, items[index+1:], depth-1, new_set, new_value, new_cost, verbose)
        if result:
            return result

    return None


def solve_budgeted_purchase_problem(file_path):
    """
    Solves the budgeted purchase problem.
    """
    target, budget, output_flag, items = read_input_data(file_path)
    solution = None
    depth = 1

    while not solution and depth <= len(items):
        if output_flag == 'V' and depth > 1:
            print()
        if output_flag == 'V':
            print(f"Depth = {depth}.")
        solution = search_with_iterative_deepening(target, budget, items, depth, verbose=output_flag == 'V')
        depth += 1

    if not solution:
        return "No Solution"
    else:
        if output_flag == 'V':
            solution_value = sum(item[1] for item in items if item[0] in solution)
            solution_cost = sum(item[2] for item in items if item[0] in solution)
            print(f"\nFound solution {' '.join(f'{{{item}}}' for item in solution)}. Value = {solution_value}. Cost = {solution_cost}.")
        return ' '.join(solution)


def main():
    file_path = 'testID.txt'

    if not os.path.exists(file_path):
        print('Error: The specified file does not exist.')
        sys.exit(1)

    solution = solve_budgeted_purchase_problem(file_path)
    print(solution)


if __name__ == "__main__":
    main()
