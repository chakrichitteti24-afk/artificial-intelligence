"""
Experiment 04: Heuristic Search (A* Search)
Objective: Implement A* Search algorithm to find the optimal path using both path cost and heuristic.
"""

import heapq

def a_star_search(graph, heuristics, start, goal):
    """
    Function to perform A* Search on a graph.
    
    Args:
        graph (dict): Adjacency list where keys are nodes and values are lists of (neighbor, edge_cost) tuples.
        heuristics (dict): Estimated cost from node to goal.
        start (str): The starting node.
        goal (str): The goal node.
        
    Returns:
        tuple: (path, total_cost)
    """
    # Priority queue stores tuples of (f_score, g_score, current_node, path)
    pq = []
    heapq.heappush(pq, (heuristics[start], 0, start, [start]))
    
    # Dictionary to keep track of the minimum g_score to reach a node
    g_scores = {start: 0}
    
    while pq:
        f_score, current_g, current_node, path = heapq.heappop(pq)
        
        # If we reached the goal, return the path and cost
        if current_node == goal:
            return path, current_g
            
        # Explore neighbors
        for neighbor, cost in graph.get(current_node, []):
            tentative_g = current_g + cost
            
            # If we found a shorter path to neighbor, or neighbor not visited
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f = tentative_g + heuristics[neighbor]
                heapq.heappush(pq, (f, tentative_g, neighbor, path + [neighbor]))
                
    return [], 0 # No path found

if __name__ == "__main__":
    # Example graph represented as an adjacency list with costs
    # Format: {node: [(neighbor, cost), ...]}
    example_graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('B', 2), ('C', 5), ('G', 12)],
        'B': [('C', 2)],
        'C': [('G', 3)],
        'G': []
    }
    
    # Example heuristic values (estimated distance to goal 'G')
    heuristic_values = {
        'S': 7,
        'A': 6,
        'B': 2,
        'C': 1,
        'G': 0
    }
    
    start_node = 'S'
    goal_node = 'G'
    print(f"Starting A* Search from '{start_node}' to '{goal_node}'...")
    
    path_found, cost = a_star_search(example_graph, heuristic_values, start_node, goal_node)
    
    print("\nA* Search Traversal Path:")
    if path_found:
        print(" -> ".join(path_found))
        print(f"Total Path Cost: {cost}")
    else:
        print("Goal not reachable.")
