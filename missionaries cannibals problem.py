from collections import deque

start = (3, 3, 1)  # (Missionaries, Cannibals, Boat on left=1/right=0)
goal = (0, 0, 0)
moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

queue = deque([[start]])
visited = set()

while queue:
    path = queue.popleft()
    state = path[-1]
    if state == goal:
        for step in path:
            print(step)
        break
    if state in visited: continue
    visited.add(state)
    M, C, B = state
    for m, c in moves:
        newM = M - m if B else M + m
        newC = C - c if B else C + c
        newB = 1 - B
        if 0 <= newM <= 3 and 0 <= newC <= 3:
            otherM = 3 - newM
            otherC = 3 - newC
            if (newM == 0 or newM >= newC) and (otherM == 0 or otherM >= otherC):
                next_state = (newM, newC, newB)
                if next_state not in visited:
                    queue.append(path + [next_state])