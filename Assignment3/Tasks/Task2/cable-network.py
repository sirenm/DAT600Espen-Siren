import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import heapq

#initialize undirected graph
G = nx.Graph()

G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'D', weight=1)
G.add_edge('B', 'D', weight=4)
G.add_edge('B', 'H', weight=8)
G.add_edge('D', 'C', weight=2)
G.add_edge('D', 'E', weight=2)
G.add_edge('D', 'F', weight=4)
G.add_edge('C', 'G', weight=6)
G.add_edge('G', 'F', weight=9)
G.add_edge('F', 'H', weight=7)
G.add_edge('E', 'H', weight=8)

graph = nx.adjacency_matrix(G)
graph = graph.toarray()


mst = nx.minimum_spanning_tree(G)

def matrix_to_graph(matrix):
    graph = {}
    for i in range(len(matrix)):
        graph[i] = {}
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                graph[i][j] = matrix[i][j]
    return graph

graphtouse = matrix_to_graph(graph)
mst_weight = mst.size(weight='weight')

# print(mst_weight)


def prims_algorithm(graph, start_vertex):
    min_spanning_tree = []
    total_cost = 0
    visited = set()
    visited.add(start_vertex)

    possible_edges = []
    for to_vertex, cost in graph[start_vertex].items():
        possible_edges.append((cost, start_vertex, to_vertex))

    heapq.heapify(possible_edges)

    while possible_edges:
        cost, from_vertex, to_vertex = heapq.heappop(possible_edges)

        if to_vertex not in visited:
            visited.add(to_vertex)
            total_cost += cost
            min_spanning_tree.append((from_vertex, to_vertex, cost))

            for next_vertex, next_cost in graph[to_vertex].items():
                if next_vertex not in visited:
                    heapq.heappush(possible_edges, (next_cost, to_vertex, next_vertex))

    return min_spanning_tree, total_cost


# print(prims_algorithm(graphtouse, start_vertex=0))

def prims_algorithm_edge_constraint(graph, start_vertex, max_edges):
    min_spanning_tree = []
    total_cost = 0
    visited = set()
    visited.add(start_vertex)

    edge_count = {}
    for vertex in graph:
        edge_count[vertex] = 0

    possible_edges = []
    for to_vertex, cost in graph[start_vertex].items():
        possible_edges.append((cost, start_vertex, to_vertex))

    heapq.heapify(possible_edges)


    while possible_edges:
        print(possible_edges)
        cost, from_vertex, to_vertex = heapq.heappop(possible_edges)
        print(cost, from_vertex, to_vertex)

        if to_vertex not in visited and edge_count[from_vertex] < max_edges:
            visited.add(to_vertex)
            total_cost += cost

            min_spanning_tree.append((from_vertex, to_vertex, cost))

            edge_count[from_vertex] += 1
            edge_count[to_vertex] += 1


            for next_vertex, next_cost in graph[to_vertex].items():

                if next_vertex not in visited and edge_count[next_vertex] < max_edges:
                    heapq.heappush(possible_edges, (next_cost, to_vertex, next_vertex))


    return min_spanning_tree, total_cost

# for key, items in graphtouse.items():
#     print(key, items)

mst_with_constraint = prims_algorithm_edge_constraint(graphtouse, start_vertex=0, max_edges=3)
print(mst_with_constraint)