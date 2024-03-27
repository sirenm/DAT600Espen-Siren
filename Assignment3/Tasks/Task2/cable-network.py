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

#Task 2a
def prims_algorithm(graph):
    start_vertex = list(graph.keys())[0]
    min_spanning_tree = []
    total_cost = 0
    visited = set()
    visited.add(start_vertex)

    possible_edges = []
    for to_vertex, cost in graph[start_vertex].items():
        possible_edges.append((cost, start_vertex, to_vertex))

    #Sorted nondecreasing order of edges
    heapq.heapify(possible_edges)

    while possible_edges:
        #While possible edges (e), extract minimal cost e, from_vertex, to_vertex
        cost, from_vertex, to_vertex = heapq.heappop(possible_edges)

        if to_vertex not in visited:
            visited.add(to_vertex)
            total_cost += cost
            min_spanning_tree.append((from_vertex, to_vertex, cost))

            for next_vertex, next_cost in graph[to_vertex].items():
                if next_vertex not in visited:
                    heapq.heappush(possible_edges, (next_cost, to_vertex, next_vertex))

    return min_spanning_tree, total_cost


# print(prims_algorithm(graphtouse))
#Task 2b
def prims_algorithm_edge_constraint(graph, max_edges):
    start_vertex = list(graph.keys())[0]
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
        cost, from_vertex, to_vertex = heapq.heappop(possible_edges)

        vertex_not_visited = to_vertex not in visited
        under_edge_count = edge_count[from_vertex] < max_edges

        if vertex_not_visited and under_edge_count:
            visited.add(to_vertex)
            total_cost += cost
            min_spanning_tree.append((from_vertex, to_vertex, cost))
            edge_count[from_vertex] += 1
            edge_count[to_vertex] += 1

            for next_vertex, next_cost in graph[to_vertex].items():
                vertex_not_visited = next_vertex not in visited
                under_edge_count = edge_count[next_vertex] < max_edges

                if vertex_not_visited and under_edge_count:
                    heapq.heappush(possible_edges, (next_cost, to_vertex, next_vertex))

    return min_spanning_tree, total_cost

mst_with_constraint = prims_algorithm_edge_constraint(graphtouse, max_edges=3)
# print(mst_with_constraint)

#Task 2c
def prims_algorithm_edge_swap(graph, max_edges):
    start_vertex = list(graph.keys())[0]
    min_spanning_tree = []
    total_cost = 0
    visited = set([start_vertex])

    edge_count = {vertex: 0 for vertex in graph}
    possible_edges = [(cost, start_vertex, to_vertex) for to_vertex, cost in graph[start_vertex].items()]
    heapq.heapify(possible_edges)

    max_edge_in_mst = (0, None, None)
    edges_not_in_mst = []

    while possible_edges:
        cost, from_vertex, to_vertex = heapq.heappop(possible_edges)
        if to_vertex not in visited and edge_count[from_vertex] < max_edges:
            visited.add(to_vertex)
            total_cost += cost
            min_spanning_tree.append((cost, from_vertex, to_vertex))
            edge_count[from_vertex] += 1
            edge_count[to_vertex] += 1

            if cost > max_edge_in_mst[0]:
                max_edge_in_mst = (cost, from_vertex, to_vertex)

            for next_vertex, next_cost in graph[to_vertex].items():
                if next_vertex not in visited and edge_count[next_vertex] < max_edges:
                    heapq.heappush(possible_edges, (next_cost, to_vertex, next_vertex))
        else:
            edges_not_in_mst.append((cost, from_vertex, to_vertex))

    min_edge_not_in_mst = min(edges_not_in_mst)

    if min_edge_not_in_mst[0] < max_edge_in_mst[0]:
        min_spanning_tree.remove((max_edge_in_mst[0], max_edge_in_mst[1], max_edge_in_mst[2]))
        min_spanning_tree.append(min_edge_not_in_mst)
        total_cost = total_cost - max_edge_in_mst[0] + min_edge_not_in_mst[0]

    return min_spanning_tree, total_cost


mst_with_cost = prims_algorithm_edge_swap(graphtouse, 3)
print(mst_with_cost)