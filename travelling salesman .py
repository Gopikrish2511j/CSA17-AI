from collections import deque

goal = '123456780'

def to_grid(state):
    return [list(state[i:i+3]) for i in range(0, 9, 3)]

def print_grid(state):
    grid = to_grid(state)
    for row in grid:
        print(' '.join(row))
    print("↓")

def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        visited.add(state)
        zero = state.index('0')
        x, y = divmod(zero, 3)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = nx * 3 + ny
                lst = list(state)
                lst[zero], lst[nz] = lst[nz], lst[zero]
                new_state = ''.join(lst)
                if new_state not in visited:
                    queue.append((new_state, path + [state]))
    return None

# Example start state: 0 is the empty space
start = '123406758'

solution = bfs(start)

if solution:
    print("Puzzle steps to solve:")
    for step in solution:
        print_grid(step)
else:
    print("No solution found.")