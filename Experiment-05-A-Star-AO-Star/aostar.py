"""
AO* Search Algorithm Implementation

This script demonstrates the AO* search algorithm, which is used for solving 
AND-OR graphs. It finds an optimal solution graph from a start node to goal nodes.
"""

def cost(H, condition, weight=1):
    """Calculates the cost of a condition (AND/OR)."""
    cost_val = 0
    if type(condition) == tuple: # AND node
        for node in condition:
            cost_val += H.get(node, 0) + weight
    else: # OR node
        cost_val = H.get(condition, 0) + weight
    return cost_val

def update_cost(H, Conditions, weight=1):
    """Updates the heuristic costs for a node based on its conditions."""
    Main_nodes = list(Conditions.keys())
    Main_nodes.reverse() # Start from bottom-up
    least_cost = {}
    for key in Main_nodes:
        condition = Conditions[key]
        print(f"Evaluating Node: {key}")
        c = []
        for val in condition:
            c.append(cost(H, val, weight))
        
        # Minimum cost among OR alternatives, or the cost of the AND combination
        min_cost = min(c)
        H[key] = min_cost
        
        # Save the optimal path choice
        optimal_choice = condition[c.index(min_cost)]
        least_cost[key] = optimal_choice
        print(f"  Updated Cost of {key}: {min_cost}")
        print(f"  Optimal Choice for {key}: {optimal_choice}")
        print("-" * 30)
    return least_cost

def shortest_path(Start, Updated_cost, H):
    """Reconstructs the shortest path from the updated costs."""
    Path = Start
    if Start in Updated_cost.keys():
        optimal_choice = Updated_cost[Start]
        if type(optimal_choice) == tuple: # AND node
            Path += " -> ("
            for node in optimal_choice:
                Path += shortest_path(node, Updated_cost, H) + " + "
            Path = Path[:-3] + ")"
        else: # OR node
            Path += " -> " + shortest_path(optimal_choice, Updated_cost, H)
    return Path

if __name__ == "__main__":
    # Heuristic Values for Nodes
    H = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0}
    
    # Conditions: Dictionary defining AND/OR graph.
    # Tuples represent AND conditions, strings represent OR conditions.
    Conditions = {
        'A': ['B', ('C', 'D')],
        'B': [('E', 'F')],
        'C': ['G', ('H', 'I')],
        'D': ['J']
    }
    
    print("--- AO* Search Algorithm ---\n")
    print("Initial Heuristic Costs:", H)
    print("Graph Conditions:", Conditions)
    print("\nStarting Cost Updates...")
    print("=" * 30)
    
    weight = 1
    Updated_cost = update_cost(H, Conditions, weight=weight)
    
    print("=" * 30)
    print("\nFinal Optimal Path Choices:")
    for node, choice in Updated_cost.items():
        print(f"{node} -> {choice}")
        
    print(f"\n✅ Shortest Path:\n{shortest_path('A', Updated_cost, H)}")
