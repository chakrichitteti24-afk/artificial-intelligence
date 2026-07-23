"""
Experiment 01: Breadth-First Search (BFS)
Objective: Implement BFS to traverse a graph level-by-level.
"""

from collections import deque

def bfs(graph, start):
    """
    Function to perform Breadth-First Search (BFS) on a graph.
    
    Args:
        graph (dict): The graph represented as an adjacency list.
        start (str): The starting node for the traversal.
        
    Returns:
        list: The order of visited nodes.
    """
    # Set to keep track of visited nodes to avoid cycles
    visited = set()
    
    # Queue for BFS, initialized with the starting node
    queue = deque([start])
    
    # Mark the start node as visited
    visited.add(start)
    
    # List to store the traversal order
    order = []

    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        order.append(vertex)
        
        # Get all adjacent vertices of the dequeued vertex
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return order

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    example_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B', 'H'],
        'F': ['C'],
        'G': ['C'],
        'H': ['E']
    }
    
    start_node = 'A'
    print(f"Starting BFS traversal from node '{start_node}'...")
    traversal_order = bfs(example_graph, start_node)
    
    print("\nBFS Traversal Order:")
    print(" -> ".join(traversal_order))
