import heapq


def shortest_path_with_limit(graph, start, end, extra_paths):
    queue = [(0, start, extra_paths)]
    visited = set()

    while queue:
        cost, current, extra = heapq.heappop(queue)

        if current == end:
            return cost

        if (current, extra) in visited:
            continue
        visited.add((current, extra))

        for neighbor, weight, limit in graph[current]:
            new_cost = cost + weight
            new_extra = extra
            if limit > 0:
                new_extra = extra - 1

            if new_extra >= 0:
                heapq.heappush(queue, (new_cost, neighbor, new_extra))

    return None


# Пример графа
graph = {
    'A': [('B', 1, 0), ('C', 5, 1)],
    'B': [('C', 2, 0)],
    'C': [('D', 3, 0)],
    'D': [('E', 4, 0)],
    'E': []
}

start = 'A'
end = 'E'
extra_paths = 1

result = shortest_path_with_limit(graph, start, end, extra_paths)
if result is not None:
    print(f"Самый короткий путь между вершинами {start} и {end} равен {result}")
else:
    print("Путь не найден")
