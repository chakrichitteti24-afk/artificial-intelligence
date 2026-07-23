"""
Experiment 06: Water Jug Problem
Objective: Implement the Water Jug Problem using Breadth-First Search.
"""

from collections import deque

def solve_water_jug(jug1_cap, jug2_cap, target):
    """
    Solves the water jug problem using BFS.
    
    Args:
        jug1_cap (int): Capacity of the first jug.
        jug2_cap (int): Capacity of the second jug.
        target (int): Target amount of water.
        
    Returns:
        list: A sequence of states from the initial state to the target state.
    """
    # A dictionary to store the parent of each state to reconstruct the path
    parent = {}
    
    # A set to keep track of visited states
    visited = set()
    
    # Queue for BFS, storing tuples of (jug1_amount, jug2_amount)
    queue = deque([(0, 0)])
    visited.add((0, 0))
    parent[(0, 0)] = None
    
    target_state = None
    
    while queue:
        current_state = queue.popleft()
        amt1, amt2 = current_state
        
        # Check if we have reached the target
        if amt1 == target or amt2 == target:
            target_state = current_state
            break
            
        # Possible next states
        next_states = []
        
        # 1. Fill jug 1
        next_states.append((jug1_cap, amt2))
        # 2. Fill jug 2
        next_states.append((amt1, jug2_cap))
        # 3. Empty jug 1
        next_states.append((0, amt2))
        # 4. Empty jug 2
        next_states.append((amt1, 0))
        # 5. Pour jug 1 to jug 2
        pour_to_2 = min(amt1, jug2_cap - amt2)
        next_states.append((amt1 - pour_to_2, amt2 + pour_to_2))
        # 6. Pour jug 2 to jug 1
        pour_to_1 = min(amt2, jug1_cap - amt1)
        next_states.append((amt1 + pour_to_1, amt2 - pour_to_1))
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                parent[state] = current_state
                queue.append(state)
                
    # If a solution was found, reconstruct the path
    if target_state:
        path = []
        curr = target_state
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        return path
    else:
        return None

def print_solution(path):
    """Prints the path to the solution."""
    if not path:
        print("No solution possible.")
        return
        
    print(f"| {'Jug 1':^10} | {'Jug 2':^10} |")
    print(f"|{'-'*12}+{'-'*12}|")
    for state in path:
        print(f"| {state[0]:^10} | {state[1]:^10} |")

if __name__ == "__main__":
    print("--- Water Jug Problem ---")
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2
    
    print(f"Jug 1 Capacity: {jug1_capacity}L")
    print(f"Jug 2 Capacity: {jug2_capacity}L")
    print(f"Target: {target_amount}L")
    print("\nFinding solution...\n")
    
    solution_path = solve_water_jug(jug1_capacity, jug2_capacity, target_amount)
    print_solution(solution_path)
