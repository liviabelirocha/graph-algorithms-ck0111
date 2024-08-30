import sys
from collections import defaultdict
import heapq

from utils.graph import Graph

def prim(connections, start=0):
    graph = Graph(connections)

    mst = defaultdict(lambda: {'color': 'white', 'key': sys.maxsize, 'parent': None})

    mst[start]['key'] = 0

    heap = [(0, start)]

    while len(heap) != 0:
        _, u = heapq.heappop(heap)
        mst[u]['color'] = 'black'

        for v, w in graph._graph[u]:
            if mst[v]['color'] == 'white' and w < mst[v]['key']:
                mst[v]['key'] = w
                mst[v]['parent'] = u
                heapq.heappush(heap, (w, v))

    weight = 0
    print("Edges in the constructed MST") 
    for i in mst: 
        weight += mst[i]['key'] 
        print(f"{i} - {mst[i]['parent']} = {mst[i]['key']}") 
    print("Minimum Spanning Tree", weight) 