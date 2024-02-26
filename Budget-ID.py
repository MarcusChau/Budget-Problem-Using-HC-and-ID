'''

Iterative Deepening Algorithm for Budgeted Purchase Problem
Author: Marcus Chau

'''
def iterative_deeping_algorithm():
    file_path = 'testID.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    parts = lines[0].split()
    target, budget = int(parts[0]), int(parts[1])
    flag = parts[2] if len(parts) > 2 else 'C' 

    items = []
    for line in lines[1:]:
        parts = line.split()
        name = parts[0]
        value = int(parts[1])
        cost = int(parts[2])
        items.append((name, value, cost))

    solution = None
    depth = 1
    while not solution and depth <= len(items):
        if flag == 'V' and depth > 1:
            print()
        if flag == 'V':
            print(f"Depth = {depth}.")
        solution = search_with_iterative_deepening(target, budget, items, depth, verbose=flag == 'V')
        depth += 1

    if not solution:
        print("No Solution")
    else:
        if flag == 'V':
            solution_value = sum(item[1] for item in items if item[0] in solution)
            solution_cost = sum(item[2] for item in items if item[0] in solution)
            print(f"\nFound solution {' '.join(f'{{{item}}}' for item in solution)}. Value = {solution_value}. Cost = {solution_cost}.")
        print(' '.join(solution))


def search_with_iterative_deepening(target, budget, items, depth, current_set=[], total_value=0, total_cost=0, verbose=False):
    if total_cost > budget:
        return None
    if total_value >= target and total_cost <= budget:
        return current_set

    if depth == 0:
        return None

    index = 0
    for item in items:
        name, value, cost = item
        new_set = current_set + [name]
        new_value = total_value + value
        new_cost = total_cost + cost


        if verbose:
            item_list = ' '.join(f'{{{name}}}' for name in new_set)
            print(f"{item_list}. Value = {new_value}. Cost = {new_cost}.")

        result = search_with_iterative_deepening(target, budget, items[index+1:], depth-1, new_set, new_value, new_cost, verbose)
        if result:
            return result
        
        index += 1

    return None

if __name__ == "__main__":
    iterative_deeping_algorithm()
