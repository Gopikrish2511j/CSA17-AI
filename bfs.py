from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

start = 'A'
queue = deque([start])
visited = []

while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=' ')
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)