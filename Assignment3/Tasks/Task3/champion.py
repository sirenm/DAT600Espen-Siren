import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#initialize undirected graph
G = nx.DiGraph()
adj_matrix = [
[0, 1, 0, 1, 0, 0, 0],
[1, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0],
[0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0],
]

npArray = np.array(adj_matrix)
G = nx.from_numpy_array(npArray, create_using=nx.MultiDiGraph)

graph_list = nx.to_dict_of_lists(G)

#Task 3a
def reach_all(node, graph):
    visited = {n: False for n in graph}

    def dfs(current_node):
        visited[current_node] = True

        for next_node in graph[current_node]:
            if not visited[next_node]:
                dfs(next_node)

    dfs(node)

    for node in graph:
        if not visited[node]:
            return False
    return True

# plt.figure(figsize=(8, 6))
# nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', arrows=True)
# plt.show()

print(reach_all(0,graph_list))

def return_champions(graph):
    champions = []
    for node in graph:
        if reach_all(node, graph):
            champions.append(node)
    if champions:
        return champions
    else:
        "No champion nodes found"

print(return_champions(graph_list))


#Task 2b
visited = {node: False for node in graph_list}
start_time = {node: None for node in graph_list}
finish_time = {node: None for node in graph_list}
time = [0]

def dfs(node, graph):
    global time
    time[0] += 1
    start_time[node] = time[0]
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, graph)

    time[0] += 1
    finish_time[node] = time[0]


def transpose(graph):
    transposed = {node: [] for node in graph}
    for src in graph:
        for dst in graph[src]:
            transposed[dst].append(src)
    return transposed

# DFS function
def dfs_tranposed(node, graph, order, current_scc):
    global time
    time[0] += 1
    start_time[node] = time[0]
    visited[node] = True
    current_scc.append(node)

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs_tranposed(next_node, graph, order, current_scc)

    time[0] += 1
    finish_time[node] = time[0]

def find_SCCs(transposed_graph, finish_time):
    nodes_ordered_by_finish_time = sorted(finish_time, key=finish_time.get, reverse=True)
    
    for node in visited:
        visited[node] = False

    sccs = []
    for node in nodes_ordered_by_finish_time:
        if not visited[node]:
            current_scc = []
            dfs_tranposed(node, transposed_graph, nodes_ordered_by_finish_time, current_scc)
            sccs.append(current_scc)

    return sccs

#1. calculate dfs(G)
dfs(0, graph_list) #Populating finish_time

#2. calculate G^T
transposed_graph = transpose(graph_list)

#3. call dfs(transposed_g)
#Strongly connected components for transposed graph is equal to the original graph
sccs = find_SCCs(transposed_graph, finish_time)
print(sccs)