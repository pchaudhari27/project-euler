import numpy as np
import heapq

# iterative bfs for directed graph (slight modifications for undirected)
# assuming graph[a, b] = 1 means that a has a directed edge to b
def bfs(start_node, graph):
    queue = [start_node]
    visited = np.zeros(len(graph), int)

    while queue:
        curr_node = queue.pop(0)
        if visited[curr_node]:
            continue

        yield curr_node
        visited[curr_node] = 1
        for neighbor, edge in enumerate(graph[curr_node]):
            if edge:
                queue.append(neighbor)

# iterative dfs for directed graph (slight modifications for undirected)
# assuming graph[a, b] = 1 means that a has a directed edge to b
def dfs(start_node, graph):
    stack = [start_node]
    visited = np.zeros(len(graph), int)

    while stack:
        curr_node = stack.pop()
        if visited[curr_node]:
            continue

        yield curr_node
        visited[curr_node] = 1
        for neighbor, edge in enumerate(graph[curr_node]):
            if edge:
                stack.append(neighbor)


# takes graph in matrix notation, where graph[a,b] = weight of edge between a,b
# if there is no edge between a,b, then the default value is -1
def dijkstra(start_node, end_node, graph):
    visited = np.zeros(len(graph))
    regular_range = range(len(graph))

    # initialize distance to be very large
    distances = {i: 0 if i  == start_node else np.max(graph) * 10**10 for i in regular_range}
    queue = [start_node]

    # consider all unvisited neighbors
    while queue:
        current = queue.pop(0)
        if current == end_node:
            break

        for neighbor in regular_range:
            if visited[neighbor] == 0 and graph[current][neighbor] >= 0:
                distances[neighbor] = min(distances[neighbor], distances[current] + graph[current][neighbor])
                queue.append(neighbor)
        
        visited[current] = 1

    
    return distances[end_node]




