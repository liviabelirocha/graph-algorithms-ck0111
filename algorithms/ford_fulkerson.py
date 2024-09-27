import sys
from collections import defaultdict

from utils.network import Network

def bfs(graph, s, t, parent):
    colors = defaultdict(list)

    for i in range(graph.V()):
        colors[i] = 'white'
    
    queue = [s]
    colors[s] = 'gray'


    while len(queue) > 0:
        v = queue.pop(0)

        for u, _ in graph._graph[v]:
            if colors[u]== 'white' and graph.get_weight(v, u) > 0:
                colors[u]= 'gray'
                parent[u] = v
                queue.append(u)
                if u == t:
                    return True
        
        colors[v] = 'black'

    return False


def ford_fulkerson(connections, source, sink):
    network = Network(connections, directed=True)

    flow = 0

    parent = [None] * network.V()

    while bfs(network, source, sink, parent):
        path_flow = sys.maxsize
        s = sink

        while (s != source):
            path_flow = min(path_flow, network.get_weight(parent[s], s))
            s = parent[s]

        flow += path_flow

        v = sink
        while (v != source):
            u = parent[v]
            network.change_weight(u, v, network.get_weight(u, v) - path_flow)
            network.change_weight(v, u, network.get_weight(v, u) + path_flow)
            v = u

    print('Max flow:', flow)
    return flow
    