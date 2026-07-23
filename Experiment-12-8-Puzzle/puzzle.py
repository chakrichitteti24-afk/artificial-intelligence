"""
Experiment 12: 8-Puzzle Problem using A* Search
Objective: Implement the A* Search algorithm to solve the 8-puzzle game.
"""

import heapq

class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost # f(n) = g(n) + h(n)

    def __lt__(self, other):
        # Enables priority queue to sort by lowest cost
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

def get_blank_pos(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    i, j = get_blank_pos(state.board)
    # Possible moves: Up, Down, Left, Right
    moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
    
    for di, dj, move in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            # Create a deep copy of the board
            new_board = [list(row) for row in state.board]
            # Swap the blank tile (0) with the target tile
            new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
            # Convert back to tuple for hashability
            neighbors.append((tuple(tuple(row) for row in new_board), move))
    return neighbors

def manhattan_distance(board, goal):
    """
    Heuristic function h(n): Sum of the Manhattan distances of tiles to their goal positions.
    """
    dist = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                # Find position of 'val' in the goal state
                for gi in range(3):
                    for gj in range(3):
                        if goal[gi][gj] == val:
                            dist += abs(i - gi) + abs(j - gj)
    return dist

def solve_puzzle(start, goal):
    open_set = []
    closed_set = set()
    
    start_cost = manhattan_distance(start, goal)
    start_state = PuzzleState(start, None, None, 0, start_cost)
    heapq.heappush(open_set, start_state)

    while open_set:
        current = heapq.heappop(open_set)
        
        if current.board == goal:
            # Reconstruct path
            path = []
            curr = current
            while curr.parent:
                path.append(curr.move)
                curr = curr.parent
            return path[::-1] # Reverse the path

        closed_set.add(current.board)
        
        for next_board, move in get_neighbors(current):
            if next_board not in closed_set:
                g_n = current.depth + 1
                h_n = manhattan_distance(next_board, goal)
                f_n = g_n + h_n
                next_state = PuzzleState(next_board, current, move, g_n, f_n)
                heapq.heappush(open_set, next_state)
    return None

def print_board(board):
    for row in board:
        print(" | ".join(str(val) if val != 0 else " " for val in row))
        print("-" * 9)

if __name__ == "__main__":
    # 0 represents the blank space
    start_board = ((1, 2, 3), 
                   (4, 0, 5), 
                   (7, 8, 6))
                   
    goal_board =  ((1, 2, 3), 
                   (4, 5, 6), 
                   (7, 8, 0))
                   
    print("Solving 8-Puzzle using A* Search...\n")
    print("Start State:")
    print_board(start_board)
    print("\nGoal State:")
    print_board(goal_board)
    
    solution = solve_puzzle(start_board, goal_board)
    
    if solution:
        print("\nSolution Found!")
        print("Sequence of Moves to reach goal:", " -> ".join(solution))
        print("Total Moves:", len(solution))
    else:
        print("\nNo solution exists for this configuration.")
