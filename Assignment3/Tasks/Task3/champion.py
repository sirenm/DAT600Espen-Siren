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
