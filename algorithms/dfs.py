from utils.graph import Graph
from collections import defaultdict

def dfs(connections, start=0):
    graph = Graph(connections)

    info = defaultdict(lambda: {'color': 'white', 'depth': 0})
    for i in range(graph.V()):
        info[i] = {'color': 'white'}

    stack = []
    stack.append(start)
    info[start] = {'color': 'gray', 'depth': 0}
    
    while len(stack) > 0:
        v = stack.pop()
        for u, _ in graph._graph[v]:
            if info[u]['color'] == 'white':
                info[u] = {'color': 'gray', 'depth': info[v]['depth'] + 1}
                stack.append(u)
        info[v]['color'] = 'black'