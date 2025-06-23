from queue import PriorityQueue

graph = {}
nodes = input("Nodes: ").split()
for n in nodes:
    graph[n] = []

print("Edges (from to cost), 'done' to stop:")
while True:
    e = input()
    if e == 'done': break
    a, b, c = e.split()
    c = int(c)
    graph[a].append((b, c))
    graph[b].append((a, c))  # Remove for directed graph

h = {}
print("Heuristics (node value):")
for _ in nodes:
    n, val = input().split()
    h[n] = int(val)

start = input("Start: ")
goal = input("Goal: ")

open_set = PriorityQueue()
open_set.put((h[start], 0, start))
came_from = {}
g = {start: 0}

while not open_set.empty():
    f, cost, node = open_set.get()
    if node == goal: break
    for n, c in graph[node]:
        new_g = g[node] + c
        if n not in g or new_g < g[n]:
            g[n] = new_g
            open_set.put((new_g + h[n], new_g, n))
            came_from[n] = node

path = []
n = goal
while n != start:
    path.append(n)
    n = came_from[n]
path.append(start)
path.reverse()

print("Path:", ' -> '.join(path))
print("Cost:", g[goal])
