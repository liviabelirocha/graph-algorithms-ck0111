from utils.graph import Graph
from utils.union_find import UnionFind

def kruskal():
    connections = [(0, 1, 4), (0, 7, 8), 
                   (1, 2, 8), (1, 7, 11),
                   (2, 3, 7), (2, 8, 2), (2, 5, 4),
                   (3, 4, 9), (3, 5, 14),
                   (4, 5, 10),
                   (5, 6, 2),
                   (6, 7, 1), (6, 8, 6),
                   (7, 8, 7)]

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