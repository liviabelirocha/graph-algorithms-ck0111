import sys
from collections import defaultdict
import heapq

from utils.graph import Graph

def dijkstra(connections, start):
    graph = Graph(connections, directed=True)

    dict = defaultdict(lambda: {'weight': sys.maxsize, 'parent': None, 'color': 'white'})

    dict[start]['weight'] = 0

    heap = [(0, start)]

    while len(heap) != 0:
        _, u = heapq.heappop(heap)
        dict[u]['color'] = 'black'

        for v, w in graph._graph[u]:
            vertix_weight = w + dict[u]['weight']
            if vertix_weight < dict[v]['weight']:
                dict[v]['weight'] = vertix_weight
                dict[v]['parent'] = u
                if (dict[v]['color'] == 'white'):
                    heapq.heappush(heap, (vertix_weight, v))

    print('VERTIX | PARENT | WEIGHT')
    for i in dict: 
        print(f"{i} | {dict[i]['parent']} | {dict[i]['weight']}") 