import math
def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player, values):
    if depth == 0 or isinstance(node, int):
        return values[node] if not isinstance(node, int) else node
    if maximizing_player:
        max_eval = -math.inf
        for child in node:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False, values)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break 
        return max_eval
    else:
        min_eval = math.inf
        for child in node:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True, values)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval
game_tree = [
    [3, 5, 6],        
    [9, [1, 2], 0]   
]
leaf_values = [3, 5, 6, 9, 1, 2, 0]
best_value = alpha_beta_pruning(game_tree, 3, -math.inf, math.inf, True, leaf_values)
print("Best value for the maximizing player:",best_value)