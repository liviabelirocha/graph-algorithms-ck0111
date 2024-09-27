import sys
from collections import defaultdict

from utils.graph import Graph

def bellman_ford(connections, start):
    graph = Graph(connections, directed=True)

    dict = defaultdict(lambda: {'weight': sys.maxsize, 'parent': None})
    dict[start]['weight'] = 0

    for _ in range(graph.V() - 1):
        for u, v, w in graph._edges:
            vertix_weight = w + dict[u]['weight']
            if vertix_weight < dict[v]['weight']:
                dict[v]['weight'] = vertix_weight
                dict[v]['parent'] = u

    for u, v, w in graph._edges:
        if dict[u]['weight'] + w < dict[v]['weight']:
            raise ValueError("Graph contains a negative-weight cycle")

    print('VERTIX | PARENT | WEIGHT')
    for i in dict: 
        print(f"{i} | {dict[i]['parent']} | {dict[i]['weight']}") 