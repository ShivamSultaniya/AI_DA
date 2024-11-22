import copy
import heapq

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(goal.index(state[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_moves(state):
    moves = []
    x, y = find_blank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)

    return moves

def hill_climbing(initial, goal):
    current_state = initial
    goal_flat = [tile for row in goal for tile in row]
    steps = [current_state]

    while True:
        current_flat = [tile for row in current_state for tile in row] 
        current_heuristic = manhattan_distance(current_state, goal_flat)

        neighbors = generate_moves(current_state)
        neighbor_states = []
        for neighbor in neighbors:
            neighbor_flat = [tile for row in neighbor for tile in row] 
            heuristic = manhattan_distance(neighbor, goal_flat)
            neighbor_states.append((heuristic, neighbor))

        neighbor_states.sort()
        best_neighbor = neighbor_states[0][1]
        best_heuristic = neighbor_states[0][0]

        if best_heuristic < current_heuristic:
            current_state = best_neighbor
            steps.append(current_state)
        else:
            break

    return steps, current_heuristic


def print_steps(steps):
    for i, step in enumerate(steps):
        print(f"Step {i}:")
        for row in step:
            print(row)
        print()


if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [5, 0, 6],
        [4, 7, 8]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    steps, heuristic = hill_climbing(initial_state, goal_state)

    print("Steps to reach the solution:")
    print_steps(steps)

    if heuristic == 0:
        print("Solution found!")
    else:
        print("Local maxima or plateau reached, solution not found.")
