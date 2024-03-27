graph_from_figure_1_with_additional_edges = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['A','E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G', 'J'],
    'F': ['B', 'G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': ['C'],
    'J': ['I']
}

visited = {node: False for node in graph_from_figure_1_with_additional_edges}
start_time = {node: None for node in graph_from_figure_1_with_additional_edges}
finish_time = {node: None for node in graph_from_figure_1_with_additional_edges}
time = [0]

def dfs(node, graph, edge_to_remove):
    global time
    time[0] += 1
    start_time[node] = time[0]
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, graph, edge_to_remove)
        elif finish_time[next_node] is None:
            edge_to_remove.append((node, next_node))

    time[0] += 1
    finish_time[node] = time[0]


def remove_edges(graph):
    edges_to_remove = []
    for node in graph:
        if not visited[node]:
            dfs(node, graph, edges_to_remove)
            
    for node, neighbour in edges_to_remove:
        print(f"Removed edge {node} -> {neighbour}")
        graph[node].remove(neighbour)

    return graph

dag = remove_edges(graph_from_figure_1_with_additional_edges)
print(dag)