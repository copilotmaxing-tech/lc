
# A* Search Algorithm

# Graph with edge costs
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {'G': 2},
    'E': {'G': 4},
    'F': {'G': 2},
    'G': {}
}

# Heuristic values (estimated distance to goal)
h = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 2,
    'G': 0
}

def astar(start, goal):
    open_list = [(start, 0)]
    visited = set()
    parent = {}
    g = {start: 0}

    while open_list:
        # Select node with minimum f(n)
        open_list.sort(key=lambda x: x[1] + h[x[0]])
        current, _ = open_list.pop(0)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()

            print("Shortest Path:", path)
            print("Total Cost:", g[goal])
            return

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current].items():
            new_cost = g[current] + cost

            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                parent[neighbor] = current
                open_list.append((neighbor, new_cost))

    print("No path found!")


# Execute A*
astar('A', 'G')
