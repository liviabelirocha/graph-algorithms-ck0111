from utils.graph import Graph
from collections import defaultdict

def bfs(connections, start=0):
    graph = Graph(connections)

    colors = defaultdict(list)
    for i in range(graph.V()):
        colors[i] = 'white'

    queue = [start]
    colors[start] = 'gray'

    while len(queue) > 0:
        v = queue.pop(0)

        for u, _ in graph._graph[v]:
            if colors[u] == 'white':
                colors[u] = 'gray'
                queue.append(u)
        
        colors[v] = 'black'