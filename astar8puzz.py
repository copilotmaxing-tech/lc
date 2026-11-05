
import heapq

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1

            x1, y1 = i // 3, i % 3
            x2, y2 = goal_pos // 3, goal_pos % 3

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate possible next states
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row, col = zero // 3, zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Algorithm
def astar(start):
    pq = []

    # (f, g, state, path)
    heapq.heappush(pq, (heuristic(start), 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None


# Initial state (0 represents blank space)
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Solve puzzle
solution = astar(start)

# Print solution
if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found!")
