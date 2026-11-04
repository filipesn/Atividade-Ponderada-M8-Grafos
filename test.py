import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import heapq
import matplotlib.image as mpimg
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Updated graph with new weights
graph = {
    0: {1: 13, 2: 16},
    1: {0: 13, 2: 9, 3: 12, 4: 20},
    2: {0: 16, 1: 9, 4: 15, 5: 14},
    # 2: {0: 16, 1: 9, 5: 14},
    3: {1: 12, 4: 8, 6: 14},
    4: {1: 20, 2: 15, 3: 8, 5: 7, 7: 17},
    # 4: {1: 20, 3: 8, 5: 7, 7: 17},
    5: {2: 14, 4: 7, 7: 24},
    6: {3: 14, 7: 12},
    7: {4: 17, 5: 24, 6: 12}
}

# Create the networkx graph with updated weights
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

def dijkstra(graph, start):
    queue, visited, min_dist = [(0, start)], set(), {start: 0}
    prev = {start: None}
    while queue:
        (cost, node) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                new_cost = cost + weight
                if neighbor not in min_dist or new_cost < min_dist[neighbor]:
                    min_dist[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor))
                    prev[neighbor] = node
    return min_dist, prev

def get_path(prev, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = prev[end]
    path.reverse()
    return path



shortest_paths, prev = dijkstra(graph, 0)
print("Shortest paths:", shortest_paths)

from networkx.algorithms import tree

mst = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
edgelist = list(mst)
print(sorted(sorted(e) for e in edgelist))

