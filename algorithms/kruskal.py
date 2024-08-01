from utils.graph import Graph
from utils.union_find import UnionFind

def kruskal(connections):
    graph = Graph(connections)
    union_find = UnionFind(list(graph._graph.keys()))
    
    sorted_graph = graph.sort()

    mst = []
    # index for sorted edges
    i = 0
    # index used for mst[]
    e = 0

    while e < graph.V() - 1:
        u, v, w = sorted_graph[i]
        i += 1

        x = union_find.find(u)
        y = union_find.find(v)

        # if doesnt create a cycle
        if x != y:
            e += 1
            mst.append([u, v, w])
            union_find.union(x, y)


    weight = 0
    print("Edges in the constructed MST") 
    for u, v, w in mst: 
        weight += w 
        print(f"{u} - {v} = {w}") 
    print("Minimum Spanning Tree", weight) 