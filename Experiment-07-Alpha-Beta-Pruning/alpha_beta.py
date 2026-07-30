"""
Experiment 07: Alpha-Beta Pruning
Objective: Implement the Alpha-Beta Pruning algorithm to optimize the Minimax search process.
"""

import math

def minimax_alpha_beta(depth, node_index, is_max, scores, alpha, beta, target_depth):
    """
    Minimax algorithm with Alpha-Beta Pruning.
    
    Parameters:
    depth (int): Current depth in the game tree.
    node_index (int): Index of the current node in the scores array.
    is_max (bool): True if current move is Maximizer, False for Minimizer.
    scores (list): The leaf nodes' scores.
    alpha (int): The best already explored option along path to the root for maximizer.
    beta (int): The best already explored option along path to the root for minimizer.
    target_depth (int): The depth at which the leaf nodes are located.
    
    Returns:
    int: The optimal value a player can achieve.
    """
    # Terminating condition: leaf node is reached
    if depth == target_depth:
        return scores[node_index]

    if is_max:
        best = -math.inf
        # Recur for left and right children
        for i in range(2):
            val = minimax_alpha_beta(depth + 1, node_index * 2 + i, False, scores, alpha, beta, target_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Alpha-Beta Pruning
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        # Recur for left and right children
        for i in range(2):
            val = minimax_alpha_beta(depth + 1, node_index * 2 + i, True, scores, alpha, beta, target_depth)
            best = min(best, val)
            beta = min(beta, best)
            
            # Alpha-Beta Pruning
            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    # Example scores for leaf nodes in a game tree
    scores = [3, 5, 6, 9, 1, 2, 0, -1]
    
    # Target depth of the tree
    tree_depth = math.log(len(scores), 2)
    tree_depth = int(tree_depth)
    
    print("+----------------------------------------+")
    print("|         Alpha-Beta Pruning Test        |")
    print("+----------------------------------------+")
    print("|  Leaf node scores:                     |")
    print(f"|  {str(scores):<38}|")
    print("+----------------------------------------+")
    
    # Calculate optimal value
    optimal_value = minimax_alpha_beta(0, 0, True, scores, -math.inf, math.inf, tree_depth)
    
    print(f"|  Optimal value is : {optimal_value:<19}|")
    print("+----------------------------------------+")
