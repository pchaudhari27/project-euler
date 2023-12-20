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




