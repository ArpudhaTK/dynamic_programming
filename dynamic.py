# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 06:10:16 2023

@author: arpud
"""

def dynamic_prog(graph, source):
    vertices = list(graph.keys())
    num_vertices = len(vertices)

    J = {vertex: float('inf') for vertex in vertices}
    J[source] = 0

    # Iterate for each vertex
    for i in range(num_vertices):
        # Iterate through all edges (i, j)
        for i_vertex in vertices:
            for j_vertex, cost in graph[i_vertex].items():
                # Update optimal cost based on the principle
                if J[j_vertex] > J[i_vertex] + cost:
                    J[j_vertex] = J[i_vertex] + cost

    return J

graph = {
    'A': {'B': 3, 'C': 5},
    'B': {'C': 1, 'D': 2},
    'C': {'D': 4},
    'D': {}
}

source_vertex = 'A'
optimal_costs = dynamic_prog(graph, source_vertex)


print("Optimal Costs:", optimal_costs)
