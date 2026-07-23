"""
Experiment 03: Depth-First Search (DFS)
Objective: Implement DFS to traverse a graph exploring as far as possible along each branch before backtracking.
"""

def dfs(graph, start):
    """
    Function to perform Depth-First Search (DFS) on a graph.
    
    Args:
        graph (dict): The graph represented as an adjacency list.
        start (str): The starting node for the traversal.
        
    Returns:
        list: The order of visited nodes.
    """
    visited = set()
    order = []
    
    # We use an iterative approach with a stack
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            
            # Add neighbors to stack
            # We reverse the neighbors to visit them in alphabetical/numerical order 
            # if that's how they are stored in the adjacency list.
            # (Because it's a stack, pushing A then B means popping B then A).
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
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
    print(f"Starting DFS traversal from node '{start_node}'...")
    traversal_order = dfs(example_graph, start_node)
    
    print("\nDFS Traversal Order:")
    print(" -> ".join(traversal_order))
