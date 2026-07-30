"""
Experiment 05: A* Search and AO* Search Algorithms
Objective: Implement A* Search for weighted graphs and AO* Search for AND-OR graphs.
"""

# ─────────────────────────────────────────────
#  PART 1 : A* Search Algorithm
# ─────────────────────────────────────────────

def a_star_algorithm(graph, heuristics, start, goal):
    """
    Implements the A* search algorithm.

    Args:
        graph (dict): Adjacency list with edge weights {node: {neighbor: weight}}.
        heuristics (dict): Heuristic values for each node.
        start (str): Starting node.
        goal (str): Goal node.

    Returns:
        tuple: (path list, total cost) or (None, inf) if no path.
    """
    open_set = {start}
    closed_set = set()

    g_score = {start: 0}
    parents = {start: start}

    while open_set:
        current_node = min(
            open_set,
            key=lambda n: g_score.get(n, float('inf')) + heuristics.get(n, float('inf'))
        )

        if current_node == goal:
            path = []
            while parents[current_node] != current_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        open_set.remove(current_node)
        closed_set.add(current_node)

        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor in closed_set:
                continue
            tentative_g = g_score[current_node] + weight
            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g >= g_score.get(neighbor, float('inf')):
                continue
            parents[neighbor] = current_node
            g_score[neighbor] = tentative_g

    return None, float('inf')


# ─────────────────────────────────────────────
#  PART 2 : AO* Search Algorithm
# ─────────────────────────────────────────────

def ao_cost(H, condition, weight=1):
    """Calculate cost of a condition (AND node = tuple, OR node = string)."""
    if isinstance(condition, tuple):
        return sum(H.get(node, 0) + weight for node in condition)
    return H.get(condition, 0) + weight


def ao_update_cost(H, Conditions, weight=1):
    """Update heuristic costs bottom-up and return optimal choices."""
    nodes = list(Conditions.keys())
    nodes.reverse()
    least_cost = {}

    for key in nodes:
        costs = [ao_cost(H, val, weight) for val in Conditions[key]]
        min_cost = min(costs)
        H[key] = min_cost
        optimal = Conditions[key][costs.index(min_cost)]
        least_cost[key] = optimal
        print(f"  Evaluating Node: {key}")
        print(f"    Updated Cost  : {min_cost}")
        print(f"    Optimal Choice: {optimal}")
        print("  " + "-" * 28)

    return least_cost


def ao_shortest_path(start, updated_cost, H):
    """Reconstruct the optimal AND-OR path."""
    path = start
    if start in updated_cost:
        choice = updated_cost[start]
        if isinstance(choice, tuple):
            path += " -> ("
            for node in choice:
                path += ao_shortest_path(node, updated_cost, H) + " + "
            path = path[:-3] + ")"
        else:
            path += " -> " + ao_shortest_path(choice, updated_cost, H)
    return path


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":

    # ── A* Example ──────────────────────────────
    print("=" * 40)
    print("   PART 1: A* Search Algorithm")
    print("=" * 40)

    graph = {
        'A': {'B': 2, 'E': 3},
        'B': {'C': 1, 'G': 9},
        'C': {},
        'E': {'D': 6},
        'D': {'G': 1},
        'G': {}
    }

    heuristics = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }

    start_node = 'A'
    goal_node  = 'G'

    print(f"\nFinding path from '{start_node}' to '{goal_node}'...")
    path, cost = a_star_algorithm(graph, heuristics, start_node, goal_node)

    if path:
        print(f"\nPath found : {' -> '.join(path)}")
        print(f"Total Cost : {cost}")
    else:
        print("\nNo path found.")

    # ── AO* Example ─────────────────────────────
    print()
    print("=" * 40)
    print("   PART 2: AO* Search Algorithm")
    print("=" * 40)

    H = {'A': -1, 'B': 5, 'C': 2, 'D': 4,
         'E': 7,  'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0}

    Conditions = {
        'A': ['B', ('C', 'D')],
        'B': [('E', 'F')],
        'C': ['G', ('H', 'I')],
        'D': ['J']
    }

    print("\nInitial Heuristic Costs:", H)
    print("AND-OR Graph Conditions:", Conditions)
    print("\nStarting Cost Updates...")
    print("  " + "=" * 28)

    updated_cost = ao_update_cost(H, Conditions, weight=1)

    print("  " + "=" * 28)
    print("\nFinal Optimal Path Choices:")
    for node, choice in updated_cost.items():
        print(f"  {node} -> {choice}")

    print(f"\nShortest Path:")
    print(f"  {ao_shortest_path('A', updated_cost, H)}")
