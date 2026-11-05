
from collections import deque

def bfs(capacity_a, capacity_b, target):
    queue = deque([(0, 0)])
    visited = set()
    parent = {}

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        if a == target or b == target:
            path = []
            state = (a, b)

            while state in parent:
                path.append(state)
                state = parent[state]

            path.append((0, 0))
            return path[::-1]

        # All possible operations
        next_states = [
            (capacity_a, b),  # Fill A
            (a, capacity_b),  # Fill B
            (0, b),            # Empty A
            (a, 0),            # Empty B
            (a - min(a, capacity_b - b),
             b + min(a, capacity_b - b)),  # A -> B
            (a + min(b, capacity_a - a),
             b - min(b, capacity_a - a))   # B -> A
        ]

        for state in next_states:
            if state not in visited and state not in parent:
                parent[state] = (a, b)
                queue.append(state)

    return None


path = bfs(4, 3, 2)

if path:
    for state in path:
        print(state)
else:
    print("No solution")











def dfs(capacity_a, capacity_b, target):
    stack = [(0, 0)]
    visited = set()
    parent = {}

    while stack:
        a, b = stack.pop()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        if a == target or b == target:
            path = []
            state = (a, b)

            while state in parent:
                path.append(state)
                state = parent[state]

            path.append((0, 0))
            return path[::-1]

        next_states = [
            (capacity_a, b),  # Fill A
            (a, capacity_b),  # Fill B
            (0, b),            # Empty A
            (a, 0),            # Empty B
            (a - min(a, capacity_b - b),
             b + min(a, capacity_b - b)),  # A -> B
            (a + min(b, capacity_a - a),
             b - min(b, capacity_a - a))   # B -> A
        ]

        for state in next_states:
            if state not in visited and state not in parent:
                parent[state] = (a, b)
                stack.append(state)

    return None


path = dfs(4, 3, 2)

if path:
    for state in path:
        print(state)
else:
    print("No solution")
