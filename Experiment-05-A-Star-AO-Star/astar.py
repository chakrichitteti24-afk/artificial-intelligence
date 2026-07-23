"""
A* Search Algorithm Implementation

This script demonstrates the A* search algorithm for finding the shortest path
from a start node to a goal node in a weighted graph using heuristics.
"""

def a_star_algorithm(graph, heuristics, start, goal):
    """
    Implements the A* search algorithm.
    
    Args:
        graph (dict): The adjacency list of the graph with edge weights.
        heuristics (dict): The heuristic values for each node.
        start (str): The starting node.
        goal (str): The goal node.
        
    Returns:
        list: The optimal path from start to goal.
    """
    # Open set contains nodes to be evaluated
    open_set = {start}
    # Closed set contains nodes already evaluated
    closed_set = set()
    
    # g_score maps each node to the cost of the cheapest path from start
    g_score = {start: 0}
    # parents keeps track of the path
    parents = {start: start}
    
    while open_set:
        # Find the node with the lowest f(n) = g(n) + h(n) in open_set
        current_node = None
        current_f = float('inf')
        
        for node in open_set:
            # f(n) = g(n) + h(n)
            f_score = g_score.get(node, float('inf')) + heuristics.get(node, float('inf'))
            if f_score < current_f:
                current_node = node
                current_f = f_score
                
        if current_node == goal:
            # We reached the goal, reconstruct the path
            path = []
            while parents[current_node] != current_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start)
            path.reverse()
            return path, current_f
            
        # Move current node from open_set to closed_set
        open_set.remove(current_node)
        closed_set.add(current_node)
        
        # Explore neighbors
        if current_node in graph:
            for neighbor, weight in graph[current_node].items():
                if neighbor in closed_set:
                    continue
                    
                # Tentative g_score for the neighbor
                tentative_g = g_score[current_node] + weight
                
                if neighbor not in open_set:
                    open_set.add(neighbor)
                elif tentative_g >= g_score.get(neighbor, float('inf')):
                    continue # This is not a better path
                    
                # This path is the best so far
                parents[neighbor] = current_node
                g_score[neighbor] = tentative_g
                
    return None, float('inf') # Path not found

if __name__ == "__main__":
    # Example Graph
    graph = {
        'A': {'B': 2, 'E': 3},
        'B': {'C': 1, 'G': 9},
        'C': {},
        'E': {'D': 6},
        'D': {'G': 1},
        'G': {}
    }
    
    # Heuristics (Straight-line distance to goal 'G')
    heuristics = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    
    start_node = 'A'
    goal_node = 'G'
    
    print(f"--- A* Search Algorithm ---")
    print(f"Finding path from '{start_node}' to '{goal_node}'...")
    
    path, cost = a_star_algorithm(graph, heuristics, start_node, goal_node)
    
    if path:
        print(f"\n✅ Path found: {' -> '.join(path)}")
        print(f"Total Cost: {cost}")
    else:
        print("\n❌ No path found.")
