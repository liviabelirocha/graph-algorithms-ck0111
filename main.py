from algorithms.kruskal import kruskal
from algorithms.prim import prim
from algorithms.bfs import bfs
from algorithms.dfs import dfs

if __name__ == '__main__':
    connections = [(0, 1, 4), (0, 7, 8), 
                   (1, 2, 8), (1, 7, 11),
                   (2, 3, 7), (2, 8, 2), (2, 5, 4),
                   (3, 4, 9), (3, 5, 14),
                   (4, 5, 10),
                   (5, 6, 2),
                   (6, 7, 1), (6, 8, 6),
                   (7, 8, 7)]

    kruskal(connections)
    prim(connections)
    