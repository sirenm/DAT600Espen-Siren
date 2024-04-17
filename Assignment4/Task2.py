import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges between nodes with capacities
edges = [
    ('s', 'v1', 14),
    ('s', 'v2', 25),
    ('v1', 'v4', 21),
    ('v1', 'v3', 3),
    ('v2', 'v3', 13),
    ('v2', 'v5', 7),
    ('v3', 'v1', 6),
    ('v3', 'v5', 15),
    ('v4', 'v3', 10),
    ('v4', 't', 20),
    ('v5', 'v4', 5),
    ('v5', 't', 10)
]

for u, v, capacity in edges:
    G.add_edge(u, v, capacity=capacity)

# Calculate maximum flow
flow_value, flow_dict = nx.maximum_flow(G, 's', 't')
print("Maximum Flow Value:", flow_value)

# Calculate minimum cut
min_cut_value, (reachable, non_reachable) = nx.minimum_cut(G, 's', 't')

bottleneck_edges = []
for u, v, d in G.edges(data=True):
    if u in reachable and v in non_reachable:
        bottleneck_edges.append((u, v))
print(bottleneck_edges)