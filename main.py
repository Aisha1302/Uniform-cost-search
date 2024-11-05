import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]
    visited = {start: 0}
    path = {start: None}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)


        if current_node == goal:
            final_path = []
            while current_node:
                final_path.append(current_node)
                current_node = path[current_node]
            return final_path[::-1], visited[goal]

        for neighbor, cost in graph.get(current_node, []):
            new_cost = current_cost + cost

            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                path[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return None, float("inf")



graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}


start_node = 'A'
goal_node = 'D'
path, cost = uniform_cost_search(graph, start_node, goal_node)
print(f"Path: {path}")
print(f"Cost: {cost}")
