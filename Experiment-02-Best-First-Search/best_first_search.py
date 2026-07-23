"""
Experiment 02: Best-First Search
Objective: Implement Best-First Search using a priority queue based on heuristics.
"""

import heapq

def best_first_search(graph, heuristics, start, goal):
    """
    Function to perform Best-First Search on a graph.
    
    Args:
        graph (dict): The graph represented as an adjacency list.
        heuristics (dict): A dictionary mapping each node to its heuristic value (estimated cost to goal).
        start (str): The starting node.
        goal (str): The goal node.
        
    Returns:
        list: The traversal path from start to goal, or empty if no path.
    """
    # Priority Queue to store nodes to explore. Stores tuples of (heuristic, node)
    pq = []
    heapq.heappush(pq, (heuristics[start], start))
    
    visited = set()
    visited.add(start)
    
    path = []
    
    while pq:
        # Get the node with the lowest heuristic value
        current_heuristic, current_node = heapq.heappop(pq)
        path.append(current_node)
        
        # Check if we have reached the goal
        if current_node == goal:
            return path
            
        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(pq, (heuristics[neighbor], neighbor))
                
    # If the queue is empty and goal wasn't reached, return the path explored so far (or empty list)
    return path

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    example_graph = {
        'S': ['A', 'B', 'C'],
        'A': ['S', 'D', 'E'],
        'B': ['S', 'F', 'G'],
        'C': ['S', 'H'],
        'D': ['A'],
        'E': ['A'],
        'F': ['B'],
        'G': ['B', 'I'],
        'H': ['C'],
        'I': ['G']
    }
    
    # Example heuristic values (estimated distance to goal 'I')
    heuristic_values = {
        'S': 10,
        'A': 8,
        'B': 5,
        'C': 7,
        'D': 9,
        'E': 10,
        'F': 6,
        'G': 2,
        'H': 8,
        'I': 0
    }
    
    start_node = 'S'
    goal_node = 'I'
    print(f"Starting Best-First Search from '{start_node}' to '{goal_node}'...")
    
    path_found = best_first_search(example_graph, heuristic_values, start_node, goal_node)
    
    print("\nBest-First Search Traversal Path:")
    if path_found and path_found[-1] == goal_node:
        print(" -> ".join(path_found))
        print("\nGoal Reached!")
    else:
        print(" -> ".join(path_found))
        print("\nGoal not reachable.")
