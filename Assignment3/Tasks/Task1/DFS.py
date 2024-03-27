# Example usage
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
#Alphabetical
for node in graph_from_figure_1:
    graph_from_figure_1[node].sort()

visited = {node: False for node in graph_from_figure_1}
start_time = {node: None for node in graph_from_figure_1}
finish_time = {node: None for node in graph_from_figure_1}
time = [0]

# DFS function
def dfs(node):
    global time
    time[0] += 1
    start_time[node] = time[0]
    visited[node] = True

    for next_node in graph_from_figure_1[node]:
        if not visited[next_node]:
            dfs(next_node)

    time[0] += 1
    finish_time[node] = time[0]


start_node = 'A'
dfs(start_node)
for node in graph_from_figure_1:
    print(f"Node {node}: Start Time = {start_time[node]}, Finish Time = {finish_time[node]}")