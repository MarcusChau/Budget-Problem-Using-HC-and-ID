'''

Hill Climbing Algorithm for Budgeted Purchase Problem
Author: Marcus Chau

'''
import random

def run_hill_climbing_algorithm():
    file_path = 'testHC.txt'

    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    parts = lines[0].split()
    target = int(parts[0])
    budget = int(parts[1])
    flag = parts[2]
    num_restarts = int(parts[3])

    items = []
    for line in lines[1:]:
        parts = line.split()
        name = parts[0]
        value = int(parts[1])
        cost = int(parts[2])
        items.append((name, value, cost))

    
    best_state = None
    best_error = float('inf')
    for _ in range(num_restarts):
        current_state = [random.choice([True, False]) for _ in items]

        if flag == 'V':
            total_value = 0
            total_cost = 0
            for i in range(len(items)):
                name, value, cost = items[i]
                selected = current_state[i]
                if selected:
                    total_value += value
                    total_cost += cost

            state_items_arr = []
            for i in range(len(items)):
                if current_state[i]:
                    name, _, _ = items[i]
                    state_items_arr.append(name)
            state_items = ' '.join(state_items_arr)
            print(f"{{{state_items}}}. Value = {total_value}. Cost = {total_cost}. Error = {max(0, total_cost - budget) + max(0, target - total_value)}.")

        while True:
            neighbors = []
            for i in range(len(items)):
                neighbor = current_state.copy()
                neighbor[i] = not neighbor[i]
                neighbors.append(neighbor)

            best_neighbor = None
            best_neighbor_error = float('inf')
            for neighbor in neighbors:
                total_value = 0
                total_cost = 0
                for i in range(len(items)):
                    name, value, cost = items[i]
                    selected = neighbor[i]
                    if selected:
                        total_value += value
                        total_cost += cost
                error = max(0, total_cost - budget) + max(0, target - total_value)

                if error < best_neighbor_error:
                    best_neighbor = neighbor
                    best_neighbor_error = error

            current_error = max(0, total_cost - budget) + max(0, target - total_value)
            if best_neighbor_error >= current_error:
                break

            current_state = best_neighbor

            if flag == 'V':
                total_value = 0
                total_cost = 0
                for i in range(len(items)):
                    name, value, cost = items[i]
                    selected = current_state[i]
                    if selected:
                        total_value += value
                        total_cost += cost

                state_items_arr = []
                for i in range(len(items)):
                    if current_state[i]:
                        name, _, _ = items[i]
                        state_items_arr.append(name)
                state_items = ' '.join(state_items_arr)
                print(f"{{{state_items}}}. Value = {total_value}. Cost = {total_cost}. Error = {max(0, total_cost - budget) + max(0, target - total_value)}.")

        total_value = 0
        total_cost = 0
        for i in range(len(items)):
            name, value, cost = items[i]
            selected = current_state[i]
            if selected:
                total_value += value
                total_cost += cost
        current_error = max(0, total_cost - budget) + max(0, target - total_value)

        if current_error < best_error:
            best_error = current_error
            best_state = current_state


    if best_error != 0:
        print("No solution found.")
    else:
        print("Found solution:")
        total_value = 0
        total_cost = 0
        for i in range(len(items)):
            name, value, cost = items[i]
            selected = best_state[i]
            if selected:
                total_value += value
                total_cost += cost

        state_items_arr = []
        for i in range(len(items)):
            if current_state[i]:
                name, _, _ = items[i]
                state_items_arr.append(name)
        state_items = ' '.join(state_items_arr)
        print(f"{{{state_items}}}. Value = {total_value}. Cost = {total_cost}. Error = {max(0, total_cost - budget) + max(0, target - total_value)}.")


if __name__ == "__main__":
    run_hill_climbing_algorithm()
