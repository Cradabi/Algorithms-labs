from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return None

# Пример использования
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'E'
shortest_path = bfs(graph, start_node, end_node)
print(f"Кратчайший путь из {start_node} в {end_node}: {shortest_path}")
