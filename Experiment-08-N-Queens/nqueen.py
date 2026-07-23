"""
Experiment 08: N-Queens Problem
Objective: Place N chess queens on an N×N chessboard so that no two queens threaten each other.
"""

def print_solution(board):
    """
    Helper function to print the board in a clean format.
    Q represents a Queen, and . represents an empty square.
    """
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].
    We only need to check the left side because we place queens column by column from left to right.
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, col, n, solutions):
    """
    Recursive utility function to solve N-Queens problem using backtracking.
    """
    # Base case: If all queens are placed, then return true
    if col >= n:
        solution = []
        for row in board:
            solution.append("".join(row))
        solutions.append(solution)
        return True

    res = False
    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 'Q'

            # Make result true if any placement is possible
            res = solve_n_queens_util(board, col + 1, n, solutions) or res

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col] (BACKTRACK)
            board[i][col] = '.'

    # Return whether any solution was found
    return res

def solve_n_queens(n):
    """
    Main function to solve the N-Queens problem.
    It returns a list of all possible solutions.
    """
    # Initialize an N x N board with '.'
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    if not solve_n_queens_util(board, 0, n, solutions):
        print("Solution does not exist")
        return []
    
    return solutions

if __name__ == "__main__":
    n = 4  # Standard example to keep output concise, usually 8 is used for the full problem
    print(f"Solving {n}-Queens Problem...\n")
    solutions = solve_n_queens(n)
    
    print(f"Total solutions found: {len(solutions)}\n")
    for idx, sol in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in sol:
            print(" ".join(row))
        print()
