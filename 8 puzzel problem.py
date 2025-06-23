from collections import deque
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
def bfs(start):
    if start == GOAL: return [start]
    queue, visited = deque([(start, [start])]), {start}
    while queue:
        current, path = queue.popleft()
        zero_pos = current.index(0)
        for d in (-3, 3, -1, 1):
            new_pos = zero_pos + d
            if 0 <= new_pos < 9 and not (zero_pos % 3 == 2 and d == 1) and not (zero_pos % 3 == 0 and d == -1):
                new_state = list(current)
                new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
                new_state = tuple(new_state)
                if new_state not in visited:
                    if new_state == GOAL: return path + [new_state]
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))
    return None
def print_puzzle(puzzle):
    print("\n".join(str(puzzle[i:i+3]) for i in range(0, 9, 3)))
    print("\n")
start_state = (8, 2, 3, 4, 7, 6, 0, 5, 1)
solution = bfs(start_state)
if solution:
    print(f"Solution found in {len(solution)-1} moves!")
    for i, state in enumerate(solution):
        print(f"Move {i}:")
        print_puzzle(state)
else:
    print("No solution found!")