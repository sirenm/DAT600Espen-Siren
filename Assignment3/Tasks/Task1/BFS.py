from collections import defaultdict
from queue import Queue

# inspired from https://www.youtube.com/watch?v=oDqjPvD54Ss&t=216s
graph_from_figure_1 = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G', 'J'],
    'F': ['B', 'G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': [],
    'J': ['I']
}

def solve(s, graph):
    q = Queue()
    q.put(s)
    visited = {s: True}
    prev = {s: None}
    time = 0
    start_time = {s: time}
    finish_time = {}


    while not q.empty():
        u = q.get()
        time += 1

        for v in sorted(graph[u]):
            if v not in visited:
                visited[v] = True
                start_time[v] = time
                q.put(v)
                prev[v] = u

        finish_time[u] = time
    return prev, start_time, finish_time

def bfs(s, graph):
    prev, start_time, finish_time = solve(s, graph)

    result = defaultdict(dict)
    for n, previous_node in prev.items():
        result[n] = {
            'previous': previous_node,
            'start_time': start_time.get(n, None),
            'finish_time': finish_time.get(n, None)
        }
    return result

shortest_path = bfs('A', graph_from_figure_1)

# Improved printing for readability
for node, info in shortest_path.items():
    print(f"Node {node}: Previous: {info['previous']}, Start Time: {info['start_time']}, Finish Time: {info['finish_time']}")
