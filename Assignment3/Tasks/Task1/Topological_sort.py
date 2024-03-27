#inspired from https://www.youtube.com/watch?v=eL-KzMXSXXI&t=205s
graph_from_figure_1 = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G', 'J'],
    'F': ['G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': [],
    'J': ['I']
}

time = [0]
start_time = {}
finish_time = {}
visited = {node: False for node in graph_from_figure_1}

def dfs(node):
    global time, start_time, finish_time, visited
    time[0] += 1
    start_time[node] = time[0]
    visited[node] = True

    for next_node in graph_from_figure_1[node]:
        if not visited[next_node]:
            dfs(next_node)

    time[0] += 1
    finish_time[node] = time[0]

def topology_sort(graph):
    global visited
    number_of_nodes = len(graph)
    ordering = [None] * number_of_nodes
    i = number_of_nodes - 1

    for node in graph:
        if not visited[node]:
            dfs(node)

    #Sort node on timings
    sorted_nodes = sorted(graph, key=lambda node: finish_time[node])
    
    for node in sorted_nodes:
        ordering[i] = node
        i -= 1
    #return ordered nodes
    return ordering

ordering = topology_sort(graph_from_figure_1)
print(ordering)
